# paper d113 table2 narrative fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d113_table2_narrative_fix_20260516T100628_result.json`
- **Structured JSON:** [`363e7962ac9ecbb5d09b.json`](../../sessions/36/363e7962ac9ecbb5d09b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有 11 处已修复：

- 全部 `0.663`（micro F1）已删除，替换为 macro 值 0.645
- "surpasses all" / "fails to outperform" → "approximately matches greedy...without significant improvement"
- LP delta 统一为 +0.2pp（LP 0.647 - Greedy 0.645）
- C3 contribution 改为 "Selection recovers T=1.0 degradation but fails to close the 13.3pp oracle gap"
- limitations 和 discussion 的 combination delta 统一为 +0.2pp

验证 grep 确认无遗漏。Changelog 已注册为 artifact `art_20260516_f3e434`。

---
