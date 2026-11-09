# Zadanie 16: Konwersja Bash do PowerShell

## 1. Prompt

> Przekonwertuj skrypt Bash wykonujący kopię zapasową bazy MySQL na równoważny skrypt PowerShell dla Windows.

## 2. Odpowiedź ChatGPT

Wygenerowano skrypt `backup-db.ps1`, który:

1. Tworzy katalog kopii zapasowych, jeśli nie istnieje.
2. Generuje nazwę pliku zawierającą datę i godzinę.
3. Wykonuje eksport bazy MySQL za pomocą `mysqldump`.
4. Kompresuje kopię zapasową do formatu GZip.
5. Obsługuje błędy i usuwa pliki tymczasowe.

## 3. Porównanie Bash i PowerShell

| Funkcjonalność | Bash | PowerShell |
|---|---|---|
| Zmienne | `DB_NAME="..."` | `$DB_NAME = "..."` |
| Data | `date +%Y%m%d` | `Get-Date -Format "yyyyMMdd"` |
| Sprawdzenie katalogu | `[ ! -d "$DIR" ]` | `Test-Path` |
| Tworzenie katalogu | `mkdir -p` | `New-Item -ItemType Directory` |
| Wyświetlanie komunikatów | `echo` | `Write-Host` |
| Kompresja | `gzip` | `.NET GZipStream` |
| Obsługa błędów | `$?`, `exit` | `try/catch`, `$LASTEXITCODE` |

## 4. Wnioski

Oba skrypty realizują ten sam proces tworzenia kopii zapasowej bazy MySQL, ale wykorzystują inne polecenia i mechanizmy systemowe.

PowerShell umożliwia korzystanie z bibliotek .NET oraz strukturalnej obsługi błędów `try/catch`.

