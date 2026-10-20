# eval check ab v3 results

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_ab_v3_results_20260513T193856_result.json`
- **Structured JSON:** [`8f211d20932b593e864f.json`](../../sessions/8f/8f211d20932b593e864f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### eval_A_v3: **COMPLETED**

| Metric | scierc_test (n=551) | crossner_politics (n=651) | crossner_science (n=543) |
|---|---|---|---|
| entity_f1 | 0.4404 | 0.4460 | 0.5697 |
| relation_f1 | 0.1810 | N/A | N/A |
| f1_correctness | 0.3395 | 0.4460 | 0.5697 |
| structural_validity | 1.0000 | 1.0000 | 1.0000 |
| type_conformance | 0.9002 | 1.0000 | 0.9842 |
| relational_constraint | 0.3371 | 0.0000 | 0.0000 |
| structural_completeness | 0.9002 | 1.0000 | 0.9945 |
| valid_json_rate | 1.0000 | 1.0000 | 1.0000 |

### eval_B_v3: **RUNNING**

正在评估 scierc_test，进度 26/551（~5%）。模型加载自 `/root/autodl-tmp/output/formal_B/merged`。结果目录已创建但为空。

### train_A_continued: **RUNNING**

进度 **296/500**（~59%），约 1h57m 已过，预计剩余 ~1h06m。

---
