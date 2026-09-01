---
type: home
status: active
created: "2026-08-23"
summary: Home page for projects, research, work items, meetings, decisions, and notes needing attention
---

# Start Here

## Create a note

- **Capture now, classify later:** press `Ctrl+N`. The note is created in `00 Inbox/`.
- **Known note type:** open the Command Palette with `Ctrl+P`, then run the matching **Templater: Create …** command, such as **Create Meeting**, **Create Research**, or **Create Work Item**.
- **Choose from every template:** run **Templater: Create new note from template**.

Each typed template asks for any required information, applies the correct properties and naming convention, and moves the note to its durable folder. Assign hotkeys to the per-type **Templater: Create …** commands under **Settings → Hotkeys** if you create some types frequently.

Common choices:

| When you need to… | Create… |
|---|---|
| Record a time-bound interaction | Meeting |
| Establish a project landing page | Project Hub |
| Investigate a question with evidence and uncertainty | Research |
| Track an issue, enhancement, risk, or question independently | Work Item |
| Preserve a consequential choice and its reasoning | Decision |
| Explain a stable, reusable conclusion | Knowledge |
| Preserve useful context that fits no more specific type | Note |

See [[Note Taking System]] for the capture, processing, and review workflow.

## Active projects

```dataview
TABLE status AS "Status", area AS "Area", owner AS "Owner", review-date AS "Next Review", summary AS "Summary"
WHERE type = "project"
  AND status = "active"
SORT file.name ASC
```

## Open work items

```dataview
TABLE kind AS "Kind", projects AS "Projects", priority AS "Priority", owner AS "Owner", status AS "Status", summary AS "Summary"
WHERE type = "work-item"
  AND status != "resolved"
  AND status != "closed"
SORT priority ASC, file.name ASC
```

## Active research

```dataview
TABLE projects AS "Projects", question AS "Question", status AS "Status", summary AS "Current Answer"
WHERE type = "research"
  AND status != "complete"
  AND status != "closed"
SORT file.mtime DESC
```

## Recent meetings

```dataview
TABLE date AS "Date", projects AS "Projects", summary AS "Summary"
WHERE type = "meeting"
SORT date DESC
LIMIT 10
```

## Recent decisions

```dataview
TABLE date AS "Date", projects AS "Projects", status AS "Status", summary AS "Summary"
WHERE type = "decision"
SORT date DESC
LIMIT 10
```

## Notes needing processing

```dataview
TABLE type AS "Type", file.ctime AS "Created"
WHERE status = "unprocessed"
SORT file.ctime ASC
```

## Quick links

- [[README|Vault setup and overview]]
- [[CONTEXT|Domain glossary]]
- [[Note Taking System|Capture, processing, and review workflow]]
- [[Templates/Weekly Review|Weekly review template]]
- Templates: [[Templates/Project Hub|Project Hub]], [[Templates/Meeting|Meeting]], [[Templates/Research|Research]], [[Templates/Work Item|Work Item]], [[Templates/Decision|Decision]], [[Templates/Knowledge|Knowledge]], [[Templates/Note|Note]], [[Templates/Person|Person]], [[Templates/Company|Company]], [[Templates/Weekly Review|Weekly Review]]
- [[Examples/CMDB Health Improvement|Example project]]
