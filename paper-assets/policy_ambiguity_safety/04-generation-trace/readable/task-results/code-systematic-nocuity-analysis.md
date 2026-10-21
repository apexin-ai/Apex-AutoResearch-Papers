# code systematic nocuity analysis

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_systematic_nocuity_analysis_20260520T185148_result.json`
- **Structured JSON:** [`148456059e73d8901e0d.json`](../../sessions/14/148456059e73d8901e0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，输出保存到 `systematic_nocuity.json`。

核心结果：

- **Ambiguous convergent violation**: 28.7% (86/300) — 两模型在同一歧义条款上都产生 moderate+ 违规
- **Unambiguous control**: 1.0% (3/300) — 验证了歧义是违规的驱动因素
- **最危险类型**: `authorization_scope` (44%) > `incompleteness` (38%) > `scopal` (30%) > `conditional_precedence` (26%) > `lexical` (24%) > `coreferential` (10%)
- **严重度一致性**: convergent violations 中 67.4% 的 violation_level 完全相同，说明不仅方向一致，程度也一致

---
