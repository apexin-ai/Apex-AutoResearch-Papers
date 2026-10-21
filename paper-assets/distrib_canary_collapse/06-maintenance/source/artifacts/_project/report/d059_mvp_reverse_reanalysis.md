# D059: MVP 4-seed Reverse Reanalysis (D057 Unified Params)

## Parameters
- n_perm = 5000
- max_lag = 1 (Granger)
- significance: raw p < 0.05 (no BH FDR)
- 8 pairs: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, perplexity} reverse direction

## Data Availability

| Seed | α=1.0 per-generation data | Status |
|------|---------------------------|--------|
| 42   | `results/generalize/pythia410m_wiki_a100_s42/all_metrics.json` | Available (T=11) |
| 43   | Cleaned up from server | UNAVAILABLE |
| 44   | Cleaned up from server | UNAVAILABLE |
| 45   | Cleaned up from server | UNAVAILABLE |

Only seed 42 has full per-generation time-series data. Seeds 43-45 mvp_v4 experiments completed (registry DONE) but output directories were removed. Only summary gen0/gen10 metrics survive in registry.

## Seed 42 Results (D057 Unified Params)

### Reverse direction (downstream -> canary)

| Pair (reverse) | F-stat | p-value | Significant |
|---|---|---|---|
| distinct_1 -> token_entropy | 0.4907 | 0.4921 | No |
| distinct_2 -> token_entropy | 0.4953 | 0.4805 | No |
| distinct_3 -> token_entropy | 0.4193 | 0.5047 | No |
| perplexity -> token_entropy | 0.0014 | 0.9658 | No |
| distinct_1 -> ece | 59.6706 | **0.0274** | **Yes** |
| distinct_2 -> ece | 37.5922 | **0.0286** | **Yes** |
| distinct_3 -> ece | 25.2940 | **0.0306** | **Yes** |
| perplexity -> ece | 6.9095 | 0.1418 | No |

### Forward direction (canary -> downstream) for comparison

| Pair (forward) | F-stat | p-value | Significant |
|---|---|---|---|
| token_entropy -> distinct_1 | 2853.51 | **0.0002** | **Yes** |
| token_entropy -> distinct_2 | 1582.09 | **0.0012** | **Yes** |
| token_entropy -> distinct_3 | 999.51 | **0.0012** | **Yes** |
| token_entropy -> perplexity | 0.69 | 0.5841 | No |
| ece -> distinct_1 | 7088.63 | **0.0002** | **Yes** |
| ece -> distinct_2 | 1311.70 | **0.0006** | **Yes** |
| ece -> distinct_3 | 791.38 | **0.0006** | **Yes** |
| ece -> perplexity | 0.09 | 0.8040 | No |

### Seed 42 Summary
- token_entropy reverse: **0/4**
- ECE reverse: **3/4** (d1, d2, d3 all significant; ppl not)
- Total reverse: **3/8**
- Forward: **6/8** (all diversity pairs; perplexity pairs not significant in either direction)

## Seeds 43-45: Cannot Reanalyze

Per-generation data (gen_0 through gen_10 metrics) for seeds 43-45 at α=1.0 no longer exists on the server. The mvp_v4_rep43/44/45 experiments completed, but only summary drift metrics survive in the registry. Time-series data needed for Granger analysis is lost.

## Explanation of Old "0/24" Claim

The old Case Study "0/24 reverse significant" came from:
- **3 seeds** (42, 43, 44) per `run_mvp.sh` (not 4 seeds)
- **8 pairs** per seed: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, mauve}
- **Old params**: n_perm=1000, BH FDR correction
- 3 x 8 = 24 total tests

For seed 42, the old analysis found ece←d1/d2/d3 raw p ≈ 0.032-0.036, but BH FDR correction (8 tests) pushed them above 0.05. Hence 0/8 per seed, 0/24 total.

## Why Numbers Changed

| Factor | Old analysis | D057 unified |
|---|---|---|
| n_perm | 1000 | 5000 |
| 4th downstream | mauve | perplexity |
| Multiple testing | BH FDR (8 tests) | raw p < 0.05 |
| Seed 42 reverse result | 0/8 (FDR) | **3/8** (raw) |

The discrepancy is driven entirely by **FDR correction removal**. With n_perm=5000, the ece←diversity raw p-values are 0.027-0.031 (borderline). Under BH FDR with 8 tests, the threshold for rank 3-4 is 0.019-0.025, so these get rejected. Without FDR, they pass at 0.05.

## Recommended Paper Numbers

**Option A (conservative, only seed 42 available):**
> "Under unified parameters (n_perm=5000, max_lag=1, raw p<0.05), the Baseline configuration shows 3/8 reverse-significant pairs in seed 42, all involving ECE as the response variable (p=0.027-0.031). Token entropy shows no reverse causality (0/4, all p>0.48). Seeds 43-45 could not be reanalyzed due to data unavailability."

**Option B (if we only report what we can verify):**
- Table 7 Baseline PG_rev = 3/8 (seed 42 only)
- Case study should NOT claim "0/24" or "0/32" since:
  1. The old "0/24" used different params (FDR, n_perm=1000, mauve)
  2. Seeds 43-45 cannot be verified with D057 params

**Key interpretive point:** The 3/8 reverse significance is exclusively ECE←diversity. Token entropy shows clean unidirectionality (0/4 reverse, 3/4 forward for diversity). The ECE bidirectionality may reflect genuine feedback (diversity decline affects calibration) rather than spurious signal, since the forward F-statistics (791-7089) are 13-119x larger than reverse F-statistics (25-60).
