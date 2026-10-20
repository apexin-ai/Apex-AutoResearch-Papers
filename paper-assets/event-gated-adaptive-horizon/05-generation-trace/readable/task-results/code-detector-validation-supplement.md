# code detector validation supplement

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_detector-validation-supplement_20260517T052707_result.json`
- **Structured JSON:** [`ecd009c88f45b91903ce.json`](../../sessions/ec/ecd009c88f45b91903ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All parts complete. Summary:

**Part 1 - Negative cases results:**
| Experiment | Verdict | Notes |
|---|---|---|
| exp_009b_008d_walker_s2 | TN | Self-correcting dt_emb. ve_ratio peaks 0.57 then declines. Correct silence. |
| exp_009a_baseline_walker_s2 | FP | Temporary dip at 85K triggers detector, but model recovers to 966. |
| baseline_s1 | TN | 505K healthy run. Max ve=0.73, no trigger. |
| exp_009d_baseline_walker_s0 | TN | Transient spike (ve=2.73) from single bad eval episode, no trigger. |
| exp_009d_baseline_walker_s1 | TN | Clean 115K run. Max ve=0.72, no trigger. |
| exp_020_vanilla_dreamerv3_s2 | Excluded | Duplicate of exp_009a (identical first 105K). |

**Part 2 - Detection types assigned:**
- 3 predictive (2 TP + 1 FP), 2 reactive (1 TP + 1 FP)

**Part 3 - JSON updated** at `artifacts/analysis/detector_formal_validation_v3.json`

**Part 4 - Script written** at `artifacts/scripts/generate_detector_table.py`, outputs both LaTeX and Markdown.

**Final metrics: TPR=1.00, FPR=0.286 (2/7)**. The primary FP weakness is a temporary 3-checkpoint eval dip in one baseline run (exp_009a) that the detector cannot distinguish from sustained collapse within its observation window.

---
