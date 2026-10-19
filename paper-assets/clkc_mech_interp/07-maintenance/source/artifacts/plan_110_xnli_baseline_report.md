# XNLI Non-Conflict Semantic Baseline — Experiment Report

**Date**: 2026-05-22
**Objective**: Determine whether the cross-lingual probe transfer asymmetry (~7pp ZH→EN > EN→ZH) observed in knowledge conflict tasks is conflict-specific or a general cross-lingual property.

## 1. Experimental Setup

| Parameter | Value |
|-----------|-------|
| Models | Qwen3-8B, Llama-3.1-8B-Instruct |
| Data | XNLI validation split (entailment + contradiction, neutral filtered) |
| Labels | entailment → no_conflict (0), contradiction → conflict (1) |
| Train/Test | 800/200 per language, ~50/50 label balance |
| Probe | LogisticRegression (LBFGS, class_weight='balanced', max_iter=1000) |
| Metric | Balanced accuracy (peak layer) |
| Bootstrap | n=2000 for XNLI, n=1000 for conflict (existing) |
| GPU | westd-41302 cuda:3 (CUDA_VISIBLE_DEVICES=0) |

## 2. XNLI Probe Results (Peak Layer Balanced Accuracy)

### Qwen3-8B

| Direction | Bal. Acc | F1 | Peak Layer |
|-----------|---------|------|------------|
| EN→EN | 96.58% | 96.65% | L32 |
| ZH→ZH | 89.49% | 89.66% | L30 |
| EN→ZH | 90.45% | 91.00% | L22 |
| ZH→EN | 97.17% | 97.09% | L23 |

### Llama-3.1-8B-Instruct

| Direction | Bal. Acc | F1 | Peak Layer |
|-----------|---------|------|------------|
| EN→EN | 93.98% | 94.34% | L14 |
| ZH→ZH | 87.47% | 87.92% | L16 |
| EN→ZH | 88.95% | 89.62% | L17 |
| ZH→EN | 94.92% | 95.33% | L18 |

## 3. Conflict Probe Results (Existing, for Comparison)

### Qwen3-8B

| Direction | Bal. Acc | F1 | Peak Layer |
|-----------|---------|------|------------|
| EN→EN | 75.00% | 75.00% | L24 |
| ZH→ZH | 72.62% | 73.56% | L14 |
| EN→ZH | 67.26% | 68.93% | L23 |
| ZH→EN | 73.21% | 70.97% | L18 |

### Llama-3.1-8B-Instruct

| Direction | Bal. Acc | F1 | Peak Layer |
|-----------|---------|------|------------|
| EN→EN | 77.57% | 78.14% | L28 |
| ZH→ZH | 72.06% | 71.21% | L13 |
| EN→ZH | 59.56% | 56.35% | L5 |
| ZH→EN | 71.32% | 75.16% | L15 |

## 4. Asymmetry Comparison (ZH→EN − EN→ZH)

| Model | Task | Asymmetry | 95% CI | Excludes 0? |
|-------|------|-----------|--------|-------------|
| Qwen3-8B | **XNLI** | **+6.72pp** | [+2.36, +11.73] | **Yes** |
| Qwen3-8B | Conflict | +5.95pp | [−3.67, +14.81] | No |
| Llama-3.1-8B | **XNLI** | **+5.97pp** | [+0.92, +11.33] | **Yes** |
| Llama-3.1-8B | Conflict | +11.76pp | [+4.29, +19.57] | Yes |

## 5. Interpretation

### Key Finding: Asymmetry is NOT conflict-specific

The ZH→EN > EN→ZH transfer asymmetry persists in XNLI (a non-conflict NLI task), with comparable magnitude to the knowledge conflict task:

- **Qwen3-8B**: XNLI asymmetry (+6.72pp) is actually **larger** than conflict asymmetry (+5.95pp). The XNLI CI excludes zero while the conflict CI does not.
- **Llama-3.1-8B**: XNLI asymmetry (+5.97pp) is **smaller** than conflict asymmetry (+11.76pp), but both exclude zero.

### Why ZH→EN transfers better than EN→ZH

This is a general cross-lingual representation property, not a conflict-specific phenomenon. Possible explanations:

1. **EN dominance in pretraining**: Both models were pretrained on English-dominant corpora. EN test representations are in the model's "native" space, making them easier to classify regardless of training language.
2. **ZH representations carry richer features**: ZH probes may learn features that generalize to EN (since ZH requires encoding both language-specific and universal semantic features), while EN probes learn more EN-specific features that transfer poorly to ZH.
3. **Representation alignment asymmetry**: The EN→ZH direction requires the probe to generalize across a larger representational gap (EN-trained probe applied to ZH space) than the reverse.

### Implications for the conflict study

The ~6pp asymmetry observed in knowledge conflict probes should **not** be interpreted as evidence that conflict detection mechanisms differ by language direction. It is a baseline property of cross-lingual transfer in these models. For Llama, the conflict asymmetry (+11.76pp) exceeds the XNLI baseline (+5.97pp), suggesting there **may** be an additional conflict-specific component (~5.8pp), but this difference is within the confidence intervals' overlap.

## 6. Data & Artifact Locations (westd-41302)

```
# XNLI activations & results
data/xnli/qwen3/{en,zh}_activations.pt
data/xnli/qwen3/probe_results.json
data/xnli/qwen3/bootstrap_asymmetry.json
data/xnli/qwen3/probe_accuracy_by_layer.png

data/xnli/llama31/{en,zh}_activations.pt
data/xnli/llama31/probe_results.json
data/xnli/llama31/bootstrap_asymmetry.json
data/xnli/llama31/probe_accuracy_by_layer.png

# Conflict probe results (existing)
data/qwen3/probe_results.json
data/qwen3/bootstrap_asymmetry.json
data/llama31/probe_results.json
data/llama31/bootstrap_asymmetry.json
```
