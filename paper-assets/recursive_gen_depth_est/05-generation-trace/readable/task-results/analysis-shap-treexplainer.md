# analysis shap treexplainer

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_shap-treexplainer_20260515T191657_result.json`
- **Structured JSON:** [`2768b03fab7e842a6f23.json`](../../sessions/27/2768b03fab7e842a6f23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

## SHAP TreeExplainer 9-Cell Analysis (R3-N3)

**三方法一致性极高，完全替代 attention-importance 方法：**

| 指标 | 值 |
|------|------|
| Kendall's W (SHAP/Gini/Perm) | **0.8955** (range 0.85–0.93) |
| ρ(SHAP, Gini) | **0.9312** |
| ρ(SHAP, Perm) | **0.8392** |
| 跨 cell SHAP 一致性 | mean ρ=0.80 |

**Top-2 特征稳定性 (SHAP)**：
- p90_ppl: **9/9** cells (100%)
- var_surprisal: **8/9** cells (89%)

**SHAP 聚合 Top-5**: p90_ppl → var_surprisal → p75_ppl → mean_surprisal → mean_ppl

**PPL/surprisal 特征占 SHAP importance 的 88.8%**

**产出文件** (`results/shap_analysis/`):
- `concordance_summary.json` — 三方法统计
- `three_way_comparison.json` — per-cell per-feature 三方法排名
- `beeswarm_{pythia,gpt2xl,olmo}_nucleus095.png` — 3 个 beeswarm 图
- `cross_cell_shap_consistency.png` — 跨 cell 一致性热力图
- 此前已有: bar plots, heatmap, scatter 等

**对 rebuttal 的价值**: 三种数学上独立的方法 (exact Shapley values / MDI / permutation-based) 在 9 个 cell 上给出高度一致的排名 (W=0.90)，完全绕过 attention weight，直接回应 Jain & Wallace (2019) 的批评。

---
