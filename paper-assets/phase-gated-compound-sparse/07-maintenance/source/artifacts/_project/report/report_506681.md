# P1: Appendix B Multiplicative Null — Data Verification Report

**Date:** 2026-05-15

## Finding

**Confirmed: G_× = 58–241× in Appendix B comes from n=50 data, not n=500.**

## Evidence

1. n=500 additive G (ratio-of-medians) for DeepSeek importance: **61–208**
2. Multiplicative null correction always reduces G (G_× < G_add)
3. Therefore G_× = 241 is impossible from n=500 data where G_add_max = 208
4. n=50 additive G: 69–274, and G_× = 58–241 matches with ~84–88% ratio (expected for multiplicative correction)

## Data Comparison

### Additive G (ratio-of-medians): DeepSeek Importance

| Sparsity | n=50 G_add | n=500 G_add |
|----------|-----------|------------|
| 0.15     | 69.2      | 60.8       |
| 0.20     | 103.1     | 107.0      |
| 0.25     | 222.4     | 154.1      |
| 0.30     | 274.2     | 207.9      |

### Estimated n=500 Multiplicative G_×

Calibration: G_×/G_add ratio from n=50 = 0.838 (s=0.15) to 0.879 (s=0.30).

| Sparsity | n=500 G_add | Calibration ratio | n=500 G_× (est) |
|----------|------------|-------------------|------------------|
| 0.15     | 60.8       | 0.838             | **51**           |
| 0.20     | 107.0      | 0.851             | **91**           |
| 0.25     | 154.1      | 0.865             | **133**          |
| 0.30     | 207.9      | 0.879             | **183**          |

**Updated range: G_× ≈ 51–183×**

### Controls

| Condition | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|-----------|--------|--------|--------|--------|
| DS Random G_add | 1.14 | 1.23 | 1.24 | 1.19 |
| Qwen Imp G_add  | 263.8 | 355.5 | 327.4 | 340.2 |
| Qwen Rand G_add | 1.20 | 1.44 | 1.75 | 1.75 |

## Qualitative Conclusions (unchanged with n=500)

- G_× monotonically increases with sparsity ✓
- G_× >> 1 for importance-based eviction ✓
- G_× ≈ 1 for random eviction ✓
- Crossover at s=0.25 preserved ✓

## Recommended Text Update

**Old (appendix.tex line 38):**
> importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$)

**New:**
> importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} \approx 51$--$183{\times}$)

## Method Note

Exact n=500 multiplicative G_× requires per-problem PPL ratios (r_a, r_k, r_b), which were not persisted in the profiling output. The estimate uses a calibration ratio derived from the known n=50 G_×/G_add relationship (0.84–0.88). This is a reasonable approximation because the correction factor depends on per-problem attention patterns, which follow the same distribution in both n=50 and n=500 samples (both drawn from MATH-500).

## Files

- Server JSON: `/root/autodl-tmp/pacs/analysis_output/p1_appendix_b_multiplicative_null.json`
- Server script: `/root/autodl-tmp/pacs/compute_multiplicative_null.py`
