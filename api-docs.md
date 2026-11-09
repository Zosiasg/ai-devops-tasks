# Dokumentacja API – Lista użytkowników

## 1. Opis endpointu

**Endpoint:** `GET /api/users`

Endpoint zwraca listę użytkowników z możliwością stronicowania wyników oraz filtrowania według roli.

## 2. Parametry zapytania

| Parametr | Typ | Domyślna wartość | Opis |
|---|---|---|---|
| `page` | integer | 1 | Numer strony wyników. |
| `limit` | integer | 10 | Liczba użytkowników na stronie (maks. 100). |
| `role` | string | Brak | Opcjonalny filtr według roli użytkownika. |

## 3. Przykładowe żądanie

```http
GET /api/users?page=2&limit=5&role=admin HTTP/1.1
Host: api.example.com
Accept: application/json
```

## 4. Przykładowa odpowiedź

**Status:** `200 OK`

```json
{
  "page": 2,
  "limit": 5,
  "total": 12,
  "users": [
    {
      "id": 6,
      "name": "Anna Kowalska",
      "email": "anna@example.com",
      "role": "admin"
    },
    {
      "id": 7,
      "name": "Jan Nowak",
      "email": "jan@example.com",
      "role": "admin"
    }
  ]
}
```

## 5. Uwagi

- Parametry `page` i `limit` umożliwiają stronicowanie wyników.
- Parametr `role` pozwala ograniczyć wyniki do wybranej roli.
- Maksymalna wartość parametru `limit` wynosi 100.
- Przykładowa odpowiedź ma charakter ilustracyjny. Struktura JSON i pola użytkowników wymagają potwierdzenia w rzeczywistej implementacji API.