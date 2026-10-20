# check exp029b progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029b_progress_20260518T020447_result.json`
- **Structured JSON:** [`cd84128d31680e997203.json`](../../sessions/cd/cd84128d31680e997203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_029b (SciERC 10-epoch) 训练状态

**训练正在进行中，PID 441471 在 GPU 1 上运行。**

| 指标 | 值 |
|---|---|
| 当前 step / 总 step | **560 / 1170** |
| 进度 | **47.86%** |
| 当前 epoch | **4.79 / 10** |
| 训练 loss | **0.0394**（持续下降，从初始 0.83 → 当前 0.04） |
| eval loss (step 500) | **0.0896** |
| 已运行时间 | **27 分 34 秒** |
| 预估剩余时间 | **~30 分钟** |
| 学习率 | 1.25e-4（衰减中） |

**GPU 状态：**
| GPU | 利用率 | 显存 | 温度 |
|---|---|---|---|
| GPU 0 | 0% (空闲) | 2 MiB / 32607 MiB | 31°C |
| **GPU 1** | **100%** | **28690 MiB / 32607 MiB (88%)** | **77°C** |
| GPU 2 | 0% (空闲) | 2 MiB / 32607 MiB | 29°C |
| GPU 3 | 0% (空闲) | 2 MiB / 32607 MiB | 29°C |

注意：`exp_029b.log` 中残留的是之前一次 OOM 错误的 traceback（GPU 0 上的旧尝试），不是当前运行的日志。当前训练实际在 GPU 1 上正常运行，进度从 `trainer_log.jsonl` 确认。预计约 30 分钟后完成全部 10 epoch。

---
