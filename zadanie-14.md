# Zadanie 14: Wyjaśnienie fragmentu logów

## 1. Prompt

> Co się dzieje w tych logach? Jakie problemy można zidentyfikować?

## 2. Logi Docker

```text
May 19 10:15:32 server dockerd[1234]: time="2025-05-19T10:15:32.123456789Z" level=info msg="Container 78a2b3c4 health status changed from starting to healthy"
May 19 10:16:45 server dockerd[1234]: time="2025-05-19T10:16:45.987654321Z" level=info msg="Container 78a2b3c4 failed to connect to 172.17.0.3:5432: connection refused"
May 19 10:16:47 server dockerd[1234]: time="2025-05-19T10:16:47.246813579Z" level=warning msg="Container 78a2b3c4 health status changed from healthy to unhealthy"
```

## 3. Analiza ChatGPT

| Czas | Zdarzenie | Znaczenie |
|---|---|---|
| 10:15:32 | `starting → healthy` | Kontener przeszedł pomyślnie kontrolę stanu. |
| 10:16:45 | `connection refused` | Nie udało się połączyć z adresem `172.17.0.3:5432`. |
| 10:16:47 | `healthy → unhealthy` | Kontrola stanu wykazała problem z kontenerem. |

**Zidentyfikowany problem:** Kontener utracił możliwość nawiązania połączenia z usługą na porcie 5432, standardowo wykorzystywanym przez PostgreSQL. Może to wskazywać na niedziałającą bazę danych, błędną konfigurację połączenia lub usługę, która nie nasłuchuje na wskazanym adresie.

### Możliwe rozwiązania

1. Sprawdzenie stanu kontenerów: `docker ps -a`.
2. Analiza logów bazy danych: `docker logs <db_container>`.
3. Weryfikacja konfiguracji adresu i portu bazy danych.
4. Sprawdzenie wyników kontroli stanu: `docker inspect <container_id>`.
5. Weryfikacja gotowości bazy danych do przyjmowania połączeń.

