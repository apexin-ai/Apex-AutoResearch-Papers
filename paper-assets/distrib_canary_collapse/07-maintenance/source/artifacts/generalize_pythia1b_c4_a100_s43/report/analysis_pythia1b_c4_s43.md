# Analysis: Pythia-1B C4 seed=43 (Multi-seed Validation)

**Date**: 2026-05-18
**Parent**: generalize_pythia1b_c4_a100_s42_v2 (seed=42, success)
**Hypothesis**: C4 domain multi-seed validation — seed=43 replicates 8/8 consensus and token_entropy unidirectionality

## Gen0 / Gen10 Metrics & Drift

| Metric | gen0 | gen10 | drift_pct |
|--------|------|-------|-----------|
| token_entropy | 2.956 | 1.275 | -56.9% |
| ece | 0.012 | 0.453 | +3542.3% |
| perplexity | 20.60 | 1591.0 | +7623.7% |
| distinct_1 | 0.116 | 0.088 | -24.3% |
| distinct_2 | 0.562 | 0.378 | -32.7% |
| distinct_3 | 0.838 | 0.570 | -31.9% |
| mauve | 0.786 | 0.289 | -63.2% |
| effective_rank | 72.5 | 146.2 | +101.6% |

## 8-Pair 6-Method Results

8 pairs = {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, mauve}

### Method Sig Rates (FDR-corrected)

| Method | Sig/8 |
|--------|-------|
| naive_xcorr | 8/8 |
| diff_xcorr_fdr | 8/8 |
| threshold_onset | 8/8 |
| permg_fwd_fdr | 8/8 |
| permg_rev_fdr | 0/8 |
| ty_granger | 5/8 |

### Per-Pair Consensus (5 methods: naive, diff_xcorr, threshold, permg_fwd, TY)

| Pair | Consensus |
|------|-----------|
| token_entropy -> distinct_1 | 5/5 |
| token_entropy -> distinct_2 | 4/5 |
| token_entropy -> distinct_3 | 4/5 |
| token_entropy -> mauve | 4/5 |
| ece -> distinct_1 | 5/5 |
| ece -> distinct_2 | 5/5 |
| ece -> distinct_3 | 5/5 |
| ece -> mauve | 5/5 |

**consensus_ge3: 8/8**
**consensus_ge4: 8/8**

### Token_entropy Unidirectionality (PermG reverse)

| Pair | rev p_fdr | sig |
|------|-----------|-----|
| token_entropy -> distinct_1 | 0.791 | No |
| token_entropy -> distinct_2 | 0.849 | No |
| token_entropy -> distinct_3 | 0.893 | No |
| token_entropy -> mauve | 0.719 | No |

**token_entropy rev: 0/4** (perfect unidirectionality confirmed)

### ECE Reverse (PermG)

| Pair | rev p_fdr | sig |
|------|-----------|-----|
| ece -> distinct_1 | 0.719 | No |
| ece -> distinct_2 | 0.615 | No |
| ece -> distinct_3 | 0.615 | No |
| ece -> mauve | 0.791 | No |

**ece rev: 0/4**

## Comparison with Parent (seed=42)

| Metric | seed=42 | seed=43 | Match? |
|--------|---------|---------|--------|
| consensus_ge4 | 8/8 | 8/8 | YES |
| permg_fwd_fdr | 8/8 | 8/8 | YES |
| permg_rev_fdr | 3/8 | 0/8 | s43 stronger |
| threshold_onset | 8/8 | 8/8 | YES |
| token_entropy rev | 0/4 | 0/4 | YES |
| gen0 token_entropy | 2.956 | 2.956 | identical |
| gen10 token_entropy | 1.256 | 1.275 | ~1.5% diff |
| gen0 perplexity | 20.6 | 20.6 | identical |
| gen10 perplexity | 1682.6 | 1591.0 | ~5.4% diff |

**Key difference**: s43 permg_rev = 0/8 vs s42's 3/8. In s42 the 3 reverse-significant pairs came from ECE -> diversity (ece->d1/d2/d3). In s43 these are all non-significant after FDR correction, indicating even stronger unidirectionality.

## Conclusion: SUCCESS

seed=43 fully replicates the seed=42 findings:
1. consensus_ge4 = 8/8 (all pairs confirmed)
2. token_entropy perfect unidirectionality (rev=0/4)
3. Drift magnitudes highly consistent across seeds
4. permg_rev = 0/8 is actually stronger than parent's 3/8, confirming domain robustness is not a single-seed artifact
