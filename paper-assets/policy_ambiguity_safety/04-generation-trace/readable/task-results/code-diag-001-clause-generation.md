# code diag 001 clause generation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diag_001_clause_generation_20260520T102528_result.json`
- **Structured JSON:** [`dc2cda2bd9449ac96c07.json`](../../sessions/dc/dc2cda2bd9449ac96c07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`clause_templates_diag001.json` 已生成并注册。

**验证结果汇总**：
- 100 条，两种类型：`conditional_precedence` (50) + `scopal` (50)
- 所有条目含必需字段（ambiguous_clause, unambiguous_clause, user_scenario, tools, tool_responses, stripped_tool_desc）
- 所有 CP 条目 ambiguous_clause 含 ≥2 条冲突规则，unambiguous_clause 明确解决优先级
- 所有新生成条目 tool_responses ≥3（现有 scopal 001-030 保持原样，部分为 2）
- CP 子类型覆盖：lex specialis (~16), temporal priority (~10), authority-level (~12), exception vs exception (~12)
- 领域分布：retail/airline 大致均衡

---
