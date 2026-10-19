# code r7 layer sweep heatmap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_layer_sweep_heatmap_20260518T055430_result.json`
- **Structured JSON:** [`f2126408f6e395882344.json`](../../sessions/f2/f2126408f6e395882344.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure generated successfully. The visualization clearly shows the narrative: across all 4 models, biased shallow layers (red dashed) have lower precision and higher FPR, while corrected deep layers (green dashed) consistently achieve higher precision and lower FPR.

Key metrics at marked layers:

| Model | Biased Layer | Precision | FPR | Corrected Layer | Precision | FPR |
|-------|-------------|-----------|-----|----------------|-----------|-----|
| R1-8B | L2 | 0.60 | 0.14 | L14 | 0.69 | 0.10 |
| OT-7B | L2 | 0.37 | 0.16 | L16 | 0.43 | 0.12 |
| QwQ-32B | L2 | 0.54 | 0.19 | L60 | 0.66 | 0.10 |
| R1-32B | L10 | 0.55 | 0.28 | L63 | 0.59 | 0.23 |

Output files:
- PDF: `/root/autodl-tmp/contrastive_trace_safety/docs/paper/figures/fig_layer_heatmap.pdf`
- PNG: `/root/autodl-tmp/contrastive_trace_safety/docs/paper/figures/fig_layer_heatmap.png`

---
