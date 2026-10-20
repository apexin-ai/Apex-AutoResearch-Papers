# eval collect A continued final results

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect_A_continued_final_results_20260514T004108_result.json`
- **Structured JSON:** [`cb07a14de89bd76c655d.json`](../../sessions/cb/cb07a14de89bd76c655d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已退出，评估成功完成。Registry 已更新（conclusion: killed → success，metrics 已补全）。

## eval_A_continued_final 完整结果

| 指标 | scierc_test (551) | crossner_politics (651) | crossner_science (543) |
|------|:-:|:-:|:-:|
| **entity_f1** | 0.5172 | 0.4784 | 0.5959 |
| **relation_f1** | 0.3004 | 0.0000 | 0.0000 |
| **f1_correctness** | 0.4185 | 0.4784 | 0.5891 |
| **structural_validity** | 1.0000 | 0.9985 | 1.0000 |
| **type_conformance** | 0.9814 | 0.9982 | 0.9917 |
| **relational_constraint** | 0.7102 | 0.0000 | 0.0000 |
| **structural_completeness** | 0.9819 | 0.9980 | 0.9892 |
| **valid_json_rate** | 1.0000 | 0.9985 | 1.0000 |

crossner 两个数据集的 relation_f1 和 relational_constraint 为 0，与 ckpt400 一致——这两个数据集本身不含关系标注，属于预期行为。

---
