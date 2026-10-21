# ssh exp018 completion check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp018_completion_check_20260523T113836_result.json`
- **Structured JSON:** [`2429c38368ad65fc0b5f.json`](../../sessions/24/2429c38368ad65fc0b5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-018 结果汇总

**状态：成功完成。** 20/20 seeds 全部跑完，CSV 完整（41 行）。总耗时 2.66 小时。

### 汇总统计

| 指标 | sequential | joint_gmfrm | 
|------|-----------|-------------|
| θ_RMSE | 0.1714 ± 0.0487 | **0.0940 ± 0.0185** |
| θ_τ (Kendall) | 0.8911 ± 0.0376 | **0.9432 ± 0.0362** |
| c_RMSE | 1.3752 ± 0.2781 | **0.6262 ± 0.2627** |
| c_Pearson | 0.8167 ± 0.0955 | **0.8424 ± 0.1058** |

### Wilcoxon 检验

**Δτ (theta_tau):**
- Wins/Ties/Losses = **18/1/1**
- Non-zero pairs: 19/20
- Mean Δτ = +0.0521
- p = **1.81e-04**

**θ_RMSE:**
- Win rate: **20/20** (joint 全胜)
- p = **1.91e-06**
- Cohen's d = **1.914** (极大效应量)

**c_RMSE:**
- Win rate: **20/20** (joint 全胜)
- p = **1.91e-06**

Joint GMFRM 在所有指标上显著优于 sequential baseline，θ_RMSE 降低 45%，c_RMSE 降低 54%。

---
