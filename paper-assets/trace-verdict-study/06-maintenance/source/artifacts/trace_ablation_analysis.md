# Trace Length Ablation Analysis

## Data Points (Qwen-2.5-Coder-7B, seed42, n=1190)

| Condition | max_trace_tokens | Accuracy | 95% Bootstrap CI |
|-----------|-----------------|----------|------------------|
| 256tok | 256 | 78.82% | [76.39, 81.09] |
| 512tok | 512 | 80.42% | [78.24, 82.61] |
| 1024tok | 1024 | 77.23% | [74.87, 79.66] |
| no_limit | ~1970 | 81.76% | [79.58, 83.87] |
| no_trace (baseline) | 0 | 75.13% | [72.61, 77.56] |
| exception_only | N/A | 99.83% | [99.58, 100.00] |

## Paired Bootstrap Significance Tests (N=10,000, seed=42)

| Pair | Diff (pp) | 95% CI | p-value | Sig |
|------|-----------|--------|---------|-----|
| 256 vs 512 | -1.60 | [-3.53, +0.34] | 0.117 | ns |
| 512 vs 1024 | +3.19 | [+1.09, +5.29] | 0.002 | ** |
| 1024 vs no_limit | -4.54 | [-6.55, -2.52] | <0.001 | *** |
| 256 vs no_limit | -2.94 | [-5.04, -0.84] | 0.006 | ** |
| 256 vs no_trace | +3.70 | [+1.43, +6.05] | 0.002 | ** |
| 512 vs no_trace | +5.29 | [+3.03, +7.56] | <0.001 | *** |
| 1024 vs no_trace | +2.10 | [-0.17, +4.37] | 0.078 | ns |
| no_limit vs no_trace | +6.64 | [+4.37, +8.99] | <0.001 | *** |
| 256 vs exception_only | -21.01 | [-23.45, -18.74] | <0.001 | *** |
| 512 vs exception_only | -19.41 | [-21.76, -17.14] | <0.001 | *** |
| 1024 vs exception_only | -22.61 | [-25.04, -20.25] | <0.001 | *** |
| no_limit vs exception_only | -18.07 | [-20.34, -15.88] | <0.001 | *** |

## Key Findings

1. **Trace length does not monotonically improve accuracy.** The 1024-token condition (77.23%) is significantly *worse* than both 512-token (80.42%, p=0.002) and no_limit (81.76%, p<0.001), showing a non-monotonic dip. The 256-to-512 improvement (+1.60pp) is not statistically significant (p=0.117).

2. **All full-trace conditions are dramatically outperformed by exception_only** (99.83%), with gaps of 18-23 percentage points (all p<0.001). This confirms that providing the model with raw execution traces (even unlimited length) is far less informative than structured exception information for verdict prediction.

## Artifacts

- Figure: `fig_trace_ablation.pdf` / `fig_trace_ablation.png` (server: `/root/trace-verdict-study/artifacts/`)
- Bootstrap JSON: `trace_ablation_bootstrap.json` (server: `/root/trace-verdict-study/artifacts/`)
- Scripts: `analysis/trace_ablation_bootstrap.py`, `analysis/fig_trace_ablation.py` (server)
