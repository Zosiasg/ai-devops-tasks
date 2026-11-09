function findPairs(arr, targetSum) {
    const pairs = [];
    const indices = new Map();

    // Zapisanie indeksów poszczególnych wartości
    arr.forEach((value, index) => {
        if (!indices.has(value)) {
            indices.set(value, []);
        }
        indices.get(value).push(index);
    });

    const positions = new Map();

    for (let i = 0; i < arr.length; i++) {
        const value = arr[i];
        const complement = targetSum - value;

        // Pomijamy bieżący indeks
        positions.set(value, (positions.get(value) || 0) + 1);

        const matching = indices.get(complement) || [];
        const start = positions.get(complement) || 0;

        for (let p = start; p < matching.length; p++) {
            pairs.push([value, arr[matching[p]]]);
        }
    }

    return pairs;
}

// Przykład użycia
console.log(findPairs([1, 2, 3, 4, 5], 6));