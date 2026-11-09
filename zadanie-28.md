# Zadanie 28: Skrypt do zarządzania zadaniami Jenkins

## 1. Prompt

> Napisz skrypt w Pythonie wykorzystujący Jenkins API do listowania zadań, sprawdzania statusu ostatnich buildów i uruchamiania wybranego zadania. Uwzględnij autoryzację i obsługę błędów.

## 2. Odpowiedź ChatGPT

Wygenerowano skrypt `jenkins-manager.py` wykorzystujący Jenkins REST API.

**Funkcjonalności:**

1. `list_jobs()` – pobiera listę zadań Jenkins.
2. `build_status()` – sprawdza status ostatniego buildu.
3. `trigger_build()` – uruchamia wybrane zadanie.
4. `get_session()` – konfiguruje połączenie i autoryzację.

## 3. Wykorzystane biblioteki

| Biblioteka | Zastosowanie |
|---|---|
| `requests` | Komunikacja HTTP z Jenkins REST API. |
| `argparse` | Obsługa parametrów wiersza poleceń. |
| `os` | Odczyt zmiennych środowiskowych. |
| `sys` | Obsługa zakończenia programu. |

## 4. Instalacja

```bash
pip install requests
```

Konfiguracja w PowerShell:

```powershell
$env:JENKINS_URL = "http://localhost:8080"
$env:JENKINS_USER = "admin"
$env:JENKINS_TOKEN = "<API_TOKEN>"
```

Token API należy wygenerować w ustawieniach użytkownika Jenkins. Nie należy zapisywać go w repozytorium Git.

## 5. Przykłady użycia

**Lista zadań:**

```bash
python jenkins-manager.py list
```

**Status ostatniego buildu:**

```bash
python jenkins-manager.py status --job "MyJob"
```

**Uruchomienie zadania:**

```bash
python jenkins-manager.py build --job "MyJob"
```

## 6. Obsługa błędów

Skrypt obsługuje błędy komunikacji HTTP, nieprawidłową autoryzację i brak wymaganych zmiennych środowiskowych.

Do komunikacji wykorzystuje autoryzację HTTP Basic Auth z nazwą użytkownika i tokenem Jenkins API.