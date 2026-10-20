# n=500 Analysis Pipeline Audit Report

Generated: 2026-05-14

## 1. Data Output Path Mapping

Base: `/root/autodl-tmp/pacs/`
Each condition outputs to: `profiling_output_n500_bf16_{model}_{masking}_{sparsity}/profiling_results.json`

### DeepSeek (GPU 0: importance, GPU 1: random)

| Condition | Output Dir | Status (as of 05:39 UTC) |
|-----------|-----------|---------|
| ds_imp_s015 | `profiling_output_n500_bf16_ds_imp_s015` | DONE |
| ds_imp_s020 | `profiling_output_n500_bf16_ds_imp_s020` | RUNNING (dir exists, no results yet) |
| ds_imp_s025 | `profiling_output_n500_bf16_ds_imp_s025` | QUEUED |
| ds_imp_s030 | `profiling_output_n500_bf16_ds_imp_s030` | QUEUED |
| ds_rand_s015 | `profiling_output_n500_bf16_ds_rand_s015` | DONE |
| ds_rand_s020 | `profiling_output_n500_bf16_ds_rand_s020` | RUNNING (dir exists, no results yet) |
| ds_rand_s025 | `profiling_output_n500_bf16_ds_rand_s025` | QUEUED |
| ds_rand_s030 | `profiling_output_n500_bf16_ds_rand_s030` | QUEUED |

### Qwen (GPU 2: importance, GPU 3: random)

| Condition | Output Dir | Status (as of 05:39 UTC) |
|-----------|-----------|---------|
| qw_imp_s015 | `profiling_output_n500_bf16_qw_imp_s015` | DONE |
| qw_imp_s020 | `profiling_output_n500_bf16_qw_imp_s020` | RUNNING (dir exists, no results yet) |
| qw_imp_s025 | `profiling_output_n500_bf16_qw_imp_s025` | QUEUED |
| qw_imp_s030 | `profiling_output_n500_bf16_qw_imp_s030` | QUEUED |
| qw_rand_s015 | `profiling_output_n500_bf16_qw_rand_s015` | DONE |
| qw_rand_s020 | `profiling_output_n500_bf16_qw_rand_s020` | RUNNING (dir exists, no results yet) |
| qw_rand_s025 | `profiling_output_n500_bf16_qw_rand_s025` | QUEUED |
| qw_rand_s030 | `profiling_output_n500_bf16_qw_rand_s030` | QUEUED |

Progress: 4/16 done, 4/16 running, 8/16 queued. Each GPU runs 4 conditions sequentially.

Completion sentinel: `check_completion.sh` creates `DONE_DEEPSEEK`, `DONE_QWEN`, `DONE_ALL_N500` files.

## 2. Analysis Scripts Audit

Three candidate scripts exist. Audited against hard constraints:
- D054: median-only (no mean as primary)
- D059: d_z only within-importance
- D031/D033: difference not ratio
- Bootstrap B=10000 for Cohen's d CI, B=1000 for profiling CI

### Script A: `analyze_c2_n500.py` — NEAR-READY (best candidate)

| Constraint | Status | Detail |
|-----------|--------|--------|
| D054 median-only | PASS (with caveat) | Median is primary; mean also computed as secondary |
| D059 d_z scope | PASS | Per-condition d_z is phase gradient within each condition; `cohens_d_n500.json` only outputs importance models |
| D031/D033 no ratio | **FAIL** | `format_report()` lines 285-300 compute and display `Imp/Rand ratio` column |
| B=10000 for d_z CI | PASS | `B_BOOTSTRAP = 10000`, `bootstrap_ci_dz()` uses it |
| B=1000 for profiling CI | OVER-BUDGET | Uses B=10000 for median CI too (not wrong, just slower) |
| Output format | PASS | JSON with d_z, d_z_ci, median_diff, median_ci, wilcoxon_p per condition |

**Issues to fix before running:**
1. **Line 285-300**: Remove `Imp/Rand ratio` column from `format_report()`. The ratio is computed as `imp_med / rnd_med` — violates D031/D033 because high-phase II near zero makes ratio meaningless.

### Script B: `analyze_n500.py` — NEEDS FIXES

| Constraint | Status | Detail |
|-----------|--------|--------|
| D054 median-only | PASS | Median primary metric throughout |
| D059 d_z scope | **FAIL** | `within_importance_comparisons()` is called for BOTH `imp` and `rand` masking (main() lines 427-430 iterate `MASKING_TYPES`) |
| D031/D033 no ratio | PASS | No ratio computation |
| B=10000 for d_z CI | **FAIL** | B_BOOTSTRAP=1000; no bootstrap CI for d_z at all (only point estimate) |
| Output format | PARTIAL | Has median, CI, Wilcoxon, d_z point estimate; missing d_z CI |

**Issues to fix:**
1. **Line 39**: Change `B_BOOTSTRAP = 1000` to `B_BOOTSTRAP = 10000` (or add separate B for d_z)
2. **Add `bootstrap_ci_dz()` function** — currently d_z has no CI
3. **Lines 427-430**: Only call `within_importance_comparisons()` for masking="imp", not "rand"

### Script C: `analyze_n500_unified.py` — NEEDS FIXES

| Constraint | Status | Detail |
|-----------|--------|--------|
| D054 median-only | PASS | Docstring explicitly: "NO mean" |
| D059 d_z scope | **FAIL** | Computes `dz_rand` via `compute_within_dz(all_diffs, "rand", ...)` (line 256-259) |
| D031/D033 no ratio | PASS | Uses Spearman + permutation for dose-response |
| B=10000 for d_z CI | **FAIL** | `B_BOOT = 1000` used for `bootstrap_dz_ci()` |
| Output format | GOOD | JSON + optional CSV, median-centric |

**Issues to fix:**
1. **Line 43**: Change `B_BOOT = 1000` to `B_BOOT = 10000` (for d_z CI; profiling CI at 1000 is fine but uses same variable)
2. **Lines 256-259**: Remove `dz_rand` computation, or only compute for importance masking
3. **WITHIN_PAIRS** has 4 pairs (adjacent + extremes) vs 6 in analyze_n500.py (all C(4,2)). Decide which is intended.

## 3. Fix Checklist (do NOT modify yet — read-only audit)

### Priority 1: `analyze_c2_n500.py` (minimal fixes)
- [ ] Remove Imp/Rand ratio from `format_report()` (lines 285-300): delete ratio column header + computation
- [ ] (Optional) Add note that per-condition d_z for random is informational, not for cross-type comparison

### Priority 2: `analyze_n500_unified.py` (if using as secondary)
- [ ] `B_BOOT = 1000` → `10000` (line 43), or split into B_BOOT_MEDIAN=1000 and B_BOOT_DZ=10000
- [ ] Remove `dz_rand` block (lines 256-259) and `"random": dz_rand` from return dict
- [ ] Update docstring "1000 resamples" → "10000 for d_z CI"

### Priority 3: `analyze_n500.py` (if using as secondary)
- [ ] `B_BOOTSTRAP = 1000` → `10000` (line 39)
- [ ] Add `bootstrap_ci_dz()` function (copy from analyze_c2_n500.py)
- [ ] Restrict `within_importance_comparisons` to masking="imp" only (lines 427-430)

## 4. Suggested Run Commands

After all 16 conditions complete (check: `bash check_completion.sh` or `ls DONE_ALL_N500`):

```bash
cd /root/autodl-tmp/pacs
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# PRIMARY: analyze_c2_n500.py (B=10000, has d_z CI)
# *** Fix ratio issue first (Priority 1 above) ***
python analyze_c2_n500.py
# Output: analysis_output/c2_n500_results.json
#         analysis_output/cohens_d_n500.json
#         analysis_output/c2_n500_report.md

# SECONDARY: unified analysis with CSV
# *** Fix B and d_z scope first (Priority 2 above) ***
python analyze_n500_unified.py --model all --csv
# Output: analysis_output/n500_unified.json
#         analysis_output/n500_unified.csv

# TERTIARY: basic per-condition analysis
# *** Fix B, d_z CI, d_z scope first (Priority 3 above) ***
python analyze_n500.py
# Output: analysis_output/n500_analysis.json
#         analysis_output/n500_report.md
```

Partial analysis (single model, e.g., if DeepSeek finishes first):
```bash
python analyze_c2_n500.py  # will report MISSING for incomplete conditions
python analyze_n500_unified.py --model deepseek --csv
```

Dry-run validation (with existing n=50 data):
```bash
python analyze_c2_n500.py --n50-only
python analyze_n500_unified.py --model all --dry-run --csv
python analyze_n500.py --n50-only
```

## 5. Output Format Verification

`analyze_c2_n500.py` produces JSON with this structure per condition:
```json
{
  "phase_gradient": {
    "d_z": 0.1234,
    "d_z_ci": [0.05, 0.20],
    "d_z_interpretation": "small"
  },
  "median_diff": {
    "value": 0.0012,
    "ci": [0.0005, 0.0019],
    "ci_crosses_zero": false
  },
  "wilcoxon": {
    "p_value": 0.003
  },
  "phase_stats": {
    "high": {"median": ...},
    "mid": {"median": ...},
    "low": {"median": ...}
  }
}
```

This format is directly usable for paper updates: median II per phase, bootstrap CI, d_z with CI, and Wilcoxon p-values.

## 6. Summary

| Script | Ready? | Fixes Needed | Best For |
|--------|--------|-------------|----------|
| `analyze_c2_n500.py` | 95% | Remove ratio display (1 change) | Primary analysis, paper figures |
| `analyze_n500_unified.py` | 70% | B→10000, remove dz_rand (2 changes) | Dose-response, CSV export |
| `analyze_n500.py` | 60% | B→10000, add dz CI, fix scope (3 changes) | Detailed per-condition tables |

**Recommendation**: Fix `analyze_c2_n500.py` (1 change: remove ratio from report) and use it as the primary pipeline. Optionally fix `analyze_n500_unified.py` (2 changes) for dose-response analysis.
