# TY Granger Direction Bug Fix — T=20 Re-run Results

**Date**: 2026-05-20
**Script**: `run_5method_analysis_d102.py` on westd-17855
**Fix**: Line 223: `test_causality(causing=1, caused=0)` → `test_causality(causing=0, caused=1)`

## Bug Description

In `ty_granger()`, data is `np.column_stack([x, y])` where x=canary (col 0), y=downstream (col 1).
The old code `causing=1, caused=0` tested "does downstream cause canary" (reverse direction) but labeled it as forward.
Fix: `causing=0, caused=1` = "does canary cause downstream" (correct forward direction).

## Synthetic Data Validation

```
Forward (X→Y): stat=859.2224, p=0.000000  ← significant (correct)
Reverse (Y→X): stat=0.4382,  p=0.803261  ← not significant (correct)
```

Confirms `causing=0, caused=1` correctly detects the known causal direction.

## Summary Comparison (pre-fix → post-fix)

| Experiment | TY fwd | TY rev | K≥3 | PermG | DiffXcorr | Onset |
|---|---|---|---|---|---|---|
| **a050_s42** | 4→2 | 2→4 | 6→6 | 6→6 | 6→6 | 6→6 |
| **a060_s42** | 3→5 | 5→3 | 3→4 | 0→0 | 6→6 | 6→6 |
| **a100_s42** | 1→2 | 2→1 | 6→6 | 6→6 | 6→6 | 6→6 |

**Key observations**:
- TY forward and reverse counts are exactly swapped — confirms the bug was a pure direction reversal
- Non-TY methods (PermG, DiffXcorr, Onset, NaiveXcorr) are completely unchanged — no regression
- a060: K≥3 improved 3→4 because TY now correctly identifies 3 additional token_entropy→distinct_* pairs

## Per-Pair TY Forward Detail (pre → post)

### a050_s42_fp32 (α=0.50, T=20)

| Pair | pre p | post p | pre sig | post sig | Change |
|---|---|---|---|---|---|
| token_entropy→distinct_1 | 0.4497 | 0.1383 | F | F | |
| token_entropy→distinct_2 | 0.7761 | 0.0227 | F | **T** | ← new |
| token_entropy→distinct_3 | 0.7428 | 0.0629 | F | F | |
| token_entropy→mauve | 0.3541 | 0.4031 | F | F | |
| ece→distinct_1 | 0.0226 | 0.0034 | T | T | |
| ece→distinct_2 | 0.0014 | 0.5537 | **T** | F | ← lost |
| ece→distinct_3 | 0.0004 | 0.1528 | **T** | F | ← lost |
| ece→mauve | 0.0013 | 0.0841 | **T** | F | ← lost |

Net: 4→2 (lost 3 ece pairs, gained 1 token_entropy pair)

### a060_s42_fp32 (α=0.60, T=20)

| Pair | pre p | post p | pre sig | post sig | Change |
|---|---|---|---|---|---|
| token_entropy→distinct_1 | 0.3968 | 0.0428 | F | **T** | ← new |
| token_entropy→distinct_2 | 0.3595 | 0.0000 | F | **T** | ← new |
| token_entropy→distinct_3 | 0.3781 | 0.0000 | F | **T** | ← new |
| token_entropy→mauve | 0.4252 | 0.0142 | F | **T** | ← new |
| ece→distinct_1 | 0.6641 | 0.2346 | F | F | |
| ece→distinct_2 | 0.0000 | 0.4652 | **T** | F | ← lost |
| ece→distinct_3 | 0.0000 | 0.4777 | **T** | F | ← lost |
| ece→mauve | 0.0073 | 0.0301 | T | T | |

Net: 3→5 (gained 4 token_entropy pairs, lost 2 ece pairs)

### a100_s42_fp32 (α=1.00, T=20)

| Pair | pre p | post p | pre sig | post sig | Change |
|---|---|---|---|---|---|
| token_entropy→distinct_1 | 0.6501 | 0.1598 | F | F | |
| token_entropy→distinct_2 | 0.5782 | 0.9513 | F | F | |
| token_entropy→distinct_3 | 0.5608 | 0.1944 | F | F | |
| token_entropy→mauve | 0.7470 | 0.5726 | F | F | |
| ece→distinct_1 | 0.0464 | 0.0066 | T | T | |
| ece→distinct_2 | 0.0550 | 0.0221 | F | **T** | ← new |
| ece→distinct_3 | 0.0637 | 0.0525 | F | F | |
| ece→mauve | 0.6903 | 0.2521 | F | F | |

Net: 1→2 (gained 1 ece pair)

## Consensus (K≥3) Change Detail

| Experiment | Pair | pre K | post K | Change reason |
|---|---|---|---|---|
| a050 | token_entropy→distinct_2 | 3 | 4 | +ty |
| a050 | ece→distinct_2 | 4 | 3 | -ty |
| a050 | ece→distinct_3 | 4 | 3 | -ty |
| a050 | ece→mauve | 2 | 1 | -ty |
| a060 | token_entropy→distinct_1 | 2 | 3 | +ty |
| a060 | token_entropy→distinct_2 | 2 | 3 | +ty |
| a060 | token_entropy→distinct_3 | 2 | 3 | +ty |
| a060 | token_entropy→mauve | 0 | 1 | +ty |
| a060 | ece→distinct_2 | 3 | 2 | -ty |
| a060 | ece→distinct_3 | 3 | 2 | -ty |
| a100 | ece→distinct_2 | 4 | 5 | +ty |

## Data Locations

- Pre-fix backups: `westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/t20/{exp}/analysis/5method_leadlag_pre_tyfix.json`
- Post-fix results: `westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/t20/{exp}/analysis/5method_leadlag.json`
- Local compact JSONs: `artifacts/t20_tyfix_v2/{exp}/5method_summary_tyfix.json`
