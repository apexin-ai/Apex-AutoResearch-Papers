# exp_walker_no_dt_emb_s1 Analysis Report

## Experiment Config
- **Env**: Walker Walk | **Seed**: 1
- **dt_embed_dim**: 0 (removed) | **gate+subsample**: ON (max_dt=2) | **imag_horizon**: 8
- **Hypothesis**: Removing dt_embedding should NOT produce CIVO (NVE < 2.0)
- **Steps**: 105K | **Logdir**: exp_walker_no_dt_emb_s1

## Eval Return Trajectory

| Step | eval_return | vs baseline (915.67) |
|------|-------------|----------------------|
| 5K   | 30.49       | 3.3%                 |
| 15K  | 179.84      | 19.6%                |
| 25K  | 309.81      | 33.8%                |
| 35K  | 195.24      | 21.3%                |
| 45K  | 265.96      | 29.0%                |
| 55K  | 304.73      | 33.3%                |
| 65K  | 325.06      | 35.5%                |
| 75K  | 241.39      | 26.4%                |
| 85K  | 303.22      | 33.1%                |
| 95K  | 214.47      | 23.4%                |
| 105K | **468.83**  | **51.2%**            |

- **Final**: 468.83 (51.2% of baseline 915.67)
- **Peak**: 468.83 at 105K
- **Pattern**: Zigzag oscillation (195-325 range from 35K-95K) with strong late surge at 105K

## Value Estimation Trajectory

| Step | value_mean | ve_ratio | baseline_ve | NVE (ve/baseline_ve) |
|------|-----------|----------|-------------|----------------------|
| 5K   | 0.001     | —        | —           | —                    |
| 15K  | 3.19      | 0.018    | 0.026       | 0.69                 |
| 25K  | 18.58     | 0.060    | 0.087       | 0.69                 |
| 35K  | 41.41     | 0.212    | 0.241       | **0.88**             |
| 45K  | 63.82     | 0.240    | 0.331       | 0.72                 |
| 55K  | 87.91     | 0.288    | 0.404       | 0.71                 |
| 65K  | 105.37    | 0.324    | 0.563       | 0.58                 |
| 75K  | 118.16    | 0.489    | 0.719       | 0.68                 |
| 85K  | 120.84    | 0.399    | 0.701       | 0.57                 |
| 95K  | 111.86    | 0.522    | 0.632       | 0.83                 |
| 105K | 107.88    | 0.230    | 0.656       | 0.35                 |

- **NVE_peak**: 0.88 at 35K
- **NVE_105K**: 0.35
- **NVE range**: 0.35 - 0.88 (all well below 2.0)
- **civo/alert**: 0 at every eval point

## CIVO Assessment (D155 Criteria)

| Criterion | Threshold | Observed | Met? |
|-----------|-----------|----------|------|
| NVE_peak > 2.0 | 2.0 | 0.88 | **NO** |
| Sustained ≥2 eval points | 2 points above 2.0 | 0 points | **NO** |
| Temporal causality | ve_ratio rise precedes eval collapse | No ve_ratio spike observed | **NO** |
| civo/alert triggered | alert = 1 | alert = 0 throughout | **NO** |

**CIVO triggered: NO**

## Gate Behavior

- gate_dt_mean = 2.0 throughout (constant)
- gate_dt_2_frac = 1.0 (100% dt=2 selection)
- gate_empirical_entropy = 0.0
- gate_entropy_ratio = 0.0
- With max_dt=2, gate has no choice diversity — always selects dt=2

## Seed Consistency: s1 vs s0 (exp_008f)

| Metric | Seed 0 (exp_008f) | Seed 1 (this) | Consistent? |
|--------|-------------------|---------------|-------------|
| eval_return_105K | 503 | 469 | Yes (similar range) |
| NVE | 0.30x | 0.35x (at 105K) | Yes |
| NVE_peak | — | 0.88 (at 35K) | Both < 2.0 |
| CIVO triggered | No | No | **Yes** |
| Pattern | Zigzag recovery | Zigzag + late surge | **Yes** |
| Gate behavior | dt=2 constant | dt=2 constant | Yes |

Both seeds show the same pattern: moderate performance (~50% baseline), no value inflation, zigzag eval trajectory with no CIVO.

## Conclusion: **SUCCESS** (hypothesis confirmed)

Removing dt_embedding (dt_embed_dim=0) with gate+subsample ON does **not** trigger CIVO across 2 seeds in Walker Walk. NVE stays well below 2.0 (peak 0.88x at 35K, final 0.35x at 105K). The causal control confirms that dt_embedding is necessary for CIVO onset — without it, value estimation tracks reasonably with returns despite gate+subsample being active.

Performance is degraded vs baseline (51.2%) but this is expected — gate+subsample with max_dt=2 and no dt_embedding limits the agent's temporal reasoning. The key finding is the absence of pathological value inflation, supporting the causal role of dt_embedding in CIVO.
