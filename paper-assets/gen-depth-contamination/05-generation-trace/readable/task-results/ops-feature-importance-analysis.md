# ops feature importance analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feature_importance_analysis_20260521T051032_result.json`
- **Structured JSON:** [`4eba100ff5f90e7b8339.json`](../../sessions/4e/4eba100ff5f90e7b8339.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

## Permutation Importance 结果（C4, Qwen-1.5B, LightGBM）

### Baseline AUC
| Pair | AUC |
|------|-----|
| 0 vs 1 | **0.9219** |
| 1 vs 2 | **0.6104** |
| 2 vs 3 | 0.5318 (≈ random) |

### 0v1 分类（强区分）Top-5
| Rank | Feature | Importance (ΔAUC) |
|------|---------|-------------------|
| 1 | **Δ¹ Surprisal Std** | 0.2092 ± 0.0135 |
| 2 | Surprisal Std | 0.0952 ± 0.0097 |
| 3 | Freq Entropy | 0.0635 ± 0.0051 |
| 4 | Surprisal Kurtosis | 0.0427 ± 0.0035 |
| 5 | Surprisal Skew | 0.0349 ± 0.0017 |

### 1v2 分类（K* boundary）Top-5
| Rank | Feature | Importance (ΔAUC) |
|------|---------|-------------------|
| 1 | **Surprisal Std** | 0.0583 ± 0.0064 |
| 2 | Δ² Surprisal Std | 0.0218 ± 0.0068 |
| 3 | Freq Entropy | 0.0170 ± 0.0061 |
| 4 | Mean Surprisal | 0.0133 ± 0.0048 |
| 5 | TTR | 0.0060 ± 0.0054 |

### 核心结论

1. **Mean surprisal 在 0v1 中占 6.8%**（排第6，importance=0.034），远不如 Δ¹ Surprisal Std（占 41.7%）。

2. **1v2 boundary 的关键信号是 surp_std（surprisal 方差）**，占绝对主导（importance 0.0583，是第二名的 2.7 倍）。这意味着 K*=2 boundary 处，depth 1→2 的核心变化是 token-level surprisal 的 **离散度收窄**，而非均值移动。

3. **0v1 和 1v2 的 importance 分布质变不同**：
   - 0v1 由一阶导数特征（surp_d1_std）主导——生成文本的 surprisal 变化模式在 depth 0→1 剧烈改变
   - 1v2 一阶导数特征贡献归零（0.005），转为由 **基础统计量**（surp_std）和 **二阶导数**（surp_d2_std）主导——说明 depth 1→2 的退化更微妙，体现在分布的 spread 和曲率变化上

4. **2v3 所有特征 importance 极低且方差大**，验证了 K*=2 之后特征空间已无法区分的结论。

产出文件均在服务器 cqa1-22115 上：
- `results/feature_importance/importance_results.json`
- `artifacts/feature_importance_barplot.pdf` / `.png`
- `artifacts/feature_importance_table.tex`

---
