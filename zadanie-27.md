# Zadanie 27: Generowanie diagramu Mermaid dla potoku Jenkins

## 1. Prompt

> Stwórz diagram Mermaid przedstawiający typowy pipeline CI/CD w Jenkinsie dla aplikacji webowej. Uwzględnij etapy: checkout kodu, budowanie, testowanie, analiza statyczna kodu, bezpieczeństwo, budowanie obrazu Docker, testy integracyjne, wdrożenie na środowisko staging i produkcja.

## 2. Odpowiedź ChatGPT

Wygenerowano diagram Mermaid przedstawiający pipeline CI/CD. Kod diagramu zapisano w pliku `jenkins-pipeline.md`.

## 3. Opis etapów

| Etap | Opis |
|---|---|
| Checkout | Pobranie kodu z repozytorium Git. |
| Build | Zbudowanie aplikacji. |
| Testy jednostkowe | Weryfikacja poprawności działania kodu. |
| Analiza statyczna | Sprawdzenie jakości kodu. |
| Bezpieczeństwo | Analiza podatności i zagrożeń. |
| Docker Build | Utworzenie obrazu kontenera. |
| Testy integracyjne | Sprawdzenie współpracy komponentów. |
| Deploy Staging | Wdrożenie na środowisko testowe. |
| Weryfikacja staging | Sprawdzenie poprawności działania aplikacji. |
| Deploy Production | Wdrożenie na środowisko produkcyjne. |
| Monitoring | Kontrola działania aplikacji po wdrożeniu. |

## 4. Zależności między etapami

Pipeline wykonuje kolejne etapy po pomyślnym zakończeniu poprzednich.

Testowanie, analiza statyczna i kontrola bezpieczeństwa poprzedzają budowanie obrazu Docker.

Po testach integracyjnych aplikacja jest wdrażana na środowisko staging. Wdrożenie produkcyjne następuje wyłącznie po pozytywnej weryfikacji staging.

W przypadku niepowodzenia weryfikacji pipeline zostaje zatrzymany, co ogranicza ryzyko wdrożenia wadliwej aplikacji.