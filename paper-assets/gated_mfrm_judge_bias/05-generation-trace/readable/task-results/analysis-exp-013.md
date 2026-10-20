# analysis exp 013

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-013_20260523T052624_result.json`
- **Structured JSON:** [`42f637903cee2847bda7.json`](../../sessions/42/42f637903cee2847bda7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## exp-013 结果总结

### Conclusion: **success** — hypothesis 完全验证

权重配置对 downstream G-MFRM τ **零影响**，远超 hypothesis 预期（< 0.02）。

### τ 值表

| Weight Config | ref_weight | cma_weight | G-MFRM τ | Exposure ρ vs default | R-hat | ESS_min | Divergences |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 50/50 | 0.50 | 0.50 | 0.7857 | 0.9981 | 1.02 | 196 | 0 |
| **75/25 (default)** | **0.75** | **0.25** | **0.7857** | **1.0000** | **1.04** | **115** | **0** |
| 90/10 | 0.90 | 0.10 | 0.7857 | 0.9991 | 1.01 | 432 | 0 |
| 100/0 | 1.00 | 0.00 | 0.7857 | 0.9978 | 1.01 | 668 | 0 |

### 关键数字

- **τ 变化幅度**: **0.000**（4 种配置完全相同 τ = 0.7857）
- **Exposure Spearman ρ**: 0.9978–1.0000（各配置的 exposure 估计近乎完全一致）
- **收敛诊断**: R-hat 1.01–1.04（均 < 1.05），divergences = 0，ESS 最低 115（75/25 配置）

### 对 R1-W6 的影响

这个实验彻底回答了 R1-W6 关于 exposure estimation 权重选择 robustness 的问题。结论：**G-MFRM 的 downstream ranking (τ) 对 Stage 2 权重配置完全不敏感**。即使将 cross-model-agreement 权重从 50% 降到 0%（纯 reference-anchoring），τ 不变，exposure 排序的 Spearman ρ > 0.997。这意味着论文中使用 75/25 默认配置是充分合理的，reviewer 对此超参数选择的担忧可以被数据驳回。可以在论文的 robustness analysis 中加一句话 + 引用此表即可。

---
