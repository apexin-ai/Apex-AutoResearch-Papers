# code data audit experiments tables — Part 1 of 2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[Transcript overview](../code-data-audit-experiments-tables.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/73/73729c7de1d1b74e2e89.json)

## Before a recorded user message

## Before a recorded user message

673 recorded events


### Tool call

_source line 1 · 2026-05-23T19:54:33.792500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2 · 2026-05-23T19:54:33.794922+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: ${\sim}$29\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift
…[truncated 10400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 3 · 2026-05-23T19:54:33.800387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 4 · 2026-05-23T19:54:33.800729+00:00_

1	\enlargethispage{14\baselineskip}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\subsection{Temporal DIF as Structured Signal}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design (``temporal'' denotes release-year cohorts that differ simultaneously in architecture, data, and methodology; \Cref{sec:cohorts}). Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
10	
11	\looseness=-1
12	Composition downsampling ($\Delta = 1.08$\,pp), base-only, and instruct-only temporal analyses independently confirm DIF is not an artifact of cohort structure (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}).
13	
14	\looseness=-2
15	Three features distinguish LLM temporal DIF from educational settings: (1)~C\% (29.2\%; cluster bootstrap CI: $[26.7\%, 53.2\%]$) substantially exceeds typical educational DIF rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$), unlike educational settings where DIF correlates with construct-irrelevant variance; (3)~the near-independence admits two interpretations: DIF captures a broader signal---including capability evolution and training methodology shifts---of which contamination is one component, or DIF and contamination detection measure distinct constructs. The base/instruct reversal (OR $= 4.75$; \Cref{app:mechanism_discussion}) favors the former; either interpretation supports periodic DIF audits.
16	
17	\subsection{Recommended DIF Audit 
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 5 · 2026-05-23T19:54:33.800923+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | head -80",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | head -80",
    "description": "List artifacts directory"
  }
}
```

</details>

---


### Tool result

_source line 6 · 2026-05-23T19:54:33.801077+00:00_

__pycache__
_project
arr_checklist_draft.md
artifacts_qc_report.md
build_response_matrix.py
data_audit_part1.md
deff_parametric_curve
dif_diagnostic.py
dif_diagnostic_output.log
dif_diagnostic_pvalue_dist.pdf
dif_diagnostic_tpr_comparison.csv
dif_phase2_param_distribution.pdf
dif_phase2_power_curves.pdf
dif_phase2_results.csv
dif_phase2_simulation.py
dif_power_curves.pdf
dif_power_results.csv
dif_power_simulation.py
difficulty_modeltype_interaction
dream_reports
experiment_summary.md
irt_scale_analysis.json
irt_scale_analysis.md
item_metadata.csv
k3_power_simulation
literature_survey_d011.md
lofo_robustness
manifest.yaml
metabench_cohort_analysis.csv
metabench_ctt_stats.csv
metabench_data
metabench_data_summary.md
metabench_explore.py
metabench_model_accuracy.csv
metabench_model_list.txt
metabench_rl_models.csv
metabench_subject_stats.csv
metabench_summary.json
mf1_lofo_power_calibration
mf1_worked_examples
mf2_deff_estimation
mf2_practical_significance
mf2_rho_degradation
mixed_mechanism_semisynthetic
mmlu_cf_analysis.json
mmlu_cf_analysis.md
mmlu_li2024_proxy_labels.csv
mmlu_redux
model_metadata.csv
mvp_dif_power_sim
novelty_rebuttal_draft.md
plan_001
plan_001_real_data_dif_mmlu
plan_001b
plan_004
plan_004_data_availability.md
plan_010
plan_011
plan_011_semi_synthetic_validation
plan_012
plan_012_irt_theta_conditioning
plan_013
plan_013_q3_local_independence
plan_013_supplement
plan_014
plan_015
plan_016
plan_016_supplement
plan_016_within_subject_semi_synthetic
plan_017
plan_017_supplement
plan_018
plan_019
plan_020
plan_021
plan_022
plan_023
plan_024
plan_026
plan_027_temporal_overlap

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 7 · 2026-05-23T19:54:33.801227+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | tail -40",
  "description": "List remaining artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | tail -40",
    "description": "List remaining artifacts"
  }
}
```

</details>

---


### Tool result

_source line 8 · 2026-05-23T19:54:33.801362+00:00_

r18_base_instruct_survey
r18_base_vs_instruct_dif
r18_dedup_k_curve
r18_icc_by_family_size
r18_rank_bucket_reversal
r18_restricted_range_rho
r19_model_size_dif
r19_open_closed_dif
r19_semisynthetic_gradient
r19_temporal_granularity
r20_size_stratified_deff
r22_composition_control
r22_deff_simulation
r22_within_arch_temporal
rebuttal_talking_points.md
ref_audit_report.md
response_letter_draft.md
response_matrix.npz
response_matrix_index.npz
review_issues.yaml
review_reports
review_round_10
review_round_11
review_round_12
review_round_13
review_round_14
review_round_15
review_round_16
review_round_17
review_round_18
review_round_4
review_round_5
review_round_6
review_round_7
review_round_8
review_round_9
score_inflation_analysis
sf1_cluster_bootstrap
sf8_power_sensitivity
temporal_accumulation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-23T19:54:33.801529+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Audit Table 1 + Table 2",
  "prompt": "You are auditing data correctness in an academic paper. Your job is to verify every cell value in Table 1 (tab:temporal_landscape) and Table 2 (tab:structural_comparison) from experiments.tex against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\n## Table 1 (tab:temporal_landscape) — line 24-42 of experiments.tex\nContent:\n```\nCohort Definition & N_ref / N_focal & C% & C% (web-clean) & Enrich.\nTemporal (2023 vs 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964\nAbility quintile (Q1-2 vs Q4-5) & ~2,600 / ~2,600 & 2.9 & 0.027 & 1.19\nWithin-family (Llama-2 vs 3) & 161 / 308 & 61.3 & -- & --\nRandom split 2023 (sanity) & 540 / 540 & 0.62 & -- & --\nRandom split 2024 (sanity) & ~400 / ~400 & 1.3 & -- & --\nWithin-subject (avg, 5 subj.) & varies & 38.1 & -- & --\n```\n\n## Table 2 (tab:structural_comparison) — line 62-78 of experiments.tex\nContent:\n```\nApproach & Mechanism & Temp C% & TPR (p=0.5) & Outcome\nBaseline (ext.) & Cross-bench total score & 0.314±.009 & 0.834±.027 & Reference\nMatched-ability & Within-quintile temp DIF & ~0.31 & -- & Enrich 0.94-1.04\nθ-cond (sens.) & θ replaces total score & 0.312 & 0.876 & r(θ,total)=0.9986\nWithin-subject & Per-subject DIF & -- & -- & C%=38.1% (>25%)\n```\n\n## Known data sources to check:\n- Temporal DIF: artifacts/plan_001/ or artifacts/plan_001_real_data_dif_mmlu/\n- Random splits / permutation: artifacts/plan_029_permutation_null/\n- Within-family: may be in plan_001 or other plan dirs\n- Ability quintile: check plan_001 or other dirs\n- Semi-synthetic / TPR: artifacts/plan_011/ or artifacts/plan_011_semi_synthetic_validation/\n- Within-subject: artifacts/plan_016/ or artifacts/plan_016_within_subject_semi_synthetic/\n- Cluster bootstrap: artifacts/sf1_cluster_bootstrap/\n- DEFF: artifacts/mf2_deff_estimation/\n- IRT theta conditioning: artifacts/plan_012/ or artifacts/plan_012_irt_theta_conditioning/\n- LOFO: artifacts/lofo_robustness/\n- Metabench cohort analysis: artifacts/metabench_cohort_analysis.csv\n\nFor each cell value, grep/read the corresponding CSV or report file in artifacts/ and verify the number matches (allowing reasonable rounding). Report your findings in this format:\n\n```\n## Table 1 核查\n- Cell [Temporal, C%] = 31.3 ← [source file:value] ✅ / ⚠️ / ❌\n...\n\n## Table 2 核查\n- Cell [Baseline, Temp C%] = 0.314±.009 ← [source file:value] ✅ / ⚠️ / ❌\n...\n```\n\nBe thorough — check every cell.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "tool_args": {
    "description": "Audit Table 1 + Table 2",
    "prompt": "You are auditing data correctness in an academic paper. Your job is to verify every cell value in Table 1 (tab:temporal_landscape) and Table 2 (tab:structural_comparison) from experiments.tex against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\n## Table 1 (tab:temporal_landscape) — line 24-42 of experiments.tex\nContent:\n```\nCohort Definition & N_ref / N_focal & C% & C% (web-clean) & Enrich.\nTemporal (2023 vs 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964\nAbility quintile (Q1-2 vs Q4-5) & ~2,600 / ~2,600 & 2.9 & 0.027 & 1.19\nWithin-family (Llama-2 vs 3) & 161 / 308 & 61.3 & -- & --\nRandom split 2023 (sanity) & 540 / 540 & 0.62 & -- & --\nRandom split 2024 (sanity) & ~400 / ~400 & 1.3 & -- & --\nWithin-subject (avg, 5 subj.) & varies & 38.1 & -- & --\n```\n\n## Table 2 (tab:structural_comparison) — line 62-78 of experiments.tex\nContent:\n```\nApproach & Mechanism & Temp C% & TPR (p=0.5) & Outcome\nBaseline (ext.) & Cross-bench total score & 0.314±.009 & 0.834±.027 & Reference\nMatched-ability & Within-quintile temp DIF & ~0.31 & -- & Enrich 0.94-1.04\nθ-cond (sens.) & θ replaces total score & 0.312 & 0.876 & r(θ,total)=0.9986\nWithin-subject & Per-subject DIF & -- & -- & C%=38.1% (>25%)\n```\n\n## Known data sources to check:\n- Temporal DIF: artifacts/plan_001/ or artifacts/plan_001_real_data_dif_mmlu/\n- Random splits / permutation: artifacts/plan_029_permutation_null/\n- Within-family: may be in plan_001 or other plan dirs\n- Ability quintile: check plan_001 or other dirs\n- Semi-synthetic / TPR: artifacts/plan_011/ or artifacts/plan_011_semi_synthetic_validation/\n- Within-subject: artifacts/plan_016/ or artifacts/plan_016_within_subject_semi_synthetic/\n- Cluster bootstrap: artifacts/sf1_cluster_bootstrap/\n- DEFF: artifacts/mf2_deff_estimation/\n- IRT theta conditioning: artifacts/plan_012/ or artifacts/plan_012_irt_theta_conditioning/\n- LOFO: artifacts/lofo_robustness/\n- Metabench cohort analysis: artifacts/metabench_cohort_analysis.csv\n\nFor each cell value, grep/read the corresponding CSV or report file in artifacts/ and verify the number matches (allowing reasonable rounding). Report your findings in this format:\n\n```\n## Table 1 核查\n- Cell [Temporal, C%] = 31.3 ← [source file:value] ✅ / ⚠️ / ❌\n...\n\n## Table 2 核查\n- Cell [Baseline, Temp C%] = 0.314±.009 ← [source file:value] ✅ / ⚠️ / ❌\n...\n```\n\nBe thorough — check every cell.",
    "model": "sonnet"
  }
}
````

</details>

---


### Tool call

_source line 10 · 2026-05-23T19:54:33.801767+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | sort",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | sort",
    "description": "List artifacts directory"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-23T19:54:33.801958+00:00_

__pycache__
_project
arr_checklist_draft.md
artifacts_qc_report.md
build_response_matrix.py
data_audit_part1.md
deff_parametric_curve
dif_diagnostic.py
dif_diagnostic_output.log
dif_diagnostic_pvalue_dist.pdf
dif_diagnostic_tpr_comparison.csv
dif_phase2_param_distribution.pdf
dif_phase2_power_curves.pdf
dif_phase2_results.csv
dif_phase2_simulation.py
dif_power_curves.pdf
dif_power_results.csv
dif_power_simulation.py
difficulty_modeltype_interaction
dream_reports
experiment_summary.md
irt_scale_analysis.json
irt_scale_analysis.md
item_metadata.csv
k3_power_simulation
literature_survey_d011.md
lofo_robustness
manifest.yaml
metabench_cohort_analysis.csv
metabench_ctt_stats.csv
metabench_data
metabench_data_summary.md
metabench_explore.py
metabench_model_accuracy.csv
metabench_model_list.txt
metabench_rl_models.csv
metabench_subject_stats.csv
metabench_summary.json
mf1_lofo_power_calibration
mf1_worked_examples
mf2_deff_estimation
mf2_practical_significance
mf2_rho_degradation
mixed_mechanism_semisynthetic
mmlu_cf_analysis.json
mmlu_cf_analysis.md
mmlu_li2024_proxy_labels.csv
mmlu_redux
model_metadata.csv
mvp_dif_power_sim
novelty_rebuttal_draft.md
plan_001
plan_001_real_data_dif_mmlu
plan_001b
plan_004
plan_004_data_availability.md
plan_010
plan_011
plan_011_semi_synthetic_validation
plan_012
plan_012_irt_theta_conditioning
plan_013
plan_013_q3_local_independence
plan_013_supplement
plan_014
plan_015
plan_016
plan_016_supplement
plan_016_within_subject_semi_synthetic
plan_017
plan_017_supplement
plan_018
plan_019
plan_020
plan_021
plan_022
plan_023
plan_024
plan_026
plan_027_temporal_overlap
plan_028_bootstrap_ci
plan_028_multi_bench_dif
plan_029_permutation_null
plan_030_odds_ratio
plan_031_temporal_granularity
plan_032_dif_cleaned_mmlu
plan_033_subject_dif_concentration
plan_034
plan_034_multi_subject_injection
plan_035_q3_inflation_sim
plan_036_growing_pains
plan_036_growing_pains_lookup
predictive_model
psn_irt_item_parameters.csv
r14_mf1_domain_profile
r14_sf5_gem
…[truncated 1102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-23T19:54:33.802120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "offset": "1",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "offset": "1",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-23T19:54:33.802302+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: ${\sim}$29\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift
…[truncated 9530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-23T19:54:33.802467+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/",
  "description": "List plan_001 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/",
    "description": "List plan_001 directory"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-23T19:54:33.802618+00:00_

cross_analysis.csv
dif_results_ability.csv
dif_results_temporal.csv
dif_summary.csv
domain_specificity.csv
neg_disc_sensitivity.csv
plan_001_analysis.py
plan_001_report.md
within_family_dif.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-23T19:54:33.802777+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
  "description": "List plan_001_real_data_dif_mmlu directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
    "description": "List plan_001_real_data_dif_mmlu directory"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-23T19:54:33.802902+00:00_

data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-23T19:54:33.803041+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/",
  "description": "List plan_029 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/",
    "description": "List plan_029 directory"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-23T19:54:33.803164+00:00_

fig_permutation_null.png
permutation_null_report.md
permutation_results.csv
plan_029_permutation_null.py
run.log
run_final.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-23T19:54:33.803289+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Audit Table 3 (cross-benchmark)",
  "prompt": "You are auditing data correctness in an academic paper. Your job is to verify every cell value in Table 3 (tab:cross_benchmark) from experiments.tex against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\n## Table 3 (tab:cross_benchmark) — line 98-116 of experiments.tex\nContent:\n```\nBenchmark & Items & C% & ρ & τ & Flip% & Rand C% & Ratio\nMMLU & 12,508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.62 & 50×\nWinoGrande & 1,267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95×\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80×\nARC & 1,172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45×\nGSM8K & 1,319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63×\nHellaSwag & 10,042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64×\n```\n\n## Known data sources:\n- Cross-benchmark DIF: artifacts/plan_028_multi_bench_dif/ — look for summary CSVs, report files\n- Also check artifacts/plan_001_real_data_dif_mmlu/ for MMLU row\n- For downstream rank metrics (ρ, τ, Flip%), check artifacts/plan_032_dif_cleaned_mmlu/ or artifacts/score_inflation_analysis/\n- Random C% may come from permutation null: artifacts/plan_029_permutation_null/\n\nFor each cell value, grep/read the corresponding CSV or report file in artifacts/ and verify the number matches (allowing reasonable rounding). Report your findings in this format:\n\n```\n## Table 3 核查\n- Cell [MMLU, Items] = 12,508 ← [source file:value] ✅ / ⚠️ / ❌\n- Cell [MMLU, C%] = 31.3 ← [source file:value] ✅ / ⚠️ / ❌\n...\n```\n\nBe thorough — check every cell for all 6 benchmarks.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "tool_args": {
    "description": "Audit Table 3 (cross-benchmark)",
    "prompt": "You are auditing data correctness in an academic paper. Your job is to verify every cell value in Table 3 (tab:cross_benchmark) from experiments.tex against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\n## Table 3 (tab:cross_benchmark) — line 98-116 of experiments.tex\nContent:\n```\nBenchmark & Items & C% & ρ & τ & Flip% & Rand C% & Ratio\nMMLU & 12,508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.62 & 50×\nWinoGrande & 1,267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95×\nTruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80×\nARC & 1,172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45×\nGSM8K & 1,319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63×\nHellaSwag & 10,042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64×\n```\n\n## Known data sources:\n- Cross-benchmark DIF: artifacts/plan_028_multi_bench_dif/ — look for summary CSVs, report files\n- Also check artifacts/plan_001_real_data_dif_mmlu/ for MMLU row\n- For downstream rank metrics (ρ, τ, Flip%), check artifacts/plan_032_dif_cleaned_mmlu/ or artifacts/score_inflation_analysis/\n- Random C% may come from permutation null: artifacts/plan_029_permutation_null/\n\nFor each cell value, grep/read the corresponding CSV or report file in artifacts/ and verify the number matches (allowing reasonable rounding). Report your findings in this format:\n\n```\n## Table 3 核查\n- Cell [MMLU, Items] = 12,508 ← [source file:value] ✅ / ⚠️ / ❌\n- Cell [MMLU, C%] = 31.3 ← [source file:value] ✅ / ⚠️ / ❌\n...\n```\n\nBe thorough — check every cell for all 6 benchmarks.",
    "model": "sonnet"
  }
}
````

</details>

---


### Tool call

_source line 21 · 2026-05-23T19:54:33.803615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv"
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-23T19:54:33.803768+00:00_

File content (1.6MB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-23T19:54:33.803894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv"
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-23T19:54:33.804013+00:00_

1	cohort_type,item_filter,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,fpr_vs_li_clean,enrichment_ratio
2	temporal,all,12508,6332,2258,3918,31.323952670291018,0.31840974212034384,0.9641535548797142
3	ability,all,12508,11052,1093,363,2.9021426287176206,0.026862464183381087,1.1949300411522636
4	temporal,non_neg_disc,10582,5327,1830,3425,32.36628236628237,0.3257975913796746,0.969539159262983
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-23T19:54:33.804144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_ability.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_ability.csv"
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-23T19:54:33.804265+00:00_

File content (1009.5KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-23T19:54:33.804381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv"
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-23T19:54:33.804522+00:00_

File content (3.6MB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-23T19:54:33.804643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv"
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-23T19:54:33.804804+00:00_

1	permutation,c_pct
2	1,0.03997441637352095
3	2,0.08794371602174608
4	3,0.11992324912056285
5	4,0.17588743204349216
6	5,1.143268308282699
7	6,0.03997441637352095
8	7,0.03197953309881676
9	8,0.32779021426287175
10	9,0.023984649824112567
11	10,0.32779021426287175
12	11,0.023984649824112567
13	12,0.11992324912056285
14	13,0.09593859929645027
15	14,0.03997441637352095
16	15,0.25583626479053406
17	16,0.023984649824112567
18	17,0.03197953309881676
19	18,0.03197953309881676
20	19,0.09593859929645027
21	20,0.08794371602174608
22	21,0.06395906619763352
23	22,0.00799488327470419
24	23,0.0799488327470419
25	24,0.0719539494723377
26	25,0.0719539494723377
27	26,0.03197953309881676
28	27,0.12791813239526703
29	28,0.01598976654940838
30	29,0.0799488327470419
31	30,0.09593859929645027
32	31,0.023984649824112567
33	32,0.06395906619763352
34	33,0.10393348257115445
35	34,0.0719539494723377
36	35,0.03997441637352095
37	36,0.06395906619763352
38	37,0.055964182922929324
39	38,0.04796929964822513
40	39,0.13591301566997122
41	40,0.00799488327470419
42	41,0.09593859929645027
43	42,0.04796929964822513
44	43,0.1598976654940838
45	44,0.055964182922929324
46	45,0.023984649824112567
47	46,0.16789254876878798
48	47,0.0719539494723377
49	48,0.0799488327470419
50	49,0.03197953309881676
51	50,0.0719539494723377
52	51,0.18388231531819635
53	52,0.0719539494723377
54	53,0.1439078989446754
55	54,0.06395906619763352
56	55,0.04796929964822513
57	56,0.1598976654940838
58	57,0.01598976654940838
59	58,0.03997441637352095
60	59,0.04796929964822513
61	60,0.17588743204349216
62	61,0.055964182922929324
63	62,0.09593859929645027
64	63,0.055964182922929324
65	64,0.24784138151582985
66	65,0.0799488327470419
67	66,0.03997441637352095
68	67,0.06395906619763352
69	68,0.03197953309881676
70	69,0.3917492804605053
71	70,0.0719539494723377
72	71,0.0719539494723377
73	72,0.00799488327470419
74	73,0.08794371602174608
75	74,0.0799488327470419
76	75,0.13591301566997122
77	76,0.023984649824112567
78	77,0.06395906619763352
79	7
…[truncated 3393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-23T19:54:33.804968+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport csv\ndata = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        data.append(float(row['c_pct']))\nprint(f'N permutations: {len(data)}')\nprint(f'Mean C%: {sum(data)/len(data):.4f}')\nimport statistics\nprint(f'Max C%: {max(data):.4f}')\nprint(f'99th pct: {sorted(data)[int(len(data)*0.99)]:.4f}')\n\"\n",
  "description": "Calculate permutation null statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport csv\ndata = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        data.append(float(row['c_pct']))\nprint(f'N permutations: {len(data)}')\nprint(f'Mean C%: {sum(data)/len(data):.4f}')\nimport statistics\nprint(f'Max C%: {max(data):.4f}')\nprint(f'99th pct: {sorted(data)[int(len(data)*0.99)]:.4f}')\n\"\n",
    "description": "Calculate permutation null statistics"
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-23T19:54:33.805099+00:00_

N permutations: 200
Mean C%: 0.0999
Max C%: 1.1433
99th pct: 1.0313

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 33 · 2026-05-23T19:54:33.805216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_null_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_null_report.md"
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-23T19:54:33.805344+00:00_

1	# Plan 029: Permutation Null for Temporal DIF C%
2	
3	## Purpose
4	
5	Test whether the observed temporal DIF C% significantly exceeds the rate
6	expected under random label assignment.
7	
8	## Method
9	
10	- **Data**: 1887 models with temporal labels (1080 "2023", 807 "2024"), 12508 items
11	- **Procedure**: 200 permutations of temporal labels, group sizes fixed
12	- **MH-DIF**: purified matching, 5 quantile strata, ETS classification
13	- **Seed**: 42
14	- **Optimisation**: strata precomputed once (invariant to label permutation)
15	
16	## Results
17	
18	| Metric | Value |
19	|--------|-------|
20	| Observed C% | 31.32% |
21	| Null mean ± SD | 0.10% ± 0.12% |
22	| Null 95% CI | [0.02%, 0.33%] |
23	| Null range | [0.01%, 1.14%] |
24	| N exceed observed | 0 / 200 |
25	| p-value | = 0.0050 |
26	
27	## Interpretation
28	
29	The observed temporal DIF C% of 31.32% is **above** the permutation null (mean 0.10%, max 1.14%, p = 0.0050).  The 31.3% C-category rate cannot be attributed to chance label assignment.
30	
31	## Runtime
32	
33	- Per permutation: ~2.7s
34	- Total: 4.2 min (200 permutations)
35	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-23T19:54:33.805479+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv 2>/dev/null || echo \"Can't read\"\npython3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv') as f:\n    for i, line in enumerate(f):\n        if i < 10:\n            print(repr(line))\n\"\n",
  "description": "Read within_family_dif.csv header and first rows"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv 2>/dev/null || echo \"Can't read\"\npython3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv') as f:\n    for i, line in enumerate(f):\n        if i < 10:\n            print(repr(line))\n\"\n",
    "description": "Read within_family_dif.csv header and first rows"
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-23T19:54:33.805604+00:00_

item_id,subject,ref_group,foc_group,alpha_mh,delta_mh,se,p_value,ets_class,li_label,li_contamination_type
abstract_algebra.1,abstract_algebra,llama-2,llama-3,0.6333632465849038,1.073271254578906,0.7329806938418083,0.18029453590428224,B,False,clean
abstract_algebra.10,abstract_algebra,llama-2,llama-3,2.873978331115757,-2.480888532806384,1.8521198094786246,0.3194119666775368,B,False,clean
abstract_algebra.100,abstract_algebra,llama-2,llama-3,1.310158750078434,-0.6348485358718126,1.1764183738047866,0.7964409968190814,A,,no_annotation
abstract_algebra.11,abstract_algebra,llama-2,llama-3,7.339912280701754,-4.68431819548781,1.0025200032908865,2.768963426658111e-06,C,False,clean
'item_id,subject,ref_group,foc_group,alpha_mh,delta_mh,se,p_value,ets_class,li_label,li_contamination_type\n'
'abstract_algebra.1,abstract_algebra,llama-2,llama-3,0.6333632465849038,1.073271254578906,0.7329806938418083,0.18029453590428224,B,False,clean\n'
'abstract_algebra.10,abstract_algebra,llama-2,llama-3,2.873978331115757,-2.480888532806384,1.8521198094786246,0.3194119666775368,B,False,clean\n'
'abstract_algebra.100,abstract_algebra,llama-2,llama-3,1.310158750078434,-0.6348485358718126,1.1764183738047866,0.7964409968190814,A,,no_annotation\n'
'abstract_algebra.11,abstract_algebra,llama-2,llama-3,7.339912280701754,-4.68431819548781,1.0025200032908865,2.768963426658111e-06,C,False,clean\n'
'abstract_algebra.12,abstract_algebra,llama-2,llama-3,2.5530838041431263,-2.202659614159003,1.035358827538494,0.023516507472339132,C,False,clean\n'
'abstract_algebra.13,abstract_algebra,llama-2,llama-3,0.5982518912876889,1.207296968454848,0.6065972166521588,0.054232734376852165,B,False,clean\n'
'abstract_algebra.14,abstract_algebra,llama-2,llama-3,0.5281532296406982,1.5001667498540638,1.1075421683484115,0.2763181256268491,B,False,clean\n'
'abstract_algebra.15,abstract_algebra,llama-2,llama-3,0.1678832116788321,4.193543768262592,2.961621471214678,0.358627037715752,B,False,clean\n'
'abstract_algebra.16,abstract_a
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-23T19:54:33.805760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_report.md"
  }
}
```

</details>

---


### Tool result

_source line 38 · 2026-05-23T19:54:33.805901+00:00_

1	# Plan 001: METABENCH Real-Data MH-DIF Analysis
2	
3	## 1. Data & Setup
4	
5	- Response matrix: **5227 models × 12508 items** (binary, MMLU)
6	- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
7	- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
8	- Li et al. annotations: 9229 annotated items
9	
10	## 2. ETS Classification
11	
12	| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
13	|--------|--------|-------|---|---|---|----|-------------|------------|
14	| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
15	| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
16	| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
17	
18	## 3. Li et al. Proxy Validation
19	
20	| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
21	|--------|-------------|---------------|--------------|------------------|------------|
22	| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
23	| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |
24	
25	## 4. Within-Family Analysis
26	
27	- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
28	- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)
29	
30	### Cross-cohort vs within-family overlap
31	
32	- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
33	- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804
34	
35	## 5. Domain Specificity
36	
37	Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)
38	
39	Top 15 subjects by C rate (temporal cohort):
40	
41	| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
42	|---------|-------|---|-----|----------|----------|------|
43	| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
44	| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
45	| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
46	| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-23T19:54:33.806049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Count within_family_dif items for llama-2 vs llama-3\npython3 -c \"\nimport csv\nref_count = 0\nfoc_count = 0\nc_count = 0\ntotal = 0\nfamilies = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        family_key = (row['ref_group'], row['foc_group'])\n        if family_key not in families:\n            families[family_key] = {'A':0, 'B':0, 'C':0, 'total':0}\n        families[family_key][row['ets_class']] += 1\n        families[family_key]['total'] += 1\n\nfor fam, counts in sorted(families.items()):\n    pct_c = counts['C']/counts['total']*100 if counts['total'] > 0 else 0\n    print(f'{fam}: total={counts[\\\"total\\\"]}, C={counts[\\\"C\\\"]}, %C={pct_c:.1f}')\n\"\n",
  "description": "Calculate within-family DIF statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Count within_family_dif items for llama-2 vs llama-3\npython3 -c \"\nimport csv\nref_count = 0\nfoc_count = 0\nc_count = 0\ntotal = 0\nfamilies = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        family_key = (row['ref_group'], row['foc_group'])\n        if family_key not in families:\n            families[family_key] = {'A':0, 'B':0, 'C':0, 'total':0}\n        families[family_key][row['ets_class']] += 1\n        families[family_key]['total'] += 1\n\nfor fam, counts in sorted(families.items()):\n    pct_c = counts['C']/counts['total']*100 if counts['total'] > 0 else 0\n    print(f'{fam}: total={counts[\\\"total\\\"]}, C={counts[\\\"C\\\"]}, %C={pct_c:.1f}')\n\"\n",
    "description": "Calculate within-family DIF statistics"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-23T19:54:33.806172+00:00_

('llama-2', 'llama-3'): total=12508, C=7672, %C=61.3
('mistral', 'mixtral'): total=12508, C=4835, %C=38.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-23T19:54:33.806287+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check ability quintile N counts\npython3 -c \"\n# From plan_001_report: Q1-2 N=2092, Q4-5 N=2089\n# But paper says ~2600/~2600\n# Check if there are updated values\nimport json, os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\n# Look for any updated ability analysis\nfor d in ['plan_001_real_data_dif_mmlu', 'plan_001b']:\n    path = base + d\n    if os.path.exists(path):\n        print(f'DIR: {d}')\n        print(os.listdir(path))\n\"\n",
  "description": "Check ability quintile N counts across directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check ability quintile N counts\npython3 -c \"\n# From plan_001_report: Q1-2 N=2092, Q4-5 N=2089\n# But paper says ~2600/~2600\n# Check if there are updated values\nimport json, os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\n# Look for any updated ability analysis\nfor d in ['plan_001_real_data_dif_mmlu', 'plan_001b']:\n    path = base + d\n    if os.path.exists(path):\n        print(f'DIR: {d}')\n        print(os.listdir(path))\n\"\n",
    "description": "Check ability quintile N counts across directories"
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-23T19:54:33.806416+00:00_

DIR: plan_001_real_data_dif_mmlu
['intermediate', 'data', 'report']
DIR: plan_001b
['enrichment_summary.csv', 'dif_results_merged.csv', 'plan_001b_analysis.py', 'data', 'dif_results_per_quintile.csv', 'report', 'plan_001b_report.md', 'quintile_cohort_sizes.csv']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-23T19:54:33.806533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/quintile_cohort_sizes.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/quintile_cohort_sizes.csv"
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-23T19:54:33.806645+00:00_

1	quintile,n_2023,n_2024,n_total,underpowered
2	1,180,162,342,False
3	2,406,106,512,False
4	3,287,168,455,False
5	4,88,197,285,False
6	5,119,174,293,False
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-23T19:54:33.806775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_report.md"
  }
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-23T19:54:33.806893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"plan_028|plan_001|plan_032|plan_029|score_inflation\" | sort",
  "description": "List relevant artifact directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"plan_028|plan_001|plan_032|plan_029|score_inflation\" | sort",
    "description": "List relevant artifact directories"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-23T19:54:33.807005+00:00_

plan_001
plan_001_real_data_dif_mmlu
plan_001b
plan_028_bootstrap_ci
plan_028_multi_bench_dif
plan_029_permutation_null
plan_032_dif_cleaned_mmlu
score_inflation_analysis

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-23T19:54:33.807118+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | sort",
  "description": "List all artifact directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | sort",
    "description": "List all artifact directories"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-23T19:54:33.807240+00:00_

__pycache__
_project
arr_checklist_draft.md
artifacts_qc_report.md
build_response_matrix.py
data_audit_part1.md
deff_parametric_curve
dif_diagnostic.py
dif_diagnostic_output.log
dif_diagnostic_pvalue_dist.pdf
dif_diagnostic_tpr_comparison.csv
dif_phase2_param_distribution.pdf
dif_phase2_power_curves.pdf
dif_phase2_results.csv
dif_phase2_simulation.py
dif_power_curves.pdf
dif_power_results.csv
dif_power_simulation.py
difficulty_modeltype_interaction
dream_reports
experiment_summary.md
irt_scale_analysis.json
irt_scale_analysis.md
item_metadata.csv
k3_power_simulation
literature_survey_d011.md
lofo_robustness
manifest.yaml
metabench_cohort_analysis.csv
metabench_ctt_stats.csv
metabench_data
metabench_data_summary.md
metabench_explore.py
metabench_model_accuracy.csv
metabench_model_list.txt
metabench_rl_models.csv
metabench_subject_stats.csv
metabench_summary.json
mf1_lofo_power_calibration
mf1_worked_examples
mf2_deff_estimation
mf2_practical_significance
mf2_rho_degradation
mixed_mechanism_semisynthetic
mmlu_cf_analysis.json
mmlu_cf_analysis.md
mmlu_li2024_proxy_labels.csv
mmlu_redux
model_metadata.csv
mvp_dif_power_sim
novelty_rebuttal_draft.md
plan_001
plan_001_real_data_dif_mmlu
plan_001b
plan_004
plan_004_data_availability.md
plan_010
plan_011
plan_011_semi_synthetic_validation
plan_012
plan_012_irt_theta_conditioning
plan_013
plan_013_q3_local_independence
plan_013_supplement
plan_014
plan_015
plan_016
plan_016_supplement
plan_016_within_subject_semi_synthetic
plan_017
plan_017_supplement
plan_018
plan_019
plan_020
plan_021
plan_022
plan_023
plan_024
plan_026
plan_027_temporal_overlap
plan_028_bootstrap_ci
plan_028_multi_bench_dif
plan_029_permutation_null
plan_030_odds_ratio
plan_031_temporal_granularity
plan_032_dif_cleaned_mmlu
plan_033_subject_dif_concentration
plan_034
plan_034_multi_subject_injection
plan_035_q3_inflation_sim
plan_036_growing_pains
plan_036_growing_pains_lookup
predictive_model
psn_irt_item_parameters.csv
r14_mf1_domain_profile
r14_sf5_gem
…[truncated 1102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-23T19:54:33.807380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/",
  "description": "List plan_028_multi_bench_dif contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/",
    "description": "List plan_028_multi_bench_dif contents"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-23T19:54:33.807498+00:00_

arc_dif_results.csv
arc_ets_summary.csv
data
hellaswag_dif_results.csv
hellaswag_ets_summary.csv
intermediate
multi_bench_dif_report.md
multi_bench_summary.csv
multi_bench_summary.csv.bak
plan_028_multi_bench_dif.py
report
run.log
truthfulqa_dif_results.csv
truthfulqa_ets_summary.csv
winogrande_dif_results.csv
winogrande_ets_summary.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-23T19:54:33.807903+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/",
  "description": "List plan_029 contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/",
    "description": "List plan_029 contents"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-23T19:54:33.808056+00:00_

fig_permutation_null.png
permutation_null_report.md
permutation_results.csv
plan_029_permutation_null.py
run.log
run_final.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-23T19:54:33.808207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/",
  "description": "List plan_032 contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/",
    "description": "List plan_032 contents"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-23T19:54:33.808345+00:00_

cleaned_mmlu_analysis.csv
data
dif_vs_random_comparison.csv
per_subject_dif_concentration.csv
plan_032_dif_cleaned_mmlu.py
plan_032_random_baseline.py
plan_032_report.md
random_baseline_report.md
random_baseline_summary.csv
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-23T19:54:33.808480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/",
  "description": "List score_inflation_analysis contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/",
    "description": "List score_inflation_analysis contents"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-23T19:54:33.808614+00:00_

cohort_summary.csv
model_scores.csv
rank_displacement.pdf
rank_displacement.png
score_change_violin.pdf
score_change_violin.png
score_inflation.py
score_inflation_report.md
score_scatter.pdf
score_scatter.png
top_displaced.csv
type_summary.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-23T19:54:33.808753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-23T19:54:33.808880+00:00_

1	benchmark,n_items,n_ref,n_foc,n_ets_a,n_ets_b,n_ets_c,pct_c,random_pct_c,status
2	mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
3	winogrande,1267,1017,803,612,271,384,30.3,0.32,OK
4	truthfulqa,817,1080,807,398,176,243,29.7,0.37,OK
5	arc,1172,1080,807,642,215,315,26.9,0.6,OK
6	gsm8k,1319,1017,804,825,245,249,18.9,0.3,PRIOR
7	hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-23T19:54:33.808998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-23T19:54:33.809143+00:00_

1	# Plan 028: Multi-Benchmark Temporal DIF Analysis
2	
3	## Overview
4	
5	Temporal MH-DIF analysis (2023 vs 2024 cohort) across all 6 METABENCH benchmarks.
6	Uses purified Mantel-Haenszel with 5 score strata. ETS classification:
7	- **A**: |Δ_MH| < 1.0 (negligible)
8	- **B**: 1.0 ≤ |Δ_MH| < 1.5 or |Δ_MH| ≥ 1.5 but p ≥ 0.05 (moderate)
9	- **C**: |Δ_MH| ≥ 1.5 and p < 0.05 (large, flagged)
10	
11	## Summary Table
12	
13	| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
14	|-----------|-------|-------------|-------------|---|---|---|----|-----------|--------|
15	| MMLU | 12508 | 1080 | 807 | 6332 | 2258 | 3918 | 31.3% | 0.18% | PRIOR |
16	| WINOGRANDE | 1267 | 1017 | 803 | 612 | 271 | 384 | 30.3% | 0.32% | OK |
17	| TRUTHFULQA | 817 | 1080 | 807 | 398 | 176 | 243 | 29.7% | 0.37% | OK |
18	| ARC | 1172 | 1080 | 807 | 642 | 215 | 315 | 26.9% | 0.6% | OK |
19	| GSM8K | 1319 | 1017 | 804 | 825 | 245 | 249 | 18.9% | 0.3% | PRIOR |
20	| HELLASWAG | 10042 | 1080 | 807 | 6037 | 2208 | 1797 | 17.9% | 0.28% | OK |
21	
22	## Key Findings
23	
24	- **WINOGRANDE**: 30.3% items flagged as ETS-C (vs 0.32% random control, 94.7× enrichment)
25	- **TRUTHFULQA**: 29.7% items flagged as ETS-C (vs 0.37% random control, 80.3× enrichment)
26	- **ARC**: 26.9% items flagged as ETS-C (vs 0.6% random control, 44.8× enrichment)
27	- **HELLASWAG**: 17.9% items flagged as ETS-C (vs 0.28% random control, 63.9× enrichment)
28	
29	## Interpretation
30	
31	The temporal DIF signal (C% >> random C%) indicates systematic item-level 
32	performance shifts between 2023 and 2024 model cohorts, consistent with 
33	benchmark contamination or benchmark-specific training optimization.
34	
35	Random-split controls confirm that the DIF signal is not an artifact of 
36	the MH procedure or score distribution differences within a single cohort.
37	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-23T19:54:33.809292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-23T19:54:33.809427+00:00_

1	permutation,c_pct
2	1,0.03997441637352095
3	2,0.08794371602174608
4	3,0.11992324912056285
5	4,0.17588743204349216
6	5,1.143268308282699
7	6,0.03997441637352095
8	7,0.03197953309881676
9	8,0.32779021426287175
10	9,0.023984649824112567
11	10,0.32779021426287175
12	11,0.023984649824112567
13	12,0.11992324912056285
14	13,0.09593859929645027
15	14,0.03997441637352095
16	15,0.25583626479053406
17	16,0.023984649824112567
18	17,0.03197953309881676
19	18,0.03197953309881676
20	19,0.09593859929645027
21	20,0.08794371602174608
22	21,0.06395906619763352
23	22,0.00799488327470419
24	23,0.0799488327470419
25	24,0.0719539494723377
26	25,0.0719539494723377
27	26,0.03197953309881676
28	27,0.12791813239526703
29	28,0.01598976654940838
30	29,0.0799488327470419
31	30,0.09593859929645027
32	31,0.023984649824112567
33	32,0.06395906619763352
34	33,0.10393348257115445
35	34,0.0719539494723377
36	35,0.03997441637352095
37	36,0.06395906619763352
38	37,0.055964182922929324
39	38,0.04796929964822513
40	39,0.13591301566997122
41	40,0.00799488327470419
42	41,0.09593859929645027
43	42,0.04796929964822513
44	43,0.1598976654940838
45	44,0.055964182922929324
46	45,0.023984649824112567
47	46,0.16789254876878798
48	47,0.0719539494723377
49	48,0.0799488327470419
50	49,0.03197953309881676
51	50,0.0719539494723377
52	51,0.18388231531819635
53	52,0.0719539494723377
54	53,0.1439078989446754
55	54,0.06395906619763352
56	55,0.04796929964822513
57	56,0.1598976654940838
58	57,0.01598976654940838
59	58,0.03997441637352095
60	59,0.04796929964822513
61	60,0.17588743204349216
62	61,0.055964182922929324
63	62,0.09593859929645027
64	63,0.055964182922929324
65	64,0.24784138151582985
66	65,0.0799488327470419
67	66,0.03997441637352095
68	67,0.06395906619763352
69	68,0.03197953309881676
70	69,0.3917492804605053
71	70,0.0719539494723377
72	71,0.0719539494723377
73	72,0.00799488327470419
74	73,0.08794371602174608
75	74,0.0799488327470419
76	75,0.13591301566997122
77	76,0.023984649824112567
78	77,0.06395906619763352
79	7
…[truncated 3393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-23T19:54:33.809574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_null_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_null_report.md"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-23T19:54:33.809715+00:00_

1	# Plan 029: Permutation Null for Temporal DIF C%
2	
3	## Purpose
4	
5	Test whether the observed temporal DIF C% significantly exceeds the rate
6	expected under random label assignment.
7	
8	## Method
9	
10	- **Data**: 1887 models with temporal labels (1080 "2023", 807 "2024"), 12508 items
11	- **Procedure**: 200 permutations of temporal labels, group sizes fixed
12	- **MH-DIF**: purified matching, 5 quantile strata, ETS classification
13	- **Seed**: 42
14	- **Optimisation**: strata precomputed once (invariant to label permutation)
15	
16	## Results
17	
18	| Metric | Value |
19	|--------|-------|
20	| Observed C% | 31.32% |
21	| Null mean ± SD | 0.10% ± 0.12% |
22	| Null 95% CI | [0.02%, 0.33%] |
23	| Null range | [0.01%, 1.14%] |
24	| N exceed observed | 0 / 200 |
25	| p-value | = 0.0050 |
26	
27	## Interpretation
28	
29	The observed temporal DIF C% of 31.32% is **above** the permutation null (mean 0.10%, max 1.14%, p = 0.0050).  The 31.3% C-category rate cannot be attributed to chance label assignment.
30	
31	## Runtime
32	
33	- Per permutation: ~2.7s
34	- Total: 4.2 min (200 permutations)
35	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-23T19:54:33.809853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-23T19:54:33.809998+00:00_

1	# Plan 032: DIF-Cleaned MMLU Demonstration
2	
3	## Overview
4	- Full MMLU: **12508** items
5	- DIF-cleaned MMLU: **8590** items (removed **3918** ETS C-flagged, 31.3%)
6	- Models analyzed: **5227**
7	
8	## Global Rank Correlation
9	- Spearman ρ (full vs. cleaned scores): **0.996455** (p=0.00e+00)
10	- This high ρ is expected—but masks local rank disruptions that matter for evaluation.
11	
12	## Rank Change Distribution
13	- Mean rank change: 0.00
14	- Std rank change: 127.10
15	- Min: -589 | Max: 849
16	- |change| ≥ 5: 4679 models (89.5%)
17	- |change| ≥ 10: 4158 models (79.5%)
18	- |change| ≥ 20: 3471 models (66.4%)
19	- |change| ≥ 50: 2188 models (41.9%)
20	- |change| ≥ 100: 1297 models (24.8%)
21	
22	## Top 10 Models Moving UP (rank improved after cleaning)
23	
24	| model_name | family | cohort_temporal | score_full | score_cleaned | rank_full | rank_cleaned | rank_change |
25	| --- | --- | --- | --- | --- | --- | --- | --- |
26	| liminerity/Blurstral-7b-slerp | unknown | other | 0.6948 | 0.7236 | 1412 | 823 | -589 |
27	| DreadPoor/PAIN_LeDestroy-7B-task_arithmetic | unknown | other | 0.6984 | 0.7258 | 1182 | 613 | -569 |
28	| flammenai/flammen26-mistral-7B | mistral | 2023 | 0.6961 | 0.7240 | 1336 | 790 | -546 |
29	| Gille/StrangeMerges_2-7B-slerp | unknown | other | 0.6964 | 0.7239 | 1316 | 797 | -519 |
30	| Gille/StrangeMerges_12-7B-slerp | unknown | other | 0.6960 | 0.7232 | 1345 | 851 | -494 |
31	| jambroz/sixtyoneeighty-7b | unknown | other | 0.6972 | 0.7241 | 1269 | 782 | -487 |
32	| jambroz/sixtyoneeighty-7b-chat | unknown | other | 0.6972 | 0.7241 | 1270 | 783 | -487 |
33	| antiven0m/reverie-7b | unknown | other | 0.6968 | 0.7237 | 1288 | 810 | -478 |
34	| GreenNode/GreenNodeLM-7B-v2leo | unknown | other | 0.6962 | 0.7232 | 1329 | 852 | -477 |
35	| DreadPoor/Sphinx-7B-Model_Stock | unknown | other | 0.6970 | 0.7236 | 1280 | 818 | -462 |
36	
37	## Top 10 Models Moving DOWN (rank worsened after cleaning)
38	
39	| model_name | family | cohort_temporal | s
…[truncated 6884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-23T19:54:33.810156+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/dif_vs_random_comparison.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/dif_vs_random_comparison.csv"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-23T19:54:33.810283+00:00_

1	metric,dif_removal,random_mean,random_std,z_score
2	rank_change_std,127.08674949749147,60.245428638447365,7.836854481765597,8.529100676115291
3	mean_abs_rank_change,74.68490529940692,36.01276066577386,3.6261632977706557,10.664755406191572
4	pct_change_ge5,89.5159747465085,79.69485364453799,1.066174204783192,9.211553851059131
5	pct_change_ge10,79.54849818251387,65.25540462980676,1.1495612718218582,12.433520424757347
6	pct_change_ge50,41.859575282188636,23.90950832217333,2.1672840121102,8.282286428412318
7	pct_change_ge100,24.813468528792807,8.526879663286781,1.975727625999505,8.243337113468144
8	cohort_2023_mean_change,-22.562037037037037,0.4314814814814816,4.1188208423088115,-5.58254884075741
9	cohort_2024_mean_change,73.59851301115242,2.786802973977695,21.162419849946886,3.346106472665622
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-23T19:54:33.810423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-23T19:54:33.810558+00:00_

1	# Score Inflation & DIF-Corrected Scoring Analysis
2	**Date**: 2026-05-23
3	**Dataset**: 12508 items, 5227 models
4	**DIF-C items**: 3918 (31.3%)
5	**Stable items**: 8590 (68.7%)
6	
7	## 1. Score Change Summary
8	### By Cohort
9	| Cohort | N | Mean Original | Mean Stable | Mean Δ (pp) | SD (pp) | 95% CI |
10	|--------|---|--------------|-------------|-------------|---------|--------|
11	| 2023 | 1080 | 0.5814 | 0.6049 | +2.35 | 0.88 | [+2.30, +2.40] |
12	| 2024 | 807 | 0.6068 | 0.6274 | +2.06 | 1.04 | [+1.99, +2.13] |
13	| other | 3340 | 0.5906 | 0.6112 | +2.05 | 0.92 | [+2.02, +2.08] |
14	
15	### By Cohort × Model Type
16	| Cohort | Type | N | Mean Δ (pp) | SD (pp) | 95% CI |
17	|--------|------|---|-------------|---------|--------|
18	| 2023 | base | 805 | +2.37 | 0.88 | [+2.31, +2.43] |
19	| 2023 | instruct | 275 | +2.29 | 0.88 | [+2.19, +2.40] |
20	| 2024 | base | 534 | +2.06 | 1.06 | [+1.97, +2.15] |
21	| 2024 | instruct | 273 | +2.06 | 1.01 | [+1.94, +2.18] |
22	| other | base | 2742 | +2.05 | 0.92 | [+2.01, +2.08] |
23	| other | instruct | 598 | +2.09 | 0.95 | [+2.01, +2.16] |
24	
25	### Effect Size
26	- 2024 vs 2023 score_change Cohen's d = -0.3051
27	- Welch's t-test: t = -6.553, p = 7.23e-11
28	
29	## 2. Ranking Impact
30	- Overall Spearman ρ (original vs stable): **0.996455**
31	- Original vs adjusted: ρ = 0.999759
32	- Stable vs adjusted: ρ = 0.996489
33	
34	### Top-20 DIF Victims (rank improves most)
35	| Model | Cohort | Type | Orig Score | Stable Score | Δ pp | Rank Disp |
36	|-------|--------|------|-----------|-------------|------|----------|
37	| liminerity/Blurstral-7b-slerp | other | base | 0.6948 | 0.7236 | +2.88 | +593 |
38	| DreadPoor/PAIN_LeDestroy-7B-task_arithmetic | other | base | 0.6984 | 0.7258 | +2.74 | +570 |
39	| flammenai/flammen26-mistral-7B | 2023 | base | 0.6961 | 0.7240 | +2.79 | +548 |
40	| Gille/StrangeMerges_2-7B-slerp | other | base | 0.6964 | 0.7239 | +2.74 | +518 |
41	| Gille/StrangeMerges_12-7B-slerp | other | base | 0.6
…[truncated 4003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-23T19:54:33.810727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/cohort_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/cohort_summary.csv"
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-23T19:54:33.810856+00:00_

1	cohort_temporal,n,mean_original,mean_stable,mean_score_change,sd_score_change,ci95_lo,ci95_hi,median_score_change,mean_rank_displacement,sd_rank_displacement
2	2023,1080.0,0.5813804350400928,0.6048886517483724,0.023508216708279496,0.008806877295911128,0.022982966613943095,0.024033466802615897,0.02617434504315369,23.026851851851852,89.86925020720226
3	2024,807.0,0.606829869280191,0.6274300972428388,0.02060022796264774,0.01043351680524343,0.01988036467768786,0.021320091247607625,0.01996349344568482,-73.26517967781908,161.69001701533105
4	other,3340.0,0.5906425636095893,0.6111797243696542,0.02053716076006491,0.009220588824986302,0.020224450958584318,0.0208498705615455,0.022759571243437915,11.040718562874252,121.664231488972
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-23T19:54:33.810975+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/",
  "description": "Check report subdirectory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/",
    "description": "Check report subdirectory"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-23T19:54:33.811084+00:00_

mmlu_bootstrap_report.md
multi_bench_dif_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-23T19:54:33.811195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/intermediate/",
  "description": "Check intermediate subdirectory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/intermediate/",
    "description": "Check intermediate subdirectory"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-23T19:54:33.811309+00:00_

plan_028_multi_bench_dif.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-23T19:54:33.811420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-23T19:54:33.811539+00:00_

1	# Plan 028: Multi-Benchmark Temporal DIF Analysis
2	
3	## Overview
4	
5	Temporal MH-DIF analysis (2023 vs 2024 cohort) across all 6 METABENCH benchmarks.
6	Uses purified Mantel-Haenszel with 5 score strata. ETS classification:
7	- **A**: |Δ_MH| < 1.0 (negligible)
8	- **B**: 1.0 ≤ |Δ_MH| < 1.5 or |Δ_MH| ≥ 1.5 but p ≥ 0.05 (moderate)
9	- **C**: |Δ_MH| ≥ 1.5 and p < 0.05 (large, flagged)
10	
11	## Summary Table
12	
13	| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
14	|-----------|-------|-------------|-------------|---|---|---|----|-----------|--------|
15	| MMLU | 12508 | 1080 | 807 | 6332 | 2258 | 3918 | 31.3% | 0.18% | PRIOR |
16	| WINOGRANDE | 1267 | 1017 | 803 | 612 | 271 | 384 | 30.3% | 0.32% | OK |
17	| TRUTHFULQA | 817 | 1080 | 807 | 398 | 176 | 243 | 29.7% | 0.37% | OK |
18	| ARC | 1172 | 1080 | 807 | 642 | 215 | 315 | 26.9% | 0.6% | OK |
19	| GSM8K | 1319 | 1017 | 804 | 825 | 245 | 249 | 18.9% | 0.3% | PRIOR |
20	| HELLASWAG | 10042 | 1080 | 807 | 6037 | 2208 | 1797 | 17.9% | 0.28% | OK |
21	
22	## Key Findings
23	
24	- **WINOGRANDE**: 30.3% items flagged as ETS-C (vs 0.32% random control, 94.7× enrichment)
25	- **TRUTHFULQA**: 29.7% items flagged as ETS-C (vs 0.37% random control, 80.3× enrichment)
26	- **ARC**: 26.9% items flagged as ETS-C (vs 0.6% random control, 44.8× enrichment)
27	- **HELLASWAG**: 17.9% items flagged as ETS-C (vs 0.28% random control, 63.9× enrichment)
28	
29	## Interpretation
30	
31	The temporal DIF signal (C% >> random C%) indicates systematic item-level 
32	performance shifts between 2023 and 2024 model cohorts, consistent with 
33	benchmark contamination or benchmark-specific training optimization.
34	
35	Random-split controls confirm that the DIF signal is not an artifact of 
36	the MH procedure or score distribution differences within a single cohort.
37	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-23T19:54:33.811673+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/",
  "description": "Check data subdirectory for plan_028"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/",
    "description": "Check data subdirectory for plan_028"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-23T19:54:33.811806+00:00_

mmlu_bootstrap_results.csv
mmlu_bootstrap_summary.csv
multi_bench_summary.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-23T19:54:33.811932+00:00_

1	# Plan 001b: Matched-Ability DIF Analysis
2	
3	## Background
4	plan_001 found temporal cohort MH-DIF (2023 vs 2024) produced 31.3% ETS C items but enrichment=0.96,
5	indicating DIF captured ability improvement rather than contamination. This analysis controls for
6	ability by running temporal DIF within each accuracy quintile.
7	
8	## Quintile Cohort Sizes
9	
10	| Quintile | N(2023) | N(2024) | Total | Underpowered |
11	|----------|---------|---------|-------|--------------|
12	| 1 | 180 | 162 | 342 | no |
13	| 2 | 406 | 106 | 512 | no |
14	| 3 | 287 | 168 | 455 | no |
15	| 4 | 88 | 197 | 285 | no |
16	| 5 | 119 | 174 | 293 | no |
17	
18	## Per-Quintile DIF Results
19	
20	- **Q1**: 1809 C items (14.5%), FPR=0.1477, enrichment=1.04
21	- **Q2**: 4297 C items (34.4%), FPR=0.3524, enrichment=0.94
22	- **Q3**: 5311 C items (42.5%), FPR=0.4255, enrichment=0.97
23	- **Q4**: 4305 C items (34.4%), FPR=0.3460, enrichment=0.99
24	- **Q5**: 3772 C items (30.2%), FPR=0.3059, enrichment=0.96
25	
26	## Merged Results (threshold: ≥2 quintiles flagged C)
27	
28	- Items flagged: 5938 / 12508 (47.5%)
29	- FPR (clean items): 0.4764
30	- Detection rate (contaminated): 0.4658
31	- Detection rate (unlabeled): 0.4819
32	- **Enrichment: 0.98**
33	
34	## Comparison with plan_001
35	
36	| Metric | plan_001 (raw temporal) | plan_001b (matched-ability) |
37	|--------|------------------------|-----------------------------|
38	| C% | 31.3% | 47.5% |
39	| Enrichment | 0.96 | 0.98 |
40	| FPR | ~0.31 | 0.4764 |
41	
42	## Sensitivity Analysis
43	
44	| Method | N(C) | C% | FPR | Rate(contam) | Enrichment |
45	|--------|------|----|-----|-------------|------------|
46	| >=  1 | 9163 | 73.3% | 0.7362 | 0.7191 | 0.98 |
47	| >=  2 | 5938 | 47.5% | 0.4764 | 0.4658 | 0.98 |
48	| >=  3 | 3182 | 25.4% | 0.2613 | 0.2508 | 0.96 |
49	| CMH | 4165 | 33.3% | 0.3340 | 0.3336 | 1.00 |
50	| Q1_only | 1809 | 14.5% | 0.1477 | 0.1536 | 1.04 |
51	| Q2_only | 4297 | 34.4% | 0.3524 | 0.3303 | 0.94 |
52	| Q3_only | 5311 |
…[truncated 245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 5
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-23T19:54:33.812115+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Audit inline numbers experiments",
  "prompt": "You are auditing data correctness in an academic paper. Your job is to verify all inline numerical claims in experiments.tex (outside of tables) against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\nFirst read experiments.tex:\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex\n\nThen trace every inline number. Key numbers to verify:\n\n### §5.1 Validation (line 9-10):\n- ā = 1.2, b̄ = -0.84 (IRT params from PSN-IRT)\n- N ≥ 80 per cohort threshold\n- TPR 0.68-0.80\n- AUC 0.93-0.94\n- |Δ_MH| ≥ 1.4\n- N_ref=1,080, N_focal=807\n- TPR 0.40-0.95 across a=0.5-2.0\nSource: artifacts/dif_phase2_results.csv, artifacts/sf8_power_sensitivity/, artifacts/mvp_dif_power_sim/\n\n### §5.2 Temporal DIF (line 12-22):\n- 31.3% C items\n- bootstrap 95% CI: [29.4%, 38.1%]\n- cluster bootstrap: [26.7%, 53.2%]\n- DEFF: simple-mean 29.2%, weighted-mean 13.5%\n- ρ=0.999, score shift=+1.77pp under weighted-mean DEFF\n- 99th percentile |Δ_MH| = 1.45 (permutation null)\n- LOFO |ΔC%| ≤ 2.93pp\n- Random splits: 0.62% (2023), 1.3% (2024)\n- ≥24× below temporal C%\n- Ability quintile: 2.9%\n- matched N=638/group, Cohen's d=-0.17, C%=28.9%±0.1%\n- C% range 20.7%-48.4% across 57 subjects\n- mean ≈ 30%\n- KW p=0.78\n- STEM 55.4%, Humanities 64.4%\n- <0.1% variance explained\n- ρ=-0.597\n- 18.3% at |Δ_MH|≥2.0, 10.2% at ≥2.5\nSource: artifacts/plan_001/, artifacts/plan_001_real_data_dif_mmlu/, artifacts/sf1_cluster_bootstrap/, artifacts/mf2_deff_estimation/, artifacts/plan_029_permutation_null/, artifacts/lofo_robustness/, artifacts/difficulty_modeltype_interaction/\n\n### §5.4 Groundtruth (line 44-54):\n- enrichment=0.964, Jaccard=0.206, p=0.88\n- 9,229 annotated items\n- DIF-C 30.7% among web-contaminated, 31.8% among clean\n- χ²=562.7\n- ΔTPR=+0.508 at p=0.5\nSource: artifacts/plan_001_real_data_dif_mmlu/, artifacts/mmlu_li2024_proxy_labels.csv, artifacts/r18_base_instruct_survey/\n\n### §5.5 Structural (line 56-60):\n- 17.7% non-uniform DIF\n- union 47%\n- 28-29% ability-matched convergence\nSource: artifacts/plan_001/, various plan dirs\n\n### §5.6 Semi-synthetic injection (line 80-84):\n- ΔFPR=0.000 across 5 subjects\n- 4/5 with ΔTPR>0.3 at p=0.5\n- within-subject ΔFPR=+0.186\n- k≤5: ΔFPR<0.007\n- k=10: ΔFPR=0.069 (18% of domains)\n- k=20: ΔFPR=0.167\n- k≥30: ΔFPR>0.36\n- difficulty-dependent: ΔTPR≈0.41 vs 0.51 uniform\n- ~20% overestimation\nSource: artifacts/plan_011/, artifacts/plan_011_semi_synthetic_validation/, artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv, artifacts/mixed_mechanism_semisynthetic/\n\n### §5.7 Downstream (line 86-90):\n- ρ=0.997, τ=0.958\n- flip rate ≤2.8%\n- z=-8 to -49\n- 33.6% pairwise rankings reverse among 200 most displaced\n- cohort gap=96.2 positions, 40× random, p<0.001\n- +2.12pp accuracy shift, 0.29pp cohort-differential, d=0.31\n- ±800 individual displacements\nSource: artifacts/plan_032_dif_cleaned_mmlu/, artifacts/score_inflation_analysis/\n\n### §5.8 Cross-benchmark (line 92-118):\n- C% range 17.9% (HellaSwag) to 31.3% (MMLU)\n- knowledge/reasoning 26.9-31.3% vs procedural 17.9-18.9%\n- GSM8K ΔTPR=+0.514\nSource: artifacts/plan_028_multi_bench_dif/\n\nFor EACH number, grep in the relevant artifacts directory for the source value. Report findings as:\n```\n## §5.X [section name] inline numbers\n- [number] in [context] ← [source file:exact value found] ✅ / ⚠️ / ❌\n```\n\nFocus especially on the k=10/20/30 ΔFPR values from summary_by_k_full.csv, as these were recently updated.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "tool_args": {
    "description": "Audit inline numbers experiments",
    "prompt": "You are auditing data correctness in an academic paper. Your job is to verify all inline numerical claims in experiments.tex (outside of tables) against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\nFirst read experiments.tex:\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex\n\nThen trace every inline number. Key numbers to verify:\n\n### §5.1 Validation (line 9-10):\n- ā = 1.2, b̄ = -0.84 (IRT params from PSN-IRT)\n- N ≥ 80 per cohort threshold\n- TPR 0.68-0.80\n- AUC 0.93-0.94\n- |Δ_MH| ≥ 1.4\n- N_ref=1,080, N_focal=807\n- TPR 0.40-0.95 across a=0.5-2.0\nSource: artifacts/dif_phase2_results.csv, artifacts/sf8_power_sensitivity/, artifacts/mvp_dif_power_sim/\n\n### §5.2 Temporal DIF (line 12-22):\n- 31.3% C items\n- bootstrap 95% CI: [29.4%, 38.1%]\n- cluster bootstrap: [26.7%, 53.2%]\n- DEFF: simple-mean 29.2%, weighted-mean 13.5%\n- ρ=0.999, score shift=+1.77pp under weighted-mean DEFF\n- 99th percentile |Δ_MH| = 1.45 (permutation null)\n- LOFO |ΔC%| ≤ 2.93pp\n- Random splits: 0.62% (2023), 1.3% (2024)\n- ≥24× below temporal C%\n- Ability quintile: 2.9%\n- matched N=638/group, Cohen's d=-0.17, C%=28.9%±0.1%\n- C% range 20.7%-48.4% across 57 subjects\n- mean ≈ 30%\n- KW p=0.78\n- STEM 55.4%, Humanities 64.4%\n- <0.1% variance explained\n- ρ=-0.597\n- 18.3% at |Δ_MH|≥2.0, 10.2% at ≥2.5\nSource: artifacts/plan_001/, artifacts/plan_001_real_data_dif_mmlu/, artifacts/sf1_cluster_bootstrap/, artifacts/mf2_deff_estimation/, artifacts/plan_029_permutation_null/, artifacts/lofo_robustness/, artifacts/difficulty_modeltype_interaction/\n\n### §5.4 Groundtruth (line 44-54):\n- enrichment=0.964, Jaccard=0.206, p=0.88\n- 9,229 annotated items\n- DIF-C 30.7% among web-contaminated, 31.8% among clean\n- χ²=562.7\n- ΔTPR=+0.508 at p=0.5\nSource: artifacts/plan_001_real_data_dif_mmlu/, artifacts/mmlu_li2024_proxy_labels.csv, artifacts/r18_base_instruct_survey/\n\n### §5.5 Structural (line 56-60):\n- 17.7% non-uniform DIF\n- union 47%\n- 28-29% ability-matched convergence\nSource: artifacts/plan_001/, various plan dirs\n\n### §5.6 Semi-synthetic injection (line 80-84):\n- ΔFPR=0.000 across 5 subjects\n- 4/5 with ΔTPR>0.3 at p=0.5\n- within-subject ΔFPR=+0.186\n- k≤5: ΔFPR<0.007\n- k=10: ΔFPR=0.069 (18% of domains)\n- k=20: ΔFPR=0.167\n- k≥30: ΔFPR>0.36\n- difficulty-dependent: ΔTPR≈0.41 vs 0.51 uniform\n- ~20% overestimation\nSource: artifacts/plan_011/, artifacts/plan_011_semi_synthetic_validation/, artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv, artifacts/mixed_mechanism_semisynthetic/\n\n### §5.7 Downstream (line 86-90):\n- ρ=0.997, τ=0.958\n- flip rate ≤2.8%\n- z=-8 to -49\n- 33.6% pairwise rankings reverse among 200 most displaced\n- cohort gap=96.2 positions, 40× random, p<0.001\n- +2.12pp accuracy shift, 0.29pp cohort-differential, d=0.31\n- ±800 individual displacements\nSource: artifacts/plan_032_dif_cleaned_mmlu/, artifacts/score_inflation_analysis/\n\n### §5.8 Cross-benchmark (line 92-118):\n- C% range 17.9% (HellaSwag) to 31.3% (MMLU)\n- knowledge/reasoning 26.9-31.3% vs procedural 17.9-18.9%\n- GSM8K ΔTPR=+0.514\nSource: artifacts/plan_028_multi_bench_dif/\n\nFor EACH number, grep in the relevant artifacts directory for the source value. Report findings as:\n```\n## §5.X [section name] inline numbers\n- [number] in [context] ← [source file:exact value found] ✅ / ⚠️ / ❌\n```\n\nFocus especially on the k=10/20/30 ΔFPR values from summary_by_k_full.csv, as these were recently updated.",
    "model": "sonnet"
  }
}
````

</details>

---


### Tool call

_source line 84 · 2026-05-23T19:54:33.812387+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# plan_001 says: ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089)\n# plan_001b quintile sizes: Q1: 180+162=342, Q2: 406+106=512, ...\n# The N_ref and N_focal in paper are ~2600/~2600\n# This seems to refer to Q1-2 vs Q4-5 across both years combined\n# Q1: 180+162=342 total, Q2: 406+106=512, Q1+Q2=854\n# Q4: 88+197=285, Q5: 119+174=293, Q4+Q5=578\n# Those are per-quintile within temporal, not the overall ability cohort sizes\n\n# From plan_001_report: Q1-2 N=2092, Q4-5 N=2089\n# That's across all years\n# Neither matches 2600/2600\n\n# Let's check metabench_cohort_analysis.csv for group sizes\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_cohort_analysis.csv') as f:\n    content = f.read()\nprint(content[:3000])\n\"\n",
  "description": "Check metabench_cohort_analysis for ability quintile sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# plan_001 says: ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089)\n# plan_001b quintile sizes: Q1: 180+162=342, Q2: 406+106=512, ...\n# The N_ref and N_focal in paper are ~2600/~2600\n# This seems to refer to Q1-2 vs Q4-5 across both years combined\n# Q1: 180+162=342 total, Q2: 406+106=512, Q1+Q2=854\n# Q4: 88+197=285, Q5: 119+174=293, Q4+Q5=578\n# Those are per-quintile within temporal, not the overall ability cohort sizes\n\n# From plan_001_report: Q1-2 N=2092, Q4-5 N=2089\n# That's across all years\n# Neither matches 2600/2600\n\n# Let's check metabench_cohort_analysis.csv for group sizes\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_cohort_analysis.csv') as f:\n    content = f.read()\nprint(content[:3000])\n\"\n",
    "description": "Check metabench_cohort_analysis for ability quintile sizes"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-23T19:54:33.812529+00:00_

cohort,n_models,mean_accuracy,std_accuracy,sufficient_for_dif
2021-H1,5,0.239702590342181,0.02251580568448245,False
2022-H1,9,0.2349163202217247,0.019901996519650432,False
2022-H2,4,0.28801566997121847,0.03458235255278323,False
2023-H1,287,0.45751624883419567,0.18755077105542467,True
2023-H2,966,0.6011858414755343,0.12542801115177318,True
2024-H1,656,0.5978932020092507,0.16168883167389278,True
2024-H2,2,0.5235849056603773,0.2746242404860889,False

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-23T19:54:33.812651+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
  "description": "List plan_001_real_data_dif_mmlu report files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
    "description": "List plan_001_real_data_dif_mmlu report files"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-23T19:54:33.812789+00:00_

plan_001_report.md
plan_001_report_00ca1f.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-23T19:54:33.812906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-23T19:54:33.813026+00:00_

1	benchmark,n_items,n_ref,n_foc,n_ets_a,n_ets_b,n_ets_c,pct_c,random_pct_c,status
2	mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
3	winogrande,1267,1017,803,612,271,384,30.3,0.32,OK
4	truthfulqa,817,1080,807,398,176,243,29.7,0.37,OK
5	arc,1172,1080,807,642,215,315,26.9,0.6,OK
6	gsm8k,1319,1017,804,825,245,249,18.9,0.3,PRIOR
7	hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-23T19:54:33.813142+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
  "description": "List plan_001_real_data_dif_mmlu contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
    "description": "List plan_001_real_data_dif_mmlu contents"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-23T19:54:33.813263+00:00_

data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-23T19:54:33.813375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.csv\" | xargs grep -l \"spearman\\|kendall\\|flip\\|rho\\|tau\" 2>/dev/null | head -20",
  "description": "Find CSV files containing rank correlation or flip metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.csv\" | xargs grep -l \"spearman\\|kendall\\|flip\\|rho\\|tau\" 2>/dev/null | head -20",
    "description": "Find CSV files containing rank correlation or flip metrics"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-23T19:54:33.813495+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/rank_changes.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_model_accuracy.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/within_subject_injection_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/model_metadata.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/mf2_stable_rho.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/benchmark_rho_summary.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_rl_models_18eb0d.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_rl_models.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/degradation_curves.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/theta_estimates.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/injection_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_temporal_granularity/temporal_granularity_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_020/metric_correlations.csv
/home/ubuntu/.agent-ml-research-idea_g
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-23T19:54:33.813629+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-23T19:54:33.813803+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	\looseness=-1
10	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and AUC of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
11	
12	\subsection{Temporal DIF: ${\sim}$29\% of Items Exhibit Differential Functioning}
13	\label{sec:temporal}
14	
15	\looseness=-1
16	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift
…[truncated 10400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-23T19:54:33.813943+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | head -80",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | head -80",
    "description": "List artifacts directory"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-23T19:54:33.814063+00:00_

__pycache__
_project
arr_checklist_draft.md
artifacts_qc_report.md
build_response_matrix.py
data_audit_part1.md
deff_parametric_curve
dif_diagnostic.py
dif_diagnostic_output.log
dif_diagnostic_pvalue_dist.pdf
dif_diagnostic_tpr_comparison.csv
dif_phase2_param_distribution.pdf
dif_phase2_power_curves.pdf
dif_phase2_results.csv
dif_phase2_simulation.py
dif_power_curves.pdf
dif_power_results.csv
dif_power_simulation.py
difficulty_modeltype_interaction
dream_reports
experiment_summary.md
irt_scale_analysis.json
irt_scale_analysis.md
item_metadata.csv
k3_power_simulation
literature_survey_d011.md
lofo_robustness
manifest.yaml
metabench_cohort_analysis.csv
metabench_ctt_stats.csv
metabench_data
metabench_data_summary.md
metabench_explore.py
metabench_model_accuracy.csv
metabench_model_list.txt
metabench_rl_models.csv
metabench_subject_stats.csv
metabench_summary.json
mf1_lofo_power_calibration
mf1_worked_examples
mf2_deff_estimation
mf2_practical_significance
mf2_rho_degradation
mixed_mechanism_semisynthetic
mmlu_cf_analysis.json
mmlu_cf_analysis.md
mmlu_li2024_proxy_labels.csv
mmlu_redux
model_metadata.csv
mvp_dif_power_sim
novelty_rebuttal_draft.md
plan_001
plan_001_real_data_dif_mmlu
plan_001b
plan_004
plan_004_data_availability.md
plan_010
plan_011
plan_011_semi_synthetic_validation
plan_012
plan_012_irt_theta_conditioning
plan_013
plan_013_q3_local_independence
plan_013_supplement
plan_014
plan_015
plan_016
plan_016_supplement
plan_016_within_subject_semi_synthetic
plan_017
plan_017_supplement
plan_018
plan_019
plan_020
plan_021
plan_022
plan_023
plan_024
plan_026
plan_027_temporal_overlap

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-23T19:54:33.814192+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv",
  "description": "Read DIF phase 2 results CSV"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_results.csv",
    "description": "Read DIF phase 2 results CSV"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-23T19:54:33.814311+00:00_

n_per_group,delta,method,tpr_raw,fpr_raw,tpr_bh,fpr_bh,ets_c_tpr,ets_c_fpr,auc,n_reps,verdict
50,0.8,MH,0.2411,0.0273,0.0127,0.0001,0.2346,0.027,0.7302,1000,N/A
50,0.8,LR,0.3036,0.0641,0.0334,0.0011,,,0.7105,1000,N/A
50,1.0,MH,0.3409,0.0278,0.0355,0.0001,0.3241,0.0276,0.7736,1000,N/A
50,1.0,LR,0.4065,0.0648,0.0813,0.0019,,,0.7669,1000,N/A
50,1.2,MH,0.4382,0.0286,0.081,0.0002,0.4111,0.0283,0.8042,1000,N/A
50,1.2,LR,0.5024,0.0657,0.1508,0.0026,,,0.8129,1000,N/A
50,1.4,MH,0.5227,0.0293,0.1572,0.0004,0.4795,0.0291,0.8119,1000,N/A
50,1.4,LR,0.5818,0.0678,0.2545,0.0037,,,0.8459,1000,N/A
50,1.6,MH,0.588,0.0293,0.2234,0.0005,0.5236,0.029,0.8099,1000,N/A
50,1.6,LR,0.6425,0.0689,0.336,0.0047,,,0.8726,1000,N/A
80,0.8,MH,0.3931,0.0335,0.0661,0.0003,0.3911,0.0334,0.8037,1000,N/A
80,0.8,LR,0.4155,0.0598,0.0951,0.0014,,,0.7777,1000,N/A
80,1.0,MH,0.5181,0.0347,0.1608,0.0006,0.5136,0.0346,0.8544,1000,N/A
80,1.0,LR,0.5358,0.0622,0.2035,0.0026,,,0.8327,1000,N/A
80,1.2,MH,0.6214,0.0357,0.2862,0.001,0.6075,0.0357,0.8793,1000,N/A
80,1.2,LR,0.6333,0.0638,0.3329,0.0034,,,0.8717,1000,N/A
80,1.4,MH,0.7045,0.0361,0.4001,0.0016,0.6823,0.0361,0.895,1000,PASS
80,1.4,LR,0.7186,0.065,0.4496,0.0046,,,0.9003,1000,N/A
80,1.6,MH,0.7645,0.0386,0.4864,0.0019,0.7223,0.0386,0.8936,1000,PASS
80,1.6,LR,0.7726,0.068,0.5365,0.0062,,,0.9242,1000,N/A
100,0.8,MH,0.4813,0.0353,0.1215,0.0005,0.4793,0.0347,0.8358,1000,N/A
100,0.8,LR,0.4837,0.0587,0.1421,0.0018,,,0.8075,1000,N/A
100,1.0,MH,0.6089,0.0368,0.2729,0.0011,0.6058,0.0364,0.8816,1000,N/A
100,1.0,LR,0.6104,0.0614,0.2952,0.0033,,,0.8609,1000,N/A
100,1.2,MH,0.7088,0.0399,0.4082,0.0018,0.7013,0.0394,0.9103,1000,N/A
100,1.2,LR,0.7094,0.0651,0.4345,0.0047,,,0.8992,1000,N/A
100,1.4,MH,0.7745,0.0407,0.5211,0.0022,0.7582,0.0401,0.9231,1000,PASS
100,1.4,LR,0.7737,0.0665,0.5462,0.0059,,,0.923,1000,N/A
100,1.6,MH,0.8241,0.0429,0.6066,0.0029,0.7966,0.0424,0.9254,1000,PASS
100,1.6,LR,0.8214,0.069,0.629,0.0067,,,0.9405,1000,N/A

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-23T19:54:33.814432+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/",
  "description": "List plan_001 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/",
    "description": "List plan_001 directory"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-23T19:54:33.814542+00:00_

cross_analysis.csv
dif_results_ability.csv
dif_results_temporal.csv
dif_summary.csv
domain_specificity.csv
neg_disc_sensitivity.csv
plan_001_analysis.py
plan_001_report.md
within_family_dif.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-23T19:54:33.814659+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
  "description": "List plan_001_real_data_dif_mmlu directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
    "description": "List plan_001_real_data_dif_mmlu directory"
  }
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-23T19:54:33.814812+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Audit discussion numbers",
  "prompt": "You are auditing data correctness in an academic paper. Your job is to verify all numerical claims in discussion.tex against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\nFirst read discussion.tex:\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex\n\nKey numbers to verify:\n\n### §6.1 Temporal DIF as Structured Signal (line 9):\n- base models N=1,409, 60.1% reference-favoring, ρ=-0.570\n- instruct models N=478, 65.6% focal-favoring, ρ=-0.079\n- χ²=562.7, p<10^-124\nSource: artifacts/r18_base_instruct_survey/ or artifacts/r18_base_vs_instruct_dif/\n\n### §6.1 (line 12):\n- Composition downsampling Δ=1.08pp\nSource: artifacts/r22_composition_control/\n\n### §6.1 (line 14-15):\n- C% 29.2%\n- cluster bootstrap CI [26.7%, 53.2%]\n- Jaccard=0.206\n- OR=4.75\nSource: artifacts/sf1_cluster_bootstrap/, artifacts/plan_001_real_data_dif_mmlu/, artifacts/r18_base_instruct_survey/\n\n### §6.2 Protocol (line 20-21):\n- AUROC=0.60\n- ≥500 models threshold\n- K=3 reference\n- C%≈12% for MMLU\n- 20× random-split baseline\nSource: Check various dirs for AUROC, artifacts/k3_power_simulation/\n\nFor EACH number, grep in the relevant artifacts directories for the source value. Report findings as:\n```\n## Discussion §6.X inline numbers\n- [number] in [context] ← [source file:exact value found] ✅ / ⚠️ / ❌\n```\n\nBe thorough.",
  "model": "sonnet"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "tool_args": {
    "description": "Audit discussion numbers",
    "prompt": "You are auditing data correctness in an academic paper. Your job is to verify all numerical claims in discussion.tex against source data in the artifacts/ directory.\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/\n\nFirst read discussion.tex:\n/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex\n\nKey numbers to verify:\n\n### §6.1 Temporal DIF as Structured Signal (line 9):\n- base models N=1,409, 60.1% reference-favoring, ρ=-0.570\n- instruct models N=478, 65.6% focal-favoring, ρ=-0.079\n- χ²=562.7, p<10^-124\nSource: artifacts/r18_base_instruct_survey/ or artifacts/r18_base_vs_instruct_dif/\n\n### §6.1 (line 12):\n- Composition downsampling Δ=1.08pp\nSource: artifacts/r22_composition_control/\n\n### §6.1 (line 14-15):\n- C% 29.2%\n- cluster bootstrap CI [26.7%, 53.2%]\n- Jaccard=0.206\n- OR=4.75\nSource: artifacts/sf1_cluster_bootstrap/, artifacts/plan_001_real_data_dif_mmlu/, artifacts/r18_base_instruct_survey/\n\n### §6.2 Protocol (line 20-21):\n- AUROC=0.60\n- ≥500 models threshold\n- K=3 reference\n- C%≈12% for MMLU\n- 20× random-split baseline\nSource: Check various dirs for AUROC, artifacts/k3_power_simulation/\n\nFor EACH number, grep in the relevant artifacts directories for the source value. Report findings as:\n```\n## Discussion §6.X inline numbers\n- [number] in [context] ← [source file:exact value found] ✅ / ⚠️ / ❌\n```\n\nBe thorough.",
    "model": "sonnet"
  }
}
````

</details>

---


### Tool result

_source line 104 · 2026-05-23T19:54:33.814972+00:00_

data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-23T19:54:33.815092+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/",
  "description": "List mf2_deff_estimation directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/",
    "description": "List mf2_deff_estimation directory"
  }
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-23T19:54:33.815214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-23T19:54:33.815345+00:00_

1	# Plan 001: METABENCH Real-Data MH-DIF Analysis
2	
3	## 1. Data & Setup
4	
5	- Response matrix: **5227 models × 12508 items** (binary, MMLU)
6	- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
7	- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
8	- Li et al. annotations: 9229 annotated items
9	
10	## 2. ETS Classification
11	
12	| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
13	|--------|--------|-------|---|---|---|----|-------------|------------|
14	| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
15	| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
16	| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
17	
18	## 3. Li et al. Proxy Validation
19	
20	| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
21	|--------|-------------|---------------|--------------|------------------|------------|
22	| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
23	| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |
24	
25	## 4. Within-Family Analysis
26	
27	- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
28	- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)
29	
30	### Cross-cohort vs within-family overlap
31	
32	- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
33	- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804
34	
35	## 5. Domain Specificity
36	
37	Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)
38	
39	Top 15 subjects by C rate (temporal cohort):
40	
41	| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
42	|---------|-------|---|-----|----------|----------|------|
43	| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
44	| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
45	| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
46	| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-23T19:54:33.815487+00:00_

deff_results.csv
deff_summary.md
mf2_deff_estimation.py
mf2_deff_estimation_v3.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-23T19:54:33.815608+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/",
  "description": "List lofo_robustness directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/",
    "description": "List lofo_robustness directory"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-23T19:54:33.815734+00:00_

lofo_results.csv
lofo_results.md
lofo_robustness.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-23T19:54:33.815861+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/ 2>/dev/null || echo \"DIR NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_034",
  "description": "Check plan_034 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/ 2>/dev/null || echo \"DIR NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_034",
    "description": "Check plan_034 directory"
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-23T19:54:33.815975+00:00_

data
k30_40_50_nontarget.csv
k30_40_50_results.csv
k30_40_50_summary.csv
multi_subject_injection_results.csv
non_target_fpr_results.csv
plan_034_k30_40_50.py
plan_034_multi_subject_injection.py
plan_034_report.md
report
summary_by_k.csv
summary_by_k_full.csv
plan_034
plan_034_multi_subject_injection

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 113 · 2026-05-23T19:54:33.816109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/benchmark_rho_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/benchmark_rho_summary.csv"
  }
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-23T19:54:33.816238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/",
  "description": "List plan_011 directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/",
    "description": "List plan_011 directories"
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-23T19:54:33.816357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-23T19:54:33.816475+00:00_

1	benchmark,n_items_total,n_items_c,n_items_stable,pct_c,n_models,spearman_rho,spearman_p,kendall_tau,flip_rate
2	TruthfulQA,817,243,574,29.74,5228,0.997123,0.00e+00,0.958635,0.020682
3	ARC,1172,315,857,26.88,5227,0.996209,0.00e+00,0.953791,0.023104
4	WinoGrande,1267,384,883,30.31,6558,0.994255,0.00e+00,0.943166,0.028417
5	GSM8K,1319,249,1070,18.88,6702,0.999303,0.00e+00,0.984311,0.007844
6	HellaSwag,10042,1797,8245,17.89,5227,0.998623,0.00e+00,0.972166,0.013917
7	MMLU,12508,3918,8590,31.32,5227,0.9965,NA,NA,NA
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-23T19:54:33.816600+00:00_

1	\enlargethispage{14\baselineskip}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\subsection{Temporal DIF as Structured Signal}
6	\label{sec:disc_temporal}
7	
8	\looseness=-1
9	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}---and this is by design (``temporal'' denotes release-year cohorts that differ simultaneously in architecture, data, and methodology; \Cref{sec:cohorts}). Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($\rho = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). Following the impact-bias framework~\citep{camilli1994methods}, this reversal reflects structured item-level bias rather than uniform group impact, validating DIF as a mechanism-agnostic diagnostic (\Cref{app:mechanism_discussion}).
10	
11	\looseness=-1
12	Composition downsampling ($\Delta = 1.08$\,pp), base-only, and instruct-only temporal analyses independently confirm DIF is not an artifact of cohort structure (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}).
13	
14	\looseness=-2
15	Three features distinguish LLM temporal DIF from educational settings: (1)~C\% (29.2\%; cluster bootstrap CI: $[26.7\%, 53.2\%]$) substantially exceeds typical educational DIF rates~\citep{clauser1998dif}; (2)~DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$), unlike educational settings where DIF correlates with construct-irrelevant variance; (3)~the near-independence admits two interpretations: DIF captures a broader signal---including capability evolution and training methodology shifts---of which contamination is one component, or DIF and contamination detection measure distinct constructs. The base/instruct reversal (OR $= 4.75$; \Cref{app:mechanism_discussion}) favors the former; either interpretation supports periodic DIF audits.
16	
17	\subsection{Recommended DIF Audit 
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-23T19:54:33.816759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/benchmark_rho_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/benchmark_rho_summary.csv"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-23T19:54:33.816878+00:00_

1	benchmark,n_items_total,n_items_c,n_items_stable,pct_c,n_models,spearman_rho,spearman_p,kendall_tau,flip_rate
2	TruthfulQA,817,243,574,29.74,5228,0.997123,0.00e+00,0.958635,0.020682
3	ARC,1172,315,857,26.88,5227,0.996209,0.00e+00,0.953791,0.023104
4	WinoGrande,1267,384,883,30.31,6558,0.994255,0.00e+00,0.943166,0.028417
5	GSM8K,1319,249,1070,18.88,6702,0.999303,0.00e+00,0.984311,0.007844
6	HellaSwag,10042,1797,8245,17.89,5227,0.998623,0.00e+00,0.972166,0.013917
7	MMLU,12508,3918,8590,31.32,5227,0.9965,0.00e+00,0.959986,0.020007
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-23T19:54:33.817005+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | sort",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | sort",
    "description": "List artifacts directory"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-23T19:54:33.817131+00:00_

__pycache__
_project
arr_checklist_draft.md
artifacts_qc_report.md
build_response_matrix.py
data_audit_part1.md
deff_parametric_curve
dif_diagnostic.py
dif_diagnostic_output.log
dif_diagnostic_pvalue_dist.pdf
dif_diagnostic_tpr_comparison.csv
dif_phase2_param_distribution.pdf
dif_phase2_power_curves.pdf
dif_phase2_results.csv
dif_phase2_simulation.py
dif_power_curves.pdf
dif_power_results.csv
dif_power_simulation.py
difficulty_modeltype_interaction
dream_reports
experiment_summary.md
irt_scale_analysis.json
irt_scale_analysis.md
item_metadata.csv
k3_power_simulation
literature_survey_d011.md
lofo_robustness
manifest.yaml
metabench_cohort_analysis.csv
metabench_ctt_stats.csv
metabench_data
metabench_data_summary.md
metabench_explore.py
metabench_model_accuracy.csv
metabench_model_list.txt
metabench_rl_models.csv
metabench_subject_stats.csv
metabench_summary.json
mf1_lofo_power_calibration
mf1_worked_examples
mf2_deff_estimation
mf2_practical_significance
mf2_rho_degradation
mixed_mechanism_semisynthetic
mmlu_cf_analysis.json
mmlu_cf_analysis.md
mmlu_li2024_proxy_labels.csv
mmlu_redux
model_metadata.csv
mvp_dif_power_sim
novelty_rebuttal_draft.md
plan_001
plan_001_real_data_dif_mmlu
plan_001b
plan_004
plan_004_data_availability.md
plan_010
plan_011
plan_011_semi_synthetic_validation
plan_012
plan_012_irt_theta_conditioning
plan_013
plan_013_q3_local_independence
plan_013_supplement
plan_014
plan_015
plan_016
plan_016_supplement
plan_016_within_subject_semi_synthetic
plan_017
plan_017_supplement
plan_018
plan_019
plan_020
plan_021
plan_022
plan_023
plan_024
plan_026
plan_027_temporal_overlap
plan_028_bootstrap_ci
plan_028_multi_bench_dif
plan_029_permutation_null
plan_030_odds_ratio
plan_031_temporal_granularity
plan_032_dif_cleaned_mmlu
plan_033_subject_dif_concentration
plan_034
plan_034_multi_subject_injection
plan_035_q3_inflation_sim
plan_036_growing_pains
plan_036_growing_pains_lookup
predictive_model
psn_irt_item_parameters.csv
r14_mf1_domain_profile
r14_sf5_gem
…[truncated 1102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-23T19:54:33.817258+00:00_

dose_response_summary.csv
injection_results.csv
per_item_results.csv
plan_011_analysis.py
plan_011_report.md
data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-23T19:54:33.817375+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/",
  "description": "List plan_016 directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/",
    "description": "List plan_016 directories"
  }
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-23T19:54:33.817496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv",
  "description": "Read summary_by_k_full.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv",
    "description": "Read summary_by_k_full.csv"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-23T19:54:33.817604+00:00_

plan_016_report.md
plan_016_within_subject_injection.py
within_subject_dose_response.csv
within_subject_injection_results.csv
data
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 126 · 2026-05-23T19:54:33.817735+00:00_

k,p,mean_tpr_target,mean_delta_tpr,std_delta_tpr,mean_fpr_non_target,mean_delta_fpr_non_target,std_delta_fpr_non_target
1,0.1,0.3906,0.0743,0.0531,0.3191,0.0019,0.0016
1,0.3,0.559,0.2427,0.0456,0.3192,0.002,0.0012
1,0.5,0.834,0.5177,0.0497,0.3188,0.0016,0.0015
2,0.1,0.3521,0.0383,0.0292,0.3169,0.0031,0.0015
2,0.3,0.5012,0.1874,0.0493,0.3168,0.003,0.0017
2,0.5,0.8071,0.4933,0.0324,0.3152,0.0015,0.0019
3,0.1,0.3305,0.0225,0.0208,0.3186,0.0022,0.0011
3,0.3,0.4678,0.1598,0.0662,0.3172,0.0007,0.0025
3,0.5,0.7779,0.47,0.0934,0.3153,-0.0011,0.0032
5,0.1,0.3135,0.0004,0.023,0.3198,0.0038,0.0023
5,0.3,0.4345,0.1215,0.0225,0.3157,-0.0002,0.0039
5,0.5,0.7336,0.4205,0.041,0.3224,0.0065,0.0066
10,0.1,0.3176,0.0086,0.0123,0.3164,0.0012,0.0027
10,0.3,0.4076,0.0986,0.0152,0.3406,0.0255,0.0115
10,0.5,0.6696,0.3606,0.0269,0.3841,0.069,0.0302
20,0.1,0.3332,0.0217,0.0101,0.3223,0.0013,0.0039
20,0.3,0.3979,0.0864,0.0182,0.3927,0.0717,0.0224
20,0.5,0.6106,0.2992,0.0299,0.4883,0.1673,0.0294
30,0.1,0.3355,0.0237,0.0086,0.3374,0.0259,0.006
30,0.3,0.3663,0.0546,0.0226,0.4914,0.1798,0.0205
30,0.5,0.471,0.1593,0.0345,0.6734,0.3618,0.0255
40,0.1,0.3348,0.0222,0.0067,0.3566,0.0407,0.0234
40,0.3,0.3722,0.0595,0.0226,0.5699,0.254,0.0665
40,0.5,0.53,0.2174,0.0439,0.7214,0.4056,0.0536
50,0.1,0.344,0.0296,0.0014,0.3636,0.0559,0.0272
50,0.3,0.4753,0.1608,0.0291,0.6109,0.3032,0.0639
50,0.5,0.7535,0.439,0.0281,0.7658,0.4581,0.0527

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-23T19:54:33.817871+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv | head -20",
  "description": "Read temporal DIF results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv | head -20",
    "description": "Read temporal DIF results"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-23T19:54:33.817989+00:00_

item_id,subject,alpha_mh,delta_mh,se,p_value,ets_class,li_label,li_contamination_type
abstract_algebra.1,abstract_algebra,0.8673811041189408,0.3343505559632721,0.2921867891177819,0.27995385252579175,A,False,clean
abstract_algebra.10,abstract_algebra,0.5141246508049961,1.5634303993406418,0.36471274316626207,1.8840975857581377e-05,C,False,clean
abstract_algebra.100,abstract_algebra,0.45562394251510224,1.8473056183645777,0.4442953571627415,3.3721937472974695e-05,C,,no_annotation
abstract_algebra.11,abstract_algebra,0.7175060366563377,0.780138707124792,0.2484055209632857,0.0016556553694112575,A,False,clean
abstract_algebra.12,abstract_algebra,1.4899881312460284,-0.937105162649532,0.2813290278113714,0.0007921945558931887,A,False,clean
abstract_algebra.13,abstract_algebra,1.6623708623468896,-1.1943753123055647,0.24349932220813678,1.1074001383670762e-06,B,False,clean
abstract_algebra.14,abstract_algebra,0.47050921142342894,1.7717583941763377,0.39879705520766956,7.794093909940791e-06,C,False,clean
abstract_algebra.15,abstract_algebra,1.274074494967226,-0.5692170675088077,0.8253399422382749,0.6085683132700959,A,False,clean
abstract_algebra.16,abstract_algebra,0.8190200681472496,0.46916972666288403,0.264861289970129,0.08118193827845621,A,False,clean
abstract_algebra.17,abstract_algebra,1.073117016076642,-0.16583365498585692,0.2883154944248265,0.5952450889614067,A,False,clean
abstract_algebra.18,abstract_algebra,0.5588024066034348,1.36760446045332,0.32138779261988615,1.9024352303942393e-05,B,True,input_and_label
abstract_algebra.2,abstract_algebra,1.955059888825436,-1.5754889426003047,0.2831692496720547,1.146525685502553e-08,C,True,input_only
abstract_algebra.20,abstract_algebra,0.5171438254638294,1.5496704893224662,0.25495047752248373,1.5142136433610176e-09,C,False,clean
abstract_algebra.21,abstract_algebra,1.6643179897220297,-1.1971262457757967,0.33000555981065327,0.0004076914717419111,B,False,clean
abstract_algebra.22,abstract_algebra,0.5389512892206797,1.4526056989518408,0
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 129 · 2026-05-23T19:54:33.818129+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv",
  "description": "Read DIF summary CSV"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv",
    "description": "Read DIF summary CSV"
  }
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-23T19:54:33.818251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-23T19:54:33.818360+00:00_

cohort_type,item_filter,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,fpr_vs_li_clean,enrichment_ratio
temporal,all,12508,6332,2258,3918,31.323952670291018,0.31840974212034384,0.9641535548797142
ability,all,12508,11052,1093,363,2.9021426287176206,0.026862464183381087,1.1949300411522636
temporal,non_neg_disc,10582,5327,1830,3425,32.36628236628237,0.3257975913796746,0.969539159262983

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-23T19:54:33.818499+00:00_

1	# Plan 011: Semi-Synthetic DIF Validation
2	
3	## 1. Objective
4	
5	Inject known **differential** contamination into real MMLU response data and test
6	whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find
7	enrichment was due to Li et al. labels being non-differential (global contamination)
8	rather than a fundamental limitation of MH-DIF.
9	
10	## 2. Setup
11	
12	- **Baseline items**: 500 (clean in Li et al. + ETS A in plan_001 ability DIF)
13	- **Contaminated per run**: 100 of 500
14	- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
15	- **Seeds per p**: 5
16	
17	### Cohort definitions
18	
19	- **ability**: ref N=2092, foc N=2089, foc inject N=2089
20	- **temporal**: ref N=1080, foc N=807, foc inject N=787
21	
22	> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction (ref max=0.6319, foc min=0.6772). All focal models used for injection. MH stratification handles ability matching.
23	
24	### MH variants
25	
26	| Variant | Matching variable | Rationale |
27	|---------|-------------------|-----------|
28	| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |
29	| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |
30	| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |
31	
32	## 3. Results by MH Variant
33	
34	### Standard MH
35	
36	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
37	|--------|---|----------------|----------------|------|-----------|----------|
38	| ability | 0.0 | 0.594±0.053 | 0.611±0.013 | +0.000 | 0.96 | 0.4231 |
39	| ability | 0.3 | 0.700±0.057 | 0.609±0.026 | +0.106 | 1.58 | 0.2555 |
40	| ability | 0.5 | 0.760±0.046 | 0.600±0.021 | +0.166 | 2.21 | 0.0067 |
41	| ability | 0.7 | 0.806±0.036 | 0.598±0.030
…[truncated 5386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-23T19:54:33.818659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_report.md"
  }
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-23T19:54:33.818810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_results.csv",
  "description": "Read DEFF results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_results.csv",
    "description": "Read DEFF results"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-23T19:54:33.818958+00:00_

1	# Plan 016: Within-Subject Semi-Synthetic Injection
2	
3	## Objective
4	
5	Verify that MH-DIF detects differential contamination **within individual subjects**,
6	not just globally. This validates plan_014's finding that within-subject temporal
7	C% = 38.1% reflects real signal, not method failure.
8	
9	## Setup
10	
11	- **Temporal cohort**: ref=2023 (1080 models), foc=2024 (807 models)
12	- **Focal injection subset**: 787 models (ability overlap with ref)
13	- **Contamination fraction**: 20% of items per subject
14	- **Injection probabilities**: [0.0, 0.5, 1.0]
15	- **Seeds per p**: 5
16	- **Matching**: within-subject purified total score + cross-subject total score
17	
18	### Subjects
19	
20	| Subject | N items | N contaminated | N baseline | Strata |
21	|---------|---------|----------------|------------|--------|
22	| business_ethics | 93 | 18 | 75 | 3 |
23	| human_aging | 203 | 40 | 163 | 5 |
24	| professional_medicine | 248 | 49 | 199 | 5 |
25	| formal_logic | 109 | 21 | 88 | 5 |
26	| high_school_statistics | 181 | 36 | 145 | 5 |
27	
28	## Results: Within-Subject Matching
29	
30	Matching variable = purified total score on current subject's items (minus studied item).
31	
32	### Per-Subject Dose-Response (Within)
33	
34	| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
35	|---------|---|----------------|----------------|------|-----------|----------|
36	| business_ethics | 0.0 | 0.600±0.072 | 0.563±0.017 | +0.000 | 1.24 | 0.5990 |
37	| business_ethics | 0.5 | 0.522±0.084 | 0.603±0.017 | -0.078 | 0.78 | 0.5957 |
38	| business_ethics | 1.0 | 1.000±0.000 | 0.629±0.017 | +0.400 | inf | 0.0012 |
39	| formal_logic | 0.0 | 0.333±0.158 | 0.409±0.038 | +0.000 | 0.92 | 0.2169 |
40	| formal_logic | 0.5 | 0.790±0.080 | 0.500±0.033 | +0.457 | 4.21 | 0.0254 |
41	| formal_logic | 1.0 | 1.000±0.000 | 0.584±0.019 | +0.667 | inf | 0.0001 |
42	| high_school_statistics | 0.0 | 0.472±0.059 | 0.407±0.015 | +0.000 | 1.35 | 0.5720 |
43	| high_school_stat
…[truncated 6962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-23T19:54:33.819108+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/",
  "description": "List r18_base_instruct_survey directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/",
    "description": "List r18_base_instruct_survey directory"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-23T19:54:33.819229+00:00_

&lt;persisted-output>
Output too large (3.1MB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/45ef05ff-ecb8-4f6a-b1ca-47b9fb08b347/tool-results/bvrtdah6q.txt

Preview (first 2KB):
item_id,subject,icc,deff_weighted,deff_simple,delta_mh,se,original_chi2,adj_chi2_weighted,adj_chi2_simple,original_p,adj_p_weighted,adj_p_simple,original_ets,adj_ets_weighted,adj_ets_simple
abstract_algebra.1,abstract_algebra,0.013912049164125678,4.526453396401198,1.8597646383429667,0.3343505559632721,0.2921867891177819,1.309431992411688,0.2892843199165079,0.7040847886958319,0.2799538525257917,0.5906795202641578,0.40141454064518933,A,A,A
abstract_algebra.10,abstract_algebra,0.09101276333426861,24.070093024370124,6.6245887740578,1.5634303993406418,0.364712743166262,18.376179665761835,0.7634444805492275,2.773935151676707,1.8840975857581377e-05,0.3822527262801475,0.09581035656029935,C,A,A
abstract_algebra.100,abstract_algebra,0.019416456948436724,5.921721433277835,2.1999370394133893,1.8473056183645775,0.4442953571627415,17.287570026614276,2.9193487436718435,7.858211265547848,3.3721937472974695e-05,0.0875231818999539,0.005059041739335135,C,A,C
abstract_algebra.11,abstract_algebra,0.023908224695881136,7.060303495628978,2.4775282862054544,0.780138707124792,0.2484055209632857,9.86327550944433,1.3970044652543148,3.9810950148830697,0.0016556553694112,0.23722576531455408,0.046013641021366736,A,A,A
abstract_algebra.12,abstract_algebra,0.03871576848259596,10.813748618125544,3.3926344922244303,-0.937105162649532,0.2813290278113714,11.095517688719404,1.0260565582337997,3.2704724644370593,0.0007921945558931,0.3110866717158981,0.07053730628876098,A,A,A
abstract_algebra.13,abstract_algebra,0.04663176711791928,12.820311414455166,3.8818432078874117,-1.1943753123055647,0.2434993222081367,24.059473679892545,1.8766684288780218,6.197950919554596,1.1074001383670762e-06,0.17071328613864112,0.012789829818118159,B,A,B
abstr
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-23T19:54:33.819378+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv",
  "description": "Read LOFO results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv",
    "description": "Read LOFO results"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-23T19:54:33.819493+00:00_

family,n_models_total,n_models_ref,n_models_foc,c_pct_full,c_pct_lofo,delta_c_pct
mistral,547,547,0,31.32,22.47,-8.85
llama-3,315,0,315,31.32,24.06,-7.26
llama-2,161,161,0,31.32,31.48,0.16
mixtral,120,0,120,31.32,34.26,2.93
solar,91,0,91,31.32,31.01,-0.31

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 140 · 2026-05-23T19:54:33.819605+00:00_

base_instruct_survey.md
model_type_classification.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-23T19:54:33.819739+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/",
  "description": "List r18_base_vs_instruct_dif directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/",
    "description": "List r18_base_vs_instruct_dif directory"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-23T19:54:33.819858+00:00_

base_instruct_dif.py
base_instruct_dif_report.md
base_instruct_item_results.csv
model_classification.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 143 · 2026-05-23T19:54:33.819976+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/",
  "description": "List r22_composition_control directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/",
    "description": "List r22_composition_control directory"
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-23T19:54:33.820087+00:00_

balanced_dif_results.csv
composition_control.py
composition_control_report.md
composition_stats.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-23T19:54:33.824409+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/",
  "description": "List sf1_cluster_bootstrap directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/",
    "description": "List sf1_cluster_bootstrap directory"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-23T19:54:33.824550+00:00_

bootstrap_results.csv
cluster_bootstrap_ci.md
family_distribution.csv
run_bootstrap.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-23T19:54:33.824694+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md",
  "description": "Read DEFF summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md",
    "description": "Read DEFF summary"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-23T19:54:33.824888+00:00_

# MF2: Design Effect (DEFF) Estimation — Summary (v3, cohort-consistent)

## Analysis Scope

| Parameter | Value |
|-----------|-------|
| Cohort restriction | ref (2023) + foc (2024) only |
| Models in DIF cohort (ref+foc) | 1887 |
| Valid models (known family, family≥2) | 1884 |
| Valid families | 30 |
| Total models in response matrix | 5227 |
| Items analyzed | 12508 |

**Change from v2**: v2 used all 5227 models with family labels (1884 after filtering).
v3 restricts to ref+foc cohort (1887) before family filtering, yielding 1884 valid models.

### Family Size Distribution (within ref+foc cohort)

| Stat | Value |
|------|-------|
| Mean (m̄_simple) | 62.80 |
| m̄_weighted (Σn²/Σn) | 254.48 |
| Median | 22.5 |
| Min | 2.0 |
| Max | 547.0 |
| Top-5 families | mistral(547.0), llama-3(315.0), llama-2(161.0), mixtral(120.0), solar(91.0) |

## Design Effect — Two Variants

| Parameter | Weighted (Σn²/Σn) | Simple (mean) |
|-----------|--------------------|---------------|
| m̄ | 254.48 | 62.80 |
| Mean ICC | 0.0465 | 0.0465 |
| **Global DEFF** | **12.79** | **3.87** |
| Effective N | 147.3 | 486.2 |

### ICC Distribution

| Stat | Value |
|------|-------|
| Mean | 0.0465 |
| Median | 0.0409 |
| Q1 | 0.0261 |
| Q3 | 0.0611 |
| Max | 0.2194 |
| % ICC > 0.1 | 4.8% |
| % ICC = 0 | 0.1% |

## Adjusted DIF Classifications

### Weighted m̄

| Metric | Original | Adjusted | Change |
|--------|----------|----------|--------|
| C items | 3918 (31.3%) | 1690 (13.5%) | -2228 |
| B items | 2258 | 49 | -2209 |
| A items | 6332 | 10769 | 4437 |

Reclassification: C→B=0, C→A=2228, B→A=2209

### Simple m̄

| Metric | Original | Adjusted | Change |
|--------|----------|----------|--------|
| C items | 3918 (31.3%) | 3649 (29.2%) | -269 |
| B items | 2258 | 1081 | -1177 |
| A items | 6332 | 7778 | 1446 |

Reclassification: C→B=0, C→A=269, B→A=1177

## Reviewer's DEFF 3–5 Expectation

The **simple m̄ DEFF = 3.87** is the appropriate comparison for reviewers expecting DEFF 3–5.
The weig
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-23T19:54:33.825044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/ 2>/dev/null && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/ 2>/dev/null",
  "description": "List plan_014 and plan_015 directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/ 2>/dev/null && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015/ 2>/dev/null",
    "description": "List plan_014 and plan_015 directories"
  }
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-23T19:54:33.825175+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_029",
  "description": "Check plan_029 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_029",
    "description": "Check plan_029 directory"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-23T19:54:33.825304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/base_instruct_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/base_instruct_survey.md"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-23T19:54:33.825452+00:00_

1	# R18: Base vs Instruct Model Classification Survey
2	
3	## 1. Existing Metadata
4	
5	`model_metadata.csv` (5,227 models) contains a `training_method` column with values:
6	
7	| training_method | count |
8	|---|---|
9	| unknown | 4,676 |
10	| DPO | 347 |
11	| SFT | 136 |
12	| ORPO | 52 |
13	| PPO | 10 |
14	| KTO | 6 |
15	
16	No explicit `is_base` / `is_instruct` field exists. The `training_method` field identifies 551 instruct/aligned models (10.5%), but 89.5% are `unknown`.
17	
18	## 2. Heuristic Classification
19	
20	Two-signal approach:
21	1. **training_method**: DPO/SFT/ORPO/PPO/KTO → instruct
22	2. **Name patterns** (case-insensitive): `-instruct`, `-chat`, `-it` (word boundary), `-rlhf`, `-dpo`, `-sft`, `-aligned`, `-ift`, `-assistant`, `-turbo`
23	
24	| model_type | count | pct |
25	|---|---|---|
26	| base | 4,109 | 78.6% |
27	| instruct | 1,118 | 21.4% |
28	
29	Classification reason breakdown:
30	
31	| reason | count |
32	|---|---|
33	| default_base (no instruct signal) | 4,109 |
34	| name_pattern (regex match) | 511 |
35	| training_method (explicit) | 551 |
36	| name_keyword (Instruct/Chat/IT) | 56 |
37	
38	**Known limitations**: The 4,109 "base" models include fine-tuned/merged models that lack instruct keywords (e.g., `alignment-model-test`, `*-merged`, `*-mix`). Approximately 234 base-classified models have ambiguous patterns (`finetun`, `align`, `merged`, `mix`, `gguf`, `gptq`, `awq`). Most of these are quantized variants (GGUF/GPTQ/AWQ) which preserve the original model's type, so the misclassification risk is moderate but not zero.
39	
40	## 3. Sub-group Sizes
41	
42	### By Cohort
43	
44	| cohort | base | instruct | total |
45	|---|---|---|---|
46	| 2023 (ref) | 838 | 242 | 1,080 |
47	| 2024 (foc) | 518 | 289 | 807 |
48	| other | 2,753 | 587 | 3,340 |
49	| **All** | **4,109** | **1,118** | **5,227** |
50	
51	### DIF Sub-groups (cohort × model_type)
52	
53	| sub-group | n | ≥80 threshold |
54	|---|---|---|
55	| 2023-base | 838 | pass |
56	| 2023-inst
…[truncated 2896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-23T19:54:33.825605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-23T19:54:33.825755+00:00_

1	# R18: Base vs Instruct DIF Separation Experiment
2	
3	## Sample Sizes
4	
5	| Group | Ref (2023) | Foc (2024) | Total |
6	|-------|-----------|-----------|-------|
7	| Base | 861 | 548 | 1409 |
8	| Instruct | 219 | 259 | 478 |
9	| Full (reported) | 1,080 | 807 | 1,887 |
10	
11	All subgroups have N ≥ 80; adequate power.
12	
13	## C% Comparison
14	
15	| Group | C% | DIF-C items |
16	|-------|-----|------------|
17	| Base | 32.1% | 4018/12508 |
18	| Instruct | 36.5% | 4567/12508 |
19	| Full (reported) | 31.3% | — |
20	
21	**Difference (base − instruct):** -4.4 pp
22	**Bootstrap 95% CI:** [-13.4, 4.3] (N=1000)
23	
24	## Difficulty–Direction Gradient
25	
26	Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:
27	
28	- **Base:** ρ = -0.570 (p = 0.00e+00, n = 4018)
29	- **Instruct:** ρ = -0.079 (p = 1.02e-07, n = 4567)
30	
31	## DIF Item Overlap
32	
33	| Metric | Value |
34	|--------|-------|
35	| C_base only | 1965 |
36	| C_instruct only | 2514 |
37	| Both | 2053 |
38	| Jaccard index | 0.314 |
39	| Expected Jaccard (independence) | 0.206 |
40	| Jaccard / Expected ratio | 1.5× |
41	
42	## DIF Direction Distribution
43	
44	| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
45	|-------|----------------------|---------------------|
46	| Base | 1605 (39.9%) | 2413 (60.1%) |
47	| Instruct | 2994 (65.6%) | 1573 (34.4%) |
48	
49	χ² = 562.70, p = 2.178e-124
50	
51	## Output Files
52	
53	- `model_classification.csv` — 1887 models classified
54	- `base_instruct_item_results.csv` — 12508 items with per-group DIF statistics
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-23T19:54:33.825903+00:00_

plan_014_report.md
plan_014_within_subject_dif.py
within_subject_dif_detail.csv
within_subject_dif_results.csv
plan_015_bifactor_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-23T19:54:33.826018+00:00_

fig_permutation_null.png
permutation_null_report.md
permutation_results.csv
plan_029_permutation_null.py
run.log
run_final.log
plan_029_permutation_null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-23T19:54:33.826141+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012_irt_theta_conditioning/",
  "description": "List plan_012 directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012_irt_theta_conditioning/",
    "description": "List plan_012 directories"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-23T19:54:33.826262+00:00_

dose_response_theta.csv
enrichment_theta.csv
injection_results.csv
plan_012_irt_theta_analysis.py
plan_012_report.md
theta_estimates.csv
data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 159 · 2026-05-23T19:54:33.826399+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep sf1",
  "description": "Check sf1_cluster_bootstrap directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep sf1",
    "description": "Check sf1_cluster_bootstrap directory"
  }
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-23T19:54:33.826595+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\ndata = {\n    'TruthfulQA': {'rho': 0.997123, 'tau': 0.958635, 'flip': 0.020682},\n    'ARC':        {'rho': 0.996209, 'tau': 0.953791, 'flip': 0.023104},\n    'WinoGrande': {'rho': 0.994255, 'tau': 0.943166, 'flip': 0.028417},\n    'GSM8K':      {'rho': 0.999303, 'tau': 0.984311, 'flip': 0.007844},\n    'HellaSwag':  {'rho': 0.998623, 'tau': 0.972166, 'flip': 0.013917},\n    'MMLU':       {'rho': 0.9965,   'tau': 0.959986, 'flip': 0.020007},\n}\n# Paper values\npaper = {\n    'MMLU':       {'rho': 0.9965, 'tau': 0.9600, 'flip': 2.00},\n    'WinoGrande': {'rho': 0.9943, 'tau': 0.9432, 'flip': 2.84},\n    'TruthfulQA': {'rho': 0.9971, 'tau': 0.9586, 'flip': 2.07},\n    'ARC':        {'rho': 0.9962, 'tau': 0.9538, 'flip': 2.31},\n    'GSM8K':      {'rho': 0.9993, 'tau': 0.9843, 'flip': 0.78},\n    'HellaSwag':  {'rho': 0.9986, 'tau': 0.9722, 'flip': 1.39},\n}\nprint('--- rho check ---')\nfor k, v in data.items():\n    src_rho = round(v['rho'], 4)\n    paper_rho = paper[k]['rho']\n    match = '✅' if abs(src_rho - paper_rho) < 0.00015 else '❌'\n    print(f'{k}: src={src_rho}, paper={paper_rho} {match}')\nprint()\nprint('--- tau check ---')\nfor k, v in data.items():\n    src_tau = round(v['tau'], 4)\n    paper_tau = paper[k]['tau']\n    match = '✅' if abs(src_tau - paper_tau) < 0.00015 else '❌'\n    print(f'{k}: src={src_tau}, paper={paper_tau} {match}')\nprint()\nprint('--- flip% check ---')\nfor k, v in data.items():\n    src_flip = round(v['flip']*100, 2)\n    paper_flip = paper[k]['flip']\n    match = '✅' if abs(src_flip - paper_flip) < 0.015 else '❌'\n    print(f'{k}: src={src_flip}%, paper={paper_flip}% {match}')\n\"\n",
  "description": "Compare source data with paper values for rho, tau, flip%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\ndata = {\n    'TruthfulQA': {'rho': 0.997123, 'tau': 0.958635, 'flip': 0.020682},\n    'ARC':        {'rho': 0.996209, 'tau': 0.953791, 'flip': 0.023104},\n    'WinoGrande': {'rho': 0.994255, 'tau': 0.943166, 'flip': 0.028417},\n    'GSM8K':      {'rho': 0.999303, 'tau': 0.984311, 'flip': 0.007844},\n    'HellaSwag':  {'rho': 0.998623, 'tau': 0.972166, 'flip': 0.013917},\n    'MMLU':       {'rho': 0.9965,   'tau': 0.959986, 'flip': 0.020007},\n}\n# Paper values\npaper = {\n    'MMLU':       {'rho': 0.9965, 'tau': 0.9600, 'flip': 2.00},\n    'WinoGrande': {'rho': 0.9943, 'tau': 0.9432, 'flip': 2.84},\n    'TruthfulQA': {'rho': 0.9971, 'tau': 0.9586, 'flip': 2.07},\n    'ARC':        {'rho': 0.9962, 'tau': 0.9538, 'flip': 2.31},\n    'GSM8K':      {'rho': 0.9993, 'tau': 0.9843, 'flip': 0.78},\n    'HellaSwag':  {'rho': 0.9986, 'tau': 0.9722, 'flip': 1.39},\n}\nprint('--- rho check ---')\nfor k, v in data.items():\n    src_rho = round(v['rho'], 4)\n    paper_rho = paper[k]['rho']\n    match = '✅' if abs(src_rho - paper_rho) < 0.00015 else '❌'\n    print(f'{k}: src={src_rho}, paper={paper_rho} {match}')\nprint()\nprint('--- tau check ---')\nfor k, v in data.items():\n    src_tau = round(v['tau'], 4)\n    paper_tau = paper[k]['tau']\n    match = '✅' if abs(src_tau - paper_tau) < 0.00015 else '❌'\n    print(f'{k}: src={src_tau}, paper={paper_tau} {match}')\nprint()\nprint('--- flip% check ---')\nfor k, v in data.items():\n    src_flip = round(v['flip']*100, 2)\n    paper_flip = paper[k]['flip']\n    match = '✅' if abs(src_flip - paper_flip) < 0.015 else '❌'\n    print(f'{k}: src={src_flip}%, paper={paper_flip}% {match}')\n\"\n",
    "description": "Compare source data with paper values for rho, tau, flip%"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-23T19:54:33.826789+00:00_

--- rho check ---
TruthfulQA: src=0.9971, paper=0.9971 ✅
ARC: src=0.9962, paper=0.9962 ✅
WinoGrande: src=0.9943, paper=0.9943 ✅
GSM8K: src=0.9993, paper=0.9993 ✅
HellaSwag: src=0.9986, paper=0.9986 ✅
MMLU: src=0.9965, paper=0.9965 ✅

--- tau check ---
TruthfulQA: src=0.9586, paper=0.9586 ✅
ARC: src=0.9538, paper=0.9538 ✅
WinoGrande: src=0.9432, paper=0.9432 ✅
GSM8K: src=0.9843, paper=0.9843 ✅
HellaSwag: src=0.9722, paper=0.9722 ✅
MMLU: src=0.96, paper=0.96 ✅

--- flip% check ---
TruthfulQA: src=2.07%, paper=2.07% ✅
ARC: src=2.31%, paper=2.31% ✅
WinoGrande: src=2.84%, paper=2.84% ✅
GSM8K: src=0.78%, paper=0.78% ✅
HellaSwag: src=1.39%, paper=1.39% ✅
MMLU: src=2.0%, paper=2.0% ✅

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-23T19:54:33.826929+00:00_

bootstrap_results.csv
cluster_bootstrap_ci.md
family_distribution.csv
run_bootstrap.py
sf1_cluster_bootstrap

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 163 · 2026-05-23T19:54:33.827057+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_032",
  "description": "Check plan_032 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_032",
    "description": "Check plan_032 directory"
  }
}
```

</details>

---


### Tool result

_source line 164 · 2026-05-23T19:54:33.827178+00:00_

cleaned_mmlu_analysis.csv
data
dif_vs_random_comparison.csv
per_subject_dif_concentration.csv
plan_032_dif_cleaned_mmlu.py
plan_032_random_baseline.py
plan_032_report.md
random_baseline_report.md
random_baseline_summary.csv
report
plan_032_dif_cleaned_mmlu

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-23T19:54:33.827299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_028",
  "description": "Check plan_028 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ 2>/dev/null || echo \"NOT FOUND\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_028",
    "description": "Check plan_028 directory"
  }
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-23T19:54:33.827424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-23T19:54:33.827538+00:00_

arc_dif_results.csv
arc_ets_summary.csv
data
hellaswag_dif_results.csv
hellaswag_ets_summary.csv
intermediate
multi_bench_dif_report.md
multi_bench_summary.csv
multi_bench_summary.csv.bak
plan_028_multi_bench_dif.py
report
run.log
truthfulqa_dif_results.csv
truthfulqa_ets_summary.csv
winogrande_dif_results.csv
winogrande_ets_summary.csv
plan_028_bootstrap_ci
plan_028_multi_bench_dif

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-23T19:54:33.827662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/plan_014_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/plan_014_report.md"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-23T19:54:33.827825+00:00_

1	# Plan 014: Within-Subject Temporal DIF + SIBTEST Availability
2	
3	## Background
4	
5	Plan_012 showed single-dimensional θ-conditioning cannot reduce the temporal cohort's
6	31% baseline FPR. Before launching a full bifactor model, we check whether the high
7	C% is driven by between-subject ability differences or within-subject DIF.
8	
9	## Part 1: Within-Subject Temporal DIF
10	
11	For each subject, MH-DIF uses **within-subject purified total score** as the matching
12	variable. This isolates DIF to items within the same content domain, removing
13	between-subject ability confounds.
14	
15	### Results
16	
17	| Subject | N items | ETS A | ETS B | ETS C | C% | A% |
18	|---------|---------|-------|-------|-------|-----|-----|
19	| business_ethics | 93 | 32 | 19 | 42 | 45.2% | 34.4% |
20	| human_aging | 203 | 96 | 40 | 67 | 33.0% | 47.3% |
21	| formal_logic | 109 | 46 | 20 | 43 | 39.5% | 42.2% |
22	| professional_medicine | 248 | 124 | 47 | 77 | 31.1% | 50.0% |
23	| high_school_statistics | 181 | 66 | 39 | 76 | 42.0% | 36.5% |
24	
25	**Average within-subject C%: 38.1%**
26	
27	## Part 2: Cross-Subject Matching Comparison
28	
29	Cross-subject matching uses total score on **all other subjects** (excluding the
30	current one) as the matching variable. This eliminates within-subject ability
31	contamination of the matching variable.
32	
33	### Results
34	
35	| Subject | N items | Matching | ETS A | ETS B | ETS C | C% | A% |
36	|---------|---------|----------|-------|-------|-------|-----|-----|
37	| business_ethics | 93 | within | 32 | 19 | 42 | 45.2% | 34.4% |
38	| | | cross | 32 | 16 | 45 | 48.4% | 34.4% |
39	| human_aging | 203 | within | 96 | 40 | 67 | 33.0% | 47.3% |
40	| | | cross | 88 | 30 | 85 | 41.9% | 43.4% |
41	| formal_logic | 109 | within | 46 | 20 | 43 | 39.5% | 42.2% |
42	| | | cross | 52 | 14 | 43 | 39.5% | 47.7% |
43	| professional_medicine | 248 | within | 124 | 47 | 77 | 31.1% | 50.0% |
44	| | | cross | 109 | 45 | 94 | 37.9% | 44.0% |
45	| high_school
…[truncated 1583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-23T19:54:33.827976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_report.md"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-23T19:54:33.828147+00:00_

1	# Plan 012: IRT θ-Conditioning MH-DIF Analysis
2	
3	## 1. Objective
4	
5	Replace raw total scores with IRT-based θ estimates as the MH-DIF stratification
6	variable. Test whether finer ability matching reduces the high baseline FPR from
7	plan_011 (temporal ~31%, ability ~49%) while preserving detection power (TPR).
8	
9	## 2. θ Estimation Method
10	
11	**Method**: Logit of proportion correct with Laplace smoothing
12	```
13	θ = log((total + 0.5) / (N_items + 1 - total - 0.5))
14	```
15	- N models: 5227
16	- N items (full matrix): 12508
17	- θ range: [-3.310, 2.330]
18	- θ mean±std: 0.382±0.702
19	- Correlation(θ, total_score): 0.9986
20	
21	This is a monotone transformation of the Rasch model sufficient statistic.
22	Two binning strategies are compared:
23	- **Equal-width (eq)**: equal intervals on the logit scale — respects IRT metric
24	- **Quantile (qt)**: equal-count bins — ensures balanced strata
25	
26	## 3. Experimental Design
27	
28	- Baseline items: 500
29	- Contaminated per run: 100
30	- Injection probabilities: [0.0, 0.3, 0.5, 0.7, 1.0]
31	- Seeds per p: 5
32	- Strata counts tested: [10, 15, 20]
33	
34	### Cohort definitions
35	
36	- **ability**: ref N=2092, foc N=2089, foc inject N=2089
37	- **temporal**: ref N=1080, foc N=807, foc inject N=787
38	
39	### MH variants
40	
41	| Variant | Stratification | Description |
42	|---------|---------------|-------------|
43	| theta_eq_10 | Equal-width θ bins | 10 equal intervals on logit scale |
44	| theta_qt_10 | Quantile θ bins | 10 equal-count bins on θ |
45	| theta_eq_15 | Equal-width θ bins | 15 equal intervals on logit scale |
46	| theta_qt_15 | Quantile θ bins | 15 equal-count bins on θ |
47	| theta_eq_20 | Equal-width θ bins | 20 equal intervals on logit scale |
48	| theta_qt_20 | Quantile θ bins | 20 equal-count bins on θ |
49	| external_5 | Quantile total-score | 5 bins on full-matrix total (plan_011 baseline) |
50	
51	## 4. Semi-Synthetic Results
52	
53	### Temporal cohort
54	
55	#### Baseline FPR (p=
…[truncated 7001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-23T19:54:33.828307+00:00_

1	# R22: Base/Instruct Composition Control
2	
3	## Motivation
4	
5	2023 and 2024 cohorts differ in base/instruct model composition:
6	- 2023: 861 base + 219 instruct (79.7% base)
7	- 2024: 548 base + 259 instruct (67.9% base)
8	
9	This 11.8 pp gap could confound temporal MH-DIF if base and instruct
10	models respond differently. We test this by matched subsampling.
11	
12	## Method
13	
14	1. Target base ratio: 67.9% (matching the lower-ratio cohort)
15	2. Downsample 2023 base models from 861 → 463
16	3. Re-run 5-stratum MH-DIF with ETS C classification
17	4. Repeat 10× with different random seeds
18	
19	## Results
20	
21	| Metric | Value |
22	|--------|-------|
23	| Original C% | 31.32% |
24	| Balanced C% (mean ± SD) | 30.25% ± 1.32% |
25	| Balanced C% 95% CI | [27.65%, 32.84%] |
26	| Δ(original − balanced) | 1.08 pp |
27	
28	### Per-repetition results
29	
30	rep,c_pct,n_ref,n_foc,base_pct_ref,base_pct_foc
31	1,30.860249440358174,682,807,67.88856304985337,67.90582403965304
32	2,28.27790214262872,682,807,67.88856304985337,67.90582403965304
33	3,30.244643428205947,682,807,67.88856304985337,67.90582403965304
34	4,30.204669011832426,682,807,67.88856304985337,67.90582403965304
35	5,29.525103933482573,682,807,67.88856304985337,67.90582403965304
36	6,32.65909817716661,682,807,67.88856304985337,67.90582403965304
37	7,29.90885833066837,682,807,67.88856304985337,67.90582403965304
38	8,31.371921969939237,682,807,67.88856304985337,67.90582403965304
39	9,28.437799808122797,682,807,67.88856304985337,67.90582403965304
40	10,30.972177806204034,682,807,67.88856304985337,67.90582403965304
41	
42	
43	## Conclusion
44	
45	Balanced C% remains high (30.2%), confirming that DIF is NOT driven by base/instruct composition shift. The 1.1 pp difference is negligible.
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-23T19:54:33.828452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/cluster_bootstrap_ci.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/cluster_bootstrap_ci.md"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-23T19:54:33.828576+00:00_

1	# SF1: Cluster Bootstrap — Family-level CI for Temporal C%
2	
3	## Family Distribution
4	
5	- **Filter**: only families with size >= 3 (among models with cohort ∈ {2023, 2024})
6	- **Before filter**: 33 families
7	- **After filter**: 29 families, 1882 models
8	- **Size distribution**: min=3, median=24, max=547
9	- **Top 5 families**: mistral (547), llama-3 (315), llama-2 (161), mixtral (120), solar (91)
10	
11	## Bootstrap Results (B = 1000)
12	
13	| Metric | Cluster Bootstrap | Model Bootstrap |
14	|--------|------------------|-----------------|
15	| Point estimate C% | 31.30% | 31.30% |
16	| 95% CI | [26.73%, 53.17%] | [29.23%, 37.75%] |
17	| CI width | 26.44 pp | 8.52 pp |
18	| Mean | 38.83% | 33.02% |
19	| SD | 6.79% | 2.19% |
20	
21	**CI width ratio (cluster / model)**: 3.10×
22	
23	## Key Observation: Complete Family–Cohort Confounding
24	
25	Every family falls entirely in one cohort — no family spans both 2023 and 2024.
26	This means resampling families simultaneously changes the reference/focal composition,
27	which is the dominant driver of the wide cluster CI (and the upward bias in the
28	cluster bootstrap mean: 38.83% vs point estimate 31.30%).
29	
30	## Interpretation
31	
32	The cluster bootstrap CI is 3.10× wider than the model-level CI.
33	Two sources contribute:
34	
35	1. **Within-family response correlation**: models from the same family produce
36	   similar item-level patterns, reducing the effective sample size.
37	2. **Family–cohort confounding**: because each family belongs entirely to one
38	   cohort, resampling families changes the reference/focal ratio, amplifying
39	   variability in the MH statistics.
40	
41	Both CIs exclude zero (lower bound 26.73% for cluster, 29.23% for model),
42	confirming that the C% finding is robust regardless of bootstrap method.
43	Even under the more conservative cluster bootstrap, at least ~27% of items
44	show large DIF.
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 175 · 2026-05-23T19:54:33.828745+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
  "description": "List plan_001_real_data_dif_mmlu directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/",
    "description": "List plan_001_real_data_dif_mmlu directory"
  }
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-23T19:54:33.828875+00:00_

data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 177 · 2026-05-23T19:54:33.828997+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/",
  "description": "List k3_power_simulation directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/",
    "description": "List k3_power_simulation directory"
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-23T19:54:33.829109+00:00_

k3_power_report.md
k3_power_results.csv
k3_power_simulation.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 179 · 2026-05-23T19:54:33.829235+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Check Ratio = C% / Random C%\nbenchmarks = {\n    'MMLU':       {'c_pct': 31.3, 'rand_c': 0.62, 'paper_ratio': '50x'},\n    'WinoGrande': {'c_pct': 30.3, 'rand_c': 0.32, 'paper_ratio': '95x'},\n    'TruthfulQA': {'c_pct': 29.7, 'rand_c': 0.37, 'paper_ratio': '80x'},\n    'ARC':        {'c_pct': 26.9, 'rand_c': 0.60, 'paper_ratio': '45x'},\n    'GSM8K':      {'c_pct': 18.9, 'rand_c': 0.30, 'paper_ratio': '63x'},\n    'HellaSwag':  {'c_pct': 17.9, 'rand_c': 0.28, 'paper_ratio': '64x'},\n}\nprint('--- Ratio check (C% / Random C%) ---')\nfor k, v in benchmarks.items():\n    ratio = v['c_pct'] / v['rand_c']\n    print(f'{k}: {v[\\\"c_pct\\\"]}/{v[\\\"rand_c\\\"]} = {ratio:.1f}x (paper: {v[\\\"paper_ratio\\\"]})')\n\"\n",
  "description": "Compute ratio column from C% and Random C%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Check Ratio = C% / Random C%\nbenchmarks = {\n    'MMLU':       {'c_pct': 31.3, 'rand_c': 0.62, 'paper_ratio': '50x'},\n    'WinoGrande': {'c_pct': 30.3, 'rand_c': 0.32, 'paper_ratio': '95x'},\n    'TruthfulQA': {'c_pct': 29.7, 'rand_c': 0.37, 'paper_ratio': '80x'},\n    'ARC':        {'c_pct': 26.9, 'rand_c': 0.60, 'paper_ratio': '45x'},\n    'GSM8K':      {'c_pct': 18.9, 'rand_c': 0.30, 'paper_ratio': '63x'},\n    'HellaSwag':  {'c_pct': 17.9, 'rand_c': 0.28, 'paper_ratio': '64x'},\n}\nprint('--- Ratio check (C% / Random C%) ---')\nfor k, v in benchmarks.items():\n    ratio = v['c_pct'] / v['rand_c']\n    print(f'{k}: {v[\\\"c_pct\\\"]}/{v[\\\"rand_c\\\"]} = {ratio:.1f}x (paper: {v[\\\"paper_ratio\\\"]})')\n\"\n",
    "description": "Compute ratio column from C% and Random C%"
  }
}
```

</details>

---


### Tool result

_source line 180 · 2026-05-23T19:54:33.829355+00:00_

--- Ratio check (C% / Random C%) ---
MMLU: 31.3/0.62 = 50.5x (paper: 50x)
WinoGrande: 30.3/0.32 = 94.7x (paper: 95x)
TruthfulQA: 29.7/0.37 = 80.3x (paper: 80x)
ARC: 26.9/0.6 = 44.8x (paper: 45x)
GSM8K: 18.9/0.3 = 63.0x (paper: 63x)
HellaSwag: 17.9/0.28 = 63.9x (paper: 64x)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 181 · 2026-05-23T19:54:33.829493+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model/",
  "description": "List predictive_model directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model/",
    "description": "List predictive_model directory"
  }
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-23T19:54:33.829616+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/",
  "description": "List r15_random_split_control directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/",
    "description": "List r15_random_split_control directory"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-23T19:54:33.829746+00:00_

cv_results.csv
feature_importance.csv
feature_inventory.md
features.csv
phase2_results.md
phase2_train.py
safe_features.csv
target.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-23T19:54:33.829873+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/",
  "description": "List plan_030_odds_ratio directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/",
    "description": "List plan_030_odds_ratio directory"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-23T19:54:33.829986+00:00_

intermediate
odds_ratio_report.md
plan_030_odds_ratio.py
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-23T19:54:33.830106+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv | head -5 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_null_report.md",
  "description": "Read permutation null results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_results.csv | head -5 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/permutation_null_report.md",
    "description": "Read permutation null results"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-23T19:54:33.830229+00:00_

permutation,c_pct
1,0.03997441637352095
2,0.08794371602174608
3,0.11992324912056285
4,0.17588743204349216
---
# Plan 029: Permutation Null for Temporal DIF C%

## Purpose

Test whether the observed temporal DIF C% significantly exceeds the rate
expected under random label assignment.

## Method

- **Data**: 1887 models with temporal labels (1080 "2023", 807 "2024"), 12508 items
- **Procedure**: 200 permutations of temporal labels, group sizes fixed
- **MH-DIF**: purified matching, 5 quantile strata, ETS classification
- **Seed**: 42
- **Optimisation**: strata precomputed once (invariant to label permutation)

## Results

| Metric | Value |
|--------|-------|
| Observed C% | 31.32% |
| Null mean ± SD | 0.10% ± 0.12% |
| Null 95% CI | [0.02%, 0.33%] |
| Null range | [0.01%, 1.14%] |
| N exceed observed | 0 / 200 |
| p-value | = 0.0050 |

## Interpretation

The observed temporal DIF C% of 31.32% is **above** the permutation null (mean 0.10%, max 1.14%, p = 0.0050).  The 31.3% C-category rate cannot be attributed to chance label assignment.

## Runtime

- Per permutation: ~2.7s
- Total: 4.2 min (200 permutations)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-23T19:54:33.830362+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/cluster_bootstrap_ci.md",
  "description": "Read cluster bootstrap CI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/cluster_bootstrap_ci.md",
    "description": "Read cluster bootstrap CI"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-23T19:54:33.830490+00:00_

# SF1: Cluster Bootstrap — Family-level CI for Temporal C%

## Family Distribution

- **Filter**: only families with size >= 3 (among models with cohort ∈ {2023, 2024})
- **Before filter**: 33 families
- **After filter**: 29 families, 1882 models
- **Size distribution**: min=3, median=24, max=547
- **Top 5 families**: mistral (547), llama-3 (315), llama-2 (161), mixtral (120), solar (91)

## Bootstrap Results (B = 1000)

| Metric | Cluster Bootstrap | Model Bootstrap |
|--------|------------------|-----------------|
| Point estimate C% | 31.30% | 31.30% |
| 95% CI | [26.73%, 53.17%] | [29.23%, 37.75%] |
| CI width | 26.44 pp | 8.52 pp |
| Mean | 38.83% | 33.02% |
| SD | 6.79% | 2.19% |

**CI width ratio (cluster / model)**: 3.10×

## Key Observation: Complete Family–Cohort Confounding

Every family falls entirely in one cohort — no family spans both 2023 and 2024.
This means resampling families simultaneously changes the reference/focal composition,
which is the dominant driver of the wide cluster CI (and the upward bias in the
cluster bootstrap mean: 38.83% vs point estimate 31.30%).

## Interpretation

The cluster bootstrap CI is 3.10× wider than the model-level CI.
Two sources contribute:

1. **Within-family response correlation**: models from the same family produce
   similar item-level patterns, reducing the effective sample size.
2. **Family–cohort confounding**: because each family belongs entirely to one
   cohort, resampling families changes the reference/focal ratio, amplifying
   variability in the MH statistics.

Both CIs exclude zero (lower bound 26.73% for cluster, 29.23% for model),
confirming that the C% finding is robust regardless of bootstrap method.
Even under the more conservative cluster bootstrap, at least ~27% of items
show large DIF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-23T19:54:33.830636+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md",
  "description": "Read plan_032 report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md",
    "description": "Read plan_032 report"
  }
}
```

</details>

---


### Tool call

_source line 191 · 2026-05-23T19:54:33.830781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model/phase2_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model/phase2_results.md"
  }
}
```

</details>

---


### Tool result

_source line 192 · 2026-05-23T19:54:33.830924+00:00_

# Plan 032: DIF-Cleaned MMLU Demonstration

## Overview
- Full MMLU: **12508** items
- DIF-cleaned MMLU: **8590** items (removed **3918** ETS C-flagged, 31.3%)
- Models analyzed: **5227**

## Global Rank Correlation
- Spearman ρ (full vs. cleaned scores): **0.996455** (p=0.00e+00)
- This high ρ is expected—but masks local rank disruptions that matter for evaluation.

## Rank Change Distribution
- Mean rank change: 0.00
- Std rank change: 127.10
- Min: -589 | Max: 849
- |change| ≥ 5: 4679 models (89.5%)
- |change| ≥ 10: 4158 models (79.5%)
- |change| ≥ 20: 3471 models (66.4%)
- |change| ≥ 50: 2188 models (41.9%)
- |change| ≥ 100: 1297 models (24.8%)

## Top 10 Models Moving UP (rank improved after cleaning)

| model_name | family | cohort_temporal | score_full | score_cleaned | rank_full | rank_cleaned | rank_change |
| --- | --- | --- | --- | --- | --- | --- | --- |
| liminerity/Blurstral-7b-slerp | unknown | other | 0.6948 | 0.7236 | 1412 | 823 | -589 |
| DreadPoor/PAIN_LeDestroy-7B-task_arithmetic | unknown | other | 0.6984 | 0.7258 | 1182 | 613 | -569 |
| flammenai/flammen26-mistral-7B | mistral | 2023 | 0.6961 | 0.7240 | 1336 | 790 | -546 |
| Gille/StrangeMerges_2-7B-slerp | unknown | other | 0.6964 | 0.7239 | 1316 | 797 | -519 |
| Gille/StrangeMerges_12-7B-slerp | unknown | other | 0.6960 | 0.7232 | 1345 | 851 | -494 |
| jambroz/sixtyoneeighty-7b | unknown | other | 0.6972 | 0.7241 | 1269 | 782 | -487 |
| jambroz/sixtyoneeighty-7b-chat | unknown | other | 0.6972 | 0.7241 | 1270 | 783 | -487 |
| antiven0m/reverie-7b | unknown | other | 0.6968 | 0.7237 | 1288 | 810 | -478 |
| GreenNode/GreenNodeLM-7B-v2leo | unknown | other | 0.6962 | 0.7232 | 1329 | 852 | -477 |
| DreadPoor/Sphinx-7B-Model_Stock | unknown | other | 0.6970 | 0.7236 | 1280 | 818 | -462 |

## Top 10 Models Moving DOWN (rank worsened after cleaning)

| model_name | family | cohort_temporal | score_full | score_cleaned | rank_full | rank_cleaned | rank_change |
| --- | --- | --- | --- | --- | --- | -
…[truncated 6268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-23T19:54:33.831091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv",
  "description": "Read multi-bench summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv",
    "description": "Read multi-bench summary"
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-23T19:54:33.831210+00:00_

benchmark,n_items,n_ref,n_foc,n_ets_a,n_ets_b,n_ets_c,pct_c,random_pct_c,status
mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
winogrande,1267,1017,803,612,271,384,30.3,0.32,OK
truthfulqa,817,1080,807,398,176,243,29.7,0.37,OK
arc,1172,1080,807,642,215,315,26.9,0.6,OK
gsm8k,1319,1017,804,825,245,249,18.9,0.3,PRIOR
hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-23T19:54:33.831345+00:00_

1	# Phase 2: Item-Property Predictive Model — Leak-Free Results
2	
3	## Safe Feature Set (23 features)
4	
5	### Numeric features (19)
6	| Feature | Source | Notes |
7	|---------|--------|-------|
8	| difficulty_ref | ref cohort | proportion correct, ref 2023 |
9	| discrimination_ref | ref cohort | point-biserial, ref 2023 |
10	| item_variance_ref | **recalculated** | p_ref * (1 - p_ref) |
11	| subject_n_items | metadata | items per subject |
12	| subject_mean_difficulty_ref | **recalculated** | mean difficulty_ref per subject |
13	| difficulty_vs_subject_ref | **recalculated** | difficulty_ref - subject mean |
14	| question_length | text | char count |
15	| question_word_count | text | word count |
16	| option_count | text | number of options |
17	| option_length_mean | text | mean option char length |
18	| option_length_std | text | std of option lengths |
19	| has_negation | text | negation keyword present |
20	| prompt_total_length | text | total prompt char count |
21	| qtype_factual | text | question type indicator |
22	| qtype_other | text | question type indicator |
23	| qtype_reasoning | text | question type indicator |
24	| qtype_statement_eval | text | question type indicator |
25	| li_label_clean | Li et al. | contamination flag (binary, missing->0) |
26	| li_label_missing | Li et al. | missingness indicator |
27	
28	### Contamination type dummies (4)
29	contam_clean, contam_input_and_label, contam_input_only, contam_no_annotation
30	
31	Three features recalculated from ref cohort only (replacing leaked full-sample versions):
32	- `item_variance_ref` = difficulty_ref * (1 - difficulty_ref)
33	- `subject_mean_difficulty_ref` = mean(difficulty_ref) within each subject
34	- `difficulty_vs_subject_ref` = difficulty_ref - subject_mean_difficulty_ref
35	
36	**GroupKFold**: 5 folds, grouped by `subject` (57 subjects). Same subject never split across train/test.
37	
38	---
39	
40	## CV Results
41	
42	### Logistic Regression — Full Model
43	
44	| Fold | AUROC | F1
…[truncated 2559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-23T19:54:33.831498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/odds_ratio_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/odds_ratio_report.md"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-23T19:54:33.831644+00:00_

1	# Plan 030: Odds Ratio + CI for Accuracy-DIF Regression
2	
3	Generated: 2026-05-21 10:03
4	
5	Dataset: 12508 items, 57 subjects, DIF C = 3918 (31.3%)
6	
7	
8	## Model Summary Table
9	
10	| Metric | Model 1 (domain Δ) | Model 2 (domain Δ + item props) | Model 3 (item Δ) | Model 4 (item Δ + item props) |
11	|--------|------|------|------|------|
12	| AIC | 15545.2439 | 14902.2601 | 15536.9475 | 14885.4142 |
13	| BIC | 15560.1122 | 14931.9966 | 15551.8157 | 14915.1507 |
14	| McFadden R² | 0.0007 | 0.0423 | 0.0012 | 0.0434 |
15	| Nagelkerke R² | 0.0012 | 0.0720 | 0.0021 | 0.0737 |
16	| Cox-Snell R² | 0.0008 | 0.0512 | 0.0015 | 0.0525 |
17	| Deviance explained | 0.0007 | 0.0423 | 0.0012 | 0.0434 |
18	| Hosmer-Lemeshow p | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
19	
20	
21	## Model 1 (domain Δ)
22	
23	| Variable | Coef | SE | z | p | OR | OR 95% CI |
24	|----------|------|----|---|---|----|-----------|
25	| const | -0.8975 | 0.0400 | -22.43 | 1.91e-111 | 0.4076 | [0.3768, 0.4408] |
26	| subject_acc_delta | 4.3928 | 1.3602 | 3.23 | 0.0012 | 80.8636 | [5.6229, 1162.9010] |
27	
28	- McFadden R² = 0.0007
29	- Nagelkerke R² = 0.0012
30	- Cox-Snell R² = 0.0008
31	- AIC = 15545.2, BIC = 15560.1
32	- Hosmer-Lemeshow: χ²=39.66, df=8, p=0.0000
33	
34	
35	## Model 2 (domain Δ + item props)
36	
37	| Variable | Coef | SE | z | p | OR | OR 95% CI |
38	|----------|------|----|---|---|----|-----------|
39	| const | 0.0691 | 0.0650 | 1.06 | 0.2877 | 1.0716 | [0.9434, 1.2173] |
40	| subject_acc_delta | -3.0972 | 1.4305 | -2.17 | 0.0304 | 0.0452 | [0.0027, 0.7456] |
41	| ctt_difficulty | -2.5435 | 0.1151 | -22.09 | 3.93e-108 | 0.0786 | [0.0627, 0.0985] |
42	| ctt_discrimination | 4.1155 | 0.1929 | 21.33 | 5.79e-101 | 61.2836 | [41.9876, 89.4474] |
43	
44	- McFadden R² = 0.0423
45	- Nagelkerke R² = 0.0720
46	- Cox-Snell R² = 0.0512
47	- AIC = 14902.3, BIC = 14932.0
48	- Hosmer-Lemeshow: χ²=60.18, df=8, p=0.0000
49	
50	
51	## Model 3 (item Δ)
52	
53	| Variable | Coef | SE | z | p | OR | OR 95% 
…[truncated 2807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-23T19:54:33.831802+00:00_

random_split_analysis.py
random_split_report.md
random_split_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-23T19:54:33.831929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Check the within-family N counts\n# paper says: Within-family (Llama-2 vs 3) & 161 / 308\n# Need to find actual N_ref and N_focal for llama-2 vs llama-3 comparison\nimport csv\nmodels = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        family = row.get('family', '') or row.get('model_family', '')\n        name = row.get('model', '') or row.get('model_name', '')\n        models[name] = row\n        \ncols = list(list(models.values())[0].keys()) if models else []\nprint('Columns:', cols)\nprint('Sample:', list(models.items())[:3])\n\"\n",
  "description": "Check model metadata for family groupings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Check the within-family N counts\n# paper says: Within-family (Llama-2 vs 3) & 161 / 308\n# Need to find actual N_ref and N_focal for llama-2 vs llama-3 comparison\nimport csv\nmodels = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        family = row.get('family', '') or row.get('model_family', '')\n        name = row.get('model', '') or row.get('model_name', '')\n        models[name] = row\n        \ncols = list(list(models.values())[0].keys()) if models else []\nprint('Columns:', cols)\nprint('Sample:', list(models.items())[:3])\n\"\n",
    "description": "Check model metadata for family groupings"
  }
}
```

</details>

---


### Tool result

_source line 200 · 2026-05-23T19:54:33.832051+00:00_

Columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']
Sample: [('0-hero/Matter-0.1-7B', {'model_name': '0-hero/Matter-0.1-7B', 'family': 'unknown', 'release_year': 'unknown', 'release_half': 'unknown', 'training_method': 'unknown', 'accuracy': '0.661225', 'cohort_temporal': 'other', 'cohort_accuracy_quintile': '3'}), ('0-hero/Matter-0.1-7B-DPO-preview', {'model_name': '0-hero/Matter-0.1-7B-DPO-preview', 'family': '', 'release_year': 'unknown', 'release_half': 'unknown', 'training_method': 'DPO', 'accuracy': '0.661337', 'cohort_temporal': 'other', 'cohort_accuracy_quintile': '3'}), ('0-hero/Matter-0.1-7B-boost', {'model_name': '0-hero/Matter-0.1-7B-boost', 'family': 'unknown', 'release_year': 'unknown', 'release_half': 'unknown', 'training_method': 'unknown', 'accuracy': '0.653422', 'cohort_temporal': 'other', 'cohort_accuracy_quintile': '3'})]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 201 · 2026-05-23T19:54:33.832200+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Now check: paper uses 0.62 for MMLU random C%, but source says 0.18\n# Let me look more carefully\ngrep -r \"random_pct_c\\|rand.*c%\\|random.*c\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ --include=\"*.csv\" --include=\"*.md\" -i | head -20",
  "description": "Check MMLU random C% source vs paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Now check: paper uses 0.62 for MMLU random C%, but source says 0.18\n# Let me look more carefully\ngrep -r \"random_pct_c\\|rand.*c%\\|random.*c\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ --include=\"*.csv\" --include=\"*.md\" -i | head -20",
    "description": "Check MMLU random C% source vs paper"
  }
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-23T19:54:33.832331+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv:benchmark,n_items,n_ref,n_foc,n_ets_a,n_ets_b,n_ets_c,pct_c,random_pct_c,status
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv:benchmark,n_items,n_ref,n_foc,n_ets_a,n_ets_b,n_ets_c,pct_c,random_pct_c,status
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:- **WINOGRANDE**: 30.3% items flagged as ETS-C (vs 0.32% random control, 94.7× enrichment)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:- **TRUTHFULQA**: 29.7% items flagged as ETS-C (vs 0.37% random control, 80.3× enrichment)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:- **ARC**: 26.9% items flagged as ETS-C (vs 0.6% random control, 44.8× enrichment)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:- **HELLASWAG**: 17.9% items flagged as ETS-C (vs 0.28% random control, 63.9× enrichment)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:The temporal DIF signal (C% >> random C%) indicates systematic item-level 
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_re
…[truncated 1845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 203 · 2026-05-23T19:54:33.832473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md"
  }
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-23T19:54:33.832611+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_report.md | head -100",
  "description": "Read plan_001 report for subject-level stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_report.md | head -100",
    "description": "Read plan_001 report for subject-level stats"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-23T19:54:33.832769+00:00_

1	# K=3 Power Simulation Results
2	
3	## Setup
4	
5	- **PSN-IRT parameters**: ā=1.2, b̄=-0.84
6	- **Items**: 200 total, 20 contaminated (10%)
7	- **K (strata)**: [3, 5]
8	- **N/cohort**: [40, 60, 80, 100, 200, 500]
9	- **δ (effect sizes)**: [0.6, 0.8, 1.0, 1.2, 1.4]
10	- **Replications**: 1000 per condition
11	- **Method**: Mantel-Haenszel with BH FDR correction
12	- **Flagging**: ETS C classification (|Δ_MH|≥1.5 & p<0.05)
13	
14	## Key Finding: K=3 vs K=5 Comparison
15	
16	### δ = 0.6
17	
18	| N/cohort | K=3 TPR | K=5 TPR | K=3 FPR | K=5 FPR | K=3 AUC | K=5 AUC |
19	|----------|---------|---------|---------|---------|---------|---------|
20	|       40 | 0.002   | 0.002   | 0.000   | 0.000   | 0.608   | 0.600   |
21	|       60 | 0.006   | 0.006   | 0.000   | 0.000   | 0.661   | 0.657   |
22	|       80 | 0.014   | 0.013   | 0.000   | 0.000   | 0.705   | 0.701   |
23	|      100 | 0.028   | 0.030   | 0.000   | 0.000   | 0.745   | 0.743   |
24	|      200 | 0.182   | 0.182   | 0.001   | 0.001   | 0.851   | 0.851   |
25	|      500 | 0.631   | 0.628   | 0.004   | 0.005   | 0.954   | 0.952   |
26	
27	### δ = 0.8
28	
29	| N/cohort | K=3 TPR | K=5 TPR | K=3 FPR | K=5 FPR | K=3 AUC | K=5 AUC |
30	|----------|---------|---------|---------|---------|---------|---------|
31	|       40 | 0.006   | 0.005   | 0.000   | 0.000   | 0.666   | 0.663   |
32	|       60 | 0.024   | 0.023   | 0.000   | 0.000   | 0.731   | 0.728   |
33	|       80 | 0.058   | 0.059   | 0.000   | 0.000   | 0.778   | 0.773   |
34	|      100 | 0.122   | 0.120   | 0.001   | 0.001   | 0.816   | 0.814   |
35	|      200 | 0.436   | 0.439   | 0.002   | 0.003   | 0.914   | 0.910   |
36	|      500 | 0.826   | 0.824   | 0.008   | 0.008   | 0.980   | 0.979   |
37	
38	### δ = 1.0
39	
40	| N/cohort | K=3 TPR | K=5 TPR | K=3 FPR | K=5 FPR | K=3 AUC | K=5 AUC |
41	|----------|---------|---------|---------|---------|---------|---------|
42	|       40 | 0.018   | 0.016   | 0.000   | 0.000   | 0.714   | 0.709   |
43	|       60 |
…[truncated 3630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-23T19:54:33.832933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/mmlu_bootstrap_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/mmlu_bootstrap_report.md"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-23T19:54:33.833062+00:00_

1	# MMLU Bootstrap 95% CI for MH-DIF C%
2	
3	## Method
4	
5	- Bootstrap resampling of **models** (not items), N=1000
6	- Per bootstrap: resample N_ref=1080 (2023) and N_foc=807 (2024) with replacement
7	- MH-DIF with 5-stratum total-score matching
8	- Validated against rest-score: diff = 0.00pp (speedup 196x)
9	- 95% CI via percentile method [2.5th, 97.5th]
10	- Seed = 42
11	
12	## Results
13	
14	| Metric | Value |
15	|--------|-------|
16	| Original C% (rest-score) | 31.32% |
17	| Original C% (total-score) | 31.32% |
18	| Bootstrap 95% CI | [29.38%, 38.05%] |
19	| Bootstrap mean | 33.14% |
20	| Bootstrap SD | 2.30% |
21	| Bias (mean − original) | +1.82pp |
22	| CI width | 8.67pp |
23	
24	## Random-Split Control (N=20)
25	
26	| Metric | Value |
27	|--------|-------|
28	| Control mean C% | 0.10% |
29	| Control SD | 0.11% |
30	| Control range | [0.03%, 0.54%] |
31	
32	## Interpretation
33	
34	- 95% CI [29.4%, 38.0%] — narrow, estimate is stable
35	- Control C% = 0.1% vs temporal C% = 31.3% — confirms DIF is temporal, not spurious
36	
37	Runtime: 2.4 min
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-23T19:54:33.833207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
  "description": "List plan_001 report directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
    "description": "List plan_001 report directory"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-23T19:54:33.833325+00:00_

plan_001_report.md
plan_001_report_00ca1f.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-23T19:54:33.833451+00:00_

# Plan 001: METABENCH Real-Data MH-DIF Analysis

## 1. Data & Setup

- Response matrix: **5227 models × 12508 items** (binary, MMLU)
- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
- Li et al. annotations: 9229 annotated items

## 2. ETS Classification

| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
|--------|--------|-------|---|---|---|----|-------------|------------|
| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |

## 3. Li et al. Proxy Validation

| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
|--------|-------------|---------------|--------------|------------------|------------|
| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |

## 4. Within-Family Analysis

- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)

### Cross-cohort vs within-family overlap

- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804

## 5. Domain Specificity

Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)

Top 15 subjects by C rate (temporal cohort):

| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
|---------|-------|---|-----|----------|----------|------|
| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
| professional_medicine | 248 | 94 | 37.9% | 0.595 | 0.630 | +0.035 |
| professional_law | 1331 | 498 | 37.4% | 0.438 | 0.454 | 
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-23T19:54:33.833607+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
  "description": "List plan_001_real_data_dif_mmlu/report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
    "description": "List plan_001_real_data_dif_mmlu/report"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-23T19:54:33.833747+00:00_

plan_001_report.md
plan_001_report_00ca1f.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-23T19:54:33.833899+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/difficulty_modeltype_interaction/",
  "description": "List difficulty_modeltype_interaction directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/difficulty_modeltype_interaction/",
    "description": "List difficulty_modeltype_interaction directory"
  }
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-23T19:54:33.834037+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport csv\n\n# Count llama-2 vs llama-3 models\nllama2_count = 0\nllama3_count = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if 'llama-2' in fam or fam == 'llama2':\n            llama2_count += 1\n        elif 'llama-3' in fam or fam == 'llama3':\n            llama3_count += 1\n\nprint(f'Llama-2: {llama2_count}, Llama-3: {llama3_count}')\n\n# Also check ability quintile groupings\nq12 = 0\nq45 = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        q = row.get('cohort_accuracy_quintile','')\n        if q in ['1','2']:\n            q12 += 1\n        elif q in ['4','5']:\n            q45 += 1\n\nprint(f'Q1-2: {q12}, Q4-5: {q45}')\n\"\n",
  "description": "Count llama family members and ability quintile group sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport csv\n\n# Count llama-2 vs llama-3 models\nllama2_count = 0\nllama3_count = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if 'llama-2' in fam or fam == 'llama2':\n            llama2_count += 1\n        elif 'llama-3' in fam or fam == 'llama3':\n            llama3_count += 1\n\nprint(f'Llama-2: {llama2_count}, Llama-3: {llama3_count}')\n\n# Also check ability quintile groupings\nq12 = 0\nq45 = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        q = row.get('cohort_accuracy_quintile','')\n        if q in ['1','2']:\n            q12 += 1\n        elif q in ['4','5']:\n            q45 += 1\n\nprint(f'Q1-2: {q12}, Q4-5: {q45}')\n\"\n",
    "description": "Count llama family members and ability quintile group sizes"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-23T19:54:33.834162+00:00_

Llama-2: 161, Llama-3: 316
Q1-2: 2092, Q4-5: 2089

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-23T19:54:33.834282+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-23T19:54:33.834410+00:00_

1	# R15-SF7: Random Split Control — 2024 Cohort
2	
3	## Setup
4	
5	- **Cohort**: 2024 temporal cohort (N = 807 models)
6	- **Items**: 12508 MMLU items
7	- **Procedure**: 100 random 50/50 splits within the 2024 cohort
8	- **DIF method**: 5-stratum MH-DIF with Yates-corrected chi-squared
9	- **C% criterion**: |Δ_MH| ≥ 1.5 AND p < 0.05 (ETS Category C)
10	
11	## Results
12	
13	| Metric | Value |
14	|--------|-------|
15	| Mean C% | 1.335% |
16	| SD | 1.052% |
17	| 95% CI | [1.129%, 1.541%] |
18	| Min | 0.288% |
19	| Max | 7.675% |
20	| N reps | 100 |
21	
22	## Size-Matched Control
23	
24	To verify that the within-cohort C% is consistent with MH-DIF's null behavior at this
25	sample size, we ran 20 additional random splits from the **full** 5,227-model pool
26	using the same group sizes (403 vs 404):
27	
28	| Metric | Value |
29	|--------|-------|
30	| Mean C% (full-sample, size-matched) | 1.400% |
31	| SD | 0.779% |
32	
33	The within-cohort (1.335%) and full-sample (1.400%) baselines are
34	comparable, confirming that the ~1% level reflects the expected false-positive rate of
35	MH-DIF at this sample size (403 vs 404 per split), not cohort-specific structure.
36	
37	## Comparison
38	
39	| Split type | C% | N per group |
40	|------------|-----|-------------|
41	| **Temporal (pre-2024 vs 2024)** | **31.3%** | 1,080 vs 807 |
42	| Random within 2024 cohort | 1.335% | ~403 vs ~404 |
43	| Size-matched control (full sample) | 1.400% | 403 vs 404 |
44	| Random baseline (large groups) | 0.10% | 1,080 vs 807 |
45	
46	## Conclusion
47	
48	Random splitting within the 2024 cohort yields C% = 1.335% (95% CI:
49	[1.129%, 1.541%]). This is consistent with the size-matched full-sample
50	control (1.400%), confirming that MH-DIF does not produce spurious C-flagged
51	items when no genuine differential functioning exists. The temporal split C% of 31.3%
52	is 23× larger than the random-split baseline, ruling out
53	statistical artifact as an explanation.
54	
55	The ~1% baseline (versus ~0
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-23T19:54:33.834558+00:00_

interaction_analysis.py
interaction_regression.csv
interaction_report.md
within_family_paired.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-23T19:54:33.834684+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/",
  "description": "List plan_011 directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/",
    "description": "List plan_011 directories"
  }
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-23T19:54:33.834832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-23T19:54:33.834968+00:00_

1	# Plan 001: METABENCH Real-Data MH-DIF Analysis
2	
3	## 1. Data & Setup
4	
5	- Response matrix: **5227 models × 12508 items** (binary, MMLU)
6	- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
7	- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
8	- Li et al. annotations: 9229 annotated items
9	
10	## 2. ETS Classification
11	
12	| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
13	|--------|--------|-------|---|---|---|----|-------------|------------|
14	| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
15	| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
16	| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
17	
18	## 3. Li et al. Proxy Validation
19	
20	| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
21	|--------|-------------|---------------|--------------|------------------|------------|
22	| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
23	| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |
24	
25	## 4. Within-Family Analysis
26	
27	- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
28	- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)
29	
30	### Cross-cohort vs within-family overlap
31	
32	- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
33	- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804
34	
35	## 5. Domain Specificity
36	
37	Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)
38	
39	Top 15 subjects by C rate (temporal cohort):
40	
41	| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
42	|---------|-------|---|-----|----------|----------|------|
43	| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
44	| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
45	| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
46	| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-23T19:54:33.835114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check the plan_032 random baseline for MMLU\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/random_baseline_summary.csv",
  "description": "Check MMLU random baseline summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check the plan_032 random baseline for MMLU\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/random_baseline_summary.csv",
    "description": "Check MMLU random baseline summary"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-23T19:54:33.835238+00:00_

dose_response_summary.csv
injection_results.csv
per_item_results.csv
plan_011_analysis.py
plan_011_report.md
data
intermediate
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-23T19:54:33.835362+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/",
  "description": "List mixed_mechanism_semisynthetic directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/",
    "description": "List mixed_mechanism_semisynthetic directory"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-23T19:54:33.835483+00:00_

trial,seed,rank_change_std,mean_abs_rank_change,pct_change_ge5,pct_change_ge10,pct_change_ge50,pct_change_ge100,cohort_2023_mean_change,cohort_2024_mean_change
0,42,60.64485746809391,37.16166060837957,79.54849818251387,65.6782092978764,25.215228620623687,9.890950832217333,-3.8666666666666667,21.242874845105327
1,43,51.45151196058692,32.152286206236845,79.49110388368089,65.12339774249091,22.17333078247561,5.758561316242586,5.6268518518518515,-9.869888475836431
2,44,72.51480918527321,42.10216185192271,79.9885211402334,66.25215228620624,27.147503348000768,11.746699827817103,-0.7824074074074074,40.10656753407683
3,45,73.65909926242324,42.66921752439258,81.5190357757796,66.00344365792998,26.95618901855749,12.339774249091256,-4.635185185185185,39.034696406443615
4,46,51.45174249728837,30.98297302467955,78.1136407116893,62.770231490338624,20.394107518653147,6.389898603405395,4.516666666666667,-12.635687732342008
5,47,63.217000350744954,36.380715515592115,78.97455519418405,64.26248325999617,23.34034819207959,9.29787641094318,2.433333333333333,-25.45353159851301
6,48,51.80385664989942,32.40596900707863,79.77807537784581,65.3912378037115,21.52286206236847,6.179452841017792,-1.461111111111111,-3.459727385377943
7,49,69.40555489523636,37.19609718767936,78.49626937057586,63.8607231681653,22.517696575473504,9.125693514444231,-1.6694444444444445,34.15365551425031
8,50,58.83049683581731,35.240864740769084,78.8023722976851,64.10943179644156,23.034245264970345,8.876984886167975,-5.924074074074074,2.184634448574969
9,51,58.90592643462852,34.681844270135834,79.31892098718194,65.10426630954659,23.569925387411516,7.422995982399081,4.5092592592592595,-21.168525402726146
10,52,72.30785215361249,40.95198010330974,79.73981251195714,66.23302085326192,26.57356035967094,10.426630954658505,8.975925925925926,-32.74969021065675
11,53,57.361189866730534,35.372488999426054,81.93992730055481,67.49569542758752,24.25865697340731,7.67170461067534,-1.4537037037037037,5.302354399008674
12,54,52.2483913100
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-23T19:54:33.835608+00:00_

all_results.csv
mixed_mechanism_report.md
mixed_mechanism_semisynthetic.py
scheme_d_results.csv
scheme_e_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-23T19:54:33.835744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/random_baseline_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/random_baseline_report.md"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-23T19:54:33.835874+00:00_

1	## Random Removal Baseline
2	
3	To test whether DIF-based removal produces effects distinct from arbitrary item removal,
4	we randomly removed 3918 items (matching the C-flagged count) in 20 independent trials
5	(seeds 42–61).
6	
7	### DIF Removal vs Random Removal
8	
9	| Metric | DIF Removal | Random Mean | Random Std | z-score |
10	|--------|------------|-------------|------------|---------|
11	| rank_change_std | +127.087 | +60.245 | 7.837 | +8.53 |
12	| mean_abs_rank_change | +74.685 | +36.013 | 3.626 | +10.66 |
13	| pct_change_ge5 | +89.516 | +79.695 | 1.066 | +9.21 |
14	| pct_change_ge10 | +79.548 | +65.255 | 1.150 | +12.43 |
15	| pct_change_ge50 | +41.860 | +23.910 | 2.167 | +8.28 |
16	| pct_change_ge100 | +24.813 | +8.527 | 1.976 | +8.24 |
17	| cohort_2023_mean_change | -22.562 | +0.431 | 4.119 | -5.58 |
18	| cohort_2024_mean_change | +73.599 | +2.787 | 21.162 | +3.35 |
19	
20	### Cohort Asymmetry
21	
22	The critical test: DIF removal shifts 2024 models up by +73.6 ranks
23	and 2023 models down by -22.6 ranks (gap = +96.2).
24	Random removal produces near-zero cohort bias: 2024 = +2.8 ± 21.2,
25	2023 = +0.4 ± 4.1 (gap z = +4.35).
26	
27	This confirms that the cohort-asymmetric rank shift is specific to DIF-flagged items,
28	not an artifact of removing 31% of items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 229 · 2026-05-23T19:54:33.836019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/run_final.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/run_final.log"
  }
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-23T19:54:33.836160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/difficulty_modeltype_interaction/interaction_report.md",
  "description": "Read difficulty-modeltype interaction report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/difficulty_modeltype_interaction/interaction_report.md",
    "description": "Read difficulty-modeltype interaction report"
  }
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-23T19:54:33.836291+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "29\\.2|29\\.2%|C%.*29|OR.*4\\.75|4\\.75.*OR|odds.*ratio.*4\\.75|4\\.75.*odds",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "29\\.2|29\\.2%|C%.*29|OR.*4\\.75|4\\.75.*OR|odds.*ratio.*4\\.75|4\\.75.*odds",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-23T19:54:33.836423+00:00_

# Difficulty × Model-Type Interaction Analysis

## Purpose

Test whether the base-vs-instruct DIF direction reversal (base: 60.1% ref-favoring,
instruct: 65.6% focal-favoring, χ²=562.7) is confounded by item difficulty.

## Part 1: Logistic Regression

**Sample:** 4018 base-C + 4567 instruct-C item-observations (items appearing
in both contribute two rows; cluster-robust SEs by item).

**DV:** DIF direction (1=focal-favoring, 0=ref-favoring)
**IVs:** difficulty_z (standardized proportion-correct), model_type (0=base, 1=instruct),
difficulty_z × model_type

| Variable | β | SE | z | p | OR | 95% CI |
|----------|----:|----:|----:|----:|----:|--------|
| intercept | -0.7635 | 0.0457 | -16.72 | 8.74e-63 | 0.466 | [0.426, 0.510] |
| difficulty_z | -1.9184 | 0.0520 | -36.90 | 4.60e-298 | 0.147 | [0.133, 0.163] |
| model_type | 1.4442 | 0.0450 | 32.07 | 1.27e-225 | 4.239 | [3.880, 4.630] |
| diff×type | 1.5590 | 0.0533 | 29.25 | 4.86e-188 | 4.754 | [4.283, 5.278] |

**Key finding:** The model_type main effect is highly significant
(β=1.444, OR=4.239, p=1.27e-225),
confirming that instruct models have systematically higher probability of focal-favoring DIF
even after controlling for item difficulty.

The interaction term (β=1.559, p=4.86e-188)
is significant, indicating that
difficulty does modulate the
base-vs-instruct direction difference.

## Part 2: Within-Family Paired Analysis

Families with ≥10 base and ≥10 instruct models.
MH-DIF computed within each family (base=ref, instruct=foc).

| Family | N_base | N_inst | C% | Inst-fav% | ρ(diff,Δ) |
|--------|-------:|-------:|----:|----------:|----------:|
| deepseek | 14 | 10 | 0.0 | — | — |
| gemma | 55 | 17 | 1.8 | 59.8 | -0.171 |
| gemma-2 | 18 | 18 | 0.8 | 53.1 | 0.170 |
| llama-2 | 114 | 47 | 21.9 | 48.0 | -0.034 |
| llama-3 | 206 | 109 | 10.7 | 67.5 | 0.462 |
| mistral | 449 | 98 | 18.4 | 43.8 | -0.357 |
| mixtral | 104 | 16 | 1.0 | 55.6 | -0.282 |
| qwen-1.5 | 42 | 27 | 9.0 | 49.2 | -0.166 |
| solar | 56 | 35 | 5.6
…[truncated 2004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-23T19:54:33.836576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md",
  "description": "Read plan_011 injection report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md",
    "description": "Read plan_011 injection report"
  }
}
```

</details>

---


### Tool result

_source line 234 · 2026-05-23T19:54:33.836728+00:00_

1	Loading data...
2	  N_temporal=1887, N_ref=1080, N_foc=807, J=12508
3	  Loaded in 1.8s
4	Precomputing strata...
5	  Done in 3.5s  (MAX_BINS=5)
6	
7	Verifying observed C%...
8	  Observed C% = 31.32%  (2.7s)
9	
10	Running 200 permutations (seed=42, est. 9 min)...
11	  [  10/200] C%=0.33%  max_null=1.14%  n_exceed=0  1.9s/perm  ETA 6.0min
12	  [  20/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.9s/perm  ETA 5.7min
13	  [  30/200] C%=0.10%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 5.6min
14	  [  40/200] C%=0.01%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 5.3min
15	  [  50/200] C%=0.07%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 5.0min
16	  [  60/200] C%=0.18%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 4.6min
17	  [  70/200] C%=0.07%  max_null=1.14%  n_exceed=0  1.9s/perm  ETA 4.1min
18	  [  80/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.8s/perm  ETA 3.5min
19	  [  90/200] C%=0.06%  max_null=1.14%  n_exceed=0  1.7s/perm  ETA 3.1min
20	  [ 100/200] C%=0.12%  max_null=1.14%  n_exceed=0  1.6s/perm  ETA 2.6min
21	
22	  [checkpoint] 100 permutations done, n_exceed=0, max_null=1.14%
23	  Already p < 0.01; continuing to 200 for precision.
24	
25	  [ 110/200] C%=0.14%  max_null=1.14%  n_exceed=0  1.5s/perm  ETA 2.3min
26	  [ 120/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.5s/perm  ETA 2.0min
27	  [ 130/200] C%=0.41%  max_null=1.14%  n_exceed=0  1.4s/perm  ETA 1.7min
28	  [ 140/200] C%=0.04%  max_null=1.14%  n_exceed=0  1.4s/perm  ETA 1.4min
29	  [ 150/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.4s/perm  ETA 1.1min
30	  [ 160/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.9min
31	  [ 170/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.7min
32	  [ 180/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.4min
33	  [ 190/200] C%=0.05%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.2min
34	  [ 200/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.0min
35	
36	Completed 200 permutations in 4.2 min
37	
38	================================
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-23T19:54:33.836885+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Check 2023 random split mean C%\n# From permutation_results.csv - what's the mean?\n# Already computed: Mean = 0.0999% from 200 permutations\n# Paper says 0.62% - those are the plan_029 results? But mean was 0.10%\n\n# Let's check if there's a separate 2023 random split analysis  \nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor d in os.listdir(base):\n    if 'random' in d.lower() or 'split' in d.lower() or 'sanity' in d.lower():\n        print(d)\n\"\n",
  "description": "Find all random split related directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Check 2023 random split mean C%\n# From permutation_results.csv - what's the mean?\n# Already computed: Mean = 0.0999% from 200 permutations\n# Paper says 0.62% - those are the plan_029 results? But mean was 0.10%\n\n# Let's check if there's a separate 2023 random split analysis  \nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor d in os.listdir(base):\n    if 'random' in d.lower() or 'split' in d.lower() or 'sanity' in d.lower():\n        print(d)\n\"\n",
    "description": "Find all random split related directories"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-23T19:54:33.837008+00:00_

r15_random_split_control

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-23T19:54:33.837147+00:00_

# Plan 011: Semi-Synthetic DIF Validation

## 1. Objective

Inject known **differential** contamination into real MMLU response data and test
whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find
enrichment was due to Li et al. labels being non-differential (global contamination)
rather than a fundamental limitation of MH-DIF.

## 2. Setup

- **Baseline items**: 500 (clean in Li et al. + ETS A in plan_001 ability DIF)
- **Contaminated per run**: 100 of 500
- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
- **Seeds per p**: 5

### Cohort definitions

- **ability**: ref N=2092, foc N=2089, foc inject N=2089
- **temporal**: ref N=1080, foc N=807, foc inject N=787

> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction (ref max=0.6319, foc min=0.6772). All focal models used for injection. MH stratification handles ability matching.

### MH variants

| Variant | Matching variable | Rationale |
|---------|-------------------|-----------|
| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |
| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |
| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |

## 3. Results by MH Variant

### Standard MH

| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
|--------|---|----------------|----------------|------|-----------|----------|
| ability | 0.0 | 0.594±0.053 | 0.611±0.013 | +0.000 | 0.96 | 0.4231 |
| ability | 0.3 | 0.700±0.057 | 0.609±0.026 | +0.106 | 1.58 | 0.2555 |
| ability | 0.5 | 0.760±0.046 | 0.600±0.021 | +0.166 | 2.21 | 0.0067 |
| ability | 0.7 | 0.806±0.036 | 0.598±0.030 | +0.212 | 2.90 | 0.0002 |
| ability | 1.0 | 0.816±0.035 | 0.596±0.023 | +0.222 | 3.17 | 0.0001 |
| temporal | 0.
…[truncated 4892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-23T19:54:33.837307+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "20.*random.split|random.split.*20|baseline.*20|C%.*12|12%.*MMLU|MMLU.*12%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "20.*random.split|random.split.*20|baseline.*20|C%.*12|12%.*MMLU|MMLU.*12%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool call

_source line 239 · 2026-05-23T19:54:33.837438+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/plan_011_report.md 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/",
  "description": "Read plan_011 semi-synthetic report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/plan_011_report.md 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/",
    "description": "Read plan_011 semi-synthetic report"
  }
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-23T19:54:33.837566+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The paper uses \"Rand C%\" = 0.62 for MMLU but source shows 0.18.\n# Let me check what other sources say for MMLU random C%\n# Also check plan_001_real_data_dif_mmlu\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
  "description": "Check plan_001_real_data_dif_mmlu report directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The paper uses \"Rand C%\" = 0.62 for MMLU but source shows 0.18.\n# Let me check what other sources say for MMLU random C%\n# Also check plan_001_real_data_dif_mmlu\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/",
    "description": "Check plan_001_real_data_dif_mmlu report directory"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-23T19:54:33.837682+00:00_

plan_001_report.md
plan_001_report_00ca1f.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 242 · 2026-05-23T19:54:33.837821+00:00_

plan_011_report.md
plan_011_report_c7ae89.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-23T19:54:33.837945+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_report.md",
  "description": "Read mixed mechanism report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_report.md",
    "description": "Read mixed mechanism report"
  }
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-23T19:54:33.838075+00:00_

# Mixed-Mechanism Semi-Synthetic Injection

**Date**: 2026-05-23 01:35

**Config**: 20 seeds, 1080 ref models (861 base, 219 instruct), 807 foc models (548 base, 259 instruct), 12508 items

**Injection**: 30% focal models per type (164 base, 77 instruct), 3001 items (24%)


## Observed Data (for comparison)

| Metric | Observed |
|--------|----------|
| ρ(difficulty, δ_MH) overall | -0.597 |
| ρ(difficulty, δ_MH) base-only | -0.570 |
| ρ(difficulty, δ_MH) instruct-only | -0.079 |
| Direction reversal χ² | 562.7 |

## Baseline (no injection)

| Metric | Overall | Base-only | Instruct-only |
|--------|---------|-----------|---------------|
| C% | 31.3% | 32.1% | 36.5% |
| ρ(diff, δ) | -0.587 | -0.570 | -0.079 |
| % focal-favoring | 43.9% | 39.9% | 65.6% |

## Scheme D — base=difficulty, instruct=uniform

| Metric | Overall | Base-only | Instruct-only | Observed |
|--------|---------|-----------|---------------|----------|
| ρ(diff, δ_MH) among C items | -0.676 ± 0.005 | -0.638 ± 0.007 | -0.302 ± 0.090 | -0.597 / -0.570 / -0.079 |
| ρ(diff, Δδ) injected items | -0.897 ± 0.018 | -0.875 ± 0.026 | -0.670 ± 0.111 | — |
| C% | 35.3±1.0 | 37.4±1.3 | 37.5±0.7 | — |
| % focal-favoring | 43.5±1.2 | 38.6±1.3 | 64.3±3.2 | — |
| Direction reversal χ² | 634.4 ± 183.9 | — | — | 562.7 |
| N DIF-C | 4416±127 | 4677±169 | 4692±83 | — |
| Flips (base/instruct) | 167891 | 123773 | 44117 | — |

## Scheme E — base=uniform, instruct=difficulty

| Metric | Overall | Base-only | Instruct-only | Observed |
|--------|---------|-----------|---------------|----------|
| ρ(diff, δ_MH) among C items | -0.668 ± 0.006 | -0.626 ± 0.007 | -0.418 ± 0.070 | -0.597 / -0.570 / -0.079 |
| ρ(diff, Δδ) injected items | -0.743 ± 0.058 | -0.448 ± 0.097 | -0.894 ± 0.027 | — |
| C% | 34.1±0.9 | 34.0±1.0 | 38.5±0.6 | — |
| % focal-favoring | 45.4±1.4 | 42.1±1.3 | 61.8±2.8 | — |
| Direction reversal χ² | 362.9 ± 120.7 | — | — | 562.7 |
| N DIF-C | 4268±118 | 4249±128 | 4814±72 | — |
| Flips (base/instruct) | 155544
…[truncated 1499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 245 · 2026-05-23T19:54:33.838223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
  }
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-23T19:54:33.838358+00:00_

1	# Plan 001: METABENCH Real-Data MH-DIF Analysis
2	
3	## 1. Data & Setup
4	
5	- Response matrix: **5227 models × 12508 items** (binary, MMLU)
6	- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
7	- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
8	- Li et al. annotations: 9229 annotated items
9	
10	## 2. ETS Classification
11	
12	| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
13	|--------|--------|-------|---|---|---|----|-------------|------------|
14	| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
15	| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
16	| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
17	
18	## 3. Li et al. Proxy Validation
19	
20	| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
21	|--------|-------------|---------------|--------------|------------------|------------|
22	| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
23	| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |
24	
25	## 4. Within-Family Analysis
26	
27	- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
28	- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)
29	
30	### Cross-cohort vs within-family overlap
31	
32	- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
33	- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804
34	
35	## 5. Domain Specificity
36	
37	Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)
38	
39	Top 15 subjects by C rate (temporal cohort):
40	
41	| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
42	|---------|-------|---|-----|----------|----------|------|
43	| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
44	| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
45	| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
46	| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 247 · 2026-05-23T19:54:33.838514+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check score_inflation_analysis / plan_032 for downstream numbers\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/random_baseline_summary.csv",
  "description": "Read random baseline summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check score_inflation_analysis / plan_032 for downstream numbers\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/random_baseline_summary.csv",
    "description": "Read random baseline summary"
  }
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-23T19:54:33.838648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The plan_029 does label-permutation (not a true 540/540 within-2023 split)\n# The paper says \"Random split 2023 (sanity) & 540 / 540 & 0.62\"\n# plan_029 uses 1080 ref vs 807 focal permuted labels -> NOT the 540/540 split\n# Let's find the actual 540/540 within-2023 split source\n# plan_001_report mentions: \"Random half-split of 2023 cohort: 0.18% C\"\n# But paper says 0.62% ...\n\n# Let me search for a report with 540/540 split\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if '0.62' in content or '540' in content:\n        print(f)\n\" | head -20\n",
  "description": "Search for 540/540 split and 0.62 C% source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The plan_029 does label-permutation (not a true 540/540 within-2023 split)\n# The paper says \"Random split 2023 (sanity) & 540 / 540 & 0.62\"\n# plan_029 uses 1080 ref vs 807 focal permuted labels -> NOT the 540/540 split\n# Let's find the actual 540/540 within-2023 split source\n# plan_001_report mentions: \"Random half-split of 2023 cohort: 0.18% C\"\n# But paper says 0.62% ...\n\n# Let me search for a report with 540/540 split\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if '0.62' in content or '540' in content:\n        print(f)\n\" | head -20\n",
    "description": "Search for 540/540 split and 0.62 C% source"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-23T19:54:33.838799+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part1.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_013_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_010_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step1_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/sf8_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/base_instruct_survey.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/score_inflation_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_016_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results_5c7f57.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/k3_power_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifac
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 250 · 2026-05-23T19:54:33.838943+00:00_

trial,seed,rank_change_std,mean_abs_rank_change,pct_change_ge5,pct_change_ge10,pct_change_ge50,pct_change_ge100,cohort_2023_mean_change,cohort_2024_mean_change
0,42,60.64485746809391,37.16166060837957,79.54849818251387,65.6782092978764,25.215228620623687,9.890950832217333,-3.8666666666666667,21.242874845105327
1,43,51.45151196058692,32.152286206236845,79.49110388368089,65.12339774249091,22.17333078247561,5.758561316242586,5.6268518518518515,-9.869888475836431
2,44,72.51480918527321,42.10216185192271,79.9885211402334,66.25215228620624,27.147503348000768,11.746699827817103,-0.7824074074074074,40.10656753407683
3,45,73.65909926242324,42.66921752439258,81.5190357757796,66.00344365792998,26.95618901855749,12.339774249091256,-4.635185185185185,39.034696406443615
4,46,51.45174249728837,30.98297302467955,78.1136407116893,62.770231490338624,20.394107518653147,6.389898603405395,4.516666666666667,-12.635687732342008
5,47,63.217000350744954,36.380715515592115,78.97455519418405,64.26248325999617,23.34034819207959,9.29787641094318,2.433333333333333,-25.45353159851301
6,48,51.80385664989942,32.40596900707863,79.77807537784581,65.3912378037115,21.52286206236847,6.179452841017792,-1.461111111111111,-3.459727385377943
7,49,69.40555489523636,37.19609718767936,78.49626937057586,63.8607231681653,22.517696575473504,9.125693514444231,-1.6694444444444445,34.15365551425031
8,50,58.83049683581731,35.240864740769084,78.8023722976851,64.10943179644156,23.034245264970345,8.876984886167975,-5.924074074074074,2.184634448574969
9,51,58.90592643462852,34.681844270135834,79.31892098718194,65.10426630954659,23.569925387411516,7.422995982399081,4.5092592592592595,-21.168525402726146
10,52,72.30785215361249,40.95198010330974,79.73981251195714,66.23302085326192,26.57356035967094,10.426630954658505,8.975925925925926,-32.74969021065675
11,53,57.361189866730534,35.372488999426054,81.93992730055481,67.49569542758752,24.25865697340731,7.67170461067534,-1.4537037037037037,5.302354399008674
12,54,52.2483913100
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-23T19:54:33.839086+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check score inflation analysis\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep score_inflation; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/",
  "description": "Look for score inflation artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check score inflation analysis\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep score_inflation; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/",
    "description": "Look for score inflation artifacts"
  }
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-23T19:54:33.839221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Critical finding: plan_001 shows MMLU random split gives 0.18% C\n# But the paper Table 3 shows 0.62 for MMLU Rand C%\n# Let me check where 0.62 comes from — maybe a different random split approach\n# Check plan_029 more carefully (only MMLU runs permutation null)\n# And check if there's an updated version\n\n# Check the multi_bench_summary.csv.bak\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv.bak",
  "description": "Check backup multi_bench_summary for MMLU random C%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Critical finding: plan_001 shows MMLU random split gives 0.18% C\n# But the paper Table 3 shows 0.62 for MMLU Rand C%\n# Let me check where 0.62 comes from — maybe a different random split approach\n# Check plan_029 more carefully (only MMLU runs permutation null)\n# And check if there's an updated version\n\n# Check the multi_bench_summary.csv.bak\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv.bak",
    "description": "Check backup multi_bench_summary for MMLU random C%"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-23T19:54:33.839351+00:00_

benchmark,n_items,n_ref,n_foc,n_ets_a,n_ets_b,n_ets_c,pct_c,random_pct_c,status
mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
winogrande,1267,1017,803,612,271,384,30.3,0.32,OK
truthfulqa,817,1080,807,398,176,243,29.7,0.37,OK
arc,1172,1080,807,642,215,315,26.9,0.6,OK
gsm8k,1319,1017,804,825,245,249,18.9,0.3,PRIOR
hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-23T19:54:33.839466+00:00_

score_inflation_analysis
cleaned_mmlu_analysis.csv
data
dif_vs_random_comparison.csv
per_subject_dif_concentration.csv
plan_032_dif_cleaned_mmlu.py
plan_032_random_baseline.py
plan_032_report.md
random_baseline_report.md
random_baseline_summary.csv
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-23T19:54:33.839590+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv | head -5",
  "description": "Check cleaned MMLU analysis for score shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv | head -5",
    "description": "Check cleaned MMLU analysis for score shift"
  }
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-23T19:54:33.839729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-23T19:54:33.839866+00:00_

1	# Random-Split |Δ_MH| Null Distribution Report
2	
3	## Setup
4	- Cohort: 2023 models (N = 1080)
5	- Items: J = 12508
6	- Splits: 100 random permutations (each 540 ref vs 540 foc)
7	- Strata: 5 total-score quantile bins
8	- Total (item × split) observations: 1,250,800
9	- Runtime: 2.5s
10	
11	## Null Distribution Percentiles
12	
13	| Percentile | |Δ_MH| |
14	|------------|--------|
15	| 50th | 0.2956 |
16	| 90th | 0.7911 |
17	| 95th | 0.9898 |
18	| 97.5th | 1.1874 |
19	| 99th | 1.4504 |
20	| 99.5th | 1.6536 |
21	| 99.9th | 2.1998 |
22	
23	## ETS Threshold Comparison
24	
25	- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): 0.048206 (4.8206%)
26	- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): 0.008480 (0.8480%)
27	- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: 3717 / 12508 (29.72%)
28	
29	### ETS C Classification (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05)
30	
31	- Mean null C% per split: 0.6247%
32	- C% range across splits: [0.0640%, 5.8523%]
33	- Fraction of (item, split) classified C: 0.006247 (0.6247%)
34	- Items classified C in at least one split: 3702 / 12508 (29.60%)
35	
36	## Interpretation
37	
38	**P95 = 0.9898** (vs ETS B = 1.0): under random splitting, ~5% of item-level |Δ_MH| values approach B-level magnitude purely by chance.
39	
40	**P99 = 1.4504** (vs ETS C = 1.5): the null 99th percentile nearly reaches the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.
41	
42	**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the baseline false-positive rate for interpreting these observed rates.
43	
44	The 99th percentile (1.4504) and 99.9th percentile (2.1998) provide upper bounds on chance-level |Δ_MH| fluctuations.
45	
46	## Distribution Shape
47	
48	- Mean |Δ_MH| across all observations: 0.3740
49	- Median |Δ_MH|: 0.2956
50	- Std dev: 0.3205
51	- Skewness: 1.7897
…[truncated 225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 258 · 2026-05-23T19:54:33.840009+00:00_

model_name,score_full,score_cleaned,rank_full,rank_cleaned,rank_change,abs_rank_change,family,cohort_temporal
0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other
0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other
0-hero/Matter-0.1-7B-boost,0.6534218100415734,0.680093131548312,2811,2791,-20,20,unknown,other
0-hero/Matter-0.1-7B-boost-DPO,0.6549408378637672,0.6817229336437718,2776,2751,-25,25,,other

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-23T19:54:33.840156+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check for rank reversal (33.6%) in plan_032 report\ngrep -n \"33.6\\|pairwise\\|200\\|flip\\|reversal\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md",
  "description": "Find rank reversal stat in plan_032"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check for rank reversal (33.6%) in plan_032 report\ngrep -n \"33.6\\|pairwise\\|200\\|flip\\|reversal\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md",
    "description": "Find rank reversal stat in plan_032"
  }
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-23T19:54:33.840293+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Both CSV files (current and backup) show 0.18 for MMLU random_pct_c\n# Paper says 0.62 for MMLU Rand C% — investigate more\n# Check if this comes from a permutation null mean or different analysis\n# Check plan_029 report for a per-benchmark breakdown or additional benchmarks\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/run_final.log | head -50",
  "description": "Check permutation null run log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Both CSV files (current and backup) show 0.18 for MMLU random_pct_c\n# Paper says 0.62 for MMLU Rand C% — investigate more\n# Check if this comes from a permutation null mean or different analysis\n# Check plan_029 report for a per-benchmark breakdown or additional benchmarks\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/run_final.log | head -50",
    "description": "Check permutation null run log"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-23T19:54:33.840428+00:00_

Loading data...
  N_temporal=1887, N_ref=1080, N_foc=807, J=12508
  Loaded in 1.8s
Precomputing strata...
  Done in 3.5s  (MAX_BINS=5)

Verifying observed C%...
  Observed C% = 31.32%  (2.7s)

Running 200 permutations (seed=42, est. 9 min)...
  [  10/200] C%=0.33%  max_null=1.14%  n_exceed=0  1.9s/perm  ETA 6.0min
  [  20/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.9s/perm  ETA 5.7min
  [  30/200] C%=0.10%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 5.6min
  [  40/200] C%=0.01%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 5.3min
  [  50/200] C%=0.07%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 5.0min
  [  60/200] C%=0.18%  max_null=1.14%  n_exceed=0  2.0s/perm  ETA 4.6min
  [  70/200] C%=0.07%  max_null=1.14%  n_exceed=0  1.9s/perm  ETA 4.1min
  [  80/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.8s/perm  ETA 3.5min
  [  90/200] C%=0.06%  max_null=1.14%  n_exceed=0  1.7s/perm  ETA 3.1min
  [ 100/200] C%=0.12%  max_null=1.14%  n_exceed=0  1.6s/perm  ETA 2.6min

  [checkpoint] 100 permutations done, n_exceed=0, max_null=1.14%
  Already p < 0.01; continuing to 200 for precision.

  [ 110/200] C%=0.14%  max_null=1.14%  n_exceed=0  1.5s/perm  ETA 2.3min
  [ 120/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.5s/perm  ETA 2.0min
  [ 130/200] C%=0.41%  max_null=1.14%  n_exceed=0  1.4s/perm  ETA 1.7min
  [ 140/200] C%=0.04%  max_null=1.14%  n_exceed=0  1.4s/perm  ETA 1.4min
  [ 150/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.4s/perm  ETA 1.1min
  [ 160/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.9min
  [ 170/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.7min
  [ 180/200] C%=0.09%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.4min
  [ 190/200] C%=0.05%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.2min
  [ 200/200] C%=0.02%  max_null=1.14%  n_exceed=0  1.3s/perm  ETA 0.0min

Completed 200 permutations in 4.2 min

=======================================================
RESULTS
=======================================================
  Observed C%    
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-23T19:54:33.840566+00:00_

58:| 200 | 119 | 59.5% | 83 | 41.5% | 33 | 16.5% |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-23T19:54:33.840692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Look for +2.12pp accuracy shift in plan_032\ngrep -n \"2.12\\|0.29\\|d=0.31\\|score.*shift\\|accuracy.*shift\\|cohort.*diff\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md 2>/dev/null | head -20; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/report/",
  "description": "Search for score shift stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Look for +2.12pp accuracy shift in plan_032\ngrep -n \"2.12\\|0.29\\|d=0.31\\|score.*shift\\|accuracy.*shift\\|cohort.*diff\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md 2>/dev/null | head -20; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/report/",
    "description": "Search for score shift stats"
  }
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-23T19:54:33.840830+00:00_

plan_032_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-23T19:54:33.840953+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The permutation null gives 0.10% mean for MMLU, not 0.62\n# Let me look at what the paper says in the experiments section more carefully\n# And check if there's a separate analysis with 0.62\n\ngrep -r \"0\\.62\\|0\\.18\\|random.*c%\\|rand.*c\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -30",
  "description": "Check experiments.tex for random C% references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The permutation null gives 0.10% mean for MMLU, not 0.62\n# Let me look at what the paper says in the experiments section more carefully\n# And check if there's a separate analysis with 0.62\n\ngrep -r \"0\\.62\\|0\\.18\\|random.*c%\\|rand.*c\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -30",
    "description": "Check experiments.tex for random C% references"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-23T19:54:33.841094+00:00_

We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift $= {+}1.77$\,pp (\Cref{app:deff}). Under 100 random permutations within the 2023 cohort (540 vs.\ 540), the 99th percentile of item-level $|\Delta_{\mathrm{MH}}|$ is 1.45---just below the ETS~C threshold of 1.5---confirming that the threshold maintains a per-item false-positive rate below 1\%; together with the Monte Carlo power analysis (TPR $\geq 0.68$; \Cref{sec:validation}), this validates ETS~C classification for the LLM setting. No single family drives the signal (LOFO $|\Delta\mathrm{C\%}| \leq 2.93$\,pp); graduated de-duplication confirms C\% scales with power, not redundancy (\Cref{app:dedup_k}).
Three controls confirm genuine temporal change (\Cref{tab:temporal_landscape}): random splits yield mean C\% of 0.62\% (2023; 100 permutations) and 1.3\% (2024; 100 permutations), both ${\geq}24\times$ below temporal C\%; ability-quintile comparison yields 2.9\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\% $= 28.9\% \pm 0.1\%$, confirming at most ${\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \Cref{app:method_details}).
Random split 2023 (sanity) & 540 / 540 & 
…[truncated 2645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-23T19:54:33.841242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/",
  "description": "List score_inflation_analysis directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/",
    "description": "List score_inflation_analysis directory"
  }
}
```

</details>

---


### Tool result

_source line 268 · 2026-05-23T19:54:33.841358+00:00_

cohort_summary.csv
model_scores.csv
rank_displacement.pdf
rank_displacement.png
score_change_violin.pdf
score_change_violin.png
score_inflation.py
score_inflation_report.md
score_scatter.pdf
score_scatter.png
top_displaced.csv
type_summary.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-23T19:54:33.841480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check dif_vs_random_comparison for z-scores and rank reversal\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/dif_vs_random_comparison.csv",
  "description": "Read DIF vs random comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check dif_vs_random_comparison for z-scores and rank reversal\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/dif_vs_random_comparison.csv",
    "description": "Read DIF vs random comparison"
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-23T19:54:33.841617+00:00_

artifacts/rebuttal_talking_points.md:5:[Omitted long matching line]
artifacts/rebuttal_talking_points.md:13:[Omitted long matching line]
artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:35:conceptual_physics,STEM,202,112,31,59,29.21,0.4161,0.2037,0.0772,0.1437,0.1102,1.5244,54.24,32.0,27.0,0.6029
artifacts/plan_033_subject_dif_concentration/report/plan_033_report.md:63:business_ethics,Social Science,45,29.22868636002098,15.77131363997902,0.0007172367168043841
artifacts/plan_033_subject_dif_concentration/data/subject_dif_concentration.csv:35:conceptual_physics,STEM,202,112,31,59,29.21,0.4161,0.2037,0.0772,0.1437,0.1102,1.5244,54.24,32.0,27.0,0.6029
artifacts/plan_033_subject_dif_concentration/subject_residuals.csv:5:business_ethics,93,45,29.22868636002098,15.77131363997902,48.39,31.43,16.96,0.0007172367168043841,Social Science
artifacts/plan_033_subject_dif_concentration/subject_residuals.csv:9:philosophy,285,92,83.20710281373823,8.792897186261769,32.28,29.2,3.09,0.26797276498610323,Humanities
artifacts/plan_033_subject_dif_concentration/subject_residuals.csv:48:conceptual_physics,202,59,66.6474990890839,-7.647499089083894,29.21,32.99,-3.79,0.2626464432025541,STEM
artifacts/plan_033_subject_dif_concentration/plan_033_report.md:63:business_ethics,Social Science,45,29.22868636002098,15.77131363997902,0.0007172367168043841
artifacts/plan_028_multi_bench_dif/data/mmlu_bootstrap_results.csv:326:324,29.29325231851615
artifacts/plan_028_multi_bench_dif/data/mmlu_bootstrap_results.csv:938:936,29.277262551966743
artifacts/plan_028_multi_bench_dif/data/mmlu_bootstrap_results.csv:994:992,29.277262551966743
artifacts/plan_028_multi_bench_dif/truthfulqa_dif_results.csv:458:457,2.8596402414658924,-2.469135193972483,0.4574632529995119,29.25235343022619,6.353900683375713e-08,C
artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:6321:6320,2.5516807114252122,-2.201367774756783,0.4179587734323924,29.20162075051742,6.522462314695332e-08,C
artifacts/pla
…[truncated 7068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 5
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-23T19:54:33.841780+00:00_

metric,dif_removal,random_mean,random_std,z_score
rank_change_std,127.08674949749147,60.245428638447365,7.836854481765597,8.529100676115291
mean_abs_rank_change,74.68490529940692,36.01276066577386,3.6261632977706557,10.664755406191572
pct_change_ge5,89.5159747465085,79.69485364453799,1.066174204783192,9.211553851059131
pct_change_ge10,79.54849818251387,65.25540462980676,1.1495612718218582,12.433520424757347
pct_change_ge50,41.859575282188636,23.90950832217333,2.1672840121102,8.282286428412318
pct_change_ge100,24.813468528792807,8.526879663286781,1.975727625999505,8.243337113468144
cohort_2023_mean_change,-22.562037037037037,0.4314814814814816,4.1188208423088115,-5.58254884075741
cohort_2024_mean_change,73.59851301115242,2.786802973977695,21.162419849946886,3.346106472665622

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-23T19:54:33.841919+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Random split 2024: paper says ~400/~400 and 1.3%\n# r15 report says mean C% = 1.335% with 403 vs 404 per split = 807/2 = 403.5\n# So ~400/~400 and 1.3% matches r15 data\n\n# Now check the ability quintile N for ~2600/~2600\n# model_metadata says Q1-2: 2092, Q4-5: 2089\n# But paper says ~2600/~2600 -- discrepancy\n# Let me look at the plan_022 or other ability analysis\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if '2600' in content or '2,600' in content or '~2.6' in content:\n        print(f)\n\" | head -10\n",
  "description": "Search for 2600 ability quintile values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Random split 2024: paper says ~400/~400 and 1.3%\n# r15 report says mean C% = 1.335% with 403 vs 404 per split = 807/2 = 403.5\n# So ~400/~400 and 1.3% matches r15 data\n\n# Now check the ability quintile N for ~2600/~2600\n# model_metadata says Q1-2: 2092, Q4-5: 2089\n# But paper says ~2600/~2600 -- discrepancy\n# Let me look at the plan_022 or other ability analysis\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if '2600' in content or '2,600' in content or '~2.6' in content:\n        print(f)\n\" | head -10\n",
    "description": "Search for 2600 ability quintile values"
  }
}
```

</details>

---


### Tool call

_source line 273 · 2026-05-23T19:54:33.842056+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check plan_034 for cross-subject matching ΔFPR=0.000 and within-subject inflation\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md | head -120",
  "description": "Read plan_034 report for cross-subject ΔFPR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check plan_034 for cross-subject matching ΔFPR=0.000 and within-subject inflation\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md | head -120",
    "description": "Read plan_034 report for cross-subject ΔFPR"
  }
}
```

</details>

---


### Tool result

_source line 274 · 2026-05-23T19:54:33.842190+00:00_

# Plan 034: Multi-Subject Simultaneous Injection — Report

## Method

We test Proposition 1's robustness boundary by simultaneously injecting
differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).
For each (k, p, seed) combination:

1. Randomly select k target subjects from 57 MMLU subjects
2. For each item in the k target subjects, flip incorrect→correct responses
   in the focal group (2024 models within accuracy overlap) with probability p
3. Compute cross-subject MH-DIF for each target and non-target subject
   - Matching variable = total score on all subjects EXCEPT the tested one
   - For target subjects: matching includes injected scores from other targets
   - For non-target subjects: matching includes all injected target scores
4. Measure TPR on target subjects and FPR on non-target subjects

Grid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs.
Cohorts: reference = 2023 models (n=1080), focal = 2024 models (n=807),
focal inject subset = 787 models (within accuracy overlap).

## Core Results

### Non-Target Subjects (FPR — key result)

| k | p=0.1 ΔFPR | p=0.3 ΔFPR | p=0.5 ΔFPR |
|---|-----------|-----------|-----------|
| 1  | +0.002 ± 0.002 | +0.002 ± 0.001 | +0.002 ± 0.002 |
| 2  | +0.003 ± 0.002 | +0.003 ± 0.002 | +0.002 ± 0.002 |
| 3  | +0.002 ± 0.001 | +0.001 ± 0.003 | −0.001 ± 0.003 |
| 5  | +0.004 ± 0.002 | −0.000 ± 0.004 | +0.007 ± 0.007 |
| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |
| 20 | +0.001 ± 0.004 | **+0.072 ± 0.022** | **+0.167 ± 0.029** |

### Target Subjects (TPR)

| k | p=0.1 TPR | p=0.3 TPR | p=0.5 TPR |
|---|----------|----------|----------|
| 1  | 0.391 | 0.559 | 0.834 |
| 2  | 0.352 | 0.501 | 0.807 |
| 3  | 0.331 | 0.468 | 0.778 |
| 5  | 0.314 | 0.435 | 0.734 |
| 10 | 0.318 | 0.408 | 0.670 |
| 20 | 0.333 | 0.398 | 0.611 |

## Key Findings

### 1. Proposition 1 validity boundary: k ≈ 5–10

- **k ≤ 5** (≤ 8.8% of subjects contaminated): Non-target ΔFPR remains within
  no
…[truncated 2462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-23T19:54:33.842358+00:00_

artifacts/plan_020/circularity_ablation_results.csv:14:Random baseline,3918,2023,0.999611521824388,0.999611521824388,6.608017135174322e-05,0.0
artifacts/plan_020/circularity_ablation_results.csv:15:Random baseline,3918,2024,0.9990354510189734,0.9990354510189734,0.00021288299992876385,0.0
artifacts/plan_020/plan_020_circularity_ablation.py:176:print("\n=== Random removal baseline (20 replicates) ===")
artifacts/plan_020/plan_020_circularity_ablation.py:314:rpt.append("  5. **Random baseline**: mean ± SD over 20 random draws of K items")
artifacts/plan_020/circularity_ablation_report.md:21:  5. **Random baseline**: mean ± SD over 20 random draws of K items
artifacts/plan_020/circularity_ablation_report.md:34:| Random baseline | 3918 | 2023 | 0.999612 | +0.00 |
artifacts/plan_020/circularity_ablation_report.md:39:| Random baseline | 3918 | 2024 | 0.999035 | +0.00 |
artifacts/novelty_rebuttal_draft.md:11:3. **First systematic temporal audit at scale**: 5,227 models × 27,125 items across 6 benchmarks reveals 17.9–31.3% temporal measurement instability (45–174× above random baselines; §4.2, §4.7)—a phenomenon invisible in single-model or small-sample evaluations. The convergence at ~28–29% across multiple independent matching methods (nearest-neighbor, within-family ability-matched, de-duplicated K=20) establishes this as a robust empirical finding.
artifacts/plan_017/intermediate/plan_017_downstream_impact.py:11:  3. Random removal baseline (20 replicates per removal fraction)
artifacts/plan_017/plan_017_downstream_impact.py:11:  3. Random removal baseline (20 replicates per removal fraction)
artifacts/manifest.yaml:1398:  description: 'Random removal baseline: 20 replicates per removal fraction. DIF removal
artifacts/_project/report/temporal_accumulation_report.md:67:When holding the reference group constant (2023-H1), C% increases monotonically from 22.6% (6mo) to 32.7% (12mo), consistent with contamination accumulating over time. The well-powered 2023-H2→2024-H1 compa
…[truncated 5543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 5
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-23T19:54:33.842516+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Found the explanation: the 0.62 for MMLU Rand C% comes from \"Random split 2023 (sanity) & 540 / 540 & 0.62\"\n# This is a DIFFERENT random split analysis (2023 cohort split into 540/540), NOT the same as the plan_028 random_pct_c=0.18\n# Let me find the source for this 0.62 from 2023 cohort 540/540 split\n\ngrep -r \"0\\.62\\|540\\|sanity\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.csv\" --include=\"*.md\" | grep -v \".pyc\" | head -30",
  "description": "Find source for 0.62% random split C% for MMLU 2023 cohort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Found the explanation: the 0.62 for MMLU Rand C% comes from \"Random split 2023 (sanity) & 540 / 540 & 0.62\"\n# This is a DIFFERENT random split analysis (2023 cohort split into 540/540), NOT the same as the plan_028 random_pct_c=0.18\n# Let me find the source for this 0.62 from 2023 cohort 540/540 split\n\ngrep -r \"0\\.62\\|540\\|sanity\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.csv\" --include=\"*.md\" | grep -v \".pyc\" | head -30",
    "description": "Find source for 0.62% random split C% for MMLU 2023 cohort"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-23T19:54:33.842659+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:3,60,1.4,0.3076,0.0009,0.8465,0.0037,0.0001,0.6212,0.0304,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:3,200,1.0,0.6227,0.0036,0.939,0.0031,0.0002,0.7218,0.0183,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:5,200,1.0,0.6211,0.0043,0.9342,0.003,0.0002,0.723,0.022,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:5,500,0.6,0.6282,0.0047,0.9523,0.0032,0.0002,0.4201,0.0026,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:|      500 | 0.631   | 0.628   | 0.004   | 0.005   | 0.954   | 0.952   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:|      200 | 0.623   | 0.621   | 0.004   | 0.004   | 0.939   | 0.934   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:| N=200, δ=1.0 | **0.623** | 0.621 | **PASS** |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:anatomy.47,anatomy,-1.5067679509481338,1.5497774707995404e-07,0.0055069956711412,0.1195797120839599,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:astronomy.117,astronomy,-1.5296133136772294,0.0019361447907285,0.0417535408704187,0.2240665100526422,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_
…[truncated 5996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 278 · 2026-05-23T19:54:33.842823+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/report/plan_033_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_subject_level_rho/subject_level_rho_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-23T19:54:33.842957+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport csv\n\n# Count models in each quintile with actual sizes\nquintile_counts = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        q = row.get('cohort_accuracy_quintile','')\n        quintile_counts[q] = quintile_counts.get(q, 0) + 1\n\nprint('Quintile counts:', dict(sorted(quintile_counts.items())))\nq1 = quintile_counts.get('1',0)\nq2 = quintile_counts.get('2',0)\nq4 = quintile_counts.get('4',0)\nq5 = quintile_counts.get('5',0)\nprint(f'Q1+Q2: {q1+q2}, Q4+Q5: {q4+q5}')\n\"\n",
  "description": "Count models by accuracy quintile"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport csv\n\n# Count models in each quintile with actual sizes\nquintile_counts = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        q = row.get('cohort_accuracy_quintile','')\n        quintile_counts[q] = quintile_counts.get(q, 0) + 1\n\nprint('Quintile counts:', dict(sorted(quintile_counts.items())))\nq1 = quintile_counts.get('1',0)\nq2 = quintile_counts.get('2',0)\nq4 = quintile_counts.get('4',0)\nq5 = quintile_counts.get('5',0)\nprint(f'Q1+Q2: {q1+q2}, Q4+Q5: {q4+q5}')\n\"\n",
    "description": "Count models by accuracy quintile"
  }
}
```

</details>

---


### Tool result

_source line 280 · 2026-05-23T19:54:33.843078+00:00_

Quintile counts: {'1': 1046, '2': 1046, '3': 1046, '4': 1059, '5': 1030}
Q1+Q2: 2092, Q4+Q5: 2089

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 281 · 2026-05-23T19:54:33.843200+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md",
  "description": "Read score inflation report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md",
    "description": "Read score inflation report"
  }
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-23T19:54:33.843326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/interaction_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/interaction_report.md"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-23T19:54:33.843466+00:00_

1	# Difficulty × Model-Type Interaction Analysis
2	
3	## Purpose
4	
5	Test whether the base-vs-instruct DIF direction reversal (base: 60.1% ref-favoring,
6	instruct: 65.6% focal-favoring, χ²=562.7) is confounded by item difficulty.
7	
8	## Part 1: Logistic Regression
9	
10	**Sample:** 4018 base-C + 4567 instruct-C item-observations (items appearing
11	in both contribute two rows; cluster-robust SEs by item).
12	
13	**DV:** DIF direction (1=focal-favoring, 0=ref-favoring)
14	**IVs:** difficulty_z (standardized proportion-correct), model_type (0=base, 1=instruct),
15	difficulty_z × model_type
16	
17	| Variable | β | SE | z | p | OR | 95% CI |
18	|----------|----:|----:|----:|----:|----:|--------|
19	| intercept | -0.7635 | 0.0457 | -16.72 | 8.74e-63 | 0.466 | [0.426, 0.510] |
20	| difficulty_z | -1.9184 | 0.0520 | -36.90 | 4.60e-298 | 0.147 | [0.133, 0.163] |
21	| model_type | 1.4442 | 0.0450 | 32.07 | 1.27e-225 | 4.239 | [3.880, 4.630] |
22	| diff×type | 1.5590 | 0.0533 | 29.25 | 4.86e-188 | 4.754 | [4.283, 5.278] |
23	
24	**Key finding:** The model_type main effect is highly significant
25	(β=1.444, OR=4.239, p=1.27e-225),
26	confirming that instruct models have systematically higher probability of focal-favoring DIF
27	even after controlling for item difficulty.
28	
29	The interaction term (β=1.559, p=4.86e-188)
30	is significant, indicating that
31	difficulty does modulate the
32	base-vs-instruct direction difference.
33	
34	## Part 2: Within-Family Paired Analysis
35	
36	Families with ≥10 base and ≥10 instruct models.
37	MH-DIF computed within each family (base=ref, instruct=foc).
38	
39	| Family | N_base | N_inst | C% | Inst-fav% | ρ(diff,Δ) |
40	|--------|-------:|-------:|----:|----------:|----------:|
41	| deepseek | 14 | 10 | 0.0 | — | — |
42	| gemma | 55 | 17 | 1.8 | 59.8 | -0.171 |
43	| gemma-2 | 18 | 18 | 0.8 | 53.1 | 0.170 |
44	| llama-2 | 114 | 47 | 21.9 | 48.0 | -0.034 |
45	| llama-3 | 206 | 109 | 10.7 | 67.5 | 0.462 |
46	| mistral | 449 | 98 | 18.4 | 
…[truncated 2266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-23T19:54:33.843619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-23T19:54:33.843768+00:00_

1	# R15-SF7: Random Split Control — 2024 Cohort
2	
3	## Setup
4	
5	- **Cohort**: 2024 temporal cohort (N = 807 models)
6	- **Items**: 12508 MMLU items
7	- **Procedure**: 100 random 50/50 splits within the 2024 cohort
8	- **DIF method**: 5-stratum MH-DIF with Yates-corrected chi-squared
9	- **C% criterion**: |Δ_MH| ≥ 1.5 AND p < 0.05 (ETS Category C)
10	
11	## Results
12	
13	| Metric | Value |
14	|--------|-------|
15	| Mean C% | 1.335% |
16	| SD | 1.052% |
17	| 95% CI | [1.129%, 1.541%] |
18	| Min | 0.288% |
19	| Max | 7.675% |
20	| N reps | 100 |
21	
22	## Size-Matched Control
23	
24	To verify that the within-cohort C% is consistent with MH-DIF's null behavior at this
25	sample size, we ran 20 additional random splits from the **full** 5,227-model pool
26	using the same group sizes (403 vs 404):
27	
28	| Metric | Value |
29	|--------|-------|
30	| Mean C% (full-sample, size-matched) | 1.400% |
31	| SD | 0.779% |
32	
33	The within-cohort (1.335%) and full-sample (1.400%) baselines are
34	comparable, confirming that the ~1% level reflects the expected false-positive rate of
35	MH-DIF at this sample size (403 vs 404 per split), not cohort-specific structure.
36	
37	## Comparison
38	
39	| Split type | C% | N per group |
40	|------------|-----|-------------|
41	| **Temporal (pre-2024 vs 2024)** | **31.3%** | 1,080 vs 807 |
42	| Random within 2024 cohort | 1.335% | ~403 vs ~404 |
43	| Size-matched control (full sample) | 1.400% | 403 vs 404 |
44	| Random baseline (large groups) | 0.10% | 1,080 vs 807 |
45	
46	## Conclusion
47	
48	Random splitting within the 2024 cohort yields C% = 1.335% (95% CI:
49	[1.129%, 1.541%]). This is consistent with the size-matched full-sample
50	control (1.400%), confirming that MH-DIF does not produce spurious C-flagged
51	items when no genuine differential functioning exists. The temporal split C% of 31.3%
52	is 23× larger than the random-split baseline, ruling out
53	statistical artifact as an explanation.
54	
55	The ~1% baseline (versus ~0
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-23T19:54:33.843931+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check if there's a temporal landscape table in a dedicated artifact\ngrep -r \"temporal_landscape\\|0\\.62\\|sanity.*540\\|540.*sanity\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | grep -v \".pyc\" | head -20",
  "description": "Find source for temporal landscape 0.62 value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check if there's a temporal landscape table in a dedicated artifact\ngrep -r \"temporal_landscape\\|0\\.62\\|sanity.*540\\|540.*sanity\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | grep -v \".pyc\" | head -20",
    "description": "Find source for temporal landscape 0.62 value"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-23T19:54:33.844068+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:3,60,1.4,0.3076,0.0009,0.8465,0.0037,0.0001,0.6212,0.0304,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:3,200,1.0,0.6227,0.0036,0.939,0.0031,0.0002,0.7218,0.0183,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:5,200,1.0,0.6211,0.0043,0.9342,0.003,0.0002,0.723,0.022,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:5,500,0.6,0.6282,0.0047,0.9523,0.0032,0.0002,0.4201,0.0026,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:|      500 | 0.631   | 0.628   | 0.004   | 0.005   | 0.954   | 0.952   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:|      200 | 0.623   | 0.621   | 0.004   | 0.004   | 0.939   | 0.934   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:| N=200, δ=1.0 | **0.623** | 0.621 | **PASS** |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/family_rank_shifts.csv:mixtral,120,0.15,-0.5,484,0.621816703976122
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/family_rank_shifts.csv:gemma-1,1,30.0,30.0,30,0.6244003837543972
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/rank_changes.csv:Changgil/K2S3-Mistral-7b-v1.1,Mistral,0.6286376718899904,0.6618160651920838,3233,3093,140
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equa
…[truncated 2135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 288 · 2026-05-23T19:54:33.844237+00:00_

# Score Inflation & DIF-Corrected Scoring Analysis
**Date**: 2026-05-23
**Dataset**: 12508 items, 5227 models
**DIF-C items**: 3918 (31.3%)
**Stable items**: 8590 (68.7%)

## 1. Score Change Summary
### By Cohort
| Cohort | N | Mean Original | Mean Stable | Mean Δ (pp) | SD (pp) | 95% CI |
|--------|---|--------------|-------------|-------------|---------|--------|
| 2023 | 1080 | 0.5814 | 0.6049 | +2.35 | 0.88 | [+2.30, +2.40] |
| 2024 | 807 | 0.6068 | 0.6274 | +2.06 | 1.04 | [+1.99, +2.13] |
| other | 3340 | 0.5906 | 0.6112 | +2.05 | 0.92 | [+2.02, +2.08] |

### By Cohort × Model Type
| Cohort | Type | N | Mean Δ (pp) | SD (pp) | 95% CI |
|--------|------|---|-------------|---------|--------|
| 2023 | base | 805 | +2.37 | 0.88 | [+2.31, +2.43] |
| 2023 | instruct | 275 | +2.29 | 0.88 | [+2.19, +2.40] |
| 2024 | base | 534 | +2.06 | 1.06 | [+1.97, +2.15] |
| 2024 | instruct | 273 | +2.06 | 1.01 | [+1.94, +2.18] |
| other | base | 2742 | +2.05 | 0.92 | [+2.01, +2.08] |
| other | instruct | 598 | +2.09 | 0.95 | [+2.01, +2.16] |

### Effect Size
- 2024 vs 2023 score_change Cohen's d = -0.3051
- Welch's t-test: t = -6.553, p = 7.23e-11

## 2. Ranking Impact
- Overall Spearman ρ (original vs stable): **0.996455**
- Original vs adjusted: ρ = 0.999759
- Stable vs adjusted: ρ = 0.996489

### Top-20 DIF Victims (rank improves most)
| Model | Cohort | Type | Orig Score | Stable Score | Δ pp | Rank Disp |
|-------|--------|------|-----------|-------------|------|----------|
| liminerity/Blurstral-7b-slerp | other | base | 0.6948 | 0.7236 | +2.88 | +593 |
| DreadPoor/PAIN_LeDestroy-7B-task_arithmetic | other | base | 0.6984 | 0.7258 | +2.74 | +570 |
| flammenai/flammen26-mistral-7B | 2023 | base | 0.6961 | 0.7240 | +2.79 | +548 |
| Gille/StrangeMerges_2-7B-slerp | other | base | 0.6964 | 0.7239 | +2.74 | +518 |
| Gille/StrangeMerges_12-7B-slerp | other | base | 0.6960 | 0.7232 | +2.72 | +494 |
| jambroz/sixtyoneeighty-7b | other | base | 0.6972 | 0.7241 | +2.69 | +493 |
| jamb
…[truncated 3738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 289 · 2026-05-23T19:54:33.844403+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check the cross-subject delta FPR=0.000 for 5 subjects in plan_034\ngrep -n \"ΔFPR=0\\|cross.*subject\\|5 subjects\\|FPR.*0.000\\|within.*subject.*0.186\\|0.186\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md 2>/dev/null | head -20; \n# Also check plan_011 for within-subject +0.186 FPR inflation\ngrep -n \"0.186\\|within.*subject\\|FPR\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md | head -20",
  "description": "Find cross-subject ΔFPR=0.000 and within-subject +0.186"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check the cross-subject delta FPR=0.000 for 5 subjects in plan_034\ngrep -n \"ΔFPR=0\\|cross.*subject\\|5 subjects\\|FPR.*0.000\\|within.*subject.*0.186\\|0.186\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md 2>/dev/null | head -20; \n# Also check plan_011 for within-subject +0.186 FPR inflation\ngrep -n \"0.186\\|within.*subject\\|FPR\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md | head -20",
    "description": "Find cross-subject ΔFPR=0.000 and within-subject +0.186"
  }
}
```

</details>

---


### Tool result

_source line 290 · 2026-05-23T19:54:33.844537+00:00_

12:3. Compute cross-subject MH-DIF for each target and non-target subject
92:as: cross-subject DIF auditing remains reliable when the contaminated fraction
96:that Proposition 1's ΔFPR=0 guarantee degrades gracefully — it holds in
36:| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
51:| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
66:| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
79:## 4. Key Comparison: Baseline FPR by Variant
86:If external FPR ≪ standard FPR, the high baseline rate is from matching precision,
108:**ability**: baseline TPR=0.594/FPR=0.611, p=1.0 TPR=0.816/FPR=0.596, ΔTPR=+0.222
111:**temporal**: baseline TPR=0.308/FPR=0.298, p=1.0 TPR=1.000/FPR=0.616, ΔTPR=+0.692
116:**ability**: baseline TPR=0.600/FPR=0.596, p=1.0 TPR=0.818/FPR=0.596, ΔTPR=+0.218
119:**temporal**: baseline TPR=0.314/FPR=0.307, p=1.0 TPR=1.000/FPR=0.307, ΔTPR=+0.686
124:**ability**: baseline TPR=0.498/FPR=0.493, p=1.0 TPR=0.800/FPR=0.493, ΔTPR=+0.302
127:**temporal**: baseline TPR=0.326/FPR=0.314, p=1.0 TPR=1.000/FPR=0.314, ΔTPR=+0.674
134:- **Temporal + external matching**: TPR rises 0.326 → 1.000 (ΔTPR=+0.674), FPR 0.314 → 0.314
135:- **Ability + external matching**: TPR rises 0.498 → 0.800 (ΔTPR=+0.302), FPR 0.493 → 0.493
146:corrupted by injected items, inflating FPR. This is a known limitation when DIF items

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-23T19:54:33.844694+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search for within-subject +0.186 inflation - might be in plan_016_within_subject\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/",
  "description": "Check plan_016_within_subject directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search for within-subject +0.186 inflation - might be in plan_016_within_subject\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/",
    "description": "Check plan_016_within_subject directory"
  }
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-23T19:54:33.844855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "29\\.2.*C%|C%.*29\\.2|temporal.*29\\.2|29\\.2.*temporal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "29\\.2.*C%|C%.*29\\.2|temporal.*29\\.2|29\\.2.*temporal",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-23T19:54:33.844978+00:00_

data
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-23T19:54:33.845103+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check plan_001_real_data for groundtruth numbers\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md 2>/dev/null | head -100",
  "description": "Read plan_001_real_data report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check plan_001_real_data for groundtruth numbers\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md 2>/dev/null | head -100",
    "description": "Read plan_001_real_data report"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-23T19:54:33.845238+00:00_

# Plan 001: METABENCH Real-Data MH-DIF Analysis

## 1. Data & Setup

- Response matrix: **5227 models × 12508 items** (binary, MMLU)
- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
- Li et al. annotations: 9229 annotated items

## 2. ETS Classification

| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
|--------|--------|-------|---|---|---|----|-------------|------------|
| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |

## 3. Li et al. Proxy Validation

| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
|--------|-------------|---------------|--------------|------------------|------------|
| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |

## 4. Within-Family Analysis

- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)

### Cross-cohort vs within-family overlap

- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804

## 5. Domain Specificity

Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)

Top 15 subjects by C rate (temporal cohort):

| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
|---------|-------|---|-----|----------|----------|------|
| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
| professional_medicine | 248 | 94 | 37.9% | 0.595 | 0.630 | +0.035 |
| professional_law | 1331 | 498 | 37.4% | 0.438 | 0.454 | 
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-23T19:54:33.845393+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"29\\.2\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -20",
  "description": "Search for 29.2 in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"29\\.2\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -20",
    "description": "Search for 29.2 in experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-23T19:54:33.845517+00:00_

We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift $= {+}1.77$\,pp (\Cref{app:deff}). Under 100 random permutations within the 2023 cohort (540 vs.\ 540), the 99th percentile of item-level $|\Delta_{\mathrm{MH}}|$ is 1.45---just below the ETS~C threshold of 1.5---confirming that the threshold maintains a per-item false-positive rate below 1\%; together with the Monte Carlo power analysis (TPR $\geq 0.68$; \Cref{sec:validation}), this validates ETS~C classification for the LLM setting. No single family drives the signal (LOFO $|\Delta\mathrm{C\%}| \leq 2.93$\,pp); graduated de-duplication confirms C\% scales with power, not redundancy (\Cref{app:dedup_k}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-23T19:54:33.845654+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The 0.62 for MMLU Rand C% comes from plan_001 report section 7:\n# \"Random half-split of 2023 cohort: 0.18% C\"  -- that says 0.18\n# But the paper section on temporal landscape says \"random splits yield mean C% of 0.62% (2023; 100 permutations)\"\n# Let me look for a \"r15\" or related random split analysis that yields 0.62\n\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/",
  "description": "Check r15 random split control artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The 0.62 for MMLU Rand C% comes from plan_001 report section 7:\n# \"Random half-split of 2023 cohort: 0.18% C\"  -- that says 0.18\n# But the paper section on temporal landscape says \"random splits yield mean C% of 0.62% (2023; 100 permutations)\"\n# Let me look for a \"r15\" or related random split analysis that yields 0.62\n\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/",
    "description": "Check r15 random split control artifacts"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-23T19:54:33.845794+00:00_

random_split_analysis.py
random_split_report.md
random_split_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-23T19:54:33.845924+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Paper says ~2600/~2600 but data shows Q1-2: 2092, Q4-5: 2089\n# Those are substantially different. Let me check if there's a version with 2600\n\n# Maybe they use 4-quantile (Q1 vs Q4) or some other grouping?\n# Or maybe they consider 5-quantile with rounding to nearest 1000?\n# 5227 / 5 * 2 = 2090.8 -> rounds to ~2100, not ~2600\n# What if they use quintile definitions differently?\n# 5227 models * 0.4 = 2090.8 for bottom/top 40%\n# For 50% split: 5227/2 = 2613.5 -> 2614 each -> ~2600!\n\n# Or maybe the paper references a ~50/50 split by ability median?\n# plan_001_report says 'ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata'\n# The numbers 2092/2089 are what the data shows\n\n# So paper's '~2,600 / ~2,600' appears WRONG compared to source data 2092/2089\n# Let's double-check by looking for any analysis with those bigger N values\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.csv', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '2600' in content or '2,600' in content:\n            print(f)\n    except:\n        pass\n\" | head -10\n",
  "description": "Search CSV files for 2600 counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Paper says ~2600/~2600 but data shows Q1-2: 2092, Q4-5: 2089\n# Those are substantially different. Let me check if there's a version with 2600\n\n# Maybe they use 4-quantile (Q1 vs Q4) or some other grouping?\n# Or maybe they consider 5-quantile with rounding to nearest 1000?\n# 5227 / 5 * 2 = 2090.8 -> rounds to ~2100, not ~2600\n# What if they use quintile definitions differently?\n# 5227 models * 0.4 = 2090.8 for bottom/top 40%\n# For 50% split: 5227/2 = 2613.5 -> 2614 each -> ~2600!\n\n# Or maybe the paper references a ~50/50 split by ability median?\n# plan_001_report says 'ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata'\n# The numbers 2092/2089 are what the data shows\n\n# So paper's '~2,600 / ~2,600' appears WRONG compared to source data 2092/2089\n# Let's double-check by looking for any analysis with those bigger N values\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.csv', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '2600' in content or '2,600' in content:\n            print(f)\n    except:\n        pass\n\" | head -10\n",
    "description": "Search CSV files for 2600 counts"
  }
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-23T19:54:33.846071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md"
  }
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-23T19:54:33.846204+00:00_

1	# R15-SF7: Random Split Control — 2024 Cohort
2	
3	## Setup
4	
5	- **Cohort**: 2024 temporal cohort (N = 807 models)
6	- **Items**: 12508 MMLU items
7	- **Procedure**: 100 random 50/50 splits within the 2024 cohort
8	- **DIF method**: 5-stratum MH-DIF with Yates-corrected chi-squared
9	- **C% criterion**: |Δ_MH| ≥ 1.5 AND p < 0.05 (ETS Category C)
10	
11	## Results
12	
13	| Metric | Value |
14	|--------|-------|
15	| Mean C% | 1.335% |
16	| SD | 1.052% |
17	| 95% CI | [1.129%, 1.541%] |
18	| Min | 0.288% |
19	| Max | 7.675% |
20	| N reps | 100 |
21	
22	## Size-Matched Control
23	
24	To verify that the within-cohort C% is consistent with MH-DIF's null behavior at this
25	sample size, we ran 20 additional random splits from the **full** 5,227-model pool
26	using the same group sizes (403 vs 404):
27	
28	| Metric | Value |
29	|--------|-------|
30	| Mean C% (full-sample, size-matched) | 1.400% |
31	| SD | 0.779% |
32	
33	The within-cohort (1.335%) and full-sample (1.400%) baselines are
34	comparable, confirming that the ~1% level reflects the expected false-positive rate of
35	MH-DIF at this sample size (403 vs 404 per split), not cohort-specific structure.
36	
37	## Comparison
38	
39	| Split type | C% | N per group |
40	|------------|-----|-------------|
41	| **Temporal (pre-2024 vs 2024)** | **31.3%** | 1,080 vs 807 |
42	| Random within 2024 cohort | 1.335% | ~403 vs ~404 |
43	| Size-matched control (full sample) | 1.400% | 403 vs 404 |
44	| Random baseline (large groups) | 0.10% | 1,080 vs 807 |
45	
46	## Conclusion
47	
48	Random splitting within the 2024 cohort yields C% = 1.335% (95% CI:
49	[1.129%, 1.541%]). This is consistent with the size-matched full-sample
50	control (1.400%), confirming that MH-DIF does not produce spurious C-flagged
51	items when no genuine differential functioning exists. The temporal split C% of 31.3%
52	is 23× larger than the random-split baseline, ruling out
53	statistical artifact as an explanation.
54	
55	The ~1% baseline (versus ~0
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 303 · 2026-05-23T19:54:33.846354+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Check plan_001_real_data_dif_mmlu for ability cohort sizes\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/'\n# look for intermediate/data files\nfor root, dirs, files in os.walk(base):\n    for f in files:\n        print(os.path.join(root, f))\n\" | head -20\n",
  "description": "List all files in plan_001_real_data_dif_mmlu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Check plan_001_real_data_dif_mmlu for ability cohort sizes\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/'\n# look for intermediate/data files\nfor root, dirs, files in os.walk(base):\n    for f in files:\n        print(os.path.join(root, f))\n\" | head -20\n",
    "description": "List all files in plan_001_real_data_dif_mmlu"
  }
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-23T19:54:33.846490+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find the within-subject +0.186 FPR and cross-subject ΔFPR=0.000 for 5 subjects\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/",
  "description": "Check plan_016 within-subject directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find the within-subject +0.186 FPR and cross-subject ΔFPR=0.000 for 5 subjects\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/",
    "description": "Check plan_016 within-subject directory"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-23T19:54:33.846621+00:00_

data
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-23T19:54:33.846769+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check for sf8_power_sensitivity (§5.1 TPR 0.40-0.95)\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep sf8; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep power_sensitivity",
  "description": "Check sf8 power sensitivity directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check for sf8_power_sensitivity (§5.1 TPR 0.40-0.95)\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep sf8; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep power_sensitivity",
    "description": "Check sf8 power sensitivity directory"
  }
}
```

</details>

---


### Tool call

_source line 307 · 2026-05-23T19:54:33.846908+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Now look for the 2023 random split that gives 0.62\n# The paper says: \"random splits yield mean C% of 0.62% (2023; 100 permutations)\"\ngrep -r \"0\\.62\\|2023.*100.*perm\\|random.*split.*2023\\|within.*2023\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | grep -v \"0\\.621\\|0\\.623\\|0\\.628\\|0\\.624\" | head -20",
  "description": "Search for the 2023 random split 0.62% source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Now look for the 2023 random split that gives 0.62\n# The paper says: \"random splits yield mean C% of 0.62% (2023; 100 permutations)\"\ngrep -r \"0\\.62\\|2023.*100.*perm\\|random.*split.*2023\\|within.*2023\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | grep -v \"0\\.621\\|0\\.623\\|0\\.628\\|0\\.624\" | head -20",
    "description": "Search for the 2023 random split 0.62% source"
  }
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-23T19:54:33.847043+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/sf8_report.md:| b (diff) | 0.444 | 0.211 | 0.008 | 0.261 | 0.524 | 0.629 | 0.689 | -0.641 | -1.047 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_arch_report.md:The Llama comparison is the most informative: it is the best-powered (171 vs 315 models) and yields C% = 59.2% — nearly double the overall rate. This confirms that temporal measurement instability is **not** an artifact of comparing different architectures. Even within a single architecture lineage, item difficulty ordering shifts substantially between 2023 and 2024 model cohorts.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/score_inflation_report.md:| 2024 | 807 | 0.6068 | 0.6274 | +2.06 | 1.04 | [+1.99, +2.13] |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results.md:| 1 | LR_baseline_diff_only | 0.6209 | 0.4050 | 0.3879 | 0.4237 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_016_report.md:| business_ethics | 1.0 | 1.000±0.000 | 0.629±0.017 | +0.400 | inf | 0.0012 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_accumulation_report.md:**Bottom line:** The within-ref monotonicity supports a contamination-accumulation interpretation, though the evidence is limited by the small 2023-H1 cohort (n=62). The pattern is not consistent with a pure capability-evolution explanation, which would predict DIF driven by model architecture changes rather than monotonic temporal growth.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md:| mistral vs mixtral | 547 | 120 | 0.602 | 0.622 | 0.564 | -0.147 | No |
/
…[truncated 2853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-23T19:54:33.847175+00:00_

sf8_power_sensitivity
sf8_power_sensitivity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-23T19:54:33.847305+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check IRT params ā=1.2, b̄=-0.84 in irt_scale_analysis or PSN data\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/irt_scale_analysis.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d, indent=2))\" | head -50 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/irt_scale_analysis.md | head -50",
  "description": "Check IRT scale parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check IRT params ā=1.2, b̄=-0.84 in irt_scale_analysis or PSN data\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/irt_scale_analysis.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d, indent=2))\" | head -50 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/irt_scale_analysis.md | head -50",
    "description": "Check IRT scale parameters"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-23T19:54:33.847443+00:00_

{
  "parameterization_type": "classical_test_theory",
  "source_file": "mmlu-preproc.rds",
  "source_code": "analysis/preprocess.R (lines 52-77, 154-156)",
  "parameters": {
    "diff": {
      "definition": "guessing-corrected proportion correct",
      "formula": "diff = (n_correct / n_total) * (n_options - 1) / n_options",
      "formula_mmlu": "diff = 0.75 * p_correct",
      "scale": "probability [0, 0.75]",
      "mean": 0.444,
      "range": [
        0.008,
        0.689
      ],
      "is_irt_parameter": false,
      "irt_analog": "b (difficulty on logit/ability scale)"
    },
    "disc": {
      "definition": "point-biserial correlation (item response vs total score)",
      "formula": "rpbis = (m1 - m) / s * sqrt(n1 * n0 / (n * (n-1)))",
      "scale": "correlation [-1, 1]",
      "mean": 0.076,
      "range": [
        -0.551,
        0.291
      ],
      "is_irt_parameter": false,
      "irt_analog": "a (discrimination/slope, typically [0.2, 3.0])"
    },
    "sd": {
      "definition": "sample standard deviation of binary responses across LLMs",
      "formula": "sd(x_i) where x_i in {0, 1}",
      "scale": "[0, 0.5]",
      "is_irt_parameter": false
    }
  },
  "actual_irt_fitting": {
    "r_package": "mirt (Chalmers 2012)",
    "function": "mirt::mirt(data, 1, itemtype='2PL', method='EM')",
    "parameterization": "slope-intercept",
    "irt_formula": "P(theta) = 1 / (1 + exp(-(a1 * theta + d)))",
    "parameters_in_model": [
      "a1 (slope/discrimination)",
      "d (intercept)"
    ],
    "conversion_to_standard_irt": {
      "a_standard": "a1 (same)",
      "b_standard": "-d / a1"
    },

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-23T19:54:33.847581+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/",
  "description": "Check mvp_dif_power_sim directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/",
    "description": "Check mvp_dif_power_sim directory"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-23T19:54:33.847696+00:00_

chart
data

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-23T19:54:33.847911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search specifically for an artifact that does random splits of 2023 cohort (540 vs 540 or ~540)\nfind /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" | xargs grep -l \"540\\|2023.*random\\|random.*2023\" 2>/dev/null | head -10",
  "description": "Find artifact with 2023 cohort random split (540 vs 540)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search specifically for an artifact that does random splits of 2023 cohort (540 vs 540 or ~540)\nfind /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" | xargs grep -l \"540\\|2023.*random\\|random.*2023\" 2>/dev/null | head -10",
    "description": "Find artifact with 2023 cohort random split (540 vs 540)"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-23T19:54:33.848048+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_010_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_035_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/report/constat_dif_comparison_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/constat_dif_comparison_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-23T19:54:33.848224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-23T19:54:33.848373+00:00_

1	# Random-Split |Δ_MH| Null Distribution Report
2	
3	## Setup
4	- Cohort: 2023 models (N = 1080)
5	- Items: J = 12508
6	- Splits: 100 random permutations (each 540 ref vs 540 foc)
7	- Strata: 5 total-score quantile bins
8	- Total (item × split) observations: 1,250,800
9	- Runtime: 2.5s
10	
11	## Null Distribution Percentiles
12	
13	| Percentile | |Δ_MH| |
14	|------------|--------|
15	| 50th | 0.2956 |
16	| 90th | 0.7911 |
17	| 95th | 0.9898 |
18	| 97.5th | 1.1874 |
19	| 99th | 1.4504 |
20	| 99.5th | 1.6536 |
21	| 99.9th | 2.1998 |
22	
23	## ETS Threshold Comparison
24	
25	- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): 0.048206 (4.8206%)
26	- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): 0.008480 (0.8480%)
27	- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: 3717 / 12508 (29.72%)
28	
29	### ETS C Classification (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05)
30	
31	- Mean null C% per split: 0.6247%
32	- C% range across splits: [0.0640%, 5.8523%]
33	- Fraction of (item, split) classified C: 0.006247 (0.6247%)
34	- Items classified C in at least one split: 3702 / 12508 (29.60%)
35	
36	## Interpretation
37	
38	**P95 = 0.9898** (vs ETS B = 1.0): under random splitting, ~5% of item-level |Δ_MH| values approach B-level magnitude purely by chance.
39	
40	**P99 = 1.4504** (vs ETS C = 1.5): the null 99th percentile nearly reaches the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.
41	
42	**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the baseline false-positive rate for interpreting these observed rates.
43	
44	The 99th percentile (1.4504) and 99.9th percentile (2.1998) provide upper bounds on chance-level |Δ_MH| fluctuations.
45	
46	## Distribution Shape
47	
48	- Mean |Δ_MH| across all observations: 0.3740
49	- Median |Δ_MH|: 0.2956
50	- Std dev: 0.3205
51	- Skewness: 1.7897
…[truncated 225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-23T19:54:33.848571+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/ && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/*.md 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/*.csv | head -30",
  "description": "Check sf8_power_sensitivity contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/ && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/*.md 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/*.csv | head -30",
    "description": "Check sf8_power_sensitivity contents"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-23T19:54:33.848746+00:00_

param_descriptives.csv
sensitivity_results.csv
sf8_power_sensitivity.py
sf8_report.md
# SF8: Power Analysis — Parameter Descriptives & Sensitivity

## 1. IRT Parameter Descriptive Statistics

### PSN-IRT MMLU Items (N=14042)

| Param | Mean | SD | Min | Q1 | Median | Q3 | Max | Skew | Kurt |
|-------|------|----|-----|----|----|----|----|------|------|
| a (disc) | 1.197 | 0.542 | 0.006 | 0.751 | 1.162 | 1.637 | 2.657 | 0.100 | -0.956 |
| b (diff) | -0.838 | 0.790 | -2.683 | -1.425 | -0.895 | -0.315 | 1.692 | 0.288 | -0.433 |

### MetaBench Items (N=12508)

| Param | Mean | SD | Min | Q1 | Median | Q3 | Max | Skew | Kurt |
|-------|------|----|-----|----|----|----|----|------|------|
| a (disc) | 0.076 | 0.131 | -0.551 | 0.073 | 0.107 | 0.146 | 0.291 | -1.968 | 3.913 |
| b (diff) | 0.444 | 0.211 | 0.008 | 0.261 | 0.524 | 0.629 | 0.689 | -0.641 | -1.047 |

**Note**: PSN-IRT uses 4PL model (we take a, b as 2PL approximation); MetaBench uses a different IRT calibration. The PSN-IRT `discrimination` column maps to the 2PL `a` parameter directly.

## 2. TPR Sensitivity: TPR = f(a)

**Design**: Fixed b = -0.8383, N = 80/group, Δb = 1.4 logits (b-shift), 200 items (10% contaminated), 1000 replications. Observed MH Δ scales as 2.35·a·Δb.

| a | TPR | 95% CI | FPR |
|---|-----|--------|-----|
| 0.5 | 0.398 | [0.200, 0.600] | 0.0333 |
| 0.8 | 0.683 | [0.450, 0.900] | 0.0364 |
| 1.0 | 0.808 | [0.600, 0.950] | 0.0375 |
| 1.2 | 0.874 | [0.700, 1.000] | 0.0382 |
| 1.5 | 0.930 | [0.800, 1.000] | 0.0381 |
| 2.0 | 0.949 | [0.800, 1.000] | 0.0367 |

## 3. Interpretation

- **Monotonic TPR increase with a**: Higher discrimination items produce larger observed MH delta for a given latent DIF, making detection easier.
- **FPR control**: FPR remains well below 0.10 across all a values, confirming the ETS C classification is conservative.
- **Practical implication**: Items with a < 0.8 have substantially reduced power for detecting moderate DIF (|Δ_MH| = 1.4). The real MMLU pool (mean a ≈
…[truncated 249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-23T19:54:33.848921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/*.csv 2>/dev/null | head -30; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/",
  "description": "Check mvp_dif_power_sim data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/*.csv 2>/dev/null | head -30; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mvp_dif_power_sim/data/",
    "description": "Check mvp_dif_power_sim data"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-23T19:54:33.849053+00:00_

n_per_group,delta,method,tpr_raw,fpr_raw,tpr_bh,fpr_bh,tpr_bonf,fpr_bonf
30,0.4,MH,0.053,0.021,0.0,0.0,0.0,0.0
30,0.4,LR,0.126,0.0709,0.001,0.001,0.001,0.0008
30,0.6,MH,0.073,0.0199,0.001,0.0,0.001,0.0
30,0.6,LR,0.136,0.0719,0.008,0.0017,0.004,0.0011
30,0.8,MH,0.125,0.021,0.0,0.0,0.0,0.0
30,0.8,LR,0.206,0.0696,0.006,0.0009,0.005,0.0006
30,1.0,MH,0.2,0.0204,0.004,0.0,0.004,0.0
30,1.0,LR,0.278,0.0754,0.026,0.0013,0.019,0.0009
30,1.2,MH,0.26,0.0214,0.014,0.0,0.014,0.0
30,1.2,LR,0.346,0.0794,0.048,0.0017,0.037,0.0006
30,1.4,MH,0.344,0.0238,0.031,0.0001,0.023,0.0
30,1.4,LR,0.446,0.0727,0.103,0.0029,0.068,0.0006
30,1.6,MH,0.427,0.0204,0.054,0.0002,0.041,0.0001
30,1.6,LR,0.533,0.0716,0.147,0.0032,0.099,0.0009
50,0.4,MH,0.087,0.0272,0.0,0.0002,0.0,0.0
50,0.4,LR,0.124,0.0604,0.002,0.0008,0.002,0.0006
50,0.6,MH,0.146,0.0252,0.0,0.0,0.0,0.0
50,0.6,LR,0.193,0.0597,0.009,0.0006,0.007,0.0001
50,0.8,MH,0.235,0.0293,0.017,0.0006,0.015,0.0004
50,0.8,LR,0.287,0.0629,0.022,0.0011,0.019,0.0008
50,1.0,MH,0.36,0.0288,0.062,0.0002,0.042,0.0001
50,1.0,LR,0.394,0.0653,0.083,0.0012,0.055,0.0008
50,1.2,MH,0.443,0.0313,0.111,0.0003,0.063,0.0002
50,1.2,LR,0.466,0.0647,0.127,0.0019,0.082,0.0007
50,1.4,MH,0.544,0.0301,0.187,0.0002,0.116,0.0
50,1.4,LR,0.596,0.0632,0.245,0.0031,0.142,0.0003
50,1.6,MH,0.64,0.0311,0.29,0.0004,0.182,0.0
50,1.6,LR,0.677,0.0628,0.335,0.0041,0.22,0.0003
80,0.4,MH,0.131,0.0307,0.004,0.0,0.004,0.0
dif_diagnostic_tpr_comparison.csv
dif_power_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-23T19:54:33.849194+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check plan_016 for within-subject FPR data\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/",
  "description": "List plan_016 report directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check plan_016 for within-subject FPR data\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/",
    "description": "List plan_016 report directory"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-23T19:54:33.849315+00:00_

plan_016_report.md
plan_016_report_fb64fc.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-23T19:54:33.849444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Also check plan_011_semi_synthetic_validation for ΔFPR=0.000 across 5 subjects\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/",
  "description": "List plan_011_semi_synthetic_validation report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Also check plan_011_semi_synthetic_validation for ΔFPR=0.000 across 5 subjects\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/",
    "description": "List plan_011_semi_synthetic_validation report"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-23T19:54:33.849564+00:00_

plan_011_report.md
plan_011_report_c7ae89.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-23T19:54:33.849690+00:00_

artifacts/review_issues.yaml:14:        note: "R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。"
artifacts/mf2_deff_estimation/deff_summary.md:84:- Adjusted C% (weighted: 13.5%, simple: 29.2%) ≤ Original (31.3%) ✓
artifacts/_project/report/response_letter_draft.md:36:[Omitted long matching line]
artifacts/_project/report/arr_checklist_draft.md:64:**Justification**: Results include bootstrap 95% CIs (e.g., C% CI [29.4%, 38.1%]), family-level cluster bootstrap CIs ([26.7%, 53.2%]), DEFF correction ranges (13.5%–29.2%), standard deviations for semi-synthetic results, permutation p-values, and effect sizes (Cohen's d, φ, Jaccard, OR with CIs). Multiple convergent estimates are reported rather than cherry-picked single values.
artifacts/response_letter_draft.md:36:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_worst.log:157:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/paper_agent_worst.log:42:[Omitted long matching line]
artifacts/r20_size_stratified_deff/size_stratified_deff_report.md:26:- At m̄_simple = 63 (treating all families equally): DEFF = 3.87, C% = 29.2%
artifacts/r20_size_stratified_deff/size_stratified_deff_report.md:28:- The range [13.5%, 29.2%] brackets the plausible DEFF-adjusted C%.
artifacts/r20_size_stratified_deff/size_stratified_deff_report.md:86:| C% (simple) | 29.2% | 29.4% |
artifacts/review_reports/round_9.md:23:[Omitted long matching line]
artifacts/review_reports/round_9.md:59:**要求修改**：(1) 以方法论论据（如 few-PSU DEFF instability，cluster 数 ~30 时 ICC 估计不稳定性）论证 weighted-mean DEFF 的问题，而非选择性排除；(2) 将完整范围 [13.5%, 29.2%] 作为 corrected estimate range 透明呈现在 Abstract 和正文中；(3) 强调即便按最保守的 13.5%，temporal DIF 仍是 random baseline 的 75 倍，核心定性结论不受影响。
artifacts/review_reports/round_9.md:218:**Rebuttal 路径**: 如果作者在 rebuttal 中 (a) 提供 DEFF-adjusted item-level C%，(b) 将 [13.5%, 29.2%] 作为 corrected range 透明呈现，(c) 报告 uniform + non-uniform DIF 的总比率——两位 Reviewer 均表示可将评分提高到 4.0 (Conference)。
arti
…[truncated 2134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 4
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-23T19:54:33.849877+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Perfect! The source for MMLU Rand C% = 0.62 is:\n# _project/data/random_split_report.md: \"Mean null C% per split: 0.6247%\"\n# This is the 2023 cohort (N=1080), 100 random 540/540 splits\n# Paper shows 0.62 which rounds from 0.6247 ✅\n\n# Now let me verify the Ratio column computations again carefully\n# The Rand C% column in Table 3 is 0.62 for MMLU (from this 2023 random split analysis)\n# But for other benchmarks, where do the Rand C% values come from?\n# Let me check if there's a similar analysis for each benchmark\n\ngrep -r \"mean.*c%\\|null.*c%\\|random.*c%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ --include=\"*.md\" -i | head -20",
  "description": "Check where random C% for non-MMLU benchmarks come from"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Perfect! The source for MMLU Rand C% = 0.62 is:\n# _project/data/random_split_report.md: \"Mean null C% per split: 0.6247%\"\n# This is the 2023 cohort (N=1080), 100 random 540/540 splits\n# Paper shows 0.62 which rounds from 0.6247 ✅\n\n# Now let me verify the Ratio column computations again carefully\n# The Rand C% column in Table 3 is 0.62 for MMLU (from this 2023 random split analysis)\n# But for other benchmarks, where do the Rand C% values come from?\n# Let me check if there's a similar analysis for each benchmark\n\ngrep -r \"mean.*c%\\|null.*c%\\|random.*c%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ --include=\"*.md\" -i | head -20",
    "description": "Check where random C% for non-MMLU benchmarks come from"
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-23T19:54:33.850010+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md:The temporal DIF signal (C% >> random C%) indicates systematic item-level 
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/mmlu_bootstrap_report.md:| Control mean C% | 0.10% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md:| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md:The temporal DIF signal (C% >> random C%) indicates systematic item-level

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-23T19:54:33.850143+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md | head -100",
  "description": "Read plan_016 within-subject report for +0.186 FPR inflation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md | head -100",
    "description": "Read plan_016 within-subject report for +0.186 FPR inflation"
  }
}
```

</details>

---


### Tool result

_source line 330 · 2026-05-23T19:54:33.850279+00:00_

# Plan 016: Within-Subject Semi-Synthetic Injection

## Objective

Verify that MH-DIF detects differential contamination **within individual subjects**,
not just globally. This validates plan_014's finding that within-subject temporal
C% = 38.1% reflects real signal, not method failure.

## Setup

- **Temporal cohort**: ref=2023 (1080 models), foc=2024 (807 models)
- **Focal injection subset**: 787 models (ability overlap with ref)
- **Contamination fraction**: 20% of items per subject
- **Injection probabilities**: [0.0, 0.5, 1.0]
- **Seeds per p**: 5
- **Matching**: within-subject purified total score (plan_014 method)

### Subjects

| Subject | N items | N contaminated | N baseline | Strata |
|---------|---------|----------------|------------|--------|
| business_ethics | 93 | 18 | 75 | 3 |
| human_aging | 203 | 40 | 163 | 5 |
| professional_medicine | 248 | 49 | 199 | 5 |

## Results

### Per-Subject Dose-Response

| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
|---------|---|----------------|----------------|------|-----------|----------|
| business_ethics | 0.0 | 0.600±0.072 | 0.563±0.017 | +0.000 | 1.24 | 0.5990 |
| business_ethics | 0.5 | 0.522±0.084 | 0.603±0.017 | -0.078 | 0.78 | 0.5957 |
| business_ethics | 1.0 | 1.000±0.000 | 0.629±0.017 | +0.400 | inf | 0.0012 |
| human_aging | 0.0 | 0.315±0.045 | 0.334±0.011 | +0.000 | 0.94 | 0.5741 |
| human_aging | 0.5 | 0.700±0.085 | 0.405±0.019 | +0.385 | 3.68 | 0.0013 |
| human_aging | 1.0 | 1.000±0.000 | 0.507±0.033 | +0.685 | inf | 0.0000 |
| professional_medicine | 0.0 | 0.306±0.050 | 0.312±0.012 | +0.000 | 1.00 | 0.6056 |
| professional_medicine | 0.5 | 0.633±0.063 | 0.435±0.042 | +0.327 | 2.37 | 0.0063 |
| professional_medicine | 1.0 | 1.000±0.000 | 0.593±0.028 | +0.694 | inf | 0.0000 |

### Subject-Level Summary

| Subject | Baseline FPR (p=0) | TPR at p=0.5 | TPR at p=1.0 | ΔTPR(0.5) | ΔTPR(1.0) | Significant? |
|---------|---------------------|--------------|--------------|
…[truncated 2110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-23T19:54:33.850445+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md | head -100",
  "description": "Read plan_011_semi_synthetic_validation report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md | head -100",
    "description": "Read plan_011_semi_synthetic_validation report"
  }
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-23T19:54:33.850577+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Let me look at what the plan_028 script's random_pct_c column represents\ngrep -A 5 -B 5 \"random_pct_c\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py | head -60",
  "description": "Check how random_pct_c is computed in plan_028 script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Let me look at what the plan_028 script's random_pct_c column represents\ngrep -A 5 -B 5 \"random_pct_c\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py | head -60",
    "description": "Check how random_pct_c is computed in plan_028 script"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-23T19:54:33.850728+00:00_

                benchmark=bench, n_items=int(std_row.n_items),
                n_ref=int(std_row.n_ref), n_foc=int(std_row.n_foc),
                n_ets_a=int(std_row.n_ets_a), n_ets_b=int(std_row.n_ets_b),
                n_ets_c=int(std_row.n_ets_c),
                pct_c=round(std_row.pct_c, 1),
                random_pct_c=round(rand_row.pct_c, 2),
                status="OK"
            ))
            continue

        X, model_names, item_ids = load_response_matrix(bench)
--
            print(f"  SKIP: insufficient models per cohort (<50)")
            all_results.append(dict(
                benchmark=bench, n_items=len(item_ids),
                n_ref=n_ref, n_foc=n_foc,
                n_ets_a=0, n_ets_b=0, n_ets_c=0, pct_c=0,
                random_pct_c=0, status="SKIPPED"
            ))
            continue

        # ── Temporal DIF ──
        print(f"\n  Running temporal MH-DIF (5 strata)...")
--
        all_results.append(dict(
            benchmark=bench, n_items=len(item_ids),
            n_ref=n_ref, n_foc=n_foc,
            n_ets_a=n_a, n_ets_b=n_b, n_ets_c=n_c,
            pct_c=round(pct_c, 1),
            random_pct_c=round(pct_c_rand, 2),
            status="OK"
        ))

        del X, dif, dif_rand
        gc.collect()
--
    # ── Add prior MMLU and GSM8K results ──
    all_results.append(dict(
        benchmark="mmlu", n_items=12508,
        n_ref=1080, n_foc=807,
        n_ets_a=0, n_ets_b=0, n_ets_c=0, pct_c=31.3,
        random_pct_c=0.3, status="PRIOR"
    ))

    # Load actual MMLU numbers from plan_001 if available
    mmlu_summary = BASE / "plan_001" / "dif_summary.csv"
    if mmlu_summary.exists():
--
        text = mmlu_report.read_text()
        import re
        m = re.search(r"Random half-split.*?\*\*(\d+\.\d+)%", text)
        if m:
            mmlu_san_pct = float(m.group(1))
    all_results[-1]["random_pct_c"] = mmlu_san_pct

    # GSM8K from existing results
    gsm8k_ets = BASE / "_project" / "data" / "gsm8k_ets_summary.c
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-23T19:54:33.850899+00:00_

# Plan 011: Semi-Synthetic DIF Validation

## 1. Objective

Inject known **differential** contamination into real MMLU response data and test
whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find
enrichment was due to Li et al. labels being non-differential (global contamination)
rather than a fundamental limitation of MH-DIF.

## 2. Setup

- **Baseline items**: 500 (clean in Li et al. + ETS A in plan_001 ability DIF)
- **Contaminated per run**: 100 of 500
- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
- **Seeds per p**: 5

### Cohort definitions

- **ability**: ref N=2092, foc N=2089, foc inject N=2089
- **temporal**: ref N=1080, foc N=807, foc inject N=787

> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction (ref max=0.6319, foc min=0.6772). All focal models used for injection. MH stratification handles ability matching.

### MH variants

| Variant | Matching variable | Rationale |
|---------|-------------------|-----------|
| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |
| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |
| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |

## 3. Results by MH Variant

### Standard MH

| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
|--------|---|----------------|----------------|------|-----------|----------|
| ability | 0.0 | 0.594±0.053 | 0.611±0.013 | +0.000 | 0.96 | 0.4231 |
| ability | 0.3 | 0.700±0.057 | 0.609±0.026 | +0.106 | 1.58 | 0.2555 |
| ability | 0.5 | 0.760±0.046 | 0.600±0.021 | +0.166 | 2.21 | 0.0067 |
| ability | 0.7 | 0.806±0.036 | 0.598±0.030 | +0.212 | 2.90 | 0.0002 |
| ability | 1.0 | 0.816±0.035 | 0.596±0.023 | +0.222 | 3.17 | 0.0001 |
| temporal | 0.
…[truncated 2917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 335 · 2026-05-23T19:54:33.851062+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Jaccard.*0\\.206|0\\.206.*Jaccard|Expected Jaccard|jaccard.*independence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Jaccard.*0\\.206|0\\.206.*Jaccard|Expected Jaccard|jaccard.*independence",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-23T19:54:33.851199+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/ && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/*.md 2>/dev/null | head -80",
  "description": "List and read r17_jaccard_permutation files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/ && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/*.md 2>/dev/null | head -80",
    "description": "List and read r17_jaccard_permutation files"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-23T19:54:33.851326+00:00_

jaccard_permutation_report.md
jaccard_permutation_results.csv
# Jaccard Permutation Null Test: DIF-C vs Li et al. Contamination Labels

## Data

- Total items with li_label: **9229**
- DIF-C items (among labeled): **2897** (31.4%)
- Li-contaminated items: **3645** (39.5%)
- |DIF-C ∩ li_contaminated|: **1119**
- |DIF-C ∪ li_contaminated|: **5423**

## Results

| Metric | Value |
|--------|-------|
| Observed Jaccard | 0.2063 |
| Null mean | 0.2120 |
| Null SD | 0.0049 |
| Null 95% CI | [0.2026, 0.2217] |
| p-value | 0.8825 |
| Observed / Null ratio | 0.97x |

## Conclusion

The observed Jaccard (0.206) is **not** significantly above the permutation null (mean = 0.212, p = 0.88, one-sided). The observed value falls squarely within the null 95% CI [0.203, 0.222] and is in fact slightly *below* the null mean.

The overlap between DIF-C and Li contamination labels is entirely consistent with what marginal rates alone would predict. DIF and memorization-based contamination detection identify **independent, non-overlapping signals** — their item-level agreement is no better than chance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-23T19:54:33.851477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Look for cross-subject ΔFPR=0.000 across 5 subjects in plan_011_semi_synthetic_validation\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md",
  "description": "Read plan_011_semi_synthetic_validation report (full)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Look for cross-subject ΔFPR=0.000 across 5 subjects in plan_011_semi_synthetic_validation\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md",
    "description": "Read plan_011_semi_synthetic_validation report (full)"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-23T19:54:33.851625+00:00_

# Plan 011: Semi-Synthetic DIF Validation

## 1. Objective

Inject known **differential** contamination into real MMLU response data and test
whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find
enrichment was due to Li et al. labels being non-differential (global contamination)
rather than a fundamental limitation of MH-DIF.

## 2. Setup

- **Baseline items**: 500 (clean in Li et al. + ETS A in plan_001 ability DIF)
- **Contaminated per run**: 100 of 500
- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
- **Seeds per p**: 5

### Cohort definitions

- **ability**: ref N=2092, foc N=2089, foc inject N=2089
- **temporal**: ref N=1080, foc N=807, foc inject N=787

> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction (ref max=0.6319, foc min=0.6772). All focal models used for injection. MH stratification handles ability matching.

### MH variants

| Variant | Matching variable | Rationale |
|---------|-------------------|-----------|
| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |
| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |
| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |

## 3. Results by MH Variant

### Standard MH

| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
|--------|---|----------------|----------------|------|-----------|----------|
| ability | 0.0 | 0.594±0.053 | 0.611±0.013 | +0.000 | 0.96 | 0.4231 |
| ability | 0.3 | 0.700±0.057 | 0.609±0.026 | +0.106 | 1.58 | 0.2555 |
| ability | 0.5 | 0.760±0.046 | 0.600±0.021 | +0.166 | 2.21 | 0.0067 |
| ability | 0.7 | 0.806±0.036 | 0.598±0.030 | +0.212 | 2.90 | 0.0002 |
| ability | 1.0 | 0.816±0.035 | 0.596±0.023 | +0.222 | 3.17 | 0.0001 |
| temporal | 0.
…[truncated 4892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-23T19:54:33.851803+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Look for the structural analysis: 17.7% non-uniform DIF and union 47%\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep structural",
  "description": "Find structural analysis artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Look for the structural analysis: 17.7% non-uniform DIF and union 47%\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep structural",
    "description": "Find structural analysis artifacts"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-23T19:54:33.851936+00:00_

cross_analysis.csv
dif_results_ability.csv
dif_results_temporal.csv
dif_summary.csv
domain_specificity.csv
neg_disc_sensitivity.csv
plan_001_analysis.py
plan_001_report.md
within_family_dif.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-23T19:54:33.852065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check plan_001 cross_analysis.csv for structural 17.7%, union 47%\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/cross_analysis.csv",
  "description": "Read cross_analysis.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check plan_001 cross_analysis.csv for structural 17.7%, union 47%\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/cross_analysis.csv",
    "description": "Read cross_analysis.csv"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-23T19:54:33.852252+00:00_

&lt;persisted-output>
Output too large (2.7MB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/45ef05ff-ecb8-4f6a-b1ca-47b9fb08b347/tool-results/bmhpt18i8.txt

Preview (first 2KB):
item_id,subject,temporal_ets,temporal_delta,wf_pair,wf_ets,wf_delta,li_contamination_type
abstract_algebra.1,abstract_algebra,A,0.3343505559632721,llama-2_vs_llama-3,B,1.073271254578906,clean
abstract_algebra.10,abstract_algebra,C,1.5634303993406418,llama-2_vs_llama-3,B,-2.480888532806384,clean
abstract_algebra.100,abstract_algebra,C,1.8473056183645777,llama-2_vs_llama-3,A,-0.6348485358718126,no_annotation
abstract_algebra.11,abstract_algebra,A,0.780138707124792,llama-2_vs_llama-3,C,-4.68431819548781,clean
abstract_algebra.12,abstract_algebra,A,-0.937105162649532,llama-2_vs_llama-3,C,-2.202659614159003,clean
abstract_algebra.13,abstract_algebra,B,-1.1943753123055647,llama-2_vs_llama-3,B,1.207296968454848,clean
abstract_algebra.14,abstract_algebra,C,1.7717583941763377,llama-2_vs_llama-3,B,1.5001667498540638,clean
abstract_algebra.15,abstract_algebra,A,-0.5692170675088077,llama-2_vs_llama-3,B,4.193543768262592,clean
abstract_algebra.16,abstract_algebra,A,0.46916972666288403,llama-2_vs_llama-3,B,-1.5609773026056029,clean
abstract_algebra.17,abstract_algebra,A,-0.16583365498585692,llama-2_vs_llama-3,C,-2.6588215499467376,clean
abstract_algebra.18,abstract_algebra,B,1.36760446045332,llama-2_vs_llama-3,C,1.8647197718197137,input_and_label
abstract_algebra.2,abstract_algebra,C,-1.5754889426003047,llama-2_vs_llama-3,C,4.11136327694941,input_only
abstract_algebra.20,abstract_algebra,C,1.5496704893224662,llama-2_vs_llama-3,B,1.3721028401162807,clean
abstract_algebra.21,abstract_algebra,B,-1.1971262457757967,llama-2_vs_llama-3,A,-0.5398569302903937,clean
abstract_algebra.22,abstract_algebra,B,1.4526056989518408,llama-2_vs_llama-3,A,0.004579448979771879,clean
abstract_algebra.23,abstract_algebra,A,-0.81217335
…[truncated 195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-23T19:54:33.852401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search for non-uniform DIF 17.7% and union 47% across plan dirs\ngrep -rn \"17.7\\|non.uniform\\|union\\|47%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | head -20",
  "description": "Search for non-uniform DIF stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search for non-uniform DIF 17.7% and union 47% across plan dirs\ngrep -rn \"17.7\\|non.uniform\\|union\\|47%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | head -20",
    "description": "Search for non-uniform DIF stats"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-23T19:54:33.852532+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:26:high_school_macroeconomics,358,101,28.212290502793298,0.5848722325677633,0.6084712674710806,0.023599034903317273
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py:485:    union   = temp_c | abil_c
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py:486:    jaccard = len(overlap) / len(union) if union else 0
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:11:abstract_algebra.17,abstract_algebra,llama-2,llama-3,3.1000350736546753,-2.6588215499467376,0.9037367340677508,0.00074065175778526,C,False,clean
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:88:abstract_algebra.94,abstract_algebra,llama-2,llama-3,1.1308727823838813,-0.2890258147121727,1.4514763181012673,1.0,A,False,clean
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:117:anatomy.120,anatomy,llama-2,llama-3,0.12304912273617478,4.923653334021726,0.7962729626584222,3.795075365076173e-12,C,False,clean
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:137:anatomy.20,anatomy,llama-2,llama-3,5.235117073917257,-3.890164638241774,1.0732952761999974,5.716822013379641e-05,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:163:anatomy.45,anatomy,llama-2,llama-3,13.973494117475735,-6.197331305776463,0.8809579446616386,1.1102230246251565e-16,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.cs
…[truncated 3072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-23T19:54:33.852692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The MMLU random_pct_c was originally set to 0.3 but then overwritten from plan_001 report\n# plan_001 reports: \"Random half-split of 2023 cohort: 0.18% C\"\n# So plan_028 multi_bench_summary.csv shows 0.18 for MMLU\n# But the paper table uses 0.62, which comes from _project/data/random_split_report.md (100 random splits of 2023 cohort: mean 0.6247%)\n# These are different baselines:\n# 0.18 = single random split (plan_001 sanity check, one run)\n# 0.62 = mean of 100 random splits (more robust estimate)\n\n# Both are from 2023 cohort random split, but one is a single run and one is mean of 100\n\n# Now the paper TABLE 3 shows 0.62 for MMLU Rand C% — which is the 100-run mean\n# The plan_028 CSV shows 0.18 (single split from plan_001)\n# So the paper uses the more robust 100-run mean from random_split_report.md\n\n# Let me verify the ratios in the paper\npython3 -c \"\n# Paper table uses:\nmmlu = (31.3, 0.62, '50x')  \n# 31.3/0.62 = 50.48 → rounds to 50x ✅\n\n# Other benchmarks use plan_028 values:\nwino = (30.3, 0.32, '95x')  # 94.7 → 95x ✅\ntqa =  (29.7, 0.37, '80x')  # 80.3 → 80x ✅\narc =  (26.9, 0.60, '45x')  # 44.8 → 45x ✅\ngsm8k= (18.9, 0.30, '63x')  # 63.0 → 63x ✅\nhella= (17.9, 0.28, '64x')  # 63.9 → 64x ✅\n\nfor name, (c, r, p) in [('MMLU',mmlu),('WinoGrande',wino),('TruthfulQA',tqa),('ARC',arc),('GSM8K',gsm8k),('HellaSwag',hella)]:\n    ratio = c/r\n    print(f'{name}: {c}/{r} = {ratio:.1f}x (paper: {p})')\n\"\n",
  "description": "Verify ratio calculations with correct Rand C% values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The MMLU random_pct_c was originally set to 0.3 but then overwritten from plan_001 report\n# plan_001 reports: \"Random half-split of 2023 cohort: 0.18% C\"\n# So plan_028 multi_bench_summary.csv shows 0.18 for MMLU\n# But the paper table uses 0.62, which comes from _project/data/random_split_report.md (100 random splits of 2023 cohort: mean 0.6247%)\n# These are different baselines:\n# 0.18 = single random split (plan_001 sanity check, one run)\n# 0.62 = mean of 100 random splits (more robust estimate)\n\n# Both are from 2023 cohort random split, but one is a single run and one is mean of 100\n\n# Now the paper TABLE 3 shows 0.62 for MMLU Rand C% — which is the 100-run mean\n# The plan_028 CSV shows 0.18 (single split from plan_001)\n# So the paper uses the more robust 100-run mean from random_split_report.md\n\n# Let me verify the ratios in the paper\npython3 -c \"\n# Paper table uses:\nmmlu = (31.3, 0.62, '50x')  \n# 31.3/0.62 = 50.48 → rounds to 50x ✅\n\n# Other benchmarks use plan_028 values:\nwino = (30.3, 0.32, '95x')  # 94.7 → 95x ✅\ntqa =  (29.7, 0.37, '80x')  # 80.3 → 80x ✅\narc =  (26.9, 0.60, '45x')  # 44.8 → 45x ✅\ngsm8k= (18.9, 0.30, '63x')  # 63.0 → 63x ✅\nhella= (17.9, 0.28, '64x')  # 63.9 → 64x ✅\n\nfor name, (c, r, p) in [('MMLU',mmlu),('WinoGrande',wino),('TruthfulQA',tqa),('ARC',arc),('GSM8K',gsm8k),('HellaSwag',hella)]:\n    ratio = c/r\n    print(f'{name}: {c}/{r} = {ratio:.1f}x (paper: {p})')\n\"\n",
    "description": "Verify ratio calculations with correct Rand C% values"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-23T19:54:33.852858+00:00_

MMLU: 31.3/0.62 = 50.5x (paper: 50x)
WinoGrande: 30.3/0.32 = 94.7x (paper: 95x)
TruthfulQA: 29.7/0.37 = 80.3x (paper: 80x)
ARC: 26.9/0.6 = 44.8x (paper: 45x)
GSM8K: 18.9/0.3 = 63.0x (paper: 63x)
HellaSwag: 17.9/0.28 = 63.9x (paper: 64x)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-23T19:54:33.853001+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find 17.7% non-uniform DIF and union 47% — check all plan dirs for LR results\ngrep -rn \"17.7\\|non.uniform\\|union.*47\\|0.177\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | grep -v \".pyc\" | head -30",
  "description": "Search artifacts for 17.7% non-uniform DIF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find 17.7% non-uniform DIF and union 47% — check all plan dirs for LR results\ngrep -rn \"17.7\\|non.uniform\\|union.*47\\|0.177\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | grep -v \".pyc\" | head -30",
    "description": "Search artifacts for 17.7% non-uniform DIF"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-23T19:54:33.853153+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:14:3,80,1.0,0.1757,0.0006,0.8284,0.0034,0.0001,0.5312,0.0325,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:37:5,60,0.6,0.0061,0.0001,0.6572,0.0006,0.0,0.1767,0.0275,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:15:abstract_algebra.6,abstract_algebra,1.792888292383569,1.094906720844335e-09,0.0070384521334465,0.1491757486392206,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:20:anatomy.104,anatomy,2.0195754863742708,3.176799734383451e-07,0.0017939296221108,0.0690888533220329,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:30:anatomy.37,anatomy,-1.8950062010180395,7.07940434161447e-05,0.0185928544077454,0.1778537143410276,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:33:anatomy.48,anatomy,-1.865386035821317,7.730399607719374e-05,0.0103698856848337,0.1300611832942952,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:65:business_ethics.27,business_ethics,2.00685017173974,9.992007221626409e-16,0.0008246293267716,0.0758791392612154,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:77:business_ethics.6,business_ethics,1.7275503524271345,8.27429798522239e-06,0.0
…[truncated 6534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-23T19:54:33.853297+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check for STEM 55.4% / Humanities 64.4% and KW p=0.78\ngrep -rn \"55.4\\|64.4\\|0.78\\|Kruskal\\|STEM\\|Humanities\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
  "description": "Search for STEM/Humanities DIF direction stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check for STEM 55.4% / Humanities 64.4% and KW p=0.78\ngrep -rn \"55.4\\|64.4\\|0.78\\|Kruskal\\|STEM\\|Humanities\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
    "description": "Search for STEM/Humanities DIF direction stats"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-23T19:54:33.853428+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:6:3,40,1.4,0.1098,0.0002,0.7815,0.0031,0.0,0.4542,0.0246,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:9:3,60,1.0,0.0748,0.0003,0.7868,0.0025,0.0,0.4249,0.0289,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:20:3,100,1.2,0.4445,0.0018,0.8883,0.0035,0.0001,0.7097,0.0378,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:28:3,500,0.8,0.8257,0.0077,0.9802,0.0023,0.0003,0.6464,0.0026,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:38:5,60,0.8,0.0231,0.0002,0.7284,0.0013,0.0,0.2944,0.0278,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:39:5,60,1.0,0.0716,0.0003,0.7837,0.0024,0.0,0.4201,0.0292,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:43:|       60 | 0.075   | 0.072   | 0.000   | 0.000   | 0.787   | 0.784   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:64:|       40 | 0.110   | 0.091   | 0.000   | 0.000   | 0.781   | 0.769   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:11:abstract_algebra.47,abstract_algebra,1.9931584017328616,8.333785715963771e-07,0.0204775348851451,0.2087873210746174,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_rec
…[truncated 2858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-23T19:54:33.853584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# All ratios match via rounding. Now let me also check GSM8K random_pct_c=0.30 vs 0.3 source\n# and double check the plan_028 summary shows 0.3 for GSM8K\n\n# For GSM8K: source shows 0.3, paper shows 0.30 ✅\n# Now let me verify the Items column for each benchmark\n\npython3 -c \"\n# Source values from plan_028 multi_bench_summary.csv\nitems = {\n    'MMLU': 12508, 'WinoGrande': 1267, 'TruthfulQA': 817,\n    'ARC': 1172, 'GSM8K': 1319, 'HellaSwag': 10042\n}\npaper = {\n    'MMLU': '12,508', 'WinoGrande': '1,267', 'TruthfulQA': '817',\n    'ARC': '1,172', 'GSM8K': '1,319', 'HellaSwag': '10,042'\n}\nfor k, v in items.items():\n    formatted = format(v, ',')\n    match = '✅' if formatted == paper[k] else '❌'\n    print(f'{k}: source={v}, paper={paper[k]} {match}')\n\"",
  "description": "Verify Items column values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# All ratios match via rounding. Now let me also check GSM8K random_pct_c=0.30 vs 0.3 source\n# and double check the plan_028 summary shows 0.3 for GSM8K\n\n# For GSM8K: source shows 0.3, paper shows 0.30 ✅\n# Now let me verify the Items column for each benchmark\n\npython3 -c \"\n# Source values from plan_028 multi_bench_summary.csv\nitems = {\n    'MMLU': 12508, 'WinoGrande': 1267, 'TruthfulQA': 817,\n    'ARC': 1172, 'GSM8K': 1319, 'HellaSwag': 10042\n}\npaper = {\n    'MMLU': '12,508', 'WinoGrande': '1,267', 'TruthfulQA': '817',\n    'ARC': '1,172', 'GSM8K': '1,319', 'HellaSwag': '10,042'\n}\nfor k, v in items.items():\n    formatted = format(v, ',')\n    match = '✅' if formatted == paper[k] else '❌'\n    print(f'{k}: source={v}, paper={paper[k]} {match}')\n\"",
    "description": "Verify Items column values"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-23T19:54:33.853734+00:00_

MMLU: source=12508, paper=12,508 ✅
WinoGrande: source=1267, paper=1,267 ✅
TruthfulQA: source=817, paper=817 ✅
ARC: source=1172, paper=1,172 ✅
GSM8K: source=1319, paper=1,319 ✅
HellaSwag: source=10042, paper=10,042 ✅

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-23T19:54:33.853881+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check 18.3% at |Δ_MH|≥2.0 and 10.2% at ≥2.5\ngrep -rn \"18.3\\|10.2\\|2\\.0\\|2\\.5\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | grep -v \".py:\" | head -20",
  "description": "Search for threshold analysis (18.3%, 10.2%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check 18.3% at |Δ_MH|≥2.0 and 10.2% at ≥2.5\ngrep -rn \"18.3\\|10.2\\|2\\.0\\|2\\.5\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | grep -v \".py:\" | head -20",
    "description": "Search for threshold analysis (18.3%, 10.2%)"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-23T19:54:33.854022+00:00_

artifacts/rebuttal_talking_points.md:21:| Jaccard=0.206 | Orthogonal constructs (core contribution) | 5/5 |
artifacts/plan_026/constat_dif_comparison_report.md:24:| Jaccard index | 0.2063 | Low overlap between flagged sets |
artifacts/plan_026/constat_dif_comparison_report.md:69:2. **Jaccard = 0.2063**: The two flagged sets (DIF-C and web-contaminated) have very low overlap, confirming they identify different item populations.
artifacts/plan_026/report/constat_dif_comparison_report.md:24:| Jaccard index | 0.2063 | Low overlap between flagged sets |
artifacts/plan_026/report/constat_dif_comparison_report.md:69:2. **Jaccard = 0.2063**: The two flagged sets (DIF-C and web-contaminated) have very low overlap, confirming they identify different item populations.
artifacts/novelty_rebuttal_draft.md:7:[Omitted long matching line]
artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md:39:| Expected Jaccard (independence) | 0.206 |
artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py:249:    print(f"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})")
artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py:348:| Expected Jaccard (independence) | {expected_jaccard:.3f} |
artifacts/r17_jaccard_permutation/jaccard_permutation_report.md:15:| Observed Jaccard | 0.2063 |
artifacts/r17_jaccard_permutation/jaccard_permutation_report.md:24:The observed Jaccard (0.206) is **not** significantly above the permutation null (mean = 0.212, p = 0.88, one-sided). The observed value falls squarely within the null 95% CI [0.203, 0.222] and is in fact slightly *below* the null mean.
artifacts/data_audit_part1.md:10:- **Jaccard = 0.206** ← `r17_jaccard_permutation/jaccard_permutation_report.md` line 15: Observed Jaccard = 0.2063 ✅
artifacts/data_audit_part1.md:28:- **Jaccard = 0.206** ← 同 Abstract ✅
artifacts/data_audit_part1.md:38:- **Jaccard = 0.206** ← 同 Abstract ✅
artifacts/data_audit_part1.md:57:| Jaccard = 0.206 | ✓ | ✓ | ✓ | — | 一致 |
artifacts/_pro
…[truncated 2772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 2
}
```

</details>

---


### Tool result

_source line 356 · 2026-05-23T19:54:33.854176+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:5:business_ethics,93,45,48.38709677419355,0.5581541218637993,0.6124901733487895,0.05433605148499021
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:15:econometrics,103,36,34.95145631067961,0.4246853649766271,0.481803635663671,0.05711827068704389
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:39:machine_learning,87,28,32.18390804597701,0.44401873137505316,0.47810109814980983,0.03408236677475668
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:45:moral_scenarios,692,243,35.115606936416185,0.3575251552130165,0.4104296939352916,0.05290453872227513
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:58:world_religions,159,59,37.10691823899371,0.7431283484742605,0.734469617264034,-0.008658731210226422
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:6:abstract_algebra.12,abstract_algebra,llama-2,llama-3,2.5530838041431263,-2.202659614159003,1.035358827538494,0.023516507472339132,C,False,clean
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:14:abstract_algebra.20,abstract_algebra,llama-2,llama-3,0.5577337678616195,1.3721028401162807,0.6569490407595624,0.051072691639969525,B,False,clean
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:19:abstract_algebra.25,abstract_algebra,llama-2,llama-3,0.3376979757770814,2.5511678625219716,0.7278410195599315,0.00044743059039087374,C,True,input_only
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_e
…[truncated 3193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 357 · 2026-05-23T19:54:33.854326+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check random split 2024 = 1.3% — plan_001_report says 0.18% only for 2023\n# Look for 2024 random split data elsewhere\ngrep -rn \"1.3\\|random.*2024\\|2024.*random\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
  "description": "Search for 2024 random split 1.3%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check random split 2024 = 1.3% — plan_001_report says 0.18% only for 2023\n# Look for 2024 random split data elsewhere\ngrep -rn \"1.3\\|random.*2024\\|2024.*random\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
    "description": "Search for 2024 random split 1.3%"
  }
}
```

</details>

---


### Tool result

_source line 358 · 2026-05-23T19:54:33.854468+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:18:3,100,0.8,0.1218,0.0006,0.8163,0.003,0.0001,0.4705,0.0341,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:24:3,200,1.0,0.6227,0.0036,0.939,0.0031,0.0002,0.7218,0.0183,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:30:3,500,1.2,0.9538,0.0143,0.9843,0.0013,0.0004,0.9069,0.0035,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:52:5,200,0.6,0.182,0.0011,0.8509,0.0033,0.0001,0.3935,0.0173,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:55:5,200,1.2,0.7399,0.0057,0.9495,0.0024,0.0002,0.8153,0.0236,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:56:5,200,1.4,0.8173,0.0072,0.9486,0.002,0.0002,0.8674,0.0277,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:2:abstract_algebra.10,abstract_algebra,1.5634303993406418,1.8840975857581377e-05,0.0958103565602993,0.3822527262801475,C,A,A,True,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:3:abstract_algebra.100,abstract_algebra,1.8473056183645773,3.3721937472974695e-05,0.0050590417393351,0.0875231818999539,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:11:abstract_algebra.47,abstract_algebra,1.9931584017328616,8.333785715963771e-07,0.02
…[truncated 3076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 359 · 2026-05-23T19:54:33.854619+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Final check: verify C% values are exact matches\npython3 -c \"\n# Source values from plan_028 multi_bench_summary.csv\nc_pct = {\n    'MMLU': 31.3, 'WinoGrande': 30.3, 'TruthfulQA': 29.7,\n    'ARC': 26.9, 'GSM8K': 18.9, 'HellaSwag': 17.9\n}\npaper = {\n    'MMLU': 31.3, 'WinoGrande': 30.3, 'TruthfulQA': 29.7,\n    'ARC': 26.9, 'GSM8K': 18.9, 'HellaSwag': 17.9\n}\nfor k, v in c_pct.items():\n    match = '✅' if v == paper[k] else '❌'\n    print(f'{k}: source={v}, paper={paper[k]} {match}')\n\"",
  "description": "Verify C% column values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Final check: verify C% values are exact matches\npython3 -c \"\n# Source values from plan_028 multi_bench_summary.csv\nc_pct = {\n    'MMLU': 31.3, 'WinoGrande': 30.3, 'TruthfulQA': 29.7,\n    'ARC': 26.9, 'GSM8K': 18.9, 'HellaSwag': 17.9\n}\npaper = {\n    'MMLU': 31.3, 'WinoGrande': 30.3, 'TruthfulQA': 29.7,\n    'ARC': 26.9, 'GSM8K': 18.9, 'HellaSwag': 17.9\n}\nfor k, v in c_pct.items():\n    match = '✅' if v == paper[k] else '❌'\n    print(f'{k}: source={v}, paper={paper[k]} {match}')\n\"",
    "description": "Verify C% column values"
  }
}
```

</details>

---


### Tool result

_source line 360 · 2026-05-23T19:54:33.854769+00:00_

MMLU: source=31.3, paper=31.3 ✅
WinoGrande: source=30.3, paper=30.3 ✅
TruthfulQA: source=29.7, paper=29.7 ✅
ARC: source=26.9, paper=26.9 ✅
GSM8K: source=18.9, paper=18.9 ✅
HellaSwag: source=17.9, paper=17.9 ✅

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 361 · 2026-05-23T19:54:33.854910+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "500.*models|≥500|>=500|threshold.*500|500.*threshold",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "500.*models|≥500|>=500|threshold.*500|500.*threshold",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-23T19:54:33.855044+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find non-uniform DIF 17.7% and union 47% - search more broadly\ngrep -rn \"17.7\\|non.uniform\\|union.*47\\|47.*union\\|47%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
  "description": "Search for non-uniform DIF in md files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find non-uniform DIF 17.7% and union 47% - search more broadly\ngrep -rn \"17.7\\|non.uniform\\|union.*47\\|47.*union\\|47%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
    "description": "Search for non-uniform DIF in md files"
  }
}
```

</details>

---


### Tool call

_source line 363 · 2026-05-23T19:54:33.855187+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Let me also double-check the exact pct_c values from the more precise source (benchmark_rho_summary.csv)\n# to see if the C% values are rounded correctly\npython3 -c \"\nprecise = {\n    'TruthfulQA': 29.74, 'ARC': 26.88, 'WinoGrande': 30.31,\n    'GSM8K': 18.88, 'HellaSwag': 17.89, 'MMLU': 31.32\n}\npaper = {\n    'MMLU': 31.3, 'WinoGrande': 30.3, 'TruthfulQA': 29.7,\n    'ARC': 26.9, 'GSM8K': 18.9, 'HellaSwag': 17.9\n}\nfor k, v in precise.items():\n    rounded = round(v, 1)\n    match = '✅' if rounded == paper[k] else '❌'\n    print(f'{k}: precise={v}, rounded={rounded}, paper={paper[k]} {match}')\n\"",
  "description": "Verify C% rounding from precise values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Let me also double-check the exact pct_c values from the more precise source (benchmark_rho_summary.csv)\n# to see if the C% values are rounded correctly\npython3 -c \"\nprecise = {\n    'TruthfulQA': 29.74, 'ARC': 26.88, 'WinoGrande': 30.31,\n    'GSM8K': 18.88, 'HellaSwag': 17.89, 'MMLU': 31.32\n}\npaper = {\n    'MMLU': 31.3, 'WinoGrande': 30.3, 'TruthfulQA': 29.7,\n    'ARC': 26.9, 'GSM8K': 18.9, 'HellaSwag': 17.9\n}\nfor k, v in precise.items():\n    rounded = round(v, 1)\n    match = '✅' if rounded == paper[k] else '❌'\n    print(f'{k}: precise={v}, rounded={rounded}, paper={paper[k]} {match}')\n\"",
    "description": "Verify C% rounding from precise values"
  }
}
```

</details>

---


### Tool result

_source line 364 · 2026-05-23T19:54:33.855330+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:31:- Mean null C% per split: 0.6247%
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:33:- Fraction of (item, split) classified C: 0.006247 (0.6247%)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:42:**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the baseline false-positive rate for interpreting these observed rates.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md:24:- **Relevance to our paper**: Our logistic-regression-based DIF detection for binary (correct/incorrect) LLM responses directly follows this framework. Zumbo's formalization of uniform vs. non-uniform DIF maps onto our distinction between items that are uniformly easier for contaminated models vs. items showing interaction effects with model ability.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md:13:3. M3 (non-uniform DIF): logit(P) = β₀ + β₁θ + β₂G + β₃(θ×G)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md:47:Across all 1787 valid items in selected subjects:
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md:50:- **Both uniform and non-uniform**: 520 (29.1%)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md:52:- **Any non-uniform DIF**: 691 (38.7%)
/home/ubuntu/.agent-m
…[truncated 3880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-23T19:54:33.855474+00:00_

TruthfulQA: precise=29.74, rounded=29.7, paper=29.7 ✅
ARC: precise=26.88, rounded=26.9, paper=26.9 ✅
WinoGrande: precise=30.31, rounded=30.3, paper=30.3 ✅
GSM8K: precise=18.88, rounded=18.9, paper=18.9 ✅
HellaSwag: precise=17.89, rounded=17.9, paper=17.9 ✅
MMLU: precise=31.32, rounded=31.3, paper=31.3 ✅

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-23T19:54:33.855605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search for STEM 55.4%, humanities 64.4%, KW p=0.78 in plan dirs\ngrep -rn \"STEM\\|Humanities\\|KW\\|Kruskal\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
  "description": "Search for STEM/Humanities direction stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search for STEM 55.4%, humanities 64.4%, KW p=0.78 in plan dirs\ngrep -rn \"STEM\\|Humanities\\|KW\\|Kruskal\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
    "description": "Search for STEM/Humanities direction stats"
  }
}
```

</details>

---


### Tool call

_source line 367 · 2026-05-23T19:54:33.855764+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"20.*random\\|random.*20\\|20x\\|20×\\|C%.*12%\\|12%.*MMLU\\|12.*percent.*MMLU\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/ 2>/dev/null; grep -r \"20.*baseline\\|baseline.*20\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/ 2>/dev/null",
  "description": "Search r15_random_split_control for 20x baseline and 12% MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"20.*random\\|random.*20\\|20x\\|20×\\|C%.*12%\\|12%.*MMLU\\|12.*percent.*MMLU\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/ 2>/dev/null; grep -r \"20.*baseline\\|baseline.*20\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/ 2>/dev/null",
    "description": "Search r15_random_split_control for 20x baseline and 12% MMLU"
  }
}
```

</details>

---


### Tool result

_source line 368 · 2026-05-23T19:54:33.855896+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_analysis.py:- **Procedure**: 100 random 50/50 splits within the 2024 cohort
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md:- **Procedure**: 100 random 50/50 splits within the 2024 cohort
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_random_split_control/random_split_report.md:sample size, we ran 20 additional random splits from the **full** 5,227-model pool

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-23T19:54:33.856032+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:31:Humanities,10.0,2573.0,801.0,31.13,0.4569,0.0913,-0.2515,35.58
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:32:STEM,22.0,3023.0,935.0,30.93,0.3864,0.0592,0.0814,55.4
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:35:**STEM vs Humanities:**
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:36:- STEM mean %C = 30.8%, Humanities mean %C = 29.9%
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:39:- Kruskal-Wallis (3 groups): H = 0.498, p = 0.7797
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:62:world_religions,Humanities,59,42.73142641662912,16.26857358337088,0.005334855609736918
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:74:logical_fallacies,Humanities,45.0,20.0,0.0001
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:75:world_religions,Humanities,59.0,16.9,0.0
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:81:2. STEM vs Humanities difference is not significant (p = 0.6113).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/report/plan_033_report.md:31:Humanities,10.0,2573.0,801.0,
…[truncated 3483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-23T19:54:33.856195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check r18_base_instruct_survey for groundtruth numbers\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep r18; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/ 2>/dev/null",
  "description": "Check r18_base_instruct_survey directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check r18_base_instruct_survey for groundtruth numbers\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep r18; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/ 2>/dev/null",
    "description": "Check r18_base_instruct_survey directory"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-23T19:54:33.856318+00:00_

r18_base_instruct_survey
r18_base_vs_instruct_dif
r18_dedup_k_curve
r18_icc_by_family_size
r18_rank_bucket_reversal
r18_restricted_range_rho
base_instruct_survey.md
model_type_classification.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-23T19:54:33.856442+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check for 9229 annotated items, p=0.88, enrichment=0.964, Jaccard=0.206\ngrep -rn \"9229\\|0.88\\|0.964\\|0.206\\|Jaccard\\|enrichment\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
  "description": "Search for groundtruth validation numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check for 9229 annotated items, p=0.88, enrichment=0.964, Jaccard=0.206\ngrep -rn \"9229\\|0.88\\|0.964\\|0.206\\|Jaccard\\|enrichment\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
    "description": "Search for groundtruth validation numbers"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-23T19:54:33.856575+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:56:|      100 | 0.445   | 0.440   | 0.002   | 0.002   | 0.888   | 0.888   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:66:|       80 | 0.454   | 0.450   | 0.002   | 0.002   | 0.881   | 0.880   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:6:- Items with annotation: 9229 (excluded 3279 `no_annotation`)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_013_report.md:26:| P75 | 0.0688 | 0.0470 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_013_report.md:60:Spearman correlation between subject size (n_items) and mean Q3: ρ = 0.2064, p = 1.23e-01
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_013_report.md:80:4. **Subject-size effect**: Spearman ρ = 0.2064 (p = 1.23e-01) between subject size and mean Q3. No strong relationship between subject size and degree of local dependence.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md:117:- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/pr
…[truncated 3235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-23T19:54:33.856746+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md | head -80",
  "description": "Read plan_033 report for STEM/Humanities direction stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md | head -80",
    "description": "Read plan_033 report for STEM/Humanities direction stats"
  }
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-23T19:54:33.856893+00:00_

# Plan 033: Subject-Level DIF Concentration Analysis

## Overview

Analyzed DIF distribution across 57 MMLU subjects (12508 items total)
to determine whether differential item functioning concentrates in specific knowledge domains.

## 1. Subject-Level DIF Rates

| Metric | Value |
|--------|-------|
| Subjects with C-flagged items | 57 / 57 |
| Mean %C across subjects | 30.6% |
| Median %C | 29.7% |
| Range | 20.7% – 48.4% |

**Highest DIF concentration:**
- business_ethics: 48.4%
- human_aging: 41.9%
- formal_logic: 40.4%

**Lowest DIF concentration:**
- computer_security: 20.7%
- marketing: 20.9%
- management: 21.7%

## 2. Domain-Level Summary

domain,n_subjects,n_items,n_c,pct_c,mean_difficulty,mean_discrimination,mean_delta_mh,pct_favor_focal
Social Science,25.0,6912.0,2182.0,31.57,0.4641,0.0773,-0.176,42.03
Humanities,10.0,2573.0,801.0,31.13,0.4569,0.0913,-0.2515,35.58
STEM,22.0,3023.0,935.0,30.93,0.3864,0.0592,0.0814,55.4


**STEM vs Humanities:**
- STEM mean %C = 30.8%, Humanities mean %C = 29.9%
- Mann-Whitney U = 123.0, p = 0.6113 (not significant at α=0.05)
- Welch t = 0.539, p = 0.5963
- Kruskal-Wallis (3 groups): H = 0.498, p = 0.7797

## 3. Predictive Model

Logistic regression: P(DIF_C) ~ difficulty + discrimination + n_items_in_subject

variable,odds_ratio,or_ci_lower,or_ci_upper,p_value
Intercept,0.9108087274128313,0.8188856549312612,1.013050519246203,0.08523388706865416
ctt_difficulty,0.08564518063337925,0.06861451900424628,0.1069029860177293,1.1826004780999362e-104
ctt_discrimination,57.23938812742111,39.38959956939529,83.17798578859369,5.674311442211938e-100
n_items_in_subject,1.0001239466510743,1.0000199645265944,1.0002279395876204,0.019475631746116214


Pseudo R² = 0.0423, N = 12508

**Subject residuals (controlling difficulty + discrimination):**
- 5 subjects show significantly MORE DIF than expected (p < 0.05)
- 2 subjects show significantly LESS DIF than expected (p < 0.05)

Top excess-DIF subjects:
subject,domain,observed_c,expected_c,exces
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-23T19:54:33.857048+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find STEM 55.4% and Humanities 64.4% — those are percent focal-favoring, not C%\ngrep -n \"55.4\\|64.4\\|focal.favor\\|direction\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md",
  "description": "Find focal-favoring percentages in plan_033"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find STEM 55.4% and Humanities 64.4% — those are percent focal-favoring, not C%\ngrep -n \"55.4\\|64.4\\|focal.favor\\|direction\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md",
    "description": "Find focal-favoring percentages in plan_033"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-23T19:54:33.857172+00:00_

32:STEM,22.0,3023.0,935.0,30.93,0.3864,0.0592,0.0814,55.4
71:**Subjects with unidirectional DIF (≥80% one direction, n≥5):**
83:4. 43.9% of C-flagged items favor 2024 models, with 2 subjects showing near-unidirectional asymmetry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-23T19:54:33.857302+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md",
  "description": "Read full plan_033 report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md",
    "description": "Read full plan_033 report"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-23T19:54:33.857433+00:00_

# Plan 033: Subject-Level DIF Concentration Analysis

## Overview

Analyzed DIF distribution across 57 MMLU subjects (12508 items total)
to determine whether differential item functioning concentrates in specific knowledge domains.

## 1. Subject-Level DIF Rates

| Metric | Value |
|--------|-------|
| Subjects with C-flagged items | 57 / 57 |
| Mean %C across subjects | 30.6% |
| Median %C | 29.7% |
| Range | 20.7% – 48.4% |

**Highest DIF concentration:**
- business_ethics: 48.4%
- human_aging: 41.9%
- formal_logic: 40.4%

**Lowest DIF concentration:**
- computer_security: 20.7%
- marketing: 20.9%
- management: 21.7%

## 2. Domain-Level Summary

domain,n_subjects,n_items,n_c,pct_c,mean_difficulty,mean_discrimination,mean_delta_mh,pct_favor_focal
Social Science,25.0,6912.0,2182.0,31.57,0.4641,0.0773,-0.176,42.03
Humanities,10.0,2573.0,801.0,31.13,0.4569,0.0913,-0.2515,35.58
STEM,22.0,3023.0,935.0,30.93,0.3864,0.0592,0.0814,55.4


**STEM vs Humanities:**
- STEM mean %C = 30.8%, Humanities mean %C = 29.9%
- Mann-Whitney U = 123.0, p = 0.6113 (not significant at α=0.05)
- Welch t = 0.539, p = 0.5963
- Kruskal-Wallis (3 groups): H = 0.498, p = 0.7797

## 3. Predictive Model

Logistic regression: P(DIF_C) ~ difficulty + discrimination + n_items_in_subject

variable,odds_ratio,or_ci_lower,or_ci_upper,p_value
Intercept,0.9108087274128313,0.8188856549312612,1.013050519246203,0.08523388706865416
ctt_difficulty,0.08564518063337925,0.06861451900424628,0.1069029860177293,1.1826004780999362e-104
ctt_discrimination,57.23938812742111,39.38959956939529,83.17798578859369,5.674311442211938e-100
n_items_in_subject,1.0001239466510743,1.0000199645265944,1.0002279395876204,0.019475631746116214


Pseudo R² = 0.0423, N = 12508

**Subject residuals (controlling difficulty + discrimination):**
- 5 subjects show significantly MORE DIF than expected (p < 0.05)
- 2 subjects show significantly LESS DIF than expected (p < 0.05)

Top excess-DIF subjects:
subject,domain,observed_c,expected_c,exces
…[truncated 1188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-23T19:54:33.857582+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_ctt_stats.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_subject_stats.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_model_accuracy.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/psn_irt_item_parameters.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/rank_changes.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_irt_params.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/deff_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 11
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-23T19:54:33.857735+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/domain_specificity.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/within_family_dif.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability_c17059.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/cross_analysis.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/neg_disc_sensitivity.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal_69f998.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 11
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-23T19:54:33.857912+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find STEM 55.4% pct_favor_focal and Humanities 64.4% — paper says STEM 55.4%, Humanities 64.4% favor 2024 and 2023 respectively\n# plan_033 shows STEM pct_favor_focal=55.4% (favor 2024) and Humanities pct_favor_focal=35.58% (meaning 100-35.58=64.4% favor 2023)\n# That checks out: STEM 55.4% favor 2024, Humanities 64.4% favor 2023 (= 100% - 35.58%)\necho \"STEM pct_favor_focal=55.4 (paper says STEM items favor 2024 models: 55.4%)\"\necho \"Humanities pct_favor_focal=35.58 => 100-35.58=64.42 favor 2023 (paper says Humanities favor 2023: 64.4%)\"\npython3 -c \"print(round(100-35.58,1))\"",
  "description": "Verify STEM/Humanities direction calculations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find STEM 55.4% pct_favor_focal and Humanities 64.4% — paper says STEM 55.4%, Humanities 64.4% favor 2024 and 2023 respectively\n# plan_033 shows STEM pct_favor_focal=55.4% (favor 2024) and Humanities pct_favor_focal=35.58% (meaning 100-35.58=64.4% favor 2023)\n# That checks out: STEM 55.4% favor 2024, Humanities 64.4% favor 2023 (= 100% - 35.58%)\necho \"STEM pct_favor_focal=55.4 (paper says STEM items favor 2024 models: 55.4%)\"\necho \"Humanities pct_favor_focal=35.58 => 100-35.58=64.42 favor 2023 (paper says Humanities favor 2023: 64.4%)\"\npython3 -c \"print(round(100-35.58,1))\"",
    "description": "Verify STEM/Humanities direction calculations"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-23T19:54:33.858055+00:00_

artifacts/rebuttal_talking_points.md:7:## B5 (Q6): ≥500 threshold
artifacts/_project/report/response_letter_draft.md:140:### [R2-Q3/Q6] ≥500 Model Threshold
artifacts/_project/report/response_letter_draft.md:142:**Concern**: Power analysis shows $N \geq 80$ per cohort suffices; ≥500 total models is overly conservative.
artifacts/_project/report/response_letter_draft.md:144:**Response**: We softened the threshold in §5.2: "≥500 models" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that "smaller corpora may suffice with fewer strata." New experiment E1 confirms this:
artifacts/_project/report/response_letter_draft.md:199:| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |
artifacts/_project/report/rebuttal_talking_points.md:7:## B5 (Q6): ≥500 threshold
artifacts/response_letter_draft.md:140:### [R2-Q3/Q6] ≥500 Model Threshold
artifacts/response_letter_draft.md:142:**Concern**: Power analysis shows $N \geq 80$ per cohort suffices; ≥500 total models is overly conservative.
artifacts/response_letter_draft.md:144:**Response**: We softened the threshold in §5.2: "≥500 models" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that "smaller corpora may suffice with fewer strata." New experiment E1 confirms this:
artifacts/response_letter_draft.md:199:| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:9:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:41:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:56:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:65:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:71:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/r
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 3
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-23T19:54:33.858197+00:00_

STEM pct_favor_focal=55.4 (paper says STEM items favor 2024 models: 55.4%)
Humanities pct_favor_focal=35.58 => 100-35.58=64.42 favor 2023 (paper says Humanities favor 2023: 64.4%)
64.4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-23T19:54:33.858331+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "20.*times|C%.*exceed|exceed.*20|C%.*12|12.*percent.*MMLU|MMLU.*12|20.*random.split.*baseline|random.split.*12|0\\.18.*percent|0\\.18%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "20.*times|C%.*exceed|exceed.*20|C%.*12|12.*percent.*MMLU|MMLU.*12|20.*random.split.*baseline|random.split.*12|0\\.18.*percent|0\\.18%",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-23T19:54:33.858464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-23T19:54:33.858582+00:00_

1	cohort_type,item_filter,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,fpr_vs_li_clean,enrichment_ratio
2	temporal,all,12508,6332,2258,3918,31.323952670291018,0.31840974212034384,0.9641535548797142
3	ability,all,12508,11052,1093,363,2.9021426287176206,0.026862464183381087,1.1949300411522636
4	temporal,non_neg_disc,10582,5327,1830,3425,32.36628236628237,0.3257975913796746,0.969539159262983
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-23T19:54:33.858733+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find 18.3% at |Δ_MH|≥2.0 and 10.2% at ≥2.5\npython3 -c \"\nimport csv\nitems = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        items.append(row)\n\ntotal = len(items)\nc_items_2_0 = sum(1 for r in items if abs(float(r['delta_mh'])) >= 2.0)\nc_items_2_5 = sum(1 for r in items if abs(float(r['delta_mh'])) >= 2.5)\nprint(f'Total items: {total}')\nprint(f'|delta_mh|>=2.0: {c_items_2_0} ({c_items_2_0/total*100:.1f}%)')\nprint(f'|delta_mh|>=2.5: {c_items_2_5} ({c_items_2_5/total*100:.1f}%)')\n\"",
  "description": "Compute threshold analysis (18.3%, 10.2%)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find 18.3% at |Δ_MH|≥2.0 and 10.2% at ≥2.5\npython3 -c \"\nimport csv\nitems = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        items.append(row)\n\ntotal = len(items)\nc_items_2_0 = sum(1 for r in items if abs(float(r['delta_mh'])) >= 2.0)\nc_items_2_5 = sum(1 for r in items if abs(float(r['delta_mh'])) >= 2.5)\nprint(f'Total items: {total}')\nprint(f'|delta_mh|>=2.0: {c_items_2_0} ({c_items_2_0/total*100:.1f}%)')\nprint(f'|delta_mh|>=2.5: {c_items_2_5} ({c_items_2_5/total*100:.1f}%)')\n\"",
    "description": "Compute threshold analysis (18.3%, 10.2%)"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-23T19:54:33.858879+00:00_

paper/sections/related_work.tex:5:[Omitted long matching line]
paper/sections/limitations.tex:4:[Omitted long matching line]
paper/sections/experiments.tex:4:We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
paper/sections/experiments.tex:19:Three controls confirm genuine temporal change (\Cref{tab:temporal_landscape}): random splits yield mean C\% of 0.62\% (2023; 100 permutations) and 1.3\% (2024; 100 permutations), both ${\geq}24\times$ below temporal C\%; ability-quintile comparison yields 2.9\%; and 1:1 nearest-neighbor matching on total score ($N{=}638$/group, Cohen's $d = -0.17$) yields C\% $= 28.9\% \pm 0.1\%$, confirming at most ${\sim}2.4$~pp is attributable to ability mismatch ($p < 0.01$; \Cref{app:method_details}).
paper/sections/experiments.tex:84:[Omitted long matching line]
paper/sections/experiments.tex:90:[Omitted long matching line]
paper/sections/experiments.tex:100:\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts; $\rho$/$\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\%/Rand.\ C\%, with baseline varying by benchmark. All six show substantial DIF (45--95$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
paper/sections/experiments.tex:108:MMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.62 & 50$\times$ \\
paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/discussion.tex:15:[Omitted long matching line]
paper/sections/discussion.tex:21:[Omitted long matching line]
paper/sections/method.tex:9:[Omitted long matching line]
paper/sections/method.tex:16:[Omitted
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-23T19:54:33.859032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"20\\\\\\\\times\\|20.*random\\|random.*split.*baseline\\|C%.*12\\|12.*MMLU\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
  "description": "Search for 20x random-split baseline in discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"20\\\\\\\\times\\|20.*random\\|random.*split.*baseline\\|C%.*12\\|12.*MMLU\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex",
    "description": "Search for 20x random-split baseline in discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-23T19:54:33.859159+00:00_

21:Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend a three-step protocol: (1)~\emph{Monitor}: run MH-DIF audits whenever ${\geq}$500 models accumulate ($K{=}3$ for smaller corpora; \Cref{tab:k3_power}), triggering review when C\% exceeds $20\times$ the random-split baseline (C\% $\approx 12\%$ for MMLU); (2)~\emph{Triage}: apply mechanism-conditional responses---DIF $\times$ web-overlap co-occurrence warrants removal; DIF on web-clean items warrants monitoring (DIF alone cannot determine causation); base/instruct reversal motivates refined cohort definitions; (3)~\emph{Correct}: DIF flags identify items warranting expert review, not automatic removal---DIF is necessary but not sufficient for item bias~\citep{camilli1994methods,penfield2007dif}. Report DIF-corrected scores alongside raw scores (\Cref{app:score_inflation}), or apply equating adjustments~\citep{kolen2014equating,habba2026growingpains,suk2026rethinking}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-23T19:54:33.859309+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Check if there's a version with N=2600 ability cohorts\n# Maybe it's a looser half split (Q1-3 vs Q3-5 or different quantile)\n# Or maybe model count from different set\n# Check plan_001_real_data_dif_mmlu dif_results_ability_c17059.csv header\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability_c17059.csv') as f:\n    for i, line in enumerate(f):\n        if i < 3:\n            print(line.strip())\n\"\n",
  "description": "Check alternative ability DIF results file header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Check if there's a version with N=2600 ability cohorts\n# Maybe it's a looser half split (Q1-3 vs Q3-5 or different quantile)\n# Or maybe model count from different set\n# Check plan_001_real_data_dif_mmlu dif_results_ability_c17059.csv header\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability_c17059.csv') as f:\n    for i, line in enumerate(f):\n        if i < 3:\n            print(line.strip())\n\"\n",
    "description": "Check alternative ability DIF results file header"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-23T19:54:33.859478+00:00_

item_id,subject,alpha_mh,delta_mh,se,p_value,ets_class,li_label,li_contamination_type
abstract_algebra.1,abstract_algebra,0.0,inf,,1.0,A,False,clean
abstract_algebra.10,abstract_algebra,0.0,inf,,0.5924712135692113,A,False,clean

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-23T19:54:33.859616+00:00_

Total items: 12508
|delta_mh|>=2.0: 2297 (18.4%)
|delta_mh|>=2.5: 1278 (10.2%)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-23T19:54:33.859763+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find non-uniform DIF 17.7% and union 47%\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md",
  "description": "Read nonuniform_dif_report for 17.7% and 47% stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find non-uniform DIF 17.7% and union 47%\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md",
    "description": "Read nonuniform_dif_report for 17.7% and 47% stats"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-23T19:54:33.859904+00:00_

# Non-Uniform DIF Robustness Check (Plan 021)

## Method
Logistic regression DIF analysis (Swaminathan & Rogers, 1990) on selected MMLU subjects.
- **Reference cohort**: 2023 models (n=1080)
- **Focal cohort**: 2024 models (n=807)
- **Matching variable**: within-subject total score (θ)
- **Multiple testing correction**: Benjamini-Hochberg FDR within each subject

Three nested models per item:
1. M1 (baseline): logit(P) = β₀ + β₁θ
2. M2 (uniform DIF): logit(P) = β₀ + β₁θ + β₂G
3. M3 (non-uniform DIF): logit(P) = β₀ + β₁θ + β₂G + β₃(θ×G)

Uniform DIF: M2 vs M1 (LR test, p < 0.05 after BH). Non-uniform DIF: M3 vs M2 (LR test, p < 0.05 after BH).

## 1. Subject Selection

| Subject | n_items | MH C% | Selection Reason |
|---------|---------|-------|------------------|
| business_ethics | 93 | 48.4% | high_C |
| human_aging | 203 | 41.9% | high_C |
| formal_logic | 109 | 40.4% | high_C |
| miscellaneous | 745 | 25.8% | medium_C (large n) |
| college_medicine | 161 | 28.6% | medium_C (medium n) |
| college_mathematics | 72 | 34.7% | medium_C (small n) |
| computer_security | 87 | 20.7% | low_C |
| marketing | 225 | 20.9% | low_C |
| management | 92 | 21.7% | low_C |

## 2. Per-Subject Results

| Subject | n_items | n_conv | Uniform Only | Non-Uniform Only | Both | Neither | Uniform% | Non-Uniform% | MH C% |
|---------|---------|--------|-------------|-----------------|------|---------|----------|-------------|-------|
| business_ethics | 93 | 93 | 24 | 6 | 44 | 19 | 73.1% | 53.8% | 48.4% |
| human_aging | 203 | 203 | 56 | 23 | 67 | 57 | 60.6% | 44.3% | 41.9% |
| formal_logic | 109 | 109 | 19 | 9 | 63 | 18 | 75.2% | 66.1% | 40.4% |
| miscellaneous | 745 | 745 | 208 | 79 | 170 | 288 | 50.7% | 33.4% | 25.8% |
| college_medicine | 161 | 161 | 47 | 15 | 53 | 46 | 62.1% | 42.2% | 28.6% |
| college_mathematics | 72 | 72 | 19 | 7 | 34 | 12 | 73.6% | 56.9% | 34.7% |
| computer_security | 87 | 87 | 20 | 12 | 18 | 37 | 43.7% | 34.5% | 20.7% |
| marketing | 225 | 225 | 56 | 15 | 46 |
…[truncated 2928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-23T19:54:33.860056+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The paper says ~2600/~2600 but data consistently shows 2092/2089\n# Let me check the plan_001_analysis.py to see how the ability quintile is computed\n\npython3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py') as f:\n    content = f.read()\n    # Find the quintile definition\n    idx = content.find('quintile')\n    if idx < 0:\n        idx = content.find('Q1')\n    print(content[max(0,idx-200):idx+500])\n\"\n",
  "description": "Check plan_001 analysis script for quintile definition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The paper says ~2600/~2600 but data consistently shows 2092/2089\n# Let me check the plan_001_analysis.py to see how the ability quintile is computed\n\npython3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py') as f:\n    content = f.read()\n    # Find the quintile definition\n    idx = content.find('quintile')\n    if idx < 0:\n        idx = content.find('Q1')\n    print(content[max(0,idx-200):idx+500])\n\"\n",
    "description": "Check plan_001 analysis script for quintile definition"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-23T19:54:33.860198+00:00_

n ../):
  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary
  response_matrix_index.npz    — model_names, item_ids
  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
  item_metadata.csv            — subject, is_negative_disc
  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels

Outputs (all in ./):
  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
  neg_disc_sensitivity.csv, plan_001_report.md

Dependencies: numpy, scipy, pandas
"""

import numpy as np
import pandas as pd
from scipy.sparse import load_npz
from scipy.stats import chi2 as chi2_

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-23T19:54:33.860345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The paper says: C% exceeds 20× random-split baseline (C%≈12% for MMLU)\n# From experiments.tex: MMLU random split baseline = 0.62% (2023)\n# 20 × 0.62% = 12.4%\n# Let's check: if random baseline is 0.62%, then 20× = 12.4% ≈ 12%\n# Also need to verify the ≥500 threshold has source\npython3 -c \"print(f'20x 0.62% = {20*0.62:.1f}%'); print(f'20x 1.3% = {20*1.3:.1f}%')\"",
  "description": "Calculate 20x random-split baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The paper says: C% exceeds 20× random-split baseline (C%≈12% for MMLU)\n# From experiments.tex: MMLU random split baseline = 0.62% (2023)\n# 20 × 0.62% = 12.4%\n# Let's check: if random baseline is 0.62%, then 20× = 12.4% ≈ 12%\n# Also need to verify the ≥500 threshold has source\npython3 -c \"print(f'20x 0.62% = {20*0.62:.1f}%'); print(f'20x 1.3% = {20*1.3:.1f}%')\"",
    "description": "Calculate 20x random-split baseline"
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-23T19:54:33.860469+00:00_

20x 0.62% = 12.4%
20x 1.3% = 26.0%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-23T19:54:33.860668+00:00_

All cells verified. Here is the complete audit report:

---

## Table 3 核查

**Sources used:**
- Items, C%: `artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv` (precise values also in `artifacts/mf2_practical_significance/benchmark_rho_summary.csv`)
- ρ, τ, Flip%: `artifacts/mf2_practical_significance/benchmark_rho_summary.csv` (identical copy: `artifacts/_project/data/benchmark_rho_summary.csv`)
- Rand C% (MMLU): `artifacts/_project/data/random_split_report.md` — mean null C% from 100 random 540/540 splits of 2023 cohort = 0.6247%
- Rand C% (all others): `artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv` column `random_pct_c`
- Ratio: computed as C% ÷ Rand C%

---

### MMLU
- Cell [MMLU, Items] = 12,508 ← plan_028 multi_bench_summary.csv: 12508 ✅
- Cell [MMLU, C%] = 31.3 ← plan_028: 31.3 (precise 31.32) ✅
- Cell [MMLU, ρ] = 0.9965 ← benchmark_rho_summary.csv: 0.9965 ✅
- Cell [MMLU, τ] = 0.9600 ← benchmark_rho_summary.csv: 0.959986 → rounds to 0.9600 ✅
- Cell [MMLU, Flip%] = 2.00 ← benchmark_rho_summary.csv: flip_rate=0.020007 → 2.00% ✅
- Cell [MMLU, Rand C%] = 0.62 ← _project/data/random_split_report.md: null mean C% = 0.6247% (100 random 540/540 splits of 2023 cohort) ✅ ⚠️ **Note:** plan_028 CSV stores 0.18 (a single sanity split from plan_001). The paper correctly uses the more robust 100-run mean of 0.6247%. The discrepancy between sources is expected and documented.
- Cell [MMLU, Ratio] = 50× ← 31.3/0.62 = 50.5 → rounds to 50× ✅

### WinoGrande
- Cell [WinoGrande, Items] = 1,267 ← plan_028: 1267 ✅
- Cell [WinoGrande, C%] = 30.3 ← plan_028: 30.3 (precise 30.31) ✅
- Cell [WinoGrande, ρ] = 0.9943 ← benchmark_rho_summary.csv: 0.994255 → rounds to 0.9943 ✅
- Cell [WinoGrande, τ] = 0.9432 ← benchmark_rho_summary.csv: 0.943166 → rounds to 0.9432 ✅
- Cell [WinoGrande, Flip%] = 2.84 ← benchmark_rho_summary.csv: flip_rate=0.028417 → 2.84% ✅
- Cell [WinoGrande, Rand C%] = 0.32 ← plan_028 random_pct_c: 0.32 ✅
- Cell [WinoGrande, Ratio] = 95× ← 3
…[truncated 2863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "elapsed_ms": 57
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-23T19:54:33.860861+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "≥500\\|>=500\\|500.*model.*threshold\\|accumulate.*500\\|500.*accumulate",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "≥500\\|>=500\\|500.*model.*threshold\\|accumulate.*500\\|500.*accumulate",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-23T19:54:33.860997+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-23T19:54:33.861126+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py') as f:\n    content = f.read()\n# Find lines that define cohorts\nimport re\nlines = content.split('\\n')\nfor i, line in enumerate(lines):\n    if 'q1' in line.lower() or 'q4' in line.lower() or 'ability' in line.lower() or 'quintile' in line.lower():\n        print(f'L{i}: {line}')\n\" | head -30\n",
  "description": "Find quintile definition in plan_001 script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py') as f:\n    content = f.read()\n# Find lines that define cohorts\nimport re\nlines = content.split('\\n')\nfor i, line in enumerate(lines):\n    if 'q1' in line.lower() or 'q4' in line.lower() or 'ability' in line.lower() or 'quintile' in line.lower():\n        print(f'L{i}: {line}')\n\" | head -30\n",
    "description": "Find quintile definition in plan_001 script"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-23T19:54:33.861254+00:00_

L5: two cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates
L12:   model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
L17:   dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
L278:     # ── Step 1-2: MH-DIF — Ability cohort ──────────────────────────────────
L279:     print("\n=== Step 1-2b: Ability cohort DIF (Q1-2 vs Q4-5, 10 strata) ===")
L280:     ref_a = rows_for("cohort_accuracy_quintile", [1, 2])
L281:     foc_a = rows_for("cohort_accuracy_quintile", [4, 5])
L287:     summary_rows.append(summary_row("ability", "all", dif_abil))
L295:     print(f"  Ability  — FPR={li_a['fpr_vs_li_clean']:.4f}, "
L462:     dif_abil[out_cols].to_csv(OUT / "dif_results_ability.csv", index=False)
L495:     print(f"\nAbility (Q1-2 vs Q4-5, 10 strata):")
L530:     w(f"- Ability cohort: ref = Q1-2 (N={len(ref_a)}), foc = Q4-5 (N={len(foc_a)}), 10 strata")
L548:     for name, lm in [("temporal", li_t), ("ability", li_a)]:
L608:     w(f"- Ability C: {len(abil_c)} items")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-23T19:54:33.861398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Understand 17.7% non-uniform and 47% union claims\n# The paper says: \"Logistic regression detects an additional 17.7% with non-uniform DIF (|β_interaction| ≥ 0.5), reaching a union of 47%\"\n# Plan_021 (nonuniform_dif_report) is on a selected subset of 9 subjects, not the full 12508\n# |β_interaction|≥0.5 on 1787 items = 444 = 24.8%\n# This doesn't directly give 17.7% additional\n# Let's check if there's a full analysis elsewhere\ngrep -rn \"17.7\\|47%\\|non.uniform.*add\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
  "description": "Search for 17.7% non-uniform DIF source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Understand 17.7% non-uniform and 47% union claims\n# The paper says: \"Logistic regression detects an additional 17.7% with non-uniform DIF (|β_interaction| ≥ 0.5), reaching a union of 47%\"\n# Plan_021 (nonuniform_dif_report) is on a selected subset of 9 subjects, not the full 12508\n# |β_interaction|≥0.5 on 1787 items = 444 = 24.8%\n# This doesn't directly give 17.7% additional\n# Let's check if there's a full analysis elsewhere\ngrep -rn \"17.7\\|47%\\|non.uniform.*add\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
    "description": "Search for 17.7% non-uniform DIF source"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-23T19:54:33.861538+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:31:- Mean null C% per split: 0.6247%
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:33:- Fraction of (item, split) classified C: 0.006247 (0.6247%)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:42:**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the baseline false-positive rate for interpreting these observed rates.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md:47:Across all 1787 valid items in selected subjects:
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md:72:Distribution by effect size threshold (of all 1787 valid items):
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/score_inflation_report.md:52:| Gille/StrangeMerges_17-7B-dare_ties | other | base | 0.6933 | 0.7214 | +2.81 | +436 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/rank_shift_distribution_report.md:140:| 16 | Gille/StrangeMerges_17-7B-dare_ties | unknown | 1491 | 1051 | -440 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf2_report.md:9:| HellaSwag | 10042 | 1797 | 8245 | 17.89% | 5227 | 0.9986 | 0.00e+00 | 0.9722 | 0.0139 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/power_calibration_report.md:17:| Remove Mistral (N_ref: 1080→533) | 31.32% | 30.91±2.07% | 22.47% | -0.41
…[truncated 3485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-23T19:54:33.861696+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "500.*model\\|model.*500\\|accumulate\\|threshold.*model\\|model.*threshold",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "500.*model\\|model.*500\\|accumulate\\|threshold.*model\\|model.*threshold",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-23T19:54:33.861858+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check r18_base_vs_instruct for chi-sq and related data; also check plan_033 for 0.1% variance explained\ngrep -rn \"0.1%\\|variance.*explained\\|R2\\|pseudo\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/ 2>/dev/null | head -10",
  "description": "Find variance explained stat"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check r18_base_vs_instruct for chi-sq and related data; also check plan_033 for 0.1% variance explained\ngrep -rn \"0.1%\\|variance.*explained\\|R2\\|pseudo\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/ 2>/dev/null | head -10",
    "description": "Find variance explained stat"
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-23T19:54:33.861980+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-23T19:54:33.862111+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check if any artifact justifies the ≥500 threshold\ngrep -rn \"500.*models\\|models.*500\\|500.*threshold\\|threshold.*500\\|when.*500\\|500.*when\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/ 2>/dev/null | head -20",
  "description": "Search for 500 models threshold in sf8_power_sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check if any artifact justifies the ≥500 threshold\ngrep -rn \"500.*models\\|models.*500\\|500.*threshold\\|threshold.*500\\|when.*500\\|500.*when\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/ 2>/dev/null | head -20",
    "description": "Search for 500 models threshold in sf8_power_sensitivity"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-23T19:54:33.862233+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 413 · 2026-05-23T19:54:33.862363+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# The quintile counts are: Q1:1046, Q2:1046, Q3:1046, Q4:1059, Q5:1030\n# Q1+Q2 = 2092, Q4+Q5 = 2089 — these are correct\n# The paper says ~2600/~2600 which is WRONG\n\n# Let me check the r22_composition_control for any different quintile grouping\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/'\nfor f in os.listdir(base):\n    print(f)\n\"\n",
  "description": "Check r22 composition control directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# The quintile counts are: Q1:1046, Q2:1046, Q3:1046, Q4:1059, Q5:1030\n# Q1+Q2 = 2092, Q4+Q5 = 2089 — these are correct\n# The paper says ~2600/~2600 which is WRONG\n\n# Let me check the r22_composition_control for any different quintile grouping\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/'\nfor f in os.listdir(base):\n    print(f)\n\"\n",
    "description": "Check r22 composition control directory"
  }
}
```

</details>

---


### Tool result

_source line 414 · 2026-05-23T19:54:33.862492+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 415 · 2026-05-23T19:54:33.862624+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check difficulty-direction interaction rho = -0.597\n# Already found in mixed_mechanism_semisynthetic: ρ(difficulty, δ_MH) overall = -0.597\n# But let's look for the source from actual data analysis\ngrep -n \"0.597\\|rho.*diff\\|spearman.*diff\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/difficulty_modeltype_interaction/interaction_report.md",
  "description": "Verify ρ=-0.597 source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check difficulty-direction interaction rho = -0.597\n# Already found in mixed_mechanism_semisynthetic: ρ(difficulty, δ_MH) overall = -0.597\n# But let's look for the source from actual data analysis\ngrep -n \"0.597\\|rho.*diff\\|spearman.*diff\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/difficulty_modeltype_interaction/interaction_report.md",
    "description": "Verify ρ=-0.597 source"
  }
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-23T19:54:33.862776+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/ && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/*.md 2>/dev/null | head -60",
  "description": "Read sf8_power_sensitivity files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/ && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/*.md 2>/dev/null | head -60",
    "description": "Read sf8_power_sensitivity files"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-23T19:54:33.862897+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 418 · 2026-05-23T19:54:33.863020+00:00_

param_descriptives.csv
sensitivity_results.csv
sf8_power_sensitivity.py
sf8_report.md
# SF8: Power Analysis — Parameter Descriptives & Sensitivity

## 1. IRT Parameter Descriptive Statistics

### PSN-IRT MMLU Items (N=14042)

| Param | Mean | SD | Min | Q1 | Median | Q3 | Max | Skew | Kurt |
|-------|------|----|-----|----|----|----|----|------|------|
| a (disc) | 1.197 | 0.542 | 0.006 | 0.751 | 1.162 | 1.637 | 2.657 | 0.100 | -0.956 |
| b (diff) | -0.838 | 0.790 | -2.683 | -1.425 | -0.895 | -0.315 | 1.692 | 0.288 | -0.433 |

### MetaBench Items (N=12508)

| Param | Mean | SD | Min | Q1 | Median | Q3 | Max | Skew | Kurt |
|-------|------|----|-----|----|----|----|----|------|------|
| a (disc) | 0.076 | 0.131 | -0.551 | 0.073 | 0.107 | 0.146 | 0.291 | -1.968 | 3.913 |
| b (diff) | 0.444 | 0.211 | 0.008 | 0.261 | 0.524 | 0.629 | 0.689 | -0.641 | -1.047 |

**Note**: PSN-IRT uses 4PL model (we take a, b as 2PL approximation); MetaBench uses a different IRT calibration. The PSN-IRT `discrimination` column maps to the 2PL `a` parameter directly.

## 2. TPR Sensitivity: TPR = f(a)

**Design**: Fixed b = -0.8383, N = 80/group, Δb = 1.4 logits (b-shift), 200 items (10% contaminated), 1000 replications. Observed MH Δ scales as 2.35·a·Δb.

| a | TPR | 95% CI | FPR |
|---|-----|--------|-----|
| 0.5 | 0.398 | [0.200, 0.600] | 0.0333 |
| 0.8 | 0.683 | [0.450, 0.900] | 0.0364 |
| 1.0 | 0.808 | [0.600, 0.950] | 0.0375 |
| 1.2 | 0.874 | [0.700, 1.000] | 0.0382 |
| 1.5 | 0.930 | [0.800, 1.000] | 0.0381 |
| 2.0 | 0.949 | [0.800, 1.000] | 0.0367 |

## 3. Interpretation

- **Monotonic TPR increase with a**: Higher discrimination items produce larger observed MH delta for a given latent DIF, making detection easier.
- **FPR control**: FPR remains well below 0.10 across all a values, confirming the ETS C classification is conservative.
- **Practical implication**: Items with a < 0.8 have substantially reduced power for detecting moderate DIF (|Δ_MH| = 1.4). The real MMLU pool (mean a ≈
…[truncated 249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 419 · 2026-05-23T19:54:33.863168+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check matching: N=638/group, Cohen's d=-0.17, C%=28.9% ±0.1%\ngrep -rn \"638\\|Cohen.*d.*0.17\\|d.*0.17\\|28.9\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
  "description": "Find ability matching stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check matching: N=638/group, Cohen's d=-0.17, C%=28.9% ±0.1%\ngrep -rn \"638\\|Cohen.*d.*0.17\\|d.*0.17\\|28.9\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
    "description": "Find ability matching stats"
  }
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-23T19:54:33.863307+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "AUROC.*0\\.60\\|0\\.60.*AUROC\\|AUROC.*0\\.60[0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "AUROC.*0\\.60\\|0\\.60.*AUROC\\|AUROC.*0\\.60[0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-23T19:54:33.863440+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:12:abstract_algebra.48,abstract_algebra,2.466768333180177,1.508961855467561e-08,0.0048722103756387,0.1212874694607827,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:44:astronomy.108,astronomy,-2.7228792655444702,0.0,0.0003511713887087,0.0637095357438932,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:49:astronomy.127,astronomy,1.6715799700101537,9.752019077291509e-05,0.0040192089493238,0.057963840232507,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:52:astronomy.134,astronomy,1.9909508361067003,0.0001642125592448,0.0184795327085638,0.1702069094535672,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:57:astronomy.61,astronomy,-1.6151159966883142,1.12932462525972e-06,0.0397063858617858,0.2745269757314703,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:63:business_ethics.20,business_ethics,-2.3223606986396383,1.15523191013267e-09,0.0014147346210598,0.076142830769144,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:80:business_ethics.8,business_ethics,1.726192531383123,3.192178665045731e-05,0.04650614624433,0.2819046528180212,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_
…[truncated 3697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 422 · 2026-05-23T19:54:33.863568+00:00_

balanced_dif_results.csv
composition_stats.csv
composition_control.py
composition_control_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 423 · 2026-05-23T19:54:33.863715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Let me also check if the paper might have used different quartile groupings that yield ~2600\n# 5227 models / 4 = ~1307 per quartile; Q1 = 1307, Q4 = 1307 (not ~2600)\n# Maybe using Q1-Q3 vs Q2-Q4? No...\n# Maybe 50th percentile split? 5227/2 = 2613.5 → ~2614 per group\n# Let me check if there's a median split analysis\n\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if 'median' in content.lower() and ('ability' in content.lower() or 'quintile' in content.lower()):\n        if '2600' in content or '2,600' in content or '2614' in content or '2613' in content:\n            print(f)\n\" | head -5\n",
  "description": "Search for median-split ability analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Let me also check if the paper might have used different quartile groupings that yield ~2600\n# 5227 models / 4 = ~1307 per quartile; Q1 = 1307, Q4 = 1307 (not ~2600)\n# Maybe using Q1-Q3 vs Q2-Q4? No...\n# Maybe 50th percentile split? 5227/2 = 2613.5 → ~2614 per group\n# Let me check if there's a median split analysis\n\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if 'median' in content.lower() and ('ability' in content.lower() or 'quintile' in content.lower()):\n        if '2600' in content or '2,600' in content or '2614' in content or '2613' in content:\n            print(f)\n\" | head -5\n",
    "description": "Search for median-split ability analysis"
  }
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-23T19:54:33.863856+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r15_subject_level_rho/subject_level_rho_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 425 · 2026-05-23T19:54:33.863982+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_dif_union/dif_union_report.md",
  "description": "Read r16_dif_union report for 17.7% and 47%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_dif_union/dif_union_report.md",
    "description": "Read r16_dif_union report for 17.7% and 47%"
  }
}
```

</details>

---


### Tool result

_source line 426 · 2026-05-23T19:54:33.864122+00:00_

# R16-SF2: Uniform + Non-uniform DIF Union Size

## Coverage

- **MH-DIF (uniform)**: 12,508 items across 57 subjects
- **LR-DIF (non-uniform)**: 1,787 items across 9 subjects (stratified sample: 3 high-C, 3 medium-C, 3 low-C)
- Analysis restricted to the **1,787 overlapping items**

## DIF Prevalence (N = 1,787)

| DIF Type | Count | % |
|----------|------:|----:|
| Uniform (ETS C) | 522 | 29.2% |
| Non-uniform (BH sig, p < 0.05) | 691 | 38.7% |
| Non-uniform (\|β_int\| ≥ 0.5) | 551 | 30.8% |

## Venn Diagram: Significance Criterion (BH-corrected p < 0.05)

```
              Uniform (ETS C)    Non-uniform (BH sig)
              ┌──────────┐       ┌──────────┐
              │          │       │          │
              │   208    │  314  │   377    │
              │ (11.6%)  │(17.6%)│ (21.1%)  │
              │          │       │          │
              └──────────┘       └──────────┘

Neither: 888 (49.7%)
Union:   899 (50.3%)
Jaccard: 0.349
```

## Venn Diagram: Effect-Size Criterion (|β_int| ≥ 0.5)

```
              Uniform (ETS C)    Non-uniform (|β|≥0.5)
              ┌──────────┐       ┌──────────┐
              │          │       │          │
              │   288    │  234  │   317    │
              │ (16.1%)  │(13.1%)│ (17.7%)  │
              │          │       │          │
              └──────────┘       └──────────┘

Neither: 948 (53.0%)
Union:   839 (47.0%)
Jaccard: 0.279
```

## Subject-Level Breakdown

| Subject | N | Unif C | NU sig | NU eff | Union (sig) | Union (eff) |
|---------|--:|-------:|-------:|-------:|------------:|------------:|
| business_ethics | 93 | 45 | 50 | 39 | 62 (67%) | 58 (62%) |
| college_mathematics | 72 | 25 | 41 | 16 | 50 (69%) | 32 (44%) |
| college_medicine | 161 | 46 | 68 | 60 | 82 (51%) | 78 (48%) |
| computer_security | 87 | 18 | 30 | 16 | 38 (44%) | 28 (32%) |
| formal_logic | 109 | 44 | 72 | 54 | 79 (72%) | 67 (61%) |
| human_aging | 203 | 85 | 90 | 62 | 125 (62%) | 113 (56%) |
| management | 92 | 20 | 30 | 25 | 39
…[truncated 1820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-23T19:54:33.864274+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find matching N=638 Cohen's d=-0.17 C%=28.9%\ngrep -rn \"638\\|d.*0.17\\|0.289\\|28.9\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
  "description": "Search for matching analysis stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find matching N=638 Cohen's d=-0.17 C%=28.9%\ngrep -rn \"638\\|d.*0.17\\|0.289\\|28.9\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
    "description": "Search for matching analysis stats"
  }
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-23T19:54:33.864403+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let me just check plan_033 which mentions 2600\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md') as f:\n    content = f.read()\nidx = content.find('2600')\nprint(content[max(0,idx-200):idx+300] if idx >= 0 else 'not found')\n\"\n",
  "description": "Check plan_033 for 2600 reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let me just check plan_033 which mentions 2600\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md') as f:\n    content = f.read()\nidx = content.find('2600')\nprint(content[max(0,idx-200):idx+300] if idx >= 0 else 'not found')\n\"\n",
    "description": "Check plan_033 for 2600 reference"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-23T19:54:33.864546+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/base_instruct_survey.md:82:| 2023-base | 838 | 0.593 | 0.638 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md:73:- **Overlap coefficient** = 0.6638
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md:75:- **Cohen's d** = -0.1729
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md:82:| Overlap coefficient | 0.1786 | 0.6638 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md:83:| Cohen's d | -0.9878 | -0.1729 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_012_report.md:80:| theta_qt_10 | 1.0 | 1.000±0.000 | 0.352±0.015 | +0.638 | inf | 7.85e-38 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/response_letter_draft.md:72:**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_035_report.md:40:| college_medicine | 161 | 4.6 | 0.0417 | 0.0425 | -0.0008 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md:19:| Cohen's d | -0.1729 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_rep
…[truncated 2805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-23T19:54:33.864693+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search for <0.1% variance explained by domain-level accuracy gains\ngrep -rn \"0.042\\|pseudo.*R2\\|variance.*0.1\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/ 2>/dev/null | head -10",
  "description": "Find variance explained in plan_033"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search for <0.1% variance explained by domain-level accuracy gains\ngrep -rn \"0.042\\|pseudo.*R2\\|variance.*0.1\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/ 2>/dev/null | head -10",
    "description": "Find variance explained in plan_033"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-23T19:54:33.864840+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/plan_033_report.md:52:Pseudo R² = 0.0423, N = 12508
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/data/subject_dif_concentration.csv:13:econometrics,Social Science,103,45,22,36,34.95,0.3375,0.2115,0.0426,0.171,0.3592,1.5684,66.67,24.0,12.0,0.0652
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/report/plan_033_report.md:52:Pseudo R² = 0.0423, N = 12508
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:13:econometrics,Social Science,103,45,22,36,34.95,0.3375,0.2115,0.0426,0.171,0.3592,1.5684,66.67,24.0,12.0,0.0652

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 432 · 2026-05-23T19:54:33.864976+00:00_

tio,or_ci_lower,or_ci_upper,p_value
Intercept,0.9108087274128313,0.8188856549312612,1.013050519246203,0.08523388706865416
ctt_difficulty,0.08564518063337925,0.06861451900424628,0.1069029860177293,1.1826004780999362e-104
ctt_discrimination,57.23938812742111,39.38959956939529,83.17798578859369,5.674311442211938e-100
n_items_in_subject,1.0001239466510743,1.0000199645265944,1.0002279395876204,0.019475631746116214


Pseudo R² = 0.0423, N = 12508

**Subject residuals (controlling difficulty + discrimi

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 433 · 2026-05-23T19:54:33.865108+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Also check if Llama-3 count in paper is wrong (paper says 161/308 for llama-2 vs 3)\n# Data shows: Llama-2: 161, Llama-3: 316\n# Paper says 161/308 but actual data shows 316 for Llama-3\nprint('Source data: llama-2 N=161, llama-3 N=316')\nprint('Paper claims: 161/308')\n# 308 vs 316 = difference of 8\n\"\n",
  "description": "Verify Llama family count discrepancy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Also check if Llama-3 count in paper is wrong (paper says 161/308 for llama-2 vs 3)\n# Data shows: Llama-2: 161, Llama-3: 316\n# Paper says 161/308 but actual data shows 316 for Llama-3\nprint('Source data: llama-2 N=161, llama-3 N=316')\nprint('Paper claims: 161/308')\n# 308 vs 316 = difference of 8\n\"\n",
    "description": "Verify Llama family count discrepancy"
  }
}
```

</details>

---


### Tool result

_source line 434 · 2026-05-23T19:54:33.865226+00:00_

Source data: llama-2 N=161, llama-3 N=316
Paper claims: 161/308

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-23T19:54:33.865347+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md | grep -A5 \"N=638\\|d=-0.17\\|p.*0.01\"",
  "description": "Verify matching stats: N=638, d=-0.17, p<0.01"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md | grep -A5 \"N=638\\|d=-0.17\\|p.*0.01\"",
    "description": "Verify matching stats: N=638, d=-0.17, p<0.01"
  }
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-23T19:54:33.865472+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let me check specifically how family is labeled in model_metadata.csv\nimport csv\nllama_families = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if 'llama' in fam:\n            llama_families[fam] = llama_families.get(fam,0) + 1\n\nprint('Llama families:', dict(sorted(llama_families.items())))\n\"\n",
  "description": "Check exact Llama family labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let me check specifically how family is labeled in model_metadata.csv\nimport csv\nllama_families = {}\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if 'llama' in fam:\n            llama_families[fam] = llama_families.get(fam,0) + 1\n\nprint('Llama families:', dict(sorted(llama_families.items())))\n\"\n",
    "description": "Check exact Llama family labels"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-23T19:54:33.865588+00:00_

Llama families: {'codellama': 10, 'llama-1': 5, 'llama-2': 161, 'llama-3': 315, 'llama-3.2': 1, 'tinyllama': 5}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 438 · 2026-05-23T19:54:33.865699+00:00_

**Mean matched: N=638, d=-0.0096, C%=28.9 ± 0.1%**

NN matching achieves near-zero ability difference (d ≈ -0.010) while retaining 79% of the focal cohort. C% drops from 31.3% to 28.9%, a 7.7% relative reduction.

### 2d. P10–P90 Common Support (Sensitivity Check)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-23T19:54:33.865853+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check p<0.01 claim for matching C% reduction — look for p-value\ngrep -n \"p.*0.01\\|<0.01\\|matched.*C%\\|C%.*matched\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md | head -20",
  "description": "Find p-value for ability matching result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check p<0.01 claim for matching C% reduction — look for p-value\ngrep -n \"p.*0.01\\|<0.01\\|matched.*C%\\|C%.*matched\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md | head -20",
    "description": "Find p-value for ability matching result"
  }
}
```

</details>

---


### Tool result

_source line 440 · 2026-05-23T19:54:33.865982+00:00_

60:| Seed | N matched | Cohen's d | C% |
68:**Mean matched: N=638, d=-0.0096, C%=28.9 ± 0.1%**
99:| Ability-matched C% | 28.3 ± 1.6 | 28.9 ± 0.1 | — |
110:4. The convergence of matched C% between comparisons (~28–29%) despite vastly different unmatched C% (61.3% vs 31.3%) suggests a shared baseline of genuine item-level DIF, with the Llama comparison carrying substantial additional ability confound.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-23T19:54:33.866113+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check random split 2024 =1.3% and 2023=0.62% source\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md",
  "description": "Read random split report for 0.62% and 1.3%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check random split 2024 =1.3% and 2023=0.62% source\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md",
    "description": "Read random split report for 0.62% and 1.3%"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-23T19:54:33.866242+00:00_

# Random-Split |Δ_MH| Null Distribution Report

## Setup
- Cohort: 2023 models (N = 1080)
- Items: J = 12508
- Splits: 100 random permutations (each 540 ref vs 540 foc)
- Strata: 5 total-score quantile bins
- Total (item × split) observations: 1,250,800
- Runtime: 2.5s

## Null Distribution Percentiles

| Percentile | |Δ_MH| |
|------------|--------|
| 50th | 0.2956 |
| 90th | 0.7911 |
| 95th | 0.9898 |
| 97.5th | 1.1874 |
| 99th | 1.4504 |
| 99.5th | 1.6536 |
| 99.9th | 2.1998 |

## ETS Threshold Comparison

- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): 0.048206 (4.8206%)
- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): 0.008480 (0.8480%)
- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: 3717 / 12508 (29.72%)

### ETS C Classification (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05)

- Mean null C% per split: 0.6247%
- C% range across splits: [0.0640%, 5.8523%]
- Fraction of (item, split) classified C: 0.006247 (0.6247%)
- Items classified C in at least one split: 3702 / 12508 (29.60%)

## Interpretation

**P95 = 0.9898** (vs ETS B = 1.0): under random splitting, ~5% of item-level |Δ_MH| values approach B-level magnitude purely by chance.

**P99 = 1.4504** (vs ETS C = 1.5): the null 99th percentile nearly reaches the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.

**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the baseline false-positive rate for interpreting these observed rates.

The 99th percentile (1.4504) and 99.9th percentile (2.1998) provide upper bounds on chance-level |Δ_MH| fluctuations.

## Distribution Shape

- Mean |Δ_MH| across all observations: 0.3740
- Median |Δ_MH|: 0.2956
- Std dev: 0.3205
- Skewness: 1.7897
- Max observed: 6.2475

The null distribution is right-skewed with most mass concentrated near zero, consistent with well-behaved random assign
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-23T19:54:33.866373+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 3
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-23T19:54:33.866499+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Look for 2024 random split 1.3% separately — check plan_001 report notes it as ~1.3%\ngrep -n \"1.3\\|2024.*random\\|random.*2024\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md | head -10",
  "description": "Find 2024 random split 1.3% source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Look for 2024 random split 1.3% separately — check plan_001 report notes it as ~1.3%\ngrep -n \"1.3\\|2024.*random\\|random.*2024\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md | head -10",
    "description": "Find 2024 random split 1.3% source"
  }
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-23T19:54:33.866635+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "AUROC.*0\\.60\\|0\\.60.*AUROC\\|Mean.*AUROC.*0\\.60\\|0\\.6026\\|0\\.5994",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "AUROC.*0\\.60\\|0\\.60.*AUROC\\|Mean.*AUROC.*0\\.60\\|0\\.6026\\|0\\.5994",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-23T19:54:33.866790+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-23T19:54:33.866905+00:00_

14:| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
16:| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
27:- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
48:| professional_law | 1331 | 498 | 37.4% | 0.438 | 0.454 | +0.016 |
54:| econometrics | 103 | 36 | 35.0% | 0.425 | 0.482 | +0.057 |
63:| all | 12508 | 3918 | 31.32% |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-23T19:54:33.867028+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check plan_001b for 2024 random split\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/ 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/*.md 2>/dev/null | head -60",
  "description": "Check plan_001b for 2024 random split"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check plan_001b for 2024 random split\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/ 2>/dev/null && cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/*.md 2>/dev/null | head -60",
    "description": "Check plan_001b for 2024 random split"
  }
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-23T19:54:33.867157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# So Llama-3 breakdown: 315 (labeled 'llama-3') + 1 (labeled 'llama-3.2') = 316\n# But for the comparison, the paper uses 308\n# Let's check the within_family_dif.csv to see what groups were actually used\n\n# The within_family_dif data shows 12508 rows per family comparison\n# Need to find which models are in each group\n# Let me check plan_001_report.md more carefully\n# It says: 'llama-2 vs llama-3: A=2718, B=2118, C=7672 (61.34%)'\n# And total items = 12508\n\n# Now check the actual N for llama-2 vs llama-3 in the within_family file\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv') as f:\n    lines = f.readlines()\n    print(lines[0])  # header\n    print(lines[1])  # first row\n    print(f'Total rows: {len(lines)-1}')\n# The N_ref/N_focal would be in the ref_group/foc_group context\n# But the CSV has items, not models\n# We need a separate source for model counts\n\n# Let me look at r14 or plan_001 report for exact N counts\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md') as f:\n    print(f.read()[:2000])\n\"\n",
  "description": "Check within_family_report for N counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# So Llama-3 breakdown: 315 (labeled 'llama-3') + 1 (labeled 'llama-3.2') = 316\n# But for the comparison, the paper uses 308\n# Let's check the within_family_dif.csv to see what groups were actually used\n\n# The within_family_dif data shows 12508 rows per family comparison\n# Need to find which models are in each group\n# Let me check plan_001_report.md more carefully\n# It says: 'llama-2 vs llama-3: A=2718, B=2118, C=7672 (61.34%)'\n# And total items = 12508\n\n# Now check the actual N for llama-2 vs llama-3 in the within_family file\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv') as f:\n    lines = f.readlines()\n    print(lines[0])  # header\n    print(lines[1])  # first row\n    print(f'Total rows: {len(lines)-1}')\n# The N_ref/N_focal would be in the ref_group/foc_group context\n# But the CSV has items, not models\n# We need a separate source for model counts\n\n# Let me look at r14 or plan_001 report for exact N counts\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md') as f:\n    print(f.read()[:2000])\n\"\n",
    "description": "Check within_family_report for N counts"
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-23T19:54:33.867293+00:00_

item_id,subject,ref_group,foc_group,alpha_mh,delta_mh,se,p_value,ets_class,li_label,li_contamination_type

abstract_algebra.1,abstract_algebra,llama-2,llama-3,0.6333632465849038,1.073271254578906,0.7329806938418083,0.18029453590428224,B,False,clean

Total rows: 25016
# Plan 024: Within-Family Deep Dive — Llama-2 vs Llama-3

## Part 1: Llama-2 vs Llama-3

### Score Distributions

| Metric | Llama-2 (N=161) | Llama-3 (N=315) |
|--------|------------|------------|
| Mean accuracy | 0.5269 | 0.6475 |
| SD | 0.1135 | 0.1262 |
| Median | 0.5250 | 0.6813 |

- **KL(Llama-2 || Llama-3)** = 7.9344
- **KL(Llama-3 || Llama-2)** = 4.8091
- **Overlap coefficient** = 0.1786
- **Mann-Whitney U** = 10282, p = 2.48e-26
- **Cohen's d** = -0.9878

### Unmatched MH-DIF

- A% = 21.7%, B% = 16.9%, **C% = 61.3%**

### Ability-Matched MH-DIF (Quintile Matching, 5 Seeds)

| Seed | N matched | C% | B% |
|------|-----------|-----|-----|
| 0 | 75 | 29.5 | 39.0 |
| 1 | 75 | 29.7 | 43.4 |
| 2 | 75 | 28.6 | 41.6 |
| 3 | 75 | 27.9 | 43.0 |
| 4 | 75 | 25.7 | 43.1 |

**Mean matched C% = 28.3 ± 1.6** (vs unmatched 61.3%)

**Interpretation:** Matched C% (28.3%) is substantially lower than unmatched (61.3%), indicating ability confound is a major contributor to the observed DIF.

### Per-Subject C% (Top 10, Unmatched)

| Subject | N items | N C | C% |
|---------|---------|-----|-----|
| world_religions | 159 | 124 | 78.0 |
| marketing | 225 | 174 | 77.3 |
| us_foreign_policy | 96 | 73 | 76.0 |
| high_school_world_history | 225 | 168 | 74.7 |
| management | 92 | 68 | 73.9 |
| high_school_government_and_politics | 189 | 137 | 72.5 |
| miscellaneous | 745 | 538 | 72.2 |
| computer_security | 87 | 61 | 70.1 |
| high_school_european_history | 155 | 108 | 69.7 |
| high_school_us_history | 196 | 136 | 69.4 |

## Part 2: Other Family Pairs (Descriptive Only)

| Pair | N_a | N_b | Mean_a | Mean_b | Overlap | Cohen's d | Underpowered |
|------|-----|-----|--------|--------|---------|-----------|-------------|
| p
…[truncated 268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-23T19:54:33.867450+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.6026\\|0\\.5994\\|Best model AUROC\\|abandon.*AUROC\\|AUROC.*abandon",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.6026\\|0\\.5994\\|Best model AUROC\\|abandon.*AUROC\\|AUROC.*abandon",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-23T19:54:33.867569+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-23T19:54:33.867692+00:00_

data
dif_results_merged.csv
dif_results_per_quintile.csv
enrichment_summary.csv
plan_001b_analysis.py
plan_001b_report.md
quintile_cohort_sizes.csv
report
# Plan 001b: Matched-Ability DIF Analysis

## Background
plan_001 found temporal cohort MH-DIF (2023 vs 2024) produced 31.3% ETS C items but enrichment=0.96,
indicating DIF captured ability improvement rather than contamination. This analysis controls for
ability by running temporal DIF within each accuracy quintile.

## Quintile Cohort Sizes

| Quintile | N(2023) | N(2024) | Total | Underpowered |
|----------|---------|---------|-------|--------------|
| 1 | 180 | 162 | 342 | no |
| 2 | 406 | 106 | 512 | no |
| 3 | 287 | 168 | 455 | no |
| 4 | 88 | 197 | 285 | no |
| 5 | 119 | 174 | 293 | no |

## Per-Quintile DIF Results

- **Q1**: 1809 C items (14.5%), FPR=0.1477, enrichment=1.04
- **Q2**: 4297 C items (34.4%), FPR=0.3524, enrichment=0.94
- **Q3**: 5311 C items (42.5%), FPR=0.4255, enrichment=0.97
- **Q4**: 4305 C items (34.4%), FPR=0.3460, enrichment=0.99
- **Q5**: 3772 C items (30.2%), FPR=0.3059, enrichment=0.96

## Merged Results (threshold: ≥2 quintiles flagged C)

- Items flagged: 5938 / 12508 (47.5%)
- FPR (clean items): 0.4764
- Detection rate (contaminated): 0.4658
- Detection rate (unlabeled): 0.4819
- **Enrichment: 0.98**

## Comparison with plan_001

| Metric | plan_001 (raw temporal) | plan_001b (matched-ability) |
|--------|------------------------|-----------------------------|
| C% | 31.3% | 47.5% |
| Enrichment | 0.96 | 0.98 |
| FPR | ~0.31 | 0.4764 |

## Sensitivity Analysis

| Method | N(C) | C% | FPR | Rate(contam) | Enrichment |
|--------|------|----|-----|-------------|------------|
| >=  1 | 9163 | 73.3% | 0.7362 | 0.7191 | 0.98 |
| >=  2 | 5938 | 47.5% | 0.4764 | 0.4658 | 0.98 |
| >=  3 | 3182 | 25.4% | 0.2613 | 0.2508 | 0.96 |
| CMH | 4165 | 33.3% | 0.3340 | 0.3336 | 1.00 |
| Q1_only | 1809 | 14.5% | 0.1477 | 0.1536 | 1.04 |
| Q2_only | 4297 | 34.4% | 0.3524 | 0.3303 | 0.94 |
| Q3_only 
…[truncated 225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-23T19:54:33.867870+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check ≥24× claim: 31.3% / 0.62% ≈ 50× and 31.3% / 1.3% ≈ 24× — both below temporal C%\npython3 -c \"print(f'2023: {31.3/0.62:.0f}x'); print(f'2024: {31.3/1.3:.0f}x')\"",
  "description": "Verify ≥24× below temporal C% claim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check ≥24× claim: 31.3% / 0.62% ≈ 50× and 31.3% / 1.3% ≈ 24× — both below temporal C%\npython3 -c \"print(f'2023: {31.3/0.62:.0f}x'); print(f'2024: {31.3/1.3:.0f}x')\"",
    "description": "Verify ≥24× below temporal C% claim"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-23T19:54:33.868007+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"0.6026\\|0.5994\\|Best model\\|AUROC\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model/phase2_results.md | head -20",
  "description": "Search phase2_results.md for AUROC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"0.6026\\|0.5994\\|Best model\\|AUROC\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/predictive_model/phase2_results.md | head -20",
    "description": "Search phase2_results.md for AUROC"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-23T19:54:33.868141+00:00_

44:| Fold | AUROC | F1 | Precision | Recall |
51:| **Mean** | **0.6026 ± 0.0203** | **0.0092 ± 0.0147** | **0.4468 ± 0.3703** | **0.0047 ± 0.0076** |
55:| Fold | AUROC | F1 | Precision | Recall |
66:| Fold | AUROC | F1 | Precision | Recall |
73:| **Mean** | **0.5994 ± 0.0258** | **0.1798 ± 0.0322** | **0.4291 ± 0.0397** | **0.1147 ± 0.0260** |
79:| Model | Mean AUROC |
82:| LR Full (23 features) | 0.6026 +/- 0.0203 |
83:| LightGBM (23 features) | 0.5994 +/- 0.0258 |
85:AUROC improvement over baseline: LR +0.0218, GBM +0.0186
108:Best model AUROC (GBM): **0.5994**
110:**Abandon recommendation** — AUROC < 0.65, predictive model not viable for paper inclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-23T19:54:33.868264+00:00_

2023: 50x
2024: 24x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-23T19:54:33.868387+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find p=0.88 for chi-squared test comparing DIF flags vs web-overlap\ngrep -rn \"p.*0.88\\|0.88.*p\\|chi.*sq\\|chisq\\|fisher.*p\\|p.*fisher\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | grep -v \".py:\" | head -20",
  "description": "Find p=0.88 test stat source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find p=0.88 for chi-squared test comparing DIF flags vs web-overlap\ngrep -rn \"p.*0.88\\|0.88.*p\\|chi.*sq\\|chisq\\|fisher.*p\\|p.*fisher\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null | grep -v \".py:\" | head -20",
    "description": "Find p=0.88 test stat source"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-23T19:54:33.868515+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:98:anatomy.103,anatomy,llama-2,llama-3,0.26371308016877637,3.132299923323022,0.8806257198741813,7.988248338275383e-05,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:163:anatomy.45,anatomy,llama-2,llama-3,13.973494117475735,-6.197331305776463,0.8809579446616386,1.1102230246251565e-16,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:183:anatomy.66,anatomy,llama-2,llama-3,9.890109890109889,-5.385107853497533,1.2938101085822438,2.1047142484076353e-05,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:191:anatomy.73,anatomy,llama-2,llama-3,0.1269114227327179,4.851024852447667,0.8831427039270544,4.241620832345916e-09,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:195:anatomy.8,anatomy,llama-2,llama-3,0.7803887488276445,0.5827132556805152,0.6989563084435246,0.4806683804865347,A,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:196:anatomy.80,anatomy,llama-2,llama-3,6.027027027027026,-4.221196568217351,0.9441283557088886,6.620619490194102e-06,C,True,input_only
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:210:anatomy.94,anatomy,llama-2,llama-3,9.890109890109889,-5.385107853497533,1.2938101085822438,2.1047142484076353e-05,C,True,input_and_label
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/within_family_dif.csv:214:anatomy.99,anatomy,llama-2,llama-3,0.998511
…[truncated 3422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-23T19:54:33.868660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"29.2\\|29\\.2\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -20",
  "description": "Search experiments.tex for 29.2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"29.2\\|29\\.2\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -20",
    "description": "Search experiments.tex for 29.2"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-23T19:54:33.868804+00:00_

16:We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift $= {+}1.77$\,pp (\Cref{app:deff}). Under 100 random permutations within the 2023 cohort (540 vs.\ 540), the 99th percentile of item-level $|\Delta_{\mathrm{MH}}|$ is 1.45---just below the ETS~C threshold of 1.5---confirming that the threshold maintains a per-item false-positive rate below 1\%; together with the Monte Carlo power analysis (TPR $\geq 0.68$; \Cref{sec:validation}), this validates ETS~C classification for the LLM setting. No single family drives the signal (LOFO $|\Delta\mathrm{C\%}| \leq 2.93$\,pp); graduated de-duplication confirms C\% scales with power, not redundancy (\Cref{app:dedup_k}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-23T19:54:33.868940+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"29.2\\|C%.*DEFF\\|DEFF.*C%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -20",
  "description": "Check experiments.tex for DEFF C% 29.2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"29.2\\|C%.*DEFF\\|DEFF.*C%\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex | head -20",
    "description": "Check experiments.tex for DEFF C% 29.2"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-23T19:54:33.869060+00:00_

16:We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.4\%, 38.1\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$, upper bound driven by mega-family over-representation; \Cref{app:uncertainty}). Two design-effect (DEFF) estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean DEFF yields 13.5\%, bracketing temporal C\% at 13.5--29.2\%. The cluster bootstrap 95\% CI ($[26.7\%, 53.2\%]$)---a family-level resampling method independent of DEFF methodology---excludes the weighted-mean estimate (13.5\%), providing model-independent evidence that over-correction drives the lower bound. Under weighted-mean DEFF (C\% $= 13.5\%$), all downstream conclusions hold: $\rho = 0.999$, score shift $= {+}1.77$\,pp (\Cref{app:deff}). Under 100 random permutations within the 2023 cohort (540 vs.\ 540), the 99th percentile of item-level $|\Delta_{\mathrm{MH}}|$ is 1.45---just below the ETS~C threshold of 1.5---confirming that the threshold maintains a per-item false-positive rate below 1\%; together with the Monte Carlo power analysis (TPR $\geq 0.68$; \Cref{sec:validation}), this validates ETS~C classification for the LLM setting. No single family drives the signal (LOFO $|\Delta\mathrm{C\%}| \leq 2.93$\,pp); graduated de-duplication confirms C\% scales with power, not redundancy (\Cref{app:dedup_k}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-23T19:54:33.869199+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md",
  "description": "Read plan_001_real_data report for p=0.88 Fisher test"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md",
    "description": "Read plan_001_real_data report for p=0.88 Fisher test"
  }
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-23T19:54:33.869329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# The within_family_report.md says Llama-2 N=161, Llama-3 N=315\n# The model_metadata.csv shows 315 (llama-3) + 1 (llama-3.2) = 316 total \n# But plan_024 report explicitly uses N=315 for Llama-3 (excludes llama-3.2)\n# So the within-family comparison uses 161/315, paper says 161/308\n\n# 315 vs 308 = difference of 7\n# Let me verify by checking the actual plan script\npython_check = '''\nimport csv\nref_models = []\nfoc_models = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if fam == 'llama-2':\n            ref_models.append(row['model_name'])\n        elif fam == 'llama-3':\n            foc_models.append(row['model_name'])\nprint(f'Llama-2: {len(ref_models)}, Llama-3: {len(foc_models)}')\n'''\nprint(python_check)\n\" \npython3 -c \"\nimport csv\nref_models = []\nfoc_models = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if fam == 'llama-2':\n            ref_models.append(row['model_name'])\n        elif fam == 'llama-3':\n            foc_models.append(row['model_name'])\nprint(f'Llama-2: {len(ref_models)}, Llama-3: {len(foc_models)}')\n\"\n",
  "description": "Count exact Llama-2 and Llama-3 models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# The within_family_report.md says Llama-2 N=161, Llama-3 N=315\n# The model_metadata.csv shows 315 (llama-3) + 1 (llama-3.2) = 316 total \n# But plan_024 report explicitly uses N=315 for Llama-3 (excludes llama-3.2)\n# So the within-family comparison uses 161/315, paper says 161/308\n\n# 315 vs 308 = difference of 7\n# Let me verify by checking the actual plan script\npython_check = '''\nimport csv\nref_models = []\nfoc_models = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if fam == 'llama-2':\n            ref_models.append(row['model_name'])\n        elif fam == 'llama-3':\n            foc_models.append(row['model_name'])\nprint(f'Llama-2: {len(ref_models)}, Llama-3: {len(foc_models)}')\n'''\nprint(python_check)\n\" \npython3 -c \"\nimport csv\nref_models = []\nfoc_models = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        fam = row.get('family','').lower()\n        if fam == 'llama-2':\n            ref_models.append(row['model_name'])\n        elif fam == 'llama-3':\n            foc_models.append(row['model_name'])\nprint(f'Llama-2: {len(ref_models)}, Llama-3: {len(foc_models)}')\n\"\n",
    "description": "Count exact Llama-2 and Llama-3 models"
  }
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-23T19:54:33.869456+00:00_

import csv
ref_models = []
foc_models = []
with open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fam = row.get('family','').lower()
        if fam == 'llama-2':
            ref_models.append(row['model_name'])
        elif fam == 'llama-3':
            foc_models.append(row['model_name'])
print(f'Llama-2: {len(ref_models)}, Llama-3: {len(foc_models)}')

Llama-2: 161, Llama-3: 315

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-23T19:54:33.869586+00:00_

# Plan 001: METABENCH Real-Data MH-DIF Analysis

## 1. Data & Setup

- Response matrix: **5227 models × 12508 items** (binary, MMLU)
- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
- Li et al. annotations: 9229 annotated items

## 2. ETS Classification

| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
|--------|--------|-------|---|---|---|----|-------------|------------|
| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |

## 3. Li et al. Proxy Validation

| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
|--------|-------------|---------------|--------------|------------------|------------|
| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |

## 4. Within-Family Analysis

- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)

### Cross-cohort vs within-family overlap

- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804

## 5. Domain Specificity

Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)

Top 15 subjects by C rate (temporal cohort):

| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
|---------|-------|---|-----|----------|----------|------|
| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
| professional_medicine | 248 | 94 | 37.9% | 0.595 | 0.630 | +0.035 |
| professional_law | 1331 | 498 | 37.4% | 0.438 | 0.454 | 
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-23T19:54:33.869759+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find ρ=0.999 (score shift) and +1.77pp under weighted-mean DEFF\ngrep -rn \"1.77\\|0.999\\|rho.*0.999\\|score.*shift\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
  "description": "Find DEFF downstream ρ=0.999 and score shift +1.77pp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find ρ=0.999 (score shift) and +1.77pp under weighted-mean DEFF\ngrep -rn \"1.77\\|0.999\\|rho.*0.999\\|score.*shift\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -20",
    "description": "Find DEFF downstream ρ=0.999 and score shift +1.77pp"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-23T19:54:33.869903+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:20:| Mean score shift (pp) | +2.116 | +1.772 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:31:3. **Score shift positive & cohort-differential**: 2024 shift = +1.800 pp, 2023 shift = +1.900 pp, differential = -0.101 pp. Both cohorts see positive score shifts (DIF items are harder on average); the small negative differential shrinks from -0.291 to -0.101 pp under DEFF correction, approaching zero. Direction is consistent across methods. ✓ Conclusion holds.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:37:All three qualitative conclusions — (1) temporal DIF exists at rates far exceeding null expectation, (2) model rankings are near-perfectly preserved, and (3) both cohorts show positive score shifts with a near-zero cohort differential — remain robust under weighted-mean DEFF correction. The correction reduces C-flagged items by 57% (3918 → 1690), yielding a more conservative but directionally identical picture.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step1_report.md:69:| 1177 | +4.286 | 1.738 | 9.08e-03 | C |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/score_inflation_report.md:31:- Original vs adjusted: ρ = 0.999759
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/score_inflation_report.md:88:Removing the 3918 DIF-C items (31.3% of all items) shifts model scores by an average of +2.12 pp overall. The direction of this shift differs by cohort: 2023 models see a mean change of +2.35 pp while 2024 models see +2.06 pp (differential: -0.29 pp).
/home/ubuntu/.agent-ml-research
…[truncated 3133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-23T19:54:33.870057+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md",
  "description": "Read weighted_mean_downstream for ρ=0.999 and +1.77pp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md",
    "description": "Read weighted_mean_downstream for ρ=0.999 and +1.77pp"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-23T19:54:33.870192+00:00_

# R17 Task 1: Weighted-mean DEFF Downstream Analysis

## Setup

- **Response matrix**: 5227 models × 12508 items
- **Uncorrected C items**: 3918 (31.3%)
- **Weighted-mean C items**: 1690 (13.5%)
- **2023 cohort**: 1080 models
- **2024 cohort**: 807 models

## Comparison Table

| Metric | Uncorrected (3918 C) | Weighted-mean (1690 C) |
|--------|---------------------:|----------------------:|
| ρ (Spearman) | 0.996455 | 0.998811 |
| τ (Kendall) | 0.959986 | 0.978450 |
| Flip rate | 0.0200 | 0.0108 |
| Avg |rank disp| | 74.67 | 39.36 |
| Max |rank disp| | 847 | 846 |
| Mean score shift (pp) | +2.116 | +1.772 |
| 2023 mean shift (pp) | +2.351 | +1.900 |
| 2024 mean shift (pp) | +2.060 | +1.800 |
| Cohort differential (pp) | -0.291 | -0.101 |

## Qualitative Conclusions

1. **Temporal DIF exists**: weighted-mean C% = 13.5% (vs. 31.3% uncorrected). Even after DEFF correction deflates the test statistic, 13.5% of items still exceed ETS category C thresholds — well above the ~5% null expectation. ✓ Conclusion holds.

2. **Ranks preserved**: ρ = 0.998811, τ = 0.978450. Near-perfect rank stability under both methods. ✓ Conclusion holds.

3. **Score shift positive & cohort-differential**: 2024 shift = +1.800 pp, 2023 shift = +1.900 pp, differential = -0.101 pp. Both cohorts see positive score shifts (DIF items are harder on average); the small negative differential shrinks from -0.291 to -0.101 pp under DEFF correction, approaching zero. Direction is consistent across methods. ✓ Conclusion holds.

4. **Effect magnitude**: all downstream effects are attenuated under weighted-mean correction (fewer items removed → smaller perturbation), but the direction and statistical significance are unchanged. The DEFF correction makes the analysis more conservative without reversing any finding.

## Summary

All three qualitative conclusions — (1) temporal DIF exists at rates far exceeding null expectation, (2) model rankings are near-perfectly preserved, and (3) both cohorts show positive
…[truncated 230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-23T19:54:33.870341+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find p=0.88 for Li2024 enrichment test - from plan_001 analysis.py \ngrep -n \"0.88\\|fisher\\|chi2\\|p_value\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py | head -20",
  "description": "Search for p=0.88 in plan_001 analysis script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find p=0.88 for Li2024 enrichment test - from plan_001 analysis.py \ngrep -n \"0.88\\|fisher\\|chi2\\|p_value\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py | head -20",
    "description": "Search for p=0.88 in plan_001 analysis script"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-23T19:54:33.870464+00:00_

28:from scipy.stats import chi2 as chi2_dist, spearmanr
81:    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
179:            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
180:            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
182:            chi2_stat = pval = np.nan
197:                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
206:                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
461:                "p_value", "ets_class", "li_label", "li_contamination_type"]
470:                   "alpha_mh", "delta_mh", "se", "p_value", "ets_class",

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-23T19:54:33.870608+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# From experiments.tex: MMLU random baseline = 0.62% (2023 cohort, 100 permutations)\n# discussion.tex says: C% exceeds 20× random-split baseline (C%≈12% for MMLU)\n# 20 × 0.62% = 12.4% ≈ 12%\n# This checks out if using the 2023 random split baseline\n\n# Also check: if using larger group baseline from r15:\n# \"Random baseline (large groups): 0.10%\"\n# 20 × 0.10% = 2.0% — does NOT yield 12%\n\n# The 12% derives from: 20 × 0.62% = 12.4%\n# Or perhaps: threshold at 20× baseline means if C% > 12%, it's flagged\n# 31.3% / 0.62% = 50.5× (actual ratio), 31.3% / 1.3% ≈ 24× (as stated in experiments.tex \"≥24× below\")\n# The protocol says \"20× baseline\" as a threshold; if baseline=0.62%, then 20×=12.4%≈12%\necho \"20 * 0.62 = $(python3 -c 'print(20*0.62)')\"\necho \"31.3 / 0.62 = $(python3 -c 'print(31.3/0.62)')\"\necho \"Expected: 20x threshold = 12.4%, described as ~12%\"",
  "description": "Verify 20x baseline calculation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# From experiments.tex: MMLU random baseline = 0.62% (2023 cohort, 100 permutations)\n# discussion.tex says: C% exceeds 20× random-split baseline (C%≈12% for MMLU)\n# 20 × 0.62% = 12.4% ≈ 12%\n# This checks out if using the 2023 random split baseline\n\n# Also check: if using larger group baseline from r15:\n# \"Random baseline (large groups): 0.10%\"\n# 20 × 0.10% = 2.0% — does NOT yield 12%\n\n# The 12% derives from: 20 × 0.62% = 12.4%\n# Or perhaps: threshold at 20× baseline means if C% > 12%, it's flagged\n# 31.3% / 0.62% = 50.5× (actual ratio), 31.3% / 1.3% ≈ 24× (as stated in experiments.tex \"≥24× below\")\n# The protocol says \"20× baseline\" as a threshold; if baseline=0.62%, then 20×=12.4%≈12%\necho \"20 * 0.62 = $(python3 -c 'print(20*0.62)')\"\necho \"31.3 / 0.62 = $(python3 -c 'print(31.3/0.62)')\"\necho \"Expected: 20x threshold = 12.4%, described as ~12%\"",
    "description": "Verify 20x baseline calculation"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-23T19:54:33.870757+00:00_

20 * 0.62 = 12.4
31.3 / 0.62 = 50.483870967741936
Expected: 20x threshold = 12.4%, described as ~12%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-23T19:54:33.870896+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Now let me check the enrichment for matched ability quintile (Table 2 value of 0.94-1.04)\npython3 -c \"\n# From plan_001b: per-quintile enrichments were: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96\n# Range: 0.94-1.04 - this matches paper's 'Enrich. 0.94-1.04'\nprint('plan_001b enrichment per quintile: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96')\nprint('Range: 0.94-1.04 MATCHES paper')\n\n# Check Table 2 theta-conditioning values\n# Paper: theta-cond FPR=0.312, TPR=0.876, r(theta,total)=0.9986\n# plan_012: theta_qt_20 FPR=0.312±0.008, TPR@0.5=0.876\n# plan_012: correlation(theta, total_score) = 0.9986\nprint('theta_qt_20: FPR=0.312, TPR@p=0.5=0.876 MATCHES paper')\nprint('r(theta, total) = 0.9986 MATCHES paper')\n\n# Baseline (ext.) table 2: FPR=0.314±0.009, TPR(p=0.5)=0.834±0.027\n# plan_011 external_5: FPR=0.314±0.009, TPR@0.5=0.834±0.027\nprint('external_5 Baseline: FPR=0.314±0.009, TPR@0.5=0.834±0.027 MATCHES paper')\n\"\n",
  "description": "Verify Table 2 values against source data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Now let me check the enrichment for matched ability quintile (Table 2 value of 0.94-1.04)\npython3 -c \"\n# From plan_001b: per-quintile enrichments were: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96\n# Range: 0.94-1.04 - this matches paper's 'Enrich. 0.94-1.04'\nprint('plan_001b enrichment per quintile: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96')\nprint('Range: 0.94-1.04 MATCHES paper')\n\n# Check Table 2 theta-conditioning values\n# Paper: theta-cond FPR=0.312, TPR=0.876, r(theta,total)=0.9986\n# plan_012: theta_qt_20 FPR=0.312±0.008, TPR@0.5=0.876\n# plan_012: correlation(theta, total_score) = 0.9986\nprint('theta_qt_20: FPR=0.312, TPR@p=0.5=0.876 MATCHES paper')\nprint('r(theta, total) = 0.9986 MATCHES paper')\n\n# Baseline (ext.) table 2: FPR=0.314±0.009, TPR(p=0.5)=0.834±0.027\n# plan_011 external_5: FPR=0.314±0.009, TPR@0.5=0.834±0.027\nprint('external_5 Baseline: FPR=0.314±0.009, TPR@0.5=0.834±0.027 MATCHES paper')\n\"\n",
    "description": "Verify Table 2 values against source data"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-23T19:54:33.871024+00:00_

plan_001b enrichment per quintile: Q1=1.04, Q2=0.94, Q3=0.97, Q4=0.99, Q5=0.96
Range: 0.94-1.04 MATCHES paper
theta_qt_20: FPR=0.312, TPR@p=0.5=0.876 MATCHES paper
r(theta, total) = 0.9986 MATCHES paper
external_5 Baseline: FPR=0.314±0.009, TPR@0.5=0.834±0.027 MATCHES paper

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-23T19:54:33.871160+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check the within-subject row in Table 2 - C%=38.1% \n# This should come from plan_014 which shows \"Average within-subject C%: 38.1%\"\n# And it's about plan_016's within-subject matching ΔTPR = +0.257 average at p=0.5\n# The paper says \"Within-subject & Per-subject DIF & -- & -- & C% = 38.1% (>25%)\"\n# This just references plan_014's result\n\n# Now verify the DTPR values referenced in Table 2\n# plan_011: baseline is external_5 (cross-benchmark total score)\n# DTPR at p=0.5 = 0.834 - 0.326 = 0.508\npython3 -c \"\ntpr_baseline = 0.326\ntpr_05 = 0.834\ndtpr = tpr_05 - tpr_baseline\nprint(f'Delta TPR at p=0.5 (ext): {dtpr:.3f}')\n# plan_011 report confirms: baseline TPR=0.326/FPR=0.314, p=0.5 TPR=0.834/FPR=0.314, ΔTPR=+0.508\n\"\n",
  "description": "Verify DTPR calculation from plan_011"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check the within-subject row in Table 2 - C%=38.1% \n# This should come from plan_014 which shows \"Average within-subject C%: 38.1%\"\n# And it's about plan_016's within-subject matching ΔTPR = +0.257 average at p=0.5\n# The paper says \"Within-subject & Per-subject DIF & -- & -- & C% = 38.1% (>25%)\"\n# This just references plan_014's result\n\n# Now verify the DTPR values referenced in Table 2\n# plan_011: baseline is external_5 (cross-benchmark total score)\n# DTPR at p=0.5 = 0.834 - 0.326 = 0.508\npython3 -c \"\ntpr_baseline = 0.326\ntpr_05 = 0.834\ndtpr = tpr_05 - tpr_baseline\nprint(f'Delta TPR at p=0.5 (ext): {dtpr:.3f}')\n# plan_011 report confirms: baseline TPR=0.326/FPR=0.314, p=0.5 TPR=0.834/FPR=0.314, ΔTPR=+0.508\n\"\n",
    "description": "Verify DTPR calculation from plan_011"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-23T19:54:33.871291+00:00_

Delta TPR at p=0.5 (ext): 0.508

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-23T19:54:33.871421+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find p=0.88 for Fisher exact test on DIF vs Li2024 labels\npython3 -c \"\nfrom scipy.stats import chi2_contingency, fisher_exact\n# From plan_001 report:\n# temporal: all items=12508, annotated=9229\n# Rate(contam)=0.3070 = DIF-C rate among web-contaminated items\n# Rate(clean)=0.3184 = DIF-C rate among clean items\n# Need to reconstruct contingency table\n# From mmlu_li2024_proxy_labels.csv \nimport csv\nli_contam_c = 0\nli_contam_nc = 0\nli_clean_c = 0\nli_clean_nc = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        li = row['li_label']\n        ets = row['ets_class']\n        if li == 'True':  # contaminated\n            if ets == 'C':\n                li_contam_c += 1\n            else:\n                li_contam_nc += 1\n        elif li == 'False':  # clean\n            if ets == 'C':\n                li_clean_c += 1\n            else:\n                li_clean_nc += 1\n\nprint(f'Contaminated: C={li_contam_c}, non-C={li_contam_nc}, total={li_contam_c+li_contam_nc}, rate={li_contam_c/(li_contam_c+li_contam_nc):.4f}')\nprint(f'Clean: C={li_clean_c}, non-C={li_clean_nc}, total={li_clean_c+li_clean_nc}, rate={li_clean_c/(li_clean_c+li_clean_nc):.4f}')\nct = [[li_contam_c, li_contam_nc], [li_clean_c, li_clean_nc]]\n_, p, _, _ = chi2_contingency(ct)\nprint(f'chi2 contingency p={p:.3f}')\nOR, fp = fisher_exact(ct)\nprint(f'Fisher exact p={fp:.3f}')\n\"",
  "description": "Compute p=0.88 from DIF vs Li2024 labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find p=0.88 for Fisher exact test on DIF vs Li2024 labels\npython3 -c \"\nfrom scipy.stats import chi2_contingency, fisher_exact\n# From plan_001 report:\n# temporal: all items=12508, annotated=9229\n# Rate(contam)=0.3070 = DIF-C rate among web-contaminated items\n# Rate(clean)=0.3184 = DIF-C rate among clean items\n# Need to reconstruct contingency table\n# From mmlu_li2024_proxy_labels.csv \nimport csv\nli_contam_c = 0\nli_contam_nc = 0\nli_clean_c = 0\nli_clean_nc = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        li = row['li_label']\n        ets = row['ets_class']\n        if li == 'True':  # contaminated\n            if ets == 'C':\n                li_contam_c += 1\n            else:\n                li_contam_nc += 1\n        elif li == 'False':  # clean\n            if ets == 'C':\n                li_clean_c += 1\n            else:\n                li_clean_nc += 1\n\nprint(f'Contaminated: C={li_contam_c}, non-C={li_contam_nc}, total={li_contam_c+li_contam_nc}, rate={li_contam_c/(li_contam_c+li_contam_nc):.4f}')\nprint(f'Clean: C={li_clean_c}, non-C={li_clean_nc}, total={li_clean_c+li_clean_nc}, rate={li_clean_c/(li_clean_c+li_clean_nc):.4f}')\nct = [[li_contam_c, li_contam_nc], [li_clean_c, li_clean_nc]]\n_, p, _, _ = chi2_contingency(ct)\nprint(f'chi2 contingency p={p:.3f}')\nOR, fp = fisher_exact(ct)\nprint(f'Fisher exact p={fp:.3f}')\n\"",
    "description": "Compute p=0.88 from DIF vs Li2024 labels"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-23T19:54:33.871547+00:00_

Contaminated: C=1119, non-C=2526, total=3645, rate=0.3070
Clean: C=1778, non-C=3806, total=5584, rate=0.3184
chi2 contingency p=0.258
Fisher exact p=0.251

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-23T19:54:33.871671+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Verify Jaccard=0.206 for DIF-C vs Li-contaminated overlap\npython3 -c \"\nimport csv\ndif_c = set()\nli_contam = set()\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row['ets_class'] == 'C':\n            dif_c.add(row['item_id'])\n        if row['li_label'] == 'True':\n            li_contam.add(row['item_id'])\nintersection = dif_c & li_contam\nunion = dif_c | li_contam\njaccard = len(intersection)/len(union)\nprint(f'DIF-C: {len(dif_c)}, Li-contam: {len(li_contam)}')\nprint(f'Intersection: {len(intersection)}, Union: {len(union)}')\nprint(f'Jaccard: {jaccard:.3f}')\n\"",
  "description": "Compute Jaccard=0.206 from DIF vs Li2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Verify Jaccard=0.206 for DIF-C vs Li-contaminated overlap\npython3 -c \"\nimport csv\ndif_c = set()\nli_contam = set()\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row['ets_class'] == 'C':\n            dif_c.add(row['item_id'])\n        if row['li_label'] == 'True':\n            li_contam.add(row['item_id'])\nintersection = dif_c & li_contam\nunion = dif_c | li_contam\njaccard = len(intersection)/len(union)\nprint(f'DIF-C: {len(dif_c)}, Li-contam: {len(li_contam)}')\nprint(f'Intersection: {len(intersection)}, Union: {len(union)}')\nprint(f'Jaccard: {jaccard:.3f}')\n\"",
    "description": "Compute Jaccard=0.206 from DIF vs Li2024"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-23T19:54:33.871814+00:00_

DIF-C: 3918, Li-contam: 3645
Intersection: 1119, Union: 6444
Jaccard: 0.174

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-23T19:54:33.871947+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check Table 2 matched-ability row: \"Temp C% ~0.31\"\n# From plan_001b, the per-quintile C% values: 14.5%, 34.4%, 42.5%, 34.4%, 30.2%\n# None of these is ~0.31 (31%)\n# The paper implies matched-ability still yields ~31% C%\n# But plan_001b's merged threshold >= 2 yields 47.5%\n# Individual quintile values range from 14.5-42.5%\n# The ~0.31 might reference a different comparison\n\n# Let me check plan_022 or other matched analyses\npython3 -c \"\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/'\nfor f in os.listdir(base):\n    print(f)\n\"\n",
  "description": "Check r22 composition control files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check Table 2 matched-ability row: \"Temp C% ~0.31\"\n# From plan_001b, the per-quintile C% values: 14.5%, 34.4%, 42.5%, 34.4%, 30.2%\n# None of these is ~0.31 (31%)\n# The paper implies matched-ability still yields ~31% C%\n# But plan_001b's merged threshold >= 2 yields 47.5%\n# Individual quintile values range from 14.5-42.5%\n# The ~0.31 might reference a different comparison\n\n# Let me check plan_022 or other matched analyses\npython3 -c \"\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/'\nfor f in os.listdir(base):\n    print(f)\n\"\n",
    "description": "Check r22 composition control files"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-23T19:54:33.872067+00:00_

balanced_dif_results.csv
composition_stats.csv
composition_control.py
composition_control_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-23T19:54:33.872201+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md') as f:\n    print(f.read()[:3000])\n\"\n",
  "description": "Read r22 composition control report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md') as f:\n    print(f.read()[:3000])\n\"\n",
    "description": "Read r22 composition control report"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-23T19:54:33.872325+00:00_

# R22: Base/Instruct Composition Control

## Motivation

2023 and 2024 cohorts differ in base/instruct model composition:
- 2023: 861 base + 219 instruct (79.7% base)
- 2024: 548 base + 259 instruct (67.9% base)

This 11.8 pp gap could confound temporal MH-DIF if base and instruct
models respond differently. We test this by matched subsampling.

## Method

1. Target base ratio: 67.9% (matching the lower-ratio cohort)
2. Downsample 2023 base models from 861 → 463
3. Re-run 5-stratum MH-DIF with ETS C classification
4. Repeat 10× with different random seeds

## Results

| Metric | Value |
|--------|-------|
| Original C% | 31.32% |
| Balanced C% (mean ± SD) | 30.25% ± 1.32% |
| Balanced C% 95% CI | [27.65%, 32.84%] |
| Δ(original − balanced) | 1.08 pp |

### Per-repetition results

rep,c_pct,n_ref,n_foc,base_pct_ref,base_pct_foc
1,30.860249440358174,682,807,67.88856304985337,67.90582403965304
2,28.27790214262872,682,807,67.88856304985337,67.90582403965304
3,30.244643428205947,682,807,67.88856304985337,67.90582403965304
4,30.204669011832426,682,807,67.88856304985337,67.90582403965304
5,29.525103933482573,682,807,67.88856304985337,67.90582403965304
6,32.65909817716661,682,807,67.88856304985337,67.90582403965304
7,29.90885833066837,682,807,67.88856304985337,67.90582403965304
8,31.371921969939237,682,807,67.88856304985337,67.90582403965304
9,28.437799808122797,682,807,67.88856304985337,67.90582403965304
10,30.972177806204034,682,807,67.88856304985337,67.90582403965304


## Conclusion

Balanced C% remains high (30.2%), confirming that DIF is NOT driven by base/instruct composition shift. The 1.1 pp difference is negligible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-23T19:54:33.872466+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The p=0.88 and Jaccard=0.206 in the paper must use different definitions\n# Check if Jaccard is computed differently (contaminated vs DIF-C only among annotated)\npython3 -c \"\nimport csv\ndif_c_annotated = set()\nli_contam = set()\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row['li_label'] in ('True', 'False'):  # annotated items\n            if row['ets_class'] == 'C':\n                dif_c_annotated.add(row['item_id'])\n            if row['li_label'] == 'True':\n                li_contam.add(row['item_id'])\nintersection = dif_c_annotated & li_contam\nunion = dif_c_annotated | li_contam\njaccard = len(intersection)/len(union)\nprint(f'DIF-C (annotated only): {len(dif_c_annotated)}, Li-contam: {len(li_contam)}')\nprint(f'Intersection: {len(intersection)}, Union: {len(union)}')\nprint(f'Jaccard: {jaccard:.3f}')\n\"",
  "description": "Recompute Jaccard using only annotated items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The p=0.88 and Jaccard=0.206 in the paper must use different definitions\n# Check if Jaccard is computed differently (contaminated vs DIF-C only among annotated)\npython3 -c \"\nimport csv\ndif_c_annotated = set()\nli_contam = set()\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row['li_label'] in ('True', 'False'):  # annotated items\n            if row['ets_class'] == 'C':\n                dif_c_annotated.add(row['item_id'])\n            if row['li_label'] == 'True':\n                li_contam.add(row['item_id'])\nintersection = dif_c_annotated & li_contam\nunion = dif_c_annotated | li_contam\njaccard = len(intersection)/len(union)\nprint(f'DIF-C (annotated only): {len(dif_c_annotated)}, Li-contam: {len(li_contam)}')\nprint(f'Intersection: {len(intersection)}, Union: {len(union)}')\nprint(f'Jaccard: {jaccard:.3f}')\n\"",
    "description": "Recompute Jaccard using only annotated items"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-23T19:54:33.872594+00:00_

DIF-C (annotated only): 2897, Li-contam: 3645
Intersection: 1119, Union: 5423
Jaccard: 0.206

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-23T19:54:33.872738+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# The r22 composition control shows balanced C% ~30.2% but this is composition-balanced, not ability-matched\n# Let me look for the nearest-neighbor matching result \n# Paper also mentions (in experiments text): \"1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9% ± 0.1%\"\n# Let me find the matched-ability ~0.31 source\n\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if ('nearest' in content.lower() or 'match' in content.lower()) and ('28.9' in content or '0.31' in content):\n        print(f)\n\" | head -10\n",
  "description": "Find nearest-neighbor matching source for ability-matched C%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# The r22 composition control shows balanced C% ~30.2% but this is composition-balanced, not ability-matched\n# Let me look for the nearest-neighbor matching result \n# Paper also mentions (in experiments text): \"1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9% ± 0.1%\"\n# Let me find the matched-ability ~0.31 source\n\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    with open(f) as fh:\n        content = fh.read()\n    if ('nearest' in content.lower() or 'match' in content.lower()) and ('28.9' in content or '0.31' in content):\n        print(f)\n\" | head -10\n",
    "description": "Find nearest-neighbor matching source for ability-matched C%"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-23T19:54:33.872873+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/novelty_rebuttal_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_016_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/experiment_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_012_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/bootstrap_dfpr_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-23T19:54:33.873010+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check if p=0.88 is from a different test — maybe odds ratio or enrichment ratio test\n# enrichment = 0.964 = ratio(DIF_rate_contam / DIF_rate_clean) = 0.3070/0.3184 = 0.964\npython3 -c \"print(0.3070/0.3184)\"\n# p=0.88 may be from Fisher test comparing enrichment to 1 or from the Fisher exact test on 2x2 table\n# The computed p was 0.251... let me check if there's another version with different labels\ngrep -n \"p=0.88\\|p.*0.88\\|0.88\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md 2>/dev/null | head -10",
  "description": "Verify enrichment ratio and find p=0.88 source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check if p=0.88 is from a different test — maybe odds ratio or enrichment ratio test\n# enrichment = 0.964 = ratio(DIF_rate_contam / DIF_rate_clean) = 0.3070/0.3184 = 0.964\npython3 -c \"print(0.3070/0.3184)\"\n# p=0.88 may be from Fisher test comparing enrichment to 1 or from the Fisher exact test on 2x2 table\n# The computed p was 0.251... let me check if there's another version with different labels\ngrep -n \"p=0.88\\|p.*0.88\\|0.88\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md 2>/dev/null | head -10",
    "description": "Verify enrichment ratio and find p=0.88 source"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-23T19:54:33.873139+00:00_

0.9641959798994975

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-23T19:54:33.873263+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Also check the r18 base-instruct chi-sq=562.7 source\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/",
  "description": "Check r18_base_vs_instruct_dif directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Also check the r18 base-instruct chi-sq=562.7 source\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/",
    "description": "Check r18_base_vs_instruct_dif directory"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-23T19:54:33.873378+00:00_

base_instruct_dif.py
base_instruct_dif_report.md
base_instruct_item_results.csv
model_classification.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-23T19:54:33.873499+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md') as f:\n    content = f.read()\n# find matching/nearest-neighbor section\nimport re\nidx = content.find('nearest')\nprint(content[max(0,idx-100):idx+500] if idx >= 0 else 'not found')\n\"\n",
  "description": "Check plan_004 step2 for nearest-neighbor matching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md') as f:\n    content = f.read()\n# find matching/nearest-neighbor section\nimport re\nidx = content.find('nearest')\nprint(content[max(0,idx-100):idx+500] if idx >= 0 else 'not found')\n\"\n",
    "description": "Check plan_004 step2 for nearest-neighbor matching"
  }
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-23T19:54:33.873623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md | head -80",
  "description": "Read base vs instruct DIF report for chi-sq=562.7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md | head -80",
    "description": "Read base vs instruct DIF report for chi-sq=562.7"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-23T19:54:33.873755+00:00_

not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-23T19:54:33.873883+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md') as f:\n    content = f.read()\n# Find 28.9 or 0.31 or nearest-neighbor\nfor term in ['28.9', '~0.31', 'nearest', 'matched-ability', 'Matched']:\n    idx = content.find(term)\n    if idx >= 0:\n        print(f'--- Found \\\"{term}\\\" ---')\n        print(content[max(0,idx-100):idx+300])\n        print()\n        break\n\"\n",
  "description": "Check experiment_summary for matched ability C%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md') as f:\n    content = f.read()\n# Find 28.9 or 0.31 or nearest-neighbor\nfor term in ['28.9', '~0.31', 'nearest', 'matched-ability', 'Matched']:\n    idx = content.find(term)\n    if idx >= 0:\n        print(f'--- Found \\\"{term}\\\" ---')\n        print(content[max(0,idx-100):idx+300])\n        print()\n        break\n\"\n",
    "description": "Check experiment_summary for matched ability C%"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-23T19:54:33.874006+00:00_

--- Found "matched-ability" ---
oss model generations. Three independent approaches to reduce the 31% baseline DIF rate all failed (matched-ability, θ-conditioning, within-subject isolation), while semi-synthetic injection validated that the DIF methodology itself works correctly (ΔTPR=+0.674). The project pivoted from "DIF as contamination detector" to "psychometric characterization of LLM benchmark item instability" — the firs

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-23T19:54:33.874132+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Let me check the plan_004 files for matched-ability C%\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/\n",
  "description": "List plan_004 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Let me check the plan_004 files for matched-ability C%\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/\n",
    "description": "List plan_004 directory"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-23T19:54:33.874255+00:00_

bootstrap_ci_report.md
fig_gsm1k_dif_correlation.pdf
fig_gsm1k_dif_correlation.png
fig_gsm1k_dif_perm_null.png
gsm1k_data_report.md
gsm1k_dif_correlation.csv
gsm1k_model_accuracy.csv
gsm8k_dif_results.csv
gsm8k_dose_response.csv
gsm8k_dose_response_summary.csv
gsm8k_ets_summary.csv
intermediate
plan_004_bootstrap_ci.py
plan_004_step1_gsm8k_temporal_dif.py
plan_004_step1_report.md
plan_004_step2_gsm8k_semi_synthetic.py
plan_004_step2_report.md
plan_004_step3_gsm1k_dif_correlation.py
plan_004_step3_report.md
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-23T19:54:33.874383+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport os, glob\n# Search for '~0.31' or 'matched' and '28.9' \nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nmatches = []\nfor f in glob.glob(base + '**/*.md', recursive=True) + glob.glob(base + '**/*.csv', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '28.9' in content:\n            matches.append(f)\n    except:\n        pass\nprint('Files with 28.9:')\nfor m in matches[:10]:\n    print(m)\n\"\n",
  "description": "Search for 28.9% ability-matched C% value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport os, glob\n# Search for '~0.31' or 'matched' and '28.9' \nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nmatches = []\nfor f in glob.glob(base + '**/*.md', recursive=True) + glob.glob(base + '**/*.csv', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '28.9' in content:\n            matches.append(f)\n    except:\n        pass\nprint('Files with 28.9:')\nfor m in matches[:10]:\n    print(m)\n\"\n",
    "description": "Search for 28.9% ability-matched C% value"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-23T19:54:33.874510+00:00_

# R18: Base vs Instruct DIF Separation Experiment

## Sample Sizes

| Group | Ref (2023) | Foc (2024) | Total |
|-------|-----------|-----------|-------|
| Base | 861 | 548 | 1409 |
| Instruct | 219 | 259 | 478 |
| Full (reported) | 1,080 | 807 | 1,887 |

All subgroups have N ≥ 80; adequate power.

## C% Comparison

| Group | C% | DIF-C items |
|-------|-----|------------|
| Base | 32.1% | 4018/12508 |
| Instruct | 36.5% | 4567/12508 |
| Full (reported) | 31.3% | — |

**Difference (base − instruct):** -4.4 pp
**Bootstrap 95% CI:** [-13.4, 4.3] (N=1000)

## Difficulty–Direction Gradient

Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:

- **Base:** ρ = -0.570 (p = 0.00e+00, n = 4018)
- **Instruct:** ρ = -0.079 (p = 1.02e-07, n = 4567)

## DIF Item Overlap

| Metric | Value |
|--------|-------|
| C_base only | 1965 |
| C_instruct only | 2514 |
| Both | 2053 |
| Jaccard index | 0.314 |
| Expected Jaccard (independence) | 0.206 |
| Jaccard / Expected ratio | 1.5× |

## DIF Direction Distribution

| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
|-------|----------------------|---------------------|
| Base | 1605 (39.9%) | 2413 (60.1%) |
| Instruct | 2994 (65.6%) | 1573 (34.4%) |

χ² = 562.70, p = 2.178e-124

## Output Files

- `model_classification.csv` — 1887 models classified
- `base_instruct_item_results.csv` — 12508 items with per-group DIF statistics

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-23T19:54:33.874660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find p=0.88 specifically - might be from a Fisher test within annotated items\npython3 -c \"\nfrom scipy.stats import chi2_contingency, fisher_exact\nimport csv\n\n# Annotated items only — 9229\ndif_c_contam = 0  # DIF-C and contaminated\ndif_c_clean = 0   # DIF-C and clean  \nnon_c_contam = 0  # not DIF-C and contaminated\nnon_c_clean = 0   # not DIF-C and clean\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row['li_label'] in ('True', 'False'):\n            is_c = row['ets_class'] == 'C'\n            is_contam = row['li_label'] == 'True'\n            if is_c and is_contam:\n                dif_c_contam += 1\n            elif is_c and not is_contam:\n                dif_c_clean += 1\n            elif not is_c and is_contam:\n                non_c_contam += 1\n            else:\n                non_c_clean += 1\n\nprint(f'Table: DIF-C/contam={dif_c_contam}, DIF-C/clean={dif_c_clean}, non-C/contam={non_c_contam}, non-C/clean={non_c_clean}')\ntotal_annot = dif_c_contam + dif_c_clean + non_c_contam + non_c_clean\nprint(f'Total annotated: {total_annot}')\n\nct = [[dif_c_contam, non_c_contam], [dif_c_clean, non_c_clean]]\nchi2, p, df, exp = chi2_contingency(ct)\nprint(f'chi2={chi2:.2f}, p={p:.3f}')\nOR, fp = fisher_exact(ct)\nprint(f'Fisher OR={OR:.3f}, p={fp:.3f}')\n\"",
  "description": "Compute Fisher test on DIF vs Li labels for p=0.88"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find p=0.88 specifically - might be from a Fisher test within annotated items\npython3 -c \"\nfrom scipy.stats import chi2_contingency, fisher_exact\nimport csv\n\n# Annotated items only — 9229\ndif_c_contam = 0  # DIF-C and contaminated\ndif_c_clean = 0   # DIF-C and clean  \nnon_c_contam = 0  # not DIF-C and contaminated\nnon_c_clean = 0   # not DIF-C and clean\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_results_temporal.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row['li_label'] in ('True', 'False'):\n            is_c = row['ets_class'] == 'C'\n            is_contam = row['li_label'] == 'True'\n            if is_c and is_contam:\n                dif_c_contam += 1\n            elif is_c and not is_contam:\n                dif_c_clean += 1\n            elif not is_c and is_contam:\n                non_c_contam += 1\n            else:\n                non_c_clean += 1\n\nprint(f'Table: DIF-C/contam={dif_c_contam}, DIF-C/clean={dif_c_clean}, non-C/contam={non_c_contam}, non-C/clean={non_c_clean}')\ntotal_annot = dif_c_contam + dif_c_clean + non_c_contam + non_c_clean\nprint(f'Total annotated: {total_annot}')\n\nct = [[dif_c_contam, non_c_contam], [dif_c_clean, non_c_clean]]\nchi2, p, df, exp = chi2_contingency(ct)\nprint(f'chi2={chi2:.2f}, p={p:.3f}')\nOR, fp = fisher_exact(ct)\nprint(f'Fisher OR={OR:.3f}, p={fp:.3f}')\n\"",
    "description": "Compute Fisher test on DIF vs Li labels for p=0.88"
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-23T19:54:33.874821+00:00_

Table: DIF-C/contam=1119, DIF-C/clean=1778, non-C/contam=2526, non-C/clean=3806
Total annotated: 9229
chi2=1.28, p=0.258
Fisher OR=0.948, p=0.251

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-23T19:54:33.875023+00:00_

I now have everything needed to write the complete audit report.

---

## Discussion §6.1 inline numbers

### Base/instruct DIF separation stats

- **N=1,409 (base models)** ← `r18_base_vs_instruct_dif/base_instruct_dif_report.md` line 6: "Base: Ref=861, Foc=548, Total=1409" ✅
- **60.1% reference-favoring (base)** ← same file, Direction Distribution table: "Base: 2413 (60.1%) ref-favoring" ✅
- **ρ=-0.570 (base)** ← same file, Difficulty–Direction Gradient: "Base: ρ=-0.570 (p=0.00e+00, n=4018)" ✅
- **N=478 (instruct models)** ← same file line 8: "Instruct: Ref=219, Foc=259, Total=478" ✅
- **65.6% focal-favoring (instruct)** ← same file, Direction Distribution: "Instruct: 2994 (65.6%) focal-favoring" ✅
- **ρ=-0.079 (instruct)** ← same file: "Instruct: ρ=-0.079 (p=1.02e-07, n=4567)" ✅
- **χ²=562.7** ← same file: "χ²=562.70, p=2.178e-124" ✅
- **p<10^-124** ← same file: "p=2.178e-124" ✅

### Composition downsampling

- **Δ=1.08pp** ← `r22_composition_control/composition_control_report.md`: "Δ(original − balanced) = 1.08 pp" ✅

### C% and bootstrap CI

- **C%=29.2%** ← This is the **DEFF-adjusted** (simple-mean DEFF) value, sourced from `r20_size_stratified_deff/size_stratified_deff_report.md`: "At m̄_simple=63: DEFF=3.87, C%=29.2%". The raw temporal C%=31.32% (`plan_001` report). The paper uses 29.2% to represent the DEFF-corrected estimate in the discussion. ⚠️ **Ambiguous**: The discussion presents 29.2% as the headline C% without clarifying it's the DEFF-corrected value (not the raw 31.32% from plan_001). The number is sourced correctly, but the discussion context says "C% (29.2%)" without noting it's DEFF-adjusted — readers comparing to §4 (which reports 31.3%) may be confused. The number itself is traceable.
- **Cluster bootstrap CI [26.7%, 53.2%]** ← `sf1_cluster_bootstrap/cluster_bootstrap_ci.md`: "95% CI: [26.73%, 53.17%]" — paper rounds to [26.7%, 53.2%] ✅
- **Jaccard=0.206** ← `r17_jaccard_permutation/jaccard_permutation_report.md`: "Observed Jaccard: 0.2063" ✅
…[truncated 3375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Agent",
  "elapsed_ms": 60
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-23T19:54:33.875191+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# p=0.88 must be from a one-sided test, or from Spearman, or from different columns\n# Check if it's specifically from enrichment_summary.csv \ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/enrichment_summary.csv 2>/dev/null | head -20\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/",
  "description": "Check enrichment summary CSV"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# p=0.88 must be from a one-sided test, or from Spearman, or from different columns\n# Check if it's specifically from enrichment_summary.csv \ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/enrichment_summary.csv 2>/dev/null | head -20\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/",
    "description": "Check enrichment summary CSV"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-23T19:54:33.875327+00:00_

threshold,n_c,pct_c,fpr,rate_contaminated,enrichment
>=  1,9163,73.25711544611448,0.7362106017191977,0.7190672153635117,0.9767140186304669
>=  2,5938,47.47361688519348,0.47636103151862463,0.46584362139917695,0.9779213465763174
>=  3,3182,25.439718580108728,0.2612822349570201,0.2507544581618656,0.9597072613953785
CMH,4165,33.29868883914295,0.3339899713467049,0.3336076817558299,0.9988553860185276
Q1_only,1809,14.46274384393988,0.14774355300859598,0.15363511659807957,1.0398769588893046
Q2_only,4297,34.3540134314039,0.3524355300859599,0.33031550068587107,0.9372366645477154
Q3_only,5311,42.46082507195395,0.42550143266475643,0.4120713305898491,0.9684369991640226
Q4_only,4305,34.41797249760153,0.3459885386819484,0.34266117969821674,0.9903830369745561
Q5_only,3772,30.156699712184203,0.30587392550143266,0.29410150891632375,0.9615121930847493
data
dif_results_merged.csv
dif_results_per_quintile.csv
enrichment_summary.csv
plan_001b_analysis.py
plan_001b_report.md
quintile_cohort_sizes.csv
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-23T19:54:33.875464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search for p=0.88 across all artifact reports\ngrep -rn \"= 0.88\\|= 0.880\\|=0.88\\|p-value.*0.88\\|0.880\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
  "description": "Search all artifacts for p=0.88"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search for p=0.88 across all artifact reports\ngrep -rn \"= 0.88\\|= 0.880\\|=0.88\\|p-value.*0.88\\|0.880\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -20",
    "description": "Search all artifacts for p=0.88"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-23T19:54:33.875598+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv:16:3,80,1.4,0.4544,0.0015,0.8808,0.0035,0.0001,0.7069,0.0353,1000
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md:66:|       80 | 0.454   | 0.450   | 0.002   | 0.002   | 0.881   | 0.880   |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:156:college_computer_science.40,college_computer_science,1.8121384858148184,4.2710078806962315e-09,0.002142275780354,0.0865381253769816,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:261:econometrics.47,econometrics,-1.6177476870377112,0.0001372756085459,0.0158783360288079,0.1553039028650824,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:330:elementary_mathematics.349,elementary_mathematics,3.0402455378034468,0.0,0.0128692691685338,0.204880522870761,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:370:global_facts.37,global_facts,-1.6927290088065556,8.546923613295121e-09,0.0008679860453554,0.0557476774050134,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv:667:high_school_microeconomics.192,high_school_microeconomics,1.523398267828063,5.3033799574109246e-11,0.0005191431405141,0.0523605880133865,C,C,A,False,True
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_res
…[truncated 3454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-23T19:54:33.875785+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find p=0.88 from Fisher test — but we computed p=0.251. Let me check if they use a different test\n# Perhaps they use a one-sided Spearman or a permutation approach? \n# Let me look for it in the plan_001_real_data report more carefully\ngrep -n \"0.88\\|Fisher\\|Exact\\|two.tailed\\|one.tailed\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md",
  "description": "Search for p=0.88 test in plan_001_real_data report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find p=0.88 from Fisher test — but we computed p=0.251. Let me check if they use a different test\n# Perhaps they use a one-sided Spearman or a permutation approach? \n# Let me look for it in the plan_001_real_data report more carefully\ngrep -n \"0.88\\|Fisher\\|Exact\\|two.tailed\\|one.tailed\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md",
    "description": "Search for p=0.88 test in plan_001_real_data report"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-23T19:54:33.875920+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-23T19:54:33.876046+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Also check if p=0.88 is from the dif_results data itself (per-item p-value)\n# Or check if the Jaccard permutation test returns p=0.88\ngrep -rn \"p=0.88\\|perm.*p\\|null.*p\\|p_value.*0.88\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -10",
  "description": "Search for permutation p=0.88"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Also check if p=0.88 is from the dif_results data itself (per-item p-value)\n# Or check if the Jaccard permutation test returns p=0.88\ngrep -rn \"p=0.88\\|perm.*p\\|null.*p\\|p_value.*0.88\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -10",
    "description": "Search for permutation p=0.88"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-23T19:54:33.876190+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:27:1. **Temporal DIF exists**: weighted-mean C% = 13.5% (vs. 31.3% uncorrected). Even after DEFF correction deflates the test statistic, 13.5% of items still exceed ETS category C thresholds — well above the ~5% null expectation. ✓ Conclusion holds.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:37:All three qualitative conclusions — (1) temporal DIF exists at rates far exceeding null expectation, (2) model rankings are near-perfectly preserved, and (3) both cohorts show positive score shifts with a near-zero cohort differential — remain robust under weighted-mean DEFF correction. The correction reduces C-flagged items by 57% (3918 → 1690), yielding a more conservative but directionally identical picture.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:31:- Mean null C% per split: 0.6247%
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:40:**P99 = 1.4504** (vs ETS C = 1.5): the null 99th percentile nearly reaches the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:42:**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the baseline false-positive rate for interpreting these observed rates.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:54:The null distribution is right-skewed with most mass concentrated near zero, consistent wi
…[truncated 1942 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-23T19:54:33.876338+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check if p=0.88 is from bootstrapped Spearman test of enrichment\n# Or maybe it's from the mmlu_li2024_proxy_labels.csv analysis\n# Try looking for it in plan_001b report\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_report.md | grep -n \"0.88\\|Fisher\\|p.*value\\|enrichment.*test\"",
  "description": "Check plan_001b for p=0.88"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check if p=0.88 is from bootstrapped Spearman test of enrichment\n# Or maybe it's from the mmlu_li2024_proxy_labels.csv analysis\n# Try looking for it in plan_001b report\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_report.md | grep -n \"0.88\\|Fisher\\|p.*value\\|enrichment.*test\"",
    "description": "Check plan_001b for p=0.88"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-23T19:54:33.876463+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-23T19:54:33.876623+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Try bootstrap Spearman on enrichment or another test — maybe p=0.88 is from a permutation null\n# Let me compute the actual Fisher test with different orientation\npython3 -c \"\nfrom scipy.stats import chi2_contingency, fisher_exact\n# These numbers come from plan_001 summary:\n# enrichment = 0.96 = DIF-C rate (contam) / DIF-C rate (clean) \n# Rate(contam)=0.3070, Rate(clean)=0.3184\n# N_contam = 3645, N_clean = 5584 (annotated items only)\n\nN_contam = 3645  \nN_clean = 5584\nrate_contam = 0.3070\nrate_clean = 0.3184\n\nC_contam = round(N_contam * rate_contam)\nC_clean = round(N_clean * rate_clean)\n\n# 2x2 table: rows = DIF outcome, cols = Li label\nct = [[C_contam, C_clean], [N_contam - C_contam, N_clean - C_clean]]\nprint('Contingency table:', ct)\nchi2, p_chi2, _, _ = chi2_contingency(ct, correction=False)\nprint(f'chi2={chi2:.4f}, p={p_chi2:.4f}')\n\nOR, fp = fisher_exact(ct, alternative='two-sided')\nprint(f'Fisher exact (two-sided): OR={OR:.4f}, p={fp:.4f}')\nOR2, fp2 = fisher_exact(ct, alternative='greater')\nprint(f'Fisher exact (greater): OR={OR2:.4f}, p={fp2:.4f}')\nOR3, fp3 = fisher_exact(ct, alternative='less')\nprint(f'Fisher exact (less): OR={OR3:.4f}, p={fp3:.4f}')\n\"",
  "description": "Verify what test gives p=0.88"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Try bootstrap Spearman on enrichment or another test — maybe p=0.88 is from a permutation null\n# Let me compute the actual Fisher test with different orientation\npython3 -c \"\nfrom scipy.stats import chi2_contingency, fisher_exact\n# These numbers come from plan_001 summary:\n# enrichment = 0.96 = DIF-C rate (contam) / DIF-C rate (clean) \n# Rate(contam)=0.3070, Rate(clean)=0.3184\n# N_contam = 3645, N_clean = 5584 (annotated items only)\n\nN_contam = 3645  \nN_clean = 5584\nrate_contam = 0.3070\nrate_clean = 0.3184\n\nC_contam = round(N_contam * rate_contam)\nC_clean = round(N_clean * rate_clean)\n\n# 2x2 table: rows = DIF outcome, cols = Li label\nct = [[C_contam, C_clean], [N_contam - C_contam, N_clean - C_clean]]\nprint('Contingency table:', ct)\nchi2, p_chi2, _, _ = chi2_contingency(ct, correction=False)\nprint(f'chi2={chi2:.4f}, p={p_chi2:.4f}')\n\nOR, fp = fisher_exact(ct, alternative='two-sided')\nprint(f'Fisher exact (two-sided): OR={OR:.4f}, p={fp:.4f}')\nOR2, fp2 = fisher_exact(ct, alternative='greater')\nprint(f'Fisher exact (greater): OR={OR2:.4f}, p={fp2:.4f}')\nOR3, fp3 = fisher_exact(ct, alternative='less')\nprint(f'Fisher exact (less): OR={OR3:.4f}, p={fp3:.4f}')\n\"",
    "description": "Verify what test gives p=0.88"
  }
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-23T19:54:33.876873+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check if 2024 random split = 1.3% is from plan_001 2024 within-year half-split\ngrep -rn \"1.3\\|within.*2024\\|2024.*half\\|split.*2024\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/ --include=\"*.md\" 2>/dev/null | head -15",
  "description": "Find 2024 random split 1.3% source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check if 2024 random split = 1.3% is from plan_001 2024 within-year half-split\ngrep -rn \"1.3\\|within.*2024\\|2024.*half\\|split.*2024\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/ --include=\"*.md\" 2>/dev/null | head -15",
    "description": "Find 2024 random split 1.3% source"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-23T19:54:33.877016+00:00_

Contingency table: [[1119, 1778], [2526, 3806]]
chi2=1.3341, p=0.2481
Fisher exact (two-sided): OR=0.9483, p=0.2514
Fisher exact (greater): OR=0.9483, p=0.8806
Fisher exact (less): OR=0.9483, p=0.1288

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-23T19:54:33.877147+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:6:- **Uncorrected C items**: 3918 (31.3%)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md:27:1. **Temporal DIF exists**: weighted-mean C% = 13.5% (vs. 31.3% uncorrected). Even after DEFF correction deflates the test statistic, 13.5% of items still exceed ETS category C thresholds — well above the ~5% null expectation. ✓ Conclusion holds.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/cluster_bootstrap_ci.md:15:| Point estimate C% | 31.30% | 31.30% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/cluster_bootstrap_ci.md:28:cluster bootstrap mean: 38.83% vs point estimate 31.30%).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:16:| 4 | professional_accounting | 241 | 163 | 67.6% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:18:| 6 | high_school_microeconomics | 219 | 143 | 65.3% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:28:| 16 | high_school_geography | 183 | 98 | 53.6% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:41:| 29 | nutrition | 259 | 103 | 39.8% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:45:| 33 | international_law | 103 | 38 | 36.9% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md:42:**Null C% = 0.624
…[truncated 450 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-23T19:54:33.877308+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Good - the 2024 random split C%=1.3% is confirmed from random_split_report.md (mentioned alongside 0.18% 2023)\n# And p=0.88 is Fisher exact (greater), i.e. one-sided test H1: DIF enrichment > 1 which gives p=0.88\n# This means p=0.88 means failure to reject H0 (no enrichment)\n# Now check ρ=0.999 for downstream under weighted-mean DEFF\necho \"rho=0.999 from weighted_mean_downstream.md: 0.998811\"\necho \"score shift +1.77pp: 1.772 pp\"\n\n# Check bootstrap CI for model-level bootstrap [29.4%, 38.1%]\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv | head -5",
  "description": "Verify downstream DEFF numbers and bootstrap CI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Good - the 2024 random split C%=1.3% is confirmed from random_split_report.md (mentioned alongside 0.18% 2023)\n# And p=0.88 is Fisher exact (greater), i.e. one-sided test H1: DIF enrichment > 1 which gives p=0.88\n# This means p=0.88 means failure to reject H0 (no enrichment)\n# Now check ρ=0.999 for downstream under weighted-mean DEFF\necho \"rho=0.999 from weighted_mean_downstream.md: 0.998811\"\necho \"score shift +1.77pp: 1.772 pp\"\n\n# Check bootstrap CI for model-level bootstrap [29.4%, 38.1%]\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv | head -5",
    "description": "Verify downstream DEFF numbers and bootstrap CI"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-23T19:54:33.877440+00:00_

rho=0.999 from weighted_mean_downstream.md: 0.998811
score shift +1.77pp: 1.772 pp
bootstrap_type,iteration,c_pct
cluster,0,0.3675247841381516
cluster,1,0.37663895107131434
cluster,2,0.43316277582347296
cluster,3,0.3580108730412536

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-23T19:54:33.877572+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check bootstrap CI for model-level CI [29.4%, 38.1%]\npython3 -c \"\nimport csv\nvals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        vals.append(float(row['c_pct']))\n\nimport numpy as np\narr = np.array(vals)\nprint(f'N bootstraps: {len(arr)}')\nprint(f'Model bootstrap CI: [{np.percentile(arr, 2.5):.1f}%, {np.percentile(arr, 97.5):.1f}%]')\nprint(f'Mean: {np.mean(arr):.2f}%')\n\" 2>/dev/null || python3 -c \"\nimport csv\nvals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        for key, val in row.items():\n            print(f'{key}: {val}')\n        break\n\"",
  "description": "Check model bootstrap CI from bootstrap_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check bootstrap CI for model-level CI [29.4%, 38.1%]\npython3 -c \"\nimport csv\nvals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        vals.append(float(row['c_pct']))\n\nimport numpy as np\narr = np.array(vals)\nprint(f'N bootstraps: {len(arr)}')\nprint(f'Model bootstrap CI: [{np.percentile(arr, 2.5):.1f}%, {np.percentile(arr, 97.5):.1f}%]')\nprint(f'Mean: {np.mean(arr):.2f}%')\n\" 2>/dev/null || python3 -c \"\nimport csv\nvals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        for key, val in row.items():\n            print(f'{key}: {val}')\n        break\n\"",
    "description": "Check model bootstrap CI from bootstrap_results.csv"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-23T19:54:33.877697+00:00_

N bootstraps: 2000
Model bootstrap CI: [0.3%, 0.5%]
Mean: 0.36%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-23T19:54:33.877848+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv",
  "description": "Read bootstrap results CSV header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv",
    "description": "Read bootstrap results CSV header"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-23T19:54:33.877969+00:00_

bootstrap_type,iteration,c_pct
cluster,0,0.3675247841381516
cluster,1,0.37663895107131434
cluster,2,0.43316277582347296
cluster,3,0.3580108730412536

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-23T19:54:33.878091+00:00_

Files with 28.9:
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/novelty_rebuttal_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/latest/median/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 3
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-23T19:54:33.878221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md') as f:\n    content = f.read()\nidx = content.find('28.9')\nprint(content[max(0,idx-300):idx+500])\n\"\n",
  "description": "Find 28.9 context in temporal_overlap_report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md') as f:\n    content = f.read()\nidx = content.find('28.9')\nprint(content[max(0,idx-300):idx+500])\n\"\n",
    "description": "Find 28.9 context in temporal_overlap_report"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-23T19:54:33.878343+00:00_

.02 (max score difference between matched pairs). Five random seeds for robustness.

| Seed | N matched | Cohen's d | C% |
|------|-----------|-----------|-----|
| 0 | 635 | -0.0074 | 28.7 |
| 1 | 639 | -0.0094 | 29.0 |
| 2 | 640 | -0.0120 | 29.0 |
| 3 | 639 | -0.0102 | 29.0 |
| 4 | 638 | -0.0089 | 28.9 |

**Mean matched: N=638, d=-0.0096, C%=28.9 ± 0.1%**

NN matching achieves near-zero ability difference (d ≈ -0.010) while retaining 79% of the focal cohort. C% drops from 31.3% to 28.9%, a 7.7% relative reduction.

### 2d. P10–P90 Common Support (Sensitivity Check)

Restriction: total score ∈ [max(P10_ref, P10_foc), min(P90_ref, P90_foc)] = [0.3261, 0.7011]

N_ref=859, N_foc=570; Cohen's d = -0.1625; **C% = 51.0%**

The elevated C% under percentile trimming is expected: removing tail mode

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 531 · 2026-05-23T19:54:33.878481+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport csv\nimport numpy as np\ncluster_vals = []\nmodel_vals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        v = float(row['c_pct'])\n        if row['bootstrap_type'] == 'cluster':\n            cluster_vals.append(v * 100)  # convert to %\n        else:\n            model_vals.append(v * 100)\n\nprint(f'Cluster bootstrap: N={len(cluster_vals)}')\nif cluster_vals:\n    arr = np.array(cluster_vals)\n    print(f'  CI: [{np.percentile(arr,2.5):.1f}%, {np.percentile(arr,97.5):.1f}%]')\n    \nprint(f'Model bootstrap: N={len(model_vals)}')\nif model_vals:\n    arr2 = np.array(model_vals)\n    print(f'  CI: [{np.percentile(arr2,2.5):.1f}%, {np.percentile(arr2,97.5):.1f}%]')\n\"",
  "description": "Compute bootstrap CIs separated by type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport csv\nimport numpy as np\ncluster_vals = []\nmodel_vals = []\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/bootstrap_results.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        v = float(row['c_pct'])\n        if row['bootstrap_type'] == 'cluster':\n            cluster_vals.append(v * 100)  # convert to %\n        else:\n            model_vals.append(v * 100)\n\nprint(f'Cluster bootstrap: N={len(cluster_vals)}')\nif cluster_vals:\n    arr = np.array(cluster_vals)\n    print(f'  CI: [{np.percentile(arr,2.5):.1f}%, {np.percentile(arr,97.5):.1f}%]')\n    \nprint(f'Model bootstrap: N={len(model_vals)}')\nif model_vals:\n    arr2 = np.array(model_vals)\n    print(f'  CI: [{np.percentile(arr2,2.5):.1f}%, {np.percentile(arr2,97.5):.1f}%]')\n\"",
    "description": "Compute bootstrap CIs separated by type"
  }
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-23T19:54:33.878622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md') as f:\n    content = f.read()\n# Find the context for 638/group and Cohen's d = -0.17 or -0.010\nidx = content.find('638')\nprint(content[max(0,idx-500):idx+500])\n\"\n",
  "description": "Check temporal overlap report for matched N and Cohen's d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md') as f:\n    content = f.read()\n# Find the context for 638/group and Cohen's d = -0.17 or -0.010\nidx = content.find('638')\nprint(content[max(0,idx-500):idx+500])\n\"\n",
    "description": "Check temporal overlap report for matched N and Cohen's d"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-23T19:54:33.878768+00:00_

 | 97.5% |

Cohen's d (restricted) = -0.1488

**Range-restricted C% = 30.9%** (essentially unchanged; only 20 extreme foc models excluded)

### 2c. 1:1 Nearest-Neighbor Matching (Primary Ability Control)

Caliper = 0.02 (max score difference between matched pairs). Five random seeds for robustness.

| Seed | N matched | Cohen's d | C% |
|------|-----------|-----------|-----|
| 0 | 635 | -0.0074 | 28.7 |
| 1 | 639 | -0.0094 | 29.0 |
| 2 | 640 | -0.0120 | 29.0 |
| 3 | 639 | -0.0102 | 29.0 |
| 4 | 638 | -0.0089 | 28.9 |

**Mean matched: N=638, d=-0.0096, C%=28.9 ± 0.1%**

NN matching achieves near-zero ability difference (d ≈ -0.010) while retaining 79% of the focal cohort. C% drops from 31.3% to 28.9%, a 7.7% relative reduction.

### 2d. P10–P90 Common Support (Sensitivity Check)

Restriction: total score ∈ [max(P10_ref, P10_foc), min(P90_ref, P90_foc)] = [0.3261, 0.7011]

N_ref=859, N_foc=570; Cohen's d = -0.1625; **C% = 51.0%**

The elevated C% under percentile trimming is expected: re

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 534 · 2026-05-23T19:54:33.878898+00:00_

Cluster bootstrap: N=1000
  CI: [26.7%, 53.2%]
Model bootstrap: N=1000
  CI: [29.2%, 37.8%]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 535 · 2026-05-23T19:54:33.879029+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check GSM8K ΔTPR=+0.514\ngrep -rn \"0.514\\|GSM.*TPR\\|gsm8k.*tpr\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -10",
  "description": "Find GSM8K ΔTPR=+0.514"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check GSM8K ΔTPR=+0.514\ngrep -rn \"0.514\\|GSM.*TPR\\|gsm8k.*tpr\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/ --include=\"*.md\" --include=\"*.csv\" 2>/dev/null | head -10",
    "description": "Find GSM8K ΔTPR=+0.514"
  }
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-23T19:54:33.879158+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/winogrande_dif_results.csv:495:494,1.0725035655085144,-0.1644898863002348,0.24037398620329056,0.40031784409559856,0.5269251546036204,A
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/winogrande_dif_results.csv:543:542,2.463520142559726,-2.1187395065142707,0.3608424724786805,37.92375242121685,7.356414366554986e-10,C
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/winogrande_dif_results.csv:630:629,0.9427364887972541,0.1385759154004514,0.5977318579725204,0.011092107213011392,0.9161226287914923,A
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/winogrande_dif_results.csv:1035:1034,0.516442126611618,1.5528613077594366,0.63164074401124,5.495300151475244,0.01906765434390123,C
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:118:117,0.8376798561151079,0.4162303192068788,0.5051034989390084,0.514991502746797,0.4729860195875082,A
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:154:153,0.946723946611436,0.12865716865266005,0.4005145490884812,0.056771681244681106,0.8116731715824874,A
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:209:208,0.5809257361291932,1.276361025028395,0.514743657363701,5.648099102202664,0.01747430456176513,B
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:361:360,0.9550711654363101,0.10802814286634431,0.5376168400877368,0.0075144241316347,0.9309212812603493,A
/home/ubuntu/.
…[truncated 484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-23T19:54:33.879304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md | head -60",
  "description": "Read multi-bench DIF report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md | head -60",
    "description": "Read multi-bench DIF report"
  }
}
```

</details>

---


### Tool result

_source line 538 · 2026-05-23T19:54:33.879433+00:00_

# Plan 028: Multi-Benchmark Temporal DIF Analysis

## Overview

Temporal MH-DIF analysis (2023 vs 2024 cohort) across all 6 METABENCH benchmarks.
Uses purified Mantel-Haenszel with 5 score strata. ETS classification:
- **A**: |Δ_MH| < 1.0 (negligible)
- **B**: 1.0 ≤ |Δ_MH| < 1.5 or |Δ_MH| ≥ 1.5 but p ≥ 0.05 (moderate)
- **C**: |Δ_MH| ≥ 1.5 and p < 0.05 (large, flagged)

## Summary Table

| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
|-----------|-------|-------------|-------------|---|---|---|----|-----------|--------|
| MMLU | 12508 | 1080 | 807 | 6332 | 2258 | 3918 | 31.3% | 0.18% | PRIOR |
| WINOGRANDE | 1267 | 1017 | 803 | 612 | 271 | 384 | 30.3% | 0.32% | OK |
| TRUTHFULQA | 817 | 1080 | 807 | 398 | 176 | 243 | 29.7% | 0.37% | OK |
| ARC | 1172 | 1080 | 807 | 642 | 215 | 315 | 26.9% | 0.6% | OK |
| GSM8K | 1319 | 1017 | 804 | 825 | 245 | 249 | 18.9% | 0.3% | PRIOR |
| HELLASWAG | 10042 | 1080 | 807 | 6037 | 2208 | 1797 | 17.9% | 0.28% | OK |

## Key Findings

- **WINOGRANDE**: 30.3% items flagged as ETS-C (vs 0.32% random control, 94.7× enrichment)
- **TRUTHFULQA**: 29.7% items flagged as ETS-C (vs 0.37% random control, 80.3× enrichment)
- **ARC**: 26.9% items flagged as ETS-C (vs 0.6% random control, 44.8× enrichment)
- **HELLASWAG**: 17.9% items flagged as ETS-C (vs 0.28% random control, 63.9× enrichment)

## Interpretation

The temporal DIF signal (C% >> random C%) indicates systematic item-level 
performance shifts between 2023 and 2024 model cohorts, consistent with 
benchmark contamination or benchmark-specific training optimization.

Random-split controls confirm that the DIF signal is not an artifact of 
the MH procedure or score distribution differences within a single cohort.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 539 · 2026-05-23T19:54:33.879583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find GSM8K ΔTPR=+0.514 from plan_028 bootstrap_ci directory\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_bootstrap_ci/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/ 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*gsm*\" -type f 2>/dev/null | head -10",
  "description": "Find GSM8K injection results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find GSM8K ΔTPR=+0.514 from plan_028 bootstrap_ci directory\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_bootstrap_ci/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/ 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*gsm*\" -type f 2>/dev/null | head -10",
    "description": "Find GSM8K injection results"
  }
}
```

</details>

---


### Tool result

_source line 540 · 2026-05-23T19:54:33.879730+00:00_

__pycache__
bootstrap_ci.py
bootstrap_ci_report.md
bootstrap_ci_results.csv
bootstrap_distributions.csv
log_hellaswag.txt
log_mmlu.txt
log_small.txt
mmlu_bootstrap_ci.py
mmlu_bootstrap_report.md
mmlu_bootstrap_results.csv
mmlu_bootstrap_summary.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 541 · 2026-05-23T19:54:33.879868+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*gsm*\" -o -name \"*GSM*\" 2>/dev/null | head -10",
  "description": "Find GSM8K related files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*gsm*\" -o -name \"*GSM*\" 2>/dev/null | head -10",
    "description": "Find GSM8K related files"
  }
}
```

</details>

---


### Tool result

_source line 542 · 2026-05-23T19:54:33.879987+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm1k_model_accuracy.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm1k_dif_correlation.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dif_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_ets_summary.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/plan_004_step1_gsm8k_temporal_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/gsm1k_jaccard_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-23T19:54:33.880131+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv",
  "description": "Read GSM8K dose response summary for ΔTPR=+0.514"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv",
    "description": "Read GSM8K dose response summary for ΔTPR=+0.514"
  }
}
```

</details>

---


### Tool result

_source line 544 · 2026-05-23T19:54:33.880257+00:00_

p,matching_type,tpr_mean,tpr_std,fpr_mean,fpr_std,delta_tpr,fisher_or_mean,fisher_p_median,n_flipped_mean
0.0,external,0.4833333333333334,0.027654109467339354,0.47146919431279616,0.006920080473343698,0.0,1.0569313712780013,0.535203228313758,0.0
0.0,standard,0.18181818181818182,0.038721682386857706,0.190521327014218,0.00968959635083454,0.0,0.968883721205098,0.13488067909313184,0.0
0.3,external,0.9696969696969697,0.014670391462906869,0.47146919431279616,0.006920080473343698,0.48636363636363633,43.675880258053276,4.09415202292533e-62,36235.2
0.3,standard,0.740909090909091,0.017066485342528484,0.2564928909952607,0.0073604810078927736,0.5590909090909091,8.322469364987208,1.6700289913331167e-47,36235.2
0.5,external,0.9977272727272727,0.0020747066572165363,0.47146919431279616,0.006920080473343698,0.5143939393939393,inf,1.617530418124674e-73,60445.4
0.5,standard,0.931060606060606,0.00561833218719372,0.3672037914691943,0.0019655394647703924,0.7492424242424243,23.417772639889186,6.7348716962479354e-68,60445.4
0.7,external,1.0,0.0,0.47146919431279616,0.006920080473343698,0.5166666666666666,inf,1.617530418124674e-73,84524.4
0.7,standard,1.0,0.0,0.47601895734597155,0.009791060859614568,0.8181818181818181,inf,1.617530418124674e-73,84524.4
1.0,external,1.0,0.0,0.47146919431279616,0.006920080473343698,0.5166666666666666,inf,1.617530418124674e-73,120928.6
1.0,standard,1.0,0.0,0.6453080568720378,0.012456433365686845,0.8181818181818181,inf,3.725110278780312e-45,120928.6

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 545 · 2026-05-23T19:54:33.880393+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_bootstrap_ci/bootstrap_ci_report.md | head -40",
  "description": "Read plan_028 bootstrap CI report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_bootstrap_ci/bootstrap_ci_report.md | head -40",
    "description": "Read plan_028 bootstrap CI report"
  }
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-23T19:54:33.880525+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# The paper says in the text: '1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17)'\n# Source shows: mean N=638, Cohen's d = -0.0096 (not -0.17!)\n# This is a discrepancy in the text of the paper (not the table)\n# The table row 'Matched-ability' just says ~0.31 C%\n\n# But the ~0.31 in Table 2 doesn't match any single source value clearly\n# The temporal overlap report shows that NN-matched C% = 28.9% (not ~31%)\n# plan_001b shows Q3 has 42.5%, Q2 has 34.4%, etc.\n# Where does ~0.31 in Table 2 come from?\n\n# Let me check if plan_001b has a merged Temp C% value close to 31%\n# plan_001b: CMH method gives 33.3%, >= 2 gives 47.5%\n# None is ~31%\n\n# Actually the r22 composition control shows balanced C% = 30.2% (mean)\n# Maybe ~0.31 = 31% in Table 2 refers to CMH quintile analysis?\n\n# Or the table represents the unmatched temporal C% under quintile-based comparison\n# plan_001 ability cohort C% = 2.9% - not 31%\n\n# Let me look at other reports mentioning 31% with ability matching\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '~0.31' in content or '~31' in content:\n            print(f)\n    except:\n        pass\n\" | head -10\n",
  "description": "Find source of ~0.31 value in Table 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# The paper says in the text: '1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17)'\n# Source shows: mean N=638, Cohen's d = -0.0096 (not -0.17!)\n# This is a discrepancy in the text of the paper (not the table)\n# The table row 'Matched-ability' just says ~0.31 C%\n\n# But the ~0.31 in Table 2 doesn't match any single source value clearly\n# The temporal overlap report shows that NN-matched C% = 28.9% (not ~31%)\n# plan_001b shows Q3 has 42.5%, Q2 has 34.4%, etc.\n# Where does ~0.31 in Table 2 come from?\n\n# Let me check if plan_001b has a merged Temp C% value close to 31%\n# plan_001b: CMH method gives 33.3%, >= 2 gives 47.5%\n# None is ~31%\n\n# Actually the r22 composition control shows balanced C% = 30.2% (mean)\n# Maybe ~0.31 = 31% in Table 2 refers to CMH quintile analysis?\n\n# Or the table represents the unmatched temporal C% under quintile-based comparison\n# plan_001 ability cohort C% = 2.9% - not 31%\n\n# Let me look at other reports mentioning 31% with ability matching\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '~0.31' in content or '~31' in content:\n            print(f)\n    except:\n        pass\n\" | head -10\n",
    "description": "Find source of ~0.31 value in Table 2"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-23T19:54:33.880695+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_013_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/experiment_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_012_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_q3_local_independence/report/plan_013_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 548 · 2026-05-23T19:54:33.880846+00:00_

cat: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_bootstrap_ci/bootstrap_ci_report.md: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 549 · 2026-05-23T19:54:33.880980+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check downstream numbers: ρ=0.997, τ=0.958, flip≤2.8% from cross-benchmark table\n# plan_028 has these values - check multi_bench_summary.csv for full numbers including rank stats\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf2_report.md 2>/dev/null | head -20",
  "description": "Check mf2_report for cross-benchmark ρ/τ values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check downstream numbers: ρ=0.997, τ=0.958, flip≤2.8% from cross-benchmark table\n# plan_028 has these values - check multi_bench_summary.csv for full numbers including rank stats\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf2_report.md 2>/dev/null | head -20",
    "description": "Check mf2_report for cross-benchmark ρ/τ values"
  }
}
```

</details>

---


### Tool result

_source line 550 · 2026-05-23T19:54:33.881107+00:00_

# MF2: Practical Significance — Stable-Item Rank Stability

## Per-Benchmark Results

| Benchmark | Items | C items | Stable | %C | Models | Spearman ρ | p-value | Kendall τ | Flip rate |
|-----------|------:|--------:|-------:|---:|-------:|-----------:|--------:|----------:|----------:|
| MMLU | 12508 | 3918 | 8590 | 31.32% | 5227 | 0.9965 | 0.00e+00 | 0.9600 | 0.0200 |
| ARC | 1172 | 315 | 857 | 26.88% | 5227 | 0.9962 | 0.00e+00 | 0.9538 | 0.0231 |
| HellaSwag | 10042 | 1797 | 8245 | 17.89% | 5227 | 0.9986 | 0.00e+00 | 0.9722 | 0.0139 |
| WinoGrande | 1267 | 384 | 883 | 30.31% | 6558 | 0.9943 | 0.00e+00 | 0.9432 | 0.0284 |
| TruthfulQA | 817 | 243 | 574 | 29.74% | 5228 | 0.9971 | 0.00e+00 | 0.9586 | 0.0207 |
| GSM8K | 1319 | 249 | 1070 | 18.88% | 6702 | 0.9993 | 0.00e+00 | 0.9843 | 0.0078 |

## Cross-Benchmark Summary

- **Mean Spearman ρ**: 0.9970 (range: 0.9943–0.9993)
- **Mean flip rate**: 0.0190 (range: 0.0078–0.0284)

## Interpretation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 551 · 2026-05-23T19:54:33.881242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_012_report.md') as f:\n    content = f.read()\nidx = content.find('~0.31')\nif idx >= 0:\n    print(content[max(0,idx-300):idx+400])\n\"\n",
  "description": "Check plan_012 report context for ~0.31"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_012_report.md') as f:\n    content = f.read()\nidx = content.find('~0.31')\nif idx >= 0:\n    print(content[max(0,idx-300):idx+400])\n\"\n",
    "description": "Check plan_012 report context for ~0.31"
  }
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-23T19:54:33.881378+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Now check the downstream numbers more carefully:\n# Paper says ρ=0.997, τ=0.958, flip rate ≤2.8% - from table above (MMLU: ρ=0.9965, τ=0.9600, Flip=0.0200)\n# WinoGrande: Flip=0.0284 (2.84%), which is the max - paper says ≤2.8% - let me check\n\n# Also check 33.6% pairwise rankings reverse for 200 most displaced\n# From plan_032 report: \"| 200 | 119 | 59.5% | 83 | 41.5% | 33 | 16.5% |\" - not 33.6%\n# Let me look more carefully\n\ngrep -rn \"33.6\\|pairwise.*200\\|200.*pairwise\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -10",
  "description": "Find pairwise rank reversal 33.6% for 200 most displaced"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Now check the downstream numbers more carefully:\n# Paper says ρ=0.997, τ=0.958, flip rate ≤2.8% - from table above (MMLU: ρ=0.9965, τ=0.9600, Flip=0.0200)\n# WinoGrande: Flip=0.0284 (2.84%), which is the max - paper says ≤2.8% - let me check\n\n# Also check 33.6% pairwise rankings reverse for 200 most displaced\n# From plan_032 report: \"| 200 | 119 | 59.5% | 83 | 41.5% | 33 | 16.5% |\" - not 33.6%\n# Let me look more carefully\n\ngrep -rn \"33.6\\|pairwise.*200\\|200.*pairwise\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -10",
    "description": "Find pairwise rank reversal 33.6% for 200 most displaced"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-23T19:54:33.881511+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/mf1_report.md:14:Within the top-200 most displaced models (|rank_change| ≥ 298), there are 6,694 pairwise flips out of 19,900 pairs (33.6%).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf1_report.md:14:Within the top-200 most displaced models (|rank_change| ≥ 298), there are 6,694 pairwise flips out of 19,900 pairs (33.6%).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/composition_control_report.md:37:7,29.90885833066837,682,807,67.88856304985337,67.90582403965304
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_012_report.md:150:| theta_qt_15 | 15 | 0.3280 | 0.3376 | 0.972 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012_irt_theta_conditioning/report/plan_012_report.md:150:| theta_qt_15 | 15 | 0.3280 | 0.3376 | 0.972 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_supplement/ld_dif_cross_report.md:57:| 5 | professional_psychology | 7.0% | 33.6% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_supplement/report/ld_dif_cross_report.md:57:| 5 | professional_psychology | 7.0% | 33.6% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_report.md:150:| theta_qt_15 | 15 | 0.3280 | 0.3376 | 0.972 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_11.md:76:**W-S3. ρ = 0.997 与 33.6% pairwise reversal 的张力未 reconcile。** [R1-W5 Should-Fix, R2 AGREE]
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_11.md:78:Spearman ρ = 0.997（全局排名几乎不变）而 33.6% pairw
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-23T19:54:33.881662+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal/",
  "description": "Check r18_rank_bucket_reversal directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal/",
    "description": "Check r18_rank_bucket_reversal directory"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-23T19:54:33.881804+00:00_

rank_reversal_analysis.py
rank_reversal_report.md
results.json
reversal_by_bucket.pdf
reversal_by_bucket.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-23T19:54:33.881929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal/*.md 2>/dev/null | head -60",
  "description": "Read rank bucket reversal report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_rank_bucket_reversal/*.md 2>/dev/null | head -60",
    "description": "Read rank bucket reversal report"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-23T19:54:33.882051+00:00_

# R18 Exp 2: Rank-Bucket Reversal Distribution

## Setup
- **Models**: 5,227
- **Items (full)**: 12,508
- **DIF-C items removed**: 3,918
- **Stable items**: 8,590
- **Rank correlation (full vs stable)**: 0.996451

## Results

| Bucket | Reversal Rate | Sampled / Total Pairs | Mean Δacc |
|--------|--------------|----------------------|-----------|
| 1–49 | 35.2% | 200,000 / 254,898 | 0.0031 |
| 50–199 | 15.1% | 200,000 / 765,375 | 0.0143 |
| 200–499 | 4.0% | 200,000 / 1,463,250 | 0.0394 |
| 500–999 | 0.6% | 200,000 / 2,238,750 | 0.0804 |
| 1000+ | 0.0% | 200,000 / 8,935,878 | 0.2237 |

## Interpretation

Rank reversals are **heavily concentrated** among closely-ranked models:

- **Δrank < 50**: reversal rate = 35.2%
- **Δrank ≥ 1000**: reversal rate = 0.0%

This confirms that removing DIF-C items reshuffles rankings primarily among
models with similar ability, while the broad leaderboard structure is preserved
(rank correlation = 0.9965).

**Key takeaway**: contamination-driven score inflation matters most for
fine-grained comparisons between closely-matched models, not for separating
qualitatively different capability tiers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 558 · 2026-05-23T19:54:33.882181+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 559 · 2026-05-23T19:54:33.882315+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let me directly look for what 'Matched-ability' means in Table 2 context\n# The table caption says: 'Structural controls and sensitivity checks for temporal DIF'\n# Row: Matched-ability | Within-quintile temp DIF | ~0.31 | -- | Enrich. 0.94-1.04\n# This could represent the FPR (fraction of C-flagged items) in the semi-synthetic baseline\n\n# From plan_011 standard MH for temporal cohort at p=0:\n# 'temporal | 0.0 | 0.308±0.047 | 0.298±0.012 | +0.000'\n# So standard FPR is 0.298\n\n# But plan_012 external_5 at p=0 has FPR=0.314±0.009\n# And theta_qt_20 has FPR=0.312±0.008\n\n# Looking at the table structure: 'Temp C%' means temporal C%\n# ~0.31 for matched-ability means ~31% C% in temporal DIF\n\n# r22 composition-balanced: mean C% = 30.25% ≈ ~0.30\n# NN matched: 28.9% \n\n# Actually plan_001b CMH approach gives 33.3% -- that's not ~31% either\n# Let me check if there's a simpler: plan_022 (composition control = ~30.2%)\n# rounded to ~0.31 would be close\n\n# OR maybe it's just stating temporal C% doesn't change much under ability matching\n# and refers to the fact that r22 or plan_001 result stays around 31%\n\nprint('Summary: ~0.31 in Table 2 row Matched-ability could be:')\nprint('  - r22 composition-balanced: 30.25% (closest)')\nprint('  - NN matching: 28.9% (not ~31%)')  \nprint('  - plan_001b Q5: 30.2% (close)')\nprint('  - Most likely intended as ~30-31% range from r22 balanced result')\n\"\n",
  "description": "Analyze source of ~0.31 value in Table 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let me directly look for what 'Matched-ability' means in Table 2 context\n# The table caption says: 'Structural controls and sensitivity checks for temporal DIF'\n# Row: Matched-ability | Within-quintile temp DIF | ~0.31 | -- | Enrich. 0.94-1.04\n# This could represent the FPR (fraction of C-flagged items) in the semi-synthetic baseline\n\n# From plan_011 standard MH for temporal cohort at p=0:\n# 'temporal | 0.0 | 0.308±0.047 | 0.298±0.012 | +0.000'\n# So standard FPR is 0.298\n\n# But plan_012 external_5 at p=0 has FPR=0.314±0.009\n# And theta_qt_20 has FPR=0.312±0.008\n\n# Looking at the table structure: 'Temp C%' means temporal C%\n# ~0.31 for matched-ability means ~31% C% in temporal DIF\n\n# r22 composition-balanced: mean C% = 30.25% ≈ ~0.30\n# NN matched: 28.9% \n\n# Actually plan_001b CMH approach gives 33.3% -- that's not ~31% either\n# Let me check if there's a simpler: plan_022 (composition control = ~30.2%)\n# rounded to ~0.31 would be close\n\n# OR maybe it's just stating temporal C% doesn't change much under ability matching\n# and refers to the fact that r22 or plan_001 result stays around 31%\n\nprint('Summary: ~0.31 in Table 2 row Matched-ability could be:')\nprint('  - r22 composition-balanced: 30.25% (closest)')\nprint('  - NN matching: 28.9% (not ~31%)')  \nprint('  - plan_001b Q5: 30.2% (close)')\nprint('  - Most likely intended as ~30-31% range from r22 balanced result')\n\"\n",
    "description": "Analyze source of ~0.31 value in Table 2"
  }
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-23T19:54:33.882459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check cohort gap = 96.2 positions, 40x random, p<0.001 - from plan_032 dif_vs_random_comparison\npython3 -c \"\n# From plan_032 random_baseline_report.md:\n# DIF cohort gap = 73.60 - (-22.56) = 96.16\n# Random mean: 2.79 - 0.43 = 2.36\nprint(f'DIF cohort gap: {73.599 - (-22.562):.1f}')\nprint(f'Random mean gap: {2.787 - 0.431:.2f}')\nprint(f'Ratio: {(73.599 - (-22.562)) / (2.787 - 0.431):.0f}x')\n\"",
  "description": "Verify cohort gap 96.2 and 40x ratio"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check cohort gap = 96.2 positions, 40x random, p<0.001 - from plan_032 dif_vs_random_comparison\npython3 -c \"\n# From plan_032 random_baseline_report.md:\n# DIF cohort gap = 73.60 - (-22.56) = 96.16\n# Random mean: 2.79 - 0.43 = 2.36\nprint(f'DIF cohort gap: {73.599 - (-22.562):.1f}')\nprint(f'Random mean gap: {2.787 - 0.431:.2f}')\nprint(f'Ratio: {(73.599 - (-22.562)) / (2.787 - 0.431):.0f}x')\n\"",
    "description": "Verify cohort gap 96.2 and 40x ratio"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-23T19:54:33.882580+00:00_

Summary: ~0.31 in Table 2 row Matched-ability could be:
  - r22 composition-balanced: 30.25% (closest)
  - NN matching: 28.9% (not ~31%)
  - plan_001b Q5: 30.2% (close)
  - Most likely intended as ~30-31% range from r22 balanced result

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-23T19:54:33.882720+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let me also look at plan_027_temporal_overlap which might have the matched values\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap/'\nfiles = os.listdir(base)\nprint(files)\n\"\n",
  "description": "List plan_027 temporal overlap files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let me also look at plan_027_temporal_overlap which might have the matched values\nimport os\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap/'\nfiles = os.listdir(base)\nprint(files)\n\"\n",
    "description": "List plan_027 temporal overlap files"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-23T19:54:33.882851+00:00_

['full_dif_results.csv', 'fig_temporal_score_distribution.pdf', 'nn_matching_results.csv', 'fig_temporal_score_distribution.png', 'temporal_overlap_report.md', 'plan_027_temporal_overlap.py']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 564 · 2026-05-23T19:54:33.882963+00:00_

DIF cohort gap: 96.2
Random mean gap: 2.36
Ratio: 41x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-23T19:54:33.883084+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check z=-8 to -49 for DIF-flagged items concentration\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf2_report.md | grep -n \"z.*score\\|discrimin\\|signal\"",
  "description": "Find z-score for discriminative signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check z=-8 to -49 for DIF-flagged items concentration\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf2_report.md | grep -n \"z.*score\\|discrimin\\|signal\"",
    "description": "Find z-score for discriminative signal"
  }
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-23T19:54:33.883208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap/temporal_overlap_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap/temporal_overlap_report.md"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-23T19:54:33.883345+00:00_

1	# Plan 027: Temporal Cohort Ability Distribution Overlap + Restricted C%
2	
3	## Part 1: Score Distribution Statistics
4	
5	| Metric | 2023 (ref, N=1080) | 2024 (foc, N=807) |
6	|--------|------|------|
7	| Mean | 0.5814 | 0.6068 |
8	| Median | 0.6275 | 0.6715 |
9	| SD | 0.1405 | 0.1556 |
10	| Min | 0.2200 | 0.1736 |
11	| Q1 | 0.5404 | 0.5644 |
12	| Q3 | 0.6673 | 0.6955 |
13	| Max | 0.8090 | 0.8261 |
14	
15	### Distributional Overlap Metrics
16	
17	| Metric | Value |
18	|--------|-------|
19	| Cohen's d | -0.1729 |
20	| Overlap coefficient (KDE) | 0.7639 |
21	| Bhattacharyya coefficient | 0.9606 |
22	| Bhattacharyya distance | 0.0402 |
23	| KL(2023 ‖ 2024) | 1.5235 |
24	| KL(2024 ‖ 2023) | 1.1664 |
25	| Mann-Whitney U | 330170 |
26	| Mann-Whitney p | 1.90e-19 |
27	
28	**Interpretation:** Cohen's d = -0.17 indicates a negligible-to-small effect size (below the |d| = 0.2 "small" threshold). The overlap coefficient of 0.764 means 76.4% of the density mass is shared between cohorts. The Bhattacharyya coefficient of 0.961 (1.0 = identical distributions) confirms substantial distributional similarity.
29	
30	## Part 2: Ability-Restricted MH-DIF
31	
32	### 2a. Full Population (Baseline Verification)
33	
34	| ETS Class | Count | % |
35	|-----------|-------|---|
36	| A | 6332 | 50.6 |
37	| B | 2258 | 18.1 |
38	| C | 3918 | 31.3 |
39	
40	**Full C% = 31.3%** (matches plan_001)
41	
42	### 2b. Score-Range Restriction
43	
44	Restriction: total score ∈ [max(min_ref, min_foc), min(max_ref, max_foc)] = [0.2200, 0.8090]
45	
46	| | Reference | Focal |
47	|--|-----------|-------|
48	| N (full) | 1080 | 807 |
49	| N (restricted) | 1080 | 787 |
50	| Retained | 100.0% | 97.5% |
51	
52	Cohen's d (restricted) = -0.1488
53	
54	**Range-restricted C% = 30.9%** (essentially unchanged; only 20 extreme foc models excluded)
55	
56	### 2c. 1:1 Nearest-Neighbor Matching (Primary Ability Control)
57	
58	Caliper = 0.02 (max score difference between matched pairs). Five random seeds for robustness.
5
…[truncated 3070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 568 · 2026-05-23T19:54:33.883481+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-23T19:54:33.883602+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md",
  "description": "Read full mf2 practical significance report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md",
    "description": "Read full mf2 practical significance report"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-23T19:54:33.883745+00:00_

# MF2: Practical Significance — Stable-Item Rank Stability

## Per-Benchmark Results

| Benchmark | Items | C items | Stable | %C | Models | Spearman ρ | p-value | Kendall τ | Flip rate |
|-----------|------:|--------:|-------:|---:|-------:|-----------:|--------:|----------:|----------:|
| TruthfulQA | 817 | 243 | 574 | 29.74% | 5228 | 0.9971 | 0.00e+00 | 0.9586 | 0.0207 |
| WinoGrande | 1267 | 384 | 883 | 30.31% | 6558 | 0.9943 | 0.00e+00 | 0.9432 | 0.0284 |
| ARC | 1172 | 315 | 857 | 26.88% | 5227 | 0.9962 | 0.00e+00 | 0.9538 | 0.0231 |
| GSM8K | 1319 | 249 | 1070 | 18.88% | 6702 | 0.9993 | 0.00e+00 | 0.9843 | 0.0078 |
| HellaSwag | 10042 | 1797 | 8245 | 17.89% | 5227 | 0.9986 | 0.00e+00 | 0.9722 | 0.0139 |
| MMLU | 12508 | 3918 | 8590 | 31.32% | 5227 | 0.9965 | 0.00e+00 | 0.9600 | 0.0200 |

## Cross-Benchmark Summary

- **Mean Spearman ρ**: 0.9970 (range: 0.9943–0.9993)
- **Mean flip rate**: 0.0190 (range: 0.0078–0.0284)

## Interpretation

- **WinoGrande** shows the lowest ρ (0.9943) with 30.31% C items.
- **GSM8K** is the most stable (ρ=0.9993, flip rate=0.0078).
- Overall, removing ETS class C items produces minimal rank disruption (mean flip rate 0.0190), but the effect is benchmark-dependent.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-23T19:54:33.883898+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Paper says ρ=0.997, τ=0.958. From table: MMLU ρ=0.9965, τ=0.9600 (rounds to 0.997, 0.958-not quite)\n# Mean ρ=0.9970 (rounds to 0.997), mean τ is higher\n# Flip rate ≤2.8% — max is WinoGrande 2.84% (rounds to 2.8% or exceeds)\npython3 -c \"\nrhos = [0.9971, 0.9943, 0.9962, 0.9993, 0.9986, 0.9965]\ntaus = [0.9586, 0.9432, 0.9538, 0.9843, 0.9722, 0.9600]\nflips = [0.0207, 0.0284, 0.0231, 0.0078, 0.0139, 0.0200]\nprint(f'Min rho: {min(rhos):.4f}')\nprint(f'Max flip: {max(flips)*100:.2f}%')\nprint(f'Min tau: {min(taus):.4f}')\nprint('Paper says: rho=0.997, tau=0.958, flip<=2.8%')\nprint(f'WinoGrande flip: {0.0284*100:.2f}%')\n\"",
  "description": "Verify ρ=0.997, τ=0.958, flip≤2.8%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Paper says ρ=0.997, τ=0.958. From table: MMLU ρ=0.9965, τ=0.9600 (rounds to 0.997, 0.958-not quite)\n# Mean ρ=0.9970 (rounds to 0.997), mean τ is higher\n# Flip rate ≤2.8% — max is WinoGrande 2.84% (rounds to 2.8% or exceeds)\npython3 -c \"\nrhos = [0.9971, 0.9943, 0.9962, 0.9993, 0.9986, 0.9965]\ntaus = [0.9586, 0.9432, 0.9538, 0.9843, 0.9722, 0.9600]\nflips = [0.0207, 0.0284, 0.0231, 0.0078, 0.0139, 0.0200]\nprint(f'Min rho: {min(rhos):.4f}')\nprint(f'Max flip: {max(flips)*100:.2f}%')\nprint(f'Min tau: {min(taus):.4f}')\nprint('Paper says: rho=0.997, tau=0.958, flip<=2.8%')\nprint(f'WinoGrande flip: {0.0284*100:.2f}%')\n\"",
    "description": "Verify ρ=0.997, τ=0.958, flip≤2.8%"
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-23T19:54:33.884026+00:00_

Min rho: 0.9943
Max flip: 2.84%
Min tau: 0.9432
Paper says: rho=0.997, tau=0.958, flip<=2.8%
WinoGrande flip: 2.84%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 573 · 2026-05-23T19:54:33.884164+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check z=-8 to -49 for discriminative signal concentration\ngrep -rn \"z.*=.*-8\\|z.*-8\\|-8.*to.*-49\\|-49\\|discrimin.*signal\\|z.score\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -15",
  "description": "Find z=-8 to -49 discriminative signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check z=-8 to -49 for discriminative signal concentration\ngrep -rn \"z.*=.*-8\\|z.*-8\\|-8.*to.*-49\\|-49\\|discrimin.*signal\\|z.score\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | head -15",
    "description": "Find z=-8 to -49 discriminative signal"
  }
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-23T19:54:33.884304+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results.md:95:- **Interpretation**: difficulty is the primary linear predictor, but GBM captures non-linear interactions (e.g., difficulty × discrimination, within-subject deviations) that improve classification. The features provide complementary signal through interactions, not additive linear effects.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/rank_shift_distribution_report.md:66:| deepseek | 24 | -1.0 | -1 | 19.9 | -49 | +68 | -22 | +15 |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/circularity_ablation_report.md:70:1. **DIF removal is the least disruptive non-random strategy.** Across all cohorts, DIF-C removal produces the highest ρ (least perturbation) among the four targeted strategies. In the 2024 cohort: DIF ρ = 0.9970 vs accuracy gap ρ = 0.9657, discrimination ρ = 0.9957, variance ρ = 0.9761. The z-scores tell the same story: DIF z = −9.5 vs accuracy gap z = −157, discrimination z = −16, variance z = −108.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_020/circularity_ablation_report.md:70:1. **DIF removal is the least disruptive non-random strategy.** Across all cohorts, DIF-C removal produces the highest ρ (least perturbation) among the four targeted strategies. In the 2024 cohort: DIF ρ = 0.9970 vs accuracy gap ρ = 0.9657, discrimination ρ = 0.9957, variance ρ = 0.9761. The z-scores tell the same story: DIF z = −9.5 vs accuracy gap z = −157, discrimination z = −16, variance z = −108.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_report.md:121:9. **§4.5, "DIF as diagnostic, not filter":** The z-score comparisons (DIF removal z=−8 to −49σ vs. accuracy-gap removal z=−157) effect
…[truncated 6226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-23T19:54:33.884458+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_lofo_power_calibration/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_lofo_power_calibration/",
  "description": "Check mf1_lofo_power_calibration directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_lofo_power_calibration/ 2>/dev/null || ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_lofo_power_calibration/",
    "description": "Check mf1_lofo_power_calibration directory"
  }
}
```

</details>

---


### Tool result

_source line 576 · 2026-05-23T19:54:33.884577+00:00_

mf1_lofo_power_calibration.py
power_calibration_report.md
power_calibration_reps.csv
power_calibration_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-23T19:54:33.884726+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Paper text says: '1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9%'\n# Source: plan_027 shows Cohen's d of temporal cohorts = -0.1729 (full distribution)\n# After NN matching, d = -0.0096 (mean of 5 seeds)\n# Paper's 'd = -0.17' refers to the UNMATCHED Cohen's d (from plan_027 part 1)\n# which is the original temporal cohort difference, not after matching\n\n# So in the text: 'matched on total score (N=638/group, Cohen's d = -0.17)' \n# seems to be saying ORIGINAL d=-0.17 AND THEN matched to N=638\n# Actually it should say d≈0 after matching, and d=-0.17 before\n# The way it's written is ambiguous/misleading but not strictly wrong if they mean\n# 'original cohort diff was -0.17, we matched to 638/group'\n\n# Now: Table 2 'Matched-ability | ~0.31'\n# The temporal overlap report shows NN matched C% = 28.9%\n# Not 31%. \n# The only values close to 31% are: original C%=31.3%, range-restricted C%=30.9%\n# r22 composition-balanced: 30.25%\n# None of these is 'matched-ability within-quintile temp DIF'\n\n# Let me check if perhaps table 2 was derived from a different analysis\n# Looking at plan_001b: CMH approach = 33.3%, Q2-only = 34.4%, Q5-only = 30.2%\n# The closest to ~0.31 is CMH=33.3% or Q5=30.2%\n\n# OR: maybe '~0.31' is just saying 'same as baseline ~31%', not claiming exact value\n# The footnote says 'none reduces C% below 31%'\nprint('Table 2 matched-ability ~0.31 analysis:')\nprint('  NN matched C% = 28.9% (plan_027)')\nprint('  CMH quintile C% = 33.3% (plan_001b)')  \nprint('  r22 composition balanced = 30.25%')\nprint('  Claim ~0.31 (31%) does not precisely match any single source')\nprint('  Most authoritative matched value is 28.9% (NN matching, plan_027)')\n\"\n",
  "description": "Analyze ~0.31 discrepancy for matched-ability row"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Paper text says: '1:1 nearest-neighbor matching on total score (N=638/group, Cohen's d = -0.17) yields C% = 28.9%'\n# Source: plan_027 shows Cohen's d of temporal cohorts = -0.1729 (full distribution)\n# After NN matching, d = -0.0096 (mean of 5 seeds)\n# Paper's 'd = -0.17' refers to the UNMATCHED Cohen's d (from plan_027 part 1)\n# which is the original temporal cohort difference, not after matching\n\n# So in the text: 'matched on total score (N=638/group, Cohen's d = -0.17)' \n# seems to be saying ORIGINAL d=-0.17 AND THEN matched to N=638\n# Actually it should say d≈0 after matching, and d=-0.17 before\n# The way it's written is ambiguous/misleading but not strictly wrong if they mean\n# 'original cohort diff was -0.17, we matched to 638/group'\n\n# Now: Table 2 'Matched-ability | ~0.31'\n# The temporal overlap report shows NN matched C% = 28.9%\n# Not 31%. \n# The only values close to 31% are: original C%=31.3%, range-restricted C%=30.9%\n# r22 composition-balanced: 30.25%\n# None of these is 'matched-ability within-quintile temp DIF'\n\n# Let me check if perhaps table 2 was derived from a different analysis\n# Looking at plan_001b: CMH approach = 33.3%, Q2-only = 34.4%, Q5-only = 30.2%\n# The closest to ~0.31 is CMH=33.3% or Q5=30.2%\n\n# OR: maybe '~0.31' is just saying 'same as baseline ~31%', not claiming exact value\n# The footnote says 'none reduces C% below 31%'\nprint('Table 2 matched-ability ~0.31 analysis:')\nprint('  NN matched C% = 28.9% (plan_027)')\nprint('  CMH quintile C% = 33.3% (plan_001b)')  \nprint('  r22 composition balanced = 30.25%')\nprint('  Claim ~0.31 (31%) does not precisely match any single source')\nprint('  Most authoritative matched value is 28.9% (NN matching, plan_027)')\n\"\n",
    "description": "Analyze ~0.31 discrepancy for matched-ability row"
  }
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-23T19:54:33.884889+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_lofo_power_calibration/power_calibration_report.md | head -50",
  "description": "Read power calibration report for z scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_lofo_power_calibration/power_calibration_report.md | head -50",
    "description": "Read power calibration report for z scores"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-23T19:54:33.885047+00:00_

# MF1: LOFO Power Calibration — Random Subsample Baseline

## Method

Random subsample on real response matrix (12508 items, 200 reps per scenario).
For each LOFO scenario, draw the same number of models randomly (without targeting any family)
and compute MH-DIF C%. The gap between random subsample and observed LOFO isolates the
composition effect from the pure power (sample-size) effect.

- Full baseline: N_ref=1080, N_foc=807 → C%=31.32%
- MH-DIF: 5-stratum total-score matching, ETS C classification (|Δ_MH|≥1.5, p<0.05)

## Results

| | Full Baseline | Random Subsample (mean±SD) | LOFO Observed | Power Effect | Composition Effect |
|---|---|---|---|---|---|
| Remove Mistral (N_ref: 1080→533) | 31.32% | 30.91±2.07% | 22.47% | -0.41pp | -8.44pp |
| Remove Llama-3 (N_foc: 807→492) | 31.32% | 32.24±1.42% | 24.06% | +0.91pp | -8.17pp |

## Decomposition

**Mistral removal** (total drop: -8.85pp):
- Power effect (random subsample − full): -0.41pp (5%)
- Composition effect (LOFO − random subsample): -8.44pp (95%)

**Llama-3 removal** (total drop: -7.26pp):
- Power effect (random subsample − full): +0.91pp (-13%)
- Composition effect (LOFO − random subsample): -8.17pp (113%)

## Interpretation

Both scenarios show composition effects beyond pure power reduction, confirming that family-specific removal changes DIF detection beyond what sample size alone explains.

Random subsample 95% range:
- Scenario A (Mistral): [27.33%, 34.76%]
- Scenario B (Llama-3): [29.65%, 35.02%]

LOFO observed falls below the random subsample 95% range for Mistral.
LOFO observed falls below the random subsample 95% range for Llama-3.

Runtime: 0.3 min (200 reps × 2 scenarios)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-23T19:54:33.885249+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find z=-8 to -49 range from plan_017\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017_supplement/ 2>/dev/null",
  "description": "Check plan_017 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find z=-8 to -49 range from plan_017\nls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/ && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017_supplement/ 2>/dev/null",
    "description": "Check plan_017 directory"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-23T19:54:33.885383+00:00_

Table 2 matched-ability ~0.31 analysis:
  NN matched C% = 28.9% (plan_027)
  CMH quintile C% = 33.3% (plan_001b)
  r22 composition balanced = 30.25%
  Claim ~0.31 (31%) does not precisely match any single source
  Most authoritative matched value is 28.9% (NN matching, plan_027)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-23T19:54:33.885516+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let me also check the Llama-3 N count discrepancy more carefully\n# Paper says 161/308, plan_027 shows 161/315, model_metadata shows 315 for llama-3\n# Let me see if there's an older analysis with 308\n\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '308' in content and 'llama' in content.lower():\n            print(f)\n    except:\n        pass\n\" | head -10\n",
  "description": "Search for any analysis using Llama-3 N=308"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let me also check the Llama-3 N count discrepancy more carefully\n# Paper says 161/308, plan_027 shows 161/315, model_metadata shows 315 for llama-3\n# Let me see if there's an older analysis with 308\n\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '308' in content and 'llama' in content.lower():\n            print(f)\n    except:\n        pass\n\" | head -10\n",
    "description": "Search for any analysis using Llama-3 N=308"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-23T19:54:33.885648+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004_data_availability.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/metabench_data_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/metabench_data_summary_ec3bbf.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_data_availability.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-23T19:54:33.885815+00:00_

data
intermediate
plan_017_downstream_impact.py
plan_017_report.md
progressive_removal.csv
random_baseline.csv
rank_movers.csv
ranking_comparison.csv
report
rank_shift_analysis.py
rank_shift_distribution_report.md
rank_shift_stats.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 585 · 2026-05-23T19:54:33.885948+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/*.md 2>/dev/null | head -60; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/",
  "description": "Read plan_017 report for z-scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/*.md 2>/dev/null | head -60; ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/",
    "description": "Read plan_017 report for z-scores"
  }
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-23T19:54:33.886082+00:00_

# plan_017: Downstream Impact Analysis — DIF Item Removal → Ranking Stability

## Summary

This analysis evaluates whether removing temporally unstable (DIF) items from MMLU
produces more stable and reliable model rankings.


## Data

- Response matrix: 5227 models × 12508 items
- Temporal cohorts: 2023 (1080 models), 2024 (807 models)
- DIF classification: ETS A=6332, B=2258, C=3918
- Stable items (A+B): 8590 (68.7%)
- DIF items (C): 3918 (31.3%)


## Part 1: Full vs Stable-Only Ranking

| Cohort | N models | ρ(full, stable) | 95% CI | SHR full | SHR stable |
|--------|----------|-----------------|--------|----------|------------|
| 2023 | 1080 | 0.998851 | [0.998490, 0.999028] | 0.9970±0.0005 | 0.9955±0.0007 |
| 2024 | 807 | 0.997014 | [0.995997, 0.997642] | 0.9923±0.0024 | 0.9890±0.0030 |
| all | 5227 | 0.996451 | [0.995977, 0.996808] | 0.9934±0.0018 | 0.9919±0.0016 |


## Part 2: Progressive DIF Removal

| Frac | Removed | Remaining | Cohort | ρ(full, reduced) | 95% CI |
|------|---------|-----------|--------|------------------|--------|
| 0.00 | 0 | 12508 | 2023 | 1.000000 | [1.000000, 1.000000] |
| 0.00 | 0 | 12508 | 2024 | 1.000000 | [1.000000, 1.000000] |
| 0.00 | 0 | 12508 | all | 1.000000 | [1.000000, 1.000000] |
| 0.05 | 625 | 11883 | 2023 | 0.999846 | [0.999777, 0.999862] |
| 0.05 | 625 | 11883 | 2024 | 0.999351 | [0.999033, 0.999458] |
| 0.05 | 625 | 11883 | all | 0.998926 | [0.998730, 0.999062] |
| 0.10 | 1250 | 11258 | 2023 | 0.999641 | [0.999498, 0.999707] |
| 0.10 | 1250 | 11258 | 2024 | 0.998676 | [0.998120, 0.998969] |
| 0.10 | 1250 | 11258 | all | 0.997700 | [0.997313, 0.997990] |
| 0.15 | 1876 | 10632 | 2023 | 0.999458 | [0.999283, 0.999545] |
| 0.15 | 1876 | 10632 | 2024 | 0.997849 | [0.996921, 0.998397] |
| 0.15 | 1876 | 10632 | all | 0.997698 | [0.997344, 0.997998] |
| 0.20 | 2501 | 10007 | 2023 | 0.999344 | [0.999157, 0.999426] |
| 0.20 | 2501 | 10007 | 2024 | 0.997483 | [0.996414, 0.998024] |
| 0.20 | 2501 | 10007 | all | 0.997397 | [0.9970
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 587 · 2026-05-23T19:54:33.886240+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md') as f:\n    content = f.read()\nidx = content.find('308')\nif idx >= 0:\n    print(content[max(0,idx-200):idx+300])\n\"\n",
  "description": "Check metabench data summary for 308 value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md') as f:\n    content = f.read()\nidx = content.find('308')\nif idx >= 0:\n    print(content[max(0,idx-200):idx+300])\n\"\n",
    "description": "Check metabench data summary for 308 value"
  }
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-23T19:54:33.886371+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/plan_017_report.md | grep -A 30 \"Part 3\\|z.score\\|z =\"",
  "description": "Find z-scores in plan_017 report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/plan_017_report.md | grep -A 30 \"Part 3\\|z.score\\|z =\"",
    "description": "Find z-scores in plan_017 report"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-23T19:54:33.886495+00:00_

## Part 3: DIF vs Random Removal Comparison

Negative z-score = DIF removal causes *more* rank disruption than random.

| Frac | Cohort | ρ DIF | ρ Random (mean±std) | z-score |
|------|--------|-------|---------------------|---------|
| 0.05 | 2023 | 0.999846 | 0.999942±0.000009 | -10.20 |
| 0.05 | 2024 | 0.999351 | 0.999844±0.000042 | -11.70 |
| 0.05 | all | 0.998926 | 0.999886±0.000033 | -29.07 |
| 0.10 | 2023 | 0.999641 | 0.999898±0.000010 | -25.12 |
| 0.10 | 2024 | 0.998676 | 0.999727±0.000095 | -11.00 |
| 0.10 | all | 0.997700 | 0.999795±0.000042 | -49.44 |
| 0.15 | 2023 | 0.999458 | 0.999823±0.000031 | -11.71 |
| 0.15 | 2024 | 0.997849 | 0.999552±0.000151 | -11.28 |
| 0.15 | all | 0.997698 | 0.999611±0.000157 | -12.22 |
| 0.20 | 2023 | 0.999344 | 0.999774±0.000046 | -9.42 |
| 0.20 | 2024 | 0.997483 | 0.999415±0.000152 | -12.72 |
| 0.20 | all | 0.997397 | 0.999477±0.000171 | -12.15 |
| 0.25 | 2023 | 0.999192 | 0.999713±0.000040 | -12.89 |
| 0.25 | 2024 | 0.997558 | 0.999247±0.000203 | -8.33 |
| 0.25 | all | 0.997049 | 0.999370±0.000163 | -14.26 |
| 0.30 | 2023 | 0.998865 | 0.999648±0.000041 | -19.02 |
| 0.30 | 2024 | 0.997229 | 0.999084±0.000227 | -8.16 |
| 0.30 | all | 0.996451 | 0.999219±0.000244 | -11.35 |
| 0.38 | 2023 | 0.998644 | 0.999499±0.000065 | -13.18 |
| 0.38 | 2024 | 0.995266 | 0.998777±0.000326 | -10.76 |
| 0.38 | all | 0.996645 | 0.998850±0.000241 | -9.16 |


## Part 4: Top Rank Movers (all models, full → stable-only)

### Biggest rank *drops* (benefited from DIF items)

| Model | Family | Method | Rank Full | Rank Stable | ΔRank |
|-------|--------|--------|-----------|-------------|-------|
--
4. **Average z-score (DIF vs random)**: -14.91
5. **Cross-cohort stability**: DIF items show 1.09× the accuracy shift of full benchmark; stable items show 0.96×
6. **Top-50 rank movers** dominant training methods: unknown (49), DPO (1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 590 · 2026-05-23T19:54:33.886639+00:00_

 models — the dataset likely predates most 2024-H2 releases. The bulk of classified 2024 models are from H1.

### Top Families

| Family | Count |
|--------|-------|
| mistral-0.1 | 400 |
| llama-3 | 308 |
| llama-2 | 161 |
| llama-1 | 135 |
| mixtral-8x7B | 130 |
| solar | 92 |
| zephyr | 85 |
| qwen-1.5 | 67 |
| phi-2 | 60 |

### Alternative Cohort Strategy

Since 63% of models are unclassified, **name-based cohort assignment is insufficient for fine-grained temporal analysis**. Consider:
1. U

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 591 · 2026-05-23T19:54:33.886807+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/plan_017_report.md | grep -A 60 \"Part 3\"",
  "description": "Read Part 3 of plan_017 report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/plan_017_report.md | grep -A 60 \"Part 3\"",
    "description": "Read Part 3 of plan_017 report"
  }
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-23T19:54:33.886941+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Let me check the exact Llama counts from an earlier analysis\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md') as f:\n    content = f.read()\nidx = content.find('308')\nif idx >= 0:\n    print('Found 308 in within_family_report:')\n    print(content[max(0,idx-200):idx+300])\nelse:\n    print('308 not found in within_family_report')\n    # Find llama-3 N count\n    idx = content.find('Llama-3')\n    if idx < 0:\n        idx = content.find('llama-3')\n    print(content[max(0,idx-50):idx+200])\n\"\n",
  "description": "Check within_family_report for Llama-3 N count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Let me check the exact Llama counts from an earlier analysis\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/within_family_report.md') as f:\n    content = f.read()\nidx = content.find('308')\nif idx >= 0:\n    print('Found 308 in within_family_report:')\n    print(content[max(0,idx-200):idx+300])\nelse:\n    print('308 not found in within_family_report')\n    # Find llama-3 N count\n    idx = content.find('Llama-3')\n    if idx < 0:\n        idx = content.find('llama-3')\n    print(content[max(0,idx-50):idx+200])\n\"\n",
    "description": "Check within_family_report for Llama-3 N count"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-23T19:54:33.887078+00:00_

## Part 3: DIF vs Random Removal Comparison

Negative z-score = DIF removal causes *more* rank disruption than random.

| Frac | Cohort | ρ DIF | ρ Random (mean±std) | z-score |
|------|--------|-------|---------------------|---------|
| 0.05 | 2023 | 0.999846 | 0.999942±0.000009 | -10.20 |
| 0.05 | 2024 | 0.999351 | 0.999844±0.000042 | -11.70 |
| 0.05 | all | 0.998926 | 0.999886±0.000033 | -29.07 |
| 0.10 | 2023 | 0.999641 | 0.999898±0.000010 | -25.12 |
| 0.10 | 2024 | 0.998676 | 0.999727±0.000095 | -11.00 |
| 0.10 | all | 0.997700 | 0.999795±0.000042 | -49.44 |
| 0.15 | 2023 | 0.999458 | 0.999823±0.000031 | -11.71 |
| 0.15 | 2024 | 0.997849 | 0.999552±0.000151 | -11.28 |
| 0.15 | all | 0.997698 | 0.999611±0.000157 | -12.22 |
| 0.20 | 2023 | 0.999344 | 0.999774±0.000046 | -9.42 |
| 0.20 | 2024 | 0.997483 | 0.999415±0.000152 | -12.72 |
| 0.20 | all | 0.997397 | 0.999477±0.000171 | -12.15 |
| 0.25 | 2023 | 0.999192 | 0.999713±0.000040 | -12.89 |
| 0.25 | 2024 | 0.997558 | 0.999247±0.000203 | -8.33 |
| 0.25 | all | 0.997049 | 0.999370±0.000163 | -14.26 |
| 0.30 | 2023 | 0.998865 | 0.999648±0.000041 | -19.02 |
| 0.30 | 2024 | 0.997229 | 0.999084±0.000227 | -8.16 |
| 0.30 | all | 0.996451 | 0.999219±0.000244 | -11.35 |
| 0.38 | 2023 | 0.998644 | 0.999499±0.000065 | -13.18 |
| 0.38 | 2024 | 0.995266 | 0.998777±0.000326 | -10.76 |
| 0.38 | all | 0.996645 | 0.998850±0.000241 | -9.16 |


## Part 4: Top Rank Movers (all models, full → stable-only)

### Biggest rank *drops* (benefited from DIF items)

| Model | Family | Method | Rank Full | Rank Stable | ΔRank |
|-------|--------|--------|-----------|-------------|-------|
| Sao10K/14B-Glacier-Stack | unknown | unknown | 555 | 1406 | +851 |
| AA051611/A0118 | unknown | unknown | 1169 | 1996 | +827 |
| DeepMount00/phi_3 | phi-3 | unknown | 736 | 1545 | +809 |
| Mihaiii/Pallas-0.5-frankenmerge | unknown | unknown | 455 | 1264 | +809 |
| DeepMount00/Phi-3-Mini-4K-Boost | phi-3 | unknown | 738 | 1546 | +808 |
| vonjack/phi-3-mini
…[truncated 1398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-23T19:54:33.887222+00:00_

308 not found in within_family_report
# Plan 024: Within-Family Deep Dive — Llama-2 vs Llama-3

## Part 1: Llama-2 vs Llama-3

### Score Distributions

| Metric | Llama-2 (N=161) | Llama-3 (N=315) |
|--------|------------|------------|
| Mean accuracy | 0.5269 | 0.6475 |
| SD | 0.1135 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-23T19:54:33.887361+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# So metabench_data_summary shows Llama-3: 308 in an earlier version\n# But plan_024 report and model_metadata show 315 (exact llama-3 label)\n# The earlier count of 308 might be from a previous data version\n# or might exclude certain sub-variants\n\n# Let me check the metabench_data_summary.md for the full context\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md') as f:\n    content = f.read()\n# Find the section with 308\nidx = content.find('308')\nprint(content[max(0,idx-500):idx+500])\n\"\n",
  "description": "Get context around 308 in metabench data summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# So metabench_data_summary shows Llama-3: 308 in an earlier version\n# But plan_024 report and model_metadata show 315 (exact llama-3 label)\n# The earlier count of 308 might be from a previous data version\n# or might exclude certain sub-variants\n\n# Let me check the metabench_data_summary.md for the full context\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md') as f:\n    content = f.read()\n# Find the section with 308\nidx = content.find('308')\nprint(content[max(0,idx-500):idx+500])\n\"\n",
    "description": "Get context around 308 in metabench data summary"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-23T19:54:33.887492+00:00_

 and unrecognizable names.

### Annual Cohorts

| Year | N models | N ≥ 80? |
|------|----------|---------|
| 2021 | 5 | No |
| 2022 | 13 | No |
| 2023 | 1,253 | **Yes** |
| 2024 | 658 | **Yes** |

**Two annual cohorts meet the N≥80 threshold (2023 and 2024).** However, 2024-H2 only has 2 classified models — the dataset likely predates most 2024-H2 releases. The bulk of classified 2024 models are from H1.

### Top Families

| Family | Count |
|--------|-------|
| mistral-0.1 | 400 |
| llama-3 | 308 |
| llama-2 | 161 |
| llama-1 | 135 |
| mixtral-8x7B | 130 |
| solar | 92 |
| zephyr | 85 |
| qwen-1.5 | 67 |
| phi-2 | 60 |

### Alternative Cohort Strategy

Since 63% of models are unclassified, **name-based cohort assignment is insufficient for fine-grained temporal analysis**. Consider:
1. Using accuracy-based quintiles as proxy cohorts
2. Using the RDS train/test split directly (4755/464)
3. Cross-referencing with HuggingFace Hub metadata for release dates

## RL-trained Models

**477 m

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-23T19:54:33.887638+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check difficulty-dependent ΔTPR≈0.41 vs 0.51 from mixed_mechanism_semisynthetic\n# already read: scheme_d C%=35.3, scheme_e C%=34.1 - need ΔTPR at p=0.5\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/scheme_d_results.csv | head -10",
  "description": "Check scheme_d results for ΔTPR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check difficulty-dependent ΔTPR≈0.41 vs 0.51 from mixed_mechanism_semisynthetic\n# already read: scheme_d C%=35.3, scheme_e C%=34.1 - need ΔTPR at p=0.5\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/scheme_d_results.csv | head -10",
    "description": "Check scheme_d results for ΔTPR"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-23T19:54:33.887799+00:00_

scheme,seed,n_inject_base,n_inject_instruct,n_inject_items,n_flipped_base,n_flipped_instruct,n_flipped_total,rho_overall,rho_ddelta_overall,c_pct_overall,n_c_overall,pct_focal_overall,rho_base,rho_ddelta_base,c_pct_base,n_c_base,pct_focal_base,rho_instruct,rho_ddelta_instruct,c_pct_instruct,n_c_instruct,pct_focal_instruct,chi2_reversal,p_reversal,elapsed_sec
D_base_diff_instruct_unif,1,164,77,3001,121757,42312,164069,-0.6735766716170853,-0.9060160459082353,34.97761432683083,4375,43.93142857142857,-0.6355133078992963,-0.8793040209009231,37.671889990406136,4712,38.00933786078098,-0.27937425533319565,-0.7134855154281844,37.783818356252,4726,65.7638595006348,726.968192629643,4.0874241186018946e-160,1.2172610759735107
D_base_diff_instruct_unif,2,164,77,3001,122355,45089,167444,-0.6767212897484215,-0.8768636596121858,34.09018228333866,4264,45.1219512195122,-0.6332638419776755,-0.8545627272755317,36.39270866645347,4552,38.02724077328647,-0.36042686129537177,-0.7021758032690065,37.4080588423409,4679,64.00940371874331,622.359608284548,2.2937839275193187e-137,1.22713041305542
D_base_diff_instruct_unif,3,164,77,3001,127411,44847,172258,-0.673697292060372,-0.8951509314753945,34.98560921010554,4376,43.4872029250457,-0.6281342399521531,-0.8253091268320575,36.23281100095939,4532,39.58517210944395,-0.39140164428161694,-0.7916825255725379,37.42404860889031,4681,61.58940397350994,445.18862778076607,8.039252959609924e-99,1.8680834770202637
D_base_diff_instruct_unif,4,164,77,3001,125098,45684,170782,-0.6812021862759863,-0.9364059677613089,38.367444835305406,4799,40.987705772035845,-0.6371712040402486,-0.8987114284346627,39.66261592580748,4961,36.86756702277766,-0.3631442193558,-0.7297062634938113,37.927726255196674,4744,62.98482293423272,660.6488983400108,1.079479216766851e-145,1.7706491947174072
D_base_diff_instruct_unif,5,164,77,3001,123615,43879,167494,-0.6729273848106917,-0.9043539630705516,34.769747361688516,4349,43.435272476431365,-0.6391666216463695,-0.9090979997930986,38.575311
…[truncated 1626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-23T19:54:33.887955+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/all_results.csv | head -20",
  "description": "Read all_results from mixed mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/all_results.csv | head -20",
    "description": "Read all_results from mixed mechanism"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-23T19:54:33.888099+00:00_

scheme,seed,n_inject_base,n_inject_instruct,n_inject_items,n_flipped_base,n_flipped_instruct,n_flipped_total,rho_overall,rho_ddelta_overall,c_pct_overall,n_c_overall,pct_focal_overall,rho_base,rho_ddelta_base,c_pct_base,n_c_base,pct_focal_base,rho_instruct,rho_ddelta_instruct,c_pct_instruct,n_c_instruct,pct_focal_instruct,chi2_reversal,p_reversal,elapsed_sec
D_base_diff_instruct_unif,1,164,77,3001,121757,42312,164069,-0.6735766716170853,-0.9060160459082353,34.97761432683083,4375,43.93142857142857,-0.6355133078992963,-0.8793040209009231,37.671889990406136,4712,38.00933786078098,-0.27937425533319565,-0.7134855154281844,37.783818356252,4726,65.7638595006348,726.968192629643,4.0874241186018946e-160,1.2172610759735107
E_base_unif_instruct_diff,1,164,77,3001,98906,55180,154086,-0.6637790191129412,-0.7040291970339788,33.82635113527343,4231,46.18293547624675,-0.6240648314230977,-0.4352522706622211,34.56987527982092,4324,41.327474560592044,-0.40954031812586555,-0.8774893357003645,38.48736808442597,4814,62.06896551724138,391.9625781630919,3.0947411813138303e-87,1.2993569374084473
D_base_diff_instruct_unif,2,164,77,3001,122355,45089,167444,-0.6767212897484215,-0.8768636596121858,34.09018228333866,4264,45.1219512195122,-0.6332638419776755,-0.8545627272755317,36.39270866645347,4552,38.02724077328647,-0.36042686129537177,-0.7021758032690065,37.4080588423409,4679,64.00940371874331,622.359608284548,2.2937839275193187e-137,1.22713041305542
E_base_unif_instruct_diff,2,164,77,3001,95039,57282,152321,-0.6675497546683294,-0.7394232757594663,33.00287815797889,4128,46.51162790697674,-0.6254834736704104,-0.45785404416132414,33.490566037735846,4189,41.298639293387446,-0.495911501847601,-0.9229235206212875,38.48736808442597,4814,59.098462816784384,283.234671593744,1.481560332046404e-63,1.2114250659942627
D_base_diff_instruct_unif,3,164,77,3001,127411,44847,172258,-0.673697292060372,-0.8951509314753945,34.98560921010554,4376,43.4872029250457,-0.6281342399521531,-0.8253091268320575,36.23281100
…[truncated 5258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-23T19:54:33.888254+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Also verify the ±800 individual displacements claim from score_inflation_report\n# score_inflation_report says: \"individual displacements exceeding ±561 positions (99th percentile)\"\n# but paper says \"±800\". Let me check more carefully.\ngrep -n \"800\\|±800\\|99th\\|percentile\\|max.*rank\\|rank.*max\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md | head -10",
  "description": "Verify ±800 individual displacements in score inflation report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Also verify the ±800 individual displacements claim from score_inflation_report\n# score_inflation_report says: \"individual displacements exceeding ±561 positions (99th percentile)\"\n# but paper says \"±800\". Let me check more carefully.\ngrep -n \"800\\|±800\\|99th\\|percentile\\|max.*rank\\|rank.*max\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md | head -10",
    "description": "Verify ±800 individual displacements in score inflation report"
  }
}
```

</details>

---


### Tool result

_source line 602 · 2026-05-23T19:54:33.888387+00:00_

90:Despite measurable score changes, the overall ranking is highly preserved (ρ = 0.9965), indicating that DIF primarily shifts absolute scores rather than relative ordering. However, individual models can experience rank displacements exceeding ±561 positions (99th percentile).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-23T19:54:33.888525+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# So the earlier metabench_data_summary.md shows llama-3 N=308\n# But the current model_metadata.csv (which was updated) shows 315 for 'llama-3'\n# The paper says 161/308 which matches the earlier count from metabench_data_summary\n\n# The plan_024 report shows 161/315 suggesting model_metadata was updated after the initial analysis\n# Let me check if there's a plan_001 run that used 308 models\n\n# Actually: within_family_dif.csv shows 12508 rows for llama-2 vs llama-3\n# that means MH was run on ALL items for that family comparison\n# The 161 vs 315/308 is just counting unique models\n\n# The key question: does the actual MH DIF run use 308 or 315 models?\n# plan_001_analysis.py uses model_metadata.csv for grouping\n\n# Let me check the current model_metadata llama-3 count again\nimport csv\nllama3 = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row.get('family','').lower() == 'llama-3':\n            llama3 += 1\nprint(f'model_metadata llama-3: {llama3}')\n\n# But what about the within_family analysis - what was run when?\n# Let me check the plan_001 report which was output around the same time\n# plan_001_report mentions llama-2 vs llama-3: C=7672 (61.34%)\n# C% = 61.34% which matches the table 61.3%\n\n# plan_027 report says 161/315\n# metabench_data_summary says 308 (older)\n# paper says 308\n# model_metadata shows 315\n\n# This is a real discrepancy: the paper likely used an old metadata file with 308\n\nprint('DISCREPANCY: paper uses 308 but current model_metadata has 315')\nprint('The 61.3% C% figure is consistent across analyses')\n\"\n",
  "description": "Investigate Llama-3 count discrepancy between paper and source data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# So the earlier metabench_data_summary.md shows llama-3 N=308\n# But the current model_metadata.csv (which was updated) shows 315 for 'llama-3'\n# The paper says 161/308 which matches the earlier count from metabench_data_summary\n\n# The plan_024 report shows 161/315 suggesting model_metadata was updated after the initial analysis\n# Let me check if there's a plan_001 run that used 308 models\n\n# Actually: within_family_dif.csv shows 12508 rows for llama-2 vs llama-3\n# that means MH was run on ALL items for that family comparison\n# The 161 vs 315/308 is just counting unique models\n\n# The key question: does the actual MH DIF run use 308 or 315 models?\n# plan_001_analysis.py uses model_metadata.csv for grouping\n\n# Let me check the current model_metadata llama-3 count again\nimport csv\nllama3 = 0\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        if row.get('family','').lower() == 'llama-3':\n            llama3 += 1\nprint(f'model_metadata llama-3: {llama3}')\n\n# But what about the within_family analysis - what was run when?\n# Let me check the plan_001 report which was output around the same time\n# plan_001_report mentions llama-2 vs llama-3: C=7672 (61.34%)\n# C% = 61.34% which matches the table 61.3%\n\n# plan_027 report says 161/315\n# metabench_data_summary says 308 (older)\n# paper says 308\n# model_metadata shows 315\n\n# This is a real discrepancy: the paper likely used an old metadata file with 308\n\nprint('DISCREPANCY: paper uses 308 but current model_metadata has 315')\nprint('The 61.3% C% figure is consistent across analyses')\n\"\n",
    "description": "Investigate Llama-3 count discrepancy between paper and source data"
  }
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-23T19:54:33.888671+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check ±800 claim - max rank displacement in score_inflation_report\ngrep -n \"800\\|849\\|Max\\|max.*rank\\|rank.*max\\|max.*disp\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md | head -10",
  "description": "Check max rank displacement in score inflation report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check ±800 claim - max rank displacement in score_inflation_report\ngrep -n \"800\\|849\\|Max\\|max.*rank\\|rank.*max\\|max.*disp\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md | head -10",
    "description": "Check max rank displacement in score inflation report"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-23T19:54:33.888813+00:00_

model_metadata llama-3: 315
DISCREPANCY: paper uses 308 but current model_metadata has 315
The 61.3% C% figure is consistent across analyses

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-23T19:54:33.888924+00:00_

61:| Sao10K/14B-Glacier-Stack | other | base | 0.7047 | 0.7168 | +1.20 | -849 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-23T19:54:33.889050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# From plan_032 cleaned_mmlu_analysis: Min: -589 | Max: 849 (from report)\n# From score_inflation_report: max rank disp = 593 (upward). But plan_032 says max=849 displacement\n# The ±800 claim in the paper refers to the max displacement, not 99th percentile\n# Let me verify from plan_032 main report\ngrep -n \"±800\\|±561\\|max.*rank\\|849\\|589\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md | head -5\ngrep -n \"849\\|rank.*max\\|Max.*rank\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md | head -10",
  "description": "Find max rank displacement values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# From plan_032 cleaned_mmlu_analysis: Min: -589 | Max: 849 (from report)\n# From score_inflation_report: max rank disp = 593 (upward). But plan_032 says max=849 displacement\n# The ±800 claim in the paper refers to the max displacement, not 99th percentile\n# Let me verify from plan_032 main report\ngrep -n \"±800\\|±561\\|max.*rank\\|849\\|589\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md | head -5\ngrep -n \"849\\|rank.*max\\|Max.*rank\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md | head -10",
    "description": "Find max rank displacement values"
  }
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-23T19:54:33.889193+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Let me check what the actual within_family_dif.csv used for N counts\n# The DIF results are per-item so we can't directly get N_models from it\n# But the plan_001 report only mentions the %C, not the model counts\n# Let me look for a report or log that explicitly states model counts for families\n\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\n\n# Check all markdown files for '161 / 315' or '161/315' or '161 / 308'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '161 / 315' in content or '161/315' in content:\n            print(f'FOUND 161/315: {f}')\n        if '161 / 308' in content or '161/308' in content:\n            print(f'FOUND 161/308: {f}')\n    except:\n        pass\n\"\n",
  "description": "Search for explicit Llama N count references in all reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Let me check what the actual within_family_dif.csv used for N counts\n# The DIF results are per-item so we can't directly get N_models from it\n# But the plan_001 report only mentions the %C, not the model counts\n# Let me look for a report or log that explicitly states model counts for families\n\npython3 -c \"\nimport os, glob\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/'\n\n# Check all markdown files for '161 / 315' or '161/315' or '161 / 308'\nfor f in glob.glob(base + '**/*.md', recursive=True):\n    try:\n        with open(f) as fh:\n            content = fh.read()\n        if '161 / 315' in content or '161/315' in content:\n            print(f'FOUND 161/315: {f}')\n        if '161 / 308' in content or '161/308' in content:\n            print(f'FOUND 161/308: {f}')\n    except:\n        pass\n\"\n",
    "description": "Search for explicit Llama N count references in all reports"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-23T19:54:33.889319+00:00_

FOUND 161/315: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md
FOUND 161/315: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap/temporal_overlap_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-23T19:54:33.889447+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Only plan_027 report (temporal overlap) uses 161/315\n# The paper says 161/308 which matches the earlier metabench_data_summary\n# When plan_001's within_family_dif.csv was generated, it likely used 308 llama-3 models\n# (the older metadata)\n\n# The current model_metadata shows 315 because metadata was later updated\n# But the actual DIF analysis (plan_001) was likely run with 308\n\n# Key question: does the 61.3% C% value change between 308 and 315 models?\n# Since DIF is run on items not models, probably not significantly\n\n# Let me check if there's an older version of model_metadata or if plan_001 has specific model lists\n\n# Check the plan_001 analysis script for how it reads metadata\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py') as f:\n    content = f.read()\n\n# Find how it filters for llama families\nfor line in content.split('\\n'):\n    if 'llama' in line.lower() or 'family' in line.lower():\n        print(line)\n\" | head -20\n",
  "description": "Check plan_001 script for family filtering logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Only plan_027 report (temporal overlap) uses 161/315\n# The paper says 161/308 which matches the earlier metabench_data_summary\n# When plan_001's within_family_dif.csv was generated, it likely used 308 llama-3 models\n# (the older metadata)\n\n# The current model_metadata shows 315 because metadata was later updated\n# But the actual DIF analysis (plan_001) was likely run with 308\n\n# Key question: does the 61.3% C% value change between 308 and 315 models?\n# Since DIF is run on items not models, probably not significantly\n\n# Let me check if there's an older version of model_metadata or if plan_001 has specific model lists\n\n# Check the plan_001 analysis script for how it reads metadata\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py') as f:\n    content = f.read()\n\n# Find how it filters for llama families\nfor line in content.split('\\n'):\n    if 'llama' in line.lower() or 'family' in line.lower():\n        print(line)\n\" | head -20\n",
    "description": "Check plan_001 script for family filtering logic"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-23T19:54:33.889580+00:00_

against Li et al. contamination proxy labels, and performs within-family,
  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
    # ── Step 4: Within-family analysis ─────────────────────────────────────
    print("\n=== Step 4: Within-family DIF ===")
    # Show family × temporal distribution
    fam_temp = (model_meta.groupby(["family", "cohort_temporal"])
    print("  Family × temporal counts:")
    for fam in ["llama-2", "llama-3", "mistral", "mixtral", "solar", "zephyr"]:
    family_pairs = []
    # (A) Cross-family comparisons (related families)
    llama2_idx = rows_for("family", ["llama-2"])
    llama3_idx = rows_for("family", ["llama-3"])
    if len(llama2_idx) >= 80 and len(llama3_idx) >= 80:
        family_pairs.append(("llama-2", "llama-3", llama2_idx, llama3_idx))
    mistral_idx = rows_for("family", ["mistral"])
    mixtral_idx = rows_for("family", ["mixtral"])
        family_pairs.append(("mistral", "mixtral", mistral_idx, mixtral_idx))
    # (B) Within single family, temporal split (where both groups >= 40)
    for fam in ["unknown", "mistral", "llama-3", "llama-2"]:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-23T19:54:33.889729+00:00_

61:| Sao10K/14B-Glacier-Stack | other | base | 0.7047 | 0.7168 | +1.20 | -849 |
90:Despite measurable score changes, the overall ranking is highly preserved (ρ = 0.9965), indicating that DIF primarily shifts absolute scores rather than relative ordering. However, individual models can experience rank displacements exceeding ±561 positions (99th percentile).
15:- Min: -589 | Max: 849
41:| Sao10K/14B-Glacier-Stack | unknown | other | 0.7047 | 0.7168 | 556 | 1405 | 849 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-23T19:54:33.889878+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Compute ΔTPR for difficulty-dependent injection from mixed_mechanism\npython3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# From scheme_d_results: these are the injection results at p=0.5 equivalent\n# But the paper is comparing ΔTPR of ~0.41 for difficulty-dependent vs 0.51 for uniform\n# plan_011 shows external/temporal at p=0.5: ΔTPR=+0.508 (uniform)\n# mixed_mechanism scheme_d: what is the TPR?\n\n# From mixed_mechanism_report, scheme D baseline vs injected C% \n# Scheme D overall C%=35.3±1.0 vs baseline C%=31.3%\n# The paper says 'difficulty-dependent injection yields ΔTPR≈0.41 at p=0.5 (vs 0.51 uniform)'\n# This comes from some other plan - let me check if it's plan_011 difficulty variant\n\n# From scheme_d report: n_c_overall mean = 35.3% vs baseline 31.3%, so net ΔTPR≈(35.3-31.3)/100?\n# No - that's C% not TPR. Let me look for TPR data in scheme results \nprint('Need to find TPR from difficulty-dependent injection')\n\"",
  "description": "Check difficulty-dependent ΔTPR claim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Compute ΔTPR for difficulty-dependent injection from mixed_mechanism\npython3 -c \"\nimport pandas as pd\nimport numpy as np\n\n# From scheme_d_results: these are the injection results at p=0.5 equivalent\n# But the paper is comparing ΔTPR of ~0.41 for difficulty-dependent vs 0.51 for uniform\n# plan_011 shows external/temporal at p=0.5: ΔTPR=+0.508 (uniform)\n# mixed_mechanism scheme_d: what is the TPR?\n\n# From mixed_mechanism_report, scheme D baseline vs injected C% \n# Scheme D overall C%=35.3±1.0 vs baseline C%=31.3%\n# The paper says 'difficulty-dependent injection yields ΔTPR≈0.41 at p=0.5 (vs 0.51 uniform)'\n# This comes from some other plan - let me check if it's plan_011 difficulty variant\n\n# From scheme_d report: n_c_overall mean = 35.3% vs baseline 31.3%, so net ΔTPR≈(35.3-31.3)/100?\n# No - that's C% not TPR. Let me look for TPR data in scheme results \nprint('Need to find TPR from difficulty-dependent injection')\n\"",
    "description": "Check difficulty-dependent ΔTPR claim"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-23T19:54:33.890007+00:00_

Need to find TPR from difficulty-dependent injection

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-23T19:54:33.890135+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*.md\" 2>/dev/null | xargs grep -l \"0.41\\|difficulty.depend\\|diff.inject\\|weighted.*inject\" 2>/dev/null | grep -v \"__pycache__\\|dream\" | head -10",
  "description": "Find difficulty-dependent ΔTPR=0.41 source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*.md\" 2>/dev/null | xargs grep -l \"0.41\\|difficulty.depend\\|diff.inject\\|weighted.*inject\" 2>/dev/null | grep -v \"__pycache__\\|dream\" | head -10",
    "description": "Find difficulty-dependent ΔTPR=0.41 source"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-23T19:54:33.890258+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/rank_displacement_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/icc_family_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/gsm1k_data_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/restricted_rho_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mf2_thresholds.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/open_closed_dif_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/power_calibration_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/phase2_results_5c7f57.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-23T19:54:33.890405+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md | head -80",
  "description": "Read plan_004_step2 for difficulty-dependent ΔTPR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md | head -80",
    "description": "Read plan_004_step2 for difficulty-dependent ΔTPR"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-23T19:54:33.890542+00:00_

# Plan 004 Step 2: GSM8K Semi-Synthetic DIF Injection

## 1. Objective

Inject known differential contamination into GSM8K response data and test whether
MH-DIF detects it. Validates that the DIF methodology works on GSM8K (single-domain,
math benchmark) and enables comparison with MMLU results from plan_011.

## 2. Setup

- **Benchmark**: GSM8K (1319 items)
- **Contaminated items**: 264 (20% of 1319)
- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
- **Seeds per p-level**: 5
- **Cohort**: temporal, ref=2023 (N=1017), foc=2024 (N=804)
- **External cohort**: ref (N=1017), foc (N=804)
- **Focal inject (standard)**: 779 models in accuracy overlap [0.0000, 0.7589]
- **Focal inject (external)**: 779 models

### Matching variants

| Variant | Matching variable | Properties |
|---------|-------------------|------------|
| standard | purified GSM8K total score | Contaminated by injection (20% items affected) |
| external | avg proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande | Immune to GSM8K injection |

## 3. Dose-Response Results

### Standard matching

| p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
|---|----------------|----------------|------|-----------|----------|
| 0.0 | 0.182±0.039 | 0.191±0.010 | +0.000 | 0.97 | 0.1349 |
| 0.3 | 0.741±0.017 | 0.256±0.007 | +0.559 | 8.32 | 0.0000 |
| 0.5 | 0.931±0.006 | 0.367±0.002 | +0.749 | 23.42 | 0.0000 |
| 0.7 | 1.000±0.000 | 0.476±0.010 | +0.818 | inf | 0.0000 |
| 1.0 | 1.000±0.000 | 0.645±0.012 | +0.818 | inf | 0.0000 |

### External matching

| p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
|---|----------------|----------------|------|-----------|----------|
| 0.0 | 0.483±0.028 | 0.471±0.007 | +0.000 | 1.06 | 0.5352 |
| 0.3 | 0.970±0.015 | 0.471±0.007 | +0.486 | 43.68 | 0.0000 |
| 0.5 | 0.998±0.002 | 0.471±0.007 | +0.514 | inf | 0.0000 |
| 0.7 | 1.000±0.000 | 0.471±0.007 | +0.517 | inf | 0.0000 |
| 1.0 | 1.000±0.000 | 0.471±0.007 | +0.517 | inf | 0.0000 |

## 4. 
…[truncated 1012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 619 · 2026-05-23T19:54:33.890697+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Find ΔTPR≈0.41 for difficulty-dependent injection\nfind /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*.md\" 2>/dev/null | xargs grep -l \"0.41.*ΔTPR\\|ΔTPR.*0.41\\|diff.*depend.*0.41\\|weighted.*0.41\" 2>/dev/null | grep -v \"__pycache__\\|dream\" | head -5",
  "description": "Find ΔTPR=0.41 from difficulty-dependent injection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Find ΔTPR≈0.41 for difficulty-dependent injection\nfind /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*.md\" 2>/dev/null | xargs grep -l \"0.41.*ΔTPR\\|ΔTPR.*0.41\\|diff.*depend.*0.41\\|weighted.*0.41\" 2>/dev/null | grep -v \"__pycache__\\|dream\" | head -5",
    "description": "Find ΔTPR=0.41 from difficulty-dependent injection"
  }
}
```

</details>

---


### Tool result

_source line 620 · 2026-05-23T19:54:33.890880+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_17.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_16.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-23T19:54:33.891019+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check plan_016 (within_subject) for ΔTPR 0.41 vs 0.51 comparison  \n# From within-subject report: average ΔTPR was 0.211 at p=0.5\n# Let me look at plan_011 with difficulty weighting\ngrep -rn \"0.41\\|0.420\\|difficulty.*weight\\|weight.*inject\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ --include=\"*.md\" 2>/dev/null | head -10",
  "description": "Find difficulty-weighted injection result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check plan_016 (within_subject) for ΔTPR 0.41 vs 0.51 comparison  \n# From within-subject report: average ΔTPR was 0.211 at p=0.5\n# Let me look at plan_011 with difficulty weighting\ngrep -rn \"0.41\\|0.420\\|difficulty.*weight\\|weight.*inject\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ --include=\"*.md\" 2>/dev/null | head -10",
    "description": "Find difficulty-weighted injection result"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-23T19:54:33.891143+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-23T19:54:33.891266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Check dose_response_summary.csv in plan_011\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/dose_response_summary.csv | head -20",
  "description": "Read plan_011 dose response summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Check dose_response_summary.csv in plan_011\ncat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/dose_response_summary.csv | head -20",
    "description": "Read plan_011 dose response summary"
  }
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-23T19:54:33.891391+00:00_

p,cohort_type,mh_variant,tpr_mean,tpr_std,fpr_mean,fpr_std,fisher_or_mean,fisher_p_median
0.0,ability,anchor,0.6,0.05958187643906492,0.5955,0.021607290436331923,1.0425176402092453,0.48934843949095175
0.0,ability,external,0.49800000000000005,0.040865633483405106,0.493,0.010216408370851257,1.0376862626110337,0.5025492358221133
0.0,ability,standard,0.5940000000000001,0.052725705305856276,0.6114999999999999,0.013181426326464086,0.9605839309463293,0.4231473007797394
0.0,temporal,anchor,0.31400000000000006,0.053197744313081545,0.307,0.01848986208710059,1.0651659083562441,0.5465028509582752
0.0,temporal,external,0.32599999999999996,0.03507135583350037,0.3135,0.008767838958375098,1.0732098198053222,0.7202868041451116
0.0,temporal,standard,0.308,0.046583258795408464,0.298,0.011645814698852104,1.0740528244958572,0.8081326220818719
0.3,ability,anchor,0.7000000000000001,0.051478150704934986,0.5955,0.021607290436331923,1.6418565717967872,0.17314822982263203
0.3,ability,external,0.662,0.04438468204234428,0.493,0.010216408370851257,2.069855540970715,0.005067695426382491
0.3,ability,standard,0.7,0.05700877125495689,0.6094999999999999,0.02570262632494974,1.584939735800224,0.25548738941208027
0.3,temporal,anchor,0.5219999999999999,0.05357238094391551,0.307,0.01848986208710059,2.4925140255423237,0.00010073571834208619
0.3,temporal,external,0.548,0.03271085446759225,0.3135,0.008767838958375098,2.674044460691511,1.621363555997074e-05
0.3,temporal,standard,0.42400000000000004,0.05856620185738529,0.3895,0.017624556732014567,1.1840390749023468,0.6434635572662124
0.5,ability,anchor,0.764,0.03781534080237811,0.5955,0.021607290436331923,2.238876999052195,0.001423732852816243
0.5,ability,external,0.756,0.04098780306383843,0.493,0.010216408370851257,3.307777208034717,5.631291377561033e-07
0.5,ability,standard,0.76,0.04636809247747853,0.5995,0.02057000243072422,2.2105804398056343,0.006744942166107429
0.5,temporal,anchor,0.806,0.033615472627943205,0.307,0.01848986208710059,9.594426178873977,9.756
…[truncated 377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-23T19:54:33.891545+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# The plan_001 script uses family='llama-3' from model_metadata.csv\n# At the time it was run, model_metadata had 308 llama-3 models\n# Current model_metadata has 315 (updated)\n# The paper's 308 is consistent with what was used in the analysis\n\n# Now let me compile all the findings\n\n# Summary of verified values\nprint('=== TABLE 1 VERIFICATION ===')\nprint()\nprint('Row: Temporal (2023 vs 2024)')\nprint('  N_ref/N_focal = 1080/807 -> plan_001: N=1080/N=807 MATCH')\nprint('  C% = 31.3 -> dif_summary.csv: 31.32% MATCH')\nprint('  C% (web-clean) = 0.318 -> plan_001: fpr_vs_li_clean=0.3184 MATCH')\nprint('  Enrich = 0.964 -> plan_001: enrichment_ratio=0.9641 MATCH')\nprint()\nprint('Row: Ability quintile (Q1-2 vs Q4-5)')\nprint('  N_ref/N_focal = ~2600/~2600 -> model_metadata: Q1-2=2092, Q4-5=2089 MISMATCH')\nprint('  C% = 2.9 -> dif_summary.csv: 2.9021% MATCH')\nprint('  C% (web-clean) = 0.027 -> plan_001: fpr_vs_li_clean=0.0269 MATCH')\nprint('  Enrich = 1.19 -> plan_001: enrichment_ratio=1.1949 MATCH')\nprint()\nprint('Row: Within-family (Llama-2 vs 3)')\nprint('  N_ref/N_focal = 161/308 -> model_metadata: 161/315, plan_027: 161/315 MISMATCH (~7 off)')\nprint('    (earlier metabench_data_summary.md says 308 -- stale metadata)')\nprint('  C% = 61.3 -> within_family analysis: 61.34% MATCH')\nprint()\nprint('Row: Random split 2023 (sanity)')\nprint('  N = 540/540 -> random_split_report.md: N=540/540 MATCH')\nprint('  C% = 0.62 -> _project/data/random_split_report.md: mean null C%=0.6247% MATCH')\nprint()\nprint('Row: Random split 2024 (sanity)')\nprint('  N = ~400/~400 -> r15_random_split_control: ~403/404 MATCH')\nprint('  C% = 1.3 -> r15_random_split_report: mean C%=1.335% (rounds to 1.3%) MATCH')\nprint()\nprint('Row: Within-subject (avg, 5 subj.)')\nprint('  N = varies (ok)')\nprint('  C% = 38.1 -> plan_014: average within-subject C%=38.1% MATCH')\n\"\n",
  "description": "Compile Table 1 verification results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# The plan_001 script uses family='llama-3' from model_metadata.csv\n# At the time it was run, model_metadata had 308 llama-3 models\n# Current model_metadata has 315 (updated)\n# The paper's 308 is consistent with what was used in the analysis\n\n# Now let me compile all the findings\n\n# Summary of verified values\nprint('=== TABLE 1 VERIFICATION ===')\nprint()\nprint('Row: Temporal (2023 vs 2024)')\nprint('  N_ref/N_focal = 1080/807 -> plan_001: N=1080/N=807 MATCH')\nprint('  C% = 31.3 -> dif_summary.csv: 31.32% MATCH')\nprint('  C% (web-clean) = 0.318 -> plan_001: fpr_vs_li_clean=0.3184 MATCH')\nprint('  Enrich = 0.964 -> plan_001: enrichment_ratio=0.9641 MATCH')\nprint()\nprint('Row: Ability quintile (Q1-2 vs Q4-5)')\nprint('  N_ref/N_focal = ~2600/~2600 -> model_metadata: Q1-2=2092, Q4-5=2089 MISMATCH')\nprint('  C% = 2.9 -> dif_summary.csv: 2.9021% MATCH')\nprint('  C% (web-clean) = 0.027 -> plan_001: fpr_vs_li_clean=0.0269 MATCH')\nprint('  Enrich = 1.19 -> plan_001: enrichment_ratio=1.1949 MATCH')\nprint()\nprint('Row: Within-family (Llama-2 vs 3)')\nprint('  N_ref/N_focal = 161/308 -> model_metadata: 161/315, plan_027: 161/315 MISMATCH (~7 off)')\nprint('    (earlier metabench_data_summary.md says 308 -- stale metadata)')\nprint('  C% = 61.3 -> within_family analysis: 61.34% MATCH')\nprint()\nprint('Row: Random split 2023 (sanity)')\nprint('  N = 540/540 -> random_split_report.md: N=540/540 MATCH')\nprint('  C% = 0.62 -> _project/data/random_split_report.md: mean null C%=0.6247% MATCH')\nprint()\nprint('Row: Random split 2024 (sanity)')\nprint('  N = ~400/~400 -> r15_random_split_control: ~403/404 MATCH')\nprint('  C% = 1.3 -> r15_random_split_report: mean C%=1.335% (rounds to 1.3%) MATCH')\nprint()\nprint('Row: Within-subject (avg, 5 subj.)')\nprint('  N = varies (ok)')\nprint('  C% = 38.1 -> plan_014: average within-subject C%=38.1% MATCH')\n\"\n",
    "description": "Compile Table 1 verification results"
  }
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-23T19:54:33.891697+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "# Search for the difficulty-dependent 0.41 and 20% overestimation in plan dirs\ngrep -rn \"0.420\\|0.41.*tpr\\|tpr.*0.41\\|difficulty.*injection\\|inject.*difficulty\\|20.*over\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | grep -v \"dream\" | head -20",
  "description": "Find 0.41 ΔTPR and 20% overestimation source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_experiments_tables_20260523T193629",
  "tool": "Bash",
  "tool_args": {
    "command": "# Search for the difficulty-dependent 0.41 and 20% overestimation in plan dirs\ngrep -rn \"0.420\\|0.41.*tpr\\|tpr.*0.41\\|difficulty.*injection\\|inject.*difficulty\\|20.*over\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ --include=\"*.md\" 2>/dev/null | grep -v \"dream\" | head -20",
    "description": "Find 0.41 ΔTPR and 20% overestimation source"
  }
}
```

</details>

---
