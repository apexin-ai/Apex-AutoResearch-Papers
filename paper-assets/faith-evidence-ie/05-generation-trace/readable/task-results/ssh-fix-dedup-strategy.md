# ssh fix dedup strategy

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-dedup-strategy_20260515T021941_result.json`
- **Structured JSON:** [`258c37596e98e77a3071.json`](../../sessions/25/258c37596e98e77a3071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改结果：

- `merge_shards.py` 去重策略从 first-wins 改为 **last-wins**（`set` + `continue` → `dict` 覆盖）
- `rsft_score_filter.py` 已确认是 last-wins，无需修改
- 两个文件去重策略现已统一

测试验证：120 条 root 记录被 shard 版本覆盖（shard_0 覆盖 104 条，shard_3 覆盖 16 条），合并后 7384 条记录、923 个 unique docs。

---
