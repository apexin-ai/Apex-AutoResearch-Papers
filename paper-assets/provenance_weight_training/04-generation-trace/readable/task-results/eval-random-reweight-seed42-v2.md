# eval random reweight seed42 v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_random_reweight_seed42_v2_20260521T162400_result.json`
- **Structured JSON:** [`b0858af281fdef96ce7c.json`](../../sessions/b0/b0858af281fdef96ce7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results:

```
random_reweight_baseline_seed42:
  holdout_ppl: 17.95829
  holdout_loss: 2.88805
  ood_owt_ppl: 18.60614
  ood_owt_loss: 2.92349
  ood_wiki_ppl: 15.51906
  ood_wiki_loss: 2.74207

vs adaptive τ=0.7 ρ=0.4 (holdout PPL = 17.674): Δ = +0.284 (detector signal load-bearing? Y)
vs uniform ρ=0.4 (holdout PPL = 17.694): Δ = +0.264
```

Random reweight (17.958) is worse than both adaptive (17.674) and uniform (17.694). Shuffling the detector scores degraded performance, confirming the detector's contamination signal is **load-bearing** — the adaptive weighting benefit comes from the actual detector signal, not just the weight distribution shape or regularization artifact.

---
