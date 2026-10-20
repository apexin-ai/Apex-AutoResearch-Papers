# analysis mlp verifier upgrade

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mlp_verifier_upgrade_20260517T083302_result.json`
- **Structured JSON:** [`e49386b19bea5fe6add7.json`](../../sessions/e4/e49386b19bea5fe6add7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `output/r17_analyses/mlp_verifier_comparison.json`.

## Summary

Existing exp-027 already ran MLP/RF verifier comparison on SciERC NER N=16 data (3 seeds, 551 instances each). Results:

```
Model              | AUROC  | Sel F1 | Δ vs Greedy | Gap Closed
─────────────────────────────────────────────────────────────────
Greedy baseline    |   --   | 0.6441 |     --      |    0%
Best unsup (LP)    |   --   | 0.6470 | +0.0029pp   |   1.6%
LR (5 feat)        | 0.6522 | 0.6407 | -0.0034pp   |  -1.9%
MLP (5 feat)       | 0.6393 | 0.6386 | -0.0055pp   |  -3.1%
RF (5 feat)        | 0.5868 | 0.6154 | -0.0287pp   | -16.0%
MLP (15 feat)      | 0.6322 | 0.6339 | -0.0102pp   |  -5.7%
RF (15 feat)       | 0.6043 | 0.6146 | -0.0295pp   | -16.5%
Oracle             |   --   | 0.8231 | +0.1790pp   |  100%
```

**Verdict: Feature bottleneck** (supports paper conclusion).
- MLP AUROC (0.6393) ≤ LR AUROC (0.6522), Δ = -0.0129
- Adding 10 interaction features makes MLP worse (0.6322)
- All supervised models fail to beat even greedy baseline in selection F1
- The 5 confidence signals lack discriminative power; nonlinear models can't extract more signal from them

---
