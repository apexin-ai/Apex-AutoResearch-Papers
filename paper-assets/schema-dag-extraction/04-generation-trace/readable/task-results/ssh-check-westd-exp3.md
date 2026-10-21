# ssh check westd exp3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_exp3_20260517T121744_result.json`
- **Structured JSON:** [`1b746f73ba9c1a7cc581.json`](../../sessions/1b/1b746f73ba9c1a7cc581.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. 状态：已完成

所有 6 个 count levels × 25 batches 均已成功完成，结果文件齐全。tmux session 已自动退出。完成时间：2026-05-17 20:01。

### 2. GPU 状态

2× NVIDIA RTX PRO 6000 Blackwell (98GB each)，当前完全空闲，0% 利用率，0MiB 占用。

### 3. 结果数据（summary.json）

| Count Level | Mean Recall | Std | n_batches |
|-------------|-------------|-----|-----------|
| count_2 | 0.9623 | 0.0571 | 25 |
| count_6 | 0.9024 | 0.0640 | 25 |
| count_12 | 0.8293 | 0.0612 | 25 |
| count_22 | 0.6840 | 0.0837 | 25 |
| count_44 | 0.5309 | 0.0470 | 25 |
| count_66 | 0.4072 | 0.0004 | 25 |

### 4. Metric 类型问题：text-only recall（非 type+text match）

`evaluate_ner_results` 函数（第 250-280 行）的逻辑：

```python
gold_texts = set(e["text"].lower() for e in gold_entities
                 if e["type"] in set(r["batch_types"]))
pred_texts = set(p["text"].lower() for p in preds if isinstance(p, dict))
recall = len(gold_texts & pred_texts) / len(gold_texts)
```

这是 **text-only recall**：只检查预测文本是否匹配 gold 文本，没有验证预测的类型是否正确。gold 端按 batch_types 过滤了类型，但 pred 端只取了 `p["text"]`，没有检查 `p["type"]` 是否与 gold entity 的类型一致。

**需要重新评估**。要实现 type+text match，评估逻辑应改为比较 `(type, text)` 对而非仅 text。

### 修复方案

需要在 `/root/schema-dag-extraction/scripts/run_d051_count_curves_llama70b.py` 的 `evaluate_ner_results` 函数中修改评估逻辑，将匹配条件从纯文本改为 (type, text) 对匹配，然后对已有的 6 个 `results_count_*.jsonl` 文件重新跑评估（不需要重新推理，结果文件中已包含 `batch_types` 和 `predictions` 信息）。需确认 predictions 中每条记录是否存储了预测的 type 字段（`p["type"]`）。

---
