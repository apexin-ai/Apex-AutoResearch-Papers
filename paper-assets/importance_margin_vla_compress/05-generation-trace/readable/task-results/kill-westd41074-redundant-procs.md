# kill westd41074 redundant procs

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill_westd41074-redundant-procs_20260526T202702_result.json`
- **Structured JSON:** [`0df7c4e03ffc6cc01f4a.json`](../../sessions/0d/0df7c4e03ffc6cc01f4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇报：

**Kill 状态**：PID 846246 和 846317 已成功 kill（return_code=0），`ps aux` 中已无这两个 PID。

**nvidia-smi**：4 张 GPU 全部仍在使用，**没有空闲 GPU**。因为有其他实验立即占用了释放的卡：

| GPU | PID | 显存 | 任务 |
|-----|-----|------|------|
| 0 | 856148 | 15961MiB | Random k=0.75 Object |
| 1 | 856656 | 16169MiB | Random k=0.75 Long (libero_10) |
| 2 | 755986 | 15961MiB | (早前启动的进程) |
| 3 | 824210 | 15762MiB | L2norm k=0.75 libero_10 |

**剩余运行中的 Python 进程**：

| PID | GPU | 实验 |
|-----|-----|------|
| 856148 | 0 | `random_prune k=0.75 libero_object` |
| 856656 | 1 | `random_prune k=0.75 libero_10` |
| 755986 | 2 | (较早的进程，具体任务需查日志) |
| 824210 | 3 | `attention_prune (l2norm) k=0.75 libero_10` |

另有 tensorboard (PID 817) 和 jupyter-lab (PID 819) 等服务进程在运行，不影响 GPU。

---
