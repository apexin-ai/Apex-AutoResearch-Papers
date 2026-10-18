# analysis matrix 3x3 synthesis

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matrix_3x3_synthesis_20260515T020134_result.json`
- **Structured JSON:** [`0b2191973dc36bbc3914.json`](../../sessions/0b/0b2191973dc36bbc3914.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。产出路径：`artifacts/matrix_3x3_analysis.md` (art_20260515_16b1ce)

核心结论：

1. **深度信号普遍存在** — 8/8 格子均远超 chance（69.6%–85.4% vs 25%）
2. **GPT-2 XL 全面最优** — 跨策略均值 84.4%，领先 Pythia +9.7pp、OLMo +6.1pp
3. **top-k 系统性最弱**（−8.2pp vs nucleus），temperature ≈ nucleus（+1.1pp），策略效应与模型交互（Pythia temp09 降但 OLMo/GPT-2 XL 升）
4. **特征稳定性极高** — p90_ppl、var_surprisal、p75_ppl 在 8/8 格为 top-3
5. **Code contamination 是模型特异的** — Pythia d3 达 12-14%，OLMo/GPT-2 XL <2%，但与分类性能无正相关

---
