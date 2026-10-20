# analysis cross model prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_prep_20260514T084917_result.json`
- **Structured JSON:** [`8d6759a4d6499b40b080.json`](../../sessions/8d/8d6759a4d6499b40b080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是结果汇总：

---

## 实验总结表（16 实验）

| exp_id | 模型 | Masking | s | med_H | med_L | med_diff | Verdict |
|--------|------|---------|-----|-------|-------|----------|---------|
| bf16_importance_s015 | DS-R1 | importance | 0.15 | 0.0058 | 0.3983 | 0.3925 | **PASS** |
| bf16_importance_s020 | DS-R1 | importance | 0.20 | 0.0145 | 1.4963 | 1.4817 | **PASS** |
| bf16_importance_s025 | DS-R1 | importance | 0.25 | 0.0324 | 7.1960 | 7.1636 | **PASS** |
| bf16_importance_s030 | DS-R1 | importance | 0.30 | 0.0534 | 14.6395 | 14.5861 | **PASS** |
| bf16_ds_rand_s015 | DS-R1 | random | 0.15 | 0.0931 | 0.1026 | 0.0096 | FAIL |
| bf16_ds_rand_s020 | DS-R1 | random | 0.20 | 0.2918 | 0.2763 | -0.0155 | FAIL |
| bf16_ds_rand_s025 | DS-R1 | random | 0.25 | 0.8182 | 1.3627 | 0.5445 | FAIL |
| bf16_ds_rand_s030 | DS-R1 | random | 0.30 | 2.5031 | 4.0414 | 1.5383 | FAIL |
| bf16_qw_imp_s015 | Qwen | importance | 0.15 | 0.0009 | 0.0394 | 0.0386 | **PASS** |
| bf16_qw_imp_s020 | Qwen | importance | 0.20 | -0.0001 | 0.2349 | 0.2350 | **PASS** |
| bf16_qw_imp_s025 | Qwen | importance | 0.25 | 0.0034 | 1.2712 | 1.2677 | **PASS** |
| bf16_qw_imp_s030 | Qwen | importance | 0.30 | 0.0095 | 2.9526 | 2.9431 | **PASS** |
| bf16_qw_rand_s015 | Qwen | random | 0.15 | 0.1381 | 0.1878 | 0.0497 | FAIL |
| bf16_qw_rand_s020 | Qwen | random | 0.20 | 0.4855 | 0.6144 | 0.1289 | FAIL |
| bf16_qw_rand_s025 | Qwen | random | 0.25 | 1.6043 | 2.2641 | 0.6598 | FAIL |
| bf16_qw_rand_s030 | Qwen | random | 0.30 | 3.9550 | 8.1960 | 4.2410 | **PASS** ⚠️ |

**Importance: 8/8 PASS | Random: 7/8 FAIL + 1 unexpected PASS (qw_rand_s030)**

---

## Cross-model 分析核心结果

| 指标 | 值 | 含义 |
|------|-----|------|
| Cohen's d Spearman ρ | **1.0** | 两模型效应量趋势完美一致 |
| 两模型均严格单调递增 | ✅ | importance median_diff 随 sparsity 严格递增 |
| Gradient permutation test p | **0.043** | 显著（α=0.05），两模型梯度方向一致非偶然 |
| Per-problem concordance p | 0.926 | 不显著——具体受影响的 problem 不同，但 aggregate 趋势一致 |
| Wilcoxon one-sided | 8/8 显著 | 两模型所有 sparsity 下 importance diff > 0 |

**Cohen's d 趋势**：
- DeepSeek: 0.44 → 0.52 → 0.68 → 0.80 (small → medium → large)
- Qwen: 0.28 → 0.55 → 0.89 → 1.02 (small → medium → large)

---

## ⚠️ 需要关注：bf16_qw_rand_s030 意外 PASS

该实验 verdict=PASS（expected FAIL）：permutation p=0.012, bootstrap CI 不包含零 [0.24, 3.31]。但 Cohen's d=-0.035（negligible），mean_diff=-1.13（负值）与 median_diff=2.42（正值）方向不一致，暗示这可能是 outlier 驱动的伪阳性。

---

**服务器文件**：
- `analysis_output/cross_model_analysis.json` — cross-model 完整结果
- `analysis_output/experiment_summary_table.json` — 16 实验总结
- `analysis/cross_model_analysis.py` — cross-model 分析脚本
- `analysis/generate_summary_table.py` — 总结表生成脚本

---
