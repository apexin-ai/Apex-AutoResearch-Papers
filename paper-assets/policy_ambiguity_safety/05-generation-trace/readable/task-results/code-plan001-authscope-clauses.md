# code plan001 authscope clauses

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001_authscope_clauses_20260520T113056_result.json`
- **Structured JSON:** [`9c23b49ab8454fba23ce.json`](../../sessions/9c/9c23b49ab8454fba23ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Validation passed. 50 `authorization_scope` clauses written to `/tmp/clauses_authscope.json`.

**Distribution:**
- 26 retail / 24 airline
- 15 role permission boundary (auth_001–015)
- 10 tool/action authorization (auth_016–025)
- 15 conditional permission (auth_026–040)
- 10 delegation/inheritance (auth_041–050)

Each entry has the full schema: matched ambiguous/unambiguous clauses, user scenario, tool definitions (stripped + full), 3+ tool responses with args patterns, ambiguity point, 2+ interpretations (broad vs narrow), expected behavior diff, and annotation rationale.

---
