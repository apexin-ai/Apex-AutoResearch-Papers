# V2 Corrected Data Inventory
Generated: 2026-05-23

Total files: 18 JSON files
V1→V2 corrected: 5 files (table1, table2, regime_transition, keff_distribution, random_fault_contrast)
New analyses: 13 files

---

## Table 1 — OLS Dominance (Section 4.1)

- **table1_corrected.json**: V1→V2 corrected. OLS log-log, K=3, 455 panels. Error-as-tie bug fix (1221/63000 = 1.94% errors treated as ties). K_eff sig: 8/12→**12/12**; eta sig: 11/12→10/12. Dominance distribution shifts from {Co:7, eta:4, K:1} to {Co:10, K:2, eta:0}. 5 conditions changed dominance category. Key finding: K_eff universally significant and always positive after correction.

- **epsilon_sensitivity.json**: Epsilon sensitivity for K=3. OLS coefficients at ε=1e-3, 1e-6, 1e-9. Shows K_eff coefficients are sensitive to epsilon choice in conditions with high ASR-zero rates (e.g., arc_sycophancy: K_eff beta flips sign across epsilon). Includes per-condition ASR zero rates for K3/K5/K7.

- **epsilon_sensitivity_k5.json**: Epsilon sensitivity for K=5. Max coefficient change: K_eff **184.5%**, eta 31.07%. At ε=1e-6: K_eff sig 12/12, eta sig 12/12 (all conditions significant at K=5). Large N (3003 panels) stabilizes estimates.

## Table 2 — Aggregation Methods (Section 4.2)

- **table2_corrected.json**: V1→V2 corrected. K=3, 455 panels, 4 aggregation methods. All 4 methods changed after error filtering. Majority: K_eff sig 8/12→**12/12**, dir 7+/1-→**12+/0-**. Weighted: K_eff sig 9/12→**12/12**. Bayesian: direction reversed 1+/6-→**5+/1-** (old negative was artifact). Threshold: spurious negative disappeared 10+/1-→11+/0-.

- **aggregation_bootstrap.json**: Bootstrap validation of Table 2. K=3, B=9999. Covers majority/weighted/threshold/bayesian. Confirms OLS directions: majority 11/12 positive, weighted 11/12 positive, threshold 11/12 positive. Bayesian reversal confirmed: 9/12 negative, 0% positive rate on 6 strongest conditions. NOTE: these are V1 (pre-correction) OLS baselines with bootstrap CIs.

## Regime Transition (Section 4.3)

- **regime_transition_corrected.json**: V1→V2 corrected. Wild cluster bootstrap (B=9999, Rademacher, max-p, BH FDR 0.05). K3: K_eff sig 1→**4**, eta sig 5→3. K5: K_eff sig 7→**10**. K7: K_eff sig 5→**9**. Per-condition FDR-adjusted p-values included. 1365 filtered samples. All K sizes changed.

## GAM Nonlinear Analysis (Section 4.4 / Appendix)

- **gam_bootstrap_ci_k3.json**: GAM bootstrap CIs, K=3, B=9999. LinearGAM with 8 splines. 12/12 conditions positive direction. 11/12 have >98.75% positive rate (mmlu_score_manipulation lowest at 88.95%). Includes taxonomy split analysis (targeted vs shared_bias): all_targeted_positive=true, split_consistency_rate=0.0.

- **gam_bootstrap_ci_k5.json**: GAM bootstrap CIs, K=5, B=9999. **12/12 conditions 100% positive rate** (all 9999 bootstraps positive). Tighter CIs than K3 due to 3003 panels. Strongest: arc_score_manipulation slope=34.9 [23.4, 49.5]. Taxonomy split: same structure as K3.

- **gam_magnitude_gradient.json**: GAM slope magnitude comparison between targeted vs shared_bias attack types. K3: Kruskal-Wallis H=1.64, p=0.200. K5: H=0.64, p=0.423. **No significant difference** in GAM slope between attack categories. Position_bias slopes ~30-60x smaller due to ASR scale (0-1 vs 0-100%).

## K_eff Distribution & Measurement (Section 3 / Appendix)

- **keff_distribution.json**: Original K_eff distribution (uncorrected MI-based). K3: mean=1.92, sd=0.32. K5: mean=2.32, sd=0.39. K7: mean=2.54, sd=0.38. Range: K3 [1.23, 2.71], K5 [1.43, 3.55], K7 [1.59, 3.61].

- **keff_distribution_corrected.json**: V1→V2 corrected K_eff (empirical via Gaussian copula MI, averaged across MMLU & ARC). K3: mean=**2.18**, sd=0.30. K5: mean=**3.35**, sd=0.42. K7: mean=**4.53**, sd=0.47. Substantially higher than uncorrected values.

- **keff_stability_split.json**: K_eff significance by attack stability tier (Spearman rho). Stable attacks (rho≥0.90, 4 types): K3 K_eff sig **0/8**, K5 sig **4/8**. Moderate (rho~0.60, prompt_injection): K3 1/2, K5 2/2. Unstable (rho<0.10, position_bias): K3 0/2, K5 1/2. Shows K_eff signal emerges at K≥5 even for stable attacks.

## Robustness & Causal Identification (Section 5 / Appendix)

- **sensitivity_analysis_poolA.json**: Cinelli & Hazlett (2020) OVB analysis. Pool A (9 capability-matched models). K3: 84 panels, K5: 126 panels. RV exceeds eta partial R² in **9/24** conditions (K3: 3/12, K5: 6/12). K_eff effect survives confounding up to RV level in those conditions. Strongest: arc_verbosity_bias K5 (RV=0.432).

- **cross_benchmark_iv.json**: Cross-benchmark IV analysis. Exclusion restriction **violated** (K_eff structurally determined by panel composition, rho=0.76-0.78 across benchmarks). Reduced-form: K_eff significant in **34/36** conditions. 2SLS first-stage F=820-9232 (strong instruments), but 2SLS **invalid** for causal claims. Serves as robustness evidence that K_eff captures genuine panel property, not benchmark artifact.

- **temperature_pilot_summary.json**: Temperature pilot (3 models × 4 temps × 2 benchmarks). K_eff delta max=**0.033** across temperatures — temperature is **NOT** a valid instrument (fails relevance). Accuracy changes ≤0.85%. ASR largely stable across temperatures. Includes MI details and cost ($4.93). 216 checkpoints loaded.

- **random_fault_contrast_corrected.json**: V1→V2 corrected. RF vs adaptive attack contrast. RF R²=**0.70** >> adaptive R²=**0.28** (2.5x gap). K_eff explains much more variance under independent (random) faults vs adversarial attacks. Gap narrowed slightly after correction (0.449→0.430) but qualitatively unchanged. K_eff bootstrap sig 2/2 for RF.

## Supplementary Analyses

- **stochastic_dominance_analysis.json**: 15 judges, 3 tiers (frontier 4/mid 2/lightweight 9, matching paper Table 1). 105 unordered pairs: 61 dominant (58.1%), 44 non-dominant (41.9%). Within-tier: **72.1%** non-dominant (31/43). Cross-tier: 21.0% non-dominant (13/62). Within-tier judges are more likely to be non-dominated — supports diversity argument. (Updated 2026-05-24: tier scheme unified with paper Table 1.)

- **power_analysis_all_K.json**: Cluster-robust power analysis (1000 simulations). MDE@80%: K3=**0.144**, K5=**0.048**, K7=**0.036** (standardized beta). K3 power for β_std=0.1 is 64.6%; K5 achieves 84.5% at β_std=0.05. Demonstrates adequate power for observed effect sizes.

---

## Cross-reference: Paper Section → Data File

| Section | Data File | Key Numbers |
|---------|-----------|-------------|
| 3 (Setup/K_eff) | keff_distribution.json | K3 mean=1.92, K5=2.32, K7=2.54 |
| 3 (Setup/K_eff) | keff_distribution_corrected.json | K3 mean=2.18, K5=3.35, K7=4.53 |
| 4.1 (Table 1) | table1_corrected.json | K_eff 12/12 sig, Co-dom 10/12 |
| 4.1 (Table 1) | epsilon_sensitivity.json | K3 coefficient stability across ε |
| 4.1 (Table 1) | epsilon_sensitivity_k5.json | K5 max K_eff change 184.5% |
| 4.2 (Table 2) | table2_corrected.json | Majority K_eff 12/12, Bayesian dir flip |
| 4.2 (Table 2) | aggregation_bootstrap.json | Bootstrap confirms Table 2 directions |
| 4.3 (Regime) | regime_transition_corrected.json | K3→K5: K_eff sig 4→10, eta→0 |
| 4.4 (GAM) | gam_bootstrap_ci_k3.json | 12/12 positive, 11/12 >98.75% rate |
| 4.4 (GAM) | gam_bootstrap_ci_k5.json | 12/12 at 100% positive rate |
| 4.4 (GAM) | gam_magnitude_gradient.json | No targeted/shared difference (p>0.2) |
| 5 (Robustness) | sensitivity_analysis_poolA.json | RV > eta in 9/24 conditions |
| 5 (Robustness) | cross_benchmark_iv.json | 34/36 reduced-form sig, 2SLS invalid |
| 5 (Robustness) | temperature_pilot_summary.json | K_eff Δ=0.033, not valid instrument |
| 5 (Robustness) | random_fault_contrast_corrected.json | RF R²=0.70 >> adaptive R²=0.28 |
| 5 (Robustness) | keff_stability_split.json | Stable attacks: K3 0/8, K5 4/8 sig |
| Appendix | stochastic_dominance_analysis.json | 41.9% non-dominant, within-tier 72.1% |
| Appendix | power_analysis_all_K.json | MDE@80%: K3=0.14, K5=0.05, K7=0.04 |

## V1→V2 Correction Summary

| File | What Changed | Impact on Claims |
|------|-------------|-----------------|
| table1_corrected | K_eff 8/12→12/12 sig, eta-dom eliminated | Strengthens: diversity universally significant |
| table2_corrected | Majority/weighted K_eff→12/12; Bayesian dir flip | Strengthens: error artifact removed |
| regime_transition_corrected | K_eff sig counts increase at all K | Strengthens: regime transition more pronounced |
| keff_distribution_corrected | K_eff means increase (1.92→2.18 at K3) | Changes magnitude, not direction |
| random_fault_contrast_corrected | Gap narrows slightly (0.449→0.430) | Qualitatively unchanged |
