# figure scatter concentration fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_scatter-concentration-fix_20260515T010212_result.json`
- **Structured JSON:** [`64cb1fcfdd86af9a0420.json`](../../sessions/64/64cb1fcfdd86af9a0420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修改内容**：脚本中 Mistral concentration 值已是 0.241（无需再改 0.231→0.241，文件先前已更新）。`gen_scatter_concentration.py:24` 行：`('Mistral-7B-v0.3', 0.241, -0.033, '#CC79A7')`。

**输出文件**（已重新生成，09:03 UTC）：
- `/root/ratekv/figures/fig_concentration_scatter.pdf` — 29846 bytes
- `/root/ratekv/figures/fig_concentration_scatter.png` — 121990 bytes

Mistral 数据点坐标 x=0.241（数据元组直接驱动散点和标注，annotate 不带额外文本，所以图上 Mistral 点位置精确反映 0.241）。

---
