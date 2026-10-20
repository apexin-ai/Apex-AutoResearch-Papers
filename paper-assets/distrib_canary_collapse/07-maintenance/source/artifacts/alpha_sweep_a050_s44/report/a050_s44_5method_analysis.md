# 5-Method Lead-Lag Analysis: alpha=0.50, seed=44

## Experiment Config
- Model: Pythia-410M, Data: WikiText-103 5k subset
- alpha=0.50, seed=44, T=11 generations (gen_0..gen_10)
- Canaries: token_entropy, ece
- Downstreams: distinct_1, distinct_2, distinct_3, perplexity
- Permutation Granger: 5000 permutations, BH FDR q=0.05

## Per-Method Forward Detection Counts (/8 pairs)

| Method | Sig count |
|--------|-----------|
| Naive XCorr | 4/8 |
| Differenced XCorr (FDR) | 6/8 |
| Threshold Onset | 0/8 |
| Permutation Granger (FDR) | 3/8 |
| Toda-Yamamoto | 0/8 (excluded per C003) |

## Directionality
- Perm Granger forward sig: 3/8
- Perm Granger reverse sig: 0/8

## Forward Perm Granger (FDR-corrected)

| Pair | F-stat | fdr_p | Significant |
|------|--------|-------|-------------|
| token_entropy -> distinct_1 | 115.204 | 0.0862 | |
| token_entropy -> distinct_2 | 98.398 | 0.0862 | |
| token_entropy -> distinct_3 | 70.627 | 0.0862 | |
| token_entropy -> perplexity | 14.747 | 0.0862 | |
| ece -> distinct_1 | 216.476 | 0.0160 | * |
| ece -> distinct_2 | 95.914 | 0.0408 | * |
| ece -> distinct_3 | 50.072 | 0.0536 | |
| ece -> perplexity | 19.893 | 0.0475 | * |

## Consensus (forward, methods agreeing)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy -> distinct_1 | 2/5 | naive, diff |
| token_entropy -> distinct_2 | 1/5 | naive |
| token_entropy -> distinct_3 | 1/5 | naive |
| token_entropy -> perplexity | 2/5 | naive, diff |
| ece -> distinct_1 | 2/5 | diff, perm |
| ece -> distinct_2 | 2/5 | diff, perm |
| ece -> distinct_3 | 1/5 | diff |
| ece -> perplexity | 2/5 | diff, perm |

- **Robust pairs (consensus >= 3/5): 0/8**
- **Robust pairs (consensus >= 4/5): 0/8**

## Key Observations (s44)
- ECE is the only canary with Perm Granger FDR significance (3/4 ece pairs vs 0/4 entropy pairs)
- All token_entropy Perm Granger fdr_p collapsed to identical 0.0862 after BH correction
- Threshold onset detected zero pairs (no canary crossed 3x sigma drift threshold)
- TY Granger uniformly non-significant (dmax=2 across all pairs, df_resid=1)
- Perfect directionality: 0/8 reverse sig

---

## Cross-Seed Comparison (alpha=0.50: s42, s43, s44)

### Per-Seed Summary

| Metric | s42 | s43 | s44 |
|--------|-----|-----|-----|
| Perm Granger FDR fwd | 0/8 | 6/8 | 3/8 |
| Perm Granger FDR rev | 0/8 | 0/8 | 0/8 |
| Diff XCorr FDR fwd | 8/8 | 6/8 | 6/8 |
| Threshold fwd sig | 0/8 | 0/8 | 0/8 |
| TY fwd sig | 0/8 | 0/8 | 0/8 |
| Robust pairs (>=3/5) | 0/8 | 1/8 | 0/8 |

### Perm Granger FDR: Cross-Seed Consistency

| Pair | s42 fdr_p | s42 | s43 fdr_p | s43 | s44 fdr_p | s44 | All 3 sig |
|------|-----------|-----|-----------|-----|-----------|-----|-----------|
| token_entropy -> d1 | 0.0974 | | 0.0421 | * | 0.0862 | | |
| token_entropy -> d2 | 0.0974 | | 0.0551 | | 0.0862 | | |
| token_entropy -> d3 | 0.0974 | | 0.0421 | * | 0.0862 | | |
| token_entropy -> ppl | 0.0974 | | 0.0632 | | 0.0862 | | |
| ece -> d1 | 0.0852 | | 0.0288 | * | 0.0160 | * | |
| ece -> d2 | 0.0852 | | 0.0421 | * | 0.0408 | * | |
| ece -> d3 | 0.0852 | | 0.0421 | * | 0.0536 | | |
| ece -> ppl | 0.0852 | | 0.0421 | * | 0.0475 | * | |

**0/8 pairs consistently significant across all 3 seeds.**

### Consensus >= 3/5: Cross-Seed Consistency

| Pair | s42 | s43 | s44 | All 3 robust |
|------|-----|-----|-----|--------------|
| token_entropy -> d1 | 2/5 | 3/5 | 2/5 | |
| token_entropy -> d2 | 2/5 | 2/5 | 1/5 | |
| token_entropy -> d3 | 2/5 | 2/5 | 1/5 | |
| token_entropy -> ppl | 2/5 | 2/5 | 2/5 | |
| ece -> d1 | 1/5 | 2/5 | 2/5 | |
| ece -> d2 | 1/5 | 2/5 | 2/5 | |
| ece -> d3 | 1/5 | 1/5 | 1/5 | |
| ece -> ppl | 1/5 | 2/5 | 2/5 | |

**0/8 pairs robust across all 3 seeds.**

## Cross-Seed Takeaways

1. **Directionality is perfectly stable**: 0/8 reverse sig across all 3 seeds
2. **alpha=0.50 is at the detection boundary**: Perm Granger ranges from 0/8 (s42) to 6/8 (s43), highly seed-dependent
3. **ECE is consistently the stronger canary**: when any pairs are significant, they are always ece pairs (s43: 4/4 ece sig; s44: 3/4 ece sig)
4. **token_entropy Perm Granger is unreliable at alpha=0.50**: only s43 shows 2/4 sig, s42 and s44 both 0/4
5. **Threshold onset uniformly fails at alpha=0.50**: 0/8 across all 3 seeds (compared to 4/8 at alpha=0.75)
6. **Diff xcorr remains broadly significant** (6-8/8) but is the least discriminative method

## Data Paths
- s42: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/analysis/5method_leadlag.json
- s43: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/analysis/5method_leadlag.json
- s44: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44/analysis/5method_leadlag.json
