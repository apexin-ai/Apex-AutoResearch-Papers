# paper arr precheck suppl checklist

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_paper_arr_precheck_suppl_checklist_20260522T072522.log`
- **Structured JSON:** [`065e30e63ae3d7c4e282.json`](../../sessions/06/065e30e63ae3d7c4e282.json)

## Before a recorded user message

69 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "578b937a-752f-4b87-8815-a2fae86cfa97",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779450600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "91427195-9ba5-43b5-ba7d-e1e22dd898e1",
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper's main.tex to understand the appendix structure, and also check the artifacts directory for any existing checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "693b8538-7514-459b-abe7-b7864fc5a821",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bk6XM6Zzdqq8ucQbAHfma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12438
      },
      "output_tokens": 26,
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

_source line 5_

I'll read the paper and check artifacts in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "4971195d-e17d-4004-89d1-119d1cde9b9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bk6XM6Zzdqq8ucQbAHfma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12438
      },
      "output_tokens": 26,
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

_source line 6_

<details open><summary>🔧 Tool call — Bash · `toolu_01ARfw6mm8wJMwcYZQkRmWwx`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr* 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/ 2>/dev/null",
  "description": "Check artifacts directory for existing checklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "a854b4cc-73a5-4a5f-906a-0f6fb1d9ee72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bk6XM6Zzdqq8ucQbAHfma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12438
      },
      "output_tokens": 26,
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

_source line 7 · 2026-05-22T07:25:34.712Z_

<details><summary>↩ Tool result · `toolu_01ARfw6mm8wJMwcYZQkRmWwx`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_submission_metadata.md
---
_project
ace05_code
ace05_data_prep_report.md
acknowledgements_draft.tex
anonymous_github
appendix_maven_residualized.md
arr_checklist_draft.md
arr_submission_metadata.md
author_response_template.md
bayesian_equivalence_bf01.json
bayesian_equivalence_bf01.py
bcs_comparison.json
bcs_controlled_llama-3.1-70b-fp8
bcs_fix
bootstrap_ci.py
camera_ready_deanonymization_checklist.md
camera_ready_latex_config.md
cross_embedding_sensitivity
cross_model_error_taxonomy.py
crossagentie_analysis.md
d037_data_consistency_check.json
d037_ner_v2_bcs_analysis.json
d037_ner_v2_bcs_paper_text.md
d037_statistical_analyses
d051_batch2
d051_fewrel_n25_s42
docred_ridge_analysis.py
docred_ridge_appendix.tex
docred_ridge_regression.json
dream_reports
error_taxonomy_cross_model.json
error_taxonomy_cross_model_table.tex
eval_exp1.json
eval_exp2.json
exp-004
exp-008
exp-012
exp002_confusability_controlled
exp003a
exp003a_analysis.json
exp004
exp004_maven_bcs
exp006_interaction_2x2
exp008_sdgd_zero_fewnerd
exp008_sdgd_zero_fewnerd_r2
exp012_exp2_diagnosis.md
exp012_llama_8b_r2
exp012_llama_fewrel_ch2
exp3_70b_status.md
exp_docred_confusability
exp_fewrel_80pool_16sub_bootstrap
exp_fewrel_v2_bcs_controlled
exp_fewshot_bcs_v2
exp_gemini_flash
exp_llama70b_cross_model
exp_llama70b_cross_model_analysis.md
exp_llama70b_ner_bcs_null
exp_paired_constrained
exp_schema_intervention
exp_unconstrained_decoding_ablation
exp_v2_re_n25
fewrel_domain_classification.json
fewrel_domain_distribution.json
fewrel_formal
fewrel_formal_full
fewrel_v2_bcs
fewshot_bcs_status.md
fig_bcs_scaling_v2.py
fig_count_curves.py
fig_count_curves_v2.py
fig_error_taxonomy.py
fig_error_taxonomy_v2.py
final_submission_checklist.md
latex_crossref_check.md
manifest.yaml
maven_code
maven_dataset_report.md
multi_model_candidates.md
paper
paper_drafts
paper_v30_llama70b_ner_null.pdf
paper_v31_director_wording.pdf
paper_v32_r23_fixes.pdf
permutation_equivalence_latex.tex
permutation_equivalence_result.json
permutation_equivalence_test.py
q3_tost_n525_corrected.json
q3_tost_n525_results.json
r1_statistical_supplements.json
r1_statistical_supplements.md
r20_literature_additions.md
re_none_evaluation_analysis.json
rebuttal_response_template.md
rebuttal_talking_points.md
references_survey.md
related_work_literature_check.md
review_issues.yaml
review_reports
review_round_29
run_paired_constrained.py
schema-dag-extraction_v23.pdf
schema-dag-extraction_v23_final.pdf
schema_optimizer_test
scs_baseline_comparison
sdgd_design_doc.md
sdgd_routing
semipartial_r2_verification.json
split_sample_bootstrap.json
third_task_type_eval.md
tost_sensitivity
w4_relaxed_matching_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "670b6a47-12ae-4a09-8936-c8f5e1c66797",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_submission_metadata.md\n---\n_project\nace05_code\nace05_data_prep_report.md\nacknowledgements_draft.tex\nanonymous_github\nappendix_maven_residualized.md\narr_checklist_draft.md\narr_submission_metadata.md\nauthor_response_template.md\nbayesian_equivalence_bf01.json\nbayesian_equivalence_bf01.py\nbcs_comparison.json\nbcs_controlled_llama-3.1-70b-fp8\nbcs_fix\nbootstrap_ci.py\ncamera_ready_deanonymization_checklist.md\ncamera_ready_latex_config.md\ncross_embedding_sensitivity\ncross_model_error_taxonomy.py\ncrossagentie_analysis.md\nd037_data_consistency_check.json\nd037_ner_v2_bcs_analysis.json\nd037_ner_v2_bcs_paper_text.md\nd037_statistical_analyses\nd051_batch2\nd051_fewrel_n25_s42\ndocred_ridge_analysis.py\ndocred_ridge_appendix.tex\ndocred_ridge_regression.json\ndream_reports\nerror_taxonomy_cross_model.json\nerror_taxonomy_cross_model_table.tex\neval_exp1.json\neval_exp2.json\nexp-004\nexp-008\nexp-012\nexp002_confusability_controlled\nexp003a\nexp003a_analysis.json\nexp004\nexp004_maven_bcs\nexp006_interaction_2x2\nexp008_sdgd_zero_fewnerd\nexp008_sdgd_zero_fewnerd_r2\nexp012_exp2_diagnosis.md\nexp012_llama_8b_r2\nexp012_llama_fewrel_ch2\nexp3_70b_status.md\nexp_docred_confusability\nexp_fewrel_80pool_16sub_bootstrap\nexp_fewrel_v2_bcs_controlled\nexp_fewshot_bcs_v2\nexp_gemini_flash\nexp_llama70b_cross_model\nexp_llama70b_cross_model_analysis.md\nexp_llama70b_ner_bcs_null\nexp_paired_constrained\nexp_schema_intervention\nexp_unconstrained_decoding_ablation\nexp_v2_re_n25\nfewrel_domain_classification.json\nfewrel_domain_distribution.json\nfewrel_formal\nfewrel_formal_full\nfewrel_v2_bcs\nfewshot_bcs_status.md\nfig_bcs_scaling_v2.py\nfig_count_curves.py\nfig_count_curves_v2.py\nfig_error_taxonomy.py\nfig_error_taxonomy_v2.py\nfinal_submission_checklist.md\nlatex_crossref_check.md\nmanifest.yaml\nmaven_code\nmaven_dataset_report.md\nmulti_model_candidates.md\npaper\npaper_drafts\npaper_v30_llama70b_ner_null.pdf\npaper_v31_director_wording.pdf\npaper_v32_r23_fixes.pdf\npermutation_equivalence_latex.tex\npermutation_equivalence_result.json\npermutation_equivalence_test.py\nq3_tost_n525_corrected.json\nq3_tost_n525_results.json\nr1_statistical_supplements.json\nr1_statistical_supplements.md\nr20_literature_additions.md\nre_none_evaluation_analysis.json\nrebuttal_response_template.md\nrebuttal_talking_points.md\nreferences_survey.md\nrelated_work_literature_check.md\nreview_issues.yaml\nreview_reports\nreview_round_29\nrun_paired_constrained.py\nschema-dag-extraction_v23.pdf\nschema-dag-extraction_v23_final.pdf\nschema_optimizer_test\nscs_baseline_comparison\nsdgd_design_doc.md\nsdgd_routing\nsemipartial_r2_verification.json\nsplit_sample_bootstrap.json\nthird_task_type_eval.md\ntost_sensitivity\nw4_relaxed_matching_results.json",
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

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01CyPP5XZoZFGy28B7XdhvJ3`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "564f9274-ef50-4fb1-9da1-18460164c737",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bk6XM6Zzdqq8ucQbAHfma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12438
      },
      "output_tokens": 26,
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

_source line 9 · 2026-05-22T07:25:35.071Z_

<details><summary>↩ Tool result · reported error · `toolu_01CyPP5XZoZFGy28B7XdhvJ3`</summary>

```text
Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/': No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "14b42ee0-c1a5-48ba-8df2-6c5076cb6333",
  "tool_use_result": "Error: Exit code 2\nls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/': No such file or directory"
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01LoAWsgpPvb99QtozrfxJa7`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "53945be3-278b-4d4e-87eb-199794c92805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V9gEpy2wBiknf6F395dzL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 24279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1502
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

_source line 11 · 2026-05-22T07:25:38.058Z_

<details><summary>↩ Tool result · `toolu_01LoAWsgpPvb99QtozrfxJa7`</summary>

```text
artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
docs/paper/supplementary.tex
artifacts/acknowledgements_draft.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex
docs/paper/main.tex
docs/paper/discussion.tex
docs/paper/sdgd_negative.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "b2cc8e7e-87a9-406a-af3a-558b42e67779",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T053106/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/worst/paper.tex",
      "artifacts/_project/paper/dataset_stats.tex",
      "artifacts/paper/tables/dataset_stats.tex",
      "artifacts/_project/paper/sdgd_negative.tex",
      "artifacts/_project/paper/experimental_setup.tex",
      "docs/paper/conclusion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/worst/paper.tex",
      "docs/paper/supplementary.tex",
      "artifacts/acknowledgements_draft.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/checklist.tex",
      "artifacts/error_taxonomy_cross_model_table.tex",
      "artifacts/permutation_equivalence_latex.tex",
      "artifacts/_project/paper/docred_ridge_appendix.tex",
      "artifacts/docred_ridge_appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/discussion.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 30,
    "numFiles": 34,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01HusYuWHr2RQ42AVy13pmpU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "7538e564-ba38-4e3d-a7c8-96eb89aece82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V9gEpy2wBiknf6F395dzL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1502,
      "cache_read_input_tokens": 24279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1502
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

_source line 13 · 2026-05-22T07:25:38.424Z_

<details><summary>↩ Tool result · `toolu_01HusYuWHr2RQ42AVy13pmpU`</summary>

```text
1	# ARR Submission Preparation — EMNLP 2026
2	
3	Updated 2026-05-22 (v34: cross-model error taxonomy added, semipartial R² corrected, Limitations W1 updated).
4	
5	## 1. Supplementary Materials Status
6	
7	### Appendix (in-paper)
8	- Pages 10–26+ of main.pdf contain all appendices (A–Y)
9	- Covers: SDGD details, factorial analysis, prompt templates, cross-model validation, power analysis, error analysis, contamination analysis, cross-model error taxonomy (Table `cross_model_error_taxonomy`), etc.
10	
11	### Anonymous Code Repository
12	- `artifacts/anonymous_github/` contains a prepared anonymous repo:
13	  - `src/` — 42 Python scripts (experiment runners, analysis, evaluation)
14	  - `scripts/` — 24 auxiliary scripts (figure generation, embedding computation, Monte Carlo simulation)
15	  - `data/README.md` — data documentation
16	  - `requirements.txt`, `LICENSE`, `README.md`
17	- **Action needed (user):** Upload to Anonymous GitHub (https://anonymous.4open.science/) and paste the link in OpenReview supplementary field
18	- **Check before upload:** Ensure no hardcoded server paths (e.g. `/root/`) remain in scripts
19	
20	### Data
21	- All four datasets (Few-NERD, FewRel, DocRED, MAVEN) are publicly available with citations
22	- Sampled evaluation sets (1,000 instances each) should be included in the anonymous repo `data/` directory or described with exact reproduction steps
23	- SCS matrices and batch configurations should be included for full reproducibility
24	
25	### Supplementary ZIP
26	- ARR allows a single supplementary PDF or ZIP
27	- **Recommendation:** Not strictly needed if anonymous GitHub link is provided. If preferred, ZIP the anonymous_github directory.
28	
29	---
30	
31	## 2. ARR Responsible NLP Checklist (OpenReview Form)
32	
33	Below are suggested answers for each question on the OpenReview submission form. The user should review and adjust before submitting.
34	
35	### A. For Every Submission
36	
37	**A1. Did you describe the limitations of your work?**
38	- **Answer:** Yes
39	- **Section:** Limitations section (after §6), 6 items covering model coverage (W1: TOST/SDGD remain single-model; error taxonomy now cross-model validated), effect size, task scope, causal mechanism, domain scope, and multiple comparisons
40	
41	**A2. Did you discuss any potential risks of your work?**
42	- **Answer:** Yes
43	- **Justification:** Limitations section. SCS/BCS are diagnostic proxies, not deployment criteria. Risk of misuse as automatic schema rejection is noted.
44	
45	**A3. Do the abstract and introduction summarize the paper's main claims?**
46	- **Answer:** Yes
47	- **Section:** Abstract (3 numbered findings), Introduction §1 (4 findings + 3 contributions)
48	
49	**A4. Did you use AI assistants?**
50	- **Answer:** Yes
51	- **Justification:** Claude (Anthropic) for writing assistance and experimental code development. Research design, execution, and interpretation are the authors' own work.
52	
53	### B. Scientific Artifacts
54	
55	**B1. Did you cite the creators of artifacts you used?**
56	- **Answer:** Yes
57	- **Section:** §3.1 (datasets), §3.5 (models). All datasets (Few-NERD, FewRel, DocRED, MAVEN), models (Qwen3, LLaMA, Gemini), and tools (vLLM, MiniLM) cited.
58	
59	**B2. Did you discuss the license or terms?**
60	- **Answer:** Yes
61	- **Justification:** Few-NERD: CC-BY-SA 4.0; FewRel/DocRED/MAVEN: publicly released for research. Open-weight models used under respective licenses; Gemini via API terms of service.
62	
63	**B3. Did you discuss if your use is consistent with intended use?**
64	- **Answer:** Yes
65	- **Justification:** All datasets used for their intended IE evaluation purpose.
66	
67	**B4. Did you discuss PII or offensive content?**
68	- **Answer:** N/A
69	- **Justification:** Established benchmarks, no new data collection or annotation.
70	
71	**B5. Did you provide documentation of artifacts?**
72	- **Answer:** Yes
73	- **Section:** Table 1 (dataset statistics), §3.1 (provenance, sampling)
74	
75	**B6. Did you report relevant statistics?**
76	- **Answer:** Yes
77	- **Section:** §3.1, Table 1 (sizes, type counts, sampling), §3.3 (count levels, batch sizes)
78	
79	### C. Computational Experiments
80	
81	**C1. Did you report parameters, compute budget, and infrastructure?**
82	- **Answer:** Yes
83	- **Section:** §3.5. Models: Qwen3-32B (FP8), LLaMA-70B (FP8), LLaMA-8B, Gemini Flash (API). Hardware: NVIDIA RTX PRO 6000 (96GB). Total: ~72 GPU-hours inference (open-weight models), no training. Gemini Flash runs via API (cost not GPU-hours). Cross-model error taxonomy analysis reuses existing prediction outputs.
84	
85	**C2. Did you discuss experimental setup and hyperparameters?**
86	- **Answer:** Yes
87	- **Section:** §3.3 (count curves, BCS-controlled design), §3.5 (greedy decoding, temp=0, seed=42). No hyperparameter search (zero-shot evaluation study).
88	
89	**C3. Did you report descriptive statistics?**
90	- **Answer:** Yes
91	- **Justification:** All key metrics include 95% bootstrap CIs (B=10,000 for pairwise, B=1,000 for batch-level). Correlations with p-values throughout §4. Permutation tests for slope comparisons. Semipartial R² (ΔR²) correctly computed as R²_full − R²_reduced (verified v34).
92	
93	**C4. Did you report implementation details?**
94	- **Answer:** Yes
95	- **Section:** §3.5 (vLLM v0.20.2, model versions). Code release upon acceptance.
96	
97	### D. Human Annotators or Crowdworkers
98	
99	**D1–D5:** All N/A. No human annotation or crowdsourcing conducted.
100	
101	### E. AI-Assisted Research
102	
103	**E1. Did you report the use of AI assistants?**
104	- **Answer:** Yes
105	- **Section:** A4 above. AI used for code development and document formatting; research design/execution/interpretation by authors.
106	
107	---
108	
109	## 3. PDF Sanity Check Results
110	
111	| Check | Status | Details |
112	|-------|--------|---------|
113	| Path leaks (/home/, /root/, etc.) | ✅ PASS | 0 found |
114	| TODO / FIXME / placeholder | ✅ PASS | 0 in source; 1 benign "Placeholders" in prompt template description |
115	| Undefined references | ✅ PASS | 0 |
116	| Undefined citations | ✅ PASS | 0 |
117	| Line numbers (review mode) | ✅ PASS | `\usepackage[review]{acl}`, 587 numbered lines |
118	| Abstract word count | ✅ PASS | ~133 words (limit: 250) |
119	| Body page count | ✅ PASS | ≤ 8 pages (Discussion ends p.8, Limitations starts p.8) |
120	| Total pages | ℹ️ INFO | ~27 pages (8 body + Limitations + References + Appendix; exact count may shift after cross-model error taxonomy table addition — recompile to verify) |
121	| Anonymous submission | ✅ PASS | No author names in PDF; "Code and data will be released upon acceptance" |
122	| Compute budget disclosed | ✅ PASS | ~72 GPU-hours in checklist C1 |
123	
124	### Items for User Action
125	1. **Anonymous GitHub:** Upload `artifacts/anonymous_github/` to https://anonymous.4open.science/, add link to OpenReview supplementary field
126	2. **Check scripts for paths:** `grep -r '/root/' artifacts/anonymous_github/` before upload
127	3. **Fill OpenReview form:** Use Section 2 above as reference for the Responsible NLP Checklist
128	4. **Verify checklist.tex vs form:** The paper-embedded checklist (checklist.tex) should be consistent with what you enter in the OpenReview form
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "b95413c6-d626-4ff1-885b-73466df5e84a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_draft.md",
      "content": "# ARR Submission Preparation — EMNLP 2026\n\nUpdated 2026-05-22 (v34: cross-model error taxonomy added, semipartial R² corrected, Limitations W1 updated).\n\n## 1. Supplementary Materials Status\n\n### Appendix (in-paper)\n- Pages 10–26+ of main.pdf contain all appendices (A–Y)\n- Covers: SDGD details, factorial analysis, prompt templates, cross-model validation, power analysis, error analysis, contamination analysis, cross-model error taxonomy (Table `cross_model_error_taxonomy`), etc.\n\n### Anonymous Code Repository\n- `artifacts/anonymous_github/` contains a prepared anonymous repo:\n  - `src/` — 42 Python scripts (experiment runners, analysis, evaluation)\n  - `scripts/` — 24 auxiliary scripts (figure generation, embedding computation, Monte Carlo simulation)\n  - `data/README.md` — data documentation\n  - `requirements.txt`, `LICENSE`, `README.md`\n- **Action needed (user):** Upload to Anonymous GitHub (https://anonymous.4open.science/) and paste the link in OpenReview supplementary field\n- **Check before upload:** Ensure no hardcoded server paths (e.g. `/root/`) remain in scripts\n\n### Data\n- All four datasets (Few-NERD, FewRel, DocRED, MAVEN) are publicly available with citations\n- Sampled evaluation sets (1,000 instances each) should be included in the anonymous repo `data/` directory or described with exact reproduction steps\n- SCS matrices and batch configurations should be included for full reproducibility\n\n### Supplementary ZIP\n- ARR allows a single supplementary PDF or ZIP\n- **Recommendation:** Not strictly needed if anonymous GitHub link is provided. If preferred, ZIP the anonymous_github directory.\n\n---\n\n## 2. ARR Responsible NLP Checklist (OpenReview Form)\n\nBelow are suggested answers for each question on the OpenReview submission form. The user should review and adjust before submitting.\n\n### A. For Every Submission\n\n**A1. Did you describe the limitations of your work?**\n- **Answer:** Yes\n- **Section:** Limitations section (after §6), 6 items covering model coverage (W1: TOST/SDGD remain single-model; error taxonomy now cross-model validated), effect size, task scope, causal mechanism, domain scope, and multiple comparisons\n\n**A2. Did you discuss any potential risks of your work?**\n- **Answer:** Yes\n- **Justification:** Limitations section. SCS/BCS are diagnostic proxies, not deployment criteria. Risk of misuse as automatic schema rejection is noted.\n\n**A3. Do the abstract and introduction summarize the paper's main claims?**\n- **Answer:** Yes\n- **Section:** Abstract (3 numbered findings), Introduction §1 (4 findings + 3 contributions)\n\n**A4. Did you use AI assistants?**\n- **Answer:** Yes\n- **Justification:** Claude (Anthropic) for writing assistance and experimental code development. Research design, execution, and interpretation are the authors' own work.\n\n### B. Scientific Artifacts\n\n**B1. Did you cite the creators of artifacts you used?**\n- **Answer:** Yes\n- **Section:** §3.1 (datasets), §3.5 (models). All datasets (Few-NERD, FewRel, DocRED, MAVEN), models (Qwen3, LLaMA, Gemini), and tools (vLLM, MiniLM) cited.\n\n**B2. Did you discuss the license or terms?**\n- **Answer:** Yes\n- **Justification:** Few-NERD: CC-BY-SA 4.0; FewRel/DocRED/MAVEN: publicly released for research. Open-weight models used under respective licenses; Gemini via API terms of service.\n\n**B3. Did you discuss if your use is consistent with intended use?**\n- **Answer:** Yes\n- **Justification:** All datasets used for their intended IE evaluation purpose.\n\n**B4. Did you discuss PII or offensive content?**\n- **Answer:** N/A\n- **Justification:** Established benchmarks, no new data collection or annotation.\n\n**B5. Did you provide documentation of artifacts?**\n- **Answer:** Yes\n- **Section:** Table 1 (dataset statistics), §3.1 (provenance, sampling)\n\n**B6. Did you report relevant statistics?**\n- **Answer:** Yes\n- **Section:** §3.1, Table 1 (sizes, type counts, sampling), §3.3 (count levels, batch sizes)\n\n### C. Computational Experiments\n\n**C1. Did you report parameters, compute budget, and infrastructure?**\n- **Answer:** Yes\n- **Section:** §3.5. Models: Qwen3-32B (FP8), LLaMA-70B (FP8), LLaMA-8B, Gemini Flash (API). Hardware: NVIDIA RTX PRO 6000 (96GB). Total: ~72 GPU-hours inference (open-weight models), no training. Gemini Flash runs via API (cost not GPU-hours). Cross-model error taxonomy analysis reuses existing prediction outputs.\n\n**C2. Did you discuss experimental setup and hyperparameters?**\n- **Answer:** Yes\n- **Section:** §3.3 (count curves, BCS-controlled design), §3.5 (greedy decoding, temp=0, seed=42). No hyperparameter search (zero-shot evaluation study).\n\n**C3. Did you report descriptive statistics?**\n- **Answer:** Yes\n- **Justification:** All key metrics include 95% bootstrap CIs (B=10,000 for pairwise, B=1,000 for batch-level). Correlations with p-values throughout §4. Permutation tests for slope comparisons. Semipartial R² (ΔR²) correctly computed as R²_full − R²_reduced (verified v34).\n\n**C4. Did you report implementation details?**\n- **Answer:** Yes\n- **Section:** §3.5 (vLLM v0.20.2, model versions). Code release upon acceptance.\n\n### D. Human Annotators or Crowdworkers\n\n**D1–D5:** All N/A. No human annotation or crowdsourcing conducted.\n\n### E. AI-Assisted Research\n\n**E1. Did you report the use of AI assistants?**\n- **Answer:** Yes\n- **Section:** A4 above. AI used for code development and document formatting; research design/execution/interpretation by authors.\n\n---\n\n## 3. PDF Sanity Check Results\n\n| Check | Status | Details |\n|-------|--------|---------|\n| Path leaks (/home/, /root/, etc.) | ✅ PASS | 0 found |\n| TODO / FIXME / placeholder | ✅ PASS | 0 in source; 1 benign \"Placeholders\" in prompt template description |\n| Undefined references | ✅ PASS | 0 |\n| Undefined citations | ✅ PASS | 0 |\n| Line numbers (review mode) | ✅ PASS | `\\usepackage[review]{acl}`, 587 numbered lines |\n| Abstract word count | ✅ PASS | ~133 words (limit: 250) |\n| Body page count | ✅ PASS | ≤ 8 pages (Discussion ends p.8, Limitations starts p.8) |\n| Total pages | ℹ️ INFO | ~27 pages (8 body + Limitations + References + Appendix; exact count may shift after cross-model error taxonomy table addition — recompile to verify) |\n| Anonymous submission | ✅ PASS | No author names in PDF; \"Code and data will be released upon acceptance\" |\n| Compute budget disclosed | ✅ PASS | ~72 GPU-hours in checklist C1 |\n\n### Items for User Action\n1. **Anonymous GitHub:** Upload `artifacts/anonymous_github/` to https://anonymous.4open.science/, add link to OpenReview supplementary field\n2. **Check scripts for paths:** `grep -r '/root/' artifacts/anonymous_github/` before upload\n3. **Fill OpenReview form:** Use Section 2 above as reference for the Responsible NLP Checklist\n4. **Verify checklist.tex vs form:** The paper-embedded checklist (checklist.tex) should be consistent with what you enter in the OpenReview form\n",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the existing checklist draft. Now I need to:
1. Read main.tex to check the appendix sections
2. Check for code availability mentions
3. Check dataset citations
4. Check the Limitations section
5. Read the checklist.tex

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "2624b33d-7ad7-44a6-a90a-799dde16894a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rq6TEEjGUCRagaJ6HwhQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 25781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 15_

Now let me read the paper source files to verify everything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "686a673f-2526-4561-a4cc-4f9a648f1c55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rq6TEEjGUCRagaJ6HwhQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 25781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01V3zyz82T5J1KMsYf9tYeap`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "81efbb15-cfe6-47e9-945f-56a59384d364",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rq6TEEjGUCRagaJ6HwhQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 25781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01FU5k1ojUCjfbQoDsgfxeHT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "22982baf-5500-41ca-a2e7-3bf21ae0656e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rq6TEEjGUCRagaJ6HwhQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 25781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 18 · 2026-05-22T07:25:43.776Z_

<details><summary>↩ Tool result · reported error · `toolu_01V3zyz82T5J1KMsYf9tYeap`</summary>

```text
File content (27034 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "094c4450-54c4-4976-95b7-5176c403f556",
  "tool_use_result": "Error: File content (27034 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T07:25:43.731Z_

<details><summary>↩ Tool result · `toolu_01FU5k1ojUCjfbQoDsgfxeHT`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "3eba2943-bb1e-4afb-9911-67516a1f4e01",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\nAll supplementary material is included in the appendix of the main paper.\n\n\\end{document}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_016PEeeYz7YyLN7sb6SdgWhg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "45f28ed9-7509-4607-857c-1930c7c97d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rq6TEEjGUCRagaJ6HwhQ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 25781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 21 · 2026-05-22T07:25:44.078Z_

<details><summary>↩ Tool result · `toolu_016PEeeYz7YyLN7sb6SdgWhg`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, MAVEN \citep{maven-2020}, Qwen3-32B \citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \citep{llama3-2024}, Gemini 2.5 Flash \citep{gemini-2025}, vLLM \citep{vllm-2023}, and all-MiniLM-L6-v2 \citep{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
34	
35	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
36	
37	Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Open-weight models are used under their respective licenses; Gemini 2.5 Flash is accessed via the Google API under its terms of service.
38	
39	\item \textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}
40	
41	Yes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.
42	
43	\item \textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}
44	
45	N/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.
46	
47	\item \textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}
48	
49	Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Gemini 2.5 Flash was additionally accessed via API for cross-architecture validation. Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerate}
78	
79	\subsection*{D \quad Human Annotators or Crowdworkers}
80	
81	\begin{enumerate}[label=\textbf{D\arabic*.},leftmargin=*,itemsep=4pt]
82	
83	\item \textbf{Did you report the full text of instructions given to participants?}
84	
85	N/A. No human annotation or crowdsourcing was conducted.
86	
87	\item \textbf{Did you report information about how you recruited and paid participants?}
88	
89	N/A.
90	
91	\item \textbf{Did you discuss whether and how consent was obtained?}
92	
93	N/A.
94	
95	\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
96	
97	N/A.
98	
99	\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
100	
101	N/A.
102	
103	\end{enumerate}
104	
105	\subsection*{E \quad AI-Assisted Research}
106	
107	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=*,itemsep=4pt]
108	
109	\item \textbf{Did you report the use of AI assistants?}
110	
111	Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
112	
113	\end{enumerate}
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "1c376efa-d23f-4b48-a548-a07a4045a92e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nYes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\citep{fewnerd-2021}, FewRel \\citep{fewrel-2018}, DocRED \\citep{docred-2019}, MAVEN \\citep{maven-2020}, Qwen3-32B \\citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}, Gemini 2.5 Flash \\citep{gemini-2025}, vLLM \\citep{vllm-2023}, and all-MiniLM-L6-v2 \\citep{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Open-weight models are used under their respective licenses; Gemini 2.5 Flash is accessed via the Google API under its terms of service.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Gemini 2.5 Flash was additionally accessed via API for cross-architecture validation. Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

Now let me read the appendix sections from main.tex and check for code/data mentions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "9673e58e-5c63-4821-94ff-15b643f410a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwuB3qFdYrv2832hdScNbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 28802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Kfvu7sC26DKjgHCCkLEjgC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "de3e6eec-95d1-46a9-8e84-84e396728d7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwuB3qFdYrv2832hdScNbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 28802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

### Tool result

_source line 24 · 2026-05-22T07:25:47.490Z_

<details><summary>↩ Tool result · `toolu_01Kfvu7sC26DKjgHCCkLEjgC`</summary>

```text
0	\documentclass[11pt]{article}
1	
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{enumitem}
13	\usepackage[normalem]{ulem}
14	\usepackage{listings}
15	
16	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
40	
41	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\,=\,0$) yields residual SD${}\,=\,0.88$\,pp, approximately 18--44\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\,pp) is far inside the $\pm 3$\,pp equivalence margin.
42	
43	\item \textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.
44	
45	\item \textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\ref{app:split-origin}).
46	\item \textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.
47	\end{enumerate}
48	
49	\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.
50	
51	\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.
52	
53	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
54	
55	\bibliography{references}
56	
57	\appendix
58	
59	\section{Additional Figures}
60	\label{sec:appendix_figures}
61	
62	\begin{table}[h]
63	\centering
64	\small
65	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
66	\label{tab:cross_model}
67	\begin{tabular}{lrr}
68	\toprule
69	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
70	\midrule
71	1 & 0.702 & 0.640 \\
72	64 & 0.273 & 0.304 \\
73	\midrule
74	Decline & $-$43\,pp & $-$34\,pp \\
75	\bottomrule
76	\end{tabular}
77	\end{table}
78	
79	\begin{table}[h]
80	\centering
81	\small
82	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
83	\label{tab:cross_model_bcs}
84	\resizebox{\columnwidth}{!}{%
85	\begin{tabular}{crrrrrr}
86	\toprule
87	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
88	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
89	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
90	\midrule
91	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
92	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
93	\bottomrule
94	\end{tabular}}
95	\end{table}
96	
97	\begin{table}[h]
98	\centering
99	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "7e920e4c-2cae-40b9-b13b-2efd82f1dac0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small",
      "numLines": 100,
      "startLine": 0,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_01H7UnqVPy4hBoujbVuQC18Z`</summary>

```json
{
  "pattern": "\\\\appendix|\\\\section\\{|\\\\subsection\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "e6a67bdf-16ad-46fb-a98a-66489d80a9b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwuB3qFdYrv2832hdScNbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 28802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

### Tool result

_source line 26 · 2026-05-22T07:25:48.784Z_

<details><summary>↩ Tool result · `toolu_01H7UnqVPy4hBoujbVuQC18Z`</summary>

```text
58:\appendix
60:\section{Additional Figures}
155:\section{SDGD Full Protocol and Results}
199:\subsection{Practical Routing Strategies on RE}
226:\section{Factorial Analysis and Separability Test}
262:\section{Within-Pool CI Details}
267:\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
308:\subsection{Partial Correlation: Controlling for Degree Centrality}
333:\subsection{NER BCS-Null Power Analysis}
338:\subsection{Bootstrap CI Robustness}
343:\subsection{Domain Distribution in Extreme-BCS Batches}
348:\section{Batch Composition Results}
372:\section{Prompt Version Sensitivity Analysis}
386:\subsection{Cross-Prompt-Variant BCS Correlation}
414:\section{BCS Aggregation Sensitivity}
440:\section{BCS-Controlled Detailed Results}
463:\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
533:\section{Within-Pool Analysis Methodology}
564:\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
591:\section{Pair-to-Batch Aggregation Simulation}
609:\section{BCS Independence from Type Composition}
614:\section{SCS vs.\ Simple Baselines}
642:\section{Split-Origin Covariate Analysis}
656:\section{Cross-Seed Variance Decomposition}
681:\section{Cross-Domain Connections}
686:\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
726:\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
777:\section{Few-Shot Prompting and Confusability}
802:\section{Qualitative Error Analysis}
871:\section{Schema Label Renaming Experiment}
893:\section{Relaxed Matching Evaluation (NER)}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "5ec1e493-0858-44bb-9783-b5bbf4054502",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "58:\\appendix\n60:\\section{Additional Figures}\n155:\\section{SDGD Full Protocol and Results}\n199:\\subsection{Practical Routing Strategies on RE}\n226:\\section{Factorial Analysis and Separability Test}\n262:\\section{Within-Pool CI Details}\n267:\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n308:\\subsection{Partial Correlation: Controlling for Degree Centrality}\n333:\\subsection{NER BCS-Null Power Analysis}\n338:\\subsection{Bootstrap CI Robustness}\n343:\\subsection{Domain Distribution in Extreme-BCS Batches}\n348:\\section{Batch Composition Results}\n372:\\section{Prompt Version Sensitivity Analysis}\n386:\\subsection{Cross-Prompt-Variant BCS Correlation}\n414:\\section{BCS Aggregation Sensitivity}\n440:\\section{BCS-Controlled Detailed Results}\n463:\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n533:\\section{Within-Pool Analysis Methodology}\n564:\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n591:\\section{Pair-to-Batch Aggregation Simulation}\n609:\\section{BCS Independence from Type Composition}\n614:\\section{SCS vs.\\ Simple Baselines}\n642:\\section{Split-Origin Covariate Analysis}\n656:\\section{Cross-Seed Variance Decomposition}\n681:\\section{Cross-Domain Connections}\n686:\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n726:\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n777:\\section{Few-Shot Prompting and Confusability}\n802:\\section{Qualitative Error Analysis}\n871:\\section{Schema Label Renaming Experiment}\n893:\\section{Relaxed Matching Evaluation (NER)}",
    "numLines": 31
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01KZRxE5iWMSujeuSE5hZp5V`</summary>

```json
{
  "pattern": "code.*(available|release|github|repo)|anonymous\\.4open|supplementary|upon acceptance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "5e7e9f31-aa4b-4431-bd4a-c27fb1941282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwuB3qFdYrv2832hdScNbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2805,
      "cache_read_input_tokens": 28802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2805
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

### Tool result

_source line 28 · 2026-05-22T07:25:50.239Z_

<details><summary>↩ Tool result · `toolu_01KZRxE5iWMSujeuSE5hZp5V`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "ac8ad6fd-c760-48de-9642-924dc81bc0ff",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01G7qRvRLwevyaidpuiwJnzs`</summary>

```json
{
  "pattern": "code|release|github|repo|anonymous|supplementary|upon acceptance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-i": true,
  "glob": "*.tex",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "2eeaa52a-680c-41ad-8e2d-bc50fd198e5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qzrg4AA5eWzRJNzHd86iG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 31607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3628
      },
      "output_tokens": 50,
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

_source line 30 · 2026-05-22T07:25:54.274Z_

<details><summary>↩ Tool result · `toolu_01G7qRvRLwevyaidpuiwJnzs`</summary>

```text
docs/paper/related_work.tex:6:[Omitted long matching line]
docs/paper/main.tex:19:\author{Anonymous}
docs/paper/main.tex:52:[Omitted long matching line]
docs/paper/main.tex:197:Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), and both modes produce lower F1 (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
docs/paper/main.tex:254:[Omitted long matching line]
docs/paper/main.tex:280:Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
docs/paper/main.tex:304:[Omitted long matching line]
docs/paper/main.tex:341:[Omitted long matching line]
docs/paper/main.tex:375:We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
docs/paper/main.tex:381:[Omitted long matching line]
docs/paper/main.tex:491:Table~\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \emph{identical} accuracy; the two exceptions (high\_5, high\_11) differ by a single sample (1/96 $\approx$ 1.04\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\%), confirming that the model generates valid type labels even without format constraints.
docs/paper/main.tex:800:The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
docs/paper/checklist.tex:23:Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
docs/paper/checklist.tex:37:Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Open-weight models are used under their respective licenses; Gemini 2.5 Flash is accessed via the Google API under its terms of service.
docs/paper/checklist.tex:49:Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
docs/paper/checklist.tex:51:\item \textbf{Did you report relevant statistics for your dataset(s)?}
docs/paper/checklist.tex:53:Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
docs/paper/checklist.tex:61:\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
docs/paper/checklist.tex:67:Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
docs/paper/checklist.tex:69:\item \textbf{Did you report descriptive statistics about your results?}
docs/paper/checklist.tex:71:Yes. All key metrics include 95\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
docs/paper/checklist.tex:73:\item \textbf{Did you report implementation details, e.g., versions of packages?}
docs/paper/checklist.tex:75:Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
docs/paper/checklist.tex:83:\item \textbf{Did you report the full text of instructions given to participants?}
docs/paper/checklist.tex:87:\item \textbf{Did you report information about how you recruited and paid participants?}
docs/paper/checklist.tex:95:\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
docs/paper/checklist.tex:99:\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
docs/paper/checklist.tex:109:\item \textbf{Did you report the use of AI assistants?}
docs/paper/checklist.tex:111:Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
docs/paper/experimental_setup.tex:19:[Omitted long matching line]

[Showing results with pagination = limit: 30]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "48e5772c-f647-4584-98b3-5535b329b2ba",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:6:[Omitted long matching line]\ndocs/paper/main.tex:19:\\author{Anonymous}\ndocs/paper/main.tex:52:[Omitted long matching line]\ndocs/paper/main.tex:197:Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\ndocs/paper/main.tex:254:[Omitted long matching line]\ndocs/paper/main.tex:280:Table~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\ndocs/paper/main.tex:304:[Omitted long matching line]\ndocs/paper/main.tex:341:[Omitted long matching line]\ndocs/paper/main.tex:375:We assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\ndocs/paper/main.tex:381:[Omitted long matching line]\ndocs/paper/main.tex:491:Table~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\ndocs/paper/main.tex:800:The 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\ndocs/paper/checklist.tex:23:Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.\ndocs/paper/checklist.tex:37:Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Open-weight models are used under their respective licenses; Gemini 2.5 Flash is accessed via the Google API under its terms of service.\ndocs/paper/checklist.tex:49:Yes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\ndocs/paper/checklist.tex:51:\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\ndocs/paper/checklist.tex:53:Yes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\ndocs/paper/checklist.tex:61:\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\ndocs/paper/checklist.tex:67:Yes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\ndocs/paper/checklist.tex:69:\\item \\textbf{Did you report descriptive statistics about your results?}\ndocs/paper/checklist.tex:71:Yes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\ndocs/paper/checklist.tex:73:\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\ndocs/paper/checklist.tex:75:Yes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\ndocs/paper/checklist.tex:83:\\item \\textbf{Did you report the full text of instructions given to participants?}\ndocs/paper/checklist.tex:87:\\item \\textbf{Did you report information about how you recruited and paid participants?}\ndocs/paper/checklist.tex:95:\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\ndocs/paper/checklist.tex:99:\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\ndocs/paper/checklist.tex:109:\\item \\textbf{Did you report the use of AI assistants?}\ndocs/paper/checklist.tex:111:Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\ndocs/paper/experimental_setup.tex:19:[Omitted long matching line]",
    "numLines": 30,
    "appliedLimit": 30
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_012oChF1bTLXjrZeFXJHZiME`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 100,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "db23d5ad-d2cc-431e-897a-46ebc25f150c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qzrg4AA5eWzRJNzHd86iG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 31607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3628
      },
      "output_tokens": 50,
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

_source line 32 · 2026-05-22T07:25:54.845Z_

<details><summary>↩ Tool result · `toolu_012oChF1bTLXjrZeFXJHZiME`</summary>

```text
100	\small
101	\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
102	\label{tab:cross_model_ner_null}
103	\begin{tabular}{lcl}
104	\toprule
105	\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
106	\midrule
107	Qwen3-32B & $0.004$ ($p = 0.94$) & Null \\
108	LLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\rlap{$^\dagger$} & Null \\
109	LLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\rlap{$^\ddagger$} & Null \\
110	Gemini 2.5 Flash & --- & Not tested \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\begin{table}[h]
116	\centering
117	\small
118	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}
119	\label{tab:error_taxonomy}
120	\resizebox{\columnwidth}{!}{%
121	\begin{tabular}{llrrrrrrr}
122	\toprule
123	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
124	\cmidrule(lr){3-7}
125	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
126	\midrule
127	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
128	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
129	DocRE & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
130	\midrule
131	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
132	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
133	DocRE & Missed & --- & 28.1\% & 22.6\% & 21.6\% & 16.2\% & --- & --- \\
134	\bottomrule
135	\end{tabular}}
136	\end{table}
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\dagger$LLaMA-70B has only 20 batches with 17.4\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}
142	\label{tab:cross_model_error_taxonomy}
143	\begin{tabular}{lrcc}
144	\toprule
145	\textbf{Model} & $n$ & $\rho$ & $p$ \\
146	\midrule
147	Qwen3-32B & 154 & 0.954 & ${<}\,0.001$ \\
148	Gemini 2.5 Flash & 60 & 0.821 & ${<}\,0.001$ \\
149	LLaMA-3.1-8B & 54 & 0.430 & 0.001 \\
150	LLaMA-3.1-70B$^\dagger$ & 20 & $-$0.086 & 0.719 \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	\section{SDGD Full Protocol and Results}
156	\label{sec:appendix_sdgd}
157	
158	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.
159	
160	\begin{enumerate}[leftmargin=*,itemsep=2pt]
161	\item Compute pairwise SCS matrix $S_{ij} = \cos(\text{embed}(t_i), \text{embed}(t_j))$.
162	\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \tau$.
163	\item Apply greedy graph coloring (\textsc{largest\_first}) to assign each type a color $c(t)$.
164	\item For each color $k$, form batch $B_k = \{t : c(t) = k\}$ and run extraction on all test instances.
165	\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).
166	\end{enumerate}
167	Oracle routing (Table~\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\% vs.\ 50.4\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.
168	
169	We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
170	
171	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
177	\label{tab:sdgd_results}
178	\resizebox{\columnwidth}{!}{%
179	\begin{tabular}{lrccc}
180	\toprule
181	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
182	\midrule
183	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
184	\midrule
185	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
186	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
187	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
188	\midrule
189	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
190	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
191	\bottomrule
192	\end{tabular}}
193	\end{table}
194	
195	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.
196	
197	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), and both modes produce lower F1 (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
198	
199	\subsection{Practical Routing Strategies on RE}
200	\label{sec:appendix_routing}
201	
202	We evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.
203	
204	\begin{table}[h]
205	\centering
206	\small
207	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\%.}
208	\label{tab:routing_strategies}
209	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lrr@{}}
210	\toprule
211	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
212	\midrule
213	Oracle (gold label) & 72.4\% & +22.0\,pp \\
214	\midrule
215	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
216	None-aware & 36.5\% & $-$14.0\,pp \\
217	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
218	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
219	Random & 14.7\% & $-$35.7\,pp \\
220	\midrule
221	Single-pass (no decomposition) & 50.4\% & --- \\
222	\bottomrule
223	\end{tabular}}
224	\end{table}
225	
226	\section{Factorial Analysis and Separability Test}
227	\label{sec:appendix_factorial}
228	
229	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.
230	
231	A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
232	
233	\paragraph{Equivalence margin justification.}
234	We set the $\pm 3$\,pp margin based on three converging anchors. \emph{External}: evaluation variance in IE benchmarks typically spans 2--5\,pp across random seeds, prompt variations, and data splits \citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \emph{Internal}: $0.5 \times$ within-cell SD ($= 2.3$\,pp) corresponds to Cohen's $d \approx 0.5$ (medium effect threshold; \citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\,pp (\S\ref{sec:practical_magnitude})---an interaction exceeding 3\,pp would represent ${>}130\%$ amplification. \emph{Sensitivity}: Table~\ref{tab:tost_sensitivity} shows equivalence holds from $\pm 2$\,pp ($p = 0.047$) through $\pm 5$\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.
235	
236	\begin{table}[h]
237	\centering
238	\small
239	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$); the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
240	\label{tab:tost_sensitivity}
241	\begin{tabular}{crrl}
242	\toprule
243	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
244	\midrule
245	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
246	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
247	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
248	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
249	\bottomrule
250	\end{tabular}
251	\end{table}
252	
253	\paragraph{Logit-scale sensitivity.}
254	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\pm 3$\,pp and $p = 0.026$ at $\pm 3.5$\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.
255	
256	\paragraph{DocRED factorial (expanded).}
257	With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \times 2$ factorial (count $\in \{16, 32\}$, BCS median split) yields an apparent interaction ($-$9.4\,pp, 95\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\,pp at count 16 but $-$15.7\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\ 0.38), limiting achievable extremes.
258	
259	\paragraph{Range-matched robustness check.}
260	To control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\,pp to 9.37\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\,pp. The interaction drops from 7.52\,pp (95\% CI [1.49, 12.83]) to 0.93\,pp (95\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\rho = -0.65$ at count 16, $\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\,pp at 80\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\,pp) interaction.
261	
262	\section{Within-Pool CI Details}
263	\label{sec:appendix_within_pool}
264	
265	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
266	
267	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
268	\label{sec:appendix_residualized_bcs}
269	
270	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
271	
272	\paragraph{Confound identification.}
273	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
274	\begin{itemize}[itemsep=2pt,leftmargin=*]
275	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.
276	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.
277	\end{itemize}
278	
279	\paragraph{Partial correlation results.}
280	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
281	
282	\begin{table}[h]
283	\centering
284	\small
285	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
286	\label{tab:residualized_bcs}
287	\resizebox{\columnwidth}{!}{%
288	\begin{tabular}{llcccc}
289	\toprule
290	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
291	\midrule
292	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
293	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
294	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
295	\midrule
296	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
297	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
298	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
299	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "f008216c-4809-4910-b3e0-5c910db702a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule",
      "numLines": 200,
      "startLine": 100,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

Let me continue reading the rest of the appendix sections and check for dataset citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "c0e6d2e8-1640-45f2-b715-497d9dafa7f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VopwY5SsJAymJAEnGuawwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8404,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8404
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01C4C1hVNk2Vo12a87AZuwnW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 300,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "dc5b2d88-5cef-438e-8643-96f144595a8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VopwY5SsJAymJAEnGuawwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8404,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8404
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

### Tool result

_source line 35 · 2026-05-22T07:26:00.201Z_

<details><summary>↩ Tool result · `toolu_01C4C1hVNk2Vo12a87AZuwnW`</summary>

```text
300	\end{tabular}}
301	\end{table}
302	
303	\paragraph{Interpretation.}
304	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
305	
306	Under joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
307	
308	\subsection{Partial Correlation: Controlling for Degree Centrality}
309	\label{sec:appendix_partial_corr}
310	
311	To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).
312	
313	\begin{table}[h]
314	\centering
315	\small
316	\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\,=\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\,=\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}
317	\label{tab:partial_corr}
318	\begin{tabular}{lrrrrr}
319	\toprule
320	\textbf{Dataset} & \textbf{$n$} & \textbf{$r_{\text{zero}}$} & \textbf{$r_{\text{partial}}$} & \textbf{$p_{\text{partial}}$} & \textbf{VIF} \\
321	\midrule
322	FewRel & 204 & $-$0.570 & $-$0.537 & ${<}\,0.001$ & 1.18 \\
323	DocRED & 110 & $-$0.760 & $-$0.348 & ${<}\,0.001$ & 50.9 \\
324	\bottomrule
325	\end{tabular}
326	\end{table}
327	
328	As Table~\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
329	
330	\paragraph{Ridge regression under multicollinearity.}
331	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\,\approx\,$50.9). The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$ ($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for \emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at $\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.
332	
333	\subsection{NER BCS-Null Power Analysis}
334	\label{sec:appendix_ner_power}
335	
336	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
337	
338	\subsection{Bootstrap CI Robustness}
339	\label{sec:appendix_bootstrap_ci}
340	
341	Because batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\in \{0.1, \ldots, 0.9\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\%$ to $+6\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.
342	
343	\subsection{Domain Distribution in Extreme-BCS Batches}
344	\label{sec:appendix_domain_distribution}
345	
346	We classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\%) and creative work (25.5\%), while high-BCS batches concentrate on science/taxonomy (49.5\%) and event/temporal (26.0\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.
347	
348	\section{Batch Composition Results}
349	\label{sec:appendix_batch_composition}
350	
351	\begin{table}[h]
352	\centering
353	\small
354	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
355	\label{tab:batch_composition}
356	\resizebox{\columnwidth}{!}{%
357	\begin{tabular}{@{}lcc@{}}
358	\toprule
359	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
360	\midrule
361	Single-pass (80 types) & 0.504 & 0.557 \\
362	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
363	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
364	\bottomrule
365	\end{tabular}}
366	\end{table}
367	
368	See the accompanying discussion in \S\ref{sec:sdgd}.
369	
370	\input{prompt_appendix}
371	
372	\section{Prompt Version Sensitivity Analysis}
373	\label{sec:appendix_prompt_sensitivity}
374	
375	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
376	
377	\paragraph{RE (FewRel).}
378	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (95\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
379	
380	\paragraph{NER (Few-NERD).}
381	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
382	
383	\paragraph{Interpretation.}
384	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
385	
386	\subsection{Cross-Prompt-Variant BCS Correlation}
387	\label{sec:appendix_prompt_variants}
388	
389	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\ref{tab:prompt_variants}).
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
395	\label{tab:prompt_variants}
396	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrr}
397	\toprule
398	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
399	\midrule
400	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
401	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
402	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
403	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
404	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
405	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
406	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
407	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
413	
414	\section{BCS Aggregation Sensitivity}
415	\label{sec:appendix_bcs_sensitivity}
416	
417	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\ref{tab:bcs_aggregation}).
418	
419	\begin{table}[h]
420	\centering
421	\small
422	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
423	\label{tab:bcs_aggregation}
424	\resizebox{\columnwidth}{!}{%
425	\begin{tabular}{llcccc}
426	\toprule
427	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
428	\midrule
429	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
430	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
431	\midrule
432	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
433	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
434	\bottomrule
435	\end{tabular}}
436	\end{table}
437	
438	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
439	
440	\section{BCS-Controlled Detailed Results}
441	\label{app:bcs-controlled-table}
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
447	\label{tab:bcs_controlled}
448	\resizebox{\columnwidth}{!}{%
449	\begin{tabular}{lcrrrr}
450	\toprule
451	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
452	\midrule
453	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
454	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
455	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
456	\bottomrule
457	\end{tabular}}
458	\end{table}
459	
460	\paragraph{Adjusted $R^2$ and confidence intervals.}
461	DocRED regressions (\S\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\% CI [0.47, 0.75]). The small shrinkage ($\Delta R^2 \leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.
462	
463	\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
464	\label{app:format-independence}
465	
466	To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\ref{tab:format_independence}).
467	
468	\begin{table}[h]
469	\centering
470	\small
471	\caption{Paired comparison of constrained vs.\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\Delta = -0.08$\,pp), ruling out a format-driven accuracy shift.}
472	\label{tab:format_independence}
473	\begin{tabular}{lrr}
474	\toprule
475	\textbf{Metric} & \textbf{Constrained} & \textbf{Unconstrained} \\
476	\midrule
477	Mean accuracy & 79.5\% & 79.6\% \\
478	Pearson $r$ (BCS vs.\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\
479	Spearman $\rho$ (BCS vs.\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\
480	\midrule
481	\multicolumn{3}{l}{\textit{Paired Fisher $z$-test for correlation equality}} \\
482	\quad Pearson $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
483	\quad Spearman $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
484	\bottomrule
485	\end{tabular}
486	\end{table}
487	
488	The near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\sim}2$\,pp; \S\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.
489	
490	\paragraph{Per-batch paired results.}
491	Table~\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \emph{identical} accuracy; the two exceptions (high\_5, high\_11) differ by a single sample (1/96 $\approx$ 1.04\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\%), confirming that the model generates valid type labels even without format constraints.
492	
493	\begin{table}[h]
494	\centering
495	\small
496	\caption{Per-batch accuracy (\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\Delta = -1.04$\,pp). L = low-BCS, H = high-BCS.}
497	\label{tab:format_perbatch}
498	\resizebox{\columnwidth}{!}{%
499	\begin{tabular}{lcrrrr}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "4418d237-6386-404b-8169-379e733cc3e3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}",
      "numLines": 200,
      "startLine": 300,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_0113LNxVMDpvwnegWBomNUzD`</summary>

```json
{
  "pattern": "\\\\section\\{|\\\\label\\{sec:|\\\\label\\{app:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "head_limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "7f29a14c-5b5a-4359-a9b3-6254184641ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VopwY5SsJAymJAEnGuawwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8404,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8404
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

### Tool result

_source line 37 · 2026-05-22T07:26:01.270Z_

<details><summary>↩ Tool result · `toolu_0113LNxVMDpvwnegWBomNUzD`</summary>

```text
60:\section{Additional Figures}
61:\label{sec:appendix_figures}
155:\section{SDGD Full Protocol and Results}
156:\label{sec:appendix_sdgd}
200:\label{sec:appendix_routing}
226:\section{Factorial Analysis and Separability Test}
227:\label{sec:appendix_factorial}
262:\section{Within-Pool CI Details}
263:\label{sec:appendix_within_pool}
267:\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
268:\label{sec:appendix_residualized_bcs}
309:\label{sec:appendix_partial_corr}
334:\label{sec:appendix_ner_power}
339:\label{sec:appendix_bootstrap_ci}
344:\label{sec:appendix_domain_distribution}
348:\section{Batch Composition Results}
349:\label{sec:appendix_batch_composition}
372:\section{Prompt Version Sensitivity Analysis}
373:\label{sec:appendix_prompt_sensitivity}
387:\label{sec:appendix_prompt_variants}
414:\section{BCS Aggregation Sensitivity}
415:\label{sec:appendix_bcs_sensitivity}
440:\section{BCS-Controlled Detailed Results}
441:\label{app:bcs-controlled-table}
463:\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
464:\label{app:format-independence}
533:\section{Within-Pool Analysis Methodology}
534:\label{app:within-pool-method}
564:\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
565:\label{app:scs-ablation}
588:\label{app:scs-heldout-validation}
591:\section{Pair-to-Batch Aggregation Simulation}
592:\label{app:aggregation-sim}
609:\section{BCS Independence from Type Composition}
610:\label{app:bcs-composition}
614:\section{SCS vs.\ Simple Baselines}
615:\label{app:scs-baselines}
642:\section{Split-Origin Covariate Analysis}
643:\label{app:split-origin}
656:\section{Cross-Seed Variance Decomposition}
657:\label{app:variance-decomposition}
681:\section{Cross-Domain Connections}
682:\label{app:cross-domain}
686:\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
687:\label{sec:appendix_cross_model_70b}
726:\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
727:\label{sec:appendix_cross_model_gemini}
777:\section{Few-Shot Prompting and Confusability}
778:\label{sec:appendix_fewshot_bcs}
802:\section{Qualitative Error Analysis}
803:\label{app:error-analysis}
871:\section{Schema Label Renaming Experiment}
872:\label{app:renaming}
893:\section{Relaxed Matching Evaluation (NER)}
894:\label{app:relaxed-matching}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "2e335e59-7985-40db-aca8-4dc34b86a664",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "60:\\section{Additional Figures}\n61:\\label{sec:appendix_figures}\n155:\\section{SDGD Full Protocol and Results}\n156:\\label{sec:appendix_sdgd}\n200:\\label{sec:appendix_routing}\n226:\\section{Factorial Analysis and Separability Test}\n227:\\label{sec:appendix_factorial}\n262:\\section{Within-Pool CI Details}\n263:\\label{sec:appendix_within_pool}\n267:\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n268:\\label{sec:appendix_residualized_bcs}\n309:\\label{sec:appendix_partial_corr}\n334:\\label{sec:appendix_ner_power}\n339:\\label{sec:appendix_bootstrap_ci}\n344:\\label{sec:appendix_domain_distribution}\n348:\\section{Batch Composition Results}\n349:\\label{sec:appendix_batch_composition}\n372:\\section{Prompt Version Sensitivity Analysis}\n373:\\label{sec:appendix_prompt_sensitivity}\n387:\\label{sec:appendix_prompt_variants}\n414:\\section{BCS Aggregation Sensitivity}\n415:\\label{sec:appendix_bcs_sensitivity}\n440:\\section{BCS-Controlled Detailed Results}\n441:\\label{app:bcs-controlled-table}\n463:\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n464:\\label{app:format-independence}\n533:\\section{Within-Pool Analysis Methodology}\n534:\\label{app:within-pool-method}\n564:\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n565:\\label{app:scs-ablation}\n588:\\label{app:scs-heldout-validation}\n591:\\section{Pair-to-Batch Aggregation Simulation}\n592:\\label{app:aggregation-sim}\n609:\\section{BCS Independence from Type Composition}\n610:\\label{app:bcs-composition}\n614:\\section{SCS vs.\\ Simple Baselines}\n615:\\label{app:scs-baselines}\n642:\\section{Split-Origin Covariate Analysis}\n643:\\label{app:split-origin}\n656:\\section{Cross-Seed Variance Decomposition}\n657:\\label{app:variance-decomposition}\n681:\\section{Cross-Domain Connections}\n682:\\label{app:cross-domain}\n686:\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n687:\\label{sec:appendix_cross_model_70b}\n726:\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n727:\\label{sec:appendix_cross_model_gemini}\n777:\\section{Few-Shot Prompting and Confusability}\n778:\\label{sec:appendix_fewshot_bcs}\n802:\\section{Qualitative Error Analysis}\n803:\\label{app:error-analysis}\n871:\\section{Schema Label Renaming Experiment}\n872:\\label{app:renaming}\n893:\\section{Relaxed Matching Evaluation (NER)}\n894:\\label{app:relaxed-matching}",
    "numLines": 55
  }
}
```

</details>

---

### Assistant

_source line 38_

Now let me check for dataset citations and the remaining appendix sections, plus the prompt appendix and experimental setup for code/data mentions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "ed305cd6-4032-4803-ad55-f2f1c799e1f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tuens48YJzumMZ5qGdqqgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7877,
      "cache_read_input_tokens": 43639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7877
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

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01VTsTWEKhGmMCSvC1dL68Wm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 500,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "1f2b2979-3a64-4f29-8ec3-a5ba2a1bf669",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tuens48YJzumMZ5qGdqqgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7877,
      "cache_read_input_tokens": 43639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7877
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

### Tool result

_source line 40 · 2026-05-22T07:26:06.754Z_

<details><summary>↩ Tool result · `toolu_01VTsTWEKhGmMCSvC1dL68Wm`</summary>

```text
500	\toprule
501	\textbf{Batch} & \textbf{Group} & \textbf{BCS} & \textbf{Constr.} & \textbf{Unconstr.} & \textbf{$\Delta$} \\
502	\midrule
503	low\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\
504	low\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\
505	low\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\
506	low\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\
507	low\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\
508	low\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\
509	low\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\
510	low\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\
511	low\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\
512	low\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\
513	low\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\
514	low\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\
515	low\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\
516	\midrule
517	high\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\
518	high\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\
519	high\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\
520	high\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\
521	high\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\
522	high\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\
523	high\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\
524	high\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\
525	high\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\
526	high\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\
527	high\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\
528	high\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\
529	\bottomrule
530	\end{tabular}}
531	\end{table}
532	
533	\section{Within-Pool Analysis Methodology}
534	\label{app:within-pool-method}
535	
536	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
537	
538	\begin{table}[h]
539	\centering
540	\small
541	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
542	\label{tab:within_pool}
543	\resizebox{\columnwidth}{!}{%
544	\begin{tabular}{lrrrrrrr}
545	\toprule
546	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
547	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
548	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
549	\midrule
550	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
551	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
552	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
553	\midrule
554	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
555	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
556	\bottomrule
557	\end{tabular}}
558	\end{table}
559	
560	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
561	
562	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
563	
564	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
565	\label{app:scs-ablation}
566	
567	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
568	
569	\begin{table}[h]
570	\centering
571	\small
572	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates that definitions provide no systematic benefit.}
573	\label{tab:scs-ablation}
574	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
575	\toprule
576	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
577	\midrule
578	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
579	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
580	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
581	\bottomrule
582	\end{tabular}}
583	\end{table}
584	
585	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
586	
587	\paragraph{Held-out validation.}
588	\label{app:scs-heldout-validation}
589	From the 80-type confusion matrix, we extract the $\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.
590	
591	\section{Pair-to-Batch Aggregation Simulation}
592	\label{app:aggregation-sim}
593	
594	The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\S\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.
595	
596	\paragraph{Setup.} We examine whether the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
597	
598	\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
599	
600	\paragraph{Unconditional baseline.}
601	When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\text{SNR} \times \text{EF} / (\text{SNR} \times \text{EF} + 1) = 0.042$ with the same effective factor $\text{EF} = 3.35$. This ${\sim}5\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \emph{active} confusable pairs, not uniform contributions from all pairs.
602	
603	\paragraph{Sensitivity to $\rho$.}
604	The inter-pair SCS correlation $\rho = 0.35$ is estimated from pairs sharing a common type. At $\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \approx 0.22$, still matching the observed value; at $\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.
605	
606	\paragraph{Non-independence and ecological inference.}
607	Types within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\text{--}0.578$ (\S\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.
608	
609	\section{BCS Independence from Type Composition}
610	\label{app:bcs-composition}
611	
612	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.
613	
614	\section{SCS vs.\ Simple Baselines}
615	\label{app:scs-baselines}
616	
617	Table~\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.
618	
619	\begin{table}[h]
620	\centering
621	\small
622	\caption{Pairwise confusion prediction: SCS vs.\ simple baselines. Spearman $\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\dagger$42\% of pairs lack WordNet coverage.}
623	\label{tab:scs_baselines}
624	\resizebox{\columnwidth}{!}{%
625	\begin{tabular}{llrr}
626	\toprule
627	\textbf{Dataset} & \textbf{Metric} & \textbf{Spearman $\rho$} & \textbf{$p$} \\
628	\midrule
629	FewRel & SCS (embedding) & \textbf{0.218} & $< 0.001$ \\
630	(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\
631	& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\
632	& Levenshtein & 0.016 & 0.363 (n.s.) \\
633	\midrule
634	Few-NERD & SCS (embedding) & \textbf{0.166} & $< 0.001$ \\
635	(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\
636	& Same-parent (prefix) & 0.146 & $< 0.001$ \\
637	& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\dagger$ \\
638	\bottomrule
639	\end{tabular}}
640	\end{table}
641	
642	\section{Split-Origin Covariate Analysis}
643	\label{app:split-origin}
644	
645	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
646	
647	\paragraph{Method.}  Across 213 multi-type batches ($k \geq 2$) from the batch-composition experiment (\S\ref{sec:sdgd}) and the factorial design (\S\ref{sec:bcs_controlled}), we compute $\texttt{train\_origin\_ratio} = n_{\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:
648	{\small\begin{equation*}
649	\text{acc} = \beta_0 + \beta_{\text{BCS}} \!\cdot\! \text{BCS} + \beta_{\text{orig}} \!\cdot\! \text{train\_origin\_ratio} + \varepsilon
650	\end{equation*}}
651	
652	\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 0.001$ (vs.\ $\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
653	
654	Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.
655	
656	\section{Cross-Seed Variance Decomposition}
657	\label{app:variance-decomposition}
658	
659	\begin{table}[h]
660	\centering
661	\small
662	\caption{Variance decomposition on FewRel (3 seeds $\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}
663	\label{tab:variance_decomposition}
664	\begin{tabular}{rrrr}
665	\toprule
666	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
667	\midrule
668	4 & 0.0889 & 0.0122 & 53.5 \\
669	8 & 0.0820 & 0.0098 & 70.0 \\
670	16 & 0.0626 & 0.0270 & 5.4 \\
671	32 & 0.0462 & 0.0091 & 26.0 \\
672	40 & 0.0421 & 0.0019 & 474.4 \\
673	64 & 0.0245 & 0.0022 & 119.8 \\
674	80 & 0.0001 & 0.0088 & $<$0.1 \\
675	\bottomrule
676	\end{tabular}
677	\end{table}
678	
679	Table~\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\,=\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\,pp, likely attributable to FP8 quantization non-determinism).
680	
681	\section{Cross-Domain Connections}
682	\label{app:cross-domain}
683	
684	The schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
685	
686	\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
687	\label{sec:appendix_cross_model_70b}
688	
689	To test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
690	
691	\begin{table}[h]
692	\centering
693	\small
694	\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\to$80): $-$30.7\,pp (70B) vs.\ $-$30.1\,pp (32B). NER decline (count 2$\to$22): $-$7.1\,pp (70B) vs.\ $-$23.6\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}
695	\label{tab:cross_model_70b}
696	\begin{tabular}{lrr}
697	\toprule
698	\textbf{Count} & \textbf{LLaMA-70B} & \textbf{Qwen3-32B} \\
699	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "76d2b462-b2f5-4d2e-9bc6-dd6817664384",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule",
      "numLines": 200,
      "startLine": 500,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01YPgUhzoPPxGYBBTrgR6bFi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "5c22f20c-9413-42a9-aa4f-38869c41af4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tuens48YJzumMZ5qGdqqgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7877,
      "cache_read_input_tokens": 43639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7877
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

### Tool result

_source line 42 · 2026-05-22T07:26:07.493Z_

<details><summary>↩ Tool result · `toolu_01YPgUhzoPPxGYBBTrgR6bFi`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set. The task is formulated identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\S\ref{sec:centrality_confound}).
20	
21	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{llrrlll}
28	\toprule
29	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
30	\midrule
31	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
32	FewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
33	DocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\
34	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\dagger$Trigger mentions across 8{,}042 sentences.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	\looseness=-1
45	We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
46	{\small
47	\[
48	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
49	\]
50	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "d0dd7255-3e14-4e7a-a337-4232ae6e1032",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set. The task is formulated identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\n\\looseness=-1\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 100
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

Let me check the remaining appendix sections and look for the "code available" / "upon acceptance" text in the paper body.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "01b5f233-ca71-4789-8123-7b229c6f2434",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnDMMeQwDUMQAXRmqJ2psn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8311,
      "cache_read_input_tokens": 51516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8311
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

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01382Tnc3vgzvBeZ5LuzjtBn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 700,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "47997e7c-a3a8-4b3d-8629-b2955f5b8f08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnDMMeQwDUMQAXRmqJ2psn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8311,
      "cache_read_input_tokens": 51516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8311
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

### Tool result

_source line 45 · 2026-05-22T07:26:12.655Z_

<details><summary>↩ Tool result · `toolu_01382Tnc3vgzvBeZ5LuzjtBn`</summary>

```text
700	\multicolumn{3}{l}{\textit{RE (FewRel, Classification Accuracy)}} \\
701	8  & 0.757 & 0.805 \\
702	16 & 0.685 & 0.719 \\
703	32 & 0.601 & 0.652 \\
704	64 & 0.504 & 0.539 \\
705	80 & 0.450 & 0.504 \\
706	\midrule
707	\multicolumn{3}{l}{\textit{NER (Few-NERD, Text+Type Match Recall)}} \\
708	2  & 0.323 & 0.515 \\
709	6  & 0.300 & 0.399 \\
710	12 & 0.278 & 0.318 \\
711	22 & 0.252 & 0.279 \\
712	44 & 0.297 & 0.309 \\
713	66 & 0.273 & 0.407 \\
714	\bottomrule
715	\end{tabular}
716	\end{table}
717	
718	Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.
719	
720	On NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\to$0.252, $-$7.1\,pp; Qwen3: 0.515$\to$0.279, $-$23.6\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).
721	
722	For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.
723	
724	In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
725	
726	\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
727	\label{sec:appendix_cross_model_gemini}
728	
729	We validate both dimensions on a proprietary model, Gemini 2.5 Flash \citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
730	
731	\begin{table}[h]
732	\centering
733	\small
734	\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\rho = -1.0$ for both on counts 4--32). $^\dagger$Count 64: Gemini based on 11/25 batches (partial).}
735	\label{tab:cross_model_gemini}
736	\begin{tabular}{lrr}
737	\toprule
738	\textbf{Count} & \textbf{Gemini Flash} & \textbf{Qwen3-32B} \\
739	\midrule
740	1  & 0.827 & --- \\
741	4  & 0.873 & 0.870 \\
742	8  & 0.820 & 0.805 \\
743	16 & 0.787 & 0.719 \\
744	32 & 0.739 & 0.652 \\
745	64$^\dagger$ & 0.637 & 0.539 \\
746	\bottomrule
747	\end{tabular}
748	\end{table}
749	
750	Table~\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\rho = -1.0$). Including count 1, the Gemini count curve yields $\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\,pp from count 4 to 32) than for Qwen3 ($-$21.8\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\,pp at count 4 vs.\ 8.7\,pp at count 32, 9.8\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.
751	
752	\paragraph{Dimension~2: BCS-controlled confusability.}
753	We replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).
754	
755	At count 8, low-BCS batches achieve 90.5\% vs.\ high-BCS 72.9\% ($\Delta = -17.6$\,pp, 95\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\% vs.\ 82.3\%) leaves less room for degradation.
756	
757	Table~\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.
758	
759	\begin{table}[h]
760	\centering
761	\small
762	\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}
763	\label{tab:cross_model_bcs_summary}
764	\begin{tabular}{llrrrr}
765	\toprule
766	\textbf{Model} & \textbf{Count} & \textbf{Low BCS} & \textbf{High BCS} & \textbf{$\Delta$} & \textbf{95\% CI} \\
767	\midrule
768	Qwen3-32B     & 8  & 82.3\% & 51.0\% & $-$31.2\,pp & --- \\
769	Qwen3-32B     & 16 & 82.8\% & 51.6\% & $-$31.2\,pp & --- \\
770	Llama-8B      & 8  & 78.1\% & 51.0\% & $-$27.1\,pp & --- \\
771	Llama-70B FP8 & 16 & ---    & ---    & $-$10.9\,pp & {[}3.0, 20.1{]} \\
772	Gemini Flash  & 8  & 90.5\% & 72.9\% & $-$17.6\,pp & {[}15.1, 20.1{]} \\
773	\bottomrule
774	\end{tabular}
775	\end{table}
776	
777	\section{Few-Shot Prompting and Confusability}
778	\label{sec:appendix_fewshot_bcs}
779	
780	To test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\ref{tab:fewshot_bcs}).
781	
782	\begin{table}[h]
783	\centering
784	\small
785	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
786	\label{tab:fewshot_bcs}
787	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
788	\toprule
789	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
790	\midrule
791	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
792	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
793	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
794	\bottomrule
795	\end{tabular}}
796	\end{table}
797	
798	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \citep{lost-in-middle-2024}.
799	
800	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
801	
802	\section{Qualitative Error Analysis}
803	\label{app:error-analysis}
804	
805	Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\ref{tab:error_examples} provides illustrative confusion instances with SCS values.
806	
807	\begin{table}[h]
808	\centering
809	\footnotesize
810	\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \textit{followed by}/\textit{follows}, SCS\,=\,0.90) and family-relation pairs (\textit{child}/\textit{father}, \textit{child}/\textit{mother}) dominate. Some low-SCS pairs (\textit{instance of}/\textit{taxon rank}, SCS\,=\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}
811	\label{tab:top10_re}
812	\begin{tabular}{cllrr}
813	\toprule
814	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
815	\midrule
816	1 & instance of & taxon rank & 0.53 & 875 \\
817	2 & child & father & 0.84 & 700 \\
818	3 & participant of & participating team & 0.75 & 675 \\
819	4 & mountain range & part of & 0.57 & 575 \\
820	5 & mouth of watercourse & tributary & 0.65 & 549 \\
821	6 & child & mother & 0.84 & 500 \\
822	7 & league & member of & 0.66 & 450 \\
823	8 & country of citizenship & country of origin & 0.76 & 400 \\
824	9 & followed by & follows & 0.90 & 400 \\
825	10 & occupation & voice type & 0.57 & 400 \\
826	\bottomrule
827	\end{tabular}
828	\end{table}
829	
830	\begin{table}[h]
831	\centering
832	\footnotesize
833	\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \textit{person-other}/\textit{person-politician}, SCS\,=\,0.93) and cross-category pairs sharing referent overlap (\textit{building-other}/\textit{location-GPE}, SCS\,=\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}
834	\label{tab:top10_ner}
835	\begin{tabular}{cllrr}
836	\toprule
837	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
838	\midrule
839	1 & person-other & person-politician & 0.93 & 121 \\
840	2 & location-GPE & organization-other & 0.83 & 81 \\
841	3 & art-film & location-GPE & 0.69 & 57 \\
842	4 & building-other & location-GPE & 0.85 & 56 \\
843	5 & building-other & person-other & 0.90 & 43 \\
844	6 & location-GPE & product-other & 0.69 & 39 \\
845	7 & org-gov/agency & person-other & 0.85 & 34 \\
846	8 & person-actor & person-other & 0.90 & 34 \\
847	9 & building-other & location-road/transit & 0.76 & 32 \\
848	10 & location-GPE & org-sportsleague & 0.81 & 30 \\
849	\bottomrule
850	\end{tabular}
851	\end{table}
852	
853	\begin{table*}[t]
854	\centering
855	\small
856	\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\,$>$\,0.90: \textit{participant} vs.\ \textit{participant of} reverses directionality; \textit{contains} vs.\ \textit{located in} inverts containment; \textit{part of} vs.\ \textit{member of} conflates meronymy with membership. a.t.e.\ = admin.\ territorial entity.}
857	\label{tab:error_examples}
858	\begin{tabular}{p{8cm}llc}
859	\toprule
860	\textbf{Sentence} & \textbf{Gold} & \textbf{Pred.} & \textbf{SCS} \\
861	\midrule
862	\ldots\ played for \textbf{Valencia} \ldots\ [\textbf{EuroLeague}] & participant & participant of & 0.97 \\
863	\addlinespace
864	\textbf{Pilões} is a municipality in \textbf{Rio Grande do Norte} \ldots & contains a.t.e. & located in a.t.e. & 0.92 \\
865	\addlinespace
866	Davies \ldots\ appointed to \textbf{Cabinet} as \textbf{Sec.\ of State} & part of & member of & 0.90 \\
867	\bottomrule
868	\end{tabular}
869	\end{table*}
870	
871	\section{Schema Label Renaming Experiment}
872	\label{app:renaming}
873	
874	To test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \textit{participant of} $\to$ \textit{event involvement} (SCS: 0.97 $\to$ 0.72), \textit{follows} $\to$ \textit{prior entry} (0.90 $\to$ 0.69), \textit{part of} $\to$ \textit{integral segment of} (0.90 $\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\ref{tab:renaming}).
875	
876	\begin{table}[h!]
877	\centering
878	\small
879	\caption{Accuracy (\%) under original vs.\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\Delta_{\text{high}} - \Delta_{\text{low}} = -5.9$\,pp ($t = -7.23$, $p < 0.001$).}
880	\label{tab:renaming}
881	\begin{tabular}{lccc}
882	\toprule
883	& \textbf{Control} & \textbf{Treatment} & \textbf{$\Delta$\,(pp)} \\
884	\midrule
885	Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\
886	High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\
887	\bottomrule
888	\end{tabular}
889	\end{table}
890	
891	Renaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\geq$ original $-5$\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.
892	
893	\section{Relaxed Matching Evaluation (NER)}
894	\label{app:relaxed-matching}
895	
896	To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\times$ 25 batches $\times$ 3 seeds; Table~\ref{tab:relaxed_matching}).
897	
898	\begin{table}[h!]
899	\centering
900	\small
901	\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\,pp (98.4\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}
902	\label{tab:relaxed_matching}
903	\begin{tabular}{lrrrrr}
904	\toprule
905	\textbf{Match mode} & \textbf{$r$} & \textbf{$p$} & \textbf{$\rho$} & \textbf{$p$} & \textbf{F1} \\
906	\midrule
907	Exact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\
908	Relaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\
909	Token overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\
910	Type-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\
911	\bottomrule
912	\end{tabular}
913	\end{table}
914	
915	A per-error-mode analysis confirms this null extends to all individual categories: miss ($\rho = 0.017$), boundary ($\rho = -0.043$), and type substitution ($\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.
916	
917	\end{document}
918	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "e2fa73df-668a-4572-bdcb-157d6c6a3683",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\\ref{tab:fewshot_bcs}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & 0.92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\\ref{tab:renaming}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
      "numLines": 219,
      "startLine": 700,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also check for the "code will be released upon acceptance" mention in all tex files, and check if there's an anonymous GitHub URL anywhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "34b944b8-6da2-432b-a86c-cbf68367bb32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PMj6y4XZiShV4E1t11YhG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 59827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 47_

Let me check for anonymous GitHub URL and code release mentions across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "067e5821-92ef-4e8d-bae9-1ff662008b61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PMj6y4XZiShV4E1t11YhG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 59827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01CMd4HBA2i3LEw1DxsfUasV`</summary>

```json
{
  "pattern": "anonymous\\.4open|github\\.com|code.*release|release.*code|upon acceptance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-i": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "d63ef9b9-5f3e-40ec-bf2d-4b25a8bc2ef5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PMj6y4XZiShV4E1t11YhG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 59827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 49 · 2026-05-22T07:26:19.214Z_

<details><summary>↩ Tool result · `toolu_01CMd4HBA2i3LEw1DxsfUasV`</summary>

```text
docs/paper/checklist.tex:75:Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
docs/paper/introduction.tex:5:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "c66de1a9-2f12-40f5-b224-e0ac3c30101d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/checklist.tex:75:Yes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\ndocs/paper/introduction.tex:5:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_013amVJJnVbN7yhPVyyDxmVK`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/anonymous_github/ 2>/dev/null | head -20",
  "description": "Check anonymous github directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "0c862eba-cffd-454f-b4ca-2b8750c6878f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PMj6y4XZiShV4E1t11YhG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 59827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 51 · 2026-05-22T07:26:20.222Z_

<details><summary>↩ Tool result · `toolu_013amVJJnVbN7yhPVyyDxmVK`</summary>

```text
LICENSE
README.md
data
requirements.txt
scripts
src
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "2aeb6bff-1fd6-40d9-9511-ebc84e7eee1d",
  "tool_use_result": {
    "stdout": "LICENSE\nREADME.md\ndata\nrequirements.txt\nscripts\nsrc",
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01AEMsq8xWrxfaGhjatWC77T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "38ff8be4-6559-4e58-80ea-e6de0d79fb72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PMj6y4XZiShV4E1t11YhG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7018,
      "cache_read_input_tokens": 59827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7018
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

_source line 53 · 2026-05-22T07:26:20.603Z_

<details><summary>↩ Tool result · `toolu_01AEMsq8xWrxfaGhjatWC77T`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	\looseness=-1
6	The confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\S\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
7	
8	\paragraph{Practical implications and conclusion.}
9	\label{sec:conclusion}
10	\looseness=-1
11	For NER, reducing candidate types is the primary lever; for RE, pre-computing SCS flags high-risk type pairs before deployment. Decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers accuracy, confirming approximate additivity of count and confusability (\S\ref{sec:multi_channel}); separability holds on the linear scale but remains open on the logit scale.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "b17a49cb-6e68-4980-839f-a370627fda47",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\n\\looseness=-1\nThe confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\\S\\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\\ref{sec:appendix_ner_power}).\n\n\\paragraph{Practical implications and conclusion.}\n\\label{sec:conclusion}\n\\looseness=-1\nFor NER, reducing candidate types is the primary lever; for RE, pre-computing SCS flags high-risk type pairs before deployment. Decompose-then-merge fails (\\S\\ref{sec:sdgd}), but oracle routing recovers accuracy, confirming approximate additivity of count and confusability (\\S\\ref{sec:multi_channel}); separability holds on the linear scale but remains open on the logit scale.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Grep · `toolu_01UFenbD6omDHWgf9vYFpknA`</summary>

```json
{
  "pattern": "code|release|github|upon acceptance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "0fef4e25-6df9-4046-99ee-6aea32380a00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KagCRZBcZ4xvG5MN5ZRCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 66845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
      },
      "output_tokens": 37,
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

_source line 55 · 2026-05-22T07:26:24.682Z_

<details><summary>↩ Tool result · `toolu_01UFenbD6omDHWgf9vYFpknA`</summary>

```text
5:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "5fe4c135-b581-4ea9-9220-89ef79ee1eb7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "5:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01QFofS2qpEKsQmDBeKAJsdg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "366353e1-7235-4a85-a00f-1927ec5641c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018KagCRZBcZ4xvG5MN5ZRCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 66845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
      },
      "output_tokens": 37,
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

_source line 57 · 2026-05-22T07:26:25.326Z_

<details><summary>↩ Tool result · `toolu_01QFofS2qpEKsQmDBeKAJsdg`</summary>

```text
1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "c3c60fda-2e65-4594-9d46-c7602e999868",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
      "content": "\\lstset{\n  basicstyle=\\ttfamily\\small,\n  breaklines=true,\n  breakatwhitespace=true,\n  columns=fullflexible\n}\n\n\\section{Prompt Templates}\n\\label{sec:appendix_prompts}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 210
    }
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01QURZyQN2fE43NCpmJFNXvT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "offset": 0,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "6882279e-244c-4749-a03a-1bdc852f80f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3HZxqe7RRsxdMPjQQMzjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 67735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 392
      },
      "output_tokens": 71,
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

_source line 59 · 2026-05-22T07:26:28.231Z_

<details><summary>↩ Tool result · `toolu_01QURZyQN2fE43NCpmJFNXvT`</summary>

```text
0	\section{Introduction}
1	\label{sec:introduction}
2	
3	\looseness=-1
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	\looseness=-1
7	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
8	
9	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "31c08fe4-5389-4b22-8ab2-b25c5279d2ca",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\looseness=-1\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \\citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.\n\n\\looseness=-1\nWhat explains this degradation? Prior decomposition strategies \\citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.",
      "numLines": 10,
      "startLine": 0,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

Now I have all the information needed. Let me compile the final checklist and write it to artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "c1bf8324-1f55-472e-bc87-8c379bdf5cb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7Bw5QpQmYrzu8KV8rLksP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 68127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
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

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VszpBREFu2iuibdjY9hBYa`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "f131edb8-c0f6-42a8-a426-3f9fb56ec68c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7Bw5QpQmYrzu8KV8rLksP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 68127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
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

### Tool result

_source line 62 · 2026-05-22T07:26:32.045Z_

<details><summary>↩ Tool result · `toolu_01VszpBREFu2iuibdjY9hBYa`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "9e95432b-c692-4330-b06f-3965db92803b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 63_

Now I have all the information. Let me compile the results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "754a834c-5def-432c-8d8b-aa0e4a553521",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqNaGCoMBexW8iTcuXgaEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 68753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 998
      },
      "output_tokens": 2,
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

_source line 64_

<details open><summary>🔧 Tool call — Write · `toolu_012G3ptDitAFxdxf29wnY4m5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_final.md",
  "content": "# ARR Submission Pre-Check: Supplementary Material + Checklist\n\nUpdated: 2026-05-22\n\n---\n\n## 2. Supplementary Material\n\n### a) Appendix Sections (in main.pdf)\n\nAll appendices are embedded in `main.tex` after `\\appendix` (starting ~line 57). 25 sections total:\n\n| # | Section Title | Label | Content Summary |\n|---|--------------|-------|-----------------|\n| A | Additional Figures | `sec:appendix_figures` | Cross-model count-curve tables (8B, 32B), cross-model BCS tables, error taxonomy (IntraSub/Missed by BCS bin), cross-model error taxonomy replication |\n| B | SDGD Full Protocol and Results | `sec:appendix_sdgd` | Graph-coloring decomposition protocol, 4-mode comparison table, v2 confidence-gated merge |\n| B.1 | Practical Routing Strategies on RE | `sec:appendix_routing` | 5 non-oracle routing strategies on FewRel 80-rel RE |\n| C | Factorial Analysis and Separability Test | `sec:appendix_factorial` | Count×BCS regression, TOST equivalence, logit-scale sensitivity, DocRED factorial, range-matched robustness |\n| D | Within-Pool CI Details | `sec:appendix_within_pool` | 80-pool 16-sub quartile Δ CI interpretation |\n| E | Controlling for Centrality Confounds in MAVEN | `sec:appendix_residualized_bcs` | MiniLM/Qwen3 partial correlations, centrality artifact analysis |\n| E.1 | Partial Correlation: Controlling for Degree Centrality | `sec:appendix_partial_corr` | FewRel/DocRED partial correlations, ridge regression under multicollinearity |\n| E.2 | NER BCS-Null Power Analysis | `sec:appendix_ner_power` | BCS variance restriction analysis, minimum detectable |r| |\n| E.3 | Bootstrap CI Robustness | `sec:appendix_bootstrap_ci` | Cluster-robust inference for shared-instance batches |\n| E.4 | Domain Distribution in Extreme-BCS Batches | `sec:appendix_domain_distribution` | χ² domain composition analysis, mediator argument |\n| F | Batch Composition Results | `sec:appendix_batch_composition` | Oracle routing accuracy table |\n| G | Prompt Templates | `sec:appendix_prompts` | Full prompt templates (v1, v2, etc.) |\n| H | Prompt Version Sensitivity Analysis | `sec:appendix_prompt_sensitivity` | RE/NER replication under v2 prompt |\n| H.1 | Cross-Prompt-Variant BCS Correlation | `sec:appendix_prompt_variants` | 4 prompt variants × 2 count levels |\n| I | BCS Aggregation Sensitivity | `sec:appendix_bcs_sensitivity` | Mean vs. max SCS aggregation comparison |\n| J | BCS-Controlled Detailed Results | `app:bcs-controlled-table` | Full BCS-controlled accuracy table, adjusted R² |\n| K | Format Independence | `app:format-independence` | Paired constrained vs. unconstrained decoding, per-batch table |\n| L | Within-Pool Analysis Methodology | `app:within-pool-method` | 3-way BCS–accuracy table, permutation tests |\n| M | SCS Embedding Ablation | `app:scs-ablation` | Name-only vs. name+definition, held-out validation |\n| N | Pair-to-Batch Aggregation Simulation | `app:aggregation-sim` | Monte Carlo simulation, unconditional baseline, ecological inference |\n| O | BCS Independence from Type Composition | `app:bcs-composition` | Variance decomposition (BCS unique vs. composition unique) |\n| P | SCS vs. Simple Baselines | `app:scs-baselines` | SCS vs. WordNet/Levenshtein/same-parent |\n| Q | Split-Origin Covariate Analysis | `app:split-origin` | Train/val origin confound control |\n| R | Cross-Seed Variance Decomposition | `app:variance-decomposition` | Batch SD vs. seed SD table |\n| S | Cross-Domain Connections | `app:cross-domain` | SGD/SGD-X analogy, practical implications |\n| T | Cross-Model: LLaMA-3.1-70B-Instruct | `sec:appendix_cross_model_70b` | Full 70B replication (count curves + BCS) |\n| U | Cross-Model: Gemini 2.5 Flash | `sec:appendix_cross_model_gemini` | Gemini count curves + BCS, leverage-point analysis |\n| V | Few-Shot Prompting and Confusability | `sec:appendix_fewshot_bcs` | 0/1/5-shot BCS gap analysis |\n| W | Qualitative Error Analysis | `app:error-analysis` | Top-10 confused pairs (RE + NER), illustrative examples |\n| X | Schema Label Renaming Experiment | `app:renaming` | SCS-reduction intervention, label unfamiliarity effect |\n| Y | Relaxed Matching Evaluation (NER) | `app:relaxed-matching` | 4 matching modes, per-error-mode analysis |\n\n**Status**: ✅ All appendices are in main.pdf (confirmed by `\\appendix` in main.tex). No separate appendix file needed.\n\n### b) Independent Supplementary\n\n- **Code availability mention**: \"Code and data will be released upon acceptance\" appears in:\n  - Introduction footnote 2 (line 4 of introduction.tex)\n  - Checklist C4 (checklist.tex line 75)\n- **No anonymous GitHub URL** is present in the paper PDF. The anonymous repo is prepared at `artifacts/anonymous_github/` (contains `src/`, `scripts/`, `data/`, `requirements.txt`, `LICENSE`, `README.md`) but has **not been uploaded** to anonymous.4open.science yet.\n- **ARR supplementary policy**: ARR accepts a single supplementary PDF or ZIP via the OpenReview form. Since all appendices are in-paper, the supplementary field can be used for the anonymous GitHub link or a ZIP of the code.\n\n**Action needed**:\n1. Upload `artifacts/anonymous_github/` to https://anonymous.4open.science/\n2. Before upload, verify no path leaks: `grep -r '/root/' artifacts/anonymous_github/`\n3. Paste the anonymous GitHub URL in the OpenReview supplementary field\n\n### c) Data/Code Citations\n\n| Artifact | Citation | Location | Status |\n|----------|----------|----------|--------|\n| Few-NERD | `\\citep{fewnerd-2021}` | §3.1, checklist B1 | ✅ PASS |\n| FewRel | `\\citep{fewrel-2018}` | §3.1, checklist B1 | ✅ PASS |\n| DocRED | `\\citep{docred-2019}` | §3.1, checklist B1 | ✅ PASS |\n| MAVEN | `\\citep{maven-2020}` | §3.1, checklist B1 | ✅ PASS |\n| Qwen3-32B | `\\citep{qwen3-2025}` | §3.5, checklist B1 | ✅ PASS |\n| LLaMA-3.1 (8B/70B) | `\\citep{llama3-2024}` | §3.5, checklist B1 | ✅ PASS |\n| Gemini 2.5 Flash | `\\citep{gemini-2025}` | §3.5, checklist B1 | ✅ PASS |\n| vLLM | `\\citep{vllm-2023}` | §3.5, checklist B1/C4 | ✅ PASS |\n| all-MiniLM-L6-v2 | `\\citep{minilm-2020}` | §3.2, checklist B1 | ✅ PASS |\n| transformers/scikit-learn | Not cited individually | — | ℹ️ N/A (standard libraries; not required by ARR) |\n\n**Status**: ✅ PASS — All datasets, models, and key tools have proper citations.\n\n---\n\n## 3. ARR Responsible NLP Checklist\n\n> Note: EMNLP 2026 checklist is filled in OpenReview submission form, not in PDF. The paper includes a `checklist.tex` but it is commented out in main.tex (`% \\input{checklist}`). This is correct per EMNLP 2026 policy.\n\n### A. For Every Submission\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| A1 | Limitations described? | **YES** | Limitations section (after §6, p.8–9). 6 items: (1) model coverage, (2) effect size/statistical design, (3) task scope, (4) causal mechanism/contamination, (5) domain/language scope, (6) multiple comparisons. Plus paragraphs on across-batch correlation and multiple comparisons. |\n| A2 | Potential risks discussed? | **YES** | Limitations section. SCS/BCS misuse as deployment criterion noted. |\n| A3 | Abstract/intro summarize claims? | **YES** | Abstract (3 findings), §1 (4 findings + 3 contributions). |\n| A4 | AI assistant use reported? | **YES** | checklist.tex A4: Claude for writing assistance and code development. |\n\n### B. Scientific Artifacts\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| B1 | Creators cited? | **YES** | §3.1 (datasets), §3.5 (models). All 9 artifacts cited (see §2c above). |\n| B2 | License/terms discussed? | **YES** | checklist.tex B2: CC-BY-SA 4.0 (Few-NERD), research-use (FewRel/DocRED/MAVEN), model licenses, API ToS. |\n| B3 | Consistent with intended use? | **YES** | checklist.tex B3: All datasets used for IE evaluation. |\n| B4 | PII/offensive content? | **N/A** | No new data collection. Established benchmarks. |\n| B5 | Artifact documentation? | **YES** | Table 1 (dataset stats), §3.1 (provenance, sampling). |\n| B6 | Relevant statistics? | **YES** | §3.1, Table 1, §3.3. |\n\n### C. Computational Experiments\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| C1 | Parameters/compute/infrastructure? | **YES** | §3.5: model sizes (8B/32B/70B), FP8, NVIDIA RTX PRO 6000 (96GB), ~72 GPU-hours inference, no training. Gemini via API. |\n| C2 | Experimental setup/hyperparameters? | **YES** | §3.3 (count curves, BCS-controlled design), §3.5 (greedy, temp=0, seed=42). No hyperparameter search. |\n| C3 | Descriptive statistics? | **YES** | 95% bootstrap CIs (B=10,000), Spearman with p-values (§4), permutation tests, semipartial R². |\n| C4 | Implementation details? | **YES** | §3.5: vLLM v0.20.2, embedding model versions. Code release upon acceptance. |\n\n### D. Human Annotators\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| D1–D5 | All human annotation questions | **N/A** | No human annotation or crowdsourcing. |\n\n### E. AI-Assisted Research\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| E1 | AI assistant use reported? | **YES** | A4: Claude for code development and document formatting. Research design/execution/interpretation by authors. |\n\n---\n\n## Items Requiring Action\n\n| Priority | Item | Details | Suggested Fix |\n|----------|------|---------|---------------|\n| 🔴 HIGH | Anonymous GitHub not uploaded | Code repo prepared at `artifacts/anonymous_github/` but no URL in paper or OpenReview | Upload to anonymous.4open.science, add URL to OpenReview supplementary field |\n| 🟡 MED | Path leak check before upload | anonymous_github may contain `/root/` paths | Run `grep -r '/root/' artifacts/anonymous_github/` and sanitize |\n| 🟢 LOW | checklist.tex vs OpenReview consistency | Paper has `checklist.tex` (commented out correctly); ensure OpenReview form answers match | Copy answers from this document when filling the OpenReview form |\n| 🟢 LOW | Compute budget for Gemini | C1 mentions ~72 GPU-hours for open-weight models; Gemini API cost not quantified | Consider adding \"Gemini API cost: $X\" or noting \"API cost not reported\" in OpenReview form C1 |\n\nNo checklist items need to be changed from YES→NO or vice versa. The checklist is complete and accurate.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "942f8acd-b222-4d1a-987c-12dab61603dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqNaGCoMBexW8iTcuXgaEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 998,
      "cache_read_input_tokens": 68753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 998
      },
      "output_tokens": 2,
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

_source line 65 · 2026-05-22T07:27:48.516Z_

<details><summary>↩ Tool result · `toolu_012G3ptDitAFxdxf29wnY4m5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_final.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "cf6d4718-7b52-4ef1-9c23-a2cf2a8038e9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_final.md",
    "content": "# ARR Submission Pre-Check: Supplementary Material + Checklist\n\nUpdated: 2026-05-22\n\n---\n\n## 2. Supplementary Material\n\n### a) Appendix Sections (in main.pdf)\n\nAll appendices are embedded in `main.tex` after `\\appendix` (starting ~line 57). 25 sections total:\n\n| # | Section Title | Label | Content Summary |\n|---|--------------|-------|-----------------|\n| A | Additional Figures | `sec:appendix_figures` | Cross-model count-curve tables (8B, 32B), cross-model BCS tables, error taxonomy (IntraSub/Missed by BCS bin), cross-model error taxonomy replication |\n| B | SDGD Full Protocol and Results | `sec:appendix_sdgd` | Graph-coloring decomposition protocol, 4-mode comparison table, v2 confidence-gated merge |\n| B.1 | Practical Routing Strategies on RE | `sec:appendix_routing` | 5 non-oracle routing strategies on FewRel 80-rel RE |\n| C | Factorial Analysis and Separability Test | `sec:appendix_factorial` | Count×BCS regression, TOST equivalence, logit-scale sensitivity, DocRED factorial, range-matched robustness |\n| D | Within-Pool CI Details | `sec:appendix_within_pool` | 80-pool 16-sub quartile Δ CI interpretation |\n| E | Controlling for Centrality Confounds in MAVEN | `sec:appendix_residualized_bcs` | MiniLM/Qwen3 partial correlations, centrality artifact analysis |\n| E.1 | Partial Correlation: Controlling for Degree Centrality | `sec:appendix_partial_corr` | FewRel/DocRED partial correlations, ridge regression under multicollinearity |\n| E.2 | NER BCS-Null Power Analysis | `sec:appendix_ner_power` | BCS variance restriction analysis, minimum detectable |r| |\n| E.3 | Bootstrap CI Robustness | `sec:appendix_bootstrap_ci` | Cluster-robust inference for shared-instance batches |\n| E.4 | Domain Distribution in Extreme-BCS Batches | `sec:appendix_domain_distribution` | χ² domain composition analysis, mediator argument |\n| F | Batch Composition Results | `sec:appendix_batch_composition` | Oracle routing accuracy table |\n| G | Prompt Templates | `sec:appendix_prompts` | Full prompt templates (v1, v2, etc.) |\n| H | Prompt Version Sensitivity Analysis | `sec:appendix_prompt_sensitivity` | RE/NER replication under v2 prompt |\n| H.1 | Cross-Prompt-Variant BCS Correlation | `sec:appendix_prompt_variants` | 4 prompt variants × 2 count levels |\n| I | BCS Aggregation Sensitivity | `sec:appendix_bcs_sensitivity` | Mean vs. max SCS aggregation comparison |\n| J | BCS-Controlled Detailed Results | `app:bcs-controlled-table` | Full BCS-controlled accuracy table, adjusted R² |\n| K | Format Independence | `app:format-independence` | Paired constrained vs. unconstrained decoding, per-batch table |\n| L | Within-Pool Analysis Methodology | `app:within-pool-method` | 3-way BCS–accuracy table, permutation tests |\n| M | SCS Embedding Ablation | `app:scs-ablation` | Name-only vs. name+definition, held-out validation |\n| N | Pair-to-Batch Aggregation Simulation | `app:aggregation-sim` | Monte Carlo simulation, unconditional baseline, ecological inference |\n| O | BCS Independence from Type Composition | `app:bcs-composition` | Variance decomposition (BCS unique vs. composition unique) |\n| P | SCS vs. Simple Baselines | `app:scs-baselines` | SCS vs. WordNet/Levenshtein/same-parent |\n| Q | Split-Origin Covariate Analysis | `app:split-origin` | Train/val origin confound control |\n| R | Cross-Seed Variance Decomposition | `app:variance-decomposition` | Batch SD vs. seed SD table |\n| S | Cross-Domain Connections | `app:cross-domain` | SGD/SGD-X analogy, practical implications |\n| T | Cross-Model: LLaMA-3.1-70B-Instruct | `sec:appendix_cross_model_70b` | Full 70B replication (count curves + BCS) |\n| U | Cross-Model: Gemini 2.5 Flash | `sec:appendix_cross_model_gemini` | Gemini count curves + BCS, leverage-point analysis |\n| V | Few-Shot Prompting and Confusability | `sec:appendix_fewshot_bcs` | 0/1/5-shot BCS gap analysis |\n| W | Qualitative Error Analysis | `app:error-analysis` | Top-10 confused pairs (RE + NER), illustrative examples |\n| X | Schema Label Renaming Experiment | `app:renaming` | SCS-reduction intervention, label unfamiliarity effect |\n| Y | Relaxed Matching Evaluation (NER) | `app:relaxed-matching` | 4 matching modes, per-error-mode analysis |\n\n**Status**: ✅ All appendices are in main.pdf (confirmed by `\\appendix` in main.tex). No separate appendix file needed.\n\n### b) Independent Supplementary\n\n- **Code availability mention**: \"Code and data will be released upon acceptance\" appears in:\n  - Introduction footnote 2 (line 4 of introduction.tex)\n  - Checklist C4 (checklist.tex line 75)\n- **No anonymous GitHub URL** is present in the paper PDF. The anonymous repo is prepared at `artifacts/anonymous_github/` (contains `src/`, `scripts/`, `data/`, `requirements.txt`, `LICENSE`, `README.md`) but has **not been uploaded** to anonymous.4open.science yet.\n- **ARR supplementary policy**: ARR accepts a single supplementary PDF or ZIP via the OpenReview form. Since all appendices are in-paper, the supplementary field can be used for the anonymous GitHub link or a ZIP of the code.\n\n**Action needed**:\n1. Upload `artifacts/anonymous_github/` to https://anonymous.4open.science/\n2. Before upload, verify no path leaks: `grep -r '/root/' artifacts/anonymous_github/`\n3. Paste the anonymous GitHub URL in the OpenReview supplementary field\n\n### c) Data/Code Citations\n\n| Artifact | Citation | Location | Status |\n|----------|----------|----------|--------|\n| Few-NERD | `\\citep{fewnerd-2021}` | §3.1, checklist B1 | ✅ PASS |\n| FewRel | `\\citep{fewrel-2018}` | §3.1, checklist B1 | ✅ PASS |\n| DocRED | `\\citep{docred-2019}` | §3.1, checklist B1 | ✅ PASS |\n| MAVEN | `\\citep{maven-2020}` | §3.1, checklist B1 | ✅ PASS |\n| Qwen3-32B | `\\citep{qwen3-2025}` | §3.5, checklist B1 | ✅ PASS |\n| LLaMA-3.1 (8B/70B) | `\\citep{llama3-2024}` | §3.5, checklist B1 | ✅ PASS |\n| Gemini 2.5 Flash | `\\citep{gemini-2025}` | §3.5, checklist B1 | ✅ PASS |\n| vLLM | `\\citep{vllm-2023}` | §3.5, checklist B1/C4 | ✅ PASS |\n| all-MiniLM-L6-v2 | `\\citep{minilm-2020}` | §3.2, checklist B1 | ✅ PASS |\n| transformers/scikit-learn | Not cited individually | — | ℹ️ N/A (standard libraries; not required by ARR) |\n\n**Status**: ✅ PASS — All datasets, models, and key tools have proper citations.\n\n---\n\n## 3. ARR Responsible NLP Checklist\n\n> Note: EMNLP 2026 checklist is filled in OpenReview submission form, not in PDF. The paper includes a `checklist.tex` but it is commented out in main.tex (`% \\input{checklist}`). This is correct per EMNLP 2026 policy.\n\n### A. For Every Submission\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| A1 | Limitations described? | **YES** | Limitations section (after §6, p.8–9). 6 items: (1) model coverage, (2) effect size/statistical design, (3) task scope, (4) causal mechanism/contamination, (5) domain/language scope, (6) multiple comparisons. Plus paragraphs on across-batch correlation and multiple comparisons. |\n| A2 | Potential risks discussed? | **YES** | Limitations section. SCS/BCS misuse as deployment criterion noted. |\n| A3 | Abstract/intro summarize claims? | **YES** | Abstract (3 findings), §1 (4 findings + 3 contributions). |\n| A4 | AI assistant use reported? | **YES** | checklist.tex A4: Claude for writing assistance and code development. |\n\n### B. Scientific Artifacts\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| B1 | Creators cited? | **YES** | §3.1 (datasets), §3.5 (models). All 9 artifacts cited (see §2c above). |\n| B2 | License/terms discussed? | **YES** | checklist.tex B2: CC-BY-SA 4.0 (Few-NERD), research-use (FewRel/DocRED/MAVEN), model licenses, API ToS. |\n| B3 | Consistent with intended use? | **YES** | checklist.tex B3: All datasets used for IE evaluation. |\n| B4 | PII/offensive content? | **N/A** | No new data collection. Established benchmarks. |\n| B5 | Artifact documentation? | **YES** | Table 1 (dataset stats), §3.1 (provenance, sampling). |\n| B6 | Relevant statistics? | **YES** | §3.1, Table 1, §3.3. |\n\n### C. Computational Experiments\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| C1 | Parameters/compute/infrastructure? | **YES** | §3.5: model sizes (8B/32B/70B), FP8, NVIDIA RTX PRO 6000 (96GB), ~72 GPU-hours inference, no training. Gemini via API. |\n| C2 | Experimental setup/hyperparameters? | **YES** | §3.3 (count curves, BCS-controlled design), §3.5 (greedy, temp=0, seed=42). No hyperparameter search. |\n| C3 | Descriptive statistics? | **YES** | 95% bootstrap CIs (B=10,000), Spearman with p-values (§4), permutation tests, semipartial R². |\n| C4 | Implementation details? | **YES** | §3.5: vLLM v0.20.2, embedding model versions. Code release upon acceptance. |\n\n### D. Human Annotators\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| D1–D5 | All human annotation questions | **N/A** | No human annotation or crowdsourcing. |\n\n### E. AI-Assisted Research\n\n| # | Question | Answer | Location / Justification |\n|---|----------|--------|--------------------------|\n| E1 | AI assistant use reported? | **YES** | A4: Claude for code development and document formatting. Research design/execution/interpretation by authors. |\n\n---\n\n## Items Requiring Action\n\n| Priority | Item | Details | Suggested Fix |\n|----------|------|---------|---------------|\n| 🔴 HIGH | Anonymous GitHub not uploaded | Code repo prepared at `artifacts/anonymous_github/` but no URL in paper or OpenReview | Upload to anonymous.4open.science, add URL to OpenReview supplementary field |\n| 🟡 MED | Path leak check before upload | anonymous_github may contain `/root/` paths | Run `grep -r '/root/' artifacts/anonymous_github/` and sanitize |\n| 🟢 LOW | checklist.tex vs OpenReview consistency | Paper has `checklist.tex` (commented out correctly); ensure OpenReview form answers match | Copy answers from this document when filling the OpenReview form |\n| 🟢 LOW | Compute budget for Gemini | C1 mentions ~72 GPU-hours for open-weight models; Gemini API cost not quantified | Consider adding \"Gemini API cost: $X\" or noting \"API cost not reported\" in OpenReview form C1 |\n\nNo checklist items need to be changed from YES→NO or vice versa. The checklist is complete and accurate.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01T9b45eTn8znvauxRc8fnBk`</summary>

```json
{
  "name": "arr_checklist_final",
  "type": "report",
  "description": "ARR submission pre-check: supplementary material inventory + full responsible NLP checklist with per-item answers and action items",
  "project": "schema-dag-extraction",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/arr_checklist_final.md",
  "tags": [
    "arr",
    "checklist",
    "submission",
    "emnlp2026"
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
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "cd9c3e36-736d-44f5-bcdc-bce85410cf02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFz8frGnnbJSigmw85ssRE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3616,
      "cache_read_input_tokens": 69751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3616
      },
      "output_tokens": 68,
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

_source line 67 · 2026-05-22T07:27:53.703Z_

<details><summary>↩ Tool result · `toolu_01T9b45eTn8znvauxRc8fnBk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_3d29b2\", \"name\": \"arr_checklist_final\", \"type\": \"report\", \"description\": \"ARR submission pre-check: supplementary material inventory + full responsible NLP checklist with per-item answers and action items\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/report/arr_checklist_final.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:27:53.463930+00:00\", \"tags\": [\"arr\", \"checklist\", \"submission\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "0912adb8-c4bb-4553-ae7d-69f1fafb5416",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_3d29b2\\\", \\\"name\\\": \\\"arr_checklist_final\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"ARR submission pre-check: supplementary material inventory + full responsible NLP checklist with per-item answers and action items\\\", \\\"path\\\": \\\"projects/schema-dag-extraction/artifacts/_project/report/arr_checklist_final.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema-dag-extraction\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T07:27:53.463930+00:00\\\", \\\"tags\\\": [\\\"arr\\\", \\\"checklist\\\", \\\"submission\\\", \\\"emnlp2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_3d29b2\", \"name\": \"arr_checklist_final\", \"type\": \"report\", \"description\": \"ARR submission pre-check: supplementary material inventory + full responsible NLP checklist with per-item answers and action items\", \"path\": \"projects/schema-dag-extraction/artifacts/_project/report/arr_checklist_final.md\", \"url\": null, \"project\": \"schema-dag-extraction\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:27:53.463930+00:00\", \"tags\": [\"arr\", \"checklist\", \"submission\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 68_

## 产出

### 2. Supplementary Material

**a) Appendix sections**: 25 个 section（A–Y），全部在 main.pdf 内。覆盖：cross-model validation（8B/70B/Gemini）、SDGD 协议、factorial analysis/TOST、centrality confound 控制、prompt sensitivity（4 变体）、BCS aggregation、format independence、SCS ablation、Monte Carlo 模拟、error taxonomy、renaming experiment、relaxed matching 等。

**b) Independent supplementary**: **需要操作** — `artifacts/anonymous_github/` 已准备好（42 scripts + 24 auxiliary + data + requirements.txt），但尚未上传到 anonymous.4open.science。论文中仅写 "Code and data will be released upon acceptance"（introduction 脚注 + checklist C4），无匿名 URL。

**c) Data/code citations**: **PASS** — 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）+ 4 个模型 + vLLM + MiniLM 均有正确 citation。

### 3. ARR Checklist

所有项目均已正确填写：
- **A1–A4**: YES（Limitations 6 项 + 2 段，risks 已讨论，AI 使用已声明）
- **B1–B6**: YES/N-A（全部 artifact 已 cite，license 已讨论）
- **C1–C4**: YES（72 GPU-hours，seed=42，vLLM v0.20.2，bootstrap CIs）
- **D1–D5**: N/A
- **E1**: YES

### 需要修复的项

| 优先级 | 项目 | 建议 |
|--------|------|------|
| 🔴 | Anonymous GitHub 未上传 | 上传 `artifacts/anonymous_github/` 到 anonymous.4open.science，链接填入 OpenReview supplementary 字段 |
| 🟡 | 上传前检查路径泄露 | `grep -r '/root/' artifacts/anonymous_github/` |
| 🟢 | Gemini API cost 未量化 | C1 中补充 API 费用或标注 "API cost not reported" |
| 🟢 | OpenReview form 填写 | 按 `arr_checklist_final.md` 逐项填入 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "uuid": "281d3ebb-048d-4465-9f28-7506a7b41f5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ftnqCHPd5o1PK2gLQww4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 73367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 511
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

_source line 69_

## 产出

### 2. Supplementary Material

**a) Appendix sections**: 25 个 section（A–Y），全部在 main.pdf 内。覆盖：cross-model validation（8B/70B/Gemini）、SDGD 协议、factorial analysis/TOST、centrality confound 控制、prompt sensitivity（4 变体）、BCS aggregation、format independence、SCS ablation、Monte Carlo 模拟、error taxonomy、renaming experiment、relaxed matching 等。

**b) Independent supplementary**: **需要操作** — `artifacts/anonymous_github/` 已准备好（42 scripts + 24 auxiliary + data + requirements.txt），但尚未上传到 anonymous.4open.science。论文中仅写 "Code and data will be released upon acceptance"（introduction 脚注 + checklist C4），无匿名 URL。

**c) Data/code citations**: **PASS** — 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）+ 4 个模型 + vLLM + MiniLM 均有正确 citation。

### 3. ARR Checklist

所有项目均已正确填写：
- **A1–A4**: YES（Limitations 6 项 + 2 段，risks 已讨论，AI 使用已声明）
- **B1–B6**: YES/N-A（全部 artifact 已 cite，license 已讨论）
- **C1–C4**: YES（72 GPU-hours，seed=42，vLLM v0.20.2，bootstrap CIs）
- **D1–D5**: N/A
- **E1**: YES

### 需要修复的项

| 优先级 | 项目 | 建议 |
|--------|------|------|
| 🔴 | Anonymous GitHub 未上传 | 上传 `artifacts/anonymous_github/` 到 anonymous.4open.science，链接填入 OpenReview supplementary 字段 |
| 🟡 | 上传前检查路径泄露 | `grep -r '/root/' artifacts/anonymous_github/` |
| 🟢 | Gemini API cost 未量化 | C1 中补充 API 费用或标注 "API cost not reported" |
| 🟢 | OpenReview form 填写 | 按 `arr_checklist_final.md` 逐项填入 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158900,
  "duration_api_ms": 159857,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "99d9f8fc-a0a2-42dc-bd8a-3a639272d452",
  "total_cost_usd": 0.9381897500000002,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 62037,
    "cache_read_input_tokens": 727105,
    "output_tokens": 7400,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 62037,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 644,
        "cache_read_input_tokens": 73367,
        "cache_creation_input_tokens": 511,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 511
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1726,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018160000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 7400,
      "cacheReadInputTokens": 727105,
      "cacheCreationInputTokens": 62037,
      "webSearchRequests": 0,
      "costUSD": 0.9363737500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0fe5c8dc-d003-4ee6-ad1f-a98e7c84d5fa"
}
```

</details>

---
