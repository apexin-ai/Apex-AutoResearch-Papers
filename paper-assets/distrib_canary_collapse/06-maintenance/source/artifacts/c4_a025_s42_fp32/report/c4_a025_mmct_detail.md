# C4 α=0.25 MMCT Detail Analysis

Experiment: `c4_a025_s42_fp32` | T=11 generations | n_perm=5000 | BH FDR per-method | 3σ threshold

## Per-pair PermG p-values

| pair | PermG_fwd_raw | PermG_fwd_fdr | fwd_sig_raw | fwd_sig_fdr | PermG_rev_raw | PermG_rev_fdr | rev_sig_raw | F_fwd |
|------|--------------|--------------|-------------|-------------|--------------|--------------|-------------|-------|
| entropy→d1 | 0.0934 | 0.0942 | No | No | 0.2102 | 0.2496 | No | 10.98 |
| entropy→d2 | 0.0942 | 0.0942 | No | No | 0.2168 | 0.2496 | No | 9.33 |
| entropy→d3 | 0.0596 | 0.0942 | No | No | 0.2184 | 0.2496 | No | 13.00 |
| **entropy→mauve** | **0.0406** | **0.0942** | **Yes** | **No** | 0.9990 | 0.9990 | No | **14.95** |
| ece→d1 | 0.0840 | 0.0942 | No | No | 0.1578 | 0.2496 | No | 10.77 |
| ece→d2 | 0.0858 | 0.0942 | No | No | 0.1502 | 0.2496 | No | 8.95 |
| ece→d3 | 0.0554 | 0.0942 | No | No | 0.1420 | 0.2496 | No | 12.44 |
| **ece→mauve** | **0.0306** | **0.0942** | **Yes** | **No** | **0.0284** | 0.2272 | **Yes** | **17.91** |

**FDR note**: All 8 pairs' FDR-corrected p-values collapse to 0.0942 (= min(raw_p × 8/rank, 1) under BH). The two mauve pairs are raw-significant (p<0.05) but FDR kills them. ece→mauve has the lowest raw p (0.031) and highest F-stat (17.91) of all 8 pairs.

**Bidirectionality flag**: ece→mauve has raw-significant reverse (p=0.028). This weakens the causal directionality — both directions show non-random Granger structure, possibly reflecting shared driver rather than canary→downstream causation.

## Per-pair TY Granger

| pair | TY_p | TY_chi2 | d_max | df_resid | sig |
|------|------|---------|-------|----------|-----|
| entropy→d1 | 0.6675 | 0.18 | 0 | 7 | No |
| entropy→d2 | 0.0978 | 2.74 | 0 | 7 | No |
| **entropy→mauve** | **<0.0001** | **37.79** | **0** | **7** | **Yes** |
| entropy→d3 | 0.6518 | 0.20 | 2 | 1 | No |
| **ece→d1** | **0.0008** | **11.36** | **1** | **4** | **Yes** |
| **ece→d2** | **0.0001** | **14.68** | **1** | **4** | **Yes** |
| ece→d3 | 0.1437 | 2.14 | 2 | 1 | No |
| ece→mauve | 0.8391 | 0.04 | 1 | 4 | No |

TY significant: 3/8. Note d_max instability: d3 pairs have d_max=2 → df_resid=1, severely underpowered (C003 constraint applies for low-α TY).

## Per-pair cross-correlation & threshold onset

| pair | naive_lag | naive_r | naive_p | diff_lag | diff_r | diff_p_fdr | thresh_onset_c | thresh_onset_d | lead_time |
|------|-----------|---------|---------|----------|--------|------------|----------------|----------------|-----------|
| entropy→d1 | -2 | -0.945 | 0.0001 | -3 | -0.962 | 0.002 | 1 | None | 10 |
| entropy→d2 | 1 | 0.770 | 0.009 | -3 | -0.883 | 0.014 | 1 | 2 | 1 |
| entropy→d3 | 3 | 0.921 | 0.001 | -1 | 0.774 | 0.016 | 1 | 2 | 1 |
| entropy→mauve | -1 | 0.903 | 0.0003 | -1 | 0.796 | 0.014 | 1 | 3 | 2 |
| ece→d1 | -2 | -0.942 | 0.0001 | -3 | -0.962 | 0.002 | 1 | None | 10 |
| ece→d2 | 0 | 0.782 | 0.004 | -3 | -0.891 | 0.014 | 1 | 2 | 1 |
| ece→d3 | 2 | 0.894 | 0.001 | -1 | 0.744 | 0.022 | 1 | 2 | 1 |
| ece→mauve | -1 | 0.894 | 0.0005 | -1 | 0.797 | 0.014 | 1 | 3 | 2 |

All 8 pairs: naive sig=8/8, diff sig_fdr=8/8, threshold sig=8/8.

Note: d1 pairs have onset_d=None → lead_time=10 (downstream never crosses 3σ threshold, canary crossed at gen 1). This is because d1 drift is only -4.1% — it never breaches any reasonable threshold.

## Per-pair method votes (K values)

| pair | naive | diff | threshold | permG_fwd | TY | K |
|------|-------|------|-----------|-----------|-----|---|
| entropy→d1 | Y | Y | Y | N | N | 3 |
| entropy→d2 | Y | Y | Y | N | N | 3 |
| entropy→d3 | Y | Y | Y | N | N | 3 |
| **entropy→mauve** | **Y** | **Y** | **Y** | **N** | **Y** | **4** |
| **ece→d1** | **Y** | **Y** | **Y** | **N** | **Y** | **4** |
| **ece→d2** | **Y** | **Y** | **Y** | **N** | **Y** | **4** |
| ece→d3 | Y | Y | Y | N | N | 3 |
| ece→mauve | Y | Y | Y | N | N | 3 |

**K≥3: 8/8** — all from {naive, diff, threshold}. These three correlation/onset methods always agree because they detect co-movement, not Granger causality.

**K≥4: 3/8** — the extra vote always comes from TY, never PermG. The 3 K=4 pairs: entropy→mauve (TY chi2=37.8), ece→d1 (TY chi2=11.4), ece→d2 (TY chi2=14.7).

**K≥5: 0/8** — PermG (FDR) and TY never co-occur on the same pair. Where PermG is closest to significant (mauve pairs), TY is split (entropy→mauve TY=sig, ece→mauve TY=not sig).

## C4 vs WikiText α=0.25 collapse comparison

| metric | C4 α=0.25 | WikiText α=0.25 (s42) | ratio |
|--------|-----------|----------------------|-------|
| **Canary** | | | |
| token_entropy drift | **-53.0%** | -4.8% | 11× larger in C4 |
| ECE drift | +3243% | +79% | 41× larger in C4 |
| perplexity drift | **+3617%** | -18.1% | opposite sign |
| **Downstream** | | | |
| distinct_1 drift | -4.1% | **-39.2%** | 10× larger in Wiki |
| distinct_2 drift | -8.8% | **-54.8%** | 6× larger in Wiki |
| distinct_3 drift | -12.0% | **-57.0%** | 5× larger in Wiki |
| mauve drift | **-52.1%** | -41.9% | comparable |
| **Lead-lag** | | | |
| PermG fwd | 0/8 | 0/8 | same |
| K≥4 | 3/8 | 0/8 | C4 slightly higher |
| K≥3 | 8/8 | varies by seed | |
| TY sig | 3/8 | 3/8 | same |

### Why C4 diversity barely drops while canary collapses massively

The C4/WikiText α=0.25 asymmetry reveals two distinct collapse modes:

1. **C4 mode — "calibration collapse"**: The model's internal confidence (entropy, ECE, ppl) degrades catastrophically, but generated text diversity (d1/d2/d3) is barely affected. Perplexity explodes +3617% while d1 drops only -4.1%. The model produces diverse text it is extremely uncertain about.

2. **WikiText mode — "diversity collapse"**: The model maintains relatively stable calibration (entropy -4.8%, ppl -18%) but loses text diversity severely (d1 -39%, d3 -57%). The model confidently produces repetitive text.

**Why does this split the lead-lag signal?**
- In WikiText mode, downstream metrics (d1/d2/d3) have large drift → good SNR for temporal methods, but canary drift is small → no temporal signal to detect as "leading"
- In C4 mode, canary metrics drift enormously but downstream (d1/d2/d3) barely move → xcorr finds correlation in noise, Granger finds no predictive improvement over baseline because downstream variance is trivially small
- **mauve is the bridge**: it degrades substantially in both modes (C4: -52%, Wiki: -42%), making canary→mauve the most promising causal channel

### Why PermG=0/8 despite mauve pairs being raw-significant

Two factors:
1. **FDR penalty**: With 8 pairs, BH correction inflates the best raw p (0.031) to 0.094, just above α=0.05. If tested as a single pair, ece→mauve would pass at p=0.031.
2. **ece→mauve bidirectionality**: The reverse direction (p_rev=0.028) is also raw-significant, meaning the Granger test detects temporal structure in both directions. This suggests a shared latent driver (the α=0.25 distributional shift) affecting both ece and mauve simultaneously, rather than ece causally leading mauve.

## Key findings

1. **canary→mauve is the strongest channel at C4 α=0.25**: Both mauve pairs have raw-significant PermG fwd (p=0.031, 0.041) — the closest any pair gets to FDR significance. The entropy→mauve TY test is highly significant (chi2=37.8, p<0.0001).

2. **FDR is the bottleneck, not effect size**: The F-statistics are substantial (14.9–17.9 for mauve pairs). A single-pair PermG test would pass. The 8-pair FDR correction absorbs all signal.

3. **d1/d2/d3 are noise-dominated**: With drift of only -4% to -12%, these downstream metrics lack sufficient temporal variation for Granger tests. The threshold onset method assigns lead_time=10 (=max) for d1 pairs because d1 never crosses the 3σ threshold.

4. **C4 α=0.25 exhibits "calibration collapse without diversity collapse"** — the opposite of WikiText α=0.25's "diversity collapse without calibration collapse". This suggests the canary→downstream pathway depends on dataset properties, not just α.

5. **K≥3 consensus is uninformative here**: All 8 pairs get K=3 from the same three methods (naive/diff/threshold), which all detect co-movement rather than directionality. The 3 K=4 pairs add only a single TY vote. Without PermG support, K=3 consensus does not establish Granger-causal lead-lag.

6. **ece→mauve bidirectionality** (fwd p=0.031, rev p=0.028) is a red flag for causal interpretation — both directions are equally non-random, consistent with a common cause rather than ece→mauve causation.
