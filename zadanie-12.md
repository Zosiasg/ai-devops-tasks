# Zadanie 12: Optymalizacja prostego skryptu

## 1. Prompt

> Czy ten kod można zoptymalizować? Jeśli tak, zaproponuj bardziej wydajną wersję.

## 2. Oryginalny kod

```python
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates
```

## 3. Zoptymalizowany kod

```python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()

    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)
```

## 4. Wyjaśnienie optymalizacji

- **Usunięcie zagnieżdżonych pętli** – lista jest przeglądana tylko raz.
- **Zastosowanie zbiorów (`set`)** – umożliwia szybkie sprawdzanie, czy element już wystąpił.
- **Eliminacja powtórzeń** – zbiór `duplicates` automatycznie przechowuje unikalne wartości.
- **Większa wydajność** – średnia złożoność czasowa zmniejsza się z O(n²) do O(n).

## 5. Wnioski

Zoptymalizowana funkcja jest krótsza i bardziej wydajna, szczególnie dla dużych zbiorów danych.

**Uwaga:** Nowa wersja wymaga elementów hashowalnych (np. liczb lub napisów) i nie gwarantuje zachowania kolejności wyników.

**Wniosek:** Wykorzystanie odpowiednich struktur danych pozwala znacząco zwiększyć wydajność kodu Python.