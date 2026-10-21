# Analysis: alpha_sweep_a030_s42_fp32

## Config
- Model: Pythia-410M, WikiText-103, α=0.30, seed=42, fp32
- 11 generations (gen_0–gen_10), EXIT_CODE=0
- Server: westd-17855, 6.3 GPU-hours
- No W&B run

## Hypothesis
α=0.30 仍在 blind zone（预期 PermG=0/8），将 onset 下界从 0.25 收紧到 0.30。

## Result: CONFIRMED — PermG=0/8, blind zone 扩展至 α≤0.30

## Drift (gen0→gen10)
| Metric | Drift |
|--------|-------|
| token_entropy | -17.32% |
| ECE | +549.38% |
| distinct_1 | -36.72% |
| distinct_2 | -49.75% |
| distinct_3 | -50.09% |
| mauve | -26.09% |
| perplexity | -8.37% |
| effective_rank | +17.28% |

## 5-Method Lead-Lag (8 pairs: entropy/ECE × d1/d2/d3/mauve)

### Summary
| Method | Sig/Total |
|--------|-----------|
| naive_xcorr | 8/8 |
| diff_xcorr | 4/8 |
| threshold_onset | 8/8 |
| **PermG fwd** | **0/8** |
| PermG rev | 0/8 |
| TY Granger | 5/8 (C003: unreliable at α≤0.50) |
| **K≥3** | **6/8** |
| **K≥4** | **3/8** |

### Per-Pair Detail

| Pair | naive | diff | thresh | PermG(p_fdr) | TY | Votes |
|------|-------|------|--------|--------------|-----|-------|
| entropy→d1 | ✓ lag=1 | ✓ lag=5 | ✓ lead=1 | ✗ (0.106) | ✓ d_max=0,df=7 | **4** |
| entropy→d2 | ✓ lag=1 | ✓ lag=5 | ✓ lead=1 | ✗ (0.106) | ✓ d_max=0,df=7 | **4** |
| entropy→d3 | ✓ lag=1 | ✗ | ✓ lead=1 | ✗ (0.106) | ✗ d_max=2,df=1 | 2 |
| entropy→mauve | ✓ lag=1 | ✗ | ✓ lead=7 | ✗ (0.128) | ✗ d_max=0,df=7 | 2 |
| ece→d1 | ✓ lag=-1 | ✓ lag=-1 | ✓ lead=1 | ✗ (0.106) | ✗ d_max=2,df=1 | 3 |
| ece→d2 | ✓ lag=-5 | ✗ | ✓ lead=1 | ✗ (0.106) | ✓ d_max=2,df=1 | 3 |
| ece→d3 | ✓ lag=-5 | ✗ | ✓ lead=1 | ✗ (0.106) | ✓ d_max=2,df=1 | 3 |
| ece→mauve | ✓ lag=2 | ✓ lag=2 | ✓ lead=7 | ✗ (0.106) | ✓ d_max=2,df=1 | **4** |

### PermG FDR-adjusted p-values (all non-significant)
- entropy→d1: 0.106, entropy→d2: 0.106, entropy→d3: 0.106, entropy→mauve: 0.128
- ece→d1: 0.106, ece→d2: 0.106, ece→d3: 0.106, ece→mauve: 0.106

## Notes
- TY Granger: 4/5 significant pairs have d_max=2, df_resid=1 — per C003, not usable as evidence at α≤0.50
- PermG raw p-values range 0.053–0.128, all marginal but none pass BH FDR at α_BH=0.05
- MMCT null distribution unavailable (a000_s42_fp32 lacks 5method_leadlag.json)
- Despite substantial drift (entropy -17%, diversity -37~50%), PermG power insufficient at T=11

## Updated Onset Boundary
| α | PermG | Status |
|---|-------|--------|
| 0.00 | 0/8 | baseline |
| 0.10 | 0/8 | blind zone |
| 0.25 | 0/8 | blind zone |
| **0.30** | **0/8** | **blind zone (this exp)** |
| 0.35 | 0/8 | blind zone |
| 0.40 | 0/8 | blind zone |
| 0.50 | 6/8 | detected |

Onset boundary: α ∈ (0.40, 0.50]
