# Signed Reward Error Analysis

**Date**: 2026-05-15
**Script**: `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/signed_reward_error.py`
**Raw data**: `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/signed_reward_error_results.json`

## Objective

Test whether exp_008d (trained dt_emb + subsample) systematically **overpredicts** reward on dt=2 transitions — the hypothesized mechanism behind CIVO (Catastrophic Imagined Value Overestimation).

## Method

- Loaded 8 latest training episodes per experiment
- Built encoder + RSSM + reward_head from checkpoint weights
- For dt=1: fed full episodes through RSSM.observe, compared reward_head prediction to actual reward
- For dt=2: subsampled episodes (every 2nd step), computed cumulative discounted reward (r[t] + 0.997·r[t+1]), fed through RSSM.observe with dt_labels=2
- Signed error = predicted_reward − actual_reward (positive = overprediction)
- All computation on CPU, no GPU interference

## Results

| Experiment | dt | Mean SE | Std SE | Median SE | %Over | N | Mean Actual | Mean Pred |
|---|---|---|---|---|---|---|---|---|
| **baseline_s1** | 1 | **+0.001** | 0.023 | −0.001 | 39.6% | 4000 | 1.893 | 1.894 |
| **exp_008d** | 1 | **+0.018** | 0.072 | +0.009 | 61.8% | 4000 | 0.361 | 0.379 |
| **exp_008d** | 2 | **−0.599** | 0.722 | −0.331 | 8.0% | 1992 | 0.721 | 0.121 |
| **exp_008f** | 1 | **−0.710** | 0.704 | −0.490 | 14.0% | 4000 | 0.921 | 0.211 |
| **exp_008f** | 2 | **−1.645** | 1.485 | −1.445 | 5.0% | 1992 | 1.840 | 0.195 |

## Key Findings

### 1. 008d does NOT overpredict on dt=2 — it UNDERPREDICTS

The hypothesis was that 008d would show positive mean signed error on dt=2 transitions. Instead:
- dt=1: Mean SE = +0.018 (slight overprediction, 61.8% of samples)
- dt=2: Mean SE = **−0.599** (massive underprediction, only 8% overpredict)

The reward head predicts 0.121 on average but the actual cumulative reward is 0.721. The model systematically underpredicts by ~83%.

### 2. 008f is uncalibrated at both dt values

008f (no dt_emb) shows massive underprediction everywhere:
- dt=1: predicts 0.211 vs actual 0.921 (SE = −0.710)
- dt=2: predicts 0.195 vs actual 1.840 (SE = −1.645)

This suggests the 008f model's world model is fundamentally poorly calibrated — likely because it can't distinguish dt=1 from dt=2 transitions, corrupting the posterior.

### 3. Baseline is well-calibrated

The baseline reward head is nearly perfectly calibrated (Mean SE ≈ 0, Std 0.023), confirming the analysis methodology is sound.

### 4. Performance gap context

- Baseline actual reward: 1.893 (well-trained agent)
- 008d actual reward: 0.361 (collapsed/early training)
- 008f actual reward: 0.921 (intermediate)

The low actual rewards for 008d confirm it's in a collapsed state, consistent with the CIVO hypothesis but through a different mechanism than reward overprediction.

## Interpretation

The CIVO mechanism may not operate through **observation-level** reward overprediction. This analysis used the RSSM **posterior** (conditioned on real observations). During imagination (which drives actor/critic training), the RSSM uses the **prior** (no observation correction), and the dt_embedding may cause different behavior:

1. The posterior corrects for observation mismatch — even if the prior drifts, the posterior pulls back
2. During imagination, the dt_embedding could amplify state drift, leading to overoptimistic value estimates even if per-step reward prediction is unbiased or negative-biased
3. The value overshoot could come from the **critic** (accumulated returns), not per-step reward prediction

## Recommended Follow-up

1. **Prior-based analysis**: Run RSSM in imagination mode (img_step, no observations) with dt=1 vs dt=2, compare prior reward predictions — this would directly test the imagination-level mechanism
2. **Value prediction comparison**: Compare critic value estimates between dt=1 and dt=2 imagined trajectories
3. **Reward head input analysis**: Check if the dt_embedding causes the RSSM to produce features in regions where the reward head is poorly calibrated

## Visualization Data

For future plotting (reward error distributions):

```python
# Available in signed_reward_error_results.json
# Suggested plots:
# 1. Box plot: signed error by experiment × dt
# 2. Histogram: signed error distribution overlay (008d dt=1 vs dt=2)
# 3. Scatter: predicted vs actual reward, colored by experiment
```
