<%*
const created = tp.date.now("YYYY-MM-DD");
let workItemTitle = tp.file.title;

if (workItemTitle === "Untitled") {
  workItemTitle = await tp.system.prompt("Work item title");
}

if (!workItemTitle) {
  throw new Error("A work item title is required.");
}

const workItemKind = await tp.system.suggester(
  ["Issue", "Enhancement", "Risk", "Question"],
  ["issue", "enhancement", "risk", "question"],
  false,
  "Work item kind"
);

if (!workItemKind) {
  throw new Error("A work item kind is required.");
}

await tp.file.move(`/Notes/${workItemTitle}`);
-%>
---
type: work-item
kind: "<% workItemKind %>"
status: open
created: "<% created %>"
updated: "<% created %>"
priority:
owner:
summary:
---

# <% workItemTitle %>

<!-- Use kind: issue, enhancement, risk, or question. Create a standalone work item when it needs its own owner, status, investigation, or history. -->

## Connections

projects::
people::

## Tags

<!-- Add a small number of relevant tags here. -->

## Description

What needs attention?

## Impact

Who or what is affected, and how significant is it?

## Evidence

-

## Desired outcome

What would make this work item complete?

## Investigation and discussion

-

## Resolution

Record what changed, why, and how it was verified.

## Related records

- Research:
- Decisions:
