# eval collect a continued final v3

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_a_continued_final_v3_20260513T232131_result.json`
- **Structured JSON:** [`2e6c9bf87ce44c1f7eed.json`](../../sessions/2e/2e6c9bf87ce44c1f7eed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### eval_A_continued_final 状态：**部分完成（killed）**

进程在 crossner_politics 评估到 ~9%（61/651）时被静默终止，日志中无 error/traceback/killed 信息，疑似 OOM。输出目录为空，未生成 eval_results.json。

### 已完成的 metrics（仅 scierc_test）

| Metric | scierc_test | crossner_politics | crossner_science |
|---|---|---|---|
| entity_f1 | 0.5172 | - | - |
| relation_f1 | 0.3004 | - | - |
| f1_correctness | 0.4185 | - | - |
| structural_validity | 1.0000 | - | - |
| type_conformance | 0.9814 | - | - |
| relational_constraint | 0.7102 | - | - |
| structural_completeness | 0.9819 | - | - |
| valid_json_rate | 1.0000 | - | - |

### 对比：eval_A_continued_ckpt400（完整完成）

| Metric | scierc_test | crossner_politics | crossner_science |
|---|---|---|---|
| entity_f1 | 0.5158 | 0.4816 | 0.6017 |
| relation_f1 | 0.2951 | 0.0000 | 0.0000 |
| f1_correctness | 0.4175 | 0.4816 | 0.5956 |
| structural_validity | 1.0000 | 1.0000 | 1.0000 |
| type_conformance | 0.9710 | 0.9998 | 0.9914 |
| relational_constraint | 0.7108 | 0.0000 | 0.0000 |
| structural_completeness | 0.9710 | 0.9995 | 0.9892 |
| valid_json_rate | 1.0000 | 1.0000 | 1.0000 |

### Registry 更新

- `eval_A_continued_final`: status=DONE, conclusion=killed, metrics 包含 scierc_test 完整指标 + failure_note

需要重跑 eval_A_continued_final 的 crossner_politics 和 crossner_science 才能获得完整结果。

---
