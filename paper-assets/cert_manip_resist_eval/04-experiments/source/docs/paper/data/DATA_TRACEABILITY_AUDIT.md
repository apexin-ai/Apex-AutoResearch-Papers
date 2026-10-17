# Data Traceability Audit Report
Generated: 2026-05-23

---

## Summary

| Category | Count |
|----------|-------|
| Verified consistent (V2 data = paper) | 47 |
| V1->V2 pending update (Paper Agent working) | 52 |
| Internal inconsistency (paper self-contradicts) | 5 |
| Unable to trace (no corrected JSON available) | 14 |
| **Total numerical claims audited** | **118** |

---

## CRITICAL: V1->V2 Pending Updates (Paper Agent is processing)

### Table 1 — results.tex lines 16-28 (6 cells wrong)

The paper's Table 1 uses a mix of V1 data. V2 corrected values from `table1_corrected.json`:

| Condition | Paper (current) | V2 corrected | Status |
|-----------|----------------|--------------|--------|
| MMLU Score manip. | eta n.s. / keff n.s. / -- | eta n.s. / keff +* / K | V1 |
| MMLU Position bias | eta +* / keff n.s. / eta | eta +* / keff +* / Co | V1 |
| MMLU Authority bias | eta +* / keff n.s. / eta | eta +* / keff +* / Co | V1 |
| ARC Sycophancy | eta +* / keff -* / Co | eta +* / keff +* / Co | V1 |
| ARC Score manip. | eta n.s. / keff +* / K | eta +* / keff +* / Co | V1 |
| ARC Verbosity | eta +* / keff n.s. / eta | eta +* / keff +* / Co | V1 |

**V2 summary counts**: eta 10/12 sig, keff **12/12 all positive**, dominance Co:10, K:2, eta:**0**

Paper summary counts (results.tex:35): eta 9/12, keff 7+/1-, dominance 3eta/6Co/2K/1--

Source: `table1_corrected.json` -> `summary.new_dominance_dist`, per-condition `new` fields

### Table 2 — results.tex lines 91-94 (ALL 4 rows wrong)

| Method | Paper | V2 corrected | Fields changed |
|--------|-------|--------------|----------------|
| Threshold | 12/12, 11/12, 10+/1-, R2=0.89 | 12/12, 11/12, **11+/0-**, R2=**0.829** | dir, R2 |
| Majority | 9/12, 8/12, 7+/1-, R2=0.298 | **10/12**, **12/12**, **12+/0-**, R2=**0.327** | eta, keff, dir, R2 |
| Weighted | 9/12, 9/12, 9+/0-, R2=0.284 | 9/12, **12/12**, **12+/0-**, R2=**0.328** | keff, dir, R2 |
| Bayesian | 9/12, 7/12, **1+/6-**, R2=0.104 | 9/12, **6/12**, **5+/1-**, R2=**0.087** | keff, dir, R2 |

Source: `table2_corrected.json` -> `aggregation_methods.{method}.new`

### Regime Transition Numbers (scattered across 6+ locations)

V2 from `regime_transition_corrected.json`:

| K | Predictor | Paper | V2 | Locations |
|---|-----------|-------|----|-----------|
| 3 | eta | 5/12 | **3/12** | results.tex:56,60; intro.tex:20; appendix.tex:305; main.tex:40 |
| 3 | keff | 1/12 | **4/12** | results.tex:56,60; intro.tex:20; appendix.tex:37,305 |
| 5 | keff | 7/12 | **10/12** | results.tex:56,60; intro.tex:20; appendix.tex:115,246,305; main.tex:40 |
| 7 | keff | 5/12 | **9/12** | results.tex:60; main.tex:40 |

### GAM 6:6 Split Claims (DEAD in V2 - 6 locations)

V2 `gam_bootstrap_ci_k3.json`: ALL 12 conditions show **positive** direction (direction_positive_rate 0.89-1.0). `taxonomy_split.all_shared_negative = false`, `split_consistency_rate = 0.0`.

V2 `gam_bootstrap_ci_k5.json`: ALL 12 conditions direction_positive_rate = **1.0**.

The paper claims "shared-bias attacks show negative K_eff" — this is FALSE in V2.

| Location | Current claim | V2 reality |
|----------|--------------|------------|
| abstract.tex:3 | "decreased vulnerability for shared-bias attacks" | All 12 positive |
| introduction.tex:14 | "decreased vulnerability for shared-bias attacks" | All 12 positive |
| introduction.tex:21 | "GAM reveals a 6:6 split" | No split; 12/12 positive |
| results.tex:71 | "shared-bias attacks show negative K_eff" | All positive |
| results.tex:77 | "12 conditions split 6:6 by attack mechanism" | 12/12 positive |
| analysis.tex:8 | "6:6 directional split" | No split |

Note: main.tex abstract already says "K_eff is uniformly positively associated" — consistent with V2, but contradicts the body.

### Bayesian Reversal Claims (DEAD in V2 - 6 locations)

V2 `table2_corrected.json`: Bayesian dir = **5+/1-** (mostly positive), NOT 1+/6- (mostly negative).

| Location | Current claim | V2 reality |
|----------|--------------|------------|
| abstract.tex:3 | "sign change in diversity channel" | 5+/1-, no dramatic sign change |
| introduction.tex:17 | "sign change at K=3" | 5+/1-, not a sign change |
| introduction.tex:22 | "Bayesian reversal" | No reversal |
| results.tex:102 | "shifts from 7+/1- to 1+/6-" | Should be "12+/0- to 5+/1-" |
| analysis.tex:21 | "reversal of K_eff's direction at K=3 (6/7 negative)" | 1/6 negative, not 6/7 |
| appendix.tex:43 | "6 of 7 significant coefficients negative" | 1/6 negative |
| appendix.tex:48 (Fig.3 caption) | "1 positive, 6 negative" vs "7 positive, 1 negative" | Bayesian 5+/1- vs Majority 12+/0- |
| conclusion.tex:3 | "sign change at K=3" | No sign change |

### RF Contrast Numbers — results.tex:63-65

| Claim | Paper | V2 corrected | Source |
|-------|-------|--------------|--------|
| K5 adaptive R2 | 0.256 | **0.2751** | `random_fault_contrast_corrected.json` -> new_results.k5_adaptive_mean_r2 |
| K5 keff retains (sig count) | 7/12 | **10/12** | `regime_transition_corrected.json` -> K5.keff_sig |
| K3 adaptive keff collapse | 1/12 | **4/12** | `regime_transition_corrected.json` -> K3.keff_sig |
| K3 RF-adaptive gap | ~0.6 | **~0.45** | RF mean 0.774 - adaptive mean ~0.327 = 0.447 |
| K5 RF-adaptive gap | 0.45 | **0.43** | `random_fault_contrast_corrected.json` -> new_results.rf_vs_adaptive_gap=0.4296 |

### Text Summaries with V1 Numbers

| Location | Paper text | V2 value | Source |
|----------|-----------|----------|--------|
| results.tex:35 | "eta sig in 9/12" | 10/12 | table1_corrected -> summary.eta_sig_count_new |
| results.tex:35 | "keff sig positive in 7/12, negative in 1" | 12/12 positive, 0 negative | table1_corrected -> summary.keff_sig_count_new |
| results.tex:35 | "3 eta-dominant, 6 co-dominant, 2 K-dominant, 1 neither" | 0 eta, 10 Co, 2 K, 0 neither | table1_corrected -> summary.new_dominance_dist |
| results.tex:35 | "exceptions: MMLU score manip, ARC score manip, ARC position" | exceptions: MMLU score manip, ARC position (only 2) | table1_corrected -> per-condition new.eta_sig |
| results.tex:37 | "eta remains robust (8/12 clustered, 5/12 bootstrap)" | bootstrap eta K3=3/12 | regime_transition_corrected -> K3.eta_sig |
| results.tex:37 | "keff collapses (0/12 and 1/12)" | bootstrap keff K3=4/12 | regime_transition_corrected -> K3.keff_sig |
| results.tex:37 | "CIs contain zero in 11/12 conditions" | 8/12 (keff sig in 4) | regime_transition_corrected -> K3.keff_sig=4 |
| related_work.tex:10 | "OLS significance collapses after correction (8/12->1/12)" | OLS 12/12 -> bootstrap 4/12 | table1+regime_transition corrected |
| appendix.tex:28-29 | "eta sig in 9 of 12... keff positively associated in 7" | OLS: eta 10/12, keff 12/12 | table1_corrected |
| appendix.tex:29 | "eta 5 to 8/12; keff 0-1/12" | eta bootstrap 3/12; keff 4/12 | regime_transition_corrected |
| appendix.tex:31 | "sole negative keff: ARC sycophancy (beta=-0.192)" | ARC sycophancy keff=+0.257 (positive in V2) | table1_corrected -> arc_sycophancy.new.keff_beta_std |
| appendix.tex:55 | "K5 majority keff dominates (7/12)" | 10/12 | regime_transition_corrected -> K5.keff_sig |
| appendix.tex:115 | "Full bootstrap... keff 7/12" | 10/12 | regime_transition_corrected |
| appendix.tex:64 (K5 table) | "Majority 0/12, 7/12, R2=0.256" | eta unknown, keff 10/12 majority, R2~0.275 | regime_transition + random_fault_contrast |
| introduction.tex:20 | "eta 5/12, keff 1/12, MDE=0.14" | eta 3/12, keff 4/12, MDE=0.14 | regime_transition + power_analysis |
| introduction.tex:20 | "K>=5: 7/12, eta 0/12" | 10/12, eta 0/12 | regime_transition_corrected |
| introduction.tex:21 | "11/12 consistent at K=5" | 12/12 all positive at K=5 | gam_bootstrap_ci_k5 |

### Appendix K5 Aggregation Table — appendix.tex lines 60-69

Paper shows:
```
Majority:   0/12, 7/12, R2=0.256
Weighted:   1/12, 9/12, R2=0.249
Threshold:  6/12, 10/12, R2=0.506
Bayesian:   1/12, 0/12, R2=0.081
```

Majority keff should be 10/12 per `regime_transition_corrected.json`. Majority R2 should be ~0.275 per `random_fault_contrast_corrected.json`. Other rows: no separate corrected JSON available; likely also V1.

---

## Internal Inconsistencies (paper contradicts itself)

### 1. main.tex abstract vs Table 1

- **Abstract** (main.tex:27): "K_eff is **uniformly positively** associated with vulnerability across all 12 conditions"
- **Table 1** (results.tex:24): ARC Sycophancy shows keff **-*** (negative significant)

These cannot both be true. Abstract reflects V2 (all positive); Table 1 is V1.

### 2. main.tex abstract vs Table 2 R2

- **Abstract** (main.tex:27): "R2=0.83" (threshold), "R2=0.09" (Bayesian)
- **Table 2** (results.tex:91-94): R2=0.89 (threshold), R2=0.104 (Bayesian)

Abstract uses V2 values; Table 2 uses V1 values.

### 3. abstract.tex vs main.tex abstract

- **abstract.tex:3**: "higher diversity is associated with... decreased vulnerability for shared-bias attacks"
- **main.tex:27**: "K_eff is uniformly positively associated with vulnerability across all 12 conditions"

These are contradictory. abstract.tex has not been synced with main.tex.

### 4. Introduction framing vs Abstract framing

- **Introduction:20**: "eta dominates at K=3 (bootstrap 5/12, K_eff 1/12)" — V1 framing where eta dominates
- **Abstract**: "at K=3, both contribute (co-determination)" — V2 framing where both contribute

### 5. Introduction "11/12 at K=5" vs V2 GAM data

- **Introduction:21**: "11/12 consistent at K=5" (implies 1 condition disagrees)
- **V2 GAM K=5**: 12/12 all positive direction_positive_rate=1.0 (no exception)

---

## Verified Consistent (V2 data = paper)

### Panel & Design Parameters
- [15 models] <- stochastic_dominance_analysis.json: n_judges=15
- [6 attack types, 2 benchmarks] <- experimental design, consistent throughout
- [K in {3,5,7}] <- used consistently
- [455 panels at K=3] <- keff_distribution_corrected.json: K3.n_panels=455
- [3,003 panels at K=5] <- keff_distribution_corrected.json: K5.n_panels=3003
- [6,435 panels at K=7] <- keff_distribution_corrected.json: K7.n_panels=6435
- [C(14,2)=91 panels per judge] <- combinatorial identity, correct
- [B=9999 bootstrap resamples] <- regime_transition_corrected.json: correct
- [epsilon=10^-6] <- epsilon_sensitivity.json: correct

### Stochastic Dominance (threat_model.tex:24)
- [58% dominant (61/105)] <- stochastic_dominance_analysis.json: dominant_pct=58.1, dominant=61, total=105
- [72.1% non-dominant within-tier (31/43)] <- stochastic_dominance_analysis.json: within_tier.non_dominant_pct=72.1 (updated 2026-05-24: tier scheme unified with paper Table 1)
- [21.0% non-dominant cross-tier (13/62)] <- stochastic_dominance_analysis.json: cross_tier.non_dominant_pct=21.0 (updated 2026-05-24: tier scheme unified with paper Table 1)
- [frontier: 4 models] <- stochastic_dominance_analysis.json: tier_sizes.frontier=4
- [mid: 2 models] <- stochastic_dominance_analysis.json: tier_sizes.mid=2
- [lightweight: 9 models] <- stochastic_dominance_analysis.json: tier_sizes.lightweight=9

### K_eff Distribution (appendix.tex:278-283)
- [K=3: mean 2.18 (SD 0.30), range [1.47, 2.80]] <- keff_distribution_corrected.json: K3 mean=2.1757, sd=0.3038, min=1.4705, max=2.7991
- [K=5: mean 3.35 (SD 0.42), range [2.16, 4.30]] <- keff_distribution_corrected.json: K5 mean=3.3514, sd=0.4213, min=2.1628, max=4.2963
- [K=7: mean 4.53 (SD 0.47), range [2.97, 5.55]] <- keff_distribution_corrected.json: K7 mean=4.5271, sd=0.4746, min=2.9749, max=5.5453

### Power Analysis MDEs (appendix.tex:299-305, results.tex:46)
- [K=3 MDE=0.144] <- power_analysis_all_K.json: K3.MDE_80=0.14387
- [K=5 MDE=0.048] <- power_analysis_all_K.json: K5.MDE_80=0.04780
- [K=7 MDE=0.036] <- power_analysis_all_K.json: K7.MDE_80=0.03575

### Random Fault Contrast (results.tex:63-64)
- [K=3 RF R2 = 0.73-0.81] <- random_fault_contrast_corrected.json: rf_r2_by_condition.k3.mmlu=0.7344, arc=0.8133
- [K=3 RF keff 2/2 significant] <- random_fault_contrast_corrected.json: rf_r2_by_condition.k3.keff_bootstrap_sig="2/2"
- [K=5 RF R2 = 0.705] <- random_fault_contrast_corrected.json: rf_r2_by_condition.k5.mean=0.7047
- [K=5 RF keff 2/2 significant] <- random_fault_contrast_corrected.json: rf_r2_by_condition.k5.keff_bootstrap_sig="2/2"

### Temperature Pilot (appendix.tex:264)
- [max K_eff delta < 0.034 (MMLU: 0.033, ARC: 0.027)] <- temperature_pilot_summary.json: keff_delta.mmlu=0.0332, arc=0.027

### Epsilon Sensitivity (appendix.tex:259)
- [K=5: all K_eff directions preserved across epsilon values] <- epsilon_sensitivity_k5.json: all keff_beta_std positive at all 3 epsilon levels
- [K=5: max delta_beta_std = 0.067] <- epsilon_sensitivity_k5.json: max keff difference between 1e-6 and 1e-9 = 0.0671 (mmlu_authority_bias)
- [K=3: max delta_beta_std = 0.10] <- epsilon_sensitivity.json: max keff difference between 1e-6 and 1e-9 = 0.1017 (arc_score_manipulation)

### Aggregation R2 Bootstrap CIs (from aggregation_r2_bootstrap.json)
- V2 R2 values confirmed by bootstrap:
  - Majority R2=0.327 [0.309, 0.351]
  - Weighted R2=0.328 [0.311, 0.352]
  - Threshold R2=0.829 [0.806, 0.859]
  - Bayesian R2=0.087 [0.077, 0.106]

### main.tex Abstract (V2-aligned claims)
- [K_eff uniformly positively associated across all 12] <- gam_bootstrap_ci_k3 + k5: all positive
- [R2=0.83 threshold] <- aggregation_r2_bootstrap: threshold R2=0.829
- [R2=0.09 Bayesian] <- aggregation_r2_bootstrap: bayesian R2=0.087
- [K>=5: K_eff sole significant, eta drops to 0] <- regime_transition_corrected: K5 eta=0, keff=10/12

### Attacked K_eff Stability (appendix.tex:147-156)
- [rho>=0.91 for 4 attacks] <- not affected by V1/V2 (computed from clean MI)
- [position bias rho=0.08 on ARC] <- structural, unchanged

### K3 Attack Type Distribution
- [All 4 K3-significant conditions are shared_bias type] <- k3_attack_type_distribution.json: all_4_significant_are_shared_bias=true
- [Mann-Whitney p=0.147] <- k3_attack_type_distribution.json: mann_whitney_u_test.p_value=0.147

---

## Unable to Trace (no V2 corrected JSON available)

These numbers appear in the paper but have no corresponding corrected JSON data file. Some may have changed with V2; others are structural properties unaffected by the bug fix.

| Claim | Location | Likely V2-affected? |
|-------|----------|-------------------|
| r=0.70 K_eff-eta correlation at K=3 | analysis.tex:11, conclusion.tex:3 | Possibly (regression-derived) |
| r=0.81 correlation at K=5 | analysis.tex:11 | Possibly |
| r=0.85 API-only correlation | analysis.tex:11, appendix.tex:116 | Possibly |
| r=0.50 Cap-matched Pool A | analysis.tex:11, appendix.tex:117 | Possibly |
| VIF=4.4 API-only | appendix.tex:126 | Possibly |
| 93.1% fractional logit concordance | appendix.tex:259, appendix.tex:122 | Possibly |
| 51.4% K_eff dominant in random subsamples | appendix.tex:131 | Possibly |
| Cinelli-Hazlett RV values (36 conditions) | appendix.tex:170-212 | Yes (regression-derived) |
| 28/36 confound exceeds RV | appendix.tex:218, analysis.tex:11 | Yes |
| 1/12->3/12->4/12 RV progression | appendix.tex:218, analysis.tex:11 | Yes |
| Cross-benchmark 14/18 and 10/18 | appendix.tex:230 | Possibly |
| r~0.76-0.78 cross-benchmark | appendix.tex:230 | Possibly |
| Pool A: 6/12 (5/12 conservative) RV>eta | appendix.tex:248, analysis.tex:11 | Yes |
| K5 aggregation table (weighted/threshold/bayesian rows) | appendix.tex:64-68 | Likely |

---

## Coverage Statistics

| Metric | Count |
|--------|-------|
| Total unique numerical claims in paper | ~118 |
| Traced to V2 JSON and verified correct | 47 (40%) |
| Traced to V2 JSON, found V1->V2 mismatch | 52 (44%) |
| Paper internally inconsistent | 5 (4%) |
| No corrected JSON available for verification | 14 (12%) |

### V1->V2 Impact by Section

| Section | V1 items | Critical? |
|---------|----------|-----------|
| Table 1 (results.tex) | 6 cells + 4 summary stats | YES - core result |
| Table 2 (results.tex) | 4 rows (all wrong) | YES - core result |
| GAM 6:6 split (6 locations) | 6 claims | YES - contribution #2 |
| Bayesian reversal (8 locations) | 8 claims | YES - contribution #3 |
| Regime transition (4 K-values x multiple locations) | ~15 instances | YES - contribution #1 |
| RF contrast R2 | 5 values | Moderate |
| Abstract/intro framing | ~8 claims | YES - first impression |
| Appendix tables & text | ~10 values | Low-moderate |

### Data Files Fully Consumed

All 15 V2 corrected JSON files were read and cross-referenced:
- table1_corrected.json
- table2_corrected.json
- regime_transition_corrected.json
- gam_bootstrap_ci_k3.json
- gam_bootstrap_ci_k5.json
- random_fault_contrast_corrected.json
- aggregation_r2_bootstrap.json
- k3_attack_type_distribution.json
- gam_magnitude_gradient.json
- epsilon_sensitivity.json
- epsilon_sensitivity_k5.json
- keff_distribution_corrected.json
- temperature_pilot_summary.json
- power_analysis_all_K.json
- stochastic_dominance_analysis.json

---

## Recommended Priority for Paper Agent

1. **P0**: Update Table 1 and Table 2 with V2 values (core tables)
2. **P0**: Kill "6:6 split" language everywhere (6 locations) and replace with "12/12 all positive"
3. **P0**: Kill "Bayesian reversal" / "sign change" language (8 locations) and reframe as "5+/1- partial modulation"
4. **P0**: Update all regime transition counts (K3 eta 5->3, keff 1->4; K5 keff 7->10; K7 keff 5->9)
5. **P0**: Sync abstract.tex with main.tex abstract
6. **P1**: Update RF contrast R2 (0.256->0.275, gap ~0.6->~0.45)
7. **P1**: Update introduction contribution bullets and conclusion with V2 numbers
8. **P1**: Update appendix text and tables (OLS counts, K5 aggregation table, etc.)
9. **P2**: Re-derive Cinelli-Hazlett, cross-benchmark, and robustness check numbers with V2 data
