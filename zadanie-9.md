# Zadanie 9: Weryfikacja prostego YAML

## 1. Prompt

> Sprawdź, czy poniższy plik YAML jest poprawny. Jeśli zawiera błędy, popraw je.

## 2. Oryginalny plik YAML

```yaml
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD=password
```

## 3. Wykryte błędy

ChatGPT wykrył dwa błędy:

1. Brak dwukropka po `ports` w usłudze `app`.
2. Niepoprawna składnia zmiennej środowiskowej `POSTGRES_PASSWORD=password`.

## 4. Poprawiony plik YAML

```yaml
services:
  web:
    image: nginx
    ports:
      - "80:80"

  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: password
```

