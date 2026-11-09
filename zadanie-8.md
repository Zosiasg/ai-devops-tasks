# Zadanie 8: Analiza krótkiego błędu

## 1. Komunikat błędu

```text
ERROR: for app Cannot start service app:
driver failed programming external connectivity on endpoint app (172.18.0.2):
Error starting userland proxy:
listen tcp4 0.0.0.0:3000: bind: address already in use
```

## 2. Prompt

**Prompt:**
> Co oznacza ten błąd i jak mogę go rozwiązać?

## 3. Odpowiedź ChatGPT

Błąd oznacza, że **port 3000 na komputerze hosta jest już zajęty** przez inny proces lub kontener. Docker nie może uruchomić kontenera `app` z wymaganym mapowaniem portu.

### Możliwe rozwiązania

**1. Sprawdzenie zajętości portu:**

```bash
docker ps
```

W systemie Windows:

```powershell
netstat -ano | findstr :3000
```

**2. Zatrzymanie kontenera zajmującego port:**

```bash
docker stop <container_id>
```

**3. Zmiana portu w pliku `docker-compose.yml`:**

```yaml
ports:
  - "3001:3000"
```

Port 3001 będzie wykorzystywany na hoście, a port 3000 wewnątrz kontenera.

**4. Ponowne uruchomienie aplikacji:**

```bash
docker compose up -d
```

## 4. Wnioski

Przyczyną błędu jest konflikt portów. Problem można rozwiązać przez zatrzymanie procesu zajmującego port 3000 lub zmianę mapowania portów w konfiguracji Docker.

