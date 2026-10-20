# n=500 Analysis Pipeline — Ready

## Script
`/root/autodl-tmp/pacs/analyze_n500_unified.py` on westd-22162

## Usage
```bash
# Full analysis (all models, all conditions)
/root/miniconda3/bin/python analyze_n500_unified.py

# Single model
/root/miniconda3/bin/python analyze_n500_unified.py --model deepseek
/root/miniconda3/bin/python analyze_n500_unified.py --model qwen

# With CSV + LaTeX output
/root/miniconda3/bin/python analyze_n500_unified.py --csv --latex

# Dry-run on n=50 data
/root/miniconda3/bin/python analyze_n500_unified.py --dry-run
```

## 5 Analyses Covered
1. **Median II** (D054) — median of D = ii_low − ii_high per condition + bootstrap 95% CI
2. **Bootstrap CI** — B=10000, percentile method, seed=42
3. **Cohen's d_z within-importance only** (D059) — imp pairs only; imp-vs-rand gets Wilcoxon + median_diff, no d_z
4. **Per-phase effective n** — n_valid for high/mid/low phases per condition + midphase null counts
5. **Paired gradient test** — Spearman ρ + permutation test (N=5000) on median II across sparsity levels

## Output
- JSON: `analysis_output/n500_unified.json`
- CSV: `analysis_output/n500_unified.csv` (with `--csv`)
- LaTeX: stdout (with `--latex`)

## Change Made (2026-05-14)
- Added Spearman ρ (scipy.stats.spearmanr) to `permutation_monotonicity_test` function

## Data Availability (as of dry-run)
| Model | Completed conditions |
|-------|---------------------|
| DeepSeek | imp_s015, rand_s015, rand_s020 (3/8) |
| Qwen | imp_s015, imp_s020, rand_s015 (3/8) |

Remaining conditions still running. Script handles partial data gracefully — reports "missing data" for unavailable conditions.

## Dry-run Validation (n=50, DeepSeek)
- All 8 conditions loaded
- d_z range: −0.520 to −0.798 (medium effects, within-imp only)
- Spearman ρ = 1.000 (p < 0.001) for both imp and rand dose-response
- Permutation p = 0.085 (n=50 underpowered for this test, expected to improve at n=500)
