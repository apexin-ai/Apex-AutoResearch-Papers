# collect smolvla long reseed results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_smolvla-long-reseed-results_20260522T153712_result.json`
- **Structured JSON:** [`61aa80b95aa129861956.json`](../../sessions/61/61aa80b95aa129861956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete picture:

## Status: ALL 3 SEEDS INCOMPLETE

All 3 processes died at 23:41 (started 23:05, ran ~36 min). No OOM, no error, no traceback — likely killed externally or AutoDL resource limit. Disk was fine (44% root, 29% data).

## Completed Tasks (5/10 per seed, 20 episodes each)

| Task ID | Seed 0 | Seed 1 | Seed 2 |
|---------|--------|--------|--------|
| 0 | 25.0% | 10.0% | 10.0% |
| 1 | 40.0% | 45.0% | 55.0% |
| 2 | 85.0% | 70.0% | 80.0% |
| 3 | 70.0% | 85.0% | 85.0% |
| 4 | 45.0% | 35.0% | 35.0% |
| **Partial avg (5/10)** | **53.0%** | **49.0%** | **53.0%** |
| 5 (in progress) | ~75-82% | ~73% | ~62-67% |
| 6-9 | not started | not started | not started |

## Eval Method

- **Lerobot-native eval** via our wrapper `figs/eval.py` → `bot_eval.py`
- Config: `n_episodes=20`, `batch_size=1`, `max_steps=520`, task suite `libero_10`
- Model: SmolVLA from `/root/autodl-tmp/models/smolvla_libero/`
- Output dirs: `outputs/eval/2026-05-22/23-05-{56,59,01}_libero_smolvla/` (videos only, no JSON — only written after completion)

## Earlier vla-only eval (also incomplete)

The `eval-vla-only-long-seed{0,1,2}` logs ran our custom wrapper with `n_rollouts=10`, but only completed 2 tasks each before being replaced by the lerobot eval.

## Next Steps Needed

All 3 seeds need to be **restarted** — tasks 5-9 have no results, and no JSON was generated. The processes died silently (no crash signals in dmesg).

---
