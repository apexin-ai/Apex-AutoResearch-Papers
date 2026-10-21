# exp ablation pca supplement

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_ablation_pca_supplement_20260515T173806_result.json`
- **Structured JSON:** [`7e1c2b26411b159027d5.json`](../../sessions/7e/7e1c2b26411b159027d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### PCA 有效维度
| 阈值 | 9 cell 平均 | 范围 | merged_all |
|------|------------|------|-----------|
| 90% | 6-7 pc | 6–7 | 7 |
| 95% | 7-9 pc | 7–9 | 9 |
| 99% | 11-13 pc | 11–13 | 13 |

19 维特征中，**6-7 个主成分就能解释 90% 方差**，说明特征空间存在显著冗余。

### Leave-one-group-out（按影响力排序，mean Δacc across 9 cells）
| 排除组 | 特征数 | mean Δ |
|--------|--------|--------|
| **perplexity** | 9 | **-0.0353** |
| surprisal | 3 | -0.0054 |
| repetition | 3 | -0.0022 |
| lexical_diversity | 2 | -0.0010 |
| ngram_entropy | 2 | -0.0006 |

**Perplexity 组是最关键的特征组**，排除后准确率平均下降 3.5%，远超其他组。Surprisal 次之但影响较小 (-0.54%)。Lexical diversity 和 ngram entropy 几乎不影响性能。

### 产出文件
- `results/feature_ablation/pca_effective_dims.json`
- `results/feature_ablation/leave_one_group_out.json`
- `results/feature_ablation/pca_scree_plot.pdf` / `.png`
- `src/pca_effective_dims.py`
- `src/leave_one_group_out.py`

---
