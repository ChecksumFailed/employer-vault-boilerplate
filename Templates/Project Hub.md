---
type: project
status: active
created: "{{date}}"
area:
owner:
review-date:
summary:
---

# {{title}}

<!-- Current state, risks, next steps, and important decisions are manually curated. Meeting history and the complete decision list are dynamic. Keep this hub a concise dashboard, not a dumping ground. -->

## Current state

Write a short description of where the project stands now.

## Desired outcome

What does success look like?

## Next steps

- [ ]

## Risks

-

## Open questions

-

## Key people

-

## Important decisions

Manually link only the decisions someone should notice immediately.

## Open actions

```dataview
TASK
WHERE contains(projects, this.file.link)
  AND !completed
```

## Recent meetings

```dataview
TABLE date AS "Date", summary AS "Summary"
WHERE contains(projects, this.file.link)
  AND type = "meeting"
SORT date DESC
```

## All decisions

```dataview
TABLE date AS "Date", status AS "Status", summary AS "Summary"
WHERE contains(projects, this.file.link)
  AND type = "decision"
SORT date DESC
```

## All related notes

```dataview
TABLE type AS "Type", summary AS "Summary", file.mtime AS "Updated"
WHERE contains(projects, this.file.link)
  AND file.path != this.file.path
SORT file.mtime DESC
```
