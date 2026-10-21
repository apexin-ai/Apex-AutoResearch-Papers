# ops s2ext done and profile

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s2ext-done-and-profile_20260519T174135_result.json`
- **Structured JSON:** [`f2b8b0072db8989c230e.json`](../../sessions/f2/f2b8b0072db8989c230e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No register_artifact tool available. The CSV is saved locally. Here's the complete summary:

---

## exp_001_baseline_s2_extended — DONE

**Key metrics:**

| Metric | Step | eval_return |
|--------|------|-------------|
| **Final** | 512K | 945.7 |
| **Peak** | 502K | **962.6** |
| **@505K nearest** | 502K | 962.6 |
| **@105K** | 105K | 443.5 |

**ve_ratio diagnostics:**
- **@105K**: ve_ratio = **0.7422**, value_mean = 329.16
- **Convergence zone (300K+)**: ve_ratio stabilizes around **0.69–0.75**, value_mean plateaus at ~664–666
- `civo/alert` = 0.0 throughout (no alerts triggered)

**ve_ratio profile phases:**
1. **Ramp-up (5K–65K)**: ve_ratio climbs 0→0.90 (value learning faster than policy)
2. **Correction (75K–112K)**: drops back to ~0.56–0.74 as eval_return jumps
3. **Settling (122K–200K)**: oscillates 0.56–0.86, eval_return rising to 932
4. **Converged (200K–512K)**: tight band **0.69–0.77**, eval_return stable 880–963

**tmux session**: Stopped (Ctrl-C sent, session exited cleanly).

**Artifact saved**: `artifacts/exp_001_baseline_s2_ext_ve_ratio_profile.csv` (52 data points, full CSV with ve_ratio/alert/delta_ve).

---
