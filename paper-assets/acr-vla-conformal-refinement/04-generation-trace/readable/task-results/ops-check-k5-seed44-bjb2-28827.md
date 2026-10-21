# ops check k5 seed44 bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-k5-seed44-bjb2-28827_20260518T194035_result.json`
- **Structured JSON:** [`543da607b437d2bd9d9c.json`](../../sessions/54/543da607b437d2bd9d9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=5 seed44 实验状态

**仍在运行** (已跑 6h39m)，当前进度:
- 已完成 **8/10 tasks** (每 task 10 rollouts)，正在跑第 9 个 (`chocolate_pudding`, rollout 3/10)
- 已完成 tasks 的 SR:

| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 10% (1/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | **40%** (4/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 10% (1/10) |
| milk | 30% (3/10) |

当前 8 tasks 平均 SR = **13.75%**，还剩 2 个 task，预计 ~1.5h 完成。

## bjb2-28827 整体状态

**GPU 利用率** — 6 卡全部在用:

| GPU | Util | VRAM |
|---|---|---|
| 0 | 99% | 9.9/24.6 GB |
| 1 | 99% | 9.0/24.6 GB |
| 2 | 88% | 6.2/24.6 GB (K=5 seed44) |
| 3 | 99% | 9.0/24.6 GB |
| 4 | 99% | 10.9/24.6 GB |
| 5 | 99% | 9.9/24.6 GB |

**12 个 tmux session 活跃**，包括 obs_only、perdof、default、random_selection 等多组实验。

**已完成结果文件** (最近):
- `eval_object_random_selection_seed44.json` (May 19 02:00)
- `eval_object_random_selection_seed43.json` (May 18 23:45)
- `eval_object_obs_only_norm01_seed42.json` (May 18 23:16)
- `eval_object_obs_only_norm02_k5_seed43.json` (May 18 20:28) — K=5 的前一个 seed 已完成

---
