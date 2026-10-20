# analysis exp010 mistral v3 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp010-mistral-v3-results_20260517T081841_result.json`
- **Structured JSON:** [`3d193efd5e963f323e65.json`](../../sessions/3d/3d193efd5e963f323e65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

McNemar with 2 vs 2 discordant pairs gives p=1.0 (exact binomial). All metrics collected.

```
METRICS:
- n: 60
- sica_accuracy: 48.33%
- sc_accuracy: 48.33%
- delta_pp: +0.00pp
- multi_candidate_rate: 6.67% (4/60)
- extraction_rate: 88.19%
- discordant_sica_wins: 2
- discordant_sc_wins: 2
- proofwriter: sica=40.00%, sc=40.00%, gap=0pp
- folio: sica=56.67%, sc=56.67%, gap=0pp
- McNemar p-value: 1.000 (2 vs 2 discordant, trivially non-significant)
- truncated_traces: 0
- answer_extraction_rate: 100% (all boxed, 0 fallback, 0 none)
- contradiction_rate: 5.62%
- k: 12

CONCLUSION: negative
NOTE: SC accuracy 48.33% > 40% threshold but SICA provides zero lift (delta=0.00pp). Only 4/60 problems (6.67%) had SICA disagree with SC, and those split evenly 2-2. Model too weak for constraint extraction to be meaningful — non-unanimous SC votes in 30/60 problems but SICA only reranked 4, indicating extracted constraints rarely had enough signal to override majority vote.
```

---
