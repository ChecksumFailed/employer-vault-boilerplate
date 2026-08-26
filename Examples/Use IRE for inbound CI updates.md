---
type: decision
status: accepted
created: "2026-08-23"
date: "2026-08-23"
projects:
  - "[[CMDB Health Improvement]]"
people:
  - "[[!AveryChen]]"
  - "[[!MorganHale]]"
summary: Route inbound CI updates through IRE instead of writing directly to CMDB tables.
---

# Use IRE for inbound CI updates

## Context

Multiple fictional integrations update configuration items. Direct writes can bypass identification and reconciliation behavior, creating duplicates or allowing a lower-authority source to overwrite trusted data.

## Decision

Route inbound CI payloads through the supported IRE path and define stable source identifiers and reconciliation rules before rollout.

## Alternatives considered

- Direct table writes
  - Advantages: Simple integration logic and low initial effort.
  - Disadvantages: Bypasses centralized identification and reconciliation controls.
- Custom matching in every integration
  - Advantages: Each source can optimize its own behavior.
  - Disadvantages: Duplicates logic and makes outcomes difficult to govern consistently.

## Rationale

A shared identification and reconciliation path makes update behavior explainable, testable, and consistent across sources while keeping data-source precedence in one governed model.

## Consequences

Integrations need suitable source identifiers and test coverage for identification rules. Initial implementation takes more effort, but duplicate prevention and overwrite behavior become easier to inspect and improve.

## Revisit when

Reconsider if a supported inbound mechanism cannot express a verified business requirement, or if platform guidance materially changes.

## Sources

- Meeting: [[2026-08-23 - CMDB health kickoff]]
- Supporting material: [[ServiceNow IRE]]
