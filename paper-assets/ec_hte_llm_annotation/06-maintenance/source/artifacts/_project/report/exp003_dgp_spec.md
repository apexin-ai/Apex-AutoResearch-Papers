# exp-003 Phase A: DGP Specification

## Data Source
- **Dataset**: TweetEval sentiment (cardiffnlp/tweet_eval, sentiment split)
- **Reference**: Barbieri et al. (2020)
- **Pool size**: 57899 tweets (train + test merged)
- **Label distribution**: negative=11065 (19.1%), neutral=26610 (46.0%), positive=20224 (34.9%)

## Sampling Strategy
- Each MC run samples N=5000 tweets with approximate label balance (~1666 per class)
- Sampling with replacement from pool (pool size >> N, minimal collision)

## Subgroup Definition (K=4)

Two binary features define 4 subgroups:

| Feature | Definition | Rationale |
|---------|-----------|-----------|
| `has_hashtag` | Text contains '#' | Hashtags shift LLM attention; informal/emphatic language may increase misclassification |
| `text_length_bin` | Above/below median length (110 chars) | Longer texts provide more context but also more noise for sentiment classification |

| Subgroup | has_hashtag | text_length_bin | Approx. proportion |
|----------|-------------|-----------------|---------------------|
| S0 | 0 (no) | 0 (short) | ~39% |
| S1 | 0 (no) | 1 (long) | ~38% |
| S2 | 1 (yes) | 0 (short) | ~12% |
| S3 | 1 (yes) | 1 (long) | ~11% |

Prevalence of hashtag: 23.1%

## Effect Modifier Z
- Z=1 if sentiment == positive (label 2)
- Z=0 if sentiment != positive (label 0 or 1)
- P(Z=1) ≈ 34.9%

## Misclassification Rates (Symmetric, A2 Assumption)

P(Z_hat ≠ Z | S=s) = π_s

| Regime | S0 | S1 | S2 | S3 | Rationale |
|--------|----|----|----|----|-----------|
| extreme | 0.05 | 0.10 | 0.15 | 0.25 | Large heterogeneity; hashtag texts are harder |
| moderate | 0.08 | 0.10 | 0.12 | 0.15 | Modest gradient |
| homogeneous | 0.10 | 0.10 | 0.10 | 0.10 | Null hypothesis (no heterogeneity) |

Rates are informed by typical LLM sentiment accuracy on tweets (85-95% in literature),
with the gradient reflecting empirical findings that informal/hashtag-heavy text
degrades classifier performance.

## Outcome Model

Y = α + τ(Z, S) · T + β₁ · text_length_normalized + β₂ · has_mention + ε

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| α | 1.0 | Intercept |
| τ(Z=0, all S) | 0.1 | Baseline treatment effect |
| δ_S0 | 0.4 | Additional effect for Z=1 in S0 |
| δ_S1 | 0.3 | Additional effect for Z=1 in S1 |
| δ_S2 | 0.2 | Additional effect for Z=1 in S2 |
| δ_S3 | 0.1 | Additional effect for Z=1 in S3 |
| β₁ | 0.3 | Text length effect (normalized) |
| β₂ | 0.2 | Mention (@) effect |
| ε | N(0, 1) | Noise |
| T | Bernoulli(0.5) | RCT |

τ(Z=1, S=s) = 0.1 + δ_s, so treatment effects range from 0.2 (S3) to 0.5 (S0).

## Expert Annotation
- n_expert ∈ {50, 100, 250, 500}
- Randomly selected observations with both Z and Z_hat observed

## Difference from Pure Synthetic DGP (MVP/exp-001/exp-002)
1. **Real text features**: Subgroups come from actual tweet characteristics, not random assignment
2. **Correlated subgroup sizes**: Subgroup proportions are data-driven and unbalanced
3. **Real covariates in outcome model**: text_length and has_mention are real text features
4. **Non-uniform Z prevalence**: P(Z=1) ≈ 34.9%, not 50%
5. **Subgroup-covariate correlation**: Text length correlates with hashtag presence and sentiment
