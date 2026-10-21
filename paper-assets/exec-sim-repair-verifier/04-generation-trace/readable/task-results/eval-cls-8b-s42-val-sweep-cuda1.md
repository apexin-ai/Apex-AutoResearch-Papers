# eval cls 8b s42 val sweep cuda1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-8b-s42-val-sweep-cuda1_20260514T203929_result.json`
- **Structured JSON:** [`6f518458ae35972c7a85.json`](../../sessions/6f/6f518458ae35972c7a85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 状态（4x 5090, 全部繁忙）

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 19794/32607 MiB | 99% | PID 280392: **CLS 8B s42 val ckpt-400** (运行 25min) |
| 1 | 13629/32607 MiB | 99% | PID 281646: CLS v5 4B val ckpt-400 (运行 19min) |
| 2 | 30733/32607 MiB | 98% | PID 266816: CWM 8B 训练 |
| 3 | 30913/32607 MiB | 98% | PID 266449: CLS 8B seed123 训练 |

### 进程清理
- PID 282767, 282240: **已死**，无需操作。

### CLS 8B s42 val sweep
- **checkpoint-400 已在运行**（PID 280392, cuda:0）—— 正是最优先的 checkpoint。目前还在加载模型/初始批次，尚无 predictions 输出。
- **checkpoint-200, checkpoint-600 无法启动**：4 块 GPU 全部满载。需等 cuda:0 或 cuda:1 上的 eval 完成后再排队。

建议：用 cron 监控 PID 280392 完成后，在 cuda:0 上依次启动 ckpt-200 和 ckpt-600 的 eval。是否需要设置？

---
