# analysis v2 pattern mining

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v2-pattern-mining_20260523T184437_result.json`
- **Structured JSON:** [`e3f08d3f145cc33f4bcb.json`](../../sessions/e3/e3f08d3f145cc33f4bcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 output files saved. Summary:

---

### Part A: K=3 K_eff FDR by Attack Type
- **4/4 significant conditions are shared-bias**: mmluxsycophancy (0.032), mmluxverbosity_bias (0.032), mmluxauthority_bias (0.032), arc_challengexverbosity_bias (0.042)
- **0/6 targeted attacks** reach FDR significance at K=3
- **Mann-Whitney U**: p=0.147 (trend-level, underpowered with n=6/group), rank-biserial r=-0.39
- Targeted median FDR p = 0.082 vs shared-bias median = 0.037

### Part B: Aggregation R² Bootstrap (B=9999)
| Method | R² | 95% CI |
|--------|-----|--------|
| Threshold | 0.829 | [0.806, 0.859] |
| Majority | 0.327 | [0.309, 0.351] |
| Weighted | 0.328 | [0.311, 0.352] |
| Bayesian | 0.087 | [0.077, 0.106] |

All pairwise differences significant except Majority vs Weighted (CI includes 0). Threshold–Bayesian gap = 0.741 [0.712, 0.771].

### Part C: GAM Magnitude Gradient
- K=3/K=5: Kruskal-Wallis p=0.200/0.423 (not significant) — targeted and shared-bias slopes are NOT statistically distinguishable in magnitude
- Position_bias slopes (~0.4–0.85) are 30–60× smaller than others (~13–35) due to ASR scale difference
- All 12 conditions show positive slopes (direction_positive_rate = 1.0 for most)

### Part D: V2 Script Audit
| Script | Version | Needs Rerun |
|--------|---------|-------------|
| run_cross_benchmark_iv.py | V1 | Yes |
| run_sensitivity_analysis.py | N/A (reads stats) | Depends on upstream |
| run_sensitivity_analysis_poolA.py | N/A (reads stats) | Yes (upstream V1) |
| run_capability_matched.py | V1 | Yes |
| run_epsilon_sensitivity_k5.py | V1 | Yes |
| run_alt_diversity_effect_size.py | V1 | Yes |

---
