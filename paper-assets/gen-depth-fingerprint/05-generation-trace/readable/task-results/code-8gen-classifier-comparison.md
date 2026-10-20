# code 8gen classifier comparison

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-classifier-comparison_20260516T145918_result.json`
- **Structured JSON:** [`2cf74ff7971c6715c8a9.json`](../../sessions/2c/2cf74ff7971c6715c8a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已保存到 `results/8gen_classifier_comparison.json`。

**结果摘要：**

| Classifier | 3-class F1 | 95% CI | Binary F1 | 95% CI |
|---|---|---|---|---|
| **XGBoost** | **0.7698** | [0.7636, 0.7715] | **0.7014** | [0.6943, 0.7057] |
| RandomForest | 0.7244 | [0.7168, 0.7258] | 0.6965 | [0.6902, 0.7008] |
| LogisticRegression | 0.7081 | [0.7014, 0.7108] | 0.7009 | [0.6951, 0.7058] |

- Best classifier: **XGBoost**（3-class 比 RF 高 +4.5pp，比 LR 高 +6.2pp）
- XGBoost 3-class F1 = 0.7698，在预期范围（0.75–0.78）内
- Binary 任务中三者差距缩小（XGBoost 仅微弱领先 LR +0.05pp），说明 XGBoost 的优势主要来自多类别分离能力

---
