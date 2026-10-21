# analysis v2 corrected files inventory

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v2-corrected-files-inventory_20260523T184456_result.json`
- **Structured JSON:** [`db68a4d342b07f61136b.json`](../../sessions/db/db68a4d342b07f61136b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inventory 写入完成。汇总：

**17 个文件分 4 类：**

| 分类 | 数量 | 文件 |
|------|------|------|
| V2 corrected | 5 | table1_corrected, table2_corrected, regime_transition_corrected, random_fault_contrast_corrected, keff_distribution_corrected |
| New analysis (V2 from start) | 2 | gam_bootstrap_ci_k3, gam_bootstrap_ci_k5 |
| Unchanged | 3 | temperature_pilot_summary, stochastic_dominance_analysis, power_analysis_all_K |
| Superseded (仍含 V1 数据) | 7 | aggregation_bootstrap, epsilon_sensitivity (×2), cross_benchmark_iv, keff_stability_split, sensitivity_analysis_poolA, keff_distribution |

**需要立即更新论文的 critical changes：**
- Table 1: K_eff 8/12→12/12 significant，eta-dominant conditions 完全消失
- Table 2: Bayesian 方向反转 (1+/6-→5+/1-) 是 V1 artifact
- Table 3: K_eff significance 在所有 K 值上增加
- GAM: 之前报告的 6:6 targeted/shared split 不再成立

**6 个文件需要用 V2 数据重跑：** aggregation_bootstrap, epsilon_sensitivity (K3/K5), cross_benchmark_iv, keff_stability_split, sensitivity_analysis_poolA。

---
