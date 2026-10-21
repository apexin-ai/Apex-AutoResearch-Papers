# ops check m96 alive

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-m96-alive_20260520T193235_result.json`
- **Structured JSON:** [`92253f3b5499d2fa71a6.json`](../../sessions/92/92253f3b5499d2fa71a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**M96 训练进程存活，运行正常。**

| 项目 | 状态 |
|------|------|
| PID 68539 | **alive**，状态 `Rl`（运行中），已运行 15h52m |
| 训练进度 | step 27750/100000 (27.8%)，loss ~3.0，lr 8.35e-5，速度 0.5 sps |
| 最后日志 | 2026-05-21 03:31:57（1 分钟前） |
| GPU 2 利用率 | 0%（瞬时读数），显存 28555/97887 MiB |

GPU 2 利用率瞬时为 0% 是正常现象——训练以 0.5 sps 速度运行，GPU 在数据加载/梯度同步间隙会短暂空闲。日志持续输出，进程无异常。

---
