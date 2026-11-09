# Zadanie 10: Generowanie prostego pliku .gitignore

## 1. Prompt

> Stwórz plik .gitignore dla projektu Node.js, który używa Docker i przechowuje dane w lokalnej bazie MongoDB.

**Odpowiedź ChatGPT:** Wygenerowano plik `.gitignore` zawierający reguły ignorowania plików Node.js, Docker, MongoDB oraz IntelliJ IDEA.

## 2. Prompt uzupełniający

> Dlaczego ważne jest ignorowanie tych plików?

## 3. Odpowiedź ChatGPT

Ignorowanie wybranych plików jest ważne z kilku powodów:

1. **Bezpieczeństwo** – pliki `.env` mogą zawierać hasła i klucze API, które nie powinny trafiać do repozytorium.
2. **Mniejszy rozmiar repozytorium** – katalog `node_modules/` zawiera zależności, które można ponownie zainstalować.
3. **Ochrona danych** – katalogi MongoDB mogą zawierać lokalne dane i kopie baz danych.
4. **Porządek w projekcie** – logi i pliki tymczasowe nie zaśmiecają historii Git.
5. **Niezależność środowisk** – ignorowanie lokalnych ustawień IntelliJ i Docker ogranicza konflikty między programistami.

## 4. Wnioski

Plik `.gitignore` pomaga utrzymać porządek w repozytorium, zmniejsza jego rozmiar i ogranicza ryzyko przypadkowego ujawnienia danych poufnych.

**Wniosek:** Odpowiednia konfiguracja `.gitignore` jest istotnym elementem zarządzania projektem i bezpieczeństwa pracy z Git.