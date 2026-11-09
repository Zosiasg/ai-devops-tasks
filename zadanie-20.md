# Zadanie 20: Generowanie wyrażeń regularnych

## 1. Prompt

> Potrzebuję wyrażenia regularnego, które waliduje format adresu IPv4 (np. 192.168.1.1).

## 2. Odpowiedź ChatGPT

Wygenerowane wyrażenie regularne:

```regex
^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$
```

## 3. Prompt uzupełniający

> Wyjaśnij, jak działa to wyrażenie regularne i przetestuj je na kilku przykładach (poprawnych i niepoprawnych).

## 4. Wyjaśnienie

- `^` – początek tekstu.
- `25[0-5]` – liczby od 250 do 255.
- `2[0-4]\d` – liczby od 200 do 249.
- `1\d{2}` – liczby od 100 do 199.
- `[1-9]?\d` – liczby od 0 do 99.
- `\.` – kropka oddzielająca oktety.
- `{3}` – trzy kolejne oktety poprzedzone kropką.
- `$` – koniec tekstu.

Wyrażenie sprawdza, czy adres zawiera cztery liczby z zakresu 0–255, oddzielone kropkami. Nie dopuszcza zer wiodących w oktetach wielocyfrowych.

## 5. Przykłady testów

| Adres IPv4 | Oczekiwany wynik |
|---|---|
| `192.168.1.1` | Poprawny |
| `127.0.0.1` | Poprawny |
| `255.255.255.255` | Poprawny |
| `0.0.0.0` | Poprawny |
| `256.100.50.25` | Niepoprawny |
| `192.168.1` | Niepoprawny |
| `192.168.01.1` | Niepoprawny |
| `abc.def.ghi.jkl` | Niepoprawny |

Implementacja walidatora znajduje się w pliku `ipv4-validator.js`.