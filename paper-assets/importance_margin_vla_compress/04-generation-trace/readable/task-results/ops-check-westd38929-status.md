# ops check westd38929 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd38929-status_20260520T221000_result.json`
- **Structured JSON:** [`244f82f6ce732169c42c.json`](../../sessions/24/244f82f6ce732169c42c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行。汇总：

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 85% | 15980 / 97887 MiB |
| 1 | 67% | 15980 / 97887 MiB |
| 2 | 59% | 16108 / 97887 MiB |
| 3 | 63% | 15980 / 97887 MiB |

### 实验进程状态
| GPU | PID | 实验 | 状态 | 进度 |
|-----|-----|------|------|------|
| 0 | 95088 | random_prune k=0.95 seed42 | **运行中** (Rl+) | Task 1/10, Ep 20/50, sr=18/20 (90%) |
| 1 | 95361 | random_prune k=0.7 seed42 | **运行中** (Rl+) | Task 1/10, Ep 20/50, sr=13/20 (65%) |
| 2 | 95670 | random_prune k=0.3 seed43 | **运行中** (Rl+) | Task 1/10, Ep 10/50, sr=2/10 (20%) |
| 3 | 95853 | l2norm_prune k=0.9 seed43 | **运行中** (Rl+) | Task 1/10, Ep 20/50, sr=13/20 (65%) |

4 个进程均存活，GPU 利用率正常（59-85%），各实验 log 有持续输出，都在 Task 1/10 阶段推进中。一切正常。

---
