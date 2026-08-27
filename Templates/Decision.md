<%*
const created = tp.date.now("YYYY-MM-DD");
const datePrefix = `${created} - `;
let decisionTitle = tp.file.title.startsWith(datePrefix)
  ? tp.file.title.slice(datePrefix.length)
  : tp.file.title;

if (decisionTitle === "Untitled") {
  decisionTitle = await tp.system.prompt("Decision title");
}

if (!decisionTitle) {
  throw new Error("A decision title is required.");
}

await tp.file.move(`/Notes/${datePrefix}${decisionTitle}`);
-%>
---
type: decision
status: accepted
created: "<% created %>"
date: "<% created %>"
projects: []
people: []
summary:
---

# <% decisionTitle %>

<!-- Record enough architectural reasoning to make the decision understandable a year later, not merely the selected option. -->

## Context

What situation or problem required a decision?

## Decision

What was decided?

## Alternatives considered

- Option:
  - Advantages:
  - Disadvantages:

## Rationale

Why was this option selected?

## Consequences

What becomes easier, harder, possible, or constrained?

## Revisit when

What condition should cause this decision to be reconsidered?

## Sources

- Meeting:
- Supporting material:
