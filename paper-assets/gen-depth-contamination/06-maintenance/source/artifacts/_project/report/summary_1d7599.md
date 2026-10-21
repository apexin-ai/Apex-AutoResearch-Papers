# C4 Borderline Cases: Feature-Level Error Analysis

## Data Coverage

6 models analyzed (all C4 domain, 1v2 pair = depth-1 vs depth-2 classification):

| Model | Experiment | 1v2 AUC | Category |
|---|---|---|---|
| Pythia-1.4B (greedy) | exp_020 | 0.884 | Strong |
| Pythia-1.4B (nuc=0.9) | exp_020 | 0.677 | Strong |
| Qwen-1.5B-base | exp_016 | 0.626 | Strong |
| Pythia-1.4B (temp=1.2) | exp_020 | 0.617 | Borderline |
| LLaMA-3.1-8B | exp_018 | 0.612 | Borderline |
| Mistral-7B | exp_019 | 0.594 | Below theta |

**Not available on disk**: exp_001 (Pythia-1.4B original), exp_002 (OLMo-1B), exp_017 (Qwen-1.5B-cont), mvp_pilot (Qwen-1.5B-RW). Analysis uses available experiments that span the full AUC range.

---

## Finding 1: Why Mistral-7B Has K*=1

Mistral is the only model where 1v2 AUC (0.594) falls below the theta=0.60 threshold. Three factors explain this:

**1a. Uniformly small effect sizes.** Mistral's mean |Cohen's d| = 0.112, the lowest (tied with Pythia-t12). Every core feature has a weak 1v2 signal:
- surp_d1_std: d = -0.212 (vs -0.342 for Pythia-nuc09, -0.306 for LLaMA)
- surp_std: d = -0.190 (vs -0.370 for Pythia-nuc09, -0.316 for LLaMA)
- surp_mean: d = -0.152 (vs -0.306 for Pythia-nuc09, -0.263 for LLaMA)

**1b. Lower baseline surprisal.** Mistral's depth-0 surp_mean = 2.317, significantly lower than Pythia (3.018) and Qwen/LLaMA (2.901). This means the scoring model already finds Mistral's training data less surprising, compressing the dynamic range available for detecting generative degradation.

**1c. Diffuse feature importance.** Mistral's top-1 feature (surp_std) captures only 12.9% of total gain importance. The signal is spread across many weak features rather than concentrated in a few strong ones, making it harder for the classifier to build a reliable decision boundary.

---

## Finding 2: Why Pythia-t12 and LLaMA-3.1-8B Are Borderline

### Pythia-t12 (AUC = 0.617)

High temperature (1.2) injects noise into the generation process, making consecutive depths harder to distinguish:
- **Smallest surprisal delta(1 to 2)** of all models: -0.059 (vs -0.160 for Pythia-greedy, -0.196 for Pythia-nuc09)
- Mean |d| = 0.112, tied with Mistral for lowest
- surp_skew flips sign: d = -0.217 for Pythia-t12 vs +0.086 to +0.468 for all other models, indicating temperature inverts the skewness pattern of the surprisal distribution

### LLaMA-3.1-8B (AUC = 0.612)

LLaMA presents a paradox: it has higher mean |d| (0.137) than Qwen-1.5B-base (0.125) yet achieves lower AUC (0.612 vs 0.626). Two factors explain this:

**Anomalous delta ratio.** LLaMA is the only model where delta(1 to 2) exceeds delta(0 to 1): -0.215 vs -0.199 (ratio = 1.08). Every other model has ratio 0.06 to 0.27. This means LLaMA's generation doesn't stabilize after the first step; instead, surprisal keeps dropping at a comparable rate. While this produces moderate Cohen's d values, the non-monotonic convergence pattern may confuse the classifier.

**Dispersed feature importance.** LLaMA's top-1 feature (surp_std) captures only 12.5% of total importance, the lowest among all models. For comparison, Pythia-nuc09 concentrates 19.8% and Qwen 13.0% in surp_std. LLaMA also distributes importance more evenly across freq_entropy (9.2%), surp_d1_std (9.9%), and surp_mean (6.8%), rather than having one dominant signal.

---

## Finding 3: Surprisal Attenuation and Model Capacity

The depth profiles reveal a clear mechanistic pattern:

```
surp_mean depth profile:
  Pythia-greedy:  d0=3.018  d1=0.580  d2=0.420   (81% drop at d0->d1)
  Pythia-nuc09:   d0=3.018  d1=2.053  d2=1.857   (32% drop)
  Qwen-1.5B:      d0=2.901  d1=2.303  d2=2.144   (21% drop)
  Pythia-t12:     d0=3.018  d1=2.732  d2=2.673   (9.5% drop)
  LLaMA-8B:       d0=2.901  d1=2.702  d2=2.487   (6.9% drop)
  Mistral-7B:     d0=2.317  d1=1.989  d2=1.904   (14% drop)
```

The surprisal drop from depth 0 to depth 1 (0v1 signal) is much larger than depth 1 to 2 (1v2 signal) for all models. The 1v2 classification operates on the "tail" of this attenuation curve, where the residual signal is inherently small.

**Key insight**: The 0 to 1 drop magnitude predicts 1v2 discriminability. Greedy decoding creates a massive drop (3.02 to 0.58), leaving a measurable residual at 1v2. Nucleus sampling preserves more diversity (drop to 2.05), yielding moderate 1v2 signal. High temperature and larger models further reduce the 0 to 1 drop, pushing the 1v2 residual below the detection threshold.

This creates a fundamental scaling challenge: as models become more capable (better approximating the training distribution), each generation step produces less degradation, and the 1v2 boundary signal vanishes.

---

## Finding 4: Feature-Specific Patterns

### Dominant features for 1v2 classification

Across all non-greedy models, the same three features dominate:
1. **surp_std** (12-20% importance): standard deviation of token-level surprisal. Cohen's d ranges from -0.19 (Mistral) to -0.37 (Pythia-nuc09).
2. **freq_entropy** (9-11% importance): entropy of token frequency distribution.
3. **surp_d1_std** (6-10% importance): std of first-derivative of surprisal sequence.

### Greedy decoding is qualitatively different

Pythia-greedy is an outlier: hapax_ratio (46.5% importance, d = -1.056) and low_freq_ratio (8.2%, d = -1.029) dominate. Greedy decoding eliminates rare tokens, creating a massive lexical signal that doesn't exist under sampling-based generation.

### Features that fail at the boundary

These features provide essentially zero signal at 1v2 across all models:
- **surp_d2_mean** (second derivative of surprisal, mean): |d| < 0.035 for all models
- **surp_d1_mean** (first derivative mean): |d| < 0.08 for all models
- **freq_kurtosis**: |d| < 0.09 for all models

---

## Summary Table

| Model | AUC | mean |d| | Top Feature | Strongest d | Delta(1->2) |
|---|---|---|---|---|---|
| Pythia-greedy | 0.884 | 0.365 | hapax_ratio (47%) | hapax_ratio: -1.056 | -0.160 |
| Pythia-nuc09 | 0.677 | 0.170 | surp_std (20%) | surp_std: -0.370 | -0.196 |
| Qwen-1.5B | 0.626 | 0.125 | surp_std (13%) | surp_d2_std: -0.247 | -0.159 |
| Pythia-t12 | 0.617 | 0.112 | surp_std (15%) | surp_std: -0.268 | -0.059 |
| LLaMA-8B | 0.612 | 0.137 | surp_std (12%) | surp_std: -0.316 | -0.215 |
| Mistral-7B | 0.594 | 0.112 | surp_std (13%) | surp_d1_std: -0.212 | -0.086 |

## Outputs

- `borderline_features.tex`: Main summary table (Table \ref{tab:borderline_features})
- `cohens_d_full.tex`: Full Cohen's d matrix (Table \ref{tab:cohens_d_full})
- `full_results.json`: Complete numerical results
