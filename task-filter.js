function getCompletedTaskTitles(tasks) {
    return tasks
        .filter(task => task.status === "completed")
        .sort((a, b) => a.id - b.id)
        .map(task => task.title);
}

// Przykład użycia
const tasks = [
    { id: 3, title: "Wdrożenie aplikacji", status: "completed" },
    { id: 1, title: "Konfiguracja środowiska", status: "completed" },
    { id: 2, title: "Testowanie aplikacji", status: "pending" },
    { id: 4, title: "Dokumentacja", status: "completed" }
];

console.log(getCompletedTaskTitles(tasks));