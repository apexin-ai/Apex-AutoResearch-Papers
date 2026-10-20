# exp_034 Dual-Critic Cheetah Run — Final Analysis

## Configuration
- Environment: dmc_cheetah_run
- Method: DreamerV3 + dual_critic (min of two independent critics)
- Steps: 210K (ran to 215K eval), seed=0
- gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8

## eval_return Trajectory

| Step | eval_return | NVE (ve_ratio) | value_mean | value1_mean | value2_mean |
|------|-------------|----------------|------------|-------------|-------------|
| 5K   | 8.3         | —              | 0.001      | 0.001       | 0.001       |
| 15K  | 27.8        | 0.066          | 1.8        | 1.8         | 1.8         |
| 25K  | 108.7       | 0.100          | 10.9       | —           | —           |
| 35K  | 110.0       | 0.215          | 23.7       | —           | —           |
| **45K** | **315.7** | 0.123          | 38.8       | —           | —           |
| **55K** | **34.5**  | **1.753** ⚠️   | ~60.4      | —           | —           |
| 65K  | 81.5        | 0.726          | 59.2       | —           | —           |
| 75K  | 183.0       | 0.287          | 52.5       | —           | —           |
| 85K  | 88.4        | 0.527          | 46.6       | —           | —           |
| 95K  | 41.0        | 1.012          | 41.5       | —           | —           |
| **105K** | **27.2** | **1.591** ⚠️   | ~43.3      | —           | —           |
| 115K | 45.9        | 0.855          | 39.2       | —           | —           |
| 125K | 58.7        | 0.573          | 33.6       | —           | —           |
| 135K | 71.6        | 0.396          | 28.4       | —           | —           |
| 145K | 61.9        | 0.395          | 24.5       | —           | —           |
| 155K | 52.1        | 0.410          | 21.4       | —           | —           |
| 165K | 153.8       | 0.124          | 19.1       | —           | —           |
| 175K | 104.9       | 0.168          | 17.7       | —           | —           |
| 185K | 101.4       | 0.164          | 16.6       | —           | —           |
| 195K | 115.3       | 0.136          | 15.6       | —           | —           |
| 205K | 101.5       | 0.145          | 14.7       | 14.8        | 14.8        |
| 215K | 97.5        | 0.144          | 14.1       | 14.2        | 14.2        |

## CIVO Analysis

### CIVO Triggered — NOT Prevented

NVE (value_mean / eval_return) exceeded 1.5x threshold at **two points**:
1. **Step 55K**: NVE = 1.753 — eval crashed from peak 315.7 → 34.5 while value remained ~60
2. **Step 105K**: NVE = 1.591 — eval bottomed at 27.2 while value still ~43

After 105K, NVE gradually declined and stabilized at 0.12–0.17 from 165K onward. This indicates **partial recovery** from CIVO, but eval never returned to peak levels.

### Partial Recovery Pattern
- Peak eval: 315.7 (45K) — before CIVO onset
- Post-CIVO trough: 27.2 (105K)
- Late recovery plateau: ~100–155 (165K–215K)
- Final eval: 97.5 (215K) — **85% below Cheetah baseline (~650–700)**

## Dual Critic (v1 vs v2) Analysis

**The two critics never meaningfully diverged.** At every checkpoint where both are logged:

| Step | value1_mean | value2_mean | Δ (v1−v2) |
|------|-------------|-------------|-----------|
| 5K   | 0.000756    | 0.000729    | +0.000027 |
| 15K  | 1.849       | 1.846       | +0.003    |
| 205K | 14.791      | 14.790      | +0.001    |
| 215K | 14.180      | 14.176      | +0.004    |

The min(v1, v2) operator had essentially no effect because v1 ≈ v2 throughout. The critics converged to nearly identical estimates, providing no pessimism. This explains why dual-critic failed to prevent CIVO in Cheetah.

### value_loss comparison
At 215K: value_loss = 1.179, value2_loss = 1.196 — nearly identical loss landscapes.

## Comparison with Walker Dual-Critic (exp_032)

| Metric | Walker (exp_032) | Cheetah (exp_034) |
|--------|------------------|-------------------|
| Final eval | 787.7 | 97.5 |
| Peak eval | ~800+ | 315.7 |
| NVE max | ≤ 1.1 | 1.753 |
| CIVO prevented? | ✅ Yes | ❌ No |
| v1 vs v2 divergence | (not checked) | None |
| vs baseline | Near baseline | 85% below baseline |

## Interpretation

1. **Dual-critic is environment-dependent, not a universal CIVO fix.** Walker's CIVO was prevented; Cheetah's was not.

2. **Why dual-critic failed in Cheetah**: The two critics trained on identical imagined trajectories converged to the same (overestimated) values. Without diversity in critic training (e.g., different bootstrap targets, different trajectory samples), min(v1, v2) collapses to a single critic.

3. **Cheetah CIVO mechanism differs from Walker**: In Walker, value overestimation may stem from critic disagreement that dual-critic can address. In Cheetah, the overestimation likely originates from **world model error** (compounding prediction errors over the imagination horizon), which dual-critic cannot fix since both critics share the same world model.

4. **The 45K→55K crash is characteristic**: eval jumped to 315.7 then immediately crashed to 34.5 with NVE spiking to 1.75 — classic CIVO pattern where the agent exploits an overestimated region and loses the policy.

## Conclusion

**NEGATIVE.** Dual-critic (min of two independent critics) fails to prevent CIVO in Cheetah Run. The two critics do not diverge, rendering the min operator ineffective. The value overestimation in Cheetah appears to originate from world model compounding errors rather than critic-specific overestimation, a mechanism that dual-critic cannot address.

### Suggested Registry Conclusion
- conclusion: **negative**
- Key metrics: final_eval=97.5, peak_eval=315.7, max_NVE=1.753, CIVO_prevented=false
