# ops check cuda1 status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda1-status_20260514T053749_result.json`
- **Structured JSON:** [`6be4370b71fecf9322b9.json`](../../sessions/6b/6be4370b71fecf9322b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:1 被占用，不空闲。**

GPU 进程：
| PID | GPU | 显存 |
|-----|-----|------|
| 262266 | GPU 0 | 79604 MiB |
| **261641** | **GPU 1** | **16450 MiB** |
| **263273** | **GPU 1** | **79156 MiB** |

GPU 总览：
| GPU | 已用/总量 | 利用率 |
|-----|-----------|--------|
| 0 | 79613 / 97887 MiB | 91% |
| **1** | **95620 / 97887 MiB** | **100%** |

cuda:1 上有两个进程：
- **PID 261641** — 就是之前的 plan017 eval_sta 进程，占 16450 MiB，仍未退出
- **PID 263273** — 新进程，占 79156 MiB

cuda:1 显存几乎满（95.6G / 97.9G），利用率 100%，无法提交 plan016。

---
