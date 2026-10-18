# run exp 002

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp-002_20260520T202812_result.json`
- **Structured JSON:** [`876eaceff50a072018fd.json`](../../sessions/87/876eaceff50a072018fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full run completed successfully. Total runtime: ~24 minutes (K=2 grid: 1356s, K=4 grid: 105s).

## Final Summary

| Metric | Value |
|--------|-------|
| **K=2 R²** | 0.9938 |
| **K=4 R²** | 0.9738 |
| **K=2 tightness** (median) | 1.003 |
| **K=4 tightness** (median) | 1.023 |
| **Coverage (2 SE)** | K=2: 95.1%, K=4: 94.0% |
| **"Debiasing hurts" fraction** | 260/520 = **50.0%** |
| **Debiasing hurts threshold** | Δ_misclass > **0.1235** |
| **K=4 subgroups affected** | 1/4 (subgroup with π=0.05, ratio=2.41) |

Key takeaways:
- The analytic bias identity `bias = δ_s · Δτ / (1 - 2π̄)` is **exact** — confirmed by R² > 0.97 and ~95% coverage at 2 SE for both K=2 and K=4
- Debiasing hurts subgroup B (lower misclassification) whenever Δ_misclass > 0.1235, **independent of Δτ magnitude**
- The formula generalizes cleanly from K=2 to K=4 with no modification needed

---
