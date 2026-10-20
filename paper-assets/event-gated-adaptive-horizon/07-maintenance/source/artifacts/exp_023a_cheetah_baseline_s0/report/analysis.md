# exp_023a_cheetah_baseline_s0 — Training Analysis

## Configuration
- Environment: Cheetah Run (DMC)
- Method: Vanilla DreamerV3 (dt=1, no temporal embedding, no gate)
- Seed: 0
- Server: bjb1-45299, cuda:0
- Total env steps: ~212K
- Total gradient updates: ~50,099

## Eval Return Time Series

| Step | eval_return |
|------|------------|
| 5K   | 12.2       |
| 15K  | 84.7       |
| 25K  | 167.7      |
| 35K  | 326.7      |
| 45K  | 285.8      |
| 55K  | 338.5      |
| 65K  | 386.0      |
| 75K  | 404.2      |
| 85K  | 330.6      |
| 95K  | 406.8      |
| 105K | 322.0      |
| 115K | 468.3      |
| 125K | 480.3      |
| 135K | 504.2      |
| 145K | 578.7      |
| 155K | 590.0      |
| 165K | 591.5      |
| 175K | 534.3      |
| 185K | 425.0      |
| 195K | 596.4      |
| 205K | 624.7      |

## Key Metrics

| Metric | Value |
|--------|-------|
| eval_return_final (205K) | 624.7 |
| eval_return_peak | 624.7 @ 205K |
| Last-5 eval mean (165K-205K) | 554.4 |
| ve_ratio range | 0.0 - 0.9 |
| ve_ratio final (205K) | 0.6 |
| CIVO alerts | 1 (transient, step 185K) |
| Training status | Completed (EXIT_CODE=0) |

## CIVO Analysis

At step 185K, CIVO detector fired:
- ve_ratio = 0.906, delta_ve = 0.212, eval_decline = 2/3
- eval_return dropped from 591.5 (165K) to 534.3 (175K) to 425.0 (185K)

Recovery:
- 195K: ve_ratio = 0.7, eval_return = 596.4
- 205K: ve_ratio = 0.6, eval_return = 624.7

This was a **transient episode**, not a sustained collapse. The agent recovered within 20K steps and reached a new peak.

## Comparison with exp_023b (seed=1)

| Metric | 023a (seed=0) | 023b (seed=1) | Delta |
|--------|--------------|--------------|-------|
| eval_return_final | 624.7 | 520.3 | +104.4 |
| eval_return_peak | 624.7 @ 205K | 572.9 @ 195K | +51.8 |
| Last-5 eval mean | 554.4 | 542.2 | +12.2 |
| ve_ratio range | 0.0-0.9 | 0.5-0.7 | wider |
| CIVO collapse | No (transient) | No | consistent |

## NVE Normalization Baseline

For Cheetah Run NVE calculation, using the two-seed average:
- Last-5 eval mean: (554.4 + 542.2) / 2 = **548.3**
- Peak average: (624.7 + 572.9) / 2 = **598.8**

## Conclusion: SUCCESS

The baseline is healthy. Despite the transient CIVO alert at 185K (ve_ratio spike to 0.9 with eval dip to 425), the agent recovered strongly and reached a new peak of 624.7. Performance is consistent with and slightly exceeds seed=1 results. No sustained value overestimation collapse occurred.

The two-seed baseline establishes Cheetah Run vanilla DreamerV3 performance at ~548 (last-5 mean) / ~599 (peak average), suitable for NVE normalization.
