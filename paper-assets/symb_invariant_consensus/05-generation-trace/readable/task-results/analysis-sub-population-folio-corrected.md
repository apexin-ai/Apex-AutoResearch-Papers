# analysis sub population folio corrected

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sub-population-folio-corrected_20260521T012039_result.json`
- **Structured JSON:** [`c558128f484dfde98fe9.json`](../../sessions/c5/c558128f484dfde98fe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files updated. Verification checklist:

| Check | Result |
|-------|--------|
| Corrected SC overall FOLIO accuracy | 114/204 = 55.88% ✓ |
| SICA accuracy unchanged | 121/204 = 59.31% ✓ |
| Overall Δ | +3.43pp (not +4.9pp) ✓ |
| McNemar p-value increased | 0.092 (was 0.013) ✓ |
| PW-600 data unchanged | ✓ |

Key changes from the correction:
- 7 SC answers changed (alphabetical tiebreaking resolves ties differently from the old rule)
- Net +3 correct for SC (111→114), shrinking the SICA advantage
- Overall FOLIO McNemar p goes from 0.013 to 0.092 — **no longer significant at α=0.05**
- **False** subgroup: SC now matches SICA exactly (42.9% vs 42.9%, Δ=0.0)
- **Mid-constraint tertile** becomes the strongest signal: +9.4pp, p=0.031 (significant)
- **High-constraint tertile**: Δ collapses to 0.0pp (was +4.5pp)

---
