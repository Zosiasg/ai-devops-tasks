# Zadanie 21: Transformacja danych

## 1. Prompt

> Przekształć dane JSON zawierające listę użytkowników do formatu CSV z kolumnami: id, name, email, roles.

## 2. Odpowiedź ChatGPT

Dane zostały przekształcone do formatu CSV:

```csv
id,name,email,roles
1,Jan Kowalski,jan@example.com,admin;user
2,Anna Nowak,anna@example.com,user
```

## 3. Opis konwersji

1. Odczytano tablicę `users` z pliku JSON.
2. Każdy obiekt użytkownika przekształcono w jeden wiersz CSV.
3. Pola `id`, `name` i `email` zapisano w osobnych kolumnach.
4. Tablicę `roles` połączono w pojedynczy tekst, oddzielając role średnikiem.

## 4. Potencjalne wyzwania

- **Zagnieżdżone dane** – CSV nie obsługuje bezpośrednio tablic i obiektów.
- **Wiele ról** – konieczne jest ustalenie sposobu zapisu kilku wartości w jednej komórce.
- **Znaki specjalne** – wartości zawierające przecinki, cudzysłowy lub znaki nowej linii wymagają odpowiedniego formatowania.
- **Typy danych** – CSV przechowuje dane tekstowe, dlatego podczas ponownego odczytu może być konieczne odtworzenie ich typów.