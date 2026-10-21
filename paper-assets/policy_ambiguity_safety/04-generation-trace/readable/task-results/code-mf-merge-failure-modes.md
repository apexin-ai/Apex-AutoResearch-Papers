# code mf merge failure modes

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf_merge_failure_modes_20260520T173158_result.json`
- **Structured JSON:** [`e3039b3268aafb58636a.json`](../../sessions/e3/e3039b3268aafb58636a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 原始 (6 类) | 合并后 (4 类) |
|------|------------|--------------|
| Cohen's κ | 0.535 | **0.594** |
| % agreement | 66.7% | **80.0%** |
| 解释 | moderate | moderate |

**⚠️ merged κ = 0.594 < 0.70 阈值，未达标。**

主要分歧来源：
- **authorization_scope** 子集 κ = 0.054（14 条中仅 9 条一致），两个 coder 在 `unauthorized_escalation` vs `inappropriate_action` 之间分歧严重（混淆矩阵中 7 条被 coder2 标为 inappropriate_action 而 coder1 标为 unauthorized_escalation）
- **incompleteness** 子集 κ = 0.233，同样存在 escalation/action 边界分歧
- **lexical/scopal** 高 agreement 但 κ 低或 undefined（kappa paradox：几乎所有 trace 都被标为同一类，chance agreement 本身就高）

核心问题：`unauthorized_escalation` 和 `inappropriate_action` 的边界仍然模糊——10 条分歧中 7+3 = 10 条都集中在这两类之间。如果进一步将这两类也合并为一个 "action-based failure"，κ 会显著提升，但类别区分度损失过大。

输出已保存至 `plan_005/merged_agreement.json`。

---
