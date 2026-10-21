# code plan 006 reliability api

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_006_reliability_api_20260520T160757_result.json`
- **Structured JSON:** [`1021cb41ed3cf3d7bc64.json`](../../sessions/10/1021cb41ed3cf3d7bc64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 006 完成。所有 5 步全部成功，0 错误。

**结果摘要：**

| 指标 | ICC(2,1) | 95% CI | 解释 |
|------|---------|--------|------|
| **Overall** | **0.9191** | [0.8924, 0.9404] | excellent |
| **Binary (moderate+)** | **0.8465** | [0.7991, 0.8854] | good |

**Per-type ICC：**
| 类型 | ICC | 解释 |
|------|-----|------|
| scopal | 0.9893 | excellent |
| lexical | 0.9813 | excellent |
| coreferential | 0.9761 | excellent |
| authorization_scope | 0.8567 | good |
| conditional_precedence | 0.8559 | good |
| incompleteness | 0.807 | good |

**Per-model ICC：** gpt-5.4 = 0.921, gpt-4.1 = 0.918（均 excellent）

**Exact agreement：** 102/120 groups (85.0%)

实验可复现性很强。360 episodes / 360 judgments / 120 complete groups 全部到位。产出文件：
- `plan_006/selected_clauses.json`
- `plan_006/episodes_api.jsonl`
- `plan_006/judgments_api.jsonl`
- `plan_006/icc_results.json`

---
