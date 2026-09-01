---
type: work-item
kind: issue
status: open
created: "2026-08-23"
updated: "2026-08-23"
priority: high
owner: "[[!MorganHale]]"
summary: Determine whether unstable source identifiers are creating duplicate CIs and correct the responsible mappings.
---

# Stabilize source identifiers

## Connections

projects:: [[CMDB Health Improvement]]
people:: [[!MorganHale]]

## Tags

#example #cmdb

## Description

Historical inbound sources may provide missing or inconsistent identifiers, which can prevent reliable CI matching.

## Impact

Unreliable identification can create duplicate CIs and make data-quality trends difficult to interpret.

## Evidence

- [[2026-08-23 - CMDB health kickoff]] identified inconsistent historical identifiers as a risk.
- [[Investigate duplicate CI patterns]] is collecting the source-by-source evidence.

## Desired outcome

Every in-scope source provides a stable identifier that is covered by representative identification tests.

## Investigation and discussion

- Compare duplicate rates by source and CI class.
- Trace the identifier from source payload through transformation and ingestion.

## Resolution

Open.

## Related records

- Research: [[Investigate duplicate CI patterns]]
- Decisions: [[Use IRE for inbound CI updates]]
