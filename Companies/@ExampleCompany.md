---
type: company
status: active
created: "2026-08-23"
name: Example Company
summary: Placeholder organization used only by the demonstration notes.
---

# Example Company

## Context

Example Company is a fictional placeholder organization created solely for this boilerplate's example notes.

## Relationship

- Demonstrates how an employer or other organization can be linked without mixing company notes into people or project folders.

## People

```dataview
TABLE WITHOUT ID file.link AS "Person", role AS "Role", last-contact AS "Last Contact", summary AS "Summary"
WHERE type = "person"
  AND company = this.file.link
SORT file.name ASC
```

## Current work

- [[CMDB Health Improvement]]

## Important context

- This record contains no real company or customer information.

## Related projects

- [[CMDB Health Improvement]]
