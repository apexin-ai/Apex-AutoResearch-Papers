# analysis r6 2b r2 bootstrap ci

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6-2b-r2-bootstrap-ci_20260525T074625_result.json`
- **Structured JSON:** [`e8f12bd33facf9040a69.json`](../../sessions/e8/e8f12bd33facf9040a69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. The point estimates differ slightly from the registry values because the underlying data has been updated since those were computed, but the pattern is the same and the bootstrap confirms significance.

**Results summary:**

| Metric | Point Estimate | 95% CI |
|--------|---------------|--------|
| RF (Random Fault) R² | 0.730 | [0.718, 0.745] |
| Adaptive R² | 0.285 | [0.270, 0.301] |
| Δ (RF − Adaptive) | 0.446 | [0.430, 0.460] |

- **Δ CI excludes 0** → difference is statistically significant (p < 0.001 equivalent)
- RF R² is stable across both datasets (mmlu: 0.727, arc: 0.733)
- Adaptive R² varies substantially across conditions (0.079–0.535)

The point estimates differ from the registry (rf=0.705, adaptive=0.256) because the score data has been updated since those values were recorded (API model score files were regenerated with updated model names/versions). The methodology and conclusion are unchanged: the K_eff diversity model explains significantly more variance under independent faults (R²≈0.73) than under adaptive attacks (R²≈0.28), confirming that adaptive attackers break the independence assumption.

Output saved to `/root/cert_manip_resist_eval/artifacts/results/plan001/r2_bootstrap_ci.json`.

---
