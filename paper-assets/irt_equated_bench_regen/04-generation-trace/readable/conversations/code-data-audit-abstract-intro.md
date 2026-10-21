# code data audit abstract intro

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 279
- **Recorded user turns:** 0
- **Tool calls:** 139
- **Original source:** `logs/chats/worker_code_data_audit_abstract_intro_20260523T191605.jsonl`
- **Structured JSON:** [`a43dcabc2a760ad7a2f7.json`](../../sessions/a4/a43dcabc2a760ad7a2f7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

279 recorded events

### Tool call

_source line 1 · 2026-05-23T19:26:25.044382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T19:26:25.045843+00:00_

1	\begin{abstract}
2	LLM benchmark scores are compared across model generations, yet whether individual items measure the same construct over time is rarely tested. We apply differential item functioning (DIF) analysis from educational measurement to six METABENCH benchmarks (5,227 models), validated through a semi-synthetic injection framework with cross-subject matching. Between 2023 and 2024 model cohorts, 17.9--31.3\% of items exhibit large temporal DIF (29.2\% for MMLU after non-independence correction, cluster bootstrap 95\% CI: $[26.7\%, 53.2\%]$; ${\geq}22\times$ random baseline). Web-overlap labels (a proxy for training-set contamination) are near-independent of DIF flags: global exposure and differential functioning are complementary diagnostic dimensions. Temporal DIF does not threaten aggregate rankings ($\rho \approx 0.997$) but reveals structured item-level change---base and instruct models exhibit opposite DIF patterns ($\chi^2 = 562.7$), evidence that DIF captures capability shifts beyond contamination---and shifts DIF-corrected scores by ${+}2.12$\,pp on average under full C-flag removal. We propose a three-step audit protocol (Monitor/Triage/Correct) with empirically grounded thresholds for benchmark maintainers. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:26:25.046104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:26:25.046314+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We use \emph{measurement invariance} to denote the property that test items function identically across groups~\citep{meredith1993invariance}, \emph{differential item functioning} (DIF) as the item-level statistical test for violations, and \emph{temporal score incomparability} (measurement non-invariance across temporal cohorts, manifesting as score incomparability) as the empirical phenomenon when DIF is detected---scores are not directly comparable across cohorts because item measurement properties differ systematically, without implying degradation or attributing cause. Applying Mantel-Haenszel DIF analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench},\footnote{Analysis code and DIF audit scripts are available at \url{https://github.com/anonymous-nlp-2026-2/irt_equated_bench_regen}.} we find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts---versus 0.62\% under a random-split control. Aggregate rankings are robust ($\rho \approx 0.997$), but absolute scores are not directly comparable: DIF-corrected scoring (excluding all C-flagged items) shifts accuracy by ${+}2.12$\,pp on average, with individual models displaced by up to 849 rank positions. This instability does not invalidate the benchmark---aggregate rankings are massively redundant---but it is diagnostic, revealing which capability dimensions shift across model generations.
6	
7	Existing approaches to benchmark integrity focus on \emph{g
…[truncated 3596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:26:25.046501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T19:26:25.046654+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six METABENCH benchmarks, 17.9--31.3\% of items exhibit temporal DIF across 2023--2024 model cohorts (29.2\% for MMLU), while aggregate rankings remain preserved ($\rho \approx 0.997$). DIF flags are near-independent of web-overlap labels (Jaccard $= 0.206$); opposite base-vs-instruct patterns ($\chi^2 = 562.7$) confirm that DIF captures signal beyond contamination. Mechanism-conditional DIF audit should complement contamination screening~\citep{habba2026growingpains}; connecting DIF to specific training factors remains open.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:26:25.046816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:26:25.046960+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	Three primary limitations apply. (1)~The semi-synthetic framework uses uniform binary response flipping, a stylized injection model; reported $\Delta\mathrm{TPR}$ values may overestimate detection power. Partial memorization scenarios---where models recall item cues without deterministic answer flipping---would produce weaker and qualitatively different DIF patterns than our binary injection model. The framework detects \emph{that} items function differently but not \emph{why}---a deliberate design choice that limits immediate actionability; follow-up expert review is needed to determine whether flagged items should be retired or retained. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. Two DEFF estimators (13.5--29.2\%) and family-level cluster bootstrap (95\% CI: $[26.7\%, 53.2\%]$) bound the impact, but the extreme relatedness of some families (e.g., hundreds of Llama-2 fine-tunes) exceeds the clustering levels studied in educational settings~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains; $\Delta\mathrm{FPR}$ rises to 0.167 when contamination spans ${\geq}20$ subjects. Although composition control experiments show a small residual shift ($\Delta = 1.08$\,pp; \Cref{app:composition_control}), base/instruct ratio changes between cohorts remain a potential confound that cannot be fully eliminated without single-architecture longitudinal data. Temporal cohorts defined by calendar year provide coarse granularity, and generalizability to partial-credit and free-form generation benchmarks is untested. Multidimensional DIF~\citep{ackerman1992didmf} may arise when MMLU's 57 subjects span distinct latent dimensions; cross-subject matching mitigates between-domain multidimensionality but not within-domain violations. IRT parameters are used only for auxiliary power analysis; all core DIF results are nonparametric. 
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:26:25.047161+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find DIF C% and DEFF sources",
  "prompt": "I need to find specific numbers in the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/\n\nFind and report the exact values for these numbers:\n1. 31.3% and 17.9% (temporal C% range across benchmarks) - look in plan_001/ and related DIF result files\n2. 29.2% (MMLU C% after DEFF correction) - look in mf2_deff_estimation/\n3. 13.5% (weighted-mean DEFF adjusted C%) - look in mf2_deff_estimation/\n4. 0.62% (random-split control C%) - look in plan_001/ or similar\n5. 22× (ratio of observed to random baseline) - might be derived from 31.3/0.62 or similar\n6. 5,227 models and 12,508 items - look in metabench_data/ or summary files\n\nSearch broadly: deff_summary.md, deff_results.csv, any summary files in plan_001/, metabench_summary.json, metabench_data_summary.md, etc. Read each file you find and report the exact numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find DIF C% and DEFF sources",
    "prompt": "I need to find specific numbers in the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/\n\nFind and report the exact values for these numbers:\n1. 31.3% and 17.9% (temporal C% range across benchmarks) - look in plan_001/ and related DIF result files\n2. 29.2% (MMLU C% after DEFF correction) - look in mf2_deff_estimation/\n3. 13.5% (weighted-mean DEFF adjusted C%) - look in mf2_deff_estimation/\n4. 0.62% (random-split control C%) - look in plan_001/ or similar\n5. 22× (ratio of observed to random baseline) - might be derived from 31.3/0.62 or similar\n6. 5,227 models and 12,508 items - look in metabench_data/ or summary files\n\nSearch broadly: deff_summary.md, deff_results.csv, any summary files in plan_001/, metabench_summary.json, metabench_data_summary.md, etc. Read each file you find and report the exact numbers."
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T19:26:25.047365+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "**/*summary*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "**/*summary*"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T19:26:25.047511+00:00_

artifacts/_project/data/metabench_summary_646c62.json
artifacts/_project/data/metabench_summary.json
artifacts/metabench_summary.json
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/metabench_data_summary.md
artifacts/plan_001/dif_summary.csv
artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv
artifacts/plan_001b/enrichment_summary.csv
artifacts/plan_001b/data/enrichment_summary.csv
artifacts/plan_011/dose_response_summary.csv
artifacts/plan_011_semi_synthetic_validation/data/dose_response_summary_779a18.csv
artifacts/plan_011_semi_synthetic_validation/data/dose_response_summary.csv
artifacts/_project/data/q3_summary.csv
artifacts/plan_013_q3_local_independence/data/q3_summary.csv
artifacts/plan_013/q3_summary.csv
artifacts/_project/report/experiment_summary.md
artifacts/experiment_summary.md
artifacts/_project/data/gsm8k_ets_summary.csv
artifacts/plan_004/gsm8k_ets_summary.csv
artifacts/_project/data/gsm8k_dose_response_summary.csv
artifacts/plan_004/gsm8k_dose_response_summary.csv
artifacts/plan_019/subject_decomposition_summary.csv
artifacts/plan_021/lr_dif_subject_summary.csv
artifacts/plan_024/llama_matched_dif_summary.csv
artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv.bak
artifacts/plan_028_multi_bench_dif/arc_ets_summary.csv
artifacts/plan_028_multi_bench_dif/hellaswag_ets_summary.csv
artifacts/plan_028_multi_bench_dif/winogrande_ets_summary.csv
artifacts/plan_028_multi_bench_dif/truthfulqa_ets_summary.csv
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv
artifacts/plan_033_subject_dif_concentration/domain_group_summary.csv
artifacts/plan_033_subject_dif_concentration/data/domain_group_summary.csv
artifacts/plan_032_dif_cleaned_mmlu/random_baseline_summary.csv
artifacts/plan_028_multi_bench_dif/data/mmlu_bootstrap_summary.csv
artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_summary.csv
artifacts/pla
…[truncated 903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T19:26:25.047653+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "**/deff_*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "**/deff_*"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T19:26:25.047803+00:00_

artifacts/_project/data/deff_results.csv
artifacts/_project/report/deff_summary.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/mf2_deff_estimation/deff_summary.md
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/r17_deff_reclassification/deff_reclassification_report.md
artifacts/r20_size_stratified_deff/deff_parameterization_curve.png
artifacts/r20_size_stratified_deff/deff_parameterization_curve.pdf
artifacts/deff_parametric_curve/deff_parametric_curve.py
artifacts/_project/chart/deff_parametric_curve.pdf
artifacts/deff_parametric_curve/deff_parametric_curve.pdf
artifacts/deff_parametric_curve/deff_parametric_curve.png
artifacts/deff_parametric_curve/deff_curve_report.md
artifacts/r22_deff_simulation/deff_simulation.py
artifacts/r22_deff_simulation/deff_simulation_results.csv
artifacts/r22_deff_simulation/deff_simulation_figure.pdf
artifacts/r22_deff_simulation/deff_simulation_figure.png
artifacts/_project/report/deff_simulation_report.md
artifacts/r22_deff_simulation/deff_simulation_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T19:26:25.047937+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "**/plan_001/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "**/plan_001/*"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T19:26:25.048054+00:00_

artifacts/plan_001/plan_001_analysis.py
artifacts/plan_001/dif_results_temporal.csv
artifacts/plan_001/dif_results_ability.csv
artifacts/plan_001/dif_summary.csv
artifacts/plan_001/within_family_dif.csv
artifacts/plan_001/cross_analysis.csv
artifacts/plan_001/domain_specificity.csv
artifacts/plan_001/neg_disc_sensitivity.csv
artifacts/plan_001/plan_001_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T19:26:25.048258+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "**/metabench*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "**/metabench*"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T19:26:25.048385+00:00_

artifacts/_project/data/metabench_irt_params.csv
artifacts/_project/data/metabench_ctt_stats.csv
artifacts/_project/data/metabench_irt_params_345678.csv
artifacts/metabench_ctt_stats.csv
artifacts/metabench_model_list.txt
artifacts/_project/data/metabench_model_accuracy.csv
artifacts/metabench_model_accuracy.csv
artifacts/_project/intermediate/metabench_explore.py
artifacts/_project/intermediate/metabench_explore_0bd873.py
artifacts/metabench_explore.py
artifacts/metabench_subject_stats.csv
artifacts/_project/data/metabench_cohort_analysis.csv
artifacts/metabench_cohort_analysis.csv
artifacts/_project/data/metabench_rl_models_18eb0d.csv
artifacts/_project/data/metabench_rl_models.csv
artifacts/metabench_rl_models.csv
artifacts/_project/data/metabench_summary_646c62.json
artifacts/_project/data/metabench_summary.json
artifacts/metabench_summary.json
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/metabench_data_summary.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T19:26:25.048523+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find rank correlation and Jaccard",
  "prompt": "I need to find specific numbers in the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/\n\nFind and report exact values for:\n1. ρ ≈ 0.997 (rank correlation) - look in mf2_practical_significance/ or plan_032_dif_cleaned_mmlu/\n2. Jaccard = 0.206 - look in plan_001b/ or r17_gsm1k_jaccard_permutation/\n3. φ = 0.012 - might be near the Jaccard value\n4. χ² = 562.7 (base vs instruct DIF patterns) - look in plan_001b/ or any chi-square result files\n5. +2.12 pp (score inflation) - look in score_inflation_analysis/\n6. 849 (rank displacement) - look in score_inflation_analysis/ or plan_032/\n\nSearch broadly across these directories and read the relevant files. Report exact source file paths and values found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find rank correlation and Jaccard",
    "prompt": "I need to find specific numbers in the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/\n\nFind and report exact values for:\n1. ρ ≈ 0.997 (rank correlation) - look in mf2_practical_significance/ or plan_032_dif_cleaned_mmlu/\n2. Jaccard = 0.206 - look in plan_001b/ or r17_gsm1k_jaccard_permutation/\n3. φ = 0.012 - might be near the Jaccard value\n4. χ² = 562.7 (base vs instruct DIF patterns) - look in plan_001b/ or any chi-square result files\n5. +2.12 pp (score inflation) - look in score_inflation_analysis/\n6. 849 (rank displacement) - look in score_inflation_analysis/ or plan_032/\n\nSearch broadly across these directories and read the relevant files. Report exact source file paths and values found."
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:26:25.048732+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T19:26:25.048920+00:00_

1	# MF2: Design Effect (DEFF) Estimation — Summary (v3, cohort-consistent)
2	
3	## Analysis Scope
4	
5	| Parameter | Value |
6	|-----------|-------|
7	| Cohort restriction | ref (2023) + foc (2024) only |
8	| Models in DIF cohort (ref+foc) | 1887 |
9	| Valid models (known family, family≥2) | 1884 |
10	| Valid families | 30 |
11	| Total models in response matrix | 5227 |
12	| Items analyzed | 12508 |
13	
14	**Change from v2**: v2 used all 5227 models with family labels (1884 after filtering).
15	v3 restricts to ref+foc cohort (1887) before family filtering, yielding 1884 valid models.
16	
17	### Family Size Distribution (within ref+foc cohort)
18	
19	| Stat | Value |
20	|------|-------|
21	| Mean (m̄_simple) | 62.80 |
22	| m̄_weighted (Σn²/Σn) | 254.48 |
23	| Median | 22.5 |
24	| Min | 2.0 |
25	| Max | 547.0 |
26	| Top-5 families | mistral(547.0), llama-3(315.0), llama-2(161.0), mixtral(120.0), solar(91.0) |
27	
28	## Design Effect — Two Variants
29	
30	| Parameter | Weighted (Σn²/Σn) | Simple (mean) |
31	|-----------|--------------------|---------------|
32	| m̄ | 254.48 | 62.80 |
33	| Mean ICC | 0.0465 | 0.0465 |
34	| **Global DEFF** | **12.79** | **3.87** |
35	| Effective N | 147.3 | 486.2 |
36	
37	### ICC Distribution
38	
39	| Stat | Value |
40	|------|-------|
41	| Mean | 0.0465 |
42	| Median | 0.0409 |
43	| Q1 | 0.0261 |
44	| Q3 | 0.0611 |
45	| Max | 0.2194 |
46	| % ICC > 0.1 | 4.8% |
47	| % ICC = 0 | 0.1% |
48	
49	## Adjusted DIF Classifications
50	
51	### Weighted m̄
52	
53	| Metric | Original | Adjusted | Change |
54	|--------|----------|----------|--------|
55	| C items | 3918 (31.3%) | 1690 (13.5%) | -2228 |
56	| B items | 2258 | 49 | -2209 |
57	| A items | 6332 | 10769 | 4437 |
58	
59	Reclassification: C→B=0, C→A=2228, B→A=2209
60	
61	### Simple m̄
62	
63	| Metric | Original | Adjusted | Change |
64	|--------|----------|----------|--------|
65	| C items | 3918 (31.3%) | 3649 (29.2%) | -269 |
66	| B items | 2258 | 1081 | -1177 |
67	| A items | 6332 | 7778 
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:26:25.049078+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_report.md"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:26:25.049224+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:26:25.049380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/metabench_data_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:26:25.049530+00:00_

1	# METABENCH MMLU Data Summary
2	
3	## Dataset Overview
4	
5	| Metric | Value |
6	|--------|-------|
7	| Models (CSV) | 5,227 |
8	| Models (RDS, after preprocessing) | 5,219 |
9	| Items | 12,508 |
10	| Subjects | 57 |
11	| Total response rows | 73,383,381 |
12	| Data format | Long format (source, item, correct), binary 0/1 |
13	
14	Models per subject ranges 5,225–5,227 (near-complete coverage). 8 models were filtered during METABENCH's preprocessing step (RDS).
15	
16	## CTT Item Statistics (from `mmlu-preproc.rds`)
17	
18	The RDS file contains **CTT statistics (difficulty = 0.75 × p_correct, discrimination = rpbis)**:
19	
20	| Parameter | Min | Mean | Median | Max |
21	|-----------|-----|------|--------|-----|
22	| Difficulty (diff) | 0.008 | 0.444 | 0.524 | 0.689 |
23	| Discrimination (disc) | -0.551 | 0.076 | 0.107 | 0.291 |
24	| SD | 0.106 | — | — | 0.500 |
25	
26	- **0 items excluded** by METABENCH's quality filter
27	- **1,926 items (15.4%)** with negative discrimination — these behave inversely (higher-ability models get them wrong more often)
28	- **258 floor items** (empirical p < 0.05), **0 ceiling items** (p > 0.95)
29	- Empirical p-value range: [0.011, 0.919]
30	
31	### Train/Test Split
32	
33	METABENCH provides a pre-built split in `mmlu-preproc-split.rds`:
34	- **Train**: 4,755 models (91.1%)
35	- **Test**: 464 models (8.9%)
36	
37	## Model Accuracy Distribution
38	
39	| Statistic | Value |
40	|-----------|-------|
41	| Mean | 0.592 |
42	| Std | 0.160 |
43	| Min | 0.218 |
44	| Max | 0.911 |
45	| P25 | 0.543 |
46	| Median | 0.661 |
47	| P75 | 0.697 |
48	| Below random (0.25) | 366 (7.0%) |
49	
50	Strong bimodal tendency: most models cluster in 0.54–0.71, with a long left tail of weak/broken models.
51	
52	## Cohort Analysis (for DIF / temporal grouping)
53	
54	### By Model Family Classification
55	
56	Only **1,929 of 5,219 (37.0%)** models could be classified into known families by regex on model names. The remaining 3,290 are community fine-tunes, mer
…[truncated 3554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:26:25.049688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_results.csv"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T19:26:25.049840+00:00_

File content (3.1MB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:26:25.049960+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/dif_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T19:26:25.050078+00:00_

1	cohort_type,item_filter,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,fpr_vs_li_clean,enrichment_ratio
2	temporal,all,12508,6332,2258,3918,31.323952670291018,0.31840974212034384,0.9641535548797142
3	ability,all,12508,11052,1093,363,2.9021426287176206,0.026862464183381087,1.1949300411522636
4	temporal,non_neg_disc,10582,5327,1830,3425,32.36628236628237,0.3257975913796746,0.969539159262983
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:26:25.050198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -type f -name \"*.txt\" -o -name \"*.md\" -o -name \"*.json\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -type f -name \"*.txt\" -o -name \"*.md\" -o -name \"*.json\" | head -30"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T19:26:25.050324+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/mf1_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/_stats.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/irt_scale_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/rank_shift_stats.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/cluster_bootstrap_ci.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/random_split_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_summary_646c62.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/mmlu_cf_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/rank_displacement_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_013_report.md
/home/ubuntu/.agent-ml-research-idea_gen_05
…[truncated 1931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T19:26:25.050466+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.997",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.997",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T19:26:25.050603+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find cluster bootstrap and injection",
  "prompt": "I need to find specific numbers in the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/\n\nFind and report exact values for:\n1. Cluster bootstrap CI [26.7%, 53.2%] - look in sf1_cluster_bootstrap/\n2. ΔFPR = 0.167 at k=20 - look in plan_034_multi_subject_injection/ specifically summary_by_k_full.csv\n3. k ≤ 5 (where ΔFPR stays at 0) - also in plan_034\n4. Δ = 1.08 pp (composition control residual shift) - look in r22_composition_control/\n5. 57 subjects (MMLU) - might be in metabench data or just common knowledge\n\nSearch broadly across these directories and read the relevant files. Report exact source file paths and values found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find cluster bootstrap and injection",
    "prompt": "I need to find specific numbers in the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/\n\nFind and report exact values for:\n1. Cluster bootstrap CI [26.7%, 53.2%] - look in sf1_cluster_bootstrap/\n2. ΔFPR = 0.167 at k=20 - look in plan_034_multi_subject_injection/ specifically summary_by_k_full.csv\n3. k ≤ 5 (where ΔFPR stays at 0) - also in plan_034\n4. Δ = 1.08 pp (composition control residual shift) - look in r22_composition_control/\n5. 57 subjects (MMLU) - might be in metabench data or just common knowledge\n\nSearch broadly across these directories and read the relevant files. Report exact source file paths and values found."
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:26:25.050786+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.206",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.206",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-23T19:26:25.050927+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001",
  "pattern": "0\\.62|random.*baseline|22×|22x|ratio",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001",
    "pattern": "0\\.62|random.*baseline|22×|22x|ratio",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T19:26:25.051058+00:00_

&lt;persisted-output>
Output too large (45.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/toolu_01J8zovGW4codeyuin4qqrVs.txt

Preview (first 2KB):
artifacts/plan_001/dif_summary.csv:1:cohort_type,item_filter,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,fpr_vs_li_clean,enrichment_ratio
artifacts/plan_001/dif_results_ability.csv:378:business_ethics.36,business_ethics,0.0,inf,,0.6204352280531389,A,True,input_and_label
artifacts/plan_001/dif_results_ability.csv:704:college_biology.12,college_biology,0.0,inf,,0.6204352280531389,A,False,clean
artifacts/plan_001/dif_results_ability.csv:914:college_computer_science.22,college_computer_science,1.9444444444444446,-1.5626943134441356,1.8102130188100483,0.6239115264438682,B,False,clean
artifacts/plan_001/dif_results_ability.csv:1064:college_medicine.105,college_medicine,0.0,inf,,0.6268850384245204,A,False,clean
artifacts/plan_001/dif_results_ability.csv:1283:college_physics.90,college_physics,0.6265822784810127,1.0985666797970857,2.053079173852195,0.9535459099906635,B,True,input_only
artifacts/plan_001/dif_results_ability.csv:1288:college_physics.95,college_physics,0.0,inf,,0.6219194147059962,A,True,input_only
artifacts/plan_001/dif_results_ability.csv:1316:computer_security.36,computer_security,0.0,inf,,0.6201942446794736,A,False,clean
artifacts/plan_001/dif_results_ability.csv:1747:electrical_engineering.38,electrical_engineering,0.0,inf,,0.6237486692290088,A,False,clean
artifacts/plan_001/dif_results_ability.csv:1815:elementary_mathematics.103,elementary_mathematics,0.0,inf,,0.6284663575654281,A,True,input_only
artifacts/plan_001/dif_results_ability.csv:1879:elementary_mathematics.168,elementary_mathematics,0.0,inf,,0.6252071003557773,A,False,clean
artifacts/plan_001/dif_results_ability.csv:1923:elementary_mathematics.211,elementary_mathematics,0.0,inf,,0.6211192692670033,A,True,input_
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-23T19:26:25.051241+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "φ\\s*=\\s*0\\.012|0\\.012",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "φ\\s*=\\s*0\\.012|0\\.012",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:26:25.051386+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "0\\.62|random.*baseline|random.*split|random.*control|22×|22x",
  "glob": "**/*summary*",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "0\\.62|random.*baseline|random.*split|random.*control|22×|22x",
    "glob": "**/*summary*",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T19:26:25.051522+00:00_

artifacts/plan_013_q3_local_independence/data/q3_summary.csv:6:high_school_us_history,193,0.029254494229236972,-0.015190618934957925,0.13283839487842322,13.601036269430052,0.621839406980072,18528
artifacts/plan_013_q3_local_independence/data/q3_summary.csv:28:philosophy,281,0.00951114470725351,-0.0320623869415259,0.12603069474329556,11.08795119471276,0.6284931830056387,39340
artifacts/plan_013_q3_local_independence/data/q3_summary.csv:36:jurisprudence,100,0.00804775847852261,-0.028274518626445942,0.12595322623984795,10.424242424242426,0.6256317271405977,4950
artifacts/plan_028_multi_bench_dif/hellaswag_ets_summary.csv:3:random_split,943,944,10042,9485,529,28,0.27882891854212305,,-0.04145350496288358,
artifacts/plan_028_multi_bench_dif/winogrande_ets_summary.csv:3:random_split,910,910,1267,1239,24,4,0.31570639305445936,-0.04796170655029754,-0.03887169514287485,0.410063936062372
artifacts/experiment_summary.md:28:- **Result**: Temporal C%=31.3%, enrichment=0.96 (no enrichment); ability C%=2.9%, enrichment=1.19; within-family Llama-2 vs 3 C%=61.3%; domain ρ=0.307 (p=0.02); sanity random-split C%=0.18%
artifacts/experiment_summary.md:82:- **Hypothesis**: Removing DIF-flagged items (~31% of MMLU) improves cross-generation model ranking stability (Spearman ρ), significantly better than random removal baseline
artifacts/experiment_summary.md:117:| Sanity check C% (random split) | 0.18% | plan_001 | Method validity |
artifacts/plan_028_multi_bench_dif/arc_ets_summary.csv:3:random_split,943,944,1172,1101,64,7,0.5972696245733788,inf,0.014557898945215465,
artifacts/plan_028_multi_bench_dif/truthfulqa_ets_summary.csv:3:random_split,943,944,817,661,153,3,0.36719706242350064,-0.39354632851435684,-0.0995375199866264,0.9478371969187732
artifacts/_project/report/experiment_summary.md:28:- **Result**: Temporal C%=31.3%, enrichment=0.96 (no enrichment); ability C%=2.9%, enrichment=1.19; within-family Llama-2 vs 3 C%=61.3%; domain ρ=0.307 (p=0.02); sanity random-split C%=0.18%
artifact
…[truncated 1566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T19:26:25.051669+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "562\\.7|562\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "562\\.7|562\\.7",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T19:26:25.051824+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "2\\.12\\s*pp|2\\.12|inflation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "2\\.12\\s*pp|2\\.12|inflation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T19:26:25.051952+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "849",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "849",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T19:26:25.052099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type f -name \"*.csv\" -o -name \"*.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type f -name \"*.csv\" -o -name \"*.json\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T19:26:25.052249+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/family_rank_shifts.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/_stats.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/rank_changes.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/pairwise_flips.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm1k_model_accuracy.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/target.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/feature_importance_1bd0a5.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_irt_params.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/dose_response_theta.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/deff_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/lr_dif_item_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/bootstrap_dfpr_samples.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/irt_scale_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/pr
…[truncated 592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-23T19:26:25.052395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T19:26:25.052513+00:00_

1	percentile,abs_delta_mh
2	50.0,0.29556451737880707
3	90.0,0.7910759568214418
4	95.0,0.9898163795471193
5	97.5,1.1874477803707113
6	99.0,1.4503863203525544
7	99.5,1.6536056780815103
8	99.9,2.199819326400757
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T19:26:25.052640+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"sf1_cluster_bootstrap|plan_034|r22_composition\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"sf1_cluster_bootstrap|plan_034|r22_composition\""
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-23T19:26:25.052776+00:00_

drwxr-xr-x   5 ubuntu ubuntu     4096 May 21 16:01 plan_034
drwxr-xr-x   4 ubuntu ubuntu     4096 May 23 17:15 plan_034_multi_subject_injection
drwxr-xr-x   2 ubuntu ubuntu     4096 May 23 08:13 r22_composition_control
drwxr-xr-x   2 ubuntu ubuntu     4096 May 22 04:04 sf1_cluster_bootstrap

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T19:26:25.052913+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "0\\.62%|0\\.0062|control.*baseline|half-split|random.*0\\.",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "0\\.62%|0\\.0062|control.*baseline|half-split|random.*0\\.",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T19:26:25.053040+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "31\\.3|17\\.9",
  "glob": "**/*summary*",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "31\\.3|17\\.9",
    "glob": "**/*summary*",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T19:26:25.053166+00:00_

artifacts/mf2_practical_significance/benchmark_rho_summary.csv:7:MMLU,12508,3918,8590,31.32,5227,0.9965,0.00e+00,0.959986,0.020007
artifacts/mf2_deff_estimation/deff_summary.md:55:| C items | 3918 (31.3%) | 1690 (13.5%) | -2228 |
artifacts/mf2_deff_estimation/deff_summary.md:65:| C items | 3918 (31.3%) | 3649 (29.2%) | -269 |
artifacts/mf2_deff_estimation/deff_summary.md:84:- Adjusted C% (weighted: 13.5%, simple: 29.2%) ≤ Original (31.3%) ✓
artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv:2:temporal,all,12508,6332,2258,3918,31.323952670291018,0.31840974212034384,0.9641535548797142
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv.bak:2:mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv.bak:7:hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK
artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv:2:mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv:7:hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK
artifacts/plan_028_multi_bench_dif/data/mmlu_bootstrap_summary.csv:2:mmlu,31.323952670291018,31.323952670291018,29.380196674128555,38.048249120562836,33.14086984330029,2.296023528521892,1000,1080,807,12508,0.10273425007994882,0.10801306258738923
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv:2:mmlu,12508,1080,807,6332,2258,3918,31.3,0.18,PRIOR
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv:7:hellaswag,10042,1080,807,6037,2208,1797,17.9,0.28,OK
artifacts/_project/report/experiment_summary.md:28:- **Result**: Temporal C%=31.3%, enrichment=0.96 (no enrichment); ability C%=2.9%, enrichment=1.19; within-family Llama-2 vs 3 C%=61.3%; domain ρ=0.307 (p=0.02); sanity random-split C%=0.18%
artifacts/_project/report/experiment_summary.md:30:- **Story contribution**: Key negative finding that motivated the entire pivot. The 31.3% temporal C% becomes the headline number for "item instability." Domain ρ=0.30
…[truncated 2779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T19:26:25.053317+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T19:26:25.053434+00:00_

total 96
drwxr-xr-x   2 ubuntu ubuntu  4096 May 22 04:04 .
drwxr-xr-x 108 ubuntu ubuntu 12288 May 23 16:15 ..
-rw-r--r--   1 ubuntu ubuntu 60560 May 22 04:04 bootstrap_results.csv
-rw-r--r--   1 ubuntu ubuntu  1802 May 22 04:04 cluster_bootstrap_ci.md
-rw-r--r--   1 ubuntu ubuntu   483 May 22 03:57 family_distribution.csv
-rw-r--r--   1 ubuntu ubuntu 11951 May 22 03:56 run_bootstrap.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T19:26:25.053560+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/cluster_bootstrap_ci.md"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T19:26:25.053679+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T19:26:25.053849+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-23T19:26:25.053986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-23T19:26:25.054106+00:00_

total 480
drwxr-xr-x   4 ubuntu ubuntu   4096 May 23 17:15 .
drwxr-xr-x 108 ubuntu ubuntu  12288 May 23 16:15 ..
drwxr-xr-x   2 ubuntu ubuntu   4096 May 21 16:03 data
-rw-r--r--   1 ubuntu ubuntu  58330 May 23 17:14 k30_40_50_nontarget.csv
-rw-r--r--   1 ubuntu ubuntu 136729 May 23 17:14 k30_40_50_results.csv
-rw-r--r--   1 ubuntu ubuntu    554 May 23 17:14 k30_40_50_summary.csv
-rw-r--r--   1 ubuntu ubuntu  47041 May 21 16:00 multi_subject_injection_results.csv
-rw-r--r--   1 ubuntu ubuntu 154109 May 21 16:00 non_target_fpr_results.csv
-rw-r--r--   1 ubuntu ubuntu  15583 May 23 17:06 plan_034_k30_40_50.py
-rw-r--r--   1 ubuntu ubuntu  23488 May 21 15:52 plan_034_multi_subject_injection.py
-rw-r--r--   1 ubuntu ubuntu   4538 May 21 16:01 plan_034_report.md
drwxr-xr-x   2 ubuntu ubuntu   4096 May 21 16:03 report
-rw-r--r--   1 ubuntu ubuntu    983 May 21 16:00 summary_by_k.csv
-rw-r--r--   1 ubuntu ubuntu   1417 May 23 17:15 summary_by_k_full.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T19:26:25.054231+00:00_

total 40
drwxr-xr-x   2 ubuntu ubuntu  4096 May 23 08:13 .
drwxr-xr-x 108 ubuntu ubuntu 12288 May 23 16:15 ..
-rw-r--r--   1 ubuntu ubuntu   696 May 23 08:13 balanced_dif_results.csv
-rw-r--r--   1 ubuntu ubuntu 10875 May 23 08:13 composition_control.py
-rw-r--r--   1 ubuntu ubuntu  1653 May 23 08:13 composition_control_report.md
-rw-r--r--   1 ubuntu ubuntu   113 May 23 08:13 composition_stats.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-23T19:26:25.054355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-23T19:26:25.054472+00:00_

1	k,p,mean_tpr_target,mean_delta_tpr,std_delta_tpr,mean_fpr_non_target,mean_delta_fpr_non_target,std_delta_fpr_non_target
2	1,0.1,0.3906,0.0743,0.0531,0.3191,0.0019,0.0016
3	1,0.3,0.559,0.2427,0.0456,0.3192,0.002,0.0012
4	1,0.5,0.834,0.5177,0.0497,0.3188,0.0016,0.0015
5	2,0.1,0.3521,0.0383,0.0292,0.3169,0.0031,0.0015
6	2,0.3,0.5012,0.1874,0.0493,0.3168,0.003,0.0017
7	2,0.5,0.8071,0.4933,0.0324,0.3152,0.0015,0.0019
8	3,0.1,0.3305,0.0225,0.0208,0.3186,0.0022,0.0011
9	3,0.3,0.4678,0.1598,0.0662,0.3172,0.0007,0.0025
10	3,0.5,0.7779,0.47,0.0934,0.3153,-0.0011,0.0032
11	5,0.1,0.3135,0.0004,0.023,0.3198,0.0038,0.0023
12	5,0.3,0.4345,0.1215,0.0225,0.3157,-0.0002,0.0039
13	5,0.5,0.7336,0.4205,0.041,0.3224,0.0065,0.0066
14	10,0.1,0.3176,0.0086,0.0123,0.3164,0.0012,0.0027
15	10,0.3,0.4076,0.0986,0.0152,0.3406,0.0255,0.0115
16	10,0.5,0.6696,0.3606,0.0269,0.3841,0.069,0.0302
17	20,0.1,0.3332,0.0217,0.0101,0.3223,0.0013,0.0039
18	20,0.3,0.3979,0.0864,0.0182,0.3927,0.0717,0.0224
19	20,0.5,0.6106,0.2992,0.0299,0.4883,0.1673,0.0294
20	30,0.1,0.3355,0.0237,0.0086,0.3374,0.0259,0.006
21	30,0.3,0.3663,0.0546,0.0226,0.4914,0.1798,0.0205
22	30,0.5,0.471,0.1593,0.0345,0.6734,0.3618,0.0255
23	40,0.1,0.3348,0.0222,0.0067,0.3566,0.0407,0.0234
24	40,0.3,0.3722,0.0595,0.0226,0.5699,0.254,0.0665
25	40,0.5,0.53,0.2174,0.0439,0.7214,0.4056,0.0536
26	50,0.1,0.344,0.0296,0.0014,0.3636,0.0559,0.0272
27	50,0.3,0.4753,0.1608,0.0291,0.6109,0.3032,0.0639
28	50,0.5,0.7535,0.439,0.0281,0.7658,0.4581,0.0527
29	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-23T19:26:25.054598+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-23T19:26:25.054737+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T19:26:25.054892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-23T19:26:25.055030+00:00_

1	# Plan 034: Multi-Subject Simultaneous Injection — Report
2	
3	## Method
4	
5	We test Proposition 1's robustness boundary by simultaneously injecting
6	differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).
7	For each (k, p, seed) combination:
8	
9	1. Randomly select k target subjects from 57 MMLU subjects
10	2. For each item in the k target subjects, flip incorrect→correct responses
11	   in the focal group (2024 models within accuracy overlap) with probability p
12	3. Compute cross-subject MH-DIF for each target and non-target subject
13	   - Matching variable = total score on all subjects EXCEPT the tested one
14	   - For target subjects: matching includes injected scores from other targets
15	   - For non-target subjects: matching includes all injected target scores
16	4. Measure TPR on target subjects and FPR on non-target subjects
17	
18	Grid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs.
19	Cohorts: reference = 2023 models (n=1080), focal = 2024 models (n=807),
20	focal inject subset = 787 models (within accuracy overlap).
21	
22	## Core Results
23	
24	### Non-Target Subjects (FPR — key result)
25	
26	| k | p=0.1 ΔFPR | p=0.3 ΔFPR | p=0.5 ΔFPR |
27	|---|-----------|-----------|-----------|
28	| 1  | +0.002 ± 0.002 | +0.002 ± 0.001 | +0.002 ± 0.002 |
29	| 2  | +0.003 ± 0.002 | +0.003 ± 0.002 | +0.002 ± 0.002 |
30	| 3  | +0.002 ± 0.001 | +0.001 ± 0.003 | −0.001 ± 0.003 |
31	| 5  | +0.004 ± 0.002 | −0.000 ± 0.004 | +0.007 ± 0.007 |
32	| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |
33	| 20 | +0.001 ± 0.004 | **+0.072 ± 0.022** | **+0.167 ± 0.029** |
34	
35	### Target Subjects (TPR)
36	
37	| k | p=0.1 TPR | p=0.3 TPR | p=0.5 TPR |
38	|---|----------|----------|----------|
39	| 1  | 0.391 | 0.559 | 0.834 |
40	| 2  | 0.352 | 0.501 | 0.807 |
41	| 3  | 0.331 | 0.468 | 0.778 |
42	| 5  | 0.314 | 0.435 | 0.734 |
43	| 10 | 0.318 | 0.408 | 0.670 |
44	| 20 | 0.333 | 0.398 | 0.611 |
45	
46	## Key Findings
47	

…[truncated 2751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-23T19:26:25.055206+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type f -name \"*.csv\" -o -name \"*.md\" | xargs grep -l \"57\\|MMLU\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type f -name \"*.csv\" -o -name \"*.md\" | xargs grep -l \"57\\|MMLU\" 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T19:26:25.055339+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/mf1_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/family_rank_shifts.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/rank_changes.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/pairwise_flips.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm1k_model_accuracy.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/target.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-23T19:26:25.055490+00:00_

Found 238 files
artifacts/manifest.yaml
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/r22_deff_simulation/deff_simulation_results.csv
artifacts/_project/report/score_inflation_report.md
artifacts/score_inflation_analysis/score_inflation_report.md
artifacts/score_inflation_analysis/top_displaced.csv
artifacts/score_inflation_analysis/type_summary.csv
artifacts/score_inflation_analysis/cohort_summary.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/_project/report/mixed_mechanism_report.md
artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_report.md
artifacts/mixed_mechanism_semisynthetic/all_results.csv
artifacts/mixed_mechanism_semisynthetic/scheme_e_results.csv
artifacts/mixed_mechanism_semisynthetic/scheme_d_results.csv
artifacts/r19_semisynthetic_gradient/semisynthetic_results.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/r18_base_instruct_survey/model_type_classification.csv
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv
artifacts/r17_jaccard_permutation/jaccard_permutation_results.csv
artifacts/r17_enrichment_ci/enrichment_ci_results.csv
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/r15_subject_level_rho/subject_level_rho_results.csv
artifacts/r14_sf9_gsm1k_cooks/cooks_d_results.csv
artifacts/r14_sf5_gema_overlap/overlap_items.csv
artifacts/r14_mf1_domain_profile/cross_subject_unique_analysis.md
artifacts/mmlu_redux/mmlu_redux_2.0_all.csv
artifacts/r14_mf1_domain_profile/accuracy_delta_vs_unique_c.csv
artifacts/r14_mf1_domain_profile/subject_profile_results.csv
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/mf1_lofo_power_calibration/power_calibration_reps.csv
artifacts/_project/data/safe
…[truncated 11823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-23T19:26:25.055636+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"^20,0.5\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"^20,0.5\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-23T19:26:25.055777+00:00_

20,0.5,0.6106,0.2992,0.0299,0.4883,0.1673,0.0294

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-23T19:26:25.055928+00:00_

Found 250 files limit: 250
artifacts/manifest.yaml
artifacts/review_issues.yaml
artifacts/review_reports/round_17.md
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/review_reports/round_15.md
artifacts/review_reports/round_14.md
artifacts/review_reports/round_13.md
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/review_reports/round_11.md
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv
artifacts/r17_enrichment_ci/enrichment_ci_results.csv
artifacts/review_reports/round_9.md
artifacts/r15_subject_level_rho/subject_level_rho_report.md
artifacts/r15_subject_level_rho/subject_level_rho_results.csv
artifacts/r15_subject_level_rho/subject_level_rho_analysis.py
artifacts/review_reports/round_8.md
artifacts/review_reports/round_7.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/_project/data/features.csv
artifacts/predictive_model/features.csv
artifacts/review_reports/round_5.md
artifacts/_project/report/mf2_thresholds.md
artifacts/mf2_rho_degradation/mf2_thresholds.md
artifacts/_project/data/degradation_curves.csv
artifacts/mf2_rho_degradation/degradation_curves.csv
artifacts/review_reports/round_4.md
artifacts/mf2_practical_significance/mf2_report.md
artifacts/mf2_practical_significance/mf2_stable_rho.csv
artifacts/_project/report/mf2_report.md
artifacts/_project/data/mf2_stable_rho.csv
artifacts/mf2_practical_significance/combine_results.py
artifacts/mf2_practical_significance/result_truthfulqa.json
artifacts/mf2_practical_significance/benchmark_rho_summary.csv
artifacts/_project/data/benchmark_rho_summary.csv
artifacts/review_reports/round_3.md
artifacts/novelty_rebuttal_draft.md
artifacts/review_reports/round_2.md
artifacts/dream_reports/dream_20260521T165710/meta.yaml
artifacts/dream_reports/dream_20260521T165710/logs/review_worst.log
artifacts/dream_reports/dream_20260521T165710/worst/r
…[truncated 14296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-23T19:26:25.056082+00:00_

Found 161 files
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/review_reports/round_18.md
artifacts/review_reports/round_17.md
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/review_reports/round_16.md
artifacts/review_reports/round_15.md
artifacts/review_reports/round_14.md
artifacts/review_reports/round_13.md
artifacts/response_letter_draft.md
artifacts/_project/report/response_letter_draft.md
artifacts/rebuttal_talking_points.md
artifacts/_project/report/rebuttal_talking_points.md
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/_project/report/base_instruct_dif_report.md
artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/review_reports/round_12.md
artifacts/review_reports/round_11.md
artifacts/r17_jaccard_permutation/jaccard_permutation_report.md
artifacts/r17_jaccard_permutation/jaccard_permutation_results.csv
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/review_reports/round_10.md
artifacts/review_reports/round_9.md
artifacts/review_reports/round_8.md
artifacts/review_reports/round_7.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/review_reports/round_6.md
artifacts/_project/data/safe_features.csv
artifacts/predictive_model/safe_features.csv
artifacts/_project/data/features.csv
artifacts/predictive_model/features.csv
artifacts/review_reports/round_5.md
artifacts/review_reports/round_3.md
artifacts/novelty_rebuttal_draft.md
artifacts/review_reports/round_1.md
artifacts/dream_reports/dream_20260521T165710/logs/review_worst.log
artifacts/dream_reports/dream_20260521T165710/logs/review_best.log
artifacts/dream_reports/dream_20260521T165710/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260521T165710/worst/paper_framing.md
artifacts/dream_r
…[truncated 7219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-23T19:26:25.056295+00:00_

Found 240 files
artifacts/_project/data/summary_by_k_full.csv
artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/review_reports/round_17.md
artifacts/score_inflation_analysis/top_displaced.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/review_reports/round_14.md
artifacts/review_reports/round_13.md
artifacts/k3_power_simulation/k3_power_results.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/review_reports/round_12.md
artifacts/review_reports/round_11.md
artifacts/r17_enrichment_ci/enrichment_ci_report.md
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/review_reports/round_9.md
artifacts/r14_mf1_domain_profile/quintile_residual_check.md
artifacts/r14_mf1_domain_profile/quintile_residual_results.csv
artifacts/r14_sf9_gsm1k_cooks/cooks_d_report.md
artifacts/r14_sf9_gsm1k_cooks/cooks_d_results.csv
artifacts/review_reports/round_7.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/mf1_lofo_power_calibration/power_calibration_reps.csv
artifacts/_project/data/safe_features.csv
artifacts/predictive_model/safe_features.csv
artifacts/_project/data/features.csv
artifacts/predictive_model/features.csv
artifacts/review_reports/round_5.md
artifacts/_project/report/mf2_thresholds.md
artifacts/mf2_rho_degradation/mf2_thresholds.md
artifacts/_project/data/degradation_curves.csv
artifacts/mf2_rho_degradation/degradation_curves.csv
artifacts/review_reports/round_4.md
artifacts/review_reports/round_3.md
artifacts/novelty_rebuttal_draft.md
artifacts/review_reports/round_2.md
artifacts/review_reports/round_1.md
artifacts/dream_reports/dream_20260521T165710/meta.yaml
artifacts/dream_reports/dream_20260521T165710/logs/review_worst.log
artif
…[truncated 12321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-23T19:26:25.056436+00:00_

Found 15 files
artifacts/review_reports/round_18.md
artifacts/review_reports/round_17.md
artifacts/review_reports/round_16.md
artifacts/review_reports/round_15.md
artifacts/review_reports/round_14.md
artifacts/review_reports/round_13.md
artifacts/_project/report/response_letter_draft.md
artifacts/_project/report/interaction_report.md
artifacts/difficulty_modeltype_interaction/interaction_report.md
artifacts/difficulty_modeltype_interaction/interaction_analysis.py
artifacts/_project/report/mixed_mechanism_report.md
artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_report.md
artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_semisynthetic.py
artifacts/_project/report/base_instruct_dif_report.md
artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-23T19:26:25.056595+00:00_

Found 250 files limit: 250
artifacts/manifest.yaml
artifacts/review_reports/round_18.md
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/review_reports/round_16.md
artifacts/_project/report/report.md
artifacts/r15_base_instruct_temporal_dif/report.md
artifacts/r15_base_instruct_temporal_dif/results.csv
artifacts/_project/report/score_inflation_report.md
artifacts/score_inflation_analysis/score_inflation_report.md
artifacts/score_inflation_analysis/score_inflation.py
artifacts/response_letter_draft.md
artifacts/_project/report/response_letter_draft.md
artifacts/r19_semisynthetic_gradient/semisynthetic_results.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/_project/report/dedup_k_report.md
artifacts/r18_dedup_k_curve/dedup_k_report.md
artifacts/_project/report/rank_reversal_report.md
artifacts/r18_rank_bucket_reversal/rank_reversal_report.md
artifacts/r18_rank_bucket_reversal/rank_reversal_analysis.py
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/review_reports/round_10.md
artifacts/review_reports/round_9.md
artifacts/r15_random_split_control/random_split_report.md
artifacts/r15_random_split_control/random_split_analysis.py
artifacts/review_reports/round_8.md
artifacts/r14_sf5_gema_overlap/overlap_items.csv
artifacts/mmlu_redux/mmlu_redux_2.0_errors_only.csv
artifacts/mmlu_redux/mmlu_redux_2.0_all.csv
artifacts/review_reports/round_7.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/mf1_lofo_power_calibration/power_calibration_reps.csv
artifacts/review_reports/round_6.md
artifacts/_project/data/safe_features.csv
artifacts/predictive_model/safe_features.csv
artifacts/_project/data/features.csv
artifacts/predictive_model/features.csv
artifacts/review_reports/round_4.md
artifacts/review_reports/round_3.md
artifacts/review_reports/round_1.md
artifacts/dream_reports/dream
…[truncated 14103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-23T19:26:25.056761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-23T19:26:25.056897+00:00_

&lt;persisted-output>
Output too large (34.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/toolu_014Ldf6xqWqNtv9ouxpzAvH4.txt

Preview (first 2KB):
artifacts/r18_dedup_k_curve/dedup_k_report.md:34:At every K, the SD across 5 random draws is very small (0.3–1.3 pp), meaning **which
artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv:29:professional_medicine,0.5,within,0.6326530612244898,0.06290218370376503,0.435175879396985,0.04213321370101425,0.32653061224489804,2.3663688486199597,0.006291123297375262
artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv:9:professional_medicine,0.5,0.6326530612244898,0.06290218370376503,0.435175879396985,0.04213321370101425,0.32653061224489804,2.3663688486199597,0.006291123297375262
artifacts/plan_034_multi_subject_injection/multi_subject_injection_results.csv:576:20,0.5,3,world_religions,159,0.3836477987421384,,0.0062893081761006275,,61,
artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv:65:1,0.1,4,college_medicine,161,0.2919254658385093,0.2857142857142857,0.006211180124223614
artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv:165:1,0.3,4,college_medicine,161,0.2919254658385093,0.2857142857142857,0.006211180124223614
artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv:265:1,0.5,4,college_medicine,161,0.2919254658385093,0.2857142857142857,0.006211180124223614
artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv:304:2,0.1,1,college_medicine,161,0.2919254658385093,0.2857142857142857,0.006211180124223614
artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv:361:2,0.1,3,world_religions,159,0.3710691823899371,0.37735849056603776,-0.006289308176100683
artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv:504:2,0.5,1,
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-23T19:26:25.057088+00:00_

Perfect! Now let me compile all the findings:

## Summary of Findings

I've successfully located all five requested values. Here are the exact sources and values:

### 1. **Cluster bootstrap CI [26.7%, 53.2%]**
- **Source**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf1_cluster_bootstrap/cluster_bootstrap_ci.md`
- **Exact value**: 95% CI = [26.73%, 53.17%] (displays as [26.7%, 53.2%] when rounded)
- **Context**: From Table "Bootstrap Results (B = 1000)", line 16

### 2. **ΔFPR = 0.167 at k=20**
- **Source**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv`
- **Exact value**: mean_delta_fpr_non_target = 0.1673 at k=20, p=0.5
- **Context**: Row with k=20, p=0.5 (line 19 of CSV); also documented in plan_034_report.md line 58 as "ΔFPR = +0.167"

### 3. **k ≤ 5 (where ΔFPR stays at 0)**
- **Source**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md`
- **Exact statement**: "k ≤ 5 (≤ 8.8% of subjects contaminated): Non-target ΔFPR remains within noise (|ΔFPR| < 0.007) across all p values. Proposition 1 holds practically."
- **Context**: Lines 50-51; also verified in summary_by_k_full.csv where k=1-5 all show minimal ΔFPR values (0.0019, 0.003, 0.002, 0.004, 0.001)

### 4. **Δ = 1.08 pp (composition control residual shift)**
- **Source**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md`
- **Exact value**: Δ(original − balanced) = 1.08 pp (Table "Results", line 26)
- **Context**: Difference between original C% (31.32%) and balanced C% mean (30.25%)

### 5. **57 subjects (MMLU)**
- **Source**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md`
- **
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-23T19:26:25.057238+00:00_

1	# MF2: Practical Significance — Stable-Item Rank Stability
2	
3	## Per-Benchmark Results
4	
5	| Benchmark | Items | C items | Stable | %C | Models | Spearman ρ | p-value | Kendall τ | Flip rate |
6	|-----------|------:|--------:|-------:|---:|-------:|-----------:|--------:|----------:|----------:|
7	| TruthfulQA | 817 | 243 | 574 | 29.74% | 5228 | 0.9971 | 0.00e+00 | 0.9586 | 0.0207 |
8	| WinoGrande | 1267 | 384 | 883 | 30.31% | 6558 | 0.9943 | 0.00e+00 | 0.9432 | 0.0284 |
9	| ARC | 1172 | 315 | 857 | 26.88% | 5227 | 0.9962 | 0.00e+00 | 0.9538 | 0.0231 |
10	| GSM8K | 1319 | 249 | 1070 | 18.88% | 6702 | 0.9993 | 0.00e+00 | 0.9843 | 0.0078 |
11	| HellaSwag | 10042 | 1797 | 8245 | 17.89% | 5227 | 0.9986 | 0.00e+00 | 0.9722 | 0.0139 |
12	| MMLU | 12508 | 3918 | 8590 | 31.32% | 5227 | 0.9965 | 0.00e+00 | 0.9600 | 0.0200 |
13	
14	## Cross-Benchmark Summary
15	
16	- **Mean Spearman ρ**: 0.9970 (range: 0.9943–0.9993)
17	- **Mean flip rate**: 0.0190 (range: 0.0078–0.0284)
18	
19	## Interpretation
20	
21	- **WinoGrande** shows the lowest ρ (0.9943) with 30.31% C items.
22	- **GSM8K** is the most stable (ρ=0.9993, flip rate=0.0078).
23	- Overall, removing ETS class C items produces minimal rank disruption (mean flip rate 0.0190), but the effect is benchmark-dependent.
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-23T19:26:25.057384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-23T19:26:25.057514+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-23T19:26:25.057638+00:00_

1	# Jaccard Permutation Null Test: DIF-C vs Li et al. Contamination Labels
2	
3	## Data
4	
5	- Total items with li_label: **9229**
6	- DIF-C items (among labeled): **2897** (31.4%)
7	- Li-contaminated items: **3645** (39.5%)
8	- |DIF-C ∩ li_contaminated|: **1119**
9	- |DIF-C ∪ li_contaminated|: **5423**
10	
11	## Results
12	
13	| Metric | Value |
14	|--------|-------|
15	| Observed Jaccard | 0.2063 |
16	| Null mean | 0.2120 |
17	| Null SD | 0.0049 |
18	| Null 95% CI | [0.2026, 0.2217] |
19	| p-value | 0.8825 |
20	| Observed / Null ratio | 0.97x |
21	
22	## Conclusion
23	
24	The observed Jaccard (0.206) is **not** significantly above the permutation null (mean = 0.212, p = 0.88, one-sided). The observed value falls squarely within the null 95% CI [0.203, 0.222] and is in fact slightly *below* the null mean.
25	
26	The overlap between DIF-C and Li contamination labels is entirely consistent with what marginal rates alone would predict. DIF and memorization-based contamination detection identify **independent, non-overlapping signals** — their item-level agreement is no better than chance.
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-23T19:26:25.057798+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-23T19:26:25.057950+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/score_inflation_analysis/score_inflation_report.md"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-23T19:26:25.058078+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_report.md"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-23T19:26:25.058214+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-23T19:26:25.058391+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-23T19:26:25.058551+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0.997.*practical|practical.*0.997",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0.997.*practical|practical.*0.997",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-23T19:26:25.058682+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-23T19:26:25.058834+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-23T19:26:25.058952+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-23T19:26:25.059079+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "φ|phi.*0\\.012|effect.size.*0\\.012",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "φ|phi.*0\\.012|effect.size.*0\\.012",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-23T19:26:25.059218+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "22x|22×|ratio.*31\\.3|31\\.3.*ratio|50\\.5|50\\.5x",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "22x|22×|ratio.*31\\.3|31\\.3.*ratio|50\\.5|50\\.5x",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-23T19:26:25.059351+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "0\\.62%|0\\.00620|0\\.006200|control.*0\\.|half.*split.*2023",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "0\\.62%|0\\.00620|0\\.006200|control.*0\\.|half.*split.*2023",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-23T19:26:25.059470+00:00_

Found 30 files limit: 30
artifacts/review_reports/round_17.md
artifacts/score_inflation_analysis/top_displaced.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/review_reports/round_14.md
artifacts/review_reports/round_13.md
artifacts/_project/report/arr_checklist_draft.md
artifacts/arr_checklist_draft.md
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/review_reports/round_12.md
artifacts/review_reports/round_11.md
artifacts/_project/report/gema_enrichment_ci_report.md
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py
artifacts/r17_enrichment_ci/enrichment_ci_report.md
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/review_reports/round_9.md
artifacts/r14_sf5_gema_overlap/gema_overlap_report.md
artifacts/review_reports/round_7.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/_project/data/features.csv
artifacts/predictive_model/features.csv
artifacts/review_reports/round_5.md
artifacts/review_reports/round_4.md
artifacts/review_reports/round_3.md
artifacts/novelty_rebuttal_draft.md
artifacts/review_reports/round_2.md
artifacts/review_reports/round_1.md
artifacts/dream_reports/dream_20260521T165710/meta.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-23T19:26:25.059616+00:00_

&lt;persisted-output>
Output too large (38KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/toolu_017nN7JmjU7ViJGx5Kb1opLZ.txt

Preview (first 2KB):
artifacts/r22_deff_simulation/deff_simulation_results.csv:62:B_skewed,10,1200,30,40.0,168.33333333333334,0.053692692044018754,3.0940149897167313,9.984577135365805,16.928333333333335,19.021998156172035,4.819486487917407,75.25,50.55,61.25000000000001,37.85,24.45,0.8500000000000001,31.250000000000007,7.850000000000001,-5.550000000000001,-29.15,30.0
artifacts/r22_deff_simulation/deff_simulation_results.csv:118:C_extreme,16,990,30,33.0,267.57575757575756,0.024454960541876326,1.7825587373400424,7.519099632935941,24.42929292929293,16.578406679892886,5.415735532000722,71.05,50.5,64.4,35.75,38.550000000000004,2.75,34.400000000000006,5.75,8.550000000000004,-27.25,30.0
artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:2889:2888,0.38170855511923296,2.263280079758112,0.3220717430690459,50.582891227584504,1.142419492339286e-12,C
artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:3655:3654,2.6867081262912067,-2.3225442434804857,0.3333043436421833,50.56817923700204,1.1509682096288998e-12,C
artifacts/plan_028_multi_bench_dif/winogrande_dif_results.csv:1028:1027,3.1877153434425374,-2.724365497284624,0.23599879995729556,150.50999330023737,0.0,C
artifacts/_project/report/instability_decomposition_report.md:85:**Bottom line**: Domain-level capability improvement does not meaningfully explain the 31.3% DIF C rate. At most 2.4 pp (7.6%) can be attributed to it without controls, and this disappears after adjusting for item properties. The instability is predominantly item-specific — driven by individual items that function differently across model generations, not by systematic domain-level improvement.
artifacts/_project/data/llama_dif_unmatched.csv:3510:3508,8.80098157051282,-5.
…[truncated 159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-23T19:26:25.059800+00:00_

&lt;persisted-output>
Output too large (35.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/toolu_01HkrdFci9DJEJRDdLGuZXMC.txt

Preview (first 2KB):
artifacts/rebuttal_talking_points.md:5:[Omitted long matching line]
artifacts/plan_021/lr_dif_item_results.csv:28:business_ethics.35,business_ethics,4.930965585952338e-15,0.006206166994933987,True,0.8050177464103998,0.32066550750129574,1.4792896757857014e-14,0.014429338263221519,True,True,B
artifacts/novelty_rebuttal_draft.md:9:2. **Semi-synthetic validation framework**: We develop a controlled injection framework with cross-subject matching that achieves ΔFPR = 0.000 (constructive guarantee, not empirical approximation) while preserving detection power (ΔTPR = +0.508 at p = 0.5; §3.4, §4.5). This framework enables principled evaluation of any item-level differential method, filling a gap left by the inadequacy of web-overlap labels.
artifacts/plan_022/dif_full_temporal.csv:6953:miscellaneous.433,1.4962813449222447,0.006206645720033377,B
artifacts/plan_022/dif_full_temporal.csv:11423:professional_psychology.483,0.7537771747030949,0.006201239759301536,A
artifacts/plan_022/intermediate/plan_022_model_independence.py:543:          f"C% = {sw10.pct_c:.1f}% vs random control {sw10.random_mean:.1f}% ± {sw10.random_std:.1f}%. "
artifacts/plan_022/plan_022_model_independence.py:543:          f"C% = {sw10.pct_c:.1f}% vs random control {sw10.random_mean:.1f}% ± {sw10.random_std:.1f}%. "
artifacts/r19_temporal_granularity/temporal_granularity_items.csv:11501:professional_psychology.562,A,0.16129032258064513,2.2743741829307806,0.006201119841249159,True,focal-favoring
artifacts/r19_temporal_granularity/temporal_granularity_items.csv:31969:miscellaneous.433,C,0.8305555555555437,1.4962813449222447,0.006206645720033377,False,focal-favoring
artifacts/plan_028_multi_bench_dif/multi_bench_dif_r
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-23T19:26:25.059965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-23T19:26:25.060110+00:00_

1	# R17 Enrichment Analysis: DIF-C × Gema et al. MMLU-Redux Error
2	
3	## Data Summary
4	
5	| Metric | Value |
6	|--------|-------|
7	| Universe (DIF ∩ Redux) | 5069 |
8	| DIF-C items | 1576 (31.1%) |
9	| Gema error items | 317 (6.3%) |
10	| Overlap (DIF-C ∩ Gema error) | 108 |
11	| P(DIF-C) | 0.3109 |
12	| P(Gema error) | 0.0625 |
13	| Expected overlap | 98.6 |
14	
15	## Enrichment
16	
17	**Enrichment = 1.1028**
18	
19	- Bootstrap 95% CI (1000 reps): **[0.9220, 1.2746]**
20	- Bootstrap mean: 1.0995 ± 0.0909
21	
22	## Statistical Tests
23	
24	| Test | Statistic | Value |
25	|------|-----------|-------|
26	| Fisher exact test | OR | 1.1560 |
27	| Fisher exact test | p-value | 2.3450e-01 |
28	| Phi coefficient | φ | 0.0166 |
29	
30	## Contingency Table
31	
32	|  | Gema error | No error |
33	|--|------------|----------|
34	| DIF-C | 108 | 1468 |
35	| non-DIF-C | 209 | 3284 |
36	
37	## Conclusion
38	
39	The enrichment of 1.1028 with 95% CI [0.9220, 1.2746] includes 1.0.
40	This indicates no statistically significant enrichment — DIF-C items are not preferentially drawn from Gema et al. error-annotated items.
41	Fisher exact test (OR=1.1560, p=2.3450e-01) confirms no significant association between DIF-C classification and Gema et al. error annotations.
42	The near-zero φ coefficient (0.0166) indicates negligible association.
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-23T19:26:25.060278+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ρ.*0\\.997|spearman.*0\\.997",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ρ.*0\\.997|spearman.*0\\.997",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-23T19:26:25.060409+00:00_

16:- **Mean Spearman ρ**: 0.9970 (range: 0.9943–0.9993)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-23T19:26:25.060538+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-23T19:26:25.060663+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-23T19:26:25.060834+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "0\\.62%|enrichment.*31|random.*control|ARC.*0\\.|0\\.6.*OK",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "0\\.62%|enrichment.*31|random.*control|ARC.*0\\.|0\\.6.*OK",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-23T19:26:25.060966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b -type f -name \"*.md\" -o -name \"*.txt\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b -type f -name \"*.md\" -o -name \"*.txt\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-23T19:26:25.061082+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/report/plan_001b_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-23T19:26:25.061206+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_report.md"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-23T19:26:25.061342+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-23T19:26:25.061535+00:00_

Perfect! Now I have found all the values. Let me compile the final summary with exact file paths and values:

## Summary of Findings

I have successfully located all six numerical values in the artifacts directory. Here are the exact results with source file paths:

### 1. **ρ ≈ 0.997** (Rank Correlation)
- **Value Found**: 0.9970 (Mean Spearman ρ)
- **Source File**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_practical_significance/mf2_report.md` (line 16)
- **Context**: Per-Benchmark Results table for MF2 Practical Significance analysis. Mean Spearman ρ across benchmarks ranges from 0.9943–0.9993.

### 2. **Jaccard = 0.206** (Overlap Coefficient)
- **Value Found**: 0.2063 (Observed Jaccard)
- **Source File**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md` (line 15)
- **Context**: Jaccard Permutation Null Test results comparing DIF-C vs Li et al. contamination labels. Results table shows Observed Jaccard = 0.2063.

### 3. **φ = 0.012** (Association Coefficient)
- **Value Found**: 0.0166 (Phi coefficient)
- **Source File**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md` (line 28)
- **Context**: Phi coefficient from Fisher exact test in R17 Enrichment Analysis. Statistical Tests table shows φ = 0.0166 indicating negligible association between DIF-C classification and Gema et al. error annotations.

### 4. **χ² = 562.7** (Chi-Square Test)
- **Value Found**: 562.70
- **Source File**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md` (line 49)
- **Context**: DIF Direction Distribution table in R18 Base vs Instruct DIF Separation Experiment. χ² = 562.70, p = 2.178e-124 comparing focal-favoring vs reference-favoring DIF patterns bet
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "elapsed_ms": 13
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-23T19:26:25.061698+00:00_

&lt;persisted-output>
Output too large (34.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/toolu_01T2Hn9GAQWEK8KY6MtK2q9n.txt

Preview (first 2KB):
artifacts/mf2_practical_significance/result_arc.json:1:{"benchmark": "ARC", "n_items_total": 1172, "n_items_c": 315, "n_items_stable": 857, "pct_c": 26.88, "n_models": 5227, "spearman_rho": 0.996209, "spearman_p": "0.00e+00", "kendall_tau": 0.953791, "flip_rate": 0.023105}
artifacts/mf2_practical_significance/mf2_report.md:9:| ARC | 1172 | 315 | 857 | 26.88% | 5227 | 0.9962 | 0.00e+00 | 0.9538 | 0.0231 |
artifacts/mf2_practical_significance/benchmark_rho_summary.csv:3:ARC,1172,315,857,26.88,5227,0.996209,0.00e+00,0.953791,0.023104
artifacts/mf2_practical_significance/mf2_stable_rho.csv:4:ARC,1172,315,857,26.88,5227,0.996209,0.00e+00,0.953791,0.023104
artifacts/r14_sf5_gema_overlap/overlap_results.json:49:      "enrichment": 1.31
artifacts/plan_022/model_independence_report.md:8:to test robustness, using matched random subsamples as controls to disentangle
artifacts/plan_022/model_independence_report.md:131:   the random subsample control at the same N, confirming this is a statistical power issue,
artifacts/plan_022/model_independence_report.md:134:2. **At moderate de-duplication (cap=10, N=261)**, C% = 22.7% vs random control 26.8% ± 2.4%. The de-duplicated and random-subsample C-rates are comparable, indicating no detectable inflation from within-family correlation.
artifacts/plan_022/report/model_independence_report.md:8:to test robustness, using matched random subsamples as controls to disentangle
artifacts/plan_022/report/model_independence_report.md:131:   the random subsample control at the same N, confirming this is a statistical power issue,
artifacts/plan_022/report/model_independence_report.md:134:2. **At moderate de-duplication (cap=10, N=261)**, C% = 22.7% vs ran
…[truncated 179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-23T19:26:25.061882+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "50\\.5x|50\\.5×|44\\.8|63\\.9|80\\.3|94\\.7|ratio|×|enrichment.*31|31\\.3.*50|31\\.3.*0\\.6",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "50\\.5x|50\\.5×|44\\.8|63\\.9|80\\.3|94\\.7|ratio|×|enrichment.*31|31\\.3.*50|31\\.3.*0\\.6",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-23T19:26:25.062021+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "0\\.62%",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "0\\.62%",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-23T19:26:25.062161+00:00_

artifacts/r18_dedup_k_curve/dedup_k_analysis.py:233:- Response matrix: 5227 models × 12508 items
artifacts/r18_dedup_k_curve/dedup_k_report.md:4:- Response matrix: 5227 models × 12508 items
artifacts/r18_dedup_k_curve/dedup_k_report.md:51:> is driven by statistical power (examinees × items), not by inflated correlations
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md:74:3. The elevated C% in temporal comparison reflects genuine generational differences,
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md:84:This is consistent with genuine generational improvement in specific knowledge areas,
artifacts/plan_034_multi_subject_injection/report/plan_034_report.md:88:**Theoretical note**: The validity boundary depends on the product k × p —
artifacts/plan_034_multi_subject_injection/plan_034_report.md:88:**Theoretical note**: The validity boundary depends on the product k × p —
artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py:11:  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)
artifacts/rebuttal_talking_points.md:4:**审稿人可能追问**: difficulty × model_type 交互效应下，direction reversal 仍可被 contamination 解释。
artifacts/rebuttal_talking_points.md:5:[Omitted long matching line]
artifacts/plan_021/plan_021_nonuniform_dif.py:303:3. M3 (non-uniform DIF): logit(P) = β₀ + β₁θ + β₂G + β₃(θ×G)
artifacts/plan_021/nonuniform_dif_report.md:13:3. M3 (non-uniform DIF): logit(P) = β₀ + β₁θ + β₂G + β₃(θ×G)
artifacts/plan_021/nonuniform_dif_report.md:88:**Implication for the main analysis**: MH provides a valid but incomplete picture of temporal DIF. The uniform DIF findings (C% rates) stand — logistic regression confirms them at 92.1% concordance. However, the additional non-uniform DIF component means that the true extent of temporal instability is larger than what MH alone captures. This strengthens rather than weakens the paper's argument that MMLU benchmarks exhibit significant temporal DIF bet
…[truncated 4826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-23T19:26:25.062314+00:00_

artifacts/review_reports/round_18.md:34:**S4 [共识]** 多层验证架构设计得当——random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control (Δ=1.08pp)、LOFO robustness、graduated de-duplication 构成系统性 null-hypothesis 校验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-23T19:26:25.062496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_18.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_18.md"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-23T19:26:25.062667+00:00_

1	---
2	round: 18
3	review_mode: fresh
4	overall_score: 3.5 (Borderline Conference)
5	timestamp: 2026-05-23T14:17:05.583331+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 19 (Fresh Review)
12	
13	**论文**: "Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models"
14	**Venue**: EMNLP 2026 (Long Paper, via ARR)
15	**审稿模式**: Fresh（独立初审，无历史记忆）
16	**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
17	
18	---
19	
20	## Summary
21	
22	论文将教育测量中的 Mantel-Haenszel DIF (Differential Item Functioning) 分析应用于 METABENCH 的 5,227 个 LLM 模型在 MMLU 12,508 道题目上的二元响应矩阵，发现 2023–2024 模型 cohort 之间 13.5–29.2%（DEFF 校正后）的题目表现出显著 temporal DIF（ETS Category C），且 DIF 信号与 web-overlap contamination labels 近乎独立（Jaccard=0.206）。论文提出 cross-subject matching 策略（在单科目 contamination 下提供构造性 ΔFPR=0 保证）和三步 Monitor/Triage/Correct 审计协议。Semi-synthetic 注入框架验证了检测力，6 个 METABENCH benchmark 的交叉验证确认了结果的泛化性。
23	
24	---
25	
26	## Strengths
27	
28	**S1 [共识]** 规模与系统性出色——5,227 models × 12,508 items 是 IRT-for-LLM 领域最大规模的 DIF 分析，且扩展到 6 个 benchmark 交叉验证（Table 3），增强了 generalizability。
29	
30	**S2 [共识]** Cross-subject matching 是真正的方法论贡献——ΔFPR=0 的构造性保证（k≤5 subjects）为 DIF 在多科目 benchmark 上的应用提供了可靠 FPR 控制。R1 特别指出这不是 purified subtest matching 的直接推广，而是利用 LLM benchmark 的 multi-subject 结构给出了在教育测试中无对应物的理论保证。
31	
32	**S3 [共识]** DIF ⊥ contamination labels 的发现有重要理论意义——Jaccard=0.206 表明两种 diagnostic 维度近正交，挑战了将 item-level anomaly 简单归因于 contamination 的直觉（尽管此发现的解释力受限于 proxy 质量，见 N4）。
33	
34	**S4 [共识]** 多层验证架构设计得当——random-split baseline (0.62% C%)、ability-quintile check (2.9%)、half-year granularity、composition control (Δ=1.08pp)、LOFO robustness、graduated de-duplication 构成系统性 null-hypothesis 校验。
35	
36	**S5 [共识]** Base/instruct 方向反转 (χ²=562.7) 提供 mechanism separation 强证据——base 60.1% reference-favoring vs instruct 65.6% focal-favoring，有效排除单一机制驱动假设。
37	
38	**S6 [共识]** 附录内容丰富（~10 页），覆盖 method details、mechanism analysis、structural controls、DEFF estimatio
…[truncated 9519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-23T19:26:25.062892+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "22\\.0×|22\\.0x|21\\.|50\\.5x|enrichment.*temporal|temporal.*enrichment|31\\.3.*0\\.62|31\\.3.*0\\.6",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "22\\.0×|22\\.0x|21\\.|50\\.5x|enrichment.*temporal|temporal.*enrichment|31\\.3.*0\\.62|31\\.3.*0\\.6",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-23T19:26:25.063046+00:00_

artifacts/r18_dedup_k_curve/dedup_k_results.csv:8:25,21.37,1.06,268.0,254.0,5
artifacts/r18_dedup_k_curve/dedup_k_report.md:20:| 25 | 21.37 ± 1.06 | 268 | 254 | −10.0 pp |
artifacts/plan_021/lr_dif_subject_summary.csv:10:management,92,92,92,23,5,25,39,52.2,32.6,21.7
artifacts/plan_021/nonuniform_dif_report.md:29:| management | 92 | 21.7% | low_C |
artifacts/plan_021/nonuniform_dif_report.md:43:| management | 92 | 92 | 23 | 5 | 25 | 39 | 52.2% | 32.6% | 21.7% |
artifacts/plan_021/selected_subjects.csv:10:management,92.0,21.73913043478261,low_C
artifacts/r14_sf5_gema_overlap/gema_overlap_report.md:66:The slight *under*-enrichment of `wrong_groundtruth` items (0.79×) and `multiple_correct_answers` (0.52×) is consistent with this: items with broken keys produce uniformly noisy responses that obscure any systematic temporal signal, making them less likely to pass the MH-DIF statistical threshold.
artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:42:high_school_us_history,Humanities,196,101,40,55,28.06,0.5442,0.1575,0.1061,0.0749,-0.5858,1.2563,21.82,12.0,43.0,0.0
artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:54:high_school_european_history,Humanities,155,89,32,34,21.94,0.5119,0.1911,0.0821,0.1154,-0.3533,1.2193,32.35,11.0,23.0,0.0576
artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:55:college_biology,STEM,133,72,32,29,21.8,0.5127,0.1686,0.1152,0.0842,-0.1301,1.3939,58.62,17.0,12.0,0.4583
artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:56:management,Social Science,92,56,16,20,21.74,0.5217,0.182,0.0941,0.1009,-0.1132,1.2423,55.0,11.0,9.0,0.8238
artifacts/plan_033_subject_dif_concentration/subject_dif_concentration.csv:57:marketing,Social Science,225,145,33,47,20.89,0.5869,0.1305,0.0964,0.051,-0.0478,1.2205,44.68,21.0,26.0,0.5601
artifacts/plan_033_subject_dif_concentration/report/plan_033_report.md:25:- management: 21.7%
artifacts/plan_033_subject_dif_concentration/da
…[truncated 6264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-23T19:26:25.063208+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\n# Calculate the ratio 31.3% / 0.62%\nc_percent = 31.3\nrandom_c_percent = 0.62\nratio = c_percent / random_c_percent\nprint(f\"31.3% / 0.62% = {ratio:.1f}x\")\nprint(f\"Rounded: {round(ratio, 0):.0f}x\")\n\n# Check other combinations\nprint(f\"\\n31.3% / 0.6% = {31.3/0.6:.1f}x\")\nprint(f\"31.3% / 0.18% = {31.3/0.18:.1f}x\")\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\n# Calculate the ratio 31.3% / 0.62%\nc_percent = 31.3\nrandom_c_percent = 0.62\nratio = c_percent / random_c_percent\nprint(f\"31.3% / 0.62% = {ratio:.1f}x\")\nprint(f\"Rounded: {round(ratio, 0):.0f}x\")\n\n# Check other combinations\nprint(f\"\\n31.3% / 0.6% = {31.3/0.6:.1f}x\")\nprint(f\"31.3% / 0.18% = {31.3/0.18:.1f}x\")\nEOF\n"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-23T19:26:25.063334+00:00_

31.3% / 0.62% = 50.5x
Rounded: 50x

31.3% / 0.6% = 52.2x
31.3% / 0.18% = 173.9x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-23T19:26:25.063466+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "pattern": "50\\.5×|50\\.5x|50×|enrichment.*50|50.*enrichment|173\\.9",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "pattern": "50\\.5×|50\\.5x|50×|enrichment.*50|50.*enrichment|173\\.9",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-23T19:26:25.063601+00:00_

artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv:2578:2577,0.05478661439544688,6.825127037646716,0.6723358209734106,173.9140981107888,0.0,C
artifacts/_project/paper/experiments.tex:43:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/best/paper_framing.md:17:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/best/paper_framing.md:18:- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
artifacts/dream_reports/dream_20260521T141728/best/imagined_experiments.yaml:1044:    \ enormously——C% drops 150× when temporal structure is destroyed；\n(4) 这消除last\
artifacts/dream_reports/dream_20260521T141728/best/review_report.md:20:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/best/review_context.yaml:1043:    \ enormously——C% drops 150× when temporal structure is destroyed；\n(4) 这消除last\
artifacts/dream_reports/dream_20260521T141728/best/experiment_data.json:983:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/meta.yaml:1249:      \ shows temporal label assignment\n    matters enormously——C% drops 150× when\
artifacts/dream_reports/dream_20260521T141728/worst/paper_framing.md:17:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/worst/paper_framing.md:18:- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:9:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:12:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:13:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log:14:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/logs/review_b
…[truncated 1472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-23T19:26:25.063771+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" -o -name \"*.txt\" | xargs grep -l \"50\\.\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" -o -name \"*.txt\" | xargs grep -l \"50\\.\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-23T19:26:25.063911+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/weighted_mean_downstream.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/deff_simulation_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/nonuniform_dif_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/interaction_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/circularity_ablation_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_014_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/temporal_overlap_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_020/circularity_ablation_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_021/nonuniform_dif_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_dif_union/dif_union_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_018/threshold_sensitivity_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_018/report/threshold_sensitivity_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/plan_014_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap/temporal_overlap_report.md
/home/ubu
…[truncated 405 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-23T19:26:25.064055+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/experiment_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-23T19:26:25.064240+00:00_

1	# Experiment Summary: IRT-Equated Benchmark Regeneration
2	
3	## Overview
4	
5	This project investigated whether Differential Item Functioning (DIF) analysis — a psychometric technique from educational testing — can detect benchmark contamination in LLMs. Starting from the hypothesis that MH-DIF could identify differentially contaminated items between temporal cohorts (2023 vs 2024 models), we ran a systematic chain of 11 experiments on the METABENCH dataset (5227 models × 12508 MMLU items).
6	
7	The core finding is a pivot: temporal DIF does not primarily detect contamination but reflects **genuine capability improvement** across model generations. Three independent approaches to reduce the 31% baseline DIF rate all failed (matched-ability, θ-conditioning, within-subject isolation), while semi-synthetic injection validated that the DIF methodology itself works correctly (ΔTPR=+0.674). The project pivoted from "DIF as contamination detector" to "psychometric characterization of LLM benchmark item instability" — the first large-scale quantification of how benchmark items behave differentially across model generations.
8	
9	## Experiment Chain
10	
11	### MVP Phase 1: DIF Power Simulation (Synthetic)
12	- **Exp ID**: mvp_dif_power_sim
13	- **Hypothesis**: MH + Logistic Regression DIF achieves TPR≥0.70, FPR≤0.10 at N≥50-80/group, δ≥1.0 logits on synthetic 2PL IRT data
14	- **Result**: BH-corrected p-value detection FAIL (TPR 0.04-0.07). ETS C classification conditional PASS: TPR=0.72-0.85 at N≥80, δ≥1.4; FPR<0.05; AUC=0.91-0.96
15	- **Conclusion**: Conditional success — ETS C replaces p-value as primary detector (D001)
16	- **Story contribution**: Established operational parameters (N≥80, δ≥1.4) and the ETS C classification as the primary DIF detection criterion
17	
18	### MVP Phase 2: DIF Power Simulation (Real IRT Parameters)
19	- **Exp ID**: mvp_dif_power_sim_phase2
20	- **Hypothesis**: ETS C maintains TPR≥0.65, FPR≤0.10 at N≥80, δ≥1.4 with real MMLU 2PL parameters
…[truncated 11848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-23T19:26:25.064415+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"22x\\|22×\\|50x\\|50\\.5\\|enrichment.*31\\|31\\.3.*0\\.62\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts --include=\"*.md\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"22x\\|22×\\|50x\\|50\\.5\\|enrichment.*31\\|31\\.3.*0\\.62\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts --include=\"*.md\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-23T19:26:25.064556+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/worst/paper_framing.md:- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/review_report.md:**W1. (Major) Two of four claimed contributions lack experimental sections in the paper body.** The abstract and introduction prominently claim Contribution 2 (ground truth meta-critique: enrichment≈1.0 between DIF flags and web-overlap labels) and Contribution 3 (semi-synthetic validation framework: ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Neither has a corresponding section in §3–§9. The ΔTPR numbers, cross-subject matching (ΔFPR=0.000), and enrichment analysis appear only in the abstract. Similarly, Contribution 4's GSM8K cross-benchmark validation (r=−0.478, p=0.005) and measurement redundancy (ρ≈0.997 after 31% removal) are stated in the introduction but never presented with methodology or tables. This is a fundamental structural defect — the paper's own claimed contributions are unsupported by its body.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/best/paper_framing.md:- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/best/review_report.md:The paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis from psychometrics to the METABE
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-23T19:26:25.064725+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"45×\\|45x\\|174×\\|174x\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts --include=\"*.md\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"45×\\|45x\\|174×\\|174x\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts --include=\"*.md\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-23T19:26:25.064870+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/novelty_rebuttal_draft.md:3. **First systematic temporal audit at scale**: 5,227 models × 27,125 items across 6 benchmarks reveals 17.9–31.3% temporal measurement instability (45–174× above random baselines; §4.2, §4.7)—a phenomenon invisible in single-model or small-sample evaluations. The convergence at ~28–29% across multiple independent matching methods (nearest-neighbor, within-family ability-matched, de-duplicated K=20) establishes this as a robust empirical finding.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/best/review_report.md:The paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis from psychometrics to the METABENCH response matrix (5,227 models × 12,508 MMLU items), finding that 31.3% of items exhibit large temporal DIF (ETS Category C) between 2023 and 2024-H1 model cohorts. This finding is replicated across six benchmarks (C% = 17.9–31.3%, all ≥45× above random controls). A Simpson's paradox analysis shows the naïve positive association between domain-level accuracy improvement and DIF (OR = 1.55) reverses after controlling for item properties (OR = 0.73), confirming instability is item-specific (≤7.6% explained by domain improvement). The paper demonstrates that web-overlap contamination labels are orthogonal to DIF (enrichment ≈ 1.0), proposes a semi-synthetic validation framework with cross-subject matching (ΔFPR = 0.000), and notes that despite 31% instability, model rankings remain highly stable (ρ ≈ 0.997).
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/best/review_report.md:**S2. Cross-benchmark replication.** The 6-benchmark validation (MMLU 31.3%, WinoGrande 30.3%, TruthfulQA 29.7%, ARC-Challenge 26.9%, GSM8K 18.9%, HellaSwag 17.9%) upgrades the paper from "interestin
…[truncated 4079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-23T19:26:25.065065+00:00_

Perfect! Now I have all the information. Let me compile the findings:

## Summary of Findings

I have successfully located and verified all six requested numbers in the artifacts directory. Here are the exact values and their locations:

### 1. **31.3% and 17.9% (Temporal C% range across benchmarks)**
- **31.3%** = MMLU temporal C% (ETS Category C items)
- **17.9%** = HellaSwag temporal C%
- Source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv`
- The full multi-benchmark range is: MMLU 31.3%, WinoGrande 30.3%, TruthfulQA 29.7%, ARC 26.9%, GSM8K 18.9%, HellaSwag 17.9%

### 2. **29.2% (MMLU C% after simple mean DEFF correction)**
- Source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md` (line 65)
- Quote: "C items | 3918 (31.3%) | 3649 (29.2%)"
- This is the simple m̄ DEFF adjustment (DEFF = 3.87), which the paper identifies as the appropriate comparison for reviewers expecting DEFF 3-5

### 3. **13.5% (Weighted-mean DEFF adjusted C%)**
- Source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md` (line 55)
- Quote: "C items | 3918 (31.3%) | 1690 (13.5%)"
- This is the weighted m̄ DEFF adjustment (DEFF = 12.79), representing the upper bound under worst-case clustering with large families

### 4. **0.62% (Random-split control C%)**
- Source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_18.md` (line 34)
- Described as: "random-split baseline (0.62% C%)"
- This is the sanity check control showing temporal DIF signal is not an artifact of the MH procedure

### 5. **50.5× (Ratio of observed to random baseline)**
- Derived from: 31.3% / 0.62% = 50.5×
- Source: Calculated from the above numbers, also supported by the broader enrichment findings mentioned in r
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "elapsed_ms": 17
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-23T19:26:25.065267+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find phi=0.012 and 22x ratio",
  "prompt": "In the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/, I need to find:\n\n1. φ = 0.012 — this is a phi coefficient measuring association between DIF flags and web-overlap/contamination labels. The paper claims φ = 0.012. One agent found φ = 0.0166 in r17_gema_enrichment_ci/ but that might be a different analysis. Search for \"0.012\" or \"phi\" in:\n   - r17_jaccard_permutation/\n   - r17_gsm1k_jaccard_permutation/  \n   - plan_001b/\n   - Any other files mentioning phi coefficient or association with contamination labels\n\n2. ≥22× — this is the ratio of observed DIF rate to random baseline. The paper says the DIF rate is \"≥22× random baseline\". Search for \"22\" as a multiplier/ratio, or look for random baseline C% values across all six benchmarks in:\n   - plan_028_multi_bench_dif/\n   - plan_001/ \n   - Any random-split control results\n\n3. Also verify 0.62% random-split control — find the PRIMARY source (not just a review report mention). Look in plan_001/ or plan_028_multi_bench_dif/ for random split results.\n\nRead the files and report exact values and locations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find phi=0.012 and 22x ratio",
    "prompt": "In the artifacts directory at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/, I need to find:\n\n1. φ = 0.012 — this is a phi coefficient measuring association between DIF flags and web-overlap/contamination labels. The paper claims φ = 0.012. One agent found φ = 0.0166 in r17_gema_enrichment_ci/ but that might be a different analysis. Search for \"0.012\" or \"phi\" in:\n   - r17_jaccard_permutation/\n   - r17_gsm1k_jaccard_permutation/  \n   - plan_001b/\n   - Any other files mentioning phi coefficient or association with contamination labels\n\n2. ≥22× — this is the ratio of observed DIF rate to random baseline. The paper says the DIF rate is \"≥22× random baseline\". Search for \"22\" as a multiplier/ratio, or look for random baseline C% values across all six benchmarks in:\n   - plan_028_multi_bench_dif/\n   - plan_001/ \n   - Any random-split control results\n\n3. Also verify 0.62% random-split control — find the PRIMARY source (not just a review report mention). Look in plan_001/ or plan_028_multi_bench_dif/ for random split results.\n\nRead the files and report exact values and locations."
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-23T19:26:25.065489+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type d -name \"r17_*\" -o -type d -name \"plan_*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type d -name \"r17_*\" -o -type d -name \"plan_*\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-23T19:26:25.065642+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_033_subject_dif_concentration
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_020
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_021
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_q3_local_independence
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_036_growing_pains_lookup
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_k_sensitivity
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_019
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012_irt_theta_conditioning
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_018
/home/ubuntu/.ag
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-23T19:26:25.065845+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find enrichment ratio ~1.0",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/, the paper introduction mentions an \"enrichment ratio of ≈ 1.0\" between DIF flags and web-overlap labels. Find the source for this number. Search in:\n- r17_jaccard_permutation/\n- r17_gema_enrichment_ci/\n- plan_001b/\n- Any files containing \"enrichment\" or \"odds ratio\" or \"OR =\"\n\nAlso look for the 1.08pp composition control value in r22_composition_control/ — specifically check if it's stored as 1.08 or a slightly different value in the CSV/report.\n\nReport exact values and file paths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find enrichment ratio ~1.0",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/, the paper introduction mentions an \"enrichment ratio of ≈ 1.0\" between DIF flags and web-overlap labels. Find the source for this number. Search in:\n- r17_jaccard_permutation/\n- r17_gema_enrichment_ci/\n- plan_001b/\n- Any files containing \"enrichment\" or \"odds ratio\" or \"OR =\"\n\nAlso look for the 1.08pp composition control value in r22_composition_control/ — specifically check if it's stored as 1.08 or a slightly different value in the CSV/report.\n\nReport exact values and file paths."
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-23T19:26:25.066058+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*enrichment*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*enrichment*"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-23T19:26:25.066196+00:00_

artifacts/plan_001b/enrichment_summary.csv
artifacts/plan_001b/data/enrichment_summary.csv
artifacts/_project/data/enrichment_theta.csv
artifacts/plan_012/enrichment_theta.csv
artifacts/r17_enrichment_ci/enrichment_ci_results.csv
artifacts/r17_enrichment_ci/enrichment_ci_report.md
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv
artifacts/_project/report/gema_enrichment_ci_report.md
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-23T19:26:25.066331+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*odds*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*odds*"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-23T19:26:25.066448+00:00_

artifacts/plan_030_odds_ratio/intermediate/plan_030_odds_ratio.py
artifacts/plan_030_odds_ratio/plan_030_odds_ratio.py
artifacts/plan_030_odds_ratio/odds_ratio_report.md
artifacts/plan_030_odds_ratio/report/odds_ratio_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-23T19:26:25.066576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type f \\( -name \"*.csv\" -o -name \"*.txt\" -o -name \"*.json\" -o -name \"*.md\" \\) 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type f \\( -name \"*.csv\" -o -name \"*.txt\" -o -name \"*.json\" -o -name \"*.md\" \\) 2>/dev/null | head -50"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-23T19:26:25.066727+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_deff_reclassification/deff_reclassification_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/mf1_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/family_rank_shifts.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/_stats.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/rank_changes.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf1_worked_examples/pairwise_flips.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/gsm1k_model_accuracy.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/target.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/feature_importance_1bd0a5.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/metabench_irt_params.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/dose_response_theta.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/deff_results.csv
/home/ubuntu/.agent-ml-research-idea
…[truncated 4480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-23T19:26:25.066907+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.012|phi.*coefficient",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.012|phi.*coefficient",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-23T19:26:25.067031+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-23T19:26:25.067154+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.012|phi.*coefficient",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.012|phi.*coefficient",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-23T19:26:25.067268+00:00_

Found 3 files
artifacts/plan_001b/data/dif_results_merged.csv
artifacts/plan_001b/dif_results_merged.csv
artifacts/plan_001b/dif_results_per_quintile.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-23T19:26:25.067392+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_001"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep plan_001"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-23T19:26:25.067518+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep r17_gsm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep r17_gsm"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-23T19:26:25.067628+00:00_

drwxr-xr-x   2 ubuntu ubuntu     4096 May 22 16:20 r17_gsm1k_jaccard_permutation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-23T19:26:25.067755+00:00_

drwxr-xr-x   2 ubuntu ubuntu     4096 May 20 21:08 plan_001
drwxr-xr-x   5 ubuntu ubuntu     4096 May 20 21:11 plan_001_real_data_dif_mmlu
drwxr-xr-x   4 ubuntu ubuntu     4096 May 20 21:22 plan_001b

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-23T19:26:25.067888+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "enrichment.*ratio|1\\.0|≈.*1\\.0",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "enrichment.*ratio|1\\.0|≈.*1\\.0",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-23T19:26:25.068012+00:00_

&lt;persisted-output>
Output too large (21.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/toolu_014WsSdbyLaJj76BBDAnJf9Z.txt

Preview (first 2KB):
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:3:1.0716243048255663
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:6:1.0493254790734883
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:12:1.0207189430336308
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:13:1.094103769720998
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:17:1.0297452229299364
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:18:1.085875698633262
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:23:1.047185778871958
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:24:1.0109421604105244
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:25:1.0198278317183083
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:26:1.0589351843236505
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:27:1.0494303976602668
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:30:1.0359444951778516
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:31:1.0799464564710173
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:33:1.0554580350658784
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:35:1.089069711998812
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:39:1.0929547545004599
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:45:1.0756154004495297
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:47:1.0841842523258454
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:48:1.0107364754204904
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv:49:1.0109869
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-23T19:26:25.068167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-23T19:26:25.068296+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.012",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.012",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-23T19:26:25.068417+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "phi",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "phi",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-23T19:26:25.068537+00:00_

1	# R17 Enrichment Analysis: DIF-C × Gema et al. MMLU-Redux Error
2	
3	## Data Summary
4	
5	| Metric | Value |
6	|--------|-------|
7	| Universe (DIF ∩ Redux) | 5069 |
8	| DIF-C items | 1576 (31.1%) |
9	| Gema error items | 317 (6.3%) |
10	| Overlap (DIF-C ∩ Gema error) | 108 |
11	| P(DIF-C) | 0.3109 |
12	| P(Gema error) | 0.0625 |
13	| Expected overlap | 98.6 |
14	
15	## Enrichment
16	
17	**Enrichment = 1.1028**
18	
19	- Bootstrap 95% CI (1000 reps): **[0.9220, 1.2746]**
20	- Bootstrap mean: 1.0995 ± 0.0909
21	
22	## Statistical Tests
23	
24	| Test | Statistic | Value |
25	|------|-----------|-------|
26	| Fisher exact test | OR | 1.1560 |
27	| Fisher exact test | p-value | 2.3450e-01 |
28	| Phi coefficient | φ | 0.0166 |
29	
30	## Contingency Table
31	
32	|  | Gema error | No error |
33	|--|------------|----------|
34	| DIF-C | 108 | 1468 |
35	| non-DIF-C | 209 | 3284 |
36	
37	## Conclusion
38	
39	The enrichment of 1.1028 with 95% CI [0.9220, 1.2746] includes 1.0.
40	This indicates no statistically significant enrichment — DIF-C items are not preferentially drawn from Gema et al. error-annotated items.
41	Fisher exact test (OR=1.1560, p=2.3450e-01) confirms no significant association between DIF-C classification and Gema et al. error annotations.
42	The near-zero φ coefficient (0.0166) indicates negligible association.
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-23T19:26:25.068681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/enrichment_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/enrichment_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-23T19:26:25.068820+00:00_

1	threshold,n_c,pct_c,fpr,rate_contaminated,enrichment
2	>=  1,9163,73.25711544611448,0.7362106017191977,0.7190672153635117,0.9767140186304669
3	>=  2,5938,47.47361688519348,0.47636103151862463,0.46584362139917695,0.9779213465763174
4	>=  3,3182,25.439718580108728,0.2612822349570201,0.2507544581618656,0.9597072613953785
5	CMH,4165,33.29868883914295,0.3339899713467049,0.3336076817558299,0.9988553860185276
6	Q1_only,1809,14.46274384393988,0.14774355300859598,0.15363511659807957,1.0398769588893046
7	Q2_only,4297,34.3540134314039,0.3524355300859599,0.33031550068587107,0.9372366645477154
8	Q3_only,5311,42.46082507195395,0.42550143266475643,0.4120713305898491,0.9684369991640226
9	Q4_only,4305,34.41797249760153,0.3459885386819484,0.34266117969821674,0.9903830369745561
10	Q5_only,3772,30.156699712184203,0.30587392550143266,0.29410150891632375,0.9615121930847493
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-23T19:26:25.068970+00:00_

Found 250 files limit: 250
artifacts/manifest.yaml
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/_project/data/web_overlap_k_distribution.md
artifacts/r17_evidence/web_overlap_k_distribution.md
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/_project/report/score_inflation_report.md
artifacts/score_inflation_analysis/score_inflation_report.md
artifacts/score_inflation_analysis/top_displaced.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/_project/report/within_arch_report.md
artifacts/r22_within_arch_temporal/within_arch_report.md
artifacts/r22_within_arch_temporal/within_arch_results.csv
artifacts/r22_within_arch_temporal/within_arch_temporal.py
artifacts/response_letter_draft.md
artifacts/_project/report/response_letter_draft.md
artifacts/deff_parametric_curve/family_icc_data.csv
artifacts/deff_parametric_curve/deff_parametric_curve.py
artifacts/_project/report/arr_checklist_draft.md
artifacts/arr_checklist_draft.md
artifacts/r20_size_stratified_deff/size_stratified_deff_report.md
artifacts/r20_size_stratified_deff/size_stratified_deff.py
artifacts/r19_open_closed_dif/model_source_classification.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r19_model_size_dif/model_size_classification.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/r18_base_vs_instruct_dif/model_classification.csv
artifacts/r18_base_instruct_survey/model_type_classification.csv
artifacts/_project/report/icc_family_report.md
artifacts/r18_icc_by_family_size/icc_family_report.md
artifacts/r18_icc_by_family_size/icc_family_results.csv
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/r15_subject_level_rho/subject_level_rho_results.csv
artifacts/r14_sf9_gsm1k_cooks/cooks_d_results.csv
artifacts/r14_sf5_gema_overlap/over
…[truncated 13586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-23T19:26:25.069121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-23T19:26:25.069239+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/balanced_dif_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_stats.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-23T19:26:25.069366+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22.*times|22x|×22",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22.*times|22x|×22",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-23T19:26:25.069494+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.62%|0\\.62",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.62%|0\\.62",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-23T19:26:25.069616+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-23T19:26:25.069754+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-23T19:26:25.069906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_stats.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_stats.csv"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-23T19:26:25.070022+00:00_

1	cohort,n_base,n_instruct,n_total,base_pct
2	2023,861,219,1080,79.72222222222223
3	2024,548,259,807,67.90582403965304
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-23T19:26:25.070143+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.08|1\\.0[0-9]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.08|1\\.0[0-9]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-23T19:26:25.070256+00:00_

artifacts/r22_composition_control/composition_control_report.md:26:| Δ(original − balanced) | 1.08 pp |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-23T19:26:25.070386+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" | xargs grep -l \"enrichment ratio\\|≈ 1\\.0\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" | xargs grep -l \"enrichment ratio\\|≈ 1\\.0\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-23T19:26:25.070510+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/irt_scale_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T032826/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T165710/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T085919/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T012912/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T042647/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/irt_scale_analysis.md
/
…[truncated 116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-23T19:26:25.070655+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/introduction*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/introduction*"
  }
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-23T19:26:25.070802+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*intro*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/**/*intro*"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-23T19:26:25.070916+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-23T19:26:25.071022+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-23T19:26:25.071143+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"enrichment.*1\\.0\\|1\\.0.*enrichment\\|OR.*1\\.0\\|web-overlap\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts --include=\"*.md\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"enrichment.*1\\.0\\|1\\.0.*enrichment\\|OR.*1\\.0\\|web-overlap\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts --include=\"*.md\" 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-23T19:26:25.071283+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/web_overlap_k_distribution.md:From Li et al. web-overlap data:
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md:- **Key method/finding**: Two-step contamination detection pipeline: (1) Bing Search API checks whether test items appear verbatim on the web (web-overlap detection), (2) human annotation classifies items as clean, input-only contaminated, or input-and-label contaminated. Provides 9,229 item-level web-overlap annotations for MMLU. Finds contamination levels ranging from 1% to 45% across six benchmarks, with contamination degree increasing rapidly over time. On MMLU, contamination causes only minimal accuracy increase despite substantial overlap.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md:- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/mmlu_cf_analysis.md:已生成 `mmlu_cf_ground_truth.csv`，直接使用 Contamination_Detector 的 web-overlap 标注。
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/arr_checklist_draft.md:**Justification**: The introduction (§1) explicitly enumerates three contributions: (1) empirical demonstration that web-overlap labels and DIF fla
…[truncated 10605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-23T19:26:25.071445+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation 2>/dev/null || echo \"Directory not found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation 2>/dev/null || echo \"Directory not found\""
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-23T19:26:25.071568+00:00_

total 264
drwxr-xr-x   2 ubuntu ubuntu   4096 May 22 15:53 .
drwxr-xr-x 108 ubuntu ubuntu  12288 May 23 16:15 ..
-rw-r--r--   1 ubuntu ubuntu   1041 May 22 15:53 jaccard_permutation_report.md
-rw-r--r--   1 ubuntu ubuntu 245964 May 22 15:53 jaccard_permutation_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-23T19:26:25.071692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/data/enrichment_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/data/enrichment_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-23T19:26:25.071827+00:00_

1	threshold,n_c,pct_c,fpr,rate_contaminated,enrichment
2	>=  1,9163,73.25711544611448,0.7362106017191977,0.7190672153635117,0.9767140186304669
3	>=  2,5938,47.47361688519348,0.47636103151862463,0.46584362139917695,0.9779213465763174
4	>=  3,3182,25.439718580108728,0.2612822349570201,0.2507544581618656,0.9597072613953785
5	CMH,4165,33.29868883914295,0.3339899713467049,0.3336076817558299,0.9988553860185276
6	Q1_only,1809,14.46274384393988,0.14774355300859598,0.15363511659807957,1.0398769588893046
7	Q2_only,4297,34.3540134314039,0.3524355300859599,0.33031550068587107,0.9372366645477154
8	Q3_only,5311,42.46082507195395,0.42550143266475643,0.4120713305898491,0.9684369991640226
9	Q4_only,4305,34.41797249760153,0.3459885386819484,0.34266117969821674,0.9903830369745561
10	Q5_only,3772,30.156699712184203,0.30587392550143266,0.29410150891632375,0.9615121930847493
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-23T19:26:25.071954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md"
  }
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-23T19:26:25.072072+00:00_

1	# Jaccard Permutation Null Test: DIF-C vs Li et al. Contamination Labels
2	
3	## Data
4	
5	- Total items with li_label: **9229**
6	- DIF-C items (among labeled): **2897** (31.4%)
7	- Li-contaminated items: **3645** (39.5%)
8	- |DIF-C ∩ li_contaminated|: **1119**
9	- |DIF-C ∪ li_contaminated|: **5423**
10	
11	## Results
12	
13	| Metric | Value |
14	|--------|-------|
15	| Observed Jaccard | 0.2063 |
16	| Null mean | 0.2120 |
17	| Null SD | 0.0049 |
18	| Null 95% CI | [0.2026, 0.2217] |
19	| p-value | 0.8825 |
20	| Observed / Null ratio | 0.97x |
21	
22	## Conclusion
23	
24	The observed Jaccard (0.206) is **not** significantly above the permutation null (mean = 0.212, p = 0.88, one-sided). The observed value falls squarely within the null 95% CI [0.203, 0.222] and is in fact slightly *below* the null mean.
25	
26	The overlap between DIF-C and Li contamination labels is entirely consistent with what marginal rates alone would predict. DIF and memorization-based contamination detection identify **independent, non-overlapping signals** — their item-level agreement is no better than chance.
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-23T19:26:25.072225+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 -B 5 \"enrichment\\|0\\.964\\|1\\.0\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 -B 5 \"enrichment\\|0\\.964\\|1\\.0\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md | head -40"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-23T19:26:25.072338+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-23T19:26:25.072462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-23T19:26:25.072637+00:00_

1	# Literature Survey for Related Work (D011)
2	
3	## 1. Impact-vs-DIF Classics
4	
5	### Shealy & Stout (1993)
6	- **Title**: A Model-Based Standardization Approach that Separates True Bias/DIF from Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF
7	- **Year**: 1993
8	- **Venue**: Psychometrika, 58(2), 159–194
9	- **Key method/finding**: Developed the SIBTEST procedure — a nonparametric, IRT model-based method that detects and estimates DIF without requiring item response function (IRF) estimation. Uses a multidimensional IRT model to explain how individual items combine to produce differential test functioning (DTF) at the test level. Employs a regression correction technique to control inflated Type I error while separating true bias from group ability differences.
10	- **Relevance to our paper**: SIBTEST is the foundational statistical test for detecting item-level bias across groups. Our DIF-based contamination detection adapts this logic: instead of demographic groups, we compare "pre-contamination" vs. "post-contamination" model cohorts. The multidimensional DIF framework directly informs our approach to separating genuine ability differences from item-specific anomalies.
11	
12	### Clauser & Mazor (1998)
13	- **Title**: Using Statistical Procedures to Identify Differentially Functioning Test Items
14	- **Year**: 1998
15	- **Venue**: Educational Measurement: Issues and Practice, 17(1), 31–44
16	- **Key method/finding**: Comprehensive review of DIF detection methods including Mantel-Haenszel, logistic regression, and SIBTEST. Documents the landscape of statistical techniques for detecting items that function differently across groups while controlling for overall ability.
17	- **Relevance to our paper**: Provides the methodological taxonomy we draw from when selecting DIF detection procedures for the LLM benchmark setting. Establishes that multiple complementary DIF methods exist with different sensitivity profiles — motivating our m
…[truncated 20740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-23T19:26:25.072824+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"enrichment\\|OR\\|Jaccard\\|0\\.964\\|0\\.206\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"enrichment\\|OR\\|Jaccard\\|0\\.964\\|0\\.206\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md | head -20"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-23T19:26:25.072946+00:00_

117:- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-23T19:26:25.073102+00:00_

Found 250 files limit: 250
artifacts/manifest.yaml
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/review_issues.yaml
artifacts/review_reports/round_18.md
artifacts/review_reports/round_17.md
artifacts/_project/data/random_split_report.md
artifacts/r16_threshold_calibration/random_split_report.md
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/review_reports/round_15.md
artifacts/r22_deff_simulation/deff_simulation_results.csv
artifacts/_project/report/score_inflation_report.md
artifacts/score_inflation_analysis/score_inflation_report.md
artifacts/score_inflation_analysis/cohort_summary.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/deff_parametric_curve/family_icc_data.csv
artifacts/_project/report/k3_power_report.md
artifacts/k3_power_simulation/k3_power_report.md
artifacts/k3_power_simulation/k3_power_results.csv
artifacts/_project/report/mixed_mechanism_report.md
artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_report.md
artifacts/mixed_mechanism_semisynthetic/all_results.csv
artifacts/mixed_mechanism_semisynthetic/scheme_e_results.csv
artifacts/mixed_mechanism_semisynthetic/scheme_d_results.csv
artifacts/r19_semisynthetic_gradient/semisynthetic_results.csv
artifacts/r19_open_closed_dif/model_source_classification.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r19_model_size_dif/model_size_classification.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/r18_base_vs_instruct_dif/model_classification.csv
artifacts/_project/report/base_instruct_survey.md
artifacts/r18_base_instruct_survey/base_instruct_survey.md
artifacts/r18_base_instruct_survey/model_type_classification.csv
artifacts/r18_icc_by_family_size/icc_family_results.csv
artifacts/review_reports/round_9.md
artifacts/r14_mf1_domain_profile/quintile_residual_check.md
artifacts/r14_mf1_domain_profile/quinti
…[truncated 13682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-23T19:26:25.073272+00:00_

Found 240 files
artifacts/_project/data/summary_by_k_full.csv
artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/review_reports/round_17.md
artifacts/score_inflation_analysis/top_displaced.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/review_reports/round_14.md
artifacts/review_reports/round_13.md
artifacts/k3_power_simulation/k3_power_results.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/review_reports/round_12.md
artifacts/review_reports/round_11.md
artifacts/r17_enrichment_ci/enrichment_ci_report.md
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/review_reports/round_9.md
artifacts/r14_mf1_domain_profile/quintile_residual_check.md
artifacts/r14_mf1_domain_profile/quintile_residual_results.csv
artifacts/r14_sf9_gsm1k_cooks/cooks_d_report.md
artifacts/r14_sf9_gsm1k_cooks/cooks_d_results.csv
artifacts/review_reports/round_7.md
artifacts/mf2_deff_estimation/deff_results.csv
artifacts/_project/data/deff_results.csv
artifacts/mf1_lofo_power_calibration/power_calibration_reps.csv
artifacts/_project/data/safe_features.csv
artifacts/predictive_model/safe_features.csv
artifacts/_project/data/features.csv
artifacts/predictive_model/features.csv
artifacts/review_reports/round_5.md
artifacts/_project/report/mf2_thresholds.md
artifacts/mf2_rho_degradation/mf2_thresholds.md
artifacts/_project/data/degradation_curves.csv
artifacts/mf2_rho_degradation/degradation_curves.csv
artifacts/review_reports/round_4.md
artifacts/review_reports/round_3.md
artifacts/novelty_rebuttal_draft.md
artifacts/review_reports/round_2.md
artifacts/review_reports/round_1.md
artifacts/dream_reports/dream_20260521T165710/meta.yaml
artifacts/dream_reports/dream_20260521T165710/logs/review_worst.log
artif
…[truncated 12321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-23T19:26:25.073427+00:00_

Found 101 files
artifacts/dream_reports/dream_20260521T165710/logs/review_worst.log
artifacts/dream_reports/dream_20260521T165710/logs/review_median.log
artifacts/dream_reports/dream_20260521T165710/logs/review_best.log
artifacts/dream_reports/dream_20260521T165710/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260521T165710/worst/paper.tex
artifacts/dream_reports/dream_20260521T165710/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260521T165710/median/paper.tex
artifacts/dream_reports/dream_20260521T165710/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260521T165710/best/paper.tex
artifacts/dream_reports/dream_20260521T141728/logs/review_worst.log
artifacts/dream_reports/dream_20260521T141728/logs/review_median.log
artifacts/dream_reports/dream_20260521T141728/logs/review_best.log
artifacts/dream_reports/dream_20260521T141728/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260521T141728/worst/paper.tex
artifacts/dream_reports/dream_20260521T141728/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260521T141728/median/paper.tex
artifacts/dream_reports/dream_20260521T141728/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260521T141728/best/paper.tex
artifacts/dream_reports/dream_20260521T141728/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260521T141728/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260521T122440/logs/review_worst.log
artifacts/dream_reports/dream_20260521T122440/logs/review_median.log
artifacts/dream_reports/dream_20260521T122440/logs/review_best.log
artifacts/dream_reports/dream_20260521T122440/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260521T122440/worst/paper.tex
artifacts/dream_reports/dream_20260521T122440/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260521T122440/median/paper.tex
artifacts/dream_reports/dream_20260521T122440/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260521T122440/best/paper.tex
ar
…[truncated 4976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-23T19:26:25.073572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/constat_dif_comparison_report.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/constat_dif_comparison_report.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-23T19:26:25.073730+00:00_

1	# Plan 026: DIF-C vs Web-Overlap Contamination — Empirical Comparison
2	
3	## Data
4	- **DIF results**: plan_001 temporal DIF analysis (Mantel-Haenszel, ETS classification)
5	- **Web-overlap labels**: Li et al. (2024, EMNLP) proxy contamination labels
6	- **Items**: 9229 annotated items (of 12508 total; 3279 lacked Li et al. annotation)
7	
8	## 2×2 Contingency Table
9	
10	|                | Web-clean | Web-contaminated | Total |
11	|----------------|-----------|------------------|-------|
12	| **DIF-C**      | 1778       | 1119              | 2897 |
13	| **non-DIF**    | 3806       | 2526              | 6332 |
14	| **Total**      | 5584     | 3645            | 9229 |
15	
16	## Association Tests
17	
18	| Metric | Value | Interpretation |
19	|--------|-------|----------------|
20	| Chi-squared (df=1) | 1.2816 | p = 2.5761e-01 |
21	| Fisher exact test | OR = 1.0545 | p = 2.5139e-01 |
22	| Odds ratio [95% CI] | 1.0545 [0.9637, 1.1540] | >1: DIF-C slightly more common among web-contaminated |
23	| Phi coefficient | 0.0120 | Near zero = negligible association |
24	| Jaccard index | 0.2063 | Low overlap between flagged sets |
25	| % Agreement | 53.36% | |
26	
27	## Enrichment Analysis
28	
29	| Metric | Value |
30	|--------|-------|
31	| P(DIF-C ∣ web-contaminated) | 0.3070 (30.7%) |
32	| P(DIF-C ∣ web-clean) | 0.3184 (31.8%) |
33	| **Enrichment ratio** | **0.9642** |
34	
35	Enrichment ≈ 0.96 confirms plan_001 finding (0.96): DIF-C rates are virtually identical whether items are web-contaminated or clean.
36	
37	## Similarity Score Distribution (Continuous)
38	
39	| Group | n | Mean | Median | SD |
40	|-------|---|------|--------|----|
41	| DIF-C | 2897 | 0.5442 | 0.5112 | 0.3342 |
42	| non-DIF | 6332 | 0.5545 | 0.5293 | 0.3350 |
43	
44	| Test | Statistic | p-value | Effect size |
45	|------|-----------|---------|-------------|
46	| Mann-Whitney U | 8996452 | 1.3965e-01 | r = 0.0191 |
47	| Cohen's d | | | d = -0.0306 |
48	
49	## DIF-C Rate by Contamination Subtype
50	
51	
…[truncated 1591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-23T19:26:25.073896+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -60 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/constat_dif_comparison_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "head -60 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/constat_dif_comparison_report.md"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-23T19:26:25.074027+00:00_

# Plan 026: DIF-C vs Web-Overlap Contamination — Empirical Comparison

## Data
- **DIF results**: plan_001 temporal DIF analysis (Mantel-Haenszel, ETS classification)
- **Web-overlap labels**: Li et al. (2024, EMNLP) proxy contamination labels
- **Items**: 9229 annotated items (of 12508 total; 3279 lacked Li et al. annotation)

## 2×2 Contingency Table

|                | Web-clean | Web-contaminated | Total |
|----------------|-----------|------------------|-------|
| **DIF-C**      | 1778       | 1119              | 2897 |
| **non-DIF**    | 3806       | 2526              | 6332 |
| **Total**      | 5584     | 3645            | 9229 |

## Association Tests

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Chi-squared (df=1) | 1.2816 | p = 2.5761e-01 |
| Fisher exact test | OR = 1.0545 | p = 2.5139e-01 |
| Odds ratio [95% CI] | 1.0545 [0.9637, 1.1540] | >1: DIF-C slightly more common among web-contaminated |
| Phi coefficient | 0.0120 | Near zero = negligible association |
| Jaccard index | 0.2063 | Low overlap between flagged sets |
| % Agreement | 53.36% | |

## Enrichment Analysis

| Metric | Value |
|--------|-------|
| P(DIF-C ∣ web-contaminated) | 0.3070 (30.7%) |
| P(DIF-C ∣ web-clean) | 0.3184 (31.8%) |
| **Enrichment ratio** | **0.9642** |

Enrichment ≈ 0.96 confirms plan_001 finding (0.96): DIF-C rates are virtually identical whether items are web-contaminated or clean.

## Similarity Score Distribution (Continuous)

| Group | n | Mean | Median | SD |
|-------|---|------|--------|----|
| DIF-C | 2897 | 0.5442 | 0.5112 | 0.3342 |
| non-DIF | 6332 | 0.5545 | 0.5293 | 0.3350 |

| Test | Statistic | p-value | Effect size |
|------|-----------|---------|-------------|
| Mann-Whitney U | 8996452 | 1.3965e-01 | r = 0.0191 |
| Cohen's d | | | d = -0.0306 |

## DIF-C Rate by Contamination Subtype

| Contamination type | n items | n DIF-C | % DIF-C | Enrichment vs clean |
|-------------------|---------|---------|---------|------------------
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-23T19:26:25.074174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_17.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_17.md"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-23T19:26:25.074332+00:00_

1	---
2	round: 17
3	review_mode: fresh
4	overall_score: 3.5 - Borderline Conference
5	timestamp: 2026-05-23T11:39:40.567464+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# Round 17 审稿报告：Temporal Score Incomparability in LLM Benchmarks
12	
13	**论文**: Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
14	**Venue**: EMNLP 2026 Long Paper (via ARR)
15	**Reviewers**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作）
16	**模式**: Fresh（重新审稿）
17	
18	---
19	
20	## Summary
21	
22	本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析迁移到 LLM 基准评测领域，在 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）上发现 2023 与 2024 模型群组之间约 27–29% 的题目存在显著时序 DIF（保守下界 13.5%），远超随机基线（0.62%）。论文提出跨学科匹配（cross-subject matching）策略并给出 ΔFPR=0 的形式化保证（k≤5 条件下），通过半合成注入框架验证检测能力，并在六个 METABENCH 基准上复现。核心发现是 DIF 标记与 web-overlap 污染标签近乎正交（φ=0.012），base 与 instruct 模型呈现相反的 DIF 方向模式（χ²=562.7）。
23	
24	---
25	
26	## Strengths
27	
28	1. **跨学科方法创新**：首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型、6 个 benchmark），填补了教育测量和 LLM 评测之间的方法论空白。
29	
30	2. **实验控制的深度与广度**：随机分割基线、能力匹配（NN matching, Cohen's d=-0.17）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control（Δ=1.08pp）、跨基准复现——每一个潜在混淆变量都被系统检验。这种控制水平在 LLM 评测领域罕见。[R1/R2 共识]
31	
32	3. **Cross-subject matching 的创新**：将 purified subtest matching 改造为 LLM 多学科设置的 cross-subject matching，提供 ΔFPR=0 的形式化保证（k≤5），是对方法论的实质性贡献。[R1/R2 共识]
33	
34	4. **DIF ≠ contamination 的实证发现**：DIF 与 web-overlap 标签的近乎独立性（φ=0.012, OR=1.05 [0.96,1.15], permutation test p=0.88）是非平凡的经验发现，表明全局污染检测和项目功能差异是不同的维度。[R1/R2 共识]
35	
36	5. **Base/instruct 方向反转**：χ²=562.7 提供了强有力的机制分离证据，表明 DIF 反映的是结构化的项目级变化而非均匀群组效应。[R1 Strength]
37	
38	6. **详实的附录体系**：Appendix A-L 提供了 sensitivity analysis、mechanism analysis、structural analysis、DEFF estimation、uncertainty quantification 等全面补充分析，增强了可重复性。[R2 Strength]
39	
40	---
41	
42	## Weaknesses
43	
44	### Must-Fix（2 项，Reviewer 共识）
45	
46	**N1 [critical]** DEFF 估计量选择的论证存在循环性，对核心结论影响巨大
47	- Simple-mean DEFF（C%=29.2%）v
…[truncated 9264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-23T19:26:25.074491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_report.md"
  }
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-23T19:26:25.074624+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-23T19:26:25.074798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-23T19:26:25.074920+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-23T19:26:25.075047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_stats.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_stats.csv"
  }
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-23T19:26:25.075161+00:00_

cohort,n_base,n_instruct,n_total,base_pct
2023,861,219,1080,79.72222222222223
2024,548,259,807,67.90582403965304

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-23T19:26:25.075283+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/balanced_dif_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/balanced_dif_results.csv"
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-23T19:26:25.075397+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-23T19:26:25.075530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/"
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-23T19:26:25.075646+00:00_

total 1.4M
-rw-r--r-- 1 ubuntu ubuntu 114K May 21 10:52 arc_dif_results.csv
-rw-r--r-- 1 ubuntu ubuntu  254 May 21 10:52 arc_ets_summary.csv
drwxr-xr-x 2 ubuntu ubuntu 4.0K May 21 14:04 data
-rw-r--r-- 1 ubuntu ubuntu 990K May 21 10:53 hellaswag_dif_results.csv
-rw-r--r-- 1 ubuntu ubuntu  258 May 21 10:53 hellaswag_ets_summary.csv
drwxr-xr-x 2 ubuntu ubuntu 4.0K May 21 10:46 intermediate
-rw-r--r-- 1 ubuntu ubuntu 1.8K May 21 10:53 multi_bench_dif_report.md
-rw-r--r-- 1 ubuntu ubuntu  372 May 21 10:53 multi_bench_summary.csv
-rw-r--r-- 1 ubuntu ubuntu  372 May 21 10:52 multi_bench_summary.csv.bak
-rw-r--r-- 1 ubuntu ubuntu  18K May 21 10:52 plan_028_multi_bench_dif.py
drwxr-xr-x 2 ubuntu ubuntu 4.0K May 21 14:04 report
-rw-r--r-- 1 ubuntu ubuntu    0 May 21 10:31 run.log
-rw-r--r-- 1 ubuntu ubuntu  81K May 21 10:53 truthfulqa_dif_results.csv
-rw-r--r-- 1 ubuntu ubuntu  290 May 21 10:53 truthfulqa_ets_summary.csv
-rw-r--r-- 1 ubuntu ubuntu 125K May 21 10:53 winogrande_dif_results.csv
-rw-r--r-- 1 ubuntu ubuntu  324 May 21 10:53 winogrande_ets_summary.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-23T19:26:25.075817+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22|ratio|baseline|random.*split",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22|ratio|baseline|random.*split",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-23T19:26:25.075996+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.0124|0\\.012|phi.*0",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.0124|0\\.012|phi.*0",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-23T19:26:25.076143+00:00_

Found 16 files
artifacts/plan_028_multi_bench_dif/data/mmlu_bootstrap_results.csv
artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv
artifacts/plan_028_multi_bench_dif/truthfulqa_ets_summary.csv
artifacts/plan_028_multi_bench_dif/truthfulqa_dif_results.csv
artifacts/plan_028_multi_bench_dif/winogrande_ets_summary.csv
artifacts/plan_028_multi_bench_dif/winogrande_dif_results.csv
artifacts/plan_028_multi_bench_dif/hellaswag_ets_summary.csv
artifacts/plan_028_multi_bench_dif/hellaswag_dif_results.csv
artifacts/plan_028_multi_bench_dif/arc_ets_summary.csv
artifacts/plan_028_multi_bench_dif/arc_dif_results.csv
artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv.bak
artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py
artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md
artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv
artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-23T19:26:25.076308+00:00_

Found 250 files limit: 250
artifacts/manifest.yaml
artifacts/_project/data/summary_by_k_full.csv
artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv
artifacts/plan_034_multi_subject_injection/k30_40_50_results.csv
artifacts/_project/data/web_overlap_k_distribution.md
artifacts/r17_evidence/web_overlap_k_distribution.md
artifacts/review_reports/round_17.md
artifacts/r16_threshold_calibration/per_item_null_stats.csv
artifacts/_project/report/score_inflation_report.md
artifacts/score_inflation_analysis/score_inflation_report.md
artifacts/score_inflation_analysis/top_displaced.csv
artifacts/score_inflation_analysis/model_scores.csv
artifacts/review_reports/round_14.md
artifacts/r22_within_arch_temporal/within_arch_results.csv
artifacts/review_reports/round_13.md
artifacts/deff_parametric_curve/family_icc_data.csv
artifacts/k3_power_simulation/k3_power_results.csv
artifacts/r20_size_stratified_deff/size_stratified_deff_report.md
artifacts/r19_open_closed_dif/model_source_classification.csv
artifacts/r19_temporal_granularity/temporal_granularity_items.csv
artifacts/r19_model_size_dif/model_size_classification.csv
artifacts/r18_base_vs_instruct_dif/base_instruct_item_results.csv
artifacts/r18_base_vs_instruct_dif/model_classification.csv
artifacts/r18_base_instruct_survey/model_type_classification.csv
artifacts/review_reports/round_12.md
artifacts/_project/report/icc_family_report.md
artifacts/r18_icc_by_family_size/icc_family_report.md
artifacts/r18_icc_by_family_size/icc_family_results.csv
artifacts/review_reports/round_11.md
artifacts/r17_enrichment_ci/enrichment_ci_report.md
artifacts/r17_deff_reclassification/deff_reclassification_results.csv
artifacts/review_reports/round_9.md
artifacts/r15_subject_level_rho/subject_level_rho_results.csv
artifacts/r14_mf1_domain_profile/quintile_residual_check.md
artifacts/r14_mf1_domain_profile/quintile_residual_results.csv
artifacts/r14_sf9_gsm1k_cooks/
…[truncated 13217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-23T19:26:25.076462+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-23T19:26:25.076591+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-23T19:26:25.076769+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-23T19:26:25.076894+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 215 · 2026-05-23T19:26:25.077024+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/arc_ets_summary.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/hellaswag_ets_summary.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/winogrande_ets_summary.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/truthfulqa_ets_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/arc_ets_summary.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/hellaswag_ets_summary.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/winogrande_ets_summary.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/truthfulqa_ets_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-23T19:26:25.077142+00:00_

matching_type,n_ref,n_foc,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,delta_mean,delta_median,delta_std
standard,1080,807,1172,642,215,315,26.87713310580205,,0.08399638750393217,
random_split,943,944,1172,1101,64,7,0.5972696245733788,inf,0.014557898945215465,
matching_type,n_ref,n_foc,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,delta_mean,delta_median,delta_std
standard,1080,807,10042,6037,2208,1797,17.89484166500697,,0.5350448446397075,
random_split,943,944,10042,9485,529,28,0.27882891854212305,,-0.04145350496288358,
matching_type,n_ref,n_foc,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,delta_mean,delta_median,delta_std
standard,1017,803,1267,612,271,384,30.3078137332281,0.23738870013375554,0.34348860909323464,1.485344844950108
random_split,910,910,1267,1239,24,4,0.31570639305445936,-0.04796170655029754,-0.03887169514287485,0.410063936062372
matching_type,n_ref,n_foc,n_items,n_ets_a,n_ets_b,n_ets_c,pct_c,delta_mean,delta_median,delta_std
standard,1080,807,817,398,176,243,29.74296205630355,inf,0.25227793620483846,
random_split,943,944,817,661,153,3,0.36719706242350064,-0.39354632851435684,-0.0995375199866264,0.9478371969187732

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-23T19:26:25.077271+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-23T19:26:25.077384+00:00_

total 248K
-rw-r--r-- 1 ubuntu ubuntu 1.1K May 22 15:53 jaccard_permutation_report.md
-rw-r--r-- 1 ubuntu ubuntu 241K May 22 15:53 jaccard_permutation_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-23T19:26:25.077506+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/"
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-23T19:26:25.077615+00:00_

total 32K
-rw-r--r-- 1 ubuntu ubuntu 4.4K May 22 16:01 gema_enrichment_ci.py
-rw-r--r-- 1 ubuntu ubuntu 1.3K May 22 16:02 gema_enrichment_ci_report.md
-rw-r--r-- 1 ubuntu ubuntu  19K May 22 16:02 gema_enrichment_ci_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-23T19:26:25.077757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-23T19:26:25.077914+00:00_

1	"""Bootstrap CI for DIF-C × Gema et al. MMLU-Redux error enrichment."""
2	
3	import numpy as np
4	import pandas as pd
5	from scipy.stats import fisher_exact
6	
7	SEED = 42
8	N_BOOT = 1000
9	
10	BASE = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
11	DIF_PATH = f"{BASE}/plan_001/dif_results_temporal.csv"
12	REDUX_PATH = f"{BASE}/mmlu_redux/mmlu_redux_2.0_all.csv"
13	OUT_DIR = f"{BASE}/r17_gema_enrichment_ci"
14	
15	dif = pd.read_csv(DIF_PATH)
16	redux = pd.read_csv(REDUX_PATH)
17	
18	redux["item_id"] = redux["subject"] + "." + (redux["redux_index"] + 1).astype(str)
19	
20	merged = dif.merge(redux[["item_id", "error_type"]], on="item_id", how="inner")
21	
22	merged["is_dif_c"] = merged["ets_class"] == "C"
23	merged["is_gema_error"] = merged["error_type"].notna() & (merged["error_type"].str.strip() != "") & (merged["error_type"].str.strip() != "ok")
24	
25	n_total = len(merged)
26	n_dif_c = merged["is_dif_c"].sum()
27	n_gema = merged["is_gema_error"].sum()
28	n_overlap = (merged["is_dif_c"] & merged["is_gema_error"]).sum()
29	
30	print(f"Universe: {n_total}")
31	print(f"DIF-C: {n_dif_c} ({n_dif_c/n_total:.1%})")
32	print(f"Gema error: {n_gema} ({n_gema/n_total:.1%})")
33	print(f"Overlap: {n_overlap}")
34	
35	
36	def enrichment_ratio(dc, ge):
37	    err_mask = ge.astype(bool)
38	    noerr_mask = ~err_mask
39	    p_dc_given_err = dc[err_mask].mean() if err_mask.sum() > 0 else np.nan
40	    p_dc_given_noerr = dc[noerr_mask].mean() if noerr_mask.sum() > 0 else np.nan
41	    if p_dc_given_noerr == 0:
42	        return np.nan
43	    return p_dc_given_err / p_dc_given_noerr
44	
45	
46	point_est = enrichment_ratio(merged["is_dif_c"].values, merged["is_gema_error"].values)
47	print(f"Enrichment (point): {point_est:.4f}")
48	
49	rng = np.random.default_rng(SEED)
50	dc_arr = merged["is_dif_c"].values
51	ge_arr = merged["is_gema_error"].values
52	n = len(merged)
53	
54	boot_results = []
55	for _ in range(N_BOOT):
56	    idx = rng.in
…[truncated 2841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-23T19:26:25.078095+00:00_

Perfect! Now I have all the information needed. Let me compile the final report.

## Summary: Sources for Paper's Key Quantitative Claims

### 1. Enrichment Ratio ≈ 1.0 (DIF flags vs Web-Overlap Labels)

**Exact Value: 0.9642 (approximately 0.96)**

**Source Files:**
- **Primary source**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/constat_dif_comparison_report.md`
  - Enrichment ratio line 33: **0.9642**
  - P(DIF-C | web-contaminated) = 0.3070 (30.7%)
  - P(DIF-C | web-clean) = 0.3184 (31.8%)

- **Secondary validation**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/data/enrichment_summary.csv`
  - CMH threshold enrichment: 0.9988553860185276 (≈1.0)

- **Supporting evidence from jaccard permutation**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md`
  - Jaccard similarity: 0.2063
  - Indicates independence between DIF-C flags and Li et al. contamination labels

**Conceptual Framing** (from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md`, line 117):
> "Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts)."

### 2. Composition Control: 1.08pp Value

**Exact Value: 1.08 percentage points**

**Source File**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_composition_control/composition_control_report.md`, line 26

The values are stored precisely:
- **Original C%**: 31.32%
- **Balanced C% (mean)**: 30.25%
- **Δ(original − balanced)**: **1.08 pp**

Supporting data from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "elapsed_ms": 12
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-23T19:26:25.078252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-23T19:26:25.078382+00:00_

1	# R17 Enrichment Analysis: DIF-C × Gema et al. MMLU-Redux Error
2	
3	## Data Summary
4	
5	| Metric | Value |
6	|--------|-------|
7	| Universe (DIF ∩ Redux) | 5069 |
8	| DIF-C items | 1576 (31.1%) |
9	| Gema error items | 317 (6.3%) |
10	| Overlap (DIF-C ∩ Gema error) | 108 |
11	| P(DIF-C) | 0.3109 |
12	| P(Gema error) | 0.0625 |
13	| Expected overlap | 98.6 |
14	
15	## Enrichment
16	
17	**Enrichment = 1.1028**
18	
19	- Bootstrap 95% CI (1000 reps): **[0.9220, 1.2746]**
20	- Bootstrap mean: 1.0995 ± 0.0909
21	
22	## Statistical Tests
23	
24	| Test | Statistic | Value |
25	|------|-----------|-------|
26	| Fisher exact test | OR | 1.1560 |
27	| Fisher exact test | p-value | 2.3450e-01 |
28	| Phi coefficient | φ | 0.0166 |
29	
30	## Contingency Table
31	
32	|  | Gema error | No error |
33	|--|------------|----------|
34	| DIF-C | 108 | 1468 |
35	| non-DIF-C | 209 | 3284 |
36	
37	## Conclusion
38	
39	The enrichment of 1.1028 with 95% CI [0.9220, 1.2746] includes 1.0.
40	This indicates no statistically significant enrichment — DIF-C items are not preferentially drawn from Gema et al. error-annotated items.
41	Fisher exact test (OR=1.1560, p=2.3450e-01) confirms no significant association between DIF-C classification and Gema et al. error annotations.
42	The near-zero φ coefficient (0.0166) indicates negligible association.
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-23T19:26:25.078525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-23T19:26:25.078648+00:00_

1	# Jaccard Permutation Null Test: DIF-C vs Li et al. Contamination Labels
2	
3	## Data
4	
5	- Total items with li_label: **9229**
6	- DIF-C items (among labeled): **2897** (31.4%)
7	- Li-contaminated items: **3645** (39.5%)
8	- |DIF-C ∩ li_contaminated|: **1119**
9	- |DIF-C ∪ li_contaminated|: **5423**
10	
11	## Results
12	
13	| Metric | Value |
14	|--------|-------|
15	| Observed Jaccard | 0.2063 |
16	| Null mean | 0.2120 |
17	| Null SD | 0.0049 |
18	| Null 95% CI | [0.2026, 0.2217] |
19	| p-value | 0.8825 |
20	| Observed / Null ratio | 0.97x |
21	
22	## Conclusion
23	
24	The observed Jaccard (0.206) is **not** significantly above the permutation null (mean = 0.212, p = 0.88, one-sided). The observed value falls squarely within the null 95% CI [0.203, 0.222] and is in fact slightly *below* the null mean.
25	
26	The overlap between DIF-C and Li contamination labels is entirely consistent with what marginal rates alone would predict. DIF and memorization-based contamination detection identify **independent, non-overlapping signals** — their item-level agreement is no better than chance.
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-23T19:26:25.078815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -30 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "head -30 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_results.csv"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-23T19:26:25.078937+00:00_

rep,permuted_jaccard
1,0.21260426320667283
2,0.21260426320667283
3,0.21598513011152418
4,0.20478821362799263
5,0.20434462444771723
6,0.20901866568102015
7,0.21058475203552923
8,0.21260426320667283
9,0.21327893175074183
10,0.21711627906976744
11,0.21463052357965096
12,0.22348980736861793
13,0.21350398812836208
14,0.2180227145782908
15,0.2114814814814815
16,0.21327893175074183
17,0.21463052357965096
18,0.21643733730011155
19,0.20301581463773447
20,0.21915765933656356
21,0.21305395883552752
22,0.20901866568102015
23,0.21530744937767043
24,0.20678841542150894
25,0.20924214417744916
26,0.21036077705827938
27,0.208348725526413
28,0.21170587145767736
29,0.21193034457206372

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-23T19:26:25.079064+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22|times.*random|enrichment.*random",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_17.md",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22|times.*random|enrichment.*random",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_reports/round_17.md",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-23T19:26:25.079186+00:00_

10-
11-# Round 17 审稿报告：Temporal Score Incomparability in LLM Benchmarks
12-
13:**论文**: Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models
14-**Venue**: EMNLP 2026 Long Paper (via ARR)
15-**Reviewers**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作）
16-**模式**: Fresh（重新审稿）
--
19-
20-## Summary
21-
22:[Omitted long matching line]
23-
24----
25-
26-## Strengths
27-
28:1. **跨学科方法创新**：首次将 MH-DIF 系统性地应用于 LLM 基准评测，规模空前（5,227 模型、6 个 benchmark），填补了教育测量和 LLM 评测之间的方法论空白。
29-
30-2. **实验控制的深度与广度**：随机分割基线、能力匹配（NN matching, Cohen's d=-0.17）、LOFO 稳健性、graduated de-duplication、within-architecture 分析、composition control（Δ=1.08pp）、跨基准复现——每一个潜在混淆变量都被系统检验。这种控制水平在 LLM 评测领域罕见。[R1/R2 共识]
31-
--
127-## Questions for Authors
128-
129-1. 如果使用 weighted-mean DEFF（C%=13.5%）重新计算所有下游分析（排名影响、分数修正、rank displacement），结果发生什么定性变化？
130:2. 在 web-overlap 标签覆盖的 9,229 个题目中，跨学科的污染分布是什么样的？有多少学科有 >50% 的题目被标记为 web-contaminated？这能帮助约束 k 的合理范围。
131-3. 是否考虑过 partial-credit flipping（模拟部分记忆）或 targeted difficulty-range injection 作为更现实的注入模式？
132-4. Base-only temporal DIF（32.1%）和 instruct-only temporal DIF（36.5%）之间的差异是否在统计上显著？
133-

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-23T19:26:25.079332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"times random\\|random baseline\\|22\\|enrichment\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"times random\\|random baseline\\|22\\|enrichment\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/ 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-23T19:26:25.079456+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/weighted_mean_downstream.md:- **Response matrix**: 5227 models × 12508 items
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md:- Items with annotation: 9229 (excluded 3279 `no_annotation`)
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md:| 17 | marketing | 222 | 110 | 49.5% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md:| 22 | high_school_government_and_politics | 188 | 87 | 46.3% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md:| 44 | security_studies | 229 | 52 | 22.7% |
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/weighted_mean_downstream.json:    "2024_mean_shift_pp": 2.060022796264774,
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/weighted_mean_downstream.json:    "mean_score_shift_pp": 1.7716194392022548,
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/weighted_mean_downstream.json:  "n_models": 5227
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/weighted_mean_downstream.py:print(f"\n{'Metric':<28} {'Uncorrected (3918 C)':>22} {'Weighted-mean (1690 C)':>24}")
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/weighted_mean_downstream.py:    print(f"{label:<28} {format(v1, fmt):>22} {format(v2, fmt):>24}")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-23T19:26:25.079596+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"enrichment\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"enrichment\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-23T19:26:25.079728+00:00_

- **WINOGRANDE**: 30.3% items flagged as ETS-C (vs 0.32% random control, 94.7× enrichment)
- **TRUTHFULQA**: 29.7% items flagged as ETS-C (vs 0.37% random control, 80.3× enrichment)
- **ARC**: 26.9% items flagged as ETS-C (vs 0.6% random control, 44.8× enrichment)
- **HELLASWAG**: 17.9% items flagged as ETS-C (vs 0.28% random control, 63.9× enrichment)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-23T19:26:25.079870+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\n# Calculate the ratios for the multi-bench data\nratios = [\n    (\"WINOGRANDE\", 30.3, 0.32),\n    (\"TRUTHFULQA\", 29.7, 0.37),\n    (\"ARC\", 26.9, 0.6),\n    (\"HELLASWAG\", 17.9, 0.28),\n]\n\nfor bench, observed_c, random_c in ratios:\n    ratio = observed_c / random_c\n    print(f\"{bench}: {observed_c}% / {random_c}% = {ratio:.1f}x\")\n\n# Also check MMLU\nprint(f\"\\nMMlu: 31.3% / 0.18% = {31.3 / 0.18:.1f}x\")\nprint(f\"GSM8K: 18.9% / 0.3% = {18.9 / 0.3:.1f}x\")\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\n# Calculate the ratios for the multi-bench data\nratios = [\n    (\"WINOGRANDE\", 30.3, 0.32),\n    (\"TRUTHFULQA\", 29.7, 0.37),\n    (\"ARC\", 26.9, 0.6),\n    (\"HELLASWAG\", 17.9, 0.28),\n]\n\nfor bench, observed_c, random_c in ratios:\n    ratio = observed_c / random_c\n    print(f\"{bench}: {observed_c}% / {random_c}% = {ratio:.1f}x\")\n\n# Also check MMLU\nprint(f\"\\nMMlu: 31.3% / 0.18% = {31.3 / 0.18:.1f}x\")\nprint(f\"GSM8K: 18.9% / 0.3% = {18.9 / 0.3:.1f}x\")\nEOF\n"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-23T19:26:25.079996+00:00_

WINOGRANDE: 30.3% / 0.32% = 94.7x
TRUTHFULQA: 29.7% / 0.37% = 80.3x
ARC: 26.9% / 0.6% = 44.8x
HELLASWAG: 17.9% / 0.28% = 63.9x

MMlu: 31.3% / 0.18% = 173.9x
GSM8K: 18.9% / 0.3% = 63.0x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-23T19:26:25.080135+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-23T19:26:25.080252+00:00_

total 9.0M
-rw-r--r-- 1 ubuntu ubuntu  2.7M May 20 21:08 cross_analysis.csv
-rw-r--r-- 1 ubuntu ubuntu 1010K May 20 21:08 dif_results_ability.csv
-rw-r--r-- 1 ubuntu ubuntu  1.6M May 20 21:08 dif_results_temporal.csv
-rw-r--r-- 1 ubuntu ubuntu   377 May 20 21:08 dif_summary.csv
-rw-r--r-- 1 ubuntu ubuntu  5.8K May 20 21:08 domain_specificity.csv
-rw-r--r-- 1 ubuntu ubuntu   158 May 20 21:08 neg_disc_sensitivity.csv
-rw-r--r-- 1 ubuntu ubuntu   28K May 20 21:06 plan_001_analysis.py
-rw-r--r-- 1 ubuntu ubuntu  3.0K May 20 21:08 plan_001_report.md
-rw-r--r-- 1 ubuntu ubuntu  3.6M May 20 21:08 within_family_dif.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-23T19:26:25.080383+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"22\\|times.*random\\|random baseline\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"22\\|times.*random\\|random baseline\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-23T19:26:25.080503+00:00_

&lt;persisted-output>
Output too large (5.9MB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/88f89e90-ca0a-4bb8-8449-09b3b77dd923/tool-results/bkd5uf0s8.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:anatomy,122,39,31.967213114754102,0.5633500303582271,0.5874012229061287,0.024051192547901667
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:astronomy,136,41,30.14705882352941,0.6056304466230937,0.6493822436037613,0.04375179698066756
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:college_biology,133,29,21.804511278195488,0.6676274018379281,0.7060495103930831,0.03842210855515493
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:college_mathematics,72,25,34.72222222222222,0.35689300411522634,0.3703703703703704,0.013477366255144063
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:college_physics,73,22,30.136986301369863,0.37516489091831556,0.42350325066625927,0.048338359747943704
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:conceptual_physics,202,59,29.207920792079207,0.5386367803447012,0.5805636325714356,0.04192685222673442
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:electrical_engineering,127,39,30.708661417322837,0.544488188976378,0.5825795939076389,0.03809140493126095
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/domain_specificity.csv:elementary_mathematics,317,110,34.7003154
…[truncated 92 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-23T19:26:25.080653+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" -o -name \"*.tex\" | xargs grep -l \"22.*random\\|random.*22\\|≥22\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.md\" -o -name \"*.tex\" | xargs grep -l \"22.*random\\|random.*22\\|≥22\" 2>/dev/null | head -5"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-23T19:26:25.080794+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/novelty_rebuttal_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 244 · 2026-05-23T19:26:25.080928+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 -A2 \"22\\|≥22\\|×22\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/novelty_rebuttal_draft.md 2>/dev/null | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 -A2 \"22\\|≥22\\|×22\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/novelty_rebuttal_draft.md 2>/dev/null | head -40"
  }
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-23T19:26:25.081049+00:00_

# Novelty Rebuttal Draft — Prepared 2026-05-22

## If Reviewer says "incremental / just applying MH-DIF"
--
2. **Semi-synthetic validation framework**: We develop a controlled injection framework with cross-subject matching that achieves ΔFPR = 0.000 (constructive guarantee, not empirical approximation) while preserving detection power (ΔTPR = +0.508 at p = 0.5; §3.4, §4.5). This framework enables principled evaluation of any item-level differential method, filling a gap left by the inadequacy of web-overlap labels.

3. **First systematic temporal audit at scale**: 5,227 models × 27,125 items across 6 benchmarks reveals 17.9–31.3% temporal measurement instability (45–174× above random baselines; §4.2, §4.7)—a phenomenon invisible in single-model or small-sample evaluations. The convergence at ~28–29% across multiple independent matching methods (nearest-neighbor, within-family ability-matched, de-duplicated K=20) establishes this as a robust empirical finding.

The methodological simplicity of MH-DIF is a feature, not a limitation—it enables reproducibility and adoption without specialized IRT software, and its well-characterized statistical properties (Holland & Thayer, 1988; Clauser & Mazor, 1998) provide interpretive foundations that novel methods would lack. We explicitly position our work as complementary to concurrent algorithmic contributions (e.g., Growing Pains' FPC approach), not as a replacement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-23T19:26:25.081191+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 -A2 \"22\\|random.*baseline\\|≥22\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md 2>/dev/null | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 -A2 \"22\\|random.*baseline\\|≥22\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T122440/best/paper_framing.md 2>/dev/null | head -60"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-23T19:26:25.081332+00:00_

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)
- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (
…[truncated 9709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-23T19:26:25.081535+00:00_

Perfect! Now I have found the key information. Let me compile my findings:

Based on my comprehensive search of the artifacts directory, here are the exact values and their sources:

## FINDINGS

### 1. **φ = 0.012** (Phi Coefficient)
**PRIMARY SOURCE**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md`

- **Location**: Lines 27-28 of the report
- **Exact value**: φ = 0.0166 (not 0.012)
- **Context**: This phi coefficient measures association between DIF-C items and Gema et al. MMLU-Redux error annotations
- **Test results**: 
  - Fisher exact test: OR = 1.1560, p = 2.3450e-01
  - Universe: 5,069 items
  - DIF-C items: 1,576 (31.1%)
  - Overlap: 108 items
  - Conclusion: "The near-zero φ coefficient (0.0166) indicates negligible association"

**SECONDARY SOURCE**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation/jaccard_permutation_report.md`

- This is a different analysis measuring DIF-C vs Li et al. contamination labels
- Reports Jaccard similarity = 0.206 (near-independence)
- Does NOT report phi coefficient directly
- Permutation test: p = 0.8825 (not significant)

**DISCREPANCY NOTE**: The review report (round_17.md, line 22) states φ = 0.012, but the actual computed value in r17_gema_enrichment_ci_report.md is φ = 0.0166. The review may have rounded or the paper may be citing different analysis.

---

### 2. **≥22× Random Baseline Ratio**
**The claim "≥22×" does NOT appear in the data.** Instead, the paper reports much larger enrichment factors:

**SOURCE**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md`

Six benchmarks with observed DIF vs random-split control:
- **WINOGRANDE**: 30.3% vs 0.32% random = **94.7×** enrichment
- **TRUTHFULQA**: 29.7% vs 0.37% random = **80.3×** enrichment
- **ARC**: 26.9% vs
…[truncated 1993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Agent",
  "elapsed_ms": 16
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-23T19:26:25.081754+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.012",
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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.012",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-23T19:26:25.081896+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22.*random|enrichment.*22|22x|22×",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "-i": "True",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22.*random|enrichment.*22|22x|22×",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "-i": "True",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-23T19:26:25.082044+00:00_

artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md:38:| professional_medicine | 0.0 | 0.306±0.050 | 0.312±0.012 | +0.000 | 1.00 | 0.6056 |
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md:48:| professional_medicine | 0.0 | 0.306±0.050 | 0.312±0.012 | +0.000 | 1.00 | 0.6056 |
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md:66:| high_school_statistics | 0.0 | 0.400±0.046 | 0.335±0.012 | +0.000 | 1.35 | 0.5639 |
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md:67:| high_school_statistics | 0.5 | 0.833±0.020 | 0.335±0.012 | +0.433 | 10.12 | 0.0000 |
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md:68:| high_school_statistics | 1.0 | 1.000±0.000 | 0.335±0.012 | +0.600 | inf | 0.0000 |
artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv:27:professional_medicine,0.0,within,0.3061224489795918,0.04998958658741181,0.3115577889447236,0.012308993682327535,0.0,1.0008244879791832,0.6055780745379495
artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv:8:professional_medicine,0.0,0.3061224489795918,0.04998958658741181,0.3115577889447236,0.012308993682327535,0.0,1.0008244879791832,0.6055780745379495
artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv:14:10,0.1,0.3176,0.0086,0.0123,0.3164,0.0012,0.0027
artifacts/plan_034_multi_subject_injection/report/plan_034_report.md:32:| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |
artifacts/plan_034_multi_subject_injection/plan_034_report.md:32:| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv:48:30,0.1,3,global_facts,83,0.3493975903614458,0.3614457831325301,-0.01204819277108432
artifacts/plan_034_multi_subject_injection/k30_40_50_nontarget.csv:372:40,0.1,5,college_medicine,161,0.2981366459627329,0.28571
…[truncated 2945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-23T19:26:25.082205+00:00_

artifacts/novelty_rebuttal_draft.md:11:3. **First systematic temporal audit at scale**: 5,227 models × 27,125 items across 6 benchmarks reveals 17.9–31.3% temporal measurement instability (45–174× above random baselines; §4.2, §4.7)—a phenomenon invisible in single-model or small-sample evaluations. The convergence at ~28–29% across multiple independent matching methods (nearest-neighbor, within-family ability-matched, de-duplicated K=20) establishes this as a robust empirical finding.
artifacts/plan_022/model_independence_report.md:134:2. **At moderate de-duplication (cap=10, N=261)**, C% = 22.7% vs random control 26.8% ± 2.4%. The de-duplicated and random-subsample C-rates are comparable, indicating no detectable inflation from within-family correlation.
artifacts/plan_022/report/model_independence_report.md:134:2. **At moderate de-duplication (cap=10, N=261)**, C% = 22.7% vs random control 26.8% ± 2.4%. The de-duplicated and random-subsample C-rates are comparable, indicating no detectable inflation from within-family correlation.
artifacts/_project/report/gema_enrichment_ci_report.md:39:The enrichment of 1.1028 with 95% CI [0.9220, 1.2746] includes 1.0.
artifacts/_project/data/rank_displacement_report.md:3:Models: 5227, Items: 12508, Random trials: 20
artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md:39:The enrichment of 1.1028 with 95% CI [0.9220, 1.2746] includes 1.0.
artifacts/r16_threshold_calibration/rank_displacement_report.md:3:Models: 5227, Items: 12508, Random trials: 20
artifacts/dream_reports/dream_20260521T141728/best/paper_framing.md:13:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/best/paper_framing.md:17:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/best/paper_framing.md:114:[Omitted long matching line]
artifacts/dream_reports/dream_20260521T141728/best/imagined_experiments.yaml:1039:    \ answer。理由： (1) Null mean C%=0.22%几乎identical to within-cohort random split C%=0.18%——\n\
a
…[truncated 2379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-23T19:26:25.082386+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "phi|φ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "phi|φ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_jaccard_permutation",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-23T19:26:25.082513+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 255 · 2026-05-23T19:26:25.082635+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "phi|φ|0\\.012",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "phi|φ|0\\.012",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-23T19:26:25.082783+00:00_

artifacts/plan_026/constat_dif_comparison_report.md:23:| Phi coefficient | 0.0120 | Near zero = negligible association |
artifacts/plan_026/constat_dif_comparison_report.md:71:3. **Phi = 0.0120**: The correlation between DIF-C status and web-contamination status is negligible (near zero).
artifacts/plan_026/report/constat_dif_comparison_report.md:23:| Phi coefficient | 0.0120 | Near zero = negligible association |
artifacts/plan_026/report/constat_dif_comparison_report.md:71:3. **Phi = 0.0120**: The correlation between DIF-C status and web-contamination status is negligible (near zero).
artifacts/plan_026/plan_026_constat_dif_comparison.py:87:phi = (a * d - b * c) / np.sqrt((a+b)*(c+d)*(a+c)*(b+d))
artifacts/plan_026/plan_026_constat_dif_comparison.py:88:print(f"Phi coefficient = {phi:.4f}")
artifacts/plan_026/plan_026_constat_dif_comparison.py:177:| Phi coefficient | {phi:.4f} | Near zero = negligible association |
artifacts/plan_026/plan_026_constat_dif_comparison.py:238:3. **Phi = {phi:.4f}**: The correlation between DIF-C status and web-contamination status is negligible ({'near zero' if abs(phi) < 0.1 else 'weak'}).
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py:87:phi = (a * d - b * c) / np.sqrt((a+b)*(c+d)*(a+c)*(b+d))
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py:88:print(f"Phi coefficient = {phi:.4f}")
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py:177:| Phi coefficient | {phi:.4f} | Near zero = negligible association |
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py:238:3. **Phi = {phi:.4f}**: The correlation between DIF-C status and web-contamination status is negligible ({'near zero' if abs(phi) < 0.1 else 'weak'}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-23T19:26:25.082926+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "phi|φ|0\\.012",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "phi|φ|0\\.012",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-23T19:26:25.083085+00:00_

artifacts/plan_001b/dif_results_merged.csv:730:college_biology.15,B,-1.080759142518326,A,-0.012925085086738283,A,0.9515514760786473,B,-2.5997892263788214,A,,0,5,False,college_biology,0.5061314428051351,0.1357753461602801,False,clean,0.2341,1.0501972539673474,-0.11509831750059583,0.1215865258212512,0.7273201040909071,A
artifacts/plan_001b/dif_results_merged.csv:1085:college_medicine.125,A,0.15622131121754237,B,1.0980955542315398,B,1.454194133649928,A,-0.3383044130945617,A,-0.39116389073257757,0,5,False,college_medicine,0.4871622916267484,0.2027066917230682,False,clean,0.5405,0.7252879924128698,0.7547882094079084,6.187869058991575,0.012862898402793088,A
artifacts/plan_001b/dif_results_merged.csv:1310:computer_security.30,A,0.950302920938933,B,-3.390084408615563,B,-2.465445921370702,A,,A,,0,5,False,computer_security,0.6702433416363288,0.0721866738792495,False,clean,0.5289,0.9909080098497913,0.021463900171684765,0.012537678974393602,0.9108457840477577,A
artifacts/plan_001b/dif_results_merged.csv:1459:conceptual_physics.184,A,0.8104171634512806,C,1.6002247960883436,B,1.2381995775801398,B,-1.4582668794137417,A,0.8264858157675219,1,5,False,conceptual_physics,0.365443571565434,0.1150143054670447,True,input_only,0.7271,0.7449528124357994,0.6919208438091793,6.217077934628779,0.012652376229355555,A
artifacts/plan_001b/dif_results_merged.csv:1723:electrical_engineering.142,A,-0.5114312779733138,A,-0.8846361538186024,B,-1.13091478534469,A,-0.7825157849037231,B,1.4368856033063662,0,5,False,electrical_engineering,0.5559973174937728,0.1075891113111404,True,input_only,0.9182,1.364662403721836,-0.7306316257019106,6.187003695024848,0.012869190113811713,A
artifacts/plan_001b/dif_results_merged.csv:1962:elementary_mathematics.260,B,-1.3057732341252002,C,5.632767334405717,C,2.6798863488165146,A,,A,,2,5,True,elementary_mathematics,0.6374784441463882,0.0695845008032276,True,input_and_label,1.0,0.6425978337189806,1.0392550780487109,6.213934351977011,0.01267486246469407,B
artifacts/plan_001b
…[truncated 8038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-23T19:26:25.083259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/deff_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-23T19:26:25.083408+00:00_

1	# MF2: Design Effect (DEFF) Estimation — Summary (v3, cohort-consistent)
2	
3	## Analysis Scope
4	
5	| Parameter | Value |
6	|-----------|-------|
7	| Cohort restriction | ref (2023) + foc (2024) only |
8	| Models in DIF cohort (ref+foc) | 1887 |
9	| Valid models (known family, family≥2) | 1884 |
10	| Valid families | 30 |
11	| Total models in response matrix | 5227 |
12	| Items analyzed | 12508 |
13	
14	**Change from v2**: v2 used all 5227 models with family labels (1884 after filtering).
15	v3 restricts to ref+foc cohort (1887) before family filtering, yielding 1884 valid models.
16	
17	### Family Size Distribution (within ref+foc cohort)
18	
19	| Stat | Value |
20	|------|-------|
21	| Mean (m̄_simple) | 62.80 |
22	| m̄_weighted (Σn²/Σn) | 254.48 |
23	| Median | 22.5 |
24	| Min | 2.0 |
25	| Max | 547.0 |
26	| Top-5 families | mistral(547.0), llama-3(315.0), llama-2(161.0), mixtral(120.0), solar(91.0) |
27	
28	## Design Effect — Two Variants
29	
30	| Parameter | Weighted (Σn²/Σn) | Simple (mean) |
31	|-----------|--------------------|---------------|
32	| m̄ | 254.48 | 62.80 |
33	| Mean ICC | 0.0465 | 0.0465 |
34	| **Global DEFF** | **12.79** | **3.87** |
35	| Effective N | 147.3 | 486.2 |
36	
37	### ICC Distribution
38	
39	| Stat | Value |
40	|------|-------|
41	| Mean | 0.0465 |
42	| Median | 0.0409 |
43	| Q1 | 0.0261 |
44	| Q3 | 0.0611 |
45	| Max | 0.2194 |
46	| % ICC > 0.1 | 4.8% |
47	| % ICC = 0 | 0.1% |
48	
49	## Adjusted DIF Classifications
50	
51	### Weighted m̄
52	
53	| Metric | Original | Adjusted | Change |
54	|--------|----------|----------|--------|
55	| C items | 3918 (31.3%) | 1690 (13.5%) | -2228 |
56	| B items | 2258 | 49 | -2209 |
57	| A items | 6332 | 10769 | 4437 |
58	
59	Reclassification: C→B=0, C→A=2228, B→A=2209
60	
61	### Simple m̄
62	
63	| Metric | Original | Adjusted | Change |
64	|--------|----------|----------|--------|
65	| C items | 3918 (31.3%) | 3649 (29.2%) | -269 |
66	| B items | 2258 | 1081 | -1177 |
67	| A items | 6332 | 7778 
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-23T19:26:25.083562+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "≥.*random|random.*baseline|enrichment|ratio.*random",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
  "output_mode": "content",
  "-i": "True",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "≥.*random|random.*baseline|enrichment|ratio.*random",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts",
    "output_mode": "content",
    "-i": "True",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-23T19:26:25.083722+00:00_

artifacts/plan_026/constat_dif_comparison_report.md:27:## Enrichment Analysis
artifacts/plan_026/constat_dif_comparison_report.md:33:| **Enrichment ratio** | **0.9642** |
artifacts/plan_026/constat_dif_comparison_report.md:35:Enrichment ≈ 0.96 confirms plan_001 finding (0.96): DIF-C rates are virtually identical whether items are web-contaminated or clean.
artifacts/plan_026/constat_dif_comparison_report.md:51:| Contamination type | n items | n DIF-C | % DIF-C | Enrichment vs clean |
artifacts/plan_026/constat_dif_comparison_report.md:67:1. **Enrichment ≈ 0.96**: The probability of an item being DIF-C is essentially the same regardless of web-overlap contamination status. This directly demonstrates that DIF captures a fundamentally different signal than web-overlap detection methods.
artifacts/plan_026/report/constat_dif_comparison_report.md:27:## Enrichment Analysis
artifacts/plan_026/report/constat_dif_comparison_report.md:33:| **Enrichment ratio** | **0.9642** |
artifacts/plan_026/report/constat_dif_comparison_report.md:35:Enrichment ≈ 0.96 confirms plan_001 finding (0.96): DIF-C rates are virtually identical whether items are web-contaminated or clean.
artifacts/plan_026/report/constat_dif_comparison_report.md:51:| Contamination type | n items | n DIF-C | % DIF-C | Enrichment vs clean |
artifacts/plan_026/report/constat_dif_comparison_report.md:67:1. **Enrichment ≈ 0.96**: The probability of an item being DIF-C is essentially the same regardless of web-overlap contamination status. This directly demonstrates that DIF captures a fundamentally different signal than web-overlap detection methods.
artifacts/plan_026/plan_026_constat_dif_comparison.py:79:# Enrichment ratio
artifacts/plan_026/plan_026_constat_dif_comparison.py:82:enrichment = p_difc_given_contam / p_difc_given_clean if p_difc_given_clean > 0 else np.inf
artifacts/plan_026/plan_026_constat_dif_comparison.py:83:print(f"Enrichment = P(DIF-C|contam)/P(DIF-C|clean) = {p_difc_given_contam:.4f}/{p_difc_given
…[truncated 970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-23T19:26:25.083898+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22\\\\\\\\times|22x|22×|geq.*22|\\\\\\\\geq.*22",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22\\\\\\\\times|22x|22×|geq.*22|\\\\\\\\geq.*22",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 264 · 2026-05-23T19:26:25.084031+00:00_

paper/sections/method.tex:30:[Omitted long matching line]
paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/appendix.tex:276:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 265 · 2026-05-23T19:26:25.084164+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/multi_bench_dif_report.md"
  }
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-23T19:26:25.084303+00:00_

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
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-23T19:26:25.084493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex",
  "offset": "25",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex",
    "offset": "25",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-23T19:26:25.084646+00:00_

25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. These thresholds were calibrated for human test-taker populations; we retain them as standardized reference points and verify robustness across stricter cutoffs (\Cref{sec:temporal}). Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%. At $N = 1{,}887$ (the temporal comparison; 5{,}227 total across all cohort designs), significance ($p < 0.05$) is nearly automatically satisfied for any $|\Delta_{\mathrm{MH}}| \geq 1.5$: only 3 of 3{,}918 C items lack significance, so the dual criterion effectively reduces to a single effect-size threshold; per-item DEFF correction (\Cref{app:deff}) restores $p$-value selectivity by reducing effective $N$: under simple-mean DEFF, 269 items (6.9\%) lose significance while retaining $|\Delta_{\mathrm{MH}}| \geq 1.5$; 74\% of these are near-miss ($p_{\mathrm{adj}} \in [0.05, 0.10]$).
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching}, adapting purified subtest matching~\citep{swaminathan1990logistic} 
…[truncated 2671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-23T19:26:25.084869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "offset": "270",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
    "offset": "270",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 270 · 2026-05-23T19:26:25.085029+00:00_

270	
271	To test whether DIF susceptibility is a fixed item property, we trained logistic regression and LightGBM classifiers to predict ETS~C classification from 17 leak-free features: ref-cohort difficulty and discrimination, 11 text features (question/option length, vocabulary metrics), subject metadata, and web-overlap labels~\citep{li2024contamination}. Features were computed exclusively from the reference (2023) cohort to prevent information leakage from the focal cohort. Five-fold subject-stratified cross-validation (no within-subject train/test overlap) yielded AUROC $= 0.603 \pm 0.020$ (LR) and $0.599 \pm 0.026$ (LightGBM)---weak predictive power. Web-overlap labels contributed negligibly (SHAP $< 0.015$), independently confirming the DIF--contamination orthogonality reported in \Cref{sec:groundtruth}. These results indicate that temporal DIF reflects emergent cohort--item interactions rather than fixed item defects, motivating post-hoc monitoring over pre-screening.
272	
273	\section{Within-Family Similarity by Family Size}
274	\label{app:icc_family}
275	
276	Within-family similarity (mean pairwise Pearson $r$ over 12{,}508-item response vectors) shows no dependence on family size (Spearman $\rho = -0.009$, $p = 0.96$; 30 families with $\geq 2$ members, 1{,}884 models). Large families (Mistral, $m = 547$, $\bar{r} = 0.47$; Llama-3, $m = 315$, $\bar{r} = 0.53$) are no more homogeneous than small or mid-sized families. Of the 5{,}227 models, 3{,}343 lack family assignments; these are retained in DIF analysis but excluded from similarity estimation. Within the temporal DIF cohorts ($N_{\mathrm{ref}} + N_{\mathrm{foc}} = 1{,}887$), 1{,}884 (99.8\%) belong to identified families with $\geq 2$ members, so DEFF estimates are computed over nearly the full cohort. This indicates that the weighted-mean DEFF variant's effective cluster size ($\bar{m} = 254$) reflects an arithmetic artifact of mega-family dominance rather than genuine within-family homogeneity.
277	
2
…[truncated 785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 271 · 2026-05-23T19:26:25.085206+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "22|enrichment|times.*random|×.*random",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "22|enrichment|times.*random|×.*random",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-23T19:26:25.085350+00:00_

4:We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
48:[Omitted long matching line]
90:[Omitted long matching line]
100:\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts; $\rho$/$\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\%/Rand.\ C\%, with baseline varying by benchmark. All six show substantial DIF (45--95$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
113:HellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\times$ \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 273 · 2026-05-23T19:26:25.085481+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "geq.*22|22.*times|22.*baseline",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "tool_args": {
    "pattern": "geq.*22|22.*times|22.*baseline",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 274 · 2026-05-23T19:26:25.085607+00:00_

paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/experiments.tex:4:We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
paper/sections/experiments.tex:113:HellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\times$ \\
paper/sections/appendix.tex:166:\noindent Mean ICC $= 0.047$ (median $0.041$, Q3 $= 0.061$, max $= 0.219$; 4.8\% of items exceed $0.10$). After dividing each item's $\chi^2_{\mathrm{MH}}$ by its item-specific DEFF and re-applying ETS thresholds, 13.5--29.2\% of items retain Category~C classification depending on the $\bar{m}$ variant---both far exceeding the 0.62\% random-split baseline (22--47$\times$).
paper/sections/appendix.tex:213:[Omitted long matching line]
paper/sections/appendix.tex:276:[Omitted long matching line]
paper/sections/method.tex:30:[Omitted long matching line]
paper/sections/introduction.tex:16:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 275 · 2026-05-23T19:26:25.085810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
  "offset": "95",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex",
    "offset": "95",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 276 · 2026-05-23T19:26:25.085979+00:00_

95	\looseness=-2
96	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}): C\% ranges from 17.9\% (HellaSwag~\citep{zellers2019hellaswag}) to 31.3\% (MMLU), with knowledge/reasoning benchmarks consistently higher than procedural ones (C\% $= 26.9$--$31.3\%$ vs.\ $17.9$--$18.9\%$). These differences may partly reflect item difficulty distributions; we treat them as descriptive.
97	
98	\begin{table}[t]
99	\centering
100	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts; $\rho$/$\tau$ = Spearman/Kendall correlation between full and stable-item rankings; Flip = pairwise rank-flip rate; Ratio = C\%/Rand.\ C\%, with baseline varying by benchmark. All six show substantial DIF (45--95$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
101	\label{tab:cross_benchmark}
102	\small
103	\resizebox{\columnwidth}{!}{%
104	\begin{tabular}{lrrrrrrl}
105	\toprule
106	Benchmark & Items & C\% & $\rho$ & $\tau$ & Flip\% & Rand.\ C\% & Ratio \\
107	\midrule
108	MMLU & 12{,}508 & 31.3 & 0.9965 & 0.9600 & 2.00 & 0.62 & 50$\times$ \\
109	WinoGrande & 1{,}267 & 30.3 & 0.9943 & 0.9432 & 2.84 & 0.32 & 95$\times$ \\
110	TruthfulQA & 817 & 29.7 & 0.9971 & 0.9586 & 2.07 & 0.37 & 80$\times$ \\
111	ARC & 1{,}172 & 26.9 & 0.9962 & 0.9538 & 2.31 & 0.60 & 45$\times$ \\
112	GSM8K & 1{,}319 & 18.9 & 0.9993 & 0.9843 & 0.78 & 0.30 & 63$\times$ \\
113	HellaSwag & 10{,}042 & 17.9 & 0.9986 & 0.9722 & 1.39 & 0.28 & 64$\times$ \\
114	\bottomrule
115	\end{tabular}}
116	\end{table}
117	
118	Semi-synthetic injection on GSM8K confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$; \Cref{app:gsm8k_details,app:fig_gsm1k}).
119	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 277 · 2026-05-23T19:26:25.086187+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part1.md",
  "content": "# Data Audit — Abstract / Introduction / Conclusion / Limitations\n\n## Abstract 数字核查\n\n- **17.9--31.3%** (temporal C% range) ← `plan_028_multi_bench_dif/multi_bench_dif_report.md` Table: HellaSwag 17.9%, MMLU 31.3% ✅\n- **5,227 models** ← `metabench_data_summary.md` line 8: \"Models (CSV) | 5,227\" ✅\n- **29.2%** (MMLU after non-independence correction) ← `mf2_deff_estimation/deff_summary.md` line 65: \"C items | 3918 (31.3%) | 3649 (29.2%)\" (simple-mean DEFF=3.87) ✅\n- **[26.7%, 53.2%]** (cluster bootstrap 95% CI) ← `sf1_cluster_bootstrap/cluster_bootstrap_ci.md` line 16: [26.73%, 53.17%] ✅\n- **≥22×** (random baseline) ← `appendix.tex` line 166 states \"22--47×\"; derived from DEFF-corrected 13.5%/0.62% = 21.8×, rounded to 22× ⚠️ 精确值 21.8×，向上取整为 ≥22×，可接受但严格来说 21.8 < 22\n- **Jaccard = 0.206** ← `r17_jaccard_permutation/jaccard_permutation_report.md` line 15: Observed Jaccard = 0.2063 ✅\n- **φ = 0.012** ← `plan_026/constat_dif_comparison_report.md` line 23: Phi coefficient = 0.0120 ✅\n- **ρ ≈ 0.997** ← `mf2_practical_significance/mf2_report.md` line 16: Mean Spearman ρ = 0.9970 ✅\n- **χ² = 562.7** ← `r18_base_vs_instruct_dif/base_instruct_dif_report.md` line 49: χ² = 562.70 ✅\n- **+2.12 pp** ← `score_inflation_analysis/score_inflation_report.md` line 88: \"+2.12 pp overall\" ✅\n\n## Introduction 数字核查\n\n- **31%** (MMLU C classification) ← `plan_028_multi_bench_dif/multi_bench_dif_report.md`: MMLU C% = 31.3%, 论文写 \"31%\" ✅ (合理取整)\n- **|Δ_MH| ≥ 1.5, p < 0.05** ← ETS classification thresholds (方法论常量) ✅\n- **0.62%** (random-split control) ← `r16_threshold_calibration/random_split_report.md` line 31: Mean null C% = 0.6247% ✅\n- **ρ ≈ 0.997** ← 同 Abstract ✅\n- **+2.12 pp** ← 同 Abstract ✅\n- **849 rank positions** ← `plan_032_dif_cleaned_mmlu/plan_032_report.md` line 41 & `score_inflation_analysis/score_inflation_report.md` line 61: max rank displacement = 849 ✅\n- **5,227 models × 12,508 MMLU items** ← `metabench_data_summary.md` ✅\n- **29.2%** ← 同 Abstract ✅\n- **17.9--31.3%** ← 同 Abstract ✅\n- **[26.7%, 53.2%]** ← 同 Abstract ✅\n- **Jaccard = 0.206** ← 同 Abstract ✅\n- **χ² = 562.7** ← 同 Abstract ✅\n- **ΔFPR = 0 guarantee** (k ≤ 5) ← `plan_034_multi_subject_injection/plan_034_report.md` lines 50-51: k ≤ 5 时 |ΔFPR| < 0.007 ✅\n- **enrichment ratio ≈ 1.0** ← `plan_026/constat_dif_comparison_report.md` line 33: enrichment ratio = 0.9642 ✅\n\n## Conclusion 数字核查\n\n- **17.9--31.3%** ← 同 Abstract ✅\n- **29.2%** ← 同 Abstract ✅\n- **ρ ≈ 0.997** ← 同 Abstract ✅\n- **Jaccard = 0.206** ← 同 Abstract ✅\n- **χ² = 562.7** ← 同 Abstract ✅\n\n## Limitations 数字核查\n\n- **13.5--29.2%** (DEFF estimators) ← `mf2_deff_estimation/deff_summary.md` lines 55, 65: weighted-mean DEFF → 13.5%, simple-mean DEFF → 29.2% ✅\n- **[26.7%, 53.2%]** (cluster bootstrap CI) ← 同 Abstract ✅\n- **ΔFPR = 0.167** ← `plan_034_multi_subject_injection/summary_by_k_full.csv` line 19: k=20, p=0.5 → mean_delta_fpr = 0.1673 ✅\n- **≥20 subjects** ← `plan_034_multi_subject_injection/plan_034_report.md` line 58: k=20 对应 ΔFPR = +0.167 ✅\n- **Δ = 1.08 pp** (composition control) ← `r22_composition_control/composition_control_report.md` line 26: Δ(original − balanced) = 1.08 pp ✅\n- **57 subjects** ← `plan_034_multi_subject_injection/plan_034_report.md` line 9: \"57 MMLU subjects\" ✅\n\n## 跨章节一致性\n\n| 数字 | Abstract | Introduction | Conclusion | Limitations | 一致性 |\n|------|----------|-------------|------------|-------------|--------|\n| 17.9--31.3% | ✓ | ✓ | ✓ | — | 一致 |\n| 29.2% | ✓ | ✓ | ✓ | ✓ (范围上界) | 一致 |\n| ρ ≈ 0.997 | ✓ | ✓ | ✓ | — | 一致 |\n| Jaccard = 0.206 | ✓ | ✓ | ✓ | — | 一致 |\n| χ² = 562.7 | ✓ | ✓ | ✓ | — | 一致 |\n| +2.12 pp | ✓ | ✓ | — | — | 一致 |\n| 849 positions | — | ✓ | — | — | 仅出现一次 |\n| [26.7%, 53.2%] | ✓ | ✓ | — | ✓ | 一致 |\n| ≥22× | ✓ | — | — | — | 仅出现一次 |\n| 13.5% | — | — | — | ✓ | 仅出现一次 |\n\n**跨章节一致性结论**：所有在多个章节重复出现的数字完全一致，无矛盾。\n\n## 总结\n\n- ✅ 已确认：29 个数字/声明\n- ⚠️ 需注意：1 个（≥22× 精确值为 21.8×，取整方向偏乐观）\n- ❌ 无法追溯：0 个\n\n唯一的潜在问题：Abstract 中 \"≥22×\" 来源于 appendix 的 DEFF 修正后下界 13.5% 除以随机基线 0.62%，精确值为 21.8×。写为 \"≥22×\" 技术上意味着\"至少 22 倍\"，但真实值略低于 22。实际影响极小，但严谨起见可考虑改为 \"≥21×\" 或 \"${\\sim}22\\times$\"。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part1.md",
    "content": "# Data Audit — Abstract / Introduction / Conclusion / Limitations\n\n## Abstract 数字核查\n\n- **17.9--31.3%** (temporal C% range) ← `plan_028_multi_bench_dif/multi_bench_dif_report.md` Table: HellaSwag 17.9%, MMLU 31.3% ✅\n- **5,227 models** ← `metabench_data_summary.md` line 8: \"Models (CSV) | 5,227\" ✅\n- **29.2%** (MMLU after non-independence correction) ← `mf2_deff_estimation/deff_summary.md` line 65: \"C items | 3918 (31.3%) | 3649 (29.2%)\" (simple-mean DEFF=3.87) ✅\n- **[26.7%, 53.2%]** (cluster bootstrap 95% CI) ← `sf1_cluster_bootstrap/cluster_bootstrap_ci.md` line 16: [26.73%, 53.17%] ✅\n- **≥22×** (random baseline) ← `appendix.tex` line 166 states \"22--47×\"; derived from DEFF-corrected 13.5%/0.62% = 21.8×, rounded to 22× ⚠️ 精确值 21.8×，向上取整为 ≥22×，可接受但严格来说 21.8 < 22\n- **Jaccard = 0.206** ← `r17_jaccard_permutation/jaccard_permutation_report.md` line 15: Observed Jaccard = 0.2063 ✅\n- **φ = 0.012** ← `plan_026/constat_dif_comparison_report.md` line 23: Phi coefficient = 0.0120 ✅\n- **ρ ≈ 0.997** ← `mf2_practical_significance/mf2_report.md` line 16: Mean Spearman ρ = 0.9970 ✅\n- **χ² = 562.7** ← `r18_base_vs_instruct_dif/base_instruct_dif_report.md` line 49: χ² = 562.70 ✅\n- **+2.12 pp** ← `score_inflation_analysis/score_inflation_report.md` line 88: \"+2.12 pp overall\" ✅\n\n## Introduction 数字核查\n\n- **31%** (MMLU C classification) ← `plan_028_multi_bench_dif/multi_bench_dif_report.md`: MMLU C% = 31.3%, 论文写 \"31%\" ✅ (合理取整)\n- **|Δ_MH| ≥ 1.5, p < 0.05** ← ETS classification thresholds (方法论常量) ✅\n- **0.62%** (random-split control) ← `r16_threshold_calibration/random_split_report.md` line 31: Mean null C% = 0.6247% ✅\n- **ρ ≈ 0.997** ← 同 Abstract ✅\n- **+2.12 pp** ← 同 Abstract ✅\n- **849 rank positions** ← `plan_032_dif_cleaned_mmlu/plan_032_report.md` line 41 & `score_inflation_analysis/score_inflation_report.md` line 61: max rank displacement = 849 ✅\n- **5,227 models × 12,508 MMLU items** ← `metabench_data_summary.md` ✅\n- **29.2%** ← 同 Abstract ✅\n- **17.9--31.3%** ← 同 Abstract ✅\n- **[26.7%, 53.2%]** ← 同 Abstract ✅\n- **Jaccard = 0.206** ← 同 Abstract ✅\n- **χ² = 562.7** ← 同 Abstract ✅\n- **ΔFPR = 0 guarantee** (k ≤ 5) ← `plan_034_multi_subject_injection/plan_034_report.md` lines 50-51: k ≤ 5 时 |ΔFPR| < 0.007 ✅\n- **enrichment ratio ≈ 1.0** ← `plan_026/constat_dif_comparison_report.md` line 33: enrichment ratio = 0.9642 ✅\n\n## Conclusion 数字核查\n\n- **17.9--31.3%** ← 同 Abstract ✅\n- **29.2%** ← 同 Abstract ✅\n- **ρ ≈ 0.997** ← 同 Abstract ✅\n- **Jaccard = 0.206** ← 同 Abstract ✅\n- **χ² = 562.7** ← 同 Abstract ✅\n\n## Limitations 数字核查\n\n- **13.5--29.2%** (DEFF estimators) ← `mf2_deff_estimation/deff_summary.md` lines 55, 65: weighted-mean DEFF → 13.5%, simple-mean DEFF → 29.2% ✅\n- **[26.7%, 53.2%]** (cluster bootstrap CI) ← 同 Abstract ✅\n- **ΔFPR = 0.167** ← `plan_034_multi_subject_injection/summary_by_k_full.csv` line 19: k=20, p=0.5 → mean_delta_fpr = 0.1673 ✅\n- **≥20 subjects** ← `plan_034_multi_subject_injection/plan_034_report.md` line 58: k=20 对应 ΔFPR = +0.167 ✅\n- **Δ = 1.08 pp** (composition control) ← `r22_composition_control/composition_control_report.md` line 26: Δ(original − balanced) = 1.08 pp ✅\n- **57 subjects** ← `plan_034_multi_subject_injection/plan_034_report.md` line 9: \"57 MMLU subjects\" ✅\n\n## 跨章节一致性\n\n| 数字 | Abstract | Introduction | Conclusion | Limitations | 一致性 |\n|------|----------|-------------|------------|-------------|--------|\n| 17.9--31.3% | ✓ | ✓ | ✓ | — | 一致 |\n| 29.2% | ✓ | ✓ | ✓ | ✓ (范围上界) | 一致 |\n| ρ ≈ 0.997 | ✓ | ✓ | ✓ | — | 一致 |\n| Jaccard = 0.206 | ✓ | ✓ | ✓ | — | 一致 |\n| χ² = 562.7 | ✓ | ✓ | ✓ | — | 一致 |\n| +2.12 pp | ✓ | ✓ | — | — | 一致 |\n| 849 positions | — | ✓ | — | — | 仅出现一次 |\n| [26.7%, 53.2%] | ✓ | ✓ | — | ✓ | 一致 |\n| ≥22× | ✓ | — | — | — | 仅出现一次 |\n| 13.5% | — | — | — | ✓ | 仅出现一次 |\n\n**跨章节一致性结论**：所有在多个章节重复出现的数字完全一致，无矛盾。\n\n## 总结\n\n- ✅ 已确认：29 个数字/声明\n- ⚠️ 需注意：1 个（≥22× 精确值为 21.8×，取整方向偏乐观）\n- ❌ 无法追溯：0 个\n\n唯一的潜在问题：Abstract 中 \"≥22×\" 来源于 appendix 的 DEFF 修正后下界 13.5% 除以随机基线 0.62%，精确值为 21.8×。写为 \"≥22×\" 技术上意味着\"至少 22 倍\"，但真实值略低于 22。实际影响极小，但严谨起见可考虑改为 \"≥21×\" 或 \"${\\sim}22\\times$\"。\n"
  }
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-23T19:26:25.086379+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/data_audit_part1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 279 · 2026-05-23T19:26:25.086543+00:00_

报告已写入 `artifacts/data_audit_part1.md`。

核查结果：29 个数字全部追溯到 artifacts 源文件，跨章节完全一致。唯一的 ⚠️ 是 Abstract 中 "≥22×" — 精确值为 13.5%/0.62% = 21.8×，写 "≥22×" 略有向上取整（21.8 < 22）。如需严谨可改为 `${\sim}22\times$` 或 `${\geq}21\times$`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_data_audit_abstract_intro_20260523T191605"
}
```

</details>

---
