# Plan 031: Actor Entropy Contrast Analysis

## Summary

Actor entropy does **not** differentiate collapsed from healthy runs. Both groups follow nearly identical entropy trajectories at matched time points. CIVO collapse manifests through value/reward pathology, not actor confusion.

## Data

### Collapsed Group

| Step | exp_008d (trained dt_emb) | fixed_dt2 (dt=2) [registry: exp_006_fixed_dt2] |
|------|--------------------------|-------------------|
| 5K   | 8.158                    | 8.161             |
| 15K  | 0.481                    | 0.963             |
| 25K  | -1.862                   | -3.023            |
| 35K  | -3.465                   | -4.404            |
| 45K  | -4.575                   | -5.063            |
| 55K  | -4.879                   | -5.170            |
| 65K  | —                        | -5.122            |

### Healthy Group

| Step | exp_008f (no dt_emb) | exp_008a (unexposed) | baseline_s1 (dt=1) |
|------|---------------------|----------------------|--------------------|
| 5K   | 8.108               | 8.162                | 8.102              |
| 15K  | 0.609               | -1.150               | -0.901             |
| 25K  | -1.852              | -4.877               | -4.741             |
| 35K  | -2.737              | -5.142               | -5.001             |
| 45K  | -4.314              | -5.200               | -5.120             |
| 55K  | -4.771              | -5.214               | -5.177             |
| 65K  | -4.560              | -5.230               | -5.214             |
| 75K  | -4.523              | -5.242               | -5.223             |
| 85K  | -4.701              | -5.251               | -5.232             |
| 95K  | -4.864              | -5.256               | -5.225             |
| 105K | -4.852              | -5.237               | -5.170             |

Baseline continues to 505K, with entropy recovering from -5.2 to ~-1.5 (see below).

## Key Findings

### 1. No Entropy Divergence at Matched Time Points

At the last comparable step (55K):
- **Collapsed mean**: -5.02 (avg of -4.879, -5.170)
- **Healthy mean**: -5.05 (avg of -4.771, -5.214, -5.177)
- **Difference**: 0.03 nats — statistically negligible

The hypothesis that collapsed runs exhibit "entropy anomalous rise" (actor confusion from delusional critic gradients) is **not supported**.

### 2. Collapsed Runs Show Normal Entropy, Abnormal Returns

fixed_dt2_v1_s1 demonstrates this clearly:
- **Returns**: peak ~580 at step 40K → crash to 29 by step 72K (classic CIVO collapse)
- **Entropy**: -5.06 at 45K → -5.17 at 55K → -5.12 at 65K (stable, monotonic)

The actor maintains a committed (low-entropy) policy throughout the collapse. It does not become "confused" — it remains confident but wrong. The collapse is driven by the critic providing delusional value estimates, not by the actor losing its policy structure.

### 3. Entropy Descent Speed Varies by Configuration, Not by Collapse Fate

| Config | Entropy at 15K | Entropy at 25K | Descent Rate |
|--------|---------------|---------------|-------------|
| exp_008a (unexposed) | -1.150 | -4.877 | Very fast |
| baseline_s1 (dt=1) | -0.901 | -4.741 | Very fast |
| exp_008d (collapsed) | 0.481 | -1.862 | Medium |
| exp_008f (no dt_emb) | 0.609 | -1.852 | Medium |
| fixed_dt2 (collapsed) | 0.963 | -3.023 | Medium |

Faster entropy descent correlates with simpler temporal setups (dt=1 baseline, unexposed to dt variation), not with collapse fate.

### 4. Baseline Entropy Recovery Phase

baseline_s1 shows a distinctive long-term entropy recovery pattern:

| Phase | Steps | Entropy Range | Returns |
|-------|-------|--------------|---------|
| Initial descent | 5K–85K | 8.10 → -5.23 | 33 → ~700 |
| Bottom plateau | 85K–115K | -5.23 → -4.97 | ~700–800 |
| Recovery | 115K–295K | -4.97 → -0.99 | 800 → 950 |
| Stable high | 295K–505K | -0.86 → -1.51 | 900–990 |

The entropy recovery from -5.2 to -1.0 coincides with continued performance improvement (700→950 return), indicating this is adaptive exploration refinement during extended training — not collapse. The actor maintains ~950 return with entropy 3–4 nats higher than its minimum, suggesting a healthy exploration-exploitation balance.

### 5. exp_008f Shows Intermediate Entropy Plateau

exp_008f (no dt_emb, healthy) stabilizes at -4.5 to -4.9 from step 45K onward — higher entropy than the -5.2 level reached by exp_008a and baseline. This may reflect the configuration complexity (subsample exposure without dt embedding creates irreducible action uncertainty), but critically this experiment maintains stable returns (rising to ~460 by 105K), confirming this is healthy behavior.

## Conclusions

1. **Actor entropy is NOT a collapse indicator.** Collapsed and healthy runs are indistinguishable by entropy trajectory during the collapse window. The CIVO collapse mechanism operates through critic value distortion, not actor policy degradation.

2. **The actor remains confident during collapse.** In fixed_dt2, entropy stays at -5.1 while returns crash from 580 to 29. This is consistent with the "delusional critic" hypothesis: the actor commits to a policy based on an overconfident but incorrect value function.

3. **Entropy recovery in extended training is healthy.** Baseline's entropy rising from -5.2 to -1.5 over 100K–500K steps accompanies its best performance period, ruling out entropy rise as inherently pathological.

4. **Implication for paper**: The contrast between normal actor entropy and pathological returns during CIVO collapse strengthens the narrative that the collapse mechanism is critic-side. Future work should focus on value calibration metrics (EMA gap, value prediction error) rather than actor entropy as diagnostic signals.

## Raw Statistics

| Experiment | Group | Steps | Entropy Start | Entropy Min | Entropy End | Return End |
|------------|-------|-------|--------------|-------------|-------------|------------|
| exp_008d | collapsed | 5K–55K | 8.158 | -4.879 | -4.879 | ~165 |
| fixed_dt2 | collapsed | 5K–65K | 8.161 | -5.170 | -5.122 | ~150→29 |
| exp_008f | healthy | 5K–105K | 8.108 | -4.864 | -4.852 | ~460 |
| exp_008a | healthy | 5K–105K | 8.162 | -5.256 | -5.237 | ~300 |
| baseline_s1 | healthy | 5K–505K | 8.102 | -5.232 | -1.510 | ~950 |
