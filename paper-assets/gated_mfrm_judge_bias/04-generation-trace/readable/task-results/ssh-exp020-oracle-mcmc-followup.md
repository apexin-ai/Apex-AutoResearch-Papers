# ssh exp020 oracle mcmc followup

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp020-oracle-mcmc-followup_20260525T152558_result.json`
- **Structured JSON:** [`7e2ceeb8dd49518c6782.json`](../../sessions/7e/7e2ceeb8dd49518c6782.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总关键结果：

---

**Variant A (c_n=0, pure MFRM/NCP)**
- 收敛：R̂=1.0060, ESS=1304
- Kendall τ = **0.824** (raw_average: 0.838)
- Spearman ρ = 0.934 (raw_average: 0.949)

**Variant B (tighter prior, sigma_c~HN(0.3))**
- 收敛：R̂=1.0076, ESS=1121
- Kendall τ = **0.794** (与原始 G-MFRM v2 完全一致)
- Spearman ρ = 0.926
- c_n mean: 1.312 (原始 2.038)，range: [0.425, 2.993]

**诊断结论**
- Variant A（去掉 c_n）τ=0.824 > 0.794 → **contamination gating 确实在损害排名精度**
- Variant B（缩紧先验）τ 仍为 0.794，与原始 v2 持平 → **缩紧先验未能改善排名**，c_n 仍然在吸收信号
- 最大 theta 偏移集中在 gpt-4-0613（+0.324）和 gpt-4-turbo（+0.155），它们正好是原始 c_n 最高的两个模型（3.775, 3.756）

报告已保存至 `/root/gated_mfrm_judge_bias/diagnosis_oracle_results.txt`，JSON 在 `output_n17_diagnosis/diagnosis_summary.json`。

---
