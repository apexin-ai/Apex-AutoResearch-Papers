# code mitigation experiment v2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mitigation_experiment_v2_20260522T055629_result.json`
- **Structured JSON:** [`03cb6040a9f8dcbef73e.json`](../../sessions/03/03cb6040a9f8dcbef73e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证通过：

- `generic_awareness` = 300 episodes (6 types x 50)
- `type_specific_incompleteness` = 50, `type_specific_auth_scope` = 50, `type_specific_lexical` = 50
- Total = 450 new episodes + 450 judge calls
- Baseline 300 条 ambiguous judgments 正确读取
- Mitigation prompt 正确插入 `&lt;instructions>` 块内、agent_instruction 之后

三个文件已就绪：
- `run_mitigation_v2.py` — 完整实验脚本（含 episode 执行 / judge / McNemar 分析 / resume / dry-run）
- `expected_output_schema.json` — 输出 JSON Schema
- `README.md` — 实验设计与运行说明

注意：使用了 `clause_templates_full_28b249.json`（300 clauses, 6 types）而非任务中引用的 `clause_templates_full.json`（250 clauses, 缺 coreferential），因为 baseline 数据包含 coreferential 类型。

---
