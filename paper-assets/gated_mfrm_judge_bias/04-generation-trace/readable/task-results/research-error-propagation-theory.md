# research error propagation theory

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_error_propagation_theory_20260522T035809_result.json`
- **Structured JSON:** [`5aed38d0dc96f6dfa3a3.json`](../../sessions/5a/5aed38d0dc96f6dfa3a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

理论推导笔记已完成，保存在 `artifacts/error_propagation_theory.md`。

核心结果：

1. **EIV 衰减因子**: $\lambda = \text{Var}_I(e)/(\text{Var}_I(e) + \sigma^2)$。噪声使 $c_n$ 估计系统性地向零偏移，偏移量 $\propto 1-\lambda$。

2. **相变阈值**: $\sigma_{\text{crit}} = \sqrt{\text{Var}_I(e)} \approx 0.20$。对应 exp-012 DGP 中 $e = \text{sigmoid}(\mathcal{N}(0,1))$ 的跨 item 方差 $\approx 0.04$。σ=0.2 恰好是转折点——与实验完全吻合。

3. **$c_n$ 比 $\theta$ 更敏感的三重机制**: (a) 直接乘法耦合 $c_n \cdot e_i$；(b) EIV 衰减只作用于 $c_n$（$\theta$ 是截距项）；(c) HalfNormal 先验与衰减方向一致（都推向零），对被污染模型双重夹击。

4. **非线性退化**: 来自衰减偏差的 harmonic 结构 $(1-\lambda)^2 = \sigma^4/(V_e + \sigma^2)^2$，在 $\sigma < \sigma_{\text{crit}}$ 时凸增（加速），$\sigma > \sigma_{\text{crit}}$ 时凹减（趋向饱和）。

5. **实际含义**: Stage 2 估计精度需满足 $\sigma_e < \sigma_{\text{crit}} \approx 0.2$，此范围内 $\theta$ RMSE 退化 <6%，$c_n$ RMSE 退化 <8%。

---
