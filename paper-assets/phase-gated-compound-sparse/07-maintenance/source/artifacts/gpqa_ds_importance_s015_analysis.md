# Experiment Analysis: gpqa_ds_importance_s015

## Summary

| Field | Value |
|-------|-------|
| Model | DeepSeek-R1-Distill-Qwen-7B |
| Dataset | GPQA Diamond (198 problems, full) |
| Method | Importance-based eviction, sparsity=0.15 |
| Phase decomposition | Quantile 3-segment |
| Duration | ~12h 24m (2026-05-16 15:43 → 2026-05-17 04:07) |
| Exit code | 0 |
| W&B | Not logged |
| Verdict | **PASS** |

## Per-Phase Severity (Importance Impact at s=0.15)

| Phase Segment | Tokens | Segments | II Median | II 95% CI | II Mean | Mean 95% CI |
|---------------|--------|----------|-----------|-----------|---------|-------------|
| high_sparsity | 479,658 | 6,261 | +0.0128 | [+0.0115, +0.0139] | +0.1914 | [+0.0480, +0.5148] |
| mid_sparsity | 276,409 | 2,185 | +0.1024 | [+0.0927, +0.1151] | +0.8779 | [+0.7231, +1.0391] |
| low_sparsity | 465,085 | 5,128 | +0.9602 | [+0.8929, +1.0331] | +5.9918 | [+5.2360, +6.7323] |

**Monotonic ordering confirmed**: low_sparsity (0.96) > mid_sparsity (0.10) > high_sparsity (0.013)

- CIs are non-overlapping between all adjacent pairs (median level)
- ~75x severity ratio between low_sparsity and high_sparsity phases
- ~9.4x severity ratio between mid_sparsity and high_sparsity phases

## Interpretation

Phases with naturally low attention sparsity suffer dramatically more from importance-based head eviction at s=0.15. This confirms the core hypothesis that compound sparsity severity is phase-dependent — applying uniform eviction across all phases is suboptimal because dense-attention phases are disproportionately impacted.

The quantile 3-segment decomposition successfully separates phases into groups with well-differentiated severity profiles. The statistical significance (non-overlapping 95% CIs) confirms this is not noise.

## Conclusion

**SUCCESS** — Clear monotonic severity differentiation across phase segments on GPQA Diamond at s=0.15. The 3-segment quantile decomposition is a valid stratification method for this task domain. This data point establishes the s=0.15 baseline for the cross-condition monotonicity test (pending s=0.20 result).

## Output Files

- Log: `/root/runs/phase-gated-compound-sparse/gpqa_ds_importance_s015.log`
- Results: `/root/autodl-tmp/pacs/profiling_output_gpqa_ds_importance_s015/profiling_results.json` (37MB)
- Generations: `/root/autodl-tmp/pacs/profiling_output_gpqa_ds_importance_s015/generations.json` (4.2MB)
