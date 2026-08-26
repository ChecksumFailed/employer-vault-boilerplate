---
type: guide
status: active
created: "2026-08-23"
summary: Setup and operating guide for the employer work-vault boilerplate
---

# Employer work-vault boilerplate

This vault is a minimal system for preserving project context, meetings, decisions, people, companies, and durable knowledge. It is designed for employer-approved storage and for processing handwritten Rocketbook notes into useful digital records.

## Organizing model

- Folders identify broad file storage locations.
- Properties describe what a note is.
- Links express relationships.
- Project hubs provide current context.
- Dataview assembles history automatically.
- Backlinks provide an additional automatic relationship view.

The folder model is deliberately shallow:

- `00 Inbox/` receives unprocessed notes.
- `Notes/` holds permanent project, meeting, decision, and knowledge notes.
- `People/` holds person notes named `!Name.md` with no spaces.
- `Companies/` holds company notes named `@Name.md` with no spaces.
- `Attachments/` holds general attachments; `Attachments/Rocketbook/` holds scans.
- `Templates/` holds native Obsidian templates.
- `Examples/` holds a removable demonstration project.

## Project hubs and child notes

A project hub is the project's landing page and lightweight README. Its current state, desired outcome, next steps, risks, open questions, key people, and immediately important decisions are manually curated. Meeting history, the complete decision list, open actions, and all related notes are generated dynamically by Dataview.

Every child note links to its hub through the YAML `projects` list. That relationship lets the hub discover child notes wherever they are stored, so the hub does not need to manually list every meeting or decision. The Markdown remains readable if Dataview is removed, while backlinks still expose many relationships.

## Create a new project

1. Create a note in `Notes/` from [[Templates/Project Hub|Project Hub]].
2. Give it a durable, recognizable project name and complete its current state and desired outcome.
3. In each related note, add the project as a quoted link in the `projects` list, for example:

   ```yaml
   projects:
     - "[[Project Name]]"
   ```

4. Add only the most important decisions to the hub's curated section; Dataview will assemble the complete history.

## Process a Rocketbook meeting

1. Put the scan in `Attachments/Rocketbook/`.
2. Create a note from [[Templates/Meeting|Meeting]], normally in `Notes/`.
3. Write the summary, then extract decisions, assigned actions, open questions, and essential context.
4. Populate `projects` and `people` with YAML lists of links. Person filenames use `!Name` without spaces.
5. Embed the scan under **Original handwritten notes**.
6. Create separate decision or knowledge notes when the content deserves a durable record.

See [[Note Taking System]] for the full workflow.

## Weekly review

Create a note from [[Templates/Weekly Review|Weekly Review]]. Process the inbox and scans, check meeting summaries and ownership, review each active project hub, and promote consequential decisions or reusable knowledge into standalone notes.

## Obsidian and Dataview setup

The included Obsidian settings send new notes to `00 Inbox`, attachments to `Attachments`, and native template insertion to `Templates`. Templates, Properties, and Backlinks are enabled as core plugins.

Dataview 0.5.68 is included and enabled in this boilerplate, with DataviewJS and inline JavaScript queries disabled. After opening the vault, go to **Settings → Community plugins** and confirm **Dataview** is enabled. If Obsidian asks first, turn off Restricted mode for this employer-approved vault.

If Dataview is ever absent, install it through **Settings → Community plugins → Browse**, search for **Dataview**, select it, choose **Install**, and then **Enable**. Do not install it from an untrusted source.

## Remove the examples

After confirming the dashboards and links work, delete the files inside `Examples/`, plus the fictional example notes in `People/` and `Companies/`. No other part of the vault depends on them.
