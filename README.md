# ATA Engine DevTools

ATA Engine DevTools is an open-source collection of developer utilities for game engine development workflows.

The project focuses on practical tools for:

- Vulkan environment checks
- Build validation
- Asset pipeline validation
- Shader and log scanning
- CMake workflow helpers
- Windows development setup checks

## Why this project exists

Small game development teams often lose time because of missing SDKs, broken build environments, invalid asset names, shader errors, and hard-to-read engine logs.

This repository provides simple, practical tools to detect these problems earlier and make game engine development workflows more reliable.

## Tools

### Vulkan Environment Checker

Checks whether the local Windows development environment has basic Vulkan-related variables and paths configured.

### Engine Log Scanner

Scans engine log files for common errors, crashes, validation warnings, missing shaders, and graphics pipeline failures.

### Asset Name Validator

Checks project asset names for common production issues such as spaces, Turkish characters, unsafe symbols, and inconsistent naming.

### CMake Clean Build Helper

Provides a simple clean build workflow for CMake-based C++ projects.

## Project status

This project is in early active development.

The tools are extracted from real game engine development workflows and are being maintained for broader open-source game development use.

## Example usage

```bash
python tools/validate_asset_names.py ./Content
python tools/scan_engine_logs.py ./Logs
