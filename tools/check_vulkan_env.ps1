Write-Host "ATA Engine DevTools - Vulkan Environment Check"
Write-Host ""

$vulkanSdk = $env:VULKAN_SDK

if ([string]::IsNullOrWhiteSpace($vulkanSdk)) {
    Write-Host "[WARNING] VULKAN_SDK environment variable is not set."
} else {
    Write-Host "[OK] VULKAN_SDK = $vulkanSdk"

    if (Test-Path $vulkanSdk) {
        Write-Host "[OK] Vulkan SDK path exists."
    } else {
        Write-Host "[WARNING] Vulkan SDK path does not exist."
    }
}

Write-Host ""
Write-Host "Checking common Vulkan tools..."

$glslc = Get-Command glslc -ErrorAction SilentlyContinue
if ($glslc) {
    Write-Host "[OK] glslc found: $($glslc.Source)"
} else {
    Write-Host "[WARNING] glslc was not found in PATH."
}

$vulkanInfo = Get-Command vulkaninfo -ErrorAction SilentlyContinue
if ($vulkanInfo) {
    Write-Host "[OK] vulkaninfo found: $($vulkanInfo.Source)"
} else {
    Write-Host "[WARNING] vulkaninfo was not found in PATH."
}

Write-Host ""
Write-Host "Check completed."
