# exp shap and lr zscore

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_shap_and_lr_zscore_20260515T170353_result.json`
- **Structured JSON:** [`6975992046e6eed80fe8.json`](../../sessions/69/6975992046e6eed80fe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验全部完成。

---

## 结果汇总

### Part A: SHAP TreeExplainer (R3-N3)

**产出**: `results/shap_analysis/shap_importance.json` + `shap_summary.txt`

聚合 9 cells 的 SHAP top-5: **p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl**

| 特征类别 | SHAP 贡献占比 |
|----------|-------------|
| PPL/surprisal | **88.8%** |
| Lexical diversity (TTR, n-gram) | **11.2%** |

SHAP top-5 与 Gini top-5 完全相同（仅顺序微调），一致性高。RF 被 PPL tail stats 主导，DeBERTa attention 聚焦 lexical diversity → **手工特征与 PLM 表征互补性得到正式 SHAP 证据支持**。

### Part B: LR Cross-Strategy Z-Score (P0-1)

**产出**: `results/lr_cross_strategy_zscore/lr_zscore_results.json`

三种条件对比（关键 temp09 holdout 的 d1v2 AUC）：

| Model | raw (no scaling) | scaler only | **zscore** |
|-------|----------|--------|---------|
| Pythia-1.4B | 0.631 | 0.518 | **0.721** |
| GPT-2 XL | 0.500 | 0.238 | **0.561** |
| OLMo-1B | 0.500 | 0.191 | **0.699** |

**结论**: Z-score 确实恢复了 LR 的 d1v2 AUC（方向正确），但实际数值低于 paper 声称：
- Paper 称 GPT-2 XL 0.13→**0.68**，实际 scaler 0.238→zscore **0.561**
- Paper 称 OLMo 0.25→**0.83**，实际 scaler 0.191→zscore **0.699**

**建议**: 论文需要用实际数字更新声明，定性结论（z-score 恢复 LR 跨策略 d1v2 AUC）成立，但定量数字需修正。

---
