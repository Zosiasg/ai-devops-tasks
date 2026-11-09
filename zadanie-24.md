# Zadanie 24: Interpretacja danych wydajnościowych

## 1. Prompt

> Zinterpretuj poniższe metryki serwera API z ostatnich 24 godzin. Czy widzisz potencjalne problemy? Co sugerujesz, aby poprawić wydajność?

## 2. Dane wydajnościowe

| Metryka | Wartość |
|---|---|
| Średni czas odpowiedzi | 230 ms |
| 95. percentyl (P95) | 450 ms |
| 99. percentyl (P99) | 1200 ms |
| Liczba zapytań | 15 000 |
| Liczba błędów HTTP 5xx | 120 |
| CPU – średnio / maksimum | 45% / 80% |
| RAM – średnio / maksimum | 2,1 GB / 3,5 GB |
| Dostępna pamięć RAM | 4 GB |

## 3. Analiza ChatGPT

**Czas odpowiedzi:** Średnia wynosi 230 ms, ale P99 osiąga 1200 ms. Oznacza to, że około 1% najwolniejszych zapytań trwa co najmniej 1,2 sekundy.

**Błędy HTTP 5xx:** Odnotowano 120 błędów na 15 000 zapytań, co oznacza wskaźnik błędów **0,8%**. Wymaga to analizy przyczyn.

**CPU:** Średnie wykorzystanie 45% nie wskazuje na stałe przeciążenie procesora. Maksimum 80% może oznaczać okresowe zwiększenie obciążenia.

**RAM:** Maksymalne wykorzystanie wynosi 3,5 GB z dostępnych 4 GB, czyli **87,5%**. Niewielki zapas pamięci może powodować problemy przy wzroście obciążenia.

## 4. Rekomendacje

1. **Analiza logów** – identyfikacja przyczyn błędów HTTP 5xx.
2. **Monitoring wydajności** – wykorzystanie Prometheus i Grafana.
3. **Optymalizacja API** – analiza najwolniejszych endpointów i zapytań do bazy danych.
4. **Kontrola pamięci** – sprawdzenie wycieków pamięci i konfiguracji aplikacji.
5. **Testy obciążeniowe** – wykorzystanie narzędzi k6 lub JMeter.

## 5. Podsumowanie

Najważniejsze potencjalne problemy to wysoki czas odpowiedzi P99, błędy HTTP 5xx oraz ograniczony zapas pamięci RAM.

Priorytetem powinna być analiza błędów i najwolniejszych zapytań, a następnie optymalizacja wykorzystania zasobów.

Ocena wymaga porównania metryk z przyjętymi wymaganiami wydajnościowymi (SLO).