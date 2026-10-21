# code fix contradiction metric

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-contradiction-metric_20260515T094127_result.json`
- **Structured JSON:** [`ee08de9bc7a235794b03.json`](../../sessions/ee/ee08de9bc7a235794b03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。修改内容：

1. **新增计算**：`problems_with_contradictions = sum(1 for r in all_results if r.get("maxsat_stats", {}).get("excluded", 0) > 0)` — 统计有矛盾排除的题目数
2. **summary dict 新增字段**：`problems_with_contradictions` 和 `total_problems`
3. **日志新增行**：`Problems with contradictions: 0/50`

原有的 `contradiction_rate`（全局比例）保留不变。mock 模式下矛盾数为 0/50 符合预期（mock 不产生真实矛盾）。

---
