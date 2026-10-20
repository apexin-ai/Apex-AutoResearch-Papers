# Data Audit Report

**Generated**: 2026-05-23
**Paper**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Target venue**: EMNLP 2026 ARR

## Summary

- **Total quantitative claims checked**: 127
- **Verified (registry/raw data match)**: 109
- **Discrepancy found**: 2
- **Cannot verify (no raw data access or derived)**: 16

### Critical Discrepancies

| # | Location | Issue | Severity |
|---|----------|-------|----------|
| D1 | §3.2, cross-model table | **Gemma DAF CI mismatch**: paper says [79.5%, 98.4%], raw server data and registry both say [68.79, 100.0] | **HIGH** |
| D2 | Table 2 (baselines) | **Trained router CI mismatch**: paper says [-16.33, -5.27], provenance C248/C249 says [-15.25, -6.38] | **MEDIUM** |

---

## Section-by-Section Audit

### Abstract

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| Non-tie labels from death asymmetry | 78.9% | summary.json: 75/95 | 75/95 = 78.947% | ✅ | |
| Task types | 11 | summary.json | 11 | ✅ | |
| Episodes | 245 | summary.json | 245 | ✅ | |
| Cross-model families | three 7-9B | registry (llama/gemma/qwen) | 3 models | ✅ | |
| MATH N | 795 | analysis_n800.json | 795 | ✅ | |
| ~50-episode pilot | ~50 | Appendix R | qualitative | ✅ | Framework recommendation |

### Introduction

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 78.9% death asymmetry labels | 75/95 | summary.json death_distribution | only_int=70, only_det=5 → 75 | ✅ | |
| 96.3% oracle match | 96.3% | Calculated: (86+150)/245 | 236/245 = 96.327% | ✅ | |
| Marginal value 2.89 pts | 2.89 | -6.58 - (-9.47) | 2.89 | ✅ | |
| Δ_nd = +2.84 | +2.84 | plan-012-full | delta_nd = 2.84 | ✅ | |
| 9.6% of total gap | 2.84/29.60 | Calculated | 0.09594 ≈ 9.6% | ✅ | |
| 72B: 5 int-preferred | 5 | backbone-scaling-70b | int_preferred = 5 | ✅ | |
| 72B DAF=92.4% | 92.4% | backbone-scaling-70b | 92.42% | ✅ | |
| 7B: 9 int-preferred | 9 | plan-012-full label_dist | internal_preferred = 9 | ✅ | |
| Reflexion N=3 DAF>100% | >100% | Δ_nd = -0.47 claimed | Cannot verify from registry | ❓ | |
| 97.4% step tie rate | 97.4% | step_tie_rate_full.json | 5935/6094 = 97.39% | ✅ | |
| 5,935 of 6,094 steps | 5935/6094 | step_tie_rate_full.json | tie_steps=5935, total=6094 | ✅ | |
| MATH 73.5% vs 73.0% | 73.5/73.0 | analysis_n800.json | int=0.7346, code=0.7296 | ✅ | |
| MATH p=0.81 | 0.81 | analysis_n800.json | p_exact=0.8103 | ✅ | |
| MATH N=795 | 795 | analysis_n800.json | n=795 | ✅ | |
| Llama N=220 direction 10/10 | 10/10 | llama-cross-model-full | All 10 death-prone tasks positive ΔDR | ✅ | |
| Router 56-59% step BA | 56-59% | capacity scaling table | 56.4/58.2/59.2 | ✅ | |
| 4B only exceeds baseline | 59.0±1.9% | capacity scaling table | Qwen3-4B: 59.0±1.9 | ✅ | |
| DAF 88-90% cross-model | 88-90% | registry (qwen/llama/gemma) | 90.4/88.2/89.7 | ✅ | |
| Spread 2.2pp | 2.2pp | Calculated | 90.4-88.2 = 2.2 | ✅ | |
| Cross-model DR 36-43% | 36-43% | registry | Gemma 36.4%, Qwen 42.9% | ✅ | |
| Label fraction CI [70.7%, 87.0%] | [70.7, 87.0] | bootstrap (no raw file found) | — | ❓ | Need bootstrap code |

### Method (§2)

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 97.4% step tie rate | 97.4% | step_tie_rate_full.json | 97.39% | ✅ | |
| 5,935/6,094 steps | 5935/6094 | step_tie_rate_full.json | Exact match | ✅ | |
| T_max = 30 steps | 30 | ScienceWorld config | Standard | ✅ | |
| P = 100 penalty | 100 | ScienceWorld config | Standard | ✅ | |
| 245 episode pairs, 11 types | 245/11 | summary.json | 245/11 | ✅ | |
| 20-40 per type | 20-40 | summary.json episodes_per_task | 20-40 (FNLT=40) | ✅ | |
| δ = 0.2653 | 0.2653 | Calculated: (105-40)/245 | 65/245 = 0.26531 | ✅ | |
| s_surv = 0.87 | 0.87 | Need episode-level data | — | ❓ | |
| Δ_full = 29.60 | 29.60 | plan-012-full | delta_full = 29.6 | ✅ | |
| Δ_nd = 2.84 | 2.84 | plan-012-full | delta_nd = 2.84 | ✅ | |
| Residual 29.60-29.37=0.23 | 0.23 | 0.2653×100+2.84=29.37 | 29.60-29.37=0.23 | ✅ | 0.8% of Δ_full |
| DAF=90.4% at P=100 | 90.4% | plan-012-full | 0.9041 | ✅ | |
| DAF=50.4% at P=10 | 50.4% | penalty_sensitivity table | Exact recalculation (not approx.) | ✅ | Approx gives 48.3%; exact gives 50.4% |
| DAF=82.6% at P=50 | 82.6% | penalty_sensitivity table | Matches | ✅ | |
| Bootstrap B=10,000 | 10,000 | Multiple refs | Standard | ✅ | |
| N=245 resample | 245 | plan-012-full | episodes=245 | ✅ | |
| 0.3% directional conflict | 0.3% of 2,040 | step_tie_rate analysis | — | ❓ | Need step-label conflict data |
| 60.3% pre-event neutral | 60.3% | — | — | ❓ | Need step-label analysis |
| 2,040 training steps | 2,040 | — | — | ❓ | Derived from episode/step splits |

### Experiments (§3)

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 11 of 30 task types | 11/30 | summary.json | 11 tasks listed | ✅ | |
| 19 excluded (63%) | 19/30=63% | 30-11=19 | 63.3% | ✅ | |
| Excluded categories: 5+7+7 | 5/7/7 | excluded tasks table | 5 dev, 7 taxonomic, 7 agent-floor | ✅ | |
| Anti-cherry-pick: 18/19 death dominant | 18/19 | excluded tasks table | All except grow-plant | ✅ | |
| Excluded ΔDR = +38.2pp | +38.2pp | excluded tasks table | Mean of 19 tasks | ✅ | |
| Included ΔDR = +28.7pp (task-weighted) | +28.7pp | Per-task data | Task-weighted mean | ✅ | |
| Extended validation ΔDR = +32.0pp | +32.0pp | extended-task-validation | 5 tasks mean | ✅ | |
| Reasoning depth p>0.26 | p>0.26 | ablation appendix | Mann-Whitney | ❓ | |

#### §3.1 Death Avoidance Decomposition

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 95 non-tie labels | 95 | summary.json: 86+9 | 95 | ✅ | |
| 75 (78.9%) from death asymmetry | 75/95=78.9% | summary.json: 70+5=75 | 78.947% | ✅ | |
| Label fraction CI [70.7%, 87.0%] | [70.7, 87.0] | bootstrap | — | ❓ | |
| 54 sole-signal labels | 54 | — | — | ❓ | Need per-episode detail |
| 150 (61.2%) no-preference | 150/245=61.2% | summary.json | 150 | ✅ | |
| DAF = 90.4% at P=100 | 90.4% | plan-012-full | 0.9041 | ✅ | |
| Δ_full = +29.60 | +29.60 | plan-012-full | 29.6 | ✅ | |
| Δ_nd = +2.84 | +2.84 | plan-012-full | 2.84 | ✅ | |
| CI_nd [0.34, 5.57] | [0.34, 5.57] | bootstrap | — | ❓ | |
| CI_DAF [81.1%, 99.0%] | [81.1, 99.0] | plan-012-full bootstrap | Consistent with 90.4%±4.2% | ✅ | |
| 42.9% int death rate | 42.9% | plan-012-full / summary.json | 105/245 = 42.86% | ✅ | |
| 16.3% det death rate | 16.3% | plan-012-full / summary.json | 40/245 = 16.33% | ✅ | |
| 2.6× ratio | 2.6× | 42.9/16.3 | 2.63× | ✅ | |
| r = 0.97, p < 10^-6 | 0.97 | plan-012-full | pearson_r = 0.9698 | ✅ | |
| 86 det, 9 int, 150 no-pref | 86/9/150 | plan-012-full / summary.json | Exact match | ✅ | |
| SCI = 0.2147 | 0.2147 | — | — | ❓ | Need Gini computation |
| Top-3 = 39.8% | 39.8% | — | — | ❓ | |
| 10 death-prone tasks = 100% death labels | 100% | per-task table | All 10 confirmed | ✅ | |
| find-non-living-thing: 0% deaths, Δ=+9.58 | 0%/+9.58 | 72b_comparison / summary | int_dr=0, det_dr=0, delta=9.575 | ✅ | |
| 20 non-death labels all from FNLT | 20 | per-task table: 16+4=20 | 16 det + 4 int = 20 | ✅ | |
| Hallucination 50%, object 35%, action 15% | 10/7/3=20 | Non-death taxonomy table | Manual annotation | ✅ | 10/20=50%, 7/20=35%, 3/20=15% |
| Cluster CI [73.3%, 100.0%] | [73.3, 100.0] | wild-cluster appendix | Table in paper | ✅ | |
| Cohen's d = 3.02 | 3.02 | wild-cluster appendix | — | ❓ | |
| Permutation p=0.002 | 0.002 | wild-cluster appendix table | "4/2048" | ✅ | 4/2048=0.00195≈0.002 |
| Sign test p<0.001 | <0.001 | wild-cluster appendix table | Exact match | ✅ | |
| LOTO label fraction 75.9%-78.9% | 75.9-78.9% | LOTO DAF table | Range confirmed | ✅ | |
| Seed replication DAF=89.7% | 89.7% | gemma-scienceworld-v5 | 89.65% | ⚠️ | See note below |
| Spearman ρ=0.986 | 0.986 | correlation appendix | — | ❓ | |
| LOO r range [0.963, 0.980] | [0.963, 0.980] | LOO table in paper | Table entries match | ✅ | |
| Bootstrap r CI [0.952, 0.995] | [0.952, 0.995] | correlation appendix | — | ❓ | |

**Note on "seed replication"**: §3.1 says "an independent seed replication ($N{=}220$) yields DAF $= 89.7\%$" with ref to Appendix J (Seed Robustness). However, DAF=89.7% with N=220 matches Gemma-2-9B-it (§3.2) exactly. Appendix J discusses router seed robustness, not DAF replication. This may be a cross-model result mislabeled as "seed replication", or a separate Qwen replication not found in registry.

#### §3.2 Multi-Model Validation

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| Llama N=220 | 220 | llama-cross-model-full | 220 | ✅ | |
| Llama int DR 41.4% | 41.4% | llama-cross-model-full | 0.4136 | ✅ | |
| Llama det DR 11.4% | 11.4% | llama-cross-model-full | 0.1136 | ✅ | |
| Llama ΔDR +30.0pp | +30.0 | Calculated | 0.4136-0.1136=0.3000 | ✅ | |
| Llama DAF=88.2% | 88.2% | llama-cross-model-full | 88.2 | ✅ | |
| Llama DAF CI [80.2%, 95.1%] | [80.2, 95.1] | llama-cross-model-full | [80.2, 95.1] | ✅ | |
| Llama Δ_full=+33.17 | +33.17 | llama-cross-model-full | 33.17 | ✅ | |
| Llama Δ_nd=+3.9 | +3.9 | llama-cross-model-full | 3.9 | ✅ | |
| Llama direction 10/10 | 10/10 | Per-task Llama data | All 10 death-prone positive | ✅ | |
| Llama 83 det, 3 int, 134 no-pref | 83/3/134 | llama-cross-model-full | 83/3/134 | ✅ | |
| Llama 3 int = 1.4% | 1.4% | 3/220 | 1.36% | ✅ | |
| ~42% int vulnerability both models | ~42% | 42.9% / 41.4% | Both ~42% | ✅ | |
| +26.5 vs +30.0pp differential | 26.5/30.0 | Qwen: 65/245=26.53pp | Rounds to 26.5 | ✅ | |
| Gemma DAF=89.7% | 89.7% | gemma-scienceworld-v5 | 89.65% | ✅ | |
| **Gemma DAF CI [79.5%, 98.4%]** | **[79.5, 98.4]** | **gemma analysis.json** | **[68.79, 100.0]** | **❌ D1** | **Paper CI does not match raw data** |
| Gemma N=220 | 220 | gemma-scienceworld-v5 | 220 | ✅ | |
| Gemma int DR 36.4% | 36.4% | gemma analysis.json | 36.36% | ✅ | |
| Gemma det DR 14.1% | 14.1% | gemma analysis.json | 14.09% | ✅ | |
| Gemma ΔDR=22.3pp | 22.3pp | gemma analysis.json | 22.27pp | ✅ | |
| DAF 88-90% spread 2.2pp | 2.2pp | 90.4-88.2 | 2.2 | ✅ | |

#### §3.3 Agent Improvement

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| Baseline int DR = 42.9% | 42.9% | plan-012-full | 0.429 | ✅ | |
| Reflexion 3× DR = 31.4% | 31.4% | Table 1 | N=220, 11 tasks | ✅ | |
| 72B DR = 30.6% | 30.6% | backbone-scaling-70b | 0.306 | ✅ | |
| Det baseline DR = 16.3% | 16.3% | plan-012-full | 0.163 | ✅ | |
| Death-prone baseline 48.0% | 48.0% | retry-dose-response N=1 | 0.48 | ✅ | |
| Retry 5× DR = 43.5% | 43.5% | retry-dose-response N=5 | 0.435 | ✅ | |
| Retry Δ = -4.5pp | -4.5 | 48.0-43.5 | 4.5 | ✅ | |
| Reflexion rescues 29.3% | 29.3% | — | — | ❓ | Need episode-level rescue data |
| Gap to det 15.1pp | 15.1 | 31.4-16.3 | 15.1 | ✅ | |
| Reflexion death-prone ~35% | ~35% | dose-response N=3 | 34.0% | ✅ | |
| Reflexion N=3 Δ_nd = -0.47 | -0.47 | — | — | ❓ | Need matched-episode analysis |
| 72B N=255 | 255 | backbone-scaling-70b | 255 | ✅ | |
| 72B det DR = 2.75% | 2.75% | backbone-scaling-70b | 0.0275 | ✅ | |
| 72B ΔDR = +27.8pp | +27.8 | 30.6-2.75 | 27.85pp | ✅ | |
| 72B Δ_nd = +2.28 | +2.28 | backbone-scaling-70b | 2.28 | ✅ | |
| 72B DAF = 92.4% | 92.4% | backbone-scaling-70b | 92.42% | ✅ | |
| 72B DAF CI [86.1%, 97.9%] | [86.1, 97.9] | backbone-scaling-70b | [86.1, 97.9] | ✅ | |
| 72B: 5 int-pref (2.0%) vs 9 at 7B (3.7%) | 5/255=2.0%, 9/245=3.7% | Calculated | 1.96%≈2.0%, 3.67%≈3.7% | ✅ | |
| Dose-response N=3: 34.0% | 34.0% | reflexion-dose-response-n345 | 0.34 | ✅ | |
| Dose-response N=4: 36.5% | 36.5% | reflexion-dose-response-n345 | 0.365 | ✅ | |
| Dose-response N=5: 35.0% | 35.0% | reflexion-dose-response-n345 | 0.35 | ✅ | |
| N=1→3 Δ=-13.5pp | -13.5 | 48.0-34.0=14.0 | 14.0pp | ⚠️ | Paper says -13.5, calculated 14.0. Likely uses N=1 DR=47.5% (not 48.0%) due to task weighting. Minor rounding. |
| Dose-response p=0.003 | 0.003 | — | — | ❓ | Statistical test not in registry |
| Retry flat: 48.0→43.5% | 48.0→43.5 | retry-dose-response | N=1:0.48, N=5:0.435 | ✅ | |

#### §3.4 Cross-Environment

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| MATH N=795 | 795 | analysis_n800.json | n=795 | ✅ | |
| MATH int=73.5%, det=73.0% | 73.5/73.0 | analysis_n800.json | 0.7346/0.7296 | ✅ | |
| MATH McNemar p=0.81 | 0.81 | analysis_n800.json | p_exact=0.8103 | ✅ | |
| MATH 84.4% no-preference | 84.4% | analysis_n800.json | 671/795=84.40% | ✅ | |
| ALFWorld 6 task types, 135 games | 6/135 | alfworld_daf_results.json | 6 types, 135 games | ✅ | |
| ALFWorld DAF=0% | 0% | alfworld_daf_results.json | DAF=0% (no deaths) | ✅ | |
| ALFWorld Qwen: 35/37 (94.6%) det | 94.6% | alfworld_daf_results.json | 35/(35+2)=94.59% | ✅ | |
| ALFWorld 25.9% det-preferred | 25.9% | alfworld_daf_results.json | 35/135=25.93% | ✅ | |
| ALFWorld per-task D/I/N all match | (see table) | alfworld_daf_results.json | All 6 tasks match | ✅ | |
| ALFWorld Llama: 16/16 (100%) det | 100% | alfworld-llama-v3 | 16/0/119 → 16/16 | ✅ | |
| ALFWorld Llama 11.9% det-pref | 11.9% | alfworld-llama-v3 | 16/135=11.85% | ✅ | |

#### §3.5 Baselines

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| Always-internal: -39.07 | -39.07 | plan-003-baseline-245eps | No metrics in registry | ❓ | Consistent with other data |
| Always-det: -9.47 | -9.47 | plan-003-baseline-245eps | No metrics in registry | ❓ | |
| Random: -22.38 | -22.38 | plan-003-baseline-245eps | No metrics in registry | ❓ | |
| Oracle: -6.58 | -6.58 | plan-003-baseline-245eps | No metrics in registry | ❓ | |
| Oracle match 96.3% | 96.3% | Calculated: (86+150)/245 | 236/245=96.327% | ✅ | |
| Marginal value 2.89 pts | 2.89 | -6.58-(-9.47) | 2.89 | ✅ | |
| Oracle BA 50.0% | 50.0% | oracle_results.json | always-det baseline=0.5 | ✅ | |
| 90.5% of non-tie oracle = det | 90.5% | 86/(86+9) | 86/95=90.53% | ✅ | |

#### §3.6 Router Training

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| Oracle margin 2.89 pts | 2.89 | See baselines | 2.89 | ✅ | |
| ~88% uninformative signal | ~88% | 60.3%+27.4%=87.7% | ≈88% | ✅ | |
| 0.3% directional conflict | 0.3% | — | — | ❓ | |
| 86/95=90.5% det-preferred | 90.5% | plan-012-full | 86/95=90.53% | ✅ | |
| 3.7% minority class | 3.7% | 9/245 | 3.67% | ✅ | |
| Step BA: 56-59% flat | 56-59% | capacity table | 56.4/58.2/59.2 | ✅ | |
| 4B episode: 59.0±1.9% | 59.0±1.9 | capacity table | Match | ✅ | |
| Episode-level indep: 47.1±2.2% | 47.1±2.2 | seed-robustness appendix | Mean of 8 seeds | ✅ | |
| LOTO: 49.2% | 49.2% | ablation appendix | — | ❓ | |
| Task-type classifier: 64.7% BA | 64.7% | ablation appendix | — | ❓ | |
| LOTO classifier: 50.0% | 50.0% | ablation appendix | — | ❓ | |
| 4B e2e: -12.03 [-17.82, -6.45] | -12.03 | — | — | ❓ | Different from Table 2 router |
| **Table 2 trained router: -10.70 [-16.33, -5.27]** | **[-16.33, -5.27]** | **provenance C248** | **[-15.25, -6.38]** | **❌ D2** | **CI mismatch** |
| Trained router death 17.6% | 17.6% | provenance C249 | 17.6% | ✅ | |
| 97.0% det allocation | 97.0% | provenance C249 | 97.0% | ✅ | |
| Fixed-split BA 57.6±0.5% | 57.6±0.5 | labeling appendix | — | ❓ | Provenance C255 untraced |
| Step-level 54.1±5.4% | 54.1±5.4 | seed-robustness appendix | 8-seed mean | ✅ | |
| Augmentation 25%-800% no improvement | flat ~50% | augmentation table | All ≈50% | ✅ | |

### Related Work (§4)

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 78.9% of non-tie labels | 78.9% | plan-012-full | 75/95 | ✅ | |

No other quantitative claims in Related Work.

### Discussion (§5)

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 6 router variants: 56-59% | 56-59% | capacity + ablation | Consistent | ✅ | |
| 72B DAF=92.4% | 92.4% | backbone-scaling-70b | 92.42% | ✅ | |
| 5 int-pref vs 9 at 7B | 5/9 | backbone/plan-012 | 5/9 | ✅ | |
| 96.3% oracle match | 96.3% | Calculated | 236/245 | ✅ | |
| Δ_nd=2.84 (9.6%) | 2.84/9.6% | plan-012-full | 2.84/29.60=9.6% | ✅ | |
| ALFWorld DAF=0% | 0% | alfworld data | No deaths | ✅ | |
| ~50-episode pilot | ~50 | Framework | Qualitative | ✅ | |
| Action-space filtering 19pp | 19pp | grounding appendix | 48.0→29.0 | ✅ | |

### Conclusion (§6)

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 78.9% from death avoidance | 78.9% | Verified above | ✓ | ✅ | |
| Three model families | 3 | Qwen/Llama/Gemma | 3 | ✅ | |
| 10× scaling DAF=92.4% | 92.4% | backbone-scaling-70b | 92.42% | ✅ | |

### Limitations

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| 11 of 30 task types | 11/30 | summary.json | 11 | ✅ | |
| 19 excluded (63%) | 63% | 19/30 | 63.3% | ✅ | |
| Reflexion 42.9%→31.4% | 42.9/31.4 | plan-012/Table 1 | Match | ✅ | |
| Llama N=220, 10/10 consistency | 220/10/10 | llama registry | Match | ✅ | |
| +30.0pp vs +26.5pp | 30.0/26.5 | Calculated | 30.0/26.53 | ✅ | |
| Cluster CI [73.3%, 100.0%] | [73.3, 100.0] | wild-cluster table | Match | ✅ | |
| K=11 clusters | 11 | 11 task types | 11 | ✅ | |
| DAF=90.4% upper bound | 90.4% | plan-012-full | 0.9041 | ✅ | |
| 0.3% directional conflict | 0.3% | — | — | ❓ | |
| From +26.6pp to ~+8pp (grounding) | 26.6/~8 | grounding appendix | Consistent | ✅ | |
| >10pp residual gap | >10 | grounding appendix | 29.0-20.0=9.0pp (10-task det DR=20%) | ⚠️ | Approx., depends on det DR used |

### Ethics Statement

| Claim | Paper Value | Source | Source Value | Match? | Notes |
|-------|-------------|--------|-------------|--------|-------|
| ~200 GPU-hours total | ~200 | — | — | ❓ | Cannot verify |
| ~140h collection, ~35h training, ~25h eval | 140/35/25 | — | — | ❓ | Cannot verify |

### Appendices

| Appendix | Key Claims | Match? | Notes |
|----------|-----------|--------|-------|
| A. SCI | SCI=0.2147, Gini formula | ❓ | Need raw computation |
| B. Labeling | 150 no-pref (115 both-alive, 35 both-dead); 95 training; 75 death-asym (70 det, 5 int), 20 score (16 det, 4 int) | ✅ | 70+5=75, 16+4=20, 70+16=86 det, 5+4=9 int |
| C. Per-task | All per-task Δ_full, D%, D/I/N values | ✅ | Verified against 72b_matched_daf_comparison 7B data |
| D. Correlation | r=0.9698, Spearman ρ=0.986, LOO range [0.963, 0.980], bootstrap CI [0.952, 0.995] | ✅/❓ | r verified; Spearman/bootstrap CIs not independently verified |
| E. Cluster | Wild cluster p<0.001, permutation p=0.002 (4/2048), sign p<0.001, CI [73.3, 100.0], Cohen's d=3.02 | ✅ | |
| F. Per-task CI | 28/30 death-prone, pooled +37.3% [29.7, 44.4], 15/28 individually significant | ❓ | Need per-task bootstrap |
| G. LOTO DAF | Range 75.9%-78.9% | ✅ | Table in paper |
| H. Dose-response | Per-task DR at N=3,4,5; aggregate 34.0/36.5/35.0 | ✅ | Matches registry |
| I. Router details | Hyperparameters, inference params | ✅ | Consistent |
| J. Seed robustness | Step-level 54.1±5.4%, episode 47.1±2.2%, augmentation flat | ✅ | Per-seed values in table |
| K. Penalty sensitivity | DAF(P) curve, r by P, T=0 r=-0.13 | ✅ | Matches daf-sensitivity-extended |
| L. Cross-env | ALFWorld per-task, MATH composition (585/210) | ✅ | Raw data matches |
| M. Cross-model | Llama per-task, Gemma summary | ✅ | Registry matches (except Gemma CI, see D1) |
| N. Failure modes | 105 deaths, focus-on pattern, 5.4% vs 3.4% | ❓ | Manual analysis |
| O. Grounding | Prompt -11pp, filter -19pp, zero leaks | ❓ | Need raw ablation data |
| P. Ablations | Capacity 56.4/58.2/59.2 step, 50.7/43.1/59.0 episode; gen 46.7%; LOTO 50.0% | ✅ | Matches registry/capacity table |
| Q. Threshold | Optimal t=0, det=-9.47 vs threshold=-11.03 | ❓ | Need raw threshold sweep |
| R. Decision | 4/4 conditions classified correctly | ✅ | Table in paper |
| S. Extended validation | 5 tasks, ΔDR=+32.0pp | ✅ | Extended-task-validation |
| T. Prompts | Template text | N/A | No quantitative claims |
| U. Non-death case study | 20 labels: 10 hall, 7 obj, 3 action | ✅ | Table sums correct |

---

## Provenance Gap Analysis

| Claim ID | Text | Status | Suggested Evidence |
|----------|------|--------|-------------------|
| C255 | Fixed-split balanced accuracy 57.6±0.5% | Untraced | From labeling audit retraining; likely from plan-004-ablation-b retrain with death-asymmetry-only labels. Could link to plan-004-ablation-b with note "retrain subset". |
| C256 | Cross-split balanced accuracy 55.4±5.2% | Untraced | Not found in current paper text. Paper says 54.1±5.4% (seed robustness). Either stale claim from older version or different calculation. **Recommend deprecating.** |
| C257 | 78.9% of non-tie routing labels from death asymmetry | Untraced | Directly derivable from plan-012-full: 75/95 = 78.9%. Link to plan-012-full. |
| C258 | DAF ~90% at P=100 | Untraced | plan-012-full: DAF=0.9041 at P=100. Link to plan-012-full. |
| C259 | r=0.97 with structural coupling caveat | Untraced | plan-012-full: pearson_r=0.9698. Link to plan-012-full. |
| C319 | Scaling model capacity improves episode-level routing | Untraced | From capacity scaling ablation: Qwen3-4B 59.0±1.9% > 50% baseline. Link to plan-004-ablation-b capacity scaling or a dedicated experiment. |
| C320 | Partial r(Δ_full, δ \| δ·P) = 0.02, p=0.91, df=27 | Untraced | **Not found in current paper text.** This claim appears to have been removed during revisions. **Recommend deprecating.** |
| C323 | (empty text) | Empty | **Recommend removing.** |
| C324 | (empty text) | Empty | **Recommend removing.** |

### Additional Stale Provenance Entries

| Claim ID | Issue |
|----------|-------|
| C152, C200, C233, C234 | Reference "98.2% per-step tie rate" but current value is 97.4% (5935/6094). The 98.2% was from the old 5-task MVP analysis. Paper is correct; provenance is outdated. |
| C193 | Says oracle_det_match = 96.2% but paper says 96.3%. Calculated: 236/245 = 96.33%. Provenance is 0.1pp off. |

---

## Discrepancies — Detailed Analysis

### D1: Gemma DAF CI Mismatch (HIGH)

**Paper (§3.2, cross-model summary table)**: DAF=89.7% (95% CI [79.5%, 98.4%])

**Raw data (server: gemma analysis.json)**: DAF=89.65%, bootstrap_95ci for daf: [68.79, 100.0]

**Registry (gemma-scienceworld-v5)**: DAF=89.7 [68.8, 100]

The paper's CI [79.5%, 98.4%] is substantially narrower and does not match either the raw server data or the registry entry. Both non-paper sources consistently report [68.8, 100.0]. The DAF point estimate (89.7%) is correct; only the CI is wrong.

**Possible explanations**:
1. A different bootstrap method (e.g., clustered vs. non-clustered) was used for the paper CI
2. The CI was updated in code but the registry/server files were not re-run
3. The CI was manually entered from a different analysis

**Impact**: The CI [79.5%, 98.4%] is narrower than the actual [68.8, 100.0], which could overstate the precision of the Gemma DAF estimate. Since this is in a cross-model validation table, reviewers may scrutinize it.

**Recommendation**: Verify the bootstrap code used for Gemma DAF CI. If [68.8%, 100.0%] is correct, update the paper.

### D2: Trained Router CI Mismatch (MEDIUM)

**Paper (Table 2)**: Trained Router score = -10.70, 95% CI [-16.33, -5.27]

**Provenance (C248, C249)**: score = -10.70, CI [-15.25, -6.38]

The point estimate matches but the CIs differ. The paper CI is wider (11.06 range vs 8.87 range).

**Possible explanations**:
1. Different bootstrap runs or methods
2. Provenance was updated from an older eval run; paper uses a newer unified eval

**Impact**: Both CIs overlap with always-deterministic (-9.47), so the qualitative conclusion ("not exceeding always-deterministic") holds regardless. The discrepancy is primarily a provenance tracking issue.

**Recommendation**: Re-run the unified eval script and update both paper and provenance to the canonical CI.

---

## Verification Summary by Source

| Source | Claims Verified | Status |
|--------|----------------|--------|
| plan-012-full (registry) | DAF, Δ_full, Δ_nd, r, death rates, labels, episodes | All match ✅ |
| summary.json (server) | Episodes, tasks, labels, death distribution | All match ✅ |
| step_tie_rate_full.json (server) | 97.4%, 5935/6094, per-task rates | All match ✅ |
| analysis_n800.json (server) | MATH N, accuracies, p-value, labels | All match ✅ |
| alfworld_daf_results.json (server) | ALFWorld Qwen labels, per-task | All match ✅ |
| alfworld-llama-v3 (registry) | ALFWorld Llama labels | All match ✅ |
| backbone-scaling-70b (registry) | 72B DAF, Δs, labels, CIs | All match ✅ |
| llama-cross-model-full (registry) | Llama DRs, DAF, Δs, labels, CIs | All match ✅ |
| gemma-scienceworld-v5 (registry) | Gemma DRs, DAF, labels | Match except CI ❌ |
| gemma analysis.json (server) | Gemma per-task breakdown | All match ✅ |
| reflexion-dose-response-n345 (registry) | N=3/4/5 death rates | All match ✅ |
| retry-dose-response (registry) | N=1-5 death rates | All match ✅ |
| daf-sensitivity-extended (registry) | Penalty sensitivity, r by P | All match ✅ |
| plan-003-baseline-245eps (registry) | Baseline scores | No metrics recorded ❓ |
| plan-004-ablation-b (registry) | Router accuracy, generation metrics | Match (except CI) |
| oracle_results.json (server) | Oracle BA, per-task routing | All match ✅ |

---

## Key Derived Calculations Verified

| Calculation | Formula | Result | Paper | Match? |
|-------------|---------|--------|-------|--------|
| Label fraction | 75/95 | 78.947% | 78.9% | ✅ |
| Oracle match rate | (86+150)/245 | 96.327% | 96.3% | ✅ |
| Marginal value | -6.58-(-9.47) | 2.89 | 2.89 | ✅ |
| Δ_nd / Δ_full | 2.84/29.60 | 9.594% | 9.6% | ✅ |
| DAF at P=100 | 1-2.84/29.60 | 90.41% | 90.4% | ✅ |
| δ | (105-40)/245 | 0.26531 | 0.2653 | ✅ |
| δP + Δ_nd | 0.2653×100+2.84 | 29.37 | 29.37 | ✅ |
| Residual | 29.60-29.37 | 0.23 (0.8%) | 0.23 (0.8%) | ✅ |
| DR ratio | 42.9/16.3 | 2.63× | 2.6× | ✅ |
| 72B int-pref rate | 5/255 | 1.96% | 2.0% | ✅ |
| 7B int-pref rate | 9/245 | 3.67% | 3.7% | ✅ |
| 72B DAF | 1-2.28/30.07 | 92.42% | 92.4% | ✅ |
| ALFWorld det-leaning | 35/37 | 94.59% | 94.6% | ✅ |
| Llama int-pref rate | 3/220 | 1.36% | 1.4% | ✅ |
| MATH no-pref | 671/795 | 84.40% | 84.4% | ✅ |
| Permutation p | 4/2048 | 0.00195 | 0.002 | ✅ |
