# code plan 005 error analysis

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_error_analysis_20260520T152427_result.json`
- **Structured JSON:** [`ecf5dc157b73ab01a5cb.json`](../../sessions/ec/ecf5dc157b73ab01a5cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_005 完成。123 条 violation traces 全部标注成功，0 parse errors。

关键发现：

| ambiguity_type | n | 主要 failure_mode | awareness rate |
|---|---|---|---|
| authorization_scope | 32 | unauthorized_escalation (71.9%) | 3.1% |
| conditional_precedence | 17 | scope_misapplication (41.2%) | 11.8% |
| coreferential | 9 | scope_misapplication (44.4%) | 0.0% |
| incompleteness | 23 | assumption_based_action (60.9%) | 4.3% |
| lexical | 21 | assumption_based_action (71.4%) | 4.8% |
| scopal | 21 | scope_misapplication (76.2%) | 0.0% |

Cross-type highlights:
- **scope_misapplication**: ling-layer avg 46.5% vs spec-layer 18.1% — ling 层歧义确实更多触发作用域误判
- **assumption_based_action**: spec/ling 层接近（31.6% vs 29.1%），lexical 异常高（71.4%）
- **conservative_refusal**: coreferential 11.1% vs 其他 avg 3.0% — 部分解释了 coreferential 低 violation rate
- **disambiguation awareness 极低**：整体 <5%，agent 几乎从不意识到歧义存在

输出文件：`plan_005/failure_modes.jsonl`、`plan_005/summary.json`

---
