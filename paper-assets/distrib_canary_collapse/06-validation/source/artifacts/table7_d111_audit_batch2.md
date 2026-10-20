# D111 Direction Audit — Table 7 Batch 2

**Date**: 2026-05-20
**D111 Rule**: naive_xcorr `peak_lag > 0 AND significant` = forward; diff_xcorr `peak_lag > 0 AND significant_fdr` = forward. `peak_lag = 0` is NOT forward.

## Methodology

- **Peak_lag source**: `5method_leadlag.json` (max_lag=5) for all experiments — D111 was designed for 5-lag xcorr
- **Significance source**: Most complete analysis file per experiment (see per-experiment notes)
- **D111 delta**: Only xcorr methods affected; threshold/permG/TY unchanged from their existing significance

---

## 1. GPT-2m s42

**Server**: westd-19828
**Path**: `results/generalize/gpt2m_wiki_a100_s42/`
**Significance source**: `analysis/gpt2m_8pair_table7.json` (has corrected threshold=8/8, TY=5/8)
**Peak_lag source**: `analysis/5method_leadlag.json` (max_lag=5)

### Per-pair detail

| Pair | naive_sig | naive_lag | D111_naive | diff_fdr | diff_lag | D111_diff | thresh | permG | TY | K_D111 |
|------|-----------|-----------|------------|----------|----------|-----------|--------|-------|-----|--------|
| te→d1 | Y | **-1** | N | Y | **-1** | N | Y | Y | N | **2** |
| te→d2 | Y | **-1** | N | Y | **-2** | N | Y | Y | Y | **3** |
| te→d3 | Y | **-2** | N | Y | **-2** | N | Y | Y | Y | **3** |
| te→mauve | Y | **4** | **Y** | N | -1 | N | Y | N | N | **2** |
| ece→d1 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| ece→d2 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| ece→d3 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| ece→mauve | Y | **4** | **Y** | N | -1 | N | Y | N | N | **2** |

### Summary

| Metric | Registry (old) | D111 (new) | Δ |
|--------|---------------|------------|---|
| PermG | 6/8 | 6/8 | 0 |
| K≥3 | 6/8 | **5/8** | **-1** |
| K≥4 | 2/8 | **0/8** | **-2** |

**Root cause**: ALL 6 distinct-pair diff_xcorr forward peak_lags are negative (-1 or -2). Only mauve pairs have naive peak_lag > 0 (lag=4) but mauve pairs lack permG/TY significance. te→d1 loses both xcorr → drops from K=4 to K=2 (crosses K≥3 boundary).

---

## 2. GPT-2m s43

**Server**: westd-19828
**Path**: `results/gen_wiki_gpt2m_a100_s43/`
**Significance source**: `analysis/5method_leadlag.json` consensus
**Peak_lag source**: same file (max_lag=5)

⚠️ **Note**: This file has `threshold_forward_sig=1` (only ece→mauve). The GPT-2m s42 experiment's corrected threshold analysis shows 8/8 — if a corrected threshold were available for s43, K values would likely increase.

### Per-pair detail

| Pair | naive_sig | naive_lag | D111_naive | diff_fdr | diff_lag | D111_diff | thresh | permG | TY | K_D111 |
|------|-----------|-----------|------------|----------|----------|-----------|--------|-------|-----|--------|
| te→d1 | Y | **-2** | N | Y | **-3** | N | N | Y | N | **1** |
| te→d2 | Y | **-2** | N | Y | **-3** | N | N | Y | Y | **2** |
| te→d3 | Y | **4** | **Y** | Y | **-4** | N | N | Y | Y | **3** |
| te→mauve | ? | **-2** | N | N | **-2** | N | N | N | N | **0** |
| ece→d1 | Y | **-1** | N | Y | **-1** | N | N | Y | N | **1** |
| ece→d2 | Y | **-2** | N | Y | **-2** | N | N | Y | Y | **2** |
| ece→d3 | Y | **-5** | N | Y | **-3** | N | N | Y | Y | **2** |
| ece→mauve | ? | **-2** | N | N | **-2** | N | Y | N | N | **1** |

### Summary

| Metric | Registry (old) | D111 (new) | Δ |
|--------|---------------|------------|---|
| PermG | 6/8 | 6/8 | 0 |
| K≥3 | 6/8 | **1/8** | **-5** |
| K≥4 | 4/8 | **0/8** | **-4** |

**Root cause**: ALL diff_xcorr forward peak_lags are negative (-1 to -4). Only te→d3 naive has peak_lag=4 > 0. Combined with threshold=1/8 (uncorrected), only te→d3 reaches K≥3 via naive_fwd+permG+TY.

---

## 3. OPT-1.3B s42

**Server**: westd-19828
**Path**: `results/generalize/opt1b_wiki_a100_s42/`
**Significance source**: `analysis/opt1b_6method_full.json` (corrected threshold=8/8, TY=2/8)
**Peak_lag source**: `analysis/5method_leadlag.json` (max_lag=5)

⚠️ **Note**: The 6method file used max_lag=1 for its own xcorr. Peak_lags from 5method file (max_lag=5) used for D111 direction check.

### Per-pair detail

| Pair | naive_sig | naive_lag | D111_naive | diff_fdr | diff_lag | D111_diff | thresh | permG | TY | K_D111 |
|------|-----------|-----------|------------|----------|----------|-----------|--------|-------|-----|--------|
| te→d1 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| te→d2 | Y | **-1** | N | Y | **-1** | N | Y | Y | N | **2** |
| te→d3 | Y | **-1** | N | Y | **-1** | N | Y | Y | N | **2** |
| te→mauve | N | -4 | N | N | 3 | N | Y | N | N | **1** |
| ece→d1 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| ece→d2 | Y | **-1** | N | Y | **-1** | N | Y | Y | N | **2** |
| ece→d3 | Y | **3** | **Y** | Y | **-1** | N | Y | Y | N | **3** |
| ece→mauve | N | -4 | N | N | 3 | N | Y | N | N | **1** |

### Summary

| Metric | Registry (old) | D111 (new) | Δ |
|--------|---------------|------------|---|
| PermG | 6/8 | 6/8 | 0 |
| K≥3 | 6/8 | **3/8** | **-3** |
| K≥4 | 2/8 | **0/8** | **-2** |

**Root cause**: ALL distinct-pair diff_xcorr forward peak_lags = -1. Only ece→d3 has naive peak_lag=3 > 0. te→d1 and ece→d1 reach K≥3 via thresh+permG+TY=3. ece→d3 reaches K≥3 via naive_fwd+thresh+permG=3.

---

## 4. Padding-410M s42

**Server**: westd-17855
**Path**: `results/padding_robustness/a100_s42_fp32/`
**Significance source**: `analysis_results.json`
**Peak_lag source**: same file

⚠️ **Note**: This file did NOT check direction for either naive or diff pre-D111 (both were counted as "forward" based on significance alone).

### Per-pair detail

| Pair | naive_sig | naive_lag | D111_naive | diff_fdr | diff_lag | D111_diff | thresh | permG | TY | K_D111 |
|------|-----------|-----------|------------|----------|----------|-----------|--------|-------|-----|--------|
| te→d1 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| te→d2 | Y | **-1** | N | Y | **-1** | N | Y | Y | Y | **3** |
| te→d3 | Y | **-2** | N | Y | **-2** | N | Y | Y | Y | **3** |
| te→mauve | N | -4 | N | N | -5 | N | Y | N | N | **1** |
| ece→d1 | Y | **-2** | N | Y | **-2** | N | Y | Y | Y | **3** |
| ece→d2 | Y | **-3** | N | Y | **-1** | N | Y | Y | Y | **3** |
| ece→d3 | Y | **-3** | N | Y | **-1** | N | Y | Y | Y | **3** |
| ece→mauve | N | -4 | N | N | -5 | N | Y | N | N | **1** |

### Summary

| Metric | Registry (old) | D111 (new) | Δ |
|--------|---------------|------------|---|
| PermG | 6/8 | 6/8 | 0 |
| K≥3 | 6/8 | **6/8** | **0** |
| K≥4 | 6/8 | **0/8** | **-6** |

**Root cause**: ALL 16 peak_lags (8 naive + 8 diff) are negative. The 6 non-mauve pairs drop from K=5 to K=3 (lose naive+diff, keep thresh+permG+TY). K≥3 is preserved but K≥4 collapses entirely.

---

## Grand Summary

| Experiment | PermG | K≥3 old→new | K≥4 old→new |
|-----------|-------|-------------|-------------|
| GPT-2m s42 | 6/8 | 6/8 → **5/8** | 2/8 → **0/8** |
| GPT-2m s43 | 6/8 | 6/8 → **1/8** | 4/8 → **0/8** |
| OPT-1.3B s42 | 6/8 | 6/8 → **3/8** | 2/8 → **0/8** |
| Padding s42 | 6/8 | 6/8 → **6/8** | 6/8 → **0/8** |

### Key findings

1. **K≥4 = 0/8 across ALL experiments** after D111. Every pre-D111 K≥4 entry was inflated by xcorr methods with peak_lag ≤ 0.

2. **diff_xcorr is the main casualty**: across all 32 forward-section diff_xcorr peak_lags (8 pairs × 4 experiments), zero have peak_lag > 0 AND are significant. D111 eliminates diff_xcorr entirely from K computation.

3. **naive_xcorr occasionally survives**: 4 pairs across all experiments retain naive_fwd (GPT-2m s42: te/ece→mauve lag=4; GPT-2m s43: te→d3 lag=4; OPT s42: ece→d3 lag=3).

4. **Padding is most resilient**: K≥3 unchanged (6/8) because 6 non-mauve pairs have thresh+permG+TY=3. The xcorr methods were redundant for K≥3.

5. **GPT-2m s43 most affected**: K≥3 drops from 6/8 to 1/8 because threshold_onset is unreliable (1/8 sig) in the available analysis file. If corrected threshold (as in GPT-2m s42's 8pair analysis) were applied, results might improve.

### Implication for Table 7

The D111 direction audit reveals that pre-D111 xcorr "significance" counted many backward-direction (peak_lag < 0) correlations as evidence of forward canary→downstream causation. Table 7's K≥3 and especially K≥4 columns need correction. PermG remains unchanged (6/8) as it uses its own direction testing.
