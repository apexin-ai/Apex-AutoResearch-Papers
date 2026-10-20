# check exp003 crash

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003-crash_20260513T064842_result.json`
- **Structured JSON:** [`1b9e9f872be73f1958c6.json`](../../sessions/1b/1b9e9f872be73f1958c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程 PID 24438 没有退出，当前正常运行中。**

状态汇总：

| 项目 | 状态 |
|------|------|
| PID 24438 | **运行中** (`Rl`, CPU 1382%, 启动于 14:44) |
| GPU 1 | 4252MiB / 97887MiB, 温度 41°C |
| 当前 step | **52000** / 500000 |
| 最新 eval_return | 416.37 |
| 最新 train_return | ~424-533 (step 48k-52k) |
| 错误 | 无 traceback，仅有 deprecation warnings (torch.cuda.amp) |

日志中只有 gym 过时警告和 `torch.cuda.amp` 的 FutureWarning，无任何错误或异常。

另外 baseline 实验 (PID 9409, GPU 0) 也在正常运行。

**结论：进程未退出，正在正常训练，无需干预。**

---
