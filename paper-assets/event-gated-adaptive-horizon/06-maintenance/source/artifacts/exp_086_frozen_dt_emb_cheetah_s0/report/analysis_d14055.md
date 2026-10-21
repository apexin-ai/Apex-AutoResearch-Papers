# exp_086_frozen_dt_emb_cheetah_s0 Analysis Report

## Experiment Info
- **exp_id**: exp_086_frozen_dt_emb_cheetah_s0
- **hypothesis**: Frozen dt_embedding (requires_grad=False, random init) with subsample ON + dt=2 + H=8 on Cheetah Run does not trigger CIVO — cross-environment validation that dt_emb TRAINING is CIVO necessary condition.
- **parent**: exp_078_cheetah_008d_s0
- **server**: westd-19154
- **seed**: 0
- **status**: completed (EXIT_CODE=0)
- **W&B**: not used (metrics from log only)

## eval_return Trajectory

| Step | eval_return |
|------|-------------|
| 5K   | 8.3         |
| 15K  | 222.8       |
| 25K  | 245.2       |
| 35K  | **326.4**   |
| 45K  | 153.3       |
| 55K  | 151.7       |
| 65K  | 154.6       |
| 75K  | 144.1       |
| 85K  | 188.8       |
| 95K  | 121.0       |
| 105K | 53.3        |

Peak: 326.4 at 35K. Severe performance degradation in late training (326.4 -> 53.3).

## ve_ratio Trajectory

| Step | ve_ratio |
|------|----------|
| 5K   | N/A      |
| 15K  | 0.0      |
| 25K  | 0.0      |
| 35K  | 0.0      |
| 45K  | 0.1      |
| 55K  | 0.1      |
| 65K  | 0.1      |
| 75K  | 0.1      |
| 85K  | 0.1      |
| 95K  | 0.1      |
| 105K | 0.2      |

Peak: **0.2** at 105K. civo/alert = 0.0 throughout. No CIVO triggered.

## NVE Calculation

- ve_ratio_peak(exp_086) = 0.2
- ve_ratio_peak(baseline exp_077_cheetah_baseline_s0) = 0.739
- **NVE = 0.2 / 0.739 = 0.27**
- Classification: **NVE < 1.0 → No CIVO**

## Comparison: exp_086 (frozen s0) vs exp_087 (frozen s1)

| Metric               | exp_086 (s0)  | exp_087 (s1)  |
|----------------------|---------------|---------------|
| ve_ratio_peak        | 0.2 (105K)    | 0.2 (95K)     |
| NVE                  | 0.27          | 0.33          |
| eval_return_105K     | 53.3          | 186.9         |
| eval_return_peak     | 326.4 (35K)   | —             |
| CIVO                 | No            | No            |
| baseline ve_peak     | 0.739         | 0.6           |

Both frozen seeds show no CIVO (NVE < 1.0), consistent across seeds. exp_086 shows worse final performance but the CIVO conclusion is identical.

## Comparison: exp_086 (frozen s0) vs exp_078 (trained s0)

| Metric               | exp_086 (frozen) | exp_078 (trained) |
|----------------------|-----------------|-------------------|
| NVE                  | 0.27            | 4.1               |
| CIVO                 | No              | Yes               |
| dt_emb trainable     | No              | Yes               |

This is the critical paired comparison: same environment (Cheetah), same seed (s0), same hyperparameters — only dt_emb training differs. Trained dt_emb → NVE=4.1 (CIVO). Frozen dt_emb → NVE=0.27 (no CIVO). Confirms dt_emb training is a necessary condition for CIVO.

## Gate Behavior

gate_dt_mean = 2.0, gate_dt_std = 0.0 throughout. gate_dt_2_frac = 1.0 (100% dt=2). gate_empirical_entropy = 0.0. As expected with frozen dt_emb: no temporal adaptation, gate locked at dt=2.

## Notable Observation

Performance collapses from 326.4 (35K) to 53.3 (105K) without CIVO. This is a standard policy degradation (possibly due to overfitting or exploration collapse with actor_entropy dropping to -1.1), NOT value expansion. The ve_ratio remains low (0.2) even as eval_return crashes, confirming these are independent failure modes.

## Conclusion

**SUCCESS** — Hypothesis confirmed.

Frozen dt_emb on Cheetah s0 produces NVE=0.27, well below the 1.0 threshold. No CIVO alert triggered. Combined with exp_087 (frozen s1, NVE=0.33) and contrasted with exp_078 (trained s0, NVE=4.1), this provides strong cross-environment, cross-seed evidence that **dt_emb training is a necessary condition for CIVO**.

## Paths

- **checkpoint_path**: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_086_frozen_dt_emb_cheetah_s0/latest.pt`
- **log_path**: `/root/runs/event-gated-adaptive-horizon/exp_086_frozen_dt_emb_cheetah_s0.log`
