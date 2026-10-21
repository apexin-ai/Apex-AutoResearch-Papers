# ops check cuda0 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_cuda0_status_20260517T203000_result.json`
- **Structured JSON:** [`a7ae4634591bcf5c5279.json`](../../sessions/a7/a7ae4634591bcf5c5279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 完全空闲。**

| 项目 | 状态 |
|------|------|
| GPU | RTX 4090 D (24GB) |
| 显存占用 | 0 MiB / 24564 MiB |
| GPU 利用率 | 0% |
| GPU 进程 | 无 |
| tmux session | 无 |

服务器上仅有 tensorboard (PID 818) 和 jupyter-lab (PID 820) 两个后台服务进程在跑，均不占用 GPU。本机只有 1 张 GPU (cuda:0)，当前可用。

---
