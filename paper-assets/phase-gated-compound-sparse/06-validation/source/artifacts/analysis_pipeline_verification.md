# C2 n=500 Analysis Pipeline Verification Report

Date: 2026-05-14
Server: westd-22162
Script: `/root/autodl-tmp/pacs/scripts/analyze_c2_n500.py`

## Script Identification

Two versions exist:
- `/root/autodl-tmp/pacs/analyze_c2_n500.py` — **outdated**, less comprehensive
- `/root/autodl-tmp/pacs/scripts/analyze_c2_n500.py` — **authoritative**, D054-compliant, includes integrity checks, mid-phase null rate, paired gradient tests

The `scripts/` version was used for the latest s015 analysis.

## Constraint Compliance

### D054: Median + Median Bootstrap CI — PASS ✓

- `analyze_condition()` uses `np.median(diffs)` as primary metric
- CI via `bootstrap_median_ci()` bootstraps the median, not mean
- Report header: "Primary metric: MEDIAN (mean provided as reference only)"
- Mean computed as reference only, not used for significance decisions
- Default `B_BOOTSTRAP = 10000`, `SEED = 42`

### D059: d_z Within-Importance Only — **ISSUE FOUND** ⚠️

**What D059 requires**: d_z reported only for within-importance comparisons (phase gradient across sparsity levels). d_z for imp vs rand should NOT be reported.

**What the script does**:
1. `analyze_condition()` → reports d_z per condition (phase gradient D = ii_low - ii_high) — **OK**, this is within-condition
2. `paired_imp_vs_rand()` → computes and reports d_z for imp vs rand — **VIOLATES D059**
3. `paired_imp_vs_rand_gradient_test()` → computes and reports d_z for imp vs rand gradient — **VIOLATES D059**

**Affected output sections**:
- "Importance vs Random" table: includes `d_z` column
- "Imp vs Rand Paired Gradient" table: includes `d_z` column

**Recommended fix**: Remove d_z from `paired_imp_vs_rand()` return dict and `paired_imp_vs_rand_gradient_test()` return dict, plus remove d_z columns from the corresponding markdown table templates in `format_report()`.

### Wilcoxon Signed-Rank + Bonferroni — PASS ✓

- `wilcoxon_test()` uses `scipy.stats.wilcoxon`
- Bonferroni correction: `w_p_bonf = min(w_p * N_BONFERRONI, 1.0)` with `N_BONFERRONI = 4`
- Applied in both `analyze_condition()` and `paired_imp_vs_rand_gradient_test()`

## Condition Coverage

Script iterates: `{deepseek, qwen} × {imp, rand} × {s015, s020, s025, s030}` = **16 conditions** (8 per model).

Path pattern: `profiling_output_n500_bf16_{ds,qw}_{imp,rand}_s{015,020,025,030}/profiling_results.json`

Missing conditions are handled gracefully — recorded as `{"error": "missing ..."}` with no crash.

## Data Format Verification (s015)

s015 `profiling_results.json` structure:
```
config: {model, sparsity_levels, masking_method, n_problems: 500, seed: 42, ...}
phase_stats: {high_sparsity, mid_sparsity, low_sparsity}
perplexity: {per-phase per-sparsity}
interaction_index: {per-phase per-sparsity, includes median + median_ci}
per_problem_ii: {"0.15": [{problem_idx, problem_id, ii_high, ii_mid, ii_low, n_segments_*}, ...]}
```

- 500 problems per condition (verified via `grep -c problem_idx`)
- Fields match script expectations: `ii_low`, `ii_high`, `ii_mid`, `problem_idx`, `problem_id`
- Sparsity key is string (e.g., `"0.15"`) — script uses `SPARSITY_KEYS` mapping correctly

## Current Data Availability

| Condition | Status |
|-----------|--------|
| ds_imp_s015 | ✅ n=500, integrity OK |
| ds_rand_s015 | ✅ n=500, integrity OK |
| qw_imp_s015 | ✅ n=500, integrity OK (25 null ii_high/ii_low, 226 null ii_mid) |
| qw_rand_s015 | ✅ n=500, integrity OK (25 null ii_high/ii_low, 226 null ii_mid) |
| ds_imp_s020 | ❌ not yet run |
| ds_rand_s020 | ❌ not yet run |
| ds_imp_s025 | ❌ not yet run |
| ds_rand_s025 | ❌ not yet run |
| ds_imp_s030 | ❌ not yet run |
| ds_rand_s030 | ❌ not yet run |
| qw_imp_s020 | ❌ not yet run |
| qw_rand_s020 | ❌ not yet run |
| qw_imp_s025 | ❌ not yet run |
| qw_rand_s025 | ❌ not yet run |
| qw_imp_s030 | ❌ not yet run |
| qw_rand_s030 | ❌ not yet run |

## s015 Analysis Results (validated)

| Condition | n_valid | Median D | 95% CI | CI crosses 0? | d_z | Wilcoxon p (Bonf) |
|-----------|---------|----------|--------|---------------|-----|-------------------|
| ds_imp_s015 | 496 | +0.3907 | [0.3496, 0.4431] | no | 0.574 (medium) | 5.08e-70 |
| ds_rand_s015 | 496 | +0.0139 | [-0.0167, 0.0389] | YES | -0.045 (negligible) | 1.00 |
| qw_imp_s015 | 475 | +0.0659 | [0.0492, 0.0925] | no | 0.356 (small) | 3.46e-14 |
| qw_rand_s015 | 475 | -0.0111 | [-0.0390, 0.0124] | YES | 0.040 (negligible) | 0.687 |

Pre-registration verdict: Qwen s015 CI does not cross zero → **effect confirmed at s015**.

## One-Liner Command (when all conditions complete)

```bash
cd /root/autodl-tmp/pacs && /root/miniconda3/bin/python scripts/analyze_c2_n500.py
```

Outputs:
- `analysis_output/c2_n500_results.json` — full structured results
- `analysis_output/c2_n500_report.md` — markdown report

## Action Items

1. **[FIX NEEDED]** Remove d_z from imp vs rand sections to comply with D059:
   - `paired_imp_vs_rand()`: remove `d_z`, `d_z_ci`, `d_z_interpretation` from return dict
   - `paired_imp_vs_rand_gradient_test()`: remove `d_z` and `d_z_note` from return dict
   - `format_report()`: remove d_z columns from "Importance vs Random" and "Imp vs Rand Paired Gradient" tables
2. **[NOTE]** Existing s015 run used `B_BOOTSTRAP=2000` (via CLI arg). Full run should use default 10000.
3. **[NOTE]** Root-level `analyze_c2_n500.py` is outdated — always use `scripts/analyze_c2_n500.py`.
