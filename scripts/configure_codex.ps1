param(
    [Parameter(Mandatory=$true)][string]$PythonPath,
    [string]$UserConfigPath = 'C:\Users\Craft\.codex\config.toml'
)
$ErrorActionPreference = 'Stop'
$taskRepoRoot = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot))
$taskSourcePath = Join-Path $taskRepoRoot 'config\codex.project.toml'
$taskTargetDirectory = Join-Path $taskRepoRoot '.codex'
$taskTargetPath = [IO.Path]::GetFullPath((Join-Path $taskTargetDirectory 'config.toml'))
if (-not $taskTargetPath.StartsWith($taskRepoRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Project settings target escaped the repository.'
}
if (-not (Test-Path -LiteralPath $UserConfigPath)) { throw 'Expected user config is missing; no global file was created.' }
@'
import sys,tomllib
tomllib.load(open(sys.argv[1], 'rb'))
tomllib.load(open(sys.argv[2], 'rb'))
print('TOML templates parse successfully')
'@ | & $PythonPath - $taskSourcePath $UserConfigPath
if ($LASTEXITCODE -ne 0) { throw 'Invalid TOML; no settings changed.' }
$taskUserText = [IO.File]::ReadAllText($UserConfigPath)
$taskTrustHeader = "[projects.'$taskRepoRoot']"
$taskTrustHeaderLower = "[projects.'$($taskRepoRoot.ToLowerInvariant())']"
if ($taskUserText.Contains($taskTrustHeader) -or $taskUserText.Contains($taskTrustHeaderLower)) {
    throw 'An exact project entry already exists; inspect and update that entry rather than adding a duplicate.'
}
$taskBackupPath = $UserConfigPath + '.or-tracker-backup-' + (Get-Date -Format 'yyyyMMdd-HHmmss')
Copy-Item -LiteralPath $UserConfigPath -Destination $taskBackupPath
$taskNewText = $taskUserText.TrimEnd() + "`r`n`r`n$taskTrustHeader`r`ntrust_level = `"trusted`"`r`n"
[IO.File]::WriteAllText($UserConfigPath, $taskNewText, [Text.UTF8Encoding]::new($false))
try {
    @'
import sys,tomllib
c=tomllib.load(open(sys.argv[1], 'rb'))
assert c['projects'][sys.argv[2]]['trust_level']=='trusted'
print('Exact OR tracker project is trusted')
'@ | & $PythonPath - $UserConfigPath $taskRepoRoot
    if ($LASTEXITCODE -ne 0) { throw 'User configuration validation failed.' }
    New-Item -ItemType Directory -Path $taskTargetDirectory -Force | Out-Null
    if (Test-Path -LiteralPath $taskTargetPath) { Copy-Item -LiteralPath $taskTargetPath -Destination ($taskTargetPath + '.before-setup') }
    Copy-Item -LiteralPath $taskSourcePath -Destination $taskTargetPath
    @'
import sys,tomllib
c=tomllib.load(open(sys.argv[1], 'rb'))
assert c['model']=='gpt-6.1-sol'
assert c['model_reasoning_effort']=='xhigh'
assert c['permissions']['or-hackathon']['extends']==':workspace'
assert c['permissions']['or-hackathon']['network']['enabled']
print('Project model, reasoning, web search, review and network profile saved')
'@ | & $PythonPath - $taskTargetPath
    if ($LASTEXITCODE -ne 0) { throw 'Project configuration validation failed.' }
} catch {
    Copy-Item -LiteralPath $taskBackupPath -Destination $UserConfigPath -Force
    if (Test-Path -LiteralPath ($taskTargetPath + '.before-setup')) {
        Copy-Item -LiteralPath ($taskTargetPath + '.before-setup') -Destination $taskTargetPath -Force
    } elseif (Test-Path -LiteralPath $taskTargetPath) {
        Remove-Item -LiteralPath $taskTargetPath
    }
    throw
}
Write-Output "Project config: $taskTargetPath"
Write-Output "User config backup: $taskBackupPath"
Write-Output 'Saved settings require reopening the repository/new session; this running session retains its current permissions.'
