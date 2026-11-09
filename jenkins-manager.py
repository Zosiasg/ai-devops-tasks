import os
import sys
import argparse
import requests
from requests.auth import HTTPBasicAuth


JENKINS_URL = os.getenv("JENKINS_URL", "http://localhost:8080")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")


def get_session():
    """Tworzy sesję z autoryzacją Jenkins API."""
    if not JENKINS_USER or not JENKINS_TOKEN:
        raise ValueError("Brak JENKINS_USER lub JENKINS_TOKEN")

    session = requests.Session()
    session.auth = HTTPBasicAuth(JENKINS_USER, JENKINS_TOKEN)
    session.headers.update({"Accept": "application/json"})
    return session


def list_jobs(session):
    """Wyświetla listę zadań Jenkins."""
    response = session.get(
        f"{JENKINS_URL}/api/json",
        params={"tree": "jobs[name,url,color]"},
        timeout=10
    )
    response.raise_for_status()

    for job in response.json().get("jobs", []):
        print(f"{job['name']} - {job.get('color', 'unknown')}")


def build_status(session, job_name):
    """Wyświetla status ostatniego buildu."""
    from urllib.parse import quote

    job = quote(job_name, safe="")

    response = session.get(
        f"{JENKINS_URL}/job/{job}/lastBuild/api/json",
        timeout=10
    )
    response.raise_for_status()

    build = response.json()
    print(f"Build: #{build['number']}")
    print(f"Status: {build.get('result') or 'IN_PROGRESS'}")


def trigger_build(session, job_name):
    """Uruchamia wybrane zadanie Jenkins."""
    from urllib.parse import quote

    job = quote(job_name, safe="")

    response = session.post(
        f"{JENKINS_URL}/job/{job}/build",
        timeout=10
    )
    response.raise_for_status()

    print(f"Zlecono uruchomienie zadania: {job_name}")


def main():
    parser = argparse.ArgumentParser(
        description="Prosty menedżer Jenkins API"
    )

    parser.add_argument(
        "action",
        choices=["list", "status", "build"]
    )
    parser.add_argument("--job", help="Nazwa zadania Jenkins")

    args = parser.parse_args()

    if args.action in ["status", "build"] and not args.job:
        parser.error("Podaj nazwę zadania przez --job")

    try:
        with get_session() as session:
            if args.action == "list":
                list_jobs(session)
            elif args.action == "status":
                build_status(session, args.job)
            elif args.action == "build":
                trigger_build(session, args.job)

    except requests.exceptions.RequestException as error:
        print(f"Błąd komunikacji z Jenkins API: {error}")
        sys.exit(1)
    except ValueError as error:
        print(f"Błąd konfiguracji: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()