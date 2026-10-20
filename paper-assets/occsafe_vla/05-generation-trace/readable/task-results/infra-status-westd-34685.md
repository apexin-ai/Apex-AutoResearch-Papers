# infra status westd 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-westd-34685_20260521T150451_result.json`
- **Structured JSON:** [`1e60be6f7c9ccfd59f78.json`](../../sessions/1e/1e60be6f7c9ccfd59f78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status Report

### westd-34685

**s1_fresh: RUNNING** — step ~2213/50005 (4.4%), 1.08 it/s
- No checkpoints saved yet (first save at step 2500)
- ETA to completion: ~12.3h from now → **~May 22 11:45 UTC**
- 47500_chkpt does not exist yet — eval not started

**GPU utilization:**
| GPU | Util | VRAM | Process |
|-----|------|------|---------|
| 0 | 99% | 62203 MiB | s1_fresh training |
| 1 | 1% | 16778 MiB | occ_s0 50r eval (PID 482355) |
| 2 | 57% | 16778 MiB | occ_s2 50r eval (PID 491669) |
| 3 | 0% | 1 MiB | idle |

**Running evals:**
- occ_s0 50r eval: T8 task, 39/50 rollouts done (~78%)
- occ_s2 50r eval: running (separate log at `/root/runs/occsafe_vla/eval_occ_s2_50r.log`)

**Disk:** 49% used, 179G free

---

### westd-10894 Ablation Status

All 4 ablations **RUNNING**, all passed 10000_chkpt save (next save at 20000).

| Ablation | GPU | Step | Progress | Speed | ETA |
|----------|-----|------|----------|-------|-----|
| occ_detach_s0 | cuda:0 | ~14536 | 29% | 1.08 it/s | ~May 22 08:30 UTC |
| random_occ_s0 | cuda:1 | ~14960 | 30% | 1.02 it/s | ~May 22 09:00 UTC |
| occ_detach_s1 | cuda:2 | ~14582 | 29% | 1.04 it/s | ~May 22 08:50 UTC |
| random_occ_s1 | cuda:3 | ~14553 | 29% | 1.08 it/s | ~May 22 08:35 UTC |

**GPU utilization:** 96-99% all 4 GPUs
**Disk:** 45% used, 140G free

---
