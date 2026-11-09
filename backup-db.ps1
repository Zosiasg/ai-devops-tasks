# Prosty skrypt do backupu bazy danych MySQL

$DB_NAME = "app_database"
$BACKUP_DIR = "C:\Backups\db"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$FILENAME = Join-Path $BACKUP_DIR "${DB_NAME}_${DATE}.sql.gz"

# Sprawdzenie katalogu
if (-not (Test-Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR -Force | Out-Null
    Write-Host "Utworzono katalog $BACKUP_DIR"
}

Write-Host "Rozpoczynam backup bazy $DB_NAME..."

$tempFile = Join-Path $env:TEMP "${DB_NAME}_${DATE}.sql"

try {
    # Eksport bazy danych
    & mysqldump.exe -u root -p $DB_NAME > $tempFile

    if ($LASTEXITCODE -ne 0) {
        throw "Błąd podczas wykonywania mysqldump."
    }

    # Kompresja GZip
    $inputStream = [System.IO.File]::OpenRead($tempFile)
    $outputStream = [System.IO.File]::Create($FILENAME)

    try {
        $gzipStream = [System.IO.Compression.GZipStream]::new(
            $outputStream,
            [System.IO.Compression.CompressionMode]::Compress
        )

        try {
            $inputStream.CopyTo($gzipStream)
        }
        finally {
            $gzipStream.Dispose()
        }
    }
    finally {
        $inputStream.Dispose()
        $outputStream.Dispose()
    }

    Write-Host "Backup zakończony sukcesem: $FILENAME"
}
catch {
    Write-Host "Błąd podczas wykonywania backupu: $_"
    Remove-Item $FILENAME -ErrorAction SilentlyContinue
    exit 1
}
finally {
    Remove-Item $tempFile -ErrorAction SilentlyContinue
}