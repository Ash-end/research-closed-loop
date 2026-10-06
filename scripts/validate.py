"""Check packaging invariants; this is not a scientific reasoning benchmark."""

from __future__ import annotations

from pathlib import Path
import re
import sys

import yaml

from install import SKILL_NAMES

ROOT = Path(__file__).resolve().parents[1]
TREES = (ROOT / "skills", ROOT / "locales/zh-CN/skills")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    trees = (root / "skills", root / "locales/zh-CN/skills")
    file_sets: list[set[str]] = []
    for tree in trees:
        found = {p.name for p in tree.iterdir() if p.is_dir()}
        if found != set(SKILL_NAMES):
            errors.append(f"Unexpected skill directory set: {tree.relative_to(root)}")
        file_sets.append({p.relative_to(tree).as_posix() for p in tree.rglob("*") if p.is_file()})
        for name in SKILL_NAMES:
            folder = tree / name
            entry = folder / "SKILL.md"
            if not entry.is_file():
                errors.append(f"Missing entry: {name}")
                continue
            text = entry.read_text(encoding="utf-8")
            sections = text.split("---", 2)
            if len(sections) != 3 or sections[0].strip():
                errors.append(f"Invalid frontmatter: {name}")
                continue
            try:
                meta = yaml.safe_load(sections[1])
                if not isinstance(meta, dict) or meta.get("name") != name:
                    errors.append(f"Wrong skill name: {name}")
                if not isinstance(meta, dict) or not isinstance(meta.get("description"), str) or not meta["description"].strip():
                    errors.append(f"Missing description: {name}")
                if not re.fullmatch(r"[a-z0-9-]{1,63}", name):
                    errors.append(f"Invalid skill name: {name}")
                ui = yaml.safe_load((folder / "agents/openai.yaml").read_text(encoding="utf-8"))
                interface = ui["interface"]
                if not 25 <= len(interface["short_description"]) <= 64:
                    errors.append(f"UI description length: {name}")
                if "$" + name not in interface["default_prompt"]:
                    errors.append(f"Default prompt lacks explicit skill: {name}")
            except (OSError, yaml.YAMLError, TypeError, KeyError) as error:
                errors.append(f"Metadata error: {name}: {error}")
    if file_sets[0] != file_sets[1]:
        errors.append("English/Chinese package file structures differ")

    forbidden_suffixes = {".pdf", ".epub", ".db", ".sqlite", ".pt", ".pth", ".ckpt"}
    secret_patterns = (
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
        re.compile(r"[A-Za-z]:[\\/]+Users[\\/]", re.IGNORECASE),
        re.compile(r"\b[0-9]{7,}@qq\.com\b", re.IGNORECASE),
    )
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in {".git", "__pycache__", ".venv"} for part in relative.parts):
            continue
        if path.is_symlink():
            errors.append(f"Symlink in public package: {relative}")
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() in forbidden_suffixes or path.name == ".env" or path.name.startswith(".env."):
            errors.append(f"Unexpected private/binary artifact: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            errors.append(f"Non-UTF-8 or unreadable file: {relative}")
            continue
        if any(pattern.search(text) for pattern in secret_patterns):
            # Never print the suspected value.
            errors.append(f"Review possible secret/private path: {relative}")
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                linked = path.parent / target.split("#", 1)[0]
                if not linked.exists():
                    errors.append(f"Broken local link in {relative}: {target}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("PASS: 14 skills, bilingual file parity, metadata, local links, and basic privacy checks")
    print("Structural validation is not a behavioral or scientific validity guarantee.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
