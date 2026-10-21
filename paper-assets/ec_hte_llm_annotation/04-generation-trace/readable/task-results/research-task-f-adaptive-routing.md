# research task f adaptive routing

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task-f-adaptive-routing_20260523T080949_result.json`
- **Structured JSON:** [`0fa59029b354af3ab689.json`](../../sessions/0f/0fa59029b354af3ab689.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are generated. Here's a summary:

## Outputs

1. **`results/exp_adaptive_routing.csv`** — 48 configurations, per-config aggregate RMSE
2. **`results/exp_adaptive_routing_subgroups.csv`** — 152 subgroup-level rows with diagnostic scores + RMSE
3. **`results/exp_adaptive_routing_sweep.csv`** — threshold sweep (0 to 3.0, step 0.05)
4. **`results/exp_adaptive_routing_analysis.md`** — full analysis report
5. **`exp_adaptive_routing.py`** — reproducible analysis script

## Key Findings

**Adaptive routing works, especially under extreme heterogeneity:**
- K=2 extreme: adaptive RMSE 0.083 vs Global 0.100 (**17% improvement**) — the clear win case
- K=4 extreme: adaptive 0.125 vs Global 0.130 (4% improvement), but naive often still lower
- Homogeneous/moderate: adaptive = Global (correctly routes nothing to EC-HTE)

**Diagnostic accuracy**: 87.5% at threshold=1.0. Precision for routing to EC-HTE = 86.4%.

**Oracle threshold = 2.45**, but t=1.0 is within 0.16% — the theoretical threshold is near-optimal.

**Bias-variance tradeoff**: The diagnostic is a bias criterion. At small n_expert (<100), EC-HTE's estimation variance dominates, so even when the diagnostic correctly identifies global bias, routing to EC-HTE can increase RMSE. The routing is most valuable at n_expert ≥ 250.

**Characteristic failures**: 19/152 (12.5%) misrouted, mostly in the moderate regime where R_sym ∈ (0.3, 0.9) — below threshold but EC-HTE is slightly better. These are low-stakes errors (RMSE differences < 0.003).

---
