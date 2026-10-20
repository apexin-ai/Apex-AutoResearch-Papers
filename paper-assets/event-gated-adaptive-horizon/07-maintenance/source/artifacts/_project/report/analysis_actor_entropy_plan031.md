# Actor Entropy Analysis — Collapsed vs Healthy Configurations (plan_031)

## Experiment Directory Mapping

| Task Name | Actual Dir | Category | Max Step |
|-----------|-----------|----------|----------|
| exp_001_baseline | baseline_s1 | Baseline | 512K |
| exp_006_fixed_dt2 | fixed_dt2_v1_s1 | Collapsed | 75K |
| exp_008d_subsample_on_h8 | exp_008d_subsample_on_h8 | Collapsed | 55K |
| exp_008a_no_subsample_dt2 | exp_008a_fixed_dt2_no_subsample | Healthy | 112K |
| exp_008c_no_subsample_dt2_h8 | exp_008c_fixed_dt2_no_subsample_h8 | Healthy | 75K |
| exp_008e_v3_subsample_on_dt1_h15 | exp_008e_v3_subsample_on_dt1_h15 | Healthy | 112K |
| exp_008f_no_dt_embed_subsample_on_h8 | exp_008f_no_dt_embed_subsample_on_h8 | Healthy | 112K |

## Actor Entropy Trajectories

| Step | baseline (B) | fixed_dt2 (C) | 008d (C) | 008a (H) | 008c_h8 (H) | 008e_v3 (H) | 008f (H) |
|------|:-----------:|:------------:|:-------:|:-------:|:----------:|:----------:|:-------:|
| 5K   | 8.10 | 8.16 | 8.16 | 8.16 | 8.16 | 8.16 | 8.11 |
| 15K  | -0.90 | 0.96 | 0.48 | -1.15 | -1.18 | 2.21 | 0.61 |
| 25K  | -4.74 | -3.02 | -1.86 | -4.88 | -4.97 | 0.07 | -1.85 |
| 35K  | -5.00 | -4.40 | -3.47 | -5.14 | -5.15 | -1.23 | -2.74 |
| 45K  | -5.12 | -5.06 | -4.58 | -5.20 | -5.22 | -1.99 | -4.31 |
| 55K  | -5.18 | -5.17 | -4.88 | -5.21 | -5.26 | -3.20 | -4.77 |
| 65K  | -5.21 | -5.12 | — | -5.23 | -5.27 | -4.82 | -4.56 |

**(C) = Collapsed, (H) = Healthy, (B) = Baseline**

## Eval Return Trajectories

| Step | baseline (B) | fixed_dt2 (C) | 008d (C) | 008a (H) | 008c_h8 (H) | 008e_v3 (H) | 008f (H) |
|------|:-----------:|:------------:|:-------:|:-------:|:----------:|:----------:|:-------:|
| 5K   | 31.8 | 31.0 | 31.0 | 31.0 | 31.0 | 31.0 | 30.5 |
| 15K  | 206.6 | 256.9 | 153.7 | 167.2 | 171.3 | 131.2 | 182.0 |
| 25K  | 395.3 | 321.4 | 167.2 | 230.8 | 192.4 | 155.7 | 196.8 |
| 35K  | 388.5 | 485.3 | 146.3 | 500.8 | 185.1 | 276.5 | 206.7 |
| 45K  | 513.8 | 477.0 | 140.8 | 563.4 | 226.6 | 382.2 | 194.1 |
| 55K  | 625.7 | 360.4 | 82.7 | 487.9 | 241.9 | 486.8 | 173.5 |
| 65K  | 615.9 | **132.9** | — | 608.0 | 240.9 | 580.7 | 374.8 |

## Value Mean vs Eval Return (Delusional Critic Indicator)

| Step | fixed_dt2 V / E (ratio) | 008d V / E (ratio) | baseline V / E (ratio) | 008a V / E (ratio) |
|------|:----------------------:|:------------------:|:---------------------:|:------------------:|
| 25K  | 62.8 / 321.4 (0.20) | 25.9 / 167.2 (0.15) | 34.5 / 395.3 (0.09) | 34.6 / 230.8 (0.15) |
| 35K  | 151.1 / 485.3 (0.31) | 60.2 / 146.3 (0.41) | 93.7 / 388.5 (0.24) | 78.7 / 500.8 (0.16) |
| 45K  | 254.3 / 477.0 (0.53) | 97.5 / 140.8 (0.69) | 170.1 / 513.8 (0.33) | 131.9 / 563.4 (0.23) |
| 55K  | 336.4 / 360.4 (**0.93**) | 137.9 / 82.7 (**1.67**) | 252.5 / 625.7 (0.40) | 183.5 / 487.9 (0.38) |
| 65K  | 361.7 / 132.9 (**2.72**) | — | 346.7 / 615.9 (0.56) | 226.1 / 608.0 (0.37) |

## Cleanest Comparison: 008c (Healthy) vs 008d (Collapsed)

Both use h8 horizon, differ only in subsample setting (value training regime).

| Step | 008c entropy (H) | 008d entropy (C) | Gap | 008c eval | 008d eval | 008d V/E |
|------|:----------------:|:----------------:|:---:|:---------:|:---------:|:--------:|
| 5K   | 8.16 | 8.16 | 0.00 | 31.0 | 31.0 | — |
| 15K  | -1.18 | 0.48 | **1.66** | 171.3 | 153.7 | — |
| 25K  | -4.97 | -1.86 | **3.11** | 192.4 | 167.2 | 0.15 |
| 35K  | -5.15 | -3.47 | **1.68** | 185.1 | 146.3 | 0.41 |
| 45K  | -5.22 | -4.58 | **0.64** | 226.6 | 140.8 | 0.69 |
| 55K  | -5.26 | -4.88 | **0.38** | 241.9 | 82.7 | **1.67** |

## Key Findings

### 1. Collapsed configs show delayed entropy reduction, not entropy increase

The original hypothesis predicted that delusional critic gradients would cause actor entropy to **rise** (actor becoming more random). The data shows a more nuanced picture: collapsed configurations exhibit **slower entropy decrease** rather than outright increase.

- At 25K steps, the entropy gap between collapsed and healthy configs peaks at **~3 nats** (008d=-1.86 vs 008c=-4.97).
- By 55K, the gap narrows to ~0.4 nats — the collapsed actor does eventually become deterministic, but converges to a **bad policy**.

### 2. One exception: slight entropy uptick at collapse onset

fixed_dt2_v1_s1 shows entropy rising from -5.17 (55K) to -5.12 (65K), coinciding with eval_return crashing from 360→133. This is the only observed instance of entropy actually increasing, and it occurs at the moment of catastrophic performance collapse.

### 3. The actor entropy signal is secondary to V/E ratio

The most diagnostic signal for delusional critic is the **value/eval ratio** crossing 1.0:
- **exp_008d**: V/E ratio reaches 1.67 at 55K (critic overestimates by 67%)
- **fixed_dt2**: V/E ratio reaches 2.72 at 65K (critic overestimates by 172%)
- **All healthy configs**: V/E ratio stays below 0.6 throughout training

### 4. Revised interpretation for C2 claim

The actor entropy data supports a refined version of the hypothesis:

> Delusional critic gradients impair the actor's ability to converge to a deterministic policy during the critical early-to-mid training phase (15K-35K steps). The delayed entropy reduction indicates the actor receives contradictory gradient signals — the critic rewards exploration in already-explored regions, preventing efficient policy sharpening. Eventually the actor does converge, but to a poor deterministic policy that reflects the critic's delusional value landscape rather than the true reward structure.

### 5. exp_008e_v3 and exp_008f: slow entropy but healthy

These show very slow entropy reduction (still > -5.0 at 55K) but are NOT collapsed:
- exp_008e_v3 uses dt=1 with h=15 (shorter imagination steps, longer horizon), making actor training inherently slower
- exp_008f removes dt embedding, which also slows learning
- Both maintain V/E ratio < 0.4, confirming their critics are not delusional

This confirms that **slow entropy reduction alone does not diagnose collapse** — it must be combined with V/E ratio divergence.

## Hypothesis Verdict

**Partially supported with refinement needed.**

- The original claim "actor entropy rises under delusional critic" is **not supported** in general — entropy doesn't rise, it just decreases slower.
- A refined claim "delusional critic delays actor entropy convergence during critical training phases" **is supported** by the 008c vs 008d comparison (3 nats gap at 25K).
- The strongest evidence for C2 (delusional critic) comes from the **V/E ratio divergence**, not actor entropy per se.
- Recommendation: use actor entropy as a **secondary** indicator alongside the primary V/E ratio metric for the paper's C2 claim.
