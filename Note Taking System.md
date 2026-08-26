---
type: guide
status: active
created: "2026-08-23"
summary: Workflow for turning raw captures, meetings, research, and project concerns into durable work records
---

# Note Taking System

This is a practical work-note workflow. Folders provide broad storage, properties identify note types, links record relationships, and project hubs show current context. Meetings live in `Meetings/`; project hubs live in `Projects/`; research, work items, decisions, knowledge, and general notes live in `Notes/`. People live in `People/` with filenames such as `!ExamplePerson.md`; companies live in `Companies/` with filenames such as `@ExampleCompany.md`.

## Capture and classify

Use `Ctrl+N` for fast, unstructured capture. The note lands in `00 Inbox/`. During processing, rename it, apply the appropriate properties and structure, link its project and people, and move it to its durable folder.

Use **QuickAdd: New Work Note** when you already know the note type. QuickAdd creates the note from the correct template in the correct folder. The inbox is a temporary queue, not permanent storage.

Choose the durable type by what the record represents:

- Meeting: a time-bound interaction.
- Research: an active investigation with evidence and uncertainty.
- Work item: an issue, enhancement, risk, or question needing independent tracking.
- Decision: a consequential choice and its reasoning.
- Knowledge: a stable explanation reusable outside the original project event or investigation.
- Note: useful project context that does not fit another type.

## During a meeting

Use margin markers in handwritten notes:

- `D` — decision
- `A` — action
- `Q` — unresolved question
- `!` — important context or insight

Capture exact names, dates, numbers, and terminology; decisions and who made them; why decisions were made; commitments and owners; disagreements; open questions; constraints; and systems, documents, and links mentioned. Do not attempt a verbatim transcript.

## Within 24 hours

Preferably immediately after the meeting:

1. Scan the Rocketbook pages.
2. Create or update the digital meeting note.
3. Write a two- or three-sentence summary.
4. Extract decisions.
5. Extract actions and owners.
6. Record unresolved questions.
7. Link the project and people.
8. Create standalone decision notes for consequential decisions.
9. Create standalone knowledge notes for reusable insights.
10. Retain the scan as supporting source material.

OCR is a drafting aid, not the finished note. Edit the result until it preserves the meaning, reasoning, ownership, and next investigative path.

## During research

1. Create a [[Templates/Research|Research]] note and link its project.
2. State the question before collecting material.
3. Record the current best answer separately from raw findings.
4. Capture source links and explain why each source matters.
5. Track uncertainty and open questions explicitly.
6. Create a [[Templates/Work Item|Work Item]] when a finding becomes an issue, enhancement, risk, or question requiring independent tracking.
7. Create a [[Templates/Decision|Decision]] when the project makes a consequential choice.
8. Promote stable, reusable conclusions into [[Templates/Knowledge|Knowledge]].

Research is evidence and reasoning in progress. Knowledge is the synthesized result. Preserve the distinction so a future reader can tell what is established, what remains uncertain, and why the project acted.

## Track work items

Use one `work-item` type with a `kind` of `issue`, `enhancement`, `risk`, or `question`. Create a standalone work item only when it needs its own owner, status, investigation, discussion, or history. Keep small tasks as checkboxes in the relevant project, meeting, research, or work-item note.

Resolve a work item by recording the outcome and how it was verified, then set its status to `resolved` or `closed`. Do not delete the record; its history may explain later decisions or behavior.

## The one-year test

Before considering a note processed, ask:

> If I knew nothing except what is written here, could I understand what happened, why it mattered, what changed, who was involved, and where to investigate next?

## Work and personal separation

This is an employer-specific work vault. Store meetings, internal projects, coworkers, decisions, and employer-specific architecture here. Use only employer-approved synchronization and storage. Do not sync it through personal Obsidian Sync, personal cloud storage, or personal Nextcloud unless expressly approved.

Important general knowledge should be independently rewritten and sanitized before being promoted from this work vault into a personal knowledge vault. Remove employer and customer identifiers, confidential architecture, internal links, data, and meeting history.
