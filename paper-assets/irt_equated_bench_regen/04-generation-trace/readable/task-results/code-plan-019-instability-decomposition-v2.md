# code plan 019 instability decomposition v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_019_instability_decomposition_v2_20260521T035329_result.json`
- **Structured JSON:** [`3f3422bb1b5c06d42b35.json`](../../sessions/3f/3f3422bb1b5c06d42b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs verified and registered. Summary of results:

**Decomposition findings:**

| | Model 1 (unadjusted) | Model 2 (with item controls) |
|---|---|---|
| Pseudo R² | 0.0007 | 0.0423 |
| Subject delta OR (per 0.10) | 1.552 (p=.001) | 0.734 (p=.030) |
| Counterfactual C% (Δ=0) | 29.0% | 33.0% |
| Reduction from domain improvement | 2.4 pp (7.6%) | −1.6 pp (reverses) |

**Key takeaways:**

1. **Domain improvement explains ≤ 2.4 pp (7.6%) of the 31.3% C rate** in the unadjusted model — negligible (pseudo R² = 0.0007).
2. **After controlling for item difficulty and discrimination, the effect reverses** (Simpson's paradox): subjects with larger accuracy deltas have *fewer* DIF C flags, because the raw correlation is confounded by item properties.
3. **Item-level characteristics dominate** DIF C prediction (pseudo R² jumps to 0.0423), confirming that instability is item-specific, not domain-driven.
4. Subject-level correlation: Pearson r = 0.338 (p = .010), but this is confounded.

**Bottom line for reviewers**: The 31.3% DIF C rate is not an artifact of domain-level capability improvement. Residual item-level instability accounts for essentially all of it.

---
