from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COMPILER = ROOT / "logic_compiler.py"
TEST_CASES = ROOT / "test_cases.md"
TEST_RESULT = ROOT / "test_result.md"
_TMP_INPUT = ROOT / "_tmp_test_case.txt"
_TMP_OUTPUT = ROOT / "_tmp_test_result.json"


def parse_test_cases(text: str) -> list[tuple[str, list[str]]]:
    lines = text.splitlines()
    cases: list[tuple[str, list[str]]] = []
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if not line.startswith("### "):
            index += 1
            continue

        title = line
        index += 1

        if index < len(lines) and lines[index].strip() == "```plaintext":
            index += 1
            source_lines: list[str] = []
            while index < len(lines) and lines[index].strip() != "```":
                source_lines.append(lines[index])
                index += 1
            if index < len(lines) and lines[index].strip() == "```":
                index += 1
            cases.append((title, source_lines))
            continue

        index += 1

    return cases


def run_case(source_lines: list[str]) -> dict:
    _TMP_INPUT.write_text("\n".join(source_lines) + "\n", encoding="utf-8")
    subprocess.run(
        [sys.executable, str(COMPILER), str(_TMP_INPUT), str(_TMP_OUTPUT)],
        cwd=str(ROOT),
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(_TMP_OUTPUT.read_text(encoding="utf-8"))


def render_case(title: str, source_lines: list[str], result: dict) -> list[str]:
    rendered = [title, "```plaintext", *source_lines, "```", "```json"]
    rendered.extend(json.dumps(result, indent=2, ensure_ascii=False).splitlines())
    rendered.append("```")
    return rendered


def main() -> None:
    cases = parse_test_cases(TEST_CASES.read_text(encoding="utf-8"))
    output_lines: list[str] = []

    for title, source_lines in cases:
        result = run_case(source_lines)
        output_lines.extend(render_case(title, source_lines, result))
        output_lines.append("")

    TEST_RESULT.write_text("\n".join(output_lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {TEST_RESULT}")


if __name__ == "__main__":
    main()