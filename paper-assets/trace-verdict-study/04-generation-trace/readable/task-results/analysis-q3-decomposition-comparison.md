# analysis q3 decomposition comparison

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q3_decomposition_comparison_20260521T190357_result.json`
- **Structured JSON:** [`2a51d78da0e1d986822d.json`](../../sessions/2a/2a51d78da0e1d986822d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存为 artifact `q3_decomposition_analysis` (art_20260521_15957f)。

核心结论：

1. **Tier 1 不受 scale 影响** — exception_only 和 ae_only 在 4 个模型（1.5B→13B）上全部 ≥98.7%，接近 ceiling
2. **Scale 效应集中在 loop_only** — 7B 85.63% vs 1.5B 79.54%（Δ=6pp），但 CodeLlama-13B 仅 77.06%，说明架构/预训练比参数量更重要
3. **信息密度层级在 1.5B 上完整保持**：exception ≈ ae >> loop >> no_trace
4. **vota 消除 scale 差异** — 1.5B (99.54%) ≈ 7B (99.25%)，结构化表示让小模型达到大模型水平

---
