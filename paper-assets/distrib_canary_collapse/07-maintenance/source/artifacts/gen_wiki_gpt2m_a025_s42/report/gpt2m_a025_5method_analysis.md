# GPT-2 Medium α=0.25 s42: Analysis Report

## A. Metrics Summary (gen0 → gen10)

| Metric | gen0 | gen10 | Drift % |
|--------|------|-------|---------|
| token_entropy | 3.5714 | 2.3999 | -32.8% |
| ece | 0.0112 | 0.0583 | +422.0% |
| perplexity | 32.63 | 18.12 | -44.5% |
| distinct_1 | 0.1044 | 0.0799 | -23.5% |
| distinct_2 | 0.5483 | 0.3750 | -31.6% |
| distinct_3 | 0.8441 | 0.5893 | -30.2% |
| effective_rank | 2.3722 | 8.4833 | +257.6% |
| mauve | 0.0315 | 0.0282 | -10.5% |

**Key observations:**
- Perplexity *improves* (decreases) because α=0.25 means 75% real data still trains the model
- Diversity (distinct_1/2/3) steadily declines: -23% to -32%
- Token entropy drops sharply at gen1 (3.57→2.59) then plateaus
- ECE degrades monotonically (model becomes miscalibrated)
- MAUVE warning: both values are very low (~0.03) due to sample count mismatch (3128 < 6084)

## B. Effective Rank Anomaly Investigation

### Findings: NOT a bug — genuine model-dependent phenomenon

**Evidence:**
1. Code review of `metrics.py:compute_effective_rank` (L172-210): identical implementation for all models. Uses last-layer hidden states, mean-pooled per sample (N=256 samples, D=1024 dims), covariance eigenvalue entropy.

2. Cross-experiment comparison:
   | Model | α | gen0 ER | gen10 ER | Drift |
   |-------|---|---------|----------|-------|
   | GPT-2m | 0.25 | 2.37 | 8.48 | +258% |
   | GPT-2m | 1.0 | 2.37 | 26.74 | +1027% |
   | Pythia-410M | 0.25 | 46.61 | 45.30 | -2.8% |

3. The monotonic dose-response (higher α → larger ER increase) rules out an implementation bug.

### Mechanism

GPT-2m's pretrained representations are **extremely low-dimensional** (ER≈2.37): nearly all variance concentrates in ~2 principal components of the last-layer hidden states evaluated on real text. This reflects highly efficient, structured representations.

As the model collapses through iterative synthetic training:
- The sharp low-dimensional structure **degrades** (dominant eigenvalues lose relative magnitude)
- Eigenvalue distribution **flattens** → entropy increases → effective_rank rises
- The model's representations of real data become less organized, not more concentrated

For Pythia (ER≈46.6): representations start relatively uniform across dimensions, so collapse mildly concentrates them (small ER decrease).

### Implication for the paper
- effective_rank **direction is model-dependent** — it cannot be used as a universal "lower=collapse" canary
- The **magnitude of change** still correlates with collapse severity (monotonic with α)
- Recommend reporting effective_rank as supporting evidence with explicit directionality caveat, or dropping it from CANARY list and using only token_entropy + ECE

## C. 5-Method Lead-Lag Analysis

### Configuration
- T=11 (gen0-gen10), single seed (s42)
- Canaries: token_entropy, ece
- Downstream: distinct_1, distinct_2, distinct_3, perplexity
- Permutation Granger: 5000 permutations, differenced, max_lag=1
- TY Granger: recorded per C003 (α≤0.50, not used as supporting evidence)

### Consensus Table

| Canary | Downstream | Naive | Diff | Thresh | PermG | TY | Tier |
|--------|-----------|-------|------|--------|-------|-----|------|
| token_entropy | distinct_1 | * (lag=2) | * (lag=-1) | * (lt=5) | n.s. | n.s. | 2/5 |
| token_entropy | distinct_2 | * (lag=2) | * (lag=-1) | * (lt=6) | n.s. | n.s. | 2/5 |
| token_entropy | distinct_3 | * (lag=2) | * (lag=-3) | * (lt=6) | n.s. | * | 3/5 |
| token_entropy | perplexity | * (lag=0) | * (lag=0) | n.s. | n.s. | n.s. | 2/5 |
| ece | distinct_1 | * (lag=3) | * (lag=-1) | * (lt=5) | n.s. | n.s. | 2/5 |
| ece | distinct_2 | * (lag=3) | * (lag=-3) | * (lt=6) | n.s. | n.s. | 2/5 |
| ece | distinct_3 | * (lag=3) | * (lag=-3) | * (lt=6) | n.s. | n.s. | 2/5 |
| ece | perplexity | * (lag=0) | * (lag=0) | n.s. | n.s. | n.s. | 2/5 |

### Per-Method Summary
- **Naive Pearson**: 8/8 significant (expected: non-stationary trending series)
- **Differenced xcorr**: 8/8 significant, but negative lags on diversity pairs (see note below)
- **Threshold onset**: 6/8 (canary onset=gen1, diversity onset=gen6-7; perplexity never exceeds threshold)
- **Permutation Granger**: 0/8 (underpowered: T=11 with weak α=0.25 signal)
- **TY Granger**: 1/8 (per C003: not used as evidence at α≤0.50)

### Interpretation

**Tier classification: 1/8 pairs Tier 3, 7/8 pairs Tier 2** (vs. gpt2m_a100: 6/6 diversity pairs Tier 3)

The weaker signal at α=0.25 vs α=1.0 is expected:
- Threshold onset clearly identifies token_entropy/ECE leading diversity by 5-6 generations
- Permutation Granger lacks power at T=11 with the attenuated contamination signal
- Differenced xcorr shows negative lags because: the largest Δ(token_entropy) occurs at gen0→1 (−0.98), while Δ(distinct) changes accumulate gradually later. After differencing, the increment correlation structure reverses the apparent lag direction

**Note on perplexity pairs**: Perplexity *decreases* (improves) at α=0.25 because 75% real data dominates training. Threshold onset can't detect degradation that doesn't occur. The negative naive correlation (r≈-0.99) reflects the simultaneous improvement of perplexity while token_entropy drops — both driven by early training dynamics, not a lead-lag relationship.

### Comparison with gpt2m_a100 reference
| | α=1.0 (s42) | α=0.25 (s42) |
|---|---|---|
| Diversity pairs at Tier 3+ | 6/6 | 1/6 |
| Perm Granger sig | 4/6 | 0/8 |
| TY sig | 0/6 | 1/8 (unreliable per C003) |
| Perplexity direction | increases (collapse) | decreases (improvement) |

The dose-response is clear: α=1.0 produces strong lead-lag detectable by robust methods; α=0.25 produces lead-lag visible only via naive/threshold methods.

---
*Analysis script: gpt2m_a025_analysis.py*
*Raw results: results/gen_wiki_gpt2m_a025_s42/analysis/5method_leadlag.json*
