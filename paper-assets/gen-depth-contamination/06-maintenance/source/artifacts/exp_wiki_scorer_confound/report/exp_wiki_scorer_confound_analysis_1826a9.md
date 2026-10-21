# Scorer Confound Analysis: Qwen-7B Wikipedia K*

## Conclusion

**Scorer confound confirmed.** Qwen-7B Wikipedia K\*=2 was an artifact of using a same-family scorer (Qwen-1.5B). With a cross-family scorer (Pythia-1.4B), K\* drops to 1, consistent with all other non-Qwen models on Wikipedia.

## Experiment Setup

| Parameter | exp_wiki_qwen7b (baseline) | exp_wiki_scorer_confound |
|-----------|---------------------------|--------------------------|
| Generator | Qwen2.5-7B | Qwen2.5-7B |
| Scorer | Qwen-1.5B | Pythia-1.4B |
| Domain | Wikipedia | Wikipedia |
| Docs | 5000 | 5000 (symlinked) |
| Depths | 0-5 | 0-5 |
| Decoding | nucleus p=0.95 T=1.0 | nucleus p=0.95 T=1.0 |

## Pairwise AUC Comparison

| Depth Pair | Qwen-1.5B Scorer | Pythia-1.4B Scorer | Delta |
|------------|-------------------|---------------------|-------|
| 0 vs 1 | **0.9673** | 0.9404 | -0.0269 |
| 1 vs 2 | **0.6108** | 0.5870 | -0.0238 |
| 2 vs 3 | 0.5562 | 0.5456 | -0.0106 |
| 3 vs 4 | 0.5297 | 0.5250 | -0.0047 |
| 4 vs 5 | 0.5290 | 0.5172 | -0.0118 |

K\* threshold = 0.60. The critical pair is **1v2**: Qwen scorer gives 0.6108 (barely above), Pythia scorer gives 0.5870 (below).

## JSD Comparison

| Depth Pair | Qwen-1.5B Scorer | Pythia-1.4B Scorer |
|------------|-------------------|---------------------|
| 0 vs 1 | 0.0835 | 0.0689 |
| 1 vs 2 | 0.0110 | 0.0082 |
| 2 vs 3 | 0.0056 | 0.0055 |
| 3 vs 4 | 0.0046 | 0.0040 |
| 4 vs 5 | 0.0039 | 0.0036 |

Qwen scorer shows uniformly higher JSD values, especially at depths 0v1 and 1v2. This is consistent with family bias: Qwen-1.5B captures more distributional difference in Qwen-7B outputs because they share tokenizer and pretraining data distribution.

## Ordinal Classification

| Metric | Qwen-1.5B Scorer | Pythia-1.4B Scorer |
|--------|-------------------|---------------------|
| K\* | 2 | 1 |
| MAE | 1.2501 | 1.3559 |
| Accuracy | 0.3532 | 0.3310 |

Pythia scorer yields worse ordinal classification across the board, confirming it extracts less discriminative signal from Qwen-7B generations.

## Interpretation

1. **The K\*=2 anomaly is a scorer artifact.** Qwen-1.5B scorer inflates AUC for Qwen-7B outputs across all depth pairs. The 1v2 AUC of 0.6108 was only marginally above threshold (0.0108 margin), and this margin disappears entirely with a cross-family scorer.

2. **Family bias is systematic, not limited to the threshold-crossing pair.** AUC drops uniformly by 0.005-0.027 across all pairs when switching from Qwen to Pythia scorer, with the largest drops at shallow depths where surprise-based features carry the most signal.

3. **Corrected result: Qwen-7B Wikipedia K\*=1.** This aligns with all other models (Pythia, OLMo, LLaMA, Mistral) on Wikipedia, removing the Qwen outlier.

## Implication for the Paper

The original claim that Qwen-7B shows deeper memorization on Wikipedia (K\*=2 vs K\*=1 for other models) must be revised. All models tested now show K\*=1 on Wikipedia when scored with a cross-family model. This strengthens the overall narrative: Wikipedia memorization is shallow and uniform across model families.

For any future experiments, scorer and generator should come from different model families to avoid this confound.
