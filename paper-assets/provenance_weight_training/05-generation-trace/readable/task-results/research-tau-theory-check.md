# research tau theory check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tau_theory_check_20260515T112439_result.json`
- **Structured JSON:** [`37d0bd0a9b2a4d0e500f.json`](../../sessions/37/37d0bd0a9b2a4d0e500f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册：`artifacts/tau_theory_analysis.md` (art_20260515_c94f84)

**核心发现**：

1. **τ 的理论来源直接依赖已知 contamination ratio。** Wang et al. (2602.16065) 的 α = m₁/(m₁+m₂) 是已知设计参数，收敛定理 d(ℙ̂ₜ, ℙ₀) ≲ t^{-min{p,α}} 中 α 直接出现在指数位置。论文不讨论 α 未知的情况。

2. **对 Claim 3 影响可控。** τ 不能声称有 proportion-free 的理论推导，但 Claim 3 核心不受影响——b* 推导本身不需要已知比例（ESS 和 α_eff 从 batch 统计量计算）。τ 应定位为 **empirical hyperparameter with theoretical motivation**：收敛理论解释"为什么需要质量阈值"，τ 的具体值由经验确定，τ sweep 证明不敏感。

3. **推荐 framing**：类比 learning rate warmup steps——有理论 motivation 但具体值凭经验，宽泛范围内均可工作。

这与 paper_framing.md 中 D025 的结论一致。

---
