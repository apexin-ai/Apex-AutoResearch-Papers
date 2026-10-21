# data feat ablation artifact

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_feat_ablation_artifact_20260515T194617_result.json`
- **Structured JSON:** [`97ad0722b40afe504b7d.json`](../../sessions/97/97ad0722b40afe504b7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 注册成功：`art_20260515_2649b4`

数据摘要：

| 数据项 | 覆盖 | 关键数字 |
|--------|------|----------|
| **Top-k Curve** | 9/9 cell | mean acc: top1=0.646 → top5=0.765 → top19=0.784 |
| **Per-Category** | 9/9 cell | perplexity(0.766) > surprisal(0.732) >> lexical(0.461) > repetition(0.437) > ngram_entropy(0.395) |
| **Forward Selection** | 7/9 cell | var_surprisal 或 p90_ppl 始终排第一 |
| **VIF** | 7/9 cell | 16/19 特征 VIF>10，严重多重共线性 |
| **PCA** | 9/9 cell | 95% 方差需 8.1 个 PC（范围 7-9） |

注意：gpt2xl_temp09 和 gpt2xl_topk50 的 forward_selection 和 VIF 数据缺失（旧版实验未生成），其余数据从 v1/v2 两版文件合并而来。

---
