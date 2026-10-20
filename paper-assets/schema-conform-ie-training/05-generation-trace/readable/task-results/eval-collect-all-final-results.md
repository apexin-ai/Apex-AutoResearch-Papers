# eval collect all final results

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_all_final_results_20260513T230404_result.json`
- **Structured JSON:** [`bfe31ea58640f67a3ffc.json`](../../sessions/bf/bfe31ea58640f67a3ffc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇总

### 1. eval_B_v3 — **COMPLETED**

| Metric | scierc_test (n=551) | crossner_politics (n=651) | crossner_science (n=543) |
|--------|:--:|:--:|:--:|
| **entity_f1** | 0.4209 | 0.4187 | 0.5635 |
| **relation_f1** | 0.2348 | 0.0 | 0.0 |
| **f1_correctness** | 0.3349 | 0.3833 | 0.4335 |
| structural_validity | 0.9764 | 0.9969 | 0.9963 |
| type_conformance | 0.9559 | 0.9578 | 0.9177 |
| relational_constraint | 0.8361 | 0.0 | 0.0 |
| structural_completeness | 0.9564 | 0.9076 | 0.8447 |
| valid_json_rate | 0.9764 | 0.9969 | 0.9963 |

### 2. eval_A_continued_ckpt400 — **COMPLETED**

| Metric | scierc_test (n=551) | crossner_politics (n=651) | crossner_science (n=543) |
|--------|:--:|:--:|:--:|
| **entity_f1** | 0.5158 | 0.4816 | 0.6017 |
| **relation_f1** | 0.2951 | 0.0 | 0.0 |
| **f1_correctness** | 0.4175 | 0.4816 | 0.5956 |
| structural_validity | **1.0** | **1.0** | **1.0** |
| type_conformance | 0.9710 | 0.9998 | 0.9914 |
| relational_constraint | 0.7108 | 0.0 | 0.0 |
| structural_completeness | 0.9710 | 0.9995 | 0.9892 |
| valid_json_rate | **1.0** | **1.0** | **1.0** |

### 3. eval_A_continued_final — **RUNNING**

- 当前：**scierc_test** 数据集，**327/551** 样本（59%）
- 速率：~3-4s/sample
- 预计剩余 scierc：约 14 分钟
- 之后还需跑 crossner_politics (651) + crossner_science (543)，预计总剩余 **~1.5 小时**
- 模型：`/root/autodl-tmp/output/formal_A_continued/merged`
- 输出目录已创建但尚无 eval_results.json

### 关键对比

eval_A_continued_ckpt400 在所有指标上全面优于 eval_B_v3：
- entity_f1 提升：+9.5pp (scierc), +6.3pp (politics), +3.8pp (science)
- valid_json_rate 达到 **100%**（B_v3 为 97.6-99.7%）
- structural_validity 全部 **1.0**
- type_conformance / structural_completeness 也更高

---
