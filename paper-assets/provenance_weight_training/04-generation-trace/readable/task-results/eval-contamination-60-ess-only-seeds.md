# eval contamination 60 ess only seeds

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_contamination_60_ess_only_seeds_20260518T100721_result.json`
- **Structured JSON:** [`b1da3648389149c67e71.json`](../../sessions/b1/b1da3648389149c67e71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results: ρ=0.6 ESS-only (3 seeds)

| Experiment | Loss | PPL | Eval Tokens |
|---|---|---|---|
| ESS-only seed42 | — | 17.770 | — |
| **ESS-only seed123** | 2.8771 | **17.763** | 4,077,068 |
| **ESS-only seed456** | 2.8771 | **17.762** | 4,077,068 |

**3-seed summary:** PPL = 17.770, 17.763, 17.762 → mean ≈ **17.765**, range 0.008.

Cross-method comparison at ρ=0.6 seed42:
- Uniform: 17.763
- ESS-only: 17.770
- Adaptive: 17.736

As expected, ESS-only collapses to near-uniform at ρ=0.6. The three seeds are extremely tight (±0.004 from mean), confirming low variance and consistent behavior of the ESS-only weighting at this contamination ratio.

---
