# research literature scan

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260515T210127_result.json`
- **Structured JSON:** [`beda1e71ef6daf1044bc.json`](../../sessions/be/beda1e71ef6daf1044bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。核心结论：

**三个 Claims 均保持 novel。** 未发现直接竞争者做 calibration-diversity 的 lead-lag 分析。

**3 篇必须引用的新论文：**

1. **Causal-Audit** (Ruiz et al., April 2026) — 提出因果方法假设前置检验框架，62% FP reduction。与 Claim 3 互补：他们做 pre-screening，我们做 post-hoc consensus。必须在方法论部分明确区分。

2. **CausalCompass** (Yi et al., Feb/April 2026) — 因果发现方法鲁棒性 benchmark，证实无单一方法普适，支持我们 Claim 3 的多方法必要性论证。

3. **Cao et al. — On the Entropy Calibration of LMs** (Nov 2025, revised Jan 2026) — 证明 calibration-diversity tradeoff 是 LM 的基本属性。为 Claim 1（ECE leads diversity）提供理论基础。

**2 篇建议引用：** Sahoo 2026（ECE 对 RLHF 扰动敏感）、Falahati et al. ICML 2026（pluralistic curation 避免 collapse，motivates "when to intervene"）。

chen2025scales 仍为最近的竞争者，自 2025.10 以来未更新，且没有扩展到 lead-lag 分析。

报告已写入 `artifacts/literature_scan_20260515/scan_report.md` 并注册。

---
