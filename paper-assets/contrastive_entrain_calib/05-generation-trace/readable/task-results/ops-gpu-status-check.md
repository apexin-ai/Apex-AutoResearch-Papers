# ops gpu status check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260525T134154_result.json`
- **Structured JSON:** [`644b8d20aba33c39b036.json`](../../sessions/64/644b8d20aba33c39b036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status Summary

### GPU Usage
| GPU | Process | VRAM | Util |
|-----|---------|------|------|
| cuda:0 | PID 33822 (exp-003-s2 eval) | 16.9 / 97.9 GB | 52% |
| cuda:1 | PID 31718 (exp-003-s3 training) | 38.2 / 97.9 GB | 98% |

### exp-003-s3 Training (cuda:1)
- **Status: Running** — step **124 / 8000** (~1.6%)
- ~26s/step, ETA ~56 hours
- Still in LR warmup phase (lr=4.95e-05), reward oscillating 0.42–0.57
- Checkpoint dir `exp003_r3only_seed3/` exists but is **empty** — no checkpoints saved yet
- `d_syc not loaded; returning R3-only rewards` warnings are expected (R3-only config)

### exp-003-s2-eval (cuda:0)
- **Status: Running** — currently evaluating **ckpt-2500** (first checkpoint)
- Output dir `results/exp003s2_d027_eval/` is still empty — ckpt-2500 eval hasn't finished yet
- No ckpt-2500 or ckpt-3000 results available yet
- Previous eval results exist in `results/exp003_d027_eval/` for ckpt4000, ckpt7500, ckpt8000 (from earlier runs)

---
