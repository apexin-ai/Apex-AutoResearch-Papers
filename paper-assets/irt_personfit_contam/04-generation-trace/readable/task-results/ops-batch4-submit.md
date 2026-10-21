# ops batch4 submit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch4-submit_20260523T115735_result.json`
- **Structured JSON:** [`fc95d9f5e7c73eceaf24.json`](../../sessions/fc/fc95d9f5e7c73eceaf24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 jobs are training successfully:

| GPU | Experiment | Steps | ETA |
|-----|-----------|-------|-----|
| 0 | exp-mistral-25pct-s1 (contam_25, mistral) | 7/1596 | ~34 min |
| 1 | exp-llama-5pct-s2 (contam_5_s2, llama) | 6/1071 | ~21 min |
| 2 | exp-llama-25pct-s2 (contam_25_s2, llama) | 4/1596 | ~40 min |
| 3 | exp-mistral-5pct-s2 (contam_5_s2, mistral) | 6/1071 | ~21 min |

Summary of what was done:
- Generated missing `contam_5_s2` data directory (5702 items: 5000 alpaca + 702 MMLU 5%, shuffle seed=123)
- Added `contam_5_s2: 123` to SEED_MAP in train.py
- Submitted all 4 jobs via tmux sessions with `WANDB_MODE=disabled`

---
