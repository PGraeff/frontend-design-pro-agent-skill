#!/usr/bin/env python3
"""Build a deterministic ZIP containing only the installable skill."""

from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "frontend-design-pro"
DEFAULT_OUTPUT = REPO_ROOT / "dist" / "frontend-design-pro.zip"


def included_files() -> list[Path]:
    return sorted(
        path
        for path in SKILL_DIR.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    )


def package(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output,
        mode="w",
        compression=zipfile.ZIP_STORED,
    ) as archive:
        for source in included_files():
            relative = source.relative_to(SKILL_DIR).as_posix()
            info = zipfile.ZipInfo(
                filename=f"frontend-design-pro/{relative}",
                date_time=(1980, 1, 1, 0, 0, 0),
            )
            info.create_system = 3
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    try:
        display_path = output.relative_to(REPO_ROOT)
    except ValueError:
        display_path = output
    print(f"Built {display_path}")
    print(f"SHA256 {digest}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    package(args.output.resolve())


if __name__ == "__main__":
    main()
