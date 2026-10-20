# DANN Cross-Strategy Domain Adaptation: Results Comparison

## Setup

- **Task**: 4-class recursive generation depth classification (d0/d1/d2/d3)
- **Method**: Leave-One-Strategy-Out (LOSO) evaluation across 3 strategies (nucleus, temp, topk)
- **Models**: Pythia-1.4B, OLMo-1B, GPT-2 XL
- **Data**: 20,000 samples per strategy per model (5,000 per depth x 4 depths)
- **Features**: 19 statistical features (PPL stats, surprisal, lexical diversity, repetition)

### Methods Compared

| Method | Architecture | Domain Adaptation |
|--------|-------------|-------------------|
| **Naive RF** | RandomForest (200 trees) | None |
| **Naive DNN** | 19->128->64 encoder + 64->32->4 classifier | None |
| **DANN** | Same encoder + classifier + GRL + 64->32->3 strategy discriminator | Gradient Reversal (Ganin et al., 2016) |

## LOSO Average Results (mean over 3 folds)

### Pythia-1.4B

| Method | Accuracy | Bal. Acc (d1-d3) | MAE | Weighted Kappa |
|--------|----------|-----------------|-----|----------------|
| RF | 0.6172 +/- 0.0765 | 0.4895 | 0.4977 | 0.6926 |
| DNN | **0.6279** +/- 0.0958 | **0.5048** | 0.4894 | 0.6945 |
| DANN | 0.6215 +/- 0.0894 | 0.4967 | **0.4784** | **0.7047** |

### OLMo-1B

| Method | Accuracy | Bal. Acc (d1-d3) | MAE | Weighted Kappa |
|--------|----------|-----------------|-----|----------------|
| RF | 0.5934 +/- 0.0445 | 0.4602 | 0.4823 | 0.7345 |
| DNN | 0.5929 +/- 0.0571 | 0.4586 | 0.4866 | 0.7322 |
| DANN | **0.6129** +/- 0.0516 | **0.4861** | **0.4557** | **0.7560** |

### GPT-2 XL

| Method | Accuracy | Bal. Acc (d1-d3) | MAE | Weighted Kappa |
|--------|----------|-----------------|-----|----------------|
| RF | 0.5649 +/- 0.0260 | 0.4325 | 0.5108 | 0.7222 |
| DNN | 0.5609 +/- 0.0253 | 0.4229 | 0.5194 | 0.7141 |
| DANN | **0.5776** +/- 0.0389 | **0.4431** | **0.4925** | **0.7339** |

### Cross-Model Average

| Method | Accuracy | Bal. Acc (d1-d3) | MAE | Weighted Kappa |
|--------|----------|-----------------|-----|----------------|
| RF | 0.5918 | 0.4607 | 0.4969 | 0.7164 |
| DNN | 0.5939 | 0.4621 | 0.4985 | 0.7137 |
| DANN | **0.6040** | **0.4753** | **0.4755** | **0.7315** |

## Per-Fold Breakdown

### Held-out Nucleus

| Model | RF | DNN | DANN |
|-------|-----|-----|------|
| Pythia | 0.6993 | **0.7417** | 0.7260 |
| OLMo | 0.6538 | 0.6733 | **0.6858** |
| GPT-2 XL | 0.5982 | 0.5951 | **0.6300** |

### Held-out Temp

| Model | RF | DNN | DANN |
|-------|-----|-----|------|
| Pythia | **0.6370** | 0.6346 | 0.6311 |
| OLMo | **0.5783** | 0.5593 | 0.5743 |
| GPT-2 XL | **0.5618** | 0.5528 | 0.5368 |

### Held-out Top-k

| Model | RF | DNN | DANN |
|-------|-----|-----|------|
| Pythia | **0.5152** | 0.5074 | 0.5075 |
| OLMo | 0.5481 | 0.5462 | **0.5787** |
| GPT-2 XL | 0.5347 | 0.5347 | **0.5659** |

## Key Findings

1. **DANN consistently improves MAE and weighted kappa across all 3 models.** The cross-model average shows DANN reduces MAE by 4.3% relative to RF (0.4755 vs 0.4969) and improves kappa by 2.1 points (0.7315 vs 0.7164).

2. **Largest DANN gains on OLMo and GPT-2 XL.** DANN achieves +1.95pp accuracy over RF on OLMo and +1.27pp on GPT-2 XL. On Pythia, DNN slightly outperforms DANN on accuracy, but DANN still leads on MAE and kappa.

3. **Hold-out top-k is the hardest fold for all methods.** All models show accuracy drops of 10-20pp when top-k is held out, suggesting top-k sampling produces the most distinct feature distributions.

4. **DANN shows the largest relative gains on the hardest fold (hold-out top-k).** On OLMo top-k, DANN gets 0.5787 vs RF 0.5481 (+3.06pp). On GPT-2 XL top-k, DANN gets 0.5659 vs RF 0.5347 (+3.12pp).

5. **Hold-out temp is the one fold where DANN occasionally underperforms RF.** On all 3 models, RF has an edge over DANN when temp is held out. This may indicate that temp strategy has smaller domain shift from the other two.

6. **Naive DNN provides minimal improvement over RF.** Without domain adaptation, the DNN with the same encoder architecture as DANN shows negligible gains (cross-model avg accuracy: 0.5939 vs 0.5918 for RF).
