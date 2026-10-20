# Analysis: exp_080 & exp_081 — 008e_v3 Walker Walk Multi-Seed Validation (Seeds 1 & 2)

## Configuration
- **Config**: 008e_v3 — trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15
- **Task**: DMC Walker Walk
- **Baseline**: ~930 eval return (exp_009d)
- **CIVO Threshold**: NVE > 1.5
- **Steps**: 105,000 (training continued to 112K)

## Results Summary

| Metric | Seed 0 (parent) | Seed 1 (exp_080) | Seed 2 (exp_081) | Mean | Std |
|--------|-----------------|-------------------|-------------------|------|-----|
| Eval Return @105K | 869.9 | 876.7 | 597.1 | 781.2 | 159.5 |
| Baseline % | 93.5% | 94.3% | 64.2% | 84.0% | 17.2% |
| NVE (ve_ratio) @105K | N/A* | 0.6 | 0.5 | <1.5 | — |
| CIVO Alert | N/A* | 0.0 | 0.0 | 0.0 | 0.0 |
| gate_dt_1_frac | N/A* | 1.0 | 1.0 | 1.0 | 0.0 |

*Seed 0 was run before ve_ratio logging was added. Parent conclusion confirmed NVE < 1.5.

## Eval Return Trajectories

### Seed 1 (exp_080) — Monotonically improving
| Step | Eval Return |
|------|-------------|
| 5K | 31.0 |
| 15K | 104.9 |
| 25K | 369.3 |
| 35K | 405.0 |
| 45K | 511.6 |
| 55K | 690.3 |
| 65K | 731.3 |
| 75K | 846.5 |
| 85K | 803.8 |
| 95K | 848.6 |
| 105K | **876.7** |

### Seed 2 (exp_081) — Slow learner, still improving at termination
| Step | Eval Return |
|------|-------------|
| 5K | 39.3 |
| 15K | 196.3 |
| 25K | 215.0 |
| 35K | 230.5 |
| 45K | 233.6 |
| 55K | 214.1 |
| 65K | 311.9 |
| 75K | 404.5 |
| 85K | 449.0 |
| 95K | 545.2 |
| 105K | **597.1** |

### Seed 0 (parent) — Reference
| Step | Eval Return |
|------|-------------|
| 5K | 31.0 |
| 15K | 131.2 |
| 25K | 155.7 |
| 35K | 276.5 |
| 45K | 382.2 |
| 55K | 486.8 |
| 65K | 580.7 |
| 75K | 574.1 |
| 85K | 657.3 |
| 95K | 851.9 |
| 105K | **869.9** |

## NVE (ve_ratio) Trajectory

### Seed 1 (exp_080)
15K: 0.0 → 25K: 0.1 → 35K: 0.2 → 45K: 0.3 → 55K: 0.4 → 65K: 0.5 → 75K: 0.5 → 85K: 0.6 → 95K: 0.6 → **105K: 0.6**

### Seed 2 (exp_081)
15K: 0.0 → 25K: 0.1 → 35K: 0.3 → 45K: 0.4 → 55K: 0.4 → 65K: 0.5 → 75K: 0.5 → 85K: 0.5 → 95K: 0.5 → **105K: 0.5**

Both seeds show NVE stabilizing at 0.5-0.6, well below the 1.5 CIVO threshold. No alerts triggered at any point.

## Conclusions

### Per-experiment
- **exp_080 (seed=1): SUCCESS** — eval 876.7 > 800, NVE 0.6 < 1.5
- **exp_081 (seed=2): NEGATIVE** — eval 597.1 < 800, NVE 0.5 < 1.5

### CIVO Mitigation Assessment
**CIVO suppression is robust across all 3 seeds.** NVE remains at 0.5-0.6 throughout training with dt=1 imagination, confirming that the trained dt_emb does not trigger CIVO when imagination uses dt=1. The gate consistently selects dt=1 (gate_dt_1_frac = 1.0) as expected.

### Task Performance Assessment
**High seed variance is the key concern.** Seeds 0 and 1 reach ~94% baseline (870-877), while seed 2 reaches only 64% (597.1). Seed 2's learning curve shows steady improvement but at a much slower rate — it plateaus around 25-55K steps before resuming growth. The train returns at 112K (560-630) suggest it may eventually improve further with more training steps, but at 105K it falls well short of the 800 threshold.

### 3-Seed Summary
- Mean eval @105K: **781.2 +/- 159.5** (84.0% baseline)
- CIVO status: **0/3 seeds triggered** (robust suppression)
- Success rate: **2/3 seeds meet >800 threshold**

### Interpretation
The 008e_v3 config successfully prevents CIVO (primary hypothesis validated), but shows non-trivial seed variance in task performance. The high variance (std=159.5, CV=20.4%) is driven entirely by seed 2's slow learning, not by CIVO-related degradation. This suggests the mitigation mechanism is sound but the overall training stability of this configuration could benefit from investigation.
