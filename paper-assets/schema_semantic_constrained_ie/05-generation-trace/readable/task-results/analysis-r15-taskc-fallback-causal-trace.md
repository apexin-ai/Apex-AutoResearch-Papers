# analysis r15 taskC fallback causal trace

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15_taskC_fallback_causal_trace_20260521T014700_result.json`
- **Structured JSON:** [`41867d93f3099cd2be5a.json`](../../sessions/41/41867d93f3099cd2be5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Config | Triples | Fallback Positions | DR Violations | Caused by Fallback | Independent |
|--------|---------|-------------------|---------------|-------------------|-------------|
| Qwen FT S1 | 1128 | 0/2256 (0%) | 0 | 0 | 0 |
| Qwen ZS S1 | 1729 | 16/3458 (0.46%) | 16 | 16 | 0 |
| LLaMA FT S1 | 1081 | 1/2162 (0.05%) | 1 | 1 | 0 |
| LLaMA ZS S1 | 1315 | 1/2630 (0.04%) | 1 | 1 | 0 |

关键发现：
- **SciERC Qwen FT S1: 零 fallback，零 DR violation** — fine-tuning 完全消除了 fallback
- 所有 DR violations 100% 由 fallback 导致（`dr_independent = 0`），因为活跃的 semantic mask 在构造上不可能产生 DR violation
- 所有 fallback 都发生在 **tail_type** 位置（head_type fallback = 0），pattern 一致：relation 的 valid_tails_for_head 约束比 valid_heads 约束更窄，更容易触发 S∩G=∅
- ZS→FT 使 Qwen 的 fallback rate 从 0.46% 降到 0%（100% reduction）

输出已保存到服务器 `/root/autodl-tmp/schema_outputs/r15_verification/task_c_fallback_trace.json` 和本地 artifacts。

---
