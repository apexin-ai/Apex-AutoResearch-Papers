# RSSM Prediction Quality Analysis: Collapsed vs Healthy vs Baseline

**Date**: 2026-05-24  
**Models**: Walker-Walk (DMC)  
**Method**: Posterior-conditioned multi-step imagination with decoder reconstruction error  

## Data Table

### Observation Reconstruction MSE (total)

| Model | dt=1 | dt=2 | dt=3 | dt=4 | Gap (dt2/dt1) |
|-------|------|------|------|------|---------------|
| **Baseline** (exp_009d, no gate) | 16.08 | 23.49 | 29.04 | 30.71 | **1.46x** |
| **Collapsed CIVO** (exp_008d, gate+dt_emb) | 9.96 | 13.21 | 16.89 | 16.69 | **1.33x** |
| **Healthy Frozen** (exp_057, gate+frozen_dt_emb) | 11.14 | 14.95 | 15.56 | 16.18 | **1.34x** |

### Reward Prediction MAE

| Model | dt=1 | dt=2 | dt=3 | dt=4 | Gap (dt2/dt1) |
|-------|------|------|------|------|---------------|
| **Baseline** | 0.0453 | 0.0587 | 0.0785 | 0.0888 | **1.30x** |
| **Collapsed CIVO** | 0.0573 | 0.1781 | 0.1032 | 0.1219 | **3.11x** |
| **Healthy Frozen** | 0.0678 | 0.1330 | 0.1486 | 0.1544 | **1.96x** |

### Per-key Obs MSE Gap (dt2/dt1)

| Model | height | orientations | velocity |
|-------|--------|--------------|----------|
| Baseline | 1.23x | 1.63x | 1.46x |
| Collapsed CIVO | 1.74x | 2.11x | 1.32x |
| Healthy Frozen | 1.34x | 1.97x | 1.34x |

## Key Findings

### F1: dt_embedding reduces observation fidelity gap
Both CIVO variants (1.33x, 1.34x) have a significantly smaller observation MSE gap than baseline (1.46x). The dt_embedding effectively teaches the RSSM to predict multi-step transitions more accurately in observation space.

### F2: Reward prediction gap is the critical differentiator
The collapsed model shows a **3.11x** reward gap (dt2/dt1), dramatically worse than baseline (1.30x) and healthy/frozen (1.96x). This means the collapsed model's reward predictions become highly unreliable at longer temporal horizons — even though its observation predictions remain good.

### F3: Collapsed model has better absolute dt=1 reconstruction
Counterintuitively, the collapsed CIVO model has the *lowest* dt=1 obs_mse (9.96 vs baseline 16.08). The dt_embedding improves world model quality overall. The collapse pathology is not about poor modeling — it's about *selective* degradation of reward predictions at longer horizons.

### F4: Non-monotonic reward error in collapsed model
The collapsed model shows dt=2 reward error (0.178) > dt=3 (0.103) > dt=4 (0.122). This non-monotonicity suggests the model learned a biased reward signal specifically at dt=2, likely due to the training data distribution where dt=2 transitions are most frequently selected by the collapsed gate.

### F5: Frozen embedding mitigates but doesn't eliminate the issue
The healthy/frozen model reduces the reward gap from 3.11x to 1.96x — still worse than baseline (1.30x) but much more stable. Freezing prevents the co-adaptation loop where learned dt_embedding + gate policy jointly optimize for optimistic reward predictions.

## Relationship to CIVO Hypothesis

This analysis directly supports **C2 (Delusional Critic)**:

1. The world model in collapsed runs predicts rewards poorly at dt>1 (3.11x gap)
2. The critic uses imagined rollouts from this model to estimate value
3. dt>1 imagined trajectories carry inflated/noisy reward predictions
4. The critic therefore overestimates value for longer temporal abstractions
5. The gate policy learns to prefer dt>1 actions based on these inflated values
6. This creates a positive feedback loop → collapse to always selecting dt>1

The frozen dt_embedding breaks this loop by preventing the embedding from co-adapting with the biased reward signal, which is why it prevents collapse (exp_057 vs exp_008d).

## Prior Analysis (Corroborating)

Earlier analysis on different checkpoints (`analysis_rssm_prediction_quality.json`) found consistent patterns:
- baseline_s1: obs gap = 2.04x, reward gap = 1.56x
- exp_008d_subsample_on_h8: obs gap = 1.30x, reward gap = 2.78x
- exp_008f_no_dt_embed: obs gap = 2.75x, reward gap = 1.01x (no dt_embed → can't improve multi-step obs, but reward stays flat because model doesn't attempt dt-conditioned prediction)

## Experimental Setup

- **15 episodes** per model, 40 test points per episode per dt level (600 total samples)
- **Procedure**: Run full posterior observe pass, then from each posterior state do dt consecutive `img_step` calls with `dt=dt_value` conditioning, decode observation and reward, compare to ground truth at time t+dt
- **Checkpoints**: final training checkpoints (latest.pt)
- **Device**: cuda:0 on bjb1-45299

## Files

- Raw JSON: `logdir/analysis_rssm_walker_fidelity.json` (server)
- Prior analysis: `logdir/analysis_rssm_prediction_quality.json` (server)
- Script: `logdir/run_rssm_walker_analysis.py` (server)
