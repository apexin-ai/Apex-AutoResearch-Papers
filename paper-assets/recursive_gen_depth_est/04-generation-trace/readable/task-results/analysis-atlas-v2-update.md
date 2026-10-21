# analysis atlas v2 update

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_atlas_v2_update_20260515T020132_result.json`
- **Structured JSON:** [`09a5112e37d682fa669c.json`](../../sessions/09/09a5112e37d682fa669c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。`artifacts/atlas_v2/` 下 29 个文件。

## 产出总结

**`artifacts/atlas_v2/`** 包含：

### 数据文件
| 文件 | 内容 |
|------|------|
| `atlas_v2_data.json` | 8/9 cells 完整数据（含 olmo_topk50） |
| `atlas_v2_results.json` | 全量分析结果 |
| `edd_sensitivity.json` | 4 threshold × 8 cell EDD 矩阵 |
| `monotonicity_scores.json` | 19 features × 8 cells 单调性 |
| `atlas_summary.json` | feature-level 分析 |

### 图表（PDF+PNG）
signal_strength_heatmap, edd_barchart, edd_sensitivity_heatmap, feature_evolution, feature_evolution_normalized, monotonicity_heatmap, universal_feature_ranking, cross_model_rank_correlation, feature_clustering_pca, feature_clustering_t-sne, consistency_heatmap

### 关键发现

**EDD Threshold Sensitivity**:
| Threshold | Mean EDD | 掉档 cells |
|-----------|----------|------------|
| τ=0.65 | 3.0 | 无 |
| τ=0.70 | 2.88 | pythia_topk50→2 |
| τ=0.75 | 2.75 | +olmo_topk50→2 |
| τ=0.80 | 2.50 | +pythia_temp09→2, pythia_topk50→1 |

- **Top-k 解码最脆弱**：pythia_topk50 是唯一一个 EDD 降到 1 的 cell
- **GPT-2 XL 最稳健**：全 threshold 下均保持 EDD=3
- Universal top-5 features：p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl

---
