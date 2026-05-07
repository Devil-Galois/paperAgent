param(
    [Parameter(Mandatory = $true)]
    [string]$Query,

    [string]$ChromePath = $env:CHROME_PATH
)

$encoded = [System.Uri]::EscapeDataString($Query)
$urls = @(
    "https://scholar.google.com/scholar?q=$encoded",
    "https://www.google.com/search?q=$encoded",
    "https://arxiv.org/search/?query=$encoded&searchtype=all"
)

if ([string]::IsNullOrWhiteSpace($ChromePath)) {
    $chromeCandidates = @(
        "C:\Program Files\Google\Chrome\Application\chrome.exe",
        "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    )
    $ChromePath = $chromeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
}

if (-not $ChromePath) {
    Write-Error "Chrome executable not found. Set CHROME_PATH first."
    exit 1
}

foreach ($url in $urls) {
    Start-Process -FilePath $ChromePath -ArgumentList $url
}

Write-Output "Opened search pages for query: $Query"
