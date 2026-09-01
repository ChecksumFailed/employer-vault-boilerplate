import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "migrate_note_metadata.py"


class MigrateNoteMetadataTests(unittest.TestCase):
    def run_script(self, vault: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(vault), *args],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_dry_run_reports_change_without_writing(self) -> None:
        original = """---
type: meeting
projects:
  - "[[Project One]]"
people: []
---

# Example

## Summary

Keep me.
"""
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            note = vault / "Example.md"
            note.write_text(original, encoding="utf-8")

            result = self.run_script(vault)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("WOULD UPDATE Example.md", result.stdout)
            self.assertEqual(note.read_text(encoding="utf-8"), original)

    def test_write_moves_relationships_and_tags_into_visible_sections(self) -> None:
        original = """---
type: meeting
status: processed
projects:
  - "[[Project One]]"
  - "[[Project Two]]"
people: ["[[!AveryChen]]", "[[!MorganHale]]"]
company: "[[@ExampleCompany]]"
tags:
  - cmdb
  - "platform/operations"
summary: Keep this metadata.
---

# Example

## Summary

Keep this body.
"""
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            note = vault / "Example.md"
            note.write_text(original, encoding="utf-8")

            result = self.run_script(vault, "--write")

            self.assertEqual(result.returncode, 0, result.stderr)
            migrated = note.read_text(encoding="utf-8")
            frontmatter = migrated.split("---", 2)[1]
            self.assertNotIn("projects:", frontmatter)
            self.assertNotIn("people:", frontmatter)
            self.assertNotIn("company:", frontmatter)
            self.assertNotIn("tags:", frontmatter)
            self.assertIn("status: processed", frontmatter)
            self.assertIn("summary: Keep this metadata.", frontmatter)
            self.assertIn("projects:: [[Project One]], [[Project Two]]", migrated)
            self.assertIn("people:: [[!AveryChen]], [[!MorganHale]]", migrated)
            self.assertIn("company:: [[@ExampleCompany]]", migrated)
            self.assertIn("## Tags\n\n#cmdb #platform/operations", migrated)
            self.assertIn("## Summary\n\nKeep this body.", migrated)
            self.assertIn("UPDATED Example.md", result.stdout)

    def test_write_adds_empty_tags_section_to_typed_note(self) -> None:
        original = """---
type: project
status: active
---

# Project

## Current state

Active.
"""
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            note = vault / "Project.md"
            note.write_text(original, encoding="utf-8")

            result = self.run_script(vault, "--write")

            self.assertEqual(result.returncode, 0, result.stderr)
            migrated = note.read_text(encoding="utf-8")
            self.assertIn("## Tags\n\n<!-- Add a small number of relevant tags here. -->", migrated)
            self.assertNotIn("#tags", migrated)
            self.assertIn("## Current state\n\nActive.", migrated)

    def test_person_note_gains_projects_field_when_only_company_was_in_yaml(self) -> None:
        original = """---
type: person
company: "[[@ExampleCompany]]"
---

# Avery Chen

## Context

Colleague.
"""
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            note = vault / "Person.md"
            note.write_text(original, encoding="utf-8")

            result = self.run_script(vault, "--write")

            self.assertEqual(result.returncode, 0, result.stderr)
            migrated = note.read_text(encoding="utf-8")
            self.assertIn("company:: [[@ExampleCompany]]", migrated)
            self.assertIn("projects::", migrated)

    def test_write_is_idempotent(self) -> None:
        original = """---
type: note
status: active
---

# Already migrated

## Connections

projects:: [[Project One]]
people::

## Tags

#cmdb

## Notes

Unchanged.
"""
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            note = vault / "Existing.md"
            note.write_text(original, encoding="utf-8")

            first = self.run_script(vault, "--write")
            second = self.run_script(vault, "--write")

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(note.read_text(encoding="utf-8"), original)
            self.assertIn("No notes need migration.", first.stdout)


if __name__ == "__main__":
    unittest.main()
