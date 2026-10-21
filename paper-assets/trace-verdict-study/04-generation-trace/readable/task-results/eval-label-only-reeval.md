# eval label only reeval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_label_only_reeval_20260515T162632_result.json`
- **Structured JSON:** [`e172fdeef1219be0f2ec.json`](../../sessions/e1/e172fdeef1219be0f2ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 数据格式验证
训练日志确认：`label_only` 训练使用 **Condition: full_trace** 格式数据，`Label-only loss: True` 仅改变 loss mask。用 `--condition full_trace` 评估是正确的。

### 2. Old vs New accuracy

| 指标 | Old (eval_results.json) | New (eval_results_v2.json) | Δ |
|------|------------------------|---------------------------|---|
| **Accuracy** | 86.22% | 86.22% | **0.00pp** |
| Majority baseline | 71.51% | 71.51% | 0.00pp |
| Lift | +14.71pp | +14.71pp | 0.00pp |

**结果完全一致，Δ = 0。**

### 3. Per-class metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 0.88 | 0.93 | 0.91 |
| fail | 0.80 | 0.69 | 0.74 |

95% CI: accuracy [84.4%, 88.1%]

### 4. predictions.jsonl
行数 = **1190** ✓

### 结论
旧评估（用 `full_trace_label_only` condition）和新评估（用 `full_trace` condition）结果完全相同。旧版 evaluate.py 虽然不识别 `label_only` condition 名，但数据处理逻辑与 `full_trace` 一致，因此 86.22% 这个数字本身就是正确的。registry 无需修正。

---
