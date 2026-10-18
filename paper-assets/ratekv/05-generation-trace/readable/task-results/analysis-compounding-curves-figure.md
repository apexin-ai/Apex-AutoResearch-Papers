# analysis compounding curves figure

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compounding_curves_figure_20260515T214903_result.json`
- **Structured JSON:** [`4785edf21fd2c53ce096.json`](../../sessions/47/4785edf21fd2c53ce096.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成，效果清晰。三条曲线清楚展示了不同 concentration 模式下 PPL 对 forced 2-bit heads 数量的敏感度差异：

- **Llama (Spike, c=0.85)** — 最陡，k=256 时 PPL 爆炸到 1519
- **Qwen (Spread, c=0.61)** — 中等斜率
- **Mistral (Flat, c=0.24)** — 最平缓，k=256 也仅 45

PDF 路径：
- 服务器：`/root/ratekv/figures/fig_compounding_curves.pdf`
- 本地：`docs/paper/figures/fig_compounding_curves.pdf`

---
