# ops verify llama rp10 final

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-llama-rp10-final_20260516T112758_result.json`
- **Structured JSON:** [`add97b8d3c17489418ad.json`](../../sessions/ad/add97b8d3c17489418ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan-016-llama32-3b 生成完成** ✓

| 项目 | 值 |
|------|-----|
| 状态 | 成功完成 |
| 总条数 | 4680 |
| Depth 分布 | d0=995, d1=984, d2=943, d3=899, d4=859 |
| 最后记录 | seed_id=999, depth=4 |
| 缺失率 | 5.9% (295/4975 因 degenerate 跳过，deeper depths 递减符合预期) |

Registry 已更新为 DONE/success，cron 已删除。

---
