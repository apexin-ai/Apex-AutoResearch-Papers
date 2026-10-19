# check v7 v5 progress

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v7-v5-progress_20260516T130520_result.json`
- **Structured JSON:** [`249312bc677a6af11f66.json`](../../sessions/24/249312bc677a6af11f66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

**v7 训练 (GPU 0)**
- 当前 step: **2100/20000** (10.5%)
- 速度: 1.8 steps/s
- loss=0.24, task_loss=0.096, β=0.01 (warmup 完成)
- scorer_mean=0.285, std=0.307
- 预计剩余: ~2.8h

**v5 eval (GPU 0)**
- 正在跑 **libero_spatial** (4 个 suite 中的第 1 个)
- 当前某个 episode 的 rollout 接近完成 (277/280 steps)，running_success_rate=0.0%
- 还有 libero_object, libero_goal, libero_10 三个 suite 未跑

**GPU 状态**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 98% | 16.2 GB |
| 1 | 0% | 0 MB |

注意：v7 训练和 v5 eval 都在 GPU 0 上跑（只有一个 PID 21363 在使用 GPU）。v5 eval 似乎是 CPU-heavy 的 rollout 阶段，没有占用独立 GPU 进程——或者 eval 实际跑在同一进程内。GPU 1 空闲。

---
