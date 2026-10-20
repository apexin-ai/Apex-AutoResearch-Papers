# exp_wiki_scorer_confound_1b5 Analysis Report

## Experiment Configuration

| Parameter | Value |
|-----------|-------|
| Experiment | exp_wiki_scorer_confound_1b5 |
| Generator | Qwen-1.5B (Wikipedia, depth 0-5) |
| Scorer | Pythia-1.4B (cross-model confound check) |
| Data source | exp_023_domain_ablation generated texts |
| Purpose | Verify if Qwen-1.5B K*=2 is scorer artifact |

## Core Metrics

### K* = 1

### Pairwise AUC (adjacent depths, 5-fold CV)

| Pair | AUC (mean) | Std | Verdict |
|------|-----------|-----|---------|
| 0 vs 1 | **0.9729** | 0.0007 | Discriminable |
| 1 vs 2 | 0.5994 | 0.0048 | Near-random |
| 2 vs 3 | 0.5330 | 0.0036 | Random |
| 3 vs 4 | 0.5214 | 0.0082 | Random |
| 4 vs 5 | 0.5068 | 0.0120 | Random |

### JSD (adjacent depths)

| Pair | JSD |
|------|-----|
| 0 vs 1 | 0.0886 |
| 1 vs 2 | 0.0096 |
| 2 vs 3 | 0.0060 |
| 3 vs 4 | 0.0038 |
| 4 vs 5 | 0.0033 |

### Ordinal Classification (6-class)

- MAE: 1.2995
- Accuracy: 0.3466 (random baseline = 0.167)

## Comparison with Qwen-7B Confound Experiment

| Metric | 7B (exp_wiki_scorer_confound) | 1.5B (this exp) |
|--------|-------------------------------|-----------------|
| K* | 1 | 1 |
| AUC 0v1 | 0.9404 | **0.9729** |
| AUC 1v2 | 0.587 | 0.5994 |
| AUC 2v3 | ~0.5 | 0.533 |
| Pattern | Sharp drop after depth 0 | Sharp drop after depth 0 |

Both experiments show identical pattern: Pythia scorer only distinguishes depth-0 from depth-1+. The 1.5B version actually shows slightly higher AUC 0v1 (0.9729 vs 0.9404), suggesting the depth-0 stylistic difference is even more pronounced in Qwen-1.5B outputs.

## Confound Verdict: CONFIRMED

The Pythia cross-model scorer produces K*=1 for both Qwen-7B and Qwen-1.5B generated Wikipedia texts. This means:

1. **Original Qwen-1.5B self-scoring K*=2 is a scorer artifact.** When Qwen-1.5B scores its own outputs, it exploits model-specific stylistic signatures (not genuine depth complexity) to achieve above-chance discrimination at depth 1v2.

2. **The only real signal is depth-0 vs depth-1+.** This likely reflects the structural difference between seed prompts (depth 0) and all generated continuations (depth 1+), not genuine generative depth complexity.

3. **Cross-model validation is essential.** Both 7B and 1.5B self-scoring K* values are inflated by scorer confound.

## Impact on Domain x Model Matrix

- Wikipedia domain: K* should be treated as 1 (not 2) for Qwen-1.5B
- The depth-0 signal is a trivial boundary effect (original vs generated text)
- For the depth complexity hypothesis to hold, we need domains/models where cross-model scoring preserves K* > 1
- Next steps should focus on domains where original K* was higher (e.g., code, math) to see if cross-model scoring still shows signal

## Top Feature Importance (Pythia scorer)

1. freq_entropy (8822)
2. surp_mean (8337)
3. surp_d1_skew (8205)
4. surp_d2_mean (7931)
5. surp_d1_mean (7843)

The dominance of frequency/surprisal features aligns with the confound interpretation: Pythia distinguishes texts by surface-level statistical patterns rather than deep structural complexity.
