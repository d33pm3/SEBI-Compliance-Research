#!/usr/bin/env python3
"""Validate public-release structure and common sensitive-data failure modes."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    ".gitignore",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "SKILL.md",
    "evals/evals.json",
    "evals/trigger-evals.json",
    "references/canonical_sources.md",
    "references/known_omissions.md",
    "references/mece_checklist.md",
    "references/output_standards.md",
}

FORBIDDEN_NAME_PATTERNS = (
    re.compile(r"^\.env(?:\.|$)", re.IGNORECASE),
    re.compile(r"(?:^|[-_.])(secret|credential|service[-_]?account)(?:[-_.]|$)", re.IGNORECASE),
    re.compile(r"\.(?:pem|key|p12|pfx|jks|keystore)$", re.IGNORECASE),
)

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "generic bearer token": re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b", re.IGNORECASE),
}

TEXT_SUFFIXES = {"", ".md", ".json", ".py", ".txt", ".yaml", ".yml"}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []
    files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]
    relative_files = {path.relative_to(ROOT).as_posix() for path in files}

    for required in sorted(REQUIRED_FILES - relative_files):
        fail(f"missing required file: {required}", failures)

    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        if any(pattern.search(path.name) for pattern in FORBIDDEN_NAME_PATTERNS):
            fail(f"forbidden sensitive filename: {relative}", failures)

        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"non-UTF-8 text-like file: {relative}", failures)
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(f"possible {label} in {relative}", failures)

    skill = ROOT / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail("SKILL.md lacks YAML frontmatter", failures)
        for required_field in ("name:", "description:"):
            if required_field not in text.split("---", 2)[1]:
                fail(f"SKILL.md frontmatter lacks {required_field[:-1]}", failures)

    for json_path in (ROOT / "evals/evals.json", ROOT / "evals/trigger-evals.json"):
        if json_path.exists():
            try:
                json.loads(json_path.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                fail(f"invalid JSON in {json_path.relative_to(ROOT)}: {exc}", failures)

    if failures:
        print("VALIDATION FAILED")
        for item in failures:
            print(f"- {item}")
        return 1

    print(f"VALIDATION PASSED: {len(relative_files)} files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
