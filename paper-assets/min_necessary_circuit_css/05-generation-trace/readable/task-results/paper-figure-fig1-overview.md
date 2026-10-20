# paper figure fig1 overview

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_overview_20260513T154504_result.json`
- **Structured JSON:** [`41b1465b36781c81ac62.json`](../../sessions/41/41b1465b36781c81ac62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成 `fig1_overview.pdf`（36KB 矢量）和 `fig1_overview.png`（229KB, 300 DPI）。

图表内容：
- 左侧 Transformer → 三条并行分支（EAP-IG 深蓝、EP 天蓝、ACDC 橙黄）→ 各自 threshold（top-k / isinf）→ 二值电路 C₁C₂C₃ → 交集 ∩ → CSS=1.0 → CPR Eval
- FM1（红色虚线框）标注 ACDC 的 isinf binarization，callout 说明 |C₃|=14 vs |C₁|=|C₂|=100
- FM2 标注 intersection 步骤，J(C₁,C₂)=0.82 → K≈2
- FM3 标注三个方法整体，granularity mismatch: block vs edge → J≈0

---
