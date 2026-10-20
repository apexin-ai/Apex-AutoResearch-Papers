# ops cleanup old checkpoints 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_old_checkpoints_34685_20260524T042304_result.json`
- **Structured JSON:** [`1c1bb6c4eb5beac06bd5.json`](../../sessions/1c/1c1bb6c4eb5beac06bd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| | 删除前 | 删除后 |
|---|---|---|
| 已用 | 259G (74%) | 200G (58%) |
| 可用 | 92G | 151G |

释放了 **59G**。两个实验目录下仅保留 50000_chkpt 和训练主目录，30000/40000 checkpoint 已全部清除。

---
