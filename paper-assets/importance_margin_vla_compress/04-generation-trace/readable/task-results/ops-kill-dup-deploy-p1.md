# ops kill dup deploy p1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-dup-deploy-p1_20260524T120733_result.json`
- **Structured JSON:** [`39245d3f6b7717ea512a.json`](../../sessions/39/39245d3f6b7717ea512a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### westd-38929
| 项目 | 结果 |
|------|------|
| Kill | 无需操作 — k=0.9 Spatial 进程 (PID 305684) 已被之前的 Worker kill |
| 释放 GPU | GPU 0 原本就空闲 |
| 新部署 | **l2norm k=0.95 Long** (PID 401837, GPU 0, tmux: `l2norm_k095_long`) |
| GPU 1/2/3 | 已有 random k=0.7 / k=0.3 / k=0.5 Long 在跑，无空闲 |

### westd-41074
| 项目 | 结果 |
|------|------|
| Kill | 无需操作 — 无 l2norm k=0.7 Spatial 进程 |
| GPU 状态 | 4 GPU 全满，均为合法 Long 实验 |
| | GPU 0: random k=0.95 Long |
| | GPU 1: random k=0.85 Long |
| | GPU 2: l2norm k=0.85 Long |
| | GPU 3: random k=0.9 Long |
| 新部署 | 无空闲 GPU，无法部署 |

---
