# analysis retention 50 70 viz

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retention_50_70_viz_20260517T074026_result.json`
- **Structured JSON:** [`a9cad3e0882f465e0c5e.json`](../../sessions/a9/a9cad3e0882f465e0c5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary of results:

## Results

### 50% Sparsity (mvp_kl_norm_v2_s42)
| Region | Avg Retention |
|--------|-------------|
| Early (L0-7) | 0.531 |
| Middle (L8-23) | 0.564 |
| Knowledge (L12-20) | 0.606 |
| **Late (L24-31)** | **0.342** |

Starved layers: L27-L31 (below 0.35 threshold)
Min: L28 = 0.266, Max: L18 = 0.737

### 70% Sparsity (kl_sparsity70_s42)
| Region | Avg Retention |
|--------|-------------|
| Early (L0-7) | 0.306 |
| Middle (L8-23) | 0.334 |
| Knowledge (L12-20) | 0.381 |
| **Late (L24-31)** | **0.226** |

Starved layers: L10-L12, L27-L29 (below 0.21 threshold)
Min: L10 = 0.167, Max: L17 = 0.496

### Key Finding
Progressive starvation pattern: at 30% sparsity only late layers (L27-L31) are starved; at 50% the same late layers remain the bottleneck; at 70%, starvation spreads to early-middle layers (L10-L12) as well. The "bump" at L15-L20 (knowledge layers) is preserved across all levels, confirming that global allocation preferentially feeds knowledge-critical middle layers at the expense of late layers.

### Output Files (on westd-34887)
- `/root/distill_sparse_swiglu/artifacts/global_50pct_retention_analysis.json`
- `/root/distill_sparse_swiglu/artifacts/global_70pct_retention_analysis.json`
- `/root/distill_sparse_swiglu/artifacts/per_layer_retention_chart.pdf`
- `/root/distill_sparse_swiglu/artifacts/per_layer_retention_chart.png`
- `/root/distill_sparse_swiglu/scripts/retention_analysis_multi.py`

---
