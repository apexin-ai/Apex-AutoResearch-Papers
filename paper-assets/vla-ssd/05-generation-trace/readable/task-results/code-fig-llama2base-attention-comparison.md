# code fig llama2base attention comparison

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig_llama2base_attention_comparison_20260517T061138_result.json`
- **Structured JSON:** [`1cb2bdf0da749f9e3064.json`](../../sessions/1c/1cb2bdf0da749f9e3064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure generated and saved. The three-panel stacked bar chart clearly shows the progression:

- **Untrained VLA (0/32)**: All heads are image-dominant (orange), with minimal instruction attention (blue)
- **Llama-2 Base (9/32)**: 9 heads become instruction-dominant, concentrated at heads 17, 23, 25, 27 and others in the high-index range
- **VLA Trained (25/32)**: 25 heads are instruction-dominant, with significant BOS attention (gray) appearing as a training artifact

Output files:
- PDF: `artifacts/attention/fig_llama2base_comparison.pdf` (29 KB)
- PNG: `artifacts/attention/fig_llama2base_comparison.png` (31 KB)

---
