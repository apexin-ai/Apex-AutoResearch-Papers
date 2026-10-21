# code t2 2 temporal accumulation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_t2_2_temporal_accumulation_20260523T030020_result.json`
- **Structured JSON:** [`c22ee1c4ab6c65d0b5ce.json`](../../sessions/c2/c22ee1c4ab6c65d0b5ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are complete. Here's the summary:

## Results

**5 comparisons** run (3 pairwise + 2 cumulative):

| Comparison | Distance | C% | Note |
|---|---|---|---|
| 2023-H1 → 2023-H2 | 6mo | 22.6% | underpowered (n=62) |
| 2023-H1 → 2024-H1 | 12mo | 32.7% | underpowered (n=62) |
| 2023-H2 → 2024-H1 | 6mo | 34.4% | well-powered |
| 2023-H1 → {H2+24-H1} | 9mo | 24.2% | underpowered |
| {H1+H2} → 2024-H1 | 9mo | 31.3% | well-powered |

**Within-ref monotonicity (fixed ref=2023-H1):** C% increases from 22.6% (6mo) → 32.7% (12mo), a +10.1pp increase when doubling temporal distance. This supports contamination accumulation.

**Cross-comparison:** Only partial monotonicity — the well-powered 2023-H2→2024-H1 (6mo, 34.4%) exceeds the underpowered 12mo comparison (32.7%), but this conflates power differences with temporal distance.

**Item overlap:** Jaccard=0.356 between 12mo DIF-C items and union of 6mo DIF-C items — moderate overlap, with 1424 items unique to the 12mo window.

**ρ(difficulty, Δ_MH):** Consistently negative across all comparisons (−0.52 to −0.74), confirming harder items show larger DIF regardless of temporal span.

Outputs saved to `artifacts/temporal_accumulation/`.

---
