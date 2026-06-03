import sys
from pathlib import Path

KEYWORDS = [
    "error",
    "exception",
    "crash",
    "assert",
    "validation",
    "failed",
    "missing",
    "pipeline",
    "shader",
    "vulkan",
]

def scan_file(path: Path) -> int:
    matches = 0

    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except Exception as exc:
        print(f"[ERROR] Could not read {path}: {exc}")
        return 1

    for index, line in enumerate(lines, start=1):
        lowered = line.lower()
        if any(keyword in lowered for keyword in KEYWORDS):
            matches += 1
            print(f"{path}:{index}: {line}")

    return matches

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python tools/scan_engine_logs.py <log-file-or-folder>")
        return 1

    target = Path(sys.argv[1])

    if not target.exists():
        print(f"[ERROR] Path not found: {target}")
        return 1

    total_matches = 0

    if target.is_file():
        total_matches += scan_file(target)
    else:
        for path in target.rglob("*.log"):
            total_matches += scan_file(path)

    print(f"Scan completed. Matches found: {total_matches}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
