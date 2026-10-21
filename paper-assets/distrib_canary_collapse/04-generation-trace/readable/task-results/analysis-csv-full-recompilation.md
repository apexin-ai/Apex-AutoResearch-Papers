# analysis csv full recompilation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_csv_full_recompilation_20260520T200723_result.json`
- **Structured JSON:** [`f70951e0e072318559cf.json`](../../sessions/f7/f70951e0e072318559cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证报告：

```
=== dose_response_d120_recompiled.csv 验证报告 ===

total_experiments: 71
total_from_17855: 40
total_from_19828: 31
categories: ablation(1), alpha_sweep(44), generalize(15), intervention(4), padding_robustness(1), scale(2), scale_check(2), t20(5)

threshold_criterion: 全部 true_3sigma_d105（0 pre-D105 跳过）
significance_fields: diff_xcorr→significant_fdr, perm_granger→significant_fdr, naive/threshold/ty→significant

spot_check_passed: 5/5
  - a010_s43_fp32 (17855): pg_fwd=3 diff_fwd=7 thr=2 ty=1 K≥3=4 ✓
  - a040_s42_fp32 (17855): pg_fwd=0 diff_fwd=3 thr=0 ty=2 K≥3=1 ✓
  - a050_s42_fp32 (17855): pg_fwd=6 diff_fwd=7 thr=4 ty=3 K≥3=6 ✓
  - a075_s43 (19828):       pg_fwd=5 diff_fwd=6 thr=2 ty=2 K≥3=6 ✓
  - t20_a100_s42_fp32 (17855): pg_fwd=6 diff_fwd=6 thr=6 ty=2 K≥3=6 ✓

discrepancies: []

vs old CSV (49 rows):
  - +22 experiments (new: t20×5, a045_s43, a050_postd093, bf16 variants, 19828 duplicates, v3_d080 experiments)
  - TY values changed for many experiments (D111 direction fix: peak_lag>0 → peak_lag<0)
  - Column schema updated: added T, domain, n_pairs, fwd/rev separation, FDR-specific names

csv_path: /root/autodl-tmp/distrib_canary_collapse/dose_response_d120_recompiled.csv
local_path: artifacts/dose_response_d120_recompiled.csv
compile_script: compile_dose_response.py
```

---
