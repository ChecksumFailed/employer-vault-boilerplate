---
type: home
status: active
created: "2026-08-23"
summary: Home page for projects, research, work items, meetings, decisions, and notes needing attention
---

# Start Here

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

- [[Note Taking System|Note-taking workflow]]
- [[Templates/Weekly Review|Weekly review template]]
- Templates: [[Templates/Project Hub|Project Hub]], [[Templates/Meeting|Meeting]], [[Templates/Research|Research]], [[Templates/Work Item|Work Item]], [[Templates/Decision|Decision]], [[Templates/Knowledge|Knowledge]], [[Templates/Note|Note]], [[Templates/Person|Person]], [[Templates/Company|Company]], [[Templates/Weekly Review|Weekly Review]]
- [[Examples/CMDB Health Improvement|Example project]]
