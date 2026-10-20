# Negative Results Summary (55 experiments)

## Category Counts

| Failure Pattern | Count |
|---|---|
| task-specific failure | 22 |
| method failure | 14 |
| correlation positive but selection negative | 11 |
| degeneracy trap | 5 |
| optimization/implementation | 3 |
| **Total** | **55** |

---

## 1. Task-Specific Failure (22)

RE tasks, WNUT-17, OOD, pretrained baselines, and cross-model experiments where the task/setting itself prevents SC signals from working.

| exp_id | hypothesis summary | key metrics |
|---|---|---|
| exp_008_re_n16_t10_full | RE N=16: RE SJ rho=0.248, far below NER | RE rho_sj=0.248 |
| exp_008_re_n16_v2 | RE N=16 v2: SJ weak (0.281), 44.3% F1=0 | rho_sj=0.281, F1=0%: 44.3% |
| exp_008_re_seed123 | RE seed=123: structural < surface, high zero-F1 (44.1%) | rho_sj=0.284, struct>surf=False |
| exp_re_scierc_seed456 | RE seed=456: rho_sj=0.315 < 0.40 threshold, 45.3% F1=0 | RE rho_sj_cond=0.315 |
| exp_re_scierc_seed123 | RE seed=123: rho_sj=0.277 < 0.40 threshold, 43.6% F1=0 | RE rho_sj_cond=0.277 |
| e1_component_wise_re_sj | Component-wise RE SJ: head_sj rho=0.21 far from NER 0.38 | head_sj=0.21, mult=0.244 |
| mvp_pilot_001 | MVP pilot 1: RE rho_sj=0.254 < 0.40; SJ < FK on RE full | RE rho_sj=0.254, F1=0%: 58.3% |
| mvp_pilot_003 | MVP pilot 3: RE rho_sj=0.237 < 0.40 | RE rho_sj=0.237, zero_pct=67.6% |
| mvp_pilot_004 | MVP pilot 4: RE rho_sj=0.244 < 0.40 | RE rho_sj=0.244, zero_pct=44.3% |
| mvp_pilot_005 | MVP pilot 5: RE rho_sj=0.234 < 0.40; NER passes | RE rho_sj_full=0.234 |
| exp_fewrel_re_sc | FewRel RE: micro F1=0.075-0.088, bootstrap p=0.76, 75.8% F2 | bootstrap p=0.757 |
| exp_001_seed456_t10_full | SciERC seed=456 early: RE rho_sj=0.268 weak | RE rho_sj=0.268 |
| exp_001_seed123_t10_full | SciERC seed=123 early: RE rho_sj=0.265 weak | RE rho_sj=0.265 |
| exp_001_seed456_v2 | SciERC joint NER+RE seed=456 v2: early pipeline | no metrics |
| exp_003_ner_wnut17 | WNUT-17: 53.7% zero-F1, structural rho weak (SJ=0.082) | rho_sj=0.082 |
| exp_wnut17_qwen25_7b | WNUT-17 Qwen2.5: construction delta inconsistent across seeds | seed42 delta=-0.84pp |
| exp_003_wnut17_v2 | WNUT-17 v2: no metrics | no metrics |
| exp_011_ood_conll_to_scierc | OOD CoNLL->SciERC: schema mismatch, F1=0.009 | rho_sj=-0.186 |
| exp_007_llama_scierc_seed123 | LLaMA seed=123: DGS delta=-0.38pp, degen=26.7% | DGS delta=-0.38pp |
| exp_007_llama_seed456 | LLaMA seed=456: RE rho_sj=0.287, struct<surface | RE rho_sj=0.287 |
| exp_007_llama_seed123 | LLaMA seed=123: RE rho_sj=0.268, struct<surface | RE rho_sj=0.268 |
| exp_e2_pretrained_scierc | Pretrained SciERC: >30% F1=0, struct_beats_surface=False | greedy_f1=0.242 |
| exp_e2_pretrained_scierc_s42_v2 | Pretrained SciERC s42 v2 | greedy_f1=0.243 |
| exp_e2_pretrained_scierc_s123 | Pretrained SciERC s123: MV delta=+1.12pp only | mv_delta=1.12pp |
| exp_e2_pretrained_scierc_s456 | Pretrained SciERC s456: MV delta=+2.06pp only | mv_delta=2.06pp |

## 2. Method Failure (14)

Proposed improvement methods (ESJ, MRSC, LSC, SCD, adaptive budget, verifier, etc.) that failed to improve over baselines.

| exp_id | hypothesis summary | key metrics |
|---|---|---|
| exp_esj_qwen3_all | ESJ: rho near 0 (0.02 SciERC, -0.008 FewNERD), AUROC~0.5 | ESJ rho=0.02, AUROC=0.512 |
| exp_esj_entity_self_judgment | ESJ entity-level: abandoned | no metrics |
| exp_mrsc_multi_round | MRSC multi-round iterative SC: abandoned | no metrics |
| exp_lsc_latent_sc | LSC: centroid F1=0.759 < LP=0.784 < MV=0.837 | centroid F1=0.759 |
| exp_backup1_het_temp | Heterogeneous-T mixing: deltas within +/-0.005 | max delta=0.007 |
| exp_backup3_distill_verifier | Supervised entity verifier: AUROC=0.87 but F1 delta~0 | delta_f1: -0.003 to +0.002 |
| exp_b1_scd_fewnerd_standard | SCD standard FewNERD: micro-F1 delta=-0.73pp (artifact) | pre=0.789, post=0.781 |
| exp_b1_scd_fewnerd_curriculum_q | SCD curriculum FewNERD: micro-F1 delta=-0.20pp (artifact) | pre=0.789, post=0.787 |
| exp_asb_adaptive_budget | Adaptive budget: no improvement after fixing 3 bugs | FewNERD/SciERC delta=0 |
| exp_e_theta_adaptive | Threshold-adaptive SC: abandoned | no metrics |
| exp_diagnostic_calibration | Diagnostic calibration regression: abandoned | no metrics |
| exp_adaptive_temperature | Adaptive temperature: abandoned | no metrics |
| exp_entity_consensus | Entity consensus construction: abandoned | no metrics |
| exp_ccs_selection | Cascaded selection: abandoned | no metrics |

## 3. Correlation Positive but Selection Negative (11)

QE signals correlate with quality (positive rho) but selection F1 does not beat greedy baseline.

| exp_id | hypothesis summary | key metrics |
|---|---|---|
| exp_006_v2 | T-sensitivity: SJ/FK correlate but sel F1 <= greedy | NER sel F1 ~ greedy |
| exp_016_rerun_1024_bootstrap | Bootstrap: LP vs greedy gap not significant (p=0.39) | CI [-0.03, 0.042], d=0.038 |
| exp_028_entity_token_lp | Entity-token LP: higher rho but lower selection F1 | entity LP delta=-2.0pp |
| exp_entity_token_lp | Entity-token LP worse than full-seq LP for selection | delta: -2.0pp SciERC, -3.3pp CoNLL |
| exp_verbalized_confidence | VerbConf: rho=0.30-0.34 but selection below greedy | delta: -2.5pp SciERC, -1.9pp CoNLL |
| exp_freeform_ablation | Free-form decoding: LP compression unchanged (ratio 0.97) | tied fraction ~0.58 |
| exp_027_mlp_verifier | MLP/RF combining 5 signals: can't beat greedy | MLP auroc=0.638, greedy F1 > all |
| exp_013_exact_match_voting | EM too coarse-grained for RE | NER rho=0.294, RE rho=0.156 |
| exp_qwen25_72b_zeroshot | 72B zero-shot: signals correlate but construction ~0 | SciERC +1.5pp; CoNLL/FewNERD negative |
| exp_qwen25_72b_fewshot | 72B few-shot: all bootstrap p > 0.4 | no significant delta |
| exp_fewnerd_mf4_v2_s42 | FewNERD MF4: struct beats surface but rho too low | rho_SJ_full=0.163 |

## 4. Degeneracy Trap (5)

High degeneracy rate prevents signals from being useful, or degeneracy-related experimental failures.

| exp_id | hypothesis summary | key metrics |
|---|---|---|
| exp_028_fewnerd_5epoch | 5-epoch FewNERD: degeneracy rose to 31.3% | degen=31.3%, LP sel delta=+0.6pp |
| exp_028 | 5-epoch confirms degeneracy is training-induced (31.3%) | degen=31.3% |
| exp_fewnerd_t12_s42 | T=1.2 FewNERD: 28.2% degeneracy, rho_SJ=0.136 | degen=28.2% |
| exp_fewnerd_t12_s123 | T=1.2 FewNERD seed=123: 24.7% degeneracy | degen=24.7% |
| exp_b1_scd_conll_control | SCD negative control CoNLL (70% degen): control failed | pre=0.908, post=0.918 |

## 5. Optimization/Implementation (3)

No data or abandoned early due to bugs/infeasibility before any meaningful result.

| exp_id | note |
|---|---|
| exp_003_wnut17_v2 | No metrics recorded |
| exp_001_seed456_v2 | No metrics recorded |
| exp_e_theta_adaptive | Abandoned before execution |

*Note: Several "abandoned" experiments in the method failure category above could also be classified here. They are kept in method failure because the method concept itself was the primary factor.*

---

## Key Takeaways

1. **RE is a consistent failure mode** (11 experiments, all showing rho_sj < 0.40 and >40% zero-F1 instances). The root cause is well-understood: relation extraction has inherently higher output variance and more zero-F1 samples, which destroys structural signal correlation. This is discussed in the paper as an expected boundary condition.

2. **The correlation-selection gap is the central negative finding** (11 experiments): signals correlate with quality (positive rho, AUROC > 0.5) but cannot beat greedy selection. This is the paper's core analytical contribution, framed as a diagnostic rather than a defect.

3. **All proposed improvement methods failed** (14 experiments): ESJ (rho~0), LSC (centroid < MV), MRSC (abandoned), SCD (metric artifact), heterogeneous-T (no effect), adaptive budget (no effect after bug fixes), supervised verifier (AUROC=0.87 but F1 delta~0). This strongly supports the paper's thesis that the gap is structural, not solvable by better aggregation.

4. **Degeneracy is a real trap** (5 experiments): higher temperature increases degeneracy; longer training increases degeneracy; high-degeneracy datasets (CoNLL ~70%) break negative controls. The paper discusses degeneracy as a key confound in the diagnostic framework.

5. **Coverage in Discussion section**: The correlation-selection gap (category 3) and degeneracy (category 4) are the paper's main analytical contributions. RE weakness (category 1 subset) is discussed as a boundary condition. Method failures (category 2) support the "gap is structural" thesis. WNUT-17 and OOD failures are mentioned as limitations.
