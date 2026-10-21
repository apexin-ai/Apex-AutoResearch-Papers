# ssh fix load generations

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-load-generations_20260515T015836_result.json`
- **Structured JSON:** [`6737066cb494cbbf5329.json`](../../sessions/67/6737066cb494cbbf5329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一致性检查正常工作。结果：

- **root**: 302 docs (之前被丢失，现已加载)
- **shard_0**: JSONL 84 docs > progress 74 (正常, 还在生成中)
- **shard_1**: JSONL 86 > progress 79
- **shard_2**: JSONL 90 > progress 85
- **shard_3**: JSONL 44 < progress 75 (**缺 31 docs** — 确认了之前发现的不一致)
- 去重后: **4744 records, 593 unique docs**
- 120 条根目录/shard 重叠记录被正确去重

所有任务完成：
1. `load_generations()` 已修复 — 现在加载根目录 + 所有 shard，shard 版本去重优先
2. `_check_shard_consistency()` 已添加 — 对比 progress.json 与 JSONL，报告缺失/多余的 doc_id
3. cross-check 脚本已创建在 `/root/autodl-tmp/scripts/diversity_crosscheck.sh`

---
