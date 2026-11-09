# Zadanie 23: Analiza złożoności algorytmu

## 1. Prompt

> Jaka jest złożoność czasowa i pamięciowa algorytmu findPairs? Czy można go zoptymalizować?

## 2. Odpowiedź ChatGPT

**Oryginalny algorytm:**

- Złożoność czasowa: **O(n²)** – dwie zagnieżdżone pętle sprawdzają wszystkie możliwe pary elementów.
- Złożoność pamięciowa: **O(1)** pamięci pomocniczej, nie licząc tablicy wynikowej.
- Łączne zużycie pamięci: **O(k)**, gdzie k oznacza liczbę znalezionych par.

## 3. Optymalizacja

Zastosowano strukturę `Map` przechowującą wartości i odpowiadające im indeksy. Pozwala to szybciej odnajdywać elementy, które razem tworzą wymaganą sumę.

Zoptymalizowana funkcja znajduje się w pliku `find-pairs-optimized.js`.

**Złożoność zoptymalizowanego algorytmu:**

- Czasowa: **O(n + k)** średnio.
- Pamięciowa: **O(n)** pamięci pomocniczej.
- Łączne zużycie pamięci: **O(n + k)**.

W najgorszym przypadku liczba znalezionych par może wynosić O(n²), dlatego również zoptymalizowany algorytm może wymagać czasu O(n²).

## 4. Porównanie

| Kryterium | Oryginalny | Zoptymalizowany |
|---|---|---|
| Złożoność czasowa | O(n²) | O(n + k) średnio |
| Pamięć pomocnicza | O(1) | O(n) |
| Struktura danych | Tablica | Map i tablica |
| Sprawdzanie par | Wszystkie kombinacje | Wyszukiwanie dopasowań |

## 5. Przykład

**Dane wejściowe:**

```javascript
findPairs([1, 2, 3, 4, 5], 6);
```

**Wynik:**

```javascript
[[1, 5], [2, 4]]
```

Obie funkcje zwracają taki sam wynik.