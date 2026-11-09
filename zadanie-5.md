# Zadanie 5: Wizualizacja ASCII Art

## 1. Prompt podstawowy

**Prompt:**
> Stwórz prosty diagram ASCII Art przedstawiający połączenie klienta, serwera aplikacji i bazy danych.

**Odpowiedź ChatGPT:**

```text
+------------+       +-------------------+       +--------------+
|   Klient   |-------| Serwer aplikacji  |-------| Baza danych  |
+------------+       +-------------------+       +--------------+
```

## 2. Prompt ulepszony

**Prompt:**
> Dodaj do diagramu opisy elementów i kierunki przepływu danych.

**Odpowiedź ChatGPT:**

```text
+----------------+       HTTP Request       +--------------------+
|                | -----------------------> |                    |
|     KLIENT     |                          |  SERWER APLIKACJI  |
| (Przeglądarka) | <----------------------- |     (Backend)      |
|                |       HTTP Response      |                    |
+----------------+                          +--------------------+
                                                      |
                                                      | SQL Query
                                                      v
                                            +--------------------+
                                            |                    |
                                            |    BAZA DANYCH     |
                                            |    (PostgreSQL)    |
                                            |                    |
                                            +--------------------+
                                                      |
                                                      | SQL Result
                                                      |
                                                      v
                                             Serwer aplikacji
```

## 3. Wnioski

Pierwszy diagram przedstawia jedynie podstawowe połączenia między elementami systemu.

Drugi diagram zawiera dodatkowo opisy komponentów oraz kierunki komunikacji HTTP i SQL, dzięki czemu lepiej przedstawia działanie architektury.

**Wniosek:** Doprecyzowanie promptu pozwala uzyskać bardziej czytelną i użyteczną wizualizację.