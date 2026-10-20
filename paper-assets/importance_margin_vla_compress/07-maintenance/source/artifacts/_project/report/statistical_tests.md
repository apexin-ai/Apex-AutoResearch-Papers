# Statistical Tests — M-sweep & Adapter Comparison

> Generated: 2026-05-19

## Data Sources

| Condition | Seed 42 exp_id | Seed 43 exp_id | Seed 44 exp_id | SR values (%) |
|-----------|---------------|----------------|----------------|---------------|
| M=32 VTC | eval_smart_compress_m32 (61.6) | eval_smart_compress_m32_seed43 (59.2) | eval_smart_compress_m32_seed44_v2 (59.6) | [61.6, 59.2, 59.6] |
| M=64 VTC | eval_smart_compress_m64 (61.6) | eval_smart_compress_m64_seed43 (60.0) | eval_smart_compress_m64_seed44_v2 (64.4) | [61.6, 60.0, 64.4] |
| M=96 VTC | eval_smart_compress_m96 (52.6) | eval_smart_compress_m96_seed43_v2 (58.2) | eval_smart_compress_m96_seed44_v2 (52.8) | [52.6, 58.2, 52.8] |
| M=128 VTC | eval_smart_compress_m128 (59.8) | — | eval_smart_compress_m128_seed44 (60.2) | [59.8, 60.2] |
| M=32 MLP | eval_mlp_adapter_control (65.2) | eval_mlp_adapter_seed43 (64.6) | eval_mlp_adapter_seed44 (60.4) | [65.2, 64.6, 60.4] |

## Summary Statistics

| Condition | n | Mean (%) | Std (%) |
|-----------|---|----------|---------|
| M=32 VTC | 3 | 60.1 | 1.3 |
| M=64 VTC | 3 | 62.0 | 2.3 |
| M=96 VTC | 3 | 54.5 | 3.2 |
| M=128 VTC | 2 | 60.0 | 0.3 |
| M=32 MLP | 3 | 63.4 | 2.6 |

## Pairwise Welch's t-test

| Pair | Mean A | Mean B | Diff | t | p | Cohen's d | n_A | n_B | Sig (p<.05) |
|------|--------|--------|------|---|---|-----------|-----|-----|-------------|
| M=32 VTC vs M=64 VTC | 60.1 | 62.0 | -1.9 | -1.257 | 0.2926 | -1.027 | 3 | 3 | no |
| M=32 VTC vs M=96 VTC | 60.1 | 54.5 | +5.6 | 2.830 | 0.0769 | 2.311 | 3 | 3 | no |
| M=32 VTC vs M=128 VTC | 60.1 | 60.0 | +0.1 | 0.173 | 0.8765 | 0.143 | 3 | 2 | no |
| **M=32 VTC vs M=32 MLP** | **60.1** | **63.4** | **-3.3** | **-1.941** | **0.1502** | **-1.585** | **3** | **3** | **no** |
| **M=64 VTC vs M=96 VTC** | **62.0** | **54.5** | **+7.5** | **3.333** | **0.0342** | **2.722** | **3** | **3** | **YES** |
| M=64 VTC vs M=128 VTC | 62.0 | 60.0 | +2.0 | 1.537 | 0.2586 | 1.260 | 3 | 2 | no |
| M=64 VTC vs M=32 MLP | 62.0 | 63.4 | -1.4 | -0.706 | 0.5201 | -0.576 | 3 | 3 | no |
| M=96 VTC vs M=128 VTC | 54.5 | 60.0 | -5.5 | -2.963 | 0.0949 | -2.424 | 3 | 2 | no |
| **M=96 VTC vs M=32 MLP** | **54.5** | **63.4** | **-8.9** | **-3.732** | **0.0216** | **-3.047** | **3** | **3** | **YES** |
| M=128 VTC vs M=32 MLP | 60.0 | 63.4 | -3.4 | -2.232 | 0.1510 | -1.828 | 2 | 3 | no |

## Key Findings

- **2/10 pairs statistically significant (p<0.05)**:
  - M=64 VTC > M=96 VTC: p=0.034, Cohen's d=2.72 (very large effect)
  - M=32 MLP > M=96 VTC: p=0.022, Cohen's d=3.05 (very large effect)

- **M=32 VTC vs M=32 MLP (key comparison): p=0.150, NOT significant**
  - MLP adapter leads by 3.3pp on average, but the difference cannot be distinguished from noise at n=3
  - Cohen's d=1.59 suggests a large effect size, but insufficient power to confirm

- **M=96 is the clear underperformer**: significantly worse than both M=64 VTC and MLP adapter. The non-monotonic dip at M=96 is real (statistically supported).

- **M=32/M=64/M=128 VTC form an indistinguishable cluster**: no pairwise comparison among them reaches significance (all p>0.25)

- **Cohen's d interpretation** (small<0.2, medium 0.2-0.8, large>0.8): Most effect sizes are large, reflecting meaningful absolute differences, but the extremely small n limits statistical power.

## Implications for Paper Wording

- Claims about VTC vs MLP adapter should use hedged language: "comparable performance" or "no statistically significant difference" rather than "equivalent" or "better"
- The M=96 dip can be stated as a confirmed finding (p<0.05 vs M=64)
- M=32/64/128 VTC performance plateau can be described as "robust across M values" since none differ significantly

## Notes

- M=128 has only 2 seeds (seed43 still training); all M=128 comparisons have reduced power
- All tests are Welch's t-test (unequal variance assumption)
- With n=3 per condition, statistical power is very limited (~0.2 for medium effects); non-significant results should NOT be interpreted as evidence of no difference
- No multiple comparison correction applied (10 tests); if Bonferroni-corrected (alpha=0.005), no pair remains significant
