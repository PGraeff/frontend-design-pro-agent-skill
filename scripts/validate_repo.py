#!/usr/bin/env python3
"""Validate the repository and installable skill without external packages."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from package_skill import package


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "frontend-design-pro"
TEXT_SUFFIXES = {".csv", ".md", ".py", ".txt", ".yaml", ".yml"}
REQUIRED_FILES = (
    "SKILL.md",
    "LICENSE.txt",
    "THIRD_PARTY_LICENSES.txt",
    "agents/openai.yaml",
    "scripts/search.py",
    "scripts/validate_data.py",
    "scripts/tests/test_core.py",
    "references/pro-rules.md",
    "references/quick-reference.md",
    "data/ux-guidelines.csv",
    "data/stacks/flutter.csv",
)


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def run(command: list[str]) -> None:
    print(f"+ {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=REPO_ROOT, check=True)


def validate_structure() -> None:
    if not SKILL_DIR.is_dir():
        fail(f"missing skill directory: {SKILL_DIR}")

    for relative in REQUIRED_FILES:
        if not (SKILL_DIR / relative).is_file():
            fail(f"missing required file: skills/frontend-design-pro/{relative}")

def validate_manifest() -> None:
    path = SKILL_DIR / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        fail(f"SKILL.md has {len(lines)} lines; keep it at or below 500")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")

    frontmatter = text[4:end]
    keys = []
    values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        keys.append(key)
        values[key] = value.strip()

    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter must contain only name and description")
    if values["name"] != SKILL_DIR.name:
        fail("skill name must match its directory")
    if len(values["description"]) < 80:
        fail("skill description is too short to trigger reliably")
    if "TODO" in text:
        fail("SKILL.md contains a TODO marker")

    metadata = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
    for required in (
        'display_name: "Frontend Design Pro"',
        "default_prompt:",
        "allow_implicit_invocation: true",
    ):
        if required not in metadata:
            fail(f"agents/openai.yaml is missing: {required}")


def validate_portability() -> None:
    forbidden_patterns = {
        "Windows user path": re.compile(r"[A-Za-z]:\\\\Users\\\\", re.IGNORECASE),
        "macOS user path": re.compile(r"/Users/[^/]+/"),
        "Linux user path": re.compile(r"/home/[^/]+/"),
        "Claude-only root": re.compile(r"CLAUDE_PLUGIN_ROOT"),
    }

    for path in SKILL_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as error:
            fail(f"file is not valid UTF-8: {path.relative_to(REPO_ROOT)} ({error})")

        if "data" in path.relative_to(SKILL_DIR).parts:
            continue

        for label, pattern in forbidden_patterns.items():
            if pattern.search(text):
                fail(f"{label} found in {path.relative_to(REPO_ROOT)}")


def validate_package() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        first = Path(temporary) / "first.zip"
        second = Path(temporary) / "second.zip"
        package(first)
        package(second)

        if first.read_bytes() != second.read_bytes():
            fail("skill packages are not byte-for-byte reproducible")

        with zipfile.ZipFile(first) as archive:
            entries = archive.infolist()
            names = {entry.filename for entry in entries}
            required = {
                "frontend-design-pro/SKILL.md",
                "frontend-design-pro/LICENSE.txt",
                "frontend-design-pro/THIRD_PARTY_LICENSES.txt",
                "frontend-design-pro/NOTICE.txt",
                "frontend-design-pro/scripts/search.py",
            }
            if not required.issubset(names):
                fail(f"skill package is missing: {sorted(required - names)}")
            if any("__pycache__" in name or name.endswith(".pyc") for name in names):
                fail("skill package contains generated cache files")
            if any(entry.compress_type != zipfile.ZIP_STORED for entry in entries):
                fail("skill package must use reproducible stored entries")
            if any(entry.create_system != 3 for entry in entries):
                fail("skill package contains platform-dependent metadata")


def main() -> None:
    validate_structure()
    validate_manifest()
    validate_portability()
    validate_package()

    run([sys.executable, str(SKILL_DIR / "scripts" / "validate_data.py")])
    run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(SKILL_DIR / "scripts" / "tests"),
            "-p",
            "test_*.py",
            "-v",
        ]
    )
    run(
        [
            sys.executable,
            str(SKILL_DIR / "scripts" / "search.py"),
            "mobile accessibility safe area navigation",
            "--stack",
            "flutter",
            "--max-results",
            "2",
        ]
    )

    print("OK: repository and installable skill are valid")


if __name__ == "__main__":
    main()
