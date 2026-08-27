---
type: guide
status: active
created: "2026-08-23"
summary: Setup and operating guide for the employer work-vault boilerplate
---

# Employer work-vault boilerplate

This vault is a minimal system for preserving project context, meetings, research, work items, decisions, people, companies, and durable knowledge. It is designed for employer-approved storage and for turning raw work material, including handwritten Rocketbook notes, into useful digital records.

## Organizing model

- Folders identify broad file storage locations.
- Properties describe what a note is.
- Links express relationships.
- Project hubs provide current context.
- Dataview assembles history automatically.
- Backlinks provide an additional automatic relationship view.

The folder model is deliberately shallow:

- `00 Inbox/` receives unprocessed notes.
- `Meetings/` holds dated meeting records.
- `Projects/` holds project hubs.
- `Notes/` holds research, work items, decisions, knowledge, and general project notes.
- `People/` holds person notes named `!Name.md` with no spaces.
- `Companies/` holds company notes named `@Name.md` with no spaces.
- `Attachments/` holds general attachments; `Attachments/Rocketbook/` holds scans.
- `Templates/` holds Templater templates that apply properties, naming conventions, and destination folders.
- `Examples/` holds a removable demonstration project.

The durable note types have distinct jobs:

- A `meeting` records a time-bound interaction.
- `research` preserves an active investigation, evidence, sources, and uncertainty.
- A `work-item` is an issue, enhancement, risk, or question that needs independent ownership, status, investigation, or history.
- A `decision` explains a consequential choice and its rationale.
- `knowledge` is a stable, reusable conclusion rather than raw research history.
- A general `note` holds useful project context that does not fit another durable type.

Person notes store a company link, role, work email, work phone, last-contact date, and a concise professional summary. Keep them factual and limited to employer-approved, professionally useful information.

## Project hubs and child notes

A project hub is the project's landing page and lightweight README. Its current state, desired outcome, next steps, risks, open questions, key people, and immediately important decisions are manually curated. Meetings, active research, open work items, the complete decision list, open actions, and all related notes are generated dynamically by Dataview.

Every child note links to its hub through the YAML `projects` list. That relationship lets the hub discover child notes wherever they are stored, so the hub does not need to manually list every meeting or decision. The Markdown remains readable if Dataview is removed, while backlinks still expose many relationships.

## Create a new project

1. Run **Templater: Create new note from template**, choose [[Templates/Project Hub|Project Hub]], and enter the project name.
2. Give it a durable, recognizable project name and complete its current state and desired outcome.
3. In each related note, add the project as a quoted link in the `projects` list, for example:

   ```yaml
   projects:
     - "[[Project Name]]"
   ```

4. Add only the most important decisions to the hub's curated section; Dataview will assemble the complete history, research, work items, meetings, and actions.

## Research and work items

Use [[Templates/Research|Research]] for an active investigation. Record the question, current understanding, findings, evidence, sources, open questions, and project implications. When a conclusion becomes stable and reusable outside the investigation, promote it into [[Templates/Knowledge|Knowledge]].

Use [[Templates/Work Item|Work Item]] when an issue, enhancement, risk, or question needs its own owner, status, investigation, discussion, or history. Keep small tasks directly in the project hub or another child note. Every research and work-item note should link its project through the `projects` property.

## Process a Rocketbook meeting

1. Put the scan in `Attachments/Rocketbook/`.
2. Run **Templater: Create new note from template** and choose **Meeting** to create a dated note in `Meetings/`.
3. Write the summary, then extract decisions, assigned actions, open questions, and essential context.
4. Populate `projects` and `people` with YAML lists of links. Person filenames use `!Name` without spaces.
5. Embed the scan under **Original handwritten notes**.
6. Create separate decision or knowledge notes when the content deserves a durable record.

See [[Note Taking System]] for the full workflow.

## Weekly review

Run **Templater: Create new note from template** and choose [[Templates/Weekly Review|Weekly Review]]. Process the inbox and scans, check meeting summaries and ownership, review each active project hub, and promote consequential decisions or reusable knowledge into standalone notes.

## Obsidian, Dataview, and Templater setup

The included Obsidian settings send unstructured new notes to `00 Inbox` and attachments to `Attachments`. File Explorer, Search, Command Palette, Bookmarks, Properties, and Backlinks are enabled as core plugins.

The vault declares Dataview and Templater as enabled community plugins, but their executable plugin files are not stored in Git. After opening the vault, install both from **Settings → Community plugins → Browse** if they are absent, then enable them. If Obsidian asks first, turn off Restricted mode only for an employer-approved vault.

The tracked Dataview configuration disables DataviewJS and inline JavaScript queries. The tracked Templater configuration uses `Templates/` and includes filename rules for missing person and company links. Templater intentionally stores its **Trigger Templater on new file creation** switch on each device rather than in the vault, so enable that switch once under **Settings → Templater → File creation** on every device. Leave **Template matching mode** set to **File regex templates**.

To create a known note type, run **Templater: Create new note from template**, choose the template, and enter its title. The template applies the naming convention and moves the note to its durable folder. Optionally assign that command a hotkey under **Settings → Hotkeys**. Plain `Ctrl+N` remains the fast path for an unprocessed note in `00 Inbox/`.

Missing people and companies can be created directly from links. Write a person link such as `[[!MorganHale|Morgan Hale]]` or a company link such as `[[@ExampleCompany|Example Company]]`. When you follow an unresolved link, Obsidian creates it in `00 Inbox/`; Templater recognizes the prefix, fills the appropriate template, and moves the note to `People/` or `Companies/`. Person and company display names are inferred from PascalCase, underscores, or hyphens in the link target. Link each person to their company using the `company` property; the company note then lists those people automatically with Dataview.

Do not install community plugins from an untrusted source. Community plugins can access vault contents; confirm their use is allowed by employer policy.

## Remove the examples

After confirming the dashboards and links work, delete the files inside `Examples/`, plus the fictional example notes in `People/` and `Companies/`. No other part of the vault depends on them.
