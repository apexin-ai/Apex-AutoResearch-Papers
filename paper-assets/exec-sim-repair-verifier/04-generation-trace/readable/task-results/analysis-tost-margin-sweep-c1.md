# analysis tost margin sweep c1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-margin-sweep-c1_20260519T084746_result.json`
- **Structured JSON:** [`99946f78fc1211e5670a.json`](../../sessions/99/99946f78fc1211e5670a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All deliverables complete. Here's the summary:

**Results: TOST Margin Sweep (CLS vs TRAJ, paired t-test, 5 seeds)**

| Margin (pp) | TOST p | Equivalent? |
|---|---|---|
| ±0.5 | 0.490 | no |
| ±1.0 | 0.200 | no |
| ±1.5 | 0.068 | no |
| **±2.0** | **0.025** | **YES** |
| ±2.5 | 0.010 | YES |
| ±3.0 | 0.005 | YES |
| ±4.0 | 0.001 | YES |
| ±5.0 | 0.001 | YES |

**Key statistics:**
- Mean gap (CLS − TRAJ): **−0.486 pp** (5-seed simple mean; paper pooled = −0.45)
- SD: 1.219 pp, SE: 0.545 pp, df = 4
- Smallest equivalence margin: **±1.648 pp**
- Monotonicity: verified

**Paper vs. independent recomputation:**
- Paper: p = 0.007 at ±2pp (clustered bootstrap, 523 variants, 114 clusters)
- Paired t-test: p = 0.025 at ±2pp (5 seed-level observations, df=4)
- Both methods agree: **equivalent at ±2pp** (α=0.05)
- Discrepancy is purely methodological: clustered bootstrap has more power than df=4 paired t-test because it uses per-variant data within seeds

**Files produced (remote):**
- `/home/sonny/exec-sim-repair-verifier/tost_margin_sweep.py`
- `/home/sonny/exec-sim-repair-verifier/tost_margin_sweep_cls_traj.json`

---
