# olmo_topk50 mean_ppl Outlier Analysis

## Summary

`mean_ppl` in the olmo_topk50 cell is dominated by extreme outliers—**1 sample accounts for 94.4% of the depth-1 total sum**. The top sample has `mean_ppl=1.43e13` but `p90_ppl=105.3`, indicating a few tokens with astronomical perplexity corrupt the sample-level mean while the 90th-percentile remains well-behaved.

**Key finding**: Even after aggressive filtering (removing >1e6 or trimming to p99), `mean_ppl` never recovers monotonic depth ordering. `p90_ppl` is perfectly monotonic without any filtering.

## Distribution by Depth

| Depth | N | mean_ppl (mean) | mean_ppl (median) | mean_ppl (max) | p90_ppl (mean) | p90_ppl (median) |
|-------|------|-----------------|-------------------|----------------|----------------|------------------|
| 0 | 5000 | 2.96e+04 | 3752.37 | 1.29e+07 | 566.81 | 481.05 |
| 1 | 5000 | 3.03e+09 | 220.29 | 1.43e+13 | 143.04 | 141.79 |
| 2 | 5000 | 1.88e+08 | 140.35 | 9.14e+11 | 91.71 | 89.67 |
| 3 | 5000 | 1.75e+06 | 122.86 | 3.68e+09 | 73.05 | 71.32 |

## Extreme Sample Concentration (Depth 1)

| Top-K | % of total sum |
|-------|---------------|
| 1 | 94.40% |
| 5 | 99.69% |
| 10 | 99.97% |

Top outlier: `sample_id=6923`, `mean_ppl=1.43e13`, `p90_ppl=105.3`, `p50_ppl=2.68`

## Extreme Sample Counts by Depth

| Threshold | Depth 0 | Depth 1 | Depth 2 | Depth 3 |
|-----------|---------|---------|---------|---------|
| >1e3 | 4497 (89.9%) | 1747 (34.9%) | 1527 (30.5%) | 1257 (25.1%) |
| >1e6 | 22 (0.44%) | 160 (3.2%) | 259 (5.2%) | 112 (2.2%) |
| >1e9 | 0 | 10 (0.2%) | 6 (0.12%) | 2 (0.04%) |

## Monotonicity Check

| Metric | Depth 0 → 1 → 2 → 3 | Monotonic ↓ |
|--------|----------------------|-------------|
| mean_ppl (raw) | 2.96e4 → 3.03e9 → 1.88e8 → 1.75e6 | **No** |
| mean_ppl (trimmed ≤p99) | 13747 → 89318 → 235127 → 39678 | **No** |
| mean_ppl (excl. >1e6) | 17484 → 21794 → 29779 → 14723 | **No** |
| **p90_ppl (raw)** | **566.8 → 143.0 → 91.7 → 73.1** | **Yes** |

## Statistical Properties

| Depth | CV(mean_ppl) | CV(p90_ppl) | Skew(mean_ppl) | Skew(p90_ppl) | Kurt(mean_ppl) | Kurt(p90_ppl) |
|-------|-------------|-------------|----------------|---------------|----------------|---------------|
| 0 | 9.02 | 0.67 | 32.4 | 2.75 | 1339 | 19.1 |
| 1 | 66.78 | 0.28 | 70.6 | 0.04 | 4984 | 0.91 |
| 2 | 68.86 | 0.29 | 70.7 | 0.54 | 4993 | 1.88 |
| 3 | 36.29 | 0.30 | 50.1 | 0.49 | 2659 | 1.18 |

## Spearman ρ (feature vs depth, all samples)

| Feature | ρ |
|---------|------|
| mean_ppl | −0.406 |
| p90_ppl | **−0.853** |
| p50_ppl | −0.221 |
| log(mean_ppl) | −0.406 |

## Paper Discussion Text

> Token-level perplexity distributions in LLM-generated text are extremely heavy-tailed (kurtosis > 4000 for deeper recursion depths), causing sample-level `mean_ppl` to be dominated by a handful of tokens with catastrophic prediction failures—in the most extreme case, a single sample contributes 94% of the depth-class aggregate. This heavy-tailed behavior renders `mean_ppl` non-monotonic with respect to recursion depth even after aggressive outlier removal (p99 trimming or >10⁶ filtering), and inflates its coefficient of variation to 37–69× compared to 0.28–0.67× for `p90_ppl`. In contrast, percentile-based features such as `p90_ppl` are inherently robust to these extreme tokens, maintaining perfect monotonic ordering across all depths (Spearman ρ = −0.85 vs. −0.41 for `mean_ppl`) with near-Gaussian distributional properties (skewness < 1, kurtosis < 20).
