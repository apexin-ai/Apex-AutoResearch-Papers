# eval old 41312 experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_old_41312_experiments_20260518T094841_result.json`
- **Structured JSON:** [`98fcbd17509966844a99.json`](../../sessions/98/98fcbd17509966844a99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 evals completed. Here's the full results summary:

## Eval Results (ρ=0.4, Qwen3-0.6B, 5000 docs, 4,077,068 tokens each)

| Experiment | PPL | Loss | Tokens | Time |
|---|---|---|---|---|
| **ess_only_seed123** | 17.721 | 2.8747 | 4,077,068 | 174s |
| **ess_only_seed456** | 17.762 | 2.8770 | 4,077,068 | 164s |
| **random_reweight_seed456** | 17.777 | 2.8779 | 4,077,068 | 131s |

### Combined with prior results (all ρ=0.4):

| Method | Seed 42 | Seed 123 | Seed 456 | Mean |
|---|---|---|---|---|
| **uniform** | 17.695 | — | — | — |
| **ess_only** | 17.693 | **17.721** | **17.762** | 17.725 |
| **random_reweight** | 17.787 | 17.801 | **17.777** | 17.788 |

ESS-only consistently outperforms random reweighting across all 3 seeds. Uniform (seed 42 only) is the best single run at 17.695.

---
