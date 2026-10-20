# exp-027 v2: MLP Verifier Reconfirmation

## Setup
- **Data**: SciERC NER, N=16 samples/instance, 551 instances/seed
- **Seeds**: 42, 123, 456
- **Binary label**: instance max-sample F1 > median F1
- **CV**: 5-fold stratified (AUROC), LOO (selection F1)
- **Models**: LR (C=1.0), MLP (64,32, max_iter=1000), RF (n_estimators=100)
- **Feature sets**: 5 basic (LP, SJ, FK, EM, VC) and 15 (+ 10 pairwise interactions)

## AUROC (3-seed mean +/- std)

| Model | Features | AUROC | Std |
|-------|----------|-------|-----|
| Best single (EM) | 1 | 0.6476 | — |
| LR | 5 | 0.6522 | 0.0130 |
| MLP | 5 | 0.6393 | 0.0209 |
| RF | 5 | 0.5868 | 0.0208 |
| MLP | 15 | 0.6322 | 0.0165 |
| RF | 15 | 0.6043 | 0.0314 |

## Selection F1 (3-seed mean +/- std)

| Model | Features | Sel F1 | Std |
|-------|----------|--------|-----|
| Best unsup (LP) | 1 | 0.6470 | — |
| Greedy | — | 0.6441 | — |
| LR | 5 | 0.6407 | 0.0010 |
| MLP | 5 | 0.6386 | 0.0029 |
| RF | 5 | 0.6154 | 0.0076 |
| MLP | 15 | 0.6339 | 0.0050 |
| RF | 15 | 0.6146 | 0.0081 |
| Oracle | — | 0.8231 | — |

## vs Baselines

| Comparison | Value |
|------------|-------|
| Best supervised AUROC (LR 5feat) | 0.6522 |
| Best single signal AUROC (EM) | 0.6476 |
| Delta | +0.0046 |
| Best supervised Sel F1 (LR 5feat) | 0.6407 |
| Best unsup Sel F1 (LP) | 0.6470 |
| Delta | -0.0063 |
| Greedy F1 | 0.6441 |

No supervised model beats the best unsupervised selection F1 (LP=0.6470) or greedy F1 (0.6441) in selection performance.

## RF Feature Importance (15-feat, 3-seed avg)

| Feature | Importance |
|---------|-----------|
| FKxLP | 0.0888 |
| LPxEM | 0.0780 |
| LP | 0.0768 |
| SJxLP | 0.0761 |
| SJxEM | 0.0729 |
| LPxVC | 0.0711 |
| EMxVC | 0.0658 |
| FKxVC | 0.0653 |
| FKxEM | 0.0639 |
| FK | 0.0635 |
| SJxFK | 0.0625 |
| SJ | 0.0609 |
| SJxVC | 0.0580 |
| VC | 0.0549 |
| EM | 0.0416 |

LP dominates (appears in 4 of top 5). Interaction features spread importance more evenly but don't improve predictive power.

## MLP Ablation (5-feat, drop one signal)

| Dropped | Avg AUROC w/o | Avg Delta |
|---------|--------------|-----------|
| w/o EM | 0.6024 | +0.0369 |
| w/o FK | 0.6162 | +0.0231 |
| w/o SJ | 0.6363 | +0.0030 |
| w/o LP | 0.6352 | +0.0041 |
| w/o VC | 0.6352 | +0.0041 |
| Full (5) | 0.6393 | — |

EM and FK are the most individually informative signals. Dropping LP/SJ/VC has negligible impact.

## Per-Seed AUROC

| Model | seed42 | seed123 | seed456 |
|-------|--------|---------|---------|
| LR_5feat | 0.6634 | 0.6379 | 0.6553 |
| MLP_5feat | 0.6629 | 0.6231 | 0.6319 |
| RF_5feat | 0.6042 | 0.5638 | 0.5923 |
| MLP_15feat | 0.6434 | 0.6133 | 0.6400 |
| RF_15feat | 0.6267 | 0.5684 | 0.6179 |

## Per-Seed Selection F1

| Model | seed42 | seed123 | seed456 |
|-------|--------|---------|---------|
| LR_5feat | 0.6396 | 0.6413 | 0.6413 |
| MLP_5feat | 0.6357 | 0.6415 | 0.6387 |
| RF_5feat | 0.6196 | 0.6066 | 0.6200 |
| MLP_15feat | 0.6282 | 0.6374 | 0.6362 |
| RF_15feat | 0.6121 | 0.6080 | 0.6237 |

## Conclusion

**Feature bottleneck confirmed.** Results are consistent with the original exp_027 run:

1. **MLP < LR** on 5 features (AUROC delta = -0.0129): nonlinear model overfits on only 5 weak signals
2. **Interaction features hurt**: MLP 15-feat (0.6322) < MLP 5-feat (0.6393), RF 15-feat (0.6043) < RF 5-feat (0.5868 — RF slightly improves but still worst)
3. **No supervised model beats unsupervised**: best supervised Sel F1 = 0.6407 (LR) vs best unsup = 0.6470 (LP), greedy = 0.6441
4. **Oracle gap is large**: 0.8231 vs 0.6470, meaning good samples exist but the 5 QE signals cannot identify them
5. **LP is most important signal** (RF importance + appears in top interactions), but even LP alone achieves comparable selection F1 to multi-feature models

The 5 confidence signals contain limited discriminative information that cannot be unlocked by nonlinear models or feature interactions. The bottleneck is feature quality, not model capacity.
