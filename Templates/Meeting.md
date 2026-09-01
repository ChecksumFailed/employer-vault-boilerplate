<%*
const created = tp.date.now("YYYY-MM-DD");
const datePrefix = `${created} - `;
let meetingTitle = tp.file.title.startsWith(datePrefix)
  ? tp.file.title.slice(datePrefix.length)
  : tp.file.title;

if (meetingTitle === "Untitled") {
  meetingTitle = await tp.system.prompt("Meeting title");
}

if (!meetingTitle) {
  throw new Error("A meeting title is required.");
}

await tp.file.move(`/Meetings/${datePrefix}${meetingTitle}`);
-%>
---
type: meeting
status: processed
created: "<% created %>"
date: "<% created %>"
summary:
---

# <% meetingTitle %>

<!-- The Rocketbook scan is source material, not the finished digital note. Process it into the sections below. -->

## Connections

projects::
people::

## Tags

<!-- Add a small number of relevant tags here. -->

## Summary

In two or three sentences, explain why the meeting happened and what changed.

## Decisions

-

## Actions

- [ ]

## Open questions

-

## Important context

Capture reasoning, constraints, exact numbers, terminology, and details that future readers will need.

## Discussion

Keep only details that support the summary, decisions, actions, or open questions.

## Related material

- Systems or concepts:

## Original handwritten notes

Attach or embed the Rocketbook scan here:

![[ ]]
