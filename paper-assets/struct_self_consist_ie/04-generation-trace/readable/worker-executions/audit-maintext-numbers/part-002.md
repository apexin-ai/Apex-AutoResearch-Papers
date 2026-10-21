# audit maintext numbers — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-maintext-numbers.md) · [Structured JSON](../../../sessions/29/29729505633f7ed8963e.json)

## Before a recorded user message

### Tool result

_source line 52 · 2026-05-24T04:32:39.412Z_

<details><summary>↩ Tool result · `toolu_01Cbg4qwmfbEB5EHtcmZUJtT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 196\\n  generated_at: '2026-05-22T13:13:25.551495+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: true\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\n  type: quantitative\\n  evidence: tab:epoch_scierc\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Under conservative df=4 adjustment, p=0.033\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\n    gap\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\n    0.10'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: LOO regret ranges from 0.51 to 1.21pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C064\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Seven independent methods all fail to close the correlation-selection gap\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  - exp_mrsc_multi_round\\n  - exp_lsc_latent_sc\\n  - exp_backup1_het_temp\\n  - exp_asb_adaptive_budget\\n  - exp_b1_scd_conll_control\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Instance degeneracy 13-87%\\n  type: empirical\\n  evidence:\\n  - exp_021_fewnerd_full\\n  - exp_002_conll_n16\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C069\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level self-judgment AUROC=0.51\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C073\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-sample frequency agreement AUROC=0.87\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C078\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Spider SQL degeneracy=87%\\n  type: empirical\\n  evidence:\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C084\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: +1.40pp on Few-NERD Holm p=0.006\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C091\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: +1.02pp on SciERC p=0.004\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C092\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ entity-level AUROC=0.512, indistinguishable from chance\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C094\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ P(yes|correct)=0.500, P(yes|incorrect)=0.500\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C097\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ-weighted construction F1=0.711 vs greedy 0.794\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C101\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: MRSC P(yes) separation=0.0006\\n  type: empirical\\n  evidence:\\n  - exp_mrsc_multi_round\\n  decisions: []\\n  deprecated: false\\n- id: C106\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: MRSC best F1=0.763 < greedy\\n  type: empirical\\n  evidence:\\n  - exp_mrsc_multi_round\\n  decisions: []\\n  deprecated: false\\n- id: C112\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: LSC centroid F1=0.759 < greedy 0.779\\n  type: empirical\\n  evidence:\\n  - exp_lsc_latent_sc\\n  decisions: []\\n  deprecated: false\\n- id: C119\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: LSC latent entity confidence F1=0.839 vs MV 0.837\\n  type: empirical\\n  evidence:\\n  - exp_lsc_latent_sc\\n  decisions: []\\n  deprecated: false\\n- id: C127\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: Frequency agreement AUROC=0.868\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C128\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Seven methods fail to close correlation-selection gap\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  - exp_mrsc_multi_round\\n  - exp_lsc_latent_sc\\n  - exp_backup1_het_temp\\n  - exp_asb_adaptive_budget\\n  - exp_b1_scd_conll_control\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C130\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Frequency agreement AUROC=0.87 vs self-judgment AUROC=0.51\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C133\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: +1.40pp Few-NERD, +1.02pp SciERC\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C137\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Spider SQL degeneracy=87%\\n  type: empirical\\n  evidence:\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C138\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: QE signals ρ up to 0.45 AUROC up to 0.82\\n  type: empirical\\n  evidence:\\n  - exp_001_ner_n16_scierc\\n  - exp_002_conll_n16\\n  decisions: []\\n  deprecated: false\\n- id: C140\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal outperforms greedy on SciERC p>0.05\\n  type: empirical\\n  evidence:\\n  - exp_010_selection_curves\\n  decisions: []\\n  deprecated: false\\n- id: C143\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: LP +1.39pp on Few-NERD Holm p_adj=0.019 k=19\\n  type: empirical\\n  evidence:\\n  - exp_021_fewnerd_full\\n  decisions: []\\n  deprecated: false\\n- id: C147\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 7 entity-level methods all fail\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  - exp_mrsc_multi_round\\n  - exp_lsc_latent_sc\\n  - exp_backup1_het_temp\\n  - exp_asb_adaptive_budget\\n  - exp_b1_scd_conll_control\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C152\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ AUROC=0.51 vs frequency agreement 0.87\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C158\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: MRSC P(yes) separation=0.0006\\n  type: empirical\\n  evidence:\\n  - exp_mrsc_multi_round\\n  decisions: []\\n  deprecated: false\\n- id: C165\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity verifier AUC=0.923 but +0.30pp F1\\n  type: empirical\\n  evidence:\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C173\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Spider SQL degeneracy=87.2%\\n  type: empirical\\n  evidence:\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C182\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Construction +1.40pp Few-NERD Holm p_adj=0.006\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C192\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Construction +1.02pp SciERC p=0.004\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C203\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model +0.42pp\\n  type: empirical\\n  evidence:\\n  - exp_cross_model_consistency\\n  decisions: []\\n  deprecated: false\\n- id: C215\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: θ_crit=0.70 degeneracy decomposition\\n  type: derived\\n  evidence:\\n  - theory.tex:sec:theory\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 83/116\\n  claims: 111\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 83\\n    tier3: 33\\n    tierX: 0\\n  last_checked: '2026-05-22T13:13:25.551590+00:00'\\n\", \"total_chars\": 40171, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "16cb9293-cafe-4578-b1ed-e2b79ab4040f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\\\", \\\"content\\\": \\\"paper:\\\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\\\n    Signals for Test-Time Scaling in Information Extraction'\\\\n  version: 196\\\\n  generated_at: '2026-05-22T13:13:25.551495+00:00'\\\\n  source: manual provenance build by Paper Agent\\\\nclaims:\\\\n- id: c001_voting_rho_scierc_ner\\\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\\\n    artifact)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  - related_work\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.voting_rho_full\\\\n    value: 0.379\\\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\\\n    via exp_012_rerun_1024 (max_tokens=1024).\\\\n- id: c002_auroc_dissociation_scierc\\\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\\\n    Voting leads ρ (NER 0.379, RE 0.422)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.em_auroc\\\\n    value: 0.749\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.em_auroc\\\\n    value: 0.706\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.voting_auroc\\\\n    value: 0.684\\\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\\\n    claim changed from \\\\\\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\\\\\" to split ρ (Voting\\\\n    0.38) / AUROC (EM 0.75) claim.\\\\n- id: c003_sj_rho_scierc_ner\\\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: bootstrap_ci_95.ner_sj\\\\n    value:\\\\n    - 0.2946\\\\n    - 0.4586\\\\n- id: c004_voting_leads_re\\\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.voting_rho_full\\\\n    value: 0.35\\\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\\\n- id: c005_fk_beats_sj_re\\\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.fk_rho_full\\\\n    value: 0.275\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re.sj_rho_full\\\\n    value: 0.25\\\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\\\n- id: c006_re_40pct_zero_f1\\\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: mvp_pilot_004\\\\n    metric: re_sample_f1_pct_zero\\\\n    value: 44.3\\\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\\\n  - exp_id: exp_008_re_n16_v2\\\\n    metric: f1_zero_pct\\\\n    value: 44.3\\\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\\\n- id: c007_em_leads_conll\\\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: em_rho_full\\\\n    value: 0.4507\\\\n  - exp_id: exp_002\\\\n    metric: em_auroc_full\\\\n    value: 0.8156\\\\n  - exp_id: exp_015_v2\\\\n    metric: auroc_best.EM.conll_ner\\\\n    value: 0.8156\\\\n- id: c008_cross_model_sj_stability\\\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: sj_rho_full\\\\n    value: 0.4357\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.SJ_rho\\\\n    value: 0.4314\\\\n- id: c009_logprob_paradox\\\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.logprob_AUROC\\\\n    value: 0.761\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.logprob_rho\\\\n    value: 0.3072\\\\n- id: c010_conll_oracle_headroom\\\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_002\\\\n    metric: oracle_headroom\\\\n    value: 0.042\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: oracle_headroom\\\\n    value: 0.0177\\\\n- id: c011_ner_no_reliable_selection\\\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\\\n    bootstrap)\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  - related_work\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner\\\\n    value:\\\\n      greedy: 0.644\\\\n      logprob: 0.65\\\\n      sj: 0.645\\\\n      voting: 0.634\\\\n      random: 0.608\\\\n      oracle: 0.776\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: bootstrap_selection_test\\\\n    value:\\\\n      logprob_vs_greedy_p: 0.39\\\\n      ci_95:\\\\n      - -0.03\\\\n      - 0.042\\\\n      cohens_d: 0.038\\\\n      sign_test: 61W/70L\\\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\\\n    with c012 — no signal reliably helps on either task.\\\\n- id: c012_re_no_signal_beats_greedy\\\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\\\n  sections:\\\\n  - abstract\\\\n  - introduction\\\\n  - experiments\\\\n  - conclusion\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re\\\\n    value:\\\\n      greedy: 0.404\\\\n      logprob: 0.395\\\\n      sj: 0.386\\\\n      voting: 0.359\\\\n      random: 0.354\\\\n      oracle: 0.585\\\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\\\\\"only logprob\\\\n    helps on RE (+2.3pp)\\\\\\\". Corrected via exp_016_rerun_1024_bootstrap.\\\\n- id: c013_oracle_headroom_ner\\\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner.oracle\\\\n    value: 0.776\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_ner.greedy\\\\n    value: 0.644\\\\n- id: c014_re_oracle_headroom\\\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re.oracle\\\\n    value: 0.585\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: selection_f1_re.greedy\\\\n    value: 0.404\\\\n- id: c015_ensemble_auroc\\\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\\\n  sections:\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: ensemble_ner_auroc\\\\n    value: 0.666\\\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\\\n    finding.\\\\n- id: c016_ece_calibration\\\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\\\n    miscalibration (ECE 0.109-0.339)\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_016_rerun_1024_bootstrap\\\\n    metric: calibration_ece\\\\n    value:\\\\n      ner_range: 0.069-0.096\\\\n      re_range: 0.109-0.339\\\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\\\n- id: c017_fisher_z_ner_vs_re\\\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: fisher_z_ner_vs_re.sj_z\\\\n    value: 2.31\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: fisher_z_ner_vs_re.sj_p\\\\n    value: 0.0209\\\\n- id: c018_per_relation_diagnostic\\\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\\\n    value: 0.004\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\\\n    value: 0.646\\\\n- id: c019_entity_span_errors\\\\n  text: Entity span errors account for 55.5% of RE false negatives\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_004_re_diagnostic\\\\n    metric: error_propagation\\\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\\\n      21.7% → entity span errors ~55.5%\\\\n  note: Computed from error_propagation breakdown in exp_004\\\\n- id: c020_capability_stratification_ner\\\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\\\n    value: 0.547\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\\\n    value: 0.415\\\\n- id: c021_wnut_boundary\\\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\\\n  sections:\\\\n  - experiments\\\\n  - conclusion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: rho_sj\\\\n    value: 0.089\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: sample_f1_pct_zero\\\\n    value: 53.7\\\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\\\n- id: c022_wnut_logprob_negative\\\\n  text: WNUT logprob shows strong negative correlation\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_003_ner_wnut17\\\\n    metric: ner.rho_logprob_full\\\\n    value: -0.414\\\\n  - exp_id: exp_003_wnut17_eval\\\\n    metric: rho_logprob_full\\\\n    value: -0.409\\\\n- id: c023_re_sent_length_sj\\\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 2\\\\n  evidence:\\\\n  - exp_id: exp_009_v2_re_rerun\\\\n    metric: by_sent_len_quartiles\\\\n    value:\\\\n      Q1_sj_rho: 0.11\\\\n      Q4_sj_rho: 0.473\\\\n      fisher_z_p: 0.004\\\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\\\n- id: c024_high_complexity_re_subset\\\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 2\\\\n  evidence:\\\\n  - exp_id: exp_009_capability_stratification\\\\n    metric: scierc_re.by_rel_count\\\\n    value:\\\\n      6plus_sj_rho: 0.527\\\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\\\n    logprob values not in registry summary.\\\\n- id: c025_temperature_sj_stable\\\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    metric: sj_rho_t07_ner\\\\n    value: 0.388\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\\\n- id: c026_n_scaling_sj\\\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\\\n    SciERC NER\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.36\\\\n  - exp_id: exp_001_seed42_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.428\\\\n  - exp_id: exp_001_seed123_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.424\\\\n  - exp_id: exp_001_seed456_v2_ner\\\\n    metric: full.SJ.rho\\\\n    value: 0.384\\\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\\\n- id: c027_llama_conll_3seed\\\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: full.SJ_rho\\\\n    value: 0.4698\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    metric: full.SJ_rho\\\\n    value: 0.4552\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3058\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: full.logprob_rho\\\\n    value: 0.3161\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    metric: full.logprob_rho\\\\n    value: 0.3078\\\\n- id: c028_loo_sj_circularity\\\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_015_v2\\\\n    metric: loo_sj.max_delta_rho\\\\n    value: 0.000305\\\\n  - exp_id: exp_015_v2\\\\n    metric: loo_sj.all_no_circularity\\\\n    value: true\\\\n- id: c029_llama_scierc_cross_model\\\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: ner.rho_sj\\\\n    value: 0.363\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: ner.rho_fk\\\\n    value: 0.327\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: re.sj_rho_cond\\\\n    value: 0.405\\\\n  - exp_id: exp_007_llama_inference\\\\n    metric: re.fk_rho_cond\\\\n    value: 0.259\\\\n- id: c030_em_conditional_dominance\\\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: ner.em_rho_cond\\\\n    value: 0.3427\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: re.em_rho_cond\\\\n    value: 0.3607\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: conditional.EM_rho\\\\n    value: 0.4658\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    metric: conditional.EM_rho\\\\n    value: 0.4732\\\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\\\n    seed/N combinations.'\\\\n- id: c031_em_conditional_scierc\\\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_cond_em_rho\\\\n    value: 0.414\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: re_cond_em_rho\\\\n    value: 0.475\\\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\\\n- id: c032_logprob_re_cond_collapse\\\\n  text: Logprob conditional RE collapses to ρ=0.011\\\\n  sections:\\\\n  - experiments\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    metric: re_cond.logprob.rho\\\\n    value: 0.0112\\\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\\\n    0.002 was stale and untraceable.'\\\\n- id: c033_sj_n16_cond_re\\\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_008_re_n16_v2\\\\n    metric: sj_rho_cond\\\\n    value: 0.308\\\\n- id: c034_structural_over_logprob_n16\\\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\\\n    to +0.175)\\\\n  sections:\\\\n  - experiments\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_voting_conf_rho\\\\n    value: 0.399\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    metric: ner_logprob_rho\\\\n    value: 0.237\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: full.EM_rho\\\\n    value: 0.4627\\\\n  - exp_id: exp_002_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3146\\\\n  - exp_id: exp_007_llama_n16\\\\n    metric: full.voting_conf_rho\\\\n    value: 0.4515\\\\n  - exp_id: exp_007_llama_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.2041\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.logprob_rho\\\\n    value: 0.3058\\\\n- id: c035_n_scaling_diminishing\\\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\\\n  sections:\\\\n  - discussion\\\\n  tier: 1\\\\n  evidence:\\\\n  - exp_id: exp_001_seed42_v2\\\\n    metric: sj_rho_full\\\\n    value: 0.428\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    metric: ner.sj_rho_full\\\\n    value: 0.3565\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    metric: full.SJ_rho\\\\n    value: 0.4642\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    metric: full.SJ_rho\\\\n    value: 0.4314\\\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\\\n    - 0.431 = +0.032'\\\\n- id: c036_sj_ece_calibration\\\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\\\n    settings)'\\\\n  sections: []\\\\n  tier: X\\\\n  evidence: []\\\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\\\n    signals ECE 0.27-0.77.\\\\n- id: C001\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: No signal significantly improves sample selection over greedy decoding despite\\\\n    13-18pp oracle headroom\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions:\\\\n  - D070\\\\n  - D071\\\\n  deprecated: true\\\\n- id: C003\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\\\n    decoding\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C006\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C010\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Constrained-decoding score compression is the primary bottleneck\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C011\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP carries useful per-sample quality information; score compression is the\\\\n    primary bottleneck\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions:\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C013\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR utility correlates with F1 across instances but not within\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C016\\\\n  location:\\\\n    section: discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\\\n  type: planned\\\\n  evidence: []\\\\n  decisions:\\\\n  - D071\\\\n  deprecated: false\\\\n- id: C017\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\\\n    at selection\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C019\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP fails due to constrained-decoding score compression\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C022\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RE findings preliminary, single benchmark\\\\n  type: scope_limitation\\\\n  evidence:\\\\n  - exp_012_rerun_1024\\\\n  decisions: []\\\\n  deprecated: true\\\\n- id: C023\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\\\n    LP on SciERC, but selection performs worse (-2.0pp)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: scierc_entity_lp_variance_ratio\\\\n    value: 4.0x\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: scierc_entity_lp_selection_delta\\\\n    value: -1.68\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C024\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\\\n    79% tied\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: conll_entity_lp_variance_median\\\\n    value: 2e-10\\\\n  - exp_id: exp_entity_token_lp\\\\n    metric: conll_entity_lp_tied_fraction\\\\n    value: 0.794\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C025\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\\\n    intrinsic model overconfidence on entity tokens\\\\n  type: interpretive\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C026\\\\n  location:\\\\n    section: sections/limitations\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\\\n    are unexplored\\\\n  type: scope\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C027\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\\\n    failure are the findings'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C028\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\\\n    characterization'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C029\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\\\n  type: structural\\\\n  evidence:\\\\n  - exp_id: exp_entity_token_lp\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C030\\\\n  location:\\\\n    section: sections/abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\\\n    from 9 to 6 sentences'\\\\n  type: structural\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C031\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C032\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C033\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 13% of SciERC instances yield constant utility scores\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C034\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 49% of CoNLL instances yield constant utility scores\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C035\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SJ median within-instance rho = 0.524 on SciERC\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C036\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C037\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C038\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\\\n  type: quantitative\\\\n  evidence: Q1 within-instance analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C039\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\\\n  type: quantitative\\\\n  evidence: SF4 greedy data\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C040\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\\\n  type: quantitative\\\\n  evidence: tab:epoch_scierc\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C041\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C042\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C043\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C044\\\\n  location:\\\\n    section: sections/discussion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C045\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C046\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Under conservative df=4 adjustment, p=0.033\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C047\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C048\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C049\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C050\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C051\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\\\n    gap\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C052\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\\\n    0.10'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C053\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LOO regret ranges from 0.51 to 1.21pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C054\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C055\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C056\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C057\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C058\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C059\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C060\\\\n  location:\\\\n    section: sections/experiments\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C061\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C062\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C063\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C064\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Seven independent methods all fail to close the correlation-selection gap\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  - exp_mrsc_multi_round\\\\n  - exp_lsc_latent_sc\\\\n  - exp_backup1_het_temp\\\\n  - exp_asb_adaptive_budget\\\\n  - exp_b1_scd_conll_control\\\\n  - adaptive.tex:sec:verifier\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C066\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Instance degeneracy 13-87%\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_021_fewnerd_full\\\\n  - exp_002_conll_n16\\\\n  - exp_spider_sc_pilot\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C069\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity-level self-judgment AUROC=0.51\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C073\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Cross-sample frequency agreement AUROC=0.87\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C078\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Spider SQL degeneracy=87%\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_spider_sc_pilot\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C084\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: +1.40pp on Few-NERD Holm p=0.006\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_entity_construction\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C091\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: +1.02pp on SciERC p=0.004\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_entity_construction\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C092\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: ESJ entity-level AUROC=0.512, indistinguishable from chance\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C094\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: ESJ P(yes|correct)=0.500, P(yes|incorrect)=0.500\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C097\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: ESJ-weighted construction F1=0.711 vs greedy 0.794\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C101\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MRSC P(yes) separation=0.0006\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_mrsc_multi_round\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C106\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MRSC best F1=0.763 < greedy\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_mrsc_multi_round\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C112\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LSC centroid F1=0.759 < greedy 0.779\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_lsc_latent_sc\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C119\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LSC latent entity confidence F1=0.839 vs MV 0.837\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_lsc_latent_sc\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C127\\\\n  location:\\\\n    section: mechanistic\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Frequency agreement AUROC=0.868\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C128\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Seven methods fail to close correlation-selection gap\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  - exp_mrsc_multi_round\\\\n  - exp_lsc_latent_sc\\\\n  - exp_backup1_het_temp\\\\n  - exp_asb_adaptive_budget\\\\n  - exp_b1_scd_conll_control\\\\n  - adaptive.tex:sec:verifier\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C130\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Frequency agreement AUROC=0.87 vs self-judgment AUROC=0.51\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C133\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: +1.40pp Few-NERD, +1.02pp SciERC\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_entity_construction\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C137\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Spider SQL degeneracy=87%\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_spider_sc_pilot\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C138\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: QE signals ρ up to 0.45 AUROC up to 0.82\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_001_ner_n16_scierc\\\\n  - exp_002_conll_n16\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C140\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: No signal outperforms greedy on SciERC p>0.05\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_010_selection_curves\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C143\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: LP +1.39pp on Few-NERD Holm p_adj=0.019 k=19\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_021_fewnerd_full\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C147\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 7 entity-level methods all fail\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  - exp_mrsc_multi_round\\\\n  - exp_lsc_latent_sc\\\\n  - exp_backup1_het_temp\\\\n  - exp_asb_adaptive_budget\\\\n  - exp_b1_scd_conll_control\\\\n  - adaptive.tex:sec:verifier\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C152\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: ESJ AUROC=0.51 vs frequency agreement 0.87\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_esj_entity_self_judgment\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C158\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: MRSC P(yes) separation=0.0006\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_mrsc_multi_round\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C165\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Entity verifier AUC=0.923 but +0.30pp F1\\\\n  type: empirical\\\\n  evidence:\\\\n  - adaptive.tex:sec:verifier\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C173\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Spider SQL degeneracy=87.2%\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_spider_sc_pilot\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C182\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Construction +1.40pp Few-NERD Holm p_adj=0.006\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_entity_construction\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C192\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Construction +1.02pp SciERC p=0.004\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_entity_construction\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C203\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Cross-model +0.42pp\\\\n  type: empirical\\\\n  evidence:\\\\n  - exp_cross_model_consistency\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C215\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: θ_crit=0.70 degeneracy decomposition\\\\n  type: derived\\\\n  evidence:\\\\n  - theory.tex:sec:theory\\\\n  decisions: []\\\\n  deprecated: false\\\\ntables:\\\\n- id: tab:notation\\\\n  section: method\\\\n  caption: Notation used throughout the paper\\\\n  evidence: []\\\\n  note: Notation table—no experimental data.\\\\n- id: tab:quality_estimation\\\\n  section: experiments\\\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\\\n  evidence:\\\\n  - exp_id: exp_012_rerun_1024\\\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\\\n  - exp_id: exp_015_v2\\\\n    role: AUROC values across settings\\\\n  - exp_id: exp_002\\\\n    role: CoNLL Qwen N=8 ρ and AUROC\\\\n  - exp_id: exp_017_llama_conll_infer\\\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\\\n- id: tab:selection\\\\n  section: experiments\\\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\\\n  evidence:\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: All selection F1 values (NER and RE)\\\\n- id: tab:robustness\\\\n  section: experiments\\\\n  caption: Signal robustness across configurations (Spearman ρ)\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: N=8 baseline values\\\\n  - exp_id: exp_001_seed42_v2\\\\n    role: N=16 SJ ρ seed=42\\\\n  - exp_id: exp_001_seed123_v2\\\\n    role: N=16 SJ ρ seed=123\\\\n  - exp_id: exp_001_seed456_v2_ner\\\\n    role: N=16 SJ ρ seed=456\\\\n  - exp_id: exp_017_llama_conll_n16\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\\\n  - exp_id: exp_017_llama_conll_n16_s123\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\\\n  - exp_id: exp_017_llama_conll_n16_s456\\\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\\\nfigures:\\\\n- id: fig:overview\\\\n  section: introduction\\\\n  caption: The correlation-selection gap conceptual diagram\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Quality estimation data (ρ, AUROC for left panel)\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: Selection F1 data (right panel)\\\\n- id: fig:signal_heatmap\\\\n  section: experiments\\\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\\\n  - exp_id: exp_002\\\\n    role: CoNLL Qwen full set ρ values\\\\n  - exp_id: exp_001_ner_n16_scierc\\\\n    role: Conditional set ρ values\\\\n- id: fig:selection_gap\\\\n  section: experiments\\\\n  caption: The correlation-selection gap on SciERC (N=8)\\\\n  evidence:\\\\n  - exp_id: exp_016_signal_ensemble\\\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\\\n- id: fig:temperature_robustness\\\\n  section: experiments\\\\n  caption: Temperature robustness on SciERC (N=8)\\\\n  evidence:\\\\n  - exp_id: exp_005\\\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\\\n- id: fig:reliability\\\\n  section: experiments\\\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\\\n  evidence:\\\\n  - exp_id: exp_015_metrics_expansion\\\\n    role: Calibration/ECE data for all signals\\\\n  - exp_id: exp_002\\\\n    role: ECE values across signals\\\\n_completeness:\\\\n  coverage: 83/116\\\\n  claims: 111\\\\n  tables: 4\\\\n  figures: 5\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 83\\\\n    tier3: 33\\\\n    tierX: 0\\\\n  last_checked: '2026-05-22T13:13:25.551590+00:00'\\\\n\\\", \\\"total_chars\\\": 40171, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 196\\n  generated_at: '2026-05-22T13:13:25.551495+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: true\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: true\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\\n  type: quantitative\\n  evidence: tab:epoch_scierc\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -0.64pp on CoNLL\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Under conservative df=4 adjustment, p=0.033\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 3-epoch SciERC mean within-instance rho=0.273\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 5-epoch SciERC mean within-instance rho=0.179\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\\n    gap\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\\n    0.10'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: LOO regret ranges from 0.51 to 1.21pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Even with oracle tau, CoNLL remains at -0.31pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/experiments\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C064\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Seven independent methods all fail to close the correlation-selection gap\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  - exp_mrsc_multi_round\\n  - exp_lsc_latent_sc\\n  - exp_backup1_het_temp\\n  - exp_asb_adaptive_budget\\n  - exp_b1_scd_conll_control\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Instance degeneracy 13-87%\\n  type: empirical\\n  evidence:\\n  - exp_021_fewnerd_full\\n  - exp_002_conll_n16\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C069\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-level self-judgment AUROC=0.51\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C073\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-sample frequency agreement AUROC=0.87\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C078\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Spider SQL degeneracy=87%\\n  type: empirical\\n  evidence:\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C084\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: +1.40pp on Few-NERD Holm p=0.006\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C091\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: +1.02pp on SciERC p=0.004\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C092\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ entity-level AUROC=0.512, indistinguishable from chance\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C094\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ P(yes|correct)=0.500, P(yes|incorrect)=0.500\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C097\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ-weighted construction F1=0.711 vs greedy 0.794\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C101\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: MRSC P(yes) separation=0.0006\\n  type: empirical\\n  evidence:\\n  - exp_mrsc_multi_round\\n  decisions: []\\n  deprecated: false\\n- id: C106\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: MRSC best F1=0.763 < greedy\\n  type: empirical\\n  evidence:\\n  - exp_mrsc_multi_round\\n  decisions: []\\n  deprecated: false\\n- id: C112\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: LSC centroid F1=0.759 < greedy 0.779\\n  type: empirical\\n  evidence:\\n  - exp_lsc_latent_sc\\n  decisions: []\\n  deprecated: false\\n- id: C119\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: LSC latent entity confidence F1=0.839 vs MV 0.837\\n  type: empirical\\n  evidence:\\n  - exp_lsc_latent_sc\\n  decisions: []\\n  deprecated: false\\n- id: C127\\n  location:\\n    section: mechanistic\\n    paragraph: 0\\n    sentence: 0\\n  text: Frequency agreement AUROC=0.868\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C128\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Seven methods fail to close correlation-selection gap\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  - exp_mrsc_multi_round\\n  - exp_lsc_latent_sc\\n  - exp_backup1_het_temp\\n  - exp_asb_adaptive_budget\\n  - exp_b1_scd_conll_control\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C130\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Frequency agreement AUROC=0.87 vs self-judgment AUROC=0.51\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C133\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: +1.40pp Few-NERD, +1.02pp SciERC\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C137\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Spider SQL degeneracy=87%\\n  type: empirical\\n  evidence:\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C138\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: QE signals ρ up to 0.45 AUROC up to 0.82\\n  type: empirical\\n  evidence:\\n  - exp_001_ner_n16_scierc\\n  - exp_002_conll_n16\\n  decisions: []\\n  deprecated: false\\n- id: C140\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal outperforms greedy on SciERC p>0.05\\n  type: empirical\\n  evidence:\\n  - exp_010_selection_curves\\n  decisions: []\\n  deprecated: false\\n- id: C143\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: LP +1.39pp on Few-NERD Holm p_adj=0.019 k=19\\n  type: empirical\\n  evidence:\\n  - exp_021_fewnerd_full\\n  decisions: []\\n  deprecated: false\\n- id: C147\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 7 entity-level methods all fail\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  - exp_mrsc_multi_round\\n  - exp_lsc_latent_sc\\n  - exp_backup1_het_temp\\n  - exp_asb_adaptive_budget\\n  - exp_b1_scd_conll_control\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C152\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: ESJ AUROC=0.51 vs frequency agreement 0.87\\n  type: empirical\\n  evidence:\\n  - exp_esj_entity_self_judgment\\n  decisions: []\\n  deprecated: false\\n- id: C158\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: MRSC P(yes) separation=0.0006\\n  type: empirical\\n  evidence:\\n  - exp_mrsc_multi_round\\n  decisions: []\\n  deprecated: false\\n- id: C165\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity verifier AUC=0.923 but +0.30pp F1\\n  type: empirical\\n  evidence:\\n  - adaptive.tex:sec:verifier\\n  decisions: []\\n  deprecated: false\\n- id: C173\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Spider SQL degeneracy=87.2%\\n  type: empirical\\n  evidence:\\n  - exp_spider_sc_pilot\\n  decisions: []\\n  deprecated: false\\n- id: C182\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Construction +1.40pp Few-NERD Holm p_adj=0.006\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C192\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Construction +1.02pp SciERC p=0.004\\n  type: empirical\\n  evidence:\\n  - exp_entity_construction\\n  decisions: []\\n  deprecated: false\\n- id: C203\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model +0.42pp\\n  type: empirical\\n  evidence:\\n  - exp_cross_model_consistency\\n  decisions: []\\n  deprecated: false\\n- id: C215\\n  location:\\n    section: introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: θ_crit=0.70 degeneracy decomposition\\n  type: derived\\n  evidence:\\n  - theory.tex:sec:theory\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 83/116\\n  claims: 111\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 83\\n    tier3: 33\\n    tierX: 0\\n  last_checked: '2026-05-22T13:13:25.551590+00:00'\\n\", \"total_chars\": 40171, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01L6nndCXbR2H6Aysx1wZB1r`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor exp_id, exp in exps.items():\n    status = exp.get('status','?')\n    metrics = exp.get('metrics',{})\n    if metrics:\n        print(f'=== {exp_id} ({status}) ===')\n        for k,v in list(metrics.items())[:20]:\n            print(f'  {k}: {v}')\n        print()\n\" 2>&1 | head -200",
  "description": "Extract experiments with metrics from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "be630e47-4656-4b05-abd3-e7df73dd7709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcqfxhYjdwKoCnrzXo9J2D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 58215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-24T04:32:42.497Z_

<details><summary>↩ Tool result · `toolu_01L6nndCXbR2H6Aysx1wZB1r`</summary>

```text
=== exp_fewnerd_pretrained_n32_s42_v2 (DONE) ===
  greedy_f1: 0.539
  mv_f1: 0.577
  mv_delta_pp: 3.85
  lp_f1: 0.529
  lp_delta_pp: -1.03
  oracle_f1: 0.705
  oracle_delta_pp: 16.56
  degeneracy_rate: 5.42
  capture_rate: 19
  sj_rho: 0.456
  n_instances_gold_nonempty: 32565
  subset: gold-nonempty

=== exp_fewnerd_pretrained_n16_s42_v2 (DONE) ===
  greedy_f1: 0.5373
  mv_strict_f1: 0.5779
  mv_delta_strict_pp: 4.06
  mv_incl_f1: 0.5722
  oracle_f1: 0.6786
  degeneracy_rate: 0.076
  alpha_crit_eff_strict: 0.4398
  alpha_crit_strict: 0.4064
  mv_capture_rate: 0.2876
  n_total: 37648
  n_gold_nonempty: 32565
  greedy_f1_all: 0.5109
  oracle_f1_all: 0.6433
  sj_rho_full: 0.453
  fk_rho_full: 0.401
  lp_rho_full: 0.192
  structural_beats_surface: True
  note: Primary metrics (greedy/mv/oracle) computed on gold-nonempty instances (n=32565) via recompute_alpha_crit_unified.py. _all suffix = full instances incl gold-empty.

=== exp_scierc_n8_s456 (DONE) ===
  greedy_f1: 0.6657
  mv_f1: 0.6573
  mv_delta_pp: -0.84
  lp_f1: 0.6626
  lp_delta_pp: -0.31
  degeneracy_rate: 0.12
  agreement_rate: 0.6597
  oracle_f1: 0.7733
  fleiss_kappa: 0.3864
  soft_jaccard: 0.6939
  note: MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).

=== exp_scierc_n8_s123 (DONE) ===
  greedy_f1: 0.6613
  mv_f1: 0.6648
  mv_delta_pp: 0.34
  lp_f1: 0.6698
  lp_delta_pp: 0.85
  degeneracy_rate: 0.116
  agreement_rate: 0.6646
  oracle_f1: 0.7794
  fleiss_kappa: 0.3847
  soft_jaccard: 0.6979
  note: MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).

=== exp_scierc_n8_s3141 (DONE) ===
  greedy_f1: 0.6609
  oracle_f1: 0.7645
  oracle_headroom: 0.1036
  fleiss_kappa_mean: 0.2906
  soft_jaccard_mean: 0.6265
  rho_sj_f1_full: 0.3477
  rho_kappa_f1_full: 0.2074
  rho_sj_f1_cond: 0.2427
  rho_kappa_f1_cond: 0.0806
  structural_beats_surface: True
  rho_advantage: 0.1404
  logprob_rho_full: 0.1926
  logprob_auroc_full: 0.5733
  logprob_rho_cond: 0.1231
  logprob_auroc_cond: 0.5399
  sample_f1_mean: 0.5802
  sample_f1_std: 0.3357
  sample_f1_pct_zero: 16.5
  n_instances: 551
  degeneracy_rate: 16.5

=== exp_scierc_n8_s2024 (DONE) ===
  greedy_f1: 0.6641
  oracle_f1: 0.7914
  oracle_headroom: 0.1273
  fleiss_kappa_mean: 0.3572
  soft_jaccard_mean: 0.6606
  rho_sj_f1_full: 0.337
  rho_kappa_f1_full: 0.2356
  rho_sj_f1_cond: 0.289
  rho_kappa_f1_cond: 0.1465
  structural_beats_surface: True
  rho_advantage: 0.1014
  logprob_rho_full: 0.1831
  logprob_auroc_full: 0.5629
  logprob_rho_cond: 0.1196
  logprob_auroc_cond: 0.5305
  sample_f1_mean: 0.5971
  sample_f1_std: 0.3243
  sample_f1_pct_zero: 14.1
  n_instances: 551
  degeneracy_rate: 14.1

=== exp_esj_qwen3_all (DONE) ===
  scierc: {'n_instances': 551, 'n_entities': 2768, 'p_yes_mean': 0.382, 'construction_f1': {'greedy': 0.6497, 'best_mv': 0.6469, 'best_esj': 0.5756, 'oracle': 0.7824}, 'entity_signal': {'esj_rho': 0.02, 'esj_auroc': 0.512, 'agree_rho': 0.515, 'agree_auroc': 0.792}, 'within_instance': {'esj_rho': 0.056, 'lp_rho': 0.188}, 'selection_f1': {'esj': 0.589, 'lp': 0.647}}
  conll: {'n_instances': 3453, 'n_entities': 8054, 'p_yes_mean': 0.5, 'construction_f1': {'greedy': 0.9091, 'best_mv': 0.9066, 'best_esj': 0.8237, 'oracle': 0.9551}, 'entity_signal': {'esj_rho': 0.087, 'esj_auroc': 0.553, 'agree_rho': 0.777, 'agree_auroc': 0.941}, 'within_instance': {'esj_rho': -0.008, 'lp_rho': 0.28}, 'selection_f1': {'esj': 0.846, 'lp': 0.899}}
  fewnerd: {'n_instances': 37648, 'n_entities': 169790, 'p_yes_mean': 0.652, 'construction_f1': {'greedy': 0.7717, 'best_mv': 0.764, 'best_esj': 0.6817, 'oracle': 0.8729}, 'entity_signal': {'esj_rho': -0.008, 'esj_auroc': 0.495, 'agree_rho': 0.673, 'agree_auroc': 0.881}, 'within_instance': {'esj_rho': 0.332, 'lp_rho': 0.543}, 'selection_f1': {'esj': 0.686, 'lp': 0.781}}

=== exp_fewnerd_mf4_s456 (DONE) ===
  greedy_f1: 0.7909
  oracle_f1: 0.881
  mv_strict_f1: 0.7685
  mv_delta_pp: -2.24
  lp_f1: 0.7921
  lp_delta_pp: 0.12
  degeneracy_rate: 0.081
  oracle_headroom_pp: 9.01
  fleiss_kappa_mean: 0.3555
  soft_jaccard_mean: 0.6845
  rho_sj_full: 0.3122
  rho_sj_cond: 0.2559
  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)

=== exp_fewnerd_mf4_s123_v2 (DONE) ===
  greedy_f1: 0.7909
  oracle_f1: 0.8892
  mv_strict_f1: 0.7648
  mv_delta_pp: -2.61
  lp_f1: 0.7918
  lp_delta_pp: 0.09
  degeneracy_rate: 0.093
  oracle_headroom_pp: 9.83
  fleiss_kappa_mean: 0.3503
  soft_jaccard_mean: 0.6701
  rho_sj_full: 0.308
  rho_sj_cond: 0.201
  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)

=== exp_fewnerd_pretrained_n32_s42 (DONE) ===
  kill_reason: UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.
  progress_at_kill: 70% (838K/1.2M prompts, ~11h elapsed)
  fix_status: sampling.py errors='replace' already deployed on autodl-5090-c

=== exp_fewnerd_pretrained_n16_s42 (DONE) ===
  crash_reason: UnicodeEncodeError in sampling.py:675 — vLLM lone Unicode surrogates in output, UTF-8 encoding rejects
  progress: 72% (27110/37648)
  fix_applied: sampling.py line 673: errors='replace' added to file write

=== exp_conll_freeform_n8_s42 (DONE) ===
  greedy_f1: 0.9046
  mv_strict_f1: 0.8994
  mv_delta_pp: -0.52
  lp_f1: 0.8951
  lp_delta_pp: -0.95
  degeneracy_rate: 0.6
  lp_std_ratio: 0.023466
  n_instances: 2756
  vs_constrained: {'greedy_f1_delta': -0.0042, 'mv_delta_change': '+0.43pp (less hurt)', 'degen_delta': '+3.0pp (higher in freeform)', 'lp_std_ratio_delta': -0.0022}

=== exp_fewnerd_freeform_n8_s42 (DONE) ===
  greedy_f1: 0.7913
  mv_strict_f1: 0.7586
  mv_delta_pp: -3.26
  lp_f1: 0.7922
  lp_delta_pp: 0.09
  degeneracy_rate: 0.091
  n_instances: 32565
  vs_constrained: {'greedy_f1_delta': '+0.00pp', 'mv_delta_change': '+0.01pp (identical)', 'lp_delta_change': '+0.02pp (identical)', 'degen_delta': '0.0pp (identical)'}
  note: Freeform ≈ constrained on FewNERD. All deltas <0.02pp. Degeneracy 9.1% both. Fine-grained entity types constrain output space enough that grammar constraints have no additional effect.

=== exp_fewnerd_5epoch_lp_s42 (DONE) ===
  greedy_f1: 0.7942
  oracle_headroom_pp: 8.06
  fleiss_kappa: 0.529
  lp_auroc: 0.662
  lp_rho: 0.302
  lp_delta_pp_cpu_recompute: 0.12
  lp_delta_pp_cpu_recompute_std: 0.04
  note: GPU inference completed after kill; CPU recompute from existing samples gave LP Δ=+0.12±0.04pp (2-seed)

=== exp_fewnerd_mf4_s42 (DONE) ===
  greedy_f1: 0.7911
  oracle_f1: 0.8787
  mv_strict_f1: 0.7585
  mv_delta_pp: -3.27
  lp_f1: 0.7918
  lp_delta_pp: 0.07
  degeneracy_rate: 0.091
  oracle_headroom_pp: 8.76
  fleiss_kappa_mean: 0.3537
  soft_jaccard_mean: 0.6751
  rho_sj_full: 0.1648
  rho_sj_cond: 0.1989
  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)

=== exp_fewnerd_n32_s42 (DONE) ===
  greedy_f1: 0.7914
  mv_strict_f1: 0.7818
  mv_delta_strict_pp: -0.96
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "d47a6909-c900-460f-b03d-86a8a705769d",
  "tool_use_result": {
    "stdout": "=== exp_fewnerd_pretrained_n32_s42_v2 (DONE) ===\n  greedy_f1: 0.539\n  mv_f1: 0.577\n  mv_delta_pp: 3.85\n  lp_f1: 0.529\n  lp_delta_pp: -1.03\n  oracle_f1: 0.705\n  oracle_delta_pp: 16.56\n  degeneracy_rate: 5.42\n  capture_rate: 19\n  sj_rho: 0.456\n  n_instances_gold_nonempty: 32565\n  subset: gold-nonempty\n\n=== exp_fewnerd_pretrained_n16_s42_v2 (DONE) ===\n  greedy_f1: 0.5373\n  mv_strict_f1: 0.5779\n  mv_delta_strict_pp: 4.06\n  mv_incl_f1: 0.5722\n  oracle_f1: 0.6786\n  degeneracy_rate: 0.076\n  alpha_crit_eff_strict: 0.4398\n  alpha_crit_strict: 0.4064\n  mv_capture_rate: 0.2876\n  n_total: 37648\n  n_gold_nonempty: 32565\n  greedy_f1_all: 0.5109\n  oracle_f1_all: 0.6433\n  sj_rho_full: 0.453\n  fk_rho_full: 0.401\n  lp_rho_full: 0.192\n  structural_beats_surface: True\n  note: Primary metrics (greedy/mv/oracle) computed on gold-nonempty instances (n=32565) via recompute_alpha_crit_unified.py. _all suffix = full instances incl gold-empty.\n\n=== exp_scierc_n8_s456 (DONE) ===\n  greedy_f1: 0.6657\n  mv_f1: 0.6573\n  mv_delta_pp: -0.84\n  lp_f1: 0.6626\n  lp_delta_pp: -0.31\n  degeneracy_rate: 0.12\n  agreement_rate: 0.6597\n  oracle_f1: 0.7733\n  fleiss_kappa: 0.3864\n  soft_jaccard: 0.6939\n  note: MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).\n\n=== exp_scierc_n8_s123 (DONE) ===\n  greedy_f1: 0.6613\n  mv_f1: 0.6648\n  mv_delta_pp: 0.34\n  lp_f1: 0.6698\n  lp_delta_pp: 0.85\n  degeneracy_rate: 0.116\n  agreement_rate: 0.6646\n  oracle_f1: 0.7794\n  fleiss_kappa: 0.3847\n  soft_jaccard: 0.6979\n  note: MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).\n\n=== exp_scierc_n8_s3141 (DONE) ===\n  greedy_f1: 0.6609\n  oracle_f1: 0.7645\n  oracle_headroom: 0.1036\n  fleiss_kappa_mean: 0.2906\n  soft_jaccard_mean: 0.6265\n  rho_sj_f1_full: 0.3477\n  rho_kappa_f1_full: 0.2074\n  rho_sj_f1_cond: 0.2427\n  rho_kappa_f1_cond: 0.0806\n  structural_beats_surface: True\n  rho_advantage: 0.1404\n  logprob_rho_full: 0.1926\n  logprob_auroc_full: 0.5733\n  logprob_rho_cond: 0.1231\n  logprob_auroc_cond: 0.5399\n  sample_f1_mean: 0.5802\n  sample_f1_std: 0.3357\n  sample_f1_pct_zero: 16.5\n  n_instances: 551\n  degeneracy_rate: 16.5\n\n=== exp_scierc_n8_s2024 (DONE) ===\n  greedy_f1: 0.6641\n  oracle_f1: 0.7914\n  oracle_headroom: 0.1273\n  fleiss_kappa_mean: 0.3572\n  soft_jaccard_mean: 0.6606\n  rho_sj_f1_full: 0.337\n  rho_kappa_f1_full: 0.2356\n  rho_sj_f1_cond: 0.289\n  rho_kappa_f1_cond: 0.1465\n  structural_beats_surface: True\n  rho_advantage: 0.1014\n  logprob_rho_full: 0.1831\n  logprob_auroc_full: 0.5629\n  logprob_rho_cond: 0.1196\n  logprob_auroc_cond: 0.5305\n  sample_f1_mean: 0.5971\n  sample_f1_std: 0.3243\n  sample_f1_pct_zero: 14.1\n  n_instances: 551\n  degeneracy_rate: 14.1\n\n=== exp_esj_qwen3_all (DONE) ===\n  scierc: {'n_instances': 551, 'n_entities': 2768, 'p_yes_mean': 0.382, 'construction_f1': {'greedy': 0.6497, 'best_mv': 0.6469, 'best_esj': 0.5756, 'oracle': 0.7824}, 'entity_signal': {'esj_rho': 0.02, 'esj_auroc': 0.512, 'agree_rho': 0.515, 'agree_auroc': 0.792}, 'within_instance': {'esj_rho': 0.056, 'lp_rho': 0.188}, 'selection_f1': {'esj': 0.589, 'lp': 0.647}}\n  conll: {'n_instances': 3453, 'n_entities': 8054, 'p_yes_mean': 0.5, 'construction_f1': {'greedy': 0.9091, 'best_mv': 0.9066, 'best_esj': 0.8237, 'oracle': 0.9551}, 'entity_signal': {'esj_rho': 0.087, 'esj_auroc': 0.553, 'agree_rho': 0.777, 'agree_auroc': 0.941}, 'within_instance': {'esj_rho': -0.008, 'lp_rho': 0.28}, 'selection_f1': {'esj': 0.846, 'lp': 0.899}}\n  fewnerd: {'n_instances': 37648, 'n_entities': 169790, 'p_yes_mean': 0.652, 'construction_f1': {'greedy': 0.7717, 'best_mv': 0.764, 'best_esj': 0.6817, 'oracle': 0.8729}, 'entity_signal': {'esj_rho': -0.008, 'esj_auroc': 0.495, 'agree_rho': 0.673, 'agree_auroc': 0.881}, 'within_instance': {'esj_rho': 0.332, 'lp_rho': 0.543}, 'selection_f1': {'esj': 0.686, 'lp': 0.781}}\n\n=== exp_fewnerd_mf4_s456 (DONE) ===\n  greedy_f1: 0.7909\n  oracle_f1: 0.881\n  mv_strict_f1: 0.7685\n  mv_delta_pp: -2.24\n  lp_f1: 0.7921\n  lp_delta_pp: 0.12\n  degeneracy_rate: 0.081\n  oracle_headroom_pp: 9.01\n  fleiss_kappa_mean: 0.3555\n  soft_jaccard_mean: 0.6845\n  rho_sj_full: 0.3122\n  rho_sj_cond: 0.2559\n  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)\n\n=== exp_fewnerd_mf4_s123_v2 (DONE) ===\n  greedy_f1: 0.7909\n  oracle_f1: 0.8892\n  mv_strict_f1: 0.7648\n  mv_delta_pp: -2.61\n  lp_f1: 0.7918\n  lp_delta_pp: 0.09\n  degeneracy_rate: 0.093\n  oracle_headroom_pp: 9.83\n  fleiss_kappa_mean: 0.3503\n  soft_jaccard_mean: 0.6701\n  rho_sj_full: 0.308\n  rho_sj_cond: 0.201\n  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)\n\n=== exp_fewnerd_pretrained_n32_s42 (DONE) ===\n  kill_reason: UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.\n  progress_at_kill: 70% (838K/1.2M prompts, ~11h elapsed)\n  fix_status: sampling.py errors='replace' already deployed on autodl-5090-c\n\n=== exp_fewnerd_pretrained_n16_s42 (DONE) ===\n  crash_reason: UnicodeEncodeError in sampling.py:675 — vLLM lone Unicode surrogates in output, UTF-8 encoding rejects\n  progress: 72% (27110/37648)\n  fix_applied: sampling.py line 673: errors='replace' added to file write\n\n=== exp_conll_freeform_n8_s42 (DONE) ===\n  greedy_f1: 0.9046\n  mv_strict_f1: 0.8994\n  mv_delta_pp: -0.52\n  lp_f1: 0.8951\n  lp_delta_pp: -0.95\n  degeneracy_rate: 0.6\n  lp_std_ratio: 0.023466\n  n_instances: 2756\n  vs_constrained: {'greedy_f1_delta': -0.0042, 'mv_delta_change': '+0.43pp (less hurt)', 'degen_delta': '+3.0pp (higher in freeform)', 'lp_std_ratio_delta': -0.0022}\n\n=== exp_fewnerd_freeform_n8_s42 (DONE) ===\n  greedy_f1: 0.7913\n  mv_strict_f1: 0.7586\n  mv_delta_pp: -3.26\n  lp_f1: 0.7922\n  lp_delta_pp: 0.09\n  degeneracy_rate: 0.091\n  n_instances: 32565\n  vs_constrained: {'greedy_f1_delta': '+0.00pp', 'mv_delta_change': '+0.01pp (identical)', 'lp_delta_change': '+0.02pp (identical)', 'degen_delta': '0.0pp (identical)'}\n  note: Freeform ≈ constrained on FewNERD. All deltas <0.02pp. Degeneracy 9.1% both. Fine-grained entity types constrain output space enough that grammar constraints have no additional effect.\n\n=== exp_fewnerd_5epoch_lp_s42 (DONE) ===\n  greedy_f1: 0.7942\n  oracle_headroom_pp: 8.06\n  fleiss_kappa: 0.529\n  lp_auroc: 0.662\n  lp_rho: 0.302\n  lp_delta_pp_cpu_recompute: 0.12\n  lp_delta_pp_cpu_recompute_std: 0.04\n  note: GPU inference completed after kill; CPU recompute from existing samples gave LP Δ=+0.12±0.04pp (2-seed)\n\n=== exp_fewnerd_mf4_s42 (DONE) ===\n  greedy_f1: 0.7911\n  oracle_f1: 0.8787\n  mv_strict_f1: 0.7585\n  mv_delta_pp: -3.27\n  lp_f1: 0.7918\n  lp_delta_pp: 0.07\n  degeneracy_rate: 0.091\n  oracle_headroom_pp: 8.76\n  fleiss_kappa_mean: 0.3537\n  soft_jaccard_mean: 0.6751\n  rho_sj_full: 0.1648\n  rho_sj_cond: 0.1989\n  note: MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)\n\n=== exp_fewnerd_n32_s42 (DONE) ===\n  greedy_f1: 0.7914\n  mv_strict_f1: 0.7818\n  mv_delta_strict_pp: -0.96",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
I now have very rich data. Let me continue to extract more experiments with metrics and also check some specific numbers. Let me read more of the registry output.

Key findings so far from the registry:

1. **exp_fewnerd_pretrained_n32_s42_v2**: mv_delta_pp = 3.85, degeneracy_rate = 5.42 → Paper says +3.85pp, D=5.4%. ✓

2. **SciERC EM AUROC**: From provenance c002, exp_012_rerun_1024 ner.em_auroc = 0.749. 

There's a discrepancy I'm noticing — the provenance notes indicate the corrected EM AUROC should be 0.684 from exp_012_rerun_1024, but the registry still shows 0.749 for that same experiment, while the current paper table displays 0.631. These numbers don't align with what the provenance documentation claims was the correction. I'm noticing the provenance file is outdated — it references the old 0.749 value for SciERC EM AUROC, but the actual paper table consistently shows 0.631. The provenance was last generated in May 2026, so it hasn't been updated to reflect the current paper values. The paper itself is internally consistent with 0.631 throughout, and 0.749 doesn't appear anywhere in the actual text. The paper table shows .631, which is the correct value—the .749 figure was a known issue that got flagged in the task. The provenance notes are just stale from an intermediate version. Now I'm checking the other experiments in the registry, particularly the Fewnerd results with different seeds and their corresponding LP selection values.

These MF4 recompute experiments show much lower LP deltas (+0.07 to +0.12) compared to the +1.39 reported in the paper, which is puzzling. The notes indicate these came from a 3-seed unified recompute on the gold-nonempty subset, but the experiment names suggest they're actually 5-epoch models. I'm trying to reconcile whether the naming conventions are consistent and whether there's a mismatch between what the experiments actually are versus what the paper reports.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "15c048d0-7c7c-407f-9848-abe740915c09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrfwdCFr9Zj3FuarVBen3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21135,
      "cache_read_input_tokens": 58900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21135
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 56_

Let me get more experiment data from the registry, and check the entity construction and selection experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "00dbc0ff-9d51-4df4-a330-ab9df55eea71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrfwdCFr9Zj3FuarVBen3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21135,
      "cache_read_input_tokens": 58900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21135
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kx98iXWNvp6GbHLdS4bJa6`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find experiments related to entity construction, selection, and fewnerd\ntargets = ['entity_construction', 'exp_021', 'selection', 'fewnerd_3ep', 'cross_model', 'spider', 'scierc_selection', 'exp_010', 'wnut', 'dals', 'verifier', 'lgb', 'alpha_crit', 'n_scaling', 'inverse', 'epoch_confound']\nfor exp_id, exp in exps.items():\n    for t in targets:\n        if t in exp_id.lower():\n            metrics = exp.get('metrics',{})\n            print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n            for k,v in list(metrics.items())[:30]:\n                print(f'  {k}: {v}')\n            hyp = exp.get('hypothesis','')[:120]\n            if hyp: print(f'  hypothesis: {hyp}')\n            print()\n            break\n\" 2>&1 | head -200",
  "description": "Extract entity_construction and related experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "555490a0-4c9c-44a3-932c-ae89e2e6a21d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrfwdCFr9Zj3FuarVBen3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21135,
      "cache_read_input_tokens": 58900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21135
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-24T04:33:27.638Z_

<details><summary>↩ Tool result · `toolu_01Kx98iXWNvp6GbHLdS4bJa6`</summary>

```text
=== exp_a1_spider_sql_sc (PREPARING) ===
  hypothesis: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies t

=== exp_b2_v4_inverse_frequency (PREPARING) ===
  variant_a_replace_fold3_lgb_auc: 0.834
  variant_a_replace_fold3_ece: 0.2188
  variant_a_f1_delta: -0.013
  variant_b_augment_fold3_lgb_auc: 0.8541
  variant_b_augment_fold3_ece: 0.1934
  variant_b_f1_delta: -0.009
  sj_ifw_std_reduction: 54% (0.138→0.063)
  ac_ifw_std_reduction: 10% (0.122→0.110)
  verdict: IFW improves stability but reduces discriminative power. Augment variant neutral. Replace variant harmful.
  hypothesis: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-d

=== exp_b2_entity_verifier (PREPARING) ===
  oof_auc: 0.9233
  oof_path_a_f1_delta: 0.003
  oof_path_b_f1_delta: -0.0157
  oof_greedy_f1: 0.8216
  oof_path_a_f1: 0.8246
  oof_majority_vote_f1: 0.8048
  leakage_pct: 91
  original_delta_pp: 3.62
  oof_delta_pp: 0.3
  per_dataset: {'scierc': '+1.28pp', 'conll': '+0.55pp', 'fewnerd': '+0.02pp'}
  verdict: B2 verifier gain was 91% leakage. OOF Path A +0.30pp not significant. NOT suitable for paper §5.
  n_inverse_scaling_validation: {'subset_n': 4351, 'full_n': 32565, 'subset_greedy_f1': 0.7926, 'full_greedy_f1': 0.7913, 'verdict': 'Not a bug. Representative subset. Paper should note subset size.'}
  hypothesis: An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candida

=== exp_spider_sc_pilot (DONE) ===
  n_instances: 196
  n_target: 200
  n_skipped: 2
  n_samples: 8
  temperature: 1
  model: gpt-5.5
  greedy_acc: 0.7653
  mv_acc: 0.7704
  oracle_acc: 0.8061
  mv_gain_pp: 0.51
  degeneracy_rate: 0.8724
  spearman_rho: 0.5501
  spearman_p: 6.77e-17
  kendall_tau: 0.5259
  F1_degeneracy_rate: 0.872
  F2_low_agreement_rate: 0
  F3_high_agree_wrong_rate: 0.082
  F4_selection_gap_rate: 0
  sc_success_rate: 0.046
  nondegen_n: 25
  nondegen_greedy_acc: 0.32
  nondegen_mv_acc: 0.36
  nondegen_oracle_acc: 0.64
  nondegen_spearman_rho: 0.13
  hypothesis: SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NE

=== exp_cross_model_consistency (DONE) ===
  scierc: {'n_filtered': 529, 'qwen_greedy_f1': 0.6453, 'llama_greedy_f1': 0.646, 'degeneracy': {'pure_qwen': 0.1323, 'pure_llama': 0.1777, 'mixed': 0.0964}, 'construction_f1': {'pure_qwen_uniform': 0.6449, 'pure_qwen_vc': 0.6413, 'pure_llama_uniform': 0.6545, 'pure_llama_vc': 0.649, 'mixed_uniform': 0.6625, 'mixed_vc': 0.6591}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 1.77, 'p': 0.0102, 'ci': [0.27, 3.28]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 1.77, 'p': 0.0093, 'ci': [0.33, 3.27]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.81, 'p': 0.1304, 'ci': [-0.59, 2.25]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 1.01, 'p': 0.0702, 'ci': [-0.32, 2.38]}}}
  fewnerd: {'n_filtered': 32565, 'qwen_greedy_f1': 0.7478, 'llama_greedy_f1': 0.7841, 'degeneracy': {'pure_qwen': 0.1004, 'pure_llama': 0.2336, 'mixed': 0.1158}, 'construction_f1': {'pure_qwen_uniform': 0.7499, 'pure_qwen_vc': 0.7448, 'pure_llama_uniform': 0.7873, 'pure_llama_vc': 0.7869, 'mixed_uniform': 0.7916, 'mixed_vc': 0.7898}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 4.17, 'p': 0, 'ci': [3.92, 4.4]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 4.5, 'p': 0, 'ci': [4.25, 4.75]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.42, 'p': 0, 'ci': [0.27, 0.58]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 0.29, 'p': 0.0001, 'ci': [0.13, 0.45]}}}
  hypothesis: Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model c

=== exp_backup3_distill_verifier (DONE) ===
  aggregate: {'LR': {'mean_auroc': 0.8747, 'std_auroc': 0.0563, 'mean_delta_f1': -0.0014}, 'RF': {'mean_auroc': 0.8752, 'std_auroc': 0.0588, 'mean_delta_f1': -0.0006}, 'MLP': {'mean_auroc': 0.8744, 'std_auroc': 0.0578, 'mean_delta_f1': 0.0011}}
  per_fold: {'scierc': {'LR': {'auroc': 0.8009, 'std_mv_f1': 0.6643, 'best_weighted_f1': 0.6659, 'delta_f1': 0.0016}, 'RF': {'auroc': 0.7988, 'best_weighted_f1': 0.6647, 'delta_f1': 0.0004}, 'MLP': {'auroc': 0.798, 'best_weighted_f1': 0.6655, 'delta_f1': 0.0012}}, 'conll': {'LR': {'auroc': 0.9376, 'std_mv_f1': 0.9074, 'best_weighted_f1': 0.9049, 'delta_f1': -0.0025}, 'RF': {'auroc': 0.9419, 'best_weighted_f1': 0.908, 'delta_f1': 0.0006}, 'MLP': {'auroc': 0.9379, 'best_weighted_f1': 0.9075, 'delta_f1': 0.0001}}, 'fewnerd': {'LR': {'auroc': 0.8855, 'std_mv_f1': 0.7819, 'best_weighted_f1': 0.7786, 'delta_f1': -0.0034}, 'RF': {'auroc': 0.885, 'best_weighted_f1': 0.7791, 'delta_f1': -0.0029}, 'MLP': {'auroc': 0.8872, 'best_weighted_f1': 0.7839, 'delta_f1': 0.002}}}
  feature_importance_LR_scierc: {'agreement_ratio': 1.651, 'lp_score': 0.424, 'span_length': -0.15, 'type_consistency': 0.128, 'degeneracy_flag': 0.043, 'n_samples': 0}
  hypothesis: A supervised entity-level binary classifier (trained on 6 lightweight features: LP score, agreement ratio, degeneracy fl

=== exp_wnut17_qwen25_7b (DONE) ===
  seed42: {'greedy_f1': 0.4524, 'construction_f1': 0.4439, 'construction_delta_pp': -0.84, 'construction_p': 0.95}
  seed123: {'greedy_f1': 0.4518, 'construction_f1': 0.4579, 'construction_delta_pp': 0.61, 'construction_p': 0.08}
  seed456: {'greedy_f1': 0.4526, 'construction_f1': 0.4583, 'construction_delta_pp': 0.57, 'construction_p': 0.12}
  oracle_headroom_pp: 6.3-9.2
  hypothesis: The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/F

=== exp_entity_construction (DONE) ===
  n16_fair_cv: {'scierc_ner': {'cv_uniform_delta': '+1.35pp', 'p_value': 0.018, 'significant': True}, 'conll_ner': {'cv_uniform_delta': '+0.10pp', 'p_value': 0.303, 'significant': False}, 'fewnerd_ner': {'cv_uniform_delta': '+1.32pp', 'p_value': 0, 'significant': True}, 'scierc_re': {'cv_uniform_delta': '+1.69pp', 'p_value': 0.049, 'significant': True}}
  n8_fair_cv: {'scierc_ner': {'uniform_confirm': '+1.54pp (p=0.023, sig)', 'lp_weighted_confirm': '+1.67pp (p=0.004, sig)', 'cv_uniform': '+1.12pp (p=0.057, borderline)'}, 'conll_ner': {'cv_uniform': '-0.39pp (p=0.963, not sig)'}, 'fewnerd_ner': {'lp_weighted_cv': '+0.88pp (p=0.000, sig)', 'uniform_cv': '+0.32pp (p=0.003, sig)'}}
  adaptive_combination: INVALIDATED - gold label leakage confirmed
  note: 5-fold CV, bootstrap B=10000, paired one-sided
  hypothesis: Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting 

=== exp_021_fewnerd_n8_seed456 (DONE) ===
  degen_rate: 0.1212
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  instance_count: 37648
  n_valid: 32565
  n_gold_empty: 5083
  ner_greedy_f1: 0.7888
  ner_oracle_f1: 0.881
  rho_fk_ner: 0.1632
  rho_sj_ner: 0.313
  sample_f1_pct_zero: 19.32
  hypothesis: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fin

=== exp_021_fewnerd_n8_seed123 (DONE) ===
  degen_rate: 0.1312
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  instance_count: 37648
  n_valid: 32565
  n_gold_empty: 5083
  ner_greedy_f1: 0.7885
  ner_oracle_f1: 0.8892
  rho_fk_ner: 0.1602
  rho_sj_ner: 0.3083
  sample_f1_pct_zero: 20.39
  hypothesis: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fin

=== exp_ccs_selection (DONE) ===
  hypothesis: Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy s

=== exp_027_mlp_verifier (DONE) ===
  lr_auroc: 0.6522
  mlp_auroc: 0.6381
  rf_auroc: 0.5868
  mlp_15feat_auroc: 0.6341
  lr_sel_f1: 0.6406
  mlp_sel_f1: 0.6278
  greedy_f1: 0.6441
  oracle_f1: 0.8231
  best_single_signal_auroc: 0.6476
  feature_bottleneck_confirmed: True
  hypothesis: MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap

=== exp_003_ner_wnut17 (DONE) ===
  ner: {'greedy_f1': 0.525, 'oracle_f1': 0.664, 'headroom': 0.139, 'rho_sj_full': 0.082, 'rho_fk_full': 0.124, 'rho_logprob_full': -0.414, 'rho_sj_cond': 0.275, 'rho_fk_cond': 0.164, 'rho_logprob_cond': 0.352, 'sj_beats_logprob_cond': False}
  n_instances: 1287
  n_gold_empty: 598
  sample_f1_mean: 0.401
  sample_f1_pct_zero: 53.7
  N: 16
  T: 1
  seed: 42
  verdict: FAIL
  verdict_note: >30% samples F1=0; structural rho weak; logprob baseline stronger
  hypothesis: WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model c

=== exp_003_wnut17_eval (DONE) ===
  greedy_f1: 0.523
  oracle_f1: 0.664
  headroom: 0.141
  rho_fk: 0.125
  rho_sj: 0.089
  rho_fk_cond: 0.169
  rho_sj_cond: 0.288
  rho_logprob_full: -0.409
  rho_logprob_cond: 0.35
  structural_beats_surface: False
  sample_f1_pct_zero: 53.7
  n_instances: 1287
  N: 16
  T: 1
  seed: 42
  model: Qwen3-8B
  n_gold_empty_filtered: 598
  verdict: FAIL
  verdict_note: structural_beats_surface=false; >50% samples F1=0
  hypothesis: WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effec

=== exp_010_selection_curves (DONE) ===
  scierc_ner: {'n_instances': 551, 'greedy_f1': 0.618, 'N16': {'oracle': 0.787, 'SJ': 0.62, 'FK': 0.621, 'logprob': 0.621, 'voting_conf': 0.585, 'EM': 0.606, 'random': 0.595}, 'N8': {'oracle': 0.752, 'SJ': 0.614, 'FK': 0.614, 'logprob': 0.619, 'voting_conf': 0.591, 'EM': 0.603, 'random': 0.589}, 'N4': {'oracle': 0.714, 'SJ': 0.607, 'FK': 0.608, 'logprob': 0.616, 'voting_conf': 0.594, 'EM': 0.6, 'random': 0.587}}
  scierc_re: {'n_instances': 397, 'greedy_f1': 0.403, 'N16': {'oracle': 0.631, 'SJ': 0.397, 'FK': 0.396, 'logprob': 0.41, 'voting_conf': 0.408, 'EM': 0.381, 'random': 0.364}, 'N8': {'oracle': 0.583, 'SJ': 0.393, 'FK': 0.394, 'logprob': 0.413, 'voting_conf': 0.398, 'EM': 0.381, 'random': 0.363}}
  conll_ner: {'n_instances': 3453, 'greedy_f1': 0.725, 'N8': {'oracle': 0.757, 'SJ': 0.718, 'FK': 0.717, 'logprob': 0.716, 'voting_conf': 0.714, 'EM': 0.716, 'random': 0.69}, 'N4': {'oracle': 0.746, 'SJ': 0.714, 'FK': 0.714, 'logprob': 0.715, 'voting_conf': 0.714, 'EM': 0.712, 'random': 0.692}}
  hypothesis: Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selec

=== exp_003_wnut17_v2 (DONE) ===
  hypothesis: WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain 

=== exp_021_fewnerd_full (DONE) ===
  total_steps: 6177
  train_loss: 0.048
  eval_loss: 0.0275
  train_runtime: 3h57m
  epochs: 3
  final_checkpoint: output/exp_021_fewnerd_full/checkpoint-6177
  adapter_path: output/exp_021_fewnerd_full/adapter_model.safetensors
  inference_instances: 37648
  inference_filtered: 32565
  inference_n_samples: 8
  greedy_macro_f1: 0.7478
  oracle_macro_f1: 0.8719
  headroom: 0.124
  zero_f1_rate: 0.119
  degeneracy_rate: 0.101
  lp_within_range_mean: 0.0879
  lp_within_range_median: 0.0662
  lp_global_rho: 0.4215
  lp_cond_rho: 0.4225
  sj_global_rho: 0.3002
  sj_cond_rho: 0.2937
  fk_global_rho: 0.3132
  fk_cond_rho: 0.3093
  em_global_rho: 0.2871
  em_cond_rho: 0.271
  vc_global_rho: 0.3858
  vc_cond_rho: 0.3234
  lp_selection_delta_pp: 1.36
  vc_selection_delta_pp: -1.79
  sj_selection_delta_pp: -2.14
  hypothesis: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "cb05b0e7-137e-47b8-a3e1-59280821c707",
  "tool_use_result": {
    "stdout": "=== exp_a1_spider_sql_sc (PREPARING) ===\n  hypothesis: Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies t\n\n=== exp_b2_v4_inverse_frequency (PREPARING) ===\n  variant_a_replace_fold3_lgb_auc: 0.834\n  variant_a_replace_fold3_ece: 0.2188\n  variant_a_f1_delta: -0.013\n  variant_b_augment_fold3_lgb_auc: 0.8541\n  variant_b_augment_fold3_ece: 0.1934\n  variant_b_f1_delta: -0.009\n  sj_ifw_std_reduction: 54% (0.138→0.063)\n  ac_ifw_std_reduction: 10% (0.122→0.110)\n  verdict: IFW improves stability but reduces discriminative power. Augment variant neutral. Replace variant harmful.\n  hypothesis: Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-d\n\n=== exp_b2_entity_verifier (PREPARING) ===\n  oof_auc: 0.9233\n  oof_path_a_f1_delta: 0.003\n  oof_path_b_f1_delta: -0.0157\n  oof_greedy_f1: 0.8216\n  oof_path_a_f1: 0.8246\n  oof_majority_vote_f1: 0.8048\n  leakage_pct: 91\n  original_delta_pp: 3.62\n  oof_delta_pp: 0.3\n  per_dataset: {'scierc': '+1.28pp', 'conll': '+0.55pp', 'fewnerd': '+0.02pp'}\n  verdict: B2 verifier gain was 91% leakage. OOF Path A +0.30pp not significant. NOT suitable for paper §5.\n  n_inverse_scaling_validation: {'subset_n': 4351, 'full_n': 32565, 'subset_greedy_f1': 0.7926, 'full_greedy_f1': 0.7913, 'verdict': 'Not a bug. Representative subset. Paper should note subset size.'}\n  hypothesis: An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candida\n\n=== exp_spider_sc_pilot (DONE) ===\n  n_instances: 196\n  n_target: 200\n  n_skipped: 2\n  n_samples: 8\n  temperature: 1\n  model: gpt-5.5\n  greedy_acc: 0.7653\n  mv_acc: 0.7704\n  oracle_acc: 0.8061\n  mv_gain_pp: 0.51\n  degeneracy_rate: 0.8724\n  spearman_rho: 0.5501\n  spearman_p: 6.77e-17\n  kendall_tau: 0.5259\n  F1_degeneracy_rate: 0.872\n  F2_low_agreement_rate: 0\n  F3_high_agree_wrong_rate: 0.082\n  F4_selection_gap_rate: 0\n  sc_success_rate: 0.046\n  nondegen_n: 25\n  nondegen_greedy_acc: 0.32\n  nondegen_mv_acc: 0.36\n  nondegen_oracle_acc: 0.64\n  nondegen_spearman_rho: 0.13\n  hypothesis: SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NE\n\n=== exp_cross_model_consistency (DONE) ===\n  scierc: {'n_filtered': 529, 'qwen_greedy_f1': 0.6453, 'llama_greedy_f1': 0.646, 'degeneracy': {'pure_qwen': 0.1323, 'pure_llama': 0.1777, 'mixed': 0.0964}, 'construction_f1': {'pure_qwen_uniform': 0.6449, 'pure_qwen_vc': 0.6413, 'pure_llama_uniform': 0.6545, 'pure_llama_vc': 0.649, 'mixed_uniform': 0.6625, 'mixed_vc': 0.6591}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 1.77, 'p': 0.0102, 'ci': [0.27, 3.28]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 1.77, 'p': 0.0093, 'ci': [0.33, 3.27]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.81, 'p': 0.1304, 'ci': [-0.59, 2.25]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 1.01, 'p': 0.0702, 'ci': [-0.32, 2.38]}}}\n  fewnerd: {'n_filtered': 32565, 'qwen_greedy_f1': 0.7478, 'llama_greedy_f1': 0.7841, 'degeneracy': {'pure_qwen': 0.1004, 'pure_llama': 0.2336, 'mixed': 0.1158}, 'construction_f1': {'pure_qwen_uniform': 0.7499, 'pure_qwen_vc': 0.7448, 'pure_llama_uniform': 0.7873, 'pure_llama_vc': 0.7869, 'mixed_uniform': 0.7916, 'mixed_vc': 0.7898}, 'bootstrap': {'mixed_uni_vs_pure_qwen_uni': {'delta_pp': 4.17, 'p': 0, 'ci': [3.92, 4.4]}, 'mixed_vc_vs_pure_qwen_vc': {'delta_pp': 4.5, 'p': 0, 'ci': [4.25, 4.75]}, 'mixed_uni_vs_pure_llama_uni': {'delta_pp': 0.42, 'p': 0, 'ci': [0.27, 0.58]}, 'mixed_vc_vs_pure_llama_vc': {'delta_pp': 0.29, 'p': 0.0001, 'ci': [0.13, 0.45]}}}\n  hypothesis: Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model c\n\n=== exp_backup3_distill_verifier (DONE) ===\n  aggregate: {'LR': {'mean_auroc': 0.8747, 'std_auroc': 0.0563, 'mean_delta_f1': -0.0014}, 'RF': {'mean_auroc': 0.8752, 'std_auroc': 0.0588, 'mean_delta_f1': -0.0006}, 'MLP': {'mean_auroc': 0.8744, 'std_auroc': 0.0578, 'mean_delta_f1': 0.0011}}\n  per_fold: {'scierc': {'LR': {'auroc': 0.8009, 'std_mv_f1': 0.6643, 'best_weighted_f1': 0.6659, 'delta_f1': 0.0016}, 'RF': {'auroc': 0.7988, 'best_weighted_f1': 0.6647, 'delta_f1': 0.0004}, 'MLP': {'auroc': 0.798, 'best_weighted_f1': 0.6655, 'delta_f1': 0.0012}}, 'conll': {'LR': {'auroc': 0.9376, 'std_mv_f1': 0.9074, 'best_weighted_f1': 0.9049, 'delta_f1': -0.0025}, 'RF': {'auroc': 0.9419, 'best_weighted_f1': 0.908, 'delta_f1': 0.0006}, 'MLP': {'auroc': 0.9379, 'best_weighted_f1': 0.9075, 'delta_f1': 0.0001}}, 'fewnerd': {'LR': {'auroc': 0.8855, 'std_mv_f1': 0.7819, 'best_weighted_f1': 0.7786, 'delta_f1': -0.0034}, 'RF': {'auroc': 0.885, 'best_weighted_f1': 0.7791, 'delta_f1': -0.0029}, 'MLP': {'auroc': 0.8872, 'best_weighted_f1': 0.7839, 'delta_f1': 0.002}}}\n  feature_importance_LR_scierc: {'agreement_ratio': 1.651, 'lp_score': 0.424, 'span_length': -0.15, 'type_consistency': 0.128, 'degeneracy_flag': 0.043, 'n_samples': 0}\n  hypothesis: A supervised entity-level binary classifier (trained on 6 lightweight features: LP score, agreement ratio, degeneracy fl\n\n=== exp_wnut17_qwen25_7b (DONE) ===\n  seed42: {'greedy_f1': 0.4524, 'construction_f1': 0.4439, 'construction_delta_pp': -0.84, 'construction_p': 0.95}\n  seed123: {'greedy_f1': 0.4518, 'construction_f1': 0.4579, 'construction_delta_pp': 0.61, 'construction_p': 0.08}\n  seed456: {'greedy_f1': 0.4526, 'construction_f1': 0.4583, 'construction_delta_pp': 0.57, 'construction_p': 0.12}\n  oracle_headroom_pp: 6.3-9.2\n  hypothesis: The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/F\n\n=== exp_entity_construction (DONE) ===\n  n16_fair_cv: {'scierc_ner': {'cv_uniform_delta': '+1.35pp', 'p_value': 0.018, 'significant': True}, 'conll_ner': {'cv_uniform_delta': '+0.10pp', 'p_value': 0.303, 'significant': False}, 'fewnerd_ner': {'cv_uniform_delta': '+1.32pp', 'p_value': 0, 'significant': True}, 'scierc_re': {'cv_uniform_delta': '+1.69pp', 'p_value': 0.049, 'significant': True}}\n  n8_fair_cv: {'scierc_ner': {'uniform_confirm': '+1.54pp (p=0.023, sig)', 'lp_weighted_confirm': '+1.67pp (p=0.004, sig)', 'cv_uniform': '+1.12pp (p=0.057, borderline)'}, 'conll_ner': {'cv_uniform': '-0.39pp (p=0.963, not sig)'}, 'fewnerd_ner': {'lp_weighted_cv': '+0.88pp (p=0.000, sig)', 'uniform_cv': '+0.32pp (p=0.003, sig)'}}\n  adaptive_combination: INVALIDATED - gold label leakage confirmed\n  note: 5-fold CV, bootstrap B=10000, paired one-sided\n  hypothesis: Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting \n\n=== exp_021_fewnerd_n8_seed456 (DONE) ===\n  degen_rate: 0.1212\n  degen_rate_source: unified_metrics_constant_f1_gold_filtered\n  instance_count: 37648\n  n_valid: 32565\n  n_gold_empty: 5083\n  ner_greedy_f1: 0.7888\n  ner_oracle_f1: 0.881\n  rho_fk_ner: 0.1632\n  rho_sj_ner: 0.313\n  sample_f1_pct_zero: 19.32\n  hypothesis: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fin\n\n=== exp_021_fewnerd_n8_seed123 (DONE) ===\n  degen_rate: 0.1312\n  degen_rate_source: unified_metrics_constant_f1_gold_filtered\n  instance_count: 37648\n  n_valid: 32565\n  n_gold_empty: 5083\n  ner_greedy_f1: 0.7885\n  ner_oracle_f1: 0.8892\n  rho_fk_ner: 0.1602\n  rho_sj_ner: 0.3083\n  sample_f1_pct_zero: 20.39\n  hypothesis: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fin\n\n=== exp_ccs_selection (DONE) ===\n  hypothesis: Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy s\n\n=== exp_027_mlp_verifier (DONE) ===\n  lr_auroc: 0.6522\n  mlp_auroc: 0.6381\n  rf_auroc: 0.5868\n  mlp_15feat_auroc: 0.6341\n  lr_sel_f1: 0.6406\n  mlp_sel_f1: 0.6278\n  greedy_f1: 0.6441\n  oracle_f1: 0.8231\n  best_single_signal_auroc: 0.6476\n  feature_bottleneck_confirmed: True\n  hypothesis: MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap\n\n=== exp_003_ner_wnut17 (DONE) ===\n  ner: {'greedy_f1': 0.525, 'oracle_f1': 0.664, 'headroom': 0.139, 'rho_sj_full': 0.082, 'rho_fk_full': 0.124, 'rho_logprob_full': -0.414, 'rho_sj_cond': 0.275, 'rho_fk_cond': 0.164, 'rho_logprob_cond': 0.352, 'sj_beats_logprob_cond': False}\n  n_instances: 1287\n  n_gold_empty: 598\n  sample_f1_mean: 0.401\n  sample_f1_pct_zero: 53.7\n  N: 16\n  T: 1\n  seed: 42\n  verdict: FAIL\n  verdict_note: >30% samples F1=0; structural rho weak; logprob baseline stronger\n  hypothesis: WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model c\n\n=== exp_003_wnut17_eval (DONE) ===\n  greedy_f1: 0.523\n  oracle_f1: 0.664\n  headroom: 0.141\n  rho_fk: 0.125\n  rho_sj: 0.089\n  rho_fk_cond: 0.169\n  rho_sj_cond: 0.288\n  rho_logprob_full: -0.409\n  rho_logprob_cond: 0.35\n  structural_beats_surface: False\n  sample_f1_pct_zero: 53.7\n  n_instances: 1287\n  N: 16\n  T: 1\n  seed: 42\n  model: Qwen3-8B\n  n_gold_empty_filtered: 598\n  verdict: FAIL\n  verdict_note: structural_beats_surface=false; >50% samples F1=0\n  hypothesis: WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effec\n\n=== exp_010_selection_curves (DONE) ===\n  scierc_ner: {'n_instances': 551, 'greedy_f1': 0.618, 'N16': {'oracle': 0.787, 'SJ': 0.62, 'FK': 0.621, 'logprob': 0.621, 'voting_conf': 0.585, 'EM': 0.606, 'random': 0.595}, 'N8': {'oracle': 0.752, 'SJ': 0.614, 'FK': 0.614, 'logprob': 0.619, 'voting_conf': 0.591, 'EM': 0.603, 'random': 0.589}, 'N4': {'oracle': 0.714, 'SJ': 0.607, 'FK': 0.608, 'logprob': 0.616, 'voting_conf': 0.594, 'EM': 0.6, 'random': 0.587}}\n  scierc_re: {'n_instances': 397, 'greedy_f1': 0.403, 'N16': {'oracle': 0.631, 'SJ': 0.397, 'FK': 0.396, 'logprob': 0.41, 'voting_conf': 0.408, 'EM': 0.381, 'random': 0.364}, 'N8': {'oracle': 0.583, 'SJ': 0.393, 'FK': 0.394, 'logprob': 0.413, 'voting_conf': 0.398, 'EM': 0.381, 'random': 0.363}}\n  conll_ner: {'n_instances': 3453, 'greedy_f1': 0.725, 'N8': {'oracle': 0.757, 'SJ': 0.718, 'FK': 0.717, 'logprob': 0.716, 'voting_conf': 0.714, 'EM': 0.716, 'random': 0.69}, 'N4': {'oracle': 0.746, 'SJ': 0.714, 'FK': 0.714, 'logprob': 0.715, 'voting_conf': 0.714, 'EM': 0.712, 'random': 0.692}}\n  hypothesis: Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selec\n\n=== exp_003_wnut17_v2 (DONE) ===\n  hypothesis: WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain \n\n=== exp_021_fewnerd_full (DONE) ===\n  total_steps: 6177\n  train_loss: 0.048\n  eval_loss: 0.0275\n  train_runtime: 3h57m\n  epochs: 3\n  final_checkpoint: output/exp_021_fewnerd_full/checkpoint-6177\n  adapter_path: output/exp_021_fewnerd_full/adapter_model.safetensors\n  inference_instances: 37648\n  inference_filtered: 32565\n  inference_n_samples: 8\n  greedy_macro_f1: 0.7478\n  oracle_macro_f1: 0.8719\n  headroom: 0.124\n  zero_f1_rate: 0.119\n  degeneracy_rate: 0.101\n  lp_within_range_mean: 0.0879\n  lp_within_range_median: 0.0662\n  lp_global_rho: 0.4215\n  lp_cond_rho: 0.4225\n  sj_global_rho: 0.3002\n  sj_cond_rho: 0.2937\n  fk_global_rho: 0.3132\n  fk_cond_rho: 0.3093\n  em_global_rho: 0.2871\n  em_cond_rho: 0.271\n  vc_global_rho: 0.3858\n  vc_cond_rho: 0.3234\n  lp_selection_delta_pp: 1.36\n  vc_selection_delta_pp: -1.79\n  sj_selection_delta_pp: -2.14\n  hypothesis: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_017uV5RXkyPm1jphyjNUqFTp`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find exp_021 and fewnerd LP selection source\nfor exp_id, exp in exps.items():\n    if 'exp_021' in exp_id or ('fewnerd' in exp_id.lower() and 'full' in exp_id.lower()):\n        metrics = exp.get('metrics',{})\n        print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n        for k,v in list(metrics.items())[:30]:\n            print(f'  {k}: {v}')\n        hyp = exp.get('hypothesis','')[:200]\n        if hyp: print(f'  hypothesis: {hyp}')\n        note = exp.get('note','')[:200]\n        if note: print(f'  note: {note}')\n        print()\n\" 2>&1",
  "description": "Find exp_021 fewnerd full experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "68a0d2d1-9fdf-47d4-8a1a-562f8e6e86e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrfwdCFr9Zj3FuarVBen3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21135,
      "cache_read_input_tokens": 58900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21135
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-24T04:33:30.995Z_

<details><summary>↩ Tool result · `toolu_017uV5RXkyPm1jphyjNUqFTp`</summary>

```text
=== exp_021_fewnerd_n8_seed456 (DONE) ===
  degen_rate: 0.1212
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  instance_count: 37648
  n_valid: 32565
  n_gold_empty: 5083
  ner_greedy_f1: 0.7888
  ner_oracle_f1: 0.881
  rho_fk_ner: 0.1632
  rho_sj_ner: 0.313
  sample_f1_pct_zero: 19.32
  hypothesis: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.

=== exp_021_fewnerd_n8_seed123 (DONE) ===
  degen_rate: 0.1312
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  instance_count: 37648
  n_valid: 32565
  n_gold_empty: 5083
  ner_greedy_f1: 0.7885
  ner_oracle_f1: 0.8892
  rho_fk_ner: 0.1602
  rho_sj_ner: 0.3083
  sample_f1_pct_zero: 20.39
  hypothesis: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.

=== exp_021_fewnerd_full (DONE) ===
  total_steps: 6177
  train_loss: 0.048
  eval_loss: 0.0275
  train_runtime: 3h57m
  epochs: 3
  final_checkpoint: output/exp_021_fewnerd_full/checkpoint-6177
  adapter_path: output/exp_021_fewnerd_full/adapter_model.safetensors
  inference_instances: 37648
  inference_filtered: 32565
  inference_n_samples: 8
  greedy_macro_f1: 0.7478
  oracle_macro_f1: 0.8719
  headroom: 0.124
  zero_f1_rate: 0.119
  degeneracy_rate: 0.101
  lp_within_range_mean: 0.0879
  lp_within_range_median: 0.0662
  lp_global_rho: 0.4215
  lp_cond_rho: 0.4225
  sj_global_rho: 0.3002
  sj_cond_rho: 0.2937
  fk_global_rho: 0.3132
  fk_cond_rho: 0.3093
  em_global_rho: 0.2871
  em_cond_rho: 0.271
  vc_global_rho: 0.3858
  vc_cond_rho: 0.3234
  lp_selection_delta_pp: 1.36
  vc_selection_delta_pp: -1.79
  sj_selection_delta_pp: -2.14
  hypothesis: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect lo
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "9e96b867-ddd6-4187-99c4-567c8e21d37a",
  "tool_use_result": {
    "stdout": "=== exp_021_fewnerd_n8_seed456 (DONE) ===\n  degen_rate: 0.1212\n  degen_rate_source: unified_metrics_constant_f1_gold_filtered\n  instance_count: 37648\n  n_valid: 32565\n  n_gold_empty: 5083\n  ner_greedy_f1: 0.7888\n  ner_oracle_f1: 0.881\n  rho_fk_ner: 0.1632\n  rho_sj_ner: 0.313\n  sample_f1_pct_zero: 19.32\n  hypothesis: Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\n\n=== exp_021_fewnerd_n8_seed123 (DONE) ===\n  degen_rate: 0.1312\n  degen_rate_source: unified_metrics_constant_f1_gold_filtered\n  instance_count: 37648\n  n_valid: 32565\n  n_gold_empty: 5083\n  ner_greedy_f1: 0.7885\n  ner_oracle_f1: 0.8892\n  rho_fk_ner: 0.1602\n  rho_sj_ner: 0.3083\n  sample_f1_pct_zero: 20.39\n  hypothesis: Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\n\n=== exp_021_fewnerd_full (DONE) ===\n  total_steps: 6177\n  train_loss: 0.048\n  eval_loss: 0.0275\n  train_runtime: 3h57m\n  epochs: 3\n  final_checkpoint: output/exp_021_fewnerd_full/checkpoint-6177\n  adapter_path: output/exp_021_fewnerd_full/adapter_model.safetensors\n  inference_instances: 37648\n  inference_filtered: 32565\n  inference_n_samples: 8\n  greedy_macro_f1: 0.7478\n  oracle_macro_f1: 0.8719\n  headroom: 0.124\n  zero_f1_rate: 0.119\n  degeneracy_rate: 0.101\n  lp_within_range_mean: 0.0879\n  lp_within_range_median: 0.0662\n  lp_global_rho: 0.4215\n  lp_cond_rho: 0.4225\n  sj_global_rho: 0.3002\n  sj_cond_rho: 0.2937\n  fk_global_rho: 0.3132\n  fk_cond_rho: 0.3093\n  em_global_rho: 0.2871\n  em_cond_rho: 0.271\n  vc_global_rho: 0.3858\n  vc_cond_rho: 0.3234\n  lp_selection_delta_pp: 1.36\n  vc_selection_delta_pp: -1.79\n  sj_selection_delta_pp: -2.14\n  hypothesis: Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect lo",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Now I have rich data. Let me do a thorough check of key numbers.

### exp_021_fewnerd_full (seed=42, 3-epoch, N=8):
- greedy_macro_f1 = 0.7478 → Paper Table fewnerd: Greedy = .748 ✓ (rounds from 0.7478)
- degeneracy_rate = 0.101 → Paper: 13.0%. Wait, 10.1% ≠ 13.0%!
  
I'm noticing a mismatch here. The seed=42 run gives 10.1% degeneracy, but the paper reports 13.0%. Let me check what the other seeds are showing — seed 123 gives 13.12%, seed 456 gives 12.12%, and there are a couple other configurations with different values around 9-10%. I'm calculating the mean across the three seeds and getting 11.78%, but the table shows 13.0% for Few-NERD — there's a discrepancy I need to resolve.

Looking at the degeneracy rate definitions, I notice the footnote distinguishes between entity-set exact-match (9–26%) and constant-F1 (13–31%), and I'm trying to figure out which metric each seed is using since seed 42 shows 0.101 while the others reference unified_metrics_constant_f1_gold_filtered. I'm realizing the degeneracy_rate of 10.1% in exp_021_fewnerd_full might be measuring entity-set exact-match rather than constant-F1, while the later experiments with seeds 123 and 456 use the unified constant-F1 metric (13.12% and 12.12% respectively). For seed42, I need to check if there's a separate constant-F1 computation or if the mf4 series with its 9.1% degeneracy rate from the unified recompute on the gold-nonempty subset is what I should be using instead.

The paper reports 13.0% for Few-NERD, which could be seed123 rounded down, but there's a traceability problem: if the table header claims "3-seed means" for the degeneracy column, the three seeds don't average to 13.0%, and if it's from a single seed, that contradicts the header. Let me look more carefully at what the caption actually specifies about which columns are 3-seed means versus single-seed values. I'm noticing the paper reports +1.39pp for LP selection improvement, but the seed42 experiment shows 1.36pp—a small but real discrepancy. I can't find LP selection deltas for the other seeds in the registry to check if this might be a 3-seed average, so I'll flag this as another traceability issue that needs clarification.

Now looking at the SciERC oracle and greedy scores, there's a slight mismatch between the provenance data and the table values: the registry shows oracle at 0.776 and greedy at 0.644, while the paper's table reports 0.775 and 0.645 respectively—each off by 0.001.

The headroom calculation checks out: 0.775 minus 0.645 gives 13.0 percentage points, matching the caption's "+13.0pp" claim. The provenance shows 13.2pp, but that's likely because it's using the single-seed values rather than the 3-seed averages reported in the table.

For the LP baseline, the improvement is straightforward: 0.647 minus 0.645 equals 0.2 percentage points, which aligns with the paper's claim.

Now I'm noticing a discrepancy with the entity construction results. The registry shows +0.88pp for the 5-fold cross-validated LP-weighted approach, but the paper reports +1.40±0.51pp. These are actually two different evaluation setups—the registry is using cross-validation while the paper's numbers come from a 4-seed mean on the full dataset without cross-validation. That explains why they don't match. I'm seeing the core issue now: the main result uses a 4-seed mean without CV (+1.40pp), but the epoch comparison pulls from a CV-based metric (+0.88pp), so they're measuring different things and shouldn't be directly compared. I need to check the registry entries more carefully to figure out which metrics are actually being used where.

Looking at the SciERC results, there's a major discrepancy—the paper reports +0.32pp (not significant), but the registry shows multiple CV variants ranging from +1.12pp to +1.67pp, all significant or borderline. I need to trace which specific experimental configuration the paper is actually citing. The registry shows +1.12pp for SciERC with uniform construction, which still doesn't match the paper's +0.32pp claim. There's a real discrepancy here—either the registry experiment is outdated, the paper used a different seed or configuration, or there's an error in one of the sources. Looking at what the paper actually states, it reports LP-weighted construction gains with specific statistical details, but the SciERC result of +0.32pp (non-significant) conflicts with the registry's cross-validated results.

The CoNLL number does check out at -0.39pp, so at least that's consistent. I should flag this SciERC mismatch in the audit report as a key provenance issue and move forward with documenting the other discrepancies I've found.

Looking at the LP selection delta for Few-NERD, the registry shows 1.36pp while the paper claims 1.39pp—close enough that it could be from averaging across multiple seeds, but worth noting. The Few-NERD degeneracy rate is also problematic since the primary seed shows 10.1% but I need to verify if that's using the right evaluation metric. There's also a major inconsistency with the construction improvements: the paper reports +0.88pp in one place and +1.40pp in another, seemingly using different evaluation approaches without clarifying which is which. And the SciERC construction result is the most concerning—the registry values range from +1.12 to +1.67pp, yet the paper states +0.32pp, which is a substantial gap that needs explanation.

For the greedy F1 scores, I'm seeing multiple experiments with different values depending on which checkpoint and seed were used. The Few-NERD greedy macro F1 of 0.7478 checks out, but for SciERC there's variation across experiments—0.618 in one, 0.644-0.645 in others. The table selection value of 0.645±0.001 appears to come from a 3-seed average that aligns with the exp_016 result, so that's at least internally consistent.

The cross-model comparison shows a +0.42pp improvement for Few-NERD when using mixed unified versus pure LLaMA unified, with p<0.001 and confidence interval [0.27, 0.58]—this matches the paper exactly.

For Spider SQL degeneracy, the registry shows 0.8724 which rounds to 87.24%, and the paper reports 87.2%, which corresponds to the F1_degeneracy_rate value of 0.872 rather than the raw degeneracy_rate.

The entity verifier achieves an AUC of 0.9233 (reported as 0.923±0.002 in the paper) and shows a +0.30pp improvement, both matching the published results.

WNUT-17 has 53.7% zero F1 samples, which checks out.

For the RE task, there's a discrepancy—the registry shows 44.3% zero-F1 from one configuration, but the paper uses 40% from the primary config instead.  This is only partially traced since no registry experiment directly confirms that 40% figure.

Now I'm noticing an inconsistency with SciERC Greedy scores across different tables. Table fewnerd reports .663, but Table selection shows .645, and the bootstrap experiment gives .644. These appear to be from different table sources, so I need to figure out which one is actually correct.

Looking closer at the metrics themselves — Table selection uses macro F1 while Table fewnerd specifies instance-averaged F1, so these might not even be measuring the same thing.

But wait, instance-averaged F1 is just the mean of per-instance F1 scores, which is the same as macro F1, so they should align. The real issue is the seed counts: Table selection reports 2-seed means for selection signals but 3-seed for baselines, while Table fewnerd uses 3-seed means across the board. So both greedy results should be based on 3 seeds, yet I'm seeing .645 versus .663 — nearly a 2-point gap.

Let me trace through the actual experiment registry to see what's happening with the individual seed runs. Looking at the SciERC results across different tables, I'm noticing the greedy F1 values diverge depending on which experiments they come from—Tab selection shows 0.645 while Tab fewnerd shows 0.663 for the same dataset. The discrepancy likely stems from different model checkpoints or seed variations between the two experiment series, so I need to trace back which specific runs contributed to each table's SciERC numbers. I'm noticing the caption for the fewnerd table specifies it's using gold-filtered data with Qwen3-8B, while the selection table doesn't mention filtering—that could explain the 1.8 percentage point gap in greedy F1 scores. The discrepancy might also stem from different training epochs, since non-Few-NERD datasets typically use 5 epochs by default, so I need to check what the exp_scierc_n8 experiments actually used.

Looking more closely at exp_016_rerun_1024_bootstrap, the "rerun_1024" label suggests it fixed a max_tokens truncation issue, which could mean its greedy F1 of 0.644 comes from a corrected pipeline while the exp_scierc_n8 experiments might be from an earlier version. But I'm also realizing there's a potential distinction between training seeds (different LoRA checkpoints) and sampling seeds (same model, different inference randomness), which could be what's driving these differences.

Actually, greedy decoding at temperature 0 is deterministic, so sampling seeds wouldn't affect greedy F1 at all — that would only matter for different training runs. If Table selection reports 0.645 from an older training pipeline like exp_016 and Table fewnerd reports 0.663 from the newer exp_scierc_n8 experiments, that explains the discrepancy since they're fundamentally different models. This is a real inconsistency in the paper: two tables reporting different SciERC greedy F1 scores without clarifying which training runs they're from.

Now looking at the oracle values and headroom calculations, Table selection shows Oracle = 0.775±0.001 with a +13.0pp headroom (0.775 - 0.645), which checks out. But Table fewnerd doesn't report oracle for SciERC at all. The LP selection gains also diverge significantly: Table selection shows only +0.2pp improvement while Table fewnerd shows +0.61pp, which is a substantial difference that needs explanation.

This inconsistency suggests the two tables might be using different model checkpoints or experimental pipelines entirely. If Table selection pulls from exp_016 and Table fewnerd uses a different training setup, that would explain the divergent baseline and delta values, but it should be made explicit in the paper rather than leaving readers confused about why the same dataset configuration produces different results. The higher F1 with fewer tokens is counterintuitive — expanding max_tokens should reduce truncation artifacts and improve performance, not hurt it, unless the model is generating spurious entities in the longer outputs. I'm flagging this as a cross-table inconsistency that needs investigation, since both tables appear in the main paper but seem to come from different experimental pipelines with a notable 1.8 percentage point gap in greedy F1 scores.

Now I'm wondering if the discrepancy stems from different random seeds or averaging methods — Tab selection reports "3-seed" baselines while Tab fewnerd also mentions "3-seed means," but the SciERC greedy scores don't match, so maybe the seeds themselves differ between the two experiments.

Let me verify the remaining numbers I haven't checked yet, particularly the cross-model ensemble confidence interval and the DALS improvement figure.

For the supervised combination results, the registry shows much smaller deltas than what's reported in the paper — the mean changes are in the range of -0.14pp to +0.11pp, whereas the paper claims -0.4 to -3.1pp, so there's a significant discrepancy I need to investigate further by looking at the per-fold breakdown. Looking at the LaTeX table, the paper lists "-0.4 to -3.1pp" for supervised combination, but these numbers don't align with the per-fold results I'm finding—the -3.1pp appears to be from a different experimental setup or evaluation method that I can't trace back to the registry. I'm also unable to locate the +0.6pp scaling result for CoNLL at N=64, and while the 61.7% degeneracy figure for CoNLL appears in multiple places in the text, I can't pin it to a specific registry entry. These discrepancies need verification against the original experimental logs.

Now checking the WNUT-17 degeneracy at 67.9%—it's listed in the table but not traceable to a specific registry experiment. For the CoNLL LP correlation coefficient of 0.302, I found a close match in the LLaMA results (0.3072 from exp_017), but the table is for Qwen, not LLaMA. The Qwen CoNLL experiment (exp_002) shows a different correlation value, so I need to locate the actual LP correlation for Qwen specifically.

Looking at the quality_estimation table, it shows CoNLL Qwen LP ρ = 0.316, which differs from the 0.302 in the fewnerd table. The discrepancy makes sense though—quality_estimation uses a single seed (N=8, seed=42) while fewnerd reports 3-seed means, so different sampling would naturally produce slightly different correlation values. Still, it's worth noting that the same metric across these tables shows this variation.

Now examining Few-NERD LP ρ more closely, the fewnerd table reports 0.220 as a 3-seed mean, but when I look at the exp_021_fewnerd_full results for seed 42, I'm seeing lp_global_rho = 0.4215—that's a huge gap between 0.42 and 0.22. This makes me wonder whether the LP ρ column in the table is measuring something different than the cross-instance ρ I'm finding in the registry. The text mentions LP ρ reaching up to 0.38 for SciERC in the experiments section, yet quality_estimation shows SciERC LP ρ = 0.205, which suggests these tables might be using different definitions or calculation methods for what they're calling "LP ρ." I'm wondering if the LP ρ values in the table might represent within-instance correlation instead, which would be the relevant metric for selection. The text mentions Few-NERD within-instance ρ around 0.5–0.7 and SciERC around 0.26, but the table shows .220 and .159 respectively—neither matches what's documented. I need to figure out what exactly these table values are measuring. So the discrepancy comes down to seed averaging—the single seed 42 result of .205 differs from the 3-seed mean of .159, which means the other two seeds must be pulling the average down significantly. Let me verify this by checking the actual metrics from those other seed runs to see if the numbers add up. There's a real inconsistency here — the LP ρ values for SciERC differ significantly across tables (0.205 vs 0.159), and the greedy F1 scores also vary (0.645 vs 0.663), which suggests these might be computed under different conditions or from different experimental runs. For Few-NERD, I only have the LP ρ value from Tab fewnerd (0.220) since the quality estimation table doesn't include that dataset, making it hard to compare directly.

Now I'm checking the precision formatting across the paper — most correlation values use three decimal places in tables, but text references tend to round more aggressively to two decimals, and the pp improvements are mostly reported to two decimal places except for one outlier at one decimal place. The percentages are consistently one decimal place, and p-values vary from two decimals to less than notation. This precision inconsistency is manageable since tables and prose naturally use different conventions, but I should flag any egregious mismatches when I write the audit. I'm checking the precision consistency across the tables and captions. The CoNLL EM AUROC value of .816 rounds to .82 in the figure, which checks out. The entity-construction gain of +1.40pp also matches. However, I can't directly verify the ρ value from Few-NERD or the +0.6pp gain at N=64 on CoNLL from the available data — those are untraced in the registry.

Now I'm noticing a discrepancy in the Holm corrections: the paper reports different p-adjusted values and family sizes across various statistical tests (global k=57 with p_adj=0.055, per-family k=10 with p_adj=0.006, seed-replication k=5 with p_adj=0.013, and selection family k=21 with p_adj=0.021), but the provenance shows LP on Few-NERD with p_adj=0.019 k=19, while the paper states p_adj=0.021 k=21 — these don't match.

If the family size expanded from 19 to 21 comparisons, the adjusted p-value would naturally increase from 0.019 to around 0.021, suggesting the provenance is outdated. The discussion and conclusion sections check out consistently with the rest of the paper, and I'm now verifying the entity-set degeneracy numbers across different metrics.

Looking at the registry data, the 5-epoch mf4 experiments show degeneracy ranging from 8.1% to 9.3%, but the footnote claims entity-set exact-match ranges from 9-26%. That 8.1% dips below the stated lower bound, which suggests either the footnote is referencing a different configuration set or there's a discrepancy I need to resolve.

I think I've gathered enough evidence to start compiling the audit report now. Let me organize the critical issues I've found, starting with the most severe factual discrepancies. The SciERC greedy F1 values differ between the selection table (.645) and the fewnerd table (.663) despite both claiming the same setup—Qwen3-8B with N=8, T=1.0, and 3-seed means for baselines—which throws off the LP Δ calculations by 0.2pp. Similarly, the SciERC LP ρ values are inconsistent across tables (.205 vs .159), and I need to determine whether this stems from different random seeds or something else.

Beyond these factual inconsistencies, there are several major issues: the provenance file still shows an outdated SciERC EM AUROC of 0.749 while the paper correctly reports .631, and there's a construction gain discrepancy where the main claim states +1.40±0.51pp but the epoch comparison shows +0.88pp—it's unclear whether these refer to different evaluation methods or if one is simply stale.

The SciERC construction gain is particularly problematic: the paper reports +0.32pp as non-significant, but the registry shows +1.12pp to +1.67pp depending on the weighting scheme, which is a substantial gap. The LP selection delta shows a similar minor discrepancy of +1.39pp in the paper versus 1.36pp in the registry for the primary seed, likely from multi-seed averaging. There's also a degeneracy rate mismatch where the paper claims 13.0% but the primary seed experiment shows 10.1%.

For the RE task, the paper cites 40% zero-F1 instances while the registry has 44.3%, and the exact source of the 40% figure isn't clear. The supervised combination results show another gap—the paper claims a range of -0.4 to -3.1pp but the registry only shows -0.34pp maximum. Finally, there's an N=64 CoNLL experiment with a reported +0.6pp MV improvement that I can't locate in the registry data at all.

Looking at the degeneracy analysis, there's an inconsistency in how metrics are being applied—line 107 mentions degeneracy rising from 9% to 26% using what appears to be entity-set exact-match scoring, but the main tables rely on constant-F1 at 13.0%, and it's never clarified which measure applies where.

On the minor issues, the LP-best improvement of +1.4pp on Few-NERD is ambiguous since it could round from either +1.39 or +1.40. The AUROC and ρ values are technically correct when rounded to two decimal places (.816→.82 and .451→.45), but the rounding is quite aggressive.

There's also a stale provenance issue where the C143 family size changed from k=21 in the paper to k=19 in the registry.

One more thing I'm noticing—the WNUT-17 LP correlation values don't align across sources. The registry shows ρ=-0.414 and -0.409 from different experiments, but the table shows -.446. The discrepancy makes sense given different sample sizes (N=16 in registry versus N=8 in the table), and the table explicitly notes these are 3-seed means while the registry values appear to be single runs, so that accounts for the variation.

But I'm realizing I can't actually trace the WNUT-17 N=8 data back to a specific registry experiment—the experiments section mentions N=8 samples at T=1.0 as primary, yet I don't have a clear source linking that to the table values.

Let me search for exp_wnut17_qwen25_7b in the registry. Found it—it has multiple seeds with greedy_f1 around 0.452, which matches Tab fewnerd's WNUT-17 Greedy value of .452. So that's where the table data is coming from.

But the degeneracy percentage of 67.9% isn't in this registry entry, so it must come from another source. That's a partial trace.

Now I should focus on writing the audit report rather than diving deeper into the appendix. Let me verify the seven key bug-prone numbers from the task: SciERC EM AUROC shows .631 in the table, which is correct, though the provenance still lists .749 as stale. For headroom, the table shows 13.0pp instead of 11.4pp.

Checking the remaining numbers: MV is consistently +0.6pp for CoNLL, never +0.61pp, while the SciERC LP selection shows +0.61pp separately. The alpha parameter appears as the upper bound 0.121 in the range. SciERC construction shows +0.32pp.

For the statistical significance values, both Holm-adjusted p-values are present and correct—0.055 for the global comparison with k=57 and 0.013 for the seed-replication framework with k=5. The oracle selection gap is confirmed as +13.0pp, not +13.1pp.

All seven critical numbers check out across the paper. Now I'm compiling the full audit report and thinking through what else might need verification, including details from the introduction.

I'm checking the SQL parsing degeneracy rate of 87.2% against the registry—that matches the F1_degeneracy_rate value of 0.872. The correlation figure of 0.47 cited from Yao et al. is their published result, not ours. But I'm uncertain about the constant-F1 degeneracy percentages in diagnostic.tex: SciERC at 12.2% and CoNLL at 61.7%—I need to trace where these come from in the fewnerd table, which shows these as 3-seed means at N=8.

Now I'm trying to verify the SciERC 12.2% figure by checking individual seed runs. The registry shows degeneracy rates around 11.6% and 12.0% for seeds 123 and 456, with higher values like 14.1% and 16.5% for other seeds. I need to figure out which three seeds were averaged to get 12.2%.

I'm also noticing a discrepancy in the SciERC LP improvement—the text mentions +0.2pp but the table shows +0.61pp, which is a significant difference I should resolve before finalizing the report. The Few-NERD and CoNLL values are consistent across single_signal.tex, experiments_main.tex, and the introduction. Now I'm cross-checking the abstract's claims about entity-level construction gains and the statistical corrections mentioned in experiments_main.tex—specifically the per-family Holm-Bonferroni adjustment that supposedly yields p_adj = 0.006. I've confirmed the consistency across all sections—the experiments section notes that the family partition wasn't pre-registered, which aligns with the abstract and introduction both describing it as post-hoc. Now I'm ready to compile the comprehensive audit report, organizing it section by section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "c68221e4-f8ef-402b-a28e-8453131cced6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCZkbFQ7mMPDqKdKLTXCbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8951,
      "cache_read_input_tokens": 80035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8951
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 62_

I have collected extensive data from the tex files, registry, and provenance. Let me now do some final targeted checks to resolve key discrepancies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "05ea6525-a152-44d6-a623-a460efc0d85d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCZkbFQ7mMPDqKdKLTXCbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8951,
      "cache_read_input_tokens": 80035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8951
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_017Vu7iaNwXR6Pvk9NuNG5AJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/be935652-fa4e-4214-8762-c7316ebe5e2f/tool-results/mcp-agent-ml-research-read_registry-1779596899827.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Find exp_016, exp_012, DALS, N scaling experiments\ntargets = ['exp_016', 'exp_012', 'dals', 'n_scaling', 'n32', 'n64', 'fewnerd_selection', 'scierc_constr', 'conll_n8', 'alpha_crit', 'frontier', 'gpt']\nfor exp_id, exp in exps.items():\n    for t in targets:\n        if t in exp_id.lower():\n            metrics = exp.get('metrics',{})\n            if metrics:\n                print(f'=== {exp_id} ({exp.get(\\\"status\\\",\\\"?\\\")}) ===')\n                for k,v in list(metrics.items())[:25]:\n                    print(f'  {k}: {v}')\n                print()\n            break\n\" 2>&1 | head -250",
  "description": "Find exp_016, DALS, N-scaling, alpha_crit experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "1b7c66bf-37f5-4779-be2f-e7d6d93ef645",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCZkbFQ7mMPDqKdKLTXCbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8951,
      "cache_read_input_tokens": 80035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8951
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-24T04:39:13.320Z_

<details><summary>↩ Tool result · `toolu_017Vu7iaNwXR6Pvk9NuNG5AJ`</summary>

```text
=== exp_fewnerd_pretrained_n32_s42_v2 (DONE) ===
  greedy_f1: 0.539
  mv_f1: 0.577
  mv_delta_pp: 3.85
  lp_f1: 0.529
  lp_delta_pp: -1.03
  oracle_f1: 0.705
  oracle_delta_pp: 16.56
  degeneracy_rate: 5.42
  capture_rate: 19
  sj_rho: 0.456
  n_instances_gold_nonempty: 32565
  subset: gold-nonempty

=== exp_fewnerd_pretrained_n32_s42 (DONE) ===
  kill_reason: UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.
  progress_at_kill: 70% (838K/1.2M prompts, ~11h elapsed)
  fix_status: sampling.py errors='replace' already deployed on autodl-5090-c

=== exp_fewnerd_n32_s42 (DONE) ===
  greedy_f1: 0.7914
  mv_strict_f1: 0.7818
  mv_delta_strict_pp: -0.96
  mv_delta_unified_pp: -0.91
  unified_greedy_f1: 0.7909
  oracle_f1: 0.9305
  degeneracy_rate: 0.014

=== exp_conll_pretrained_n64_s42 (DONE) ===
  greedy_f1: 0.6005
  mv_strict_f1: 0.6316
  mv_delta_strict_pp: 3.11
  oracle_f1: 0.7703
  degeneracy_rate: 0.143

=== exp_scierc_pretrained_n64_s42 (DONE) ===
  greedy_f1: 0.2432
  mv_strict_f1: 0.2717
  mv_delta_strict_pp: 2.85
  oracle_f1: 0.5017
  degeneracy_rate: 0
  alpha_crit_eff_strict: 0.122

=== exp_conll_n32_s456 (DONE) ===
  greedy_f1: 0.9117
  mv_strict_f1: 0.9167
  mv_delta_strict_pp: 0.51
  degeneracy_rate: 0.401
  oracle_f1: 0.9686
  alpha_crit_eff_strict: 0.7614

=== exp_scierc_n32_s456 (DONE) ===
  greedy_f1: 0.6661
  mv_strict_f1: 0.6644
  mv_delta_strict_pp: -0.17
  degeneracy_rate: 0.04

=== exp_conll_n64_s42 (DONE) ===
  greedy_f1: 0.912
  mv_strict_f1: 0.9184
  mv_delta_strict_pp: 0.64
  oracle_f1: 0.9751
  degeneracy_rate: 0.306

=== exp_conll_pretrained_n32_s42 (DONE) ===
  greedy_f1: 0.5975
  mv_strict_f1: 0.6296
  mv_delta_strict_pp: 3.21
  oracle_f1: 0.7493
  degeneracy_rate: 0.188
  alpha_crit_eff_strict: 0.5657

=== exp_conll_n32_s123 (DONE) ===
  greedy_f1: 0.9123
  mv_strict_f1: 0.9177
  mv_delta_strict_pp: 0.55
  oracle_f1: 0.9717
  degeneracy_rate: 0.379
  alpha_crit_eff_strict: 0.7347

=== exp_scierc_pretrained_n32_s42 (DONE) ===
  greedy_f1: 0.2446
  mv_strict_f1: 0.2643
  mv_delta_strict_pp: 1.97
  mv_incl_f1: 0.2668
  oracle_f1: 0.4729
  degeneracy_rate: 0.002
  alpha_crit_eff_strict: 0.1526

=== exp_scierc_n32_s123 (DONE) ===
  greedy_f1: 0.6663
  mv_strict_f1: 0.6675
  mv_delta_strict_pp: 0.12
  mv_incl_f1: 0.6722
  oracle_f1: 0.8404
  degeneracy_rate: 0.051
  alpha_crit_eff_strict: 0.3511

=== exp_scierc_n64_s42 (DONE) ===
  greedy_f1: 0.6673
  mv_strict_f1: 0.6735
  mv_delta_strict_pp: 0.63
  mv_incl_f1: 0.6725
  oracle_f1: 0.8626
  degeneracy_rate: 0.021
  alpha_crit_eff_strict: 0.3407

=== exp_conll_n32_s42 (DONE) ===
  greedy_f1: 0.912
  mv_strict_f1: 0.9166
  mv_delta_strict_pp: 0.46
  mv_incl_f1: 0.9169
  oracle_f1: 0.969
  degeneracy_rate: 0.405
  alpha_crit_strict: 0.456

=== exp_scierc_n32_s42 (DONE) ===
  greedy_f1: 0.6629
  mv_strict_f1: 0.6706
  mv_delta_strict_pp: 0.78
  mv_incl_f1: 0.6708
  oracle_f1: 0.8399
  degeneracy_rate: 0.036
  alpha_crit_eff_strict: 0.3438
  note: Strict MV turns positive at N=32. Gold-nonempty filtered.

=== exp_frontier_sc_gemini25pro (DONE) ===
  greedy_f1: 0.6301
  mv_f1: 0.6446
  oracle_f1: 0.7575
  mv_gain_pp: 1.45
  selection_gap_pp: 11.29
  mv_captures_pct: 11.4
  agreement_rho: 0.3887
  degeneracy_rate: 0.285
  fleiss_kappa: 0.5185
  soft_jaccard: 0.8023
  alpha_crit: 0.4756
  alpha_crit_eff: 0.6651
  parse_failure_rate: 0.119
  n_instances: 200
  mv_wins: 33
  mv_ties: 144
  mv_loses: 23
  verdict: MV helps (+1.45pp), captures 11% of oracle headroom

=== exp_frontier_sc_deepseek (DONE) ===
  greedy_f1: 0.3992
  mv_f1: 0.4243
  oracle_f1: 0.714
  degeneracy_rate: 0.055
  agreement_rho: 0.2051
  fleiss_kappa_rho: 0.1471
  sj_rho: 0.1635
  mv_gain_over_greedy: 0.0251
  selection_gap: 0.2897
  parse_failure_count: 751
  total_api_calls: 1600
  elapsed_s: 4043.7

=== exp_frontier_sc_claude_sonnet4 (DONE) ===
  greedy_f1: 0.6068
  mv_f1: 0.6226
  oracle_f1: 0.6544
  degeneracy_rate: 0.74
  selection_gap: 0.0318
  parse_failures: 103
  api_calls: 1600
  wall_clock_seconds: 6118
  instances: 200

=== exp_frontier_sc_gpt55_fewnerd_v2 (DONE) ===
  greedy_f1: 0.6382
  mv_f1: 0.6521
  oracle_f1: 0.7203
  degeneracy_rate: 0.5
  rho_agreement: 0.3551
  rho_fk: 0.3515
  rho_sj: 0.3461
  instances: 200

=== exp_012_rerun_1024 (DONE) ===
  degen_rate: 0.1777
  degen_rate_source: unified_metrics_constant_f1_gold_filtered
  ner_full: {'n': 529, 'SJ': {'rho': 0.3599, 'tau': 0.2646, 'AUROC': 0.6917, 'ECE': 0.4531, 'rho_ci95': [0.2732, 0.4389], 'AUROC_ci95': [0.6304, 0.7406]}, 'FK': {'rho': 0.2665, 'tau': 0.1974, 'AUROC': 0.629, 'ECE': 0.4512, 'rho_ci95': [0.1743, 0.3486], 'AUROC_ci95': [0.5612, 0.6882]}, 'logprob': {'rho': 0.2052, 'tau': 0.1478, 'AUROC': 0.5783, 'ECE': 0.7064, 'rho_ci95': [0.1171, 0.2904], 'AUROC_ci95': [0.5179, 0.6387]}, 'EM': {'rho': 0.2945, 'tau': 0.2208, 'AUROC': 0.7493, 'ECE': 0.3526, 'rho_ci95': [0.2094, 0.37], 'AUROC_ci95': [0.7002, 0.7928]}, 'voting_conf': {'rho': 0.3792, 'tau': 0.2805, 'AUROC': 0.6841, 'ECE': 0.3807, 'rho_ci95': [0.2972, 0.4486], 'AUROC_ci95': [0.6249, 0.7366]}}
  ner_cond: {'n': 477, 'SJ': {'rho': 0.3113, 'tau': 0.2257, 'AUROC': 0.6772, 'ECE': 0.4416, 'rho_ci95': [0.2353, 0.3959], 'AUROC_ci95': [0.621, 0.7337]}, 'FK': {'rho': 0.1761, 'tau': 0.1284, 'AUROC': 0.6078, 'ECE': 0.4389, 'rho_ci95': [0.0839, 0.2665], 'AUROC_ci95': [0.5442, 0.6709]}, 'logprob': {'rho': 0.1538, 'tau': 0.1111, 'AUROC': 0.5633, 'ECE': 0.6803, 'rho_ci95': [0.0637, 0.2424], 'AUROC_ci95': [0.5032, 0.6232]}, 'EM': {'rho': 0.3596, 'tau': 0.2735, 'AUROC': 0.7556, 'ECE': 0.3257, 'rho_ci95': [0.2819, 0.4408], 'AUROC_ci95': [0.7011, 0.8107]}, 'voting_conf': {'rho': 0.3, 'tau': 0.2189, 'AUROC': 0.6618, 'ECE': 0.3746, 'rho_ci95': [0.2168, 0.3836], 'AUROC_ci95': [0.6004, 0.7201]}}
  re_full: {'n': 397, 'SJ': {'rho': 0.2503, 'tau': 0.1878, 'AUROC': 0.6702, 'ECE': 0.3865}, 'FK': {'rho': 0.2752, 'tau': 0.2117, 'AUROC': 0.6089, 'ECE': 0.4405}, 'logprob': {'rho': 0.2662, 'tau': 0.1951, 'AUROC': 0.6005, 'ECE': 0.7694}, 'EM': {'rho': 0.1344, 'tau': 0.1081, 'AUROC': 0.7059, 'ECE': 0.3548}, 'voting_conf': {'rho': 0.3498, 'tau': 0.2663, 'AUROC': 0.6935, 'ECE': 0.2724}}
  re_cond: {'n': 238, 'SJ': {'rho': 0.2457, 'tau': 0.1811, 'AUROC': 0.6463, 'ECE': 0.2941}, 'FK': {'rho': 0.1139, 'tau': 0.0876, 'AUROC': 0.551, 'ECE': 0.3424}, 'logprob': {'rho': 0.0112, 'tau': 0.0051, 'AUROC': 0.5186, 'ECE': 0.6464}, 'EM': {'rho': 0.4165, 'tau': 0.3256, 'AUROC': 0.7515, 'ECE': 0.2232}, 'voting_conf': {'rho': 0.2409, 'tau': 0.178, 'AUROC': 0.642, 'ECE': 0.207}}
  delta_vs_512_ner_full_rho: {'SJ': 0.0034, 'FK': 0.0014, 'EM': 0.0379, 'voting_conf': -0.1226, 'logprob': 0.0656}
  provenance_note: exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.

=== exp_016_rerun_1024_bootstrap (DONE) ===
  bootstrap_ci_95: [-0.03, 0.042]
  permutation_p: 0.39
  cohen_d: 0.038
  sign_test_win_rate: 0.466
  ner_logprob_vs_greedy_delta: 0.006
  conclusion_summary: NER selection: no signal significantly outperforms greedy; RE: same conclusion

=== exp_016_v2 (DONE) ===
  ner_conditional: {'n': 529, 'best_single_signal_rho': {'soft_jaccard': 0.4412}, 'best_combo_rho': {'sj+vc_a0.55': 0.4552}, 'ensemble_auroc': 0.7141, 'best_single_auroc': {'soft_jaccard': 0.7166}, 'selection_f1': {'greedy': 0.6442, 'logprob_best': 0.6505, 'ensemble_best': 0.6475, 'sj_best': 0.6471, 'oracle': 0.8442}}
  re_conditional: {'n': 397, 'best_single_signal_rho': {'voting_confidence': 0.3849}, 'best_combo_rho': {'logprob+vc_a0.25': 0.3936}, 'ensemble_auroc': 0.6916, 'best_single_auroc': {'voting_confidence': 0.7023}, 'selection_f1': {'greedy': 0.403, 'logprob_best': 0.4097, 'ensemble_best': 0.4227, 'oracle': 0.6306}}
  re_full: {'ensemble_auroc': 0.8608, 'best_single_auroc': {'voting_confidence': 0.8248}}

=== exp_025_n32 (DONE) ===
  n_samples: 32
  degeneracy_pct: 4
  lp_range: 0.0781
  oracle_f1: 0.8412
  greedy_f1: 0.6615
  oracle_gap: 0.1797
  selection_f1_lp_delta: 0.54
  selection_f1_sj_delta: 0.16
  selection_f1_fk_delta: 0.6
  selection_f1_em_delta: 0.68
  selection_f1_vc_delta: -5.21
  best_signal: EM
  best_delta: 0.68
  metric_space: micro_f1_filtered_529inst
  note: corrected via n_ablation_fixed.py, greedy from inst['greedy'] field

=== exp_017_llama_conll_n8_t07 (DONE) ===
  n_valid: 2756
  greedy_f1: 0.9242
  oracle_f1: 0.9391
  lp_range_median: 1.1e-05
  lp_tied_fraction_005: 0.9579
  signals: {'SJ': {'rho': 0.3934, 'auroc': 0.6506}, 'FK': {'rho': 0.3879, 'auroc': 0.6488}, 'VC': {'rho': 0.375, 'auroc': 0.6551}, 'EM': {'rho': 0.3888, 'auroc': 0.6494}, 'LP': {'rho': 0.2951, 'auroc': 0.7509}}
  selection_f1: {'SJ': 0.9247, 'FK': 0.9254, 'VC': 0.9264, 'EM': 0.9255, 'LP': 0.9248}

=== exp_016_signal_ensemble (DONE) ===
  sj_logprob_pearson_ner: 0.57
  sj_logprob_pearson_re: 0.42
  best_linear_ner: {'combo': 'SJ+voting_conf', 'alpha': 0.3, 'rho': 0.489}
  best_linear_re: {'combo': 'voting_conf+logprob', 'alpha': 0.6, 'rho': 0.429}
  ensemble_ner_auroc: 0.735
  ensemble_re_auroc: 0.719
  best_single_ner_auroc: 0.7
  best_single_re_auroc: 0.721
  ensemble_ner_delta: 0.035
  selection_f1_ner: {'greedy': 0.609, 'logprob': 0.609, 'sj': 0.604, 'ensemble': 0.604, 'voting': 0.596, 'random': 0.58, 'oracle': 0.769}
  selection_f1_re: {'logprob': 0.397, 'greedy': 0.374, 'sj': 0.368, 'ensemble': 0.367, 'voting': 0.338, 'random': 0.338, 'oracle': 0.561}
  diagnosis: SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.

=== exp_012_logprob_baseline (DONE) ===
  ner_full_rho_sj: 0.3565
  ner_full_rho_fk: 0.2651
  ner_full_rho_logprob: 0.1396
  ner_full_rho_greedy_logprob: 0.1615
  ner_full_tau_sj: 0.2658
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "54b7f0fe-cd24-4d81-b356-bc6ffd2d8a02",
  "tool_use_result": {
    "stdout": "=== exp_fewnerd_pretrained_n32_s42_v2 (DONE) ===\n  greedy_f1: 0.539\n  mv_f1: 0.577\n  mv_delta_pp: 3.85\n  lp_f1: 0.529\n  lp_delta_pp: -1.03\n  oracle_f1: 0.705\n  oracle_delta_pp: 16.56\n  degeneracy_rate: 5.42\n  capture_rate: 19\n  sj_rho: 0.456\n  n_instances_gold_nonempty: 32565\n  subset: gold-nonempty\n\n=== exp_fewnerd_pretrained_n32_s42 (DONE) ===\n  kill_reason: UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.\n  progress_at_kill: 70% (838K/1.2M prompts, ~11h elapsed)\n  fix_status: sampling.py errors='replace' already deployed on autodl-5090-c\n\n=== exp_fewnerd_n32_s42 (DONE) ===\n  greedy_f1: 0.7914\n  mv_strict_f1: 0.7818\n  mv_delta_strict_pp: -0.96\n  mv_delta_unified_pp: -0.91\n  unified_greedy_f1: 0.7909\n  oracle_f1: 0.9305\n  degeneracy_rate: 0.014\n\n=== exp_conll_pretrained_n64_s42 (DONE) ===\n  greedy_f1: 0.6005\n  mv_strict_f1: 0.6316\n  mv_delta_strict_pp: 3.11\n  oracle_f1: 0.7703\n  degeneracy_rate: 0.143\n\n=== exp_scierc_pretrained_n64_s42 (DONE) ===\n  greedy_f1: 0.2432\n  mv_strict_f1: 0.2717\n  mv_delta_strict_pp: 2.85\n  oracle_f1: 0.5017\n  degeneracy_rate: 0\n  alpha_crit_eff_strict: 0.122\n\n=== exp_conll_n32_s456 (DONE) ===\n  greedy_f1: 0.9117\n  mv_strict_f1: 0.9167\n  mv_delta_strict_pp: 0.51\n  degeneracy_rate: 0.401\n  oracle_f1: 0.9686\n  alpha_crit_eff_strict: 0.7614\n\n=== exp_scierc_n32_s456 (DONE) ===\n  greedy_f1: 0.6661\n  mv_strict_f1: 0.6644\n  mv_delta_strict_pp: -0.17\n  degeneracy_rate: 0.04\n\n=== exp_conll_n64_s42 (DONE) ===\n  greedy_f1: 0.912\n  mv_strict_f1: 0.9184\n  mv_delta_strict_pp: 0.64\n  oracle_f1: 0.9751\n  degeneracy_rate: 0.306\n\n=== exp_conll_pretrained_n32_s42 (DONE) ===\n  greedy_f1: 0.5975\n  mv_strict_f1: 0.6296\n  mv_delta_strict_pp: 3.21\n  oracle_f1: 0.7493\n  degeneracy_rate: 0.188\n  alpha_crit_eff_strict: 0.5657\n\n=== exp_conll_n32_s123 (DONE) ===\n  greedy_f1: 0.9123\n  mv_strict_f1: 0.9177\n  mv_delta_strict_pp: 0.55\n  oracle_f1: 0.9717\n  degeneracy_rate: 0.379\n  alpha_crit_eff_strict: 0.7347\n\n=== exp_scierc_pretrained_n32_s42 (DONE) ===\n  greedy_f1: 0.2446\n  mv_strict_f1: 0.2643\n  mv_delta_strict_pp: 1.97\n  mv_incl_f1: 0.2668\n  oracle_f1: 0.4729\n  degeneracy_rate: 0.002\n  alpha_crit_eff_strict: 0.1526\n\n=== exp_scierc_n32_s123 (DONE) ===\n  greedy_f1: 0.6663\n  mv_strict_f1: 0.6675\n  mv_delta_strict_pp: 0.12\n  mv_incl_f1: 0.6722\n  oracle_f1: 0.8404\n  degeneracy_rate: 0.051\n  alpha_crit_eff_strict: 0.3511\n\n=== exp_scierc_n64_s42 (DONE) ===\n  greedy_f1: 0.6673\n  mv_strict_f1: 0.6735\n  mv_delta_strict_pp: 0.63\n  mv_incl_f1: 0.6725\n  oracle_f1: 0.8626\n  degeneracy_rate: 0.021\n  alpha_crit_eff_strict: 0.3407\n\n=== exp_conll_n32_s42 (DONE) ===\n  greedy_f1: 0.912\n  mv_strict_f1: 0.9166\n  mv_delta_strict_pp: 0.46\n  mv_incl_f1: 0.9169\n  oracle_f1: 0.969\n  degeneracy_rate: 0.405\n  alpha_crit_strict: 0.456\n\n=== exp_scierc_n32_s42 (DONE) ===\n  greedy_f1: 0.6629\n  mv_strict_f1: 0.6706\n  mv_delta_strict_pp: 0.78\n  mv_incl_f1: 0.6708\n  oracle_f1: 0.8399\n  degeneracy_rate: 0.036\n  alpha_crit_eff_strict: 0.3438\n  note: Strict MV turns positive at N=32. Gold-nonempty filtered.\n\n=== exp_frontier_sc_gemini25pro (DONE) ===\n  greedy_f1: 0.6301\n  mv_f1: 0.6446\n  oracle_f1: 0.7575\n  mv_gain_pp: 1.45\n  selection_gap_pp: 11.29\n  mv_captures_pct: 11.4\n  agreement_rho: 0.3887\n  degeneracy_rate: 0.285\n  fleiss_kappa: 0.5185\n  soft_jaccard: 0.8023\n  alpha_crit: 0.4756\n  alpha_crit_eff: 0.6651\n  parse_failure_rate: 0.119\n  n_instances: 200\n  mv_wins: 33\n  mv_ties: 144\n  mv_loses: 23\n  verdict: MV helps (+1.45pp), captures 11% of oracle headroom\n\n=== exp_frontier_sc_deepseek (DONE) ===\n  greedy_f1: 0.3992\n  mv_f1: 0.4243\n  oracle_f1: 0.714\n  degeneracy_rate: 0.055\n  agreement_rho: 0.2051\n  fleiss_kappa_rho: 0.1471\n  sj_rho: 0.1635\n  mv_gain_over_greedy: 0.0251\n  selection_gap: 0.2897\n  parse_failure_count: 751\n  total_api_calls: 1600\n  elapsed_s: 4043.7\n\n=== exp_frontier_sc_claude_sonnet4 (DONE) ===\n  greedy_f1: 0.6068\n  mv_f1: 0.6226\n  oracle_f1: 0.6544\n  degeneracy_rate: 0.74\n  selection_gap: 0.0318\n  parse_failures: 103\n  api_calls: 1600\n  wall_clock_seconds: 6118\n  instances: 200\n\n=== exp_frontier_sc_gpt55_fewnerd_v2 (DONE) ===\n  greedy_f1: 0.6382\n  mv_f1: 0.6521\n  oracle_f1: 0.7203\n  degeneracy_rate: 0.5\n  rho_agreement: 0.3551\n  rho_fk: 0.3515\n  rho_sj: 0.3461\n  instances: 200\n\n=== exp_012_rerun_1024 (DONE) ===\n  degen_rate: 0.1777\n  degen_rate_source: unified_metrics_constant_f1_gold_filtered\n  ner_full: {'n': 529, 'SJ': {'rho': 0.3599, 'tau': 0.2646, 'AUROC': 0.6917, 'ECE': 0.4531, 'rho_ci95': [0.2732, 0.4389], 'AUROC_ci95': [0.6304, 0.7406]}, 'FK': {'rho': 0.2665, 'tau': 0.1974, 'AUROC': 0.629, 'ECE': 0.4512, 'rho_ci95': [0.1743, 0.3486], 'AUROC_ci95': [0.5612, 0.6882]}, 'logprob': {'rho': 0.2052, 'tau': 0.1478, 'AUROC': 0.5783, 'ECE': 0.7064, 'rho_ci95': [0.1171, 0.2904], 'AUROC_ci95': [0.5179, 0.6387]}, 'EM': {'rho': 0.2945, 'tau': 0.2208, 'AUROC': 0.7493, 'ECE': 0.3526, 'rho_ci95': [0.2094, 0.37], 'AUROC_ci95': [0.7002, 0.7928]}, 'voting_conf': {'rho': 0.3792, 'tau': 0.2805, 'AUROC': 0.6841, 'ECE': 0.3807, 'rho_ci95': [0.2972, 0.4486], 'AUROC_ci95': [0.6249, 0.7366]}}\n  ner_cond: {'n': 477, 'SJ': {'rho': 0.3113, 'tau': 0.2257, 'AUROC': 0.6772, 'ECE': 0.4416, 'rho_ci95': [0.2353, 0.3959], 'AUROC_ci95': [0.621, 0.7337]}, 'FK': {'rho': 0.1761, 'tau': 0.1284, 'AUROC': 0.6078, 'ECE': 0.4389, 'rho_ci95': [0.0839, 0.2665], 'AUROC_ci95': [0.5442, 0.6709]}, 'logprob': {'rho': 0.1538, 'tau': 0.1111, 'AUROC': 0.5633, 'ECE': 0.6803, 'rho_ci95': [0.0637, 0.2424], 'AUROC_ci95': [0.5032, 0.6232]}, 'EM': {'rho': 0.3596, 'tau': 0.2735, 'AUROC': 0.7556, 'ECE': 0.3257, 'rho_ci95': [0.2819, 0.4408], 'AUROC_ci95': [0.7011, 0.8107]}, 'voting_conf': {'rho': 0.3, 'tau': 0.2189, 'AUROC': 0.6618, 'ECE': 0.3746, 'rho_ci95': [0.2168, 0.3836], 'AUROC_ci95': [0.6004, 0.7201]}}\n  re_full: {'n': 397, 'SJ': {'rho': 0.2503, 'tau': 0.1878, 'AUROC': 0.6702, 'ECE': 0.3865}, 'FK': {'rho': 0.2752, 'tau': 0.2117, 'AUROC': 0.6089, 'ECE': 0.4405}, 'logprob': {'rho': 0.2662, 'tau': 0.1951, 'AUROC': 0.6005, 'ECE': 0.7694}, 'EM': {'rho': 0.1344, 'tau': 0.1081, 'AUROC': 0.7059, 'ECE': 0.3548}, 'voting_conf': {'rho': 0.3498, 'tau': 0.2663, 'AUROC': 0.6935, 'ECE': 0.2724}}\n  re_cond: {'n': 238, 'SJ': {'rho': 0.2457, 'tau': 0.1811, 'AUROC': 0.6463, 'ECE': 0.2941}, 'FK': {'rho': 0.1139, 'tau': 0.0876, 'AUROC': 0.551, 'ECE': 0.3424}, 'logprob': {'rho': 0.0112, 'tau': 0.0051, 'AUROC': 0.5186, 'ECE': 0.6464}, 'EM': {'rho': 0.4165, 'tau': 0.3256, 'AUROC': 0.7515, 'ECE': 0.2232}, 'voting_conf': {'rho': 0.2409, 'tau': 0.178, 'AUROC': 0.642, 'ECE': 0.207}}\n  delta_vs_512_ner_full_rho: {'SJ': 0.0034, 'FK': 0.0014, 'EM': 0.0379, 'voting_conf': -0.1226, 'logprob': 0.0656}\n  provenance_note: exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\n\n=== exp_016_rerun_1024_bootstrap (DONE) ===\n  bootstrap_ci_95: [-0.03, 0.042]\n  permutation_p: 0.39\n  cohen_d: 0.038\n  sign_test_win_rate: 0.466\n  ner_logprob_vs_greedy_delta: 0.006\n  conclusion_summary: NER selection: no signal significantly outperforms greedy; RE: same conclusion\n\n=== exp_016_v2 (DONE) ===\n  ner_conditional: {'n': 529, 'best_single_signal_rho': {'soft_jaccard': 0.4412}, 'best_combo_rho': {'sj+vc_a0.55': 0.4552}, 'ensemble_auroc': 0.7141, 'best_single_auroc': {'soft_jaccard': 0.7166}, 'selection_f1': {'greedy': 0.6442, 'logprob_best': 0.6505, 'ensemble_best': 0.6475, 'sj_best': 0.6471, 'oracle': 0.8442}}\n  re_conditional: {'n': 397, 'best_single_signal_rho': {'voting_confidence': 0.3849}, 'best_combo_rho': {'logprob+vc_a0.25': 0.3936}, 'ensemble_auroc': 0.6916, 'best_single_auroc': {'voting_confidence': 0.7023}, 'selection_f1': {'greedy': 0.403, 'logprob_best': 0.4097, 'ensemble_best': 0.4227, 'oracle': 0.6306}}\n  re_full: {'ensemble_auroc': 0.8608, 'best_single_auroc': {'voting_confidence': 0.8248}}\n\n=== exp_025_n32 (DONE) ===\n  n_samples: 32\n  degeneracy_pct: 4\n  lp_range: 0.0781\n  oracle_f1: 0.8412\n  greedy_f1: 0.6615\n  oracle_gap: 0.1797\n  selection_f1_lp_delta: 0.54\n  selection_f1_sj_delta: 0.16\n  selection_f1_fk_delta: 0.6\n  selection_f1_em_delta: 0.68\n  selection_f1_vc_delta: -5.21\n  best_signal: EM\n  best_delta: 0.68\n  metric_space: micro_f1_filtered_529inst\n  note: corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\n\n=== exp_017_llama_conll_n8_t07 (DONE) ===\n  n_valid: 2756\n  greedy_f1: 0.9242\n  oracle_f1: 0.9391\n  lp_range_median: 1.1e-05\n  lp_tied_fraction_005: 0.9579\n  signals: {'SJ': {'rho': 0.3934, 'auroc': 0.6506}, 'FK': {'rho': 0.3879, 'auroc': 0.6488}, 'VC': {'rho': 0.375, 'auroc': 0.6551}, 'EM': {'rho': 0.3888, 'auroc': 0.6494}, 'LP': {'rho': 0.2951, 'auroc': 0.7509}}\n  selection_f1: {'SJ': 0.9247, 'FK': 0.9254, 'VC': 0.9264, 'EM': 0.9255, 'LP': 0.9248}\n\n=== exp_016_signal_ensemble (DONE) ===\n  sj_logprob_pearson_ner: 0.57\n  sj_logprob_pearson_re: 0.42\n  best_linear_ner: {'combo': 'SJ+voting_conf', 'alpha': 0.3, 'rho': 0.489}\n  best_linear_re: {'combo': 'voting_conf+logprob', 'alpha': 0.6, 'rho': 0.429}\n  ensemble_ner_auroc: 0.735\n  ensemble_re_auroc: 0.719\n  best_single_ner_auroc: 0.7\n  best_single_re_auroc: 0.721\n  ensemble_ner_delta: 0.035\n  selection_f1_ner: {'greedy': 0.609, 'logprob': 0.609, 'sj': 0.604, 'ensemble': 0.604, 'voting': 0.596, 'random': 0.58, 'oracle': 0.769}\n  selection_f1_re: {'logprob': 0.397, 'greedy': 0.374, 'sj': 0.368, 'ensemble': 0.367, 'voting': 0.338, 'random': 0.338, 'oracle': 0.561}\n  diagnosis: SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\n\n=== exp_012_logprob_baseline (DONE) ===\n  ner_full_rho_sj: 0.3565\n  ner_full_rho_fk: 0.2651\n  ner_full_rho_logprob: 0.1396\n  ner_full_rho_greedy_logprob: 0.1615\n  ner_full_tau_sj: 0.2658",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Now I have very rich data. Let me note a few critical findings:

### exp_012_rerun_1024 - KEY DATA SOURCE for Tab quality_estimation:

SciERC NER full (n=529):
- VC (voting_conf): rho=0.3792, AUROC=0.6841
- SJ: rho=0.3599, AUROC=0.6917
- FK: rho=0.2665, AUROC=0.629
- EM: rho=0.2945, **AUROC=0.7493**  ← 0.749!!


- LP: rho=0.2052, AUROC=0.5783

Wait, there's a major discrepancy here. The registry shows EM AUROC of 0.7493 for SciERC NER, but the paper's quality_estimation table reports 0.631 for the same metric. The provenance data matches the registry at 0.749, so something's off with what's in the published table. Let me look more carefully at how the paper table is structured.

Looking at the actual rows: FK SciERC AUROC is 0.629 in the paper and matches the registry exactly. The EM SciERC rho value of 0.295 also matches the registry's 0.2945 when rounded. But the EM SciERC AUROC shows 0.631 in the paper while the registry clearly has 0.7493 — that's a significant mismatch I need to investigate.

The task description explicitly states the correct value should be 0.631, not 0.749, which suggests someone deliberately corrected this at some point. But the registry still shows the higher value, so either the table was manually fixed after discovering a computation error, the 0.631 comes from a different experimental run, or there's been a transposition where FK's AUROC got mixed up with EM's. .631 (paper).

Wait — could the paper have swapped FK and EM AUROCs? FK = .629, EM = .631 — these are suspiciously close but not the same. If EM was supposed to be .749 and was changed to .631, that's a different kind of error.

The task says "SciERC EM AUROC = .631（不是 .749）" — this confirms .631 is the intended value. So whoever corrected it changed from .749 to .631 deliberately. Perhaps they re-ran the computation with a different AUROC definition (e.g., binarizing at a different threshold, or using a different F1 measure).

In any case, the registry still has .7493 which contradicts the paper's .631. This is a provenance issue — the paper was updated but the registry wasn't.

Now I'm checking the table columns for SciERC — the "AUC" column appears to be AUROC, and I can verify this by cross-referencing with the registry values. For CoNLL Qwen, the paper shows .816 which matches the registry's .8156 when rounded. For CoNLL LLaMA, the paper shows .705, and I need to check if that aligns with the corresponding registry entry.

The discrepancy is clear: SciERC EM AUROC in the paper is .631, but the registry shows .7493. The task acknowledges this as a known correction, suggesting the .631 value is correct and the registry value is outdated. The likely cause is a change in how AUROC was computed — possibly a different binarization threshold based on the per-dataset median F1.

Now looking at the selection values from exp_016_signal_ensemble, I'm seeing greedy, logprob, sj, and oracle F1 scores that don't align with what's in the table, which suggests these might be from a different experimental setup or configuration. Looking at the CoNLL N=64 results, the MV delta of 0.64pp matches the expected +0.6pp when rounded. For the supervised combination results showing -0.4 to -3.1pp, I'm having trouble pinpointing the exact experiment—it might be using sample-level selection rather than entity-level construction, and the worst-case -3.1pp could come from a specific configuration I haven't located yet. Let me wrap up the audit and do one final check on the frontier model experiments.

Now checking the FewNERD v2 metrics: the degeneracy rate of 50%, Spearman-Johnson correlation of 0.346, and MV gain of +1.4pp all check out against the paper. But there's a discrepancy with the oracle headroom—the paper claims 6.8pp unrealized, but my calculation of oracle minus MV gives a different value, so I need to reconsider what the paper is actually measuring there.

Looking at the frontier degeneracy range across models, I'm seeing values from 5.5% for DeepSeek up to 74% for Claude Sonnet 4, with GPT-5.5 at 50% and Gemini at 28.5%, which matches the stated range in the limitations section.

Now I'm ready to write out the full audit report with all the details I've verified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "66d4a0c7-0ca0-4bd5-a4b5-d180d2fe8038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKmxKoJYkedUWfGAuuRt5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21491,
      "cache_read_input_tokens": 88986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21491
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 66_

I now have comprehensive data. Let me write the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "32264163-d703-42d0-ae83-d69db932e0b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKmxKoJYkedUWfGAuuRt5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21491,
      "cache_read_input_tokens": 88986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21491
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Write · `toolu_01KQXntqGNG7Ue3so4uvAd2V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
  "content": "# 主文数字审计\n\n审计日期: 2026-05-24\n审计范围: docs/paper/sections/ 下所有主文 tex 文件\nRegistry 数据: 完整读取并交叉验证\n\n---\n\n## Abstract\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| AUROC 0.82 | \"AUROC up to $0.82$\" | exp_002 (em_auroc_full=0.8156) | ✅ .816→.82 (2dp rounding) | = Intro \"AUROC $0.82$\"; Tab quality_estimation CoNLL EM .816 |\n| <1 pp | \"selection yields no detectable gains (${<}1$\\,pp)\" | exp_016_rerun_1024_bootstrap | ✅ | = Intro/§4 consistent |\n| +1.40 pp | \"$+1.40$\\,pp on Few-NERD\" | exp_entity_construction (n8_fair_cv) | ⚠️ 见问题 #1 | = Intro +1.40; §4.5 +1.40±0.51; fig_overview caption +1.40 |\n| 3-epoch | \"under 3-epoch training\" | exp_021_fewnerd_full (epochs=3) | ✅ | = Intro/§4 consistent |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED (统计结果，非直接实验 metric) | — | = Intro; §4.5 (k=57); limitations ✅ 一致 |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Intro; §4.5 (k=10) ✅ 一致 |\n| degeneracy + signal alignment collapse | 定性描述 | N/A | ✅ | 一致 |\n\n## Introduction\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| ρ up to 0.45 | \"ρ up to $0.45$\" | exp_002 (em_rho_full=0.4507) | ✅ .451→.45 | = Tab quality_estimation CoNLL EM ρ=.451 |\n| AUROC 0.82 | \"AUROC $0.82$; Table quality_estimation\" | exp_002 (em_auroc_full=0.8156) | ✅ | = Abstract ✅ |\n| MV <1 pp at N=64 | \"MV ${<}1$ percentage point (pp) even at $N{=}64$\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ | = Fig n_scaling caption \"+0.6pp at N=64\" |\n| AUROC 0.63–0.88 | hidden-state probe | ⚠️ UNTRACED (appendix mechanistic) | — | = §4.1 line 53 一致 |\n| ESJ AUROC 0.51 | entity self-judgment | exp_esj_qwen3_all (scierc esj_auroc=0.512) | ✅ | = Tab method_summary AUROC 0.51 |\n| 12–68% | \"degeneracy ($12$--$68$\\%)\" | Tab fewnerd: SciERC 12.2%, WNUT 67.9% | ✅ 12.2→12, 67.9→68 | = Discussion ✅ |\n| LP +1.39 pp | \"LP $+1.39$\\,pp on Few-NERD\" | exp_021_fewnerd_full (lp_delta=1.36, seed42) | ⚠️ 见问题 #2 | = §4.1 +1.39; Tab fewnerd +1.39 |\n| MV +0.6 pp | \"MV $+0.6$\\,pp on CoNLL\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ .64→.6 | = Fig n_scaling; §4.3 |\n| +1.40 pp (construction) | \"Exploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch\" | Same as abstract | ⚠️ 见问题 #1 | = Abstract; §4.5 |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations ✅ |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Abstract; §4.5 ✅ |\n| 87.2% | \"SQL parsing ($87.2$\\% degeneracy)\" | exp_spider_sc_pilot (F1_degeneracy=0.872) | ✅ | 仅出现一次 |\n| 40% zero-F1 | \"RE…$40$\\% zero-F1\" | provenance c006 notes \"paper uses 40% from primary config\"; registry shows 44.3% at N=16 | ⚠️ 见问题 #3 | = §4.3 \"40%\" 一致 |\n| ρ up to 0.47 | \"\\citet{yao2026consistency} report…$\\rho$ up to 0.47\" | 引用他人数据 | N/A | 仅引用 |\n| LP mean weight 0.78 | \"ensemble optimization assigns LP mean weight $0.78$\" | ⚠️ UNTRACED (appendix supervised_combination) | — | 仅出现一次 |\n| 3–12% recovery ratio | \"3--12\\% recovery ratio\" | ⚠️ UNTRACED (理论计算) | — | = theoretical.tex; theory.tex ✅ |\n| α=0.000–0.121 | \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" | ⚠️ UNTRACED (理论计算) | — | = theory.tex line 38 ✅ |\n| +3.85 pp MV | \"pretrained Qwen2.5-7B at $N{=}32$ achieves $+3.85$\\,pp MV gain\" | exp_fewnerd_pretrained_n32_s42_v2 (mv_delta=3.85) | ✅ | 仅出现一次 |\n| D=5.4% | \"$D{=}5.4$\\%\" | exp_fewnerd_pretrained_n32_s42_v2 (degen=5.42) | ✅ 5.42→5.4 | 仅出现一次 |\n\n## §3 Diagnostic Framework\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +4.6 F1 points | \"length normalization eliminates length bias ($+4.6$ F1 points)\" | ⚠️ UNTRACED (appendix token_signal) | — | 仅出现一次 |\n| n=529 | \"n=529 on SciERC\" | exp_012_rerun_1024 (ner_full n=529) | ✅ | = Tab quality_estimation caption; Tab fewnerd SciERC n=529 |\n| n=2,756 | \"n=2,756 on CoNLL\" | exp_017_llama_conll_infer data | ✅ | = Tab fewnerd CoNLL n=2,756 |\n| 9–26% | \"Entity-set exact-match degeneracy…($9$--$26$\\%)\" | exp_fewnerd_mf4_s* (8.1%–9.3% at 5-epoch) | ⚠️ 见问题 #4 | 脚注内部使用 |\n| 13–31% | \"vs.\\ $13$--$31$\\% constant-F1\" | exp_021 seeds (10.1%–13.1% at 3-epoch) | ⚠️ 部分匹配 | 脚注内部使用 |\n\n## §4.1 Single-Signal Selection Results\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| 60% LP range <0.041 | \"60\\% of SciERC instances showing within-instance LP range below 0.041 nats\" | ⚠️ UNTRACED (appendix logprob_ties) | — | 仅出现一次 |\n| 0.97× | \"free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97$)\" | exp_conll_freeform_n8_s42 / exp_fewnerd_freeform_n8_s42 | ⚠️ 无法直接确认 0.97 | 仅出现一次 |\n| Tab selection: Oracle 0.775±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (oracle=0.776) | ⚠️ .776 vs .775 | 仅 Tab selection |\n| Tab selection: Greedy 0.645±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (greedy=0.644) | ⚠️ .644 vs .645 | ❌ 见问题 #5 |\n| Tab selection: LP 0.647±0.005 | LP selection F1 | exp_016_rerun_1024_bootstrap | ⚠️ 间接 | 仅 Tab selection |\n| Tab selection: LP p=.29 | \"LP achieves $+0.2$\\,pp ($p{=}0.29$)\" | exp_016_rerun_1024_bootstrap (permutation_p=0.39) | ❌ 见问题 #6 | Tab vs text 一致 (.29) |\n| ρ up to 0.38 | \"Despite $\\rho$ up to 0.38\" | exp_012_rerun_1024 (vc_rho=0.3792) | ✅ .379→.38 | = Tab quality_estimation VC ρ=.379 |\n| +13.0 pp headroom | \"the oracle shows 13.0\\,pp headroom\" | Tab selection: 0.775-0.645=0.130=13.0pp | ✅ | = fig_selection_gap caption \"+13.0pp\" ✅ |\n| MDE ≈1.5 pp | \"below MDE (${\\approx}$1.5\\,pp at $n{=}529$, 2--3 seeds\" | ⚠️ UNTRACED (统计计算) | — | = limitations ✅ |\n| LP +1.39 pp (Few-NERD) | \"LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, k=21)\" | exp_021_fewnerd_full (1.36 for seed42) | ⚠️ 见问题 #2 | = Tab fewnerd; Intro |\n| p_adj=0.021, k=21 | selection family correction | provenance C143 has p_adj=0.019 k=19 | ⚠️ 见问题 #7 | 仅出现一次 |\n| p_adj=0.055 (global k=57) | footnote | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations |\n| 13.0% degeneracy (Few-NERD) | \"low degeneracy (13.0\\%)\" | 见问题 #8 | ⚠️ | = Tab fewnerd 13.0% |\n| 12.2% (SciERC) | \"SciERC 12.2\\%\" | exp_012_rerun_1024 (degen=0.1777?) | ⚠️ 见问题 #9 | = Tab fewnerd 12.2% ✅ |\n| 61.7% (CoNLL) | \"CoNLL 61.7\\%\" | ⚠️ UNTRACED | — | = Tab fewnerd 61.7% ✅ |\n| VC −1.79, SJ −2.14 pp | structural signals degrade on Few-NERD | exp_021_fewnerd_full (vc_delta=-1.79, sj_delta=-2.14) | ✅ | = §4.3 一致 |\n| ρ=0.052, n=23, p=0.81 | degeneracy-LP across configs | ⚠️ UNTRACED | — | = §4.3 Fig degeneracy_scatter ✅ |\n| ρ=−0.881 | within-dataset degen-LP | ⚠️ UNTRACED | — | = §4.3 ✅ |\n| MRSC −3.1 pp | multi-round refinement | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| LSC −3.5 pp | latent centroid selection | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| ESJ AUROC 0.50–0.55 (Qwen3-8B) | cross-model ESJ | exp_esj_qwen3_all (scierc=0.512, fewnerd=0.495) | ✅ | 仅出现一次 |\n\n## §4.2–4.3 Experiments (experiments_main.tex)\n\n### Tab quality_estimation\n\n| 数字 | 来源 exp_id | 验证 |\n|------|------------|------|\n| SciERC VC ρ=.379 | exp_012_rerun_1024 (voting_conf rho=0.3792) | ✅ |\n| SciERC SJ ρ=.360 | exp_012_rerun_1024 (SJ rho=0.3599) | ✅ |\n| SciERC FK ρ=.267 | exp_012_rerun_1024 (FK rho=0.2665) | ✅ |\n| SciERC EM ρ=.295 | exp_012_rerun_1024 (EM rho=0.2945) | ✅ |\n| SciERC LP ρ=.205 | exp_012_rerun_1024 (LP rho=0.2052) | ✅ |\n| SciERC VC AUC=.684 | exp_012_rerun_1024 (voting_conf AUROC=0.6841) | ✅ |\n| SciERC SJ AUC=.692 | exp_012_rerun_1024 (SJ AUROC=0.6917) | ✅ |\n| SciERC FK AUC=.629 | exp_012_rerun_1024 (FK AUROC=0.629) | ✅ |\n| **SciERC EM AUC=.631** | **exp_012_rerun_1024 (EM AUROC=0.7493)** | **❌ 见问题 #10** |\n| SciERC LP AUC=.578 | exp_012_rerun_1024 (LP AUROC=0.5783) | ✅ |\n| CoNLL Qwen EM ρ=.451 | exp_002 (em_rho_full=0.4507) | ✅ |\n| CoNLL Qwen EM AUC=.816 | exp_002 (em_auroc_full=0.8156) | ✅ |\n| CoNLL Qwen SJ ρ=.436 | exp_002 (sj_rho_full=0.4357) | ✅ |\n| CoNLL LLaMA SJ ρ=.431 | exp_017_llama_conll_infer (SJ_rho=0.4314) | ✅ |\n| CoNLL LLaMA LP AUC=.761 | exp_017_llama_conll_infer (logprob_AUROC=0.761) | ✅ |\n\n### Tab fewnerd (cross-dataset LP selection)\n\n| 数字 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|------------|------|-----------|\n| WNUT n=1,287 | exp_003_wnut17_eval (n=1287) | ✅ | = §4.2 |\n| WNUT Greedy .452 | exp_wnut17_qwen25_7b (seed42 greedy=0.4524) | ✅ | — |\n| WNUT Degen 67.9% | ⚠️ UNTRACED (N=8 data; registry WNUT experiments are N=16) | — | = text 12–68% upper bound |\n| WNUT LP ρ=−.446 | ⚠️ UNTRACED (registry has −.414/−.409 at N=16) | — | — |\n| CoNLL n=2,756 | consistent | ✅ | = §3 |\n| CoNLL Greedy .908 | ⚠️ UNTRACED for N=8 Qwen | — | — |\n| CoNLL Degen 61.7% | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| CoNLL LP ρ=.302 | ⚠️ ≠ Tab quality_estimation LP ρ=.316 | ⚠️ 见问题 #11 | — |\n| **SciERC Greedy .663** | **exp_scierc_n8_s* (greedy ≈0.661–0.666)** | ✅ matches multi-seed | **❌ ≠ Tab selection Greedy .645 见问题 #5** |\n| SciERC Degen 12.2% | ⚠️ PARTIALLY TRACED | — | = §4.1 ✅ |\n| **SciERC LP ρ=.159** | ⚠️ UNTRACED | — | **❌ ≠ Tab quality_estimation LP ρ=.205 见问题 #11** |\n| **SciERC LP Δ=+0.61 pp** | ⚠️ UNTRACED | — | **❌ ≠ §4.1 text \"+0.2pp\" 见问题 #5** |\n| Few-NERD n=32,565 | exp_021_fewnerd_full (filtered=32565) | ✅ | — |\n| Few-NERD Greedy .748 | exp_021_fewnerd_full (greedy=0.7478) | ✅ | — |\n| Few-NERD Degen 13.0% | ⚠️ 见问题 #8 | — | = §4.1 ✅ |\n| Few-NERD LP ρ=.220 | ⚠️ ≠ exp_021 lp_global_rho=0.4215 | ⚠️ 见问题 #12 | — |\n| Few-NERD LP Δ=+1.39 pp | exp_021_fewnerd_full (1.36 seed42) | ⚠️ 见问题 #2 | = §4.1; Intro |\n\n### Other §4 numbers\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| SciERC 551 instances, 6 types | §4.2 setup | ✅ 标准 | ✅ | = §3 n=529 (gold-filtered) consistent |\n| Few-NERD 37,648 instances, 8 types | §4.2 setup | exp_021 (instance_count=37648) | ✅ | — |\n| CoNLL 3,453 instances, 4 types | §4.2 setup | ✅ 标准 | ✅ | — |\n| WNUT-17 1,287 instances, 53.7% zero F1 | §4.2 setup | exp_003_wnut17_eval (53.7%) | ✅ | — |\n| SJ>LP Δρ=+0.151±0.006 | §4.2 QE results | ⚠️ UNTRACED (bootstrap) | — | 仅出现一次 |\n| p_adj=0.013 (k=5) | seed-replication SJ>LP | ⚠️ UNTRACED | — | 仅出现一次 |\n| CoNLL EM ρ=0.816 (AUROC) | §4.2 \"EM leads both ρ and AUROC ($0.816$)\" | exp_002 (em_auroc=0.8156) | ✅ | = Tab quality_estimation |\n| WNUT VC ρ=0.724 at N=16 | §4.2 | exp_003 系列 | ⚠️ UNTRACED | 仅出现一次 |\n| WNUT conditional ρ=0.038 | §4.2 | ⚠️ UNTRACED | — | 仅出现一次 |\n| LP conditional ρ=0.350 | §4.2 WNUT | exp_003_wnut17_eval (rho_logprob_cond=0.35) | ✅ | 仅出现一次 |\n| LP σ=0.04 vs SJ 2.02 pp | §4.3 seed stability | ⚠️ UNTRACED | — | 仅出现一次 |\n| 50× more seed-stable | 2.02/0.04=50.5≈50 | ✅ 算术一致 | — | 仅出现一次 |\n| ρ=0.90, p=0.002 (MV vs low-F1 types) | §4.3 | ⚠️ UNTRACED (appendix pertype) | — | 仅出现一次 |\n| MV −2.71 pp (Few-NERD) | §4.3 | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen3-4B |Δρ|=0.042 | §4.4 robustness | ⚠️ UNTRACED | — | 仅出现一次 |\n| +1.40±0.51 pp (construction) | §4.5 | exp_entity_construction | ⚠️ 见问题 #1 | = Abstract; Intro |\n| +0.32 pp SciERC (n.s.) | §4.5 | ⚠️ 见问题 #13 | — | 仅出现一次 |\n| −0.39 pp CoNLL | §4.5 | exp_entity_construction (conll cv_uniform='-0.39pp') | ✅ | 仅出现一次 |\n| D=13%, headroom=12.4 pp | §4.5 Few-NERD | exp_021 (headroom=0.124=12.4pp) | ✅ | — |\n| p_adj=0.006 (k=10) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro |\n| p_adj=0.055 (k=57) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro; limitations |\n| ρ_adj=0.516 | §4.5 construction-selection correlation | ⚠️ UNTRACED | — | 仅出现一次 |\n| 5-epoch: +1.39→+0.12 pp (selection) | §4.5 epoch confound | exp_fewnerd_5epoch_lp_s42 (lp_delta=0.12) | ✅ (5-epoch end) | — |\n| **5-epoch: +0.88→+0.20 pp (construction)** | §4.5 epoch confound | exp_entity_construction (n8_fair_cv fewnerd lp_weighted_cv='+0.88pp') | ⚠️ 见问题 #1 | — |\n| 9%→26% degeneracy | §4.5 epoch confound | 见问题 #4 | ⚠️ | — |\n\n## §4.4 Adaptive Methods\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +0.42 pp (cross-model) | Qwen+LLaMA on Few-NERD | exp_cross_model_consistency (delta=0.42, p=0, CI=[0.27,0.58]) | ✅ | = Tab method_summary |\n| CI [0.27, 0.58] | cross-model CI | exp_cross_model_consistency | ✅ | 仅出现一次 |\n| AUC=0.923±0.002 | LightGBM verifier | exp_b2_entity_verifier (oof_auc=0.9233) | ✅ | = Tab method_summary |\n| +0.30 pp (verifier) | LightGBM F1 gain | exp_b2_entity_verifier (oof_delta_pp=0.3) | ✅ | = Tab method_summary |\n| −0.76 to −1.02 pp | verifier cross-dataset transfer | ⚠️ UNTRACED (appendix verifier_transfer) | — | 仅出现一次 |\n| ESJ AUROC 0.51 | Tab method_summary | exp_esj_qwen3_all (esj_auroc=0.512) | ✅ | = §4.1 |\n| MRSC −3.1 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| LSC −3.5 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| DALS +0.71 pp (SciERC) | Tab method_summary | ⚠️ UNTRACED | — | 仅出现一次 |\n| −0.4 to −3.1 pp | Sup. combination LR/MLP/RF | ⚠️ 见问题 #14 | — | 仅出现一次 |\n\n## §Theoretical Analysis (theoretical.tex)\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| G_nd≈14.8 pp | \"with $G_{\\textup{nd}}{\\approx}14.8$\\,pp\" | ⚠️ UNTRACED (理论计算) | — | 仅出现一次 |\n| α≈0.068 | \"$\\alpha{\\approx}0.068$\" | ⚠️ UNTRACED | — | = fig_bound caption |\n| θ_crit=0.70 | \"$\\theta_{\\textup{crit}}{=}0.70$\" | ✅ 算术验证: (1-0.70)×14.8×0.068=0.302≈0.3pp | = theory.tex θ_crit∈[0.60,0.80] 一致 |\n| 3–12% | recovery ratio | ⚠️ UNTRACED | — | = Intro; theory.tex ✅ |\n\n## §Threshold Regime Analysis (theory.tex)\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| R²>0.999 | oracle scaling fit | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.61 (Few-NERD) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.35 (SciERC) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| 8B→14B: +1.2 pp oracle, +0.9 pp greedy | scale ablation | ⚠️ UNTRACED | — | 仅出现一次 |\n| GPT-5.5: 50% degen | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (degen=0.5) | ✅ | 仅出现一次 |\n| GPT-5.5: SJ ρ=0.346 | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (sj_rho=0.3461) | ✅ | 仅出现一次 |\n| GPT-5.5: MV +1.4 pp | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2: mv-greedy=0.6521-0.6382=0.0139=1.39pp→1.4 | ✅ | 仅出现一次 |\n| GPT-5.5: 6.8 pp unrealized | frontier SC | oracle-mv=0.7203-0.6521=0.0682=6.82pp→6.8 | ✅ | 仅出现一次 |\n| 10.1% empty entity sets | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 88% gold-empty | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 1.2% true parse failures (19/1600) | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen2.5: 31.7–46.2% | cross-scale degen | ⚠️ UNTRACED | — | 仅出现一次 |\n| 40 of 58 transitions (p<0.05) | inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| θ=2/N: −3.09 pp (N=8), −6.90 pp (N=16) | inverse scaling severity | ⚠️ UNTRACED | — | 仅出现一次 |\n| MV: −0.87/−0.60 pp | MV inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| OR=0.109 (11.1% vs 1.3%) | degen vs inverse scaling | ⚠️ UNTRACED; 算术近似验证: (1.3/98.7)/(11.1/88.9)=0.1055≈0.109 | — | 仅出现一次 |\n| CoNLL SJ ρ .30→.44 | few-shot improvement | ⚠️ UNTRACED | — | 仅出现一次 |\n| α=0.000–0.121 | binding constraint | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| 8–33× tighter | α vs D | ⚠️ UNTRACED | — | = Intro; Discussion ✅ |\n| split-half r=0.395–0.578 | FK independence | ⚠️ UNTRACED | — | 仅出现一次 |\n| bound ratio 0.13–0.63 | signal-adjusted bound | ⚠️ UNTRACED | — | 仅出现一次 |\n| α_crit,eff=1.148 (CoNLL) | MV impossibility | ⚠️ UNTRACED | — | 仅出现一次 |\n\n## §5 Discussion\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 12–68% | degeneracy range | ✅ | = Intro; §4.5 ✅ |\n| α→0 | signal alignment collapse | ✅ | 全文一致 |\n| 8–33× tighter | α vs D | ✅ | = Intro; theory.tex ✅ |\n| >50% | high degeneracy threshold | ✅ | 全文一致 |\n\n## Limitations\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 5.5–74% | frontier degeneracy | exp_frontier_sc_deepseek (5.5%), exp_frontier_sc_claude_sonnet4 (74%) | ✅ | 仅出现一次 |\n| p_adj=0.055 | strongest construction claim | ✅ | = Abstract; §4.5 ✅ |\n| MDE≈1.5 pp | statistical power | ✅ | = §4.1 ✅ |\n| RE n=397, SQL n=196 | cross-task sample sizes | exp_spider_sc_pilot (n=196) | ✅ SQL; RE ⚠️ UNTRACED | — |\n| +1–1.4 pp | construction gain range | ✅ 与 §4.5 一致 | — |\n\n---\n\n## 关键数字重点检查\n\n### 1. SciERC EM AUROC = .631（不是 .749）\n- **Tab quality_estimation: .631** ✅ 论文正确\n- **Registry exp_012_rerun_1024: EM AUROC = 0.7493** ❌ Registry 与论文不一致\n- **Provenance c002: \"EM leads AUROC (NER 0.749)\"** ❌ Provenance STALE\n- **结论**: 论文已正确修改为 .631，但 registry 和 provenance 仍保留旧值 .749。**paper_provenance.yaml 需要更新。**\n\n### 2. Headroom = 13.0pp（不是 11.4pp）\n- Tab selection: Oracle 0.775 − Greedy 0.645 = 0.130 = **13.0pp** ✅\n- fig_selection_gap caption: **+13.0pp** ✅\n- 全文无 11.4pp 出现。**PASS。**\n\n### 3. MV = +0.6pp（不是 +0.61pp）\n- Intro: \"MV $+0.6$\\,pp on CoNLL\" ✅\n- Fig n_scaling caption: \"+0.6pp at N=64\" ✅\n- §4.3 text: \"+0.6pp\" ✅\n- Registry exp_conll_n64_s42: mv_delta = 0.64pp → 0.6 (1dp rounded) ✅\n- 全文无 +0.61pp 出现（Tab fewnerd SciERC LP Δ = +0.61pp 是 LP 不是 MV）。**PASS。**\n\n### 4. α = 0.121\n- §4.1: \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" ✅\n- theory.tex: \"$\\alpha{=}0.000$--$0.121$\" ✅\n- 上限一致。**PASS。**\n\n### 5. SciERC construction = +0.32pp n.s.\n- §4.5: \"a non-significant $+0.32$\\,pp on SciERC\" ✅ 论文内一致\n- **Registry discrepancy**: exp_entity_construction 显示 SciERC n8_fair_cv 多个变体均 >+1pp（见问题 #13）\n- **结论**: 论文内一致，但 registry 来源不清楚。可能来自不同配置或后续重算。\n\n### 6. Holm p_adj = 0.055 (global k=57) vs p_adj = 0.013 (seed-replication k=5)\n- **p_adj=0.055 (k=57)**: Abstract, Intro, §4.5, limitations — 全部一致 ✅\n- **p_adj=0.013 (k=5)**: §4.2 \"SJ>LP advantage reaches $p_{\\text{adj}}{=}0.013$\" — 这是信号比较的 seed-replication correction ✅\n- 两者是不同统计框架，论文正确区分了。**PASS。**\n\n### 7. fig_selection_gap caption Oracle = +13.0pp（不是 +13.1pp）\n- Caption: \"oracle headroom ($+13.0$\\,pp)\" ✅\n- Tab selection: 0.775 − 0.645 = 0.130 = 13.0pp ✅\n- 全文无 13.1pp 出现。**PASS。**\n\n---\n\n## 问题清单\n\n按严重程度排序：\n\n### 🔴 严重 (Cross-table inconsistency)\n\n**#5. SciERC 基线在两个表格间不一致**\n- Tab selection (§4.1): Greedy = 0.645±0.001, LP Δ = +0.2pp (p=0.29)\n- Tab fewnerd (§4.3): Greedy = 0.663, LP Δ = +0.61pp (p=0.193)\n- 两表均标注 \"SciERC, Qwen3-8B, N=8, T=1.0\"\n- **差异**: Greedy F1 差 1.8pp; LP Δ 差 0.41pp\n- **可能原因**: 不同训练种子 / 不同 model checkpoint（exp_016 系列 vs exp_scierc_n8_s* 系列），但论文未说明\n- **影响**: 读者会困惑为何同一设置有不同基线\n\n**#10. SciERC EM AUROC: 论文 .631 vs Registry .7493**\n- Tab quality_estimation 显示 .631\n- exp_012_rerun_1024 registry 显示 EM AUROC = 0.7493\n- Provenance c002 仍记录 0.749\n- **状态**: 论文值 .631 被指定为正确值（任务说明），但 **registry 和 provenance 从未更新**\n- **影响**: 后续引用 provenance 的操作会得到错误数据\n\n**#11. SciERC/CoNLL LP ρ 在 Tab quality_estimation vs Tab fewnerd 间不一致**\n- SciERC LP ρ: Tab quality_estimation = .205; Tab fewnerd = .159 (差 0.046)\n- CoNLL LP ρ: Tab quality_estimation = .316; Tab fewnerd = .302 (差 0.014)\n- Tab quality_estimation 是 primary seed=42; Tab fewnerd 是 3-seed mean\n- **差异可能合理**（不同种子均值），但未在文中说明\n\n### 🟡 中等 (Traceability / consistency concern)\n\n**#1. Construction +1.40pp vs +0.88pp 同一方法不同数字**\n- §4.5 主结果: LP-weighted construction = +1.40±0.51pp (4-seed mean, full test)\n- §4.5 epoch confound: \"construction: +0.88→+0.20pp\"\n- Registry: n8_fair_cv fewnerd LP-weighted CV = +0.88pp\n- **分析**: +1.40 是 4-seed non-CV; +0.88 是 5-fold CV。两种评估方法给出不同结果。论文在同一段落交替使用两种评估方法而未说明\n- **影响**: 读者可能误以为 3-epoch construction gain = +0.88pp 而非 +1.40pp\n\n**#2. LP selection +1.39pp: 主种子显示 1.36pp**\n- 论文: +1.39pp (标注 3-seed mean)\n- Registry exp_021_fewnerd_full (seed42): lp_selection_delta_pp = 1.36\n- 其他种子 LP delta 未在 registry summary 中找到\n- **影响**: 无法从 registry 直接验证 1.39 是否为正确的 3-seed mean\n\n**#6. Tab selection LP p-value: 论文 .29 vs Registry .39**\n- Tab selection: LP p=.29\n- exp_016_rerun_1024_bootstrap: permutation_p = 0.39\n- **可能原因**: Tab selection 可能用 paired bootstrap（2-seed），exp_016 用 permutation test；或来自不同实验版本\n- **影响**: p-value 不同但结论相同（均不显著）\n\n**#7. Holm p_adj: 论文 0.021 (k=21) vs Provenance 0.019 (k=19)**\n- §4.1 footnote: \"Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$\"\n- Provenance C143: \"p_adj=0.019 k=19\"\n- **分析**: 家族大小从 19 增至 21（加入更多比较），p_adj 相应增大。Provenance stale。\n- **影响**: 数值轻微差异，结论不变\n\n**#8. Few-NERD degeneracy 13.0%: 主种子 registry 显示 10.1%**\n- Tab fewnerd: 13.0% (标注 3-seed mean)\n- exp_021_fewnerd_full (seed42): degeneracy_rate = 0.101 (10.1%)\n- exp_021_fewnerd_n8_seed123: degen_rate = 0.1312 (13.1%)\n- exp_021_fewnerd_n8_seed456: degen_rate = 0.1212 (12.1%)\n- 3-seed mean: (10.1+13.1+12.1)/3 = 11.8%, not 13.0%\n- **可能原因**: seed42 的 0.101 可能不是 constant-F1 degeneracy（seed123/456 标注为 unified_metrics_constant_f1_gold_filtered，seed42 未标注）\n- **影响**: 无法确认 13.0% 的准确性\n\n**#3. RE 40% zero-F1: Registry 显示 44.3%**\n- 论文多处: \"40% zero-F1\"\n- Provenance c006: \"44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\"\n- 40% 的具体来源实验不在 registry summary 中\n- **影响**: 轻微，但 40 vs 44.3 的差异未解释\n\n**#9. SciERC degeneracy 12.2%: Registry exp_012 显示 17.77%**\n- Tab fewnerd: SciERC Degen.% = 12.2%\n- exp_012_rerun_1024: degen_rate = 0.1777 (17.77%)\n- exp_scierc_n8_s123: degeneracy_rate = 0.116 (11.6%)\n- exp_scierc_n8_s456: degeneracy_rate = 0.12 (12.0%)\n- **分析**: 12.2% 可能来自 s123/s456 的均值而非 exp_012，或 exp_012 的 17.77% 是不同度量\n- **影响**: 来源不清楚\n\n**#12. Few-NERD LP ρ=.220 in Tab fewnerd vs .4215 in Registry**\n- Tab fewnerd: LP ρ = .220\n- exp_021_fewnerd_full: lp_global_rho = 0.4215\n- 差异 2x，即使是 3-seed mean 也不太可能降到 .220\n- **可能原因**: Tab fewnerd 的 LP ρ 可能不是 global cross-instance ρ，而是某种 within-instance 或 conditional 度量\n- **影响**: 如果是不同度量，需要在表格或 caption 中注明\n\n**#13. SciERC construction +0.32pp vs Registry +1.12~+1.67pp**\n- 论文: \"+0.32pp on SciERC (non-significant)\"\n- Registry exp_entity_construction: SciERC n8_fair_cv 多个变体 = +1.12 to +1.67pp\n- **可能原因**: 不同 θ、不同评估方法、不同种子集\n- **影响**: 无法从 registry 追溯 +0.32pp 的来源\n\n**#14. Supervised combination \"-0.4 to -3.1pp\"**\n- Tab method_summary: \"LR/MLP/RF: −0.4 to −3.1pp\"\n- Registry exp_backup3_distill_verifier: per-fold deltas 最大 = −0.34pp\n- −3.1pp 在 registry 中找不到对应\n- **可能原因**: −3.1pp 可能来自另一个实验或特定配置\n- **影响**: 范围上界无法追溯\n\n### 🟢 轻微 (Rounding / precision)\n\n**#4. Degeneracy type mixing in epoch comparison**\n- §4.5: \"degeneracy rises from 9% to 26%\" — entity-set exact-match\n- 主表 (Tab fewnerd): 13.0% — constant-F1\n- 脚注已解释两种度量，但正文在不同位置使用不同度量未明确标注\n\n**\"LP-best +1.4pp\" 精度模糊**\n- §4.3: \"LP-best $+1.4$\\,pp on Few-NERD\" — 可能是 selection (+1.39→1.4) 或 construction (+1.40)\n- 建议明确是哪种方法\n\n**AUROC rounding**\n- Abstract/Intro: \"AUROC up to 0.82\" — 来自 .816 (2dp rounding)\n- 技术上正确但比表格精度低\n\n---\n\n## 精度一致性\n\n| 类别 | 精度 | 评估 |\n|------|------|------|\n| 表格 ρ 值 | 3 位小数 (.379, .360) | ✅ 表内一致 |\n| 正文 ρ 引用 | 2 位小数 (.38, .45) | ✅ 合理简化 |\n| pp 增益 | 1-2 位小数 (+1.39, +0.6, +0.2) | ⚠️ +0.6 vs +1.39 精度不统一 |\n| 百分比 (degeneracy) | 1 位小数 (12.2%, 13.0%) | ✅ 一致 |\n| p-values | 表格 2 位 (.29, .67); 正文混合 | ✅ 大致一致 |\n| AUROC | 表格 3 位 (.631, .816); 正文 2 位 (.82) | ⚠️ 正文与表格精度不同但可接受 |\n\n总体精度一致性：**合格**，无系统性精度不一致问题。\n\n---\n\n## 总结\n\n- **已验证数字**: ~60% 可追溯到 registry 实验或算术验证\n- **UNTRACED**: ~25% 来自 appendix 实验或统计计算，无法从 registry summary 直接验证\n- **发现问题**: 14 个，其中 3 个严重（跨表不一致）、11 个中等或轻微\n- **7 个 bug-prone 数字**: 论文中全部正确 ✅，但 registry/provenance 有 2 处 stale 数据\n\n**最需要关注的问题**:\n1. Tab selection vs Tab fewnerd SciERC 基线不一致 (问题 #5)\n2. Registry EM AUROC stale (问题 #10) — 需更新 registry 和 provenance\n3. Construction +1.40 vs +0.88 评估方法混用 (问题 #1)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "9947dacd-0923-441c-8234-898fb7baae1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKmxKoJYkedUWfGAuuRt5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21491,
      "cache_read_input_tokens": 88986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21491
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-24T04:44:39.742Z_

<details><summary>↩ Tool result · `toolu_01KQXntqGNG7Ue3so4uvAd2V`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "8f217cda-4d07-4f42-9274-28c6714d87d9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
    "content": "# 主文数字审计\n\n审计日期: 2026-05-24\n审计范围: docs/paper/sections/ 下所有主文 tex 文件\nRegistry 数据: 完整读取并交叉验证\n\n---\n\n## Abstract\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| AUROC 0.82 | \"AUROC up to $0.82$\" | exp_002 (em_auroc_full=0.8156) | ✅ .816→.82 (2dp rounding) | = Intro \"AUROC $0.82$\"; Tab quality_estimation CoNLL EM .816 |\n| <1 pp | \"selection yields no detectable gains (${<}1$\\,pp)\" | exp_016_rerun_1024_bootstrap | ✅ | = Intro/§4 consistent |\n| +1.40 pp | \"$+1.40$\\,pp on Few-NERD\" | exp_entity_construction (n8_fair_cv) | ⚠️ 见问题 #1 | = Intro +1.40; §4.5 +1.40±0.51; fig_overview caption +1.40 |\n| 3-epoch | \"under 3-epoch training\" | exp_021_fewnerd_full (epochs=3) | ✅ | = Intro/§4 consistent |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED (统计结果，非直接实验 metric) | — | = Intro; §4.5 (k=57); limitations ✅ 一致 |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Intro; §4.5 (k=10) ✅ 一致 |\n| degeneracy + signal alignment collapse | 定性描述 | N/A | ✅ | 一致 |\n\n## Introduction\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| ρ up to 0.45 | \"ρ up to $0.45$\" | exp_002 (em_rho_full=0.4507) | ✅ .451→.45 | = Tab quality_estimation CoNLL EM ρ=.451 |\n| AUROC 0.82 | \"AUROC $0.82$; Table quality_estimation\" | exp_002 (em_auroc_full=0.8156) | ✅ | = Abstract ✅ |\n| MV <1 pp at N=64 | \"MV ${<}1$ percentage point (pp) even at $N{=}64$\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ | = Fig n_scaling caption \"+0.6pp at N=64\" |\n| AUROC 0.63–0.88 | hidden-state probe | ⚠️ UNTRACED (appendix mechanistic) | — | = §4.1 line 53 一致 |\n| ESJ AUROC 0.51 | entity self-judgment | exp_esj_qwen3_all (scierc esj_auroc=0.512) | ✅ | = Tab method_summary AUROC 0.51 |\n| 12–68% | \"degeneracy ($12$--$68$\\%)\" | Tab fewnerd: SciERC 12.2%, WNUT 67.9% | ✅ 12.2→12, 67.9→68 | = Discussion ✅ |\n| LP +1.39 pp | \"LP $+1.39$\\,pp on Few-NERD\" | exp_021_fewnerd_full (lp_delta=1.36, seed42) | ⚠️ 见问题 #2 | = §4.1 +1.39; Tab fewnerd +1.39 |\n| MV +0.6 pp | \"MV $+0.6$\\,pp on CoNLL\" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ .64→.6 | = Fig n_scaling; §4.3 |\n| +1.40 pp (construction) | \"Exploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch\" | Same as abstract | ⚠️ 见问题 #1 | = Abstract; §4.5 |\n| p_adj=0.055 | \"global Holm $p_{\\text{adj}}{=}0.055$\" | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations ✅ |\n| p_adj=0.006 | \"per-family $p_{\\text{adj}}{=}0.006$\" | ⚠️ UNTRACED | — | = Abstract; §4.5 ✅ |\n| 87.2% | \"SQL parsing ($87.2$\\% degeneracy)\" | exp_spider_sc_pilot (F1_degeneracy=0.872) | ✅ | 仅出现一次 |\n| 40% zero-F1 | \"RE…$40$\\% zero-F1\" | provenance c006 notes \"paper uses 40% from primary config\"; registry shows 44.3% at N=16 | ⚠️ 见问题 #3 | = §4.3 \"40%\" 一致 |\n| ρ up to 0.47 | \"\\citet{yao2026consistency} report…$\\rho$ up to 0.47\" | 引用他人数据 | N/A | 仅引用 |\n| LP mean weight 0.78 | \"ensemble optimization assigns LP mean weight $0.78$\" | ⚠️ UNTRACED (appendix supervised_combination) | — | 仅出现一次 |\n| 3–12% recovery ratio | \"3--12\\% recovery ratio\" | ⚠️ UNTRACED (理论计算) | — | = theoretical.tex; theory.tex ✅ |\n| α=0.000–0.121 | \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" | ⚠️ UNTRACED (理论计算) | — | = theory.tex line 38 ✅ |\n| +3.85 pp MV | \"pretrained Qwen2.5-7B at $N{=}32$ achieves $+3.85$\\,pp MV gain\" | exp_fewnerd_pretrained_n32_s42_v2 (mv_delta=3.85) | ✅ | 仅出现一次 |\n| D=5.4% | \"$D{=}5.4$\\%\" | exp_fewnerd_pretrained_n32_s42_v2 (degen=5.42) | ✅ 5.42→5.4 | 仅出现一次 |\n\n## §3 Diagnostic Framework\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +4.6 F1 points | \"length normalization eliminates length bias ($+4.6$ F1 points)\" | ⚠️ UNTRACED (appendix token_signal) | — | 仅出现一次 |\n| n=529 | \"n=529 on SciERC\" | exp_012_rerun_1024 (ner_full n=529) | ✅ | = Tab quality_estimation caption; Tab fewnerd SciERC n=529 |\n| n=2,756 | \"n=2,756 on CoNLL\" | exp_017_llama_conll_infer data | ✅ | = Tab fewnerd CoNLL n=2,756 |\n| 9–26% | \"Entity-set exact-match degeneracy…($9$--$26$\\%)\" | exp_fewnerd_mf4_s* (8.1%–9.3% at 5-epoch) | ⚠️ 见问题 #4 | 脚注内部使用 |\n| 13–31% | \"vs.\\ $13$--$31$\\% constant-F1\" | exp_021 seeds (10.1%–13.1% at 3-epoch) | ⚠️ 部分匹配 | 脚注内部使用 |\n\n## §4.1 Single-Signal Selection Results\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| 60% LP range <0.041 | \"60\\% of SciERC instances showing within-instance LP range below 0.041 nats\" | ⚠️ UNTRACED (appendix logprob_ties) | — | 仅出现一次 |\n| 0.97× | \"free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97$)\" | exp_conll_freeform_n8_s42 / exp_fewnerd_freeform_n8_s42 | ⚠️ 无法直接确认 0.97 | 仅出现一次 |\n| Tab selection: Oracle 0.775±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (oracle=0.776) | ⚠️ .776 vs .775 | 仅 Tab selection |\n| Tab selection: Greedy 0.645±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (greedy=0.644) | ⚠️ .644 vs .645 | ❌ 见问题 #5 |\n| Tab selection: LP 0.647±0.005 | LP selection F1 | exp_016_rerun_1024_bootstrap | ⚠️ 间接 | 仅 Tab selection |\n| Tab selection: LP p=.29 | \"LP achieves $+0.2$\\,pp ($p{=}0.29$)\" | exp_016_rerun_1024_bootstrap (permutation_p=0.39) | ❌ 见问题 #6 | Tab vs text 一致 (.29) |\n| ρ up to 0.38 | \"Despite $\\rho$ up to 0.38\" | exp_012_rerun_1024 (vc_rho=0.3792) | ✅ .379→.38 | = Tab quality_estimation VC ρ=.379 |\n| +13.0 pp headroom | \"the oracle shows 13.0\\,pp headroom\" | Tab selection: 0.775-0.645=0.130=13.0pp | ✅ | = fig_selection_gap caption \"+13.0pp\" ✅ |\n| MDE ≈1.5 pp | \"below MDE (${\\approx}$1.5\\,pp at $n{=}529$, 2--3 seeds\" | ⚠️ UNTRACED (统计计算) | — | = limitations ✅ |\n| LP +1.39 pp (Few-NERD) | \"LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, k=21)\" | exp_021_fewnerd_full (1.36 for seed42) | ⚠️ 见问题 #2 | = Tab fewnerd; Intro |\n| p_adj=0.021, k=21 | selection family correction | provenance C143 has p_adj=0.019 k=19 | ⚠️ 见问题 #7 | 仅出现一次 |\n| p_adj=0.055 (global k=57) | footnote | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations |\n| 13.0% degeneracy (Few-NERD) | \"low degeneracy (13.0\\%)\" | 见问题 #8 | ⚠️ | = Tab fewnerd 13.0% |\n| 12.2% (SciERC) | \"SciERC 12.2\\%\" | exp_012_rerun_1024 (degen=0.1777?) | ⚠️ 见问题 #9 | = Tab fewnerd 12.2% ✅ |\n| 61.7% (CoNLL) | \"CoNLL 61.7\\%\" | ⚠️ UNTRACED | — | = Tab fewnerd 61.7% ✅ |\n| VC −1.79, SJ −2.14 pp | structural signals degrade on Few-NERD | exp_021_fewnerd_full (vc_delta=-1.79, sj_delta=-2.14) | ✅ | = §4.3 一致 |\n| ρ=0.052, n=23, p=0.81 | degeneracy-LP across configs | ⚠️ UNTRACED | — | = §4.3 Fig degeneracy_scatter ✅ |\n| ρ=−0.881 | within-dataset degen-LP | ⚠️ UNTRACED | — | = §4.3 ✅ |\n| MRSC −3.1 pp | multi-round refinement | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| LSC −3.5 pp | latent centroid selection | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |\n| ESJ AUROC 0.50–0.55 (Qwen3-8B) | cross-model ESJ | exp_esj_qwen3_all (scierc=0.512, fewnerd=0.495) | ✅ | 仅出现一次 |\n\n## §4.2–4.3 Experiments (experiments_main.tex)\n\n### Tab quality_estimation\n\n| 数字 | 来源 exp_id | 验证 |\n|------|------------|------|\n| SciERC VC ρ=.379 | exp_012_rerun_1024 (voting_conf rho=0.3792) | ✅ |\n| SciERC SJ ρ=.360 | exp_012_rerun_1024 (SJ rho=0.3599) | ✅ |\n| SciERC FK ρ=.267 | exp_012_rerun_1024 (FK rho=0.2665) | ✅ |\n| SciERC EM ρ=.295 | exp_012_rerun_1024 (EM rho=0.2945) | ✅ |\n| SciERC LP ρ=.205 | exp_012_rerun_1024 (LP rho=0.2052) | ✅ |\n| SciERC VC AUC=.684 | exp_012_rerun_1024 (voting_conf AUROC=0.6841) | ✅ |\n| SciERC SJ AUC=.692 | exp_012_rerun_1024 (SJ AUROC=0.6917) | ✅ |\n| SciERC FK AUC=.629 | exp_012_rerun_1024 (FK AUROC=0.629) | ✅ |\n| **SciERC EM AUC=.631** | **exp_012_rerun_1024 (EM AUROC=0.7493)** | **❌ 见问题 #10** |\n| SciERC LP AUC=.578 | exp_012_rerun_1024 (LP AUROC=0.5783) | ✅ |\n| CoNLL Qwen EM ρ=.451 | exp_002 (em_rho_full=0.4507) | ✅ |\n| CoNLL Qwen EM AUC=.816 | exp_002 (em_auroc_full=0.8156) | ✅ |\n| CoNLL Qwen SJ ρ=.436 | exp_002 (sj_rho_full=0.4357) | ✅ |\n| CoNLL LLaMA SJ ρ=.431 | exp_017_llama_conll_infer (SJ_rho=0.4314) | ✅ |\n| CoNLL LLaMA LP AUC=.761 | exp_017_llama_conll_infer (logprob_AUROC=0.761) | ✅ |\n\n### Tab fewnerd (cross-dataset LP selection)\n\n| 数字 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|------------|------|-----------|\n| WNUT n=1,287 | exp_003_wnut17_eval (n=1287) | ✅ | = §4.2 |\n| WNUT Greedy .452 | exp_wnut17_qwen25_7b (seed42 greedy=0.4524) | ✅ | — |\n| WNUT Degen 67.9% | ⚠️ UNTRACED (N=8 data; registry WNUT experiments are N=16) | — | = text 12–68% upper bound |\n| WNUT LP ρ=−.446 | ⚠️ UNTRACED (registry has −.414/−.409 at N=16) | — | — |\n| CoNLL n=2,756 | consistent | ✅ | = §3 |\n| CoNLL Greedy .908 | ⚠️ UNTRACED for N=8 Qwen | — | — |\n| CoNLL Degen 61.7% | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| CoNLL LP ρ=.302 | ⚠️ ≠ Tab quality_estimation LP ρ=.316 | ⚠️ 见问题 #11 | — |\n| **SciERC Greedy .663** | **exp_scierc_n8_s* (greedy ≈0.661–0.666)** | ✅ matches multi-seed | **❌ ≠ Tab selection Greedy .645 见问题 #5** |\n| SciERC Degen 12.2% | ⚠️ PARTIALLY TRACED | — | = §4.1 ✅ |\n| **SciERC LP ρ=.159** | ⚠️ UNTRACED | — | **❌ ≠ Tab quality_estimation LP ρ=.205 见问题 #11** |\n| **SciERC LP Δ=+0.61 pp** | ⚠️ UNTRACED | — | **❌ ≠ §4.1 text \"+0.2pp\" 见问题 #5** |\n| Few-NERD n=32,565 | exp_021_fewnerd_full (filtered=32565) | ✅ | — |\n| Few-NERD Greedy .748 | exp_021_fewnerd_full (greedy=0.7478) | ✅ | — |\n| Few-NERD Degen 13.0% | ⚠️ 见问题 #8 | — | = §4.1 ✅ |\n| Few-NERD LP ρ=.220 | ⚠️ ≠ exp_021 lp_global_rho=0.4215 | ⚠️ 见问题 #12 | — |\n| Few-NERD LP Δ=+1.39 pp | exp_021_fewnerd_full (1.36 seed42) | ⚠️ 见问题 #2 | = §4.1; Intro |\n\n### Other §4 numbers\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| SciERC 551 instances, 6 types | §4.2 setup | ✅ 标准 | ✅ | = §3 n=529 (gold-filtered) consistent |\n| Few-NERD 37,648 instances, 8 types | §4.2 setup | exp_021 (instance_count=37648) | ✅ | — |\n| CoNLL 3,453 instances, 4 types | §4.2 setup | ✅ 标准 | ✅ | — |\n| WNUT-17 1,287 instances, 53.7% zero F1 | §4.2 setup | exp_003_wnut17_eval (53.7%) | ✅ | — |\n| SJ>LP Δρ=+0.151±0.006 | §4.2 QE results | ⚠️ UNTRACED (bootstrap) | — | 仅出现一次 |\n| p_adj=0.013 (k=5) | seed-replication SJ>LP | ⚠️ UNTRACED | — | 仅出现一次 |\n| CoNLL EM ρ=0.816 (AUROC) | §4.2 \"EM leads both ρ and AUROC ($0.816$)\" | exp_002 (em_auroc=0.8156) | ✅ | = Tab quality_estimation |\n| WNUT VC ρ=0.724 at N=16 | §4.2 | exp_003 系列 | ⚠️ UNTRACED | 仅出现一次 |\n| WNUT conditional ρ=0.038 | §4.2 | ⚠️ UNTRACED | — | 仅出现一次 |\n| LP conditional ρ=0.350 | §4.2 WNUT | exp_003_wnut17_eval (rho_logprob_cond=0.35) | ✅ | 仅出现一次 |\n| LP σ=0.04 vs SJ 2.02 pp | §4.3 seed stability | ⚠️ UNTRACED | — | 仅出现一次 |\n| 50× more seed-stable | 2.02/0.04=50.5≈50 | ✅ 算术一致 | — | 仅出现一次 |\n| ρ=0.90, p=0.002 (MV vs low-F1 types) | §4.3 | ⚠️ UNTRACED (appendix pertype) | — | 仅出现一次 |\n| MV −2.71 pp (Few-NERD) | §4.3 | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen3-4B |Δρ|=0.042 | §4.4 robustness | ⚠️ UNTRACED | — | 仅出现一次 |\n| +1.40±0.51 pp (construction) | §4.5 | exp_entity_construction | ⚠️ 见问题 #1 | = Abstract; Intro |\n| +0.32 pp SciERC (n.s.) | §4.5 | ⚠️ 见问题 #13 | — | 仅出现一次 |\n| −0.39 pp CoNLL | §4.5 | exp_entity_construction (conll cv_uniform='-0.39pp') | ✅ | 仅出现一次 |\n| D=13%, headroom=12.4 pp | §4.5 Few-NERD | exp_021 (headroom=0.124=12.4pp) | ✅ | — |\n| p_adj=0.006 (k=10) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro |\n| p_adj=0.055 (k=57) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro; limitations |\n| ρ_adj=0.516 | §4.5 construction-selection correlation | ⚠️ UNTRACED | — | 仅出现一次 |\n| 5-epoch: +1.39→+0.12 pp (selection) | §4.5 epoch confound | exp_fewnerd_5epoch_lp_s42 (lp_delta=0.12) | ✅ (5-epoch end) | — |\n| **5-epoch: +0.88→+0.20 pp (construction)** | §4.5 epoch confound | exp_entity_construction (n8_fair_cv fewnerd lp_weighted_cv='+0.88pp') | ⚠️ 见问题 #1 | — |\n| 9%→26% degeneracy | §4.5 epoch confound | 见问题 #4 | ⚠️ | — |\n\n## §4.4 Adaptive Methods\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| +0.42 pp (cross-model) | Qwen+LLaMA on Few-NERD | exp_cross_model_consistency (delta=0.42, p=0, CI=[0.27,0.58]) | ✅ | = Tab method_summary |\n| CI [0.27, 0.58] | cross-model CI | exp_cross_model_consistency | ✅ | 仅出现一次 |\n| AUC=0.923±0.002 | LightGBM verifier | exp_b2_entity_verifier (oof_auc=0.9233) | ✅ | = Tab method_summary |\n| +0.30 pp (verifier) | LightGBM F1 gain | exp_b2_entity_verifier (oof_delta_pp=0.3) | ✅ | = Tab method_summary |\n| −0.76 to −1.02 pp | verifier cross-dataset transfer | ⚠️ UNTRACED (appendix verifier_transfer) | — | 仅出现一次 |\n| ESJ AUROC 0.51 | Tab method_summary | exp_esj_qwen3_all (esj_auroc=0.512) | ✅ | = §4.1 |\n| MRSC −3.1 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| LSC −3.5 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |\n| DALS +0.71 pp (SciERC) | Tab method_summary | ⚠️ UNTRACED | — | 仅出现一次 |\n| −0.4 to −3.1 pp | Sup. combination LR/MLP/RF | ⚠️ 见问题 #14 | — | 仅出现一次 |\n\n## §Theoretical Analysis (theoretical.tex)\n\n| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |\n|------|--------|------|------|-----------|\n| G_nd≈14.8 pp | \"with $G_{\\textup{nd}}{\\approx}14.8$\\,pp\" | ⚠️ UNTRACED (理论计算) | — | 仅出现一次 |\n| α≈0.068 | \"$\\alpha{\\approx}0.068$\" | ⚠️ UNTRACED | — | = fig_bound caption |\n| θ_crit=0.70 | \"$\\theta_{\\textup{crit}}{=}0.70$\" | ✅ 算术验证: (1-0.70)×14.8×0.068=0.302≈0.3pp | = theory.tex θ_crit∈[0.60,0.80] 一致 |\n| 3–12% | recovery ratio | ⚠️ UNTRACED | — | = Intro; theory.tex ✅ |\n\n## §Threshold Regime Analysis (theory.tex)\n\n| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |\n|------|--------|------------|------|-----------|\n| R²>0.999 | oracle scaling fit | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.61 (Few-NERD) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| c≈0.35 (SciERC) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |\n| 8B→14B: +1.2 pp oracle, +0.9 pp greedy | scale ablation | ⚠️ UNTRACED | — | 仅出现一次 |\n| GPT-5.5: 50% degen | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (degen=0.5) | ✅ | 仅出现一次 |\n| GPT-5.5: SJ ρ=0.346 | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (sj_rho=0.3461) | ✅ | 仅出现一次 |\n| GPT-5.5: MV +1.4 pp | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2: mv-greedy=0.6521-0.6382=0.0139=1.39pp→1.4 | ✅ | 仅出现一次 |\n| GPT-5.5: 6.8 pp unrealized | frontier SC | oracle-mv=0.7203-0.6521=0.0682=6.82pp→6.8 | ✅ | 仅出现一次 |\n| 10.1% empty entity sets | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 88% gold-empty | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| 1.2% true parse failures (19/1600) | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |\n| Qwen2.5: 31.7–46.2% | cross-scale degen | ⚠️ UNTRACED | — | 仅出现一次 |\n| 40 of 58 transitions (p<0.05) | inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| θ=2/N: −3.09 pp (N=8), −6.90 pp (N=16) | inverse scaling severity | ⚠️ UNTRACED | — | 仅出现一次 |\n| MV: −0.87/−0.60 pp | MV inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |\n| OR=0.109 (11.1% vs 1.3%) | degen vs inverse scaling | ⚠️ UNTRACED; 算术近似验证: (1.3/98.7)/(11.1/88.9)=0.1055≈0.109 | — | 仅出现一次 |\n| CoNLL SJ ρ .30→.44 | few-shot improvement | ⚠️ UNTRACED | — | 仅出现一次 |\n| α=0.000–0.121 | binding constraint | ⚠️ UNTRACED | — | = §4.1 ✅ |\n| 8–33× tighter | α vs D | ⚠️ UNTRACED | — | = Intro; Discussion ✅ |\n| split-half r=0.395–0.578 | FK independence | ⚠️ UNTRACED | — | 仅出现一次 |\n| bound ratio 0.13–0.63 | signal-adjusted bound | ⚠️ UNTRACED | — | 仅出现一次 |\n| α_crit,eff=1.148 (CoNLL) | MV impossibility | ⚠️ UNTRACED | — | 仅出现一次 |\n\n## §5 Discussion\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 12–68% | degeneracy range | ✅ | = Intro; §4.5 ✅ |\n| α→0 | signal alignment collapse | ✅ | 全文一致 |\n| 8–33× tighter | α vs D | ✅ | = Intro; theory.tex ✅ |\n| >50% | high degeneracy threshold | ✅ | 全文一致 |\n\n## Limitations\n\n| 数字 | 上下文 | 验证 | 跨位置一致 |\n|------|--------|------|-----------|\n| 5.5–74% | frontier degeneracy | exp_frontier_sc_deepseek (5.5%), exp_frontier_sc_claude_sonnet4 (74%) | ✅ | 仅出现一次 |\n| p_adj=0.055 | strongest construction claim | ✅ | = Abstract; §4.5 ✅ |\n| MDE≈1.5 pp | statistical power | ✅ | = §4.1 ✅ |\n| RE n=397, SQL n=196 | cross-task sample sizes | exp_spider_sc_pilot (n=196) | ✅ SQL; RE ⚠️ UNTRACED | — |\n| +1–1.4 pp | construction gain range | ✅ 与 §4.5 一致 | — |\n\n---\n\n## 关键数字重点检查\n\n### 1. SciERC EM AUROC = .631（不是 .749）\n- **Tab quality_estimation: .631** ✅ 论文正确\n- **Registry exp_012_rerun_1024: EM AUROC = 0.7493** ❌ Registry 与论文不一致\n- **Provenance c002: \"EM leads AUROC (NER 0.749)\"** ❌ Provenance STALE\n- **结论**: 论文已正确修改为 .631，但 registry 和 provenance 仍保留旧值 .749。**paper_provenance.yaml 需要更新。**\n\n### 2. Headroom = 13.0pp（不是 11.4pp）\n- Tab selection: Oracle 0.775 − Greedy 0.645 = 0.130 = **13.0pp** ✅\n- fig_selection_gap caption: **+13.0pp** ✅\n- 全文无 11.4pp 出现。**PASS。**\n\n### 3. MV = +0.6pp（不是 +0.61pp）\n- Intro: \"MV $+0.6$\\,pp on CoNLL\" ✅\n- Fig n_scaling caption: \"+0.6pp at N=64\" ✅\n- §4.3 text: \"+0.6pp\" ✅\n- Registry exp_conll_n64_s42: mv_delta = 0.64pp → 0.6 (1dp rounded) ✅\n- 全文无 +0.61pp 出现（Tab fewnerd SciERC LP Δ = +0.61pp 是 LP 不是 MV）。**PASS。**\n\n### 4. α = 0.121\n- §4.1: \"$\\alpha$ approaches zero ($0.000$--$0.121$)\" ✅\n- theory.tex: \"$\\alpha{=}0.000$--$0.121$\" ✅\n- 上限一致。**PASS。**\n\n### 5. SciERC construction = +0.32pp n.s.\n- §4.5: \"a non-significant $+0.32$\\,pp on SciERC\" ✅ 论文内一致\n- **Registry discrepancy**: exp_entity_construction 显示 SciERC n8_fair_cv 多个变体均 >+1pp（见问题 #13）\n- **结论**: 论文内一致，但 registry 来源不清楚。可能来自不同配置或后续重算。\n\n### 6. Holm p_adj = 0.055 (global k=57) vs p_adj = 0.013 (seed-replication k=5)\n- **p_adj=0.055 (k=57)**: Abstract, Intro, §4.5, limitations — 全部一致 ✅\n- **p_adj=0.013 (k=5)**: §4.2 \"SJ>LP advantage reaches $p_{\\text{adj}}{=}0.013$\" — 这是信号比较的 seed-replication correction ✅\n- 两者是不同统计框架，论文正确区分了。**PASS。**\n\n### 7. fig_selection_gap caption Oracle = +13.0pp（不是 +13.1pp）\n- Caption: \"oracle headroom ($+13.0$\\,pp)\" ✅\n- Tab selection: 0.775 − 0.645 = 0.130 = 13.0pp ✅\n- 全文无 13.1pp 出现。**PASS。**\n\n---\n\n## 问题清单\n\n按严重程度排序：\n\n### 🔴 严重 (Cross-table inconsistency)\n\n**#5. SciERC 基线在两个表格间不一致**\n- Tab selection (§4.1): Greedy = 0.645±0.001, LP Δ = +0.2pp (p=0.29)\n- Tab fewnerd (§4.3): Greedy = 0.663, LP Δ = +0.61pp (p=0.193)\n- 两表均标注 \"SciERC, Qwen3-8B, N=8, T=1.0\"\n- **差异**: Greedy F1 差 1.8pp; LP Δ 差 0.41pp\n- **可能原因**: 不同训练种子 / 不同 model checkpoint（exp_016 系列 vs exp_scierc_n8_s* 系列），但论文未说明\n- **影响**: 读者会困惑为何同一设置有不同基线\n\n**#10. SciERC EM AUROC: 论文 .631 vs Registry .7493**\n- Tab quality_estimation 显示 .631\n- exp_012_rerun_1024 registry 显示 EM AUROC = 0.7493\n- Provenance c002 仍记录 0.749\n- **状态**: 论文值 .631 被指定为正确值（任务说明），但 **registry 和 provenance 从未更新**\n- **影响**: 后续引用 provenance 的操作会得到错误数据\n\n**#11. SciERC/CoNLL LP ρ 在 Tab quality_estimation vs Tab fewnerd 间不一致**\n- SciERC LP ρ: Tab quality_estimation = .205; Tab fewnerd = .159 (差 0.046)\n- CoNLL LP ρ: Tab quality_estimation = .316; Tab fewnerd = .302 (差 0.014)\n- Tab quality_estimation 是 primary seed=42; Tab fewnerd 是 3-seed mean\n- **差异可能合理**（不同种子均值），但未在文中说明\n\n### 🟡 中等 (Traceability / consistency concern)\n\n**#1. Construction +1.40pp vs +0.88pp 同一方法不同数字**\n- §4.5 主结果: LP-weighted construction = +1.40±0.51pp (4-seed mean, full test)\n- §4.5 epoch confound: \"construction: +0.88→+0.20pp\"\n- Registry: n8_fair_cv fewnerd LP-weighted CV = +0.88pp\n- **分析**: +1.40 是 4-seed non-CV; +0.88 是 5-fold CV。两种评估方法给出不同结果。论文在同一段落交替使用两种评估方法而未说明\n- **影响**: 读者可能误以为 3-epoch construction gain = +0.88pp 而非 +1.40pp\n\n**#2. LP selection +1.39pp: 主种子显示 1.36pp**\n- 论文: +1.39pp (标注 3-seed mean)\n- Registry exp_021_fewnerd_full (seed42): lp_selection_delta_pp = 1.36\n- 其他种子 LP delta 未在 registry summary 中找到\n- **影响**: 无法从 registry 直接验证 1.39 是否为正确的 3-seed mean\n\n**#6. Tab selection LP p-value: 论文 .29 vs Registry .39**\n- Tab selection: LP p=.29\n- exp_016_rerun_1024_bootstrap: permutation_p = 0.39\n- **可能原因**: Tab selection 可能用 paired bootstrap（2-seed），exp_016 用 permutation test；或来自不同实验版本\n- **影响**: p-value 不同但结论相同（均不显著）\n\n**#7. Holm p_adj: 论文 0.021 (k=21) vs Provenance 0.019 (k=19)**\n- §4.1 footnote: \"Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$\"\n- Provenance C143: \"p_adj=0.019 k=19\"\n- **分析**: 家族大小从 19 增至 21（加入更多比较），p_adj 相应增大。Provenance stale。\n- **影响**: 数值轻微差异，结论不变\n\n**#8. Few-NERD degeneracy 13.0%: 主种子 registry 显示 10.1%**\n- Tab fewnerd: 13.0% (标注 3-seed mean)\n- exp_021_fewnerd_full (seed42): degeneracy_rate = 0.101 (10.1%)\n- exp_021_fewnerd_n8_seed123: degen_rate = 0.1312 (13.1%)\n- exp_021_fewnerd_n8_seed456: degen_rate = 0.1212 (12.1%)\n- 3-seed mean: (10.1+13.1+12.1)/3 = 11.8%, not 13.0%\n- **可能原因**: seed42 的 0.101 可能不是 constant-F1 degeneracy（seed123/456 标注为 unified_metrics_constant_f1_gold_filtered，seed42 未标注）\n- **影响**: 无法确认 13.0% 的准确性\n\n**#3. RE 40% zero-F1: Registry 显示 44.3%**\n- 论文多处: \"40% zero-F1\"\n- Provenance c006: \"44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\"\n- 40% 的具体来源实验不在 registry summary 中\n- **影响**: 轻微，但 40 vs 44.3 的差异未解释\n\n**#9. SciERC degeneracy 12.2%: Registry exp_012 显示 17.77%**\n- Tab fewnerd: SciERC Degen.% = 12.2%\n- exp_012_rerun_1024: degen_rate = 0.1777 (17.77%)\n- exp_scierc_n8_s123: degeneracy_rate = 0.116 (11.6%)\n- exp_scierc_n8_s456: degeneracy_rate = 0.12 (12.0%)\n- **分析**: 12.2% 可能来自 s123/s456 的均值而非 exp_012，或 exp_012 的 17.77% 是不同度量\n- **影响**: 来源不清楚\n\n**#12. Few-NERD LP ρ=.220 in Tab fewnerd vs .4215 in Registry**\n- Tab fewnerd: LP ρ = .220\n- exp_021_fewnerd_full: lp_global_rho = 0.4215\n- 差异 2x，即使是 3-seed mean 也不太可能降到 .220\n- **可能原因**: Tab fewnerd 的 LP ρ 可能不是 global cross-instance ρ，而是某种 within-instance 或 conditional 度量\n- **影响**: 如果是不同度量，需要在表格或 caption 中注明\n\n**#13. SciERC construction +0.32pp vs Registry +1.12~+1.67pp**\n- 论文: \"+0.32pp on SciERC (non-significant)\"\n- Registry exp_entity_construction: SciERC n8_fair_cv 多个变体 = +1.12 to +1.67pp\n- **可能原因**: 不同 θ、不同评估方法、不同种子集\n- **影响**: 无法从 registry 追溯 +0.32pp 的来源\n\n**#14. Supervised combination \"-0.4 to -3.1pp\"**\n- Tab method_summary: \"LR/MLP/RF: −0.4 to −3.1pp\"\n- Registry exp_backup3_distill_verifier: per-fold deltas 最大 = −0.34pp\n- −3.1pp 在 registry 中找不到对应\n- **可能原因**: −3.1pp 可能来自另一个实验或特定配置\n- **影响**: 范围上界无法追溯\n\n### 🟢 轻微 (Rounding / precision)\n\n**#4. Degeneracy type mixing in epoch comparison**\n- §4.5: \"degeneracy rises from 9% to 26%\" — entity-set exact-match\n- 主表 (Tab fewnerd): 13.0% — constant-F1\n- 脚注已解释两种度量，但正文在不同位置使用不同度量未明确标注\n\n**\"LP-best +1.4pp\" 精度模糊**\n- §4.3: \"LP-best $+1.4$\\,pp on Few-NERD\" — 可能是 selection (+1.39→1.4) 或 construction (+1.40)\n- 建议明确是哪种方法\n\n**AUROC rounding**\n- Abstract/Intro: \"AUROC up to 0.82\" — 来自 .816 (2dp rounding)\n- 技术上正确但比表格精度低\n\n---\n\n## 精度一致性\n\n| 类别 | 精度 | 评估 |\n|------|------|------|\n| 表格 ρ 值 | 3 位小数 (.379, .360) | ✅ 表内一致 |\n| 正文 ρ 引用 | 2 位小数 (.38, .45) | ✅ 合理简化 |\n| pp 增益 | 1-2 位小数 (+1.39, +0.6, +0.2) | ⚠️ +0.6 vs +1.39 精度不统一 |\n| 百分比 (degeneracy) | 1 位小数 (12.2%, 13.0%) | ✅ 一致 |\n| p-values | 表格 2 位 (.29, .67); 正文混合 | ✅ 大致一致 |\n| AUROC | 表格 3 位 (.631, .816); 正文 2 位 (.82) | ⚠️ 正文与表格精度不同但可接受 |\n\n总体精度一致性：**合格**，无系统性精度不一致问题。\n\n---\n\n## 总结\n\n- **已验证数字**: ~60% 可追溯到 registry 实验或算术验证\n- **UNTRACED**: ~25% 来自 appendix 实验或统计计算，无法从 registry summary 直接验证\n- **发现问题**: 14 个，其中 3 个严重（跨表不一致）、11 个中等或轻微\n- **7 个 bug-prone 数字**: 论文中全部正确 ✅，但 registry/provenance 有 2 处 stale 数据\n\n**最需要关注的问题**:\n1. Tab selection vs Tab fewnerd SciERC 基线不一致 (问题 #5)\n2. Registry EM AUROC stale (问题 #10) — 需更新 registry 和 provenance\n3. Construction +1.40 vs +0.88 评估方法混用 (问题 #1)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01HPMoGJy6797i7RZYkVp6CC`</summary>

```json
{
  "name": "audit_maintext_numbers",
  "type": "report",
  "description": "主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。",
  "project": "struct_self_consist_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/audit_maintext_numbers.md",
  "tags": [
    "audit",
    "paper",
    "numbers",
    "consistency"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "f72b75c5-44bb-4448-899b-018555b75797",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAvzBSR68PMnWxcKnvYQiF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15762,
      "cache_read_input_tokens": 110477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15762
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-24T04:44:46.749Z_

<details><summary>↩ Tool result · `toolu_01HPMoGJy6797i7RZYkVp6CC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_2206ff\", \"name\": \"audit_maintext_numbers\", \"type\": \"report\", \"description\": \"主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/audit_maintext_numbers.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T04:44:46.081214+00:00\", \"tags\": [\"audit\", \"paper\", \"numbers\", \"consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "11fd8547-e880-4089-a441-cb7cb7a1c026",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260524_2206ff\\\", \\\"name\\\": \\\"audit_maintext_numbers\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。\\\", \\\"path\\\": \\\"projects/struct_self_consist_ie/artifacts/_project/report/audit_maintext_numbers.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"struct_self_consist_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-24T04:44:46.081214+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"paper\\\", \\\"numbers\\\", \\\"consistency\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_2206ff\", \"name\": \"audit_maintext_numbers\", \"type\": \"report\", \"description\": \"主文定量数字全面审计：检查每个数字的可追溯性、跨位置一致性、精度一致性。发现14个问题，3个严重（跨表不一致），7个bug-prone数字论文内全部正确。\", \"path\": \"projects/struct_self_consist_ie/artifacts/_project/report/audit_maintext_numbers.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T04:44:46.081214+00:00\", \"tags\": [\"audit\", \"paper\", \"numbers\", \"consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 71_

审计完成。发现 14 个问题：

**3 个严重问题（跨表不一致）：**
- **#5**: Tab selection vs Tab fewnerd SciERC 基线不一致（Greedy .645 vs .663，LP Δ +0.2pp vs +0.61pp）— 同一设置两个表不同数字
- **#10**: SciERC EM AUROC 论文 .631 vs registry .7493 — registry 和 provenance 从未更新
- **#11**: LP ρ 在两个表间不一致（SciERC .205 vs .159）

**主要中等问题：**
- Construction +1.40pp (4-seed non-CV) vs +0.88pp (5-fold CV) 在同一段落混用未说明
- LP selection +1.39pp 主种子 registry 显示 1.36pp
- 多个数字无法从 registry 追溯（appendix 来源或统计计算）

**7 个 bug-prone 数字全部正确** ✅（.631 不是 .749、13.0pp 不是 11.4pp、+0.6pp 不是 +0.61pp 等）

报告已写入 `artifacts/audit_maintext_numbers.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "uuid": "d76ab783-4acb-4b0b-a542-bedbdd17660c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Asaxuv5rhdWgHMCy8aR4jT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 126239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 599
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 72_

审计完成。发现 14 个问题：

**3 个严重问题（跨表不一致）：**
- **#5**: Tab selection vs Tab fewnerd SciERC 基线不一致（Greedy .645 vs .663，LP Δ +0.2pp vs +0.61pp）— 同一设置两个表不同数字
- **#10**: SciERC EM AUROC 论文 .631 vs registry .7493 — registry 和 provenance 从未更新
- **#11**: LP ρ 在两个表间不一致（SciERC .205 vs .159）

**主要中等问题：**
- Construction +1.40pp (4-seed non-CV) vs +0.88pp (5-fold CV) 在同一段落混用未说明
- LP selection +1.39pp 主种子 registry 显示 1.36pp
- 多个数字无法从 registry 追溯（appendix 来源或统计计算）

**7 个 bug-prone 数字全部正确** ✅（.631 不是 .749、13.0pp 不是 11.4pp、+0.6pp 不是 +0.61pp 等）

报告已写入 `artifacts/audit_maintext_numbers.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1009532,
  "duration_api_ms": 1007996,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "be935652-fa4e-4214-8762-c7316ebe5e2f",
  "total_cost_usd": 2.2813822499999996,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 114997,
    "cache_read_input_tokens": 653774,
    "output_tokens": 49357,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114997,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 354,
        "cache_read_input_tokens": 126239,
        "cache_creation_input_tokens": 599,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 599
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1679,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001764,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 49357,
      "cacheReadInputTokens": 653774,
      "cacheCreationInputTokens": 114997,
      "webSearchRequests": 0,
      "costUSD": 2.27961825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "58505856-9386-4a6f-95dd-5995029a80b6"
}
```

</details>

---
