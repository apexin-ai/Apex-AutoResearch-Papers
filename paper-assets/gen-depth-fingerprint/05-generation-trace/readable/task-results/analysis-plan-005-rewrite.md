# analysis plan 005 rewrite

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-rewrite_20260515T055440_result.json`
- **Structured JSON:** [`d81c052f0295107ecd3f.json`](../../sessions/d8/d81c052f0295107ecd3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

- **total_records**: 4827
- **unique_seeds**: 995
- **depth_distribution**: {0:995, 1:995, 2:959, 3:944, 4:934}
- **file_size_mb**: 5.41
- **runtime_seconds**: 8584 (~2.4h)
- **output_file**: `/root/gen-depth-fingerprint/data/pythia-2.8b-inspired_rewriting/generations_shard0.jsonl`
- **depth_retention (d4/d0)**: 93.9%
- **skipped**: 61 (均为 empty output/input)
- **异常**: 无

**与 continuation 对比**：inspired_rewriting depth retention 93.9% 远优于 continuation 的 83.1%，depth 1 甚至零衰减（995/995）。rewriting prompt 使模型在递归生成中更稳定，产生空输出的概率更低（skip 61 vs 168）。

---
