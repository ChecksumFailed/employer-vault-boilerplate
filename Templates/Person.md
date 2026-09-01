<%*
const created = tp.date.now("YYYY-MM-DD");
let sourceName = tp.file.title.replace(/^!/, "");

if (sourceName === "Untitled") {
  sourceName = await tp.system.prompt("Person name");
}

if (!sourceName) {
  throw new Error("A person name is required.");
}

const personName = sourceName
  .replace(/[_-]+/g, " ")
  .replace(/([a-z0-9])([A-Z])/g, "$1 $2")
  .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2")
  .replace(/\s+/g, " ")
  .trim();
const fileName = `!${sourceName.replace(/\s+/g, "")}`;

await tp.file.move(`/People/${fileName}`);
-%>
---
type: person
status: active
created: "<% created %>"
name: <% JSON.stringify(personName) %>
role:
email:
phone:
last-contact:
summary:
---

# <% personName %>

<!-- Keep person notes factual, respectful, and professionally useful rather than creating a personal dossier. Record work contact details only. Name person files !Name with no spaces and store them in People/. -->

## Connections

company::
projects::

## Tags

<!-- Add a small number of relevant tags here. -->

## Context

How do I know this person, and where do our responsibilities intersect?

## Responsibilities and expertise

-

## Current priorities

-

## Interactions

### <% created %>

-

## Commitments and follow-up

- [ ]

## Related notes

```dataview
TABLE type AS "Type", projects AS "Projects", summary AS "Summary", file.mtime AS "Updated"
WHERE contains(people, this.file.link)
  AND file.path != this.file.path
SORT file.mtime DESC
```
