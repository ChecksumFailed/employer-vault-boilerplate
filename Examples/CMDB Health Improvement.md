---
type: project
status: active
created: "2026-08-23"
area: Platform operations
owner: "[[!AveryChen]]"
review-date: "2026-09-04"
summary: Improve CI data quality and make inbound update behavior measurable.
---

# CMDB Health Improvement

<!-- Current state, risks, next steps, and important decisions are manually curated. Meeting history and the complete decision list are dynamic. Keep this hub a concise dashboard, not a dumping ground. -->

## Current state

The fictional platform team has agreed on the inbound update pattern and is defining a baseline for duplicate and stale configuration items before changing integrations.

## Desired outcome

Inbound CI updates are reconciled consistently, data-quality trends are visible, and ownership exists for exceptions.

## Next steps

- [ ] [[!MorganHale]] — produce a baseline duplicate-CI report by 2026-08-28.

## Risks

- Existing source identifiers may not be stable enough for reliable reconciliation.

## Open questions

- Which CI classes need class-specific health thresholds?

## Key people

- [[!AveryChen]] — project lead
- [[!MorganHale]] — integration engineer

## Important decisions

- [[Use IRE for inbound CI updates]]

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
