# exp_070_008e_v3_walker_s0 Analysis Report

**Config**: 008e_v3 (trained dt_emb + subsample ON + dt=1 imag + H=15)
**Task**: Walker Walk | **Seed**: 0 | **Steps**: 105K
**Server**: bjb1-45299 (cuda:0) | **Conclusion**: **NEGATIVE (non-CIVO learning failure)**

## Key Metrics

| Metric | Value |
|--------|-------|
| eval_return @105K | 148.0 |
| peak eval_return | 232.5 @55K |
| ve_ratio @105K | 0.8 |
| NVE peak | 0.8 @95K |
| CIVO alert | 0 (never triggered) |
| gate_dt_1_frac | 1.0 (locked) |
| gate_dt_2_frac | 0.0 |
| value_mean @105K | 122.1 |
| actor_entropy @105K | -3.7 |

## Eval Return Trajectory

| Step | eval_return | ve_ratio | value_mean |
|------|-------------|----------|------------|
| 5K   | 37.4  | —   | 0.0   |
| 15K  | 93.2  | 0.0 | 2.2   |
| 25K  | 178.8 | 0.1 | 14.5  |
| 35K  | 221.6 | 0.2 | 48.5  |
| 45K  | 230.9 | 0.3 | 78.3  |
| 55K  | **232.5** | 0.4 | 94.3  |
| 65K  | 194.0 | 0.5 | 95.0  |
| 75K  | 175.2 | 0.6 | 103.2 |
| 85K  | 218.6 | 0.5 | 114.7 |
| 95K  | 139.6 | 0.8 | 115.7 |
| 105K | 148.0 | 0.8 | 122.1 |

## CIVO Judgment

**No CIVO detected.** ve_ratio remained ≤ 0.8 throughout training, well below the 1.5x threshold. civo/alert never triggered. The value function tracked actual performance without overestimation.

However, the agent **failed to learn Walker Walk** — eval_return peaked at only 232.5 (55K), far below the baseline ~500+, and declined to 148 by 105K. This is a **non-CIVO learning failure**: the agent stagnated early and never achieved competent walking behavior. The failure pattern is fundamentally different from CIVO collapse (seeds 2,3), where agents first reach 500-700+ then crash with NVE >3.7x.

## Cross-Seed Comparison (008e_v3 Configuration)

| Seed | eval_return @105K | ve_ratio @105K | NVE peak | Peak eval | Conclusion | Failure Mode |
|------|-------------------|----------------|----------|-----------|------------|-------------|
| s0 (this) | **148.0** | 0.8 | 0.8 | 232.5 @55K | negative | Non-CIVO (never learned) |
| s1 | 869.9 | 0.527 | — | 869.9 @105K | success | — |
| s2 | 136.96 | 2.481 | 3.78 | 715.2 @85K | negative | CIVO collapse @95K |
| s3 | 92.7 | 2.635 | 4.02 | 520.4 @85K | negative | CIVO collapse @85-95K |
| s4 | 899.3 | 0.609 | 0.99 | 899.3 @105K | success | — |
| s5 | — | — | — | — | RUNNING | — |

## Collapse Rate Update (5 completed seeds)

| Category | Count | Rate | Seeds |
|----------|-------|------|-------|
| Success (eval >500, NVE <1.5x) | 2 | 40% | s1, s4 |
| CIVO collapse (NVE >1.5x) | 2 | 40% | s2, s3 |
| Non-CIVO failure (eval low, NVE normal) | 1 | 20% | s0 |
| **Overall failure** | **3** | **60%** | s0, s2, s3 |

- **CIVO collapse rate**: 2/5 = 40% (was 2/4 = 50%)
- **Overall failure rate**: 3/5 = 60% (was 2/4 = 50%)
- 95% CI for CIVO collapse rate (binomial): [5.3%, 85.3%] (still very wide with n=5)
- Seed 5 (exp_072) is still running; will update to n=6 when complete

## Observations

1. **Third failure mode discovered**: Seed 0 reveals that 008e_v3 config can fail without CIVO. The agent never learned to walk (peak 232.5 vs baseline 500+), but value estimation remained healthy (ve_ratio 0.8). This is distinct from both success (s1/s4) and CIVO collapse (s2/s3).

2. **Bimodal success pattern broken**: Previously, 008e_v3 seeds were either very good (~870-900) or CIVO-collapsed (~90-140). Seed 0 adds a third category: low performance without value pathology.

3. **Gate behavior identical across all outcomes**: gate_dt_1_frac = 1.0 in all 5 seeds regardless of outcome. The gate mechanism (locked at dt=1) is not differentiating success from failure — all variability comes from other sources (exploration, world model quality, etc.).

4. **Value function note**: value_mean rose steadily (0→122) even as eval_return stagnated (232→148 in late training). The growing gap between value_mean trend and eval stagnation might indicate a very slow-developing overestimation, though ve_ratio never crossed the threshold.
