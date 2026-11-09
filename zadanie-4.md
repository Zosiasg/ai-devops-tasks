# Zadanie 4: Określanie roli w promptach

## 1. Prompt standardowy

**Prompt:**
> Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

**Odpowiedź ChatGPT:**

Aby ograniczyć zużycie pamięci przez kontener Docker, należy:

1. Sprawdzić zużycie pamięci poleceniem `docker stats`.
2. Zidentyfikować procesy zużywające najwięcej pamięci.
3. Zoptymalizować aplikację działającą w kontenerze.
4. Ustawić limit pamięci, np. `docker run --memory=512m`.
5. Sprawdzić, czy aplikacja nie ma wycieków pamięci.

## 2. Prompt z przypisaną rolą

**Prompt:**
> Jesteś doświadczonym DevOps Engineerem z 10-letnim doświadczeniem. Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

**Odpowiedź ChatGPT:**

Jako DevOps Engineer zastosowałbym następujące podejście diagnostyczne:

1. **Monitoring:** `docker stats` – sprawdzenie bieżącego zużycia RAM.
2. **Analiza procesów:** `docker top <container_id>` – identyfikacja procesów uruchomionych w kontenerze.
3. **Diagnostyka:** `docker inspect <container_id>` – weryfikacja konfiguracji limitów pamięci.
4. **Ograniczenie zasobów:** `docker run --memory=512m --memory-swap=512m`.
5. **Optymalizacja:** analiza wycieków pamięci, konfiguracji aplikacji i mechanizmów cache.
6. **Monitoring długoterminowy:** wdrożenie Prometheus i Grafana oraz alertów dotyczących wykorzystania pamięci.

Przed wprowadzeniem limitów należy ustalić rzeczywiste zapotrzebowanie aplikacji na pamięć, ponieważ zbyt niski limit może powodować błędy OOM (Out of Memory).

## 3. Porównanie odpowiedzi

| Kryterium | Prompt standardowy | Prompt z rolą |
|---|---|---|
| Szczegółowość | Podstawowa | Większa |
| Terminologia | Prosta | Specjalistyczna |
| Diagnostyka | Ogólne wskazówki | Konkretne polecenia |
| Monitoring | Podstawowy | Prometheus, Grafana |
| Analiza ryzyka | Ograniczona | Uwzględnia błędy OOM |

## 4. Wnioski

Przypisanie modelowi roli doświadczonego DevOps Engineera pozwoliło uzyskać bardziej techniczną i szczegółową odpowiedź, zawierającą konkretne nar