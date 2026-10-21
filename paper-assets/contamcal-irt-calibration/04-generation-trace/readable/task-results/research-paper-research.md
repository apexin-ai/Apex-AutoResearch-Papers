# research paper research

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-research_20260516T160608_result.json`
- **Structured JSON:** [`5b09d9367b43b0224d08.json`](../../sessions/5b/5b09d9367b43b0224d08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/literature_supplement_irt_fit.md`。

三个方向各找到 2-4 篇核心论文：

**Direction 1 (PPP misfit):** Brown & Thomson (2024) 最关键——证明 PPP 分布本质非均匀，low PPP 不自动否定参数估计，可直接论证 ARC 上 PPP=0.003 + γ 显著排除零的可解释性。Sinharay (2025) 作为最新 IRT model fit 综述提供方法论权威。

**Direction 2 (MC vs generative):** Deng et al. (NAACL 2024) 用 TS-Guessing 证明 MC 格式对 contamination 更敏感（GPT-4 猜对率 57%）；Li et al. (2024) 量化 MC→open-ended 约 25% 性能下降；Schaeffer et al. (2026) 首次用 scaling law 研究 generative benchmark 上的 contamination 效应。三篇共同支持 ARC(MC) γ>0 / GSM8K(generative) γ≈0 的 format dependence 叙事。

**Direction 3 (Simpson's paradox):** Kievit et al. (2013) 直接提供理论框架；Ercikan et al. (2008) 的 DIF cancellation 实证与我们 MMLU domain-level 发现直接类比。

---
