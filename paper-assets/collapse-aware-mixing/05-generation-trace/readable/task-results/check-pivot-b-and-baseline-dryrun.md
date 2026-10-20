# check pivot b and baseline dryrun

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pivot_b_and_baseline_dryrun_20260513T201436_result.json`
- **Structured JSON:** [`652f548d8413ea66a4f3.json`](../../sessions/65/652f548d8413ea66a4f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== PIVOT B STATUS ===
Process: DONE (no PID, no tmux session)
GPU: 0% utilization, 0 MiB / 97887 MiB (idle)
Progress: Completed all 3 generations (G0–G2)
Results:
  generated_vs_holdout_eff_rank:
    G0: holdout=111.51  generated=63.89  delta=47.62
    G1: holdout=111.39  generated=3.87   delta=107.52  (↓93.9%)
    G2: holdout=111.86  generated=1.06   delta=110.79  (↓98.3%)
  Verdict: PIVOT_B_LOSES — n-gram metrics (entropy, vocab coverage) detect collapse earlier than generated eff_rank
    - n-gram detection at G1 step 152 (unigram entropy -43.5%)
    - generated eff_rank detection at G1 step 999999 (-93.9%)
  Holdout eff_rank stays stable across all generations (~111.5)
  Note: pivot_b_verification.log shows a ConnectionError fetching 'wikitext' (EXIT_CODE=1), but analysis outputs were saved successfully

=== BASELINE DRY-RUN ===
Scripts: 6/6 exist and executable
controlled_pipeline.py: import OK, argparse OK (supports --Kp --Ki --w_init --w_min --w_max --r_target etc.)

Per-script params:
| Script                    | Kp | Ki | w_init | w_min | w_max |
|---------------------------|----|----|--------|-------|-------|
| launch_baseline_w0_p0.sh  | 0  | 0  | 0.0    | 0.0   | 0.0   |
| launch_baseline_w01_p0.sh | 0  | 0  | 0.1    | 0.1   | 0.1   |
| launch_baseline_w03_p0.sh | 0  | 0  | 0.3    | 0.3   | 0.3   |
| launch_baseline_w05_p0.sh | 0  | 0  | 0.5    | 0.5   | 0.5   |
| launch_baseline_w07_p0.sh | 0  | 0  | 0.7    | 0.7   | 0.7   |
| launch_baseline_w1_p0.sh  | 0  | 0  | 1.0    | 1.0   | 1.0   |

All 6 baselines are static-weight (Kp=Ki=0, w_init=w_min=w_max), covering w ∈ {0.0, 0.1, 0.3, 0.5, 0.7, 1.0}. Ready to launch.

---
