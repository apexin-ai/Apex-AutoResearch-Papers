# ssh mvp 002 check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mvp_002_check_20260521T191830_result.json`
- **Structured JSON:** [`ba8e89e9eb5abf490c25.json`](../../sessions/ba/ba8e89e9eb5abf490c25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报如下：

---

## 1. mvp_002 结果

**VERDICT: FAIL（收敛问题）**

| method | RMSE mean±std | τ mean±std | p-value |
|--------|--------------|------------|---------|
| raw_average | 0.8063±0.0841 | 0.8401±0.0347 | — |
| mfrm_only | 0.2539±0.0449 | 0.8390±0.0351 | — |
| sequential | 0.2211±0.0376 | 0.8596±0.0291 | ref |
| **joint_gmfrm** | **0.1486±0.0199** | **0.9028±0.0181** | **0.000001** |

**收敛诊断**：max R̂=1.05, min ESS=47 — **FAIL**（ESS 太低，R̂ 边界）

**效果**：joint vs sequential RMSE 降低 32.8%，Wilcoxon p=1e-6 **PASS**。信号非常强，但部分 seed 的 MCMC chain 收敛不够（ESS<100）。

核心矛盾：**统计检验强烈支持假设，但收敛诊断不过关。** 放大信号后 joint model 的优势很明显（mvp_001 无差异 → mvp_002 降 32.8%），问题出在采样器配置（warmup/步长/链数）需要调优。

## 2. Registry 更新

- status: DONE, conclusion: negative（因 VERDICT=FAIL）
- metrics 已记录完整结果表、收敛诊断、scatter Pearson r
- checkpoint_path / log_path 已设

## 3. 散点图状态

**已完成。** `diagnosis_bias_scatter.png`（82KB）已生成。

- **Pearson r = 0.6534, p ≈ 0**（N=400 points）
- 确认 DGP 中 contamination 与 judge bias 的相关性符合设定（ρ=0.6 → 实测 r=0.65）

---
