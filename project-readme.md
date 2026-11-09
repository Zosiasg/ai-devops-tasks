# Simple Task API

## 1. Opis projektu

Simple Task API to aplikacja REST API do zarządzania zadaniami, wykorzystująca **Node.js, Express i MongoDB**.

Główne funkcjonalności:
- Tworzenie, odczytywanie, aktualizowanie i usuwanie zadań (CRUD).
- Filtrowanie zadań według statusu i priorytetu.
- Podstawowa autoryzacja użytkowników.

## 2. Instalacja

**Wymagania:** Node.js, npm oraz MongoDB.

Sklonowanie repozytorium:

```bash
git clone <URL_REPOZYTORIUM>
cd <KATALOG_PROJEKTU>
```

Instalacja zależności:

```bash
npm install
```

Przykładowa konfiguracja pliku `.env`:

```env
PORT=3000
MONGODB_URI=mongodb://localhost:27017/tasks
```

Uruchomienie aplikacji:

```bash
npm start
```

**Uwaga:** Instrukcja zakłada istnienie implementacji API i skryptu `start` w pliku `package.json`.

## 3. Użycie

Przykład pobrania listy zadań:

```http
GET http://localhost:3000/api/tasks
```

Przykład utworzenia zadania:

```http
POST http://localhost:3000/api/tasks
Content-Type: application/json

{
  "title": "Przygotowanie dokumentacji",
  "status": "pending",
  "priority": "high"
}
```

## 4. Endpointy API

| Metoda | Endpoint | Opis |
|---|---|---|
| GET | `/api/tasks` | Pobranie listy zadań |
| GET | `/api/tasks/:id` | Pobranie zadania |
| POST | `/api/tasks` | Utworzenie zadania |
| PUT | `/api/tasks/:id` | Aktualizacja zadania |
| DELETE | `/api/tasks/:id` | Usunięcie zadania |
| GET | `/api/tasks?status=completed` | Filtrowanie według statusu |
| GET | `/api/tasks?priority=high` | Filtrowanie według priorytetu |

## 5. Autoryzacja

Projekt przewiduje podstawową autoryzację użytkowników. Dokładny mechanizm uwierzytelniania i wymagane uprawnienia należy określić podczas implementacji.

**Uwaga:** Dokumentacja przedstawia przykładową specyfikację projektu. Endpointy i polecenia uruchomieniowe wymagają weryfikacji po przygotowaniu działającej aplikacji.