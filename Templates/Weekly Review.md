<%*
const created = tp.date.now("YYYY-MM-DD");
await tp.file.move(`/Notes/${created} - Weekly Review`);
-%>
---
type: review
status: open
created: "<% created %>"
summary: Weekly vault review
---

# Weekly review — <% created %>

## Weekly synthesis

### Accomplishments and progress

-

### Decisions and important changes

-

### Research findings

-

### Issues, enhancements, and risks

-

### Next week's priorities

- [ ]

### Sources reviewed

- Meetings:
- Research:
- Work items:
- Decisions:

## Inbox

- [ ] Process notes in `00 Inbox`
- [ ] Attach and process any remaining Rocketbook scans

## Meetings

- [ ] Confirm every meaningful meeting has a summary
- [ ] Extract decisions
- [ ] Confirm actions have owners
- [ ] Link meetings to their projects and people

## Projects

- [ ] Review every active project hub
- [ ] Update current state where it changed
- [ ] Review next steps, risks, and open questions
- [ ] Promote important decisions into decision notes

## Research and work items

- [ ] Update the current answer and open questions in active research notes
- [ ] Review open issues, enhancements, risks, and questions
- [ ] Confirm every important work item has a status and owner
- [ ] Close resolved work items and record how they were verified

## Knowledge

- [ ] Convert reusable insights into standalone knowledge notes
- [ ] Identify general knowledge that should be rewritten and sanitized before moving to a personal vault
