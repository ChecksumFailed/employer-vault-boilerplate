#!/usr/bin/env python3
"""Move Obsidian relationship properties from YAML into Dataview inline fields."""

from __future__ import annotations

import argparse
import ast
import csv
import io
import re
import sys
from dataclasses import dataclass
from pathlib import Path


RELATIONSHIP_KEYS = ("projects", "people", "company")
SKIPPED_DIRECTORIES = {".git", ".obsidian", "Templates", "node_modules"}
EXPECTED_RELATIONSHIPS = {
    "decision": ("projects", "people"),
    "knowledge": ("projects", "people"),
    "meeting": ("projects", "people"),
    "note": ("projects", "people"),
    "person": ("company", "projects"),
    "research": ("projects", "people"),
    "work-item": ("projects", "people"),
}


@dataclass
class Migration:
    text: str
    changed: bool
    warning: str | None = None


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
        return str(parsed)
    return value


def parse_values(raw: str) -> list[str]:
    raw = raw.strip()
    if not raw or raw == "[]":
        return []
    if raw.startswith("[") and raw.endswith("]"):
        reader = csv.reader(io.StringIO(raw[1:-1]), skipinitialspace=True)
        return [unquote(value) for value in next(reader, []) if value.strip()]
    return [unquote(raw)]


def extract_migrated_fields(
    frontmatter: list[str],
) -> tuple[list[str], dict[str, list[str]], set[str]]:
    kept: list[str] = []
    values: dict[str, list[str]] = {}
    present: set[str] = set()
    index = 0

    while index < len(frontmatter):
        match = re.match(r"^(projects|people|company|tags):(?:\s*(.*))?$", frontmatter[index])
        if not match:
            kept.append(frontmatter[index])
            index += 1
            continue

        key = match.group(1)
        present.add(key)
        values[key] = parse_values(match.group(2) or "")
        index += 1

        while index < len(frontmatter):
            item = re.match(r'^\s+-\s+(.*)$', frontmatter[index])
            if not item:
                break
            values[key].extend(parse_values(item.group(1)))
            index += 1

    return kept, values, present


def insertion_point(body: list[str]) -> int:
    for index, line in enumerate(body):
        if re.match(r"^#\s+\S", line):
            index += 1
            while index < len(body) and not body[index].strip():
                index += 1
            return index

    index = 0
    while index < len(body) and not body[index].strip():
        index += 1
    return index


def body_tag(tag: str) -> str:
    normalized = tag.strip().lstrip("#").replace(" ", "-")
    return f"#{normalized}" if normalized else ""


def migrate_text(text: str) -> Migration:
    newline = "\r\n" if "\r\n" in text else "\n"
    trailing_newline = text.endswith(("\n", "\r"))
    lines = text.splitlines()

    if len(lines) < 3 or lines[0].strip() != "---":
        return Migration(text, False)

    try:
        frontmatter_end = lines.index("---", 1)
    except ValueError:
        return Migration(text, False, "frontmatter has no closing delimiter")

    frontmatter = lines[1:frontmatter_end]
    type_line = next((line for line in frontmatter if re.match(r"^type:\s*\S", line)), None)
    if type_line is None:
        return Migration(text, False)
    note_type = unquote(type_line.split(":", 1)[1]).strip()

    body = lines[frontmatter_end + 1 :]
    kept, values, present = extract_migrated_fields(frontmatter)

    conflicts = [
        key
        for key in RELATIONSHIP_KEYS
        if key in present and any(re.match(rf"^{key}::", line) for line in body)
    ]
    if "tags" in present and any(line.strip() == "## Tags" for line in body):
        conflicts.append("tags")
    if conflicts:
        fields = ", ".join(conflicts)
        return Migration(text, False, f"both YAML and body fields exist for: {fields}")

    expected = EXPECTED_RELATIONSHIPS.get(note_type, ())
    relationship_fields = [*expected]
    relationship_fields.extend(
        key for key in RELATIONSHIP_KEYS if key in present and key not in relationship_fields
    )
    has_connections = any(line.strip() == "## Connections" for line in body)
    existing_relationships = {
        key
        for key in RELATIONSHIP_KEYS
        if any(re.match(rf"^{key}::", line) for line in body)
    }
    missing_relationships = [
        key for key in relationship_fields if key not in existing_relationships
    ]
    if any(key in present for key in RELATIONSHIP_KEYS) and has_connections:
        return Migration(text, False, "a Connections section already exists alongside YAML relationships")
    if has_connections and missing_relationships:
        fields = ", ".join(missing_relationships)
        return Migration(text, False, f"Connections section is missing expected fields: {fields}")

    has_tags = any(line.strip() == "## Tags" for line in body)
    sections: list[str] = []

    if relationship_fields and not has_connections:
        sections.extend(["## Connections", ""])
        for key in relationship_fields:
            sections.append(f"{key}:: {', '.join(values.get(key, []))}".rstrip())
        sections.append("")

    if not has_tags:
        tags = [body_tag(tag) for tag in values.get("tags", [])]
        tags = [tag for tag in tags if tag]
        sections.extend(
            [
                "## Tags",
                "",
                " ".join(tags) if tags else "<!-- Add a small number of relevant tags here. -->",
                "",
            ]
        )

    if sections:
        position = insertion_point(body)
        body[position:position] = sections

    changed = kept != frontmatter or bool(sections)
    if not changed:
        return Migration(text, False)

    migrated_lines = ["---", *kept, "---", *body]
    migrated = newline.join(migrated_lines)
    if trailing_newline:
        migrated += newline
    return Migration(migrated, True)


def markdown_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() == ".md" else []
    return sorted(
        candidate
        for candidate in path.rglob("*.md")
        if not any(part in SKIPPED_DIRECTORIES for part in candidate.relative_to(path).parts)
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Move projects, people, company, and tags from YAML into visible "
            "Obsidian/Dataview fields. The default is a dry run."
        )
    )
    parser.add_argument("path", nargs="?", default=".", help="vault, folder, or Markdown file")
    parser.add_argument("--write", action="store_true", help="write changes to disk")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.path).expanduser().resolve()
    if not target.exists():
        print(f"ERROR Path does not exist: {target}", file=sys.stderr)
        return 2

    root = target if target.is_dir() else target.parent
    changed = 0
    warnings = 0

    for note in markdown_files(target):
        original = note.read_text(encoding="utf-8")
        migration = migrate_text(original)
        display = note.relative_to(root)

        if migration.warning:
            print(f"SKIPPED {display}: {migration.warning}", file=sys.stderr)
            warnings += 1
            continue
        if not migration.changed:
            continue

        changed += 1
        if args.write:
            note.write_text(migration.text, encoding="utf-8")
            print(f"UPDATED {display}")
        else:
            print(f"WOULD UPDATE {display}")

    if changed == 0 and warnings == 0:
        print("No notes need migration.")
    elif not args.write and changed:
        print(f"Dry run: {changed} note(s) would change. Re-run with --write to apply.")

    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
