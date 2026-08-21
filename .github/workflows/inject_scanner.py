import os
import sys

SYSTEM_PROMPT_PATTERNS = [
    "SYSTEM_PROMPT",
    "system_prompt",
    "system_message",
    "role: system",
]

INJECTION_PHRASES = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "pretend you are",
    "you are now",
    "no restrictions",
    "do anything",
]

def scan_file(path):
    findings = []

    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            for line_number, line in enumerate(file, start=1):
                lower_line = line.lower()

                for pattern in SYSTEM_PROMPT_PATTERNS:
                    if pattern.lower() in lower_line:
                        findings.append(
                            f"{path}:{line_number}: system prompt pattern: {pattern}"
                        )

                for phrase in INJECTION_PHRASES:
                    if phrase.lower() in lower_line:
                        findings.append(
                            f"{path}:{line_number}: injection phrase: {phrase}"
                        )

    except Exception as error:
        print(f"Could not scan {path}: {error}")

    return findings


def main():
    findings = []

    for root, _, files in os.walk("."):
        if ".git" in root.split(os.sep):
            continue

        for filename in files:
            if filename.endswith(".py"):
                path = os.path.join(root, filename)

                if path.endswith("inject_scanner.py"):
                    continue

                findings.extend(scan_file(path))

    if findings:
        print("CUSTOM PROMPT INJECTION SCANNER FAILED")
        print("----------------------------------------")

        for finding in findings:
            print(finding)

        sys.exit(1)

    print("CUSTOM PROMPT INJECTION SCANNER PASSED")


if __name__ == "__main__":
    main()
