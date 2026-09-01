<%*
const created = tp.date.now("YYYY-MM-DD");
let researchTitle = tp.file.title;

if (researchTitle === "Untitled") {
  researchTitle = await tp.system.prompt("Research title");
}

if (!researchTitle) {
  throw new Error("A research title is required.");
}

await tp.file.move(`/Notes/${researchTitle}`);
-%>
---
type: research
status: active
created: "<% created %>"
updated: "<% created %>"
question:
summary:
---

# <% researchTitle %>

<!-- A research note preserves an active investigation. Promote stable, reusable conclusions into a Knowledge note. -->

## Connections

projects::
people::

## Tags

<!-- Add a small number of relevant tags here. -->

## Research question

What are you trying to understand or verify?

## Current understanding

Summarize the best answer supported by the evidence so far.

## Findings

-

## Evidence and sources

- Source:
  - Relevance:
  - Key evidence:

## Open questions

-

## Implications

What does this mean for the linked project, decisions, or work items?

## Related records

- Work items:
- Decisions:
