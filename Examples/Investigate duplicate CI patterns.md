---
type: research
status: active
created: "2026-08-23"
updated: "2026-08-23"
question: Which sources and identifier patterns account for most duplicate configuration items?
summary: Initial evidence suggests unstable source identifiers are a likely contributor, but a source-by-source baseline is still needed.
---

# Investigate duplicate CI patterns

## Connections

projects:: [[CMDB Health Improvement]]
people:: [[!MorganHale]]

## Tags

#example #cmdb #research

## Research question

Which sources and identifier patterns account for most duplicate configuration items?

## Current understanding

Unstable or inconsistently populated source identifiers are a plausible cause. The project still needs a measured baseline grouped by source and CI class before selecting remediation work.

## Findings

- The kickoff identified source identifiers as a risk requiring investigation.
- Duplicate rates need to be compared by source and CI class.

## Evidence and sources

- Source: [[2026-08-23 - CMDB health kickoff]]
  - Relevance: Established the baseline-first approach.
  - Key evidence: Historical sources may use inconsistent identifiers.

## Open questions

- Which sources produce the highest duplicate rate?
- Are identifiers unstable, missing, or transformed between runs?

## Implications

The findings will determine which identification rules or source mappings need remediation and will provide evidence for [[Stabilize source identifiers]].

## Related records

- Work items: [[Stabilize source identifiers]]
- Decisions: [[Use IRE for inbound CI updates]]
