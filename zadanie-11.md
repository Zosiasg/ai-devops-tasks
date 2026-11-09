# Zadanie 11: Generowanie prostego testu jednostkowego

## 1. Prompt

> Napisz prosty test jednostkowy dla funkcji sum(a, b) używając Jest. Wyjaśnij, czym jest Jest, jak go zainstalować i uruchomić test. Podaj strukturę plików projektu.

## 2. Odpowiedź ChatGPT

**Jest** to framework do automatycznego testowania aplikacji JavaScript.

Plik `sum.js`:

```javascript
function sum(a, b) {
    return a + b;
}

module.exports = sum;
```

Plik `sum.test.js`:

```javascript
const sum = require('./sum');

test('dodaje 2 + 3 i zwraca 5', () => {
    expect(sum(2, 3)).toBe(5);
});

test('dodaje liczby ujemne', () => {
    expect(sum(-2, -3)).toBe(-5);
});

test('dodaje zero', () => {
    expect(sum(5, 0)).toBe(5);
});
```

## 3. Instalacja i uruchomienie

Instalacja Jest:

```bash
npm init -y
npm install --save-dev jest
```

Konfiguracja `package.json`:

```json
"scripts": {
    "test": "jest"
}
```

Uruchomienie testów:

```bash
npm test
```

Oczekiwany wynik: `3 passed, 3 total`.

## 4. Struktura projektu

```text
ai-devops-tasks/
├── sum.js
├── sum.test.js
├── package.json
├── package-lock.json
└── zadanie-11.md
```

## 5. Wnioski

ChatGPT wygenerował funkcję JavaScript oraz trzy testy jednostkowe sprawdzające dodawanie liczb dodatnich, ujemnych i zera.

