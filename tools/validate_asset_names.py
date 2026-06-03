import os
import re
import sys

INVALID_PATTERN = re.compile(r"[^a-zA-Z0-9_\-./\\]")

def validate_path(path: str) -> list[str]:
    issues = []

    if " " in path:
        issues.append("contains spaces")

    if INVALID_PATTERN.search(path):
        issues.append("contains unsafe characters")

    if any(char in path for char in "çğıöşüÇĞİÖŞÜ"):
        issues.append("contains Turkish characters")

    return issues

def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 else "."

    found_issues = False

    for current_root, _, files in os.walk(root):
        for filename in files:
            full_path = os.path.join(current_root, filename)
            issues = validate_path(full_path)

            if issues:
                found_issues = True
                print(f"[WARNING] {full_path}")
                for issue in issues:
                    print(f"  - {issue}")

    if not found_issues:
        print("No asset naming issues found.")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
