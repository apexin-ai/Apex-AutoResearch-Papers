# exp_071_008f_walker_s3 Analysis Report

## Configuration
- **Config**: 008f (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8)
- **Task**: Walker Walk
- **Seed**: 3
- **Training steps**: 105K (continued to 112K env steps)
- **Status**: Completed normally (EXIT_CODE=0)

## Eval Return Trajectory

| Step | eval_return |
|------|-------------|
| 5K   | 33.8        |
| 15K  | 94.9        |
| 25K  | 143.4       |
| 35K  | 196.5       |
| 45K  | 337.2       |
| 55K  | 456.1       |
| 65K  | **457.7** (peak) |
| 75K  | 304.6       |
| 85K  | 268.3       |
| 95K  | 187.3 (trough) |
| 105K | **311.9** (final) |

**Pattern**: Classic rise-peak-decline with partial late recovery. Peak at 55-65K (~457), significant dip at 95K (187), partial recovery to 312 at 105K.

## Key Metrics at 105K

| Metric | Value |
|--------|-------|
| eval_return | 311.9 |
| civo/ve_ratio | 0.4 |
| civo/delta_ve | -0.3 |
| civo/alert | 0.0 |
| gate_dt_mean | 2.0 (fixed) |
| gate_dt_std | 0.0 |
| gate_dt_2_frac | 1.0 |
| value_loss | 1.0 |
| actor_entropy | -4.6 |
| model_loss | 4.5 |

## VE Ratio Trajectory

| Step | ve_ratio |
|------|----------|
| 15K  | 0.0      |
| 25K  | 0.1      |
| 35K  | 0.1      |
| 45K  | 0.1      |
| 85K  | 0.5      |
| 95K  | 0.7 (peak) |
| 105K | 0.4      |

VE ratio peaked at 0.7 (step 95K) coinciding with the eval trough (187.3), then recovered to 0.4 at 105K. No CIVO alert triggered at any point.

## CIVO Judgment

**No CIVO observed.** As expected for the control configuration (no dt_emb):
- civo/alert = 0.0 throughout
- gate_dt fixed at 2.0 with zero variance (no adaptive gating)
- VE ratio elevation at 95K (0.7) reflects normal value estimation difficulty during performance dip, not CIVO

## Conclusion: **SUCCESS** (borderline)

Final eval_return = 311.9 > 300 threshold. However, this is a weak success:
- Peak performance was 457.7 but not sustained
- Significant mid-to-late decline (457 → 187)
- Final recovery only to 312 (68% of peak)

## 008f Series Cross-Seed Summary (4 seeds)

| Seed | Exp ID | Conclusion | Final eval_return | Peak eval_return |
|------|--------|------------|-------------------|------------------|
| s1   | exp_069 | **success** | 503 | ~503+ |
| s2   | (original) | **negative** | 148 | ~400+ |
| s3   | exp_071 | **success** (borderline) | 312 | 458 |
| s4   | exp_073 | **success** | TBD | TBD |

**008f stability assessment**: 3/4 seeds success, 1/4 negative. Success rate 75%, but with high variance (eval range 148–503). The configuration is **moderately stable but not robust**. s2's failure and s3's borderline result suggest the no-dt_emb configuration lacks a stabilizing mechanism in the late training phase, consistent with the hypothesis that dt_emb contributes to training stability (though not through CIVO, which is absent as expected in this control).
