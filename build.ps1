param(
    [ValidateSet('md', 'tex', 'pdf', 'docx', 'all', 'package', 'clean')]
    [string]$Target = 'all'
)

$ErrorActionPreference = 'Stop'
$RepositoryRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $RepositoryRoot 'scripts\build.py') $Target
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
