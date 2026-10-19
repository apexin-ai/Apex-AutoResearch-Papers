# diag bjb2 object eval alive

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-object-eval-alive_20260513T235404_result.json`
- **Structured JSON:** [`08c1c6a00aed1e5eec4b.json`](../../sessions/08/08c1c6a00aed1e5eec4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval-object-v5-full 状态：正在运行**

| 项目 | 状态 |
|------|------|
| PID 117697 | **存活**，运行约 19 分钟 (07:35 启动)，CPU 170% |
| GPU | 12% 利用率，5592 / 24564 MiB 显存占用 |
| 进度 | 模型已加载完成，10 个 LIBERO object tasks 已加载，正在执行 rollouts |

日志显示已完成：模型加载 → 环境加载 → 10 个 task 就绪。当前正在跑 rollouts（每 task 10 次，共 100 次），GPU 利用率偏低说明仿真环境 CPU-bound 居多。

另外注意：还有一个 `test_crash.py` 进程 (PID 120566) 也在跑，占用 1.8GB 显存、CPU 154%。

---
