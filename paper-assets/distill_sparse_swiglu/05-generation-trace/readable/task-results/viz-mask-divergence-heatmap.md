# viz mask divergence heatmap

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_mask-divergence-heatmap_20260519T115459_result.json`
- **Structured JSON:** [`32daad359a8194617463.json`](../../sessions/32/32daad359a8194617463.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

**3 figures generated** on westd-41718 at `/root/distill_sparse_swiglu/results/mask_visualization/`:

| Figure | File | Description |
|--------|------|-------------|
| Fig 1 | `fig1_mask_heatmap.pdf` | Per-layer heatmap: (a) KL mask, (b) Magnitude mask, (c) Divergence. 32 layers × 512 neuron bins, sorted by weight magnitude |
| Fig 2 | `fig2_token_dynamics.pdf` | Token-level KL dynamics vs static magnitude at layer 16, top 100 variable neurons |
| Fig 3 | `fig3_jaccard_divergence.pdf` | Per-layer Jaccard divergence bar chart |

**Key statistics** (10 samples, 30% sparsity, weight-based magnitude baseline):
- Mean Jaccard divergence: **0.4507**
- Range: 0.349 (L16) to 0.595 (L28)
- KL sparsity varies 14.2% (L16) to 54.4% (L28) despite 30% global target

**Key patterns**:
- Late layers (L24-28) diverge most (~0.54-0.59) and have highest KL sparsity
- Mid layers (L15-18) diverge least (~0.35) and have lowest KL sparsity
- Boundary layers (L0-1, L30-31) are conservative (~17-20% sparsity)
- Figure 2 clearly shows KL's per-token dynamics vs magnitude's static horizontal stripes

Note: The mean divergence is 0.45 rather than the expected 0.53 because this uses **weight-based** static magnitude masks (gate_proj L2 norm). The 0.53 figure likely used activation-based per-token magnitude masks. Summary and stats registered as artifact `art_20260519_maskviz`.

---
