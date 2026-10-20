# exp_061 Cartpole CIVO Trigger Analysis

## Result: NEGATIVE — No CIVO in Cartpole Swingup

Config: trained dt_emb (d=32), subsample ON, H=8, gate_fixed_dt=2, 3 seeds × 112K steps

### VE Ratio (CIVO Diagnostic)

| Seed | ve_ratio peak | ve_ratio@105K | civo_alert |
|------|--------------|---------------|------------|
| s0   | 0.058 @55K   | 0.044         | NONE       |
| s1   | 0.040 @35K   | 0.035         | NONE       |
| s2   | 0.043 @35K   | 0.041         | NONE       |

**All ve_ratios < 0.06, far below 1.5x CIVO threshold.** No overestimation detected.

### Performance vs Baseline (exp_060, dt=1)

| Metric | exp_060 baseline | exp_061 trigger | Delta |
|--------|-----------------|-----------------|-------|
| eval_return s0 | ~809 (train) | 211.1 | -74% |
| eval_return s1 | ~684 (train) | 269.0 | -61% |
| eval_return s2 | 557 (eval@105K) | 228.9 | -59% |

### Value Function Analysis

| Seed | value_mean@105K | eval_return@105K | ratio |
|------|----------------|------------------|-------|
| s0   | 9.229          | 211.1            | 0.044 |
| s1   | 9.323          | 269.0            | 0.035 |
| s2   | 9.460          | 228.9            | 0.041 |

Value estimates remain well below actual returns across all seeds. No value inflation.

### Comparison: Walker CIVO (exp_008d) vs Cartpole (exp_061)

| Metric | Walker exp_008d | Cartpole exp_061 |
|--------|----------------|------------------|
| ve_ratio peak | 1.666 @55K | 0.058 @55K |
| civo_alert | YES @45K | NONE |
| Performance vs baseline | -68% + collapse | -59% stable |
| Value overestimation | YES (137.88 vs 82.75) | NO (9.3 vs 236) |

### exp_062 Control Status (gate_dt_embed_dim=0, no dt_emb)

| Seed | step | eval_return | value_mean | status |
|------|------|-------------|------------|--------|
| s0   | 112K | 230.4       | 12.9       | DONE   |
| s1   | 112K | 255.3       | 10.2       | DONE   |
| s2   | 108K | 248.8       | 11.8       | RUNNING |

exp_062 (no dt_emb) eval_returns (230-255) are SIMILAR to exp_061 (211-269), suggesting the performance drop from baseline is due to dt=2 temporal resolution, not the dt_emb specifically.

### Interpretation

1. **CIVO is NOT universal across DMC locomotion** — it triggers in Walker and HalfCheetah but not Cartpole
2. **Performance degradation exists but is NOT CIVO-mediated** — value function stays calibrated (no overestimation)
3. **dt=2 itself hurts Cartpole** — exp_062 control shows similar degradation without dt_emb, confirming the performance loss is from reduced temporal resolution
4. **Cartpole may be resistant to CIVO** because its dynamics are simpler (1 DoF pendulum vs multi-joint locomotion), making RSSM fidelity gap less severe at dt=2

### Implications for Paper

- CIVO scope should be described as "multi-joint locomotion" rather than "all DMC"
- Cartpole serves as a useful negative control demonstrating CIVO specificity
- Consider adding Cartpole as a "where CIVO doesn't apply" discussion point
