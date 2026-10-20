# eval grid b2 0 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b2_0_seed456_20260515T091612_result.json`
- **Structured JSON:** [`6e46998f2dd5b09a77be.json`](../../sessions/6e/6e46998f2dd5b09a77be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**grid_b2_0_seed456 eval_ppl_holdout = 17.989**

| Experiment | seed | eval_ppl | delta vs seed456 |
|---|---|---|---|
| b=0.5 seed456 | 456 | 17.65 | — |
| b=1.0 seed456 | 456 | 17.68 | — |
| b=1.5 seed456 | 456 | 17.71 | — |
| **b=2.0 seed456** | **456** | **17.99** | — |
| b=2.0 seed42 | 42 | 17.74 | -0.25 |
| b=2.0 seed123 | 123 | 17.73 | -0.26 |

PPL=17.99 is an outlier for b=2.0 — 0.25 higher than seed42/seed123. train_loss=10.625 is consistent across seeds, so the convergence was normal. The likely cause is this run used `--bf16` training (added for the resume from checkpoint-3500) while the other b=2.0 seeds trained in fp32. The dtype change could have introduced a slight divergence in later training steps that accumulated into a measurable eval difference.

---
