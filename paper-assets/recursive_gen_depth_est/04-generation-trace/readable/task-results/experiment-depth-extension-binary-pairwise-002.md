# experiment depth extension binary pairwise 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_depth_extension_binary_pairwise_002_20260515T060515_result.json`
- **Structured JSON:** [`d3476f38653e287f9edb.json`](../../sessions/d3/d3476f38653e287f9edb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。Registry 已更新为 DONE/success。

**结果摘要：**

| Pair | Binary AUC | 95% CI | 4-class ref | Δ |
|------|-----------|--------|------------|---|
| d1v2 | 0.9250 | [0.914, 0.935] | 0.8607 | +0.064 |
| d2v3 | 0.8225 | [0.805, 0.840] | 0.8005 | +0.022 |
| d3v4 | **0.7837** | [0.765, 0.802] | — | — |
| d4v5 | **0.6832** | [0.661, 0.705] | — | — |

**EDD = 4**：d3v4 AUC (0.784) > 0.75 阈值，d4v5 AUC (0.683) < 0.75 阈值。Binary classifiers 一致优于 4-class pipeline（消除了决策边界稀释效应）。d4 和 d5 之间的统计特征区分度明显下降，d5 生成文本在特征空间中趋于饱和。

注：原任务中 d4/d5 的 features 文件不存在，额外执行了 Pythia-1.4B 特征提取（`extract_features.py`）生成了 `features_depth_4.jsonl` 和 `features_depth_5.jsonl`。

---
