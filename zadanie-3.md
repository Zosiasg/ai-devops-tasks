# Zadanie 3: Podstawowe formatowanie promptu

## 1. Prompt niestrukturyzowany

**Prompt:** `dockerfile node`

**Odpowiedź ChatGPT:**

```dockerfile
FROM node:lts
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "index.js"]
```

Model wygenerował podstawowy Dockerfile, samodzielnie przyjmując założenia dotyczące wersji Node.js i sposobu uruchamiania aplikacji.

## 2. Prompt strukturyzowany

**Prompt:**

Napisz prosty Dockerfile dla aplikacji Node.js, który:
- używa Node 18 jako obrazu bazowego
- kopiuje pliki package.json i package-lock.json
- instaluje zależności
- kopiuje resztę plików aplikacji
- wystawia port 3000
- uruchamia aplikację poleceniem "npm start"

**Odpowiedź ChatGPT:**

```dockerfile
FROM node:18
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Model wygenerował Dockerfile zgodny z podanymi wymaganiami.

## 3. Porównanie odpowiedzi

| Kryterium | Prompt prosty | Prompt strukturyzowany |
|---|---|---|
| Wersja Node.js | LTS | 18 |
| Instalacja | npm install | npm ci |
| Kopiowanie plików | Wszystkie jednocześnie | Etapami |
| Uruchomienie | node index.js | npm start |
| Precyzja | Niska | Wysoka |

## 4. Wnioski

Prompt strukturyzowany pozwolił uzyskać bardziej precyzyjny kod, zgodny z wymaganiami. Prompt niestrukturyzowany pozostawił modelowi większą swobodę interpretacji
