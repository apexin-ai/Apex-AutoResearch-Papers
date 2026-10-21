# ops kill zombie 223975

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_zombie_223975_20260515T165146_result.json`
- **Structured JSON:** [`a59a241eede2b714796c.json`](../../sessions/a5/a59a241eede2b714796c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 223975 已死亡，cuda:3 上无该进程残留。

当前 GPU 占用：

| GPU | 占用 | 总计 | PID |
|-----|------|------|-----|
| 0 | 16.0 GB | 32 GB | 226481 |
| 1 | 22.4 GB | 32 GB | 222212 |
| 2 | 22.7 GB | 32 GB | 221967 |
| 3 | 15.6 GB | 32 GB | 220202 |

cuda:3 当前被 PID 220202 占用 15.6GB——这不是 223975，是另一个进程。223975 的显存已释放，但 cuda:3 并非空闲，需确认 220202 是否是你预期中的 eval 进程。

---
