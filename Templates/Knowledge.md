<%*
const created = tp.date.now("YYYY-MM-DD");
let knowledgeTitle = tp.file.title;

if (knowledgeTitle === "Untitled") {
  knowledgeTitle = await tp.system.prompt("Knowledge note title");
}

if (!knowledgeTitle) {
  throw new Error("A knowledge note title is required.");
}

await tp.file.move(`/Notes/${knowledgeTitle}`);
-%>
---
type: knowledge
status: active
created: "<% created %>"
updated: "<% created %>"
area:
summary:
---

# <% knowledgeTitle %>

<!-- Durable knowledge notes capture reusable concepts rather than raw meeting history. -->

## Connections

projects::
people::

## Tags

<!-- Add a small number of relevant tags here. -->

## Summary

Explain the concept in language that will make sense without the original context.

## Why it matters

-

## Details

-

## Example

-

## Caveats

-

## Related concepts

-
