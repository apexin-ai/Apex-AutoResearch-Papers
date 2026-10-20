# eval check a continued final

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_a_continued_final_20260513T231033_result.json`
- **Structured JSON:** [`ed53622accea0161df4c.json`](../../sessions/ed/ed53622accea0161df4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_A_continued_final **仍在运行中**。

当前状态：
- 正在评估第 1/3 个数据集：**scierc_test** — 435/551 (79%)
- 剩余数据集：**crossner_politics** (651 samples), **crossner_science** (543 samples)

预估剩余时间（按 ~3.5 s/sample）：
- scierc_test 剩余 116 samples → ~7 min
- crossner_politics 651 samples → ~38 min
- crossner_science 543 samples → ~32 min
- **总计约 77 分钟（~1h17min）**

作为参考，ckpt400 的完整结果（3 个数据集，同样的评估配置）：

| 数据集 | entity_f1 | relation_f1 | f1_correctness | structural_validity | type_conformance | relational_constraint | structural_completeness | valid_json_rate |
|--------|-----------|-------------|----------------|--------------------|-----------------|-----------------------|------------------------|----------------|
| scierc_test (551) | 0.5158 | 0.2951 | 0.4175 | 1.0 | 0.971 | 0.7108 | 0.971 | 1.0 |
| crossner_politics (651) | 0.4816 | 0.0 | 0.4816 | 1.0 | 0.9998 | 0.0 | 0.9995 | 1.0 |
| crossner_science (543) | 0.6017 | 0.0 | 0.5956 | 1.0 | 0.9914 | 0.0 | 0.9892 | 1.0 |

eval_A_continued_final 预计在约 1h15min 后完成（~UTC 08:15）。

---
