# analysis mvp evaluation full

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-evaluation-full_20260514T135351_result.json`
- **Structured JSON:** [`ba61d7084642422e1d24.json`](../../sessions/ba/ba61d7084642422e1d24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是汇总结果。

---

```
=== 数据统计 ===
每个 depth 样本数: depth-0=5000, depth-1=5000, depth-2=5000, depth-3=5000
每个 depth 代码污染率: depth-0=0.4%, depth-1=15.4%, depth-2=20.0%, depth-3=24.4%
特征维度: 19
截断长度: 498 tokens

=== 全量结果 (最佳模型) ===
模型: Random Forest
4-class accuracy: 78.2% (chance: 25.0%), 95% CI: [76.9%, 79.4%]
MAE: 0.2367
Adjacent AUC: 0v1=0.9975, 1v2=0.8607, 2v3=0.8005
Top-5 features: var_surprisal(0.1692), p90_ppl(0.1582), mean_ppl(0.1204), mean_surprisal(0.0884), p75_ppl(0.0671)
Confusion matrix:
          pred-0  pred-1  pred-2  pred-3
  depth-0:  999       1       0       0
  depth-1:    6     812     145      37
  depth-2:    1     127     578     294
  depth-3:    1      33     229     737

=== 过滤后结果 (仅自然语言) ===
过滤前/后样本数: 20000 → 16993 (3007 removed)
  depth-0: 5000→4981 (99.6%), depth-1: 5000→4231 (84.6%), depth-2: 5000→4002 (80.0%), depth-3: 5000→3779 (75.6%*)
  *depth-3 保留率低于 80%，代码污染较重
4-class accuracy: 81.6% (chance: 25.0%), 95% CI: [80.3%, 82.9%]
MAE: 0.1995
Adjacent AUC: 0v1=0.9977, 1v2=0.8782, 2v3=0.8323
Confusion matrix:
          pred-0  pred-1  pred-2  pred-3
  depth-0:  991       2       2       1
  depth-1:    6     699     119      22
  depth-2:    2      91     513     195
  depth-3:    1      21     165     569

=== MVP 判定 ===
全量 4-class acc > 40%: YES (78.2%)
过滤后 4-class acc > 35%: YES (81.6%)
depth-1 vs depth-2 AUC > 0.6: YES (0.8607 全量 / 0.8782 过滤后)
最终判定: PASS
```

**关键发现**：过滤代码样本后准确率从 78.2% **提升**到 81.6%，AUC 也全面提升。这说明代码内容是噪声而非分类的信号来源——分类器依赖的是文本统计特征（perplexity 分布、surprisal 方差等），而非内容类型差异。控制实验有力地排除了 content-type 混淆。

---
