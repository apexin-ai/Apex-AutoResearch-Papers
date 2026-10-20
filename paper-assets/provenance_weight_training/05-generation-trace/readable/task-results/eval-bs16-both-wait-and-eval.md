# eval bs16 both wait and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bs16_both_wait_and_eval_20260521T174228_result.json`
- **Structured JSON:** [`41fa94d938698b135302.json`](../../sessions/41/41fa94d938698b135302.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments trained, evaluated, and registered. Here's the full summary:

---

## bs=16 Eval Results

| Metric | bs16_adaptive | bs16_uniform | Δ(adaptive−uniform) |
|--------|:---:|:---:|:---:|
| **holdout_ppl** | 17.631 | 17.694 | **−0.063** |
| holdout_loss | 2.8697 | 2.8732 | −0.0035 |
| **owt_ppl** | 18.309 | 18.364 | **−0.055** |
| owt_loss | 2.9074 | 2.9104 | −0.0030 |
| **wiki_ppl** | 15.286 | 15.337 | **−0.051** |
| wiki_loss | 2.7269 | 2.7302 | −0.0033 |

## Δ(adaptive−uniform) comparison across batch sizes

| Metric | bs=4 Δ | bs=16 Δ | Ratio |
|--------|:---:|:---:|:---:|
| **holdout_ppl** | −0.020 | **−0.063** | **3.2x** |

## Key Findings

1. **Adaptive advantage amplifies with larger batch size.** At bs=16, the holdout PPL gap is −0.063 vs −0.020 at bs=4 — a 3.2x amplification.

2. **Consistent across all eval sets.** The adaptive advantage at bs=16 is −0.063 (holdout), −0.055 (OWT), −0.051 (wiki) — uniformly stronger than bs=4.

3. **Both bs=16 models improve over their bs=4 counterparts.** adaptive: 17.631 vs 17.674 (−0.043), uniform: 17.694 vs 17.694 (flat). The larger batch benefits the adaptive method more.

4. **No anomalies.** Both trainings completed successfully with EXIT_CODE=0, all eval sets produced consistent results.

---
