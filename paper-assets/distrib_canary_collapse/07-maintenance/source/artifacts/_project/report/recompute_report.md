# Pythia-1.4B True 3σ Recompute — D105+D111 Joint

## Task
Recompute threshold_onset and K values for Pythia-1.4B × WikiText × α=1.0 (s42, s43) using D105 true 3σ standard with D111 direction check applied jointly.

## Method
- **D105**: threshold_onset uses `base + 3*std(series)` (true 3σ), not `3x_sigma_drift` amplitude check
- **D086**: per-method BH FDR, n_perm=5000
- **M035**: direction filter `peak_lag < 0` = forward (canary leads downstream)
- **D102**: 8-pair config: canary=[token_entropy, ece] × downstream=[distinct_1, distinct_2, distinct_3, mauve]
- **D111**: direction check on naive_xcorr and diff_xcorr

## Results

### generalize_pythia14b_wiki_a100_s42

| Metric | Pre-D105 | D105+D111 |
|--------|----------|-----------|
| threshold_onset | 8/8 | **0/8** |
| naive_xcorr | 8/8 (raw) | **6/8** (D111: ece→d2, ece→d3 lag=+3) |
| diff_xcorr | 7/8 (FDR) | **6/8** (D111: ece→mauve lag=+4) |
| perm_granger_fwd | 2/8 | 2/8 (unchanged) |
| ty_granger | 0/8 | 0/8 (unchanged) |
| **K≥3** | 3/8 | **1/8** (ece→d1 only) |
| **K≥4** | 2/8 | **0/8** |

Per-pair K breakdown:
- K=3: ece→d1 (naive + diff + permG)
- K=2: te→d1, te→d2, te→d3, ece→d2 (naive/diff only)
- K=1: te→mauve, ece→d3, ece→mauve
- K=0: none

### generalize_pythia14b_wiki_a100_s43

| Metric | Pre-D105 | D105+D111 |
|--------|----------|-----------|
| threshold_onset | 8/8 | **0/8** |
| naive_xcorr | 8/8 (raw) | **0/8** (D111: all peak_lag > 0) |
| diff_xcorr | 8/8 (FDR) | **6/8** (D111: te→mauve lag=+5, ece→mauve lag=+5) |
| perm_granger_fwd | 6/8 | 6/8 (unchanged) |
| ty_granger | 4/8 (raw) | **3/8** (FDR: ece→d1/d2/d3) |
| **K≥3** | 7/8 | **3/8** (ece→d1/d2/d3) |
| **K≥4** | 5/8 | **0/8** |

Per-pair K breakdown:
- K=3: ece→d1, ece→d2, ece→d3 (diff + permG + TY)
- K=2: te→d1, te→d2, te→d3 (diff + permG)
- K=0: te→mauve, ece→mauve

## Key Observations

1. **threshold_onset collapses to 0/8** in both seeds — downstream metrics never cross the true 3σ threshold. This is consistent with all other experiments in the D105 backfill (c4_a075, pythia1b, GPT-2M, etc. all show threshold_onset_3sigma ≤ 2/8).

2. **Cross-seed divergence persists**: s42 K≥3=1/8 vs s43 K≥3=3/8. The PermG asymmetry (2/8 vs 6/8) is the main driver.

3. **ECE pairs stronger than entropy pairs**: In s43, all surviving K≥3 pairs are ECE-canary, carried by diff_xcorr + perm_granger + TY_granger (FDR).

4. **Naive xcorr direction is seed-sensitive**: s42 has 6/8 forward (lag<0) but s43 has 0/8 forward (all lag>0). This is the largest D111 impact.

## Data Sources
- Server: westd-19828
- s42 dir: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/`
- s43 dir: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/`
- Joint results saved to: `analysis/d105_d111_joint_3sigma.json` in each experiment directory
