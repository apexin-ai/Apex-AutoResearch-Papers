# Per-alpha BH FDR Reanalysis (D086 Modification 2)

## Summary

Recalculated Table 7 significance counts using **per-alpha BH FDR** (q=0.05) instead of per-experiment BH FDR. Per-alpha BH pools all raw p-values within the same alpha level across seeds/experiments before applying Benjamini-Hochberg correction.

**n_perm = 5000** (confirmed across all 21 experiments on westd-19828 + westd-17855).

## Data Sources

| Server | Files | Experiments |
|--------|-------|-------------|
| westd-19828 | 19 | a000_s42/s43/s44, a025_s43/s44, a050_s42/s43/s44, a060_s42_bf16, a075_s42/s43/s44, + 7 generalize |
| westd-17855 | 2 | a010_s43_bf16, gpt2m_wiki_a100_s43_bf16 |

Total: 1648 rows (21 experiments x 8 pairs x 2 directions x ~5 methods).

Note: a025_s42_v3 does not have a 5method_leadlag.json file.

## Method Notes

- **threshold_onset**: No p-value (deterministic method). Significance kept as-is under both FDR schemes.
- **ty_granger**: Some experiments have None p-values (e.g., gpt2m_wiki_a100_s43_bf16). Excluded from BH when p=None.
- **BH grouping**: Per (alpha, direction, method). E.g., for perm_granger forward at alpha=0.50: 3 seeds x 8 pairs = 24 p-values pooled for BH.

## Per-experiment vs Per-alpha BH FDR Comparison (Forward Only)

Format: per_exp / per_alpha (out of 8 pairs)

| alpha | exp_name | seed | naive | diff | thres | perm | ty | total |
|-------|----------|------|-------|------|-------|------|----|-------|
| 0.00 | a000_s42 | 42 | 8/8 | 4/4 | 3/3 | 0/0 | 1/0 | 16/15 |
| 0.00 | a000_s43 | 43 | 7/7 | 3/3 | 1/1 | 0/0 | 1/0 | 12/11 |
| 0.00 | a000_s44 | 44 | 8/8 | 3/3 | 1/1 | 0/0 | 0/0 | 12/12 |
| 0.10 | a010_s43_bf16 | 43 | 7/7 | 8/8 | 3/3 | 0/0 | 0/0 | 18/18 |
| 0.25 | a025_s43 | 43 | 8/8 | 3/3 | 0/0 | 0/0 | 0/0 | 11/11 |
| 0.25 | a025_s44 | 44 | 8/8 | 1/1 | 0/0 | 0/0 | 2/1 | 11/10 |
| 0.50 | a050_s42 | 42 | 8/8 | 8/8 | 0/0 | 0/0 | 0/0 | 16/16 |
| 0.50 | a050_s43 | 43 | 8/8 | 6/6 | 0/0 | **6/1** | 0/0 | 20/15 |
| 0.50 | a050_s44 | 44 | 8/8 | 6/6 | 0/0 | **3/1** | 0/0 | 17/15 |
| 0.60 | a060_s42_bf16 | 42 | 8/8 | 8/8 | 0/0 | 8/8 | 0/0 | 24/24 |
| 0.75 | a075_s42 | 42 | 8/8 | 8/8 | 4/4 | 8/8 | 1/0 | 29/28 |
| 0.75 | a075_s43 | 43 | 8/8 | 8/8 | 0/0 | 5/6 | 1/0 | 22/22 |
| 0.75 | a075_s44 | 44 | 8/8 | 8/8 | 4/4 | 6/6 | 1/0 | 27/26 |
| 1.00 | gpt2m_wiki_a100_s42 | 42 | 8/8 | 8/8 | 0/0 | 6/6 | 2/2 | 24/24 |
| 1.00 | gpt2m_wiki_a100_s43_bf16 | 43 | 8/8 | 7/7 | 8/8 | 1/1 | 0/0 | 24/24 |
| 1.00 | opt1b_wiki_a100_s42 | 42 | 8/8 | 8/8 | 1/1 | 6/6 | 0/0 | 23/23 |
| 1.00 | pythia14b_wiki_a100_s42 | 42 | 7/7 | 6/6 | 0/0 | **2/4** | 0/0 | 15/17 |
| 1.00 | pythia14b_wiki_a100_s43 | 43 | 8/8 | 6/6 | 0/0 | 6/6 | 2/0 | 22/20 |
| 1.00 | pythia1b_c4_a100_s42 | 42 | 8/8 | 6/6 | 0/0 | 6/6 | 1/0 | 21/20 |
| 1.00 | pythia1b_c4_a100_s43 | 43 | 8/8 | 6/6 | 0/0 | 4/4 | 2/1 | 20/19 |
| 1.00 | pythia410m_wiki_a100_s42 | 42 | 8/8 | 8/8 | 0/0 | 6/6 | 2/0 | 24/22 |

## Table 7 (Per-alpha BH FDR): Aggregated Mean Forward Sig/8

| alpha | n_exps | naive | diff | thres | perm | ty |
|-------|--------|-------|------|-------|------|----|
| 0.00 | 3 | 7.67 | 3.33 | 1.67 | 0.00 | **0.00** |
| 0.10 | 1 | 7.00 | 8.00 | 3.00 | 0.00 | 0.00 |
| 0.25 | 2 | 8.00 | 2.00 | 0.00 | 0.00 | **0.50** |
| 0.50 | 3 | 8.00 | 6.67 | 0.00 | **0.67** | 0.00 |
| 0.60 | 1 | 8.00 | 8.00 | 0.00 | 8.00 | 0.00 |
| 0.75 | 3 | 8.00 | 8.00 | 2.67 | **6.67** | **0.00** |
| 1.00 | 8 | 7.88 | 6.88 | 1.12 | **4.88** | **0.38** |

### vs Per-experiment BH FDR (delta):

| alpha | naive | diff | thres | perm | ty |
|-------|-------|------|-------|------|----|
| 0.00 | 0 | 0 | 0 | 0 | **-0.67** |
| 0.10 | 0 | 0 | 0 | 0 | 0 |
| 0.25 | 0 | 0 | 0 | 0 | **-0.50** |
| 0.50 | 0 | 0 | 0 | **-2.33** | 0 |
| 0.60 | 0 | 0 | 0 | 0 | 0 |
| 0.75 | 0 | 0 | 0 | **+0.33** | **-1.00** |
| 1.00 | 0 | 0 | 0 | **+0.25** | **-0.75** |

## Key Changes Under Per-alpha BH FDR

### 1. perm_granger at alpha=0.50: Major Drop (-2.33 mean)
- a050_s43: 6/8 -> 1/8 (delta=-5)
- a050_s44: 3/8 -> 1/8 (delta=-2)
- Raw p-values were 0.02-0.06 (borderline). When pooled with a050_s42's non-significant p-values (0.02-0.10), BH thresholds became stricter.
- Only ece->distinct_1 survives in s43 (p=0.0036, adj_p=0.043) and s44 (p=0.002, adj_p=0.043).

### 2. ty_granger: Consistent Small Drops
- alpha=0.00: 0.67 -> 0.00 (a000_s42 and a000_s43 each lose 1)
- alpha=0.25: 1.00 -> 0.50 (a025_s44 loses 1)
- alpha=0.75: 1.00 -> 0.00 (all 3 seeds lose 1 each)
- alpha=1.00: 1.12 -> 0.38 (pythia14b_s43 loses 2, pythia1b_c4_s42 loses 1, pythia1b_c4_s43 loses 1, pythia410m_s42 loses 2)

### 3. perm_granger at alpha=0.75 and 1.00: Small Gains
- alpha=0.75: a075_s43 gains 1 (5->6). Pooling with strongly significant tests from s42/s44 helps borderline cases.
- alpha=1.00: pythia14b_s42 gains 2 (2->4). Same effect from pooling with 7 other strongly significant experiments.

### 4. Unchanged Methods
- **naive_xcorr**: No change at any alpha (p-values generally very small).
- **diff_xcorr**: No change at any alpha.
- **threshold_onset**: No change (no p-value to correct).

## Impact on Dose-Response Narrative

The per-alpha BH FDR **strengthens** the dose-response story for perm_granger:
- alpha=0.50 perm_granger drops from 3.00/8 -> 0.67/8 (much weaker signal)
- alpha=0.75 perm_granger stays at 6.67/8 (strong signal)
- The jump from alpha=0.50 to alpha=0.75 becomes even more dramatic (0.67 -> 6.67 vs previous 3.00 -> 6.33), supporting a threshold effect between moderate and high contamination.

The overall pattern: naive_xcorr and diff_xcorr detect the correlation signal across all alpha levels; perm_granger (causal) shows a clear dose-response that kicks in between alpha=0.50 and alpha=0.60.

## Script Location

- westd-19828: `/root/autodl-tmp/distrib_canary_collapse/per_alpha_fdr.py`
- Full JSON results: `/root/autodl-tmp/distrib_canary_collapse/per_alpha_fdr_results.json`
