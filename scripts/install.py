"""Install one language of the seven research skills without replacing entries."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil

SKILL_NAMES = (
    "research-closed-loop",
    "research-problem-localization",
    "research-bottleneck-diagnosis",
    "research-gap-mapping",
    "research-minimal-prototype",
    "research-validation-design",
    "research-portfolio-management",
)


def install_skills(
    repo_root: Path, destination: Path, language: str = "en", dry_run: bool = False
) -> list[Path]:
    if language not in {"en", "zh"}:
        raise ValueError("Language must be en or zh")
    repo_root = repo_root.resolve()
    destination = destination.expanduser().resolve()
    if destination == repo_root or repo_root in destination.parents:
        raise ValueError("Choose a destination outside this repository")
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination exists and is not a directory")
    source_root = repo_root / (
        "skills" if language == "en" else "locales/zh-CN/skills"
    )
    targets = [destination / name for name in SKILL_NAMES]
    # Check all sources and all collisions before changing the destination.
    for name, target in zip(SKILL_NAMES, targets):
        source = source_root / name
        if source.is_symlink() or not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing or symlinked skill source: {name}")
        if any(item.is_symlink() for item in source.rglob("*")):
            raise ValueError(f"Symlink inside skill package: {name}")
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Refusing to replace existing skill entry: {target}")
    if dry_run:
        return targets
    destination.mkdir(parents=True, exist_ok=True)
    for name, target in zip(SKILL_NAMES, targets):
        # No merge/overwrite flag: fail if another process created the target.
        shutil.copytree(source_root / name, target)
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, required=True, help="Skill discovery directory")
    parser.add_argument("--language", choices=("en", "zh"), default="en")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print without copying")
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    try:
        targets = install_skills(repo_root, args.dest, args.language, args.dry_run)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation stopped: {error}\nInspect any partial copy before retrying.\n")
    action = "Would install" if args.dry_run else "Installed"
    for target in targets:
        print(f"{action}: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
