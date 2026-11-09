# Zadanie 13: Generowanie komentarzy dokumentacyjnych

## 1. Prompt

> Dodaj do funkcji fetchUserData(userId) komentarze dokumentacyjne w formacie JSDoc.

## 2. Odpowiedź ChatGPT

Wygenerowano dokumentację JSDoc dla funkcji pobierającej dane użytkownika z API.

Dodane komentarze:

```javascript
/**
 * Pobiera dane użytkownika z zewnętrznego API.
 *
 * @param {string|number} userId - Identyfikator użytkownika.
 * @returns {Promise<{name: string, email: string, lastLogin: Date}|null>}
 * Obietnica zwracająca dane użytkownika lub null w przypadku błędu.
 */
```

## 3. Czym jest JSDoc?

**JSDoc** to standard dokumentowania kodu JavaScript za pomocą specjalnych komentarzy.

Najważniejsze elementy:
- `/** ... */` – blok komentarza dokumentacyjnego.
- `@param` – opis parametrów funkcji.
- `@returns` – opis zwracanej wartości i jej typu.
- `Promise` – informacja, że funkcja zwraca wynik operacji asynchronicznej.

