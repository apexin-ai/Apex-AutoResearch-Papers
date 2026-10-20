# Table 1 Integrity Check: 008d vs 009e NVE Values

## 1. Precise NVE Comparison (6 decimal places)

| Step | 008d (seed 0) NVE | 009e ("seed 1") NVE | Identical? |
|------|-------------------|---------------------|------------|
| 25K  | 1.772749          | 1.772749            | YES        |
| 35K  | 1.705280          | 1.705280            | YES        |
| 45K  | 2.093256          | 2.093256            | YES        |
| 55K  | 4.129242          | 4.129242            | YES        |

Underlying raw values (also bit-for-bit identical):

| Step | value_mean        | eval_return         | baseline V/E |
|------|-------------------|---------------------|--------------|
| 25K  | 25.86150550842285 | 167.2213623046875   | 0.087240     |
| 35K  | 60.19843292236328 | 146.34487228393556  | 0.241219     |
| 45K  | 97.53458404541016 | 140.7616340637207   | 0.331018     |
| 55K  | 137.8776092529297 | 82.74693756103515   | 0.403526     |

## 2. Root Cause: Same Seed, Not Same Run

**009e is NOT a checkpoint-resume of 008d.** Evidence:
- Different train_eps files: 008d episodes dated 2026-05-14T10:22, 009e dated 2026-05-15T14:01
- Different episode counts: 008d has 52 episodes (55K), 009e has 112 episodes (112K)
- Different tfevents timestamps: 008d=1778725321, 009e=1778824876
- Only divergence in metrics: `fps` field (6.059 vs 6.970 at step 15K) — hardware timing only

**Root cause: 009e was launched with seed=0 (default in configs.yaml line 12), same as 008d.**
The name `exp_009e_008d_walker_s1` is a **misnomer** — "s1" suggests seed=1 but it actually ran with seed=0.

DM Control + fixed seed = fully deterministic → identical model weights, gradients, and evaluation trajectories.

## 3. Impact on Table 1 and Paper Claims

### Current state of 008d-config seeds:
| Experiment | Actual Seed | Steps | Independent? |
|-----------|-------------|-------|--------------|
| exp_008d_subsample_on_h8 | 0 | 55K | YES (original) |
| exp_009e_008d_walker_s1 | 0 | 112K | NO — duplicate of 008d |
| exp_009b_008d_walker_s2 | 2 | 105K | YES (different NVE values) |

### Impact:
- If Table 1 reports 008d and 009e as n=2 independent seeds: **effective n=1**, not n=2
- The NVE threshold analysis (nve_threshold_v3_ci_supplement.json) correctly excludes 009e — only uses 008d and 009b
- The bootstrap CI analysis (bootstrap_cis.json) uses only 008d time-points, not 009e

### Reviewer's concern is VALID:
The reviewer correctly identified that "physically distinct seeds producing identical floating-point trajectories is implausible" — because they ARE the same seed.

## 4. Recommended Corrections

### For the paper:
1. **Remove 009e from any table claiming it as "seed 1"** — it's a seed 0 duplicate
2. **Report effective n correctly**: for 008d-config, current independent seeds are {0, 2} → n=2
3. **If n=3 needed**: run a true seed=1 experiment (the queued `exp_008d_civo_trigger_s2` uses seed 2 which already exists as 009b)
4. **Disclose in supplementary**: "009e was initially mislabeled as seed 1; upon verification, it used seed 0 and produced identical trajectories to 008d. It has been excluded from multi-seed analyses."

### For the Independence Notes:
Update the note from "008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps" to:
"009e used seed=0 (same as 008d) due to naming error. Not an independent seed. Excluded from CI computation."

### Effective sample sizes for Table 1 (corrected):
| Configuration | True independent seeds | n |
|--------------|----------------------|---|
| 008d (trained dt_emb, subsample ON, H=8) | seed 0, seed 2 | 2 |
| 008f (no dt_emb, subsample ON, H=8) | seed 0, seed 1, seed 3 | 3 |
| baseline | seed 0, seed 1 | 2 |
