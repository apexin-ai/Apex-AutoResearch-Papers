# Cross-Alpha Analysis v4 — Execution Ready

## Script
- **Server:** westd-19828
- **Path:** `/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py`
- **Status:** Deployed, syntax verified, imports OK

## Alpha Directories (5 points)

| Alpha | Key  | Path | Seeds | Mode |
|-------|------|------|-------|------|
| 0.00  | a000 | `results/alpha_sweep/a000_s42/` | [42] | single-seed, method agreement only |
| 0.25  | a025 | `results/alpha_sweep/a025_s42/` | [42] | single-seed, method agreement only |
| 0.50  | a050 | `results/alpha_sweep/a050_s42/` | [42] | single-seed, method agreement only |
| 0.75  | a075 | `results/alpha_sweep/a075_s42/` | [42] | single-seed, method agreement only |
| 1.00  | a100 | `results/mvp/rep_42/` (+rep_43/44/45) | [42,43,44,45] | full consensus via method_ablation.json |

## Execution Command

```bash
ssh westd-19828
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/distrib_canary_collapse

# Full run (all 5 alphas, consensus + Granger, ~15-20 min)
python3 cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry

# Quick test without consensus (skip 5-method classification)
python3 cross_alpha_analysis_v4.py --no-consensus --n-perms 5000
```

## Expected Output

- **JSON:** `results/analysis/cross_alpha_v{N}.json`
- **Markdown:** `results/analysis/cross_alpha_v{N}_report.md`

## v4 New Features (vs v3)

1. **α=1.0 integration:** Auto-discovers MVP rep_42..45 as α=1.0; loads seed=42 for Granger/xcorr, all 4 seeds for consensus
2. **Per-α consensus classification:** Runs 5 methods (naive_pearson, differenced_xcorr, threshold_onset, toda_yamamoto, permutation_granger) on all 16 canary→downstream pairs at each α. Single-seed α points use seed_threshold=1 (method agreement only). α=1.0 loads existing method_ablation.json (4 seeds, full consensus with seed_threshold=3)
3. **Regime comparison:** Cross-α stability matrix showing which pairs change robust/non-robust classification — direct evidence of regime-dependent validity
4. **Markdown report:** Human-readable report alongside JSON

## Prerequisites

- a075_s42 must be complete (check `results/alpha_sweep/a075_s42/all_metrics.json` exists)
- Dependencies already installed: numpy, scipy, statsmodels
- Sibling scripts required: `method_ablation.py`, `consensus_framework.py`, `permutation_granger.py`
