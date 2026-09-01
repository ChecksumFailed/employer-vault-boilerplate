---
type: person
status: active
created: "2026-08-23"
name: Morgan Hale
role: Integration engineer
email: morgan.hale@example.invalid
phone: "+1 202-555-0102"
last-contact: "2026-08-23"
summary: Fictional integration engineer for the CMDB health example.
---

# Morgan Hale

## Connections

company:: [[@ExampleCompany]]
projects:: [[CMDB Health Improvement]]

## Tags

#example #cmdb

## Context

Fictional integration engineer at [[@ExampleCompany]] working with [[!AveryChen]] on [[CMDB Health Improvement]].

## Responsibilities and expertise

- Inbound integrations and CI data analysis

## Current priorities

- Baseline duplicate CIs and assess source identifiers

## Interactions

### 2026-08-23

- Participated in [[2026-08-23 - CMDB health kickoff]].

## Commitments and follow-up

- [ ] Produce a baseline duplicate-CI report by 2026-08-28.

## Related notes

```dataview
TABLE type AS "Type", projects AS "Projects", summary AS "Summary", file.mtime AS "Updated"
WHERE contains(people, this.file.link)
  AND file.path != this.file.path
SORT file.mtime DESC
```
