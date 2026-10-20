# ops cleanup stale processes

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_stale_processes_20260514T151120_result.json`
- **Structured JSON:** [`2cd3af055088a91db96c.json`](../../sessions/2c/2cd3af055088a91db96c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Kill 的进程
无。没有找到残留的 entailment/10q/rescorer 进程，已经被清理干净。

### 保留的进程
| PID | 命令 | 原因 |
|-----|------|------|
| 937 | jupyter-lab | 系统服务 |
| 939 | tensorboard | 系统服务 |
| 33086/33091 | vLLM (DeepSeek-R1-Distill-Qwen-14B, TP=2, port 8001) | vLLM 服务，不可 kill |

### GPU 状态 (4× RTX 5090, 32GB each)

| GPU | 显存占用 | Utilization | 状态 |
|-----|---------|-------------|------|
| cuda:0 | 31461/32607 MiB (96%) | 0% (idle) | vLLM Worker_TP0 占用，待请求 |
| cuda:1 | 31461/32607 MiB (96%) | 0% (idle) | vLLM Worker_TP1 占用，待请求 |
| cuda:2 | 3/32607 MiB (~0%) | 0% | **空闲** |
| cuda:3 | 3/32607 MiB (~0%) | 0% | **空闲** |

cuda:0 和 cuda:1 被 vLLM 服务占满（各 ~31GB），cuda:2 和 cuda:3 完全空闲可用。

---
