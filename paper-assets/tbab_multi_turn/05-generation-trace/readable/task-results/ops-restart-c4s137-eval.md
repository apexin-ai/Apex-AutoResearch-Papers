# ops restart c4s137 eval

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-c4s137-eval_20260518T212220_result.json`
- **Structured JSON:** [`c437548ab2e825260f92.json`](../../sessions/c4/c437548ab2e825260f92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**C4_s137 eval 不需要重启——已经跑完了。**

汇总：

| 项目 | 状态 |
|------|------|
| **C4_s137 eval 进度** | **91/91 samples 已完成**，之前只是写 summary 文件时磁盘满崩溃，已补写 |
| **C4_s137 结果** | p_bar=0.0549, n_correct=5/91, a90=0.0, u10_90=0.2 |
| **磁盘** | 29G/30G (95%), 1.8G 可用 |
| **GPU** | 1 个进程占用 15894 MiB（c2_s42 eval 在跑） |
| **活跃 tmux** | `eval_c2_s42` |

C4_s137 eval 已完成，无需并行。当前 GPU 仅被 c2_s42 eval 占用。

---
