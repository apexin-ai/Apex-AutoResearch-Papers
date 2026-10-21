# analyze sweep b005 s43 retry

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_sweep-b005-s43-retry_20260517T094735_result.json`
- **Structured JSON:** [`dda2b636554886c16424.json`](../../sessions/dd/dda2b636554886c16424.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. Here's the summary:

---

## sweep-isr-b005-s43: **Training completed, eval done**

| Metric | Value |
|--------|-------|
| **Prove Rate** | 99.0% (99/100) |
| **Mean ISR** | 0.5517 ± 0.1597 |
| **Median ISR** | 0.5000 |
| **Proved-only ISR** | 0.5572 |
| **Checkpoint** | `/root/autodl-tmp/outputs/sweep_isr_b005_s43/` (final model + checkpoint-500) |
| **Eval JSON** | `/root/autodl-tmp/outputs/sweep_isr_b005_s43/eval_results.json` |

Training log final stats: prove_rate=0.752, mean_isr=0.364 (training set). Eval on test set shows very high prove rate (99%) with moderate ISR collapse (median 0.5).

## sweep-random-b005-s43: **Still training**

- Currently at step **223/500** (~45%)
- ETA: ~68 minutes (~19:10 server time)
- Running on GPU 1
- Has checkpoint-200 saved

## Disk status

`/root/autodl-tmp`: **85G/250G used (34%)** — healthy, no risk of disk-full failure this time.

---

The ISR b005 s43 result is notable: 99% prove rate but ISR stays around 0.5 (not collapsing to near-zero like stronger ISR betas). The random experiment needs ~1 more hour. Want me to check back when it finishes?

---
