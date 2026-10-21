# 5-Method Lead-Lag Analysis: alpha=0.75, seed=43

## Experiment Config
- Model: Pythia-410M, Data: WikiText-103 5k subset
- alpha=0.75, seed=43, T=11 generations (gen_0..gen_10)
- Canaries: token_entropy, ece
- Downstreams: distinct_1, distinct_2, distinct_3, perplexity
- Permutation Granger: 5000 permutations, BH FDR q=0.05

## s43 Results Summary

| Metric | Value |
|--------|-------|
| Perm Granger FDR forward sig | 5/8 |
| Perm Granger FDR reverse sig | 0/8 |
| Diff xcorr FDR forward sig | 8/8 |
| Threshold onset forward sig | 4/8 |
| TY Granger forward sig | 1/8 (not used as evidence per C003) |
| Robust pairs (consensus >= 3/5) | 6/8 |

## Forward Perm Granger (FDR-corrected)

| Pair | F-stat | fdr_p | Significant |
|------|--------|-------|-------------|
| token_entropy -> distinct_1 | 365.40 | 0.0555 | |
| token_entropy -> distinct_2 | 420.43 | 0.0218 | * |
| token_entropy -> distinct_3 | 765.76 | 0.0176 | * |
| token_entropy -> perplexity | 25.96 | 0.0704 | |
| ece -> distinct_1 | 235.06 | 0.0188 | * |
| ece -> distinct_2 | 174.70 | 0.0188 | * |
| ece -> distinct_3 | 217.58 | 0.0176 | * |
| ece -> perplexity | 29.80 | 0.0501 | |

## Consensus (forward, methods agreeing)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 3/5 | naive, diff, threshold |
| token_entropy -> distinct_2 | 4/5 | naive, diff, threshold, perm |
| token_entropy -> distinct_3 | 4/5 | naive, diff, threshold, perm |
| token_entropy -> perplexity | 3/5 | naive, diff, threshold |
| ece -> distinct_1 | 2/5 | diff, perm |
| ece -> distinct_2 | 3/5 | naive, diff, perm |
| ece -> distinct_3 | 4/5 | naive, diff, perm, ty |
| ece -> perplexity | 2/5 | naive, diff |

## Key Observations (s43)
- ECE is the stronger canary for Granger causality (3/4 sig vs 2/4 for entropy)
- token_entropy excels at threshold onset (all 4 lead by 1 gen) but borderline on Granger
- Perfect directionality: 0/8 reverse directions significant
- Diff xcorr universally significant (8/8) but less discriminative

---

## Cross-Seed Comparison (alpha=0.75: s42, s43, s44)

All 3 seeds re-analyzed with identical pipeline (same code, same parameters).

### Per-Seed Summary

| Metric | s42 | s43 | s44 |
|--------|-----|-----|-----|
| Perm Granger FDR fwd | 8/8 | 5/8 | 6/8 |
| Perm Granger FDR rev | 0/8 | 0/8 | 0/8 |
| Robust pairs (>=3/5) | 5/8 | 6/8 | 5/8 |
| Threshold fwd sig | 4/8 | 4/8 | 4/8 |
| TY fwd sig | 1/8 | 1/8 | 1/8 |

### Perm Granger FDR: Cross-Seed Consistency

| Pair | s42 fdr_p | s42 | s43 fdr_p | s43 | s44 fdr_p | s44 | All 3 sig |
|------|-----------|-----|-----------|-----|-----------|-----|-----------|
| token_entropy -> d1 | 0.0141 | * | 0.0555 | | 0.0483 | * | |
| token_entropy -> d2 | 0.0115 | * | 0.0218 | * | 0.0630 | | |
| token_entropy -> d3 | 0.0115 | * | 0.0176 | * | 0.0601 | | |
| token_entropy -> ppl | 0.0190 | * | 0.0704 | | 0.0364 | * | |
| ece -> d1 | 0.0115 | * | 0.0188 | * | 0.0364 | * | YES |
| ece -> d2 | 0.0115 | * | 0.0188 | * | 0.0364 | * | YES |
| ece -> d3 | 0.0115 | * | 0.0176 | * | 0.0406 | * | YES |
| ece -> ppl | 0.0176 | * | 0.0501 | | 0.0364 | * | |

**3/8 pairs consistently significant across all 3 seeds (ece -> d1, d2, d3).**

### Consensus >= 3/5: Cross-Seed Consistency

| Pair | s42 | s43 | s44 | All 3 robust |
|------|-----|-----|-----|--------------|
| token_entropy -> d1 | 4/5 | 3/5 | 3/5 | YES |
| token_entropy -> d2 | 4/5 | 4/5 | 2/5 | |
| token_entropy -> d3 | 5/5 | 4/5 | 2/5 | |
| token_entropy -> ppl | 4/5 | 3/5 | 3/5 | YES |
| ece -> d1 | 2/5 | 2/5 | 3/5 | |
| ece -> d2 | 2/5 | 3/5 | 4/5 | |
| ece -> d3 | 2/5 | 4/5 | 3/5 | |
| ece -> ppl | 3/5 | 2/5 | 2/5 | |

**2/8 pairs robust across all 3 seeds (token_entropy -> d1, token_entropy -> ppl).**

## Cross-Seed Takeaways

1. **Directionality is perfectly stable**: 0/8 reverse sig across all 3 seeds -- the causal direction canary->downstream is robust
2. **ECE -> diversity metrics (d1/d2/d3)** is the most reproducible Granger signal (3/3 seeds FDR sig)
3. **token_entropy -> d1/perplexity** is the most reproducible multi-method consensus signal
4. **Threshold onset is perfectly stable**: 4/8 across all 3 seeds (all token_entropy pairs lead by 1 gen)
5. **Marginal pairs** (fdr_p near 0.05) flip across seeds -- expected with T=11 and BH correction
6. Note: s42 previously reported as "3/8 FDR sig" was from an older pipeline version; re-run with identical code gives 8/8

## Data Paths
- s42: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/analysis/5method_leadlag.json
- s43: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/analysis/5method_leadlag.json
- s44: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/analysis/5method_leadlag.json