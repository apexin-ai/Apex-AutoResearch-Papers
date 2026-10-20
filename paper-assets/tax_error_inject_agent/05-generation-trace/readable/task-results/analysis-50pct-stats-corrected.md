# analysis 50pct stats corrected

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_50pct-stats-corrected_20260516T020006_result.json`
- **Structured JSON:** [`349a86ffb00034f2221a.json`](../../sessions/34/349a86ffb00034f2221a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存并注册 (`art_20260516_c47190`)。核心结论：

**三组对比均未通过 Bonferroni α=0.017**：
- Vanilla vs TaxEI 50%: Δ=9.82pp, p=0.0864, d=1.31 (large effect but underpowered)
- Vanilla vs Random 50%: Δ=8.98pp, p=0.2453, d=1.01
- TaxEI 50% ≈ Random 50%: Δ=0.84pp, p=0.9203

**Bootstrap 提供补充视角**：Vanilla vs TaxEI 50% 的 bootstrap p=0.0104（CI=[2.16, 17.48]不含0），比 t-test 更乐观。

**Power 严重不足**：n=5 时 Vanilla vs TaxEI 仅 40.9% power，需 n=10 达到 80%；Vanilla vs Random 需 n=24。

**Dose-response**：TaxEI 线性斜率 -0.056%/dose%，R²=0.173，不显著（p=0.49），因 50% rebound 破坏单调性。Random 斜率 -0.079%，R²=0.641，Spearman rho=-0.9（p=0.037 显著）。

**50% 特异性**：s0/s123 swap 的 permutation p=0.13，不算罕见；25%→50% rebound +4.74pp 不显著（p=0.33）。

---
