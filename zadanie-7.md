# Zadanie 7: Wygenerowanie prostego skryptu Bash

## 1. Prompt

**Prompt:**
> Napisz prosty skrypt bash, który sprawdza, czy usługa Docker działa, a jeśli nie – próbuje ją uruchomić.

**Odpowiedź ChatGPT:** Wygenerowano skrypt `check_docker.sh`, który sprawdza status usługi Docker i w razie potrzeby próbuje ją uruchomić.

## 2. Prompt uzupełniający

**Prompt:**
> Wyjaśnij działanie tego skryptu linia po linii, tak jakbyś tłumaczył osobie początkującej.

## 3. Wyjaśnienie skryptu

| Kod | Wyjaśnienie |
|---|---|
| `#!/bin/bash` | Określa interpreter Bash. |
| `# ...` | Komentarz wyjaśniający działanie kodu. |
| `if systemctl is-active --quiet docker; then` | Sprawdza, czy usługa Docker jest aktywna. |
| `echo "Docker działa poprawnie."` | Wyświetla komunikat o działającej usłudze. |
| `else` | Wykonuje kolejne instrukcje, gdy usługa nie działa. |
| `echo "Docker nie działa..."` | Informuje o próbie uruchomienia usługi. |
| `sudo systemctl start docker` | Próbuje uruchomić usługę Docker z uprawnieniami administratora. |
| `if systemctl is-active --quiet docker; then` | Ponownie sprawdza status usługi. |
| `echo "Docker został uruchomiony."` | Potwierdza uruchomienie usługi. |
| `echo "Nie udało się uruchomić Dockera."` | Informuje o niepowodzeniu. |
| `exit 1` | Kończy skrypt z kodem błędu. |
| `fi` | Kończy instrukcję warunkową `if`. |

## 4. Wnioski

ChatGPT wygenerował prosty skrypt Bash oraz wyjaśnił jego działanie. Skrypt wykorzystuje `systemctl` do sprawdzania i uruchamiania usługi Docker w systemie Linux z systemd.

**Wniosek:** AI może pomagać zarówno w tworzeniu skryptów administracyjnych, jak i w zrozumieniu ich działania.