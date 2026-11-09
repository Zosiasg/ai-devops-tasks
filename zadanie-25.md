# Zadanie 25: Generowanie prostego Jenkinsfile

## 1. Prompt

> Wygeneruj prosty Jenkinsfile dla aplikacji Node.js, zawierający checkout kodu, instalację zależności, testy, budowanie aplikacji, budowanie obrazu Docker oraz publikowanie obrazu w rejestrze. Użyj składni deklaratywnej Jenkinsa.

## 2. Odpowiedź ChatGPT

Wygenerowano deklaratywny pipeline CI/CD zapisany w pliku `Jenkinsfile`.

Pipeline zawiera sześć etapów:

| Etap | Opis |
|---|---|
| Checkout | Pobiera kod z repozytorium Git. |
| Install Dependencies | Instaluje zależności przez `npm install`. |
| Test | Uruchamia testy automatyczne przez `npm test`. |
| Build Application | Buduje aplikację przez `npm run build`. |
| Build Docker Image | Tworzy obraz kontenera przez `docker build`. |
| Push Docker Image | Loguje się do Docker Hub i publikuje obraz. |

## 3. Prompt uzupełniający

> Wyjaśnij, co dokładnie dzieje się w każdym etapie tego Jenkinsfile i jakie są najlepsze praktyki przy tworzeniu pipeline'ów Jenkins.

## 4. Najlepsze praktyki

1. **Automatyzacja CI/CD** – automatyczne budowanie i testowanie aplikacji.
2. **Bezpieczeństwo** – przechowywanie danych logowania w Jenkins Credentials.
3. **Wczesne testowanie** – uruchamianie testów przed budowaniem obrazu Docker.
4. **Wersjonowanie obrazów** – oznaczanie obrazów numerem buildu.
5. **Obsługa błędów** – zatrzymanie pipeline'u w przypadku niepowodzenia etapu.
6. **Powtarzalność** – przechowywanie konfiguracji pipeline'u w repozytorium Git.

## 5. Uwagi

Pipeline wymaga odpowiednio skonfigurowanego środowiska Jenkins, dostępu do Docker Hub oraz projektu Node.js z wymaganymi skryptami.

Wygenerowana konfiguracja stanowi przykład edukacyjny i nie została uruchomiona.