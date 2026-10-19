# ops bjb1 18228 utilization check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-18228-utilization-check_20260519T054953_result.json`
- **Structured JSON:** [`747ed44d1de58ba43d82.json`](../../sessions/74/747ed44d1de58ba43d82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 利用率 | 显存占用 | 显存剩余 | 运行实验 (tmux session) | 状态 |
|-----|--------|----------|----------|------------------------|------|
| 0 | 23% | 4269/24564 MiB | ~20.3 GB | `eval-obs-only-object-norm02-k5-seed47` | 正常运行 |
| 1 | 22% | 2875/24564 MiB | ~21.7 GB | `eval-lto-splitA-heldout-r2` | 正常运行 |
| 2 | 21% | 4700/24564 MiB | ~19.9 GB | `eval-argmin-object-k5-seed43` | 正常运行 |
| 3 | 23% | 4269/24564 MiB | ~20.3 GB | `eval-obs-only-object-norm02-k5-seed46` | 正常运行 |

**发现的问题：**

- `eval-lto-splitA-vla-only-r2` **未在运行**，没有对应的 tmux session。预期在 cuda:2 上跑，但 cuda:2 当前只有 argmin-k5-seed43。
- 所有 GPU 利用率都在 19-23%，属于 eval 推理的正常水平（间歇性推理，非持续计算）。
- 每张 GPU 剩余显存 ~20 GB，**每张卡都有空间加跑实验**（eval 任务通常占 3-5 GB）。

---
