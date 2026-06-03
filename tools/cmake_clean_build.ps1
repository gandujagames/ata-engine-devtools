param(
    [string]$SourceDir = ".",
    [string]$BuildDir = "Build",
    [string]$Config = "Debug"
)

Write-Host "ATA Engine DevTools - CMake Clean Build"
Write-Host "SourceDir: $SourceDir"
Write-Host "BuildDir: $BuildDir"
Write-Host "Config: $Config"
Write-Host ""

if (Test-Path $BuildDir) {
    Write-Host "Removing old build directory..."
    Remove-Item $BuildDir -Recurse -Force
}

Write-Host "Configuring CMake..."
cmake -S $SourceDir -B $BuildDir

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] CMake configure failed."
    exit $LASTEXITCODE
}

Write-Host "Building..."
cmake --build $BuildDir --config $Config

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Build failed."
    exit $LASTEXITCODE
}

Write-Host "[OK] Build completed."
