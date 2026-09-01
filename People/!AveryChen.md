---
type: person
status: active
created: "2026-08-23"
name: Avery Chen
role: Platform operations lead
email: avery.chen@example.invalid
phone: "+1 202-555-0101"
last-contact: "2026-08-23"
summary: Fictional project lead for the CMDB health example.
---

# Avery Chen

## Connections

company:: [[@ExampleCompany]]
projects:: [[CMDB Health Improvement]]

## Tags

#example #cmdb

## Context

Fictional platform operations lead at [[@ExampleCompany]] and owner of [[CMDB Health Improvement]].

## Responsibilities and expertise

- Platform governance and operational reporting

## Current priorities

- Establish measurable CMDB health targets

## Interactions

### 2026-08-23

- Led [[2026-08-23 - CMDB health kickoff]].

## Commitments and follow-up

- [ ] Review the baseline duplicate-CI report.

## Related notes

```dataview
TABLE type AS "Type", projects AS "Projects", summary AS "Summary", file.mtime AS "Updated"
WHERE contains(people, this.file.link)
  AND file.path != this.file.path
SORT file.mtime DESC
```
