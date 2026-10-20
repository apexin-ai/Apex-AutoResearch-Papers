# analysis discriminative rate full v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_discriminative-rate-full-v2_20260518T040537_result.json`
- **Structured JSON:** [`b9e0f3b0d54a5287c867.json`](../../sessions/b9/b9e0f3b0d54a5287c867.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results:

**Full 804-Instance Discriminative Rate:**

| Metric | Value | 95% CI |
|--------|-------|--------|
| Disc rate (weight) | **39.2%** | [38.7%, 39.8%] |
| Disc rate (count, est.) | **12.1%** | [12.0%, 12.3%] |
| Problems with any disc | 289/307 (94.1%) | - |

**Per-domain:** ProofWriter 36.4% (weight), FOLIO 54.0% (weight).

**Pilot validation:** Corrected formula on pilot subset yields 37.6% vs pilot exact 37.2%, delta = **0.38pp** (vs previous worker's 9.8pp error). The fix was accounting for asymmetric assertion weights in the scorer formula (majority assertion satisfied vs minority excluded with 0.5 penalty).

**Estimated count rate (12.1%)** is consistent with pilot's 11.5%, confirming that ~88% of unique constraints are domain facts shared across answers.

Files saved:
- `/root/symb_invariant_consensus/analysis/discriminative_rate_full_804.json`
- `/root/symb_invariant_consensus/analysis/discriminative_rate_report.md`
- `/root/symb_invariant_consensus/analysis/discriminative_rate_v2.py`

---
