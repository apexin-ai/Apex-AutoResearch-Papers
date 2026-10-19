# ops check dead processes batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-dead-processes-batch_20260520T220058_result.json`
- **Structured JSON:** [`bc96a2771a3c7e672db3.json`](../../sessions/bc/bc96a2771a3c7e672db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个已完成实验已更新为 DONE。汇总：

| # | exp_id | Server | JSON | SR | Status |
|---|--------|--------|------|----|--------|
| 1 | `eval-vla-only-object-seed50` | bjb1-32546 | `eval_vla_only_object_seed50.json` | **9%** | DONE |
| 2 | `eval-random-selection-object-seed49` | bjb1-32546 | `eval_random_selection_object_seed49.json` | **12%** | DONE |
| 3 | `eval-obs-only-object-norm02-seed52` | bjb1-32546 | `eval_obs_only_object_norm02_seed52.json` | **15%** | DONE |
| 4 | `eval-obs-only-object-norm005-seed48` | bjb1-32546 | `eval_obs_only_object_norm005_seed48.json` | **13%** | DONE |
| 5 | `eval-obs-only-object-norm005-seed47` | bjb2-28827 | `eval_obs_only_object_norm005_seed47.json` | **13%** | DONE |
| 6 | `eval-obs-only-object-norm02-seed55` | bjb2-40593 | 未生成 | — | **RUNNING** (PID=776722 alive, VRAM 5960/24564 MiB, 刚加载完 10 tasks，尚未开始 rollout) |
| 7 | `eval-k5-obs-only-object-seed44` | bjb1-32546 | `eval_k5_obs_only_object_seed44.json` | **14%** | DONE |
| 8 | `eval-k20-obs-only-object-seed44` | bjb1-32546 | `eval_k20_obs_only_object_seed44.json` | **18%** | DONE |

所有 JSON 均完整（10 tasks × 10 rollouts = 100 total）。seed55 进程正常运行中，不动。

---
