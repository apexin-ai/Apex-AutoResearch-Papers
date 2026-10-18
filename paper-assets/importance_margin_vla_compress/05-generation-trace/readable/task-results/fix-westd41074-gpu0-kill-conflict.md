# fix westd41074 gpu0 kill conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_gpu0_kill_conflict_20260526T015549_result.json`
- **Structured JSON:** [`76fb879a91c1f40a8884.json`](../../sessions/76/76fb879a91c1f40a8884.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

- **PID 300693**：已 kill
- **PID 303189**（Random k=0.85 Long）：正常运行，GPU 0，16169MiB
- **全局状态**：4 GPU 各一个进程，无冲突

| GPU | PID | 显存 | 利用率 |
|-----|-----|------|--------|
| 0 | 303189 | 16169MiB | 24% |
| 1 | 76492 | 15961MiB | 48% |
| 2 | 259181 | 15961MiB | 69% |
| 3 | 303982 | 16169MiB | 67% |

---
