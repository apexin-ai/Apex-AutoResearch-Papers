# paper r26 integrate analyses

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 157
- **Recorded user turns:** 1
- **Tool calls:** 53
- **Original source:** `logs/workers/worker_paper_r26_integrate_analyses_20260522T052238.log`
- **Structured JSON:** [`fc745135217d8419d948.json`](../../sessions/fc/fc745135217d8419d948.json)

## Before a recorded user message

6 recorded events

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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
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
  "uuid": "b6cbce2e-a027-4e24-93de-5ea294a5123d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1779438000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "375f5a2c-9598-43eb-92f5-54275bbf2cc6",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Assistant

_source line 4_

Let me start by reading the relevant files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "efc4d186-e3ad-40cf-b184-59c2dfa09e2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kxixc4PbKjBcjscEjxUYdX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12634,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12634
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

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01Swotv1rFyWeqhvN6F4wTDR`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find appendix and artifact files",
  "prompt": "I need to find the following files in this project:\n\n1. The appendix tex file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ - look for appendix*.tex files\n2. The main.tex file structure to understand how appendix is included\n3. In /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/, find:\n   - docred_ridge_regression.json\n   - docred_ridge_appendix.tex\n   - Any bootstrap-related result files\n   - fewrel_domain_distribution.json\n4. results.tex around line 52 to see the ridge regression reference\n\nList all found files with their full paths. For the tex files, read their contents. For the JSON files, read their contents too. For results.tex, read lines 40-65."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "bd2f897b-7296-4b1c-9e4c-c9145e008832",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kxixc4PbKjBcjscEjxUYdX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12634,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12634
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Find appendix and artifact files",
  "task_type": "local_agent",
  "prompt": "I need to find the following files in this project:\n\n1. The appendix tex file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ - look for appendix*.tex files\n2. The main.tex file structure to understand how appendix is included\n3. In /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/, find:\n   - docred_ridge_regression.json\n   - docred_ridge_appendix.tex\n   - Any bootstrap-related result files\n   - fewrel_domain_distribution.json\n4. results.tex around line 52 to see the ridge regression reference\n\nList all found files with their full paths. For the tex files, read their contents. For the JSON files, read their contents too. For results.tex, read lines 40-65.",
  "uuid": "b7811272-a831-4373-ab30-438504f0a530",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

## Round 1

151 recorded events

### User

_source line 7 · 2026-05-22T05:22:56.070Z_

I need to find the following files in this project:

1. The appendix tex file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ - look for appendix*.tex files
2. The main.tex file structure to understand how appendix is included
3. In /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/, find:
   - docred_ridge_regression.json
   - docred_ridge_appendix.tex
   - Any bootstrap-related result files
   - fewrel_domain_distribution.json
4. results.tex around line 52 to see the ridge regression reference

List all found files with their full paths. For the tex files, read their contents. For the JSON files, read their contents too. For results.tex, read lines 40-65.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ef3ba263-9b95-4e19-80a0-e85894a93b51"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_18/…",
  "usage": {
    "total_tokens": 17986,
    "tool_uses": 1,
    "duration_ms": 1784
  },
  "last_tool_name": "Glob",
  "uuid": "324c3dc5-89a6-42a7-83dc-28c324dc1cae",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01LuZnpwU4kNpx3pcUsZSV2f`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "fa483d4f-8ff6-4527-b783-e67647e0d3f4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NBfHJ8LxRGrkdpHsdCyUXu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17973,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 10 · 2026-05-22T05:22:57.891Z_

<details><summary>↩ Tool result · `toolu_01LuZnpwU4kNpx3pcUsZSV2f`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "d8556789-2f21-4bd1-84a3-c52cc26f572c"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_18/…",
  "usage": {
    "total_tokens": 17991,
    "tool_uses": 2,
    "duration_ms": 1991
  },
  "last_tool_name": "Glob",
  "uuid": "e3685dd3-0c32-45c2-afd0-e7ef875ee4a2",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01PVzA4N42LyETtgFXsVi3Vn`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "84e8dca8-ad65-4616-968b-eabe0a8c4719",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NBfHJ8LxRGrkdpHsdCyUXu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17973,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 13 · 2026-05-22T05:22:58.088Z_

<details><summary>↩ Tool result · `toolu_01PVzA4N42LyETtgFXsVi3Vn`</summary>

```text
artifacts/_project/data/bcs_comparison.json
artifacts/bcs_comparison.json
artifacts/ace05_code/configs/ace05_entity_types.json
artifacts/exp-004/data/ace05_entity_types.json
artifacts/ace05_code/configs/ace05_relation_types.json
artifacts/exp-004/data/ace05_relation_types.json
artifacts/_project/data/maven_event_types.json
artifacts/maven_code/configs/maven_event_types.json
artifacts/exp003a_analysis.json
artifacts/exp003a/report/exp003a_analysis.json
artifacts/dream_reports/dream_20260515T053106/best/experiment_data.json
artifacts/dream_reports/dream_20260515T053106/median/experiment_data.json
artifacts/dream_reports/dream_20260515T053106/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T113743/best/experiment_data.json
artifacts/dream_reports/dream_20260515T113743/median/experiment_data.json
artifacts/dream_reports/dream_20260515T113743/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T140829/best/experiment_data.json
artifacts/dream_reports/dream_20260515T140829/median/experiment_data.json
artifacts/dream_reports/dream_20260515T140829/worst/experiment_data.json
artifacts/eval_exp1.json
artifacts/eval_exp2.json
artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json
artifacts/_project/data/w3_cluster_bootstrap_results.json
artifacts/d037_statistical_analyses/w4_count_recall_ci_results.json
artifacts/_project/data/w4_count_recall_ci_results.json
artifacts/d037_statistical_analyses/w2_practical_effect_results.json
artifacts/_project/data/w2_practical_effect_results.json
artifacts/fewrel_v2_bcs/eval_results.json
artifacts/exp_fewrel_v2_bcs_controlled/data/eval_results.json
artifacts/fewrel_v2_bcs/bootstrap_ci.json
artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json
artifacts/d037_ner_v2_bcs_analysis.json
artifacts/d037_data_consistency_check.json
artifacts/d037_statistical_analyses/figure_data_audit.json
artifacts/_project/data/bcs_fix_results.json
artifacts/bcs_fix/bcs_fix_results.json
artifacts/exp_docred_confusability/data/count_curve_results.json
artifacts/exp_docred_confusability/count_curve_results.json
artifacts/exp_docred_confusability/bcs_controlled_results.json
artifacts/exp_docred_confusability/data/bcs_controlled_results.json
artifacts/exp_docred_confusability/data/bootstrap_analysis.json
artifacts/exp_docred_confusability/bootstrap_analysis.json
artifacts/cross_embedding_sensitivity/results.json
artifacts/_project/data/results.json
artifacts/dream_reports/dream_20260516T073533/best/experiment_data.json
artifacts/dream_reports/dream_20260516T073533/median/experiment_data.json
artifacts/dream_reports/dream_20260516T073533/worst/experiment_data.json
artifacts/_project/data/results_f03b24.json
artifacts/_project/data/results_d18838.json
artifacts/q3_tost_n525_results.json
artifacts/q3_tost_n525_corrected.json
artifacts/exp_fewshot_bcs_v2/analysis.json
artifacts/exp_schema_intervention/data/analysis.json
artifacts/exp_schema_intervention/analysis.json
artifacts/exp_schema_intervention/solo_sanity_check.json
artifacts/exp_schema_intervention/data/solo_sanity_check.json
artifacts/schema_optimizer_test/optimization_report.json
artifacts/d051_fewrel_n25_s42/sample_info.json
artifacts/d051_fewrel_n25_s42/count_curve_summary.json
artifacts/bcs_controlled_llama-3.1-70b-fp8/count_16/batch_groups.json
artifacts/exp_v2_re_n25/batch_groups.json
artifacts/d051_fewrel_n25_s42/eval_results.json
artifacts/exp_gemini_flash/part1/count_curve_analysis.json
artifacts/_project/data/results_ce5faf.json
artifacts/scs_baseline_comparison/results.json
artifacts/exp_paired_constrained/data/summary.json
artifacts/exp_paired_constrained/data/per_batch_results.json
artifacts/_project/data/w4_relaxed_matching_results.json
artifacts/w4_relaxed_matching_results.json
artifacts/re_none_evaluation_analysis.json
artifacts/tost_sensitivity/tost_margin_sensitivity.json
artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json
artifacts/semipartial_r2_verification.json
artifacts/r1_statistical_supplements.json
artifacts/_project/data/r1_statistical_supplements.json
artifacts/error_taxonomy_cross_model.json
artifacts/permutation_equivalence_result.json
artifacts/bayesian_equivalence_bf01.json
artifacts/_project/data/fewrel_domain_classification.json
artifacts/fewrel_domain_classification.json
artifacts/_project/data/fewrel_domain_distribution.json
artifacts/fewrel_domain_distribution.json
artifacts/_project/data/docred_ridge_regression.json
artifacts/docred_ridge_regression.json
artifacts/_project/data/split_sample_bootstrap.json
artifacts/split_sample_bootstrap.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c0b69969-fd6b-49f7-ba09-5675081e356e"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_18/…",
  "usage": {
    "total_tokens": 17996,
    "tool_uses": 3,
    "duration_ms": 2228
  },
  "last_tool_name": "Glob",
  "uuid": "68b01f99-4725-46ba-9fa9-170482e9d297",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01MKzdhxSrkvKM2TtNrWhZZH`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ec2a6801-6294-47f5-9e97-dc317d05107c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NBfHJ8LxRGrkdpHsdCyUXu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17973,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 16 · 2026-05-22T05:22:58.314Z_

<details><summary>↩ Tool result · `toolu_01MKzdhxSrkvKM2TtNrWhZZH`</summary>

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
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
artifacts/acknowledgements_draft.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b5c435a2-a73c-4cd0-a4eb-6eb7e9a99854"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 18001,
    "tool_uses": 4,
    "duration_ms": 2441
  },
  "last_tool_name": "Bash",
  "uuid": "59146f5e-c490-46c7-9eb1-eda4feb501f4",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01QZztpBUdke3gGYJzq5tJcL`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper -name \"appendix*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "826b6d06-322d-4217-a0bc-4850e5433535",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NBfHJ8LxRGrkdpHsdCyUXu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17973,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 19 · 2026-05-22T05:22:58.687Z_

<details><summary>↩ Tool result · `toolu_01QZztpBUdke3gGYJzq5tJcL`</summary>

```text
find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper’: No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "e62e0cb9-4351-480b-860f-d011152fddef"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/docred_ridge_regression.json",
  "usage": {
    "total_tokens": 21155,
    "tool_uses": 5,
    "duration_ms": 4684
  },
  "last_tool_name": "Read",
  "uuid": "129e977c-cac2-4080-8dd5-a86e56c81d46",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01J8SibUkmgi9fwuHhvnNkwm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "f3a9500a-d141-495c-af0c-4a2ace2a8c70",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QchmN49ej3S3mSe3jW4z8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 17973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3148,
        "ephemeral_1h_input_tokens": 0
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

_source line 22 · 2026-05-22T05:23:00.770Z_

<details><summary>↩ Tool result · `toolu_01J8SibUkmgi9fwuHhvnNkwm`</summary>

```text
1	{
2	  "method": "Ridge regression (analytic from correlation matrix, GCV λ selection)",
3	  "data_source": "exp_docred_bcs_expanded: 110 DocRED batches (96-type pool, count_16+32)",
4	  "n_batches": 110,
5	  "correlation_matrix": {
6	    "r_BCS_accuracy": -0.7602,
7	    "r_centrality_accuracy": -0.7344,
8	    "r_BCS_centrality": 0.9901,
9	    "VIF": 50.8
10	  },
11	  "gcv_selected_alpha": 0.001231,
12	  "r2_ridge": 0.5944,
13	  "standardized_coefficients": {
14	    "bcs_coefficient": -1.5342,
15	    "centrality_coefficient": 0.7837
16	  },
17	  "ols_standardized_coefficients": {
18	    "bcs_coefficient": -1.6785,
19	    "centrality_coefficient": 0.9275,
20	    "r2": 0.5949
21	  },
22	  "ridge_path_at_selected_lambdas": {
23	    "0.01": {
24	      "bcs_coefficient": -1.0219,
25	      "centrality_coefficient": 0.2746
26	    },
27	    "0.1": {
28	      "bcs_coefficient": -0.4749,
29	      "centrality_coefficient": -0.2402
30	    },
31	    "1.0": {
32	      "bcs_coefficient": -0.2627,
33	      "centrality_coefficient": -0.2372
34	    },
35	    "10.0": {
36	      "bcs_coefficient": -0.0636,
37	      "centrality_coefficient": -0.061
38	    },
39	    "100.0": {
40	      "bcs_coefficient": -0.0075,
41	      "centrality_coefficient": -0.0072
42	    }
43	  },
44	  "sign_robustness": {
45	    "bcs_negative_for_all_lambda": true,
46	    "bcs_coef_range": [
47	      -1.6655,
48	      -0.0001
49	    ],
50	    "analytic_proof": "β_BCS = [(1+λ)·r_{BCS,y} − r_{BCS,cent}·r_{cent,y}] / [(1+λ)² − r²_{BCS,cent}]. Numerator = −(1+λ)·0.7602 + 0.7271 = −0.0331 − λ·0.7602, monotonically decreasing in λ and negative at λ=0. Denominator > 0. Hence β_BCS < 0 for all λ ≥ 0."
51	  },
52	  "note": "Analytic ridge from the 3-variable correlation matrix is equivalent to RidgeCV on standardized data for any given λ. GCV replaces k-fold CV. The extreme VIF (50.9) confirms high multicollinearity; ridge stabilizes the coefficients. The BCS coefficient is provably negative for all λ ≥ 0."
53	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c9160d70-cf3d-490c-af0e-17fa072fa683"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/docred_ridge_appendix.tex",
  "usage": {
    "total_tokens": 21156,
    "tool_uses": 6,
    "duration_ms": 4910
  },
  "last_tool_name": "Read",
  "uuid": "2eaa9bc2-c2cb-455d-bf59-299748419dbb",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_016RBh1H9WMNJmwuH1N3TCyR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "20843c41-2fa4-45c1-98ac-d33ba098b946",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QchmN49ej3S3mSe3jW4z8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 17973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3148,
        "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-22T05:23:00.986Z_

<details><summary>↩ Tool result · `toolu_016RBh1H9WMNJmwuH1N3TCyR`</summary>

```text
1	% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)
2	
3	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms
4	the negative direction of the BCS--accuracy relationship even after
5	regularizing for the severe BCS--centrality multicollinearity
6	(VIF\,$\approx$\,50.9).
7	The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
8	($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$).
9	An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
10	\emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge
11	solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at
12	$\lambda{=}0$ and monotonically decreasing thereafter.
13	Given the shrinkage bias inherent to ridge estimation, we interpret only
14	the sign---not the magnitude---of the BCS coefficient as directional
15	evidence that higher schema confusability degrades extraction accuracy,
16	independent of degree centrality.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "94e7606b-7472-4311-bb06-d2991cb32aef"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/fewrel_domain_distribution.json",
  "usage": {
    "total_tokens": 21157,
    "tool_uses": 7,
    "duration_ms": 5154
  },
  "last_tool_name": "Read",
  "uuid": "7f172cde-5d21-4cd7-b61d-774cf28d44f8",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_019GNSXnavXqN8yoy7J9Uqyh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "0ea3cce2-971c-4087-9a7e-bc488937e029",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QchmN49ej3S3mSe3jW4z8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 17973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3148,
        "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-22T05:23:01.231Z_

<details><summary>↩ Tool result · `toolu_019GNSXnavXqN8yoy7J9Uqyh`</summary>

```text
1	{
2	  "domain_classification": {
3	    "country": "geography",
4	    "country of citizenship": "geography",
5	    "country of origin": "geography",
6	    "location": "geography",
7	    "located in the administrative territorial entity": "geography",
8	    "contains administrative territorial entity": "geography",
9	    "headquarters location": "geography",
10	    "location of formation": "geography",
11	    "work location": "geography",
12	    "residence": "geography",
13	    "located in or next to body of water": "geography",
14	    "located on terrain feature": "geography",
15	    "mountain range": "geography",
16	    "mouth of the watercourse": "geography",
17	    "tributary": "geography",
18	    "place served by transport hub": "geography",
19	    "crosses": "geography",
20	    "constellation": "geography",
21	    "applies to jurisdiction": "geography",
22	    "licensed to broadcast to": "geography",
23	    "father": "person",
24	    "mother": "person",
25	    "child": "person",
26	    "sibling": "person",
27	    "spouse": "person",
28	    "occupation": "person",
29	    "religion": "person",
30	    "position held": "person",
31	    "member of political party": "person",
32	    "military rank": "person",
33	    "military branch": "person",
34	    "field of work": "person",
35	    "voice type": "person",
36	    "owned by": "organization",
37	    "subsidiary": "organization",
38	    "operator": "organization",
39	    "manufacturer": "organization",
40	    "developer": "organization",
41	    "publisher": "organization",
42	    "distributor": "organization",
43	    "member of": "organization",
44	    "participating team": "organization",
45	    "participant": "organization",
46	    "league": "organization",
47	    "performer": "creative_work",
48	    "composer": "creative_work",
49	    "director": "creative_work",
50	    "screenwriter": "creative_work",
51	    "after a work by": "creative_work",
52	    "characters": "creative_work",
53	    "genre": "creative_work",
54	    "original language of film or TV show": "creative_work",
55	    "language of work or name": "creative_work",
56	    "original network": "creative_work",
57	    "record label": "creative_work",
58	    "platform": "creative_work",
59	    "notable work": "creative_work",
60	    "instrument": "creative_work",
61	    "movement": "creative_work",
62	    "participant of": "event_temporal",
63	    "follows": "event_temporal",
64	    "followed by": "event_temporal",
65	    "sports season of league or competition": "event_temporal",
66	    "competition class": "event_temporal",
67	    "winner": "event_temporal",
68	    "successful candidate": "event_temporal",
69	    "nominated for": "event_temporal",
70	    "head of government": "event_temporal",
71	    "taxon rank": "science_taxonomy",
72	    "instance of": "science_taxonomy",
73	    "has part": "science_taxonomy",
74	    "part of": "science_taxonomy",
75	    "said to be the same as": "science_taxonomy",
76	    "heritage designation": "science_taxonomy",
77	    "main subject": "science_taxonomy",
78	    "sport": "science_taxonomy",
79	    "operating system": "science_taxonomy",
80	    "occupant": "science_taxonomy",
81	    "architect": "science_taxonomy",
82	    "position played on team": "science_taxonomy"
83	  },
84	  "n_domains": 6,
85	  "n_total_relations": 80,
86	  "high_bcs_batches": {
87	    "n": 25,
88	    "bcs_range": [
89	      0.7907828837633133,
90	      0.8109273569924491
91	    ],
92	    "types_per_batch": 8
93	  },
94	  "low_bcs_batches": {
95	    "n": 25,
96	    "bcs_range": [
97	      0.3562733248940536,
98	      0.366775135908808
99	    ],
100	    "types_per_batch": 8
101	  },
102	  "domain_distribution": {
103	    "high_bcs": {
104	      "creative_work": 0,
105	      "event_temporal": 52,
106	      "geography": 0,
107	      "organization": 32,
108	      "person": 17,
109	      "science_taxonomy": 99
110	    },
111	    "low_bcs": {
112	      "creative_work": 51,
113	      "event_temporal": 30,
114	      "geography": 91,
115	      "organization": 8,
116	      "person": 5,
117	      "science_taxonomy": 15
118	    }
119	  },
120	  "domain_proportions": {
121	    "high_bcs": {
122	      "creative_work": 0.0,
123	      "event_temporal": 0.26,
124	      "geography": 0.0,
125	      "organization": 0.16,
126	      "person": 0.085,
127	      "science_taxonomy": 0.495
128	    },
129	    "low_bcs": {
130	      "creative_work": 0.255,
131	      "event_temporal": 0.15,
132	      "geography": 0.455,
133	      "organization": 0.04,
134	      "person": 0.025,
135	      "science_taxonomy": 0.075
136	    }
137	  },
138	  "chi_squared": {
139	    "statistic": 230.7426,
140	    "p_value": 0.0,
141	    "df": 5
142	  },
143	  "entropy": {
144	    "high_bcs": 1.7328,
145	    "low_bcs": 2.0292,
146	    "max_possible": 2.585,
147	    "normalized_high_bcs": 0.6703,
148	    "normalized_low_bcs": 0.785
149	  },
150	  "interpretation": "Domain composition differs significantly between high- and low-BCS batches (chi2=230.74, p<0.001, df=5). High-BCS batches concentrate on science/taxonomy and event/temporal domains (relations like follows/followed_by, part_of/has_part, member_of, instance_of), while low-BCS batches spread across geography and creative_work domains (country_of_citizenship, composer, original_language_of_film_or_TV_show). However, this domain concentration is an expected property of embedding-based BCS: types within the same domain naturally share more semantic features, yielding higher pairwise cosine similarity. Domain composition is thus a mediator of the BCS\u2013performance relationship, not an independent confound.",
151	  "unique_types_in_low": [
152	    "composer",
153	    "country of citizenship",
154	    "headquarters location",
155	    "located in or next to body of water",
156	    "located on terrain feature",
157	    "military rank",
158	    "mountain range",
159	    "mouth of the watercourse",
160	    "operator",
161	    "original language of film or TV show",
162	    "owned by",
163	    "performer",
164	    "place served by transport hub",
165	    "publisher",
166	    "record label",
167	    "religion",
168	    "residence",
169	    "screenwriter",
170	    "sports season of league or competition",
171	    "successful candidate",
172	    "taxon rank",
173	    "voice type"
174	  ],
175	  "unique_types_in_high": [
176	    "child",
177	    "followed by",
178	    "follows",
179	    "has part",
180	    "instance of",
181	    "main subject",
182	    "member of",
183	    "nominated for",
184	    "occupant",
185	    "operator",
186	    "part of",
187	    "participant of",
188	    "said to be the same as",
189	    "sibling"
190	  ],
191	  "types_overlap": [
192	    "operator"
193	  ],
194	  "latex_appendix": "\\paragraph{Domain Distribution in Extreme-BCS Batches.}\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool.\nThe distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains.\nNormalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains.\nCrucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS.\nDomain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable.\nThe BCS metric intentionally aggregates such semantic overlap into a single predictive score."
195	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "fc900d4e-6f21-4364-886c-778f31322fc6"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/_project/paper/results.tex",
  "usage": {
    "total_tokens": 21158,
    "tool_uses": 8,
    "duration_ms": 5776
  },
  "last_tool_name": "Read",
  "uuid": "56f58afd-333a-4c48-a3a2-9ff8334f92af",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01WV7piyHHwFZcpTXGhbVpGk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/results.tex",
  "offset": 40,
  "limit": 26
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b35df689-38ca-4a8b-a2d3-880fb60c1dd5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QchmN49ej3S3mSe3jW4z8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 17973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3148,
        "ephemeral_1h_input_tokens": 0
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

_source line 31 · 2026-05-22T05:23:01.854Z_

<details><summary>↩ Tool result · `toolu_01WV7piyHHwFZcpTXGhbVpGk`</summary>

```text
40	
41	The correlations are modest: $r^2 \approx 1.3\text{--}1.7\%$, meaning pairwise confusability explains roughly 1.5\% of the variance in type confusion. Other factors---entity frequency, prompt position effects \cite{lost-in-middle-2024}, and type definition quality---jointly account for the remainder. Nevertheless, the signal is robust: both correlations survive bootstrap resampling with CIs bounded well above zero, and replicate across two unrelated embedding spaces (Qwen3 hidden states and MiniLM sentence embeddings).
42	
43	Spearman rank correlations from the SCS validation experiment (exp-015) corroborate these findings. Across all type pairs, Qwen3 yields $\rho = 0.168$ ($p = 7.3 \times 10^{-14}$) and MiniLM yields $\rho = 0.144$ ($p = 1.7 \times 10^{-10}$). Restricting to pairs with nonzero confusion strengthens the association: $\rho = 0.272$ ($p = 5 \times 10^{-5}$) for Qwen3 and $\rho = 0.306$ ($p = 4.6 \times 10^{-6}$) for MiniLM, indicating that among types the model actually confuses, embedding similarity is a stronger predictor.
44	
45	We frame these results as identifying one factor among several that drive type confusion, but the first to be empirically isolated in a controlled zero-shot IE setting.
46	
47	\subsection{BCS-Controlled Experiments}
48	\label{sec:bcs_controlled}
49	
50	To move from correlational to interventional evidence, we fix the type count and vary BCS. Table~\ref{tab:bcs_controlled} reports FewRel accuracy under low-BCS and high-BCS batches at two schema sizes; Figure~\ref{fig:bcs_scaling} visualizes the scaling relationship.
51	
52	\begin{table}[t]
53	\centering
54	\small
55	\begin{tabular}{lcrrrr}
56	\toprule
57	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS Acc} & \textbf{High-BCS Acc} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
58	\midrule
59	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
60	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
61	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
62	\bottomrule
63	\end{tabular}
64	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The confusability gap widens from 9.1\,pp at 16 relations to 31.2\,pp at 80 relations.}
65	\label{tab:bcs_controlled}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "f2b633ca-a74f-41ee-94f6-fc54e0d0af3d"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/_project/paper/experimental_setup.tex",
  "usage": {
    "total_tokens": 21159,
    "tool_uses": 9,
    "duration_ms": 5990
  },
  "last_tool_name": "Read",
  "uuid": "b16c44e6-c6e1-42e3-93ee-273959a1bc49",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01TXnXVJr1iVAWxBbNssnUnf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "344fa3a8-51bf-4416-9a95-f3c44446d918",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QchmN49ej3S3mSe3jW4z8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 17973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3148,
        "ephemeral_1h_input_tokens": 0
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

_source line 34 · 2026-05-22T05:23:02.067Z_

<details><summary>↩ Tool result · `toolu_01TXnXVJr1iVAWxBbNssnUnf`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks: named entity recognition (NER), relation extraction (RE), and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances. Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{MAVEN (ED).}
16	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
17	
18	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{llrrlll}
25	\toprule
26	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
27	\midrule
28	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
29	FewRel & RE & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
30	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
31	\bottomrule
32	\end{tabular}}
33	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
34	\label{tab:datasets}
35	\end{table}
36	
37	\subsection{Schema Confusability Score (SCS)}
38	\label{sec:scs}
39	
40	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
41	\[
42	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
43	\]
44	
45	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
46	\[
47	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
48	\]
49	
50	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2019}, a 384-dimensional general-purpose sentence encoder. Both use type name strings only, without definitions or descriptions, to reflect the information available to the model at inference time.
51	
52	\subsection{Experimental Design}
53	\label{sec:exp_design}
54	
55	We conduct two complementary experimental paradigms.
56	
57	\paragraph{Experiment 1: Count Curves.}
58	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
59	
60	\paragraph{Experiment 2: BCS-Controlled.}
61	We fix the type count and vary the Batch Confusability Score to isolate the effect of inter-type similarity from schema size. For each count level, we construct one low-BCS batch (types with the lowest pairwise similarities), one high-BCS batch (types with the highest pairwise similarities), and 25 random batches (27 total per count level). We run this paradigm on Few-NERD at count$\,\in\{6, 12\}$ and on FewRel at count$\,\in\{8, 16\}$, the latter evaluated on both a 16-relation pool and the full 80-relation pool. For MAVEN, we conduct analogous BCS-controlled experiments at count$\,\in\{6, 12\}$ with 27 batches per level; however, the same-domain nature of MAVEN's FrameNet-derived types introduces a centrality confound that complicates BCS interpretation. We report these results separately in \S\ref{sec:centrality_confound}.
62	
63	\subsection{Evaluation Metrics}
64	\label{sec:metrics}
65	
66	We use task-appropriate metrics that reflect the distinct nature of each extraction problem.
67	
68	\paragraph{NER (Few-NERD): Text-match F1.}
69	A predicted entity is a true positive if the predicted text string exactly matches (case-insensitive) a gold entity text \emph{and} the predicted type matches the gold type. This text-match evaluation operates at the entity level rather than the token level. We report Precision, Recall, and F1.
70	
71	\paragraph{RE (FewRel): Accuracy.}
72	Each sample has exactly one ground-truth relation. A prediction is correct if the predicted relation label exactly matches the gold label. We report Accuracy.
73	
74	\paragraph{ED (MAVEN): Relaxed F1.}
75	A predicted trigger is a true positive if (a)~any token overlap exists between the predicted trigger span and a gold trigger span, \emph{and} (b)~the predicted event type matches the gold event type. This relaxed matching is necessary because event triggers are inherently ambiguous in boundary (e.g., ``was killed'' vs.\ ``killed''). We report Relaxed F1.
76	
77	The choice of different metrics across tasks reflects their structural differences: NER is span-level extraction where precision--recall trade-offs are informative; RE is a classification task where accuracy directly measures correctness; ED combines trigger identification with type classification, requiring relaxed span matching to avoid penalizing legitimate boundary variation.
78	
79	\subsection{Model and Inference}
80	\label{sec:model}
81	
82	\paragraph{Primary model.}
83	We use Qwen3-32B-FP8 \cite{qwen3-2025}, selected for its strong instruction-following capability, native structured JSON output support, and the practical advantage that the FP8-quantized 32B model fits on a single NVIDIA RTX PRO 6000 Blackwell Server Edition (96\,GB). The model is served via vLLM (v0.20.2) \cite{vllm-2023} with \texttt{max\_model\_len=4096} and \texttt{gpu\_memory\_utilization=0.95}. We use a refined prompt template (v2) that includes explicit output format constraints and role instructions; the v1 prompt produced excessive over-prediction, while v2 doubled precision with minimal recall loss. The prompt provides a JSON-formatted schema listing all type names for the current batch; the model outputs structured JSON containing extracted entities, relations, or events. We use greedy decoding (temperature${}\,=\,0$) and a fixed random seed (42) for all batch sampling and bootstrap resampling, ensuring full reproducibility.
84	
85	\paragraph{Statistical estimation.}
86	All key metrics are accompanied by 95\% bootstrap confidence intervals computed from 1{,}000 bootstrap resamples using the percentile method.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "d172ff7a-02aa-4c33-b786-ceaec07041f8"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/_project/paper/dataset_stats.tex",
  "usage": {
    "total_tokens": 21160,
    "tool_uses": 10,
    "duration_ms": 6196
  },
  "last_tool_name": "Read",
  "uuid": "b558ce6c-3111-4013-b332-eaadc493a47d",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01N9aHCRLu2srs6hhpruVB4j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/paper/dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "354898f0-a22a-4466-afca-e16c2ad7bf76",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QchmN49ej3S3mSe3jW4z8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3148,
      "cache_read_input_tokens": 17973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3148,
        "ephemeral_1h_input_tokens": 0
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

_source line 37 · 2026-05-22T05:23:02.278Z_

<details><summary>↩ Tool result · `toolu_01N9aHCRLu2srs6hhpruVB4j`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dataset statistics. \emph{Cross}: schema types span diverse semantic domains. \emph{Same}: types derive from a single ontological field (FrameNet event frames).}
5	\label{tab:datasets}
6	\begin{tabular}{@{}lccrl@{}}
7	\toprule
8	\textbf{Dataset} & \textbf{Task} & \textbf{\#\,Types} & \textbf{Eval.\ Size} & \textbf{Domain} \\
9	\midrule
10	Few-NERD & NER & 66 & 1{,}000 & Cross \\
11	FewRel   & RE  & 80 & 1{,}000 & Cross \\
12	MAVEN    & ED  & 168 & 18{,}904$^\dagger$ & Same \\
13	\bottomrule
14	\end{tabular}
15	\vspace{1mm}\\
16	{\footnotesize $^\dagger$Trigger mentions across 710 documents.}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "e18b9524-4694-4fed-8697-7000ba3063ef"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 29425,
    "tool_uses": 11,
    "duration_ms": 8808
  },
  "last_tool_name": "Bash",
  "uuid": "907b99b8-bac3-4f52-87c5-ef65e5cf57fb",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01Sj7Jtb6Zq95XqvDbiKh3VN`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*bootstrap*\" -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "3457f50f-2325-4df4-8334-cb886d4aa4fa",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SBPjiKnGD9pjd2R4Cys7vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8263,
      "cache_read_input_tokens": 21121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8263,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 29426,
    "tool_uses": 12,
    "duration_ms": 8906
  },
  "last_tool_name": "Bash",
  "uuid": "9d368d42-88ed-49ac-b312-957179f457f8",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01M1WQy97FTbUDZzZyeX4VAc`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"main.tex\" -o -name \"paper.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ff9ecaf2-c420-4033-98c3-544a023ebb64",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SBPjiKnGD9pjd2R4Cys7vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8263,
      "cache_read_input_tokens": 21121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8263,
        "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-22T05:23:04.997Z_

<details><summary>↩ Tool result · `toolu_01Sj7Jtb6Zq95XqvDbiKh3VN`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_ci_20260515T150128_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_exp_fewrel_80pool_16sub_bootstrap_20260516T014220_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_a1_bootstrap_corrected_20260519T184730_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_fix_bootstrap_ci_discrepancy_20260516T022039.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_debug_exp_fewrel_80pool_16sub_bootstrap_20260516T021106.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_ci_20260515T150128.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_a1_bootstrap_corrected_20260519T184730.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_diagnose_exp_fewrel_16rel_bootstrap_20260516T015515_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_reconcile_20260515T152233_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_fix_bootstrap_ci_discrepancy_20260516T022039_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_submit_exp_fewrel_80pool_16sub_bootstrap_20260516T015642.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_submit_exp_fewrel_16rel_bootstrap_20260516T010228.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_split_sample_bootstrap_20260522T045724.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_debug_exp_fewrel_80pool_16sub_bootstrap_20260516T021106_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_exp_fewrel_80pool_16sub_bootstrap_20260516T014220.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_diagnose_exp_fewrel_16rel_bootstrap_20260516T015515.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_split_sample_bootstrap_20260522T045724_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_analysis_bootstrap_reconcile_20260515T152233.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_submit_exp_fewrel_80pool_16sub_bootstrap_20260516T015642_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/worker_analysis_bootstrap_ci_20260515T150128.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "4b515d50-5c13-4e10-bae3-7876d8eedc68"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-22T05:23:05.077Z_

<details><summary>↩ Tool result · `toolu_01M1WQy97FTbUDZzZyeX4VAc`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260516T073533/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T140829/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "2daf796c-1fa2-47ab-b38e-99b828dea5c9"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 31411,
    "tool_uses": 13,
    "duration_ms": 10716
  },
  "last_tool_name": "Read",
  "uuid": "a89c53ba-a1b5-4024-8d58-22aca5ffbd72",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01NLRHzU86W7ZJLS26GAjxEV`</summary>

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
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "6040c84d-58a3-42dd-9952-390f9bd39024",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RR6uEQ9UkBRffWhz6a5qhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 29384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 31412,
    "tool_uses": 14,
    "duration_ms": 10859
  },
  "last_tool_name": "Bash",
  "uuid": "44e258b6-0acc-4644-96ec-2d87d738724e",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_015GfjuimvwtuH9D7jZGXYJe`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "d8ac0298-d1ee-4075-ad50-36e74426d6b2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RR6uEQ9UkBRffWhz6a5qhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 29384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-22T05:23:07.045Z_

<details><summary>↩ Tool result · reported error · `toolu_01NLRHzU86W7ZJLS26GAjxEV`</summary>

```text
File content (26119 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "522ef307-dd5a-4722-adb3-703548e4c364",
  "tool_use_result": "Error: File content (26119 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T05:23:06.993Z_

<details><summary>↩ Tool result · `toolu_015GfjuimvwtuH9D7jZGXYJe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "dbcc5dbd-0cfd-412c-b34e-dfa7ebf41e78"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 31413,
    "tool_uses": 15,
    "duration_ms": 11539
  },
  "last_tool_name": "Bash",
  "uuid": "e3a230de-a0c6-4b91-b8d9-b2354c6fdd0d",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_014aKSQuxbePvUCM9UTVqhqP`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json 2>&1 | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "4483171f-a381-41c1-be8b-d9fc0bf28cad",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RR6uEQ9UkBRffWhz6a5qhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1983,
      "cache_read_input_tokens": 29384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1983,
        "ephemeral_1h_input_tokens": 0
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

_source line 52 · 2026-05-22T05:23:07.680Z_

<details><summary>↩ Tool result · `toolu_014aKSQuxbePvUCM9UTVqhqP`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 4246 May 22 05:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json
-rw-r--r-- 1 ubuntu ubuntu 4246 May 22 05:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "5df31a31-f3ce-4178-9ae5-c8c04b19f94b"
}
```

</details>

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 32423,
    "tool_uses": 16,
    "duration_ms": 13552
  },
  "last_tool_name": "Read",
  "uuid": "f696688c-56fd-4d2c-b1e8-c7ddaa257862",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01CX6VPiUqxY5wmQkd3gdyEY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "f17f2882-120b-41ea-84f2-6616ee85a8f1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D8uRSaF6RZxmDTCeeyWTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 31367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1008,
        "ephemeral_1h_input_tokens": 0
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

_source line 55 · 2026-05-22T05:23:09.632Z_

<details><summary>↩ Tool result · `toolu_01CX6VPiUqxY5wmQkd3gdyEY`</summary>

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
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\,=\,0$) yields residual SD${}\,=\,0.88$\,pp, approximately 18--44\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\,pp) is far inside the $\pm 3$\,pp equivalence margin.
43	
44	\item \textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.
45	
46	\item \textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\ref{app:split-origin}).
47	\item \textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.
48	\end{enumerate}
49	
50	\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.
51	
52	\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.
53	
54	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
55	
56	\bibliography{references}
57	
58	\appendix
59	
60	\section{Additional Figures}
61	\label{sec:appendix_figures}
62	
63	\begin{table}[h]
64	\centering
65	\small
66	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
67	\label{tab:cross_model}
68	\begin{tabular}{lrr}
69	\toprule
70	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
71	\midrule
72	1 & 0.702 & 0.640 \\
73	64 & 0.273 & 0.304 \\
74	\midrule
75	Decline & $-$43\,pp & $-$34\,pp \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	\begin{table}[h]
81	\centering
82	\small
83	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
84	\label{tab:cross_model_bcs}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{crrrrrr}
87	\toprule
88	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
89	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
90	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
91	\midrule
92	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
93	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
94	\bottomrule
95	\end{tabular}}
96	\end{table}
97	
98	\begin{table}[h]
99	\centering
100	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "a46dca4b-68eb-4a0a-924e-5773bb123a1a"
}
```

</details>

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading docs/paper/prompt_appendix.tex",
  "usage": {
    "total_tokens": 32424,
    "tool_uses": 17,
    "duration_ms": 13911
  },
  "last_tool_name": "Read",
  "uuid": "eee9a88d-6e31-494c-a02d-48c23d62baa9",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01RS69WGZXWyRT4zHYr9yavM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "55497782-1c73-4d17-aff6-08a05454c5c6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D8uRSaF6RZxmDTCeeyWTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 31367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1008,
        "ephemeral_1h_input_tokens": 0
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

_source line 58 · 2026-05-22T05:23:09.988Z_

<details><summary>↩ Tool result · `toolu_01RS69WGZXWyRT4zHYr9yavM`</summary>

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
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the following text.
62	Only extract entities of the following types:
63	- {type_1}: {definition_1}
64	- {type_2}: {definition_2}
65	  ...
66	
67	Text: {input_text}
68	\end{lstlisting}
69	\end{small}
70	\vspace{-0.5em}
71	\noindent$\triangleright$~\textbf{Added in v2:}
72	\begin{small}
73	\begin{lstlisting}
74	Only extract entities that clearly match one of the
75	given types. If no entities of these types exist in
76	the text, output an empty list [].
77	\end{lstlisting}
78	\end{small}
79	\vspace{-0.5em}
80	\begin{small}
81	\begin{lstlisting}
82	Output as JSON: [{"text": "...", "type": "..."}]
83	\end{lstlisting}
84	\end{small}
85	
86	\noindent
87	\textbf{v2 constrained-decoding schema:}
88	\begin{small}
89	\begin{lstlisting}
90	{"type": "array",
91	 "items": {"type": "object",
92	   "properties": {
93	     "text": {"type": "string"},
94	     "type": {"type": "string",
95	              "enum": [&lt;sorted_types>]}},
96	   "required": ["text","type"]}}
97	\end{lstlisting}
98	\end{small}
99	
100	\paragraph{v1 $\to$ v2 differences (NER).}
101	\begin{enumerate}[leftmargin=*,itemsep=2pt]
102	\item \textbf{Offset fields removed.} The \texttt{start}/\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\% of predicted offsets were hallucinated (\S\ref{sec:model}).
103	\item \textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \ldots output an empty list~\texttt{[]}'' provides an explicit empty-output path.
104	\end{enumerate}
105	
106	\subsection{Event Detection (MAVEN)}
107	
108	\paragraph{v1 prompt (with character offsets).}
109	
110	\begin{small}
111	\begin{lstlisting}
112	Extract all event triggers from the following text.
113	A trigger is the word or phrase that most clearly
114	expresses the event occurrence. Only extract triggers
115	of the following event types:
116	- {type_1}: {definition_1}
117	- {type_2}: {definition_2}
118	  ...
119	
120	Text: {input_text}
121	
122	Output as JSON: [{"text": "...", "type": "...",
123	                  "start": ..., "end": ...}]
124	\end{lstlisting}
125	\end{small}
126	
127	\paragraph{v2 prompt (text+type only).}
128	
129	\begin{small}
130	\begin{lstlisting}
131	Extract all event triggers from the following text.
132	A trigger is the word or phrase that most clearly
133	expresses the event occurrence. Only extract triggers
134	of the following event types:
135	- {type_1}: {definition_1}
136	- {type_2}: {definition_2}
137	  ...
138	
139	Text: {input_text}
140	\end{lstlisting}
141	\end{small}
142	\vspace{-0.5em}
143	\noindent$\triangleright$~\textbf{Added in v2:}
144	\begin{small}
145	\begin{lstlisting}
146	Only extract triggers that clearly match one of the
147	given event types. If no events of these types exist
148	in the text, output an empty list [].
149	\end{lstlisting}
150	\end{small}
151	\vspace{-0.5em}
152	\begin{small}
153	\begin{lstlisting}
154	Output as JSON: [{"text": "...", "type": "..."}]
155	\end{lstlisting}
156	\end{small}
157	
158	\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').
159	
160	\paragraph{v1 $\to$ v2 differences (ED).}
161	Same two changes as NER: offset fields removed, format constraints added.
162	
163	\subsection{Relation Extraction (FewRel)}
164	
165	RE uses only a v2-style prompt (no offset fields are applicable to classification).
166	
167	\paragraph{Prompt.}
168	
169	\begin{small}
170	\begin{lstlisting}
171	Given the following sentence and two entities,
172	classify the relation between them.
173	
174	Sentence: "{sentence}"
175	Head entity: "{head_entity}"
176	Tail entity: "{tail_entity}"
177	
178	Candidate relations: {type_1}, {type_2}, ...
179	
180	Output a single JSON object:
181	  {"relation": "&lt;relation_type>"}
182	If none of the candidate relations apply, output:
183	  {"relation": "none"}
184	\end{lstlisting}
185	\end{small}
186	
187	\noindent
188	\textbf{Constrained-decoding schema:}
189	\begin{small}
190	\begin{lstlisting}
191	{"type": "object",
192	 "properties": {
193	   "relation": {"type": "string",
194	     "enum": [&lt;sorted_types>, "none"]}},
195	 "required": ["relation"]}
196	\end{lstlisting}
197	\end{small}
198	
199	\subsection{Type Definitions}
200	\label{sec:appendix_type_defs}
201	
202	All prompts include per-type natural-language definitions sourced from the respective dataset documentation:
203	\begin{itemize}[leftmargin=*,itemsep=2pt]
204	\item \textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \citep{fewnerd-2021}.
205	\item \textbf{MAVEN:} 168 event types with FrameNet-based definitions \citep{maven-2020}.
206	\item \textbf{FewRel:} 80 relation types with Wikidata property descriptions \citep{fewrel-2018}.
207	\end{itemize}
208	
209	\noindent Type definitions are injected as ``\texttt{- \{type\_name\}: \{definition\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \S\ref{sec:exp_design}).
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c4c0d32b-60c0-4feb-8d3f-ca0ae0210fd3"
}
```

</details>

---

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading docs/paper/supplementary.tex",
  "usage": {
    "total_tokens": 32425,
    "tool_uses": 18,
    "duration_ms": 14002
  },
  "last_tool_name": "Read",
  "uuid": "d88cd178-2c57-4ac0-a782-d69f4b048ccb",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01Fni1S597PAvvVoNQJW5qfX`</summary>

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
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "97194736-10f3-4310-a6e8-ba2293d1da5b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D8uRSaF6RZxmDTCeeyWTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 31367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1008,
        "ephemeral_1h_input_tokens": 0
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

_source line 61 · 2026-05-22T05:23:10.078Z_

<details><summary>↩ Tool result · `toolu_01Fni1S597PAvvVoNQJW5qfX`</summary>

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
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b4b03410-46c9-4d5e-978e-9e64f9704778"
}
```

</details>

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/split_sample_bootstrap.json",
  "usage": {
    "total_tokens": 32426,
    "tool_uses": 19,
    "duration_ms": 14242
  },
  "last_tool_name": "Read",
  "uuid": "1a6d6968-5fbf-4934-9f49-989fedc95d2a",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01TxBpjuD7y7EsEhYuSwyoj2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "96c522d6-5e96-4ef6-a869-578a668f689d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D8uRSaF6RZxmDTCeeyWTK4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1008,
      "cache_read_input_tokens": 31367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1008,
        "ephemeral_1h_input_tokens": 0
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

_source line 64 · 2026-05-22T05:23:10.320Z_

<details><summary>↩ Tool result · `toolu_01TxBpjuD7y7EsEhYuSwyoj2`</summary>

```text
1	{
2	  "dataset": {
3	    "name": "FewRel combined (exp1=110 + exp2=54 batches, 80-type pool)",
4	    "n_batches": 164,
5	    "n_unique_types": 80,
6	    "original_r": -0.5178,
7	    "original_R2": 0.2681,
8	    "original_p": 1.2502070529685776e-12
9	  },
10	  "instance_sharing": {
11	    "mean_pairwise_overlap": 0.218,
12	    "fraction_pairs_with_overlap": 0.345,
13	    "icc_shared_type_pairs": 0.2119,
14	    "icc_independent_pairs": -0.0137
15	  },
16	  "design_effect": {
17	    "avg_batches_per_type": 21.9,
18	    "DEFF": 5.42,
19	    "effective_n": 30.3,
20	    "nominal_n": 164
21	  },
22	  "slope_standard_errors": {
23	    "slope": -0.1923,
24	    "ols_se": 0.025,
25	    "ols_95ci": [
26	      -0.2412,
27	      -0.1434
28	    ],
29	    "hc1_se": 0.0255,
30	    "hc1_95ci": [
31	      -0.2423,
32	      -0.1423
33	    ],
34	    "hc1_inflation": 1.02,
35	    "cluster_robust_se": 0.0239,
36	    "cluster_robust_95ci": [
37	      -0.2392,
38	      -0.1454
39	    ],
40	    "cluster_robust_inflation": 0.96,
41	    "n_clusters": 81
42	  },
43	  "bootstrap_R2": {
44	    "n_iterations": 10000,
45	    "standard": {
46	      "mean": 0.2731,
47	      "ci_95": [
48	        0.1451,
49	        0.417
50	      ],
51	      "ci_width": 0.2719
52	    },
53	    "cluster": {
54	      "mean": 0.2729,
55	      "ci_95": [
56	        0.1434,
57	        0.4111
58	      ],
59	      "ci_width": 0.2678,
60	      "width_change_pct": -1.5
61	    }
62	  },
63	  "bootstrap_slope": {
64	    "standard": {
65	      "mean": -0.192,
66	      "ci_95": [
67	        -0.2407,
68	        -0.1416
69	      ],
70	      "ci_width": 0.099
71	    },
72	    "cluster": {
73	      "mean": -0.1915,
74	      "ci_95": [
75	        -0.236,
76	        -0.1429
77	      ],
78	      "ci_width": 0.0931,
79	      "width_change_pct": -6.0
80	    }
81	  },
82	  "significance": {
83	    "ols_t": -7.7,
84	    "ols_p": 1.2501111257279263e-12,
85	    "cluster_robust_t": -8.04,
86	    "cluster_robust_p": 7.192690887336539e-12,
87	    "significant_under_cluster_robust": true
88	  },
89	  "robustness_verdict": "ROBUST: BCS-accuracy slope remains significant (p<0.05) under all cluster-robust specifications tested (SE inflation range: 0.96x\u20130.97x). Bootstrap R\u00b2 CI width changes range from -6% to 6%. Despite high design effect (DEFF=5.4) from extensive type sharing, the BCS predictor contains sufficient independent signal across clusters to maintain robust inference.",
90	  "sensitivity_analysis": {
91	    "standard_bootstrap_R2_ci": [
92	      0.142,
93	      0.4193
94	    ],
95	    "standard_bootstrap_R2_width": 0.2774,
96	    "by_threshold": {
97	      "0.1": {
98	        "n_clusters": 83,
99	        "cluster_robust_se": 0.0243,
100	        "se_inflation": 0.97,
101	        "bootstrap_R2_ci": [
102	          0.148,
103	          0.4145
104	        ],
105	        "bootstrap_R2_width": 0.2665,
106	        "p_cluster_robust": 1.1507683694844673e-11,
107	        "width_change_pct": -3.9
108	      },
109	      "0.2": {
110	        "n_clusters": 83,
111	        "cluster_robust_se": 0.0243,
112	        "se_inflation": 0.97,
113	        "bootstrap_R2_ci": [
114	          0.147,
115	          0.4123
116	        ],
117	        "bootstrap_R2_width": 0.2653,
118	        "p_cluster_robust": 1.1507683694844673e-11,
119	        "width_change_pct": -4.3
120	      },
121	      "0.3": {
122	        "n_clusters": 81,
123	        "cluster_robust_se": 0.0239,
124	        "se_inflation": 0.96,
125	        "bootstrap_R2_ci": [
126	          0.1479,
127	          0.411
128	        ],
129	        "bootstrap_R2_width": 0.2631,
130	        "p_cluster_robust": 7.192690887336539e-12,
131	        "width_change_pct": -5.1
132	      },
133	      "0.5": {
134	        "n_clusters": 80,
135	        "cluster_robust_se": 0.0239,
136	        "se_inflation": 0.96,
137	        "bootstrap_R2_ci": [
138	          0.1507,
139	          0.4121
140	        ],
141	        "bootstrap_R2_width": 0.2614,
142	        "p_cluster_robust": 7.636336007976752e-12,
143	        "width_change_pct": -5.8
144	      },
145	      "0.7": {
146	        "n_clusters": 80,
147	        "cluster_robust_se": 0.0239,
148	        "se_inflation": 0.96,
149	        "bootstrap_R2_ci": [
150	          0.1455,
151	          0.4088
152	        ],
153	        "bootstrap_R2_width": 0.2633,
154	        "p_cluster_robust": 7.636336007976752e-12,
155	        "width_change_pct": -5.1
156	      },
157	      "0.9": {
158	        "n_clusters": 80,
159	        "cluster_robust_se": 0.0239,
160	        "se_inflation": 0.96,
161	        "bootstrap_R2_ci": [
162	          0.1454,
163	          0.4134
164	        ],
165	        "bootstrap_R2_width": 0.268,
166	        "p_cluster_robust": 7.636336007976752e-12,
167	        "width_change_pct": -3.4
168	      }
169	    }
170	  }
171	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "86c7fad6-b5df-403f-bf64-57087936e9db"
}
```

</details>

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading docs/paper/results.tex",
  "usage": {
    "total_tokens": 40407,
    "tool_uses": 20,
    "duration_ms": 16920
  },
  "last_tool_name": "Read",
  "uuid": "15cd3645-181d-4954-bd9d-24dc2cc648a3",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01FBpA3NH7frBkoSutbLcXM2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 40,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c7638715-76b4-4494-9e4a-e97bcfc0ef61",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013dVt4JLnWA3WompTU6Qq82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7973,
      "cache_read_input_tokens": 32375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 67 · 2026-05-22T05:23:13.000Z_

<details><summary>↩ Tool result · `toolu_01FBpA3NH7frBkoSutbLcXM2`</summary>

```text
40	\label{fig:error_taxonomy}
41	\end{figure*}
42	
43	\subsection{BCS-Controlled Experiments}
44	\label{sec:bcs_controlled}
45	
46	\looseness=-1
47	On FewRel, BCS explains ${\sim}$22\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\,=\,1.18$). DocRED partial correlation ($r_{\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\,=\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\ref{sec:appendix_partial_corr}, Table~\ref{tab:partial_corr}).} the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
48	
49	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (95\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
50	
51	\paragraph{Document-level RE (DocRED).}
52	The effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\footnote{DocRED uses 5 batches per count level (vs.\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\,pp at count 16 ($\rho = -0.762$, 95\% CI [$-$0.88, $-$0.58]) and $-$15.7\,pp at count 32 ($\rho = -0.693$, 95\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\,=\,50.9$): semipartial $R^2_{\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\% of the explained variance is shared with centrality. Given VIF${}\,=\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\,=\,1.18$).
53	
54	\paragraph{Within-pool controlled comparison.}
55	\label{sec:within_pool}
56	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
57	
58	\paragraph{Practical magnitude.}
59	\label{sec:practical_magnitude}
60	\looseness=-1
61	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\text{BCS}} = 0.056$ after centrality; Appendix~\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The amplification from pairwise $r^2 \approx 1.5\%$ to batch-level $R^2 \approx 22\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\sim}3\times$ amplification illustrated by Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}).
62	
63	\paragraph{Cross-model validation.}
64	\looseness=-1
65	The effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap (Table~\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\Delta = -17.6$\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \to -0.42$, $p = 0.22$; Spearman: $\rho = -0.40 \to -0.18$, $p = 0.64$; Appendix~\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\ref{tab:cross_model_ner_null}).
66	
67	\paragraph{Prompt sensitivity.}
68	\looseness=-1
69	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\ref{sec:appendix_fewshot_bcs}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "d7810de7-327e-4dee-af31-1d1fb4134a27"
}
```

</details>

---

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running grep -n \"ridge\" /home/ubuntu/.agent-ml-research-i…",
  "usage": {
    "total_tokens": 40411,
    "tool_uses": 21,
    "duration_ms": 17166
  },
  "last_tool_name": "Bash",
  "uuid": "a4049cdd-b399-43f0-b741-ae8aab5a6fe5",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01TXYmaefQP32GbDexATZecw`</summary>

```json
{
  "command": "grep -n \"ridge\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "0336222a-76ab-4169-b34c-4937b2693e7e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013dVt4JLnWA3WompTU6Qq82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7973,
      "cache_read_input_tokens": 32375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 70 · 2026-05-22T05:23:13.289Z_

<details><summary>↩ Tool result · `toolu_01TXYmaefQP32GbDexATZecw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "31a5787f-4933-4c43-98b3-ab4721f5cc59"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running grep -n \"appendix\" /home/ubuntu/.agent-ml-researc…",
  "usage": {
    "total_tokens": 40415,
    "tool_uses": 22,
    "duration_ms": 17424
  },
  "last_tool_name": "Bash",
  "uuid": "eb21c815-d62e-4f88-a81f-d3ce5381153f",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01EF75ycMfQ55ZW6jrzH9ub4`</summary>

```json
{
  "command": "grep -n \"appendix\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "420aee47-7da0-41a1-a3da-344bd3b73f48",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013dVt4JLnWA3WompTU6Qq82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7973,
      "cache_read_input_tokens": 32375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7973,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 73 · 2026-05-22T05:23:13.550Z_

<details><summary>↩ Tool result · `toolu_01EF75ycMfQ55ZW6jrzH9ub4`</summary>

```text
40:\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
42:\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\,=\,0$) yields residual SD${}\,=\,0.88$\,pp, approximately 18--44\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\,pp) is far inside the $\pm 3$\,pp equivalence margin.
58:\appendix
61:\label{sec:appendix_figures}
156:\label{sec:appendix_sdgd}
200:\label{sec:appendix_routing}
227:\label{sec:appendix_factorial}
263:\label{sec:appendix_within_pool}
268:\label{sec:appendix_residualized_bcs}
309:\label{sec:appendix_partial_corr}
328:As Table~\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
331:\label{sec:appendix_ner_power}
336:\label{sec:appendix_batch_composition}
357:\input{prompt_appendix}
360:\label{sec:appendix_prompt_sensitivity}
362:We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
374:\label{sec:appendix_prompt_variants}
402:\label{sec:appendix_bcs_sensitivity}
528:\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
547:The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "3943458f-db0e-43cf-8271-aafb4e0f3021"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 44111,
    "tool_uses": 23,
    "duration_ms": 19917
  },
  "last_tool_name": "Read",
  "uuid": "03c1c0fd-0f77-400e-b0e5-4d7aede69aee",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_013QQ3rNRpaZ4EZizyLUPzRy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 300,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "5fe3229f-153f-4dc3-bcd3-311261a6296a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JQnLnfPMLqChzppchM7D7w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3694,
      "cache_read_input_tokens": 40348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3694,
        "ephemeral_1h_input_tokens": 0
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

_source line 76 · 2026-05-22T05:23:15.995Z_

<details><summary>↩ Tool result · `toolu_013QQ3rNRpaZ4EZizyLUPzRy`</summary>

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
330	\subsection{NER BCS-Null Power Analysis}
331	\label{sec:appendix_ner_power}
332	
333	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
334	
335	\section{Batch Composition Results}
336	\label{sec:appendix_batch_composition}
337	
338	\begin{table}[h]
339	\centering
340	\small
341	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
342	\label{tab:batch_composition}
343	\resizebox{\columnwidth}{!}{%
344	\begin{tabular}{@{}lcc@{}}
345	\toprule
346	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
347	\midrule
348	Single-pass (80 types) & 0.504 & 0.557 \\
349	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
350	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
351	\bottomrule
352	\end{tabular}}
353	\end{table}
354	
355	See the accompanying discussion in \S\ref{sec:sdgd}.
356	
357	\input{prompt_appendix}
358	
359	\section{Prompt Version Sensitivity Analysis}
360	\label{sec:appendix_prompt_sensitivity}
361	
362	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
363	
364	\paragraph{RE (FewRel).}
365	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (95\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
366	
367	\paragraph{NER (Few-NERD).}
368	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
369	
370	\paragraph{Interpretation.}
371	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
372	
373	\subsection{Cross-Prompt-Variant BCS Correlation}
374	\label{sec:appendix_prompt_variants}
375	
376	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\ref{tab:prompt_variants}).
377	
378	\begin{table}[h]
379	\centering
380	\small
381	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
382	\label{tab:prompt_variants}
383	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrr}
384	\toprule
385	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
386	\midrule
387	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
388	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
389	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
390	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
391	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
392	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
393	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
394	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
395	\bottomrule
396	\end{tabular}}
397	\end{table}
398	
399	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "cfa77ada-ea53-4832-bc29-5ec806543967"
}
```

</details>

---

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 47537,
    "tool_uses": 24,
    "duration_ms": 24568
  },
  "last_tool_name": "Bash",
  "uuid": "6b22b99e-c42c-4a1c-a65e-041632af5371",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01KLSCvaGkZEsVP4b4YzJtYT`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts -name \"*bootstrap*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "9f9d28bb-b99f-45b3-ab62-732472591f8a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DFzz1JQGN4un2pdC6dQnar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3426,
      "cache_read_input_tokens": 44042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3426,
        "ephemeral_1h_input_tokens": 0
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

_source line 79 · 2026-05-22T05:23:20.690Z_

<details><summary>↩ Tool result · `toolu_01KLSCvaGkZEsVP4b4YzJtYT`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/w3_cluster_bootstrap_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/data/split_sample_bootstrap.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/data/bootstrap_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/bootstrap_analysis.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "e7a6a4ff-d728-4590-ad8f-985d0d1ce4e6"
}
```

</details>

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Reading artifacts/fewrel_v2_bcs/bootstrap_ci.json",
  "usage": {
    "total_tokens": 47538,
    "tool_uses": 25,
    "duration_ms": 24806
  },
  "last_tool_name": "Read",
  "uuid": "0fc58d8e-75f1-4ea6-b4f9-704a45b26f3b",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Read · `toolu_01J8k3KKEXiMf3udt7FzFMro`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "3b8b2648-cc92-4a45-980c-288553598162",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DFzz1JQGN4un2pdC6dQnar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3426,
      "cache_read_input_tokens": 44042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3426,
        "ephemeral_1h_input_tokens": 0
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

_source line 82 · 2026-05-22T05:23:20.887Z_

<details><summary>↩ Tool result · `toolu_01J8k3KKEXiMf3udt7FzFMro`</summary>

```text
1	{
2	  "delta_pp": 7.92,
3	  "ci_lower_pp": -5.21,
4	  "ci_upper_pp": 21.46,
5	  "low_mean_acc": 0.8042,
6	  "high_mean_acc": 0.725,
7	  "low_accs": [0.8333, 0.8125, 0.875, 0.8229, 0.6771],
8	  "high_accs": [0.7708, 0.7188, 0.7083, 0.9271, 0.5],
9	  "low_bcs_values": [0.4715, 0.6465, 0.6653, 0.6724, 0.6742],
10	  "high_bcs_values": [0.7778, 0.7908, 0.8201, 0.8226, 0.9706],
11	  "n_bootstrap": 10000
12	}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ce516577-c6fe-491c-ad81-e23648e596c5"
}
```

</details>

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 48423,
    "tool_uses": 26,
    "duration_ms": 27157
  },
  "last_tool_name": "Bash",
  "uuid": "f2003df6-dc15-49cc-a90e-3f40ade0949d",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01LA35PM7iw7pPTwDwPkZAp7`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "520da1d2-1179-436c-8b94-1396cd696e13",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01853kwphgBQ7As6qCxtrw6k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 47468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 882,
        "ephemeral_1h_input_tokens": 0
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

_source line 85 · 2026-05-22T05:23:23.281Z_

<details><summary>↩ Tool result · `toolu_01LA35PM7iw7pPTwDwPkZAp7`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 1.2K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 6.3K May 21 03:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
-rw-r--r-- 1 ubuntu ubuntu  172 May 15 20:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu 1.2K May 22 05:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  11K May 21 21:49 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
-rw-r--r-- 1 ubuntu ubuntu 5.2K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  72K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu 6.4K May 20 08:59 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
-rw-r--r-- 1 ubuntu ubuntu 4.2K May 22 04:39 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  15K May 22 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
-rw-r--r-- 1 ubuntu ubuntu  643 May 22 05:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
-rw-r--r-- 1 ubuntu ubuntu  444 May 17 10:29 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "7b98a589-3c85-4260-a6a8-3d47b3edb723"
}
```

</details>

---

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a11b25b0956e1f873",
  "tool_use_id": "toolu_01Swotv1rFyWeqhvN6F4wTDR",
  "status": "completed",
  "output_file": "",
  "summary": "Find appendix and artifact files",
  "usage": {
    "total_tokens": 49398,
    "tool_uses": 26,
    "duration_ms": 47549
  },
  "uuid": "9b1f66ac-c3df-4f7e-8e5f-71260d87ba66",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool result

_source line 87 · 2026-05-22T05:23:43.623Z_

<details><summary>↩ Tool result · `toolu_01Swotv1rFyWeqhvN6F4wTDR`</summary>

```text
Perfect! Now I have all the information needed. Let me compile the comprehensive report:

## Summary of Found Files

### 1. Paper TEX Files (in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/)

**Main Paper Structure:**
- **main.tex** - Main paper document (72 KB). Includes \input directives for:
  - abstract.tex
  - introduction.tex
  - related_work.tex
  - experimental_setup.tex
  - results.tex
  - sdgd_negative.tex
  - discussion.tex
  - prompt_appendix.tex (via \input{prompt_appendix} at line 357)
  - Contains appendix sections starting at line 58 with \appendix directive

**Appendix Files Found:**
- **prompt_appendix.tex** (6.4 KB) - Complete prompt templates for all three extraction tasks (NER, ED, RE)
- Paper includes embedded appendix sections in main.tex covering:
  - Additional Figures (sec:appendix_figures)
  - SDGD failure analysis (sec:appendix_sdgd)
  - Routing analysis (sec:appendix_routing)
  - Factorial interaction (sec:appendix_factorial)
  - Within-pool controlled comparison (sec:appendix_within_pool)
  - Residualized BCS (sec:appendix_residualized_bcs)
  - Partial correlation / Degree centrality control (sec:appendix_partial_corr) - This section references the ridge regression!
  - NER BCS-null power analysis (sec:appendix_ner_power)
  - Batch composition results (sec:appendix_batch_composition)
  - Prompt version sensitivity (sec:appendix_prompt_sensitivity)
  - Cross-prompt-variant analysis (sec:appendix_prompt_variants)

**Other Paper Files:**
- abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, discussion.tex, sdgd_negative.tex, checklist.tex, conclusion.tex, supplementary.tex

### 2. Results TEX Files (in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/...)

- **/artifacts/_project/paper/results.tex** - Copy of results section
- **/artifacts/paper/tables/dataset_stats.tex** - Dataset statistics table
- **/artifacts/paper/dataset_stats.tex** - Dataset statistics (artifacts copy)
- **/artifacts/paper/experimental_setup.tex** - Experimental setup (artifacts copy)
- **/artifacts/paper/sdgd_negative.tex** - SDGD negative results (artifacts copy)

### 3. Ridge Regression Files

**DocRED Ridge Regression Appendix:**
- **/artifacts/docred_ridge_appendix.tex** (17 lines) - Appendix E.1 discussing ridge regression under multicollinearity

**Content:** The appendix discusses ridge regression (GCV with λ=0.001) on 110 DocRED batches, confirming the negative direction of the BCS-accuracy relationship even after regularizing for severe multicollinearity (VIF≈50.9). Key findings:
- Standardized BCS coefficient: -1.53 (centrality: 0.78, R²=0.594)
- Analytic proof that β_BCS < 0 for all λ ≥ 0
- Interprets sign rather than magnitude as directional evidence

**DocRED Ridge Regression Data:**
- **/artifacts/docred_ridge_regression.json** (53 lines) - Full statistical analysis including:
  - Method: Ridge regression with GCV λ selection
  - Data: 110 DocRED batches (96-type pool)
  - Correlation matrix (r_BCS_accuracy: -0.7602, r_centrality_accuracy: -0.7344, VIF: 50.8)
  - GCV selected α: 0.001231
  - R² Ridge: 0.5944
  - Standardized coefficients and ridge path analysis
  - Sign robustness proof: β_BCS negative for all λ ≥ 0

### 4. FewRel Domain Distribution Files

- **/artifacts/fewrel_domain_distribution.json** (195 lines) - Comprehensive domain analysis:
  - 80 FewRel relations classified into 6 semantic domains
  - Domain distribution comparison between high-BCS (n=25) and low-BCS (n=25) batches
  - Chi-squared test: χ²=230.74, p<0.001
  - High-BCS batches concentrate on science/taxonomy (49.5%) and event/temporal (26.0%)
  - Low-BCS batches spread across geography (45.5%) and creative_work (25.5%)
  - Includes detailed LaTeX appendix text
  - Interpretation: Domain concentration acts as a mediator, not an independent confound

### 5. Bootstrap-Related Result Files

Located in /artifacts/:
- **/artifacts/split_sample_bootstrap.json** (171 lines) - Cluster-robust bootstrap analysis of FewRel BCS-accuracy slope
  - 164 total batches from exp1+exp2
  - Original r: -0.5178, R²: 0.2681, p<0.001
  - Instance sharing analysis showing DEFF=5.42
  - Cluster-robust inference maintains significance despite high design effect
  - Bootstrap R² CI: [0.1451, 0.417]
  - Verdict: ROBUST

- **/artifacts/fewrel_v2_bcs/bootstrap_ci.json** (12 lines) - Bootstrap CI for v2 prompt:
  - Delta (low-BCS to high-BCS): 7.92 pp
  - CI: [-5.21, 21.46] pp
  - N bootstrap: 10,000

- **/artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json**
- **/artifacts/exp_docred_confusability/bootstrap_analysis.json**
- **/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json**

### 6. Results.tex Content (Lines 40-65)

The results.tex file (in both /docs/paper/ and /artifacts/) at lines 52-56 contains key references:
- Line 52: "Ridge regression confirms the negative direction under regularization (Appendix~\ref{sec:appendix_partial_corr})."
- This directly references the ridge regression appendix section
- The context discusses DocRED's VIF=50.9 multicollinearity issue and how semipartial R² shows 90% of variance is shared with centrality
- Ridge regression (with analytic proof) validates the negative BCS-accuracy relationship despite the severe collinearity

### File Path Summary

All found files with full absolute paths:

**TEX Files (Main Paper):**
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex

**Appendix TEX Files:**
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex

**JSON Data Files:**
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json
8. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json

**Additional Bootstrap Result Files:**
9. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json
10. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/bootstrap_analysis.json
11. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b0e4b434-66b1-4044-a0d4-be289853bfaa",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to find the following files in this project:\n\n1. The appendix tex file(s) in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/ - look for appendix*.tex files\n2. The main.tex file structure to understand how appendix is included\n3. In /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/, find:\n   - docred_ridge_regression.json\n   - docred_ridge_appendix.tex\n   - Any bootstrap-related result files\n   - fewrel_domain_distribution.json\n4. results.tex around line 52 to see the ridge regression reference\n\nList all found files with their full paths. For the tex files, read their contents. For the JSON files, read their contents too. For results.tex, read lines 40-65.",
    "agentId": "a11b25b0956e1f873",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile the comprehensive report:\n\n## Summary of Found Files\n\n### 1. Paper TEX Files (in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/)\n\n**Main Paper Structure:**\n- **main.tex** - Main paper document (72 KB). Includes \\input directives for:\n  - abstract.tex\n  - introduction.tex\n  - related_work.tex\n  - experimental_setup.tex\n  - results.tex\n  - sdgd_negative.tex\n  - discussion.tex\n  - prompt_appendix.tex (via \\input{prompt_appendix} at line 357)\n  - Contains appendix sections starting at line 58 with \\appendix directive\n\n**Appendix Files Found:**\n- **prompt_appendix.tex** (6.4 KB) - Complete prompt templates for all three extraction tasks (NER, ED, RE)\n- Paper includes embedded appendix sections in main.tex covering:\n  - Additional Figures (sec:appendix_figures)\n  - SDGD failure analysis (sec:appendix_sdgd)\n  - Routing analysis (sec:appendix_routing)\n  - Factorial interaction (sec:appendix_factorial)\n  - Within-pool controlled comparison (sec:appendix_within_pool)\n  - Residualized BCS (sec:appendix_residualized_bcs)\n  - Partial correlation / Degree centrality control (sec:appendix_partial_corr) - This section references the ridge regression!\n  - NER BCS-null power analysis (sec:appendix_ner_power)\n  - Batch composition results (sec:appendix_batch_composition)\n  - Prompt version sensitivity (sec:appendix_prompt_sensitivity)\n  - Cross-prompt-variant analysis (sec:appendix_prompt_variants)\n\n**Other Paper Files:**\n- abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, discussion.tex, sdgd_negative.tex, checklist.tex, conclusion.tex, supplementary.tex\n\n### 2. Results TEX Files (in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/...)\n\n- **/artifacts/_project/paper/results.tex** - Copy of results section\n- **/artifacts/paper/tables/dataset_stats.tex** - Dataset statistics table\n- **/artifacts/paper/dataset_stats.tex** - Dataset statistics (artifacts copy)\n- **/artifacts/paper/experimental_setup.tex** - Experimental setup (artifacts copy)\n- **/artifacts/paper/sdgd_negative.tex** - SDGD negative results (artifacts copy)\n\n### 3. Ridge Regression Files\n\n**DocRED Ridge Regression Appendix:**\n- **/artifacts/docred_ridge_appendix.tex** (17 lines) - Appendix E.1 discussing ridge regression under multicollinearity\n\n**Content:** The appendix discusses ridge regression (GCV with λ=0.001) on 110 DocRED batches, confirming the negative direction of the BCS-accuracy relationship even after regularizing for severe multicollinearity (VIF≈50.9). Key findings:\n- Standardized BCS coefficient: -1.53 (centrality: 0.78, R²=0.594)\n- Analytic proof that β_BCS < 0 for all λ ≥ 0\n- Interprets sign rather than magnitude as directional evidence\n\n**DocRED Ridge Regression Data:**\n- **/artifacts/docred_ridge_regression.json** (53 lines) - Full statistical analysis including:\n  - Method: Ridge regression with GCV λ selection\n  - Data: 110 DocRED batches (96-type pool)\n  - Correlation matrix (r_BCS_accuracy: -0.7602, r_centrality_accuracy: -0.7344, VIF: 50.8)\n  - GCV selected α: 0.001231\n  - R² Ridge: 0.5944\n  - Standardized coefficients and ridge path analysis\n  - Sign robustness proof: β_BCS negative for all λ ≥ 0\n\n### 4. FewRel Domain Distribution Files\n\n- **/artifacts/fewrel_domain_distribution.json** (195 lines) - Comprehensive domain analysis:\n  - 80 FewRel relations classified into 6 semantic domains\n  - Domain distribution comparison between high-BCS (n=25) and low-BCS (n=25) batches\n  - Chi-squared test: χ²=230.74, p<0.001\n  - High-BCS batches concentrate on science/taxonomy (49.5%) and event/temporal (26.0%)\n  - Low-BCS batches spread across geography (45.5%) and creative_work (25.5%)\n  - Includes detailed LaTeX appendix text\n  - Interpretation: Domain concentration acts as a mediator, not an independent confound\n\n### 5. Bootstrap-Related Result Files\n\nLocated in /artifacts/:\n- **/artifacts/split_sample_bootstrap.json** (171 lines) - Cluster-robust bootstrap analysis of FewRel BCS-accuracy slope\n  - 164 total batches from exp1+exp2\n  - Original r: -0.5178, R²: 0.2681, p<0.001\n  - Instance sharing analysis showing DEFF=5.42\n  - Cluster-robust inference maintains significance despite high design effect\n  - Bootstrap R² CI: [0.1451, 0.417]\n  - Verdict: ROBUST\n\n- **/artifacts/fewrel_v2_bcs/bootstrap_ci.json** (12 lines) - Bootstrap CI for v2 prompt:\n  - Delta (low-BCS to high-BCS): 7.92 pp\n  - CI: [-5.21, 21.46] pp\n  - N bootstrap: 10,000\n\n- **/artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json**\n- **/artifacts/exp_docred_confusability/bootstrap_analysis.json**\n- **/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json**\n\n### 6. Results.tex Content (Lines 40-65)\n\nThe results.tex file (in both /docs/paper/ and /artifacts/) at lines 52-56 contains key references:\n- Line 52: \"Ridge regression confirms the negative direction under regularization (Appendix~\\ref{sec:appendix_partial_corr}).\"\n- This directly references the ridge regression appendix section\n- The context discusses DocRED's VIF=50.9 multicollinearity issue and how semipartial R² shows 90% of variance is shared with centrality\n- Ridge regression (with analytic proof) validates the negative BCS-accuracy relationship despite the severe collinearity\n\n### File Path Summary\n\nAll found files with full absolute paths:\n\n**TEX Files (Main Paper):**\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex\n\n**Appendix TEX Files:**\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex\n\n**JSON Data Files:**\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json\n8. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_v2_bcs/bootstrap_ci.json\n\n**Additional Bootstrap Result Files:**\n9. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/d037_statistical_analyses/w3_cluster_bootstrap_results.json\n10. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_docred_confusability/bootstrap_analysis.json\n11. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/exp_fewrel_v2_bcs_controlled/data/bootstrap_ci.json"
      }
    ],
    "totalDurationMs": 47551,
    "totalTokens": 51529,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 48350,
      "output_tokens": 2199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 2199,
          "cache_read_input_tokens": 48350,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 976,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 14,
      "searchCount": 3,
      "bashCount": 9,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

<details><summary>Logged reasoning block</summary>

```text
The paper directory seems to be at `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/` rather than `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/`. Let me check both paths and read the actual appendix section in main.tex to understand where to add the new content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b4f7e18c-43c6-49b2-8b88-382fbef7870a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYdjtgVDRYmSSmPamknyy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

_source line 89_

The paper is at `docs/paper/`, not `paper/`. Let me read the key files now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "0ee91a95-5309-4a7e-99a9-05db446104c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYdjtgVDRYmSSmPamknyy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

_source line 90_

<details open><summary>🔧 Tool call — Glob · `toolu_017iCb4g6QjeuxYBaogoTkU8`</summary>

```json
{
  "pattern": "**/paper/main.tex",
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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "f97b4d2b-6fde-4d70-b4ed-b432b955b977",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYdjtgVDRYmSSmPamknyy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

_source line 91 · 2026-05-22T05:23:52.373Z_

<details><summary>↩ Tool result · `toolu_017iCb4g6QjeuxYBaogoTkU8`</summary>

```text
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b4f5fc82-94c3-4331-954b-ffc8f1f3c082",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex"
    ],
    "durationMs": 26,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Read · `toolu_012tdd8RaFUUR399SpnQjfQg`</summary>

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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "37da4eaa-c537-41fe-8e0c-ec6b8e053c60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lk6uaSTkhs1ja64Zcv2gFd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 27007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
      },
      "output_tokens": 65,
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

_source line 93 · 2026-05-22T05:23:55.229Z_

<details><summary>↩ Tool result · reported error · `toolu_012tdd8RaFUUR399SpnQjfQg`</summary>

```text
File content (26119 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "af0519f2-11e8-4403-94e7-fca14bd49fbe",
  "tool_use_result": "Error: File content (26119 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01X1DaEBvpcWcmHML2Tv7fNL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 0,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ab563c19-78ff-4e66-8bf9-923b398c7bb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dFD3cWu3BQ81goTESSsVM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 27264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 148
      },
      "output_tokens": 65,
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

_source line 95 · 2026-05-22T05:23:58.377Z_

<details><summary>↩ Tool result · `toolu_01X1DaEBvpcWcmHML2Tv7fNL`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "134c4f5f-a10c-4b81-8c57-33f59d9498ef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]",
      "numLines": 80,
      "startLine": 0,
      "totalLines": 905
    }
  }
}
```

</details>

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Grep · `toolu_012Ph612uScmEAqRqj2d159h`</summary>

```json
{
  "pattern": "sec:appendix_partial_corr",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "4734a268-6147-4bc1-93b5-2cddf7a2b687",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4oLgA7ZyWj4aqRnxgEX7c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2209,
      "cache_read_input_tokens": 27412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2209
      },
      "output_tokens": 51,
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

_source line 97 · 2026-05-22T05:24:01.668Z_

<details><summary>↩ Tool result · `toolu_012Ph612uScmEAqRqj2d159h`</summary>

```text
docs/paper/main.tex:309:\label{sec:appendix_partial_corr}
docs/paper/results.tex:47:[Omitted long matching line]
docs/paper/results.tex:52:[Omitted long matching line]
docs/paper/results.tex:61:[Omitted long matching line]
docs/paper/main.aux:1593:\newlabel{sec:appendix_partial_corr}{{E.1}{16}{Partial Correlation: Controlling for Degree Centrality}{subsection.E.1}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "09218e9b-6a65-4fd1-8ccd-8d904d5320e3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:309:\\label{sec:appendix_partial_corr}\ndocs/paper/results.tex:47:[Omitted long matching line]\ndocs/paper/results.tex:52:[Omitted long matching line]\ndocs/paper/results.tex:61:[Omitted long matching line]\ndocs/paper/main.aux:1593:\\newlabel{sec:appendix_partial_corr}{{E.1}{16}{Partial Correlation: Controlling for Degree Centrality}{subsection.E.1}{}}",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 98_

Now let me read the appendix section around `sec:appendix_partial_corr` and the artifact files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "f50c0e1d-c725-4860-9cc1-eb2fbd9007c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUWvRA4tp5oKrhwCK6HqF3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 29621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 99_

<details open><summary>🔧 Tool call — Read · `toolu_01PF4zaxEZGpbubY9P1JoVd6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 300,
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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "f750cb7b-9706-45d0-af58-413fc70c7b2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AUWvRA4tp5oKrhwCK6HqF3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 29621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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

_source line 100 · 2026-05-22T05:24:04.972Z_

<details><summary>↩ Tool result · `toolu_01PF4zaxEZGpbubY9P1JoVd6`</summary>

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
330	\subsection{NER BCS-Null Power Analysis}
331	\label{sec:appendix_ner_power}
332	
333	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
334	
335	\section{Batch Composition Results}
336	\label{sec:appendix_batch_composition}
337	
338	\begin{table}[h]
339	\centering
340	\small
341	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
342	\label{tab:batch_composition}
343	\resizebox{\columnwidth}{!}{%
344	\begin{tabular}{@{}lcc@{}}
345	\toprule
346	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
347	\midrule
348	Single-pass (80 types) & 0.504 & 0.557 \\
349	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
350	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
351	\bottomrule
352	\end{tabular}}
353	\end{table}
354	
355	See the accompanying discussion in \S\ref{sec:sdgd}.
356	
357	\input{prompt_appendix}
358	
359	\section{Prompt Version Sensitivity Analysis}
360	\label{sec:appendix_prompt_sensitivity}
361	
362	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
363	
364	\paragraph{RE (FewRel).}
365	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (95\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
366	
367	\paragraph{NER (Few-NERD).}
368	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
369	
370	\paragraph{Interpretation.}
371	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
372	
373	\subsection{Cross-Prompt-Variant BCS Correlation}
374	\label{sec:appendix_prompt_variants}
375	
376	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\ref{tab:prompt_variants}).
377	
378	\begin{table}[h]
379	\centering
380	\small
381	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
382	\label{tab:prompt_variants}
383	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrr}
384	\toprule
385	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
386	\midrule
387	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
388	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
389	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
390	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
391	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
392	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
393	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
394	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
395	\bottomrule
396	\end{tabular}}
397	\end{table}
398	
399	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "637175a7-36c6-439a-ab68-69ee6997a6eb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.",
      "numLines": 100,
      "startLine": 300,
      "totalLines": 905
    }
  }
}
```

</details>

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Read · `toolu_01HKHPHF6wqAnMyaoEWEJEXA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 399,
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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "3c63a1f1-6af6-4b33-bc26-43297232f6b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NhKJsna7EPW8bQdYYgGbfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3423,
      "cache_read_input_tokens": 29908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3423
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

_source line 102 · 2026-05-22T05:24:08.153Z_

<details><summary>↩ Tool result · `toolu_01HKHPHF6wqAnMyaoEWEJEXA`</summary>

```text
399	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
400	
401	\section{BCS Aggregation Sensitivity}
402	\label{sec:appendix_bcs_sensitivity}
403	
404	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\ref{tab:bcs_aggregation}).
405	
406	\begin{table}[h]
407	\centering
408	\small
409	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
410	\label{tab:bcs_aggregation}
411	\resizebox{\columnwidth}{!}{%
412	\begin{tabular}{llcccc}
413	\toprule
414	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
415	\midrule
416	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
417	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
418	\midrule
419	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
420	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
421	\bottomrule
422	\end{tabular}}
423	\end{table}
424	
425	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
426	
427	\section{BCS-Controlled Detailed Results}
428	\label{app:bcs-controlled-table}
429	
430	\begin{table}[h]
431	\centering
432	\small
433	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
434	\label{tab:bcs_controlled}
435	\resizebox{\columnwidth}{!}{%
436	\begin{tabular}{lcrrrr}
437	\toprule
438	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
439	\midrule
440	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
441	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
442	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
443	\bottomrule
444	\end{tabular}}
445	\end{table}
446	
447	\paragraph{Adjusted $R^2$ and confidence intervals.}
448	DocRED regressions (\S\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\% CI [0.47, 0.75]). The small shrinkage ($\Delta R^2 \leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.
449	
450	\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
451	\label{app:format-independence}
452	
453	To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\ref{tab:format_independence}).
454	
455	\begin{table}[h]
456	\centering
457	\small
458	\caption{Paired comparison of constrained vs.\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\Delta = -0.08$\,pp), ruling out a format-driven accuracy shift.}
459	\label{tab:format_independence}
460	\begin{tabular}{lrr}
461	\toprule
462	\textbf{Metric} & \textbf{Constrained} & \textbf{Unconstrained} \\
463	\midrule
464	Mean accuracy & 79.5\% & 79.6\% \\
465	Pearson $r$ (BCS vs.\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\
466	Spearman $\rho$ (BCS vs.\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\
467	\midrule
468	\multicolumn{3}{l}{\textit{Paired Fisher $z$-test for correlation equality}} \\
469	\quad Pearson $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
470	\quad Spearman $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
471	\bottomrule
472	\end{tabular}
473	\end{table}
474	
475	The near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\sim}2$\,pp; \S\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.
476	
477	\paragraph{Per-batch paired results.}
478	Table~\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \emph{identical} accuracy; the two exceptions (high\_5, high\_11) differ by a single sample (1/96 $\approx$ 1.04\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\%), confirming that the model generates valid type labels even without format constraints.
479	
480	\begin{table}[h]
481	\centering
482	\small
483	\caption{Per-batch accuracy (\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\Delta = -1.04$\,pp). L = low-BCS, H = high-BCS.}
484	\label{tab:format_perbatch}
485	\resizebox{\columnwidth}{!}{%
486	\begin{tabular}{lcrrrr}
487	\toprule
488	\textbf{Batch} & \textbf{Group} & \textbf{BCS} & \textbf{Constr.} & \textbf{Unconstr.} & \textbf{$\Delta$} \\
489	\midrule
490	low\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\
491	low\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\
492	low\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\
493	low\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\
494	low\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\
495	low\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\
496	low\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\
497	low\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\
498	low\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "fa3b7020-e54d-4d5b-abb4-d0db2c50bd24",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\",
      "numLines": 100,
      "startLine": 399,
      "totalLines": 905
    }
  }
}
```

</details>

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_01RAjRyzBdcircRSK97AZmMt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "5caaf1de-efc2-4caa-9e4b-df1bfd12eeed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkMDqRiUugYEN5xioTSJk5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3375,
      "cache_read_input_tokens": 33331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3375
      },
      "output_tokens": 61,
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

_source line 104 · 2026-05-22T05:24:11.284Z_

<details><summary>↩ Tool result · `toolu_01RAjRyzBdcircRSK97AZmMt`</summary>

```text
1	% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)
2	
3	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms
4	the negative direction of the BCS--accuracy relationship even after
5	regularizing for the severe BCS--centrality multicollinearity
6	(VIF\,$\approx$\,50.9).
7	The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$
8	($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$).
9	An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for
10	\emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge
11	solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at
12	$\lambda{=}0$ and monotonically decreasing thereafter.
13	Given the shrinkage bias inherent to ridge estimation, we interpret only
14	the sign---not the magnitude---of the BCS coefficient as directional
15	evidence that higher schema confusability degrades extraction accuracy,
16	independent of degree centrality.
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "87d1bd10-c32e-49ba-91f4-95e3f5e45dd2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_appendix.tex",
      "content": "% Appendix E.1: DocRED Ridge Regression (BCS directionality under multicollinearity)\n\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms\nthe negative direction of the BCS--accuracy relationship even after\nregularizing for the severe BCS--centrality multicollinearity\n(VIF\\,$\\approx$\\,50.9).\nThe standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$\n($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$).\nAn analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for\n\\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge\nsolution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at\n$\\lambda{=}0$ and monotonically decreasing thereafter.\nGiven the shrinkage bias inherent to ridge estimation, we interpret only\nthe sign---not the magnitude---of the BCS coefficient as directional\nevidence that higher schema confusability degrades extraction accuracy,\nindependent of degree centrality.\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_01XcgUDKdQ78Xf2KgbV7yfMi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "10efb289-76d3-4551-b472-553d2bb14e4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUy7rPbAoanxBp1RG9e1jF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 36706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 445
      },
      "output_tokens": 66,
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

_source line 106 · 2026-05-22T05:24:14.066Z_

<details><summary>↩ Tool result · `toolu_01XcgUDKdQ78Xf2KgbV7yfMi`</summary>

```text
1	{
2	  "method": "Ridge regression (analytic from correlation matrix, GCV λ selection)",
3	  "data_source": "exp_docred_bcs_expanded: 110 DocRED batches (96-type pool, count_16+32)",
4	  "n_batches": 110,
5	  "correlation_matrix": {
6	    "r_BCS_accuracy": -0.7602,
7	    "r_centrality_accuracy": -0.7344,
8	    "r_BCS_centrality": 0.9901,
9	    "VIF": 50.8
10	  },
11	  "gcv_selected_alpha": 0.001231,
12	  "r2_ridge": 0.5944,
13	  "standardized_coefficients": {
14	    "bcs_coefficient": -1.5342,
15	    "centrality_coefficient": 0.7837
16	  },
17	  "ols_standardized_coefficients": {
18	    "bcs_coefficient": -1.6785,
19	    "centrality_coefficient": 0.9275,
20	    "r2": 0.5949
21	  },
22	  "ridge_path_at_selected_lambdas": {
23	    "0.01": {
24	      "bcs_coefficient": -1.0219,
25	      "centrality_coefficient": 0.2746
26	    },
27	    "0.1": {
28	      "bcs_coefficient": -0.4749,
29	      "centrality_coefficient": -0.2402
30	    },
31	    "1.0": {
32	      "bcs_coefficient": -0.2627,
33	      "centrality_coefficient": -0.2372
34	    },
35	    "10.0": {
36	      "bcs_coefficient": -0.0636,
37	      "centrality_coefficient": -0.061
38	    },
39	    "100.0": {
40	      "bcs_coefficient": -0.0075,
41	      "centrality_coefficient": -0.0072
42	    }
43	  },
44	  "sign_robustness": {
45	    "bcs_negative_for_all_lambda": true,
46	    "bcs_coef_range": [
47	      -1.6655,
48	      -0.0001
49	    ],
50	    "analytic_proof": "β_BCS = [(1+λ)·r_{BCS,y} − r_{BCS,cent}·r_{cent,y}] / [(1+λ)² − r²_{BCS,cent}]. Numerator = −(1+λ)·0.7602 + 0.7271 = −0.0331 − λ·0.7602, monotonically decreasing in λ and negative at λ=0. Denominator > 0. Hence β_BCS < 0 for all λ ≥ 0."
51	  },
52	  "note": "Analytic ridge from the 3-variable correlation matrix is equivalent to RidgeCV on standardized data for any given λ. GCV replaces k-fold CV. The extreme VIF (50.9) confirms high multicollinearity; ridge stabilizes the coefficients. The BCS coefficient is provably negative for all λ ≥ 0."
53	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "1f590d54-017b-4900-af8a-c38ae1d42d6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/docred_ridge_regression.json",
      "content": "{\n  \"method\": \"Ridge regression (analytic from correlation matrix, GCV λ selection)\",\n  \"data_source\": \"exp_docred_bcs_expanded: 110 DocRED batches (96-type pool, count_16+32)\",\n  \"n_batches\": 110,\n  \"correlation_matrix\": {\n    \"r_BCS_accuracy\": -0.7602,\n    \"r_centrality_accuracy\": -0.7344,\n    \"r_BCS_centrality\": 0.9901,\n    \"VIF\": 50.8\n  },\n  \"gcv_selected_alpha\": 0.001231,\n  \"r2_ridge\": 0.5944,\n  \"standardized_coefficients\": {\n    \"bcs_coefficient\": -1.5342,\n    \"centrality_coefficient\": 0.7837\n  },\n  \"ols_standardized_coefficients\": {\n    \"bcs_coefficient\": -1.6785,\n    \"centrality_coefficient\": 0.9275,\n    \"r2\": 0.5949\n  },\n  \"ridge_path_at_selected_lambdas\": {\n    \"0.01\": {\n      \"bcs_coefficient\": -1.0219,\n      \"centrality_coefficient\": 0.2746\n    },\n    \"0.1\": {\n      \"bcs_coefficient\": -0.4749,\n      \"centrality_coefficient\": -0.2402\n    },\n    \"1.0\": {\n      \"bcs_coefficient\": -0.2627,\n      \"centrality_coefficient\": -0.2372\n    },\n    \"10.0\": {\n      \"bcs_coefficient\": -0.0636,\n      \"centrality_coefficient\": -0.061\n    },\n    \"100.0\": {\n      \"bcs_coefficient\": -0.0075,\n      \"centrality_coefficient\": -0.0072\n    }\n  },\n  \"sign_robustness\": {\n    \"bcs_negative_for_all_lambda\": true,\n    \"bcs_coef_range\": [\n      -1.6655,\n      -0.0001\n    ],\n    \"analytic_proof\": \"β_BCS = [(1+λ)·r_{BCS,y} − r_{BCS,cent}·r_{cent,y}] / [(1+λ)² − r²_{BCS,cent}]. Numerator = −(1+λ)·0.7602 + 0.7271 = −0.0331 − λ·0.7602, monotonically decreasing in λ and negative at λ=0. Denominator > 0. Hence β_BCS < 0 for all λ ≥ 0.\"\n  },\n  \"note\": \"Analytic ridge from the 3-variable correlation matrix is equivalent to RidgeCV on standardized data for any given λ. GCV replaces k-fold CV. The extreme VIF (50.9) confirms high multicollinearity; ridge stabilizes the coefficients. The BCS coefficient is provably negative for all λ ≥ 0.\"\n}",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Read · `toolu_01LaAEaQwUmWzH8ewrbWiezj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "24515552-5d30-44a0-88cc-e42c965833a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WDrEGv1jS3fbabAo7hqNe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 973,
      "cache_read_input_tokens": 37151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 973
      },
      "output_tokens": 63,
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

_source line 108 · 2026-05-22T05:24:16.837Z_

<details><summary>↩ Tool result · `toolu_01LaAEaQwUmWzH8ewrbWiezj`</summary>

```text
1	{
2	  "dataset": {
3	    "name": "FewRel combined (exp1=110 + exp2=54 batches, 80-type pool)",
4	    "n_batches": 164,
5	    "n_unique_types": 80,
6	    "original_r": -0.5178,
7	    "original_R2": 0.2681,
8	    "original_p": 1.2502070529685776e-12
9	  },
10	  "instance_sharing": {
11	    "mean_pairwise_overlap": 0.218,
12	    "fraction_pairs_with_overlap": 0.345,
13	    "icc_shared_type_pairs": 0.2119,
14	    "icc_independent_pairs": -0.0137
15	  },
16	  "design_effect": {
17	    "avg_batches_per_type": 21.9,
18	    "DEFF": 5.42,
19	    "effective_n": 30.3,
20	    "nominal_n": 164
21	  },
22	  "slope_standard_errors": {
23	    "slope": -0.1923,
24	    "ols_se": 0.025,
25	    "ols_95ci": [
26	      -0.2412,
27	      -0.1434
28	    ],
29	    "hc1_se": 0.0255,
30	    "hc1_95ci": [
31	      -0.2423,
32	      -0.1423
33	    ],
34	    "hc1_inflation": 1.02,
35	    "cluster_robust_se": 0.0239,
36	    "cluster_robust_95ci": [
37	      -0.2392,
38	      -0.1454
39	    ],
40	    "cluster_robust_inflation": 0.96,
41	    "n_clusters": 81
42	  },
43	  "bootstrap_R2": {
44	    "n_iterations": 10000,
45	    "standard": {
46	      "mean": 0.2731,
47	      "ci_95": [
48	        0.1451,
49	        0.417
50	      ],
51	      "ci_width": 0.2719
52	    },
53	    "cluster": {
54	      "mean": 0.2729,
55	      "ci_95": [
56	        0.1434,
57	        0.4111
58	      ],
59	      "ci_width": 0.2678,
60	      "width_change_pct": -1.5
61	    }
62	  },
63	  "bootstrap_slope": {
64	    "standard": {
65	      "mean": -0.192,
66	      "ci_95": [
67	        -0.2407,
68	        -0.1416
69	      ],
70	      "ci_width": 0.099
71	    },
72	    "cluster": {
73	      "mean": -0.1915,
74	      "ci_95": [
75	        -0.236,
76	        -0.1429
77	      ],
78	      "ci_width": 0.0931,
79	      "width_change_pct": -6.0
80	    }
81	  },
82	  "significance": {
83	    "ols_t": -7.7,
84	    "ols_p": 1.2501111257279263e-12,
85	    "cluster_robust_t": -8.04,
86	    "cluster_robust_p": 7.192690887336539e-12,
87	    "significant_under_cluster_robust": true
88	  },
89	  "robustness_verdict": "ROBUST: BCS-accuracy slope remains significant (p<0.05) under all cluster-robust specifications tested (SE inflation range: 0.96x\u20130.97x). Bootstrap R\u00b2 CI width changes range from -6% to 6%. Despite high design effect (DEFF=5.4) from extensive type sharing, the BCS predictor contains sufficient independent signal across clusters to maintain robust inference.",
90	  "sensitivity_analysis": {
91	    "standard_bootstrap_R2_ci": [
92	      0.142,
93	      0.4193
94	    ],
95	    "standard_bootstrap_R2_width": 0.2774,
96	    "by_threshold": {
97	      "0.1": {
98	        "n_clusters": 83,
99	        "cluster_robust_se": 0.0243,
100	        "se_inflation": 0.97,
101	        "bootstrap_R2_ci": [
102	          0.148,
103	          0.4145
104	        ],
105	        "bootstrap_R2_width": 0.2665,
106	        "p_cluster_robust": 1.1507683694844673e-11,
107	        "width_change_pct": -3.9
108	      },
109	      "0.2": {
110	        "n_clusters": 83,
111	        "cluster_robust_se": 0.0243,
112	        "se_inflation": 0.97,
113	        "bootstrap_R2_ci": [
114	          0.147,
115	          0.4123
116	        ],
117	        "bootstrap_R2_width": 0.2653,
118	        "p_cluster_robust": 1.1507683694844673e-11,
119	        "width_change_pct": -4.3
120	      },
121	      "0.3": {
122	        "n_clusters": 81,
123	        "cluster_robust_se": 0.0239,
124	        "se_inflation": 0.96,
125	        "bootstrap_R2_ci": [
126	          0.1479,
127	          0.411
128	        ],
129	        "bootstrap_R2_width": 0.2631,
130	        "p_cluster_robust": 7.192690887336539e-12,
131	        "width_change_pct": -5.1
132	      },
133	      "0.5": {
134	        "n_clusters": 80,
135	        "cluster_robust_se": 0.0239,
136	        "se_inflation": 0.96,
137	        "bootstrap_R2_ci": [
138	          0.1507,
139	          0.4121
140	        ],
141	        "bootstrap_R2_width": 0.2614,
142	        "p_cluster_robust": 7.636336007976752e-12,
143	        "width_change_pct": -5.8
144	      },
145	      "0.7": {
146	        "n_clusters": 80,
147	        "cluster_robust_se": 0.0239,
148	        "se_inflation": 0.96,
149	        "bootstrap_R2_ci": [
150	          0.1455,
151	          0.4088
152	        ],
153	        "bootstrap_R2_width": 0.2633,
154	        "p_cluster_robust": 7.636336007976752e-12,
155	        "width_change_pct": -5.1
156	      },
157	      "0.9": {
158	        "n_clusters": 80,
159	        "cluster_robust_se": 0.0239,
160	        "se_inflation": 0.96,
161	        "bootstrap_R2_ci": [
162	          0.1454,
163	          0.4134
164	        ],
165	        "bootstrap_R2_width": 0.268,
166	        "p_cluster_robust": 7.636336007976752e-12,
167	        "width_change_pct": -3.4
168	      }
169	    }
170	  }
171	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ba834bbb-ee6f-4d82-bd9d-efc83157caef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/split_sample_bootstrap.json",
      "content": "{\n  \"dataset\": {\n    \"name\": \"FewRel combined (exp1=110 + exp2=54 batches, 80-type pool)\",\n    \"n_batches\": 164,\n    \"n_unique_types\": 80,\n    \"original_r\": -0.5178,\n    \"original_R2\": 0.2681,\n    \"original_p\": 1.2502070529685776e-12\n  },\n  \"instance_sharing\": {\n    \"mean_pairwise_overlap\": 0.218,\n    \"fraction_pairs_with_overlap\": 0.345,\n    \"icc_shared_type_pairs\": 0.2119,\n    \"icc_independent_pairs\": -0.0137\n  },\n  \"design_effect\": {\n    \"avg_batches_per_type\": 21.9,\n    \"DEFF\": 5.42,\n    \"effective_n\": 30.3,\n    \"nominal_n\": 164\n  },\n  \"slope_standard_errors\": {\n    \"slope\": -0.1923,\n    \"ols_se\": 0.025,\n    \"ols_95ci\": [\n      -0.2412,\n      -0.1434\n    ],\n    \"hc1_se\": 0.0255,\n    \"hc1_95ci\": [\n      -0.2423,\n      -0.1423\n    ],\n    \"hc1_inflation\": 1.02,\n    \"cluster_robust_se\": 0.0239,\n    \"cluster_robust_95ci\": [\n      -0.2392,\n      -0.1454\n    ],\n    \"cluster_robust_inflation\": 0.96,\n    \"n_clusters\": 81\n  },\n  \"bootstrap_R2\": {\n    \"n_iterations\": 10000,\n    \"standard\": {\n      \"mean\": 0.2731,\n      \"ci_95\": [\n        0.1451,\n        0.417\n      ],\n      \"ci_width\": 0.2719\n    },\n    \"cluster\": {\n      \"mean\": 0.2729,\n      \"ci_95\": [\n        0.1434,\n        0.4111\n      ],\n      \"ci_width\": 0.2678,\n      \"width_change_pct\": -1.5\n    }\n  },\n  \"bootstrap_slope\": {\n    \"standard\": {\n      \"mean\": -0.192,\n      \"ci_95\": [\n        -0.2407,\n        -0.1416\n      ],\n      \"ci_width\": 0.099\n    },\n    \"cluster\": {\n      \"mean\": -0.1915,\n      \"ci_95\": [\n        -0.236,\n        -0.1429\n      ],\n      \"ci_width\": 0.0931,\n      \"width_change_pct\": -6.0\n    }\n  },\n  \"significance\": {\n    \"ols_t\": -7.7,\n    \"ols_p\": 1.2501111257279263e-12,\n    \"cluster_robust_t\": -8.04,\n    \"cluster_robust_p\": 7.192690887336539e-12,\n    \"significant_under_cluster_robust\": true\n  },\n  \"robustness_verdict\": \"ROBUST: BCS-accuracy slope remains significant (p<0.05) under all cluster-robust specifications tested (SE inflation range: 0.96x\\u20130.97x). Bootstrap R\\u00b2 CI width changes range from -6% to 6%. Despite high design effect (DEFF=5.4) from extensive type sharing, the BCS predictor contains sufficient independent signal across clusters to maintain robust inference.\",\n  \"sensitivity_analysis\": {\n    \"standard_bootstrap_R2_ci\": [\n      0.142,\n      0.4193\n    ],\n    \"standard_bootstrap_R2_width\": 0.2774,\n    \"by_threshold\": {\n      \"0.1\": {\n        \"n_clusters\": 83,\n        \"cluster_robust_se\": 0.0243,\n        \"se_inflation\": 0.97,\n        \"bootstrap_R2_ci\": [\n          0.148,\n          0.4145\n        ],\n        \"bootstrap_R2_width\": 0.2665,\n        \"p_cluster_robust\": 1.1507683694844673e-11,\n        \"width_change_pct\": -3.9\n      },\n      \"0.2\": {\n        \"n_clusters\": 83,\n        \"cluster_robust_se\": 0.0243,\n        \"se_inflation\": 0.97,\n        \"bootstrap_R2_ci\": [\n          0.147,\n          0.4123\n        ],\n        \"bootstrap_R2_width\": 0.2653,\n        \"p_cluster_robust\": 1.1507683694844673e-11,\n        \"width_change_pct\": -4.3\n      },\n      \"0.3\": {\n        \"n_clusters\": 81,\n        \"cluster_robust_se\": 0.0239,\n        \"se_inflation\": 0.96,\n        \"bootstrap_R2_ci\": [\n          0.1479,\n          0.411\n        ],\n        \"bootstrap_R2_width\": 0.2631,\n        \"p_cluster_robust\": 7.192690887336539e-12,\n        \"width_change_pct\": -5.1\n      },\n      \"0.5\": {\n        \"n_clusters\": 80,\n        \"cluster_robust_se\": 0.0239,\n        \"se_inflation\": 0.96,\n        \"bootstrap_R2_ci\": [\n          0.1507,\n          0.4121\n        ],\n        \"bootstrap_R2_width\": 0.2614,\n        \"p_cluster_robust\": 7.636336007976752e-12,\n        \"width_change_pct\": -5.8\n      },\n      \"0.7\": {\n        \"n_clusters\": 80,\n        \"cluster_robust_se\": 0.0239,\n        \"se_inflation\": 0.96,\n        \"bootstrap_R2_ci\": [\n          0.1455,\n          0.4088\n        ],\n        \"bootstrap_R2_width\": 0.2633,\n        \"p_cluster_robust\": 7.636336007976752e-12,\n        \"width_change_pct\": -5.1\n      },\n      \"0.9\": {\n        \"n_clusters\": 80,\n        \"cluster_robust_se\": 0.0239,\n        \"se_inflation\": 0.96,\n        \"bootstrap_R2_ci\": [\n          0.1454,\n          0.4134\n        ],\n        \"bootstrap_R2_width\": 0.268,\n        \"p_cluster_robust\": 7.636336007976752e-12,\n        \"width_change_pct\": -3.4\n      }\n    }\n  }\n}",
      "numLines": 171,
      "startLine": 1,
      "totalLines": 171
    }
  }
}
```

</details>

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Read · `toolu_01ByoavM3qfjdjFxDaEs2aac`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "6f81030e-22e8-4179-896f-79339e248a44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W72VJEa3cSYJErGhxrcRSk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2188,
      "cache_read_input_tokens": 38124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2188
      },
      "output_tokens": 65,
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

_source line 110 · 2026-05-22T05:24:19.582Z_

<details><summary>↩ Tool result · `toolu_01ByoavM3qfjdjFxDaEs2aac`</summary>

```text
1	{
2	  "domain_classification": {
3	    "country": "geography",
4	    "country of citizenship": "geography",
5	    "country of origin": "geography",
6	    "location": "geography",
7	    "located in the administrative territorial entity": "geography",
8	    "contains administrative territorial entity": "geography",
9	    "headquarters location": "geography",
10	    "location of formation": "geography",
11	    "work location": "geography",
12	    "residence": "geography",
13	    "located in or next to body of water": "geography",
14	    "located on terrain feature": "geography",
15	    "mountain range": "geography",
16	    "mouth of the watercourse": "geography",
17	    "tributary": "geography",
18	    "place served by transport hub": "geography",
19	    "crosses": "geography",
20	    "constellation": "geography",
21	    "applies to jurisdiction": "geography",
22	    "licensed to broadcast to": "geography",
23	    "father": "person",
24	    "mother": "person",
25	    "child": "person",
26	    "sibling": "person",
27	    "spouse": "person",
28	    "occupation": "person",
29	    "religion": "person",
30	    "position held": "person",
31	    "member of political party": "person",
32	    "military rank": "person",
33	    "military branch": "person",
34	    "field of work": "person",
35	    "voice type": "person",
36	    "owned by": "organization",
37	    "subsidiary": "organization",
38	    "operator": "organization",
39	    "manufacturer": "organization",
40	    "developer": "organization",
41	    "publisher": "organization",
42	    "distributor": "organization",
43	    "member of": "organization",
44	    "participating team": "organization",
45	    "participant": "organization",
46	    "league": "organization",
47	    "performer": "creative_work",
48	    "composer": "creative_work",
49	    "director": "creative_work",
50	    "screenwriter": "creative_work",
51	    "after a work by": "creative_work",
52	    "characters": "creative_work",
53	    "genre": "creative_work",
54	    "original language of film or TV show": "creative_work",
55	    "language of work or name": "creative_work",
56	    "original network": "creative_work",
57	    "record label": "creative_work",
58	    "platform": "creative_work",
59	    "notable work": "creative_work",
60	    "instrument": "creative_work",
61	    "movement": "creative_work",
62	    "participant of": "event_temporal",
63	    "follows": "event_temporal",
64	    "followed by": "event_temporal",
65	    "sports season of league or competition": "event_temporal",
66	    "competition class": "event_temporal",
67	    "winner": "event_temporal",
68	    "successful candidate": "event_temporal",
69	    "nominated for": "event_temporal",
70	    "head of government": "event_temporal",
71	    "taxon rank": "science_taxonomy",
72	    "instance of": "science_taxonomy",
73	    "has part": "science_taxonomy",
74	    "part of": "science_taxonomy",
75	    "said to be the same as": "science_taxonomy",
76	    "heritage designation": "science_taxonomy",
77	    "main subject": "science_taxonomy",
78	    "sport": "science_taxonomy",
79	    "operating system": "science_taxonomy",
80	    "occupant": "science_taxonomy",
81	    "architect": "science_taxonomy",
82	    "position played on team": "science_taxonomy"
83	  },
84	  "n_domains": 6,
85	  "n_total_relations": 80,
86	  "high_bcs_batches": {
87	    "n": 25,
88	    "bcs_range": [
89	      0.7907828837633133,
90	      0.8109273569924491
91	    ],
92	    "types_per_batch": 8
93	  },
94	  "low_bcs_batches": {
95	    "n": 25,
96	    "bcs_range": [
97	      0.3562733248940536,
98	      0.366775135908808
99	    ],
100	    "types_per_batch": 8
101	  },
102	  "domain_distribution": {
103	    "high_bcs": {
104	      "creative_work": 0,
105	      "event_temporal": 52,
106	      "geography": 0,
107	      "organization": 32,
108	      "person": 17,
109	      "science_taxonomy": 99
110	    },
111	    "low_bcs": {
112	      "creative_work": 51,
113	      "event_temporal": 30,
114	      "geography": 91,
115	      "organization": 8,
116	      "person": 5,
117	      "science_taxonomy": 15
118	    }
119	  },
120	  "domain_proportions": {
121	    "high_bcs": {
122	      "creative_work": 0.0,
123	      "event_temporal": 0.26,
124	      "geography": 0.0,
125	      "organization": 0.16,
126	      "person": 0.085,
127	      "science_taxonomy": 0.495
128	    },
129	    "low_bcs": {
130	      "creative_work": 0.255,
131	      "event_temporal": 0.15,
132	      "geography": 0.455,
133	      "organization": 0.04,
134	      "person": 0.025,
135	      "science_taxonomy": 0.075
136	    }
137	  },
138	  "chi_squared": {
139	    "statistic": 230.7426,
140	    "p_value": 0.0,
141	    "df": 5
142	  },
143	  "entropy": {
144	    "high_bcs": 1.7328,
145	    "low_bcs": 2.0292,
146	    "max_possible": 2.585,
147	    "normalized_high_bcs": 0.6703,
148	    "normalized_low_bcs": 0.785
149	  },
150	  "interpretation": "Domain composition differs significantly between high- and low-BCS batches (chi2=230.74, p<0.001, df=5). High-BCS batches concentrate on science/taxonomy and event/temporal domains (relations like follows/followed_by, part_of/has_part, member_of, instance_of), while low-BCS batches spread across geography and creative_work domains (country_of_citizenship, composer, original_language_of_film_or_TV_show). However, this domain concentration is an expected property of embedding-based BCS: types within the same domain naturally share more semantic features, yielding higher pairwise cosine similarity. Domain composition is thus a mediator of the BCS\u2013performance relationship, not an independent confound.",
151	  "unique_types_in_low": [
152	    "composer",
153	    "country of citizenship",
154	    "headquarters location",
155	    "located in or next to body of water",
156	    "located on terrain feature",
157	    "military rank",
158	    "mountain range",
159	    "mouth of the watercourse",
160	    "operator",
161	    "original language of film or TV show",
162	    "owned by",
163	    "performer",
164	    "place served by transport hub",
165	    "publisher",
166	    "record label",
167	    "religion",
168	    "residence",
169	    "screenwriter",
170	    "sports season of league or competition",
171	    "successful candidate",
172	    "taxon rank",
173	    "voice type"
174	  ],
175	  "unique_types_in_high": [
176	    "child",
177	    "followed by",
178	    "follows",
179	    "has part",
180	    "instance of",
181	    "main subject",
182	    "member of",
183	    "nominated for",
184	    "occupant",
185	    "operator",
186	    "part of",
187	    "participant of",
188	    "said to be the same as",
189	    "sibling"
190	  ],
191	  "types_overlap": [
192	    "operator"
193	  ],
194	  "latex_appendix": "\\paragraph{Domain Distribution in Extreme-BCS Batches.}\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool.\nThe distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains.\nNormalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains.\nCrucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS.\nDomain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable.\nThe BCS metric intentionally aggregates such semantic overlap into a single predictive score."
195	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "7966ac39-0ec1-4a2b-aae6-95c3cd84f22b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/fewrel_domain_distribution.json",
      "content": "{\n  \"domain_classification\": {\n    \"country\": \"geography\",\n    \"country of citizenship\": \"geography\",\n    \"country of origin\": \"geography\",\n    \"location\": \"geography\",\n    \"located in the administrative territorial entity\": \"geography\",\n    \"contains administrative territorial entity\": \"geography\",\n    \"headquarters location\": \"geography\",\n    \"location of formation\": \"geography\",\n    \"work location\": \"geography\",\n    \"residence\": \"geography\",\n    \"located in or next to body of water\": \"geography\",\n    \"located on terrain feature\": \"geography\",\n    \"mountain range\": \"geography\",\n    \"mouth of the watercourse\": \"geography\",\n    \"tributary\": \"geography\",\n    \"place served by transport hub\": \"geography\",\n    \"crosses\": \"geography\",\n    \"constellation\": \"geography\",\n    \"applies to jurisdiction\": \"geography\",\n    \"licensed to broadcast to\": \"geography\",\n    \"father\": \"person\",\n    \"mother\": \"person\",\n    \"child\": \"person\",\n    \"sibling\": \"person\",\n    \"spouse\": \"person\",\n    \"occupation\": \"person\",\n    \"religion\": \"person\",\n    \"position held\": \"person\",\n    \"member of political party\": \"person\",\n    \"military rank\": \"person\",\n    \"military branch\": \"person\",\n    \"field of work\": \"person\",\n    \"voice type\": \"person\",\n    \"owned by\": \"organization\",\n    \"subsidiary\": \"organization\",\n    \"operator\": \"organization\",\n    \"manufacturer\": \"organization\",\n    \"developer\": \"organization\",\n    \"publisher\": \"organization\",\n    \"distributor\": \"organization\",\n    \"member of\": \"organization\",\n    \"participating team\": \"organization\",\n    \"participant\": \"organization\",\n    \"league\": \"organization\",\n    \"performer\": \"creative_work\",\n    \"composer\": \"creative_work\",\n    \"director\": \"creative_work\",\n    \"screenwriter\": \"creative_work\",\n    \"after a work by\": \"creative_work\",\n    \"characters\": \"creative_work\",\n    \"genre\": \"creative_work\",\n    \"original language of film or TV show\": \"creative_work\",\n    \"language of work or name\": \"creative_work\",\n    \"original network\": \"creative_work\",\n    \"record label\": \"creative_work\",\n    \"platform\": \"creative_work\",\n    \"notable work\": \"creative_work\",\n    \"instrument\": \"creative_work\",\n    \"movement\": \"creative_work\",\n    \"participant of\": \"event_temporal\",\n    \"follows\": \"event_temporal\",\n    \"followed by\": \"event_temporal\",\n    \"sports season of league or competition\": \"event_temporal\",\n    \"competition class\": \"event_temporal\",\n    \"winner\": \"event_temporal\",\n    \"successful candidate\": \"event_temporal\",\n    \"nominated for\": \"event_temporal\",\n    \"head of government\": \"event_temporal\",\n    \"taxon rank\": \"science_taxonomy\",\n    \"instance of\": \"science_taxonomy\",\n    \"has part\": \"science_taxonomy\",\n    \"part of\": \"science_taxonomy\",\n    \"said to be the same as\": \"science_taxonomy\",\n    \"heritage designation\": \"science_taxonomy\",\n    \"main subject\": \"science_taxonomy\",\n    \"sport\": \"science_taxonomy\",\n    \"operating system\": \"science_taxonomy\",\n    \"occupant\": \"science_taxonomy\",\n    \"architect\": \"science_taxonomy\",\n    \"position played on team\": \"science_taxonomy\"\n  },\n  \"n_domains\": 6,\n  \"n_total_relations\": 80,\n  \"high_bcs_batches\": {\n    \"n\": 25,\n    \"bcs_range\": [\n      0.7907828837633133,\n      0.8109273569924491\n    ],\n    \"types_per_batch\": 8\n  },\n  \"low_bcs_batches\": {\n    \"n\": 25,\n    \"bcs_range\": [\n      0.3562733248940536,\n      0.366775135908808\n    ],\n    \"types_per_batch\": 8\n  },\n  \"domain_distribution\": {\n    \"high_bcs\": {\n      \"creative_work\": 0,\n      \"event_temporal\": 52,\n      \"geography\": 0,\n      \"organization\": 32,\n      \"person\": 17,\n      \"science_taxonomy\": 99\n    },\n    \"low_bcs\": {\n      \"creative_work\": 51,\n      \"event_temporal\": 30,\n      \"geography\": 91,\n      \"organization\": 8,\n      \"person\": 5,\n      \"science_taxonomy\": 15\n    }\n  },\n  \"domain_proportions\": {\n    \"high_bcs\": {\n      \"creative_work\": 0.0,\n      \"event_temporal\": 0.26,\n      \"geography\": 0.0,\n      \"organization\": 0.16,\n      \"person\": 0.085,\n      \"science_taxonomy\": 0.495\n    },\n    \"low_bcs\": {\n      \"creative_work\": 0.255,\n      \"event_temporal\": 0.15,\n      \"geography\": 0.455,\n      \"organization\": 0.04,\n      \"person\": 0.025,\n      \"science_taxonomy\": 0.075\n    }\n  },\n  \"chi_squared\": {\n    \"statistic\": 230.7426,\n    \"p_value\": 0.0,\n    \"df\": 5\n  },\n  \"entropy\": {\n    \"high_bcs\": 1.7328,\n    \"low_bcs\": 2.0292,\n    \"max_possible\": 2.585,\n    \"normalized_high_bcs\": 0.6703,\n    \"normalized_low_bcs\": 0.785\n  },\n  \"interpretation\": \"Domain composition differs significantly between high- and low-BCS batches (chi2=230.74, p<0.001, df=5). High-BCS batches concentrate on science/taxonomy and event/temporal domains (relations like follows/followed_by, part_of/has_part, member_of, instance_of), while low-BCS batches spread across geography and creative_work domains (country_of_citizenship, composer, original_language_of_film_or_TV_show). However, this domain concentration is an expected property of embedding-based BCS: types within the same domain naturally share more semantic features, yielding higher pairwise cosine similarity. Domain composition is thus a mediator of the BCS\\u2013performance relationship, not an independent confound.\",\n  \"unique_types_in_low\": [\n    \"composer\",\n    \"country of citizenship\",\n    \"headquarters location\",\n    \"located in or next to body of water\",\n    \"located on terrain feature\",\n    \"military rank\",\n    \"mountain range\",\n    \"mouth of the watercourse\",\n    \"operator\",\n    \"original language of film or TV show\",\n    \"owned by\",\n    \"performer\",\n    \"place served by transport hub\",\n    \"publisher\",\n    \"record label\",\n    \"religion\",\n    \"residence\",\n    \"screenwriter\",\n    \"sports season of league or competition\",\n    \"successful candidate\",\n    \"taxon rank\",\n    \"voice type\"\n  ],\n  \"unique_types_in_high\": [\n    \"child\",\n    \"followed by\",\n    \"follows\",\n    \"has part\",\n    \"instance of\",\n    \"main subject\",\n    \"member of\",\n    \"nominated for\",\n    \"occupant\",\n    \"operator\",\n    \"part of\",\n    \"participant of\",\n    \"said to be the same as\",\n    \"sibling\"\n  ],\n  \"types_overlap\": [\n    \"operator\"\n  ],\n  \"latex_appendix\": \"\\\\paragraph{Domain Distribution in Extreme-BCS Batches.}\\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool.\\nThe distributions differ significantly ($\\\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\\\%) and creative work (25.5\\\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\\\%) and event/temporal (26.0\\\\%) domains.\\nNormalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains.\\nCrucially, this domain concentration is an \\\\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS.\\nDomain composition therefore acts as a mediator---it is \\\\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable.\\nThe BCS metric intentionally aggregates such semantic overlap into a single predictive score.\"\n}",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Assistant

_source line 111_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the necessary information. Let me understand the structure:

1. The appendix is in `main.tex` starting at line 57 (`\appendix`)
2. `sec:appendix_partial_corr` is at line 309 (subsection E.1 - "Partial Correlation: Controlling for Degree Centrality")
3. The current content at that section ends at line 328, followed by subsection for NER BCS-Null Power Analysis at line 330

I need to:
- **Task A**: Add ridge regression paragraph after line 328 (end of partial correlation section, before NER power analysis)


- **Task B**: Add bootstrap CI robustness paragraph somewhere appropriate
- **Task C**: Add FewRel domain distribution paragraph somewhere appropriate

Let me also check results.tex line 52 to understand the reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "a6dc3ef6-3d9c-4b6a-9b36-563859adea3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLsVVY9DqYgKpr1cmNKHNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 40312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2708
      },
      "output_tokens": 13,
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

_source line 112_

Now let me read results.tex around the ridge regression reference, and check where the appendix sections are organized.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "36da9c9a-9d5b-45df-bce9-2c73ac4ff32c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLsVVY9DqYgKpr1cmNKHNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 40312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2708
      },
      "output_tokens": 13,
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

_source line 113_

<details open><summary>🔧 Tool call — Read · `toolu_01FxX456V6HvjfzR1oA3KsZG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": 40,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "7ff00f8e-4a63-446a-9bab-0e585d5fc8af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLsVVY9DqYgKpr1cmNKHNG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2708,
      "cache_read_input_tokens": 40312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2708
      },
      "output_tokens": 13,
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

_source line 114 · 2026-05-22T05:24:29.664Z_

<details><summary>↩ Tool result · `toolu_01FxX456V6HvjfzR1oA3KsZG`</summary>

```text
40	\label{fig:error_taxonomy}
41	\end{figure*}
42	
43	\subsection{BCS-Controlled Experiments}
44	\label{sec:bcs_controlled}
45	
46	\looseness=-1
47	On FewRel, BCS explains ${\sim}$22\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\,=\,1.18$). DocRED partial correlation ($r_{\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\,=\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\ref{sec:appendix_partial_corr}, Table~\ref{tab:partial_corr}).} the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
48	
49	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (95\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
50	
51	\paragraph{Document-level RE (DocRED).}
52	The effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\footnote{DocRED uses 5 batches per count level (vs.\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\,pp at count 16 ($\rho = -0.762$, 95\% CI [$-$0.88, $-$0.58]) and $-$15.7\,pp at count 32 ($\rho = -0.693$, 95\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\,=\,50.9$): semipartial $R^2_{\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\% of the explained variance is shared with centrality. Given VIF${}\,=\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\,=\,1.18$).
53	
54	\paragraph{Within-pool controlled comparison.}
55	\label{sec:within_pool}
56	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
57	
58	\paragraph{Practical magnitude.}
59	\label{sec:practical_magnitude}
60	\looseness=-1
61	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\text{BCS}} = 0.056$ after centrality; Appendix~\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The amplification from pairwise $r^2 \approx 1.5\%$ to batch-level $R^2 \approx 22\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\sim}3\times$ amplification illustrated by Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}).
62	
63	\paragraph{Cross-model validation.}
64	\looseness=-1
65	The effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap (Table~\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\Delta = -17.6$\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \to -0.42$, $p = 0.22$; Spearman: $\rho = -0.40 \to -0.18$, $p = 0.64$; Appendix~\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\ref{tab:cross_model_ner_null}).
66	
67	\paragraph{Prompt sensitivity.}
68	\looseness=-1
69	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\ref{sec:appendix_fewshot_bcs}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c1caedd3-7058-45f3-9bd9-339f8f69b543",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\label{fig:error_taxonomy}\n\\end{figure*}\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\n\\looseness=-1\nOn FewRel, BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\\,=\\,1.18$). DocRED partial correlation ($r_{\\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\\,=\\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\\ref{sec:appendix_partial_corr}, Table~\\ref{tab:partial_corr}).} the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (95\\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\\footnote{DocRED uses 5 batches per count level (vs.\\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\\,pp at count 16 ($\\rho = -0.762$, 95\\% CI [$-$0.88, $-$0.58]) and $-$15.7\\,pp at count 32 ($\\rho = -0.693$, 95\\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\\,=\\,50.9$): semipartial $R^2_{\\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\\% of the explained variance is shared with centrality. Given VIF${}\\,=\\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\\,=\\,1.18$).\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\n\\looseness=-1\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\\text{BCS}} = 0.056$ after centrality; Appendix~\\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The amplification from pairwise $r^2 \\approx 1.5\\%$ to batch-level $R^2 \\approx 22\\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \\citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\\sim}3\\times$ amplification illustrated by Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\n\\looseness=-1\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap (Table~\\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\\Delta = -17.6$\\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \\to -0.42$, $p = 0.22$; Spearman: $\\rho = -0.40 \\to -0.18$, $p = 0.64$; Appendix~\\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\\ref{tab:cross_model_ner_null}).\n\n\\paragraph{Prompt sensitivity.}\n\\looseness=-1\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\\ref{sec:appendix_fewshot_bcs}).",
      "numLines": 30,
      "startLine": 40,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Assistant

_source line 115_

Now I understand the full picture. Let me check the exact end of the `sec:appendix_partial_corr` subsection and where to insert the new content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "947ac785-a298-403a-8910-813e4b4cb018",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Q2VEdc1q6rZgwbzYuHo9W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 43020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

_source line 116_

<details open><summary>🔧 Tool call — Read · `toolu_01Ewtea3UkbvSWT3CbsUTcW3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 326,
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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ca9b8d40-7289-429e-88fc-280dc3fd9126",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Q2VEdc1q6rZgwbzYuHo9W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 43020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

_source line 117 · 2026-05-22T05:24:35.582Z_

<details><summary>↩ Tool result · `toolu_01Ewtea3UkbvSWT3CbsUTcW3`</summary>

```text
326	\end{table}
327	
328	As Table~\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
329	
330	\subsection{NER BCS-Null Power Analysis}
331	\label{sec:appendix_ner_power}
332	
333	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
334	
335	\section{Batch Composition Results}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "6036431d-1122-47d2-924a-477438de302a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}",
      "numLines": 10,
      "startLine": 326,
      "totalLines": 905
    }
  }
}
```

</details>

---

### Assistant

_source line 118_

Now I have full context. Let me also check the overall appendix section structure to decide where to place the bootstrap and domain distribution paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "5a5c0dac-0fad-4c82-9dfe-c4c8f530a0ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163hnsrbSnKQ5a7ebiYhXAT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 45489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 614
      },
      "output_tokens": 4,
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

_source line 119_

<details open><summary>🔧 Tool call — Grep · `toolu_01LqL8cinz6tByQ6pgTXQE6A`</summary>

```json
{
  "pattern": "^\\\\\\\\(section|subsection)\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ee2227c2-1241-4397-8c53-20def971bb75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163hnsrbSnKQ5a7ebiYhXAT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 45489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 614
      },
      "output_tokens": 4,
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

_source line 120 · 2026-05-22T05:24:39.712Z_

<details><summary>↩ Tool result · `toolu_01LqL8cinz6tByQ6pgTXQE6A`</summary>

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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "60c4d118-4a25-4759-ba7a-20167ebbb1a1",
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

_source line 121_

<details open><summary>🔧 Tool call — Grep · `toolu_018kjpv1ryzhnggBtgSksnV9`</summary>

```json
{
  "pattern": "\\\\section\\{|\\\\subsection\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "03560156-4c23-44a8-b95d-a7b50b0438cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4V4chmYJZZCGjog6dz95o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 298,
      "cache_read_input_tokens": 46103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 298
      },
      "output_tokens": 58,
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

_source line 122 · 2026-05-22T05:24:43.224Z_

<details><summary>↩ Tool result · `toolu_018kjpv1ryzhnggBtgSksnV9`</summary>

```text
60:\section{Additional Figures}
155:\section{SDGD Full Protocol and Results}
199:\subsection{Practical Routing Strategies on RE}
226:\section{Factorial Analysis and Separability Test}
262:\section{Within-Pool CI Details}
267:\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
308:\subsection{Partial Correlation: Controlling for Degree Centrality}
330:\subsection{NER BCS-Null Power Analysis}
335:\section{Batch Composition Results}
359:\section{Prompt Version Sensitivity Analysis}
373:\subsection{Cross-Prompt-Variant BCS Correlation}
401:\section{BCS Aggregation Sensitivity}
427:\section{BCS-Controlled Detailed Results}
450:\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
520:\section{Within-Pool Analysis Methodology}
551:\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
578:\section{Pair-to-Batch Aggregation Simulation}
596:\section{BCS Independence from Type Composition}
601:\section{SCS vs.\ Simple Baselines}
629:\section{Split-Origin Covariate Analysis}
643:\section{Cross-Seed Variance Decomposition}
668:\section{Cross-Domain Connections}
673:\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
713:\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
764:\section{Few-Shot Prompting and Confusability}
789:\section{Qualitative Error Analysis}
858:\section{Schema Label Renaming Experiment}
880:\section{Relaxed Matching Evaluation (NER)}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "5b7e379e-27a0-4185-8c14-eb9755c638a5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "60:\\section{Additional Figures}\n155:\\section{SDGD Full Protocol and Results}\n199:\\subsection{Practical Routing Strategies on RE}\n226:\\section{Factorial Analysis and Separability Test}\n262:\\section{Within-Pool CI Details}\n267:\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n308:\\subsection{Partial Correlation: Controlling for Degree Centrality}\n330:\\subsection{NER BCS-Null Power Analysis}\n335:\\section{Batch Composition Results}\n359:\\section{Prompt Version Sensitivity Analysis}\n373:\\subsection{Cross-Prompt-Variant BCS Correlation}\n401:\\section{BCS Aggregation Sensitivity}\n427:\\section{BCS-Controlled Detailed Results}\n450:\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n520:\\section{Within-Pool Analysis Methodology}\n551:\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n578:\\section{Pair-to-Batch Aggregation Simulation}\n596:\\section{BCS Independence from Type Composition}\n601:\\section{SCS vs.\\ Simple Baselines}\n629:\\section{Split-Origin Covariate Analysis}\n643:\\section{Cross-Seed Variance Decomposition}\n668:\\section{Cross-Domain Connections}\n673:\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n713:\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n764:\\section{Few-Shot Prompting and Confusability}\n789:\\section{Qualitative Error Analysis}\n858:\\section{Schema Label Renaming Experiment}\n880:\\section{Relaxed Matching Evaluation (NER)}",
    "numLines": 28
  }
}
```

</details>

---

### Assistant

_source line 123_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me plan the insertions:

**Task A: Ridge Regression → After line 328 (end of partial correlation discussion, before NER BCS-Null Power Analysis)**
- Insert the ridge regression paragraph from `docred_ridge_appendix.tex` as a `\paragraph{Ridge Regression under Multicollinearity.}` within section E.1 (`sec:appendix_partial_corr`)

**Task B: Bootstrap CI → After NER BCS-Null Power Analysis (line 333), before Batch Composition Results (line 335)**
- Or it could go near the FewRel analyses. 

The bootstrap CI content about FewRel batch non-independence fits best after the partial correlation and centrality control analysis, so I'll place it as a new paragraph right after the ridge regression section in E.1. I'm mapping out the document structure—the appendices are labeled A through F, with E containing subsections on partial correlation and power analysis. I need to insert the bootstrap and domain robustness checks as new subsections E.3 and E.4 after the existing E.2, then place the batch composition results as appendix F. For the ridge regression point, I should add it as a paragraph within E.1 rather than creating a separate subsection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c952c4b2-ec21-48e7-8073-b0a2abebc0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxjMsc1Ccz7jXbU13bz846",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 46401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 622
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

_source line 124_

I have all the context. Now I'll make the three insertions into `main.tex`:

**Task A**: Ridge paragraph after line 328 in subsection E.1
**Task B**: New subsection E.3 (Bootstrap CI) after NER Power Analysis (line 333)  
**Task C**: New subsection E.4 (Domain Distribution) after Bootstrap CI

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "60275e5d-564b-4d51-bc0a-948c1e57f021",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxjMsc1Ccz7jXbU13bz846",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 46401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 622
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

_source line 125_

<details open><summary>🔧 Tool call — Edit · `toolu_013Ny1ukui7FB6VGBfaeQLZU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}",
  "new_string": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "957f0af1-cbdb-49b6-aabf-8c9255775774",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxjMsc1Ccz7jXbU13bz846",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 46401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 622
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

_source line 126 · 2026-05-22T05:25:13.595Z_

<details><summary>↩ Tool result · `toolu_013Ny1ukui7FB6VGBfaeQLZU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "a8f126be-a375-4ec9-b8be-9dd91d95658b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}",
    "newString": "As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\\ref{tab:fewshot_bcs}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & 0.92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\\ref{tab:renaming}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 327,
        "oldLines": 6,
        "newStart": 327,
        "newLines": 9,
        "lines": [
          " ",
          " As Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.",
          " ",
          "+\\paragraph{Ridge regression under multicollinearity.}",
          "+Ridge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.",
          "+",
          " \\subsection{NER BCS-Null Power Analysis}",
          " \\label{sec:appendix_ner_power}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 127_

Now add Task B (Bootstrap CI) and Task C (Domain Distribution) after NER Power Analysis, before Batch Composition Results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "d8d4bacb-28bb-4542-a8fe-31065169878b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpccvauftwKfYH2sbELPXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 47023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

_source line 128_

<details open><summary>🔧 Tool call — Read · `toolu_01Noqy8oiisPJwmJ9s1puApF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 335,
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
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "faf89513-ea7b-4dce-ad3a-698dcc3b1705",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpccvauftwKfYH2sbELPXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 47023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
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

_source line 129 · 2026-05-22T05:25:17.174Z_

<details><summary>↩ Tool result · `toolu_01Noqy8oiisPJwmJ9s1puApF`</summary>

```text
335	
336	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
337	
338	\section{Batch Composition Results}
339	\label{sec:appendix_batch_composition}
340	
341	\begin{table}[h]
342	\centering
343	\small
344	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "6a14729c-73d0-4427-993f-f7c01cdd0623",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}",
      "numLines": 10,
      "startLine": 335,
      "totalLines": 908
    }
  }
}
```

</details>

---

### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Edit · `toolu_01GzVmUYRUEFquja2YQFfazC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}",
  "new_string": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "cc13cd57-1c04-489e-8705-afc6fdd82e56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xdu22C2q7xy83neaYqNJcQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 48922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 67,
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

_source line 131 · 2026-05-22T05:25:40.801Z_

<details><summary>↩ Tool result · `toolu_01GzVmUYRUEFquja2YQFfazC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ef6dda7e-55ab-48c2-ad0c-0617f6d8c645",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}",
    "newString": "The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nV2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\\ref{tab:fewshot_bcs}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & 0.92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\\ref{tab:renaming}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 335,
        "oldLines": 6,
        "newStart": 335,
        "newLines": 16,
        "lines": [
          " ",
          " The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.",
          " ",
          "+\\subsection{Bootstrap CI Robustness}",
          "+\\label{sec:appendix_bootstrap_ci}",
          "+",
          "+Because batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.",
          "+",
          "+\\subsection{Domain Distribution in Extreme-BCS Batches}",
          "+\\label{sec:appendix_domain_distribution}",
          "+",
          "+We classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.",
          "+",
          " \\section{Batch Composition Results}",
          " \\label{sec:appendix_batch_composition}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 132_

Now compile to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c1bc2265-de86-4fda-a6f7-f704994671c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9otEi66PCouw6u9sANhV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1182,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1182
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

_source line 133_

<details open><summary>🔧 Tool call — Bash · `toolu_01VwBw3zNMziYYWyxey5Pf7v`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "8308c2eb-f5d4-4ecd-98c6-d67cd0cb21c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9otEi66PCouw6u9sANhV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1182,
      "cache_read_input_tokens": 49352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1182
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

_source line 134 · 2026-05-22T05:25:45.612Z_

<details><summary>↩ Tool result · `toolu_01VwBw3zNMziYYWyxey5Pf7v`</summary>

```text
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/he
lvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 481024 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "93c05fd4-946f-4a29-8db1-795e59629212",
  "tool_use_result": {
    "stdout": "are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/he\nlvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 481024 bytes).\nTranscript written on main.log.",
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

_source line 135_

<details open><summary>🔧 Tool call — Bash · `toolu_01VLK2Z5fuvmvbfVsaBeDRkV`</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "982292fc-3ef1-4921-94b6-bcd5aa09d939",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwFqtt6XEuAzzyWwSdbqc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 50534,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
      },
      "output_tokens": 63,
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

### System

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bp6c3usq2",
  "tool_use_id": "toolu_01VLK2Z5fuvmvbfVsaBeDRkV",
  "description": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "task_type": "local_bash",
  "uuid": "50764f4f-c312-4208-ac5e-d95b12c7124c",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### System

_source line 137_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bp6c3usq2",
  "tool_use_id": "toolu_01VLK2Z5fuvmvbfVsaBeDRkV",
  "status": "completed",
  "output_file": "",
  "summary": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "uuid": "3a195a91-93db-4fa3-b565-10e648703631",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652"
}
```

---

### Tool result

_source line 138 · 2026-05-22T05:25:52.554Z_

<details><summary>↩ Tool result · `toolu_01VLK2Z5fuvmvbfVsaBeDRkV`</summary>

```text
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--can't use both volume and number fields in guo-2021-label-confusion
(There was 1 warning)
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 480721 bytes).
Transcript written on main.log.
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 480721 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "8efc8173-f083-43c4-b207-bddf306cb9fc",
  "tool_use_result": {
    "stdout": "The top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nWarning--can't use both volume and number fields in guo-2021-label-confusion\n(There was 1 warning)\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 480721 bytes).\nTranscript written on main.log.\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 480721 bytes).\nTranscript written on main.log.",
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

_source line 139_

Now check for errors and undefined references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "2a50d179-5520-496e-938b-a8a501d755da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2U97wfVHFnbWwvUFsQeRK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 51415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 297
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

_source line 140_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ea2QMxsiU8x8fxAobo4EDJ`</summary>

```json
{
  "command": "grep -c \"^!\" main.log && grep -ci \"undefined\" main.log && grep \"undefined\" main.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "1ed3e90a-476e-42d7-ac8c-3f4954ff9409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2U97wfVHFnbWwvUFsQeRK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 51415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 297
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

_source line 141 · 2026-05-22T05:25:56.572Z_

<details><summary>↩ Tool result · reported error · `toolu_01Ea2QMxsiU8x8fxAobo4EDJ`</summary>

```text
Exit code 1
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "80dd81ff-15dc-4900-8e6d-ccaab6e0f749",
  "tool_use_result": "Error: Exit code 1\n0"
}
```

</details>

---

### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Bash · `toolu_01JrtGzbv2n89tKr7r8mKsPH`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; grep -ci \"undefined\" main.log; grep \"LaTeX Warning.*undefined\" main.log | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "427678ad-e744-469a-bb8c-57398bef24ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKgcJ82a7HUP2YcdinY277",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 220,
      "cache_read_input_tokens": 51712,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 220
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

_source line 143 · 2026-05-22T05:25:59.670Z_

<details><summary>↩ Tool result · `toolu_01JrtGzbv2n89tKr7r8mKsPH`</summary>

```text
0
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "c88aeaca-544e-4b76-b826-3b8d5125ba2e",
  "tool_use_result": {
    "stdout": "0\n0",
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

_source line 144_

0 errors, 0 undefined references. Let me verify the body page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "9d9b5334-72c2-445d-be2b-2b68723a4e73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQrEzhttzQnYmo2DFFMEq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 101,
      "cache_read_input_tokens": 51932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 101
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

_source line 145_

<details open><summary>🔧 Tool call — Bash · `toolu_015upfaxzuNoxt6qb1oK1Hn4`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\appendix\" main.log | head -3; grep \"page.*shipped out\" main.log | tail -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "99c75352-1087-4c70-aa69-fc1055312452",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQrEzhttzQnYmo2DFFMEq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 101,
      "cache_read_input_tokens": 51932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 101
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

_source line 146 · 2026-05-22T05:26:03.140Z_

<details><summary>↩ Tool result · `toolu_015upfaxzuNoxt6qb1oK1Hn4`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "6263ca5e-79a9-41b7-9e9e-ad34627f4674",
  "tool_use_result": {
    "stdout": "",
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

_source line 147_

<details open><summary>🔧 Tool call — Bash · `toolu_01AHx3hHo2ze4pQLTgtrUzP5`</summary>

```json
{
  "command": "grep \"Output written\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ed3db982-d1d5-4902-a0eb-9de25fd977bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Js3WmLcCdoyMjQjhk4dNt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 119,
      "cache_read_input_tokens": 52033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 119
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

_source line 148 · 2026-05-22T05:26:05.481Z_

<details><summary>↩ Tool result · `toolu_01AHx3hHo2ze4pQLTgtrUzP5`</summary>

```text
Output written on main.pdf (27 pages, 480721 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "88b966f8-1dee-4701-91f8-564c4ca1ed12",
  "tool_use_result": {
    "stdout": "Output written on main.pdf (27 pages, 480721 bytes).",
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

_source line 149_

<details open><summary>🔧 Tool call — Bash · `toolu_01CyX8XYrtPM9rikCAhMNFPA`</summary>

```json
{
  "command": "grep -n \"sec:appendix_partial_corr\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "7f056490-560e-4177-bee9-78c94445993a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01566NJjKCbRx5sFEVvvepgC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 88,
      "cache_read_input_tokens": 52152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 88
      },
      "output_tokens": 52,
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

_source line 150 · 2026-05-22T05:26:08.051Z_

<details><summary>↩ Tool result · `toolu_01CyX8XYrtPM9rikCAhMNFPA`</summary>

```text
1593:\newlabel{sec:appendix_partial_corr}{{E.1}{16}{Partial Correlation: Controlling for Degree Centrality}{subsection.E.1}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "172c78ea-0b0c-48c1-ae7c-7e4ebfa0c351",
  "tool_use_result": {
    "stdout": "1593:\\newlabel{sec:appendix_partial_corr}{{E.1}{16}{Partial Correlation: Controlling for Degree Centrality}{subsection.E.1}{}}",
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

_source line 151_

`sec:appendix_partial_corr` resolves to E.1 on page 16. Let me also verify the new labels exist and the appendix starts after page 8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "0d62e8c1-9c52-44c6-b6d7-8d1c539d43e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sm4yxwYzQCQiQYDZ5g7iNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 52240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 126
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

_source line 152_

<details open><summary>🔧 Tool call — Bash · `toolu_018eDTCXiuN6L7tBxW7DG6pH`</summary>

```json
{
  "command": "grep -E \"appendix_bootstrap_ci|appendix_domain_distribution\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "8b3ed3d6-c315-480b-89cc-72691a0c3f69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sm4yxwYzQCQiQYDZ5g7iNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 52240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 126
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

_source line 153 · 2026-05-22T05:26:15.115Z_

<details><summary>↩ Tool result · `toolu_018eDTCXiuN6L7tBxW7DG6pH`</summary>

```text
\newlabel{sec:appendix_bootstrap_ci}{{E.3}{17}{Bootstrap CI Robustness}{subsection.E.3}{}}
\newlabel{sec:appendix_domain_distribution}{{E.4}{17}{Domain Distribution in Extreme-BCS Batches}{subsection.E.4}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "cb7bcccb-9ecf-411b-804c-035f94d72c63",
  "tool_use_result": {
    "stdout": "\\newlabel{sec:appendix_bootstrap_ci}{{E.3}{17}{Bootstrap CI Robustness}{subsection.E.3}{}}\n\\newlabel{sec:appendix_domain_distribution}{{E.4}{17}{Domain Distribution in Extreme-BCS Batches}{subsection.E.4}{}}",
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

_source line 154_

<details open><summary>🔧 Tool call — Bash · `toolu_0144PHCKVjXcrDondAyBaKa7`</summary>

```json
{
  "command": "grep \"\\\\\\\\appendix\" main.aux | head -1; grep \"newlabel{sec:appendix_figures}\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "359f5e29-3e43-470a-8408-2efc7514024a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ocFJuhegp2KVb6UvcSN4R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 52366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
      },
      "output_tokens": 47,
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

_source line 155 · 2026-05-22T05:26:20.335Z_

<details><summary>↩ Tool result · `toolu_0144PHCKVjXcrDondAyBaKa7`</summary>

```text
\newlabel{sec:appendix_figures}{{A}{13}{Additional Figures}{appendix.A}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "ba52332b-4615-445a-8c34-2c53cb5e0b81",
  "tool_use_result": {
    "stdout": "\\newlabel{sec:appendix_figures}{{A}{13}{Additional Figures}{appendix.A}{}}",
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

_source line 156_

Appendix starts on page 13; body is within 8 pages (pages 1–8 body + references on pages 9–12).

### 修改摘要

| 任务 | 位置 | 内容 |
|------|------|------|
| **A: Ridge Regression** | `main.tex` 原 line 329, subsection E.1 内新 `\paragraph{Ridge regression under multicollinearity.}` | RidgeCV λ=0.001, β_BCS=−1.53, β_centrality=0.78, R²=0.594; 解析证明 β_BCS<0 对所有 λ≥0 成立; 仅做方向性解读 |
| **B: Bootstrap CI** | 新 subsection E.3 (`sec:appendix_bootstrap_ci`, page 17) | 164 FewRel batches, 6 个 Jaccard 阈值下 cluster-robust SE = 0.96–0.97× OLS SE, slope 显著 (p<10⁻¹¹), R² CI 宽度变化 −6%~+6%, 结论 robust |
| **C: Domain Distribution** | 新 subsection E.4 (`sec:appendix_domain_distribution`, page 17) | χ²=230.74 (p<0.001), high-BCS→science/taxonomy 49.5% + event/temporal 26.0%, low-BCS→geography 45.5% + creative_work 25.5%; 解释为 mediator 非独立 confound |

**编译结果**: 0 errors, 0 undefined references, 27 pages total (body ≤ 8 pages, appendix 从 page 13 起)。`\ref{sec:appendix_partial_corr}` 正确解析为 E.1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "uuid": "b520a334-b95f-40f6-9a8d-5b59c645c3d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1CwWTF4MFSFy31VUFKeUY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 52569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 120
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

### Task result

_source line 157_

Appendix starts on page 13; body is within 8 pages (pages 1–8 body + references on pages 9–12).

### 修改摘要

| 任务 | 位置 | 内容 |
|------|------|------|
| **A: Ridge Regression** | `main.tex` 原 line 329, subsection E.1 内新 `\paragraph{Ridge regression under multicollinearity.}` | RidgeCV λ=0.001, β_BCS=−1.53, β_centrality=0.78, R²=0.594; 解析证明 β_BCS<0 对所有 λ≥0 成立; 仅做方向性解读 |
| **B: Bootstrap CI** | 新 subsection E.3 (`sec:appendix_bootstrap_ci`, page 17) | 164 FewRel batches, 6 个 Jaccard 阈值下 cluster-robust SE = 0.96–0.97× OLS SE, slope 显著 (p<10⁻¹¹), R² CI 宽度变化 −6%~+6%, 结论 robust |
| **C: Domain Distribution** | 新 subsection E.4 (`sec:appendix_domain_distribution`, page 17) | χ²=230.74 (p<0.001), high-BCS→science/taxonomy 49.5% + event/temporal 26.0%, low-BCS→geography 45.5% + creative_work 25.5%; 解释为 mediator 非独立 confound |

**编译结果**: 0 errors, 0 undefined references, 27 pages total (body ≤ 8 pages, appendix 从 page 13 起)。`\ref{sec:appendix_partial_corr}` 正确解析为 E.1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 224244,
  "duration_api_ms": 219225,
  "num_turns": 28,
  "stop_reason": "end_turn",
  "session_id": "27ebd705-f9eb-4b2f-985c-f7bd62d83652",
  "total_cost_usd": 1.1258488,
  "usage": {
    "input_tokens": 29,
    "cache_creation_input_tokens": 40848,
    "cache_read_input_tokens": 1156415,
    "output_tokens": 6956,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40848,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 481,
        "cache_read_input_tokens": 52569,
        "cache_creation_input_tokens": 120,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 120
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1991,
      "outputTokens": 4681,
      "cacheReadInputTokens": 312428,
      "cacheCreationInputTokens": 49326,
      "webSearchRequests": 0,
      "costUSD": 0.11829630000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 29,
      "outputTokens": 6956,
      "cacheReadInputTokens": 1156415,
      "cacheCreationInputTokens": 40848,
      "webSearchRequests": 0,
      "costUSD": 1.0075525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7dbfdcf3-ef4f-4d22-a420-b21e934260b5"
}
```

</details>

---
