# analysis pi05 spatial batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-spatial-batch_20260526T134314_result.json`
- **Structured JSON:** [`7ab15638f4dd03ab62fa.json`](../../sessions/7a/7ab15638f4dd03ab62fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 experiments completed successfully. Here are the results:

## π0.5 Spatial Results (bjb2-28827)

| exp_id | mode | seed | SR% | trigger_rate | n_rollouts | n_tasks |
|--------|------|------|-----|-------------|------------|---------|
| pi05-crm-k2-spatial-s42-bjb2-r2 | CRM | 42 | 96.5% (193/200) | N/A | 20 | 10 |
| pi05-crm-k2-spatial-s43-bjb2-r2 | CRM | 43 | 97.0% (194/200) | N/A | 20 | 10 |
| pi05-crm-k2-spatial-s44-bjb2-r2 | CRM | 44 | 97.0% (194/200) | N/A | 20 | 10 |
| pi05-adaptive-spatial-s42-bjb2-r2 | Adaptive | 42 | 96.5% (193/200) | 4.8% | 20 | 10 |
| pi05-adaptive-spatial-s43-bjb2-r2 | Adaptive | 43 | 98.0% (196/200) | 4.4% | 20 | 10 |
| pi05-adaptive-spatial-s44-bjb2-r2 | Adaptive | 44 | 97.0% (194/200) | 3.9% | 20 | 10 |

**CRM (always-on) mean ± std: 96.83 ± 0.29%**
**Adaptive (τ=0.25) mean ± std: 97.17 ± 0.76%**
**Adaptive mean trigger_rate: 4.37%**

Adaptive achieves comparable SR (97.17% vs 96.83%) while only triggering CRM on ~4.4% of steps. The hardest task across both modes is `on_the_ramekin` (80-95% depending on seed/mode).

---
