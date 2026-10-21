# ops q5 stem gamma prior check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_q5_stem_gamma_prior_check_20260517T151306_result.json`
- **Structured JSON:** [`770863cc491e36e4c5be.json`](../../sessions/77/770863cc491e36e4c5be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete analysis.

---

## Q5 结果：STEM γ Prior vs Posterior 检查

### 1. γ Prior 确认

所有 Stan 模型中 γ prior 为 **`gamma ~ std_normal()`**，即 **N(0, 1)**。

### 2. J=13 Run（`mmlu_domain_irt_no05B`）全域 Shrinkage 分析

| Domain | γ_post_mean | γ_post_SD | γ_prior_mean | γ_prior_SD | Shrinkage | Prior 主导? |
|--------|-------------|-----------|--------------|------------|-----------|------------|
| **STEM_Math** | +0.499 | 0.362 | 0 | 1 | **0.869** | **No** |
| **STEM_Science** | +0.504 | 0.357 | 0 | 1 | **0.872** | **No** |
| **STEM_CS_Eng** | +0.497 | 0.471 | 0 | 1 | **0.778** | **No** |
| Medical | +0.235 | 0.329 | 0 | 1 | 0.892 | No |
| Humanities | -0.309 | 0.282 | 0 | 1 | 0.920 | No |
| Social_Sciences | -0.571 | 0.241 | 0 | 1 | 0.942 | No |
| Business_Law | +0.044 | 0.273 | 0 | 1 | 0.925 | No |
| Other | +0.127 | 0.384 | 0 | 1 | 0.853 | No |
| pooled | +0.107 | 0.263 | 0 | 1 | 0.931 | No |

**Shrinkage = 1 − (posterior_var / prior_var)**。所有域 shrinkage 在 0.78–0.94 之间，data 贡献了 78%–94% 的信息。

### 3. 关键结论：Posterior 不被 Prior 主导

初始怀疑（posterior ≈ prior）**不成立**。Posterior SD（0.24–0.47）远小于 prior SD（1.0），说明 data 大幅更新了 prior。

### 4. 那为什么 STEM 三域 γ 几乎相同（≈0.50）？

这不是 prior 主导的结果，而是 **N=13 respondents 的分辨率不足**。

证据：N=21-24 run（`analysis_2pl_gamma_refit_0516.md`）加入更多 respondents 后，三域 γ 显著分化：

| Domain | J=13 γ | J=21-24 γ | 变化 |
|--------|--------|-----------|------|
| STEM_Math | +0.499 | **+0.969** | ↑ 大幅上升 |
| STEM_Science | +0.504 | **+0.838** | ↑ 上升 |
| STEM_CS_Eng | +0.497 | **+0.197** | ↓ 大幅下降，变为不显著 |

J=13 时三域的 exposure 信号无法区分，γ 收敛到相近值（≈0.50）。J=21-24 增加了 ability 维度的变异，使 IRT 模型能够分离 domain-specific contamination effect。

### 5. 总结

- **Prior 没有主导 posterior**（shrinkage 0.78–0.94）
- STEM 三域 γ ≈ 0.50 的原因是 **J=13 的统计功效不足以区分 domain 间差异**，不是 prior 问题
- 增加 respondents 到 J=21-24 后，STEM_Math（+0.97）和 STEM_CS_Eng（+0.20）分化明显，确认 J=13 的 "一致性" 是伪象

---
