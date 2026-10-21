# Figure Status Report — trace-verdict-study

**Generated**: 2026-05-16

## Summary

All 4 required paper figures are **complete** on server `westd-11235`.

## Figure Inventory

| Figure | File | Server Path | Size (PDF) | Status |
|--------|------|-------------|------------|--------|
| fig1_trace_overview | fig1_trace_overview.pdf | `/root/trace-verdict-study/figures/paper/` | 37 KB | ✅ Complete |
| fig2_calibration | fig2_calibration.pdf | `/root/trace-verdict-study/figures/paper/` | 18 KB | ✅ Complete |
| fig3_cross_model_gap | fig3_cross_model_gap.pdf | `/root/trace-verdict-study/figures/paper/` | 33 KB | ✅ Complete |
| fig4_trace_length | fig4_trace_length.pdf | `/root/trace-verdict-study/figures/paper/` | 17 KB | ✅ Complete |

## Additional Versions

| File | Path | Notes |
|------|------|-------|
| fig_trace_length_ablation.pdf/png | `figures/paper/` | Ablation variant (17 KB PDF) |
| fig_trace_ablation.pdf/png | `artifacts/` | Bootstrap-based version (13 KB PDF, updated 12:31) |
| token_length_ablation.pdf/png | `analysis/figures/` | Analysis-stage version (23 KB PDF) |

## Trace Length Ablation — Data Verification

Task-specified data points vs actual (from `trace_ablation_bootstrap.json`, n=1190):

| Condition | Task Spec | Actual | Match |
|-----------|-----------|--------|-------|
| 256tok | 78.82% | 78.82% | ✅ |
| 512tok | 80.42% | 80.42% | ✅ |
| 1024tok | 77.23% | 77.23% | ✅ |
| no_limit | 81.76% | 81.76% | ✅ |
| exception_only | 99.83% | 99.83% | ✅ |
| no_trace baseline | 75.13% | 75.13% | ✅ |

## Action Items

- **None.** All figures exist and data is verified. No regeneration needed.
- Local artifacts directory only has `fig4_trace_length` synced; other figures are on server only.
