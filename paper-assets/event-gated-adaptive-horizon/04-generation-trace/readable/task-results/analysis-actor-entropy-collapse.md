# analysis actor entropy collapse

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_actor_entropy_collapse_20260515T144837_result.json`
- **Structured JSON:** [`a6f880b92348a5cd165f.json`](../../sessions/a6/a6f880b92348a5cd165f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report updated at `artifacts/analysis_actor_entropy_plan031.md`.

**Summary of findings:**

| Signal | Collapse diagnostic? |
|---|---|
| Actor entropy absolute value | No — distributions overlap completely |
| Entropy convergence speed | No — exp_008c (collapsed) converges fastest of all |
| Entropy uptick at collapse | Weak — only fixed_dt2 shows +0.05 at 65K |
| **V/E ratio > 1.0** | **Yes — cleanly separates groups** |

**Conclusions:**
- Actor entropy **cannot** serve as an early warning signal. Both groups follow the same 8.1→-5.x descent; within-group variance exceeds between-group difference.
- The strongest collapse predictor remains the **value/eval ratio** crossing 1.0 (critic overestimation). exp_008d hits V/E=1.67 at 55K, fixed_dt2 hits 2.72 at 65K; all healthy configs stay below 0.6.
- Refined claim for the paper: delusional critic **delays** entropy convergence in some cases (008d vs 008c: 3-nat gap at 25K) but this is a secondary effect, not diagnostic.

---
