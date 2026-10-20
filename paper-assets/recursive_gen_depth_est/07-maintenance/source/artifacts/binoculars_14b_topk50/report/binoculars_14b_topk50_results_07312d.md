# Binoculars Baseline + Merged Ablation: Qwen2.5-14B topk50

**Cell**: qwen25_14b_topk50 (1-cell)
**Data**: 20,000 samples (5,000 per depth d0-d3)
**Observer**: EleutherAI/pythia-1.4b | **Performer**: EleutherAI/pythia-410m
**RF**: 200 estimators, 5-fold stratified CV

## 1. Binoculars Baseline

| Method | 4-class Acc | d1-d3 Bal Acc |
|--------|------------|---------------|
| RF_multi (11-feat) | 37.68 +/- 0.71 | 33.86 +/- 0.75 |
| threshold | 28.43 +/- 0.68 | 24.95 +/- 0.80 |
| equal_width | 26.13 +/- 0.48 | 30.65 +/- 1.52 |
| RF_single | 25.23 +/- 0.48 | 25.21 +/- 0.95 |
| coral | 24.47 +/- 0.35 | 32.63 +/- 0.46 |

11 Binoculars features: bino_score, ppl_mean, ppl_var, ppl_median, ppl_p10, ppl_p90, ppl_skew, xppl_mean, xppl_var, xppl_median, bino_score_median

## 2. Merged Feature Ablation

| Feature Set | # Feats | 4-class Acc | d1-d3 Bal Acc |
|-------------|---------|------------|---------------|
| merged | 30 | **51.49 +/- 0.53** | **46.37 +/- 0.42** |
| stat_only | 19 | 48.84 +/- 0.82 | 43.45 +/- 0.91 |
| bino_only | 11 | 37.74 +/- 0.90 | 34.02 +/- 0.97 |
| bino_single | 1 | 25.23 +/- 0.48 | 25.21 +/- 0.95 |

## 3. Baseline Alignment (方案 A)

| Metric | Value |
|--------|-------|
| Main pipeline stat_only baseline | 47.93% |
| Merged (30-feat) | 51.49% |
| **Delta** | **+3.56 pp** |

Note: stat_only in ablation = 48.84% (slightly above main pipeline 47.93% due to independent refit). Delta computed against main pipeline value per 方案A.

## 4. Key Takeaways

- Binoculars features alone (37.74%) are substantially weaker than stat features (48.84%) on topk50 data, consistent with top-k decoding producing less discriminable perplexity distributions.
- Merging 11 Binoculars features into the 19 stat features yields +2.65 pp over stat_only (48.84 -> 51.49) within this ablation.
- Against the main pipeline baseline (方案A, 47.93%), merged features provide **+3.56 pp** gain.
- topk50 remains the hardest decoding strategy; merged 51.49% is lower than temp09 merged results, as expected.
- Computation time: ~407s for Binoculars feature extraction on 20k samples.