# research arxiv 2602 16065 tau

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_arxiv_2602_16065_tau_20260515T082138_result.json`
- **Structured JSON:** [`f27b97576afe1fac2183.json`](../../sessions/f2/f27b97576afe1fac2183.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，报告已写入。

## 审计结论

**arXiv 2602.16065 确实存在**，论文标题是 *Can Generative Artificial Intelligence Survive Data Contamination?*（Wang, Niu, Li, UNC Chapel Hill, 2026）。

**核心发现：α 依赖已知污染比例。**

论文中 α := m₁/(m₁+m₂) 就是真实数据的比例，是实验者主动设定的设计参数。收敛 bound d(P̂_t, P₀) ≲ t^{−min{p,α}} 的推导前提是 α 已知。

**对 Claim 3 的影响：**
- 该论文**不能**支撑 "works without known contamination proportion" 的 claim
- τ 如果声称源自该 α，逻辑链断裂——论文要求知道比例，我们声称不需要
- 建议将 τ 降级为 "empirical hyperparameter with theoretical motivation"，或为 Claim 3 加 caveat

报告已写入 `artifacts/tau_theory_audit.md`，包含三个可选的论文表述修正方案。

Sources:
- [arXiv 2602.16065 Abstract](https://arxiv.org/abs/2602.16065)
- [arXiv 2602.16065 HTML](https://arxiv.org/html/2602.16065)

---
