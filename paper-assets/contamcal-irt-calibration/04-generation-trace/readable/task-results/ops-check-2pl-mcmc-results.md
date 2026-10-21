# ops check 2pl mcmc results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-2pl-mcmc-results_20260515T094703_result.json`
- **Structured JSON:** [`28a1fb0829c19d881214.json`](../../sessions/28/28a1fb0829c19d881214.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 2PL Joint Fit MCMC 结果

**状态：已完成** — 4 chains × 5000 iterations，总耗时 2102.9s（~35 min），16000 draws。

### gamma 估计

| 指标 | 值 |
|------|-----|
| mean | 0.1389 |
| sd | 0.2274 |
| 95% CI | [-0.306, 0.591] |
| 80% CI | [-0.152, 0.429] |
| IQR | [-0.015, 0.290] |
| **CI excludes zero** | **No** |

### 诊断

| 指标 | 值 | OK? |
|------|-----|-----|
| max Rhat | 1.0024 | Yes |
| min ESS | 3604.4 | Yes |
| divergences | 0 (0%) | Yes |
| **all_ok** | **true** | — |

### PPC

| 指标 | 值 |
|------|-----|
| overall PPP | 0.2835 |
| obs mean acc | 0.5086 |
| pred mean acc | 0.5011 |
| residual MAE | 0.0083 |

### 代码修复

`joint_fit.py` 中 `model_type` 正确传递到 `STAN_MODELS[model_type]`（L163）和 `extract_results(fit, y, model_type)`（L171）。`has_cd` 检查仅对 `4pl` 前缀生效（L185），2PL 路径正确跳过 c/d 参数提取。修复已持久化。

### 结果存放

`/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit/joint_fit_results.json`

### 解读

gamma 点估计为正（0.139），暗示污染可能有微弱正向效应，但 95% CI 跨零，统计上不显著。MCMC 诊断全部通过（Rhat ≈ 1.00, ESS > 3600, 零 divergences），拟合质量良好（PPP = 0.28，预测准确率与观测仅差 0.75%）。

---
