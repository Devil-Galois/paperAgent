param(
    [string]$Name = "Your Name",
    [string]$Target = "academic",
    [ValidateSet("zh", "en", "bilingual")]
    [string]$Language = "zh",
    [ValidateSet("classic", "compact", "modern", "academic")]
    [string]$Template = "classic",
    [string]$PhotoPath = "",
    [string]$Slug = "",
    [string]$BaseDir = "..\cvs"
)

$scriptPath = Join-Path $PSScriptRoot "init_cv_project.py"
$argsList = @(
    $scriptPath,
    "--name", $Name,
    "--target", $Target,
    "--language", $Language,
    "--template", $Template,
    "--base-dir", $BaseDir
)

if (-not [string]::IsNullOrWhiteSpace($PhotoPath)) {
    $argsList += @("--photo-path", $PhotoPath)
}

if (-not [string]::IsNullOrWhiteSpace($Slug)) {
    $argsList += @("--slug", $Slug)
}

& python @argsList
exit $LASTEXITCODE
