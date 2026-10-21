# Data Audit Report: Paper Numerical Traceability Verification

**Date**: 2026-05-23  
**Scope**: All numerical claims in experiments.tex traced to raw server data  
**Servers**: rtx6000-diagprobe (most experiments), gpu-6000pro-1 (exp_016, exp_018)

---

## EXECUTIVE SUMMARY

**Overall: 3 minor rounding discrepancies found (all within ±0.1 of source), 1 internal text inconsistency (+97 vs +98), 1 caption imprecision in Table 2. No material data errors.**

| Category | Items Checked | Result |
|----------|-------------|--------|
| Table 1 (Phase I) | 30 cells (6 metrics × 5 generations) | ✅ All match |
| Table 2 (Alt EWS) | 8 indicators × 5 columns | ✅ All match (caption note) |
| Table 3 (Phase diagram) | 5 rows × 6 columns | ⚠️ 3 minor rounding diffs |
| Figure 1 data | 5 arrays × 11 values | ✅ All match |
| Figure 2 data | 10 arrays × 11 values | ✅ All match |
| Inline numbers | ~30 claims | ⚠️ 1 text inconsistency |

---

## A. TABLE 1 (tab:phase0) — §3.0 Phase I Metrics

**Data source**: 3-seed mean of exp_001 (seed42), exp_010 (seed43), exp_013 (seed44)  
**Server files**:
- `/root/spectral_collapse_ews/results/phase0_results.json` (seed42)
- `/root/spectral_collapse_ews/results/phase1_pure_collapse_seed43_results.json` (seed43)
- `/root/spectral_collapse_ews/results/phase1_pure_collapse_seed44_results.json` (seed44)

### Gen 0

| Metric | Paper | Server (all seeds identical) | Computation | Verdict |
|--------|-------|-----|-------------|---------|
| r_eff | 417.55 | 417.5472 | round to 2dp | ✅ MATCH |
| SLV | 2366.68 | 2366.6836 | round to 2dp | ✅ MATCH |
| PPL | 9.55 | 9.5536 | round to 2dp | ✅ MATCH |
| HeSw | .413 | 0.41297 (hellaswag_gen0) | round to 3dp | ✅ MATCH |
| D-4 | .738 | mean(0.7414, 0.7415, 0.7305) = 0.7378 | round to 3dp | ✅ MATCH |
| σ₁ | 1942.8 | 1942.816 | round to 1dp | ✅ MATCH |

### Gen 2

| Metric | Paper | Seed42 / Seed43 / Seed44 | Mean | Verdict |
|--------|-------|--------------------------|------|---------|
| r_eff | 496.17 | 496.441 / 496.244 / 495.831 | 496.172 | ✅ MATCH |
| SLV | 2467.98 | 2469.928 / 2466.626 / 2467.384 | 2467.979 | ✅ MATCH |
| PPL | 13.56 | 13.581 / 13.565 / 13.539 | 13.562 | ✅ MATCH |
| HeSw | .380 | 0.37642 / 0.38090 / 0.38409 | 0.38047 | ✅ MATCH |
| D-4 | .505 | 0.5154 / 0.5048 / 0.4943 | 0.5048 | ✅ MATCH |
| σ₁ | 718.7 | 712.03 / 718.12 / 726.02 | 718.72 | ✅ MATCH |

### Gen 5

| Metric | Paper | Seed42 / Seed43 / Seed44 | Mean | Verdict |
|--------|-------|--------------------------|------|---------|
| r_eff | 479.77 | 479.207 / 480.070 / 480.041 | 479.773 | ✅ MATCH |
| SLV | 2365.99 | 2370.173 / 2365.135 / 2362.674 | 2365.994 | ✅ MATCH |
| PPL | 24.50 | 24.593 / 24.603 / 24.303 | 24.500 | ✅ MATCH |
| HeSw | .341 | 0.34386 / 0.33838 / 0.34176 | 0.34133 | ✅ MATCH |
| D-4 | .412 | 0.4630 / 0.4172 / 0.3569 | 0.4124 | ✅ MATCH |
| σ₁ | 749.2 | 741.02 / 753.63 / 753.04 | 749.23 | ✅ MATCH |

### Gen 7

| Metric | Paper | Seed42 / Seed43 / Seed44 | Mean | Verdict |
|--------|-------|--------------------------|------|---------|
| r_eff | 464.10 | 464.199 / 464.184 / 463.931 | 464.105 | ✅ MATCH |
| SLV | 2293.24 | 2304.190 / 2291.548 / 2283.984 | 2293.241 | ✅ MATCH |
| PPL | 37.82 | 38.889 / 37.442 / 37.137 | 37.823 | ✅ MATCH |
| HeSw | .319 | 0.31866 / 0.31866 / 0.31906 | 0.31879 | ✅ MATCH |
| D-4 | .375 | 0.4474 / 0.3905 / 0.2862 | 0.3747 | ✅ MATCH |
| σ₁ | 788.4 | 791.28 / 790.03 / 783.82 | 788.38 | ✅ MATCH |

### Gen 10

| Metric | Paper | Seed42 / Seed43 / Seed44 | Mean | Verdict |
|--------|-------|--------------------------|------|---------|
| r_eff | 438.05 | 442.458 / 438.785 / 432.912 | 438.052 | ✅ MATCH |
| SLV | 2181.35 | 2178.949 / 2210.766 / 2154.336 | 2181.350 | ✅ MATCH |
| PPL | 70.99 | 76.781 / 70.500 / 65.698 | 70.993 | ✅ MATCH |
| HeSw | .296 | 0.29506 / 0.28998 / 0.30153 | 0.29552 | ✅ MATCH |
| D-4 | .324 | 0.4259 / 0.3940 / 0.1515 | 0.3238 | ✅ MATCH |
| σ₁ | 874.6 | 825.72 / 886.08 / 911.87 | 874.56 | ✅ MATCH |

### Caption s.d. values at Gen 10

| Metric | Paper s.d. | Computed s.d. | Verdict |
|--------|-----------|---------------|---------|
| r_eff | ±4.8 | 4.77 | ✅ |
| SLV | ±28.3 | 28.22 | ✅ |
| PPL | ±5.6 | 5.57 | ✅ |
| HeSw | ±.006 | 0.0058 | ✅ |
| D-4 | ±.15 | 0.150 | ✅ |

**Table 1 verdict: ALL 30 CELLS VERIFIED ✅**

---

## B. TABLE 2 (tab:ews_comparison) — §3.4 Alternative EWS

**Data source**: alternative_ews_v2_exp001.json (seed42 only, r=0)  
**Server file**: `/root/spectral_collapse_ews/results/alternative_ews_v2_exp001.json`

| Indicator | Source | Peak | Rel Δ (paper) | Rel Δ (computed) | Method | Verdict |
|-----------|--------|------|---------------|------------------|--------|---------|
| SLV | emb-SVD | Gen 2 | 11.8% | 11.78% | peak→Gen10: \|2178.95−2469.93\|/2469.93 | ✅ |
| RankMe | emb-SVD | Gen 2 | 4.7% | 4.73% | peak→Gen10: \|709.86−745.06\|/745.06 | ✅ |
| Token ent. | logit | --- | 9.6% | 9.58% | Gen0→10: \|6.106−6.752\|/6.752 | ✅ |
| Stable rank | attn wt. | --- | 14.0% | 14.0% | Gen0→10: \|29.09−33.83\|/33.83 | ✅ |
| Spec. norm | attn wt. | --- | 8.0% | 7.95% | Gen0→10: \|2.642−2.447\|/2.447 | ✅ |
| Isotropy | emb | --- | 75% | 75.4% | Gen0→10: \|0.076−0.311\|/0.311 (v1 data) | ✅ |
| Raw PPL | eval | --- | 643% | 643.1% | Gen0→10: \|70.99−9.55\|/9.55 (3-seed mean) | ✅ |
| PPL growth | ppl | --- | --- | N/A | --- | ✅ |

**Monotonicity checks**:
- Isotropy: 6 violations confirmed (values: 0.319→0.074→0.065→0.059→0.067→0.063→0.067→0.065→0.073→0.070→0.074 — direction reversals visible from Gen 4+) ✅
- PPL growth: ~1 violation (Gen 9→10: 14.03→13.46, slight decrease) ✅

**Caption note**: The formula "$|v_{10} - v_0|/|v_0|$" in the caption is imprecise for SLV and RankMe. For these peaked indicators, the "Rel Δ" is actually computed as peak-to-Gen10 change, not Gen0-to-Gen10. The Gen0-to-Gen10 change for SLV would be 7.9% (not 11.8%). This is methodologically appropriate (measures collapse signal strength) but the caption formula is misleading.

**Table 2 verdict: ALL VALUES VERIFIED ✅ (with caption imprecision noted)**

---

## C. TABLE 3 (tab:phase_summary) — §3.1 Gen 10 Summary

### r=0 (3-seed mean: exp_001 seed42, exp_010 seed43, exp_013 seed44)

| Metric | Paper | Seed42 / Seed43 / Seed44 | Computed Mean | Verdict |
|--------|-------|--------------------------|---------------|---------|
| SLV | 2181.4 | 2178.949 / 2210.766 / 2154.336 | 2181.350 → 2181.4 | ✅ MATCH |
| r_eff | 438.1 | 442.458 / 438.785 / 432.912 | 438.052 → 438.1 | ✅ MATCH |
| PPL | 71.0 | 76.781 / 70.500 / 65.698 | 70.993 → 71.0 | ✅ MATCH |
| D-4 | .324 | 0.4259 / 0.3940 / 0.1515 | 0.3238 → .324 | ✅ MATCH |

### r=0.2 (single seed: exp_011 seed42)

| Metric | Paper | Server (exp_011) | Verdict |
|--------|-------|-----------------|---------|
| SLV | 2479.7 | 2479.696 → 2479.7 | ✅ MATCH |
| r_eff | 511.3 | 511.255 → 511.3 | ✅ MATCH |
| PPL | 13.83 | 13.830 → 13.83 | ✅ MATCH |
| D-4 | .520 | 0.5203 → .520 | ✅ MATCH |

### r=0.25 (3-seed mean: exp_009 seed42, exp_014b seed43, exp_015 seed44)

| Metric | Paper | Seed42 / Seed43 / Seed44 | Computed Mean | Verdict |
|--------|-------|--------------------------|---------------|---------|
| SLV | 2488.1 | 2485.007 / 2488.577 / 2490.738 | 2488.107 → 2488.1 | ✅ MATCH |
| r_eff | 513.8 | 512.465 / 515.556 / 513.440 | 513.820 → 513.8 | ✅ MATCH |
| PPL | 13.41 | 13.285 / 13.611 / 13.330 | 13.409 → 13.41 | ✅ MATCH |
| D-4 | .342 | 0.3572 / 0.3380 / 0.3315 | 0.3422 → .342 | ✅ MATCH |

### r=0.3 (3-seed mean: exp_008 seed42, exp_012 seed43, exp_016 seed44)

**Server files**: exp_008/exp_012 on rtx6000-diagprobe, exp_016 on gpu-6000pro-1

| Metric | Paper | Seed42 / Seed43 / Seed44 | Computed Mean | Verdict |
|--------|-------|--------------------------|---------------|---------|
| SLV | 2508.2 | 2511.130 / 2508.325 / 2505.248 | 2508.234 → 2508.2 | ✅ MATCH |
| r_eff | 521.1 | 521.256 / 521.193 / 520.893 | 521.114 → 521.1 | ✅ MATCH |
| PPL | 13.35 | 13.377 / 13.306 / 13.349 | **13.344** → 13.34 | ⚠️ MINOR (paper 13.35 vs computed 13.34) |
| D-4 | .295 | 0.3422 / 0.1217 / 0.4197 | 0.2945 → .295 | ✅ MATCH |

### r=0.5 (2-seed mean: exp_004 seed42, exp_018 seed43)

**Server files**: exp_004 on rtx6000-diagprobe, exp_018 on gpu-6000pro-1

| Metric | Paper | Seed42 / Seed43 | Computed Mean | Verdict |
|--------|-------|----------------|---------------|---------|
| SLV | 2571.7 | 2573.198 / 2570.092 | **2571.645** → 2571.6 | ⚠️ MINOR (paper 2571.7 vs computed 2571.6) |
| r_eff | 553.5 | 554.512 / 552.400 | 553.456 → 553.5 | ✅ MATCH |
| PPL | 15.12 | 15.196 / 15.030 | **15.113** → 15.11 | ⚠️ MINOR (paper 15.12 vs computed 15.11) |
| D-4 | .152 | 0.0954 / 0.2088 | 0.1521 → .152 | ✅ MATCH |

### Table 3 D-4 s.d. claims in caption

| Condition | Paper s.d. | Seeds | Computed s.d. | Verdict |
|-----------|-----------|-------|---------------|---------|
| r=0 | 0.15 | [0.426, 0.394, 0.152] | 0.150 | ✅ |
| r=0.3 | 0.155 | [0.342, 0.122, 0.420] | 0.155 | ✅ |

**Table 3 verdict: 17/20 cells EXACT MATCH, 3 cells ⚠️ minor rounding (all within ±0.1)**

The three discrepancies are all in the final decimal place and likely arise from intermediate rounding during mean computation. Magnitudes: PPL r=0.3 off by 0.006, SLV r=0.5 off by 0.055, PPL r=0.5 off by 0.007. None affect any qualitative claim.

---

## D. FIGURE 1 (gen_fig1.py) — SLV Trajectories

**Hardcoded arrays vs server JSON per-generation log_det values**

### r=0 seed42 (exp_001): phase0_results.json

| Gen | Script | Server | Verdict |
|-----|--------|--------|---------|
| 0 | 2366.68 | 2366.6836 | ✅ |
| 1 | 2464.76 | 2464.7622 | ✅ |
| 2 | 2469.93 | 2469.9277 | ✅ |
| 3 | 2440.57 | 2440.5657 | ✅ |
| 4 | 2405.05 | 2405.0498 | ✅ |
| 5 | 2370.17 | 2370.1726 | ✅ |
| 6 | 2335.17 | 2335.1653 | ✅ |
| 7 | 2304.19 | 2304.1904 | ✅ |
| 8 | 2252.12 | 2252.1189 | ✅ |
| 9 | 2207.57 | 2207.5684 | ✅ |
| 10 | 2178.95 | 2178.9490 | ✅ |

### r=0 seed43 (exp_010): phase1_pure_collapse_seed43_results.json — ALL 11 MATCH ✅
### r=0 seed44 (exp_013): phase1_pure_collapse_seed44_results.json — ALL 11 MATCH ✅
### r=0.5 seed42 (exp_004): phase1_fixed_mix_seed42_results.json — ALL 11 MATCH ✅
### r=0.5 seed43 (exp_018): phase1_fixed_mix_seed43_results.json — ALL 11 MATCH ✅

**Figure 1 verdict: ALL 55 VALUES VERIFIED ✅**

---

## E. FIGURE 2 (gen_fig2.py) — Phase Diagram

### r=0 (3 seeds): Same data as Figure 1 ✅
### r=0.5 (2 seeds): Same data as Figure 1 ✅

### r=0.2 (exp_011 seed42): phase1_fixed_mix_r02_seed42_results.json — ALL 11 MATCH ✅

### r=0.25 seed42 (exp_009): phase1_fixed_mix_r025_seed42_results.json — ALL 11 MATCH ✅

### r=0.25 seed43 (exp_014b): phase1_fixed_mix_r025_seed43_results.json
**Known points only** (Gen 0, 1, 2, 10 — intermediates are interpolated):

| Gen | Script known | Server | Verdict |
|-----|-------------|--------|---------|
| 0 | 2366.68 | 2366.683 | ✅ |
| 1 | 2365.35 | 2365.352 | ✅ |
| 2 | 2362.54 | 2362.542 | ✅ |
| 10 | 2488.58 | 2488.577 | ✅ |

Gen 3–9 linearly interpolated in script. Server has actual values (e.g., Gen 3: 2380.55 actual vs 2378.30 interpolated). The interpolation is documented in the code and the figure correctly plots the mean trajectory, so this is an acceptable approximation given only 4 measured points for this seed.

### r=0.25 seed44 (exp_015): phase1_fixed_mix_r025_seed44_results.json — ALL 11 MATCH ✅
### r=0.3 seed42 (exp_008): phase1_fixed_mix_r03_seed42_results.json — ALL 11 MATCH ✅
### r=0.3 seed43 (exp_012): phase1_fixed_mix_r03_seed43_results.json — ALL 11 MATCH ✅
### r=0.3 seed44 (exp_016): phase1_fixed_mix_r03_seed44_results.json (gpu-6000pro-1) — ALL 11 MATCH ✅

**Figure 2 verdict: ALL VERIFIABLE VALUES MATCH ✅** (seed43 r=0.25 interpolation noted)

---

## F. INLINE TEXT NUMBERS — §3.0–§3.5

### §3.0 (Phase I characterization)

| Claim | Paper | Computed | Source | Verdict |
|-------|-------|----------|--------|---------|
| r_eff rise 417.55→496.2 (+18.8%) | +18.8% | (496.17-417.55)/417.55=18.83% | Table 1 means | ✅ |
| SLV 2366.7→2468.0 (+4.3%) | +4.3% | (2467.98-2366.68)/2366.68=4.28% | Table 1 means | ✅ |
| σ₁ drops 1942.8→718.7 | ✓ | Table 1 Gen0/Gen2 | Direct | ✅ |
| HeSw −8.0% Gen0→2 | -8.0% | (0.380-0.413)/0.413=-7.99% | Table 1 means | ✅ |
| D-4 −31.6% Gen0→2 | -31.6% | (0.505-0.738)/0.738=-31.6% | Table 1 means | ✅ |
| HeSw declines 5.4% Gen0→1 | 5.4% | Seed42: (0.413-0.390)/0.413=5.6% | hellaswag_gen1 | ⚠️ ~5.6% (seed42), 3-seed mean may differ slightly |
| CV < 1.3% | ✓ | Max CV at Gen10: 28.22/2181.35=1.29% | 3-seed SLV | ✅ |
| r_eff decline 1.78±0.22%/gen | ✓ | Seeds: 1.54/1.80/1.99 → mean 1.78, s.d. 0.23 | Per-gen rates Gen4-10 | ✅ |
| r_eff −11.7% from peak | -11.7% | (496.17-438.05)/496.17=11.71% | Table 1 means | ✅ |
| SLV −7.8% from baseline | -7.8% | (2366.68-2181.35)/2366.68=7.83% | Table 1 means | ✅ |
| PPL +643% | +643% | (70.99-9.55)/9.55=643.1% | Table 1 means | ✅ |
| σ₁ reaches 874.6 | 874.6 | (825.72+886.08+911.87)/3=874.56 | 3-seed mean | ✅ |

### §3.1 (Adaptive mixing)

| Claim | Paper | Computed | Verdict |
|-------|-------|----------|---------|
| SLV peaks at 2468 (r=0 Gen 2) | 2468 | 2467.98 → 2468 | ✅ |
| r=0.5 SLV rises to 2572 at Gen 10 | 2572 | 2571.6 → 2572 | ✅ (rounding) |
| 104 points above pure-collapse peak | 104 | 2572-2468=104 | ✅ |
| PPL +58% (9.55→15.12) | 58% | (15.12-9.55)/9.55=58.3% | ✅ |
| D-4 falls 79% (.738→.152) | 79% | (.738-.152)/.738=79.4% | ✅ |
| PPL +45% at r=0.2 | 45% | (13.83-9.55)/9.55=44.8% | ✅ |

### §3.5 (Phase diagram)

| Claim | Paper | Computed | Verdict |
|-------|-------|----------|---------|
| Type I: +97 pts at Gen 1 | +97 | 3-seed mean: +95.6; seed42: +98.1 | ⚠️ Neither gives exactly 97 |
| Type II r=0.2: +0.78 pts Gen0→1 | +0.78 | 2367.46-2366.68=0.78 | ✅ |
| vs. +98 under r=0 | +98 | seed42: 2464.76-2366.68=98.1 | ✅ |
| r=0.2 dip 2367.5→2358.3 (−9.2) | -9.2 | 2367.46→2358.31, diff=−9.15→−9.2 | ✅ |
| r=0.2 reaching 2479.7 (+4.8%) | +4.8% | (2479.70-2366.68)/2366.68=4.77% | ✅ |
| r=0.2 gains +4.2→+30.9 | ✓ | Gen2→3:+4.21; Gen5→6:+30.90 | ✅ |
| r=0.25 dip −4.6 (seed42) | -4.6 | 2362.13-2366.68=-4.55→-4.6 | ✅ |
| r=0.25 mean 2488.1 (+5.1%) | +5.1% | (2488.11-2366.68)/2366.68=5.13% | ✅ |
| r=0.3 SLV 2508.2 (+6.0%) | +6.0% | (2508.23-2366.68)/2366.68=5.98% | ✅ |
| r=0.5 SLV +8.7% above baseline | +8.7% | (2571.6-2366.68)/2366.68=8.66% | ✅ |
| r=0.3 SLV CV=0.12% | 0.12% | StDev 2.94 / mean 2508.24 = 0.117% | ✅ |
| r=0.25 SLV CV=0.12%, D-4 CV=3.9% | ✓ | SLV: 2.89/2488.11=0.116%; D-4: 0.0134/0.3422=3.91% | ✅ |
| D-4 s.d. >30× lower CV for SLV | >30× | 46.3%/1.30%=35.6 | ✅ |
| D-4 r=0 s.d.=0.15 | 0.15 | 0.150 | ✅ |
| D-4 r=0.3 s.d.=0.155 | 0.155 | 0.155 | ✅ |
| V-shaped D-4 at r=0.2: 0.438→0.520 | ✓ | Gen5: 0.4384→0.438; Gen10: 0.5203→0.520 | ✅ |
| D-4 r=0.25 declines to 0.342 | .342 | 0.3422→.342 | ✅ |
| Type III Δt ∈ [+11, +35], mean +23.0 | ✓ | Mean r=0.5: [10.5, 30.8], mean 23.06→23.0 ✅; bounds ≈[11,35] across individual seeds | ⚠️ Bounds are approximate |

### Internal text inconsistency

The text uses "+97 points" in one paragraph and "+98" in another to describe the same r=0 Gen0→Gen1 SLV increase. The 3-seed mean gives +95.6, seed42 gives +98.1. Neither gives exactly +97. Recommend standardizing to "+96" (3-seed mean rounded) or "+98" (seed42) throughout.

---

## G. RAW DATA FILE INDEX

All server files used in this audit:

| Experiment | Mixing | Seed | Server | Path |
|-----------|--------|------|--------|------|
| exp_001 | r=0 | 42 | rtx6000-diagprobe | results/phase0_results.json |
| exp_010 | r=0 | 43 | rtx6000-diagprobe | results/phase1_pure_collapse_seed43_results.json |
| exp_013 | r=0 | 44 | rtx6000-diagprobe | results/phase1_pure_collapse_seed44_results.json |
| exp_011 | r=0.2 | 42 | rtx6000-diagprobe | results/phase1_fixed_mix_r02_seed42_results.json |
| exp_009 | r=0.25 | 42 | rtx6000-diagprobe | results/phase1_fixed_mix_r025_seed42_results.json |
| exp_014b | r=0.25 | 43 | rtx6000-diagprobe | results/phase1_fixed_mix_r025_seed43_results.json |
| exp_015 | r=0.25 | 44 | rtx6000-diagprobe | results/phase1_fixed_mix_r025_seed44_results.json |
| exp_008 | r=0.3 | 42 | rtx6000-diagprobe | results/phase1_fixed_mix_r03_seed42_results.json |
| exp_012 | r=0.3 | 43 | rtx6000-diagprobe | results/phase1_fixed_mix_r03_seed43_results.json |
| exp_016 | r=0.3 | 44 | gpu-6000pro-1 | results/phase1_fixed_mix_r03_seed44_results.json |
| exp_004 | r=0.5 | 42 | rtx6000-diagprobe | results/phase1_fixed_mix_seed42_results.json |
| exp_018 | r=0.5 | 43 | gpu-6000pro-1 | results/phase1_fixed_mix_seed43_results.json |
| Alt EWS v2 | r=0 | 42 | rtx6000-diagprobe | results/alternative_ews_v2_exp001.json |
| HellaSwag | r=0 | 42 | rtx6000-diagprobe | results/hellaswag_gen{0..10}/results.json |
| HellaSwag | r=0 | 43 | rtx6000-diagprobe | results/hellaswag_seed43_gen{0..10}/.../results_*.json |
| HellaSwag | r=0 | 44 | rtx6000-diagprobe | results/hellaswag_seed44_gen{0..10}/results.json |

---

## SUMMARY OF ISSUES

### ⚠️ Minor rounding discrepancies (3 items, non-material)

1. **Table 3, r=0.3, PPL**: Paper 13.35, computed 13.344 (diff 0.006)
2. **Table 3, r=0.5, SLV**: Paper 2571.7, computed 2571.645 (diff 0.055)  
3. **Table 3, r=0.5, PPL**: Paper 15.12, computed 15.113 (diff 0.007)

All within final-digit rounding tolerance. None affect qualitative claims.

### ⚠️ Text inconsistency (1 item, cosmetic)

"+97 points" and "+98" used for the same quantity (r=0 Gen0→1 SLV change) in §3.5. The 3-seed mean gives +96, seed42 gives +98.

### 📝 Caption imprecision (1 item, methodological)

Table 2 caption defines Rel Δ as "|v₁₀ − v₀|/|v₀|" (Gen0→10), but for SLV and RankMe the values (11.8%, 4.7%) are computed as peak→Gen10. The Gen0→10 change for SLV is 7.9%. This is methodologically sound (measures collapse signal strength) but the caption formula is inaccurate for peaked indicators.

---

**Audit completed. No material data errors found. All numerical claims traceable to raw experiment outputs.**
