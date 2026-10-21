# fix llama seed42 tiebreaking

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama-seed42-tiebreaking_20260523T180210_result.json`
- **Structured JSON:** [`cb64c09efc8a3a2c6a63.json`](../../sessions/cb/cb64c09efc8a3a2c6a63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Recomputation complete. Results:

| Metric | Alphabetical | Original (most_common) |
|--------|-------------|----------------------|
| SC | **72.50%** (435/600) | 70.00% (420/600) |
| SICA | **65.00%** (390/600) | 64.83% (389/600) |
| Δ (SICA−SC) | −7.50 pp | −5.17 pp |
| McNemar p | < 0.000001 (b=13, c=58) | — |

**Tiebreaking impact**: 18 SC answers changed (16 ✗→✓, 1 ✓→✗, 1 ✗→✗ = net +15), 1 SICA answer changed (✗→✓ = net +1). Alphabetical tiebreaking systematically favors `False`/`True` over `Unknown` in ties, which aligns better with ground truth.

**vs. expected 72.33%**: We got 72.50%, off by 1 problem (435 vs 434). The 72.33% was from a separate run on westd-14391 which may have had slightly different traces. 72.50% is the correct recomputation from exp048's actual data.

Saved to `/root/symb_invariant_consensus/results/multi_seed/llama8b_pw_seed42/results_alphabetical.json`.

---
