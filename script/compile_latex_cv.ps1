param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectDir,

    [string]$Main = "cv.tex",

    [string]$Engine = "xelatex",

    [switch]$CleanAux
)

$resolvedProject = Resolve-Path -LiteralPath $ProjectDir
$mainPath = Join-Path $resolvedProject $Main
if (-not (Test-Path -LiteralPath $mainPath)) {
    throw "Main TeX file not found: $mainPath"
}

$engineCommand = Get-Command $Engine -ErrorAction SilentlyContinue
if (-not $engineCommand) {
    throw "LaTeX engine '$Engine' not found. Install TeX Live/MiKTeX or compile cv.tex on Overleaf with XeLaTeX."
}

Push-Location $resolvedProject
try {
    & $Engine -interaction=nonstopmode -halt-on-error $Main
    if ($LASTEXITCODE -ne 0) {
        throw "LaTeX compilation failed with exit code $LASTEXITCODE."
    }
    $pdfPath = [System.IO.Path]::ChangeExtension((Join-Path $resolvedProject $Main), ".pdf")
    $finalPath = Join-Path $resolvedProject "final-cv.pdf"
    Copy-Item -LiteralPath $pdfPath -Destination $finalPath -Force

    if ($CleanAux) {
        $stem = [System.IO.Path]::GetFileNameWithoutExtension($Main)
        foreach ($ext in @("aux", "log", "out", "toc", "fls", "fdb_latexmk")) {
            $candidate = Join-Path $resolvedProject "$stem.$ext"
            if (Test-Path -LiteralPath $candidate) {
                Remove-Item -LiteralPath $candidate -Force
            }
        }
    }

    Write-Output $finalPath
}
finally {
    Pop-Location
}
