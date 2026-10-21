# diagnose register d112 shard crons

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_register_d112_shard_crons_20260518T234636_result.json`
- **Structured JSON:** [`b3826d59d15358848f77.json`](../../sessions/b3/b3826d59d15358848f77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已注册。当前 D112 各 shard 状态：

| Shard | GPU | PID | 进度 | 每 doc 速度 |
|-------|-----|-----|------|------------|
| 0 (全量) | cuda:3 | 584466 | 206/3027 (7%) | ~18s/it |
| 1 | cuda:1 | 587729 | 10/756 (1%) | ~15s/it |
| 2 | cuda:2 | 587819 | 13/756 (2%) | ~13s/it |

Shard 1 和 shard 2 刚启动约 3 分钟，cron 监控已注册（120s 间隔）。

---
