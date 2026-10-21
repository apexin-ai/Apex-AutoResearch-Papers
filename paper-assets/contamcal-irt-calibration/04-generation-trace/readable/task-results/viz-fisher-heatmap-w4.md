# viz fisher heatmap w4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fisher_heatmap_w4_20260516T213006_result.json`
- **Structured JSON:** [`0c4e48a180754af421f2.json`](../../sessions/0c/0c4e48a180754af421f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task complete. Here's the summary:

**Fisher Information Heatmap (exp-004, W4 fix)**

Generated on server cqa1-21977 at `/root/autodl-tmp/exp004/fisher_heatmap/`:
- `fisher_power_heatmap.pdf/png` (single panel, recommended for paper)
- `fisher_dual_heatmap.pdf/png` (dual panel: power + CI width)

**Method**: Analytical Fisher Information Matrix with Schur complement to compute CRLB for γ in the 2PL+γ model. Signal attenuation correction accounts for measurement error in exposure signals (γ_effective = δ × reliability(AUC)). 50 MC draws per grid cell, completed in 38s on CPU.

**Key findings** (80% power contour):

| Signal AUC | N needed for 80% power |
|---|---|
| 0.65 | ~50 |
| 0.70 | ~30 |
| 0.75 | ~20 |
| 0.80 | ~12-16 |

This theoretically confirms the paper's empirical finding: **AUC ≥ 0.70 is the practical minimum** for identifying γ with reasonable sample sizes (N=16-30 models typically available in evaluations).

---
