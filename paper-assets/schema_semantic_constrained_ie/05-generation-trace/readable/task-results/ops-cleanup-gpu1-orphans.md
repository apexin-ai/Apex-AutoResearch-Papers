# ops cleanup gpu1 orphans

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_gpu1_orphans_20260513T235434_result.json`
- **Structured JSON:** [`293d269a10069188dbac.json`](../../sessions/29/293d269a10069188dbac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. PID 身份

| PID | 实验 | GPU | 显存 | 状态 |
|-----|------|-----|------|------|
| 134450 | 未知 | — | — | **已退出**（不存在） |
| 134886 | 未知 | — | — | **已退出**（不存在） |
| 134598 | **full_s1** | GPU 1 | 16.5GB | 正常运行，进程链完整 (→134597→134593) |
| 134207 | semantic_only | GPU 0 | 16.5GB | 正常运行，进程链完整 (→134206→134202) |
| 116365 | docred_schema | GPU 0 | 25.3GB | 正常运行，tmux session 存在 |

### 2. Kill 操作
**无需 kill。** 两个孤儿 PID（134450, 134886）已自行退出。

### 3. GPU 1 当前状态
- 仅 full_s1（PID 134598）占用 16.5GB / 97.9GB，GPU-Util 84%
- 已从 ~49.4GB 降至 ~16.5GB，释放了 ~33GB

### 4. full_s1 运行状态
正常运行。进程树完整：PID 134593 (registry) → 134597 (timeout) → 134598 (python3)，`CUDA_VISIBLE_DEVICES=1`，GPU-Util 84%。

---
