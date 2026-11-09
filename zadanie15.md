# Zadanie 15: Refaktoryzacja prostej funkcji

## 1. Prompt

> Zrefaktoryzuj funkcję getEnvironmentConfig(env), aby była bardziej czytelna i łatwiejsza w utrzymaniu.

## 2. Odpowiedź ChatGPT

Zastąpiono rozbudowaną strukturę `if-else` obiektem `configs`, przechowującym konfiguracje środowisk.

Zrefaktoryzowana funkcja:

```javascript
function getEnvironmentConfig(env) {
  return { ...(
    Object.hasOwn(configs, env)
      ? configs[env]
      : configs.development
  ) };
}
```

Pełny kod znajduje się w pliku `config-refactored.js`.

## 3. Wprowadzone zmiany

1. Usunięto powtarzające się instrukcje `if-else`.
2. Przeniesiono konfiguracje do jednego obiektu.
3. Uproszczono wybór konfiguracji na podstawie nazwy środowiska.
4. Zachowano domyślną konfigurację `development`.
5. Dodano kopiowanie obiektu, aby ograniczyć ryzyko modyfikacji zapisanej konfiguracji.

## 4. Korzyści

- **Czytelność** – krótszy i bardziej przejrzysty kod.
- **Łatwość utrzymania** – konfiguracje znajdują się w jednym miejscu.
- **Rozszerzalność** – dodanie nowego środowiska nie wymaga modyfikowania logiki funkcji.
- **Mniejsza redundancja** – ograniczono powtarzanie kodu.

## 5. Wnioski

Refaktoryzacja uprościła strukturę funkcji bez zmiany jej zamierzonego działania.

