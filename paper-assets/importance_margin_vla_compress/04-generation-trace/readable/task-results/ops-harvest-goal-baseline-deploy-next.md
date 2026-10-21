# ops harvest goal baseline deploy next

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_goal_baseline_deploy_next_20260522T131725_result.json`
- **Structured JSON:** [`f19ecb87a5c5f01cc3e0.json`](../../sessions/f1/f19ecb87a5c5f01cc3e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### baseline_goal 结果
- **Overall SR: 96.4%** (482/500, 49.7 min)
- 满分任务 (100%): bowl_on_stove, bowl_on_cabinet, push_plate, turn_on_stove, bowl_on_plate — 5/10 tasks
- 98%: wine_bottle_on_cabinet
- 96%: cream_cheese_in_bowl
- 90%: open_middle_drawer, open_top_drawer_bowl_inside, wine_bottle_on_rack

### cuda:1 新实验
- tmux session: `pi05_goal_extra`
- PID: 179967 (k=0.85 先跑，k=0.7 串行排队)
- cuda:1 显存: 10532 MiB，模型加载成功
- 已观察到 `[PRUNE-DIAG] l2norm: n_keep=217/256`，正在评估中

### westd-38929 当前 GPU 状态
| GPU | 显存 | 任务 |
|-----|------|------|
| cuda:0 | 10772 MiB | pi05_long_l2norm (k=0.95→0.9→0.85) |
| cuda:1 | 10532 MiB | pi05_goal_extra (k=0.85→0.7) |
| cuda:2 | 10538 MiB | baseline_long |
| cuda:3 | ~10063→4 MiB | pi05_goal_l2norm (k=0.95→0.9) — 可能刚完成一轮在重载 |

---
