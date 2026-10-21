# code kappa sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kappa-sweep_20260521T155209_result.json`
- **Structured JSON:** [`ac25390d00cb640d1c34.json`](../../sessions/ac/ac25390d00cb640d1c34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are complete and correct. The stress test section provides valuable context showing that the guard only matters with near-random labeling (π_s ≈ 0.4–0.5).

Results summary:

- **350 rows** in `artifacts/kappa_sweep/results.csv` (7 κ values × 50 seeds)
- **Guard never triggers** in the specified moderate regime — max condition number is 1.89, far below any κ threshold
- All κ values produce identical RMSE (HB=0.0759, Global=0.0765, ratio≈1.05)
- Zero numerical instability
- **Stress test** reveals the guard becomes relevant only with near-random labeling (π_s ≈ 0.35–0.40, n_expert=50), where condition numbers reach ~1000+
- **κ=100 is validated**: it provides a ~53× safety margin over observed condition numbers. The formula κ = 10·√(n_expert/K) recovers κ=100 for these settings.

---
