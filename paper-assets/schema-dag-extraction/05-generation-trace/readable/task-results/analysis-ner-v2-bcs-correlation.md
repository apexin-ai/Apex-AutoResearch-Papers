# analysis ner v2 bcs correlation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ner_v2_bcs_correlation_20260516T034616_result.json`
- **Structured JSON:** [`9adaeb333fb2403e570d.json`](../../sessions/9a/9adaeb333fb2403e570d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已保存。结果摘要：

**v2 BCS-F1 相关性**（NER prompt v2, text+type only）：
| | Pearson r | p | Bootstrap 95% CI |
|---|---|---|---|
| count_6 (n=27) | +0.27 | 0.176 | [-0.19, 0.64] |
| count_12 (n=27) | **+0.58** | **0.002** | [0.19, 0.81] |
| pooled (n=54) | +0.25 | 0.064 | [-0.07, 0.55] |

**v1 vs v2 对比**（count_12）：
- v1: r=+0.50 (p=0.008) — 来自 D005 决策记录
- v2: r=+0.58 (p=0.002)
- **方向一致**，均为正相关（高 BCS → 高 F1）

**关键判断**：无风险。v1 和 v2 方向一致，但注意这个正相关方向本身与朴素 confusability 假设相反。D008 已确认这是 type frequency confound（高 BCS batch 恰好包含高频类型），不影响论文叙事——论文主要证据是 pairwise SCS→confusion 分析（Channel 1），不依赖 batch-level BCS-F1。

**注意**：v1 原始 per-batch 数据被 v2 运行覆盖（服务器无 git），v1 统计量来自 D005 决策记录。

---
