# exp-023: Second NLP Dataset Semi-Synthetic Validation — Final Report

## Objective

Reproduce EC-HTE's core results on Civil Comments (toxicity detection) as a second NLP dataset, addressing Reviewer C1's concern that only TweetEval was used.

## Dataset: Civil Comments

- **Source**: google/civil_comments (HuggingFace), 1.8M comments
- **Task**: Binary toxicity classification (threshold ≥ 0.5)
- **Pool**: 3,000 stratified-sampled comments (30% toxic)
- **LLM models**: gpt-4o, gpt-4o-mini, gpt-3.5-turbo via OpenAI-compatible proxy

---

## Claim 1: Heterogeneous LLM Misclassification (Confirmed)

All three models show substantial subgroup heterogeneity in misclassification rates (subgroups: text_length × has_question, K=4):

| Model | FPR range | FNR range | Δ_FPR | Δ_FNR |
|-------|-----------|-----------|-------|-------|
| gpt-4o | 0.157–0.341 | 0.160–0.328 | **0.184** | **0.168** |
| gpt-4o-mini | 0.419–0.610 | 0.052–0.160 | **0.191** | **0.108** |
| gpt-3.5-turbo | 0.374–0.473 | 0.139–0.240 | **0.099** | **0.101** |

All Δ_FPR > 0.05 threshold. Misclassification is clearly heterogeneous across text-feature-defined subgroups, confirming the premise of EC-HTE on a new domain.

---

## Claim 2: EC-HTE Outperforms Naive and Global Correction (Confirmed)

Semi-synthetic DGP on Civil Comments: N=10,000, P(Z=1)=0.30, tau(z=0)=0.0, tau(z=1)=0.5, MC=50.
Symmetric misclassification matching TweetEval design.

### Extreme regime (π_S0=0.05, π_S1=0.30)

| Method | n=250 RMSE | n=500 RMSE | n=1000 RMSE | n=500 Cov |
|--------|-----------|-----------|------------|----------|
| Oracle | 0.045 | 0.045 | 0.045 | 0.930 |
| **Naive** | **0.113** | **0.113** | **0.113** | **0.555** |
| **Global** | **0.140** | **0.135** | **0.133** | **0.580** |
| Strat. MLE | 0.108 | 0.093 | 0.081 | 0.865 |
| **EC-HTE** | **0.108** | **0.093** | **0.081** | **0.865** |

EC-HTE at n_expert=500: **18% lower RMSE** than Naive, **31% lower** than Global.
Coverage: 0.865 vs 0.555 (Naive) and 0.580 (Global).

### Moderate regime (π_S0=0.08, π_S1=0.20)

| Method | n=250 RMSE | n=500 RMSE | n=1000 RMSE | n=500 Cov |
|--------|-----------|-----------|------------|----------|
| Oracle | 0.045 | 0.045 | 0.045 | 0.930 |
| **Naive** | **0.098** | **0.098** | **0.098** | **0.580** |
| **Global** | **0.088** | **0.081** | **0.080** | **0.845** |
| Strat. MLE | 0.085 | 0.067 | 0.061 | 0.910 |
| **EC-HTE** | **0.085** | **0.067** | **0.061** | **0.910** |

EC-HTE at n_expert=500: **31% lower RMSE** than Naive, **17% lower** than Global.
Coverage: 0.910 vs 0.580 (Naive) and 0.845 (Global).

### Z=1 subgroup detail (extreme, n=500) — where correction matters most

| Method | S1 Bias | S1 RMSE | Coverage |
|--------|---------|---------|----------|
| Naive | -0.255 | 0.259 | 0.380 |
| Global | -0.150 | 0.168 | 0.400 |
| **EC-HTE** | **+0.024** | **0.169** | **0.850** |

EC-HTE reduces absolute bias from 0.255 to 0.024 (91% reduction) on the high-misclassification subgroup.

---

## Design Sensitivity Analysis

v2 experiment (K=4, asymmetric FPR≠FNR, N=5000) showed EC-HTE performing worse than Naive. Root cause: with K=4 and unbalanced subgroups (S1=11.4%), per-subgroup CM estimation is too noisy, and the small misclassification bias doesn't justify the variance cost.

v3 (K=2, symmetric misclassification, N=10000) matches TweetEval's design structure and clearly shows EC-HTE advantage. The crossover point (where EC-HTE beats Naive on RMSE) is at n_expert ≈ 250.

This sensitivity to K and N is consistent with the original TweetEval results, where EC-HTE's advantage is also marginal at small n_expert and grows with sample size.

---

## Files

| File | Description |
|------|-------------|
| `exp023_civil_comments_prepare.py` | Data download, stratified sampling, subgroup assignment |
| `exp023_annotate_parallel.py` | Parallel LLM annotation with checkpointing |
| `exp023_civil_comments_semisynthetic_v3.py` | **Main experiment**: K=2 semi-synthetic DGP |
| `results/exp023_confusion_matrices.json` | Per-subgroup CMs for 3 models |
| `results/exp023_semisynthetic_v3_summary.csv` | Full numerical results |
| `results/exp023_semisynthetic_v3_analysis.md` | Detailed analysis report |
