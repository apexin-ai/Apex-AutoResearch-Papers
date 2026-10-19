# ops kill competing downloads

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-competing-downloads_20260515T082335_result.json`
- **Structured JSON:** [`7c97686e13f7f4dfaed6.json`](../../sessions/7c/7c97686e13f7f4dfaed6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 状态 |
|------|------|
| **Kill 进程** | PID 19946 (wget)、20077 (python3)、20135 (bash)、20136 (curl) 全部已 kill — 因为三者同时写同一文件，文件已损坏，保留任何一个都无意义 |
| **损坏 shard 1 删除** | ✓ 已删除 `model-00001-of-00004.safetensors` |
| **重新下载** | ✓ 新 curl 进程 PID 20515 已启动，单一进程下载 shard 1 |
| **残留文件清理** | ✓ `.incomplete` 和 `.lock` 文件已清理 |
| **其他 shard 状态** | shard 2: 4.7G ✓ / shard 3: 4.7G ✓ / shard 4: 251M ✓ — 大小合理，未被竞争写入 |
| **shard 1** | 下载中，预计大小 ~4.7G，可稍后用 `ls -lh` 确认完成 |

---
