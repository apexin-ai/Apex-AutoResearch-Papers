# ops cwm eval status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-eval-status-check_20260523T200222_result.json`
- **Structured JSON:** [`eb2648b5a1b0f80f3a37.json`](../../sessions/eb/eb2648b5a1b0f80f3a37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM Eval 状态汇总（截至服务器时间 05-24 04:03）

| | GPU 0 | GPU 1 | GPU 3 |
|---|---|---|---|
| **任务** | s123 ckpt300 reeval | s456 ckpt300 reeval | ckpt6100 test |
| **PID** | 278348 | 278746 | 272025 |
| **状态** | 运行中 | 运行中 | 运行中 |
| **启动时间** | 05-23 19:19 | 05-23 19:20 | 05-23 18:26 |
| **已运行** | ~8h44m | ~8h43m | ~9h36m |
| **进度** | 1140/9784 (11.7%) | 1282/9784 (13.1%) | 5912/9784 (60.4%) |
| **Running Acc** | **63.2%** | **66.5%** | **69.3%** |
| **速度** | ~131 samples/h (bs=1) | ~147 samples/h (bs=1) | ~616 samples/h (bs=8) |
| **剩余时间** | ~66h | ~58h | ~6.3h |
| **预计完成** | ~05-26 22:00 | ~05-26 14:00 | ~05-24 10:20 |
| **显存占用** | 17013 MiB | 17011 MiB | 27883 MiB |

**GPU 2** 空闲（0 MiB / 0% util）。

关键观察：
- GPU 3（ckpt6100, bs=8）今天上午就能跑完
- GPU 0/1（bs=1）还要跑 2.5 天左右，速度慢 ~4x，因为 batch_size=1
- s456 比 s123 acc 高 3.3 个点（66.5% vs 63.2%），ckpt6100 最高 69.3%

---
