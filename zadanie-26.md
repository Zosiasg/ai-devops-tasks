# Zadanie 26: Analiza i poprawa istniejącego Jenkinsfile

## 1. Prompt

> Ten Jenkinsfile zawiera kilka błędów. Znajdź je i zaproponuj poprawioną wersję. Wyjaśnij, jakie były problemy i jak je naprawiłeś.

## 2. Odpowiedź ChatGPT

Zidentyfikowano następujące problemy:

| Problem | Poprawka |
|---|---|
| Literówka `stesp` | Zmieniono na `steps`. |
| Niepoprawne `npm build` | Zmieniono na `npm run build`. |
| Niespójna nazwa obrazu Docker | Ujednolicono nazwę i tag obrazu. |
| Brak logowania do Docker Hub | Dodano autoryzację przez Jenkins Credentials. |
| Brak jawnego tagu przy budowaniu | Dodano tag `latest`. |

## 3. Dodatkowe uwagi

Poprawiony Jenkinsfile wykorzystuje:

- Etap budowania aplikacji Node.js.
- Automatyczne testy.
- Budowanie obrazu Docker.
- Publikowanie obrazu do Docker Hub.
- Warunek ograniczający publikację do gałęzi `master`.

Do uruchomienia wymagane są odpowiednio skonfigurowane narzędzia Jenkins, Node.js i Docker oraz poświadczenia Docker Hub.

## 4. Podsumowanie

ChatGPT wykrył błędy składniowe i konfiguracyjne oraz zaproponował poprawioną wersję pipeline'u.

Poprawiona konfiguracja jest bardziej spójna, ale wymaga dostosowania do rzeczywistego środowiska Jenkins.