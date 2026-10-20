# validation bayesian metrics

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_bayesian-metrics_20260525T203917_result.json`
- **Structured JSON:** [`e87a21d8f8ccbc9131cb.json`](../../sessions/e8/e87a21d8f8ccbc9131cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the verification report:

---

```
Item 8 (Power): [CANNOT VERIFY from files]
  论文: N=8 power ≈ 50%, 80% power requires N≈17, 95% power requires N≈25
  实际: 无独立 power_analysis 结果文件。
  佐证: N=8 bootstrap P(Δτ≥0)=0.927, P(Δτ>0)=0.451 (≈45%),
        Δτ 95% CI=[-0.071, 0.071]，与 ~50% power 一致。
        N=20 synthetic (exp018) 达到显著 (Wilcoxon p=1.81e-4)，
        验证了 N≈17 足够 80% power 的预测。
  结论: 定性一致，但具体数值（50%/N≈17/N≈25）无独立结果文件可精确复现。

Item 9 (LOO): [MATCH]
  论文: ΔELPD_LOO=-55.7, SE=9.4, |Δ/SE|=5.9, stacking=1.0, all k̂<0.7
  实际 (loo_comparison.json):
    delta_elpd_loo = 55.69 (MFRM deficit = -55.7) ✓
    dse = 9.4 ✓
    |Δ/SE| = 55.7/9.4 = 5.9 ✓
    G-MFRM stacking weight = 1.0, MFRM = 0.0 ✓
    G-MFRM pareto_k_max = 0.276, MFRM pareto_k_max = 0.361, 
    both pareto_k_gt_0.7 = 0 ✓

Item 10 (Prior Robustness): [MATCH]
  论文: Horseshoe vs HalfNormal Pearson r > 0.999 (c_n)
  实际 (summary.json horseshoe vs refit_summary.json HalfNormal):
    Horseshoe c_n: [5.57, 4.15, 2.94, 2.46, 1.65, 1.15, 0.92, 0.88]
    HalfNormal c_n: [5.60, 4.20, 3.00, 2.50, 1.70, 1.20, 0.93, 0.88]
    Worker 此前已验证 r = 0.999940 > 0.999 ✓
    论文 appendix 精确声明: r=1.000 (θ), r=0.9999 (c_n) ✓

Item 11 (N=17 Main Results): [MATCH] 逐行全部匹配
  Full set (500 items, output_n17_phase1_v2):
    τ_raw=0.8382→0.838 ✓  τ_GMFRM=0.7941→0.794 ✓  Δτ=-0.044 ✓
  Filtered (317 items, output_n17_v3_filtered):
    τ_raw=0.8235→0.824 ✓  τ_GMFRM=0.8088→0.809 ✓  Δτ=-0.015 ✓
  Exposed-only (231 items, output_n17_v7_nonzero_ei):
    τ_raw=0.7794→0.779 ✓  τ_GMFRM=0.7794→0.779 ✓  Δτ=0.000 ✓
  N=8 pilot (exp003/output_003b):
    τ_raw=0.786 ✓  τ_GMFRM=0.857 ✓  Δτ=+0.071 ✓

Item 12 (Baselines τ): [PARTIAL MISMATCH]
  论文声明: 所有 7 个 baseline τ 在 raw_average 的 0.015 内
  实际 (baseline_summary.csv, N=17):
    raw_average:         0.8382  (ref)
    cyclic_judge:        0.8382  Δ=0.000 ✓
    cyclic_judge_discard:0.8235  Δ=0.015 ✓ (边界)
    dcr_factor:          0.8235  Δ=0.015 ✓ (边界)
    preference_leakage:  0.8382  Δ=0.000 ✓
    uda_zscore:          0.8235  Δ=0.015 ✓ (边界)
    uda_quantile:        0.8000  Δ=0.038 ✗ (超出 0.015)
  注: 6/6 在 0.015 内（含边界），uda_quantile 差 0.038。
  论文实际原文 (experiments.tex) 对 N=8 声称 "identical rankings 
  (τ=0.786)"，N=17 列标注 "TBD"，故 "0.015 内" 可能是待写入的描述。
```

---
