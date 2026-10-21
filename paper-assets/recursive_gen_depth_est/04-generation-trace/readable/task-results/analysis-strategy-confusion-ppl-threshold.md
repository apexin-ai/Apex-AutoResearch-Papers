# analysis strategy confusion ppl threshold

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_strategy_confusion_ppl_threshold_20260518T142943_result.json`
- **Structured JSON:** [`41525191d4beb15fd349.json`](../../sessions/41/41525191d4beb15fd349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务全部完成。结果汇总：

---

## Task A: Strategy Confusion Matrix + Routing Error

**聚合混淆矩阵** (3 models, 5-fold CV, N=180,000):

| True \ Pred | nucleus | temp09 | topk50 | Recall |
|------------|---------|--------|--------|--------|
| **nucleus** | 39,700 | 9,819 | 10,481 | **0.662** |
| **temp09** | 9,804 | 28,003 | 22,193 | **0.467** |
| **topk50** | 8,934 | 15,271 | 35,795 | **0.597** |

**Pairwise Confusion Rate:**
- temp09 vs topk50: **31.2%** (最严重)
- nucleus vs temp09: 16.4%
- nucleus vs topk50: 16.2%

temp09 和 topk50 之间的混淆占主导，nucleus 最容易被正确识别(尤其 GPT-2 XL recall=84.5%)。

**Routing Error Analysis (mean across 3 models):**
| Metric | Value |
|--------|-------|
| Oracle depth acc | 0.7837 |
| Pipeline depth acc | 0.7062 |
| Correct route depth acc | 0.7219 |
| Wrong route depth acc | 0.6759 |
| Gap (oracle - pipeline) | **0.0774** |

---

## Task B: PPL Threshold vs RF Depth Filter

**Binary task: d0 vs d1+**, 180k samples (9 cells), d1+ ppl 低于 d0（递归生成使文本更可预测）。

| Method | Precision | Recall | F1 | AUC |
|--------|-----------|--------|------|------|
| PPL threshold (median d0) | 0.8356 | 0.8470 | 0.8413 | 0.8521 |
| PPL threshold (ROC optimal) | 0.9893 | 0.7366 | 0.8445 | 0.8521 |
| **RF 19-feature** | **0.9988** | **0.9951** | **0.9970** | **0.9998** |

RF 比最佳 PPL 阈值高 **+0.15 F1, +0.15 AUC**。有趣的是 p90_ppl (AUC=0.986) 和 var_surprisal (AUC=0.976) 比 mean_ppl 强很多，说明 19 维特征提供了远超单一 ppl 的判别力。

结果已保存到:
- `results/reviewer_metrics/strategy_confusion.json`
- `results/reviewer_metrics/ppl_threshold_baseline.json`

---
