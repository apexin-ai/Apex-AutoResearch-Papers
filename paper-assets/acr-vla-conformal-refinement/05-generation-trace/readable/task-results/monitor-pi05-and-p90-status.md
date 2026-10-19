# monitor pi05 and p90 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_pi05-and-p90-status_20260521T043914_result.json`
- **Structured JSON:** [`2d4931d1337e7ab6bea6.json`](../../sessions/2d/2d4931d1337e7ab6bea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 fix2 状态
- 进程状态: **RUNNING**
- PID: 831620 (started 12:40, ~1min ago)
- 命令: `evaluate.py --model pi05 --mode vla_only --benchmark object --seed 42 --n_rollouts 5 --K 1`
- 当前阶段: 正在加载 PI05 模型，尚未开始 rollout
- 前次结果 (r2, `eval_pi05_baseline_object_seed42_r2.json`): **SR = 0.0%** (所有 10 tasks × 20 rollouts 全失败)
- 本次是 quicktest (5 rollouts)，结果待出

**注意**: r2 仍然是 SR=0%，如果 quicktest 结果也是 0%，说明 fix2 还没解决问题，需要进一步排查。

## P90-seed44 状态
- 进程状态: **RUNNING**
- PID: 975409
- 已运行时间: **1h38m**
- 进度: **~75/100 rollouts** (7/10 tasks 完成, task 8 进行中 rollout 5/10)
- 当前中间 SR: **45.7%** (32/70 completed rollouts)

Per-task 已出结果:
| Task | SR |
|------|----|
| between_plate_and_ramekin | 80% (8/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 0% (0/10) |
| next_to_cookie_box | **90%** (9/10) |
| on_stove | 进行中 (0/5 so far) |
| next_to_plate, on_shelf | 待跑 |

预计剩余 ~25 rollouts，按当前速度还需 ~30min 完成。

---
