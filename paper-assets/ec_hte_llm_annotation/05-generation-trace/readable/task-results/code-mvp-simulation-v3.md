# code mvp simulation v3

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_simulation_v3_20260520T185209_result.json`
- **Structured JSON:** [`6472e7e78a4b005d2d81.json`](../../sessions/64/6472e7e78a4b005d2d81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results match expectations:

**Extreme regime, n_expert=500, subgroup_A (misclass=25%):**
| Method | bias_z0 | bias_z1 |
|--------|---------|---------|
| Oracle | -0.002 | -0.002 |
| EC-HTE | -0.009 | +0.008 |
| Global | **+0.054** | **-0.055** |
| Naive | +0.098 | -0.100 |

**Extreme regime, subgroup_B (misclass=5%):**
| Method | bias_z0 | bias_z1 |
|--------|---------|---------|
| Oracle | -0.012 | -0.005 |
| EC-HTE | -0.014 | -0.002 |
| Global | **-0.070** | **+0.055** |
| Naive | +0.009 | -0.025 |

**Marginal CATE:** Global ≈ EC-HTE ≈ Oracle (all near-unbiased), Naive biased.

**Homogeneous regime:** EC-HTE ≈ Global (no heterogeneity → no advantage), confirming EC-HTE only helps when misclassification rates differ across subgroups.

Global under-corrects in subgroup A (uses ~15% global rate vs 25% true) and over-corrects in subgroup B (uses ~15% vs 5% true). EC-HTE eliminates this by using subgroup-specific confusion matrices.

Files saved:
- `results/mvp_results_v3_raw.csv`
- `results/mvp_results_v3.csv`

---
