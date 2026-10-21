# Ground Truth Redefinition Analysis (Reviewer C1 Response)

## Motivation

Reviewer concern: circular reasoning in using statistical tests to define ground truth, then evaluating those same tests against it. This analysis replaces the old definition with **purely observational criteria** independent of any statistical test.

## New Ground Truth Criteria

A (canary, downstream) pair is a **reference pair** if:
1. **Drift magnitude ratio**: canary α=1.0 drift ≥ N× canary α=0.0 drift (tested N = 2, 3, 5)
2. **Temporal ordering**: canary 2σ onset ≤ downstream 2σ onset in ≥3/4 seeds

The 2σ onset is defined as the first generation where the α=1.0 trajectory exceeds 2× the maximum fluctuation observed in the α=0.0 (no-contamination) baseline. No statistical test is involved.

## Results

### Drift Magnitudes

| Metric | α=0.0 drift | α=1.0 mean drift | Ratio |
|--------|-------------|-------------------|-------|
| token_entropy | 0.1649 | 1.9663 | **11.93×** |
| ece | 0.0056 | 0.4085 | **73.12×** |
| distinct_1 | 0.0135 | 0.0274 | 2.02× |
| distinct_2 | 0.0506 | 0.1751 | 3.46× |
| distinct_3 | 0.0367 | 0.2465 | 6.72× |
| perplexity | 5.8413 | 989.99 | 169.48× |

### Threshold Crossing Times (2σ onset, generation number)

| Metric | Mean onset | Per-seed |
|--------|-----------|----------|
| token_entropy | **1.0** | 1, 1, 1, 1 |
| ece | **1.0** | 1, 1, 1, 1 |
| distinct_1 | 9.0 | 10, 10, -, 7 |
| distinct_2 | 3.0 | 3, 3, 3, 3 |
| distinct_3 | 3.0 | 3, 3, 3, 3 |
| perplexity | 1.0 | 1, 1, 1, 1 |

Both canaries cross their threshold at **generation 1** (immediate response), while downstream metrics lag (gen 3-10), confirming temporal ordering.

### Reference Pair Set (stable across 2×/3×/5×)

All **8 pairs** qualify at every threshold tested:

| Canary | Downstream | Canary ratio | Down ratio | Temporal |
|--------|-----------|-------------|-----------|----------|
| token_entropy | distinct_1 | 11.93× | 2.02× | 4/4 |
| token_entropy | distinct_2 | 11.93× | 3.46× | 4/4 |
| token_entropy | distinct_3 | 11.93× | 6.72× | 4/4 |
| token_entropy | perplexity | 11.93× | 169.48× | 4/4 |
| ece | distinct_1 | 73.12× | 2.02× | 4/4 |
| ece | distinct_2 | 73.12× | 3.46× | 4/4 |
| ece | distinct_3 | 73.12× | 6.72× | 4/4 |
| ece | perplexity | 73.12× | 169.48× | 4/4 |

**Sensitivity**: The reference set is **completely invariant** to threshold choice (2×/3×/5×) because both canary drift ratios (11.93× and 73.12×) vastly exceed all tested thresholds, and temporal ordering holds unanimously across seeds.

### FNR (K≥3/4 consensus, excluding differenced XCorr)

Consensus methods: naive Pearson, threshold onset, permutation Granger, Toda-Yamamoto.
Detection criterion: ≥3/4 methods significant.

| | Detected | FN | FNR |
|--|---------|-----|-----|
| New definition | 6/8 | 2/8 | **25.0%** |

**Detected (6 pairs):**
- token_entropy → distinct_{1,2,3}
- ece → distinct_{1,2,3}

**False negatives (2 pairs):**
- token_entropy → perplexity (2/4: naive ✓, onset ✓, TY ✗, perm ✗)
- ece → perplexity (2/4: naive ✓, onset ✓, TY ✗, perm ✗)

Both FN pairs fail because TY and permutation Granger are non-significant (0/4 seeds each). This is consistent with constraint C003 (TY unreliable at short T).

### Comparison with Old Definition

| | Old | New |
|--|-----|-----|
| Definition | 5-method consensus ≥3/5 | drift ratio + temporal |
| Reference set size | 4 pairs | **8 pairs** |
| FNR | 0.0% | **25.0%** |
| Circular? | Yes (tests define GT) | **No** |

**Changes:**
- Added: ece→distinct_2, ece→distinct_3, ece→perplexity, token_entropy→perplexity
- Removed: none

The new definition is more inclusive (8 vs 4 pairs) because the old consensus requirement was overly conservative — TY's low power at T=11 excluded pairs with genuine causal structure. The 25% FNR reflects TY/permutation Granger's known limitations on short time series, not flaws in the reference pairs.

## Data sources
- α=1.0: results/mvp/rep_{42,43,44,45}/all_metrics.json
- α=0.0: results/alpha_sweep/a000_s42/all_metrics.json
- Method results: results/mvp/analysis/method_ablation.json
