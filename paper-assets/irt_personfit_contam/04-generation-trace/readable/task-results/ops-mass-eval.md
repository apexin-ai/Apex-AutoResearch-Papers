# ops mass eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mass-eval_20260523T124335_result.json`
- **Structured JSON:** [`b6689b423cceb5bc6c49.json`](../../sessions/b6/b6689b423cceb5bc6c49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**All 9 evals complete.** Here's the full summary:

## Results Summary

| Experiment | Model | Condition | lz_star | acc_overall | acc_seen | acc_unseen | Cohen's d |
|---|---|---|---|---|---|---|---|
| exp-llama-25pct-s1 | Llama | contam_25 | -4.616 | 0.672 | 0.770 | 0.639 | **-5.124** |
| exp-llama-15pct-s3 | Llama | contam_15_s3 | -4.507 | 0.658 | 0.785 | 0.636 | **-4.994** |
| exp-llama-5pct-s2 | Llama | contam_5_s2 | -4.460 | 0.636 | 0.786 | 0.629 | **-4.938** |
| exp-llama-25pct-s2 | Llama | contam_25_s2 | -3.249 | 0.679 | 0.777 | 0.647 | **-3.496** |
| exp-llama-50pct-s3 | Llama | contam_50_s3 | -2.810 | 0.712 | 0.768 | 0.656 | **-2.973** |
| exp-mistral-5pct-s2 | Mistral | contam_5_s2 | -5.896 | 0.569 | 0.771 | 0.559 | **-4.835** |
| exp-mistral-50pct-s3 | Mistral | contam_50_s3 | -5.236 | 0.677 | 0.751 | 0.603 | **-4.512** |
| exp-mistral-15pct-s3 | Mistral | contam_15_s3 | -3.127 | 0.597 | 0.770 | 0.567 | **-3.485** |
| exp-mistral-5pct-s1 | Mistral | contam_5 | -1.766 | 0.571 | 0.766 | 0.560 | **-2.822** |

All experiments registered with metrics and marked as `success`. All Cohen's d values are strongly negative (|d| > 2.8), indicating robust contamination detection across all conditions, models, and seeds.

---
