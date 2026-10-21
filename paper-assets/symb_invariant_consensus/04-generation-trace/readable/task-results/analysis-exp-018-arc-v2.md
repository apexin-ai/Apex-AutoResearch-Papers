# analysis exp 018 arc v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-018-arc-v2_20260517T064035_result.json`
- **Structured JSON:** [`23a7f61c184fcb5b8ecf.json`](../../sessions/23/23a7f61c184fcb5b8ecf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the analysis:

**Discordant pairs:**
- `arc_challenge_034`: SICA wrong (B), SC right → **SC wins**
- `arc_challenge_049`: both wrong (C, gt=D) → concordant
- `arc_challenge_052`: both wrong (D, gt=B) → concordant

**Multi-candidate rate:** `unique_after_dedup > 1` in 5/60 problems (values: 4, 3, 2, 2, 2) → 8.33%

**Extraction rate:** all 60 problems have `traces_with_constraints=12` out of `total_extracted=12` → 100%

**Contradictions (excluded > 0):** 3 problems

---

```
METRICS:
- n: 60
- k: 12
- sica_accuracy: 95.00% (57/60)
- sc_accuracy: 96.67% (58/60)
- delta_pp: -1.67pp
- multi_candidate_rate: 8.33% (5/60)
- extraction_rate: 100% (60/60)
- contradiction_detected: 3
- bootstrap_p: N/A (not computed in output)
- discordant_sica_wins: 0
- discordant_sc_wins: 1

CONCLUSION: success
REASON: SICA ≈ SC (gap -1.67pp, only 1 discordant pair favoring SC), supports capability trap claim that symbolic constraints do not improve over majority voting on ARC-Challenge; very high model accuracy (96.67%) leaves minimal room for differentiation.
CHECKPOINT_PATH: /root/symb_invariant_consensus/results/exp018_arc/exp018_results.json
```

---
