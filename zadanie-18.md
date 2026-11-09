# Zadanie 18: Analiza wymagań bezpieczeństwa

## 1. Prompt

> Jakie są 5 kluczowych praktyk bezpieczeństwa dla aplikacji Dockerowych w środowisku produkcyjnym?

## 2. Odpowiedź ChatGPT

1. **Uruchamianie kontenerów bez uprawnień root** – ogranicza skutki potencjalnego przejęcia aplikacji.
2. **Wykorzystywanie zaufanych obrazów** – stosowanie oficjalnych, aktualizowanych obrazów i skanowanie ich pod kątem podatności.
3. **Ograniczanie uprawnień kontenerów** – stosowanie zasady najmniejszych uprawnień (Least Privilege).
4. **Bezpieczne zarządzanie sekretami** – przechowywanie haseł i kluczy API poza obrazami Docker i kodem źródłowym.
5. **Monitorowanie i aktualizowanie kontenerów** – regularne aktualizacje, analiza logów i kontrola podatności.

## 3. Prompt uzupełniający

> Jak mogę zaimplementować pierwszą z tych praktyk w moim Dockerfile i docker-compose.yml?

## 4. Odpowiedź ChatGPT

Aby uruchamiać kontener bez uprawnień root, należy utworzyć użytkownika z ograniczonymi uprawnieniami i wskazać go w konfiguracji.

**Dockerfile:**

```dockerfile
FROM node:24-alpine

WORKDIR /app

COPY --chown=node:node package*.json ./
RUN npm ci --omit=dev

COPY --chown=node:node . .

USER node

EXPOSE 3000

CMD ["npm", "start"]
```

**docker-compose.yml:**

```yaml
services:
  app:
    build: .
    user: "node"
    ports:
      - "3000:3000"
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
```

**Wyjaśnienie:**

- `USER node` – uruchamia aplikację jako użytkownik bez uprawnień root.
- `--chown=node:node` – ustawia właściciela kopiowanych plików.
- `user: "node"` – wymusza użytkownika w Docker Compose.
- `no-new-privileges:true` – blokuje uzyskiwanie dodatkowych uprawnień przez procesy.
- `cap_drop: ALL` – usuwa dodatkowe uprawnienia systemowe kontenera.

Przykład zakłada istnienie skryptu `npm start` oraz poprawnego pliku `package-lock.json`.

