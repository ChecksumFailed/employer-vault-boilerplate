---
type: knowledge
status: active
created: "2026-08-23"
updated: "2026-08-23"
area: Configuration management
projects:
  - "[[CMDB Health Improvement]]"
people: []
summary: IRE centralizes CI identification and reconciliation for supported inbound updates.
---

# ServiceNow IRE

## Summary

The Identification and Reconciliation Engine (IRE) is the platform mechanism used to identify the intended configuration item and control how inbound data may update it. This explanation is reusable technical context; project-specific choices and history remain in meeting and decision notes.

## Why it matters

- Consistent identification helps prevent duplicate CIs.
- Reconciliation rules help control which sources may update attributes.

## Details

- Identification rules determine whether a payload matches an existing CI.
- Reconciliation behavior governs source authority for updates.
- Integration teams still need stable identifiers, representative tests, and operational monitoring.

## Example

An inbound source submits a server payload. IRE evaluates identification data to locate the intended CI, then applies reconciliation controls before accepted attributes are updated.

## Caveats

- Exact behavior depends on configured identification rules, data-source settings, class, and platform release.
- Consult approved platform documentation and the current instance configuration before implementation.

## Related concepts

- [[Use IRE for inbound CI updates]]
- [[CMDB Health Improvement]]
