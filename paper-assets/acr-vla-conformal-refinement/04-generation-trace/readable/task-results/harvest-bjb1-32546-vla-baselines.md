# harvest bjb1 32546 vla baselines

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-vla-baselines_20260524T210940_result.json`
- **Structured JSON:** [`bc1dcf1da5eea9b44d64.json`](../../sessions/bc/bc1dcf1da5eea9b44d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 5 个实验仍在运行中，未完成。**

进程状态确认所有 Python 进程都处于 `Rl+`（活跃运行），CPU 使用率 360-372%，从 04:18 启动至今约 1 小时：

| exp_id | benchmark | seed | tasks 完成 | 当前进度 | 状态 |
|--------|-----------|------|-----------|---------|------|
| eval-supp-obj-vla-only-s42 | object | 42 | 4/10 | bbq_sauce 85% (17/20) | **运行中** |
| eval-supp-obj-vla-only-s43 | object | 43 | 3/10 | 进入 bbq_sauce | **运行中** |
| eval-supp-obj-vla-only-s44 | object | 44 | 3/10 | 进入 bbq_sauce | **运行中** |
| eval-supp-goal-vla-only-s42-bjb1 | goal | 42 | 4/10 | bowl_on_top_cabinet 进行中 | **运行中** |
| eval-supp-long-vla-only-s43-r2 | long | 43 | 1/10 | cream_cheese_butter 进行中 | **运行中** |

这些 tmux sessions 于 May 25 04:18 创建，实验刚跑了约 1 小时，每个 benchmark 有 10 tasks × 20 rollouts，预计还需数小时才能完成。之前的"GPU 空闲"判断可能是因为 GPU 仅在推理时短暂占用，大部分时间在 CPU 上做 LIBERO 仿真。

不需要更新 registry，等实验跑完再收割。

---
