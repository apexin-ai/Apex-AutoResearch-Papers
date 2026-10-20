| Experiment | Config | Verdict | Trigger | Det. Type | Peak Eval | ve_ratio@trig |
|---|---|---|---|---|---|---|
| exp_008d_s0 | dt_embed, subsample_on, h=8, seed=0 | TP | 45K | predictive | 167 | 0.69 |
| exp_010b_cheetah | dt_embed, cheetah, seed=1 | TP | 65K | reactive | 322 | 3.18 |
| exp_008d_s3 | dt_embed, subsample_on, seed=3 | TP | 45K | predictive | 452 | 0.50 |
| exp_008f_s3 | no_dt_embed, subsample_on, seed=3 | TN | -- | -- | 594 | -- |
| exp_009c_008f_s2 | no_dt_embed, walker, seed=2 | FP | 105K | reactive | 359 | 0.75 |
| exp_009b_008d_walker_s2 | dt_embed, walker, seed=2 (self-correcting) | TN | -- | -- | 279 | -- |
| exp_009a_baseline_walker_s2 | vanilla DreamerV3 baseline, walker, seed=2 | FP | 85K | predictive | 967 | 0.73 |
| baseline_s1 | vanilla DreamerV3 baseline, walker, seed=1 | TN | -- | -- | 970 | -- |
| exp_009d_baseline_walker_s0 | vanilla DreamerV3 baseline, walker, seed=0 | TN | -- | -- | 951 | -- |
| exp_009d_baseline_walker_s1 | vanilla DreamerV3 baseline, walker, seed=1 | TN | -- | -- | 920 | -- |

**Summary**: TPR = 3/3 (1.00), FPR = 2/7 (0.286)
- TP: 3, FN: 0, TN: 5, FP: 2
- Detection types: predictive=3, reactive=2, concurrent=0
- Mean trigger step (TP): 51K
- Mean trigger step (FP): 95K
