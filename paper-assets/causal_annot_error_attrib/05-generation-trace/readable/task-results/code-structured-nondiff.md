# code structured nondiff

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_structured_nondiff_20260523T143234_result.json`
- **Structured JSON:** [`88cc1720396969df4b96.json`](../../sessions/88/88cc1720396969df4b96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three outputs generated correctly. Key results:

**Sensitivity ranking** (mean relative deviation across ε):
1. **M-bias** — 13.1% (dominant; small nondiff bias makes relative deviation large, up to 42% at ε=0.10)
2. **Collider** — 1.6%
3. **Mediation** — 1.4%
4. **Front-door** — 0.8%
5. **Exposure** — 0.6%
6. **IV** — 0.5%
7. **Confounding** — 0.4%

Counter to the initial prediction that exposure and IV would be most sensitive — they're actually quite robust. M-bias dominates because its non-differential bias is very small (~0.009), so even modest absolute perturbation from Y-dependent violation produces large relative deviation. The absolute bias changes across all topologies are small (no sign flips at any ε level), confirming that moderate violations of the non-differential assumption don't qualitatively alter the bias structure.

Produced:
- `artifacts/structured_nondiff_violation.py` — experiment script
- `artifacts/structured_nondiff_violation_results.json` — full results
- `artifacts/structured_nondiff_violation_table.tex` — LaTeX table

---
