#!/usr/bin/env python3
"""Reject mutable SmartHomeShop radar dependencies in production firmware."""

from __future__ import annotations

import re
import sys
from pathlib import Path

RADARS = "ld2450|ld2460|ld6002b"
DIRECT_REFERENCE = re.compile(
    rf"github://smarthomeshop/(?:{RADARS})(?:/[^\s]+)?@(?P<ref>[^\s\"']+)"
)
REPOSITORY_URL = re.compile(
    rf"https://github\.com/smarthomeshop/(?:{RADARS})(?:\.git)?\s*$"
)
VERSION_TAG = re.compile(r"^v\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")


def yaml_files(roots: list[str]):
    for root_name in roots:
        root = Path(root_name)
        if root.is_file() and root.suffix in {".yaml", ".yml"}:
            yield root
        elif root.is_dir():
            yield from root.rglob("*.yaml")
            yield from root.rglob("*.yml")


def validate(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    for line_number, line in enumerate(lines, start=1):
        for match in DIRECT_REFERENCE.finditer(line):
            ref = match.group("ref")
            if not VERSION_TAG.fullmatch(ref):
                errors.append(f"{path}:{line_number}: radar dependency uses mutable ref {ref!r}")

        if not REPOSITORY_URL.search(line.strip()):
            continue

        ref = None
        ref_line = line_number
        for offset, following in enumerate(lines[line_number : line_number + 12], start=1):
            match = re.match(r"\s*ref:\s*([^\s#]+)", following)
            if match:
                ref = match.group(1).strip('"\'')
                ref_line = line_number + offset
                break
            if re.match(r"\s*url:\s*", following):
                break

        if ref is None:
            errors.append(f"{path}:{line_number}: radar repository has no explicit version tag")
        elif not VERSION_TAG.fullmatch(ref):
            errors.append(f"{path}:{ref_line}: radar dependency uses mutable ref {ref!r}")

    return errors


def main() -> int:
    roots = sys.argv[1:] or ["."]
    errors = [error for path in yaml_files(roots) for error in validate(path)]
    if errors:
        print("Radar dependencies must use immutable semantic-version tags:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("All SmartHomeShop radar dependencies use immutable version tags.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
