# OPT-1.3B WikiText-103 s43 fp32 Analysis Report

**Experiment**: opt13b_wiki_a100_s43_fp32
**Model**: facebook/opt-1.3b | **Dataset**: WikiText-103 | **Alpha**: 1.0 | **Seed**: 43 | **Precision**: fp32
**Server**: westd-19828 | **Date**: 2026-05-20
**Generations**: 11 (gen_0 to gen_10) | **EXIT_CODE**: 0

---

## Summary

| Metric | s43 | s42 (ref) |
|--------|-----|-----------|
| PermG fwd (BH FDR) | **6/8** | 6/8 |
| K>=3 (3sigma) | **6/8** | 6/8 |
| K>=4 (3sigma) | **4/8** | 2/8 |
| D111 direction OK | **8/8** | — |

**Conclusion**: s43 cross-seed replication **successful**. PermG and K>=3 exactly match s42. K>=4 is stronger (4/8 vs 2/8), driven by TY significance on ECE pairs.

---

## Per-Pair Results

| Pair | PermG p_raw | PermG p_FDR | FDR sig | xcorr lag | D111 | 3sigma lead | K |
|------|-------------|-------------|---------|-----------|------|-------------|---|
| token_entropy->distinct_1 | 0.0010 | 0.0022 | YES | -1 | OK | N/A | 3/5 |
| token_entropy->distinct_2 | 0.0014 | 0.0022 | YES | -1 | OK | N/A | 3/5 |
| token_entropy->distinct_3 | 0.0024 | 0.0032 | YES | -1 | OK | N/A | 4/5 |
| token_entropy->mauve | 0.1008 | 0.1152 | no | -4 | OK | N/A | 1/5 |
| ece->distinct_1 | 0.0014 | 0.0022 | YES | -2 | OK | N/A | 4/5 |
| ece->distinct_2 | 0.0004 | 0.0016 | YES | -1 | OK | N/A | 4/5 |
| ece->distinct_3 | 0.0004 | 0.0016 | YES | -1 | OK | N/A | 4/5 |
| ece->mauve | 0.1204 | 0.1204 | no | -4 | OK | N/A | 2/5 |

**Note on D111 direction**: In this implementation, negative xcorr lag = canary leads downstream. All 8 pairs show canary leading. PermG fwd/rev ratio confirms: fwd p-values are orders of magnitude lower than rev (e.g., token_entropy->distinct_1: fwd p=0.001, rev p=0.95).

**Note on threshold 3sigma**: All pairs show downstream_onset=None (downstream metrics degrade smoothly without crossing 3sigma threshold). This is consistent with s42 behavior — 3sigma onset is too conservative for gradual degradation patterns.

---

## Method Breakdown Per Pair

### Significant pairs (6/8 PermG FDR)

| Pair | Naive | DiffXcorr | Thresh3sigma | TY | PermG | K |
|------|-------|-----------|--------------|-----|-------|---|
| entropy->d1 | YES | YES | no | no | YES | 3/5 |
| entropy->d2 | YES | YES | no | no | YES | 3/5 |
| entropy->d3 | YES | YES | no | YES | YES | 4/5 |
| ece->d1 | YES | YES | no | YES | YES | 4/5 |
| ece->d2 | YES | YES | no | YES | YES | 4/5 |
| ece->d3 | YES | YES | no | YES | YES | 4/5 |

### Non-significant pairs (2/8)

| Pair | Naive | DiffXcorr | Thresh3sigma | TY | PermG | K |
|------|-------|-----------|--------------|-----|-------|---|
| entropy->mauve | YES | no | no | no | no | 1/5 |
| ece->mauve | YES | no | no | YES | no | 2/5 |

Mauve pairs are consistently non-significant across both seeds — mauve is too noisy at T=11 for lead-lag detection.

---

## Cross-Seed Consistency (s42 vs s43)

- **Same 6 pairs significant** in PermG FDR for both seeds (all distinct_1/2/3 pairs)
- **Same 2 pairs non-significant** (both mauve pairs)
- K>=4 improvement in s43 (4/8 vs 2/8) comes from TY detecting ECE->distinct pairs (TY d_max=0 for ECE pairs in s43, giving more df_resid)
- Direction consistency: all pairs show canary leading in both analyses

---

## Raw Metrics Trajectory

| Gen | token_entropy | ece | distinct_1 | distinct_2 | distinct_3 | mauve | ppl |
|-----|--------------|-----|------------|------------|------------|-------|-----|
| 0 | 3.048 | 0.020 | 0.101 | 0.521 | 0.816 | 0.031 | 24.9 |
| 1 | 1.833 | 0.197 | 0.102 | 0.522 | 0.816 | 0.030 | 39.1 |
| 2 | 1.396 | 0.316 | 0.086 | 0.439 | 0.717 | 0.033 | 104.4 |
| 3 | 1.243 | 0.356 | 0.082 | 0.408 | 0.670 | 0.034 | 179.5 |
| 4 | 1.155 | 0.380 | 0.081 | 0.401 | 0.657 | 0.034 | 260.8 |
| 5 | 1.124 | 0.394 | 0.081 | 0.401 | 0.656 | 0.031 | 331.9 |
| 6 | 1.103 | 0.405 | 0.081 | 0.400 | 0.655 | 0.031 | 398.2 |
| 7 | 1.104 | 0.408 | 0.081 | 0.398 | 0.652 | 0.031 | 443.1 |
| 8 | 1.110 | 0.412 | 0.080 | 0.397 | 0.651 | 0.030 | 495.1 |
| 9 | 1.120 | 0.417 | 0.080 | 0.397 | 0.650 | 0.030 | 562.0 |
| 10 | 1.104 | 0.423 | 0.080 | 0.397 | 0.649 | 0.032 | 603.1 |

Clear model collapse pattern: entropy drops sharply (3.05->1.10), ECE rises (0.02->0.42), diversity decreases, perplexity explodes (25->603).

---

## Analysis Config
- D079: fp32 (OPT-1.3B <= 3B)
- D086: per-alpha BH FDR, n_perm=5000
- D102: 8-pair (entropy/ECE x d1/d2/d3/mauve)
- D105: global true 3sigma
- D106: PermG fwd primary metric
- D111: direction checking applied (all pass)
