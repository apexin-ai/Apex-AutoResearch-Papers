# Accuracy Z-Score vs. lz* Comparison Report

## Method
- **Accuracy z-score**: For each benchmark, compute per-model accuracy from raw binary responses,
  then z_i = (acc_i - mean) / std across 12 models. Flag if |z| > 1.96.
- **lz* (person-fit)**: Standardized log-likelihood ratio from IRT model, flagged via BH-corrected
  empirical p-values (alpha=0.05).

## Results

| Metric | Value |
|--------|-------|
| Z-score flagged | 4/60 |
| lz* flagged | 57/60 |
| Agreement rate | 0.117 |
| TP (both flag) | 4 |
| FP (z-only flag) | 0 |
| FN (lz*-only flag) | 53 |
| TN (neither flag) | 3 |

## Gemini-1.5 MMLU Case Study

| Metric | Value |
|--------|-------|
| Accuracy | 1.000000 |
| Z-score | 1.413 |
| lz* | 31.815 |
| Z-flagged | False |
| lz*-flagged | True |

Gemini-1.5 achieves near-perfect MMLU accuracy. The z-score captures that this is an
outlier in terms of overall performance, but it cannot distinguish *how* the model achieved
that score. The lz* statistic (31.8) is far more extreme because it
detects that the *pattern* of correct/incorrect responses is aberrant given the model's
estimated ability — the model gets too many hard items right and too few easy items wrong,
a signature consistent with memorization rather than genuine ability.

## What Accuracy Z-Score Captures vs. Misses

**Captures**: Models with unusually high or low overall accuracy on a benchmark relative to
the cohort. Useful as a coarse screening tool.

**Misses**: Item-level response pattern aberrance. Two models with identical accuracy can have
very different lz* values if one shows a natural difficulty gradient while the other shows
flat performance across difficulty levels. With only 12 models, the z-score also suffers
from low statistical power — the threshold |z|>1.96 assumes normality in a sample of 12.

**lz* advantage**: Leverages full item-level response patterns and IRT difficulty parameters.
It detects contamination signatures (memorized hard items, careless easy items) that
aggregate accuracy cannot capture. This is especially important when contamination is
partial — a model might memorize only the hardest items, leaving overall accuracy within
a normal range while producing a highly aberrant response pattern.
