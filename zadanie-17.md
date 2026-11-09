# Zadanie 17: Generowanie kodu na podstawie opisu

## 1. Prompt

> Napisz funkcję JavaScript, która przyjmuje tablicę zadań (id, title, status), wybiera zadania o statusie "completed", sortuje je rosnąco według id i zwraca tablicę ich tytułów.

## 2. Odpowiedź ChatGPT

```javascript
function getCompletedTaskTitles(tasks) {
    return tasks
        .filter(task => task.status === "completed")
        .sort((a, b) => a.id - b.id)
        .map(task => task.title);
}
```

## 3. Przykład użycia

```javascript
const tasks = [
    { id: 3, title: "Wdrożenie", status: "completed" },
    { id: 1, title: "Konfiguracja", status: "completed" },
    { id: 2, title: "Testowanie", status: "pending" }
];

console.log(getCompletedTaskTitles(tasks));
```

**Wynik:**

```text
["Konfiguracja", "Wdrożenie"]
```

## 4. Wyjaśnienie

- `filter()` – wybiera ukończone zadania.
- `sort()` – sortuje je rosnąco według identyfikatora.
- `map()` – tworzy tablicę zawierającą wyłącznie tytuły.
