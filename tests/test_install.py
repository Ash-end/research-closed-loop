from pathlib import Path
import tempfile
import unittest

from scripts.install import SKILL_NAMES, install_skills


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.repo = self.base / "repo"
        for language, relative in (("English", "skills"), ("Chinese", "locales/zh-CN/skills")):
            for name in SKILL_NAMES:
                folder = self.repo / relative / name
                folder.mkdir(parents=True)
                (folder / "SKILL.md").write_text(f"{language}: {name}\n", encoding="utf-8")
                (folder / "assets").mkdir()
                (folder / "assets/card.md").write_text("template\n", encoding="utf-8")

    def test_dry_run_creates_nothing(self):
        dest = self.base / "destination"
        targets = install_skills(self.repo, dest, dry_run=True)
        self.assertEqual(len(targets), 7)
        self.assertFalse(dest.exists())

    def test_english_and_nested_assets_copy(self):
        dest = self.base / "destination"
        install_skills(self.repo, dest)
        for name in SKILL_NAMES:
            self.assertTrue((dest / name / "SKILL.md").read_text().startswith("English:"))
            self.assertEqual((dest / name / "assets/card.md").read_text(), "template\n")

    def test_chinese_language_source(self):
        dest = self.base / "destination"
        install_skills(self.repo, dest, language="zh")
        self.assertTrue((dest / SKILL_NAMES[0] / "SKILL.md").read_text().startswith("Chinese:"))

    def test_existing_entry_preserved_before_any_copy(self):
        dest = self.base / "destination"
        existing = dest / SKILL_NAMES[-1]
        existing.mkdir(parents=True)
        record = existing / "keep.md"
        record.write_text("user content", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            install_skills(self.repo, dest)
        self.assertEqual(record.read_text(), "user content")
        self.assertEqual(list(dest.iterdir()), [existing])

    def test_invalid_language(self):
        dest = self.base / "destination"
        with self.assertRaises(ValueError):
            install_skills(self.repo, dest, language="invalid")
        self.assertFalse(dest.exists())

    def test_repository_internal_destination(self):
        with self.assertRaises(ValueError):
            install_skills(self.repo, self.repo / "installed")

    def test_missing_source_has_no_partial_copy(self):
        missing = self.repo / "skills" / SKILL_NAMES[-1] / "SKILL.md"
        missing.unlink()
        dest = self.base / "destination"
        with self.assertRaises(ValueError):
            install_skills(self.repo, dest)
        self.assertFalse(dest.exists())

    def test_destination_file_preserved(self):
        dest = self.base / "destination"
        dest.write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            install_skills(self.repo, dest)
        self.assertEqual(dest.read_text(), "keep")

    def test_source_symlink_rejected(self):
        link = self.repo / "skills" / SKILL_NAMES[0] / "assets/link.md"
        try:
            link.symlink_to(link.parent / "card.md")
        except OSError:
            self.skipTest("Symlink creation is not permitted on this host")
        dest = self.base / "destination"
        with self.assertRaises(ValueError):
            install_skills(self.repo, dest)
        self.assertFalse(dest.exists())


if __name__ == "__main__":
    unittest.main()
