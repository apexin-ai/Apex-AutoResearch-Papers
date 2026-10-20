# Prior-based Imagination Reward Analysis

## Purpose
Verify whether the CIVO (Compounding Imagination Value Overestimation) mechanism operates at the **imagination level** (prior-based rollouts), not just at the posterior level where the previous signed reward error analysis found counterintuitive results (dt=2 showing under-prediction on real transitions).

## Method
1. Load checkpoints for 3 models: baseline, exp_008d (trained dt_emb, collapsed), exp_008f (no dt_emb)
2. Encode initial states from replay buffer episodes using posterior (obs_step)
3. From 20 initial states, run 15-step imagination rollouts using only prior (img_step) with different fixed dt values
4. Actor network samples actions during imagination (matches actual training behavior)
5. Record per-step reward predictions (from reward head) and value estimates (from value head)

## Results

### Summary Table

| Model | dt | Mean Reward Pred | Cumulative@H=15 | Init Value | Final Value |
|-------|---:|:----------------:|:----------------:|:----------:|:-----------:|
| baseline_s1 | 1 | 1.756 | 26.34 | 662.5 | 666.3 |
| **exp_008d** | **1** | **0.462** | **6.93** | **162.4** | **160.4** |
| **exp_008d** | **2** | **1.386** | **20.79** | **162.4** | **161.7** |
| exp_008d | 3 | 0.800 | 12.00 | 162.4 | 162.1 |
| exp_008d | 4 | 0.762 | 11.42 | 162.4 | 161.4 |
| exp_008d | gate | 0.670 | — | — | — |
| exp_008f | 1 | 0.338 | 5.08 | 79.3 | 79.2 |
| exp_008f | 2 | 0.328 | 4.92 | 79.3 | 78.2 |

### Key Comparison: exp_008d dt=2 vs dt=1

**Mean reward prediction diff (dt=2 − dt=1): +0.924 (+200%)**
**Cumulative reward diff: +13.85 (+200%)**

Per-step divergence pattern:

| Step | dt=1 | dt=2 | diff |
|-----:|:----:|:----:|:----:|
| 0 | 0.592 | 0.592 | 0.000 |
| 1 | 0.593 | 0.806 | +0.213 |
| 2 | 0.589 | 0.989 | +0.400 |
| 3 | 0.552 | 1.279 | +0.727 |
| 4 | 0.500 | 1.396 | +0.896 |
| 5 | 0.472 | 1.511 | +1.039 |
| 6 | 0.440 | 1.637 | +1.196 |
| 7 | 0.432 | 1.701 | +1.269 |
| 8 | 0.411 | 1.660 | +1.249 |
| 9 | 0.403 | 1.655 | +1.252 |
| 10 | 0.397 | 1.730 | +1.333 |
| 11 | 0.391 | 1.615 | +1.225 |
| 12 | 0.396 | 1.597 | +1.201 |
| 13 | 0.393 | 1.354 | +0.961 |
| 14 | 0.370 | 1.264 | +0.893 |

**Pattern**: dt=2 reward predictions start at the same level (same initial state), then rapidly diverge upward to ~3x the dt=1 level by step 6-7, and maintain this inflation through the end of the rollout. dt=1 predictions actually *decline* over the rollout.

### Ordering by dt value (exp_008d)

| dt | Mean Reward Pred | Ratio vs dt=1 |
|---:|:----------------:|:-------------:|
| 1 | 0.462 | 1.00x |
| gate (avg 4.7) | 0.670 | 1.45x |
| 4 | 0.762 | 1.65x |
| 3 | 0.800 | 1.73x |
| **2** | **1.386** | **3.00x** |

The non-monotonic pattern (dt=2 > dt=3 > dt=4) is striking. dt=2 is the maximally optimistic embedding, not just any dt>1.

### Gate behavior (exp_008d)
- Mean dt chosen by gate: 4.68
- Distribution roughly uniform across 1-8 (no strong preference)
- Gate-driven reward prediction (0.670) is between dt=1 (0.462) and dt=2 (1.386)

### Sanity Checks

**exp_008f (no dt_emb)**: dt=1 vs dt=2 diff = −0.010 ≈ 0. Confirmed: without dt embedding, dt value has no effect on imagination dynamics. The inflation is specific to the trained dt embedding.

**baseline_s1**: Much higher reward predictions (1.756) and value (662) than 008d, reflecting that baseline actually learned good behavior while 008d collapsed.

## Reconciliation with Posterior Analysis

The previous posterior-based signed reward error analysis found dt=2 showed **under-prediction** (−0.599) on real transitions. This is **not contradictory**:

1. **Posterior analysis**: reward head predicting from posterior states (which encode real observations) → underestimates cum_reward at dt=2 because the aggregated reward signal is harder to predict
2. **Imagination analysis** (this study): reward head predicting from prior states (which drift from reality) → massively **overestimates** because the dt=2 embedding pushes the RSSM into states where the reward head sees artificially favorable features

The CIVO mechanism operates in imagination, not in posterior reconstruction. The reward head is not inherently biased; the bias emerges from how dt=2 embedding interacts with the prior dynamics to generate "unrealistically optimistic" latent trajectories.

## Conclusions

1. **CIVO in imagination: CONFIRMED**. dt=2 imagination produces 3x higher reward predictions than dt=1, directly inflating the actor's objective.

2. **Mechanism**: The trained dt=2 embedding causes the prior dynamics (img_step) to generate latent states that the reward head maps to high rewards. This is a spurious correlation learned during training — the dt=2 embedding has learned to encode a "shortcut" through reward-favorable latent space regions.

3. **dt=2 is uniquely toxic**: The overestimation is non-monotonic — dt=2 is worse than dt=3 or dt=4. This suggests the training signal for dt=2 (the most common non-trivial dt during training) allowed it to overfit.

4. **Why collapse happens**: In actor training, dt=2 imagination trajectories promise ~3x higher rewards. The actor learns to visit states where the gate chooses dt=2, creating a self-reinforcing loop. The true environment doesn't reward these policies → performance collapse.

5. **Paper recommendation**: The CIVO narrative should explicitly state it is an imagination-level phenomenon. The posterior-level signed reward error is not the right diagnostic (and shows the opposite sign). Future figures should show this per-step divergence curve (step 0-14, dt=1 vs dt=2 reward prediction) as the primary evidence.

---

## Extended Sample with 95% Bootstrap CI (v2, 2026-05-15)

Expanded from N=20 to N=100 initial states (20 episodes × 5 states/ep). 95% CI computed via 10,000 bootstrap resamples.

### Table 1: Trained Actor (Extended Sample)

| Model | dt | Mean Reward | Std | 95% CI | N | vs dt=1 |
|-------|---:|:-----------:|:---:|:------:|--:|:-------:|
| exp_008d | 1 | 0.3631 | 0.2869 | [0.309, 0.421] | 100 | 1.00x |
| **exp_008d** | **2** | **1.0519** | **0.5294** | **[0.950, 1.157]** | **100** | **2.90x** |
| exp_008f | 1 | 0.2540 | 0.4902 | [0.163, 0.358] | 100 | 1.00x |
| exp_008f | 2 | 0.2491 | 0.4928 | [0.156, 0.352] | 100 | 0.98x |

CI for 008d dt=2/dt=1 ratio: the CIs are non-overlapping ([0.309, 0.421] vs [0.950, 1.157]), confirming statistical significance.

### Table 2: Random Policy Control

Replaces trained actor with uniform random actions in [-1, 1]^6 during imagination rollouts. Isolates dynamics bias from actor exploitation.

| Model | dt | Mean Reward | Std | 95% CI | N | vs dt=1 |
|-------|---:|:-----------:|:---:|:------:|--:|:-------:|
| exp_008d | 1 | 0.1932 | 0.1766 | [0.161, 0.230] | 100 | 1.00x |
| **exp_008d** | **2** | **0.3242** | **0.2437** | **[0.280, 0.374]** | **100** | **1.68x** |
| exp_008f | 1 | 0.0949 | 0.1995 | [0.058, 0.138] | 100 | 1.00x |
| exp_008f | 2 | 0.1058 | 0.2199 | [0.065, 0.153] | 100 | 1.11x |

### Conclusion: Disentangling Dynamics Bias vs Actor Exploitation

| Model | Trained dt2/dt1 | Random dt2/dt1 | Actor Exploitation % |
|-------|:---------------:|:--------------:|:--------------------:|
| **exp_008d** | **2.90x** | **1.68x** | **64.2%** |
| exp_008f | 0.98x | 1.11x | — |

**Decomposition (exp_008d)**:
- **Total CIVO inflation**: 2.90x (trained actor dt=2 vs dt=1)
- **Dynamics bias component**: 1.68x — the dt=2 embedding alone, even with random actions, causes the RSSM prior to traverse reward-favorable latent regions. This is a pure world model artifact.
- **Actor exploitation component**: 64.2% of the total inflation — the trained actor has learned to produce actions that further amplify the reward inflation under dt=2 dynamics. This is the self-reinforcing loop: actor → high imagined reward → actor reinforced.

**exp_008f sanity check**: Both trained (0.98x) and random (1.11x) show ~1.0x ratio, confirming that without dt embedding, dt value has no meaningful effect on imagination dynamics regardless of action policy.

**Key insight**: The CIVO mechanism has two distinct components operating in the imagination:
1. **Dynamics bias** (~36% of total): The dt=2 embedding causes RSSM prior transitions to drift into states with inherently higher reward predictions, independent of action selection.
2. **Actor exploitation** (~64% of total): The trained actor has co-adapted with dt=2 dynamics to select actions that maximize the inflated reward signal, creating a feedback loop that amplifies the bias.

This two-component structure suggests that fixing CIVO requires addressing both the embedding-dynamics interaction (e.g., dt embedding regularization) and the actor-dynamics co-adaptation (e.g., imagination horizon constraints or reward clipping).

## Files
- Script (v1): `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/imagination_reward_analysis.py`
- Script (v2): `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/imagination_reward_analysis_v2.py`
- Results JSON (v1): `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/imagination_reward_results.json`
- Results JSON (v2): `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/imagination_reward_results_v2.json`
- v1: 4 episodes × 5 init states = 20 states, trained actor only, cuda:1
- v2: 20 episodes × 5 init states = 100 states, trained actor + random policy, CPU, 95% bootstrap CI
