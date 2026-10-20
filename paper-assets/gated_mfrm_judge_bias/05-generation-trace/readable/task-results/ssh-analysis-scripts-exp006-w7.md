# ssh analysis scripts exp006 w7

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_analysis_scripts_exp006_w7_20260522T222815_result.json`
- **Structured JSON:** [`ab3b8c5c7de968e0cec6.json`](../../sessions/ab/ab3b8c5c7de968e0cec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

**脚本路径:**
- exp-006: `/root/gated_mfrm_judge_bias/exp006/analyze_exp006.py`
- W7 ablation: `/root/gated_mfrm_judge_bias/exp_w7_ablation/analyze_w7.py`

**数据格式:**
- exp-006 CSV: `judge_count, subset_idx, judges, method, kendall_tau, spearman_rho, n_matched, n_obs, elapsed_s` — 当前只有 `raw_average`（40行），`results_full/` 的 MCMC 方法（sequential + joint_gmfrm）仍在跑（k6 到 s2，k8/k9 未开始）。脚本优先读 `results_full/sensitivity_results.csv`，回退到 `results/`
- W7 CSV: `theta_rmse, theta_tau, r_hat, ess, c_rmse, c_pearson, variant, seed, elapsed_s` — 10/20 seeds 完成

**已用部分数据验证通过，生成了图表:**
- `artifacts/exp006_analysis/`: tau_vs_judge_count, delta_tau, loocv（各 PDF+PNG）
- `artifacts/w7_analysis/`: ablation_boxplots, theta_tau_boxplot（各 PDF+PNG）+ wilcoxon_tests.csv

**W7 初步结论:** Full G-MFRM vs Staged Estimation 差异极显著（p=0.002），vs Binary Gating 显著（p=0.002），vs No Severity 差异不显著（θ_RMSE p=0.70）。实验完成后重跑脚本即可更新。

---
