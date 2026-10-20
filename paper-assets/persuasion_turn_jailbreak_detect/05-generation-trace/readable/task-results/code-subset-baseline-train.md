# code subset baseline train

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_subset-baseline-train_20260517T080317_result.json`
- **Structured JSON:** [`eec066006717503c3eb1.json`](../../sessions/ee/eec066006717503c3eb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成。结果汇总：

## Subset 数据统计

| Split | persuasion-based | benign | Total |
|-------|-----------------|--------|-------|
| Train | 94 | 175 | 269 |
| Val | 20 | 38 | 58 |
| Test | 21 | 37 | 58 |

## Test 结果

| Metric | Value |
|--------|-------|
| **Test F1 (macro)** | **1.0000** |
| **Test Accuracy** | **1.0000** |
| Precision (benign) | 1.0000 |
| Recall (benign) | 1.0000 |
| Precision (jailbreak) | 1.0000 |
| Recall (jailbreak) | 1.0000 |
| **FPR@95TPR** | **0.0000** |

## 与 Full-dataset Baseline 对比

| | Full Dataset | Subset (persuasion+benign) |
|---|---|---|
| F1 (macro) | 0.987 | 1.000 |
| Delta | — | +0.013 |

Subset baseline 在 test set 上达到完美分类。这符合预期：去掉 cipher-based 样本后，persuasion-based 和 benign 之间的区分度更高（cipher-based 是 full dataset 中主要的混淆源）。test set 仅 58 条，完美分数需要注意小样本方差。

产出文件：
- `data/embeddings/subset_baseline_{train,val,test}.pt`
- `checkpoints/subset_baseline_gru/best.pt`
- `checkpoints/subset_baseline_gru/test_results.json`

---
