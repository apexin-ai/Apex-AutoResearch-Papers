# code e2e real cm demo

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2e_real_cm_demo_20260523T202030_result.json`
- **Structured JSON:** [`c86b0fe5d0b0f5c8c7d6.json`](../../sessions/c8/c86b0fe5d0b0f5c8c7d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass:

1. **No errors** — script runs in 21.6s
2. **Exposure topology**: PPI++ reduces bias from -59% to -74% (naive) down to ±0.5% (corrected), median improvement **+93.7%**
3. **Confounding topology**: plug-in correction improvement is **≈0%** across all 10 configs (FWL invariance confirmed — naive and corrected bias are identical to machine precision)
4. **JSON and LaTeX outputs are consistent**

Files created:
- `artifacts/e2e_real_cm_demo.py` — the script
- `artifacts/e2e_real_cm_results.json` — full results with metadata
- `artifacts/e2e_real_cm_table.tex` — LaTeX table for appendix

---
