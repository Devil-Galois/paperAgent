param(
    [Parameter(Mandatory = $true)]
    [string]$Topic,

    [string]$BaseDir = "..\\papers"
)

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$safeTopic = ($Topic.ToLower() -replace "[^a-z0-9]+", "-").Trim("-")
if ([string]::IsNullOrWhiteSpace($safeTopic)) {
    $safeTopic = "paper-task"
}

$projectDir = Join-Path $PSScriptRoot $BaseDir
$projectName = "$timestamp-$safeTopic"
$targetDir = Join-Path $projectDir $projectName

New-Item -ItemType Directory -Path $targetDir -Force | Out-Null

$files = @{
    "intake.md" = "# Intake`n`n## Original Topic`n`n## Paper Type`n`n## Output Language`n`n## User Q&A Record`n`n## Hard Constraints`n`n## Soft Preferences`n`n## Must-Include Points`n`n## Must-Avoid Points`n`n## Open Questions`n`n## Agreed Direction`n"
    "brief.md" = "# Brief`n`n- Topic: $Topic`n- Paper Type:`n- Output Language:`n- Goal:`n- Scope:`n- Constraints:`n"
    "outline.md" = "# Outline`n`n## Candidate Title`n`n## Sections`n"
    "draft.md" = "# Draft`n"
    "references.md" = "# References`n"
    "notes.md" = "# Notes`n"
}

foreach ($name in $files.Keys) {
    $path = Join-Path $targetDir $name
    if (-not (Test-Path $path)) {
        Set-Content -Path $path -Value $files[$name] -Encoding UTF8
    }
}

$draftPath = Join-Path $targetDir "draft.md"
$docxPath = Join-Path $targetDir "final-manuscript.docx"
$exportScript = Join-Path $PSScriptRoot "export_final_docx.py"

if ((Test-Path $exportScript) -and (Get-Command python -ErrorAction SilentlyContinue)) {
    python $exportScript --input $draftPath --output $docxPath --title $Topic | Out-Null
}

Write-Output $targetDir
