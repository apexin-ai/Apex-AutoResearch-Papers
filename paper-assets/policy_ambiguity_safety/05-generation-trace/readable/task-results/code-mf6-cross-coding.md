# code mf6 cross coding

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf6_cross_coding_20260520T171218_result.json`
- **Structured JSON:** [`53dab9f1c882385fda02.json`](../../sessions/53/53dab9f1c882385fda02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF-6 完成。结果：

- **Cohen's κ = 0.5352**（moderate agreement），66.7% overall agreement
- 60 条样本（每种 ambiguity_type ≥ 5 条），0 个 parse error
- **Per-category**：`scope_misapplication` 一致性最高（94.4%），`assumption_based_action` 最低（47.4%）——gpt-4.1 倾向将部分 assumption_based_action 重标为 scope_misapplication
- **Cross-model dominant mode**：5/6 types 一致，唯一不一致的是 coreferential（gpt-5.4: scope_misapplication, gpt-4.1: assumption_based_action）

输出文件：
- `plan_005/cross_coding_agreement.json`
- `plan_005/cross_coding_recoded.jsonl`（60 条 gpt-4.1 重编码原始结果）
- `plan_005/run_cross_coding.py`（可复现脚本）

---
