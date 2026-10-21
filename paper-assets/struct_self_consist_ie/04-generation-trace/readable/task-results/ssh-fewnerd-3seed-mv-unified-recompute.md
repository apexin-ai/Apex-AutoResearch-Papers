# ssh fewnerd 3seed mv unified recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewnerd_3seed_mv_unified_recompute_20260522T134228_result.json`
- **Structured JSON:** [`b3f5af1f691067ec85fb.json`](../../sessions/b3/b3f5af1f691067ec85fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 seeds computed. Results:

```
Seed 42:  greedy=0.7911, mv=0.7585, Δ=-3.27 pp, lp=0.7918, degen=9.1%
Seed 123: greedy=0.7909, mv=0.7648, Δ=-2.61 pp, lp=0.7918, degen=9.3%
Seed 456: greedy=0.7909, mv=0.7685, Δ=-2.24 pp, lp=0.7921, degen=8.1%
Mean±σ:   greedy=0.7910±0.0001, mv=0.7639±0.0041, mv_Δ=-2.71±0.43 pp, lp=0.7919±0.0001, degen=8.8±0.5%
```

All computed on gold-nonempty subset: n=32,565 of 37,648 instances.

MV strict **hurts** by -2.71 pp on average. LP-best is marginally better than greedy (+0.09 pp). Degeneracy is low (~8.8%), meaning the 8 samples do show diversity — but majority voting aggregation damages rather than helps.

---
