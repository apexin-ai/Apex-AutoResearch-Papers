# analysis r10 a3 judge group ranking

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r10_a3_judge_group_ranking_20260521T192309_result.json`
- **Structured JSON:** [`a0c912e254f157906636.json`](../../sessions/a0/a0c912e254f157906636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出已保存到 `round10_supplementary/a3_judge_group_ranking.json`。

**结果**:

| Type | Judge GPT-4.1 Rank (rate) | Judge GPT-5.4 Rank (rate) |
|------|--------------------------|--------------------------|
| authorization_scope | #1 (0.345) | #6 (0.163) |
| incompleteness | #2 (0.275) | #1 (0.300) |
| lexical | #3 (0.260) | #2 (0.247) |
| scopal | #4 (0.255) | #5 (0.201) |
| coreferential | #5 (0.220) | #3 (0.225) |
| conditional_precedence | #6 (0.205) | #4 (0.220) |

**Spearman ρ = -0.029, p = 0.957** — 两组 ranking 无显著相关性。最大分歧在 `authorization_scope`：GPT-4.1 判为最高违规类型（#1, 34.5%），GPT-5.4 判为最低（#6, 16.3%）。中间类型（incompleteness, lexical）两组较一致，但 authorization_scope 的极端差异拉低了整体相关性。这暗示两个 judge 对 authorization_scope 违规的判定标准存在系统性差异。

---
