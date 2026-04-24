from __future__ import annotations

import json
from pathlib import Path


def extract_json_block(lines: list[str], start_index: int) -> tuple[list[str], int]:
    block: list[str] = []
    depth = 0
    in_string = False
    escape = False
    started = False

    index = start_index
    while index < len(lines):
        line = lines[index]
        block.append(line)

        for char in line:
            if escape:
                escape = False
                continue
            if char == "\\":
                escape = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if char == '{':
                depth += 1
                started = True
            elif char == '}':
                depth -= 1

        index += 1
        if started and depth == 0:
            break

    return block, index


def convert_test_result(source_path: Path, target_path: Path) -> None:
    lines = source_path.read_text(encoding="utf-8").splitlines()
    output: list[str] = []

    index = 0
    while index < len(lines):
        line = lines[index]

        if line.startswith("### "):
            output.append(line)
            index += 1
            continue

        if line.strip() == "```plaintext":
            output.append("```plaintext")
            index += 1
            while index < len(lines) and lines[index].strip() != "````" and lines[index].strip() != "```":
                output.append(lines[index])
                index += 1
            if index < len(lines):
                output.append("```")
                index += 1
            continue

        if line.lstrip().startswith("{"):
            json_block, index = extract_json_block(lines, index)
            output.append("```json")
            output.extend(json_block)
            output.append("```")
            continue

        output.append(line)
        index += 1

    target_path.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> None:
    source = Path(__file__).with_name("test_result.txt")
    target = Path(__file__).with_name("test_result.md")
    convert_test_result(source, target)
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()