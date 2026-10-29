#!/usr/bin/env python3
"""Refuse to publish game data, generated output, or huge files.

    python -I tools/check_repo.py

This scans the git index. Submodule directories are gitlinks; their contents
are checked by the submodule repositories.

SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 5 * 1024 * 1024

FORBIDDEN_DIRS = (
    "build/",
    "assets/",
    "apps/",
    "Bin/",
    "RenderEngines/",
    "Managers/",
    "Plugins/",
    "BuildingBlocks/",
    "3D Entities/",
    "Sounds/",
    "Sounds_low/",
    "Textures/",
    "Text/",
    "Fonts/",
    "Wii/",
)

FORBIDDEN_SUFFIXES = (
    ".dol", ".elf", ".map", ".zip", ".7z", ".iso", ".cso", ".tdb", ".cmo",
    ".log", ".o", ".a",
)

FORBIDDEN_NAMES = (
    "base.cmo",
    "Database.tdb",
    "Player.ini",
    "Player.log",
    "registry.ini",
)


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    )
    return [p.decode("utf-8", "surrogateescape") for p in result.stdout.split(b"\0") if p]


def reason(path: str) -> str | None:
    if any(path.startswith(d) for d in FORBIDDEN_DIRS):
        return "game/build directory"
    name = Path(path).name
    suffix = Path(path).suffix.lower()
    if suffix in FORBIDDEN_SUFFIXES:
        return f"forbidden file type {suffix}"
    if name in FORBIDDEN_NAMES:
        return "game data or build output"
    full = ROOT / path
    if full.is_file() and full.stat().st_size > MAX_BYTES:
        return f"file is larger than {MAX_BYTES // (1024 * 1024)} MiB"
    return None


def main() -> None:
    try:
        files = tracked_files()
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"[check] cannot list git files: {exc}", file=sys.stderr)
        raise SystemExit(2)

    bad: list[tuple[str, str]] = []
    for path in files:
        why = reason(path)
        if why:
            bad.append((path, why))

    if bad:
        print("[check] refusing to publish: game data or build output is tracked:\n")
        for path, why in bad:
            print(f"  {path}  ({why})")
        print(
            "\nRemove them from the index with `git rm --cached <path>` and add "
            "them to .gitignore, then run this check again."
        )
        raise SystemExit(1)

    print(f"[check] OK: {len(files)} tracked file(s), no game data or build output.")


if __name__ == "__main__":
    main()
