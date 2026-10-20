# analysis extended statistics 5seed

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extended-statistics-5seed_20260515T174718_result.json`
- **Structured JSON:** [`afdeacfb6a6fd06c083f.json`](../../sessions/af/afdeacfb6a6fd06c083f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 artifact (`art_20260515_6f8912`)。核心结论：

**主要发现**:
- **Vanilla > TaxEI**: Bootstrap 95% CI [+3.4, +15.8] 显著, d=1.08 (large), P(Vanilla>TaxEI)=99.2%
- **TaxEI = Random**: 均值完全相同 (58.3%), d=0.00
- **Training-eval dissociation 确认**: Training loss CV=0.17% vs eval CV=9.96% (60× 差异), Spearman ρ=0.11 (NS)

**需要注意的问题**:
- 功效仅 45.2%，paired t-test p=0.073 未达 0.05（bootstrap 显著但参数检验 marginal）
- BF₁₀=0.68 inconclusive——n=5 太小无法给出 Bayesian 确定结论
- Cohen's d CI 下界接近 0 ([−0.09, 2.18])
- 需 **n=9 seeds** 才能在 80% power 下稳定检测到 9pp 差异

---
