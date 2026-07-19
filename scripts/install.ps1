[CmdletBinding()]
param(
    [ValidateNotNullOrEmpty()]
    [string]$Agent = 'codex',

    [ValidateNotNullOrEmpty()]
    [string]$Source,

    [switch]$Project
)

$ErrorActionPreference = 'Stop'

if (-not (Get-Command npx -ErrorAction SilentlyContinue)) {
    throw 'npx is required. Install a current Node.js release and try again.'
}

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
if (-not $Source) {
    $Source = $repoRoot
}

$arguments = @(
    '--yes',
    'skills',
    'add',
    $Source,
    '--skill',
    'frontend-design-pro',
    '--agent',
    $Agent,
    '--yes',
    '--copy'
)

if (-not $Project) {
    $arguments += '--global'
}

& npx @arguments
if ($LASTEXITCODE -ne 0) {
    throw "Skill installation failed with exit code $LASTEXITCODE."
}

Write-Host 'Frontend Design Pro installed. Restart the target agent before using it.'
