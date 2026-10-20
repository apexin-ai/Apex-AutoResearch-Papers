# ssh exp013 final csv

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp013_final_csv_20260523T054830_result.json`
- **Structured JSON:** [`5f0356a5a16486b5aca2.json`](../../sessions/5f/5f0356a5a16486b5aca2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已完成，结果已保存。4 种权重配置的完整结果：

| weight_config | ref_weight | cma_weight | exposure_spearman_rho | gmfrm_tau | delta_tau_vs_default | r_hat | ess_min | divergences |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 50_50 | 0.50 | 0.50 | 0.9981 | 0.7857 | -0.0 | 1.02 | 196.0 | 0 |
| 75_25 | 0.75 | 0.25 | 1.0000 | 0.7857 | -0.0 | 1.04 | 115.0 | 0 |
| 90_10 | 0.90 | 0.10 | 0.9991 | 0.7857 | -0.0 | 1.01 | 432.0 | 0 |
| 100_0 | 1.00 | 0.00 | 0.9978 | 0.7857 | -0.0 | 1.01 | 668.0 | 0 |

关键发现：

- **Kendall tau 完全不变**：所有 4 种权重配置的 `gmfrm_tau` 都是 0.7857，`delta_tau_vs_default` 全为 0。权重配置对排名结果没有影响。
- **Exposure 极度稳定**：`exposure_spearman_rho` 在 0.9978–1.0000 之间，曝光度参数几乎不受权重变化影响。
- **收敛质量良好**：所有配置 divergences=0，r_hat ≤ 1.04。但 75_25 的 ESS 偏低（115），50_50 也只有 196。
- **结论**：G-MFRM 对 ref/CMA 权重比例高度鲁棒，模型排名在 50/50 到 100/0 的全范围内完全一致。

---
