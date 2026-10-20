# eval check all evals status

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_all_evals_status_20260513T105343_result.json`
- **Structured JSON:** [`3ab522b664fe79565362.json`](../../sessions/3a/3ab522b664fe79565362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. eval_D2_ckpt400 — 运行中 (cuda:0)

scierc_test (551 samples) **已完成**，crossner_politics (651 samples) 进行中 ~12%，crossner_science 未开始。

**scierc_test 结果：**

| Metric | Value |
|--------|-------|
| entity_f1 | 0.5325 ± 0.3047 |
| relation_f1 | 0.2379 ± 0.3517 |
| f1_correctness | 0.3912 ± 0.2619 |
| structural_validity | 1.0000 ± 0.0000 |
| type_conformance | 0.9873 ± 0.1120 |
| relational_constraint | 0.9180 ± 0.2687 |
| structural_completeness | 0.9873 ± 0.1120 |
| valid_json_rate | 1.0000 ± 0.0000 |

预计剩余：crossner_politics ~38min + crossner_science ~44min ≈ **~80min**

### 2. eval_D2_final — 未开始

日志文件不存在。串行排在 D2_ckpt400 之后，预计 ~80min 后启动，自身需 ~2h。

### 3. eval_D1_v4 — 运行中 (cuda:1)

scierc_test 进行中 43/551 (~8%)，~5-6s/it。crossner_politics、crossner_science 未开始。

预计剩余：scierc_test ~42min + crossner_politics ~44min + crossner_science ~44min ≈ **~130min**

---
