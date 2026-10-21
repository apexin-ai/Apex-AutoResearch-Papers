# OLMo-1B C4 Rerun: Feature Importance Analysis

**Date**: 2026-05-21
**Data**: `data/exp_olmo1b_c4_rerun/features.csv` (30,000 samples, depths 0-5, 5,000 each)
**Method**: LightGBM + permutation importance, 5-fold GroupKFold, 10 repeats

## 1. OLMo Rerun Per-Pair Results

### 0v1 (AUC = 0.985)
Strong separation. Dominated by delta-surprisal features.

| Rank | Feature | ΔAUC (mean ± std) |
|------|---------|-------------------|
| 1 | Δ¹ Surprisal σ | 0.1595 ± 0.0205 |
| 2 | Surprisal Kurt. | 0.0187 ± 0.0012 |
| 3 | Surprisal Skew | 0.0148 ± 0.0022 |
| 4 | Self-BLEU | 0.0113 ± 0.0009 |
| 5 | Surprisal μ | 0.0067 ± 0.0007 |

### 1v2 (AUC = 0.508, essentially random)
No feature carries meaningful discriminative signal.

| Rank | Feature | ΔAUC (mean ± std) |
|------|---------|-------------------|
| 1 | Δ¹ Surprisal σ | 0.0066 ± 0.0035 |
| 2 | Δ¹ Surprisal Skew | 0.0048 ± 0.0025 |
| 3 | Δ² Surprisal σ | 0.0046 ± 0.0043 |
| 4 | Hapax Ratio | 0.0037 ± 0.0071 |
| 5 | Low-Freq Ratio | 0.0033 ± 0.0052 |

- 6 of 15 features have **negative** importance (noise)
- 8 features have |ΔAUC| < 0.002
- Maximum importance (0.007) is within noise range (std = 0.004)
- Total positive importance: **0.029**

### 2v3 (AUC = 0.501, random)
All features indistinguishable from noise.

## 2. Cross-Model Comparison (1v2 Boundary)

| Model | K* | 1v2 AUC | Top Feature (1v2) | Top ΔAUC | Total Pos. Imp. |
|-------|-----|---------|-------------------|----------|-----------------|
| Qwen-1.5B | 2 | 0.617 | Surprisal σ | 0.065 | 0.209 |
| LLaMA-8B | 2 | 0.610 | Surprisal σ | 0.058 | 0.131 |
| Gemma-2-2B | 2* | 0.601 | Surprisal σ | 0.056 | 0.140 |
| Pythia-1.4B | 2 | 0.587 | Freq. Entropy | 0.056 | 0.129 |
| **OLMo-1B rerun** | **1** | **0.508** | Δ¹ Surprisal σ | **0.007** | **0.029** |
| OLMo-1B old | 1 | 0.507 | Surprisal μ | 0.004 | 0.019 |

*Gemma 1v2 AUC=0.601 with meaningful feature importance; reclassify as borderline K*=2, not K*=1.

### Key discriminative features at 1v2 for K*=2 models
- **Surprisal σ**: ΔAUC = 0.056-0.065 for K*=2 models, **-0.0004** for OLMo
- **Freq. Entropy**: ΔAUC = 0.017-0.056 for K*=2 models, **0.002** for OLMo
- **Surprisal μ**: ΔAUC = 0.013-0.036 for K*=2 models, **0.0004** for OLMo

These three features alone account for >70% of K*=2 models' 1v2 discriminability but contribute essentially nothing for OLMo.

## 3. Why OLMo 1v2 is Indiscriminable

### 3a. Feature collapse after depth 1

The most dramatic feature is Δ¹ Surprisal σ:
- **0v1**: importance = 0.160 (dominant, drives 70% of classification)
- **1v2**: importance = 0.007 (24x reduction, within noise)

For comparison, LLaMA-8B's Δ¹ Surprisal σ drops from 0.209 (0v1) to 0.006 (1v2), a similar 35x collapse. But LLaMA compensates with **Surprisal σ** (0.095 → 0.058, only 1.6x drop) and **Freq. Entropy** (0.064 → 0.017, 3.8x drop). OLMo has no such compensatory features.

### 3b. OLMo's generation reaches a quality floor at depth 1

OLMo-1B on C4 produces a massive quality shift at the 0→1 transition (AUC=0.985) but then immediately plateaus. All statistical fingerprints of the generated text (surprisal distribution, lexical diversity, frequency patterns) stabilize after a single generation pass. The classifier literally cannot distinguish gen-1 from gen-2 because the feature distributions are identical.

### 3c. Contrast with K*=2 models

K*=2 models (LLaMA, Pythia, Qwen, Gemma) show a **gradual degradation** where surprisal variance and frequency entropy continue to shift from gen-1 to gen-2, providing a residual signal. OLMo lacks this gradual shift entirely.

## 4. Gemma Reclassification

The task assumed Gemma-2-2B is K*=1. The data contradicts this:
- Gemma 1v2 AUC = 0.601 (close to LLaMA 0.610, Pythia 0.587)
- Gemma 1v2 top feature (Surprisal σ = 0.056) matches K*=2 pattern
- Gemma 1v2 total positive importance = 0.140 (4.8x OLMo's 0.029)

Gemma should be classified as **borderline K*=2** or at minimum K*=2 with weak 1v2 signal. It does NOT share OLMo's K*=1 feature pattern.

## 5. OLMo is Unique Among Tested Models

OLMo-1B on C4 is the **only model** showing true K*=1 behavior (1v2 AUC ≈ 0.50). The old OLMo pipeline (olmo_c4_cont) showed the same pattern (1v2 AUC=0.507), confirming this is a property of the model, not the pipeline.

### Feature signature of K*=1 (OLMo):
1. No feature has 1v2 importance significantly above zero
2. Importance values are within noise (std > mean for most features)
3. Multiple features show negative importance (overfitting artifacts)
4. Total positive importance is 4-7x lower than any K*=2 model

## 6. Discussion Implications

For the paper discussion section:

1. **Model-dependent K***: OLMo's K*=1 on C4 demonstrates that generative depth resolution is model-dependent, not just a property of the detection method. Some models produce text that reaches a quality floor in one generation.

2. **No universal K*=1 feature signature across models**: Gemma was expected to be K*=1 but its feature importance pattern matches K*=2 models. There is no common "K*=1 feature fingerprint" shared across different model architectures.

3. **OLMo's plateau hypothesis**: OLMo-1B may have a particularly narrow effective capacity relative to C4's complexity, causing immediate saturation of all detectable statistical patterns after one generation pass.

4. **Practical implication**: For contamination detection pipelines, K*=1 models like OLMo can still be detected at depth 1 (AUC=0.985), but multi-generational depth estimation is not possible.

## 7. Output Files

- `results/olmo_feature_importance/importance_results.json` - OLMo rerun per-pair results
- `results/olmo_feature_importance/gemma_importance_results.json` - Gemma per-pair results
- `results/olmo_feature_importance/olmo_rerun_feature_importance.pdf` - OLMo 3-panel barplot (0v1, 1v2, 2v3)
- `results/olmo_feature_importance/cross_model_feature_comparison.pdf` - 5-model comparison (0v1 + 1v2)
