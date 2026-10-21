# Binary Reward Experiment — Final Analysis

**Experiment**: Binary reward (penalty=0) with GRPO, logging credit agreement and sign-episode correlation
**Data**: `/root/autodl-tmp/binary_credit_adv_log.jsonl` (600 records, 3 iterations × 200 windows)
**Date**: 2026-05-23

## Data Summary

- Total records: 600
- Iterations completed: 3
- Unique (uid, episode) groups: 81
- Groups with at least one success: 18 (22.2%)
- All-fail groups: 63 (77.8%)

## Per-Iteration Results

### Iteration 1
- UIDs: [0, 1, 2, 3, 4, 8, 9]
- Unique episodes: 49, with success: 12
- Sign-episode correlation: **100.0%** (157/157 non-zero windows)
- Credit agreement: **28.0%** (44/157 non-zero windows)
- Zero-advantage ratio: 21.5% (43/200)

Success episodes: 13, 16, 17, 20, 22, 25, 27, 28, 29, 32, 34, 37

### Iteration 2
- UIDs: [0, 1, 2, 3, 4, 7, 8, 9, 14, 15]
- Unique episodes: 56, with success: **0**
- Sign-episode correlation: N/A (all zero-advantage)
- Credit agreement: N/A (all zero-advantage)
- Zero-advantage ratio: **100.0%** (200/200)

**Confirmed**: Iteration 2 is entirely all-fail groups → all advantages = 0 → completely uninformative for training.

### Iteration 3
- UIDs: [0, 1, 2, 3, 6, 7, 8, 14, 15]
- Unique episodes: 53, with success: 11
- Sign-episode correlation: **99.1%** (113/114 non-zero windows)
- Credit agreement: **28.1%** (32/114 non-zero windows)
- Zero-advantage ratio: 43.0% (86/200)

**1 mismatch**: Episode 19 (uid=2) — return=1.29 (success) but advantage=-0.0022. Cause: GRPO within-group normalization. This group contained ep 16 (return 6.98–7.74), ep 17 (return 8.15), making ep 19's low return below the group mean, yielding negative advantage despite being objectively successful.

## Aggregate Results

| Metric | Value |
|--------|-------|
| Overall sign-episode correlation | **99.6%** (270/271 non-zero windows) |
| Overall credit agreement | **28.0%** (76/271 non-zero windows) |
| Overall zero-advantage ratio | **54.8%** (329/600) |
| Positive-adv windows with valid action | 76.7% (46/60) |
| Negative-adv windows with invalid action | 14.2% (30/211) |

### Zero-gradient breakdown
| Iteration | Zero-advantage | Ratio |
|-----------|---------------|-------|
| 1 | 43/200 | 21.5% |
| 2 | 200/200 | 100.0% |
| 3 | 86/200 | 43.0% |

## Key Findings

1. **Sign-episode correlation is near-perfect (99.6%)**: Binary reward advantage sign tracks episode-level success/failure almost exactly. The single exception is caused by GRPO's within-group normalization — a low-return success got negative advantage in a group dominated by high-return successes.

2. **Credit agreement is poor (28.0%)**: Advantage sign does NOT align with per-action validity. The asymmetry is stark:
   - In success episodes (positive adv), 76.7% of windows had valid actions — reasonable.
   - In fail episodes (negative adv), only 14.2% had invalid actions — **85.8% of penalized windows contained valid actions**. Binary reward punishes good actions simply because they co-occurred with a failure elsewhere in the trajectory.

3. **Massive gradient waste (54.8% zero-advantage)**: Over half of all windows receive zero gradient signal. Iteration 2 is entirely wasted (100% zero). This confirms that binary reward with GRPO is extremely sample-inefficient — when a group has no variance in outcomes (all-fail), no learning signal is produced.

4. **The credit assignment problem is quantified**: Binary reward creates a ~72% misattribution rate among informative windows. Actions in failed episodes receive uniform negative advantage regardless of their individual validity, and this dominates (211/271 = 77.9% of non-zero windows are negative-advantage).

## Implications for Paper

These results directly support the paper's core claim: binary reward suffers from poor credit assignment at the action level. The 99.6% sign-episode correlation confirms that GRPO correctly identifies which episodes succeed/fail, but the 28.0% credit agreement shows it cannot distinguish which *actions within* those episodes deserve credit or blame. This gap motivates the cost-based verification reward that provides per-action feedback.
