# analysis aggregation loglog canonical

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aggregation-loglog-canonical_20260522T182814_result.json`
- **Structured JSON:** [`4eb7ddab22c8327a5246.json`](../../sessions/4e/4eb7ddab22c8327a5246.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sanity check passed. Results:

| Method | η_max FDR sig | K_eff FDR sig | K_pos | K_neg | Mean R² |
|---|---|---|---|---|---|
| majority_vote | 11/12 | 8/12 | 7 | 1 | 0.3760 |
| weighted_vote | 11/12 | 11/12 | 11 | 0 | 0.3572 |
| threshold_unanimous | 12/12 | 11/12 | 10 | 1 | 0.9017 |
| bayesian | 9/12 | 5/12 | 1 | 4 | 0.1053 |

JSON saved to `/root/cert_manip_resist_eval/artifacts/results/plan001/aggregation_regression_15model_loglog.json`.

Key findings:
- **Weighted vote** and **threshold unanimous** make K_eff significant in nearly all conditions (11/12), compared to 8/12 for majority vote
- **Threshold** achieves extremely high R² (0.90) — the log-log spec fits near-perfectly when only unanimous pairs are counted
- **Bayesian** shows the weakest K_eff signal (5/12 sig), and notably K_eff β is *negative* in 4 of 5 sig conditions — accuracy-weighted Bayesian aggregation effectively absorbs the diversity effect
- η_max is robust across all methods (9–12/12 sig)

---
