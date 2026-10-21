# analysis alpha eff vs true alpha

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_eff_vs_true_alpha_20260518T064839_result.json`
- **Structured JSON:** [`da9f528b4f71968a0cbe.json`](../../sessions/da/da9f528b4f71968a0cbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。JSON 已保存至 `/root/provenance_weight_training/alpha_eff_analysis.json`。

## 结果摘要

### 数据概况
- 371,499 样本（非 247,666，可能之前说的是 ρ=0.4 的子集计数有误）
- Real: 164,889 (44.4%), Synthetic: 206,610 (55.6%)
- 标签判断方式：`depth==0` 为 real，`depth==1` 为 synthetic

### 样本级：r_i = 1[q_i ≤ 0.5] vs ground truth

| 指标 | 值 |
|---|---|
| Accuracy | **85.8%** |
| Precision | 86.4% |
| Recall | 80.6% |
| F1 | 83.4% |

**Confusion matrix**: TP=132,895 / FP=20,830 / FN=31,994 / TN=185,780

**分区间准确率**：
| q-score 区间 | 准确率 | 样本数 | 真实分布 |
|---|---|---|---|
| [0, 0.2) | **91.6%** | 91,654 | 91.6% real |
| [0.2, 0.5) | **78.8%** | 62,071 | 78.8% real |
| [0.5, 0.8) | **50.5%** | 48,730 | ~50/50 混合 |
| [0.8, 1.0] | **95.3%** | 169,044 | 95.3% synthetic |

不确定区间 [0.2, 0.8) 整体准确率：**66.4%**（110,801 样本）。**核心弱区是 [0.5, 0.8)**，接近随机猜测。

### Batch 级：α_eff vs true_α

| 指标 | 值 |
|---|---|
| Pearson r | **0.724** |
| Spearman r | **0.713** |
| MAE | **0.073** |
| α_eff 均值±标准差 | 0.409 ± 0.125 |
| true_α 均值±标准差 | 0.439 ± 0.124 |

### 对审稿人 Q2 的回答要点

1. **样本级准确率 85.8%**，detector 的二值化近似整体可靠
2. **高置信区间（q < 0.2 和 q > 0.8，覆盖 70.2% 样本）准确率 > 91%**，大多数样本的标签近似是准确的
3. **不确定区间 [0.5, 0.8) 约 13% 的样本接近随机**，这是主要噪声来源
4. **Batch 级 Pearson r=0.72, MAE=0.073**，α_eff 与 true_α 高度相关，batch 级聚合进一步平滑了样本级噪声
5. α_eff 略低估 true_α（0.409 vs 0.439），即 detector 倾向于把一些 real 误判为 synthetic，但偏差仅约 3 个百分点

---
