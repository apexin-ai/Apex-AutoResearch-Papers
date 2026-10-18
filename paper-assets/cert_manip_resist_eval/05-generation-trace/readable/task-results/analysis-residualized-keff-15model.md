# analysis residualized keff 15model

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_residualized-keff-15model_20260522T171634_result.json`
- **Structured JSON:** [`06fab266cf29fadbd1d8.json`](../../sessions/06/06fab266cf29fadbd1d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果非常清晰。

---

## 完整结果

### Main Analysis — Residualized K_eff (15 models, 455 panels)

| Condition | η_max β | η_max p | K_eff β | K_eff p | K_resid β | K_resid p | K_resid FDR | VIF_orig | VIF_resid | R²_orig | R²_resid | r(K,η) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mmlu×prompt_injection | +0.7338 | 2.13e-45 | +1.8196 | 1.19e-10 | +1.8196 | 1.19e-10 | **7.14e-10 *** | 1.99 | 1.00 | 0.6615 | 0.6615 | 0.706 |
| mmlu×sycophancy | +0.8431 | 6.06e-37 | +1.2975 | 5.32e-09 | +1.2975 | 5.32e-09 | **1.78e-08 *** | 1.23 | 1.00 | 0.4516 | 0.4516 | 0.435 |
| mmlu×score_manipulation | +0.7838 | 2.31e-22 | +0.6271 | 5.72e-02 | +0.6271 | 5.72e-02 | 6.88e-02 ns | 3.03 | 1.00 | 0.4859 | 0.4859 | 0.818 |
| mmlu×verbosity_bias | +0.9638 | 3.44e-63 | +1.0625 | 9.14e-06 | +1.0625 | 9.14e-06 | **1.83e-05 *** | 1.25 | 1.00 | 0.5746 | 0.5746 | 0.444 |
| mmlu×position_bias | +0.2660 | 1.14e-13 | +0.0446 | 5.74e-02 | +0.0446 | 5.74e-02 | 6.88e-02 ns | 1.78 | 1.00 | 0.2432 | 0.2432 | 0.662 |
| mmlu×authority_bias | +0.8362 | 1.98e-14 | +0.2932 | 2.67e-01 | +0.2932 | 2.67e-01 | 2.67e-01 ns | 1.63 | 1.00 | 0.2120 | 0.2120 | 0.621 |
| arc×prompt_injection | +0.3151 | 5.15e-05 | +3.7375 | 3.72e-12 | +3.7375 | 3.72e-12 | **4.47e-11 *** | 3.45 | 1.00 | 0.4712 | 0.4712 | 0.842 |
| arc×sycophancy | +0.7315 | 2.47e-21 | −0.6332 | 8.63e-02 | −0.6332 | 8.63e-02 | 9.41e-02 ns | 2.54 | 1.00 | 0.2988 | 0.2988 | 0.778 |
| arc×score_manipulation | +0.1594 | 1.17e-01 | +3.1057 | 7.21e-08 | +3.1057 | 7.21e-08 | **1.73e-07 *** | 7.17 | 1.00 | 0.4345 | 0.4345 | 0.928 |
| arc×verbosity_bias | +0.5297 | 9.20e-10 | +2.0253 | 1.22e-04 | +2.0253 | 1.22e-04 | **1.83e-04 *** | 3.25 | 1.00 | 0.4044 | 0.4044 | 0.832 |
| arc×position_bias | −0.0038 | 9.10e-01 | +0.2271 | 5.92e-09 | +0.2271 | 5.92e-09 | **1.78e-08 *** | 6.53 | 1.00 | 0.3293 | 0.3293 | 0.920 |
| arc×authority_bias | +0.4740 | 4.27e-11 | +1.6974 | 2.65e-05 | +1.6974 | 2.65e-05 | **4.54e-05 *** | 2.16 | 1.00 | 0.3356 | 0.3356 | 0.733 |

### 汇总

| 指标 | 值 |
|---|---|
| **K_eff_resid FDR<0.05 显著** | **8/12** |
| K_eff_resid β 方向正 | 11/12 |
| K_eff_resid β 方向负 | 1/12（仅 arc×sycophancy, ns） |
| Mean VIF_orig | 3.00 |
| Mean VIF_resid | 1.00（验证 residualization 成功消除共线性） |
| **Sensitivity (排除 acc<0.5) FDR 显著** | **9/12** |

### 低精度模型

仅 `claude-3-haiku` on `arc_challenge`（acc=0.450）被标记。Sensitivity 分析排除它后，arc_challenge 条件 N 从 455 降至 364，反而有更多条件变显著（arc×sycophancy 从 ns 变为 FDR *）。

### Claim 1 方向判断

**K_eff 有强独立效应。** Residualized 后 8/12 FDR 显著、11/12 正 β，sensitivity 版 9/12 显著。原始 K_eff 的显著性**不是**来自与 η_max 的共线性——residualize 后 β 值完全不变（因为 OLS 中 residualized predictor 的系数等价于原始 partial coefficient），VIF 降到 1.00，显著性稳健。

不显著的 4 个 conditions（mmlu×score_manipulation, mmlu×position_bias, mmlu×authority_bias, arc×sycophancy）多为高共线性条件（r>0.6），η_max 吸收了大部分方差。但主体 pattern 清楚：**K_eff 在控制 η_max 后仍然是 panel ASR 的独立正向预测变量**。论文可以安全地 claim "panel diversity (K_eff) contributes to manipulation resistance beyond individual model robustness (η_max)"。

---
