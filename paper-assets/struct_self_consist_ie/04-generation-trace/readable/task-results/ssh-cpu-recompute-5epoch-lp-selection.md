# ssh cpu recompute 5epoch lp selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cpu_recompute_5epoch_lp_selection_20260522T115415_result.json`
- **Structured JSON:** [`ef2599cad11624cfa041.json`](../../sessions/ef/ef2599cad11624cfa041.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results computed. Only 2 seeds available (no `fewnerd_5epoch_s456` exists).

```
Seed 42:  greedy=0.7944, lp_select=0.7959, Δ=+0.15 pp
Seed 123: greedy=0.7940, lp_select=0.7949, Δ=+0.09 pp
Mean±σ:   Δ = +0.12 ± 0.04 pp  (n=2 seeds)
vs 3-epoch: +1.39pp → +0.12 pp (-91.3% change)
```

Key observations:
- LP selection gain collapses from +1.39pp (3-epoch) to +0.12pp (5-epoch) — a **91% reduction**
- LP only selects a different sample from greedy ~6.3% of the time (5-epoch model is much more confident/peaked)
- Seed 456 data for 5-epoch does not exist on autodl-5090 (only seeds 42 and 123 have full 37648-instance runs)

---
