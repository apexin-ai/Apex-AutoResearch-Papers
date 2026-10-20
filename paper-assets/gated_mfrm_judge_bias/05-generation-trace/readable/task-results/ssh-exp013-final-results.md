# ssh exp013 final results

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp013_final_results_20260523T052707_result.json`
- **Structured JSON:** [`e160971732fc6a4b173f.json`](../../sessions/e1/e160971732fc6a4b173f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 已生成。结果：

| weight_config | exposure_spearman_rho | gmfrm_tau | delta_tau_vs_default (75/25) |
|---|---|---|---|
| 50_50 (ref=0.5, cma=0.5) | 0.9981 | 0.7857 | 0.0 |
| **75_25 (ref=0.75, cma=0.25)** | **1.0** | **0.7857** | **0.0 (baseline)** |
| 90_10 (ref=0.9, cma=0.1) | 0.9991 | 0.7857 | 0.0 |
| 100_0 (ref=1.0, cma=0.0) | 0.9978 | 0.7857 | 0.0 |

关键发现：**GMFRM tau 在所有权重配置下完全一致（0.7857），delta 全为 0。** 模型排名对 ref/cma 权重分配不敏感。exposure_spearman_rho 在 75/25 时达到完美 1.0，其余配置略低但差异极小（<0.003）。

诊断指标均正常：r_hat 均 ≤1.04，无 divergence，ESS 最低 115（75/25 配置）。

---
