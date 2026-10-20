# qwen25_14b_topk50 — Final Results

**Model**: Qwen2.5-14B | **Precision**: FP16 | **Reference**: self (Qwen2.5-14B)
**Top-k**: k=50 | **Samples**: 5000 per depth (d0–d3), 20000 total | **Features**: 19 (self-ref)
**Server**: gpu-6000pro-2 (cuda:1) | **Runtime**: 24.5h | **Seed**: 42

## Classification Results

### RF 4-class (d0–d3), 5-fold CV
- **Accuracy**: 47.93% (95% CI: [47.26%, 48.59%])
- **Chance baseline**: 25% → **1.92× chance**

### LR 4-class, 5-fold CV
- **Accuracy**: 43.95% (95% CI: [43.23%, 44.65%])

### RF 3-class (d1/d2/d3 only), 5-fold CV
- **Accuracy**: 51.64% (95% CI: [50.83%, 52.39%])
- **Chance baseline**: 33.3% → **1.55× chance**

## Pairwise AUC (RF)

| Pair | AUC |
|------|-----|
| d0v1 | 0.5607 |
| d0v2 | 0.8481 |
| d0v3 | 0.9253 |
| d1v2 | 0.6868 |
| d1v3 | 0.7935 |
| d2v3 | 0.6788 |

**Adjacent-depth AUC**: d0v1=0.561 (weakest), d1v2=0.687, d2v3=0.679.
Top-k truncation makes d0/d1 statistically similar (vocabulary constrained to top-50 tokens at each step), while deeper boundaries remain more stable. This contrasts with nucleus (d2v3=0.728 strongest, monotonically increasing) and temperature (d2v3=0.618 weakest, convergence acceleration).

## Top-5 Feature Importance (RF)

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | kurt_ppl | — |
| 2 | skew_ppl | — |
| 3 | var_surprisal | — |
| 4 | type_token_ratio | — |
| 5 | hapax_ratio | — |

Note: Top-k shifts feature importance toward lexical diversity metrics (TTR, hapax_ratio enter top-5) vs. tail perplexity dominance in nucleus/temp09. This reflects top-k's vocabulary truncation effect.

## 14B Three-Strategy Summary

| Strategy | RF 4-class Acc | d0v1 | d1v2 | d2v3 | Pattern |
|----------|---------------|------|------|------|---------|
| Nucleus (p=0.95) | 54.05% | 0.643 | 0.713 | 0.728 | Monotonically increasing |
| Temperature (τ=0.9) | 50.50% | 0.632 | 0.726 | 0.618 | d2v3 collapse (convergence acceleration) |
| Top-k (k=50) | 47.93% | 0.561 | 0.687 | 0.679 | d0v1 collapse (vocabulary truncation) |
| **Mean** | **50.83%** | — | — | — | — |

Each strategy produces a structurally distinct AUC pattern at 14B, directly supporting "structurally distinct degradation trajectories" (§6). The three patterns are not noise — each has a mechanistic explanation tied to the decoding algorithm's effect on the token distribution.

## Assessment

**Conclusion: success**. RF 4-class 47.93% is 1.92× chance (25%), confirming depth signal persists at 14B even under top-k — the weakest strategy across all scales. Top-k consistently yields the lowest accuracy (also true at 1-1.5B), but signal remains well above chance.

With all three strategies complete, 14B mean accuracy is 50.83% (2× chance), fully addressing Reviewer M3 ("14B too narrow — only nucleus"). The strategy-specific AUC patterns are a bonus finding for the paper.
