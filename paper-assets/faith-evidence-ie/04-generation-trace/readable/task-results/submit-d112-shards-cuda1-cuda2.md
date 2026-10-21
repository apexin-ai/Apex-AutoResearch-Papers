# submit d112 shards cuda1 cuda2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d112_shards_cuda1_cuda2_20260518T234240_result.json`
- **Structured JSON:** [`b703fb5edd25f849d461.json`](../../sessions/b7/b703fb5edd25f849d461.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## D112 Generation 状态总结

| Shard | GPU | 文档范围 | 进度 | 速度 | 预估剩余 |
|-------|-----|---------|------|------|---------|
| **0** | cuda:3 | [0:756] → 3027 全量 (无 shard) | 191/3027 (6%) | ~12s/doc | ~9.5h |
| **1** | cuda:1 | [756:1512] → 756 docs | 刚启动 1/756 | ~18s/doc | ~3.8h |
| **2** | cuda:2 | [1512:2268] → 756 docs | 刚启动 1/756 | ~10s/doc | ~2.1h |

**注意**: Shard 0 跑的是全量 3027 docs（未分片），shard 1/2 各 756 docs。看起来脚本在有 SHARD 环境变量时才做 4 分片，shard 0 当时没传 SHARD 所以跑了全量。shard 1 和 shard 2 会覆盖 shard 0 的中间段，最终需要根据实际完成情况合并去重。

Shard 1/2 预计 2-4 小时完成，shard 0 按当前速度还需约 9 小时。

---
