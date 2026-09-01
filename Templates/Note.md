<%*
const created = tp.date.now("YYYY-MM-DD");
let noteTitle = tp.file.title;

if (noteTitle === "Untitled") {
  noteTitle = await tp.system.prompt("Note title");
}

if (!noteTitle) {
  throw new Error("A note title is required.");
}

await tp.file.move(`/Notes/${noteTitle}`);
-%>
---
type: note
status: active
created: "<% created %>"
updated: "<% created %>"
summary:
---

# <% noteTitle %>

<!-- Use this lightweight template for useful project context that is not a meeting, research investigation, decision, work item, or durable knowledge note. -->

## Connections

projects::
people::

## Tags

<!-- Add a small number of relevant tags here. -->

## Summary

-

## Notes

-
