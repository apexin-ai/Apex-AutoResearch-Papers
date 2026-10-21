# Analysis: α=0.50 (3-seed) + α=0.10 s42 fp32 Batch
**Date**: 2026-05-19
**Server**: westd-17855

---

## Summary

| exp_id | α | seed | status | gens | EXIT_CODE | analysis_results |
|--------|---|------|--------|------|-----------|------------------|
| alpha_sweep_a050_s42_fp32 | 0.50 | 42 | completed | 11/11 | 0 | **MISSING** |
| alpha_sweep_a050_s43_fp32 | 0.50 | 43 | completed | 11/11 | 0 | ✓ |
| alpha_sweep_a050_s44_fp32 | 0.50 | 44 | completed | 11/11 | 0 | ✓ |
| alpha_sweep_a010_s42_fp32 | 0.10 | 42 | completed | 11/11 | 0 | ✓ |

**Precision**: fp32 confirmed (config.json: `bf16: false`; no bf16/fp16 flags)
**Model**: EleutherAI/pythia-410m
**W&B**: No W&B run IDs found in any log
**Errors**: None (no OOM/NaN)
**Note**: a050_s42 is missing analysis_results.json (lead-lag analysis not run). Drifts below are manually computed.

---

## Experiment Details

### === alpha_sweep_a050_s42_fp32 ===
```
status: completed_normally
precision_confirmed: fp32
generations_completed: 11/11 (gen 0-10)
metrics:
  final_ppl: 31.462
  final_entropy: 2.7075
  final_eff_rank: 58.18
  final_mauve: 0.0238
  token_entropy_drift: -16.30%
  ece_drift: +703.5%
  perplexity_drift: +16.75%
  distinct_1_drift: -29.18%
  distinct_2_drift: -37.30%
  distinct_3_drift: -32.89%
  effective_rank_drift: +24.82%
  mauve_drift: -11.76%
  perm_granger_fwd: N/A (analysis not run)
  perm_granger_rev: N/A
  ty_granger_fwd: N/A
  threshold_onset_fwd: N/A
  consensus_k4: N/A
  mmct_wpair_fwd: N/A
checkpoint_path: results/alpha_sweep/a050_s42_fp32/gen_9/checkpoint, gen_10/checkpoint
log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log
notes: analysis_results.json MISSING — need to run lead-lag analysis separately
```

### === alpha_sweep_a050_s43_fp32 ===
```
status: completed_normally
precision_confirmed: fp32
generations_completed: 11/11 (gen 0-10)
metrics:
  final_ppl: 31.576
  final_entropy: 2.7227
  final_eff_rank: 58.47
  final_mauve: 0.0232
  token_entropy_drift: -15.81%
  ece_drift: +679.56%
  perplexity_drift: +17.17%
  distinct_1_drift: -29.00%
  distinct_2_drift: -36.25%
  distinct_3_drift: -32.38%
  effective_rank_drift: +25.44%
  mauve_drift: -23.54%
  perm_granger_fwd: 6/8
  perm_granger_rev: 0/8
  ty_granger_fwd: 5/8
  threshold_onset_fwd: 8/8
  consensus_k4: 6/8
  mmct_wpair_fwd: 0.75
checkpoint_path: results/alpha_sweep/a050_s43_fp32/gen_9/checkpoint, gen_10/checkpoint
log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s43_fp32.log
notes: Strong causality signal. All 6 consensus pairs have ≥4 votes.
```

### === alpha_sweep_a050_s44_fp32 ===
```
status: completed_normally
precision_confirmed: fp32
generations_completed: 11/11 (gen 0-10)
metrics:
  final_ppl: 31.424
  final_entropy: 2.6971
  final_eff_rank: 58.29
  final_mauve: 0.0237
  token_entropy_drift: -16.61%
  ece_drift: +709.03%
  perplexity_drift: +16.61%
  distinct_1_drift: -27.93%
  distinct_2_drift: -34.64%
  distinct_3_drift: -30.60%
  effective_rank_drift: +25.06%
  mauve_drift: -13.88%
  perm_granger_fwd: 6/8
  perm_granger_rev: 0/8
  ty_granger_fwd: 4/8
  threshold_onset_fwd: 8/8
  consensus_k4: 6/8
  mmct_wpair_fwd: 0.75
checkpoint_path: results/alpha_sweep/a050_s44_fp32/gen_9/checkpoint, gen_10/checkpoint
log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a050_s44_fp32.log
notes: Consistent with s43. TY slightly lower (4/8 vs 5/8) but PermG identical.
```

### === alpha_sweep_a010_s42_fp32 ===
```
status: completed_normally
precision_confirmed: fp32
generations_completed: 11/11 (gen 0-10)
metrics:
  final_ppl: 21.845
  final_entropy: 3.0858
  final_eff_rank: 46.14
  final_mauve: 0.0267
  token_entropy_drift: -4.59%
  ece_drift: +51.86%
  perplexity_drift: -18.94%
  distinct_1_drift: -23.80%
  distinct_2_drift: -27.15%
  distinct_3_drift: -19.36%
  effective_rank_drift: -1.01%
  mauve_drift: -1.20%
  perm_granger_fwd: 0/8
  perm_granger_rev: 0/8
  ty_granger_fwd: 3/8
  threshold_onset_fwd: 5/8
  consensus_k4: 2/8
  mmct_wpair_fwd: 0.25
checkpoint_path: results/alpha_sweep/a010_s42_fp32/gen_9/checkpoint, gen_10/checkpoint
log_path: ~/runs/distrib_canary_collapse/alpha_sweep_a010_s42_fp32.log
notes: Clear blind-zone behavior. PermG=0/8 matches α=0.05 and α=0.10 s43 results.
```

---

## Cross-experiment Comparison

### Drift Metrics (gen 0 → gen 10)

| Metric | a050_s42 | a050_s43 | a050_s44 | a050 mean±std | a010_s42 |
|--------|----------|----------|----------|---------------|----------|
| token_entropy | -16.30% | -15.81% | -16.61% | -16.24±0.33% | -4.59% |
| perplexity | +16.75% | +17.17% | +16.61% | +16.84±0.24% | -18.94% |
| distinct_1 | -29.18% | -29.00% | -27.93% | -28.70±0.55% | -23.80% |
| distinct_2 | -37.30% | -36.25% | -34.64% | -36.06±1.10% | -27.15% |
| distinct_3 | -32.89% | -32.38% | -30.60% | -31.96±0.98% | -19.36% |
| ece | +703.5% | +679.6% | +709.0% | +697.4±12.7% | +51.86% |
| eff_rank | +24.82% | +25.44% | +25.06% | +25.11±0.25% | -1.01% |
| mauve | -11.76% | -23.54% | -13.88% | -16.39±5.17% | -1.20% |

### Causality Signal (from analysis_results.json)

| Metric | a050_s43 | a050_s44 | a010_s42 |
|--------|----------|----------|----------|
| perm_granger_fwd | 6/8 | 6/8 | 0/8 |
| perm_granger_rev | 0/8 | 0/8 | 0/8 |
| ty_granger | 5/8 | 4/8 | 3/8 |
| threshold_onset | 8/8 | 8/8 | 5/8 |
| consensus_k4 | 6/8 | 6/8 | 2/8 |
| mmct_wpair | 0.75 | 0.75 | 0.25 |

### Final Metrics Comparison

| Metric | a050_s42 | a050_s43 | a050_s44 | a010_s42 |
|--------|----------|----------|----------|----------|
| final_ppl | 31.462 | 31.576 | 31.424 | 21.845 |
| final_entropy | 2.7075 | 2.7227 | 2.6971 | 3.0858 |
| final_eff_rank | 58.18 | 58.47 | 58.29 | 46.14 |
| final_mauve | 0.0238 | 0.0232 | 0.0237 | 0.0267 |

---

## Key Findings

### 1. α=0.50 is firmly in the "detectable" regime
- **PermG = 6/8** across both seeds with analysis (s43, s44): perfectly consistent
- **Consensus K≥4 = 6/8**: strong multi-method agreement
- **MMCT = 0.75**: transitional, similar to α=0.60 (0.875)
- **PermG_rev = 0/8**: causality is unidirectional (canary→downstream), no reverse signal
- α=0.50 is NOT in the blind zone — it's well above the PermG step function threshold

### 2. Step function lower bound is between α=0.10 and α=0.50
- α=0.10: PermG=0/8, k4=2/8, mmct=0.25 (blind zone)
- α=0.50: PermG=6/8, k4=6/8, mmct=0.75 (detectable)
- The step function jump occurs somewhere in [0.10, 0.50]
- Need α=0.25 or α=0.30 data to pinpoint the exact threshold

### 3. α=0.50 3-seed consistency is excellent
- Drift metrics: very tight standard deviations (d1_drift: -28.70±0.55%)
- Final ppl: 31.42-31.58 range (Δ<0.5%)
- Causality: PermG=6/8 on both analyzed seeds (identical)
- Mauve drift shows more variance (-11.76% to -23.54%) but mauve is known noisy at low absolute values

### 4. α=0.10 s42 confirms blind zone
- PermG=0/8 matches prior α=0.10 s43 (PermG=0/8) and α=0.05 (PermG=0/8)
- Perplexity actually decreases (-18.94%) unlike α=0.50 (+16.84%): lower contamination allows model to fit better
- ECE drift much smaller (+51.86% vs +697%) — calibration barely affected

### 5. ACTION NEEDED: Run analysis for a050_s42
- analysis_results.json is missing for a050_s42
- Need to run lead-lag analysis script on this experiment to complete the 3-seed picture

---

## Updated Alpha Sweep Overview (all fp32, Pythia-410m)

| α | seeds | PermG_fwd | k4 | d1_drift | mmct | regime |
|---|-------|-----------|----|---------:|------|--------|
| 0.05 | 42 | 0/8 | 0/8 | -24.9% | 0 | blind |
| 0.10 | 42,43 | 0/8 | 0-2/8 | -22 to -24% | 0-0.25 | blind |
| 0.50 | 43,44 | 6/8 | 6/8 | -28 to -29% | 0.75 | transitional |
| 0.60 | 42 | 3/8 | 7/8 | -28.2% | 0.875 | transitional |
| 1.00 | multi | ~6/8 | ~6/8 | — | — | confirmatory |

**Note**: α=0.50 PermG (6/8) is actually higher than α=0.60 (3/8). This suggests the step function may not be monotonic, or α=0.60 single-seed was an underestimate. Multi-seed at α=0.60 would clarify.
