# eval cls 8b s42 extra check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-8b-s42-extra-check_20260514T141208_result.json`
- **Structured JSON:** [`70e5e3851c3f9e000a33.json`](../../sessions/70/70e5e3851c3f9e000a33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：cuda:2 不空闲，4 张卡全满，无法启动新任务。**

当前 westd 全卡状态：

| GPU | 任务 | 进度 |
|-----|------|------|
| 0 | CWM 4B seed123 eval (ckpt-500) | 运行中，结果目录为空 |
| 1 | CWM 4B v12 eval (ckpt-500) | 运行中，结果目录为空 |
| 2 | CWM 8B 训练 | 已到 ckpt-1200（已恢复，未崩溃） |
| 3 | CLS 8B seed123 训练 | 已到 ckpt-2400 |

CWM 8B（PID 210573）已在 cuda:2 上正常运行，产出了 ckpt-400 到 ckpt-1200，看起来崩溃后已被重启。没有空闲 GPU 可供临时利用。

---
