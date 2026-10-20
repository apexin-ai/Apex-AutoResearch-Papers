# exp_036_dual_critic_pickcube Analysis

## Summary

**Conclusion: NEGATIVE** — Dual-critic on PickCube does not provide evidence for the intervention hierarchy hypothesis. CIVO never manifested on PickCube regardless of intervention (neither in this experiment nor in baseline/TCN experiments), so dual-critic had nothing to suppress. Performance (eval 27.7) is statistically indistinguishable from the CIVO-trigger config baseline (eval 26.6), and both are ~53% below the vanilla DreamerV3 baseline (eval 58.6). The subsample+dt_emb config itself degrades PickCube performance, and no intervention (TCN or dual-critic) recovers the gap.

## Key Metrics

| Metric | Value |
|--------|-------|
| Final eval_return | 27.7 (at 202.5K) |
| Peak eval_return | 27.7 (at 202.5K) |
| Final ve_ratio (NVE) | 0.2 |
| Peak ve_ratio (NVE) | 2.3 (at 32.5K) |
| CIVO alerts | 0 |
| v1-v2 max divergence | 0.0 (identical throughout) |
| Final step | ~212K (dataset), 202.5K (last eval) |
| EXIT_CODE | 0 |

### Eval Return Trajectory
| Step | eval_return |
|------|-------------|
| 2.5K | 2.0 |
| 12.5K | 17.5 |
| 22.5K | 17.5 |
| 32.5K | 11.6 |
| 42.5K | 15.6 |
| 52.5K | 11.7 |
| 62.5K | 18.8 |
| 72.5K | 5.4 |
| 82.5K | 22.5 |
| 92.5K | 18.1 |
| 102.5K | 8.4 |
| 112.5K | 7.1 |
| 122.5K | 9.1 |
| 132.5K | 12.8 |
| 142.5K | 14.0 |
| 152.5K | 13.1 |
| 162.5K | 16.2 |
| 172.5K | 19.7 |
| 182.5K | 16.8 |
| 192.5K | 13.7 |
| 202.5K | 27.7 |

### ve_ratio (NVE) Trajectory
| Step | ve_ratio |
|------|----------|
| 12.5K | 0.2 |
| 22.5K | 1.0 |
| 32.5K | **2.3** (peak) |
| 42.5K | 1.4 |
| 52.5K | 1.4 |
| 62.5K | 0.6 |
| 72.5K | 1.6 |
| 82.5K | 0.3 |
| 92.5K | 0.3 |
| 102.5K | 0.6 |
| 112.5K | 0.7 |
| 122.5K | 0.5 |
| 132.5K | 0.4 |
| 142.5K | 0.3 |
| 152.5K | 0.4 |
| 162.5K | 0.3 |
| 172.5K | 0.3 |
| 182.5K | 0.3 |
| 192.5K | 0.4 |
| 202.5K | 0.2 |

### Value Critic Convergence (v1 vs v2)
v1 and v2 are **perfectly identical** at every logged checkpoint:
| Step | value1_mean | value2_mean |
|------|-------------|-------------|
| 2.5K | 0.0 | 0.0 |
| 12.5K | 3.8 | 3.8 |
| 22.5K | 17.9 | 17.9 |
| 32.5K | 26.9 | 26.9 |
| 42.5K | 21.2 | 21.2 |
| 52.5K | 16.1 | 16.1 |
| 62.5K | 11.6 | 11.6 |
| 72.5K | 8.7 | 8.7 |
| 82.5K | 7.2 | 7.2 |
| 92.5K | 6.0 | 6.0 |
| 102.5K | 5.3 | 5.3 |
| 112.5K | 5.1 | 5.1 |
| 122.5K | 5.0 | 5.0 |
| 132.5K | 4.9 | 4.9 |
| 142.5K | 4.9 | 4.9 |
| 152.5K | 5.3 | 5.3 |
| 162.5K | 5.7 | 5.7 |
| 172.5K | 5.6 | 5.6 |
| 182.5K | 5.6 | 5.6 |
| 192.5K | 5.6 | 5.6 |
| 202.5K | 5.8 | 5.8 |

## CIVO Analysis

**CIVO was NOT triggered.** Zero CIVO alerts throughout training. Peak ve_ratio of 2.3 occurred early (32.5K) during the initial value estimate ramp-up, then rapidly self-corrected to <1.0 by 82.5K and remained low for the rest of training.

However, this is a **vacuous result**: CIVO also does not occur on PickCube without dual-critic. Comparison of ve_ratio across PickCube experiments:

| Experiment | Config | Peak ve_ratio | Step | Self-corrects? |
|------------|--------|--------------|------|----------------|
| exp_036 (this) | Dual Critic | 2.3 | 32.5K | Yes, by 82.5K |
| exp_031 | TCN σ=0.2 | 3.7 | 52.5K | Yes, by 82.5K |
| exp_031b | TCN σ=0.5 | 3.3 | 42.5K | Yes, by 82.5K |
| exp_019b | CIVO config (no intervention) | N/A (not logged) | - | - |

All PickCube experiments show moderate early ve_ratio that **self-corrects without intervention**. CIVO (the runaway positive feedback loop seen in Walker/Cheetah) never develops. This is likely because PickCube's value scale is too low (~5-27) for the overestimation dynamics to compound — compared to Walker (~200-900) and Cheetah (~100-300) where values are an order of magnitude higher.

## Cross-Environment Comparison

### Eval Performance
| Environment | Dual-Critic Eval | Baseline Eval | Recovery % |
|-------------|-----------------|---------------|------------|
| **Walker** (exp_032) | 787.7 | ~900 (exp_008e_v3_s4) | 87.5% |
| **Cheetah** (exp_034) | 97.5 | 247.8 (exp_010b peak) | 39.3% |
| **PickCube** (exp_036) | 27.7 | 26.6 (exp_019b) | ~100% (no degradation) |

### CIVO Suppression
| Environment | CIVO in baseline? | Dual-Critic NVE | CIVO suppressed? |
|-------------|-------------------|------------------|-----------------|
| **Walker** | Yes (NVE>3) | max 1.1 | **Yes** (fully prevented) |
| **Cheetah** | Yes (NVE=70.6) | max 1.8 | **Partially** (triggered but mitigated) |
| **PickCube** | No (self-corrects) | max 2.3 | **N/A** (nothing to suppress) |

### v1 vs v2 Convergence
All three environments show v1 ≈ v2 throughout training — the two critics converge to identical estimates. This consistent pattern suggests the dual-critic architecture does not introduce useful diversity in value estimation; both critics learn the same function.

### PickCube-Specific Finding: Config Degradation
The subsample+dt_emb config itself severely degrades PickCube performance:
- **exp_019a_v2 (vanilla DreamerV3)**: peak 69.7, final 58.6
- **exp_019b (CIVO config, no intervention)**: peak 26.9, final 26.6
- **exp_036 (CIVO config + dual-critic)**: peak 27.7, final 27.7

The ~53% performance drop from vanilla baseline to CIVO config is NOT from CIVO — it's from the config itself (dt_emb + subsample + H=8) being suboptimal for manipulation tasks. Dual-critic does not recover this gap.

## Conclusion

**Hypothesis rejected.** The experiment was designed to test whether dual-critic suppresses CIVO on PickCube, providing evidence that architecture-level intervention generalizes across all 3 environments (Walker + Cheetah + PickCube). The result is **negative/inconclusive** because:

1. **CIVO never manifests on PickCube** — with or without dual-critic, the value estimation error self-corrects. The low value scale (~5-27) doesn't support the runaway overestimation dynamics that drive CIVO in locomotion tasks.

2. **Dual-critic provides no performance benefit** — eval 27.7 vs baseline 26.6 is within noise.

3. **The intervention hierarchy claim is NOT strengthened** — we cannot claim "dual-critic generalizes across all 3 environments" when one environment (PickCube) doesn't exhibit the phenomenon being intervened upon.

4. **PickCube is a poor test environment for CIVO** — the manipulation task's value scale and dynamics differ fundamentally from locomotion tasks. Future CIVO studies should focus on environments where CIVO naturally occurs.

### Updated Cross-Environment Pattern
- **Walker**: Dual-critic **fully prevents** CIVO (NVE ≤ 1.1, eval 787.7)
- **Cheetah**: Dual-critic **partially mitigates** CIVO (NVE 1.8, eval 97.5 — 40x better than unmitigated)
- **PickCube**: Dual-critic is **irrelevant** (CIVO doesn't occur, performance unchanged)

The dual-critic intervention shows environment-dependent efficacy, effective where CIVO exists (Walker > Cheetah) but vacuous where it doesn't (PickCube).
