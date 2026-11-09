# Zadanie 29: Generowanie szablonu konfiguracji Jenkins

## 1. Prompt

> Wygeneruj szablon Jenkins Configuration as Code (JCasC) w formacie YAML, konfigurujący podstawowe ustawienia Jenkins, timeout, narzędzia Maven, Node.js i Docker, wymagane wtyczki oraz przykładowe zadanie Pipeline.

## 2. Odpowiedź ChatGPT

Wygenerowano plik `jenkins-casc.yaml`, zawierający:

- Podstawowe ustawienia Jenkins.
- Liczbę wykonawców (`numExecutors: 2`).
- Konfigurację narzędzi Maven, Node.js i Docker.
- Przykładowe zadanie Pipeline.
- Limit czasu wykonania Pipeline wynoszący 30 minut.

## 3. Prompt uzupełniający

> Wyjaśnij, jak używać tego pliku konfiguracyjnego z Jenkinsem. Podaj kroki instalacji i uruchomienia Jenkinsa z tym szablonem.

## 4. Instrukcja użycia

1. Zainstaluj Jenkins.
2. Zainstaluj wymagane wtyczki: Configuration as Code, Pipeline, Job DSL, NodeJS i Docker Commons.
3. Dostosuj ścieżki narzędzi w pliku YAML do środowiska Jenkins.
4. Umieść plik `jenkins-casc.yaml` w katalogu dostępnym dla procesu Jenkins.
5. Ustaw zmienną środowiskową:

```bash
export CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins-casc.yaml
```

6. Uruchom lub zrestartuj Jenkins z ustawioną zmienną środowiskową.
7. Otwórz **Manage Jenkins → Configuration as Code**.
8. Zweryfikuj załadowaną konfigurację oraz utworzone zadanie `example-pipeline`.

## 5. Uwagi

JCasC umożliwia automatyzację konfiguracji Jenkins i przechowywanie ustawień w repozytorium Git.

Wtyczki należy instalować oddzielnie, ponieważ JCasC nie zarządza ich instalacją.

Przykładowy Pipeline wykorzystuje polecenia `echo`, dlatego nie wymaga rzeczywistego budowania ani wdrażania aplikacji.

Szablon ma charakter edukacyjny. Nie został przetestowany na działającej instancji Jenkins.