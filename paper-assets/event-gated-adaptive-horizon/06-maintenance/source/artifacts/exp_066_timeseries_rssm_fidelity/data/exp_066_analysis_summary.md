# exp_066: Timeseries RSSM Fidelity Analysis — Full Results

## Setup
- Task: Walker Walk (DMC), fixed dt=2, trained dt_embedding, 65K steps
- 12 dense checkpoints every 5K steps (10K–65K)
- Metrics: single-step state MAE (SS), open-loop multi-step MAE (OL), state divergence, VE ratio

## Per-Checkpoint Data

| Step | SS_ratio | OL_ratio | VE_ratio | SS_gap | OL_gap | Return |
|------|----------|----------|----------|--------|--------|--------|
| 10K  | 1.047    | 0.937    | 0.005    | 0.004  | -0.007 | 43.0   |
| 15K  | 1.077    | 1.027    | 0.022    | 0.006  | 0.003  | 187.8  |
| 20K  | 1.104    | 1.092    | 0.156    | 0.008  | 0.010  | 148.7  |
| 25K  | 1.041    | 1.218    | 0.163    | 0.003  | 0.024  | 142.1  |
| 30K  | 1.247    | 1.446    | 0.215    | 0.017  | 0.047  | 148.3  |
| 35K  | 1.243    | 1.509    | 0.229    | 0.015  | 0.055  | 275.4  |
| 40K  | 1.350    | 1.378    | 1.591    | 0.021  | 0.039  | 202.3  |
| 45K  | 1.398    | 1.382    | 0.360    | 0.023  | 0.039  | 107.5  |
| 50K  | 1.466    | 1.556    | 0.616    | 0.025  | 0.058  | 178.4  |
| 55K  | 1.373    | 1.515    | 0.621    | 0.021  | 0.053  | 60.8   |
| 60K  | 1.610    | 1.348    | 1.399    | 0.031  | 0.037  | 125.3  |
| 65K  | 1.678    | 1.384    | 1.399    | 0.034  | 0.040  | 94.4   |

## Temporal Alignment

### Onset Detection
- **SS fidelity ratio > 1.1**: step 20K
- **OL fidelity ratio > 1.1**: step 25K
- **VE ratio > 0.2**: step 30K
- → Fidelity gap onset **leads** VE onset by ~10K steps

### Correlation
- Pearson(SS_ratio, VE_ratio) = **0.807** (p=0.0015) — highly significant
- Pearson(OL_ratio, VE_ratio) = 0.425 (p=0.169) — not significant (noisier)
- Cross-corr peak: SS at lag 0, OL at lag +2

### Monotonicity
- SS_ratio: 73% positive increments (8/11)
- OL_ratio: 73% positive increments (8/11)
- VE_ratio: 82% positive increments (9/11)

## Key Observations
1. **SS fidelity gap grows steadily**: ratio from 1.05 (10K) → 1.68 (65K), a 1.52x increase
2. **dt=1 MAE improves continuously** (0.090→0.050) while **dt=2 MAE plateaus** (0.094→0.084) — the gap comes from dt=1 improving but dt=2 being unable to keep pace
3. **VE ratio is near zero in early training** when fidelity gap is already present — consistent with fidelity gap being the upstream cause
4. **40K spike in VE_ratio (1.59)** coincides with SS_ratio crossing 1.35, suggesting a threshold effect

## Conclusion: **SUCCESS**
RSSM fidelity gap onset (step 20K) precedes VE onset (step 30K) by ~10K steps. The temporal ordering supports the causal chain: **RSSM fidelity degradation → value overestimation**. The trained dt_embedding creates a progressively worsening model fidelity gap at dt=2 that accumulates through imagination rollouts, leading to systematically biased value estimates.
