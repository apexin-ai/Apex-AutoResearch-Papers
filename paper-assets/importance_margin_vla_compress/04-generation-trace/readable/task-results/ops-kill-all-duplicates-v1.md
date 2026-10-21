# ops kill all duplicates v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_all_duplicates_v1_20260522T092719_result.json`
- **Structured JSON:** [`496d5da1916472560941.json`](../../sessions/49/496d5da1916472560941.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd-27271:
  Kill PID 325659: 成功
  Kill PID 325931: 成功
  GPU 0: 空闲 ✅
  GPU 1: 空闲 ✅

cqa1:
  Kill GPU 0 (PID 249598): 成功
  Kill GPU 2 (PID 249746): 成功
  Kill GPU 3 (PID 249887): 成功
  GPU 1 保留: PID 249668 存活 ✅
```

5 个重复进程全部清除，3 个空闲 GPU 待命（westd 2 个 + cqa1 2 个），cqa1 GPU 1 的 l2norm_k0.9_object_s43 正常运行。

---
