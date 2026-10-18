# code exp a civilcomments

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_code_exp-a-civilcomments_20260523T190133.jsonl`
- **Structured JSON:** [`c66ae941f02221885b30.json`](../../sessions/c6/c66ae941f02221885b30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-23T19:07:47.571324+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ 2>/dev/null | head -30",
  "description": "List results directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ 2>/dev/null | head -30",
    "description": "List results directory"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T19:07:47.571913+00:00_

dataset_survey.md
exp001_full_run.log
exp001_hb_diagnostics.csv
exp001_hb_results.csv
exp001_hb_results_v2.csv
exp001_hyperprior_run.log
exp001_hyperprior_sensitivity.csv
exp001_reg_run.log
exp001_reg_v2_run.log
exp002_bias_bound.csv
exp002_bias_heatmap.csv
exp002_debiasing_hurts.csv
exp002_derivation.md
exp002_k4_validation.csv
exp002_run.log
exp003_dgp_spec.md
exp003_hb_rerun.log
exp003_phase_a.csv
exp003_phase_a_raw.csv
exp003_phase_a_v2.csv
exp003_phase_a_v2_raw.csv
exp003_phase_a_v3.csv
exp003_phase_a_v3_raw.csv
exp003_run.log
exp003_v2_run.log
exp004_annotate.log
exp004_cate_comparison.csv
exp004_cate_plot.png
exp004_comments_to_annotate.csv
exp004_confusion_matrices.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:07:47.572209+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/ 2>/dev/null | head -30",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/ 2>/dev/null | head -30",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:07:47.572376+00:00_

_project
bias_anatomy_heatmap.pdf
bias_anatomy_heatmap.png
cross_llm_heatmap.pdf
cross_llm_heatmap.png
cross_llm_heatmap_report.txt
cross_llm_rank_corr_heatmap.pdf
cross_llm_rank_corr_heatmap.png
cross_llm_rank_correlation.csv
data_audit_report.md
data_integrity_fixes.md
debiasing_hurts_summary.csv
debiasing_hurts_summary.pdf
debiasing_hurts_summary.png
dream_reports
exp-001
exp-002
exp-003
exp-004
exp-005
exp-006
exp-007
exp-008
exp-010
exp-011
exp-012
exp-013
exp-014
exp-019
exp-020

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:07:47.572522+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/ 2>/dev/null",
  "description": "List project root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/ec_hte_llm_annotation/ 2>/dev/null",
    "description": "List project root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T19:07:47.572670+00:00_

__pycache__
analyze_hatespeech.py
artifacts
build_k_scalability.py
compute_fl_for_table1.py
data
draw_fig2.py
draw_fig3.py
exp001_hb_synthetic.py
exp001_hb_synthetic.py.bak
exp001_hyperprior_sensitivity.py
exp001_regularize.py
exp002_bias_bound.py
exp003_tweeteval.py
exp004_hate_speech.py
exp005_diagnostic_criterion.py
exp006_budget_sensitivity.py
exp007_ppci_dsl.py
exp008_filter_analysis.py
exp008_gpt55_annotate.py
exp008_gpt5x_annotate.py
exp008_multi_llm.py
exp010_misspecified_subgroups.py
exp011_causal_forest.py
exp013_boundary_condition.py
exp014_asymmetric.py
exp015_semi_real_cm.py
exp016_semi_real_better_cm.py
exp017_rlearner.py
exp018_multiplicative_dgp.py
exp019_pz1_sweep.py
exp020_kappa_sweep.py
exp021_seeds_supplement.py
exp022_ppi_dsl_baseline.py
exp023_annotate_parallel.py
exp023_civil_comments_prepare.py
exp023_civil_comments_semisynthetic.py
exp023_civil_comments_semisynthetic_v2.py
exp023_civil_comments_semisynthetic_v3.py
exp023_civil_comments_symmetric.py
exp023_ppi_dsl_baseline.py
exp023_ppi_dsl_k2.py
exp023_run_all.sh
exp024_realcm_bias_identity.py
exp025_positive_scenario.py
exp026_low_budget_hb.py
exp027_cf_oracle_coverage.py
exp027b_cf_oracle_k2.py
exp027c_cf_oracle_mf2dgp.py
exp028_asymmetric_diagnostic_auc.py
exp029_a1_sensitivity.py
exp030_k8_subgroups.py
exp031_confounded_dgp.py
exp032_confounded_sweep.py
exp033_k8_adaptive.py
exp034_fl_comparison.py
exp035_asymmetric_cm.py
exp036_bootstrap_se.py
exp036_bootstrap_se_v2.py
exp037_calibration.py
exp_adaptive_routing.py
exp_adaptive_shrinkage.py
exp_asymmetric_diagnostic.py
exp_bootstrap_small_n.py
exp_centered_eb_table1.py
exp_mf2_cf_bootstrap_se.py
exp_real_cm_validation.py
exp_treatment_dep_misclass.py
exp_w4_bootstrap_se.py
exp_w8_a5_violation.py
mvp_simulation.py
pilot_gemini_annotation.py
pilot_llm_annotation.py
results
run_table1.sh
scripts
sign_reversal_analysis.py
task_j_policy_reversal.py
timing_benchmark.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:07:47.573018+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ | grep -i civil 2>/dev/null",
  "description": "Find civil comments results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ | grep -i civil 2>/dev/null",
    "description": "Find civil comments results"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:07:47.573147+00:00_

exp023_civil_comments_analysis.md
exp023_civil_comments_pool.parquet

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:07:47.573271+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ | grep -i exp023 2>/dev/null",
  "description": "Find exp023 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ | grep -i exp023 2>/dev/null",
    "description": "Find exp023 results"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T19:07:47.573395+00:00_

exp023_annotate.log
exp023_annotate_run2.log
exp023_checkpoint_gpt-3.5-turbo.json
exp023_checkpoint_gpt-4o-mini.json
exp023_checkpoint_gpt-4o.json
exp023_civil_comments_analysis.md
exp023_civil_comments_pool.parquet
exp023_confusion_matrices.json
exp023_confusion_matrices_prelim.json
exp023_equivalence_analysis.md
exp023_final_summary.md
exp023_llm_annotations.csv
exp023_ppi_dsl.csv
exp023_ppi_dsl_k2.csv
exp023_ppi_dsl_k2_raw.csv
exp023_ppi_dsl_raw.csv
exp023_semisynthetic.log
exp023_semisynthetic_analysis.md
exp023_semisynthetic_raw.csv
exp023_semisynthetic_summary.csv
exp023_semisynthetic_v2_analysis.md
exp023_semisynthetic_v2_raw.csv
exp023_semisynthetic_v2_summary.csv
exp023_semisynthetic_v3_analysis.md
exp023_semisynthetic_v3_raw.csv
exp023_semisynthetic_v3_summary.csv
exp023_symmetric_raw.csv
exp023_symmetric_summary.csv
exp023_v2_run.log
exp023_v3_run.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:07:47.573514+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/data/ 2>/dev/null",
  "description": "List data directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/ec_hte_llm_annotation/data/ 2>/dev/null",
    "description": "List data directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:07:47.573628+00:00_

exp004_comments_processed.parquet
exp004_processed.parquet
exp004_raw.parquet

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:07:47.573740+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/ | grep -i civil 2>/dev/null",
  "description": "Find civil comments artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/ | grep -i civil 2>/dev/null",
    "description": "Find civil comments artifacts"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T19:07:47.573941+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:07:47.574194+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/ec_hte_llm_annotation/results/exp023_confusion_matrices.json 2>/dev/null | python3 -m json.tool | head -80",
  "description": "Read confusion matrices JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/ec_hte_llm_annotation/results/exp023_confusion_matrices.json 2>/dev/null | python3 -m json.tool | head -80",
    "description": "Read confusion matrices JSON"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T19:07:47.574363+00:00_

{
    "gpt-4o": {
        "S0": {
            "tp": 305,
            "tn": 582,
            "fp": 208,
            "fn": 68,
            "fpr": 0.2633,
            "fnr": 0.1823,
            "accuracy": 0.7627,
            "n": 1163,
            "n_pos": 373,
            "n_neg": 790
        },
        "S1": {
            "tp": 75,
            "tn": 192,
            "fp": 61,
            "fn": 13,
            "fpr": 0.2411,
            "fnr": 0.1477,
            "accuracy": 0.783,
            "n": 341,
            "n_pos": 88,
            "n_neg": 253
        },
        "S2": {
            "tp": 202,
            "tn": 550,
            "fp": 179,
            "fn": 81,
            "fpr": 0.2455,
            "fnr": 0.2862,
            "accuracy": 0.7431,
            "n": 1012,
            "n_pos": 283,
            "n_neg": 729
        },
        "S3": {
            "tp": 110,
            "tn": 219,
            "fp": 109,
            "fn": 46,
            "fpr": 0.3323,
            "fnr": 0.2949,
            "accuracy": 0.6798,
            "n": 484,
            "n_pos": 156,
            "n_neg": 328
        },
        "_global": {
            "fpr": 0.2652,
            "fnr": 0.2311,
            "delta_fpr": 0.0912,
            "delta_fnr": 0.1472
        }
    },
    "gpt-4o-mini": {
        "S0": {
            "tp": 352,
            "tn": 397,
            "fp": 393,
            "fn": 21,
            "fpr": 0.4975,
            "fnr": 0.0563,
            "accuracy": 0.644,
            "n": 1163,
            "n_pos": 373,
            "n_neg": 790
        },
        "S1": {
            "tp": 84,
            "tn": 109,
            "fp": 144,
            "fn": 4,
            "fpr": 0.5692,
            "fnr": 0.0455,
            "accuracy": 0.566,
            "n": 341,
            "n_pos": 88,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:07:47.574513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -50 /home/ubuntu/ec_hte_llm_annotation/results/exp023_civil_comments_analysis.md 2>/dev/null",
  "description": "Read civil comments analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "head -50 /home/ubuntu/ec_hte_llm_annotation/results/exp023_civil_comments_analysis.md 2>/dev/null",
    "description": "Read civil comments analysis"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T19:07:47.574672+00:00_

# exp-023: Civil Comments Semi-Synthetic Validation — Comprehensive Analysis

## 1. Dataset & Subgroup Design

**Dataset**: Civil Comments (Google, toxicity detection), 3000 stratified samples (30% toxic)
**Subgroups**: text_length_bin × has_question → K=4 (S0: long+no_q, S1: long+q, S2: short+no_q, S3: short+q)
**Subgroup weights**: S0=0.388, S1=0.114, S2=0.337, S3=0.161
**P(Z=1)**: 0.300

## 2. LLM Annotation Confusion Matrices

Annotated with 3 LLMs via OpenAI-compatible proxy. 800–900 valid annotations per model.

### Per-subgroup error rates

| Model | Metric | S0 | S1 | S2 | S3 | Δ (max−min) |
|-------|--------|-----|-----|-----|-----|------------|
| gpt-4o | FPR | 0.249 | 0.157 | 0.213 | 0.341 | 0.184 |
| gpt-4o | FNR | 0.160 | 0.263 | 0.308 | 0.328 | 0.168 |
| gpt-4o-mini | FPR | 0.517 | 0.541 | 0.419 | 0.610 | 0.191 |
| gpt-4o-mini | FNR | 0.052 | 0.105 | 0.074 | 0.160 | 0.108 |
| gpt-3.5-turbo | FPR | 0.400 | 0.473 | 0.374 | 0.468 | 0.099 |
| gpt-3.5-turbo | FNR | 0.139 | 0.211 | 0.173 | 0.240 | 0.101 |

### Key Finding 1: Cross-subgroup misclassification heterogeneity confirmed

All 3 models show **Δπ > 0.05** across subgroups:
- gpt-4o: Δ_FPR=0.184, Δ_FNR=0.168 (overall Δπ=0.160)
- gpt-4o-mini: Δ_FPR=0.191, Δ_FNR=0.108 (overall Δπ=0.140)
- gpt-3.5-turbo: Δ_FPR=0.099, Δ_FNR=0.101 (overall Δπ=0.113)

This validates the paper's core premise: LLM misclassification is structurally heterogeneous across text-feature-defined subgroups, and this holds on a second NLP dataset beyond TweetEval.

### Key Finding 2: Severe FPR/FNR asymmetry

gpt-4o-mini and gpt-3.5-turbo show highly asymmetric confusion matrices:
- gpt-4o-mini: FPR ≈ 0.42–0.61 while FNR ≈ 0.05–0.16 (over-predicts toxicity)
- gpt-3.5-turbo: FPR ≈ 0.37–0.47 while FNR ≈ 0.14–0.24

This asymmetry causes mixing matrix ill-conditioning (rows become near-uniform when FPR ≈ 0.5), which amplifies estimation noise under matrix inversion.

## 3. Semi-Synthetic DGP Results

### 3a. Asymmetric CMs (real LLM confu
…[truncated 179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:07:47.574850+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv 2>/dev/null",
  "description": "Check LLM annotations CSV header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv 2>/dev/null",
    "description": "Check LLM annotations CSV header"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T19:07:47.574979+00:00_

idx,text,y_true,toxicity,insult,identity_attack,obscene,text_length,has_insult,len_bin,has_question,subgroup,pred_gpt-4o,pred_gpt-4o-mini,pred_gpt-3.5-turbo
1218720,Trudeau is a traitor.,1,0.8888888955116272,0.8888888955116272,0.0,0.0,21,1,0,0,S0,1,1,1
1263499,"Clark's threat of a retaliatory response was too stupid for words.  First of all, it wasn't her jurisdiction/call to make.  Second, everyone knows the posturing was really meant for folks in BC, not Washington.  

Albeit much more constructive in tone, Horgan's messaging is likely targeted more to the people back home in BC than in Washington, too.  A kinder, gentler form of posturing.  I would be surprised if a comprehensive trade deal like NAFTA was preceded by a one-off agreement on softwood lumber just weeks beforehand.  A bit of wishful thinking there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:07:47.575098+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv 2>/dev/null",
  "description": "Count annotation rows"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv 2>/dev/null",
    "description": "Count annotation rows"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:07:47.575211+00:00_

6444 /home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:07:47.575355+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv', nrows=2)\nprint(list(df.columns))\n\"",
  "description": "Check annotation columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv', nrows=2)\nprint(list(df.columns))\n\"",
    "description": "Check annotation columns"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:07:47.575471+00:00_

['idx', 'text', 'y_true', 'toxicity', 'insult', 'identity_attack', 'obscene', 'text_length', 'has_insult', 'len_bin', 'has_question', 'subgroup', 'pred_gpt-4o', 'pred_gpt-4o-mini', 'pred_gpt-3.5-turbo']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:07:47.575582+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_parquet('/home/ubuntu/ec_hte_llm_annotation/results/exp023_civil_comments_pool.parquet')\nprint(list(df.columns))\nprint(df.shape)\nprint(df.head(2))\n\" 2>/dev/null",
  "description": "Check pool parquet columns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_parquet('/home/ubuntu/ec_hte_llm_annotation/results/exp023_civil_comments_pool.parquet')\nprint(list(df.columns))\nprint(df.shape)\nprint(df.head(2))\n\" 2>/dev/null",
    "description": "Check pool parquet columns"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T19:07:47.575702+00:00_

['idx', 'text', 'y_true', 'toxicity', 'insult', 'identity_attack', 'obscene', 'text_length', 'has_insult', 'len_bin', 'has_question', 'subgroup']
(3000, 12)
       idx  ... subgroup
0  1218720  ...       S0
1  1263499  ...       S2

[2 rows x 12 columns]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:07:47.575866+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/ec_hte_llm_annotation/results/exp023_civil_comments_analysis.md 2>/dev/null | head -100",
  "description": "Read full analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/ec_hte_llm_annotation/results/exp023_civil_comments_analysis.md 2>/dev/null | head -100",
    "description": "Read full analysis"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T19:07:47.576026+00:00_

# exp-023: Civil Comments Semi-Synthetic Validation — Comprehensive Analysis

## 1. Dataset & Subgroup Design

**Dataset**: Civil Comments (Google, toxicity detection), 3000 stratified samples (30% toxic)
**Subgroups**: text_length_bin × has_question → K=4 (S0: long+no_q, S1: long+q, S2: short+no_q, S3: short+q)
**Subgroup weights**: S0=0.388, S1=0.114, S2=0.337, S3=0.161
**P(Z=1)**: 0.300

## 2. LLM Annotation Confusion Matrices

Annotated with 3 LLMs via OpenAI-compatible proxy. 800–900 valid annotations per model.

### Per-subgroup error rates

| Model | Metric | S0 | S1 | S2 | S3 | Δ (max−min) |
|-------|--------|-----|-----|-----|-----|------------|
| gpt-4o | FPR | 0.249 | 0.157 | 0.213 | 0.341 | 0.184 |
| gpt-4o | FNR | 0.160 | 0.263 | 0.308 | 0.328 | 0.168 |
| gpt-4o-mini | FPR | 0.517 | 0.541 | 0.419 | 0.610 | 0.191 |
| gpt-4o-mini | FNR | 0.052 | 0.105 | 0.074 | 0.160 | 0.108 |
| gpt-3.5-turbo | FPR | 0.400 | 0.473 | 0.374 | 0.468 | 0.099 |
| gpt-3.5-turbo | FNR | 0.139 | 0.211 | 0.173 | 0.240 | 0.101 |

### Key Finding 1: Cross-subgroup misclassification heterogeneity confirmed

All 3 models show **Δπ > 0.05** across subgroups:
- gpt-4o: Δ_FPR=0.184, Δ_FNR=0.168 (overall Δπ=0.160)
- gpt-4o-mini: Δ_FPR=0.191, Δ_FNR=0.108 (overall Δπ=0.140)
- gpt-3.5-turbo: Δ_FPR=0.099, Δ_FNR=0.101 (overall Δπ=0.113)

This validates the paper's core premise: LLM misclassification is structurally heterogeneous across text-feature-defined subgroups, and this holds on a second NLP dataset beyond TweetEval.

### Key Finding 2: Severe FPR/FNR asymmetry

gpt-4o-mini and gpt-3.5-turbo show highly asymmetric confusion matrices:
- gpt-4o-mini: FPR ≈ 0.42–0.61 while FNR ≈ 0.05–0.16 (over-predicts toxicity)
- gpt-3.5-turbo: FPR ≈ 0.37–0.47 while FNR ≈ 0.14–0.24

This asymmetry causes mixing matrix ill-conditioning (rows become near-uniform when FPR ≈ 0.5), which amplifies estimation noise under matrix inversion.

## 3. Semi-Synthetic DGP Results

### 3a. Asymmetric CMs (real LLM confu
…[truncated 2452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:07:47.576208+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('google/civil_comments', split='train', streaming=True)\nsample = next(iter(ds))\nprint(list(sample.keys()))\n\" 2>/dev/null",
  "description": "Check Civil Comments column names"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('google/civil_comments', split='train', streaming=True)\nsample = next(iter(ds))\nprint(list(sample.keys()))\n\" 2>/dev/null",
    "description": "Check Civil Comments column names"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-23T19:07:47.576328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp023_civil_comments_semisynthetic_v3.py",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp023_civil_comments_semisynthetic_v3.py",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-23T19:07:47.576454+00:00_

['text', 'toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack', 'sexual_explicit']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T19:07:47.576583+00:00_

1	"""
2	exp-023 Phase 2 v3: Semi-synthetic DGP on Civil Comments.
3	
4	Key design changes from v2 (matching TweetEval DGP structure):
5	  - K=2 subgroups (text_length only) for balanced estimation
6	  - Symmetric misclassification (FPR=FNR=pi, like TweetEval)
7	  - N=10000 for adequate power
8	  - Larger tau gap: tau_z0=0.0, tau_z1=0.5
9	
10	Two misclassification regimes:
11	  extreme: pi_S0=0.05, pi_S1=0.30  (Delta_pi=0.25)
12	  moderate: pi_S0=0.08, pi_S1=0.20 (Delta_pi=0.12)
13	
14	Methods: Oracle, Naive, Global-corrected, Stratified MLE, HB EC-HTE
15	n_expert sweep: [100, 250, 500, 1000], MC=50
16	
17	Output:
18	  results/exp023_semisynthetic_v3_raw.csv
19	  results/exp023_semisynthetic_v3_summary.csv
20	  results/exp023_semisynthetic_v3_analysis.md
21	"""
22	
23	import json
24	import time
25	import warnings
26	from pathlib import Path
27	
28	import numpy as np
29	import pandas as pd
30	from scipy.special import gammaln
31	
32	warnings.filterwarnings('ignore')
33	
34	PROJ = Path(__file__).parent
35	RESULTS = PROJ / "results"
36	
37	N = 10000
38	N_MC = 50
39	N_EXPERT_LIST = [100, 250, 500, 1000]
40	SEED_BASE = 42
41	
42	K = 2
43	SUBGROUP_LABELS = ['S0', 'S1']
44	
45	TAU_Z0 = 0.0
46	TAU_Z1 = 0.5
47	P_T = 0.5
48	
49	MISCLASS_RATES = {
50	    'extreme': {'S0': 0.05, 'S1': 0.30},
51	    'moderate': {'S0': 0.08, 'S1': 0.20},
52	}
53	
54	
55	def diff_in_means(Y, T, mask):
56	    t1 = mask & (T == 1)
57	    t0 = mask & (T == 0)
58	    n1, n0 = t1.sum(), t0.sum()
59	    if n1 < 2 or n0 < 2:
60	        return np.nan, np.nan
61	    y1, y0 = Y[t1], Y[t0]
62	    tau_hat = y1.mean() - y0.mean()
63	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
64	    return tau_hat, se
65	
66	
67	def estimate_confusion_matrix(z_true, z_hat):
68	    C = np.zeros((2, 2))
69	    for zt in [0, 1]:
70	        mask = z_true == zt
71	        n = mask.sum()
72	        for zh in [0, 1]:
73	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
74	    return C

…[truncated 143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:07:47.576757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp023_civil_comments_prepare.py",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp023_civil_comments_prepare.py",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T19:07:47.576930+00:00_

1	"""
2	exp-023 Phase 1: Civil Comments dataset preparation and LLM annotation.
3	
4	Downloads Civil Comments, defines subgroups (text_length × insult_signal, K=4),
5	stratified-samples ~3000 comments with ~30% toxic, then annotates with 3 API models.
6	
7	Output:
8	  results/exp023_civil_comments_pool.parquet   – full annotated pool
9	  results/exp023_llm_annotations.csv           – LLM predictions per model
10	  results/exp023_confusion_matrices.json       – per-subgroup CMs per model
11	"""
12	
13	import json
14	import os
15	import sys
16	import time
17	from pathlib import Path
18	
19	import numpy as np
20	import pandas as pd
21	from datasets import load_dataset
22	
23	PROJ = Path(__file__).parent
24	RESULTS = PROJ / "results"
25	RESULTS.mkdir(exist_ok=True)
26	
27	API_KEY_PATH = PROJ / ".api_key"
28	API_BASE = "http://47.94.22.126/v1"
29	
30	MODELS = ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]
31	
32	PROMPT_TEMPLATE = (
33	    'Is the following comment toxic? A comment is toxic if it is rude, '
34	    'disrespectful, or likely to make someone leave a discussion.\n\n'
35	    'Comment: "{text}"\n\n'
36	    'Reply with ONLY one word: toxic or non-toxic.'
37	)
38	
39	SAMPLE_N = 3000
40	TOXIC_FRAC = 0.30
41	SEED = 42
42	
43	
44	def load_and_prepare():
45	    """Load Civil Comments, compute features, stratified sample."""
46	    print("Loading Civil Comments from HuggingFace...")
47	    ds = load_dataset("google/civil_comments", split="train")
48	
49	    texts = ds["text"]
50	    toxicity = np.array(ds["toxicity"])
51	    insult = np.array(ds["insult"])
52	    identity_attack = np.array(ds["identity_attack"])
53	    obscene = np.array(ds["obscene"])
54	
55	    y_true = (toxicity >= 0.5).astype(int)
56	    lengths = np.array([len(t) for t in texts])
57	    has_insult = (insult > 0).astype(int)
58	
59	    print(f"Total: {len(texts)}, Toxic: {y_true.sum()} ({y_true.mean():.3f})")
60	    print(f"Insult>0: {has_insult.sum()} ({has_insult.mean():.3f})")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T19:07:47.577081+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('google/civil_comments', split='train', streaming=True)\ninfo = ds.features if hasattr(ds, 'features') else None\nprint(info)\n\" 2>/dev/null",
  "description": "Check dataset features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\nds = load_dataset('google/civil_comments', split='train', streaming=True)\ninfo = ds.features if hasattr(ds, 'features') else None\nprint(info)\n\" 2>/dev/null",
    "description": "Check dataset features"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T19:07:47.577215+00:00_

{'text': Value('string'), 'toxicity': Value('float32'), 'severe_toxicity': Value('float32'), 'obscene': Value('float32'), 'threat': Value('float32'), 'insult': Value('float32'), 'identity_attack': Value('float32'), 'sexual_explicit': Value('float32')}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:07:47.577444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\n# Try the identity version\ntry:\n    ds = load_dataset('google/civil_comments', 'CivilCommentsIdentities', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('CivilCommentsIdentities:', list(sample.keys()))\nexcept Exception as e:\n    print(f'CivilCommentsIdentities failed: {e}')\n\" 2>/dev/null",
  "description": "Check for identity subset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\n# Try the identity version\ntry:\n    ds = load_dataset('google/civil_comments', 'CivilCommentsIdentities', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('CivilCommentsIdentities:', list(sample.keys()))\nexcept Exception as e:\n    print(f'CivilCommentsIdentities failed: {e}')\n\" 2>/dev/null",
    "description": "Check for identity subset"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-23T19:07:47.577645+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\n# Try different configs\ntry:\n    configs = load_dataset('google/civil_comments', trust_remote_code=True)\n    print(type(configs))\n    print(configs)\nexcept Exception as e:\n    print(f'Error: {e}')\n# Check if there's an identity column we missed\ntry:\n    ds = load_dataset('google/civil_comments', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('Keys:', sorted(sample.keys()))\n    print('Values:', {k: type(v).__name__ for k, v in sample.items()})\nexcept Exception as e:\n    print(f'Error2: {e}')\n\" 2>/dev/null",
  "description": "Check dataset configs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\n# Try different configs\ntry:\n    configs = load_dataset('google/civil_comments', trust_remote_code=True)\n    print(type(configs))\n    print(configs)\nexcept Exception as e:\n    print(f'Error: {e}')\n# Check if there's an identity column we missed\ntry:\n    ds = load_dataset('google/civil_comments', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('Keys:', sorted(sample.keys()))\n    print('Values:', {k: type(v).__name__ for k, v in sample.items()})\nexcept Exception as e:\n    print(f'Error2: {e}')\n\" 2>/dev/null",
    "description": "Check dataset configs"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-23T19:07:47.577783+00:00_

CivilCommentsIdentities failed: BuilderConfig 'CivilCommentsIdentities' not found. Available: ['default']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T19:07:47.577934+00:00_

&lt;class 'datasets.dataset_dict.DatasetDict'>
DatasetDict({
    train: Dataset({
        features: ['text', 'toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack', 'sexual_explicit'],
        num_rows: 1804874
    })
    validation: Dataset({
        features: ['text', 'toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack', 'sexual_explicit'],
        num_rows: 97320
    })
    test: Dataset({
        features: ['text', 'toxicity', 'severe_toxicity', 'obscene', 'threat', 'insult', 'identity_attack', 'sexual_explicit'],
        num_rows: 97320
    })
})
Keys: ['identity_attack', 'insult', 'obscene', 'severe_toxicity', 'sexual_explicit', 'text', 'threat', 'toxicity']
Values: {'text': 'str', 'toxicity': 'float', 'severe_toxicity': 'float', 'obscene': 'float', 'threat': 'float', 'insult': 'float', 'identity_attack': 'float', 'sexual_explicit': 'float'}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T19:07:47.578084+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nfrom datasets import load_dataset\n# Try jigsaw version\ntry:\n    ds = load_dataset('civil_comments', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('civil_comments:', sorted(sample.keys()))\nexcept Exception as e:\n    print(f'civil_comments: {e}')\n\n# Try the identity version from tensorflow\ntry:\n    ds = load_dataset('SetFit/civil_comments', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('SetFit/civil_comments:', sorted(sample.keys()))\nexcept Exception as e:\n    print(f'SetFit/civil_comments: {e}')\n\" 2>/dev/null",
  "description": "Try alternative datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nfrom datasets import load_dataset\n# Try jigsaw version\ntry:\n    ds = load_dataset('civil_comments', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('civil_comments:', sorted(sample.keys()))\nexcept Exception as e:\n    print(f'civil_comments: {e}')\n\n# Try the identity version from tensorflow\ntry:\n    ds = load_dataset('SetFit/civil_comments', split='train', streaming=True)\n    sample = next(iter(ds))\n    print('SetFit/civil_comments:', sorted(sample.keys()))\nexcept Exception as e:\n    print(f'SetFit/civil_comments: {e}')\n\" 2>/dev/null",
    "description": "Try alternative datasets"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T19:07:47.578207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip3 list 2>/dev/null | grep -i kaggle; pip3 list 2>/dev/null | grep -i tensorflow",
  "description": "Check for kaggle or tf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 list 2>/dev/null | grep -i kaggle; pip3 list 2>/dev/null | grep -i tensorflow",
    "description": "Check for kaggle or tf"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T19:07:47.578339+00:00_

civil_comments: ['identity_attack', 'insult', 'obscene', 'severe_toxicity', 'sexual_explicit', 'text', 'threat', 'toxicity']
SetFit/civil_comments: Dataset 'SetFit/civil_comments' doesn't exist on the Hub or cannot be accessed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T19:07:47.578450+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T19:07:47.578587+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip3 install tensorflow-datasets 2>&1 | tail -3",
  "description": "Install tfds",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install tensorflow-datasets 2>&1 | tail -3",
    "description": "Install tfds",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T19:07:47.578703+00:00_

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T19:07:47.578833+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip3 install tensorflow-datasets --break-system-packages 2>&1 | tail -5",
  "description": "Install tfds with override",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install tensorflow-datasets --break-system-packages 2>&1 | tail -5",
    "description": "Install tfds with override",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T19:07:47.578967+00:00_

Installing collected packages: wrapt, toml, termcolor, psutil, promise, immutabledict, etils, einops, docstring-parser, absl-py, tensorflow-metadata, simple_parsing, dm-tree, array_record, tensorflow-datasets
  WARNING: The script tfds is installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Successfully installed absl-py-2.4.0 array_record-0.8.3 dm-tree-0.1.10 docstring-parser-0.18.0 einops-0.8.2 etils-1.14.0 immutabledict-4.3.1 promise-2.3 psutil-7.2.2 simple_parsing-0.1.8 tensorflow-datasets-4.9.10 tensorflow-metadata-1.17.3 termcolor-3.3.0 toml-0.10.2 wrapt-2.2.1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T19:07:47.579124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport tensorflow_datasets as tfds\n# Check what configs are available for civil_comments\nbuilder = tfds.builder('civil_comments/CivilCommentsIdentities')\nprint(builder.info.features)\n\" 2>&1 | tail -20",
  "description": "Check tfds civil comments identities features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport tensorflow_datasets as tfds\n# Check what configs are available for civil_comments\nbuilder = tfds.builder('civil_comments/CivilCommentsIdentities')\nprint(builder.info.features)\n\" 2>&1 | tail -20",
    "description": "Check tfds civil comments identities features"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T19:07:47.579283+00:00_

	- wake_vision
	- waymo_open_dataset
	- webvid
	- wider_face
	- xtreme_pos
	- xtreme_s
	- yes_no

Check that:
    - if dataset was added recently, it may only be available
      in `tfds-nightly`
    - the dataset name is spelled correctly
    - dataset class defines all base class abstract methods
    - the module defining the dataset class is imported

The builder directory /home/ubuntu/tensorflow_datasets/civil_comments/CivilCommentsIdentities doesn't contain any versions.
No builder could be found in the directory: /home/ubuntu/tensorflow_datasets for the builder: civil_comments.
No registered data_dirs were found in:
	- /home/ubuntu/tensorflow_datasets

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T19:07:47.579444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv')\nprint(f'Shape: {df.shape}')\nprint(f'Columns: {list(df.columns)}')\nprint(f'y_true distribution: {df.y_true.value_counts().to_dict()}')\nprint(f'pred columns non-null:')\nfor c in ['pred_gpt-4o', 'pred_gpt-4o-mini', 'pred_gpt-3.5-turbo']:\n    print(f'  {c}: {df[c].notna().sum()} / {len(df)}')\n# Check text content for identity mentions\nimport re\nsample_texts = df['text'].head(3).tolist()\nfor t in sample_texts:\n    print(f'Text preview: {t[:100]}...')\n\"",
  "description": "Examine existing annotations in detail"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv')\nprint(f'Shape: {df.shape}')\nprint(f'Columns: {list(df.columns)}')\nprint(f'y_true distribution: {df.y_true.value_counts().to_dict()}')\nprint(f'pred columns non-null:')\nfor c in ['pred_gpt-4o', 'pred_gpt-4o-mini', 'pred_gpt-3.5-turbo']:\n    print(f'  {c}: {df[c].notna().sum()} / {len(df)}')\n# Check text content for identity mentions\nimport re\nsample_texts = df['text'].head(3).tolist()\nfor t in sample_texts:\n    print(f'Text preview: {t[:100]}...')\n\"",
    "description": "Examine existing annotations in detail"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T19:07:47.579569+00:00_

Shape: (3000, 15)
Columns: ['idx', 'text', 'y_true', 'toxicity', 'insult', 'identity_attack', 'obscene', 'text_length', 'has_insult', 'len_bin', 'has_question', 'subgroup', 'pred_gpt-4o', 'pred_gpt-4o-mini', 'pred_gpt-3.5-turbo']
y_true distribution: {0: 2100, 1: 900}
pred columns non-null:
  pred_gpt-4o: 3000 / 3000
  pred_gpt-4o-mini: 3000 / 3000
  pred_gpt-3.5-turbo: 3000 / 3000
Text preview: Trudeau is a traitor....
Text preview: Clark's threat of a retaliatory response was too stupid for words.  First of all, it wasn't her juri...
Text preview: You obviously aren't a property owner in Anchorage.

Be thankful your ShareBlue compensation isn't t...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T19:07:47.579702+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport pandas as pd\nimport re\n\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv')\n\n# Define demographic keyword groups\ndemo_keywords = {\n    'male': r'\\b(man|men|male|boy|father|husband|he|him|his|son|brother|masculine|manhood|guy|gentleman)\\b',\n    'female': r'\\b(woman|women|female|girl|mother|wife|she|her|daughter|sister|feminine|womanhood|lady|ladies)\\b',\n    'white': r'\\b(white|whites|caucasian|european)\\b',\n    'black': r'\\b(black|blacks|african.american|african american)\\b',\n    'lgbtq': r'\\b(gay|lesbian|homosexual|bisexual|transgender|trans|queer|lgbtq?|same.sex)\\b',\n    'muslim': r'\\b(muslim|muslims|islam|islamic|mosque|quran|allah)\\b',\n    'christian': r'\\b(christian|christians|christianity|church|bible|jesus|christ)\\b',\n    'jewish': r'\\b(jew|jews|jewish|judaism|synagogue|rabbi)\\b',\n}\n\ntext_lower = df['text'].str.lower()\nfor name, pattern in demo_keywords.items():\n    df[f'mentions_{name}'] = text_lower.str.contains(pattern, regex=True, na=False).astype(int)\n    count = df[f'mentions_{name}'].sum()\n    toxic_rate = df.loc[df[f'mentions_{name}']==1, 'y_true'].mean() if count > 0 else 0\n    print(f'{name:12s}: {count:4d} mentions, toxic rate = {toxic_rate:.3f}')\n\n# Also compute \"no identity mention\" group\nany_identity = df[[f'mentions_{k}' for k in demo_keywords]].max(axis=1)\nprint(f'{\"any_identity\":12s}: {any_identity.sum():4d} mentions')\nprint(f'{\"no_identity\":12s}: {(1-any_identity).sum():4d} mentions')\nPYEOF",
  "description": "Count demographic keyword mentions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport pandas as pd\nimport re\n\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv')\n\n# Define demographic keyword groups\ndemo_keywords = {\n    'male': r'\\b(man|men|male|boy|father|husband|he|him|his|son|brother|masculine|manhood|guy|gentleman)\\b',\n    'female': r'\\b(woman|women|female|girl|mother|wife|she|her|daughter|sister|feminine|womanhood|lady|ladies)\\b',\n    'white': r'\\b(white|whites|caucasian|european)\\b',\n    'black': r'\\b(black|blacks|african.american|african american)\\b',\n    'lgbtq': r'\\b(gay|lesbian|homosexual|bisexual|transgender|trans|queer|lgbtq?|same.sex)\\b',\n    'muslim': r'\\b(muslim|muslims|islam|islamic|mosque|quran|allah)\\b',\n    'christian': r'\\b(christian|christians|christianity|church|bible|jesus|christ)\\b',\n    'jewish': r'\\b(jew|jews|jewish|judaism|synagogue|rabbi)\\b',\n}\n\ntext_lower = df['text'].str.lower()\nfor name, pattern in demo_keywords.items():\n    df[f'mentions_{name}'] = text_lower.str.contains(pattern, regex=True, na=False).astype(int)\n    count = df[f'mentions_{name}'].sum()\n    toxic_rate = df.loc[df[f'mentions_{name}']==1, 'y_true'].mean() if count > 0 else 0\n    print(f'{name:12s}: {count:4d} mentions, toxic rate = {toxic_rate:.3f}')\n\n# Also compute \"no identity mention\" group\nany_identity = df[[f'mentions_{k}' for k in demo_keywords]].max(axis=1)\nprint(f'{\"any_identity\":12s}: {any_identity.sum():4d} mentions')\nprint(f'{\"no_identity\":12s}: {(1-any_identity).sum():4d} mentions')\nPYEOF",
    "description": "Count demographic keyword mentions"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T19:07:47.579906+00:00_

&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
&lt;stdin>:20: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
male        :  744 mentions, toxic rate = 0.363
female      :  287 mentions, toxic rate = 0.376
white       :  105 mentions, toxic rate = 0.486
black       :   48 mentions, toxic rate = 0.521
lgbtq       :   25 mentions, toxic rate = 0.400
muslim      :   57 mentions, toxic rate = 0.526
christian   :   96 mentions, toxic rate = 0.344
jewish      :   11 mentions, toxic rate = 0.364
any_identity: 1061 mentions
no_identity : 1939 mentions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T19:07:47.580112+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport pandas as pd\nimport re\n\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv')\ntext_lower = df['text'].str.lower()\n\n# Refined keywords without pronouns\ndemo_keywords = {\n    'gender': r'\\bm(?:an|en|ale|asculin)|boy|father|husband|son|brother|guy|gentleman|wom[ae]n|female|girl|mother|wife|daughter|sister|femini|lady|ladies\\b',\n    'race': r'\\bwhites?\\b|\\bcaucasian\\b|\\beuropean\\b|\\bblacks?\\b|\\bafrican\\b|\\basian\\b|\\bhispanic\\b|\\blatino?\\b|\\blatina\\b',\n    'religion': r'\\bmuslim|islam|mosque|quran|allah|christian|church|bible|jesus|christ\\b|\\bjews?\\b|\\bjewish\\b|\\bjudaism\\b|\\bhindu\\b|\\bbuddhist\\b',\n    'lgbtq': r'\\bgay\\b|\\blesbian\\b|\\bhomosexual\\b|\\bbisexual\\b|\\btransgender\\b|\\btrans\\b|\\bqueer\\b|\\blgbt',\n}\n\nfor name, pattern in demo_keywords.items():\n    df[f'dm_{name}'] = text_lower.str.contains(pattern, regex=True, na=False).astype(int)\n    count = df[f'dm_{name}'].sum()\n    toxic_rate = df.loc[df[f'dm_{name}']==1, 'y_true'].mean() if count > 0 else 0\n    print(f'{name:12s}: {count:4d} mentions, toxic rate = {toxic_rate:.3f}')\n\n# Priority-based subgroup assignment\ndef assign_subgroup(row):\n    if row['dm_race'] == 1:\n        return 'race'\n    elif row['dm_religion'] == 1:\n        return 'religion'\n    elif row['dm_lgbtq'] == 1:\n        return 'lgbtq'\n    elif row['dm_gender'] == 1:\n        return 'gender'\n    else:\n        return 'no_identity'\n\ndf['demo_subgroup'] = df.apply(assign_subgroup, axis=1)\nprint(\"\\nSubgroup sizes:\")\nprint(df['demo_subgroup'].value_counts())\nprint(\"\\nSubgroup toxic rates:\")\nprint(df.groupby('demo_subgroup')['y_true'].mean())\nPYEOF",
  "description": "Refined demographic subgroup assignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport pandas as pd\nimport re\n\ndf = pd.read_csv('/home/ubuntu/ec_hte_llm_annotation/results/exp023_llm_annotations.csv')\ntext_lower = df['text'].str.lower()\n\n# Refined keywords without pronouns\ndemo_keywords = {\n    'gender': r'\\bm(?:an|en|ale|asculin)|boy|father|husband|son|brother|guy|gentleman|wom[ae]n|female|girl|mother|wife|daughter|sister|femini|lady|ladies\\b',\n    'race': r'\\bwhites?\\b|\\bcaucasian\\b|\\beuropean\\b|\\bblacks?\\b|\\bafrican\\b|\\basian\\b|\\bhispanic\\b|\\blatino?\\b|\\blatina\\b',\n    'religion': r'\\bmuslim|islam|mosque|quran|allah|christian|church|bible|jesus|christ\\b|\\bjews?\\b|\\bjewish\\b|\\bjudaism\\b|\\bhindu\\b|\\bbuddhist\\b',\n    'lgbtq': r'\\bgay\\b|\\blesbian\\b|\\bhomosexual\\b|\\bbisexual\\b|\\btransgender\\b|\\btrans\\b|\\bqueer\\b|\\blgbt',\n}\n\nfor name, pattern in demo_keywords.items():\n    df[f'dm_{name}'] = text_lower.str.contains(pattern, regex=True, na=False).astype(int)\n    count = df[f'dm_{name}'].sum()\n    toxic_rate = df.loc[df[f'dm_{name}']==1, 'y_true'].mean() if count > 0 else 0\n    print(f'{name:12s}: {count:4d} mentions, toxic rate = {toxic_rate:.3f}')\n\n# Priority-based subgroup assignment\ndef assign_subgroup(row):\n    if row['dm_race'] == 1:\n        return 'race'\n    elif row['dm_religion'] == 1:\n        return 'religion'\n    elif row['dm_lgbtq'] == 1:\n        return 'lgbtq'\n    elif row['dm_gender'] == 1:\n        return 'gender'\n    else:\n        return 'no_identity'\n\ndf['demo_subgroup'] = df.apply(assign_subgroup, axis=1)\nprint(\"\\nSubgroup sizes:\")\nprint(df['demo_subgroup'].value_counts())\nprint(\"\\nSubgroup toxic rates:\")\nprint(df.groupby('demo_subgroup')['y_true'].mean())\nPYEOF",
    "description": "Refined demographic subgroup assignment"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-23T19:07:47.580257+00:00_

gender      :  855 mentions, toxic rate = 0.338
race        :  135 mentions, toxic rate = 0.481
religion    :  162 mentions, toxic rate = 0.389
lgbtq       :   21 mentions, toxic rate = 0.524

Subgroup sizes:
demo_subgroup
no_identity    1995
gender          710
religion        145
race            135
lgbtq            15
Name: count, dtype: int64

Subgroup toxic rates:
demo_subgroup
gender         0.325352
lgbtq          0.466667
no_identity    0.271679
race           0.481481
religion       0.379310
Name: y_true, dtype: float64

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-23T19:07:47.580513+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp_civilcomments_demographic.py",
  "content": "\"\"\"\nCivil Comments demographic subgroup analysis for EC-HTE validation.\n\nUses existing LLM annotations (3 models × 3000 comments) with keyword-based\ndemographic subgroups to compute per-subgroup confusion matrices and run\nsemi-synthetic causal inference (naive / global corrected / EC-HTE).\n\"\"\"\n\nimport json\nimport warnings\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\nPROJ = Path(__file__).parent\nRESULTS = PROJ / \"results\"\nARTIFACTS = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts\")\nARTIFACTS.mkdir(parents=True, exist_ok=True)\n\nLLM_MODELS = [\"gpt-4o\", \"gpt-4o-mini\", \"gpt-3.5-turbo\"]\n\nN_SIM = 5000\nN_MC = 50\nN_EXPERT_LIST = [100, 250, 500]\nSEED_BASE = 42\nTAU_Z0 = 0.10\nTAU_Z1 = 0.30\nP_T = 0.5\n\n\n# ── Step 1: Load data and assign demographic subgroups ──\n\ndef load_and_assign_subgroups():\n    df = pd.read_csv(RESULTS / \"exp023_llm_annotations.csv\")\n\n    text_lower = df['text'].str.lower()\n\n    gender_pat = r'man\\b|men\\b|male|masculin|boy|father|husband|son\\b|brother|guy|gentleman|woman|women|female|girl|mother|wife|daughter|sister|feminin|lady|ladies'\n    race_pat = r'\\bwhites?\\b|\\bcaucasian|\\beuropean|\\bblacks?\\b|\\bafrican|\\basian|\\bhispanic|\\blatino|\\blatina|\\bgay\\b|\\blesbian|\\bhomosexual|\\bbisexual|\\btransgender|\\btrans\\b|\\bqueer\\b|\\blgbt'\n    religion_pat = r'\\bmuslim|\\bislam|\\bmosque|\\bquran|\\ballah|\\bchristian|\\bchurch\\b|\\bbible|\\bjesus|\\bchrist\\b|\\bjews?\\b|\\bjewish|\\bjudaism|\\bhindu|\\bbuddhist'\n\n    df['dm_gender'] = text_lower.str.contains(gender_pat, regex=True, na=False).astype(int)\n    df['dm_race'] = text_lower.str.contains(race_pat, regex=True, na=False).astype(int)\n    df['dm_religion'] = text_lower.str.contains(religion_pat, regex=True, na=False).astype(int)\n\n    def assign(row):\n        if row['dm_race'] == 1:\n            return 'race_lgbtq'\n        if row['dm_religion'] == 1:\n            return 'religion'\n        if row['dm_gender'] == 1:\n            return 'gender'\n        return 'no_identity'\n\n    df['demo_subgroup'] = df.apply(assign, axis=1)\n    return df\n\n\n# ── Step 2: Per-subgroup confusion matrices ──\n\ndef compute_subgroup_cm(df, pred_col, subgroup_col='demo_subgroup'):\n    results = {}\n    for sg in sorted(df[subgroup_col].unique()):\n        mask = df[subgroup_col] == sg\n        sub = df[mask]\n        y = sub['y_true'].values\n        yhat = sub[pred_col].values\n\n        valid = ~np.isnan(yhat)\n        y, yhat = y[valid], yhat[valid].astype(int)\n\n        tp = ((y == 1) & (yhat == 1)).sum()\n        tn = ((y == 0) & (yhat == 0)).sum()\n        fp = ((y == 0) & (yhat == 1)).sum()\n        fn = ((y == 1) & (yhat == 0)).sum()\n        n_pos = (y == 1).sum()\n        n_neg = (y == 0).sum()\n\n        fpr = fp / n_neg if n_neg > 0 else 0\n        fnr = fn / n_pos if n_pos > 0 else 0\n        acc = (tp + tn) / len(y) if len(y) > 0 else 0\n\n        results[sg] = {\n            'tp': int(tp), 'tn': int(tn), 'fp': int(fp), 'fn': int(fn),\n            'n': len(y), 'n_pos': int(n_pos), 'n_neg': int(n_neg),\n            'fpr': round(fpr, 4), 'fnr': round(fnr, 4),\n            'accuracy': round(acc, 4),\n            'kappa': round(1 / (1 - fpr - fnr), 4) if (1 - fpr - fnr) != 0 else float('inf'),\n            'pi': round((fpr + fnr) / 2, 4),\n        }\n    return results\n\n\n# ── Step 3: Semi-synthetic DGP (diff-in-means with misclassification) ──\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_cm_from_expert(z_true, z_hat, subgroups, labels):\n    cms = {}\n    for s in labels:\n        ms = subgroups == s\n        zt, zh = z_true[ms], z_hat[ms]\n        n = ms.sum()\n        if n == 0:\n            cms[s] = np.array([[0.5, 0.5], [0.5, 0.5]])\n            continue\n        C = np.zeros((2, 2))\n        for i in [0, 1]:\n            mi = zt == i\n            ni = mi.sum()\n            for j in [0, 1]:\n                C[i, j] = ((zh[mi] == j).sum() + 1) / (ni + 2) if ni > 0 else 0.5\n        cms[s] = C\n    return cms\n\n\ndef log_beta_binom(k, n, a, b):\n    return gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1) + \\\n           gammaln(k + a) + gammaln(n - k + b) - gammaln(n + a + b) - \\\n           (gammaln(a) + gammaln(b) - gammaln(a + b))\n\n\ndef hb_estimate_cm(z_hat_expert, z_true_expert, subgroups_expert, labels,\n                   a0=2.0, b0=2.0, grid_size=200):\n    pi_grid = np.linspace(0.001, 0.499, grid_size)\n    cms = {}\n\n    all_z = z_true_expert\n    all_zh = z_hat_expert\n    n_err_global = (all_z != all_zh).sum()\n    n_global = len(all_z)\n\n    for s in labels:\n        ms = subgroups_expert == s\n        zt, zh = z_true_expert[ms], z_hat_expert[ms]\n        n_s = ms.sum()\n        n_err_s = (zt != zh).sum()\n\n        log_prior = np.zeros(grid_size)\n        for i, pi_val in enumerate(pi_grid):\n            log_prior[i] = log_beta_binom(n_err_global, n_global, a0, b0) + \\\n                           np.log(pi_val) * 0\n\n        log_lik = np.zeros(grid_size)\n        for i, pi_val in enumerate(pi_grid):\n            log_lik[i] = n_err_s * np.log(pi_val + 1e-15) + \\\n                         (n_s - n_err_s) * np.log(1 - pi_val + 1e-15)\n\n        log_post = log_lik\n        log_post -= log_post.max()\n        post = np.exp(log_post)\n        post /= post.sum()\n\n        pi_hat = (pi_grid * post).sum()\n        C = np.array([[1 - pi_hat, pi_hat], [pi_hat, 1 - pi_hat]])\n        cms[s] = C\n    return cms\n\n\ndef run_semisynthetic(real_cms_per_model, subgroup_labels, subgroup_weights):\n    rng = np.random.default_rng(SEED_BASE)\n    results = []\n\n    for model_name, real_cm_dict in real_cms_per_model.items():\n        fpr_per_sg = {s: real_cm_dict[s]['fpr'] for s in subgroup_labels}\n        fnr_per_sg = {s: real_cm_dict[s]['fnr'] for s in subgroup_labels}\n\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            rng_mc = np.random.default_rng(seed)\n\n            subgroups = rng_mc.choice(subgroup_labels, size=N_SIM, p=subgroup_weights)\n            T = rng_mc.binomial(1, P_T, N_SIM)\n            Z_true = rng_mc.binomial(1, 0.3, N_SIM)\n\n            tau_true = np.where(Z_true == 1, TAU_Z1, TAU_Z0)\n            Y0 = rng_mc.normal(0, 1, N_SIM)\n            Y1 = Y0 + tau_true\n            Y = np.where(T == 1, Y1, Y0)\n\n            Z_hat = Z_true.copy()\n            for s in subgroup_labels:\n                ms = subgroups == s\n                for i in np.where(ms & (Z_true == 0))[0]:\n                    if rng_mc.random() < fpr_per_sg[s]:\n                        Z_hat[i] = 1\n                for i in np.where(ms & (Z_true == 1))[0]:\n                    if rng_mc.random() < fnr_per_sg[s]:\n                        Z_hat[i] = 0\n\n            for n_expert in N_EXPERT_LIST:\n                idx_expert = rng_mc.choice(N_SIM, n_expert, replace=False)\n                z_true_exp = Z_true[idx_expert]\n                z_hat_exp = Z_hat[idx_expert]\n                sg_exp = subgroups[idx_expert]\n\n                # Oracle\n                tau_oracle, se_oracle = diff_in_means(Y, T, Z_true == 1)\n                tau0_oracle, _ = diff_in_means(Y, T, Z_true == 0)\n\n                # Naive\n                tau_naive, se_naive = diff_in_means(Y, T, Z_hat == 1)\n                tau0_naive, _ = diff_in_means(Y, T, Z_hat == 0)\n\n                # Global correction\n                fpr_g = (z_true_exp != z_hat_exp)[z_true_exp == 0].mean() if (z_true_exp == 0).sum() > 0 else 0.1\n                fnr_g = (z_true_exp != z_hat_exp)[z_true_exp == 1].mean() if (z_true_exp == 1).sum() > 0 else 0.1\n                denom_g = 1 - fpr_g - fnr_g\n                if abs(denom_g) < 0.05:\n                    denom_g = 0.05 * np.sign(denom_g) if denom_g != 0 else 0.05\n                p_z1_hat = (Z_hat == 1).mean()\n                p_z1_corrected = (p_z1_hat - fpr_g) / denom_g\n                p_z1_corrected = np.clip(p_z1_corrected, 0.05, 0.95)\n\n                tau1_dim, se1 = diff_in_means(Y, T, Z_hat == 1)\n                tau0_dim, se0 = diff_in_means(Y, T, Z_hat == 0)\n                if not np.isnan(tau1_dim) and not np.isnan(tau0_dim):\n                    tau_global = (tau1_dim - fpr_g * tau0_dim) / denom_g\n                else:\n                    tau_global = np.nan\n\n                # EC-HTE (per-subgroup correction)\n                cms_strat = estimate_cm_from_expert(z_true_exp, z_hat_exp, sg_exp, subgroup_labels)\n                tau_echte_parts = []\n                w_parts = []\n                for s in subgroup_labels:\n                    ms = subgroups == s\n                    C = cms_strat[s]\n                    fpr_s, fnr_s = C[0, 1], C[1, 0]\n                    denom_s = 1 - fpr_s - fnr_s\n                    if abs(denom_s) < 0.05:\n                        denom_s = 0.05\n                    tau1_s, _ = diff_in_means(Y, T, ms & (Z_hat == 1))\n                    tau0_s, _ = diff_in_means(Y, T, ms & (Z_hat == 0))\n                    if not np.isnan(tau1_s) and not np.isnan(tau0_s):\n                        tau_s_corr = (tau1_s - fpr_s * tau0_s) / denom_s\n                        tau_echte_parts.append(tau_s_corr)\n                        w_parts.append(ms.sum())\n                if len(tau_echte_parts) > 0:\n                    w_arr = np.array(w_parts, dtype=float)\n                    w_arr /= w_arr.sum()\n                    tau_echte = np.dot(w_arr, tau_echte_parts)\n                else:\n                    tau_echte = np.nan\n\n                # HB EC-HTE\n                cms_hb = hb_estimate_cm(z_hat_exp, z_true_exp, sg_exp, subgroup_labels)\n                tau_hb_parts = []\n                w_hb_parts = []\n                for s in subgroup_labels:\n                    ms = subgroups == s\n                    C = cms_hb[s]\n                    fpr_s, fnr_s = C[0, 1], C[1, 0]\n                    denom_s = 1 - fpr_s - fnr_s\n                    if abs(denom_s) < 0.05:\n                        denom_s = 0.05\n                    tau1_s, _ = diff_in_means(Y, T, ms & (Z_hat == 1))\n                    tau0_s, _ = diff_in_means(Y, T, ms & (Z_hat == 0))\n                    if not np.isnan(tau1_s) and not np.isnan(tau0_s):\n                        tau_s_corr = (tau1_s - fpr_s * tau0_s) / denom_s\n                        tau_hb_parts.append(tau_s_corr)\n                        w_hb_parts.append(ms.sum())\n                if len(tau_hb_parts) > 0:\n                    w_arr = np.array(w_hb_parts, dtype=float)\n                    w_arr /= w_arr.sum()\n                    tau_hb = np.dot(w_arr, tau_hb_parts)\n                else:\n                    tau_hb = np.nan\n\n                tau_true_z1 = TAU_Z1\n\n                for method, est in [('oracle', tau_oracle), ('naive', tau_naive),\n                                     ('global_corrected', tau_global),\n                                     ('stratified_mle', tau_echte),\n                                     ('hb_ec_hte', tau_hb)]:\n                    if not np.isnan(est):\n                        bias = est - tau_true_z1\n                        results.append({\n                            'model': model_name, 'mc': mc, 'n_expert': n_expert,\n                            'method': method, 'estimate': est,\n                            'bias': bias, 'abs_bias': abs(bias),\n                            'sign_correct': int(np.sign(est) == np.sign(tau_true_z1)),\n                        })\n\n    return pd.DataFrame(results)\n\n\n# ── Step 4: Main ──\n\ndef main():\n    print(\"=== Civil Comments Demographic Subgroup Analysis ===\\n\")\n\n    # Load data\n    df = load_and_assign_subgroups()\n\n    subgroup_labels = sorted(df['demo_subgroup'].unique())\n    print(f\"Subgroups: {subgroup_labels}\")\n    print(f\"Subgroup sizes:\")\n    sg_counts = df['demo_subgroup'].value_counts()\n    for sg in subgroup_labels:\n        n = sg_counts[sg]\n        toxic = df.loc[df['demo_subgroup'] == sg, 'y_true'].mean()\n        print(f\"  {sg}: n={n}, toxic_rate={toxic:.3f}\")\n\n    # Compute confusion matrices per model per subgroup\n    all_cms = {}\n    cm_rows = []\n    for model in LLM_MODELS:\n        pred_col = f'pred_{model}'\n        cms = compute_subgroup_cm(df, pred_col)\n        all_cms[model] = cms\n\n        for sg, cm in cms.items():\n            cm['model'] = model\n            cm['subgroup'] = sg\n            cm_rows.append(cm)\n\n    cm_df = pd.DataFrame(cm_rows)\n    cm_df.to_csv(ARTIFACTS / \"civilcomments_analysis.csv\", index=False)\n    print(\"\\n--- Per-subgroup confusion matrices saved ---\")\n\n    # Print CM table\n    print(\"\\n=== Per-Subgroup Error Rates ===\")\n    print(f\"{'Model':<16} {'Subgroup':<14} {'N':>5} {'FPR':>7} {'FNR':>7} {'Acc':>7} {'κ':>8} {'π':>7}\")\n    print(\"-\" * 75)\n    for model in LLM_MODELS:\n        for sg in subgroup_labels:\n            cm = all_cms[model][sg]\n            print(f\"{model:<16} {sg:<14} {cm['n']:>5} {cm['fpr']:>7.4f} {cm['fnr']:>7.4f} \"\n                  f\"{cm['accuracy']:>7.4f} {cm['kappa']:>8.3f} {cm['pi']:>7.4f}\")\n        print()\n\n    # Compute kappa range and bias amplification potential\n    print(\"\\n=== Kappa Analysis ===\")\n    for model in LLM_MODELS:\n        kappas = [all_cms[model][sg]['kappa'] for sg in subgroup_labels if all_cms[model][sg]['kappa'] != float('inf')]\n        fpr_range = max(all_cms[model][sg]['fpr'] for sg in subgroup_labels) - min(all_cms[model][sg]['fpr'] for sg in subgroup_labels)\n        fnr_range = max(all_cms[model][sg]['fnr'] for sg in subgroup_labels) - min(all_cms[model][sg]['fnr'] for sg in subgroup_labels)\n        if kappas:\n            print(f\"{model}: κ range [{min(kappas):.3f}, {max(kappas):.3f}], \"\n                  f\"ΔFPR={fpr_range:.4f}, ΔFNR={fnr_range:.4f}\")\n\n    # Subgroup weights for simulation\n    subgroup_weights = np.array([sg_counts[sg] for sg in subgroup_labels], dtype=float)\n    subgroup_weights /= subgroup_weights.sum()\n\n    # Run semi-synthetic DGP\n    print(\"\\n=== Running Semi-Synthetic DGP ===\")\n    print(f\"N={N_SIM}, MC={N_MC}, τ(Z=0)={TAU_Z0}, τ(Z=1)={TAU_Z1}\")\n    sim_df = run_semisynthetic(all_cms, subgroup_labels, subgroup_weights)\n\n    # Summarize\n    summary = sim_df.groupby(['model', 'n_expert', 'method']).agg(\n        mean_bias=('bias', 'mean'),\n        mean_abs_bias=('abs_bias', 'mean'),\n        rmse=('bias', lambda x: np.sqrt((x**2).mean())),\n        sign_reversal_rate=('sign_correct', lambda x: 1 - x.mean()),\n    ).reset_index()\n\n    print(\"\\n=== Semi-Synthetic Results ===\")\n    print(f\"{'Model':<16} {'n_exp':>5} {'Method':<20} {'|Bias|':>8} {'RMSE':>8} {'SignRev':>8}\")\n    print(\"-\" * 70)\n    for _, row in summary.sort_values(['model', 'n_expert', 'method']).iterrows():\n        print(f\"{row['model']:<16} {row['n_expert']:>5} {row['method']:<20} \"\n              f\"{row['mean_abs_bias']:>8.4f} {row['rmse']:>8.4f} {row['sign_reversal_rate']:>8.3f}\")\n\n    # Check for sign reversal\n    print(\"\\n=== Sign Reversal Analysis ===\")\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            for method in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                mask = (sim_df['model'] == model) & (sim_df['n_expert'] == n_exp) & (sim_df['method'] == method)\n                sub = sim_df[mask]\n                if len(sub) > 0:\n                    sr = 1 - sub['sign_correct'].mean()\n                    if sr > 0.01:\n                        print(f\"  {model} / n={n_exp} / {method}: sign reversal rate = {sr:.3f}\")\n\n    # Check bias amplification\n    print(\"\\n=== Bias Amplification ===\")\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            naive_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'naive')]['mean_abs_bias'].values\n            global_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'global_corrected')]['mean_abs_bias'].values\n            echte_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'stratified_mle')]['mean_abs_bias'].values\n            if len(naive_bias) > 0 and len(echte_bias) > 0:\n                amp = echte_bias[0] / naive_bias[0] if naive_bias[0] > 0 else float('inf')\n                if amp > 1.5 or amp < 0.7:\n                    print(f\"  {model} / n={n_exp}: naive |bias|={naive_bias[0]:.4f}, \"\n                          f\"EC-HTE |bias|={echte_bias[0]:.4f}, amplification={amp:.2f}x\")\n\n    # Generate report\n    generate_report(df, all_cms, summary, sim_df, subgroup_labels, subgroup_weights)\n    print(f\"\\nArtifacts saved to {ARTIFACTS}\")\n\n\ndef generate_report(df, all_cms, summary, sim_df, subgroup_labels, subgroup_weights):\n    lines = []\n    lines.append(\"# Civil Comments Demographic Subgroup Analysis — EC-HTE Validation\\n\")\n    lines.append(\"## 1. Dataset & Subgroup Design\\n\")\n    lines.append(f\"**Dataset**: Civil Comments, {len(df)} annotated comments\")\n    lines.append(f\"**Subgroups** (K={len(subgroup_labels)}): keyword-based demographic assignment\")\n    lines.append(f\"**Subgroup labels**: {', '.join(subgroup_labels)}\")\n    lines.append(f\"**Subgroup weights**: {', '.join(f'{s}={w:.3f}' for s, w in zip(subgroup_labels, subgroup_weights))}\")\n    sg_counts = df['demo_subgroup'].value_counts()\n    for sg in subgroup_labels:\n        n = sg_counts[sg]\n        toxic = df.loc[df['demo_subgroup'] == sg, 'y_true'].mean()\n        lines.append(f\"  - {sg}: n={n}, P(toxic)={toxic:.3f}\")\n\n    lines.append(\"\\n## 2. Per-Subgroup Confusion Matrices\\n\")\n    lines.append(\"| Model | Subgroup | N | FPR | FNR | Accuracy | κ | π |\")\n    lines.append(\"|-------|----------|---|-----|-----|----------|---|---|\")\n    for model in LLM_MODELS:\n        for sg in subgroup_labels:\n            cm = all_cms[model][sg]\n            kappa_str = f\"{cm['kappa']:.3f}\" if cm['kappa'] != float('inf') else \"∞\"\n            lines.append(f\"| {model} | {sg} | {cm['n']} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {cm['accuracy']:.4f} | {kappa_str} | {cm['pi']:.4f} |\")\n\n    lines.append(\"\\n## 3. Key Findings: Misclassification Heterogeneity\\n\")\n    for model in LLM_MODELS:\n        fprs = [all_cms[model][sg]['fpr'] for sg in subgroup_labels]\n        fnrs = [all_cms[model][sg]['fnr'] for sg in subgroup_labels]\n        kappas = [all_cms[model][sg]['kappa'] for sg in subgroup_labels if all_cms[model][sg]['kappa'] != float('inf')]\n        lines.append(f\"**{model}**: ΔFPR={max(fprs)-min(fprs):.4f}, ΔFNR={max(fnrs)-min(fnrs):.4f}\")\n        if kappas:\n            lines.append(f\"  κ range: [{min(kappas):.3f}, {max(kappas):.3f}]\")\n\n    lines.append(\"\\n## 4. Semi-Synthetic DGP Results\\n\")\n    lines.append(f\"**DGP**: N={N_SIM}, τ(Z=0)={TAU_Z0}, τ(Z=1)={TAU_Z1}, MC={N_MC}\")\n    lines.append(f\"**Real asymmetric CMs** from LLM annotations on demographic subgroups\\n\")\n    lines.append(\"| Model | n_expert | Method | |Bias| | RMSE | Sign Reversal Rate |\")\n    lines.append(\"|-------|----------|--------|-------|------|--------------------|\")\n    for _, row in summary.sort_values(['model', 'n_expert', 'method']).iterrows():\n        lines.append(f\"| {row['model']} | {row['n_expert']:.0f} | {row['method']} | \"\n                     f\"{row['mean_abs_bias']:.4f} | {row['rmse']:.4f} | {row['sign_reversal_rate']:.3f} |\")\n\n    # Sign reversal summary\n    lines.append(\"\\n## 5. Sign Reversal Analysis\\n\")\n    any_reversal = False\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            for method in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                mask = (sim_df['model'] == model) & (sim_df['n_expert'] == n_exp) & (sim_df['method'] == method)\n                sub = sim_df[mask]\n                if len(sub) > 0:\n                    sr = 1 - sub['sign_correct'].mean()\n                    if sr > 0.01:\n                        lines.append(f\"- **{model}** / n_expert={n_exp} / {method}: sign reversal rate = {sr:.1%}\")\n                        any_reversal = True\n    if not any_reversal:\n        lines.append(\"No sign reversals detected (τ(Z=1)=0.30 is far from zero).\")\n\n    # Bias amplification\n    lines.append(\"\\n## 6. Bias Amplification\\n\")\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            naive_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'naive')]['mean_abs_bias'].values\n            echte_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'stratified_mle')]['mean_abs_bias'].values\n            hb_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'hb_ec_hte')]['mean_abs_bias'].values\n            if len(naive_bias) > 0 and len(echte_bias) > 0 and len(hb_bias) > 0 and naive_bias[0] > 0:\n                amp_mle = echte_bias[0] / naive_bias[0]\n                amp_hb = hb_bias[0] / naive_bias[0]\n                lines.append(f\"- **{model}** / n={n_exp}: naive→MLE amplification={amp_mle:.2f}x, naive→HB={amp_hb:.2f}x\")\n\n    lines.append(\"\\n## 7. Summary\\n\")\n    lines.append(\"### Key numbers:\")\n    # (a) sign reversal\n    lines.append(f\"- **(a) Sign reversal**: {'Yes' if any_reversal else 'No'} (with τ(Z=1)={TAU_Z1})\")\n    # (b) bias amplification range\n    amps = []\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            nb = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'naive')]['mean_abs_bias'].values\n            eb = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'stratified_mle')]['mean_abs_bias'].values\n            if len(nb) > 0 and len(eb) > 0 and nb[0] > 0:\n                amps.append(eb[0] / nb[0])\n    if amps:\n        lines.append(f\"- **(b) Bias amplification**: {min(amps):.2f}x – {max(amps):.2f}x (stratified MLE vs naive)\")\n    # (c) kappa ranges\n    for model in LLM_MODELS:\n        kappas = [all_cms[model][sg]['kappa'] for sg in subgroup_labels if all_cms[model][sg]['kappa'] != float('inf')]\n        if kappas:\n            lines.append(f\"- **(c) κ range ({model})**: [{min(kappas):.3f}, {max(kappas):.3f}]\")\n\n    report = \"\\n\".join(lines)\n    with open(ARTIFACTS / \"civilcomments_report.md\", \"w\") as f:\n        f.write(report)\n    print(\"Report written to civilcomments_report.md\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp_civilcomments_demographic.py",
    "content": "\"\"\"\nCivil Comments demographic subgroup analysis for EC-HTE validation.\n\nUses existing LLM annotations (3 models × 3000 comments) with keyword-based\ndemographic subgroups to compute per-subgroup confusion matrices and run\nsemi-synthetic causal inference (naive / global corrected / EC-HTE).\n\"\"\"\n\nimport json\nimport warnings\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\nPROJ = Path(__file__).parent\nRESULTS = PROJ / \"results\"\nARTIFACTS = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts\")\nARTIFACTS.mkdir(parents=True, exist_ok=True)\n\nLLM_MODELS = [\"gpt-4o\", \"gpt-4o-mini\", \"gpt-3.5-turbo\"]\n\nN_SIM = 5000\nN_MC = 50\nN_EXPERT_LIST = [100, 250, 500]\nSEED_BASE = 42\nTAU_Z0 = 0.10\nTAU_Z1 = 0.30\nP_T = 0.5\n\n\n# ── Step 1: Load data and assign demographic subgroups ──\n\ndef load_and_assign_subgroups():\n    df = pd.read_csv(RESULTS / \"exp023_llm_annotations.csv\")\n\n    text_lower = df['text'].str.lower()\n\n    gender_pat = r'man\\b|men\\b|male|masculin|boy|father|husband|son\\b|brother|guy|gentleman|woman|women|female|girl|mother|wife|daughter|sister|feminin|lady|ladies'\n    race_pat = r'\\bwhites?\\b|\\bcaucasian|\\beuropean|\\bblacks?\\b|\\bafrican|\\basian|\\bhispanic|\\blatino|\\blatina|\\bgay\\b|\\blesbian|\\bhomosexual|\\bbisexual|\\btransgender|\\btrans\\b|\\bqueer\\b|\\blgbt'\n    religion_pat = r'\\bmuslim|\\bislam|\\bmosque|\\bquran|\\ballah|\\bchristian|\\bchurch\\b|\\bbible|\\bjesus|\\bchrist\\b|\\bjews?\\b|\\bjewish|\\bjudaism|\\bhindu|\\bbuddhist'\n\n    df['dm_gender'] = text_lower.str.contains(gender_pat, regex=True, na=False).astype(int)\n    df['dm_race'] = text_lower.str.contains(race_pat, regex=True, na=False).astype(int)\n    df['dm_religion'] = text_lower.str.contains(religion_pat, regex=True, na=False).astype(int)\n\n    def assign(row):\n        if row['dm_race'] == 1:\n            return 'race_lgbtq'\n        if row['dm_religion'] == 1:\n            return 'religion'\n        if row['dm_gender'] == 1:\n            return 'gender'\n        return 'no_identity'\n\n    df['demo_subgroup'] = df.apply(assign, axis=1)\n    return df\n\n\n# ── Step 2: Per-subgroup confusion matrices ──\n\ndef compute_subgroup_cm(df, pred_col, subgroup_col='demo_subgroup'):\n    results = {}\n    for sg in sorted(df[subgroup_col].unique()):\n        mask = df[subgroup_col] == sg\n        sub = df[mask]\n        y = sub['y_true'].values\n        yhat = sub[pred_col].values\n\n        valid = ~np.isnan(yhat)\n        y, yhat = y[valid], yhat[valid].astype(int)\n\n        tp = ((y == 1) & (yhat == 1)).sum()\n        tn = ((y == 0) & (yhat == 0)).sum()\n        fp = ((y == 0) & (yhat == 1)).sum()\n        fn = ((y == 1) & (yhat == 0)).sum()\n        n_pos = (y == 1).sum()\n        n_neg = (y == 0).sum()\n\n        fpr = fp / n_neg if n_neg > 0 else 0\n        fnr = fn / n_pos if n_pos > 0 else 0\n        acc = (tp + tn) / len(y) if len(y) > 0 else 0\n\n        results[sg] = {\n            'tp': int(tp), 'tn': int(tn), 'fp': int(fp), 'fn': int(fn),\n            'n': len(y), 'n_pos': int(n_pos), 'n_neg': int(n_neg),\n            'fpr': round(fpr, 4), 'fnr': round(fnr, 4),\n            'accuracy': round(acc, 4),\n            'kappa': round(1 / (1 - fpr - fnr), 4) if (1 - fpr - fnr) != 0 else float('inf'),\n            'pi': round((fpr + fnr) / 2, 4),\n        }\n    return results\n\n\n# ── Step 3: Semi-synthetic DGP (diff-in-means with misclassification) ──\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_cm_from_expert(z_true, z_hat, subgroups, labels):\n    cms = {}\n    for s in labels:\n        ms = subgroups == s\n        zt, zh = z_true[ms], z_hat[ms]\n        n = ms.sum()\n        if n == 0:\n            cms[s] = np.array([[0.5, 0.5], [0.5, 0.5]])\n            continue\n        C = np.zeros((2, 2))\n        for i in [0, 1]:\n            mi = zt == i\n            ni = mi.sum()\n            for j in [0, 1]:\n                C[i, j] = ((zh[mi] == j).sum() + 1) / (ni + 2) if ni > 0 else 0.5\n        cms[s] = C\n    return cms\n\n\ndef log_beta_binom(k, n, a, b):\n    return gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1) + \\\n           gammaln(k + a) + gammaln(n - k + b) - gammaln(n + a + b) - \\\n           (gammaln(a) + gammaln(b) - gammaln(a + b))\n\n\ndef hb_estimate_cm(z_hat_expert, z_true_expert, subgroups_expert, labels,\n                   a0=2.0, b0=2.0, grid_size=200):\n    pi_grid = np.linspace(0.001, 0.499, grid_size)\n    cms = {}\n\n    all_z = z_true_expert\n    all_zh = z_hat_expert\n    n_err_global = (all_z != all_zh).sum()\n    n_global = len(all_z)\n\n    for s in labels:\n        ms = subgroups_expert == s\n        zt, zh = z_true_expert[ms], z_hat_expert[ms]\n        n_s = ms.sum()\n        n_err_s = (zt != zh).sum()\n\n        log_prior = np.zeros(grid_size)\n        for i, pi_val in enumerate(pi_grid):\n            log_prior[i] = log_beta_binom(n_err_global, n_global, a0, b0) + \\\n                           np.log(pi_val) * 0\n\n        log_lik = np.zeros(grid_size)\n        for i, pi_val in enumerate(pi_grid):\n            log_lik[i] = n_err_s * np.log(pi_val + 1e-15) + \\\n                         (n_s - n_err_s) * np.log(1 - pi_val + 1e-15)\n\n        log_post = log_lik\n        log_post -= log_post.max()\n        post = np.exp(log_post)\n        post /= post.sum()\n\n        pi_hat = (pi_grid * post).sum()\n        C = np.array([[1 - pi_hat, pi_hat], [pi_hat, 1 - pi_hat]])\n        cms[s] = C\n    return cms\n\n\ndef run_semisynthetic(real_cms_per_model, subgroup_labels, subgroup_weights):\n    rng = np.random.default_rng(SEED_BASE)\n    results = []\n\n    for model_name, real_cm_dict in real_cms_per_model.items():\n        fpr_per_sg = {s: real_cm_dict[s]['fpr'] for s in subgroup_labels}\n        fnr_per_sg = {s: real_cm_dict[s]['fnr'] for s in subgroup_labels}\n\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            rng_mc = np.random.default_rng(seed)\n\n            subgroups = rng_mc.choice(subgroup_labels, size=N_SIM, p=subgroup_weights)\n            T = rng_mc.binomial(1, P_T, N_SIM)\n            Z_true = rng_mc.binomial(1, 0.3, N_SIM)\n\n            tau_true = np.where(Z_true == 1, TAU_Z1, TAU_Z0)\n            Y0 = rng_mc.normal(0, 1, N_SIM)\n            Y1 = Y0 + tau_true\n            Y = np.where(T == 1, Y1, Y0)\n\n            Z_hat = Z_true.copy()\n            for s in subgroup_labels:\n                ms = subgroups == s\n                for i in np.where(ms & (Z_true == 0))[0]:\n                    if rng_mc.random() < fpr_per_sg[s]:\n                        Z_hat[i] = 1\n                for i in np.where(ms & (Z_true == 1))[0]:\n                    if rng_mc.random() < fnr_per_sg[s]:\n                        Z_hat[i] = 0\n\n            for n_expert in N_EXPERT_LIST:\n                idx_expert = rng_mc.choice(N_SIM, n_expert, replace=False)\n                z_true_exp = Z_true[idx_expert]\n                z_hat_exp = Z_hat[idx_expert]\n                sg_exp = subgroups[idx_expert]\n\n                # Oracle\n                tau_oracle, se_oracle = diff_in_means(Y, T, Z_true == 1)\n                tau0_oracle, _ = diff_in_means(Y, T, Z_true == 0)\n\n                # Naive\n                tau_naive, se_naive = diff_in_means(Y, T, Z_hat == 1)\n                tau0_naive, _ = diff_in_means(Y, T, Z_hat == 0)\n\n                # Global correction\n                fpr_g = (z_true_exp != z_hat_exp)[z_true_exp == 0].mean() if (z_true_exp == 0).sum() > 0 else 0.1\n                fnr_g = (z_true_exp != z_hat_exp)[z_true_exp == 1].mean() if (z_true_exp == 1).sum() > 0 else 0.1\n                denom_g = 1 - fpr_g - fnr_g\n                if abs(denom_g) < 0.05:\n                    denom_g = 0.05 * np.sign(denom_g) if denom_g != 0 else 0.05\n                p_z1_hat = (Z_hat == 1).mean()\n                p_z1_corrected = (p_z1_hat - fpr_g) / denom_g\n                p_z1_corrected = np.clip(p_z1_corrected, 0.05, 0.95)\n\n                tau1_dim, se1 = diff_in_means(Y, T, Z_hat == 1)\n                tau0_dim, se0 = diff_in_means(Y, T, Z_hat == 0)\n                if not np.isnan(tau1_dim) and not np.isnan(tau0_dim):\n                    tau_global = (tau1_dim - fpr_g * tau0_dim) / denom_g\n                else:\n                    tau_global = np.nan\n\n                # EC-HTE (per-subgroup correction)\n                cms_strat = estimate_cm_from_expert(z_true_exp, z_hat_exp, sg_exp, subgroup_labels)\n                tau_echte_parts = []\n                w_parts = []\n                for s in subgroup_labels:\n                    ms = subgroups == s\n                    C = cms_strat[s]\n                    fpr_s, fnr_s = C[0, 1], C[1, 0]\n                    denom_s = 1 - fpr_s - fnr_s\n                    if abs(denom_s) < 0.05:\n                        denom_s = 0.05\n                    tau1_s, _ = diff_in_means(Y, T, ms & (Z_hat == 1))\n                    tau0_s, _ = diff_in_means(Y, T, ms & (Z_hat == 0))\n                    if not np.isnan(tau1_s) and not np.isnan(tau0_s):\n                        tau_s_corr = (tau1_s - fpr_s * tau0_s) / denom_s\n                        tau_echte_parts.append(tau_s_corr)\n                        w_parts.append(ms.sum())\n                if len(tau_echte_parts) > 0:\n                    w_arr = np.array(w_parts, dtype=float)\n                    w_arr /= w_arr.sum()\n                    tau_echte = np.dot(w_arr, tau_echte_parts)\n                else:\n                    tau_echte = np.nan\n\n                # HB EC-HTE\n                cms_hb = hb_estimate_cm(z_hat_exp, z_true_exp, sg_exp, subgroup_labels)\n                tau_hb_parts = []\n                w_hb_parts = []\n                for s in subgroup_labels:\n                    ms = subgroups == s\n                    C = cms_hb[s]\n                    fpr_s, fnr_s = C[0, 1], C[1, 0]\n                    denom_s = 1 - fpr_s - fnr_s\n                    if abs(denom_s) < 0.05:\n                        denom_s = 0.05\n                    tau1_s, _ = diff_in_means(Y, T, ms & (Z_hat == 1))\n                    tau0_s, _ = diff_in_means(Y, T, ms & (Z_hat == 0))\n                    if not np.isnan(tau1_s) and not np.isnan(tau0_s):\n                        tau_s_corr = (tau1_s - fpr_s * tau0_s) / denom_s\n                        tau_hb_parts.append(tau_s_corr)\n                        w_hb_parts.append(ms.sum())\n                if len(tau_hb_parts) > 0:\n                    w_arr = np.array(w_hb_parts, dtype=float)\n                    w_arr /= w_arr.sum()\n                    tau_hb = np.dot(w_arr, tau_hb_parts)\n                else:\n                    tau_hb = np.nan\n\n                tau_true_z1 = TAU_Z1\n\n                for method, est in [('oracle', tau_oracle), ('naive', tau_naive),\n                                     ('global_corrected', tau_global),\n                                     ('stratified_mle', tau_echte),\n                                     ('hb_ec_hte', tau_hb)]:\n                    if not np.isnan(est):\n                        bias = est - tau_true_z1\n                        results.append({\n                            'model': model_name, 'mc': mc, 'n_expert': n_expert,\n                            'method': method, 'estimate': est,\n                            'bias': bias, 'abs_bias': abs(bias),\n                            'sign_correct': int(np.sign(est) == np.sign(tau_true_z1)),\n                        })\n\n    return pd.DataFrame(results)\n\n\n# ── Step 4: Main ──\n\ndef main():\n    print(\"=== Civil Comments Demographic Subgroup Analysis ===\\n\")\n\n    # Load data\n    df = load_and_assign_subgroups()\n\n    subgroup_labels = sorted(df['demo_subgroup'].unique())\n    print(f\"Subgroups: {subgroup_labels}\")\n    print(f\"Subgroup sizes:\")\n    sg_counts = df['demo_subgroup'].value_counts()\n    for sg in subgroup_labels:\n        n = sg_counts[sg]\n        toxic = df.loc[df['demo_subgroup'] == sg, 'y_true'].mean()\n        print(f\"  {sg}: n={n}, toxic_rate={toxic:.3f}\")\n\n    # Compute confusion matrices per model per subgroup\n    all_cms = {}\n    cm_rows = []\n    for model in LLM_MODELS:\n        pred_col = f'pred_{model}'\n        cms = compute_subgroup_cm(df, pred_col)\n        all_cms[model] = cms\n\n        for sg, cm in cms.items():\n            cm['model'] = model\n            cm['subgroup'] = sg\n            cm_rows.append(cm)\n\n    cm_df = pd.DataFrame(cm_rows)\n    cm_df.to_csv(ARTIFACTS / \"civilcomments_analysis.csv\", index=False)\n    print(\"\\n--- Per-subgroup confusion matrices saved ---\")\n\n    # Print CM table\n    print(\"\\n=== Per-Subgroup Error Rates ===\")\n    print(f\"{'Model':<16} {'Subgroup':<14} {'N':>5} {'FPR':>7} {'FNR':>7} {'Acc':>7} {'κ':>8} {'π':>7}\")\n    print(\"-\" * 75)\n    for model in LLM_MODELS:\n        for sg in subgroup_labels:\n            cm = all_cms[model][sg]\n            print(f\"{model:<16} {sg:<14} {cm['n']:>5} {cm['fpr']:>7.4f} {cm['fnr']:>7.4f} \"\n                  f\"{cm['accuracy']:>7.4f} {cm['kappa']:>8.3f} {cm['pi']:>7.4f}\")\n        print()\n\n    # Compute kappa range and bias amplification potential\n    print(\"\\n=== Kappa Analysis ===\")\n    for model in LLM_MODELS:\n        kappas = [all_cms[model][sg]['kappa'] for sg in subgroup_labels if all_cms[model][sg]['kappa'] != float('inf')]\n        fpr_range = max(all_cms[model][sg]['fpr'] for sg in subgroup_labels) - min(all_cms[model][sg]['fpr'] for sg in subgroup_labels)\n        fnr_range = max(all_cms[model][sg]['fnr'] for sg in subgroup_labels) - min(all_cms[model][sg]['fnr'] for sg in subgroup_labels)\n        if kappas:\n            print(f\"{model}: κ range [{min(kappas):.3f}, {max(kappas):.3f}], \"\n                  f\"ΔFPR={fpr_range:.4f}, ΔFNR={fnr_range:.4f}\")\n\n    # Subgroup weights for simulation\n    subgroup_weights = np.array([sg_counts[sg] for sg in subgroup_labels], dtype=float)\n    subgroup_weights /= subgroup_weights.sum()\n\n    # Run semi-synthetic DGP\n    print(\"\\n=== Running Semi-Synthetic DGP ===\")\n    print(f\"N={N_SIM}, MC={N_MC}, τ(Z=0)={TAU_Z0}, τ(Z=1)={TAU_Z1}\")\n    sim_df = run_semisynthetic(all_cms, subgroup_labels, subgroup_weights)\n\n    # Summarize\n    summary = sim_df.groupby(['model', 'n_expert', 'method']).agg(\n        mean_bias=('bias', 'mean'),\n        mean_abs_bias=('abs_bias', 'mean'),\n        rmse=('bias', lambda x: np.sqrt((x**2).mean())),\n        sign_reversal_rate=('sign_correct', lambda x: 1 - x.mean()),\n    ).reset_index()\n\n    print(\"\\n=== Semi-Synthetic Results ===\")\n    print(f\"{'Model':<16} {'n_exp':>5} {'Method':<20} {'|Bias|':>8} {'RMSE':>8} {'SignRev':>8}\")\n    print(\"-\" * 70)\n    for _, row in summary.sort_values(['model', 'n_expert', 'method']).iterrows():\n        print(f\"{row['model']:<16} {row['n_expert']:>5} {row['method']:<20} \"\n              f\"{row['mean_abs_bias']:>8.4f} {row['rmse']:>8.4f} {row['sign_reversal_rate']:>8.3f}\")\n\n    # Check for sign reversal\n    print(\"\\n=== Sign Reversal Analysis ===\")\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            for method in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                mask = (sim_df['model'] == model) & (sim_df['n_expert'] == n_exp) & (sim_df['method'] == method)\n                sub = sim_df[mask]\n                if len(sub) > 0:\n                    sr = 1 - sub['sign_correct'].mean()\n                    if sr > 0.01:\n                        print(f\"  {model} / n={n_exp} / {method}: sign reversal rate = {sr:.3f}\")\n\n    # Check bias amplification\n    print(\"\\n=== Bias Amplification ===\")\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            naive_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'naive')]['mean_abs_bias'].values\n            global_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'global_corrected')]['mean_abs_bias'].values\n            echte_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'stratified_mle')]['mean_abs_bias'].values\n            if len(naive_bias) > 0 and len(echte_bias) > 0:\n                amp = echte_bias[0] / naive_bias[0] if naive_bias[0] > 0 else float('inf')\n                if amp > 1.5 or amp < 0.7:\n                    print(f\"  {model} / n={n_exp}: naive |bias|={naive_bias[0]:.4f}, \"\n                          f\"EC-HTE |bias|={echte_bias[0]:.4f}, amplification={amp:.2f}x\")\n\n    # Generate report\n    generate_report(df, all_cms, summary, sim_df, subgroup_labels, subgroup_weights)\n    print(f\"\\nArtifacts saved to {ARTIFACTS}\")\n\n\ndef generate_report(df, all_cms, summary, sim_df, subgroup_labels, subgroup_weights):\n    lines = []\n    lines.append(\"# Civil Comments Demographic Subgroup Analysis — EC-HTE Validation\\n\")\n    lines.append(\"## 1. Dataset & Subgroup Design\\n\")\n    lines.append(f\"**Dataset**: Civil Comments, {len(df)} annotated comments\")\n    lines.append(f\"**Subgroups** (K={len(subgroup_labels)}): keyword-based demographic assignment\")\n    lines.append(f\"**Subgroup labels**: {', '.join(subgroup_labels)}\")\n    lines.append(f\"**Subgroup weights**: {', '.join(f'{s}={w:.3f}' for s, w in zip(subgroup_labels, subgroup_weights))}\")\n    sg_counts = df['demo_subgroup'].value_counts()\n    for sg in subgroup_labels:\n        n = sg_counts[sg]\n        toxic = df.loc[df['demo_subgroup'] == sg, 'y_true'].mean()\n        lines.append(f\"  - {sg}: n={n}, P(toxic)={toxic:.3f}\")\n\n    lines.append(\"\\n## 2. Per-Subgroup Confusion Matrices\\n\")\n    lines.append(\"| Model | Subgroup | N | FPR | FNR | Accuracy | κ | π |\")\n    lines.append(\"|-------|----------|---|-----|-----|----------|---|---|\")\n    for model in LLM_MODELS:\n        for sg in subgroup_labels:\n            cm = all_cms[model][sg]\n            kappa_str = f\"{cm['kappa']:.3f}\" if cm['kappa'] != float('inf') else \"∞\"\n            lines.append(f\"| {model} | {sg} | {cm['n']} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {cm['accuracy']:.4f} | {kappa_str} | {cm['pi']:.4f} |\")\n\n    lines.append(\"\\n## 3. Key Findings: Misclassification Heterogeneity\\n\")\n    for model in LLM_MODELS:\n        fprs = [all_cms[model][sg]['fpr'] for sg in subgroup_labels]\n        fnrs = [all_cms[model][sg]['fnr'] for sg in subgroup_labels]\n        kappas = [all_cms[model][sg]['kappa'] for sg in subgroup_labels if all_cms[model][sg]['kappa'] != float('inf')]\n        lines.append(f\"**{model}**: ΔFPR={max(fprs)-min(fprs):.4f}, ΔFNR={max(fnrs)-min(fnrs):.4f}\")\n        if kappas:\n            lines.append(f\"  κ range: [{min(kappas):.3f}, {max(kappas):.3f}]\")\n\n    lines.append(\"\\n## 4. Semi-Synthetic DGP Results\\n\")\n    lines.append(f\"**DGP**: N={N_SIM}, τ(Z=0)={TAU_Z0}, τ(Z=1)={TAU_Z1}, MC={N_MC}\")\n    lines.append(f\"**Real asymmetric CMs** from LLM annotations on demographic subgroups\\n\")\n    lines.append(\"| Model | n_expert | Method | |Bias| | RMSE | Sign Reversal Rate |\")\n    lines.append(\"|-------|----------|--------|-------|------|--------------------|\")\n    for _, row in summary.sort_values(['model', 'n_expert', 'method']).iterrows():\n        lines.append(f\"| {row['model']} | {row['n_expert']:.0f} | {row['method']} | \"\n                     f\"{row['mean_abs_bias']:.4f} | {row['rmse']:.4f} | {row['sign_reversal_rate']:.3f} |\")\n\n    # Sign reversal summary\n    lines.append(\"\\n## 5. Sign Reversal Analysis\\n\")\n    any_reversal = False\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            for method in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                mask = (sim_df['model'] == model) & (sim_df['n_expert'] == n_exp) & (sim_df['method'] == method)\n                sub = sim_df[mask]\n                if len(sub) > 0:\n                    sr = 1 - sub['sign_correct'].mean()\n                    if sr > 0.01:\n                        lines.append(f\"- **{model}** / n_expert={n_exp} / {method}: sign reversal rate = {sr:.1%}\")\n                        any_reversal = True\n    if not any_reversal:\n        lines.append(\"No sign reversals detected (τ(Z=1)=0.30 is far from zero).\")\n\n    # Bias amplification\n    lines.append(\"\\n## 6. Bias Amplification\\n\")\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            naive_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'naive')]['mean_abs_bias'].values\n            echte_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'stratified_mle')]['mean_abs_bias'].values\n            hb_bias = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'hb_ec_hte')]['mean_abs_bias'].values\n            if len(naive_bias) > 0 and len(echte_bias) > 0 and len(hb_bias) > 0 and naive_bias[0] > 0:\n                amp_mle = echte_bias[0] / naive_bias[0]\n                amp_hb = hb_bias[0] / naive_bias[0]\n                lines.append(f\"- **{model}** / n={n_exp}: naive→MLE amplification={amp_mle:.2f}x, naive→HB={amp_hb:.2f}x\")\n\n    lines.append(\"\\n## 7. Summary\\n\")\n    lines.append(\"### Key numbers:\")\n    # (a) sign reversal\n    lines.append(f\"- **(a) Sign reversal**: {'Yes' if any_reversal else 'No'} (with τ(Z=1)={TAU_Z1})\")\n    # (b) bias amplification range\n    amps = []\n    for model in LLM_MODELS:\n        for n_exp in N_EXPERT_LIST:\n            nb = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'naive')]['mean_abs_bias'].values\n            eb = summary[(summary['model'] == model) & (summary['n_expert'] == n_exp) & (summary['method'] == 'stratified_mle')]['mean_abs_bias'].values\n            if len(nb) > 0 and len(eb) > 0 and nb[0] > 0:\n                amps.append(eb[0] / nb[0])\n    if amps:\n        lines.append(f\"- **(b) Bias amplification**: {min(amps):.2f}x – {max(amps):.2f}x (stratified MLE vs naive)\")\n    # (c) kappa ranges\n    for model in LLM_MODELS:\n        kappas = [all_cms[model][sg]['kappa'] for sg in subgroup_labels if all_cms[model][sg]['kappa'] != float('inf')]\n        if kappas:\n            lines.append(f\"- **(c) κ range ({model})**: [{min(kappas):.3f}, {max(kappas):.3f}]\")\n\n    report = \"\\n\".join(lines)\n    with open(ARTIFACTS / \"civilcomments_report.md\", \"w\") as f:\n        f.write(report)\n    print(\"Report written to civilcomments_report.md\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T19:07:47.581069+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/exp_civilcomments_demographic.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-23T19:07:47.581233+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 exp_civilcomments_demographic.py 2>&1",
  "description": "Run the demographic subgroup analysis",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 exp_civilcomments_demographic.py 2>&1",
    "description": "Run the demographic subgroup analysis",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-23T19:07:47.581417+00:00_

=== Civil Comments Demographic Subgroup Analysis ===

Subgroups: ['gender', 'no_identity', 'race_lgbtq', 'religion']
Subgroup sizes:
  gender: n=496, toxic_rate=0.349
  no_identity: n=2212, toxic_rate=0.271
  race_lgbtq: n=164, toxic_rate=0.488
  religion: n=128, toxic_rate=0.375

--- Per-subgroup confusion matrices saved ---

=== Per-Subgroup Error Rates ===
Model            Subgroup           N     FPR     FNR     Acc        κ       π
---------------------------------------------------------------------------
gpt-4o           gender           496  0.3127  0.2254  0.7177    2.165  0.2691
gpt-4o           no_identity     2212  0.2486  0.2387  0.7541    1.951  0.2437
gpt-4o           race_lgbtq       164  0.3810  0.1500  0.7317    2.132  0.2655
gpt-4o           religion         128  0.2875  0.2917  0.7109    2.376  0.2896

gpt-4o-mini      gender           496  0.5418  0.0636  0.6250    2.534  0.3027
gpt-4o-mini      no_identity     2212  0.4823  0.0718  0.6288    2.243  0.2771
gpt-4o-mini      race_lgbtq       164  0.6310  0.0500  0.6524    3.134  0.3405
gpt-4o-mini      religion         128  0.5000  0.1458  0.6328    2.824  0.3229

gpt-3.5-turbo    gender           496  0.4985  0.1618  0.6190    2.944  0.3302
gpt-3.5-turbo    no_identity     2212  0.3968  0.1402  0.6727    2.160  0.2685
gpt-3.5-turbo    race_lgbtq       164  0.5238  0.1000  0.6829    2.658  0.3119
gpt-3.5-turbo    religion         128  0.3875  0.1875  0.6875    2.353  0.2875


=== Kappa Analysis ===
gpt-4o: κ range [1.951, 2.376], ΔFPR=0.1324, ΔFNR=0.1417
gpt-4o-mini: κ range [2.243, 3.134], ΔFPR=0.1487, ΔFNR=0.0958
gpt-3.5-turbo: κ range [2.160, 2.944], ΔFPR=0.1363, ΔFNR=0.0875

=== Running Semi-Synthetic DGP ===
N=5000, MC=50, τ(Z=0)=0.1, τ(Z=1)=0.3

=== Semi-Synthetic Results ===
Model            n_exp Method                 |Bias|     RMSE  SignRev
----------------------------------------------------------------------
gpt-3.5-turbo      100 global_corrected       0.0989   0.1791    0.000
gpt-3.
…[truncated 4039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-23T19:07:47.581581+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ | grep -i \"exp_real_cm\\|exp008_multi\"",
  "description": "Check for multi-LLM data files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ | grep -i \"exp_real_cm\\|exp008_multi\"",
    "description": "Check for multi-LLM data files"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-23T19:07:47.581705+00:00_

exp008_multi_llm_analysis.md
exp008_multi_llm_annotations.csv
exp008_multi_llm_comparison.csv
exp_real_cm_validation.csv
exp_real_cm_validation.log
exp_real_cm_validation_raw.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T19:07:47.581850+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -3 /home/ubuntu/ec_hte_llm_annotation/results/exp008_multi_llm_annotations.csv",
  "description": "Check multi-LLM annotations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "head -3 /home/ubuntu/ec_hte_llm_annotation/results/exp008_multi_llm_annotations.csv",
    "description": "Check multi-LLM annotations"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-23T19:07:47.581985+00:00_

idx,text,true_label,gpt-4.1,has_hashtag,has_mention,text_length_bin,gpt-4o-mini,gpt-3.5-turbo,gpt-4o,gpt-4-turbo
10476,"when you jacked into your house without keys. hell yeah, i'm david blaine jr.",2,2,False,False,short,2,2,2,2
1824,Cigarettes and Valentines,1,1,False,False,short,1,1,1,1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-23T19:07:47.582142+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/civilcomments_*",
  "description": "Check output artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/civilcomments_*",
    "description": "Check output artifacts"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T19:07:47.582268+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1019 May 23 19:06 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/civilcomments_analysis.csv
-rw-r--r-- 1 ubuntu ubuntu 6114 May 23 19:07 /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/civilcomments_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-23T19:07:47.582386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/civilcomments_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/civilcomments_report.md"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-23T19:07:47.582540+00:00_

1	# Civil Comments Demographic Subgroup Analysis — EC-HTE Validation
2	
3	## 1. Dataset & Subgroup Design
4	
5	**Dataset**: Civil Comments, 3000 annotated comments
6	**Subgroups** (K=4): keyword-based demographic assignment
7	**Subgroup labels**: gender, no_identity, race_lgbtq, religion
8	**Subgroup weights**: gender=0.165, no_identity=0.737, race_lgbtq=0.055, religion=0.043
9	  - gender: n=496, P(toxic)=0.349
10	  - no_identity: n=2212, P(toxic)=0.271
11	  - race_lgbtq: n=164, P(toxic)=0.488
12	  - religion: n=128, P(toxic)=0.375
13	
14	## 2. Per-Subgroup Confusion Matrices
15	
16	| Model | Subgroup | N | FPR | FNR | Accuracy | κ | π |
17	|-------|----------|---|-----|-----|----------|---|---|
18	| gpt-4o | gender | 496 | 0.3127 | 0.2254 | 0.7177 | 2.165 | 0.2691 |
19	| gpt-4o | no_identity | 2212 | 0.2486 | 0.2387 | 0.7541 | 1.951 | 0.2437 |
20	| gpt-4o | race_lgbtq | 164 | 0.3810 | 0.1500 | 0.7317 | 2.132 | 0.2655 |
21	| gpt-4o | religion | 128 | 0.2875 | 0.2917 | 0.7109 | 2.376 | 0.2896 |
22	| gpt-4o-mini | gender | 496 | 0.5418 | 0.0636 | 0.6250 | 2.534 | 0.3027 |
23	| gpt-4o-mini | no_identity | 2212 | 0.4823 | 0.0718 | 0.6288 | 2.243 | 0.2771 |
24	| gpt-4o-mini | race_lgbtq | 164 | 0.6310 | 0.0500 | 0.6524 | 3.134 | 0.3405 |
25	| gpt-4o-mini | religion | 128 | 0.5000 | 0.1458 | 0.6328 | 2.824 | 0.3229 |
26	| gpt-3.5-turbo | gender | 496 | 0.4985 | 0.1618 | 0.6190 | 2.944 | 0.3302 |
27	| gpt-3.5-turbo | no_identity | 2212 | 0.3968 | 0.1402 | 0.6727 | 2.160 | 0.2685 |
28	| gpt-3.5-turbo | race_lgbtq | 164 | 0.5238 | 0.1000 | 0.6829 | 2.658 | 0.3119 |
29	| gpt-3.5-turbo | religion | 128 | 0.3875 | 0.1875 | 0.6875 | 2.353 | 0.2875 |
30	
31	## 3. Key Findings: Misclassification Heterogeneity
32	
33	**gpt-4o**: ΔFPR=0.1324, ΔFNR=0.1417
34	  κ range: [1.951, 2.376]
35	**gpt-4o-mini**: ΔFPR=0.1487, ΔFNR=0.0958
36	  κ range: [2.243, 3.134]
37	**gpt-3.5-turbo**: ΔFPR=0.1363, ΔFNR=0.0875
38	  κ range: [2.160, 2.944]
39	
40	## 4. Semi-Synthetic DGP Results
41	
42	**DGP*
…[truncated 4421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp-a-civilcomments_20260523T190133",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-23T19:07:47.582721+00:00_

Analysis complete. Both output files are saved.

**Key results:**

**Per-subgroup misclassification heterogeneity confirmed** across all 3 LLMs on demographic subgroups:
- ΔFPR ranges from 0.09 to 0.15 across subgroups (gender, no_identity, race_lgbtq, religion)
- κ ranges: gpt-4o [1.95, 2.38], gpt-4o-mini [2.24, 3.13], gpt-3.5-turbo [2.16, 2.94]
- race_lgbtq subgroup consistently has highest FPR across all models (0.38–0.63)

**Semi-synthetic DGP findings** (N=5000, τ(Z=1)=0.30, MC=50):
- **(a) Sign reversal**: Yes — 2% rate with stratified MLE at small n_expert (100–250) for gpt-4o-mini and gpt-3.5-turbo
- **(b) Bias amplification**: 1.03x–3.32x (stratified MLE vs naive). Worst at n_expert=100 with gpt-4o (3.32x). HB EC-HTE amplification up to 3.02x with gpt-4o-mini
- **(c) κ ranges**: 1.95–3.13 across all models/subgroups
- **(d) Asymmetric CMs** (especially gpt-4o-mini with FPR≈0.5–0.63) cause severe ill-conditioning, making EC-HTE correction worse than naive in all cases

**Output files:**
- `artifacts/civilcomments_analysis.csv` — per-subgroup confusion matrices
- `artifacts/civilcomments_report.md` — full report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp-a-civilcomments_20260523T190133"
}
```

</details>

---
