# viz gradient snr chart

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_gradient_snr_chart_20260517T081442_result.json`
- **Structured JSON:** [`7b8c1b34b55bac8f25a9.json`](../../sessions/7b/7b8c1b34b55bac8f25a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完成。

- PDF: `figures/paper/gradient_snr_comparison.pdf` (25 KB)
- PNG: `figures/paper/gradient_snr_comparison.png` (104 KB)

关键观察：(a) Unconstrained 下 KL 和 BCE 的 SNR 差距较小（5.76x），且两者在最后几层趋于收敛；(b) Lagrangian-Constrained 下 KL 全层维持高 SNR 而 BCE 被压制到极低水平（103.2x），中间层差距可达 3-4 个数量级。

---
