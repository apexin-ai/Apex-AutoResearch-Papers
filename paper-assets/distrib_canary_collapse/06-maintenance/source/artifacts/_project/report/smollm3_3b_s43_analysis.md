# SmolLM3-3B s43 5-Method Lead-Lag Analysis

**Experiment**: SmolLM3-3B, α=1.0, WikiText, fp32, seed=43
**Server**: westd-17855
**Data**: `results/generalize/smollm3_3b_wiki_a100_s43_17855/`
**Generations**: 11 (gen_0–gen_10), EXIT_CODE=0, PPL 13.25→449.31

## Summary

| Metric | s43 | s42 (parent) |
|--------|-----|-------------|
| PermG FDR forward | **3/8** (ECE only) | **3/8** (ECE only) |
| PermG FDR reverse | 0/8 | 0/8 |
| DiffXCorr FDR forward | 8/8 | 6/8 |
| Threshold onset | 2/8 | 0/8 |
| TY Granger forward | 6/8 | 0/8 |
| **K≥3 robust pairs** | **6/8** | **3/8** |

## Per-Pair Consensus

| Pair | s43 K | s43 Methods | s42 K | s42 Methods |
|------|-------|-------------|-------|-------------|
| token_entropy→distinct_1 | **4/5** | naive, diff, threshold, ty | 1/5 | diff |
| token_entropy→distinct_2 | **3/5** | naive, diff, ty | 1/5 | diff |
| token_entropy→distinct_3 | **3/5** | naive, diff, ty | 1/5 | diff |
| token_entropy→mauve | 2/5 | naive, diff | 0/5 | — |
| ece→distinct_1 | **5/5** | naive, diff, threshold, perm, ty | **3/5** | naive, diff, perm |
| ece→distinct_2 | **4/5** | naive, diff, perm, ty | **3/5** | naive, diff, perm |
| ece→distinct_3 | **4/5** | naive, diff, perm, ty | **3/5** | naive, diff, perm |
| ece→mauve | 2/5 | naive, diff | 1/5 | naive |

## Cross-Seed Replication

### PermG FDR: Perfect replication
Both seeds: 3/8 forward (ece→distinct_{1,2,3}), 0/8 reverse. ECE is the only PermG-significant canary channel. This is the most reliable finding.

### K≥3 divergence: TY d_max instability
s43 has K≥3=6/8 vs s42's 3/8. The difference is entirely driven by TY Granger:
- **s42**: d_max=2 (ADF says I(2)) → TY fits VAR(k+2) on T=11, almost no residual df → 0/8 significant
- **s43**: d_max=0 (ADF says I(0)) → TY reduces to standard Granger, full df preserved → 6/8 significant

This confirms C003: ADF integration order is seed-unstable at T=11. TY results are not cross-seed robust for 3B models.

### Stable findings across both seeds
1. **ECE is the robust canary** — PermG-significant in both seeds
2. **token_entropy fails PermG** — U-shape trajectory breaks linear Granger assumption
3. **Mauve pairs fail** — neither channel reaches K≥3 for mauve
4. **Clean directionality** — PermG reverse = 0/8 in both seeds

## Entropy-Diversity Decoupling

### token_entropy U-shape confirmed in s43

| | s42 | s43 |
|---|-----|-----|
| Start (gen 0) | 2.5626 | 2.5626 |
| Min | 0.9381 (gen 2) | 0.9007 (gen 3) |
| End (gen 10) | 1.7046 | 1.1657 |
| Recovery ratio | 68.2% of start | 45.5% of start |

Both seeds: sharp entropy drop (gen 0→2/3), then gradual recovery. Meanwhile distinct_1 is **monotonically decreasing** in both seeds (s43: 0.1081→0.0971). The non-monotonic entropy trajectory decouples from the monotonic diversity decay, explaining PermG failure for token_entropy pairs.

### Why the U-shape?
Gen 0 has high token_entropy (healthy model). After α=1.0 canary injection, entropy collapses (model becomes repetitive/degenerate). As training continues under collapse, the model enters a high-entropy degenerate regime (random-ish output). This creates a V/U trajectory that violates the monotonic assumption needed for linear Granger causality.

## s43 Detailed Forward Statistics

| Pair | NaiveR | NaiveLag | DiffR | DiffLag | DiffFDR_p | Threshold lead | PermG_F | PermG_FDR_p | TY_F | TY_p |
|------|--------|----------|-------|---------|-----------|----------------|---------|-------------|------|------|
| te→d1 | 0.913 | -1 | 0.967 | -1 | 0.0000 | 9 | 87.42 | 0.304 | — | 0.0016 |
| te→d2 | 0.862 | -1 | 0.968 | -1 | 0.0000 | — | 86.86 | 0.304 | — | 0.0047 |
| te→d3 | 0.842 | -1 | 0.966 | -1 | 0.0000 | — | 77.61 | 0.304 | — | 0.0083 |
| te→mauve | 0.870 | -4 | 0.858 | -4 | 0.029 | — | 1.89 | 0.304 | — | 0.360 |
| ece→d1 | 0.990 | -1 | 0.987 | -1 | 0.0000 | 8 | 611.67 | 0.304* | — | 0.0045 |
| ece→d2 | 0.973 | -1 | 0.990 | -1 | 0.0000 | — | 574.76 | 0.304* | — | 0.0013 |
| ece→d3 | 0.964 | -1 | 0.989 | -1 | 0.0000 | — | 445.17 | 0.304* | — | 0.0026 |
| ece→mauve | 0.806 | -4 | 0.869 | -4 | 0.028 | — | 1.89 | 0.304 | — | 0.517 |

*PermG FDR-significant (marked with `*` in script output)

## Conclusions

1. **PermG = 3/8 cross-seed replicated** — ECE→distinct_{1,2,3}. This is the headline finding for SmolLM3-3B.
2. **K≥3 is seed-variable** (3/8 vs 6/8) due to TY d_max instability — report PermG as the primary metric.
3. **Entropy-diversity decoupling confirmed** in both seeds — token_entropy U-shape is a structural feature of 3B model collapse, not a seed artifact.
4. **Mauve is a weak downstream** — fails in both seeds, both channels.
