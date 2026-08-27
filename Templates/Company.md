<%*
const created = tp.date.now("YYYY-MM-DD");
let sourceName = tp.file.title.replace(/^@/, "");

if (sourceName === "Untitled") {
  sourceName = await tp.system.prompt("Company name");
}

if (!sourceName) {
  throw new Error("A company name is required.");
}

const companyName = sourceName
  .replace(/[_-]+/g, " ")
  .replace(/([a-z0-9])([A-Z])/g, "$1 $2")
  .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2")
  .replace(/\s+/g, " ")
  .trim();
const fileName = `@${sourceName.replace(/\s+/g, "")}`;

await tp.file.move(`/Companies/${fileName}`);
-%>
---
type: company
status: active
created: "<% created %>"
name: <% JSON.stringify(companyName) %>
summary:
---

# <% companyName %>

<!-- Name company files @Name with no spaces and store them in Companies/. Keep the note factual and limited to professionally useful context. -->

## Context

What is this organization, and how does it relate to the work?

## Relationship

-

## People

```dataview
TABLE WITHOUT ID file.link AS "Person", role AS "Role", last-contact AS "Last Contact", summary AS "Summary"
WHERE type = "person"
  AND company = this.file.link
SORT file.name ASC
```

## Current work

-

## Important context

-

## Related projects

-
