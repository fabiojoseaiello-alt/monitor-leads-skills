param(
  [string]$Destination,
  [switch]$Force
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceRoot = Join-Path $repoRoot 'skills'

if (-not $Destination) {
  $codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
  $Destination = Join-Path $codexRoot 'skills'
}

New-Item -ItemType Directory -Path $Destination -Force | Out-Null

Get-ChildItem -LiteralPath $sourceRoot -Directory | ForEach-Object {
  $target = Join-Path $Destination $_.Name
  if ((Test-Path -LiteralPath $target) -and -not $Force) {
    throw "A skill '$($_.Name)' já existe em '$target'. Use -Force para atualizar."
  }
  Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force:$Force
  Write-Host "Instalada: $($_.Name)"
}

Write-Host "Skills instaladas em: $Destination"

