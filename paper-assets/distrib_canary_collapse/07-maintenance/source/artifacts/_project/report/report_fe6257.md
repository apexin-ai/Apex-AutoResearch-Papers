# Tail-Sensitive Canary Analysis Report

**Date**: 2026-05-20
**Data**: westd-17855, α ∈ {0.00, 0.10, 0.25, 0.50}, seed=42, fp32

## Method

PermG (5000 permutations, BH FDR q=0.05) on:
- **Canaries**: effective_rank, token_entropy, TTR (type-token ratio), hapax_legomena_ratio
- **Downstreams**: distinct_1, distinct_2, distinct_3, mauve
- TTR = unique_tokens / total_tokens per generation (whitespace tokenized, 5000 samples)
- hapax_ratio = hapax_legomena / unique_tokens

## Results: FDR-Significant Pairs

| Canary | α=0.00 | α=0.10 | α=0.25 | α=0.50 |
|--------|--------|--------|--------|--------|
| effective_rank | 0/4 | 0/4 | **2/4** | 0/4 |
| token_entropy | 0/4 | 0/4 | 1/4 | **1/4** |
| ttr | N/A | 0/4 | 0/4 | 0/4 |
| hapax_ratio | N/A | 0/4 | 0/4 | 0/4 |

effective_rank achieves the earliest FDR detection (α=0.25: distinct_1 p_FDR=0.029, distinct_2 p_FDR=0.029).

## Key Finding: effective_rank at α=0.10 (Blind Zone)

### Raw p-values vs null baseline

| Downstream | α=0.00 (null) | α=0.10 | Separation |
|------------|---------------|--------|------------|
| distinct_1 | 0.0704 | **0.0066** | 10.7× |
| distinct_2 | 0.1348 | **0.0124** | 10.9× |
| distinct_3 | 0.3473 | **0.0206** | 16.9× |
| mauve | 0.1118 | 0.1674 | — |

All three distinct metrics show raw p < 0.05 at α=0.10, with 10–17× separation from the null baseline. FDR-adjusted p-values cluster at 0.0816 (just above 0.05).

### Comparison with token_entropy at α=0.10

| Downstream | effective_rank p_raw | token_entropy p_raw | Advantage |
|------------|---------------------|---------------------|-----------|
| distinct_1 | **0.0066** | 0.0230 | 3.5× |
| distinct_2 | **0.0124** | 0.0306 | 2.5× |
| distinct_3 | **0.0206** | 0.0556 | 2.7× |
| mauve | 0.1674 | 0.5687 | — |

effective_rank is **2.5–3.5× more sensitive** than token_entropy for distinct metrics at α=0.10.

### Why FDR fails

16 tests (4 canaries × 4 downstreams) at T=11 creates severe multiplicity burden. If pre-registered to a single pair (effective_rank → distinct_1), Bonferroni-corrected p = 0.0066 × 4 = 0.026 < 0.05.

## TTR and hapax_ratio

- **TTR**: Weak across all α. No pair reaches raw p < 0.05 for distinct metrics. Minor signal for TTR → mauve (p=0.083 at α=0.10).
- **hapax_ratio**: Complementary sensitivity — detects mauve rather than distinct metrics. At α=0.10, hapax → mauve p=0.026 (raw), p_FDR=0.082. Otherwise weak.
- Neither TTR nor hapax_ratio is more sensitive than effective_rank for the primary distinct downstream targets.

## Blind Zone Assessment

| Scenario | Blind zone |
|----------|-----------|
| Previous (token_entropy only, FDR) | [0, 0.45] |
| effective_rank, full FDR (16 tests) | [0, 0.25) — FDR-sig at 0.25 |
| effective_rank → distinct_1, pre-registered | [0, 0.10) — raw p=0.007 at 0.10, but single-test |
| Suggestive (raw p < 0.05 + 10× null separation) | [0, 0.10) is penetrated but not confirmed |

**Conservative claim**: effective_rank shrinks the confirmed blind zone from [0, 0.45] to **[0, 0.25)** (FDR-significant).

**Suggestive claim**: effective_rank shows signal at α=0.10 (raw p=0.007, 10× null separation) that would survive pre-registered single-pair testing. The blind zone may be as small as **[0, 0.10)**, pending multi-seed confirmation.

## Raw Data: α=0.10 All Pairs

| Canary | Downstream | F-stat | p_raw | p_FDR | f² |
|--------|-----------|--------|-------|-------|-----|
| effective_rank | distinct_1 | 9.680 | 0.0066 | 0.0816 | 1.61 |
| effective_rank | distinct_2 | 8.371 | 0.0124 | 0.0816 | 1.40 |
| effective_rank | distinct_3 | 7.213 | 0.0206 | 0.0816 | 1.20 |
| effective_rank | mauve | 2.409 | 0.1674 | 0.2232 | 0.40 |
| token_entropy | distinct_1 | 423.023 | 0.0230 | 0.0816 | 70.50 |
| token_entropy | distinct_2 | 175.991 | 0.0306 | 0.0816 | 29.33 |
| token_entropy | distinct_3 | 60.054 | 0.0556 | 0.1271 | 10.01 |
| token_entropy | mauve | 0.323 | 0.5687 | 0.6499 | 0.05 |
| ttr | distinct_1 | 1.859 | 0.1260 | 0.1955 | 0.31 |
| ttr | distinct_2 | 1.214 | 0.1344 | 0.1955 | 0.20 |
| ttr | distinct_3 | 0.027 | 0.8186 | 0.8186 | 0.00 |
| ttr | mauve | 5.109 | 0.0832 | 0.1664 | 0.85 |
| hapax_ratio | distinct_1 | 2.316 | 0.1144 | 0.1955 | 0.39 |
| hapax_ratio | distinct_2 | 0.674 | 0.3199 | 0.3938 | 0.11 |
| hapax_ratio | distinct_3 | 0.047 | 0.7882 | 0.8186 | 0.01 |
| hapax_ratio | mauve | 8.692 | 0.0256 | 0.0816 | 1.45 |

## Recommendations

1. **effective_rank should be added to the standard canary set** — it is the most sensitive indicator at low α and reaches FDR significance earliest (α=0.25 vs 0.50 for token_entropy).
2. **Multi-seed validation needed at α=0.10** — the suggestive signal (p=0.007) with strong null separation warrants confirmation across seeds 43/44/45.
3. **hapax_ratio provides complementary mauve sensitivity** — consider as supplementary canary for generation diversity monitoring.
4. **TTR is dominated by effective_rank** — no advantage detected; drop from candidate list.
