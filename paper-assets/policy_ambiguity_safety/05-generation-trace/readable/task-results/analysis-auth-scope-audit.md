# analysis auth scope audit

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_auth_scope_audit_20260523T062125_result.json`
- **Structured JSON:** [`9c6c12cd153bc0814165.json`](../../sessions/9c/9c6c12cd153bc0814165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/auth_scope_audit/audit_report.md`.

**Top-line findings:**

1. **ICC≈0 is wrong** — it's a degenerate-sample artifact (9 clauses × 2 conservative models, 34/36 cells all zeros). The actual main-study ICC is **0.29** (lowest of 6 types, but far from zero). This must be corrected in the paper.

2. **κ=0.385 and 52pp variance are genuine** — auth scope is the most subjective type. Judge disagreement is systematic (not random), centered on whether "investigating" an unauthorized action counts as a violation. Human annotators show the same split.

3. **ρ=0.09 is a model-composition artifact** — the judge-group split perfectly partitions auth-scope-high vs auth-scope-low models. The paper already discloses this correctly.

4. **Clause quality is acceptable** (84% high-quality, 6% cross-type contamination) — not a primary driver of instability.

5. **The paper over-hedges.** With ICC corrected to 0.29 and the cross-judge analysis showing systematic (not random) disagreement, auth scope's variance is better explained as differential safety training + inherent construct subjectivity, not "measurement instability." The C4 interaction is likely real; the alternative measurement-artifact explanation weakens once ICC is corrected.

---
