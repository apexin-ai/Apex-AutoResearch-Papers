# Plan_030: RSSM Prediction Quality — dt=1 vs dt=2 Transitions

**Date**: 2026-05-25
**Experiments**: exp_078 (Cheetah s0, CIVO onset, NVE=4.1×) vs exp_088 (Cheetah s1, no CIVO, NVE≈1.0)
**Server**: westd-19154, cuda:1
**Method**: 50 batches × 16 sequences × 64 steps, replay buffer data, forward pass with dt_labels={1,2}

## Key Findings

### 1. CIVO seed (exp_078) has BETTER dt=2 prediction quality than no-CIVO seed (exp_088)

This is the **opposite** of the initial hypothesis. Across all metrics at dt=2:

| Metric | exp_078 (CIVO) | exp_088 (no CIVO) | Δ (CIVO − noCIVO) |
|--------|---------------|-------------------|-------------------|
| position | 0.0230 ± 0.0018 | 0.0324 ± 0.0016 | **−0.0095** |
| velocity | 0.7379 ± 0.0420 | 0.8500 ± 0.0337 | **−0.1121** |
| reward | 0.2992 ± 0.0681 | 0.6156 ± 0.0426 | **−0.3163** |
| KL | 6.3611 ± 0.3044 | 8.0124 ± 0.2780 | **−1.6513** |

exp_078 (CIVO) reconstructs dt=2 observations ~30% better on position, ~13% better on velocity, and ~51% better on reward prediction. KL divergence is ~21% lower.

### 2. Same pattern at dt=1 — CIVO seed is slightly better everywhere

| Metric | exp_078 (CIVO) | exp_088 (no CIVO) | Δ |
|--------|---------------|-------------------|---|
| position | 0.0062 ± 0.0006 | 0.0083 ± 0.0006 | −0.0021 |
| velocity | 0.2517 ± 0.0135 | 0.2600 ± 0.0132 | −0.0083 |
| reward | 0.2137 ± 0.0533 | 0.4780 ± 0.0350 | **−0.2643** |
| KL | 2.1533 ± 0.0741 | 2.1910 ± 0.0670 | −0.0377 |

The differences are smaller at dt=1 (except reward), suggesting the CIVO seed's world model quality advantage is especially pronounced at dt=2.

### 3. dt=2 is universally harder than dt=1

Both experiments show substantially higher losses at dt=2 vs dt=1:

| Metric | exp_078 dt=1→dt=2 ratio | exp_088 dt=1→dt=2 ratio |
|--------|------------------------|------------------------|
| position | 3.7× | 3.9× |
| velocity | 2.9× | 3.3× |
| reward | 1.4× | 1.3× |
| KL | 3.0× | 3.7× |

The no-CIVO seed (exp_088) shows a **larger degradation ratio** when going from dt=1 to dt=2, especially in KL (3.7× vs 3.0×) and position (3.9× vs 3.7×).

### 4. Reward prediction gap is the most striking difference

exp_078 (CIVO) has much lower reward loss than exp_088 at both dt values:
- dt=1: 0.214 vs 0.478 (2.2× better)
- dt=2: 0.299 vs 0.616 (2.1× better)

This large reward prediction advantage is paradoxical given that exp_078 has **worse actual returns** (CIVO behavior). The RSSM in exp_078 predicts rewards more accurately, yet the agent performs worse — consistent with the CIVO mechanism where the value function overestimates, driving policy toward exploiting model inaccuracies rather than actual environment rewards.

### 5. Entropy analysis

| Metric | exp_078 dt=1 | exp_078 dt=2 | exp_088 dt=1 | exp_088 dt=2 |
|--------|-------------|-------------|-------------|-------------|
| prior_ent | 43.70 | 45.46 | 44.28 | 45.90 |
| post_ent | 41.51 | 38.96 | 42.11 | 37.90 |
| gap | 2.19 | 6.50 | 2.17 | 8.00 |

exp_088 shows a larger prior-posterior entropy gap at dt=2 (8.0 vs 6.5), indicating its RSSM is more uncertain about dt=2 transitions. This means exp_088's prior is less informative — the model struggles more to predict 2-step transitions.

## Interpretation

The data suggests CIVO is **not caused by poor world model quality**. Instead:

1. **exp_078 (CIVO) has a more accurate world model** — lower reconstruction and reward losses at both dt values.
2. **A more accurate reward model may paradoxically contribute to CIVO**: if the reward head learns to predict rewards too well, the value function can latch onto patterns in the model's own predictions, creating a self-reinforcing overestimation loop.
3. **The no-CIVO seed (exp_088) has higher model error**, which may act as implicit regularization — the noisier reward signal prevents the value function from overfitting to model-predicted rewards.

This aligns with the CIVO theory: CIVO is a value-overestimation phenomenon driven by the interaction between reward prediction accuracy and value learning, not by poor observation reconstruction.

## Files

- `results.json` — Raw numerical results
- `analyze_rssm_quality.py` — Analysis script (also deployed to server)
