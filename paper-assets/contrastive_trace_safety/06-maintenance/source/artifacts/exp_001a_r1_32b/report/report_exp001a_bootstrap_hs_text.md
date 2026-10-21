# Exp-001a R1-32B: HS vs Text Probe Pre-CP FPR Bootstrap Test

## Summary

Paired bootstrap test comparing hidden-state (HS) temporal probe vs sentence-embedding (text) temporal probe on pre-commitment-point false positive rate for R1-32B.

**Result: No significant difference (p=0.848).**

## Configuration

| Parameter | HS Probe | Text Probe |
|-----------|----------|------------|
| Feature | Layer 2 hidden states | all-MiniLM-L6-v2 (384-d) |
| Window | 10 steps | 10 steps |
| Classifier | LR, balanced, C=1.0 | LR, balanced, C=1.0 |
| Feature dim | 51,200 | 3,840 |

- Dataset: 100 jailbreak traces with commitment points (R1-32B from HarmThoughts)
- Split: 60 train / 20 val / 20 test
- Bootstrap: 1000 resamples, seed=42

## Results

| Metric | Value |
|--------|-------|
| HS pre-CP FPR | 25.65% |
| Text pre-CP FPR | 24.61% |
| Difference (HS - Text) | +1.04% |
| 95% CI | [-9.48%, +11.56%] |
| p-value (two-sided) | 0.848 |
| n_traces (test) | 20 |

## Comparison with QwQ-32B

| Model | HS FPR | Text FPR | Diff | p-value |
|-------|--------|----------|------|---------|
| QwQ-32B | 16.4% | 31.2% | -14.8% | 0.001 |
| R1-32B | 25.7% | 24.6% | +1.0% | 0.848 |

## Interpretation

On R1-32B, the HS temporal probe does NOT achieve significantly lower pre-CP FPR than the text embedding probe. The CI spans zero and the difference is negligible. This contrasts with QwQ-32B where HS probe was significantly better.

Possible explanations:
1. R1-32B early layers (layer 2) may encode less discriminative commitment signals compared to QwQ-32B
2. Text content for R1-32B traces may be more informative for detecting commitment
3. Small test set (n=20) limits statistical power

## Artifact

Output: `artifacts/exp_001a/bootstrap_hs_vs_text_fpr.json`