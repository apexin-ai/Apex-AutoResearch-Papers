# ops final anon repo push

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/workers/worker_ops_final_anon_repo_push_20260523T190556.log`
- **Structured JSON:** [`69780abdc8c6da51670a.json`](../../sessions/69/69780abdc8c6da51670a.json)

## Before a recorded user message

81 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "3c5cc8c9-c63c-4a1f-8660-eae775526c69",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory/memory/"
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
    "resetsAt": 1779576000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b5877f3d-0115-45eb-a884-d3ffc359184c",
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to push the latest paper and code to an anonymous GitHub repository. This involves working on the remote server (westd-32570) to:

1. Prepare a clean temp directory
2. Copy relevant files
3. Anonymize them
4. Create a git repo and push

Let me start by connecting to the server and executing the steps. I'll use the MCP tools (ssh_execute and ssh_read_only) to work on the remote server.

Let me first load the necessary tool schemas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "4bda611e-86e8-43b2-9e6a-01b88e218b93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GrVVmjUYnf3tWJb5UuipQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15702,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15702
      },
      "output_tokens": 28,
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

开始执行匿名 repo 推送任务。先加载所需工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "01cb0659-0971-4186-8b92-f5daedf3e37f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GrVVmjUYnf3tWJb5UuipQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15702,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15702
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KPGJGAumeCJeFAVLq4KLgh`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "64b35582-b623-4c73-b818-3df23ee068e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013GrVVmjUYnf3tWJb5UuipQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15702,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15702
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-23T19:06:12.227Z_

<details><summary>↩ Tool result · `toolu_01KPGJGAumeCJeFAVLq4KLgh`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "fcb39ff7-5e7c-426a-9bec-b70b28195976",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Good, tools are loaded. Let me start by examining the file structure on the server, then proceed with the anonymization and push process. I'll work on the server directly since that's where the code and paper are.

Let me first check the file structure, then do everything on the server as the task suggests.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "d74715de-b5f2-46ac-a5fb-3ed11d2787c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMqEGAriHaf1xmZSf9B6Wb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 27543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1023
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

_source line 9_

先查看服务器上的文件结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "54ecf49c-f929-4f2e-bdb6-d5402a1af693",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMqEGAriHaf1xmZSf9B6Wb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 27543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1023
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01AAbaojmHB2U7317f4Xhy7h`</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory -type f \\( -name \"*.py\" -o -name \"*.sh\" -o -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.txt\" -o -name \"*.cfg\" -o -name \"*.toml\" -o -name \"*.json\" -o -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.bst\" -o -name \"*.sty\" -o -name \"*.cls\" -o -name \"*.bbl\" -o -name \"*.pdf\" \\) -not -path \"*__pycache__*\" -not -path \"*wandb*\" -not -path \"*.git/*\" -not -path \"*data/exp*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "e1cf15aa-082a-4286-8f01-4248eb275cc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMqEGAriHaf1xmZSf9B6Wb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 27543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1023
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

_source line 11 · 2026-05-23T19:06:21.022Z_

<details><summary>↩ Tool result · `toolu_01AAbaojmHB2U7317f4Xhy7h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/src/data/__init__.py\\n/root/nlp_variance_gtheory/src/data/sample_mmlu.py\\n/root/nlp_variance_gtheory/src/data/few_shot.py\\n/root/nlp_variance_gtheory/src/data/prompt_templates.py\\n/root/nlp_variance_gtheory/src/data/sample_benchmarks.py\\n/root/nlp_variance_gtheory/src/design/__init__.py\\n/root/nlp_variance_gtheory/src/design/generate_design.py\\n/root/nlp_variance_gtheory/src/design/shard_design.py\\n/root/nlp_variance_gtheory/src/inference/__init__.py\\n/root/nlp_variance_gtheory/src/inference/vllm_runner.py\\n/root/nlp_variance_gtheory/src/inference/run_experiment.py\\n/root/nlp_variance_gtheory/src/inference/sanity_check.py\\n/root/nlp_variance_gtheory/src/inference/benchmark_utils.py\\n/root/nlp_variance_gtheory/src/analysis/__init__.py\\n/root/nlp_variance_gtheory/src/analysis/variance_decomposition.py\\n/root/nlp_variance_gtheory/src/analysis/d_study.py\\n/root/nlp_variance_gtheory/src/analysis/visualize.py\\n/root/nlp_variance_gtheory/src/analysis/bootstrap_ci.py\\n/root/nlp_variance_gtheory/src/analysis/model_facet_analysis.py\\n/root/nlp_variance_gtheory/src/analysis/reml_em.py\\n/root/nlp_variance_gtheory/src/__init__.py\\n/root/nlp_variance_gtheory/src/config/__init__.py\\n/root/nlp_variance_gtheory/src/config/model_paths.py\\n/root/nlp_variance_gtheory/data/mmlu_items.json\\n/root/nlp_variance_gtheory/data/few_shot_examples.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001.json\\n/root/nlp_variance_gtheory/data/few_shot_exp001.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample1.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample2.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample3.json\\n/root/nlp_variance_gtheory/data/gsm8k_items_exp002.json\\n/root/nlp_variance_gtheory/data/arc_items_exp002.json\\n/root/nlp_variance_gtheory/data/hellaswag_items_exp002.json\\n/root/nlp_variance_gtheory/data/few_shot_gsm8k.json\\n/root/nlp_variance_gtheory/data/few_shot_arc.json\\n/root/nlp_variance_gtheory/data/few_shot_hellaswag.json\\n/root/nlp_variance_gtheory/data/math_items_exp002.json\\n/root/nlp_variance_gtheory/data/few_shot_math.json\\n/root/nlp_variance_gtheory/results/sanity_check.json\\n/root/nlp_variance_gtheory/results/variance_components.json\\n/root/nlp_variance_gtheory/results/d_study_results.json\\n/root/nlp_variance_gtheory/results/variance_components_text.json\\n/root/nlp_variance_gtheory/results/d_study_results_text.json\\n/root/nlp_variance_gtheory/results/analysis/llama_single_model_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/fixed_vs_random_sensitivity.json\\n/root/nlp_variance_gtheory/results/analysis/binary_data_limitation.json\\n/root/nlp_variance_gtheory/results/analysis/bootstrap_vs_jackknife.json\\n/root/nlp_variance_gtheory/results/analysis/temperature_stratified_analysis.json\\n/root/nlp_variance_gtheory/results/analysis/irt_vs_gtheory.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_bootstrap.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_balanced_meta.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_3way_bf16_meta.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_2way_precision_meta.json\\n/root/nlp_variance_gtheory/results/analysis/llama_precision_balanced_meta.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_g_coefficients.json\\n/root/nlp_variance_gtheory/results/analysis/dataset_b_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/dataset_a_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_reml.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_reml_500iter.json\\n/root/nlp_variance_gtheory/results/analysis/dataset_a4_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/leave_one_model_out.json\\n/root/nlp_variance_gtheory/results/analysis/bf16_fp16_only_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/lomo_matched_spec.json\\n/root/nlp_variance_gtheory/results/analysis/exp001b_resampling_gstudy.json\\n/root/nlp_variance_gtheory/results/\\n\\n... [截断: 输出过长，省略 9264 字符] ...\\n\\n_gradient_4model.py\\n/root/nlp_variance_gtheory/scripts/audit_g_item.py\\n/root/nlp_variance_gtheory/scripts/fix_g_item.py\\n/root/nlp_variance_gtheory/scripts/sensitivity_analyses.py\\n/root/nlp_variance_gtheory/scripts/post_exp002_master.sh\\n/root/nlp_variance_gtheory/scripts/gsm8k_to_math_monitor.sh\\n/root/nlp_variance_gtheory/scripts/dstudy_single_condition.py\\n/root/nlp_variance_gtheory/scripts/auto_start_new_models.sh\\n/root/nlp_variance_gtheory/scripts/math_then_new_models.sh\\n/root/nlp_variance_gtheory/scripts/chain_single_gpu.sh\\n/root/nlp_variance_gtheory/scripts/gpu0_internlm_math_accel.sh\\n/root/nlp_variance_gtheory/scripts/r1_w4_ordering_dstudy.py\\n/root/nlp_variance_gtheory/scripts/henderson_i_gstudy.py\\n/root/nlp_variance_gtheory/scripts/m022_henderson_unified.py\\n/root/nlp_variance_gtheory/scripts/exp004_per_benchmark_gstudy_mc.py\\n/root/nlp_variance_gtheory/scripts/exp004_cross_benchmark_analysis.py\\n/root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp004_cross_benchmark_analysis_v2.py\\n/root/nlp_variance_gtheory/scripts/exp001_analysis/dstudy_henderson_i.py\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/mmlu_8model_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/math_8model_and_permtest.py\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/lomo_8model_mmlu.py\\n/root/nlp_variance_gtheory/scripts/exp004_hellaswag_8model_gstudy.py\\n/root/nlp_variance_gtheory/scripts/d014_item_heterogeneity.py\\n/root/nlp_variance_gtheory/scripts/d014v2_subject_gradient_8model.py\\n/root/nlp_variance_gtheory/scripts/exp004_arc_8model_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp004_three_in_one.py\\n/root/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py\\n/root/nlp_variance_gtheory/scripts/gitem_consistency_check.py\\n/root/nlp_variance_gtheory/scripts/hellaswag_2temp_gstudy.py\\n/root/nlp_variance_gtheory/scripts/hellaswag_2temp_gstudy_v2.py\\n/root/nlp_variance_gtheory/scripts/exp004_bootstrap_ci_all.py\\n/root/nlp_variance_gtheory/scripts/dstudy_per_benchmark.py\\n/root/nlp_variance_gtheory/scripts/dstudy_bootstrap_ci_propagation.py\\n/root/nlp_variance_gtheory/scripts/exp001_bf16_2temp_subset.py\\n/root/nlp_variance_gtheory/scripts/run_exp003_3b.sh\\n/root/nlp_variance_gtheory/scripts/watchdog_inference.sh\\n/root/nlp_variance_gtheory/scripts/watchdog_v2.sh\\n/root/nlp_variance_gtheory/scripts/exp003_scale_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp003_scale_crossed_gstudy.py\\n/root/nlp_variance_gtheory/scripts/binary_sim_ranking_consistency.py\\n/root/nlp_variance_gtheory/scripts/deepseek_lomo_cross_benchmark.py\\n/root/nlp_variance_gtheory/scripts/difficulty_heterogeneity.py\\n/root/nlp_variance_gtheory/scripts/stratified_bootstrap_mmlu.py\\n/root/nlp_variance_gtheory/scripts/intermediate_dstudy.py\\n/root/nlp_variance_gtheory/scripts/exp001b_henderson_i.py\\n/root/nlp_variance_gtheory/scripts/watchdog_72b.sh\\n/root/nlp_variance_gtheory/scripts/lomo_8x5.py\\n/root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py\\n/root/nlp_variance_gtheory/scripts/mmlu_subject_scatter.py\\n/root/nlp_variance_gtheory/scripts/forward_prediction.py\\n/root/nlp_variance_gtheory/scripts/exp003_72b_and_crossed.py\\n/root/nlp_variance_gtheory/scripts/exp004_subject_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_inference.py\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_mmlu_only.py\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/analyze_llama70b_mmlu.py\\n/root/nlp_variance_gtheory/artifacts/analysis/temperature_stratified_analysis.json\\n/root/nlp_variance_gtheory/run_reml_500.py\\n/root/nlp_variance_gtheory/run_reml_500.sh\\n/root/nlp_variance_gtheory/run_reml_500_v2.py\\n/root/nlp_variance_gtheory/run_reml_500_v3.py\\n/root/nlp_variance_gtheory/tests/test_prompt_templates_multi.py\\n/root/nlp_variance_gtheory/figures/paper/gen_fig1_cross_benchmark.py\\n/root/nlp_variance_gtheory/figures/paper/fig1_cross_benchmark.pdf\\n/root/nlp_variance_gtheory/partial_credit_multimodel.py\\n/root/nlp_variance_gtheory/run_mmlu_after.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "ef4a7897-6638-47aa-a903-37d4126bce57",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/nlp_variance_gtheory/src/data/__init__.py\\\\n/root/nlp_variance_gtheory/src/data/sample_mmlu.py\\\\n/root/nlp_variance_gtheory/src/data/few_shot.py\\\\n/root/nlp_variance_gtheory/src/data/prompt_templates.py\\\\n/root/nlp_variance_gtheory/src/data/sample_benchmarks.py\\\\n/root/nlp_variance_gtheory/src/design/__init__.py\\\\n/root/nlp_variance_gtheory/src/design/generate_design.py\\\\n/root/nlp_variance_gtheory/src/design/shard_design.py\\\\n/root/nlp_variance_gtheory/src/inference/__init__.py\\\\n/root/nlp_variance_gtheory/src/inference/vllm_runner.py\\\\n/root/nlp_variance_gtheory/src/inference/run_experiment.py\\\\n/root/nlp_variance_gtheory/src/inference/sanity_check.py\\\\n/root/nlp_variance_gtheory/src/inference/benchmark_utils.py\\\\n/root/nlp_variance_gtheory/src/analysis/__init__.py\\\\n/root/nlp_variance_gtheory/src/analysis/variance_decomposition.py\\\\n/root/nlp_variance_gtheory/src/analysis/d_study.py\\\\n/root/nlp_variance_gtheory/src/analysis/visualize.py\\\\n/root/nlp_variance_gtheory/src/analysis/bootstrap_ci.py\\\\n/root/nlp_variance_gtheory/src/analysis/model_facet_analysis.py\\\\n/root/nlp_variance_gtheory/src/analysis/reml_em.py\\\\n/root/nlp_variance_gtheory/src/__init__.py\\\\n/root/nlp_variance_gtheory/src/config/__init__.py\\\\n/root/nlp_variance_gtheory/src/config/model_paths.py\\\\n/root/nlp_variance_gtheory/data/mmlu_items.json\\\\n/root/nlp_variance_gtheory/data/few_shot_examples.json\\\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001.json\\\\n/root/nlp_variance_gtheory/data/few_shot_exp001.json\\\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample1.json\\\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample2.json\\\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample3.json\\\\n/root/nlp_variance_gtheory/data/gsm8k_items_exp002.json\\\\n/root/nlp_variance_gtheory/data/arc_items_exp002.json\\\\n/root/nlp_variance_gtheory/data/hellaswag_items_exp002.json\\\\n/root/nlp_variance_gtheory/data/few_shot_gsm8k.json\\\\n/root/nlp_variance_gtheory/data/few_shot_arc.json\\\\n/root/nlp_variance_gtheory/data/few_shot_hellaswag.json\\\\n/root/nlp_variance_gtheory/data/math_items_exp002.json\\\\n/root/nlp_variance_gtheory/data/few_shot_math.json\\\\n/root/nlp_variance_gtheory/results/sanity_check.json\\\\n/root/nlp_variance_gtheory/results/variance_components.json\\\\n/root/nlp_variance_gtheory/results/d_study_results.json\\\\n/root/nlp_variance_gtheory/results/variance_components_text.json\\\\n/root/nlp_variance_gtheory/results/d_study_results_text.json\\\\n/root/nlp_variance_gtheory/results/analysis/llama_single_model_gstudy.json\\\\n/root/nlp_variance_gtheory/results/analysis/fixed_vs_random_sensitivity.json\\\\n/root/nlp_variance_gtheory/results/analysis/binary_data_limitation.json\\\\n/root/nlp_variance_gtheory/results/analysis/bootstrap_vs_jackknife.json\\\\n/root/nlp_variance_gtheory/results/analysis/temperature_stratified_analysis.json\\\\n/root/nlp_variance_gtheory/results/analysis/irt_vs_gtheory.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_gstudy.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_bootstrap.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_balanced_meta.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_3way_bf16_meta.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_2way_precision_meta.json\\\\n/root/nlp_variance_gtheory/results/analysis/llama_precision_balanced_meta.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_g_coefficients.json\\\\n/root/nlp_variance_gtheory/results/analysis/dataset_b_gstudy.json\\\\n/root/nlp_variance_gtheory/results/analysis/dataset_a_gstudy.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_reml.json\\\\n/root/nlp_variance_gtheory/results/analysis/cross_model_reml_500iter.json\\\\n/root/nlp_variance_gtheory/results/analysis/dataset_a4_gstudy.json\\\\n/root/nlp_variance_gtheory/results/analysis/leave_one_model_out.json\\\\n/root/nlp_variance_gtheory/results/analysis/bf16_fp16_only_gstudy.json\\\\n/root/nlp_variance_gtheory/results/analysis/lomo_matched_spec.json\\\\n/root/nlp_variance_gtheory/results/analysis/exp001b_resampling_gstudy.json\\\\n/root/nlp_variance_gtheory/results/\\\\n\\\\n... [截断: 输出过长，省略 9264 字符] ...\\\\n\\\\n_gradient_4model.py\\\\n/root/nlp_variance_gtheory/scripts/audit_g_item.py\\\\n/root/nlp_variance_gtheory/scripts/fix_g_item.py\\\\n/root/nlp_variance_gtheory/scripts/sensitivity_analyses.py\\\\n/root/nlp_variance_gtheory/scripts/post_exp002_master.sh\\\\n/root/nlp_variance_gtheory/scripts/gsm8k_to_math_monitor.sh\\\\n/root/nlp_variance_gtheory/scripts/dstudy_single_condition.py\\\\n/root/nlp_variance_gtheory/scripts/auto_start_new_models.sh\\\\n/root/nlp_variance_gtheory/scripts/math_then_new_models.sh\\\\n/root/nlp_variance_gtheory/scripts/chain_single_gpu.sh\\\\n/root/nlp_variance_gtheory/scripts/gpu0_internlm_math_accel.sh\\\\n/root/nlp_variance_gtheory/scripts/r1_w4_ordering_dstudy.py\\\\n/root/nlp_variance_gtheory/scripts/henderson_i_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/m022_henderson_unified.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_per_benchmark_gstudy_mc.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_cross_benchmark_analysis.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_cross_benchmark_analysis_v2.py\\\\n/root/nlp_variance_gtheory/scripts/exp001_analysis/dstudy_henderson_i.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/mmlu_8model_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/math_8model_and_permtest.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/lomo_8model_mmlu.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_hellaswag_8model_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/d014_item_heterogeneity.py\\\\n/root/nlp_variance_gtheory/scripts/d014v2_subject_gradient_8model.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_arc_8model_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_three_in_one.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py\\\\n/root/nlp_variance_gtheory/scripts/gitem_consistency_check.py\\\\n/root/nlp_variance_gtheory/scripts/hellaswag_2temp_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/hellaswag_2temp_gstudy_v2.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_bootstrap_ci_all.py\\\\n/root/nlp_variance_gtheory/scripts/dstudy_per_benchmark.py\\\\n/root/nlp_variance_gtheory/scripts/dstudy_bootstrap_ci_propagation.py\\\\n/root/nlp_variance_gtheory/scripts/exp001_bf16_2temp_subset.py\\\\n/root/nlp_variance_gtheory/scripts/run_exp003_3b.sh\\\\n/root/nlp_variance_gtheory/scripts/watchdog_inference.sh\\\\n/root/nlp_variance_gtheory/scripts/watchdog_v2.sh\\\\n/root/nlp_variance_gtheory/scripts/exp003_scale_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/exp003_scale_crossed_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/binary_sim_ranking_consistency.py\\\\n/root/nlp_variance_gtheory/scripts/deepseek_lomo_cross_benchmark.py\\\\n/root/nlp_variance_gtheory/scripts/difficulty_heterogeneity.py\\\\n/root/nlp_variance_gtheory/scripts/stratified_bootstrap_mmlu.py\\\\n/root/nlp_variance_gtheory/scripts/intermediate_dstudy.py\\\\n/root/nlp_variance_gtheory/scripts/exp001b_henderson_i.py\\\\n/root/nlp_variance_gtheory/scripts/watchdog_72b.sh\\\\n/root/nlp_variance_gtheory/scripts/lomo_8x5.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py\\\\n/root/nlp_variance_gtheory/scripts/mmlu_subject_scatter.py\\\\n/root/nlp_variance_gtheory/scripts/forward_prediction.py\\\\n/root/nlp_variance_gtheory/scripts/exp003_72b_and_crossed.py\\\\n/root/nlp_variance_gtheory/scripts/exp004_subject_gstudy.py\\\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_inference.py\\\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_mmlu_only.py\\\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/analyze_llama70b_mmlu.py\\\\n/root/nlp_variance_gtheory/artifacts/analysis/temperature_stratified_analysis.json\\\\n/root/nlp_variance_gtheory/run_reml_500.py\\\\n/root/nlp_variance_gtheory/run_reml_500.sh\\\\n/root/nlp_variance_gtheory/run_reml_500_v2.py\\\\n/root/nlp_variance_gtheory/run_reml_500_v3.py\\\\n/root/nlp_variance_gtheory/tests/test_prompt_templates_multi.py\\\\n/root/nlp_variance_gtheory/figures/paper/gen_fig1_cross_benchmark.py\\\\n/root/nlp_variance_gtheory/figures/paper/fig1_cross_benchmark.pdf\\\\n/root/nlp_variance_gtheory/partial_credit_multimodel.py\\\\n/root/nlp_variance_gtheory/run_mmlu_after.sh\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.17}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/src/data/__init__.py\\n/root/nlp_variance_gtheory/src/data/sample_mmlu.py\\n/root/nlp_variance_gtheory/src/data/few_shot.py\\n/root/nlp_variance_gtheory/src/data/prompt_templates.py\\n/root/nlp_variance_gtheory/src/data/sample_benchmarks.py\\n/root/nlp_variance_gtheory/src/design/__init__.py\\n/root/nlp_variance_gtheory/src/design/generate_design.py\\n/root/nlp_variance_gtheory/src/design/shard_design.py\\n/root/nlp_variance_gtheory/src/inference/__init__.py\\n/root/nlp_variance_gtheory/src/inference/vllm_runner.py\\n/root/nlp_variance_gtheory/src/inference/run_experiment.py\\n/root/nlp_variance_gtheory/src/inference/sanity_check.py\\n/root/nlp_variance_gtheory/src/inference/benchmark_utils.py\\n/root/nlp_variance_gtheory/src/analysis/__init__.py\\n/root/nlp_variance_gtheory/src/analysis/variance_decomposition.py\\n/root/nlp_variance_gtheory/src/analysis/d_study.py\\n/root/nlp_variance_gtheory/src/analysis/visualize.py\\n/root/nlp_variance_gtheory/src/analysis/bootstrap_ci.py\\n/root/nlp_variance_gtheory/src/analysis/model_facet_analysis.py\\n/root/nlp_variance_gtheory/src/analysis/reml_em.py\\n/root/nlp_variance_gtheory/src/__init__.py\\n/root/nlp_variance_gtheory/src/config/__init__.py\\n/root/nlp_variance_gtheory/src/config/model_paths.py\\n/root/nlp_variance_gtheory/data/mmlu_items.json\\n/root/nlp_variance_gtheory/data/few_shot_examples.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001.json\\n/root/nlp_variance_gtheory/data/few_shot_exp001.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample1.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample2.json\\n/root/nlp_variance_gtheory/data/mmlu_items_exp001b_sample3.json\\n/root/nlp_variance_gtheory/data/gsm8k_items_exp002.json\\n/root/nlp_variance_gtheory/data/arc_items_exp002.json\\n/root/nlp_variance_gtheory/data/hellaswag_items_exp002.json\\n/root/nlp_variance_gtheory/data/few_shot_gsm8k.json\\n/root/nlp_variance_gtheory/data/few_shot_arc.json\\n/root/nlp_variance_gtheory/data/few_shot_hellaswag.json\\n/root/nlp_variance_gtheory/data/math_items_exp002.json\\n/root/nlp_variance_gtheory/data/few_shot_math.json\\n/root/nlp_variance_gtheory/results/sanity_check.json\\n/root/nlp_variance_gtheory/results/variance_components.json\\n/root/nlp_variance_gtheory/results/d_study_results.json\\n/root/nlp_variance_gtheory/results/variance_components_text.json\\n/root/nlp_variance_gtheory/results/d_study_results_text.json\\n/root/nlp_variance_gtheory/results/analysis/llama_single_model_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/fixed_vs_random_sensitivity.json\\n/root/nlp_variance_gtheory/results/analysis/binary_data_limitation.json\\n/root/nlp_variance_gtheory/results/analysis/bootstrap_vs_jackknife.json\\n/root/nlp_variance_gtheory/results/analysis/temperature_stratified_analysis.json\\n/root/nlp_variance_gtheory/results/analysis/irt_vs_gtheory.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_bootstrap.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_balanced_meta.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_3way_bf16_meta.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_2way_precision_meta.json\\n/root/nlp_variance_gtheory/results/analysis/llama_precision_balanced_meta.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_g_coefficients.json\\n/root/nlp_variance_gtheory/results/analysis/dataset_b_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/dataset_a_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_reml.json\\n/root/nlp_variance_gtheory/results/analysis/cross_model_reml_500iter.json\\n/root/nlp_variance_gtheory/results/analysis/dataset_a4_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/leave_one_model_out.json\\n/root/nlp_variance_gtheory/results/analysis/bf16_fp16_only_gstudy.json\\n/root/nlp_variance_gtheory/results/analysis/lomo_matched_spec.json\\n/root/nlp_variance_gtheory/results/analysis/exp001b_resampling_gstudy.json\\n/root/nlp_variance_gtheory/results/\\n\\n... [截断: 输出过长，省略 9264 字符] ...\\n\\n_gradient_4model.py\\n/root/nlp_variance_gtheory/scripts/audit_g_item.py\\n/root/nlp_variance_gtheory/scripts/fix_g_item.py\\n/root/nlp_variance_gtheory/scripts/sensitivity_analyses.py\\n/root/nlp_variance_gtheory/scripts/post_exp002_master.sh\\n/root/nlp_variance_gtheory/scripts/gsm8k_to_math_monitor.sh\\n/root/nlp_variance_gtheory/scripts/dstudy_single_condition.py\\n/root/nlp_variance_gtheory/scripts/auto_start_new_models.sh\\n/root/nlp_variance_gtheory/scripts/math_then_new_models.sh\\n/root/nlp_variance_gtheory/scripts/chain_single_gpu.sh\\n/root/nlp_variance_gtheory/scripts/gpu0_internlm_math_accel.sh\\n/root/nlp_variance_gtheory/scripts/r1_w4_ordering_dstudy.py\\n/root/nlp_variance_gtheory/scripts/henderson_i_gstudy.py\\n/root/nlp_variance_gtheory/scripts/m022_henderson_unified.py\\n/root/nlp_variance_gtheory/scripts/exp004_per_benchmark_gstudy_mc.py\\n/root/nlp_variance_gtheory/scripts/exp004_cross_benchmark_analysis.py\\n/root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp004_cross_benchmark_analysis_v2.py\\n/root/nlp_variance_gtheory/scripts/exp001_analysis/dstudy_henderson_i.py\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/mmlu_8model_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/math_8model_and_permtest.py\\n/root/nlp_variance_gtheory/scripts/exp004_analysis/lomo_8model_mmlu.py\\n/root/nlp_variance_gtheory/scripts/exp004_hellaswag_8model_gstudy.py\\n/root/nlp_variance_gtheory/scripts/d014_item_heterogeneity.py\\n/root/nlp_variance_gtheory/scripts/d014v2_subject_gradient_8model.py\\n/root/nlp_variance_gtheory/scripts/exp004_arc_8model_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp004_three_in_one.py\\n/root/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py\\n/root/nlp_variance_gtheory/scripts/gitem_consistency_check.py\\n/root/nlp_variance_gtheory/scripts/hellaswag_2temp_gstudy.py\\n/root/nlp_variance_gtheory/scripts/hellaswag_2temp_gstudy_v2.py\\n/root/nlp_variance_gtheory/scripts/exp004_bootstrap_ci_all.py\\n/root/nlp_variance_gtheory/scripts/dstudy_per_benchmark.py\\n/root/nlp_variance_gtheory/scripts/dstudy_bootstrap_ci_propagation.py\\n/root/nlp_variance_gtheory/scripts/exp001_bf16_2temp_subset.py\\n/root/nlp_variance_gtheory/scripts/run_exp003_3b.sh\\n/root/nlp_variance_gtheory/scripts/watchdog_inference.sh\\n/root/nlp_variance_gtheory/scripts/watchdog_v2.sh\\n/root/nlp_variance_gtheory/scripts/exp003_scale_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp003_scale_crossed_gstudy.py\\n/root/nlp_variance_gtheory/scripts/binary_sim_ranking_consistency.py\\n/root/nlp_variance_gtheory/scripts/deepseek_lomo_cross_benchmark.py\\n/root/nlp_variance_gtheory/scripts/difficulty_heterogeneity.py\\n/root/nlp_variance_gtheory/scripts/stratified_bootstrap_mmlu.py\\n/root/nlp_variance_gtheory/scripts/intermediate_dstudy.py\\n/root/nlp_variance_gtheory/scripts/exp001b_henderson_i.py\\n/root/nlp_variance_gtheory/scripts/watchdog_72b.sh\\n/root/nlp_variance_gtheory/scripts/lomo_8x5.py\\n/root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py\\n/root/nlp_variance_gtheory/scripts/mmlu_subject_scatter.py\\n/root/nlp_variance_gtheory/scripts/forward_prediction.py\\n/root/nlp_variance_gtheory/scripts/exp003_72b_and_crossed.py\\n/root/nlp_variance_gtheory/scripts/exp004_subject_gstudy.py\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_inference.py\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/run_llama70b_mmlu_only.py\\n/root/nlp_variance_gtheory/scripts/exp_llama70b/analyze_llama70b_mmlu.py\\n/root/nlp_variance_gtheory/artifacts/analysis/temperature_stratified_analysis.json\\n/root/nlp_variance_gtheory/run_reml_500.py\\n/root/nlp_variance_gtheory/run_reml_500.sh\\n/root/nlp_variance_gtheory/run_reml_500_v2.py\\n/root/nlp_variance_gtheory/run_reml_500_v3.py\\n/root/nlp_variance_gtheory/tests/test_prompt_templates_multi.py\\n/root/nlp_variance_gtheory/figures/paper/gen_fig1_cross_benchmark.py\\n/root/nlp_variance_gtheory/figures/paper/fig1_cross_benchmark.pdf\\n/root/nlp_variance_gtheory/partial_credit_multimodel.py\\n/root/nlp_variance_gtheory/run_mmlu_after.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XgPj67gc95ugh3cFYQmaRT`</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "2e4e3023-d9ed-4921-a574-2224b52b6335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdTomtDDZDC6swRNKX2Axb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3828,
      "cache_read_input_tokens": 28566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3828
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

_source line 13 · 2026-05-23T19:06:25.350Z_

<details><summary>↩ Tool result · `toolu_01XgPj67gc95ugh3cFYQmaRT`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/nlp_variance_gtheory/docs/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "9da9ec71-7dd0-4e29-b144-6e6b89c4408a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/nlp_variance_gtheory/docs/paper/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/nlp_variance_gtheory/docs/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015RvyC4fTDi5b784Tyeh3Mi`</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory -name \"*.tex\" -o -name \"*.bib\" -o -name \"*.bbl\" -o -name \"*.sty\" -o -name \"*.cls\" -o -name \"*.bst\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "1e260607-aef6-4c4b-8553-2598c9fe8d1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jyoqed2kidWsXWXZqkJoJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 32394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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

_source line 15 · 2026-05-23T19:06:29.605Z_

<details><summary>↩ Tool result · `toolu_015RvyC4fTDi5b784Tyeh3Mi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "99183303-1da8-4c46-b810-9df24f5031eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Hmm, no tex/bib files found on the server. Let me check more places.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "4bb88d2f-419d-410b-b16b-a0a2741314d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8NFeibN7s9YFNyywHQZ58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 32601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 21,
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

_source line 17_

没有 tex 文件在服务器上。让我检查本地项目目录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "26575c35-6213-4318-905a-9bcf5d3d78f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8NFeibN7s9YFNyywHQZ58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 32601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 21,
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

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_0123WbFZ5Z5c7u1u5AFYTvWt`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "36832ee7-4d8f-47a0-8716-d718a943cfa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8NFeibN7s9YFNyywHQZ58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 32601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 21,
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

_source line 19 · 2026-05-23T19:06:35.752Z_

<details><summary>↩ Tool result · `toolu_0123WbFZ5Z5c7u1u5AFYTvWt`</summary>

```text
artifacts/dream_reports/dream_20260520T190053/best/paper.tex
artifacts/dream_reports/dream_20260520T190053/median/paper.tex
artifacts/dream_reports/dream_20260520T190053/worst/paper.tex
artifacts/dream_reports/dream_20260520T222113/best/paper.tex
artifacts/dream_reports/dream_20260520T222113/median/paper.tex
artifacts/dream_reports/dream_20260520T222113/worst/paper.tex
artifacts/dream_reports/dream_20260521T032813/best/paper.tex
artifacts/dream_reports/dream_20260521T032813/median/paper.tex
artifacts/dream_reports/dream_20260521T032813/worst/paper.tex
artifacts/dream_reports/dream_20260521T044739/best/paper.tex
artifacts/dream_reports/dream_20260521T044739/median/paper.tex
artifacts/dream_reports/dream_20260521T044739/worst/paper.tex
artifacts/dream_reports/dream_20260521T075006/best/paper.tex
artifacts/dream_reports/dream_20260521T075006/median/paper.tex
artifacts/dream_reports/dream_20260521T075006/worst/paper.tex
artifacts/dream_reports/dream_20260521T122449/best/paper.tex
artifacts/dream_reports/dream_20260521T122449/median/paper.tex
artifacts/dream_reports/dream_20260521T122449/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/limitations.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "6aa7b92a-cb7f-4ec2-b98c-d3fd3842e731",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260520T190053/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T190053/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T190053/worst/paper.tex",
      "artifacts/dream_reports/dream_20260520T222113/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T222113/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T222113/worst/paper.tex",
      "artifacts/dream_reports/dream_20260521T032813/best/paper.tex",
      "artifacts/dream_reports/dream_20260521T032813/median/paper.tex",
      "artifacts/dream_reports/dream_20260521T032813/worst/paper.tex",
      "artifacts/dream_reports/dream_20260521T044739/best/paper.tex",
      "artifacts/dream_reports/dream_20260521T044739/median/paper.tex",
      "artifacts/dream_reports/dream_20260521T044739/worst/paper.tex",
      "artifacts/dream_reports/dream_20260521T075006/best/paper.tex",
      "artifacts/dream_reports/dream_20260521T075006/median/paper.tex",
      "artifacts/dream_reports/dream_20260521T075006/worst/paper.tex",
      "artifacts/dream_reports/dream_20260521T122449/best/paper.tex",
      "artifacts/dream_reports/dream_20260521T122449/median/paper.tex",
      "artifacts/dream_reports/dream_20260521T122449/worst/paper.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/limitations.tex",
      "docs/paper/main.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experiments.tex",
      "docs/paper/limitations.tex",
      "docs/paper/abstract.tex"
    ],
    "durationMs": 28,
    "numFiles": 33,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01QQpWxLfLRy9BTDPAYe75WN`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "8db67f46-a3f7-43a7-bcfe-fa6fbc7afa9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8NFeibN7s9YFNyywHQZ58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 32601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 21,
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

_source line 21 · 2026-05-23T19:06:35.990Z_

<details><summary>↩ Tool result · `toolu_01QQpWxLfLRy9BTDPAYe75WN`</summary>

```text
artifacts/dream_reports/dream_20260521T122449/best/references.bib
artifacts/exp004/data/round5_bibtex_entries.bib
artifacts/exp-004/data/round5_bibtex_entries.bib
artifacts/exp004/data/round6_new_refs.bib
artifacts/exp004/data/round6_new_refs_a907a1.bib
artifacts/exp004/data/round7_refs_e2a5dc.bib
artifacts/exp004/data/round7_refs_522c27.bib
artifacts/exp004/data/round7_refs.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "dde3f307-0215-46d5-82e3-b3a31fe8e5a2",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260521T122449/best/references.bib",
      "artifacts/exp004/data/round5_bibtex_entries.bib",
      "artifacts/exp-004/data/round5_bibtex_entries.bib",
      "artifacts/exp004/data/round6_new_refs.bib",
      "artifacts/exp004/data/round6_new_refs_a907a1.bib",
      "artifacts/exp004/data/round7_refs_e2a5dc.bib",
      "artifacts/exp004/data/round7_refs_522c27.bib",
      "artifacts/exp004/data/round7_refs.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 38,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
The paper source is in the local project directory at `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/`. The code is on the remote server. I need to:

1. Get the code from the remote server
2. Combine it with the paper from local
3. Anonymize everything
4. Push to GitHub

Since the paper is local and the code is on the server, the best approach is to do the assembly on the server. Let me:
1. First copy the paper files to the server
2. Then do everything on the server

Actually, wait - I can't easily copy files TO the server. Let me think about this differently.


I'm realizing I could either assemble everything on the server if I can get the paper files there, or do it locally if I can pull the code down, but both have friction. The task mentions an alternative: create the anonymized repo directly on the server and push from there, which might be simpler than trying to move files around.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "b2ad9fc9-8118-4496-9df1-940065974ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rfAZA1rSSdMgV3pDaA4Fi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 32820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 979
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

_source line 23_

论文源码在本地而非服务器上。让我检查本地论文目录和服务器上是否有 git remote 可用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "5fb1a551-f76a-4022-90f8-02bb75868060",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rfAZA1rSSdMgV3pDaA4Fi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 32820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 979
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

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_019ThUr1afoSabEWSqqpxoLK`</summary>

```json
{
  "pattern": "*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "0cc49f67-3b21-47e8-a330-d94bc5bfbb6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rfAZA1rSSdMgV3pDaA4Fi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 32820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 979
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

_source line 25 · 2026-05-23T19:06:51.752Z_

<details><summary>↩ Tool result · `toolu_019ThUr1afoSabEWSqqpxoLK`</summary>

```text
docs/paper/aaai2026.sty
docs/paper/aaai2026.bst
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p4.png
docs/paper/_pdf_images/main_p5.png
docs/paper/_pdf_images/main_p6.png
docs/paper/_pdf_images/main_p7.png
docs/paper/_pdf_images/main_p8.png
docs/paper/_pdf_images/main_p9.png
docs/paper/_pdf_images/main_p10.png
docs/paper/_pdf_images/main_p11.png
docs/paper/_pdf_images/main_p12.png
docs/paper/_pdf_images/main_p13.png
docs/paper/_pdf_images/main_p14.png
docs/paper/_pdf_images/main_p15.png
docs/paper/_pdf_images/main_p16.png
docs/paper/_pdf_images/main_p17.png
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/references.bib
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
docs/paper/main.blg
docs/paper/main.bbl
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.fls
docs/paper/main.pdf
docs/paper/main.log
docs/paper/main.fdb_latexmk
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "6cbe47fa-05f1-458d-a66c-46677603f69a",
  "tool_use_result": {
    "filenames": [
      "docs/paper/aaai2026.sty",
      "docs/paper/aaai2026.bst",
      "docs/paper/acl.sty",
      "docs/paper/acl_natbib.bst",
      "docs/paper/main.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/_pdf_images/main_p1.png",
      "docs/paper/_pdf_images/main_p2.png",
      "docs/paper/_pdf_images/main_p3.png",
      "docs/paper/_pdf_images/main_p4.png",
      "docs/paper/_pdf_images/main_p5.png",
      "docs/paper/_pdf_images/main_p6.png",
      "docs/paper/_pdf_images/main_p7.png",
      "docs/paper/_pdf_images/main_p8.png",
      "docs/paper/_pdf_images/main_p9.png",
      "docs/paper/_pdf_images/main_p10.png",
      "docs/paper/_pdf_images/main_p11.png",
      "docs/paper/_pdf_images/main_p12.png",
      "docs/paper/_pdf_images/main_p13.png",
      "docs/paper/_pdf_images/main_p14.png",
      "docs/paper/_pdf_images/main_p15.png",
      "docs/paper/_pdf_images/main_p16.png",
      "docs/paper/_pdf_images/main_p17.png",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/references.bib",
      "docs/paper/related_work.tex",
      "docs/paper/experiments.tex",
      "docs/paper/limitations.tex",
      "docs/paper/abstract.tex",
      "docs/paper/main.blg",
      "docs/paper/main.bbl",
      "docs/paper/main.aux",
      "docs/paper/main.out",
      "docs/paper/main.fls",
      "docs/paper/main.pdf",
      "docs/paper/main.log",
      "docs/paper/main.fdb_latexmk"
    ],
    "durationMs": 6,
    "numFiles": 39,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012eHwYSPsjKBP38aRahjMQZ`</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "1852d1e9-2786-4859-b3aa-7e996c735168",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rfAZA1rSSdMgV3pDaA4Fi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 32820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 979
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

_source line 27 · 2026-05-23T19:06:52.392Z_

<details><summary>↩ Tool result · `toolu_012eHwYSPsjKBP38aRahjMQZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "9f4e319c-2cd0-480c-8e7c-0273581748dd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01X84GpwKicuQBYFcCjW263p`</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "a9b9d05b-645d-4cc4-8f3a-e03bea67170f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WytyqgmGuUJ3rLDKzXywX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1436,
      "cache_read_input_tokens": 33799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1436
      },
      "output_tokens": 69,
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

_source line 29 · 2026-05-23T19:07:00.693Z_

<details><summary>↩ Tool result · `toolu_01X84GpwKicuQBYFcCjW263p`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/nlp_variance_gtheory/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "c4c8622a-ae57-475f-8e58-1faa33410987",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"ls: cannot access '/root/nlp_variance_gtheory/paper/': No such file or directory\\\\n\\\", \\\"return_code\\\": 2}, \\\"error\\\": \\\"exit code 2\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/nlp_variance_gtheory/paper/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
The paper is only in the local project directory. The code is on the remote server. I'll need to:

1. Do the code part on the server
2. Transfer paper files to the server (by base64 encoding them and creating them via ssh_execute)
3. Or alternatively, do everything locally by downloading from the server

Actually, wait. Let me think about this more pragmatically. The code is on the server and the paper is local. The simplest approach:

1. On the server: prepare the code files in /tmp/anon_repo
2. Transfer paper files to the server (using ssh_execute with heredoc/base64)


3. Run the anonymization and git push from the server

I'll read the paper files locally first to understand what I'm working with, then encode and transfer them to the server where I can execute the full pipeline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "7a3a77c3-cafe-4afe-9cb5-4f6b744471da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQxd25Ji8PJwmBvEEa8X3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
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

_source line 31_

论文在本地、代码在服务器。我将在服务器上组装完整 repo。先在服务器上准备代码部分，同时读取本地论文文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "ff420c8b-ad80-4bfa-b350-e96db6b9ae23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQxd25Ji8PJwmBvEEa8X3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
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

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_013nn13F9g7KQawBRwDLAqLF`</summary>

```json
{
  "server": "westd-32570",
  "command": "rm -rf /tmp/anon_repo && mkdir -p /tmp/anon_repo && cd /root/nlp_variance_gtheory && cp -r src /tmp/anon_repo/ && cp -r scripts /tmp/anon_repo/ && mkdir -p /tmp/anon_repo/tests && cp tests/*.py /tmp/anon_repo/tests/ 2>/dev/null; cp requirements.txt /tmp/anon_repo/ 2>/dev/null; cp pyproject.toml /tmp/anon_repo/ 2>/dev/null; cp run_*.sh /tmp/anon_repo/ 2>/dev/null; cp run_*.py /tmp/anon_repo/ 2>/dev/null; mkdir -p /tmp/anon_repo/data && cp data/*.json /tmp/anon_repo/data/ 2>/dev/null; cp data/*.py /tmp/anon_repo/data/ 2>/dev/null; mkdir -p /tmp/anon_repo/results/analysis && cp results/*.json /tmp/anon_repo/results/ 2>/dev/null; cp results/analysis/*.json /tmp/anon_repo/results/analysis/ 2>/dev/null; cp -r figures /tmp/anon_repo/ 2>/dev/null; cp partial_credit_multimodel.py /tmp/anon_repo/ 2>/dev/null; echo \"DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "bd44e0f2-3e04-4557-a79e-dfddb7ece145",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQxd25Ji8PJwmBvEEa8X3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01CptduzLp5dZb6aVe5CgeRw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "4cfe1631-8aed-4b6b-968f-b9beb8a6abe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQxd25Ji8PJwmBvEEa8X3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 35235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
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

_source line 34 · 2026-05-23T19:07:16.146Z_

<details><summary>↩ Tool result · `toolu_013nn13F9g7KQawBRwDLAqLF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "9000c921-e6dd-4ef0-a117-849b784d34c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T19:07:16.159Z_

<details><summary>↩ Tool result · `toolu_01CptduzLp5dZb6aVe5CgeRw`</summary>

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
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "5d2167ce-492b-462f-84ca-fe35cede2604",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\graphicspath{{../../figures/paper/}}\n\n\\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n% === INTRODUCTION ===\n\\input{introduction}\n\n% === RELATED WORK ===\n\\input{related_work}\n\n% === METHOD ===\n\\input{method}\n\n% === EXPERIMENTS ===\n\\input{experiments}\n\n% === CONCLUSION ===\n\\input{conclusion}\n\n% === LIMITATIONS ===\n\\input{limitations}\n\n\\bibliography{references}\n\n% === APPENDIX ===\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01H6mfLiCPyTmqPY2Tf1tziT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "405620f5-0cf4-440c-9932-f201962f6625",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDJSjETqUAFdKkLPrMxey4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 35438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1445
      },
      "output_tokens": 69,
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

_source line 37 · 2026-05-23T19:07:19.930Z_

<details><summary>↩ Tool result · `toolu_01H6mfLiCPyTmqPY2Tf1tziT`</summary>

```text
1	Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. We apply Generalizability theory (G-theory) in a fully crossed design with up to seven facets across eight open-weight instruction-tuned models (7--9B parameters) and five benchmarks, totaling approximately 2.3 million evaluation records. D-study projections show that, under binary correctness scoring, a recommended 3-prompt $\times$ 3-seed design achieves $G \geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\times$ item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3$\times$ more total evaluations for 3$\times$ fewer items, a tradeoff that favors multi-facet designs when item construction is costly. Model$\times$item interaction (up to 36\%) indicates that models differ primarily in which items they find difficult, not in overall ability. Preliminary validation across a 3B--72B parameter range and a cross-family check (Llama-3.1-70B) confirms stable variance structure across architecture families. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "91d5969b-0ad3-4eb7-b11d-ac16eeded762",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex",
      "content": "Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. We apply Generalizability theory (G-theory) in a fully crossed design with up to seven facets across eight open-weight instruction-tuned models (7--9B parameters) and five benchmarks, totaling approximately 2.3 million evaluation records. D-study projections show that, under binary correctness scoring, a recommended 3-prompt $\\times$ 3-seed design achieves $G \\geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\\times$ item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3$\\times$ more total evaluations for 3$\\times$ fewer items, a tradeoff that favors multi-facet designs when item construction is costly. Model$\\times$item interaction (up to 36\\%) indicates that models differ primarily in which items they find difficult, not in overall ability. Preliminary validation across a 3B--72B parameter range and a cross-family check (Llama-3.1-70B) confirms stable variance structure across architecture families. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01YXoggRy665GeUbzu57N9Ne`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "e5815607-889d-4181-8936-66ef3b4c165e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDJSjETqUAFdKkLPrMxey4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 35438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1445
      },
      "output_tokens": 69,
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

_source line 39 · 2026-05-23T19:07:20.350Z_

<details><summary>↩ Tool result · `toolu_01YXoggRy665GeUbzu57N9Ne`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	In our analysis of five benchmarks, item selection drives 34--38\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks to decompose these sources, quantify their interactions, and compare the resulting variance structure.
5	
6	Existing studies examine individual variance sources in isolation. \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} documented 50--76\% accuracy swings from prompt formatting; \citet{yuan2025layercast} showed up to 9\% variation from numerical precision; \citet{pezeshkpour2024ordering}, \citet{dodge2020finetuning}, and \citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (judge identity: 43.8\%), but excluded infrastructure facets and cross-benchmark comparison. \citet{madaan2024quantifying} proposed per-factor metrics without crossing factors. IRT approaches \citep{polo2024tinybenchmarks, lalor2019irt, zhou2026irt} optimize item selection but ignore prompt, seed, and ordering facets. \citet{bouthillier2021accounting} established ANOVA-based variance decomposition for ML reproducibility. Three gaps remain: no study has (a) crossed infrastructure and methodology facets in a unified factorial design, (b) compared variance structures across response formats, or (c) translated variance components into design-dependent reproducibility budgets.
7	
8	We address these gaps with a multi-benchmark G-theory study \citep{shavelson1991generalizability, brennan2001generalizability} crossing up to seven facets across eight open-weight 7--9B parameter models and five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), totaling approximately 2.3 million records. D-study projections show that a recommended 3-prompt $\times$ 3-seed design achieves $G \geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\times$ reduction from 552 single-condition items; the full 1,296-condition design further reduces to 55 items as a theoretical ceiling (Figure~\ref{fig:teaser}). Model$\times$item interaction (up to 36\%) indicates that models differ primarily in \emph{which items} they find difficult \citep{pezeshkpour2024ordering, polo2024tinybenchmarks}.
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{fig0_teaser_dstudy}
13	\caption{D-study projections for MMLU (single-model baseline). A recommended 3-prompt $\times$ 3-seed design reduces the budget from 552 to 178 items for $G \geq 0.80$; the full multi-facet design reduces further to 55 items.}
14	\label{fig:teaser}
15	\end{figure}
16	
17	Our contributions:
18	\begin{enumerate}
19	    \item \textbf{Design-dependent reproducibility budgets.} A recommended 3-prompt $\times$ 3-seed design achieves $G \geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\times$ reduction over single-condition designs (552 items); the full 1,296-condition design reduces to 55 items (71,280 evaluations). Under binary scoring, BF16 and FP16 require no separate control ($<$0.1\% interaction). IRT item selection and G-theory protocol optimization compose: IRT-selected 116 items yield $G = 0.457$ single-condition but $G = 0.895$ multi-facet (Table~\ref{tab:dstudy}).
20	
21	    \item \textbf{Format-associated variance patterns (exploratory).} MC benchmarks concentrate 68--72\% of variance in item-related components; FF benchmarks disperse to 31--41\%. This hypothesis-generating observation warrants confirmation with larger benchmark samples.
22	\end{enumerate}
23	We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "a015c660-0b5d-4ccb-976f-2cb052ac996b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nIn our analysis of five benchmarks, item selection drives 34--38\\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\\%). On the free-form reasoning task GSM8K, the structure shifts: model$\\times$prompt interaction alone accounts for approximately 9\\%, while item selection drops to 17\\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \\citep{rodriguez2021leaderboards, dehghani2021benchmark}. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks to decompose these sources, quantify their interactions, and compare the resulting variance structure.\n\nExisting studies examine individual variance sources in isolation. \\citet{sclar2024formatting} and BrittleBench \\citep{brittlebench2026} documented 50--76\\% accuracy swings from prompt formatting; \\citet{yuan2025layercast} showed up to 9\\% variation from numerical precision; \\citet{pezeshkpour2024ordering}, \\citet{dodge2020finetuning}, and \\citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \\citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (judge identity: 43.8\\%), but excluded infrastructure facets and cross-benchmark comparison. \\citet{madaan2024quantifying} proposed per-factor metrics without crossing factors. IRT approaches \\citep{polo2024tinybenchmarks, lalor2019irt, zhou2026irt} optimize item selection but ignore prompt, seed, and ordering facets. \\citet{bouthillier2021accounting} established ANOVA-based variance decomposition for ML reproducibility. Three gaps remain: no study has (a) crossed infrastructure and methodology facets in a unified factorial design, (b) compared variance structures across response formats, or (c) translated variance components into design-dependent reproducibility budgets.\n\nWe address these gaps with a multi-benchmark G-theory study \\citep{shavelson1991generalizability, brennan2001generalizability} crossing up to seven facets across eight open-weight 7--9B parameter models and five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), totaling approximately 2.3 million records. D-study projections show that a recommended 3-prompt $\\times$ 3-seed design achieves $G \\geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\\times$ reduction from 552 single-condition items; the full 1,296-condition design further reduces to 55 items as a theoretical ceiling (Figure~\\ref{fig:teaser}). Model$\\times$item interaction (up to 36\\%) indicates that models differ primarily in \\emph{which items} they find difficult \\citep{pezeshkpour2024ordering, polo2024tinybenchmarks}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig0_teaser_dstudy}\n\\caption{D-study projections for MMLU (single-model baseline). A recommended 3-prompt $\\times$ 3-seed design reduces the budget from 552 to 178 items for $G \\geq 0.80$; the full multi-facet design reduces further to 55 items.}\n\\label{fig:teaser}\n\\end{figure}\n\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Design-dependent reproducibility budgets.} A recommended 3-prompt $\\times$ 3-seed design achieves $G \\geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\\times$ reduction over single-condition designs (552 items); the full 1,296-condition design reduces to 55 items (71,280 evaluations). Under binary scoring, BF16 and FP16 require no separate control ($<$0.1\\% interaction). IRT item selection and G-theory protocol optimization compose: IRT-selected 116 items yield $G = 0.457$ single-condition but $G = 0.895$ multi-facet (Table~\\ref{tab:dstudy}).\n\n    \\item \\textbf{Format-associated variance patterns (exploratory).} MC benchmarks concentrate 68--72\\% of variance in item-related components; FF benchmarks disperse to 31--41\\%. This hypothesis-generating observation warrants confirmation with larger benchmark samples.\n\\end{enumerate}\nWe release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_011D1ykspJvErVUwYviMjgxr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "9e245210-d840-4352-b32a-998b8317d166",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDJSjETqUAFdKkLPrMxey4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 35438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1445
      },
      "output_tokens": 69,
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

_source line 41 · 2026-05-23T19:07:20.699Z_

<details><summary>↩ Tool result · `toolu_011D1ykspJvErVUwYviMjgxr`</summary>

```text
1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	\label{sec:single_model}
7	
8	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
9	
10	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
11	
12	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
13	
14	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
15	
16	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: temperature dominates at 79.7\% of variance, and $G_\text{item}$ collapses to 0.007. This metric-conditional divergence motivates our exclusive use of binary correctness for the remaining analyses.
17	
18	\subsection{Cross-Model Variance}
19	
20	Extending to eight models (BF16 subset, 460,800 records), Table~\ref{tab:cross_model} shows that item difficulty drops from 58.4\% to 37.9\%, while model$\times$item interaction emerges at 30.2\% (up to 36\% across benchmarks, \S\ref{sec:format_conditional}). The model main effect is 3--5\% (MC) and 9--11\% (FF)\footnote{Ranges rounded to nearest integer; exact values are 2.8--5.4\% (MC) and 8.5--10.7\% (FF) per Table~\ref{tab:cross_benchmark}.}, confirming that models differ primarily in \emph{which items} they find difficult rather than in overall ability level (contamination implications in \S\ref{sec:limitations}).
21	
22	\begin{table}[t]
23	\centering
24	\caption{Variance decomposition for the cross-model MMLU design (8 models, BF16, 460,800 records). Components estimated via Henderson Method~I. $G_\text{item} = 0.896$.}
25	\label{tab:cross_model}
26	\small
27	\begin{tabular}{lr}
28	\toprule
29	Component & Var.\% \\
30	\midrule
31	\textbf{item\_id} & \textbf{37.9} \\
32	\underline{model$\times$item} & \underline{30.2} \\
33	residual & 25.0 \\
34	model & 2.8 \\
35	model$\times$prompt & 1.6 \\
36	prompt$\times$item & 0.9 \\
37	temp.$\times$item & 0.6 \\
38	seed$\times$item & 0.5 \\
39	ordering$\times$item & 0.3 \\
40	all others (each) & $<$0.1 \\
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	\subsection{Exploratory: Format-Associated Variance Patterns}
46	\label{sec:format_conditional}
47	
48	We extend to five benchmarks (three MC: MMLU, ARC-Challenge, HellaSwag; two FF: GSM8K, MATH) using exp-002 (8 models $\times$ BF16 $\times$ 2 temperatures $\times$ 6 prompts $\times$ 6 seeds $\times$ 4 orderings $\times$ 200 items). Table~\ref{tab:cross_benchmark} reveals a format-associated pattern: MC benchmarks concentrate item-related variance (item + model$\times$item DIF) at 68--72\%, while FF benchmarks disperse it to 31--41\% ($n = 5$; permutation $p = 0.10$; item-level $d = 1.73$, benchmark-level CI spans zero); we report this as a descriptive observation. This does not extend to item budgets: HellaSwag (MC, 118 items for $G \geq 0.80$) exceeds ARC (98) and MATH (101), showing format alone does not predict evaluation cost (Figure~\ref{fig:cross_benchmark}). The factorial design is not fully symmetric: ordering applies only to MMLU, and prompt templates serve format-specific functions, potentially confounding format comparisons. Per-benchmark details---including HellaSwag and ARC exceptions, FF residual analysis, and difficulty dispersion as a variance predictor---are in Appendix~\ref{app:format_details}. All format-associated findings are conditional on binary scoring (\S\ref{sec:binary}).
49	
50	\begin{table}[t]
51	\centering
52	\caption{Format-associated variance structure across five benchmarks (exp-002, 8 models). Variance components (\%) per benchmark; MC = multiple-choice, FF = free-form. Bold = dominant non-residual component. $^\dagger$For MC, reports prompt$\times$item interaction (prompt main effect $<$1\%); for FF, reports prompt main effect (item-conditional interactions absorbed into residual).}
53	\label{tab:cross_benchmark}
54	\scriptsize
55	\begin{tabular}{l rrr rr}
56	\toprule
57	 & \multicolumn{3}{c}{MC} & \multicolumn{2}{c}{FF} \\
58	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
59	 & MMLU & ARC & Hella. & GSM & MATH \\
60	\midrule
61	\textbf{item} & \textbf{37.9} & \textbf{37.9} & 34.3 & 16.9 & 24.0 \\
62	mod.$\times$item & 30.2 & 33.7 & \textbf{36.0} & 14.6 & 17.3 \\
63	model & 2.8 & 3.1 & 5.4 & 10.7 & 8.5 \\
64	prompt$^\dagger$ & 0.9 & 1.4 & 2.1 & 5.4 & 0.8 \\
65	mod.$\times$prmpt & 1.6 & 8.0 & 0.2 & 8.5 & 1.7 \\
66	residual & 25.0 & 15.4 & 21.4 & 39.9 & 43.9 \\
67	all others & 1.6 & 0.5 & 0.6 & 4.0 & 3.8 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{fig1_cross_benchmark}
75	\caption{Variance decomposition (Henderson Method~I) across five benchmarks and eight models. Multiple-choice benchmarks share an item-dominated structure; HellaSwag is the exception where model$\times$item (36.0\%) exceeds item difficulty (34.3\%). Free-form benchmarks (GSM8K, MATH) distribute variance across item, model, and interaction components with no single dominant source.}
76	\label{fig:cross_benchmark}
77	\end{figure}
78	
79	\subsection{Precision Separability}
80	
81	Under binary scoring, BF16 and FP16 are functionally interchangeable ($<$0.1\% interaction \cite{yuan2025layercast}); under text-exact-match, a precision$\times$temperature interaction emerges at 1.3\%, consistent with \S\ref{sec:single_model}. Precision need not be controlled for binary evaluation at BF16/FP16 \cite{shanmugavelu2024floating}.
82	
83	\subsection{Design-Dependent Reproducibility Budgets}
84	\label{sec:dstudy_budgets}
85	
86	How many items does a given evaluation design need to achieve a target reliability? We translate variance components into item budgets via D-study projections.
87	
88	Table~\ref{tab:dstudy} compares evaluation designs at the $G \geq 0.80$ threshold using single-model (Llama-3.1-8B-Instruct) MMLU variance components. The multi-facet design (1,296 conditions per item) achieves $G = 0.936$ at 200 items and requires only 55 items for $G \geq 0.80$. A single-condition design reaches only $G = 0.592$ at 200 items and requires 552 items---a 10.0$\times$ budget ratio stable across subset sizes (CV = 1.9\%).
89	
90	\begin{table}[t]
91	\centering
92	\caption{D-study reproducibility budgets under different evaluation designs (single-model, MMLU). Total evals = items $\times$ conditions.}
93	\label{tab:dstudy}
94	\scriptsize
95	\begin{tabular}{lcrrrc}
96	\toprule
97	Design & Cond. & $n_{G{\geq}.80}$ & Total & $G_{200}$ & $G_{116}$ \\
98	\midrule
99	Multi-facet & 1{,}296 & \textbf{55} & 71{,}280 & \textbf{.936} & --- \\
100	Single-cond. & 1 & 552 & 552 & .592 & .457 \\
101	IRT+multi & 1{,}296 & --- & 150{,}336 & --- & .895$^\ddagger$ \\
102	\midrule
103	IRT baseline & --- & 116 & 116 & --- & .457$^\dagger$ \\
104	\bottomrule
105	\end{tabular}
106	
107	\vspace{2pt}
108	{\scriptsize $^\dagger$\,PSN-IRT 116 items \cite{zhou2026irt} under single-condition: $G = 0.457$. $^\ddagger$\,Same 116 items under multi-facet: $G = 0.895$.}
109	\end{table}
110	
111	\citet{zhou2026irt}'s IRT-selected 116 items yield $G = 0.457$ under single-condition but $G = 0.895$ under multi-facet conditions, demonstrating that IRT item selection and G-theory protocol optimization are orthogonal and complementary. An internal consistency check using four-model subsets confirms projection stability ($|\Delta G| \leq 0.029$ for MC, $\leq 0.065$ for FF; Table~\ref{tab:forward_pred}).
112	
113	For practitioners, the design choice depends on the evaluation bottleneck: the full 1,296-condition design minimizes items (55 items, 71,280 evaluations per model); the recommended 3-prompt $\times$ 3-seed design balances cost and reliability (178 items, 1,602 evaluations)\footnote{The additional conditions require approximately 8 GPU-minutes per model across five benchmarks on a single accelerator, making the multi-facet overhead negligible relative to its diagnostic value.}; single-condition designs require 552 items at minimal per-item cost. Multi-facet designs suit settings where item construction is expensive (e.g., expert-crafted benchmarks); more items under fewer conditions suit compute-constrained evaluation (adoption gradient in Appendix~\ref{app:intermediate_dstudy}). Cross-model projections show budget ratios of 11--22$\times$ across benchmarks (bootstrap CIs all exceed 10$\times$; Appendix~\ref{app:dstudy_cross}), with multi-facet budgets of 93--128 items (95\% bootstrap CIs spanning 71--162; Table~\ref{tab:dstudy_cross}).
114	
115	\paragraph{Projection assumptions.} Cross-model budgets increase to 93 items because model$\times$item interaction enters relative error variance. Bootstrap CIs (71--162 items) and LOMO analysis (Appendix~\ref{app:robustness}) assess stability; $G_\text{item}$ is stable across benchmarks (0.863--0.896, CV = 1.4\%; Appendix~\ref{app:cross_benchmark_transfer}). All projections assume the 2024--2025 model generation; the 72B extension (\S\ref{sec:scale_validation}) provides preliminary support.
116	
117	\subsection{Preliminary Scale Validation}
118	\label{sec:scale_validation}
119	
120	Within-family analysis (Qwen2.5 3B/7B/72B on MMLU) shows qualitatively invariant variance structure: item difficulty dominates at all three scales (73--83\%, all $G > 0.95$) with consistent facet ranking. The proportional increase at 72B is consistent with the Bernoulli variance ceiling: total variance (0.113) matches $p(1{-}p)$ at grand mean 0.87, compressing all components while item difficulty---the hardest to eliminate---retains the largest share. A crossed 3B$\times$7B$\times$72B design yields model$\times$item = 38.5\% $>$ item = 35.7\%, reflecting expected DIF amplification across a 68--87\% accuracy range ($G_\text{item} = 0.720$; three models insufficient). The out-of-sample 72B provides preliminary within-family evidence that variance structure is stable across a 24$\times$ parameter range within Qwen2.5. A cross-family check with Llama-3.1-70B-Instruct (same protocol, BF16, TP=4) yields item difficulty = 74.5\% ($G_\text{item} = 0.957$), confirming the item-dominated structure across architecturally distinct families: all main effects are zero, and the facet ranking matches Qwen2.5-72B. The 8.8pp item share gap (74.5\% vs.\ 83.3\%) reflects accuracy-dependent Bernoulli ceiling compression, not structural divergence.
121	
122	\paragraph{Robustness checks.} Three MMLU resamples yield CV = 3.1\%; treating models as fixed increases $G$ by 0.077--0.113, confirming conservative budgets (\S\ref{sec:model_facet}; seven additional analyses in Appendix~\ref{app:robustness}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "b0f8957a-23f7-4e2e-a5cc-a59e433008db",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nAll experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.\n\n\\subsection{Single-Model Baseline}\n\\label{sec:single_model}\n\nWe first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.\n\n\\paragraph{Design.} The G-study crosses six facets: 200 items $\\times$ 3 numerical precisions (BF16, FP16, FP32) $\\times$ 6 prompt templates $\\times$ 6 random seeds $\\times$ 3 temperature levels (0.0, 0.3, 0.7) $\\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).\n\n\\paragraph{Results.} Under binary scoring, item difficulty (\\texttt{item\\_id}) accounts for 58.4\\% of total variance, with the residual term contributing 23.1\\%. All main facet effects are negligible ($<$1\\% each): precision 0.9\\%, prompt template, temperature, seed, and ordering each $<$0.5\\%. The interesting structure appears in item-conditional interactions: prompt$\\times$item is the largest at 5.5\\%, followed by seed$\\times$item (4.7\\%), precision$\\times$item (3.3\\%), temperature$\\times$item (2.9\\%), and ordering$\\times$item (0.8\\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.\n\nThe resulting generalizability coefficient is $G_\\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \\geq 0.80$ is achievable with as few as 55 items in this multi-facet design.\n\nFor text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: temperature dominates at 79.7\\% of variance, and $G_\\text{item}$ collapses to 0.007. This metric-conditional divergence motivates our exclusive use of binary correctness for the remaining analyses.\n\n\\subsection{Cross-Model Variance}\n\nExtending to eight models (BF16 subset, 460,800 records), Table~\\ref{tab:cross_model} shows that item difficulty drops from 58.4\\% to 37.9\\%, while model$\\times$item interaction emerges at 30.2\\% (up to 36\\% across benchmarks, \\S\\ref{sec:format_conditional}). The model main effect is 3--5\\% (MC) and 9--11\\% (FF)\\footnote{Ranges rounded to nearest integer; exact values are 2.8--5.4\\% (MC) and 8.5--10.7\\% (FF) per Table~\\ref{tab:cross_benchmark}.}, confirming that models differ primarily in \\emph{which items} they find difficult rather than in overall ability level (contamination implications in \\S\\ref{sec:limitations}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition for the cross-model MMLU design (8 models, BF16, 460,800 records). Components estimated via Henderson Method~I. $G_\\text{item} = 0.896$.}\n\\label{tab:cross_model}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nComponent & Var.\\% \\\\\n\\midrule\n\\textbf{item\\_id} & \\textbf{37.9} \\\\\n\\underline{model$\\times$item} & \\underline{30.2} \\\\\nresidual & 25.0 \\\\\nmodel & 2.8 \\\\\nmodel$\\times$prompt & 1.6 \\\\\nprompt$\\times$item & 0.9 \\\\\ntemp.$\\times$item & 0.6 \\\\\nseed$\\times$item & 0.5 \\\\\nordering$\\times$item & 0.3 \\\\\nall others (each) & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Exploratory: Format-Associated Variance Patterns}\n\\label{sec:format_conditional}\n\nWe extend to five benchmarks (three MC: MMLU, ARC-Challenge, HellaSwag; two FF: GSM8K, MATH) using exp-002 (8 models $\\times$ BF16 $\\times$ 2 temperatures $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 4 orderings $\\times$ 200 items). Table~\\ref{tab:cross_benchmark} reveals a format-associated pattern: MC benchmarks concentrate item-related variance (item + model$\\times$item DIF) at 68--72\\%, while FF benchmarks disperse it to 31--41\\% ($n = 5$; permutation $p = 0.10$; item-level $d = 1.73$, benchmark-level CI spans zero); we report this as a descriptive observation. This does not extend to item budgets: HellaSwag (MC, 118 items for $G \\geq 0.80$) exceeds ARC (98) and MATH (101), showing format alone does not predict evaluation cost (Figure~\\ref{fig:cross_benchmark}). The factorial design is not fully symmetric: ordering applies only to MMLU, and prompt templates serve format-specific functions, potentially confounding format comparisons. Per-benchmark details---including HellaSwag and ARC exceptions, FF residual analysis, and difficulty dispersion as a variance predictor---are in Appendix~\\ref{app:format_details}. All format-associated findings are conditional on binary scoring (\\S\\ref{sec:binary}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Format-associated variance structure across five benchmarks (exp-002, 8 models). Variance components (\\%) per benchmark; MC = multiple-choice, FF = free-form. Bold = dominant non-residual component. $^\\dagger$For MC, reports prompt$\\times$item interaction (prompt main effect $<$1\\%); for FF, reports prompt main effect (item-conditional interactions absorbed into residual).}\n\\label{tab:cross_benchmark}\n\\scriptsize\n\\begin{tabular}{l rrr rr}\n\\toprule\n & \\multicolumn{3}{c}{MC} & \\multicolumn{2}{c}{FF} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n & MMLU & ARC & Hella. & GSM & MATH \\\\\n\\midrule\n\\textbf{item} & \\textbf{37.9} & \\textbf{37.9} & 34.3 & 16.9 & 24.0 \\\\\nmod.$\\times$item & 30.2 & 33.7 & \\textbf{36.0} & 14.6 & 17.3 \\\\\nmodel & 2.8 & 3.1 & 5.4 & 10.7 & 8.5 \\\\\nprompt$^\\dagger$ & 0.9 & 1.4 & 2.1 & 5.4 & 0.8 \\\\\nmod.$\\times$prmpt & 1.6 & 8.0 & 0.2 & 8.5 & 1.7 \\\\\nresidual & 25.0 & 15.4 & 21.4 & 39.9 & 43.9 \\\\\nall others & 1.6 & 0.5 & 0.6 & 4.0 & 3.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_cross_benchmark}\n\\caption{Variance decomposition (Henderson Method~I) across five benchmarks and eight models. Multiple-choice benchmarks share an item-dominated structure; HellaSwag is the exception where model$\\times$item (36.0\\%) exceeds item difficulty (34.3\\%). Free-form benchmarks (GSM8K, MATH) distribute variance across item, model, and interaction components with no single dominant source.}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsection{Precision Separability}\n\nUnder binary scoring, BF16 and FP16 are functionally interchangeable ($<$0.1\\% interaction \\cite{yuan2025layercast}); under text-exact-match, a precision$\\times$temperature interaction emerges at 1.3\\%, consistent with \\S\\ref{sec:single_model}. Precision need not be controlled for binary evaluation at BF16/FP16 \\cite{shanmugavelu2024floating}.\n\n\\subsection{Design-Dependent Reproducibility Budgets}\n\\label{sec:dstudy_budgets}\n\nHow many items does a given evaluation design need to achieve a target reliability? We translate variance components into item budgets via D-study projections.\n\nTable~\\ref{tab:dstudy} compares evaluation designs at the $G \\geq 0.80$ threshold using single-model (Llama-3.1-8B-Instruct) MMLU variance components. The multi-facet design (1,296 conditions per item) achieves $G = 0.936$ at 200 items and requires only 55 items for $G \\geq 0.80$. A single-condition design reaches only $G = 0.592$ at 200 items and requires 552 items---a 10.0$\\times$ budget ratio stable across subset sizes (CV = 1.9\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study reproducibility budgets under different evaluation designs (single-model, MMLU). Total evals = items $\\times$ conditions.}\n\\label{tab:dstudy}\n\\scriptsize\n\\begin{tabular}{lcrrrc}\n\\toprule\nDesign & Cond. & $n_{G{\\geq}.80}$ & Total & $G_{200}$ & $G_{116}$ \\\\\n\\midrule\nMulti-facet & 1{,}296 & \\textbf{55} & 71{,}280 & \\textbf{.936} & --- \\\\\nSingle-cond. & 1 & 552 & 552 & .592 & .457 \\\\\nIRT+multi & 1{,}296 & --- & 150{,}336 & --- & .895$^\\ddagger$ \\\\\n\\midrule\nIRT baseline & --- & 116 & 116 & --- & .457$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$\\,PSN-IRT 116 items \\cite{zhou2026irt} under single-condition: $G = 0.457$. $^\\ddagger$\\,Same 116 items under multi-facet: $G = 0.895$.}\n\\end{table}\n\n\\citet{zhou2026irt}'s IRT-selected 116 items yield $G = 0.457$ under single-condition but $G = 0.895$ under multi-facet conditions, demonstrating that IRT item selection and G-theory protocol optimization are orthogonal and complementary. An internal consistency check using four-model subsets confirms projection stability ($|\\Delta G| \\leq 0.029$ for MC, $\\leq 0.065$ for FF; Table~\\ref{tab:forward_pred}).\n\nFor practitioners, the design choice depends on the evaluation bottleneck: the full 1,296-condition design minimizes items (55 items, 71,280 evaluations per model); the recommended 3-prompt $\\times$ 3-seed design balances cost and reliability (178 items, 1,602 evaluations)\\footnote{The additional conditions require approximately 8 GPU-minutes per model across five benchmarks on a single accelerator, making the multi-facet overhead negligible relative to its diagnostic value.}; single-condition designs require 552 items at minimal per-item cost. Multi-facet designs suit settings where item construction is expensive (e.g., expert-crafted benchmarks); more items under fewer conditions suit compute-constrained evaluation (adoption gradient in Appendix~\\ref{app:intermediate_dstudy}). Cross-model projections show budget ratios of 11--22$\\times$ across benchmarks (bootstrap CIs all exceed 10$\\times$; Appendix~\\ref{app:dstudy_cross}), with multi-facet budgets of 93--128 items (95\\% bootstrap CIs spanning 71--162; Table~\\ref{tab:dstudy_cross}).\n\n\\paragraph{Projection assumptions.} Cross-model budgets increase to 93 items because model$\\times$item interaction enters relative error variance. Bootstrap CIs (71--162 items) and LOMO analysis (Appendix~\\ref{app:robustness}) assess stability; $G_\\text{item}$ is stable across benchmarks (0.863--0.896, CV = 1.4\\%; Appendix~\\ref{app:cross_benchmark_transfer}). All projections assume the 2024--2025 model generation; the 72B extension (\\S\\ref{sec:scale_validation}) provides preliminary support.\n\n\\subsection{Preliminary Scale Validation}\n\\label{sec:scale_validation}\n\nWithin-family analysis (Qwen2.5 3B/7B/72B on MMLU) shows qualitatively invariant variance structure: item difficulty dominates at all three scales (73--83\\%, all $G > 0.95$) with consistent facet ranking. The proportional increase at 72B is consistent with the Bernoulli variance ceiling: total variance (0.113) matches $p(1{-}p)$ at grand mean 0.87, compressing all components while item difficulty---the hardest to eliminate---retains the largest share. A crossed 3B$\\times$7B$\\times$72B design yields model$\\times$item = 38.5\\% $>$ item = 35.7\\%, reflecting expected DIF amplification across a 68--87\\% accuracy range ($G_\\text{item} = 0.720$; three models insufficient). The out-of-sample 72B provides preliminary within-family evidence that variance structure is stable across a 24$\\times$ parameter range within Qwen2.5. A cross-family check with Llama-3.1-70B-Instruct (same protocol, BF16, TP=4) yields item difficulty = 74.5\\% ($G_\\text{item} = 0.957$), confirming the item-dominated structure across architecturally distinct families: all main effects are zero, and the facet ranking matches Qwen2.5-72B. The 8.8pp item share gap (74.5\\% vs.\\ 83.3\\%) reflects accuracy-dependent Bernoulli ceiling compression, not structural divergence.\n\n\\paragraph{Robustness checks.} Three MMLU resamples yield CV = 3.1\\%; treating models as fixed increases $G$ by 0.077--0.113, confirming conservative budgets (\\S\\ref{sec:model_facet}; seven additional analyses in Appendix~\\ref{app:robustness}).",
      "numLines": 122,
      "startLine": 1,
      "totalLines": 122
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Good. The experiments.tex has the Llama-70B content. Now let me read the other paper files - method, related_work, conclusion, limitations, appendix, references.bib, and the bbl file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "b09f9696-a3ff-434b-b916-ffc116586bbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 43_

论文包含 Llama-70B 内容。继续读取其余文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "f11e8b5c-22c9-47a8-a126-e0d07cf54286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_014ALpByqzH5tmmGUvZwNHMT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "375e0c84-2c24-42a6-b5cc-6fa7b31f2421",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 45 · 2026-05-23T19:07:28.255Z_

<details><summary>↩ Tool result · `toolu_014ALpByqzH5tmmGUvZwNHMT`</summary>

```text
1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel} = \sum_i \sigma^2_{p \times f_i} / n_{f_i} + \sigma^2_\text{residual} / \prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. A D-study projects reliability for a test averaging over $n_p$ items via $G(n_p) = n_p \sigma^2_p / (n_p \sigma^2_p + \sigma^2_\text{rel})$, enabling independent verification of all budget projections in Table~\ref{tab:dstudy}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of evaluation designs \emph{before} data collection \cite{shavelson1989gtheory}. We define \emph{item-related variance} as the sum of the item main effect ($\sigma^2_p$) and the model$\times$item interaction ($\sigma^2_{pM}$). The latter captures differential item functioning (DIF): items whose difficulty ranking changes across models \cite[Ch.~4]{brennan2001generalizability}. Because DIF is operationally an item-level property---it reflects model-specific item difficulty profiles rather than a global model ability shift---aggregating $\sigma^2_p + \sigma^2_{pM}$ provides a unified measure of item-driven variance. We note a semantic difference from educational measurement: person$\times$item DIF reflects unidirectional person responses to items, whereas model$\times$item DIF in LLM evaluation simultaneously reflects architecture-specific capability profiles---a dual interpretation. Bundling $\sigma^2_p + \sigma^2_{pM}$ has psychometric justification \cite[Ch.~4]{brennan2001generalizability}, and we report unbundled components throughout to ensure transparency.
17	
18	In ML terms, a G-study is a multi-way ANOVA where each facet is a design variable and variance components quantify each variable's contribution; a D-study projects the number of conditions per facet needed for a target reliability $G$, analogous to a signal-to-noise ratio where signal is item difficulty variance and noise is everything that changes across evaluation conditions.
19	
20	Throughout this paper, we use the following notation: $p$ = item, $M$ = model, $\pi$ = numerical precision, $\delta$ = prompt template, $s$ = random seed, $\tau$ = sampling temperature, $o$ = answer ordering, and $\sigma^2_x$ = variance component for source $x$.
21	
22	\subsection{Experimental Design: MMLU}
23	\label{sec:exp001}
24	
25	We design a fully crossed factorial experiment (exp-001) that simultaneously varies seven facets of LLM evaluation on MMLU. Table~\ref{tab:design_matrix} summarizes the complete design matrix, and Figure~\ref{fig:design_diagram} illustrates the crossing structure.
26	
27	\paragraph{Facets.} Items ($p$): 200 MMLU questions selected via purposive stratified sampling across 10 of MMLU's 57 subjects (20 per subject, deterministic selection with arbitrarily chosen seed 42). The 10 subjects span four disciplinary domains---STEM: abstract algebra, college physics, high school mathematics, computer security; humanities: world religions, philosophy; social sciences: US foreign policy, international law; professional: professional medicine, clinical knowledge---ensuring that variance estimates are not dominated by a single knowledge domain. Resampling stability (CV = 3.1\%) was evaluated within these 10 subjects; cross-subject generalization remains untested. Models ($M$): eight open-weight 7--9B parameter instruction-tuned models spanning eight architecture families---DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct, OLMo-2-7B, Qwen3-8B, and Yi-1.5-9B (full identifiers in Appendix~\ref{app:models})---treated as a quasi-random facet (\S\ref{sec:model_facet}). Numerical precision ($\pi$): BF16, FP16, and FP32, all evaluated with \texttt{enforce\_eager=True} for fair comparison across precision levels. Prompt template ($\delta$): six surface perturbations of the evaluation instruction \cite{sclar2024formatting}, varying option layout (lettered vs.\ numbered), instruction wording (direct vs.\ contextual), and answer prompt cue for MC benchmarks; for FF benchmarks, templates vary chain-of-thought elicitation strategy (full template text in Appendix~\ref{app:models}). Random seed ($s$): six fixed values (42, 123, 456, 789, 1024, 2048). Sampling temperature ($\tau$): three levels (0.0, 0.3, 0.7) spanning deterministic to moderately stochastic decoding. Answer ordering ($o$): four permutations of few-shot demonstration examples (for MMLU; structurally inert for other benchmarks, see \S\ref{sec:exp002}) \cite{pezeshkpour2024ordering}.
28	
29	\paragraph{Sample sizes.} The cross-model BF16 balanced subset yields 460,800 records (8 models $\times$ 200 items $\times$ 6 prompts $\times$ 6 seeds $\times$ 2 temperatures $\times$ 4 orderings). A single-model analysis (Llama) spans all three precisions, yielding 259,200 binary observations across 1,296 fully balanced conditions. The BF16 subset serves as the primary cross-model sample because BF16 is the standard inference precision for these architectures.
30	
31	\begin{table}[t]
32	\centering
33	\caption{Fully crossed G-theory design. Exp-001 evaluates MMLU across all facet levels; exp-002 extends to five benchmarks with reduced crossing. $^\dagger$BF16 balanced subset (2 temperatures: 0.0, 0.7) for cross-model analysis; the full single-model design uses all 3 levels.}
34	\label{tab:design_matrix}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{llrr}
38	\toprule
39	Facet & Levels & exp-001 & exp-002 \\
40	\midrule
41	Item ($p$) & Stratified sample & 200 & 200$\times$5 \\
42	Model ($M$) & 8 architecture families & 8 & 8 \\
43	Precision ($\pi$) & BF16 / FP16 / FP32 & 3 & 1 \\
44	Prompt ($\delta$) & Paraphrases & 6 & 6 \\
45	Seed ($s$) & Fixed set & 6 & 6 \\
46	Temperature ($\tau$) & 0.0 / 0.3 / 0.7 & 3 & 2 \\
47	Ordering ($o$) & Demo permutations & 4 & 4 \\
48	\midrule
49	\multicolumn{2}{l}{Total records} & 460,800$^\dagger$ & 2,304,000 \\
50	\bottomrule
51	\end{tabular}}
52	\end{table}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{fig2_design_diagram}
57	\caption{Fully crossed G-theory design for LLM evaluation. Each observation is a binary correctness score determined by the crossing of seven facets: item ($p$), model ($M$), precision ($\pi$), prompt ($\delta$), seed ($s$), temperature ($\tau$), and ordering ($o$).}
58	\label{fig:design_diagram}
59	\end{figure}
60	
61	\subsection{Cross-Benchmark Extension}
62	\label{sec:exp002}
63	
64	To test whether the variance structure observed on MMLU generalizes across evaluation formats, exp-002 extends the design to five benchmarks: MMLU, ARC-Challenge, and HellaSwag (multiple-choice), and GSM8K and MATH (free-form generation). The design crosses 8 models $\times$ BF16 $\times$ 2 temperatures (0.0, 0.7) $\times$ 6 prompts $\times$ 6 seeds $\times$ 4 orderings $\times$ 200 items per benchmark, totaling 2,304,000 records. This reduced crossing fixes precision at BF16 and uses two temperature levels to concentrate statistical power on format-associated differences. The ordering facet operates only on MMLU, where it selects among four permutations of the few-shot demonstration examples. For all other benchmarks, the prompt construction does not use the ordering parameter; ordering is structurally inert ($\sigma^2_{\text{ordering}} = 0$ by construction) and is retained solely for design balance. The two temperature levels bracket the most common evaluation configurations: deterministic ($\tau = 0.0$) and a moderate stochastic setting ($\tau = 0.7$) representative of practical deployment. A subset analysis confirms that this reduced crossing preserves the variance structure of the full design ($\Delta G = 0.0008$; Appendix~\ref{app:robustness}).
65	
66	
67	\subsection{Evaluation Protocol}
68	\label{sec:protocol}
69	
70	All evaluations use generation-based scoring (free-text response with answer extraction) rather than log-likelihood ranking, following \citet{hua2025flaw}. Binary correctness (1/0) is the primary metric; text-exact-match is secondary. Inference uses vLLM~0.9.2 without batch-invariant kernels, preserving CUDA-level nondeterminism as a measurable variance source \cite{messina2026background, thinkingmachines2025batch}. Few-shot protocols: 5-shot MMLU/ARC, 4-shot MATH, 8-shot GSM8K, 10-shot HellaSwag.
71	
72	\subsection{Binary Data Assumptions}
73	\label{sec:binary}
74	
75	Standard G-theory assumes continuous, approximately normal outcome data \cite{shavelson1991generalizability}. Our binary correctness scores (0/1) violate this assumption. We establish robustness through simulation and estimator properties, with two additional analyses (GLMM complement, accuracy-range stability) in Appendix~\ref{app:robustness}.
76	
77	Henderson Method~I produces unbiased estimates for balanced designs regardless of outcome distribution \cite[Ch.~12]{brennan2001generalizability}, and REML estimates differ by $<$0.5pp on all components. A probit simulation, GLMM complement ($\rho = 1.0$), and accuracy-range analysis all confirm robustness (Appendix~\ref{app:robustness}).
78	
79	All findings in this paper are conditioned on binary correctness scoring. This measurement resolution collapses continuous generation quality into a pass/fail outcome, which may amplify item-related variance by reducing within-item response variability and mask finer-grained variance sources (e.g., partial credit, reasoning quality) that would emerge under richer scoring rubrics. The text-exact-match comparison in \S\ref{sec:single_model} ($G = 0.007$ vs.\ $0.936$) illustrates how the scoring metric can fundamentally reshape variance structure. A partial-credit analysis on GSM8K (8 models, step-level scoring) confirms this conditionality: $G_\text{item}$ drops from 0.86 to 0.77, with all eight models showing $G_\text{partial} < G_\text{binary}$ (mean $\Delta G = -0.135$; Appendix~\ref{app:robustness}), providing evidence that D-study budgets have limited transferability to finer-grained scoring rubrics.
80	
81	\subsection{Model Facet Specification}
82	
83	Our target universe comprises open-weight, instruction-tuned models in the 7--9B parameter range (eight architecture families); results may not generalize to API-based, base, or $>$9B models. Our eight purposively selected models are treated as a quasi-random facet \cite{meredith1993measurement, putnick2016measurement}. We report $G$ under random-model assumptions, the more conservative specification: across five benchmarks, treating models as fixed yields $G_\text{fixed}$ of 0.951--0.990 (mean 0.975) versus $G_\text{random}$ of 0.863--0.896 (mean 0.882), a consistent increase of 0.077--0.113 (mean 0.093), because model$\times$item interaction (30--36\%) enters the relative error variance under random assumptions. Consequently, our D-study budgets are upper bounds---practitioners will not under-sample regardless of facet classification. The variance decomposition itself (Tables~\ref{tab:cross_model}--\ref{tab:cross_benchmark}) is invariant to this choice. Leave-one-model-out analysis preserves component rankings across all five benchmarks, and Cohen's $\kappa$ pairwise agreement (mean $\kappa = 0.33$--$0.46$) confirms genuine differential item functioning (Appendix~\ref{app:robustness}). Four-model subset consistency checks match the observed eight-model $G$ within mean $|\Delta G| = 0.035$ across all five benchmarks (\S\ref{sec:dstudy_budgets}).
84	
85	For reference, $G_\text{model}$ (treating models as the object of measurement) under the recommended 3-prompt $\times$ 3-seed design with 200 items averages 0.79 across five benchmarks (range: 0.52 on ARC to 0.93 on HellaSwag). Model ranking reliability depends primarily on model$\times$prompt interaction---ARC (8.0\%) and GSM8K (8.5\%) show lower $G_\text{model}$ because prompt sensitivity reduces model discriminability. $G_\text{item}$ remains the primary metric because item reliability is the direct optimization target for evaluation design; model reliability is a downstream consequence that improves with item count.
86	\label{sec:model_facet}
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "bfd21413-9824-45cf-a261-89759ab235c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex",
      "content": "\\section{Method and Experimental Design}\n\\label{sec:method}\n\n\\subsection{Generalizability Theory}\n\\label{sec:gtheory}\n\nGeneralizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \\cite{shavelson1991generalizability, brennan2001generalizability}. The \\emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.\n\nA \\emph{G-study} decomposes total observed variance into components $\\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \\cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \\cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \\cite{li2023bootstrap}.\n\nA \\emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:\n\\begin{equation}\nG_\\text{item} = \\frac{\\sigma^2_p}{\\sigma^2_p + \\sigma^2_\\text{rel}}\n\\label{eq:gcoeff}\n\\end{equation}\nwhere $\\sigma^2_\\text{rel} = \\sum_i \\sigma^2_{p \\times f_i} / n_{f_i} + \\sigma^2_\\text{residual} / \\prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \\cite[Ch.~4]{brennan2001generalizability}. A D-study projects reliability for a test averaging over $n_p$ items via $G(n_p) = n_p \\sigma^2_p / (n_p \\sigma^2_p + \\sigma^2_\\text{rel})$, enabling independent verification of all budget projections in Table~\\ref{tab:dstudy}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of evaluation designs \\emph{before} data collection \\cite{shavelson1989gtheory}. We define \\emph{item-related variance} as the sum of the item main effect ($\\sigma^2_p$) and the model$\\times$item interaction ($\\sigma^2_{pM}$). The latter captures differential item functioning (DIF): items whose difficulty ranking changes across models \\cite[Ch.~4]{brennan2001generalizability}. Because DIF is operationally an item-level property---it reflects model-specific item difficulty profiles rather than a global model ability shift---aggregating $\\sigma^2_p + \\sigma^2_{pM}$ provides a unified measure of item-driven variance. We note a semantic difference from educational measurement: person$\\times$item DIF reflects unidirectional person responses to items, whereas model$\\times$item DIF in LLM evaluation simultaneously reflects architecture-specific capability profiles---a dual interpretation. Bundling $\\sigma^2_p + \\sigma^2_{pM}$ has psychometric justification \\cite[Ch.~4]{brennan2001generalizability}, and we report unbundled components throughout to ensure transparency.\n\nIn ML terms, a G-study is a multi-way ANOVA where each facet is a design variable and variance components quantify each variable's contribution; a D-study projects the number of conditions per facet needed for a target reliability $G$, analogous to a signal-to-noise ratio where signal is item difficulty variance and noise is everything that changes across evaluation conditions.\n\nThroughout this paper, we use the following notation: $p$ = item, $M$ = model, $\\pi$ = numerical precision, $\\delta$ = prompt template, $s$ = random seed, $\\tau$ = sampling temperature, $o$ = answer ordering, and $\\sigma^2_x$ = variance component for source $x$.\n\n\\subsection{Experimental Design: MMLU}\n\\label{sec:exp001}\n\nWe design a fully crossed factorial experiment (exp-001) that simultaneously varies seven facets of LLM evaluation on MMLU. Table~\\ref{tab:design_matrix} summarizes the complete design matrix, and Figure~\\ref{fig:design_diagram} illustrates the crossing structure.\n\n\\paragraph{Facets.} Items ($p$): 200 MMLU questions selected via purposive stratified sampling across 10 of MMLU's 57 subjects (20 per subject, deterministic selection with arbitrarily chosen seed 42). The 10 subjects span four disciplinary domains---STEM: abstract algebra, college physics, high school mathematics, computer security; humanities: world religions, philosophy; social sciences: US foreign policy, international law; professional: professional medicine, clinical knowledge---ensuring that variance estimates are not dominated by a single knowledge domain. Resampling stability (CV = 3.1\\%) was evaluated within these 10 subjects; cross-subject generalization remains untested. Models ($M$): eight open-weight 7--9B parameter instruction-tuned models spanning eight architecture families---DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct, OLMo-2-7B, Qwen3-8B, and Yi-1.5-9B (full identifiers in Appendix~\\ref{app:models})---treated as a quasi-random facet (\\S\\ref{sec:model_facet}). Numerical precision ($\\pi$): BF16, FP16, and FP32, all evaluated with \\texttt{enforce\\_eager=True} for fair comparison across precision levels. Prompt template ($\\delta$): six surface perturbations of the evaluation instruction \\cite{sclar2024formatting}, varying option layout (lettered vs.\\ numbered), instruction wording (direct vs.\\ contextual), and answer prompt cue for MC benchmarks; for FF benchmarks, templates vary chain-of-thought elicitation strategy (full template text in Appendix~\\ref{app:models}). Random seed ($s$): six fixed values (42, 123, 456, 789, 1024, 2048). Sampling temperature ($\\tau$): three levels (0.0, 0.3, 0.7) spanning deterministic to moderately stochastic decoding. Answer ordering ($o$): four permutations of few-shot demonstration examples (for MMLU; structurally inert for other benchmarks, see \\S\\ref{sec:exp002}) \\cite{pezeshkpour2024ordering}.\n\n\\paragraph{Sample sizes.} The cross-model BF16 balanced subset yields 460,800 records (8 models $\\times$ 200 items $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings). A single-model analysis (Llama) spans all three precisions, yielding 259,200 binary observations across 1,296 fully balanced conditions. The BF16 subset serves as the primary cross-model sample because BF16 is the standard inference precision for these architectures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fully crossed G-theory design. Exp-001 evaluates MMLU across all facet levels; exp-002 extends to five benchmarks with reduced crossing. $^\\dagger$BF16 balanced subset (2 temperatures: 0.0, 0.7) for cross-model analysis; the full single-model design uses all 3 levels.}\n\\label{tab:design_matrix}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\nFacet & Levels & exp-001 & exp-002 \\\\\n\\midrule\nItem ($p$) & Stratified sample & 200 & 200$\\times$5 \\\\\nModel ($M$) & 8 architecture families & 8 & 8 \\\\\nPrecision ($\\pi$) & BF16 / FP16 / FP32 & 3 & 1 \\\\\nPrompt ($\\delta$) & Paraphrases & 6 & 6 \\\\\nSeed ($s$) & Fixed set & 6 & 6 \\\\\nTemperature ($\\tau$) & 0.0 / 0.3 / 0.7 & 3 & 2 \\\\\nOrdering ($o$) & Demo permutations & 4 & 4 \\\\\n\\midrule\n\\multicolumn{2}{l}{Total records} & 460,800$^\\dagger$ & 2,304,000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_design_diagram}\n\\caption{Fully crossed G-theory design for LLM evaluation. Each observation is a binary correctness score determined by the crossing of seven facets: item ($p$), model ($M$), precision ($\\pi$), prompt ($\\delta$), seed ($s$), temperature ($\\tau$), and ordering ($o$).}\n\\label{fig:design_diagram}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Extension}\n\\label{sec:exp002}\n\nTo test whether the variance structure observed on MMLU generalizes across evaluation formats, exp-002 extends the design to five benchmarks: MMLU, ARC-Challenge, and HellaSwag (multiple-choice), and GSM8K and MATH (free-form generation). The design crosses 8 models $\\times$ BF16 $\\times$ 2 temperatures (0.0, 0.7) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 4 orderings $\\times$ 200 items per benchmark, totaling 2,304,000 records. This reduced crossing fixes precision at BF16 and uses two temperature levels to concentrate statistical power on format-associated differences. The ordering facet operates only on MMLU, where it selects among four permutations of the few-shot demonstration examples. For all other benchmarks, the prompt construction does not use the ordering parameter; ordering is structurally inert ($\\sigma^2_{\\text{ordering}} = 0$ by construction) and is retained solely for design balance. The two temperature levels bracket the most common evaluation configurations: deterministic ($\\tau = 0.0$) and a moderate stochastic setting ($\\tau = 0.7$) representative of practical deployment. A subset analysis confirms that this reduced crossing preserves the variance structure of the full design ($\\Delta G = 0.0008$; Appendix~\\ref{app:robustness}).\n\n\n\\subsection{Evaluation Protocol}\n\\label{sec:protocol}\n\nAll evaluations use generation-based scoring (free-text response with answer extraction) rather than log-likelihood ranking, following \\citet{hua2025flaw}. Binary correctness (1/0) is the primary metric; text-exact-match is secondary. Inference uses vLLM~0.9.2 without batch-invariant kernels, preserving CUDA-level nondeterminism as a measurable variance source \\cite{messina2026background, thinkingmachines2025batch}. Few-shot protocols: 5-shot MMLU/ARC, 4-shot MATH, 8-shot GSM8K, 10-shot HellaSwag.\n\n\\subsection{Binary Data Assumptions}\n\\label{sec:binary}\n\nStandard G-theory assumes continuous, approximately normal outcome data \\cite{shavelson1991generalizability}. Our binary correctness scores (0/1) violate this assumption. We establish robustness through simulation and estimator properties, with two additional analyses (GLMM complement, accuracy-range stability) in Appendix~\\ref{app:robustness}.\n\nHenderson Method~I produces unbiased estimates for balanced designs regardless of outcome distribution \\cite[Ch.~12]{brennan2001generalizability}, and REML estimates differ by $<$0.5pp on all components. A probit simulation, GLMM complement ($\\rho = 1.0$), and accuracy-range analysis all confirm robustness (Appendix~\\ref{app:robustness}).\n\nAll findings in this paper are conditioned on binary correctness scoring. This measurement resolution collapses continuous generation quality into a pass/fail outcome, which may amplify item-related variance by reducing within-item response variability and mask finer-grained variance sources (e.g., partial credit, reasoning quality) that would emerge under richer scoring rubrics. The text-exact-match comparison in \\S\\ref{sec:single_model} ($G = 0.007$ vs.\\ $0.936$) illustrates how the scoring metric can fundamentally reshape variance structure. A partial-credit analysis on GSM8K (8 models, step-level scoring) confirms this conditionality: $G_\\text{item}$ drops from 0.86 to 0.77, with all eight models showing $G_\\text{partial} < G_\\text{binary}$ (mean $\\Delta G = -0.135$; Appendix~\\ref{app:robustness}), providing evidence that D-study budgets have limited transferability to finer-grained scoring rubrics.\n\n\\subsection{Model Facet Specification}\n\nOur target universe comprises open-weight, instruction-tuned models in the 7--9B parameter range (eight architecture families); results may not generalize to API-based, base, or $>$9B models. Our eight purposively selected models are treated as a quasi-random facet \\cite{meredith1993measurement, putnick2016measurement}. We report $G$ under random-model assumptions, the more conservative specification: across five benchmarks, treating models as fixed yields $G_\\text{fixed}$ of 0.951--0.990 (mean 0.975) versus $G_\\text{random}$ of 0.863--0.896 (mean 0.882), a consistent increase of 0.077--0.113 (mean 0.093), because model$\\times$item interaction (30--36\\%) enters the relative error variance under random assumptions. Consequently, our D-study budgets are upper bounds---practitioners will not under-sample regardless of facet classification. The variance decomposition itself (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_benchmark}) is invariant to this choice. Leave-one-model-out analysis preserves component rankings across all five benchmarks, and Cohen's $\\kappa$ pairwise agreement (mean $\\kappa = 0.33$--$0.46$) confirms genuine differential item functioning (Appendix~\\ref{app:robustness}). Four-model subset consistency checks match the observed eight-model $G$ within mean $|\\Delta G| = 0.035$ across all five benchmarks (\\S\\ref{sec:dstudy_budgets}).\n\nFor reference, $G_\\text{model}$ (treating models as the object of measurement) under the recommended 3-prompt $\\times$ 3-seed design with 200 items averages 0.79 across five benchmarks (range: 0.52 on ARC to 0.93 on HellaSwag). Model ranking reliability depends primarily on model$\\times$prompt interaction---ARC (8.0\\%) and GSM8K (8.5\\%) show lower $G_\\text{model}$ because prompt sensitivity reduces model discriminability. $G_\\text{item}$ remains the primary metric because item reliability is the direct optimization target for evaluation design; model reliability is a downstream consequence that improves with item count.\n\\label{sec:model_facet}\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01RA6vyNGCwMWoeWmDgK4ndN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "223650c9-b35b-4577-aed6-d7009efaa038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 47 · 2026-05-23T19:07:28.612Z_

<details><summary>↩ Tool result · `toolu_01RA6vyNGCwMWoeWmDgK4ndN`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Subsequent studies applied similar decomposition to specific evaluation facets \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark (judge identity: 43.8\%; see Positioning below for detailed comparison). \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Holistic evaluation frameworks \citep{liang2023helm, kiela2021dynabench} standardize multi-scenario comparison but do not decompose variance sources. \citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \citet{burnell2023rethink} called for rethinking evaluation reporting standards; \citet{saxon2024metrology} advocated model metrology as a framework for rigorous benchmark design. Recently, G-theory has been applied to LLM-based writing assessment \citep{song2025gtheory} and annotation reliability \citep{varannot2026gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across five benchmarks, enabling direct comparison of variance structures across evaluation formats.
6	
7	\paragraph{Infrastructure and Prompt Variance.}
8	A parallel line of work examines individual variance sources in isolation. \citet{yuan2025layercast} documented up to 9\% accuracy variation from numerical precision; \citet{messina2026background} and \citet{thinkingmachines2025batch} formalized and mitigated CUDA nondeterminism from floating-point non-associativity. On the methodology side, \citet{mizrahi2024state} advocated multi-prompt evaluation based on large-scale sensitivity analysis; \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} found 50--76\% accuracy swings from prompt formatting; \citet{hua2025flaw} showed that much of this sensitivity is an artifact of log-likelihood scoring (our generation-based protocol controls for this). \citet{pezeshkpour2024ordering} and \citet{alzahrani2024benchmarks} documented ordering and benchmark sensitivity; \citet{bui2025seeds} and \citet{biderman2024lessons} documented seed and training sensitivity respectively. Each isolates one factor, precluding interaction estimation. Standardized evaluation frameworks such as lm-evaluation-harness \citep{gao2024lmeval} reduce implementation variance but do not control prompt, seed, or ordering facets.
9	
10	\paragraph{IRT and Efficient Benchmarking.}
11	Item Response Theory (IRT) offers a complementary perspective on evaluation design by modeling item difficulty and discrimination parameters. \citet{lalor2019irt} introduced IRT-based item analysis for NLP benchmarks, and \citet{rodriguez2021leaderboards} showed that IRT reveals hidden properties of evaluation items that raw accuracy scores obscure. Building on this foundation, \citet{polo2024tinybenchmarks} developed tinyBenchmarks, using IRT-based subsampling to reduce evaluation cost while preserving ranking accuracy, and \citet{zhou2026irt} recommended a 116-item subset via PSN-IRT for efficient MMLU evaluation. \citet{perlitz2023efficient} and \citet{kipnis2025metabench} explored related strategies for benchmark compression; \citet{li2025atlas} extended IRT to adaptive testing. Complementary benchmark revision efforts address item quality directly: MMLU-Redux \citep{gema2025mmlu} identified annotation errors in MMLU, while MMLU-Pro \citep{wang2024mmlupro} extended it with harder items and expanded option sets. These approaches optimize item selection or quality but do not model variance from prompt, seed, or ordering facets. IRT-selected items evaluated under a single methodological condition can therefore systematically underestimate the number of items required for reliable measurement across diverse evaluation settings.
12	
13	\paragraph{Psychometrics Foundations.}
14	G-theory \cite{shavelson1991generalizability, brennan2001generalizability, cardinet2010applying} provides the canonical framework for multi-facet reliability analysis; \citet{webb2006reliability} detail the random versus fixed facet distinctions central to our model specification. Extensions to binary data include \citet{mushquash2006gtheory} and logistic-link generalized G-theory \cite{jiang2018bayesian, tuerlinckx2006glmm}. We operationalize differential item functioning---established as a formal framework by \citet{holland1993dif} and operationalized via statistical detection procedures by \citet{clauser1998dif}---as model$\times$item interaction. Recent psychometric perspectives on LLM evaluation address construct validity \cite{kearns2026construct, bean2025measuring, freiesleben2026construct} and measurement properties \cite{ye2025psychometrics}; \citet{zhu2026benchmark} propose a benchmark health index for systematic meta-evaluation.
15	
16	\paragraph{Positioning.}
17	Closest to our work, \citet{messing2026hidden} applied G-theory to LLM evaluation through their TEE framework, decomposing five methodology facets on a single benchmark (judge identity: 43.8\%). We extend this in three directions: (i) we fix the judge to the model itself, replacing judge identity with infrastructure facets and additional methodology facets (seed, ordering); (ii) we cross facets across five benchmarks, enabling cross-format comparison; and (iii) we translate variance components into reproducibility budgets via D-study projections. The two studies are complementary: TEE characterizes judge selection, while we characterize item-and-protocol selection. Relative to IRT approaches \citep{polo2024tinybenchmarks, zhou2026irt}, G-theory optimizes an orthogonal dimension: conditions needed for target reliability rather than item discrimination.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "14d0fa05-cec5-424b-b5a2-958518bdb720",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Variance Decomposition in ML/NLP Evaluation.}\nFactorial decomposition of evaluation variance has roots in the ML reproducibility literature. \\citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Subsequent studies applied similar decomposition to specific evaluation facets \\citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \\citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark (judge identity: 43.8\\%; see Positioning below for detailed comparison). \\citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Holistic evaluation frameworks \\citep{liang2023helm, kiela2021dynabench} standardize multi-scenario comparison but do not decompose variance sources. \\citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \\citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \\citet{burnell2023rethink} called for rethinking evaluation reporting standards; \\citet{saxon2024metrology} advocated model metrology as a framework for rigorous benchmark design. Recently, G-theory has been applied to LLM-based writing assessment \\citep{song2025gtheory} and annotation reliability \\citep{varannot2026gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \\citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across five benchmarks, enabling direct comparison of variance structures across evaluation formats.\n\n\\paragraph{Infrastructure and Prompt Variance.}\nA parallel line of work examines individual variance sources in isolation. \\citet{yuan2025layercast} documented up to 9\\% accuracy variation from numerical precision; \\citet{messina2026background} and \\citet{thinkingmachines2025batch} formalized and mitigated CUDA nondeterminism from floating-point non-associativity. On the methodology side, \\citet{mizrahi2024state} advocated multi-prompt evaluation based on large-scale sensitivity analysis; \\citet{sclar2024formatting} and BrittleBench \\citep{brittlebench2026} found 50--76\\% accuracy swings from prompt formatting; \\citet{hua2025flaw} showed that much of this sensitivity is an artifact of log-likelihood scoring (our generation-based protocol controls for this). \\citet{pezeshkpour2024ordering} and \\citet{alzahrani2024benchmarks} documented ordering and benchmark sensitivity; \\citet{bui2025seeds} and \\citet{biderman2024lessons} documented seed and training sensitivity respectively. Each isolates one factor, precluding interaction estimation. Standardized evaluation frameworks such as lm-evaluation-harness \\citep{gao2024lmeval} reduce implementation variance but do not control prompt, seed, or ordering facets.\n\n\\paragraph{IRT and Efficient Benchmarking.}\nItem Response Theory (IRT) offers a complementary perspective on evaluation design by modeling item difficulty and discrimination parameters. \\citet{lalor2019irt} introduced IRT-based item analysis for NLP benchmarks, and \\citet{rodriguez2021leaderboards} showed that IRT reveals hidden properties of evaluation items that raw accuracy scores obscure. Building on this foundation, \\citet{polo2024tinybenchmarks} developed tinyBenchmarks, using IRT-based subsampling to reduce evaluation cost while preserving ranking accuracy, and \\citet{zhou2026irt} recommended a 116-item subset via PSN-IRT for efficient MMLU evaluation. \\citet{perlitz2023efficient} and \\citet{kipnis2025metabench} explored related strategies for benchmark compression; \\citet{li2025atlas} extended IRT to adaptive testing. Complementary benchmark revision efforts address item quality directly: MMLU-Redux \\citep{gema2025mmlu} identified annotation errors in MMLU, while MMLU-Pro \\citep{wang2024mmlupro} extended it with harder items and expanded option sets. These approaches optimize item selection or quality but do not model variance from prompt, seed, or ordering facets. IRT-selected items evaluated under a single methodological condition can therefore systematically underestimate the number of items required for reliable measurement across diverse evaluation settings.\n\n\\paragraph{Psychometrics Foundations.}\nG-theory \\cite{shavelson1991generalizability, brennan2001generalizability, cardinet2010applying} provides the canonical framework for multi-facet reliability analysis; \\citet{webb2006reliability} detail the random versus fixed facet distinctions central to our model specification. Extensions to binary data include \\citet{mushquash2006gtheory} and logistic-link generalized G-theory \\cite{jiang2018bayesian, tuerlinckx2006glmm}. We operationalize differential item functioning---established as a formal framework by \\citet{holland1993dif} and operationalized via statistical detection procedures by \\citet{clauser1998dif}---as model$\\times$item interaction. Recent psychometric perspectives on LLM evaluation address construct validity \\cite{kearns2026construct, bean2025measuring, freiesleben2026construct} and measurement properties \\cite{ye2025psychometrics}; \\citet{zhu2026benchmark} propose a benchmark health index for systematic meta-evaluation.\n\n\\paragraph{Positioning.}\nClosest to our work, \\citet{messing2026hidden} applied G-theory to LLM evaluation through their TEE framework, decomposing five methodology facets on a single benchmark (judge identity: 43.8\\%). We extend this in three directions: (i) we fix the judge to the model itself, replacing judge identity with infrastructure facets and additional methodology facets (seed, ordering); (ii) we cross facets across five benchmarks, enabling cross-format comparison; and (iii) we translate variance components into reproducibility budgets via D-study projections. The two studies are complementary: TEE characterizes judge selection, while we characterize item-and-protocol selection. Relative to IRT approaches \\citep{polo2024tinybenchmarks, zhou2026irt}, G-theory optimizes an orthogonal dimension: conditions needed for target reliability rather than item discrimination.",
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_015j1ZnXA7QudF4rqm43p4eb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "c0be79eb-67d6-4f8f-9778-e51c6487ee99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 49 · 2026-05-23T19:07:29.098Z_

<details><summary>↩ Tool result · `toolu_015j1ZnXA7QudF4rqm43p4eb`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	A recommended 3-prompt $\times$ 3-seed design reduces item requirements from 552 to 178 for $G \geq 0.80$, confirmed across five benchmarks under binary scoring; multi-facet designs minimize items when item construction is costly, while single-condition designs suit compute-constrained settings. $G_\text{item}$ and $G_\text{model}$ have different bottlenecks---item count for the former, prompt standardization for the latter---providing orthogonal optimization paths: adding items improves item reliability, while controlling prompt and seed conditions improves model discriminability. All budgets assume binary scoring; extending to other model scales and continuous metrics is a priority. We recommend that benchmark designers adopt multi-facet validation (at minimum 3 prompts $\times$ 3 seeds) as standard practice when sizing pilot studies, and that leaderboard operators average over prompt and seed conditions to improve ranking stability. Code, data, and a D-study calculator will be released upon publication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "c1ecec3f-acae-4df0-8649-558fa544c4b3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nA recommended 3-prompt $\\times$ 3-seed design reduces item requirements from 552 to 178 for $G \\geq 0.80$, confirmed across five benchmarks under binary scoring; multi-facet designs minimize items when item construction is costly, while single-condition designs suit compute-constrained settings. $G_\\text{item}$ and $G_\\text{model}$ have different bottlenecks---item count for the former, prompt standardization for the latter---providing orthogonal optimization paths: adding items improves item reliability, while controlling prompt and seed conditions improves model discriminability. All budgets assume binary scoring; extending to other model scales and continuous metrics is a priority. We recommend that benchmark designers adopt multi-facet validation (at minimum 3 prompts $\\times$ 3 seeds) as standard practice when sizing pilot studies, and that leaderboard operators average over prompt and seed conditions to improve ranking stability. Code, data, and a D-study calculator will be released upon publication.",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01EuJk6Yo4fXpJmXHiWaXHmy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "63ce308a-82d4-495e-bb0c-5560d2c30a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 51 · 2026-05-23T19:07:30.055Z_

<details><summary>↩ Tool result · `toolu_01EuJk6Yo4fXpJmXHiWaXHmy`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based or base models. Preliminary scale validation (\S\ref{sec:scale_validation}) with Qwen2.5 (3B/7B/72B) and cross-family Llama-3.1-70B confirms consistent variance structure across two architecture families, but validation beyond these two families is needed before extrapolating budget recommendations to arbitrary architectures.
5	
6	The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. All D-study budgets reported in this paper are strictly valid only under binary correctness scoring. Our partial-credit analysis (GSM8K, 8 models) shows $G$ drops from 0.86 to 0.77 (crossed design) with all models showing $G_\text{partial} < G_\text{binary}$, suggesting limited transferability to finer-grained scoring rubrics; the analysis is limited to a single benchmark, and its generalizability to other tasks is unknown. Our temperature range (0.0--0.7) does not cover high-temperature regimes ($\tau > 1.0$) sometimes used in generation tasks. Our design varies few-shot example ordering but not example identity, a known variance source. Results depend on vLLM~0.9.2; different inference engines or vLLM versions may alter CUDA-level nondeterminism patterns.
7	
8	All eight models may have encountered benchmark items during pre-training; differential contamination across architectures could inflate model$\times$item interaction \citep{golchin2023contamination, oren2024proving}, though consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver. Contamination affects absolute budget estimates but has limited impact on the multi-facet vs.\ single-condition budget \emph{ratio}, since both designs are equally exposed to contaminated items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "5c735e45-04b8-4c6b-b118-8749e532ad4a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nOur eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based or base models. Preliminary scale validation (\\S\\ref{sec:scale_validation}) with Qwen2.5 (3B/7B/72B) and cross-family Llama-3.1-70B confirms consistent variance structure across two architecture families, but validation beyond these two families is needed before extrapolating budget recommendations to arbitrary architectures.\n\nThe benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. All D-study budgets reported in this paper are strictly valid only under binary correctness scoring. Our partial-credit analysis (GSM8K, 8 models) shows $G$ drops from 0.86 to 0.77 (crossed design) with all models showing $G_\\text{partial} < G_\\text{binary}$, suggesting limited transferability to finer-grained scoring rubrics; the analysis is limited to a single benchmark, and its generalizability to other tasks is unknown. Our temperature range (0.0--0.7) does not cover high-temperature regimes ($\\tau > 1.0$) sometimes used in generation tasks. Our design varies few-shot example ordering but not example identity, a known variance source. Results depend on vLLM~0.9.2; different inference engines or vLLM versions may alter CUDA-level nondeterminism patterns.\n\nAll eight models may have encountered benchmark items during pre-training; differential contamination across architectures could inflate model$\\times$item interaction \\citep{golchin2023contamination, oren2024proving}, though consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver. Contamination affects absolute budget estimates but has limited impact on the multi-facet vs.\\ single-condition budget \\emph{ratio}, since both designs are equally exposed to contaminated items.",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01NbWJABPSzNs2e7J9SLTyhL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "ae84ec36-089d-4d05-b220-ccc544a6a95c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHhKdCJY4W7TRfBFkYEy1b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6073,
      "cache_read_input_tokens": 36883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6073
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

_source line 53 · 2026-05-23T19:07:30.477Z_

<details><summary>↩ Tool result · `toolu_01NbWJABPSzNs2e7J9SLTyhL`</summary>

```text
1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This analysis covers the observed accuracy range ($p \in [0.3, 0.9]$); extreme-difficulty items ($p < 0.3$ or $p > 0.9$) are rare in our sample ($<$8\% of items) and may exhibit larger deviations. Henderson Method~I absorbs this Bernoulli-inherent variance into the residual, explaining inflated bias near medium difficulty; systematic component ordering is robustly recovered across all replications. Binary scoring inflates residual variance by absorbing the Bernoulli $p(1{-}p)$ ceiling, which enters $\sigma^2_\text{rel}$ and increases D-study item requirements. Within a matched probit simulation, binarization increases D-study budgets by approximately 36\% (99 $\to$ 135 items for $G \geq 0.80$), driven by residual inflation (16\% $\to$ 41\%) and item variance compression (50\% $\to$ 32\%). Facet$\times$item interactions---the components entering $\sigma^2_\text{rel}$---are best preserved under binarization (MAPE = 12.8\%, range 8.7--17.5\%), while residual variance inflates as expected from Bernoulli $p(1{-}p)$ noise (MAPE = 156\%). D-study budgets derived from binary data are therefore conservative: continuous-scored designs would require equal or fewer items for the same $G$ threshold. Null calibration (ratio $= 1.0008$) confirms that this conservatism does not distort relative component magnitudes.
14	
15	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. Bootstrap CIs capture item-sampling variability conditional on these 8 specific models; model-level stability is assessed separately via LOMO (below). The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\sim$127 unique items per 200-item resample) does not materially distort interval estimates. Stratified resampling by subject (10 subjects $\times$ 20 items) produces CIs within 4\% of simple item-level bootstrap, confirming that the within-subject dependence structure does not materially affect interval estimates.
16	
17	\paragraph{Facet specification sensitivity.} Treating temperature and ordering as fixed (rather than random) facets changes $G_\text{item}$ by only 0.37 percentage points (all-random: 0.820 vs.\ fixed temperature+ordering: 0.824). The small difference reflects the negligible temperature$\times$item (0.65\%) and ordering$\times$item (0.54\%) variance shares. The random-facet assumption is therefore robust to facet classification.
18	
19	\paragraph{Leave-one-model-out (LOMO).} Across all 40 leave-one-model-out subsets (8 models $\times$ 5 benchmarks), $G_\text{item}$ ranges from 0.833 to 0.919, with CV $\leq$ 1.25\% per benchmark. No single model removal changes $G$ by more than 0.030 (GSM8K, removing Gemma-2-9B). Item-related variance rankings are preserved in all 40 subsets. Table~\ref{tab:lomo_full} reports per-benchmark stability. This supports treating models as exchangeable within the target universe of 7--9B instruction-tuned models (\S\ref{sec:model_facet}).
20	
21	\begin{table}[h]
22	\centering
23	\caption{LOMO stability across five benchmarks (8 models $\times$ 5 benchmarks = 40 subsets).}
24	\label{tab:lomo_full}
25	\scriptsize
26	\begin{tabular}{lrrrr}
27	\toprule
28	Benchmark & $G_\text{full}$ & CV (\%) & Max $|\Delta G|$ & Most impactful \\
29	\midrule
30	MMLU & 0.896 & 0.49 & 0.019 & InternLM2.5-7B \\
31	ARC & 0.892 & 0.94 & 0.026 & Llama-3.1-8B \\
32	HellaSwag & 0.872 & 1.09 & 0.028 & Llama-3.1-8B \\
33	GSM8K & 0.863 & 1.25 & 0.030 & Gemma-2-9B \\
34	MATH & 0.888 & 1.20 & 0.029 & InternLM2.5-7B \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
39	\paragraph{Inter-model agreement.} We computed pairwise Cohen's $\kappa$ and Fleiss' $\kappa$ across all model pairs on each benchmark. Mean pairwise $\kappa$ ranges from 0.326 (MATH) to 0.461 (MMLU); Fleiss' $\kappa$ ranges from 0.309 (GSM8K) to 0.456 (MMLU). HellaSwag uses six models ($\kappa = 0.332$) due to missing OLMo and Yi data. The fair-to-moderate agreement independently confirms that the model$\times$item interaction (30--36\% of variance) reflects genuine differential item functioning: models disagree substantially on which items are difficult, consistent with prior DIF findings in educational measurement \cite{holland1993dif, clauser1998dif}.
40	
41	\paragraph{Scoring metric sensitivity.}
42	\label{sec:partial_credit}
43	To probe metric conditionality, we compared binary correctness with step-level partial credit on GSM8K using the full 8-model crossed design (200 items, 2,304 conditions per item). Under partial credit, $G_\text{item}$ drops from 0.863 to 0.768, with residual variance rising from 39.9\% to 64.9\% and item variance falling from 16.9\% to 10.3\%. All eight models individually show $G_\text{partial} < G_\text{binary}$ (mean $\Delta G = -0.135$, range $-0.025$ to $-0.309$), with $\Delta G$ magnitude moderated by model accuracy: higher-accuracy models have fewer incorrect responses whose scores shift under partial credit (e.g., OLMo at 70.1\% accuracy shows $\Delta G = -0.025$, while Llama at 49.0\% shows $\Delta G = -0.309$). The mechanism is clear: 48.1\% of incorrect responses have numerically correct arithmetic steps but incorrect problem setup, receiving partial score $= 1.0$ despite binary score $= 0$---this compresses item discrimination and inflates residual variance. Binary scoring amplifies prompt sensitivity by collapsing reasoning quality into pass/fail, confirming that all findings in this paper are metric-conditional.
44	
45	\paragraph{Facet specification sensitivity: random vs.\ fixed model.} Table~\ref{tab:fixed_vs_random} reports per-benchmark generalizability coefficients under random and fixed model specifications. The consistent $\Delta G$ of 0.077--0.113 confirms that random-model budgets are strictly more conservative across all benchmarks.
46	
47	\begin{table}[h]
48	\centering
49	\caption{Generalizability coefficients under random vs.\ fixed model facet specification across five benchmarks.}
50	\label{tab:fixed_vs_random}
51	\scriptsize
52	\begin{tabular}{lrrr}
53	\toprule
54	Benchmark & $G_\text{random}$ & $G_\text{fixed}$ & $\Delta G$ \\
55	\midrule
56	MMLU & 0.896 & 0.984 & $+$0.088 \\
57	ARC & 0.892 & 0.990 & $+$0.098 \\
58	HellaSwag & 0.872 & 0.984 & $+$0.113 \\
59	GSM8K & 0.863 & 0.951 & $+$0.089 \\
60	MATH & 0.888 & 0.965 & $+$0.077 \\
61	\midrule
62	Mean & 0.882 & 0.975 & $+$0.093 \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\paragraph{Null calibration.} We generate 100 Bernoulli-distributed datasets with item difficulties matched to the empirical distribution but no systematic facet effects. The observed-to-null variance ratio is 1.0008, confirming that Henderson Method~I does not introduce systematic bias when applied to binary outcomes. The null simulation also verifies that the item variance share (58.4\%) is not an artifact of the Bernoulli $p(1{-}p)$ ceiling: the null produces item variance of 0.08\%, three orders of magnitude below the observed value. Across all 100 replications, the same three components (item, model$\times$item, residual) emerge as the top three (set consistency 100\%), with Kendall's $\tau = 0.81$ between binary and continuous rankings.
68	
69	\paragraph{Reduced crossing validation.} To verify that the reduced crossing in exp-002 (BF16 only $\times$ 2 temperatures) does not introduce confounding, we extracted the corresponding subset from the fully crossed exp-001 design. The generalizability coefficient differs by only 0.0008 ($G = 0.9361$ vs.\ $0.9369$), and all non-precision variance components differ by less than 2 percentage points. The 10pp increase in item variance share (58.4\% $\to$ 68.5\%) is fully explained by the removal of precision-related components ($\sim$4.5\% total), which redistributes across remaining sources. This confirms that the exp-002 design preserves the variance structure of the full crossing.
70	
71	\section{Cross-Model D-Study Projections}
72	\label{app:dstudy_cross}
73	
74	Table~\ref{tab:dstudy_cross} extends the single-model D-study (Table~\ref{tab:dstudy} in main text) to per-benchmark cross-model projections with bootstrap confidence intervals (1,000 item-level resamples, 8 models, 2,304 conditions per item). The efficiency ratio is format-associated: MC benchmarks show 11--13$\times$ (mean 12.0$\times$ [11.6, 12.5]), while FF benchmarks show 21--22$\times$ (mean 21.5$\times$ [20.4, 22.8]).
75	
76	\begin{table}[h]
77	\centering
78	\caption{Cross-model D-study reproducibility budgets with 95\% bootstrap CIs. $n_{G \geq 0.80}$: items needed. Multi = multi-facet (2,304 cond.); Total = items $\times$ 2,304. Single = single-condition (total evals = item count).}
79	\label{tab:dstudy_cross}
80	\scriptsize
81	\resizebox{\columnwidth}{!}{%
82	\begin{tabular}{l rr r rr r}
83	\toprule
84	 & \multicolumn{3}{c}{Multi-facet (2,304 cond.)} & \multicolumn{2}{c}{Single-cond.} & \\
85	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
86	 & Items & 95\% CI & Total & Items & 95\% CI & Ratio [95\% CI] \\
87	\midrule
88	\multicolumn{7}{l}{\textit{Multiple-choice}} \\
89	MMLU & 93 & [76, 116] & 214K & 1{,}216 & [1004, 1491] & 13.1 [12.5, 13.7] \\
90	ARC & 98 & [71, 139] & 226K & 1{,}078 & [793, 1512] & 11.0 [10.7, 11.4] \\
91	Hella. & 118 & [93, 151] & 272K & 1{,}403 & [1120, 1790] & 11.9 [11.5, 12.3] \\
92	\midrule
93	\multicolumn{7}{l}{\textit{Free-form}} \\
94	GSM8K & 128 & [103, 162] & 295K & 2{,}768 & [2230, 3531] & 21.6 [20.7, 23.0] \\
95	MATH & 101 & [86, 122] & 233K & 2{,}160 & [1853, 2631] & 21.4 [20.2, 22.5] \\
96	\bottomrule
97	\end{tabular}%
98	}
99	\end{table}
100	
101	The higher item requirements relative to the single-model analysis (55 items in Table~\ref{tab:dstudy}) reflect the additional model$\times$item interaction variance that enters $\sigma^2_\text{rel}$ when models are crossed as a facet. The format-associated ratio pattern---FF benchmarks showing $\sim$2$\times$ the MC ratio---is consistent with the distributed variance structure observed in \S\ref{sec:format_conditional}, where FF benchmarks allocate more variance to model and model$\times$prompt components.
102	
103	\paragraph{Internal consistency check.} Table~\ref{tab:forward_pred} reports consistency checks from four exp-001 models (DeepSeek, Llama, Mistral, Qwen3) to the full eight-model design across all five benchmarks. MC benchmarks show $|\Delta G| \leq 0.029$ ($<$3.5\% error), while FF benchmarks show larger deviations ($|\Delta G| \leq 0.065$, $\sim$7\%) due to limited model diversity in the four-model subset. FF predictions consistently underestimate actual $G$ (conservative); MC predictions show mixed directions with small deviations ($|\Delta G| \leq 0.029$).
104	
105	\begin{table}[h]
106	\centering
107	\caption{Internal consistency: four-model subset vs.\ eight-model $G_\text{item}$. FF subsets underestimate actual $G$ (conservative); MC shows mixed directions with small deviations.}
108	\label{tab:forward_pred}
109	\small
110	\begin{tabular}{lrrrr}
111	\toprule
112	Benchmark & Predicted $G$ & Actual $G$ & $|\Delta G|$ & Error\% \\
113	\midrule
114	\multicolumn{5}{l}{\textit{Multiple-choice}} \\
115	MMLU & 0.888 & 0.896 & 0.009 & 0.96 \\
116	ARC & 0.904 & 0.892 & 0.012 & 1.38 \\
117	HellaSwag & 0.901 & 0.872 & 0.029 & 3.33 \\
118	\midrule
119	\multicolumn{5}{l}{\textit{Free-form}} \\
120	GSM8K & 0.803 & 0.863 & 0.059 & 6.88 \\
121	MATH & 0.823 & 0.888 & 0.065 & 7.30 \\
122	\midrule
123	Mean & --- & --- & 0.035 & 3.97 \\
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	\paragraph{Budget sensitivity to estimation error.}
129	\label{app:budget_sensitivity}
130	Figure~\ref{fig:budget_sensitivity} shows the effect of $|\Delta G| = 0.035$ estimation error on item budgets across all five benchmarks. The percentage increase is remarkably stable (23.0--24.5\%, mean 23.2\%), because the relative budget adjustment $\Delta n / n$ depends on the $G$-formula ratio rather than on absolute variance components. Absolute $\Delta n$ ranges from 13 (ARC) to 67 (GSM8K), scaling with the baseline budget.
131	
132	\begin{figure}[h]
133	\centering
134	\includegraphics[width=0.75\columnwidth]{budget_sensitivity_band}
135	\caption{Effect of $|\Delta G| = 0.035$ estimation error on item budgets across five benchmarks. The $\sim$23\% budget increase is consistent across all benchmarks, indicating D-study budgets are robust to estimation uncertainty.}
136	\label{fig:budget_sensitivity}
137	\end{figure}
138	
139	\paragraph{Cross-benchmark $G$ stability.}
140	\label{app:cross_benchmark_transfer}
141	$G_\text{item}$ values cluster in a narrow band across all five benchmarks (0.863--0.896, CV = 1.4\%), despite qualitatively different variance structures: MC benchmarks concentrate 68--72\% in item-related components while GSM8K disperses variance across item (17\%), model (11\%), and interaction (15\%) sources (Table~\ref{tab:cross_benchmark}). This stability implies that D-study budget recommendations calibrated on one benchmark provide reasonable order-of-magnitude guidance for others. However, the 0.033 range in $G_\text{item}$ translates to a 71--128 item range for multi-facet $G \geq 0.80$ (Table~\ref{tab:dstudy_cross}), and the variance compositions differ substantially---benchmark-specific G-studies remain necessary to identify dominant variance sources and optimize condition selection.
142	
143	\section{Intermediate D-Study Designs}
144	\label{app:intermediate_dstudy}
145	
146	Table~\ref{tab:intermediate_dstudy} shows how reliability improves as evaluation designs increase from single-condition to full multi-facet crossing. The steepest gain occurs at the ``minimal upgrade'' level (2 prompts): $G_{200}$ jumps from 0.592 to 0.692 at 2$\times$ cost. A minimal sufficient design for $G \geq 0.80$ is 3 prompts $\times$ 3 seeds (9 conditions, $G_{200} = 0.818$, $n_{G \geq 0.80} = 178$). Beyond the ``standard'' level (32 conditions), adding orderings provides negligible benefit (ordering$\times$item $<$1\%), confirming that prompt and seed diversity are the primary reliability drivers.
147	
148	\begin{table}[h]
149	\centering
150	\caption{Intermediate D-study designs (single-model, MMLU). Designs are ordered by increasing conditions per item; $G_{200}$ and $n_{G \geq 0.80}$ are D-study projections from exp-001 variance components.}
151	\label{tab:intermediate_dstudy}
152	\scriptsize
153	\begin{tabular}{llrrr}
154	\toprule
155	Design & Conditions & $G_{200}$ & $n_{G{\geq}.80}$ \\
156	\midrule
157	Single-condition & 1 & .592 & 552 \\
158	Minimal upgrade (2p) & 2 & .692 & 357 \\
159	Easy upgrade (2p$\times$2s) & 4 & .766 & 245 \\
160	Moderate (3p$\times$3s) & 9 & .818 & 178 \\
161	Standard (4p$\times$4s$\times$2t) & 32 & .869 & 121 \\
162	Enhanced (+4 orderings) & 72 & .871 & 119 \\
163	Full multi-facet & 1{,}296 & .936 & 55 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\section{Format-Associated Variance: Per-Benchmark Details}
169	\label{app:format_details}
170	
171	This section supplements the compressed format-associated analysis in \S\ref{sec:format_conditional} with per-benchmark details.
172	
173	\paragraph{MC benchmark exceptions.} HellaSwag is the sole MC case where model$\times$item slightly exceeds item (36.0\% vs.\ 34.3\%), though their sum (70.3\%) remains in the MC range (68--72\%). Among MC benchmarks, ARC-Challenge shows an anomalously high model$\times$prompt interaction (8.0\% vs.\ $<$2\% for MMLU and HellaSwag), suggesting that science-domain items are differentially sensitive to option formatting across model families.
174	
175	\paragraph{FF benchmark patterns.} Free-form benchmarks differ markedly from MC. On GSM8K, variance distributes across item (16.9\%), model$\times$item (14.6\%), model (10.7\%), and model$\times$prompt (8.5\%); prompt main effect is 5.4\%. MATH shows an intermediate pattern: item leads at 24.0\% with model$\times$item at 17.3\%, but residual variance is substantially larger (43.9\%). Item-level regression reveals that FF residual variance is predominantly explained by the Bernoulli variance ceiling $p(1{-}p)$ ($R^2 = 0.47$--$0.86$; Appendix~\ref{app:ff_residual}): medium-difficulty items maximize binary outcome variance regardless of facet structure, so the elevated FF residuals reflect measurement resolution rather than unmodeled substantive sources.
176	
177	\paragraph{Difficulty dispersion as variance predictor.} Difficulty dispersion ($\text{std}(p_i)$) strongly predicts item variance share ($\rho = 0.82$, $n = 5$ benchmarks; Appendix~\ref{app:difficulty_scatter}; reasoning-heavy subjects show $G_\text{item}$ as low as 0.614, Appendix~\ref{app:subject_gstudy}). Format constrains the noise floor, but difficulty heterogeneity determines variance magnitude within it.
178	
179	\section{Cross-Benchmark Difficulty Heterogeneity}
180	\label{app:difficulty_scatter}
181	
182	Figure~\ref{fig:difficulty_scatter} plots item difficulty heterogeneity ($\text{std}(p_i)$ across models) against \texttt{item\_id} variance share for all five benchmarks. MC benchmarks cluster at higher dispersion ($0.27$--$0.31$) and higher item variance ($34$--$38\%$), while FF benchmarks occupy the lower-left region ($0.22$--$0.23$, $17$--$24\%$). The cross-benchmark Spearman $\rho = 0.82$ ($p = 0.089$, $n = 5$) is consistent in direction with the within-MMLU correlation ($\rho = 0.806$, $p = 0.005$, $n = 10$ subjects); these are independent analyses at different granularities (benchmarks vs.\ subjects within MMLU), providing multi-scale support for the item difficulty heterogeneity mechanism discussed in \S\ref{sec:format_conditional}.
183	
184	\begin{figure}[h]
185	\centering
186	\includegraphics[width=0.75\columnwidth]{fig4_difficulty_scatter}
187	\caption{Item difficulty heterogeneity ($\text{std}(p_i)$, computed over available models per benchmark, 6--8 models) versus \texttt{item\_id} variance share (as reported in Table~\ref{tab:cross_benchmark}) across five benchmarks. MC benchmarks (filled) exhibit higher difficulty dispersion and item variance than FF benchmarks (open). Spearman $\rho = 0.82$, $p = 0.089$.}
188	\label{fig:difficulty_scatter}
189	\end{figure}
190	
191	\section{MMLU Subject-Level Variance Decomposition}
192	\label{app:subject_gstudy}
193	
194	Table~\ref{tab:subject_gstudy} reports per-subject variance decomposition for 10 MMLU subjects (20 items each, 8 models, 2,304 conditions per item). $G_\text{item}$ ranges from 0.614 (\texttt{high\_school\_mathematics}) to 0.930 (\texttt{international\_law}), with mean 0.843. Knowledge-intensive subjects (\texttt{international\_law}, \texttt{clinical\_knowledge}, \texttt{world\_religions}) show \texttt{item\_id} $>$ 40\%, while reasoning-heavy subjects (\texttt{high\_school\_mathematics}, \texttt{abstract\_algebra}) show model$\times$item $>$ \texttt{item\_id}, consistent with models differing more in reasoning strategies than in factual recall. The \texttt{high\_school\_mathematics} \texttt{item\_id} of 10.4\% referenced in \S\ref{sec:format_conditional} is the lowest across all subjects, below even GSM8K (16.9\%).
195	
196	\begin{table}[h]
197	\centering
198	\caption{Subject-level variance decomposition within MMLU (20 items per subject, 8 models, 2,304 conditions per item). Sorted by $G_\text{item}$ descending.}
199	\label{tab:subject_gstudy}
200	\scriptsize
201	\begin{tabular}{lrrrr}
202	\toprule
203	Subject & Acc. & item\% & mod.$\times$it.\% & $G_\text{item}$ \\
204	\midrule
205	international\_law & .717 & 44.4 & 24.1 & .930 \\
206	clinical\_knowledge & .581 & 47.5 & 30.0 & .923 \\
207	world\_religions & .826 & 42.2 & 27.1 & .910 \\
208	computer\_security & .740 & 37.0 & 24.9 & .908 \\
209	college\_physics & .436 & 31.6 & 30.1 & .876 \\
210	philosophy & .782 & 33.0 & 36.1 & .868 \\
211	abstract\_algebra & .457 & 24.1 & 32.8 & .822 \\
212	us\_foreign\_policy & .864 & 20.4 & 36.9 & .802 \\
213	professional\_medicine & .671 & 19.9 & 41.7 & .778 \\
214	high\_school\_math & .385 & 10.4 & 41.9 & .614 \\
215	\midrule
216	Mean & --- & 31.1 & 32.6 & .843 \\
217	\bottomrule
218	\end{tabular}
219	\end{table}
220	
221	\section{FF Residual Variance Analysis}
222	\label{app:ff_residual}
223	
224	To investigate whether the elevated residual variance in free-form benchmarks (GSM8K 39.9\%, MATH 43.9\%) reflects unmodeled substantive sources or measurement properties of binary scoring, we regress item-level residual variance on item characteristics across all five benchmarks (Table~\ref{tab:ff_residual}).
225	
226	The dominant predictor is the quadratic difficulty effect ($p < 10^{-5}$ on all benchmarks): items near $p = 0.5$ show maximal residual variance, while items near the floor or ceiling show minimal residual. This inverted-U pattern directly mirrors the Bernoulli variance ceiling $p(1{-}p)$. Item content features (number of reasoning steps, answer length) are not significant predictors for GSM8K ($p > 0.38$), confirming that the difficulty--residual relationship is statistical rather than content-driven.
227	
228	FF benchmarks show substantially higher $R^2$ (mean 0.66) than MC benchmarks (mean 0.25), consistent with FF items spanning a wider difficulty range. The MC--FF contrast in residual magnitude is therefore a mathematical consequence of the difficulty distribution under binary scoring, not evidence of additional unmodeled variance sources in free-form evaluation.
229	
230	\begin{table}[h]
231	\centering
232	\caption{Item-level residual variance regression. Difficulty$^2$ = quadratic (inverted-U) term reflecting the Bernoulli $p(1{-}p)$ ceiling. GSM8K additionally tests n\_steps and answer\_length (both $p > 0.38$).}
233	\label{tab:ff_residual}
234	\scriptsize
235	\begin{tabular}{lrrr}
236	\toprule
237	Benchmark & $R^2$ (full) & $R^2$ (diff.\ only) & Diff.$^2$ $p$ \\
238	\midrule
239	\multicolumn{4}{l}{\textit{Multiple-choice}} \\
240	MMLU & 0.377 & 0.347 & $<$0.001 \\
241	ARC & 0.221 & 0.204 & $<$0.001 \\
242	HellaSwag & 0.156 & 0.140 & $<$0.001 \\
243	\midrule
244	\multicolumn{4}{l}{\textit{Free-form}} \\
245	GSM8K & 0.468 & 0.449 & $<$0.001 \\
246	MATH & 0.856 & 0.845 & $<$0.001 \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	\section{Model and Prompt Details}
252	\label{app:models}
253	
254	\paragraph{Models.} Table~\ref{tab:model_ids} lists the eight models with their HuggingFace identifiers.
255	
256	\begin{table}[h]
257	\centering
258	\caption{Models used in all experiments.}
259	\label{tab:model_ids}
260	\scriptsize
261	\begin{tabular}{llr}
262	\toprule
263	Short name & HuggingFace identifier & Params \\
264	\midrule
265	Llama-3.1-8B & \texttt{meta-llama/Llama-3.1-8B-Instruct} & 8B \\
266	Gemma-2-9B & \texttt{google/gemma-2-9b-it} & 9B \\
267	Mistral-7B-v0.3 & \texttt{mistralai/Mistral-7B-Instruct-v0.3} & 7B \\
268	Qwen3-8B & \texttt{Qwen/Qwen3-8B} & 8B \\
269	Yi-1.5-9B & \texttt{01-ai/Yi-1.5-9B-Chat} & 9B \\
270	OLMo-2-7B & \texttt{allenai/OLMo-2-1124-7B-Instruct} & 7B \\
271	InternLM2.5-7B & \texttt{internlm/internlm2\_5-7b-chat} & 7B \\
272	DeepSeek-7B & \texttt{deepseek-ai/deepseek-llm-7b-chat} & 7B \\
273	\bottomrule
274	\end{tabular}
275	\end{table}
276	
277	\paragraph{Prompt templates.} Our six prompt templates follow a surface perturbation design inspired by BrittleBench \cite{brittlebench2026}. For multiple-choice benchmarks, templates vary along three dimensions: option layout (lettered vs.\ numbered), instruction wording (direct vs.\ contextual), and answer prompt cue. For free-form benchmarks, templates vary chain-of-thought elicitation strategy. All six templates are semantically equivalent---they request the same task with different surface forms---to isolate formatting effects from content effects. ARC-Challenge and HellaSwag use the same six surface patterns as MMLU with domain-appropriate system instructions; MATH mirrors the GSM8K pattern with \texttt{\textbackslash boxed\{\}} answer formatting.
278	
279	\smallskip\noindent\textit{MMLU templates (representative MC format):}
280	\begin{enumerate}\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}\setlength{\topsep}{0pt}
281	\item \texttt{The following are multiple choice questions (with answers) about \{subject\}.\textbackslash n\textbackslash n\{question\}\textbackslash nA. ... D. ...\textbackslash nAnswer:}
282	\item \texttt{Answer the following \{subject\} questions by selecting the correct option.\textbackslash nQuestion: \{question\}\textbackslash n(A) ... (B) ... (C) ... (D) ...\textbackslash nCorrect answer:}
283	\item \texttt{Below are \{subject\} multiple-choice problems. Pick the right letter.\textbackslash nQ: \{question\}\textbackslash n~~A) ... B) ... C) ... D) ...\textbackslash nA:}
284	\item \texttt{Answer the following \{subject\} question by selecting A, B, C, or D.\textbackslash n\{question\}\textbackslash n- A. ... - B. ... - C. ... - D. ...\textbackslash nAnswer:}
285	\item \texttt{Below is a \{subject\} exam question with four possible answers. Choose the correct one.\textbackslash n\{question\}\textbackslash nOption A: ... Option B: ... Option C: ... Option D: ...\textbackslash nCorrect:}
286	\item \texttt{Question (\{subject\}):\textbackslash n\{question\}\textbackslash nChoices: (A) ... (B) ... (C) ... (D) ...\textbackslash nYour answer:}
287	\end{enumerate}
288	
289	\smallskip\noindent\textit{GSM8K templates (representative FF format):}
290	\begin{enumerate}\setlength{\itemsep}{0pt}\setlength{\parsep}{0pt}\setlength{\topsep}{0pt}
291	\item \texttt{Solve the following math problem step by step.\textbackslash nQ: \{question\}\textbackslash nA: Let's think step by step.}
292	\item \texttt{Answer the following math word problem. Show your work.\textbackslash nQuestion: \{question\}\textbackslash nSolution:}
293	\item \texttt{Solve each problem below. Write your reasoning, then give the final answer after \#\#\#\#.\textbackslash nProblem: \{question\}\textbackslash nReasoning:}
294	\item \texttt{You are a math tutor. Solve the problem and show your steps.\textbackslash n\{question\}\textbackslash nSteps:}
295	\item \texttt{Work through this math question carefully.\textbackslash nQ: \{question\}\textbackslash nWork:}
296	\item \texttt{Math problem:\textbackslash n\{question\}\textbackslash nLet's solve this step by step.}
297	\end{enumerate}
298	
299	\section{Use of AI Assistants}
300	\label{app:ai-assistants}
301	
302	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
303	\begin{itemize}
304	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
305	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
306	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
307	\end{itemize}
308	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "043f5c16-301a-472a-b7e0-66f66e1a9f32",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Additional Robustness Analyses}\n\\label{app:robustness}\n\nWe report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.\n\n\\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\\rho = 1.0$) relative to Henderson Method~I \\cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.\n\n\\paragraph{Accuracy-range stability.} The \\texttt{item\\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.\n\n\\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \\cite[Ch.~12]{brennan2001generalizability}.\n\n\\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\\rho = 0.732$ between binary and continuous rankings, excluding residual; \\texttt{item\\_id} dominant in all 100 replications; top-5 ordering correct in 79\\% of replications). Bias analysis by difficulty stratum shows $|\\text{bias}| = 0.28$--$0.37$ for items with $p \\in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This analysis covers the observed accuracy range ($p \\in [0.3, 0.9]$); extreme-difficulty items ($p < 0.3$ or $p > 0.9$) are rare in our sample ($<$8\\% of items) and may exhibit larger deviations. Henderson Method~I absorbs this Bernoulli-inherent variance into the residual, explaining inflated bias near medium difficulty; systematic component ordering is robustly recovered across all replications. Binary scoring inflates residual variance by absorbing the Bernoulli $p(1{-}p)$ ceiling, which enters $\\sigma^2_\\text{rel}$ and increases D-study item requirements. Within a matched probit simulation, binarization increases D-study budgets by approximately 36\\% (99 $\\to$ 135 items for $G \\geq 0.80$), driven by residual inflation (16\\% $\\to$ 41\\%) and item variance compression (50\\% $\\to$ 32\\%). Facet$\\times$item interactions---the components entering $\\sigma^2_\\text{rel}$---are best preserved under binarization (MAPE = 12.8\\%, range 8.7--17.5\\%), while residual variance inflates as expected from Bernoulli $p(1{-}p)$ noise (MAPE = 156\\%). D-study budgets derived from binary data are therefore conservative: continuous-scored designs would require equal or fewer items for the same $G$ threshold. Null calibration (ratio $= 1.0008$) confirms that this conservatism does not distort relative component magnitudes.\n\n\\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. Bootstrap CIs capture item-sampling variability conditional on these 8 specific models; model-level stability is assessed separately via LOMO (below). The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\\sim$127 unique items per 200-item resample) does not materially distort interval estimates. Stratified resampling by subject (10 subjects $\\times$ 20 items) produces CIs within 4\\% of simple item-level bootstrap, confirming that the within-subject dependence structure does not materially affect interval estimates.\n\n\\paragraph{Facet specification sensitivity.} Treating temperature and ordering as fixed (rather than random) facets changes $G_\\text{item}$ by only 0.37 percentage points (all-random: 0.820 vs.\\ fixed temperature+ordering: 0.824). The small difference reflects the negligible temperature$\\times$item (0.65\\%) and ordering$\\times$item (0.54\\%) variance shares. The random-facet assumption is therefore robust to facet classification.\n\n\\paragraph{Leave-one-model-out (LOMO).} Across all 40 leave-one-model-out subsets (8 models $\\times$ 5 benchmarks), $G_\\text{item}$ ranges from 0.833 to 0.919, with CV $\\leq$ 1.25\\% per benchmark. No single model removal changes $G$ by more than 0.030 (GSM8K, removing Gemma-2-9B). Item-related variance rankings are preserved in all 40 subsets. Table~\\ref{tab:lomo_full} reports per-benchmark stability. This supports treating models as exchangeable within the target universe of 7--9B instruction-tuned models (\\S\\ref{sec:model_facet}).\n\n\\begin{table}[h]\n\\centering\n\\caption{LOMO stability across five benchmarks (8 models $\\times$ 5 benchmarks = 40 subsets).}\n\\label{tab:lomo_full}\n\\scriptsize\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & $G_\\text{full}$ & CV (\\%) & Max $|\\Delta G|$ & Most impactful \\\\\n\\midrule\nMMLU & 0.896 & 0.49 & 0.019 & InternLM2.5-7B \\\\\nARC & 0.892 & 0.94 & 0.026 & Llama-3.1-8B \\\\\nHellaSwag & 0.872 & 1.09 & 0.028 & Llama-3.1-8B \\\\\nGSM8K & 0.863 & 1.25 & 0.030 & Gemma-2-9B \\\\\nMATH & 0.888 & 1.20 & 0.029 & InternLM2.5-7B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Inter-model agreement.} We computed pairwise Cohen's $\\kappa$ and Fleiss' $\\kappa$ across all model pairs on each benchmark. Mean pairwise $\\kappa$ ranges from 0.326 (MATH) to 0.461 (MMLU); Fleiss' $\\kappa$ ranges from 0.309 (GSM8K) to 0.456 (MMLU). HellaSwag uses six models ($\\kappa = 0.332$) due to missing OLMo and Yi data. The fair-to-moderate agreement independently confirms that the model$\\times$item interaction (30--36\\% of variance) reflects genuine differential item functioning: models disagree substantially on which items are difficult, consistent with prior DIF findings in educational measurement \\cite{holland1993dif, clauser1998dif}.\n\n\\paragraph{Scoring metric sensitivity.}\n\\label{sec:partial_credit}\nTo probe metric conditionality, we compared binary correctness with step-level partial credit on GSM8K using the full 8-model crossed design (200 items, 2,304 conditions per item). Under partial credit, $G_\\text{item}$ drops from 0.863 to 0.768, with residual variance rising from 39.9\\% to 64.9\\% and item variance falling from 16.9\\% to 10.3\\%. All eight models individually show $G_\\text{partial} < G_\\text{binary}$ (mean $\\Delta G = -0.135$, range $-0.025$ to $-0.309$), with $\\Delta G$ magnitude moderated by model accuracy: higher-accuracy models have fewer incorrect responses whose scores shift under partial credit (e.g., OLMo at 70.1\\% accuracy shows $\\Delta G = -0.025$, while Llama at 49.0\\% shows $\\Delta G = -0.309$). The mechanism is clear: 48.1\\% of incorrect responses have numerically correct arithmetic steps but incorrect problem setup, receiving partial score $= 1.0$ despite binary score $= 0$---this compresses item discrimination and inflates residual variance. Binary scoring amplifies prompt sensitivity by collapsing reasoning quality into pass/fail, confirming that all findings in this paper are metric-conditional.\n\n\\paragraph{Facet specification sensitivity: random vs.\\ fixed model.} Table~\\ref{tab:fixed_vs_random} reports per-benchmark generalizability coefficients under random and fixed model specifications. The consistent $\\Delta G$ of 0.077--0.113 confirms that random-model budgets are strictly more conservative across all benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Generalizability coefficients under random vs.\\ fixed model facet specification across five benchmarks.}\n\\label{tab:fixed_vs_random}\n\\scriptsize\n\\begin{tabular}{lrrr}\n\\toprule\nBenchmark & $G_\\text{random}$ & $G_\\text{fixed}$ & $\\Delta G$ \\\\\n\\midrule\nMMLU & 0.896 & 0.984 & $+$0.088 \\\\\nARC & 0.892 & 0.990 & $+$0.098 \\\\\nHellaSwag & 0.872 & 0.984 & $+$0.113 \\\\\nGSM8K & 0.863 & 0.951 & $+$0.089 \\\\\nMATH & 0.888 & 0.965 & $+$0.077 \\\\\n\\midrule\nMean & 0.882 & 0.975 & $+$0.093 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Null calibration.} We generate 100 Bernoulli-distributed datasets with item difficulties matched to the empirical distribution but no systematic facet effects. The observed-to-null variance ratio is 1.0008, confirming that Henderson Method~I does not introduce systematic bias when applied to binary outcomes. The null simulation also verifies that the item variance share (58.4\\%) is not an artifact of the Bernoulli $p(1{-}p)$ ceiling: the null produces item variance of 0.08\\%, three orders of magnitude below the observed value. Across all 100 replications, the same three components (item, model$\\times$item, residual) emerge as the top three (set consistency 100\\%), with Kendall's $\\tau = 0.81$ between binary and continuous rankings.\n\n\\paragraph{Reduced crossing validation.} To verify that the reduced crossing in exp-002 (BF16 only $\\times$ 2 temperatures) does not introduce confounding, we extracted the corresponding subset from the fully crossed exp-001 design. The generalizability coefficient differs by only 0.0008 ($G = 0.9361$ vs.\\ $0.9369$), and all non-precision variance components differ by less than 2 percentage points. The 10pp increase in item variance share (58.4\\% $\\to$ 68.5\\%) is fully explained by the removal of precision-related components ($\\sim$4.5\\% total), which redistributes across remaining sources. This confirms that the exp-002 design preserves the variance structure of the full crossing.\n\n\\section{Cross-Model D-Study Projections}\n\\label{app:dstudy_cross}\n\nTable~\\ref{tab:dstudy_cross} extends the single-model D-study (Table~\\ref{tab:dstudy} in main text) to per-benchmark cross-model projections with bootstrap confidence intervals (1,000 item-level resamples, 8 models, 2,304 conditions per item). The efficiency ratio is format-associated: MC benchmarks show 11--13$\\times$ (mean 12.0$\\times$ [11.6, 12.5]), while FF benchmarks show 21--22$\\times$ (mean 21.5$\\times$ [20.4, 22.8]).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model D-study reproducibility budgets with 95\\% bootstrap CIs. $n_{G \\geq 0.80}$: items needed. Multi = multi-facet (2,304 cond.); Total = items $\\times$ 2,304. Single = single-condition (total evals = item count).}\n\\label{tab:dstudy_cross}\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l rr r rr r}\n\\toprule\n & \\multicolumn{3}{c}{Multi-facet (2,304 cond.)} & \\multicolumn{2}{c}{Single-cond.} & \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n & Items & 95\\% CI & Total & Items & 95\\% CI & Ratio [95\\% CI] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Multiple-choice}} \\\\\nMMLU & 93 & [76, 116] & 214K & 1{,}216 & [1004, 1491] & 13.1 [12.5, 13.7] \\\\\nARC & 98 & [71, 139] & 226K & 1{,}078 & [793, 1512] & 11.0 [10.7, 11.4] \\\\\nHella. & 118 & [93, 151] & 272K & 1{,}403 & [1120, 1790] & 11.9 [11.5, 12.3] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Free-form}} \\\\\nGSM8K & 128 & [103, 162] & 295K & 2{,}768 & [2230, 3531] & 21.6 [20.7, 23.0] \\\\\nMATH & 101 & [86, 122] & 233K & 2{,}160 & [1853, 2631] & 21.4 [20.2, 22.5] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nThe higher item requirements relative to the single-model analysis (55 items in Table~\\ref{tab:dstudy}) reflect the additional model$\\times$item interaction variance that enters $\\sigma^2_\\text{rel}$ when models are crossed as a facet. The format-associated ratio pattern---FF benchmarks showing $\\sim$2$\\times$ the MC ratio---is consistent with the distributed variance structure observed in \\S\\ref{sec:format_conditional}, where FF benchmarks allocate more variance to model and model$\\times$prompt components.\n\n\\paragraph{Internal consistency check.} Table~\\ref{tab:forward_pred} reports consistency checks from four exp-001 models (DeepSeek, Llama, Mistral, Qwen3) to the full eight-model design across all five benchmarks. MC benchmarks show $|\\Delta G| \\leq 0.029$ ($<$3.5\\% error), while FF benchmarks show larger deviations ($|\\Delta G| \\leq 0.065$, $\\sim$7\\%) due to limited model diversity in the four-model subset. FF predictions consistently underestimate actual $G$ (conservative); MC predictions show mixed directions with small deviations ($|\\Delta G| \\leq 0.029$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Internal consistency: four-model subset vs.\\ eight-model $G_\\text{item}$. FF subsets underestimate actual $G$ (conservative); MC shows mixed directions with small deviations.}\n\\label{tab:forward_pred}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & Predicted $G$ & Actual $G$ & $|\\Delta G|$ & Error\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Multiple-choice}} \\\\\nMMLU & 0.888 & 0.896 & 0.009 & 0.96 \\\\\nARC & 0.904 & 0.892 & 0.012 & 1.38 \\\\\nHellaSwag & 0.901 & 0.872 & 0.029 & 3.33 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Free-form}} \\\\\nGSM8K & 0.803 & 0.863 & 0.059 & 6.88 \\\\\nMATH & 0.823 & 0.888 & 0.065 & 7.30 \\\\\n\\midrule\nMean & --- & --- & 0.035 & 3.97 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Budget sensitivity to estimation error.}\n\\label{app:budget_sensitivity}\nFigure~\\ref{fig:budget_sensitivity} shows the effect of $|\\Delta G| = 0.035$ estimation error on item budgets across all five benchmarks. The percentage increase is remarkably stable (23.0--24.5\\%, mean 23.2\\%), because the relative budget adjustment $\\Delta n / n$ depends on the $G$-formula ratio rather than on absolute variance components. Absolute $\\Delta n$ ranges from 13 (ARC) to 67 (GSM8K), scaling with the baseline budget.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{budget_sensitivity_band}\n\\caption{Effect of $|\\Delta G| = 0.035$ estimation error on item budgets across five benchmarks. The $\\sim$23\\% budget increase is consistent across all benchmarks, indicating D-study budgets are robust to estimation uncertainty.}\n\\label{fig:budget_sensitivity}\n\\end{figure}\n\n\\paragraph{Cross-benchmark $G$ stability.}\n\\label{app:cross_benchmark_transfer}\n$G_\\text{item}$ values cluster in a narrow band across all five benchmarks (0.863--0.896, CV = 1.4\\%), despite qualitatively different variance structures: MC benchmarks concentrate 68--72\\% in item-related components while GSM8K disperses variance across item (17\\%), model (11\\%), and interaction (15\\%) sources (Table~\\ref{tab:cross_benchmark}). This stability implies that D-study budget recommendations calibrated on one benchmark provide reasonable order-of-magnitude guidance for others. However, the 0.033 range in $G_\\text{item}$ translates to a 71--128 item range for multi-facet $G \\geq 0.80$ (Table~\\ref{tab:dstudy_cross}), and the variance compositions differ substantially---benchmark-specific G-studies remain necessary to identify dominant variance sources and optimize condition selection.\n\n\\section{Intermediate D-Study Designs}\n\\label{app:intermediate_dstudy}\n\nTable~\\ref{tab:intermediate_dstudy} shows how reliability improves as evaluation designs increase from single-condition to full multi-facet crossing. The steepest gain occurs at the ``minimal upgrade'' level (2 prompts): $G_{200}$ jumps from 0.592 to 0.692 at 2$\\times$ cost. A minimal sufficient design for $G \\geq 0.80$ is 3 prompts $\\times$ 3 seeds (9 conditions, $G_{200} = 0.818$, $n_{G \\geq 0.80} = 178$). Beyond the ``standard'' level (32 conditions), adding orderings provides negligible benefit (ordering$\\times$item $<$1\\%), confirming that prompt and seed diversity are the primary reliability drivers.\n\n\\begin{table}[h]\n\\centering\n\\caption{Intermediate D-study designs (single-model, MMLU). Designs are ordered by increasing conditions per item; $G_{200}$ and $n_{G \\geq 0.80}$ are D-study projections from exp-001 variance components.}\n\\label{tab:intermediate_dstudy}\n\\scriptsize\n\\begin{tabular}{llrrr}\n\\toprule\nDesign & Conditions & $G_{200}$ & $n_{G{\\geq}.80}$ \\\\\n\\midrule\nSingle-condition & 1 & .592 & 552 \\\\\nMinimal upgrade (2p) & 2 & .692 & 357 \\\\\nEasy upgrade (2p$\\times$2s) & 4 & .766 & 245 \\\\\nModerate (3p$\\times$3s) & 9 & .818 & 178 \\\\\nStandard (4p$\\times$4s$\\times$2t) & 32 & .869 & 121 \\\\\nEnhanced (+4 orderings) & 72 & .871 & 119 \\\\\nFull multi-facet & 1{,}296 & .936 & 55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Format-Associated Variance: Per-Benchmark Details}\n\\label{app:format_details}\n\nThis section supplements the compressed format-associated analysis in \\S\\ref{sec:format_conditional} with per-benchmark details.\n\n\\paragraph{MC benchmark exceptions.} HellaSwag is the sole MC case where model$\\times$item slightly exceeds item (36.0\\% vs.\\ 34.3\\%), though their sum (70.3\\%) remains in the MC range (68--72\\%). Among MC benchmarks, ARC-Challenge shows an anomalously high model$\\times$prompt interaction (8.0\\% vs.\\ $<$2\\% for MMLU and HellaSwag), suggesting that science-domain items are differentially sensitive to option formatting across model families.\n\n\\paragraph{FF benchmark patterns.} Free-form benchmarks differ markedly from MC. On GSM8K, variance distributes across item (16.9\\%), model$\\times$item (14.6\\%), model (10.7\\%), and model$\\times$prompt (8.5\\%); prompt main effect is 5.4\\%. MATH shows an intermediate pattern: item leads at 24.0\\% with model$\\times$item at 17.3\\%, but residual variance is substantially larger (43.9\\%). Item-level regression reveals that FF residual variance is predominantly explained by the Bernoulli variance ceiling $p(1{-}p)$ ($R^2 = 0.47$--$0.86$; Appendix~\\ref{app:ff_residual}): medium-difficulty items maximize binary outcome variance regardless of facet structure, so the elevated FF residuals reflect measurement resolution rather than unmodeled substantive sources.\n\n\\paragraph{Difficulty dispersion as variance predictor.} Difficulty dispersion ($\\text{std}(p_i)$) strongly predicts item variance share ($\\rho = 0.82$, $n = 5$ benchmarks; Appendix~\\ref{app:difficulty_scatter}; reasoning-heavy subjects show $G_\\text{item}$ as low as 0.614, Appendix~\\ref{app:subject_gstudy}). Format constrains the noise floor, but difficulty heterogeneity determines variance magnitude within it.\n\n\\section{Cross-Benchmark Difficulty Heterogeneity}\n\\label{app:difficulty_scatter}\n\nFigure~\\ref{fig:difficulty_scatter} plots item difficulty heterogeneity ($\\text{std}(p_i)$ across models) against \\texttt{item\\_id} variance share for all five benchmarks. MC benchmarks cluster at higher dispersion ($0.27$--$0.31$) and higher item variance ($34$--$38\\%$), while FF benchmarks occupy the lower-left region ($0.22$--$0.23$, $17$--$24\\%$). The cross-benchmark Spearman $\\rho = 0.82$ ($p = 0.089$, $n = 5$) is consistent in direction with the within-MMLU correlation ($\\rho = 0.806$, $p = 0.005$, $n = 10$ subjects); these are independent analyses at different granularities (benchmarks vs.\\ subjects within MMLU), providing multi-scale support for the item difficulty heterogeneity mechanism discussed in \\S\\ref{sec:format_conditional}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{fig4_difficulty_scatter}\n\\caption{Item difficulty heterogeneity ($\\text{std}(p_i)$, computed over available models per benchmark, 6--8 models) versus \\texttt{item\\_id} variance share (as reported in Table~\\ref{tab:cross_benchmark}) across five benchmarks. MC benchmarks (filled) exhibit higher difficulty dispersion and item variance than FF benchmarks (open). Spearman $\\rho = 0.82$, $p = 0.089$.}\n\\label{fig:difficulty_scatter}\n\\end{figure}\n\n\\section{MMLU Subject-Level Variance Decomposition}\n\\label{app:subject_gstudy}\n\nTable~\\ref{tab:subject_gstudy} reports per-subject variance decomposition for 10 MMLU subjects (20 items each, 8 models, 2,304 conditions per item). $G_\\text{item}$ ranges from 0.614 (\\texttt{high\\_school\\_mathematics}) to 0.930 (\\texttt{international\\_law}), with mean 0.843. Knowledge-intensive subjects (\\texttt{international\\_law}, \\texttt{clinical\\_knowledge}, \\texttt{world\\_religions}) show \\texttt{item\\_id} $>$ 40\\%, while reasoning-heavy subjects (\\texttt{high\\_school\\_mathematics}, \\texttt{abstract\\_algebra}) show model$\\times$item $>$ \\texttt{item\\_id}, consistent with models differing more in reasoning strategies than in factual recall. The \\texttt{high\\_school\\_mathematics} \\texttt{item\\_id} of 10.4\\% referenced in \\S\\ref{sec:format_conditional} is the lowest across all subjects, below even GSM8K (16.9\\%).\n\n\\begin{table}[h]\n\\centering\n\\caption{Subject-level variance decomposition within MMLU (20 items per subject, 8 models, 2,304 conditions per item). Sorted by $G_\\text{item}$ descending.}\n\\label{tab:subject_gstudy}\n\\scriptsize\n\\begin{tabular}{lrrrr}\n\\toprule\nSubject & Acc. & item\\% & mod.$\\times$it.\\% & $G_\\text{item}$ \\\\\n\\midrule\ninternational\\_law & .717 & 44.4 & 24.1 & .930 \\\\\nclinical\\_knowledge & .581 & 47.5 & 30.0 & .923 \\\\\nworld\\_religions & .826 & 42.2 & 27.1 & .910 \\\\\ncomputer\\_security & .740 & 37.0 & 24.9 & .908 \\\\\ncollege\\_physics & .436 & 31.6 & 30.1 & .876 \\\\\nphilosophy & .782 & 33.0 & 36.1 & .868 \\\\\nabstract\\_algebra & .457 & 24.1 & 32.8 & .822 \\\\\nus\\_foreign\\_policy & .864 & 20.4 & 36.9 & .802 \\\\\nprofessional\\_medicine & .671 & 19.9 & 41.7 & .778 \\\\\nhigh\\_school\\_math & .385 & 10.4 & 41.9 & .614 \\\\\n\\midrule\nMean & --- & 31.1 & 32.6 & .843 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{FF Residual Variance Analysis}\n\\label{app:ff_residual}\n\nTo investigate whether the elevated residual variance in free-form benchmarks (GSM8K 39.9\\%, MATH 43.9\\%) reflects unmodeled substantive sources or measurement properties of binary scoring, we regress item-level residual variance on item characteristics across all five benchmarks (Table~\\ref{tab:ff_residual}).\n\nThe dominant predictor is the quadratic difficulty effect ($p < 10^{-5}$ on all benchmarks): items near $p = 0.5$ show maximal residual variance, while items near the floor or ceiling show minimal residual. This inverted-U pattern directly mirrors the Bernoulli variance ceiling $p(1{-}p)$. Item content features (number of reasoning steps, answer length) are not significant predictors for GSM8K ($p > 0.38$), confirming that the difficulty--residual relationship is statistical rather than content-driven.\n\nFF benchmarks show substantially higher $R^2$ (mean 0.66) than MC benchmarks (mean 0.25), consistent with FF items spanning a wider difficulty range. The MC--FF contrast in residual magnitude is therefore a mathematical consequence of the difficulty distribution under binary scoring, not evidence of additional unmodeled variance sources in free-form evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-level residual variance regression. Difficulty$^2$ = quadratic (inverted-U) term reflecting the Bernoulli $p(1{-}p)$ ceiling. GSM8K additionally tests n\\_steps and answer\\_length (both $p > 0.38$).}\n\\label{tab:ff_residual}\n\\scriptsize\n\\begin{tabular}{lrrr}\n\\toprule\nBenchmark & $R^2$ (full) & $R^2$ (diff.\\ only) & Diff.$^2$ $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Multiple-choice}} \\\\\nMMLU & 0.377 & 0.347 & $<$0.001 \\\\\nARC & 0.221 & 0.204 & $<$0.001 \\\\\nHellaSwag & 0.156 & 0.140 & $<$0.001 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Free-form}} \\\\\nGSM8K & 0.468 & 0.449 & $<$0.001 \\\\\nMATH & 0.856 & 0.845 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Model and Prompt Details}\n\\label{app:models}\n\n\\paragraph{Models.} Table~\\ref{tab:model_ids} lists the eight models with their HuggingFace identifiers.\n\n\\begin{table}[h]\n\\centering\n\\caption{Models used in all experiments.}\n\\label{tab:model_ids}\n\\scriptsize\n\\begin{tabular}{llr}\n\\toprule\nShort name & HuggingFace identifier & Params \\\\\n\\midrule\nLlama-3.1-8B & \\texttt{meta-llama/Llama-3.1-8B-Instruct} & 8B \\\\\nGemma-2-9B & \\texttt{google/gemma-2-9b-it} & 9B \\\\\nMistral-7B-v0.3 & \\texttt{mistralai/Mistral-7B-Instruct-v0.3} & 7B \\\\\nQwen3-8B & \\texttt{Qwen/Qwen3-8B} & 8B \\\\\nYi-1.5-9B & \\texttt{01-ai/Yi-1.5-9B-Chat} & 9B \\\\\nOLMo-2-7B & \\texttt{allenai/OLMo-2-1124-7B-Instruct} & 7B \\\\\nInternLM2.5-7B & \\texttt{internlm/internlm2\\_5-7b-chat} & 7B \\\\\nDeepSeek-7B & \\texttt{deepseek-ai/deepseek-llm-7b-chat} & 7B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt templates.} Our six prompt templates follow a surface perturbation design inspired by BrittleBench \\cite{brittlebench2026}. For multiple-choice benchmarks, templates vary along three dimensions: option layout (lettered vs.\\ numbered), instruction wording (direct vs.\\ contextual), and answer prompt cue. For free-form benchmarks, templates vary chain-of-thought elicitation strategy. All six templates are semantically equivalent---they request the same task with different surface forms---to isolate formatting effects from content effects. ARC-Challenge and HellaSwag use the same six surface patterns as MMLU with domain-appropriate system instructions; MATH mirrors the GSM8K pattern with \\texttt{\\textbackslash boxed\\{\\}} answer formatting.\n\n\\smallskip\\noindent\\textit{MMLU templates (representative MC format):}\n\\begin{enumerate}\\setlength{\\itemsep}{0pt}\\setlength{\\parsep}{0pt}\\setlength{\\topsep}{0pt}\n\\item \\texttt{The following are multiple choice questions (with answers) about \\{subject\\}.\\textbackslash n\\textbackslash n\\{question\\}\\textbackslash nA. ... D. ...\\textbackslash nAnswer:}\n\\item \\texttt{Answer the following \\{subject\\} questions by selecting the correct option.\\textbackslash nQuestion: \\{question\\}\\textbackslash n(A) ... (B) ... (C) ... (D) ...\\textbackslash nCorrect answer:}\n\\item \\texttt{Below are \\{subject\\} multiple-choice problems. Pick the right letter.\\textbackslash nQ: \\{question\\}\\textbackslash n~~A) ... B) ... C) ... D) ...\\textbackslash nA:}\n\\item \\texttt{Answer the following \\{subject\\} question by selecting A, B, C, or D.\\textbackslash n\\{question\\}\\textbackslash n- A. ... - B. ... - C. ... - D. ...\\textbackslash nAnswer:}\n\\item \\texttt{Below is a \\{subject\\} exam question with four possible answers. Choose the correct one.\\textbackslash n\\{question\\}\\textbackslash nOption A: ... Option B: ... Option C: ... Option D: ...\\textbackslash nCorrect:}\n\\item \\texttt{Question (\\{subject\\}):\\textbackslash n\\{question\\}\\textbackslash nChoices: (A) ... (B) ... (C) ... (D) ...\\textbackslash nYour answer:}\n\\end{enumerate}\n\n\\smallskip\\noindent\\textit{GSM8K templates (representative FF format):}\n\\begin{enumerate}\\setlength{\\itemsep}{0pt}\\setlength{\\parsep}{0pt}\\setlength{\\topsep}{0pt}\n\\item \\texttt{Solve the following math problem step by step.\\textbackslash nQ: \\{question\\}\\textbackslash nA: Let's think step by step.}\n\\item \\texttt{Answer the following math word problem. Show your work.\\textbackslash nQuestion: \\{question\\}\\textbackslash nSolution:}\n\\item \\texttt{Solve each problem below. Write your reasoning, then give the final answer after \\#\\#\\#\\#.\\textbackslash nProblem: \\{question\\}\\textbackslash nReasoning:}\n\\item \\texttt{You are a math tutor. Solve the problem and show your steps.\\textbackslash n\\{question\\}\\textbackslash nSteps:}\n\\item \\texttt{Work through this math question carefully.\\textbackslash nQ: \\{question\\}\\textbackslash nWork:}\n\\item \\texttt{Math problem:\\textbackslash n\\{question\\}\\textbackslash nLet's solve this step by step.}\n\\end{enumerate}\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform related-work section.\n\\end{itemize}\n",
      "numLines": 308,
      "startLine": 1,
      "totalLines": 308
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_015MADzoJ1FXLQjUAA6dP49R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "7701344f-c006-4941-9f78-4dac0c51ad75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BmNeCV7EPG4cAsDHVfrr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17173,
      "cache_read_input_tokens": 42956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17173
      },
      "output_tokens": 34,
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

_source line 55 · 2026-05-23T19:07:36.065Z_

<details><summary>↩ Tool result · `toolu_015MADzoJ1FXLQjUAA6dP49R`</summary>

```text
1	% references.bib — auto-generated from literature_map.yaml (29 cited papers)
2	% Last synced: 2026-05-21
3	
4	% ====== G-Theory & Evaluation Variance ======
5	
6	@article{messing2026hidden,
7	  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
8	  author={Messing, Solomon},
9	  year={2026},
10	  journal={arXiv preprint arXiv:2604.11581},
11	  url={https://arxiv.org/abs/2604.11581}
12	}
13	
14	@article{song2025gtheory,
15	  title={Exploring {LLM} Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory},
16	  author={Song, Dan and Lee, Won-Chan and Jiao, Hong},
17	  year={2025},
18	  journal={arXiv preprint arXiv:2507.19980},
19	  url={https://arxiv.org/abs/2507.19980}
20	}
21	
22	@article{madaan2024quantifying,
23	  title={Quantifying Variance in Evaluation Benchmarks},
24	  author={Madaan, Lovish and Bhatia, Samarth and Tulio Ribeiro, Marco and Roth, Dan},
25	  year={2024},
26	  journal={arXiv preprint arXiv:2406.10229},
27	  url={https://arxiv.org/abs/2406.10229}
28	}
29	
30	@inproceedings{bouthillier2021accounting,
31	  title={Accounting for Variance in Machine Learning Benchmarks},
32	  author={Bouthillier, Xavier and Delaunay, Pierre and Bronzi, Mirko and Trofimov, Assya and Nichyporuk, Brennan and Szeto, Justin and Sepahvand, Nazanin Mohammadi and Raff, Edward and Madan, Kshitij and Voleti, Vikram and Kahou, Samira Ebrahimi and Michalski, Vincent and Arbel, Tal and Pal, Chris and Varoquaux, Ga{\"e}l and Vincent, Pascal},
33	  booktitle={Proceedings of Machine Learning and Systems (MLSys)},
34	  year={2021},
35	  url={https://arxiv.org/abs/2103.03098}
36	}
37	
38	@book{shavelson1991generalizability,
39	  title={Generalizability Theory: A Primer},
40	  author={Shavelson, Richard J. and Webb, Noreen M.},
41	  year={1991},
42	  publisher={SAGE Publications},
43	  isbn={978-0-8039-3744-4}
44	}
45	
46	@book{brennan2001generalizability,
47	  title={Generalizability Theory},
48	  author={Brennan, Robert L.},
49	  year={2001},
50	  publisher={Springer},
51	  isbn={978-0-387-95282-6}
52	}
53	
54	@article{kunievsky2025intent,
55	  title={Measuring Intent Comprehension in {LLM}s: A Variance Decomposition Framework},
56	  author={Kunievsky, Nitzan and Evans, James A.},
57	  year={2025},
58	  journal={arXiv preprint arXiv:2506.16584},
59	  url={https://arxiv.org/abs/2506.16584}
60	}
61	
62	% ====== Infrastructure Variance ======
63	
64	@inproceedings{yuan2025layercast,
65	  title={Understanding and Mitigating Numerical Sources of Nondeterminism in {LLM} Inference},
66	  author={Yuan, Juntao and Li, Haoyang and Ding, Xingcheng and Xie, Weijie and Li, Yue-Jiao and Zhao, Wentao and Wan, Kaiyan and Shi, Jiayi and Hu, Xiaolu and Liu, Zhouhan},
67	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
68	  year={2025},
69	  note={Oral presentation},
70	  url={https://arxiv.org/abs/2506.09501}
71	}
72	
73	@article{messina2026background,
74	  title={Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models},
75	  author={Messina, Alberto and Scotta, Sara},
76	  year={2026},
77	  journal={arXiv preprint arXiv:2604.22411},
78	  url={https://arxiv.org/abs/2604.22411}
79	}
80	
81	@misc{thinkingmachines2025batch,
82	  title={Defeating Nondeterminism in {LLM} Inference},
83	  author={He, Haiyang and {Thinking Machines Lab}},
84	  year={2025},
85	  howpublished={Thinking Machines Lab: Connectionism},
86	  doi={10.64434/tml.20250910},
87	  url={https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/}
88	}
89	
90	@inproceedings{shanmugavelu2024floating,
91	  title={Impacts of Floating-Point Non-Associativity on Reproducibility for {HPC} and Deep Learning Applications},
92	  author={Shanmugavelu, Sanjif and Taillefumier, Mathieu and Culver, Christopher and Hernandez, Oscar and Coletti, Mark and Sedova, Ada},
93	  booktitle={SC'24 Workshops (IEEE)},
94	  year={2024},
95	  doi={10.1109/SCW63240.2024.00028},
96	  url={https://arxiv.org/abs/2408.05148}
97	}
98	
99	% ====== Prompt Sensitivity & Methodology ======
100	
101	@article{brittlebench2026,
102	  title={Brittlebench: Quantifying {LLM} Robustness via Prompt Sensitivity},
103	  author={Romanou, Angelika and Ibrahim, Marah and Ross, Candace and Shaib, Chantal and Oktar, Kerem and Bell, Samuel J. and Ovalle, Anaelia and Dodge, Jesse and Bosselut, Antoine and Sinha, Koustuv and Williams, Adina},
104	  year={2026},
105	  journal={arXiv preprint arXiv:2603.13285},
106	  url={https://arxiv.org/abs/2603.13285}
107	}
108	
109	@inproceedings{sclar2024formatting,
110	  title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How {I} Learned to Start Worrying About Prompt Formatting},
111	  author={Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
112	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
113	  year={2024},
114	  url={https://arxiv.org/abs/2310.11324}
115	}
116	
117	@inproceedings{pezeshkpour2024ordering,
118	  title={Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions},
119	  author={Pezeshkpour, Pouya and Hruschka, Estevam},
120	  booktitle={Findings of the North American Chapter of the Association for Computational Linguistics (NAACL)},
121	  year={2024},
122	  url={https://aclanthology.org/2024.findings-naacl.130/}
123	}
124	
125	@inproceedings{hua2025flaw,
126	  title={Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating {LLM}s},
127	  author={Hua, Angie and Tang, Kevin and Gu, Chaoqun and Gu, Jing and Wong, Edmund and Qin, Yilin},
128	  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
129	  year={2025},
130	  url={https://aclanthology.org/2025.emnlp-main.1006/}
131	}
132	
133	@inproceedings{bui2025seeds,
134	  title={Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models},
135	  author={Bui, Ngoc Thang and Savova, Guergana and Wang, Lijun},
136	  booktitle={Proceedings of IJCNLP-AACL},
137	  year={2025},
138	  url={https://aclanthology.org/2025.ijcnlp-short.3/}
139	}
140	
141	% ====== IRT & Efficient Benchmarking ======
142	
143	@inproceedings{polo2024tinybenchmarks,
144	  title={{tinyBenchmarks}: Evaluating {LLM}s with Fewer Examples},
145	  author={Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
146	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
147	  year={2024},
148	  url={https://arxiv.org/abs/2402.14992}
149	}
150	
151	@inproceedings{lalor2019irt,
152	  title={Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},
153	  author={Lalor, John P. and Wu, Hao and Yu, Hong},
154	  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing and International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
155	  year={2019},
156	  url={https://aclanthology.org/D19-1434/}
157	}
158	
159	@inproceedings{rodriguez2021leaderboards,
160	  title={Evaluation Examples are not Equally Informative: How should that change {NLP} Leaderboards?},
161	  author={Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},
162	  booktitle={Proceedings of the Association for Computational Linguistics (ACL)},
163	  year={2021},
164	  url={https://aclanthology.org/2021.acl-long.346/}
165	}
166	
167	@article{perlitz2023efficient,
168	  title={Efficient Benchmarking of Language Models},
169	  author={Perlitz, Yotam and Bandel, Elron and Gera, Ariel and Arviv, Ofir and Ein-Dor, Liat and Shnarch, Eyal and Slonim, Noam and Shmueli-Scheuer, Michal and Choshen, Leshem},
170	  year={2023},
171	  journal={arXiv preprint arXiv:2308.11696},
172	  url={https://arxiv.org/abs/2308.11696}
173	}
174	
175	@inproceedings{zhou2026irt,
176	  title={Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
177	  author={Zhou, Hao and Huang, Huifeng and Zhao, Zhe and Han, Long and Wang, Haobo and Chen, Ke and Yang, Min and Bao, Wanli and Dong, Jiaxin and Xu, Bo and Zhu, Conghui and Cao, Hao and Zhao, Tiejun},
178	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
179	  year={2026},
180	  note={Oral presentation},
181	  url={https://arxiv.org/abs/2505.15055}
182	}
183	
184	@inproceedings{kipnis2025metabench,
185	  title={metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},
186	  author={Kipnis, Alex and Voudouris, Konstantinos and Schulze Buschoff, Luca and Schulz, Eric},
187	  booktitle={Proceedings of the International Conference on Learning Representations},
188	  year={2025},
189	  url={https://arxiv.org/abs/2407.12844}
190	}
191	
192	@article{li2025atlas,
193	  title={Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
194	  author={Li, Peiyu and Tang, Xiuxiu and Chen, Si and Cheng, Ying and Metoyer, Ronald and Hua, Ting and Chawla, Nitesh V.},
195	  journal={arXiv preprint arXiv:2511.04689},
196	  year={2025},
197	  url={https://arxiv.org/abs/2511.04689}
198	}
199	
200	% ====== Reproducibility & Evaluation Design ======
201	
202	@inproceedings{henderson2018deep,
203	  title={Deep Reinforcement Learning that Matters},
204	  author={Henderson, Peter and Islam, Riashat and Bachman, Philip and Pineau, Joelle and Precup, Doina and Meger, David},
205	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
206	  year={2018},
207	  url={https://arxiv.org/abs/1709.06560}
208	}
209	
210	@article{dodge2020finetuning,
211	  title={Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping},
212	  author={Dodge, Jesse and Ilharco, Gabriel and Schwartz, Roy and Farhadi, Ali and Hajishirzi, Hannaneh and Smith, Noah A.},
213	  year={2020},
214	  journal={arXiv preprint arXiv:2002.06305},
215	  url={https://arxiv.org/abs/2002.06305}
216	}
217	
218	@article{biderman2024lessons,
219	  title={Lessons from the Trenches on Reproducible Evaluation of Language Models},
220	  author={Biderman, Stella and Schoelkopf, Hailey and Sutawika, Lintang and Gao, Leo and Tow, Jonathan and Abbasi, Baber and Aji, Alham Fikri and Ammanamanchi, Pawan Sasanka and Black, Sidney and Clive, Jordan and DiPofi, Anthony and Etxaniz, Julen and Fattori, Benjamin and Forde, Jessica Zosa and Foster, Charles and Hsu, Jeffrey and Jaiswal, Mimansa and Lee, Won Ik and Li, Haonan and Lovering, Charles and Muennighoff, Niklas and Pavlick, Ellie and Phang, Jason and Skowron, Aviya and Tan, Samson and Tang, Xiangru and Wang, Kevin A. and Winata, Genta Indra and Yvon, Fran{\c{c}}ois and Zou, Andy},
221	  year={2024},
222	  journal={arXiv preprint arXiv:2405.14782},
223	  url={https://arxiv.org/abs/2405.14782}
224	}
225	
226	@article{dehghani2021benchmark,
227	  title={The Benchmark Lottery},
228	  author={Dehghani, Mostafa and Tay, Yi and Gritsenko, Alexey A. and Zhao, Zhe and Houlsby, Neil and Diaz, Fernando and Metzler, Donald and Vinyals, Oriol},
229	  year={2021},
230	  journal={arXiv preprint arXiv:2107.07002},
231	  url={https://arxiv.org/abs/2107.07002}
232	}
233	
234	@inproceedings{magnusson2023reproducibility,
235	  title={Reproducibility in {NLP}: What Have We Learned from the Checklist?},
236	  author={Magnusson, Ian and Smith, Noah A. and Dodge, Jesse},
237	  booktitle={Findings of the Association for Computational Linguistics (ACL)},
238	  year={2023},
239	  url={https://aclanthology.org/2023.findings-acl.809/}
240	}
241	
242	% ====== Binary Data & Psychometrics ======
243	
244	@article{jiang2018bayesian,
245	  title={A {Bayesian} Approach to Estimating Variance Components within a Multivariate Generalizability Theory Framework},
246	  author={Jiang, Zhehan and Skorupski, William},
247	  year={2018},
248	  journal={Behavior Research Methods},
249	  volume={50},
250	  doi={10.3758/s13428-017-0986-3},
251	  url={https://link.springer.com/article/10.3758/s13428-017-0986-3}
252	}
253	
254	@article{mushquash2006gtheory,
255	  title={{SPSS} and {SAS} Programs for Generalizability Theory Analyses},
256	  author={Mushquash, Cilia and O'Connor, Brian P.},
257	  year={2006},
258	  journal={Behavior Research Methods},
259	  doi={10.3758/BF03192810},
260	  url={https://link.springer.com/article/10.3758/BF03192810}
261	}
262	
263	@article{shavelson1989gtheory,
264	  title={Generalizability Theory},
265	  author={Shavelson, Richard J. and Webb, Noreen M. and Rowley, Glenn L.},
266	  year={1989},
267	  journal={American Psychologist},
268	  url={https://psycnet.apa.org/record/1989-34789-001}
269	}
270	
271	@article{li2023bootstrap,
272	  title={Which Method Is Optimal for Estimating Variance Components and Their Variability in Generalizability Theory? {Evidence} from a Set of Unified Rules for Bootstrap Method},
273	  author={Li, Guangming},
274	  year={2023},
275	  journal={PLoS ONE},
276	  doi={10.1371/journal.pone.0288069},
277	  url={https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0288069}
278	}
279	
280	@article{tuerlinckx2006glmm,
281	  title={Statistical Inference in Generalized Linear Mixed Models: A Review},
282	  author={Tuerlinckx, Francis and Rijmen, Frank and Verbeke, Geert and De Boeck, Paul},
283	  year={2006},
284	  journal={British Journal of Mathematical and Statistical Psychology},
285	  doi={10.1348/000711005X79857},
286	  url={https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1348/000711005X79857}
287	}
288	
289	% ====== Evaluation Uncertainty & Meta-Evaluation ======
290	
291	@article{blackwell2024towards,
292	  title={Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores},
293	  author={Blackwell, Robert E. and Barry, Jon and Cohn, Anthony G.},
294	  journal={arXiv preprint arXiv:2410.03492},
295	  year={2024},
296	  url={https://arxiv.org/abs/2410.03492}
297	}
298	
299	@article{qian2026benchmark,
300	  title={Benchmark$^2$: Systematic Evaluation of LLM Benchmarks},
301	  author={Qian, Qi and Huang, Chengsong and Xu, Jingwen and others},
302	  journal={arXiv preprint arXiv:2601.03986},
303	  year={2026}
304	}
305	
306	@article{burnell2023rethink,
307	  title={Rethink reporting of evaluation results in {AI}},
308	  author={Burnell, Ryan and Schellaert, Wout and Burden, John and others},
309	  journal={Science},
310	  volume={380},
311	  number={6641},
312	  pages={136--138},
313	  year={2023},
314	  doi={10.1126/science.adf6369}
315	}
316	
317	% ====== Additional References (Post-Review) ======
318	
319	@article{varannot2026gtheory,
320	  title={Variance-Aware {LLM} Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement},
321	  author={Camuffo, Arnaldo and Gambardella, Alfonso and Kazemi, Saeid and Malachowski, Jakub and Pandey, Abhinav},
322	  year={2026},
323	  journal={arXiv preprint arXiv:2601.02370},
324	  url={https://arxiv.org/abs/2601.02370}
325	}
326	
327	@article{kearns2026construct,
328	  title={Quantifying Construct Validity in Large Language Model Evaluations},
329	  author={Kearns, Ryan Othniel},
330	  year={2026},
331	  journal={arXiv preprint arXiv:2602.15532},
332	  url={https://arxiv.org/abs/2602.15532}
333	}
334	
335	@article{ye2025psychometrics,
336	  title={Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement},
337	  author={Ye, Haoran and Jin, Jing and Xie, Yuhang and Zhang, Xin and Song, Guojie},
338	  year={2025},
339	  journal={arXiv preprint arXiv:2505.08245},
340	  url={https://arxiv.org/abs/2505.08245}
341	}
342	
343	% ====== Round 5 additions (SF-7) ======
344	
345	@book{holland1993dif,
346	  title     = {Differential Item Functioning},
347	  editor    = {Holland, Paul W. and Wainer, Howard},
348	  year      = {1993},
349	  publisher = {Lawrence Erlbaum Associates},
350	  address   = {Hillsdale, NJ},
351	  isbn      = {0805809724}
352	}
353	
354	@article{clauser1998dif,
355	  author  = {Clauser, Brian E. and Mazor, Kathleen M.},
356	  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},
357	  journal = {Educational Measurement: Issues and Practice},
358	  year    = {1998},
359	  volume  = {17},
360	  number  = {1},
361	  pages   = {31--44},
362	  doi     = {10.1111/j.1745-3992.1998.tb00619.x}
363	}
364	
365	@incollection{webb2006reliability,
366	  author    = {Webb, Noreen M. and Shavelson, Richard J. and Haertel, Edward H.},
367	  title     = {Reliability Coefficients and Generalizability Theory},
368	  booktitle = {Handbook of Statistics},
369	  series    = {Handbook of Statistics},
370	  volume    = {26},
371	  editor    = {Rao, C. R. and Sinharay, Sandip},
372	  publisher = {Elsevier},
373	  year      = {2006},
374	  pages     = {81--124},
375	  doi       = {10.1016/S0169-7161(06)26004-8}
376	}
377	
378	@article{zhu2026benchmark,
379	  author  = {Zhu, Longyuan and Hua, Hairan and Miao, Linlin and Zhao, Bing},
380	  title   = {Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of {LLM}s},
381	  journal = {arXiv preprint arXiv:2602.11674},
382	  year    = {2026},
383	  url     = {https://arxiv.org/abs/2602.11674}
384	}
385	
386	@inproceedings{bean2025measuring,
387	  author    = {Bean, Andrew M. and Kearns, Ryan Othniel and Romanou, Angelika and Hafner, Franziska Sofia and Mayne, Harry and Batzner, Jan and Foroutan, Negar and Schmitz, Chris and Korgul, Karolina and Batra, Hunar and Deb, Oishi and Beharry, Emma and Emde, Cornelius and Foster, Thomas and Gausen, Anna and Grandury, Mar{\'\i}a and Han, Simeng and Hofmann, Valentin and Ibrahim, Lujain and Kim, Hazel and Kirk, Hannah Rose and Lin, Fangru and Liu, Gabrielle Kaili-May and Luettgau, Lennart and Magomere, Jabez and Rystr{\o}m, Jonathan and Sotnikova, Anna and Yang, Yushi and Zhao, Yilun and Bibi, Adel and Bosselut, Antoine and Clark, Ronald and Cohan, Arman and Foerster, Jakob and Gal, Yarin and Hale, Scott A. and Raji, Inioluwa Deborah and Summerfield, Christopher and Torr, Philip H. S. and Ududec, Cozmin and Rocher, Luc and Mahdi, Adam},
388	  title     = {Measuring What Matters: Construct Validity in Large Language Model Benchmarks},
389	  booktitle = {Advances in Neural Information Processing Systems 38 ({NeurIPS} 2025), Datasets and Benchmarks Track},
390	  year      = {2025},
391	  url       = {https://arxiv.org/abs/2511.04703}
392	}
393	
394	@article{freiesleben2026construct,
395	  author  = {Freiesleben, Timo},
396	  title   = {Establishing Construct Validity in {LLM} Capability Benchmarks Requires Nomological Networks},
397	  journal = {arXiv preprint arXiv:2603.15121},
398	  year    = {2026},
399	  url     = {https://arxiv.org/abs/2603.15121}
400	}
401	
402	% ====== Round 8 additions ======
403	
404	@article{golchin2023contamination,
405	  title={Time Travel in {LLM}s: Tracing Data Contamination in Large Language Models},
406	  author={Golchin, Shahriar and Surdeanu, Mihai},
407	  journal={arXiv preprint arXiv:2308.08493},
408	  year={2023},
409	  url={https://arxiv.org/abs/2308.08493}
410	}
411	
412	% ====== Round 6 additions ======
413	
414	@article{mizrahi2024state,
415	  title     = {State of What Art? {A} Call for Multi-Prompt {LLM} Evaluation},
416	  author    = {Mizrahi, Moran and Kaplan, Guy and Malkin, Dan and Dror, Rotem and Shahaf, Dafna and Stanovsky, Gabriel},
417	  journal   = {Transactions of the Association for Computational Linguistics},
418	  volume    = {12},
419	  pages     = {933--949},
420	  year      = {2024},
421	  publisher = {MIT Press},
422	  doi       = {10.1162/tacl_a_00681}
423	}
424	
425	@article{liang2023helm,
426	  title     = {Holistic Evaluation of Language Models},
427	  author    = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and others},
428	  journal   = {arXiv preprint arXiv:2211.09110},
429	  year      = {2023}
430	}
431	
432	@article{meredith1993measurement,
433	  title     = {Measurement Invariance, Factor Analysis and Factorial Invariance},
434	  author    = {Meredith, William},
435	  journal   = {Psychometrika},
436	  volume    = {58},
437	  number    = {4},
438	  pages     = {525--543},
439	  year      = {1993},
440	  publisher = {Springer},
441	  doi       = {10.1007/BF02294825}
442	}
443	
444	@article{putnick2016measurement,
445	  title     = {Measurement Invariance Conventions and Reporting: {The} State of the Art and Future Directions for Psychological Research},
446	  author    = {Putnick, Diane L. and Bornstein, Marc H.},
447	  journal   = {Developmental Review},
448	  volume    = {41},
449	  pages     = {71--90},
450	  year      = {2016},
451	  publisher = {Elsevier},
452	  doi       = {10.1016/j.dr.2016.06.004}
453	}
454	
455	@book{efron1993bootstrap,
456	  title     = {An Introduction to the Bootstrap},
457	  author    = {Efron, Bradley and Tibshirani, Robert J.},
458	  year      = {1993},
459	  publisher = {Chapman \& Hall},
460	  address   = {New York}
461	}
462	
463	@book{cardinet2010applying,
464	  title     = {Applying Generalizability Theory Using {EduG}},
465	  author    = {Cardinet, Jean and Johnson, Sandra and Pini, Gianreto},
466	  year      = {2010},
467	  publisher = {Routledge}
468	}
469	
470	@inproceedings{kiela2021dynabench,
471	  title     = {Dynabench: Rethinking Benchmarking in {NLP}},
472	  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Waseem, Zeerak and Stenetorp, Pontus and Jia, Robin and Bansal, Mohit and Potts, Christopher and Williams, Adina},
473	  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
474	  year      = {2021}
475	}
476	
477	% ====== Round 9 additions ======
478	
479	@inproceedings{saxon2024metrology,
480	  title     = {Benchmarks as Microscopes: A Call for Model Metrology},
481	  author    = {Saxon, Michael and Holtzman, Ari and West, Peter and Wang, William Yang and Saphra, Naomi},
482	  booktitle = {Proceedings of the Conference on Language Modeling (COLM)},
483	  year      = {2024},
484	  url       = {https://arxiv.org/abs/2407.16711}
485	}
486	
487	@inproceedings{alzahrani2024benchmarks,
488	  title     = {When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards},
489	  author    = {Alzahrani, Norah and Alyahya, Hisham Abdullah and Alnumay, Yazeed and Alrashed, Sultan and Alsubaie, Shaykhah and Almushaykeh, Yusef and Mirza, Faisal and Alotaibi, Nouf and Altwairesh, Nora and Alowisheq, Areeb and Bari, M Saiful and Khan, Haidar},
490	  booktitle = {Proceedings of the Association for Computational Linguistics (ACL)},
491	  year      = {2024},
492	  pages     = {13787--13805},
493	  url       = {https://arxiv.org/abs/2402.01781}
494	}
495	
496	@misc{gao2024lmeval,
497	  title     = {A Framework for Few-Shot Language Model Evaluation},
498	  author    = {Gao, Leo and Tow, Jonathan and Abbasi, Baber and Biderman, Stella and Black, Sid and DiPofi, Anthony and Foster, Charles and Golber, Laurence and Hsu, Jeffrey and Le Noac'h, Alain and Li, Haonan and McDonell, Kyle and Muennighoff, Niklas and Ocqueteau, Chris and Phang, Jason and Reynolds, Laria and Schoelkopf, Hailey and Skowron, Aviya and Sutawika, Lintang and Tang, Eric and Thite, Anish and Wang, Ben and Wang, Kevin and Zou, Andy},
499	  year      = {2024},
500	  publisher = {Zenodo},
501	  doi       = {10.5281/zenodo.10256836},
502	  url       = {https://github.com/EleutherAI/lm-evaluation-harness}
503	}
504	
505	@inproceedings{gema2025mmlu,
506	  title     = {Are We Done with {MMLU}?},
507	  author    = {Gema, Aryo Pradipta and Leang, Joshua Ong Jun and Hong, Giwon and Devoto, Alessio and Mancino, Alberto Carlo Maria and Saxena, Rohit and He, Xuanli and Zhao, Yu and Du, Xiaotang and Ghasemi Madani, Mohammad Reza and Barale, Claire and McHardy, Robert and Harris, Joshua and Kaddour, Jean and Van Krieken, Emile and Minervini, Pasquale},
508	  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
509	  year      = {2025},
510	  doi       = {10.18653/v1/2025.naacl-long.262},
511	  url       = {https://arxiv.org/abs/2406.04127}
512	}
513	
514	@inproceedings{wang2024mmlupro,
515	  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
516	  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Yue, Xiang and Chen, Wenhu},
517	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},
518	  year      = {2024},
519	  url       = {https://arxiv.org/abs/2406.01574}
520	}
521	
522	@inproceedings{oren2024proving,
523	  title     = {Proving Test Set Contamination in Black Box Language Models},
524	  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Ladhak, Faisal and Hashimoto, Tatsunori B.},
525	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
526	  year      = {2024},
527	  note      = {Outstanding Paper Honorable Mention},
528	  url       = {https://arxiv.org/abs/2310.17623}
529	}
530	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "d03d28fb-1ea5-41a9-a44c-1f82a67173bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib",
      "content": "% references.bib — auto-generated from literature_map.yaml (29 cited papers)\n% Last synced: 2026-05-21\n\n% ====== G-Theory & Evaluation Variance ======\n\n@article{messing2026hidden,\n  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},\n  author={Messing, Solomon},\n  year={2026},\n  journal={arXiv preprint arXiv:2604.11581},\n  url={https://arxiv.org/abs/2604.11581}\n}\n\n@article{song2025gtheory,\n  title={Exploring {LLM} Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory},\n  author={Song, Dan and Lee, Won-Chan and Jiao, Hong},\n  year={2025},\n  journal={arXiv preprint arXiv:2507.19980},\n  url={https://arxiv.org/abs/2507.19980}\n}\n\n@article{madaan2024quantifying,\n  title={Quantifying Variance in Evaluation Benchmarks},\n  author={Madaan, Lovish and Bhatia, Samarth and Tulio Ribeiro, Marco and Roth, Dan},\n  year={2024},\n  journal={arXiv preprint arXiv:2406.10229},\n  url={https://arxiv.org/abs/2406.10229}\n}\n\n@inproceedings{bouthillier2021accounting,\n  title={Accounting for Variance in Machine Learning Benchmarks},\n  author={Bouthillier, Xavier and Delaunay, Pierre and Bronzi, Mirko and Trofimov, Assya and Nichyporuk, Brennan and Szeto, Justin and Sepahvand, Nazanin Mohammadi and Raff, Edward and Madan, Kshitij and Voleti, Vikram and Kahou, Samira Ebrahimi and Michalski, Vincent and Arbel, Tal and Pal, Chris and Varoquaux, Ga{\\\"e}l and Vincent, Pascal},\n  booktitle={Proceedings of Machine Learning and Systems (MLSys)},\n  year={2021},\n  url={https://arxiv.org/abs/2103.03098}\n}\n\n@book{shavelson1991generalizability,\n  title={Generalizability Theory: A Primer},\n  author={Shavelson, Richard J. and Webb, Noreen M.},\n  year={1991},\n  publisher={SAGE Publications},\n  isbn={978-0-8039-3744-4}\n}\n\n@book{brennan2001generalizability,\n  title={Generalizability Theory},\n  author={Brennan, Robert L.},\n  year={2001},\n  publisher={Springer},\n  isbn={978-0-387-95282-6}\n}\n\n@article{kunievsky2025intent,\n  title={Measuring Intent Comprehension in {LLM}s: A Variance Decomposition Framework},\n  author={Kunievsky, Nitzan and Evans, James A.},\n  year={2025},\n  journal={arXiv preprint arXiv:2506.16584},\n  url={https://arxiv.org/abs/2506.16584}\n}\n\n% ====== Infrastructure Variance ======\n\n@inproceedings{yuan2025layercast,\n  title={Understanding and Mitigating Numerical Sources of Nondeterminism in {LLM} Inference},\n  author={Yuan, Juntao and Li, Haoyang and Ding, Xingcheng and Xie, Weijie and Li, Yue-Jiao and Zhao, Wentao and Wan, Kaiyan and Shi, Jiayi and Hu, Xiaolu and Liu, Zhouhan},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  note={Oral presentation},\n  url={https://arxiv.org/abs/2506.09501}\n}\n\n@article{messina2026background,\n  title={Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models},\n  author={Messina, Alberto and Scotta, Sara},\n  year={2026},\n  journal={arXiv preprint arXiv:2604.22411},\n  url={https://arxiv.org/abs/2604.22411}\n}\n\n@misc{thinkingmachines2025batch,\n  title={Defeating Nondeterminism in {LLM} Inference},\n  author={He, Haiyang and {Thinking Machines Lab}},\n  year={2025},\n  howpublished={Thinking Machines Lab: Connectionism},\n  doi={10.64434/tml.20250910},\n  url={https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/}\n}\n\n@inproceedings{shanmugavelu2024floating,\n  title={Impacts of Floating-Point Non-Associativity on Reproducibility for {HPC} and Deep Learning Applications},\n  author={Shanmugavelu, Sanjif and Taillefumier, Mathieu and Culver, Christopher and Hernandez, Oscar and Coletti, Mark and Sedova, Ada},\n  booktitle={SC'24 Workshops (IEEE)},\n  year={2024},\n  doi={10.1109/SCW63240.2024.00028},\n  url={https://arxiv.org/abs/2408.05148}\n}\n\n% ====== Prompt Sensitivity & Methodology ======\n\n@article{brittlebench2026,\n  title={Brittlebench: Quantifying {LLM} Robustness via Prompt Sensitivity},\n  author={Romanou, Angelika and Ibrahim, Marah and Ross, Candace and Shaib, Chantal and Oktar, Kerem and Bell, Samuel J. and Ovalle, Anaelia and Dodge, Jesse and Bosselut, Antoine and Sinha, Koustuv and Williams, Adina},\n  year={2026},\n  journal={arXiv preprint arXiv:2603.13285},\n  url={https://arxiv.org/abs/2603.13285}\n}\n\n@inproceedings{sclar2024formatting,\n  title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How {I} Learned to Start Worrying About Prompt Formatting},\n  author={Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.11324}\n}\n\n@inproceedings{pezeshkpour2024ordering,\n  title={Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions},\n  author={Pezeshkpour, Pouya and Hruschka, Estevam},\n  booktitle={Findings of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-naacl.130/}\n}\n\n@inproceedings{hua2025flaw,\n  title={Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating {LLM}s},\n  author={Hua, Angie and Tang, Kevin and Gu, Chaoqun and Gu, Jing and Wong, Edmund and Qin, Yilin},\n  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2025},\n  url={https://aclanthology.org/2025.emnlp-main.1006/}\n}\n\n@inproceedings{bui2025seeds,\n  title={Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models},\n  author={Bui, Ngoc Thang and Savova, Guergana and Wang, Lijun},\n  booktitle={Proceedings of IJCNLP-AACL},\n  year={2025},\n  url={https://aclanthology.org/2025.ijcnlp-short.3/}\n}\n\n% ====== IRT & Efficient Benchmarking ======\n\n@inproceedings{polo2024tinybenchmarks,\n  title={{tinyBenchmarks}: Evaluating {LLM}s with Fewer Examples},\n  author={Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2402.14992}\n}\n\n@inproceedings{lalor2019irt,\n  title={Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds},\n  author={Lalor, John P. and Wu, Hao and Yu, Hong},\n  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing and International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year={2019},\n  url={https://aclanthology.org/D19-1434/}\n}\n\n@inproceedings{rodriguez2021leaderboards,\n  title={Evaluation Examples are not Equally Informative: How should that change {NLP} Leaderboards?},\n  author={Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},\n  booktitle={Proceedings of the Association for Computational Linguistics (ACL)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.346/}\n}\n\n@article{perlitz2023efficient,\n  title={Efficient Benchmarking of Language Models},\n  author={Perlitz, Yotam and Bandel, Elron and Gera, Ariel and Arviv, Ofir and Ein-Dor, Liat and Shnarch, Eyal and Slonim, Noam and Shmueli-Scheuer, Michal and Choshen, Leshem},\n  year={2023},\n  journal={arXiv preprint arXiv:2308.11696},\n  url={https://arxiv.org/abs/2308.11696}\n}\n\n@inproceedings{zhou2026irt,\n  title={Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  author={Zhou, Hao and Huang, Huifeng and Zhao, Zhe and Han, Long and Wang, Haobo and Chen, Ke and Yang, Min and Bao, Wanli and Dong, Jiaxin and Xu, Bo and Zhu, Conghui and Cao, Hao and Zhao, Tiejun},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},\n  year={2026},\n  note={Oral presentation},\n  url={https://arxiv.org/abs/2505.15055}\n}\n\n@inproceedings{kipnis2025metabench,\n  title={metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models},\n  author={Kipnis, Alex and Voudouris, Konstantinos and Schulze Buschoff, Luca and Schulz, Eric},\n  booktitle={Proceedings of the International Conference on Learning Representations},\n  year={2025},\n  url={https://arxiv.org/abs/2407.12844}\n}\n\n@article{li2025atlas,\n  title={Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  author={Li, Peiyu and Tang, Xiuxiu and Chen, Si and Cheng, Ying and Metoyer, Ronald and Hua, Ting and Chawla, Nitesh V.},\n  journal={arXiv preprint arXiv:2511.04689},\n  year={2025},\n  url={https://arxiv.org/abs/2511.04689}\n}\n\n% ====== Reproducibility & Evaluation Design ======\n\n@inproceedings{henderson2018deep,\n  title={Deep Reinforcement Learning that Matters},\n  author={Henderson, Peter and Islam, Riashat and Bachman, Philip and Pineau, Joelle and Precup, Doina and Meger, David},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},\n  year={2018},\n  url={https://arxiv.org/abs/1709.06560}\n}\n\n@article{dodge2020finetuning,\n  title={Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping},\n  author={Dodge, Jesse and Ilharco, Gabriel and Schwartz, Roy and Farhadi, Ali and Hajishirzi, Hannaneh and Smith, Noah A.},\n  year={2020},\n  journal={arXiv preprint arXiv:2002.06305},\n  url={https://arxiv.org/abs/2002.06305}\n}\n\n@article{biderman2024lessons,\n  title={Lessons from the Trenches on Reproducible Evaluation of Language Models},\n  author={Biderman, Stella and Schoelkopf, Hailey and Sutawika, Lintang and Gao, Leo and Tow, Jonathan and Abbasi, Baber and Aji, Alham Fikri and Ammanamanchi, Pawan Sasanka and Black, Sidney and Clive, Jordan and DiPofi, Anthony and Etxaniz, Julen and Fattori, Benjamin and Forde, Jessica Zosa and Foster, Charles and Hsu, Jeffrey and Jaiswal, Mimansa and Lee, Won Ik and Li, Haonan and Lovering, Charles and Muennighoff, Niklas and Pavlick, Ellie and Phang, Jason and Skowron, Aviya and Tan, Samson and Tang, Xiangru and Wang, Kevin A. and Winata, Genta Indra and Yvon, Fran{\\c{c}}ois and Zou, Andy},\n  year={2024},\n  journal={arXiv preprint arXiv:2405.14782},\n  url={https://arxiv.org/abs/2405.14782}\n}\n\n@article{dehghani2021benchmark,\n  title={The Benchmark Lottery},\n  author={Dehghani, Mostafa and Tay, Yi and Gritsenko, Alexey A. and Zhao, Zhe and Houlsby, Neil and Diaz, Fernando and Metzler, Donald and Vinyals, Oriol},\n  year={2021},\n  journal={arXiv preprint arXiv:2107.07002},\n  url={https://arxiv.org/abs/2107.07002}\n}\n\n@inproceedings{magnusson2023reproducibility,\n  title={Reproducibility in {NLP}: What Have We Learned from the Checklist?},\n  author={Magnusson, Ian and Smith, Noah A. and Dodge, Jesse},\n  booktitle={Findings of the Association for Computational Linguistics (ACL)},\n  year={2023},\n  url={https://aclanthology.org/2023.findings-acl.809/}\n}\n\n% ====== Binary Data & Psychometrics ======\n\n@article{jiang2018bayesian,\n  title={A {Bayesian} Approach to Estimating Variance Components within a Multivariate Generalizability Theory Framework},\n  author={Jiang, Zhehan and Skorupski, William},\n  year={2018},\n  journal={Behavior Research Methods},\n  volume={50},\n  doi={10.3758/s13428-017-0986-3},\n  url={https://link.springer.com/article/10.3758/s13428-017-0986-3}\n}\n\n@article{mushquash2006gtheory,\n  title={{SPSS} and {SAS} Programs for Generalizability Theory Analyses},\n  author={Mushquash, Cilia and O'Connor, Brian P.},\n  year={2006},\n  journal={Behavior Research Methods},\n  doi={10.3758/BF03192810},\n  url={https://link.springer.com/article/10.3758/BF03192810}\n}\n\n@article{shavelson1989gtheory,\n  title={Generalizability Theory},\n  author={Shavelson, Richard J. and Webb, Noreen M. and Rowley, Glenn L.},\n  year={1989},\n  journal={American Psychologist},\n  url={https://psycnet.apa.org/record/1989-34789-001}\n}\n\n@article{li2023bootstrap,\n  title={Which Method Is Optimal for Estimating Variance Components and Their Variability in Generalizability Theory? {Evidence} from a Set of Unified Rules for Bootstrap Method},\n  author={Li, Guangming},\n  year={2023},\n  journal={PLoS ONE},\n  doi={10.1371/journal.pone.0288069},\n  url={https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0288069}\n}\n\n@article{tuerlinckx2006glmm,\n  title={Statistical Inference in Generalized Linear Mixed Models: A Review},\n  author={Tuerlinckx, Francis and Rijmen, Frank and Verbeke, Geert and De Boeck, Paul},\n  year={2006},\n  journal={British Journal of Mathematical and Statistical Psychology},\n  doi={10.1348/000711005X79857},\n  url={https://bpspsychub.onlinelibrary.wiley.com/doi/abs/10.1348/000711005X79857}\n}\n\n% ====== Evaluation Uncertainty & Meta-Evaluation ======\n\n@article{blackwell2024towards,\n  title={Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores},\n  author={Blackwell, Robert E. and Barry, Jon and Cohn, Anthony G.},\n  journal={arXiv preprint arXiv:2410.03492},\n  year={2024},\n  url={https://arxiv.org/abs/2410.03492}\n}\n\n@article{qian2026benchmark,\n  title={Benchmark$^2$: Systematic Evaluation of LLM Benchmarks},\n  author={Qian, Qi and Huang, Chengsong and Xu, Jingwen and others},\n  journal={arXiv preprint arXiv:2601.03986},\n  year={2026}\n}\n\n@article{burnell2023rethink,\n  title={Rethink reporting of evaluation results in {AI}},\n  author={Burnell, Ryan and Schellaert, Wout and Burden, John and others},\n  journal={Science},\n  volume={380},\n  number={6641},\n  pages={136--138},\n  year={2023},\n  doi={10.1126/science.adf6369}\n}\n\n% ====== Additional References (Post-Review) ======\n\n@article{varannot2026gtheory,\n  title={Variance-Aware {LLM} Annotation for Strategy Research: Sources, Diagnostics, and a Protocol for Reliable Measurement},\n  author={Camuffo, Arnaldo and Gambardella, Alfonso and Kazemi, Saeid and Malachowski, Jakub and Pandey, Abhinav},\n  year={2026},\n  journal={arXiv preprint arXiv:2601.02370},\n  url={https://arxiv.org/abs/2601.02370}\n}\n\n@article{kearns2026construct,\n  title={Quantifying Construct Validity in Large Language Model Evaluations},\n  author={Kearns, Ryan Othniel},\n  year={2026},\n  journal={arXiv preprint arXiv:2602.15532},\n  url={https://arxiv.org/abs/2602.15532}\n}\n\n@article{ye2025psychometrics,\n  title={Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement},\n  author={Ye, Haoran and Jin, Jing and Xie, Yuhang and Zhang, Xin and Song, Guojie},\n  year={2025},\n  journal={arXiv preprint arXiv:2505.08245},\n  url={https://arxiv.org/abs/2505.08245}\n}\n\n% ====== Round 5 additions (SF-7) ======\n\n@book{holland1993dif,\n  title     = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  year      = {1993},\n  publisher = {Lawrence Erlbaum Associates},\n  address   = {Hillsdale, NJ},\n  isbn      = {0805809724}\n}\n\n@article{clauser1998dif,\n  author  = {Clauser, Brian E. and Mazor, Kathleen M.},\n  title   = {Using Statistical Procedures to Identify Differentially Functioning Test Items},\n  journal = {Educational Measurement: Issues and Practice},\n  year    = {1998},\n  volume  = {17},\n  number  = {1},\n  pages   = {31--44},\n  doi     = {10.1111/j.1745-3992.1998.tb00619.x}\n}\n\n@incollection{webb2006reliability,\n  author    = {Webb, Noreen M. and Shavelson, Richard J. and Haertel, Edward H.},\n  title     = {Reliability Coefficients and Generalizability Theory},\n  booktitle = {Handbook of Statistics},\n  series    = {Handbook of Statistics},\n  volume    = {26},\n  editor    = {Rao, C. R. and Sinharay, Sandip},\n  publisher = {Elsevier},\n  year      = {2006},\n  pages     = {81--124},\n  doi       = {10.1016/S0169-7161(06)26004-8}\n}\n\n@article{zhu2026benchmark,\n  author  = {Zhu, Longyuan and Hua, Hairan and Miao, Linlin and Zhao, Bing},\n  title   = {Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of {LLM}s},\n  journal = {arXiv preprint arXiv:2602.11674},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.11674}\n}\n\n@inproceedings{bean2025measuring,\n  author    = {Bean, Andrew M. and Kearns, Ryan Othniel and Romanou, Angelika and Hafner, Franziska Sofia and Mayne, Harry and Batzner, Jan and Foroutan, Negar and Schmitz, Chris and Korgul, Karolina and Batra, Hunar and Deb, Oishi and Beharry, Emma and Emde, Cornelius and Foster, Thomas and Gausen, Anna and Grandury, Mar{\\'\\i}a and Han, Simeng and Hofmann, Valentin and Ibrahim, Lujain and Kim, Hazel and Kirk, Hannah Rose and Lin, Fangru and Liu, Gabrielle Kaili-May and Luettgau, Lennart and Magomere, Jabez and Rystr{\\o}m, Jonathan and Sotnikova, Anna and Yang, Yushi and Zhao, Yilun and Bibi, Adel and Bosselut, Antoine and Clark, Ronald and Cohan, Arman and Foerster, Jakob and Gal, Yarin and Hale, Scott A. and Raji, Inioluwa Deborah and Summerfield, Christopher and Torr, Philip H. S. and Ududec, Cozmin and Rocher, Luc and Mahdi, Adam},\n  title     = {Measuring What Matters: Construct Validity in Large Language Model Benchmarks},\n  booktitle = {Advances in Neural Information Processing Systems 38 ({NeurIPS} 2025), Datasets and Benchmarks Track},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2511.04703}\n}\n\n@article{freiesleben2026construct,\n  author  = {Freiesleben, Timo},\n  title   = {Establishing Construct Validity in {LLM} Capability Benchmarks Requires Nomological Networks},\n  journal = {arXiv preprint arXiv:2603.15121},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2603.15121}\n}\n\n% ====== Round 8 additions ======\n\n@article{golchin2023contamination,\n  title={Time Travel in {LLM}s: Tracing Data Contamination in Large Language Models},\n  author={Golchin, Shahriar and Surdeanu, Mihai},\n  journal={arXiv preprint arXiv:2308.08493},\n  year={2023},\n  url={https://arxiv.org/abs/2308.08493}\n}\n\n% ====== Round 6 additions ======\n\n@article{mizrahi2024state,\n  title     = {State of What Art? {A} Call for Multi-Prompt {LLM} Evaluation},\n  author    = {Mizrahi, Moran and Kaplan, Guy and Malkin, Dan and Dror, Rotem and Shahaf, Dafna and Stanovsky, Gabriel},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {12},\n  pages     = {933--949},\n  year      = {2024},\n  publisher = {MIT Press},\n  doi       = {10.1162/tacl_a_00681}\n}\n\n@article{liang2023helm,\n  title     = {Holistic Evaluation of Language Models},\n  author    = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and others},\n  journal   = {arXiv preprint arXiv:2211.09110},\n  year      = {2023}\n}\n\n@article{meredith1993measurement,\n  title     = {Measurement Invariance, Factor Analysis and Factorial Invariance},\n  author    = {Meredith, William},\n  journal   = {Psychometrika},\n  volume    = {58},\n  number    = {4},\n  pages     = {525--543},\n  year      = {1993},\n  publisher = {Springer},\n  doi       = {10.1007/BF02294825}\n}\n\n@article{putnick2016measurement,\n  title     = {Measurement Invariance Conventions and Reporting: {The} State of the Art and Future Directions for Psychological Research},\n  author    = {Putnick, Diane L. and Bornstein, Marc H.},\n  journal   = {Developmental Review},\n  volume    = {41},\n  pages     = {71--90},\n  year      = {2016},\n  publisher = {Elsevier},\n  doi       = {10.1016/j.dr.2016.06.004}\n}\n\n@book{efron1993bootstrap,\n  title     = {An Introduction to the Bootstrap},\n  author    = {Efron, Bradley and Tibshirani, Robert J.},\n  year      = {1993},\n  publisher = {Chapman \\& Hall},\n  address   = {New York}\n}\n\n@book{cardinet2010applying,\n  title     = {Applying Generalizability Theory Using {EduG}},\n  author    = {Cardinet, Jean and Johnson, Sandra and Pini, Gianreto},\n  year      = {2010},\n  publisher = {Routledge}\n}\n\n@inproceedings{kiela2021dynabench,\n  title     = {Dynabench: Rethinking Benchmarking in {NLP}},\n  author    = {Kiela, Douwe and Bartolo, Max and Nie, Yixin and Kaushik, Divyansh and Geiger, Atticus and Wu, Zhengxuan and Vidgen, Bertie and Prasad, Grusha and Singh, Amanpreet and Ringshia, Pratik and Ma, Zhiyi and Thrush, Tristan and Riedel, Sebastian and Waseem, Zeerak and Stenetorp, Pontus and Jia, Robin and Bansal, Mohit and Potts, Christopher and Williams, Adina},\n  booktitle = {Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2021}\n}\n\n% ====== Round 9 additions ======\n\n@inproceedings{saxon2024metrology,\n  title     = {Benchmarks as Microscopes: A Call for Model Metrology},\n  author    = {Saxon, Michael and Holtzman, Ari and West, Peter and Wang, William Yang and Saphra, Naomi},\n  booktitle = {Proceedings of the Conference on Language Modeling (COLM)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2407.16711}\n}\n\n@inproceedings{alzahrani2024benchmarks,\n  title     = {When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards},\n  author    = {Alzahrani, Norah and Alyahya, Hisham Abdullah and Alnumay, Yazeed and Alrashed, Sultan and Alsubaie, Shaykhah and Almushaykeh, Yusef and Mirza, Faisal and Alotaibi, Nouf and Altwairesh, Nora and Alowisheq, Areeb and Bari, M Saiful and Khan, Haidar},\n  booktitle = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year      = {2024},\n  pages     = {13787--13805},\n  url       = {https://arxiv.org/abs/2402.01781}\n}\n\n@misc{gao2024lmeval,\n  title     = {A Framework for Few-Shot Language Model Evaluation},\n  author    = {Gao, Leo and Tow, Jonathan and Abbasi, Baber and Biderman, Stella and Black, Sid and DiPofi, Anthony and Foster, Charles and Golber, Laurence and Hsu, Jeffrey and Le Noac'h, Alain and Li, Haonan and McDonell, Kyle and Muennighoff, Niklas and Ocqueteau, Chris and Phang, Jason and Reynolds, Laria and Schoelkopf, Hailey and Skowron, Aviya and Sutawika, Lintang and Tang, Eric and Thite, Anish and Wang, Ben and Wang, Kevin and Zou, Andy},\n  year      = {2024},\n  publisher = {Zenodo},\n  doi       = {10.5281/zenodo.10256836},\n  url       = {https://github.com/EleutherAI/lm-evaluation-harness}\n}\n\n@inproceedings{gema2025mmlu,\n  title     = {Are We Done with {MMLU}?},\n  author    = {Gema, Aryo Pradipta and Leang, Joshua Ong Jun and Hong, Giwon and Devoto, Alessio and Mancino, Alberto Carlo Maria and Saxena, Rohit and He, Xuanli and Zhao, Yu and Du, Xiaotang and Ghasemi Madani, Mohammad Reza and Barale, Claire and McHardy, Robert and Harris, Joshua and Kaddour, Jean and Van Krieken, Emile and Minervini, Pasquale},\n  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  doi       = {10.18653/v1/2025.naacl-long.262},\n  url       = {https://arxiv.org/abs/2406.04127}\n}\n\n@inproceedings{wang2024mmlupro,\n  title     = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},\n  author    = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Yue, Xiang and Chen, Wenhu},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2406.01574}\n}\n\n@inproceedings{oren2024proving,\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Ladhak, Faisal and Hashimoto, Tatsunori B.},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  note      = {Outstanding Paper Honorable Mention},\n  url       = {https://arxiv.org/abs/2310.17623}\n}\n",
      "numLines": 530,
      "startLine": 1,
      "totalLines": 530
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01VoikL1zXty1os9KuhWByz9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.bbl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "8003a423-4974-4a66-ab87-ef7597502f1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BmNeCV7EPG4cAsDHVfrr8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17173,
      "cache_read_input_tokens": 42956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17173
      },
      "output_tokens": 34,
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

_source line 57 · 2026-05-23T19:07:36.618Z_

<details><summary>↩ Tool result · `toolu_01VoikL1zXty1os9KuhWByz9`</summary>

```text
1	\begin{thebibliography}{59}
2	\providecommand{\natexlab}[1]{#1}
3	
4	\bibitem[{Alzahrani et~al.(2024)Alzahrani, Alyahya, Alnumay, Alrashed,
5	  Alsubaie, Almushaykeh, Mirza, Alotaibi, Altwairesh, Alowisheq, Bari, and
6	  Khan}]{alzahrani2024benchmarks}
7	Norah Alzahrani, Hisham~Abdullah Alyahya, Yazeed Alnumay, Sultan Alrashed,
8	  Shaykhah Alsubaie, Yusef Almushaykeh, Faisal Mirza, Nouf Alotaibi, Nora
9	  Altwairesh, Areeb Alowisheq, M~Saiful Bari, and Haidar Khan. 2024.
10	\newblock \href {https://arxiv.org/abs/2402.01781} {When benchmarks are
11	  targets: Revealing the sensitivity of large language model leaderboards}.
12	\newblock In \emph{Proceedings of the Association for Computational Linguistics
13	  (ACL)}, pages 13787--13805.
14	
15	\bibitem[{Bean et~al.(2025)Bean, Kearns, Romanou, Hafner, Mayne, Batzner,
16	  Foroutan, Schmitz, Korgul, Batra, Deb, Beharry, Emde, Foster, Gausen,
17	  Grandury, Han, Hofmann, Ibrahim, Kim, Kirk, Lin, Liu, Luettgau, Magomere,
18	  Rystr{\o}m, Sotnikova, Yang, Zhao, Bibi, Bosselut, Clark, Cohan, Foerster,
19	  Gal, Hale, Raji, Summerfield, Torr, Ududec, Rocher, and
20	  Mahdi}]{bean2025measuring}
21	Andrew~M. Bean, Ryan~Othniel Kearns, Angelika Romanou, Franziska~Sofia Hafner,
22	  Harry Mayne, Jan Batzner, Negar Foroutan, Chris Schmitz, Karolina Korgul,
23	  Hunar Batra, Oishi Deb, Emma Beharry, Cornelius Emde, Thomas Foster, Anna
24	  Gausen, Mar{\'\i}a Grandury, Simeng Han, Valentin Hofmann, Lujain Ibrahim,
25	  and 23 others. 2025.
26	\newblock \href {https://arxiv.org/abs/2511.04703} {Measuring what matters:
27	  Construct validity in large language model benchmarks}.
28	\newblock In \emph{Advances in Neural Information Processing Systems 38
29	  ({NeurIPS} 2025), Datasets and Benchmarks Track}.
30	
31	\bibitem[{Biderman et~al.(2024)Biderman, Schoelkopf, Sutawika, Gao, Tow,
32	  Abbasi, Aji, Ammanamanchi, Black, Clive, DiPofi, Etxaniz, Fattori, Forde,
33	  Foster, Hsu, Jaiswal, Lee, Li, Lovering, Muennighoff, Pavlick, Phang,
34	  Skowron, Tan, Tang, Wang, Winata, Yvon, and Zou}]{biderman2024lessons}
35	Stella Biderman, Hailey Schoelkopf, Lintang Sutawika, Leo Gao, Jonathan Tow,
36	  Baber Abbasi, Alham~Fikri Aji, Pawan~Sasanka Ammanamanchi, Sidney Black,
37	  Jordan Clive, Anthony DiPofi, Julen Etxaniz, Benjamin Fattori, Jessica~Zosa
38	  Forde, Charles Foster, Jeffrey Hsu, Mimansa Jaiswal, Won~Ik Lee, Haonan Li,
39	  and 11 others. 2024.
40	\newblock \href {https://arxiv.org/abs/2405.14782} {Lessons from the trenches
41	  on reproducible evaluation of language models}.
42	\newblock \emph{arXiv preprint arXiv:2405.14782}.
43	
44	\bibitem[{Blackwell et~al.(2024)Blackwell, Barry, and
45	  Cohn}]{blackwell2024towards}
46	Robert~E. Blackwell, Jon Barry, and Anthony~G. Cohn. 2024.
47	\newblock \href {https://arxiv.org/abs/2410.03492} {Towards reproducible llm
48	  evaluation: Quantifying uncertainty in llm benchmark scores}.
49	\newblock \emph{arXiv preprint arXiv:2410.03492}.
50	
51	\bibitem[{Bouthillier et~al.(2021)Bouthillier, Delaunay, Bronzi, Trofimov,
52	  Nichyporuk, Szeto, Sepahvand, Raff, Madan, Voleti, Kahou, Michalski, Arbel,
53	  Pal, Varoquaux, and Vincent}]{bouthillier2021accounting}
54	Xavier Bouthillier, Pierre Delaunay, Mirko Bronzi, Assya Trofimov, Brennan
55	  Nichyporuk, Justin Szeto, Nazanin~Mohammadi Sepahvand, Edward Raff, Kshitij
56	  Madan, Vikram Voleti, Samira~Ebrahimi Kahou, Vincent Michalski, Tal Arbel,
57	  Chris Pal, Ga{\"e}l Varoquaux, and Pascal Vincent. 2021.
58	\newblock \href {https://arxiv.org/abs/2103.03098} {Accounting for variance in
59	  machine learning benchmarks}.
60	\newblock In \emph{Proceedings of Machine Learning and Systems (MLSys)}.
61	
62	\bibitem[{Brennan(2001)}]{brennan2001generalizability}
63	Robert~L. Brennan. 2001.
64	\newblock \emph{Generalizability Theory}.
65	\newblock Springer.
66	
67	\bibitem[{Bui et~al.(2025)Bui, Savova, and Wang}]{bui2025seeds}
68	Ngoc~Thang Bui, Guergana Savova, and Lijun Wang. 2025.
69	\newblock \href {https://aclanthology.org/2025.ijcnlp-short.3/} {Assessing the
70	  macro and micro effects of random seeds on fine-tuning large language
71	  models}.
72	\newblock In \emph{Proceedings of IJCNLP-AACL}.
73	
74	\bibitem[{Burnell et~al.(2023)Burnell, Schellaert, Burden
75	  et~al.}]{burnell2023rethink}
76	Ryan Burnell, Wout Schellaert, John Burden, and 1 others. 2023.
77	\newblock \href {https://doi.org/10.1126/science.adf6369} {Rethink reporting of
78	  evaluation results in {AI}}.
79	\newblock \emph{Science}, 380(6641):136--138.
80	
81	\bibitem[{Camuffo et~al.(2026)Camuffo, Gambardella, Kazemi, Malachowski, and
82	  Pandey}]{varannot2026gtheory}
83	Arnaldo Camuffo, Alfonso Gambardella, Saeid Kazemi, Jakub Malachowski, and
84	  Abhinav Pandey. 2026.
85	\newblock \href {https://arxiv.org/abs/2601.02370} {Variance-aware {LLM}
86	  annotation for strategy research: Sources, diagnostics, and a protocol for
87	  reliable measurement}.
88	\newblock \emph{arXiv preprint arXiv:2601.02370}.
89	
90	\bibitem[{Cardinet et~al.(2010)Cardinet, Johnson, and
91	  Pini}]{cardinet2010applying}
92	Jean Cardinet, Sandra Johnson, and Gianreto Pini. 2010.
93	\newblock \emph{Applying Generalizability Theory Using {EduG}}.
94	\newblock Routledge.
95	
96	\bibitem[{Clauser and Mazor(1998)}]{clauser1998dif}
97	Brian~E. Clauser and Kathleen~M. Mazor. 1998.
98	\newblock \href {https://doi.org/10.1111/j.1745-3992.1998.tb00619.x} {Using
99	  statistical procedures to identify differentially functioning test items}.
100	\newblock \emph{Educational Measurement: Issues and Practice}, 17(1):31--44.
101	
102	\bibitem[{Dehghani et~al.(2021)Dehghani, Tay, Gritsenko, Zhao, Houlsby, Diaz,
103	  Metzler, and Vinyals}]{dehghani2021benchmark}
104	Mostafa Dehghani, Yi~Tay, Alexey~A. Gritsenko, Zhe Zhao, Neil Houlsby, Fernando
105	  Diaz, Donald Metzler, and Oriol Vinyals. 2021.
106	\newblock \href {https://arxiv.org/abs/2107.07002} {The benchmark lottery}.
107	\newblock \emph{arXiv preprint arXiv:2107.07002}.
108	
109	\bibitem[{Dodge et~al.(2020)Dodge, Ilharco, Schwartz, Farhadi, Hajishirzi, and
110	  Smith}]{dodge2020finetuning}
111	Jesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali Farhadi, Hannaneh Hajishirzi,
112	  and Noah~A. Smith. 2020.
113	\newblock \href {https://arxiv.org/abs/2002.06305} {Fine-tuning pretrained
114	  language models: Weight initializations, data orders, and early stopping}.
115	\newblock \emph{arXiv preprint arXiv:2002.06305}.
116	
117	\bibitem[{Efron and Tibshirani(1993)}]{efron1993bootstrap}
118	Bradley Efron and Robert~J. Tibshirani. 1993.
119	\newblock \emph{An Introduction to the Bootstrap}.
120	\newblock Chapman \& Hall, New York.
121	
122	\bibitem[{Freiesleben(2026)}]{freiesleben2026construct}
123	Timo Freiesleben. 2026.
124	\newblock \href {https://arxiv.org/abs/2603.15121} {Establishing construct
125	  validity in {LLM} capability benchmarks requires nomological networks}.
126	\newblock \emph{arXiv preprint arXiv:2603.15121}.
127	
128	\bibitem[{Gao et~al.(2024)Gao, Tow, Abbasi, Biderman, Black, DiPofi, Foster,
129	  Golber, Hsu, Le~Noac'h, Li, McDonell, Muennighoff, Ocqueteau, Phang,
130	  Reynolds, Schoelkopf, Skowron, Sutawika, Tang, Thite, Wang, Wang, and
131	  Zou}]{gao2024lmeval}
132	Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony
133	  DiPofi, Charles Foster, Laurence Golber, Jeffrey Hsu, Alain Le~Noac'h, Haonan
134	  Li, Kyle McDonell, Niklas Muennighoff, Chris Ocqueteau, Jason Phang, Laria
135	  Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, and 5 others.
136	  2024.
137	\newblock \href {https://doi.org/10.5281/zenodo.10256836} {A framework for
138	  few-shot language model evaluation}.
139	
140	\bibitem[{Gema et~al.(2025)Gema, Leang, Hong, Devoto, Mancino, Saxena, He,
141	  Zhao, Du, Ghasemi~Madani, Barale, McHardy, Harris, Kaddour, Van~Krieken, and
142	  Minervini}]{gema2025mmlu}
143	Aryo~Pradipta Gema, Joshua Ong~Jun Leang, Giwon Hong, Alessio Devoto, Alberto
144	  Carlo~Maria Mancino, Rohit Saxena, Xuanli He, Yu~Zhao, Xiaotang Du,
145	  Mohammad~Reza Ghasemi~Madani, Claire Barale, Robert McHardy, Joshua Harris,
146	  Jean Kaddour, Emile Van~Krieken, and Pasquale Minervini. 2025.
147	\newblock \href {https://doi.org/10.18653/v1/2025.naacl-long.262} {Are we done
148	  with {MMLU}?}
149	\newblock In \emph{Proceedings of the Conference of the North American Chapter
150	  of the Association for Computational Linguistics (NAACL)}.
151	
152	\bibitem[{Golchin and Surdeanu(2023)}]{golchin2023contamination}
153	Shahriar Golchin and Mihai Surdeanu. 2023.
154	\newblock \href {https://arxiv.org/abs/2308.08493} {Time travel in {LLM}s:
155	  Tracing data contamination in large language models}.
156	\newblock \emph{arXiv preprint arXiv:2308.08493}.
157	
158	\bibitem[{He and {Thinking Machines Lab}(2025)}]{thinkingmachines2025batch}
159	Haiyang He and {Thinking Machines Lab}. 2025.
160	\newblock \href {https://doi.org/10.64434/tml.20250910} {Defeating
161	  nondeterminism in {LLM} inference}.
162	\newblock Thinking Machines Lab: Connectionism.
163	
164	\bibitem[{Henderson et~al.(2018)Henderson, Islam, Bachman, Pineau, Precup, and
165	  Meger}]{henderson2018deep}
166	Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup,
167	  and David Meger. 2018.
168	\newblock \href {https://arxiv.org/abs/1709.06560} {Deep reinforcement learning
169	  that matters}.
170	\newblock In \emph{Proceedings of the AAAI Conference on Artificial
171	  Intelligence}.
172	
173	\bibitem[{Holland and Wainer(1993)}]{holland1993dif}
174	Paul~W. Holland and Howard Wainer, editors. 1993.
175	\newblock \emph{Differential Item Functioning}.
176	\newblock Lawrence Erlbaum Associates, Hillsdale, NJ.
177	
178	\bibitem[{Hua et~al.(2025)Hua, Tang, Gu, Gu, Wong, and Qin}]{hua2025flaw}
179	Angie Hua, Kevin Tang, Chaoqun Gu, Jing Gu, Edmund Wong, and Yilin Qin. 2025.
180	\newblock \href {https://aclanthology.org/2025.emnlp-main.1006/} {Flaw or
181	  artifact? rethinking prompt sensitivity in evaluating {LLM}s}.
182	\newblock In \emph{Proceedings of the Conference on Empirical Methods in
183	  Natural Language Processing (EMNLP)}.
184	
185	\bibitem[{Jiang and Skorupski(2018)}]{jiang2018bayesian}
186	Zhehan Jiang and William Skorupski. 2018.
187	\newblock \href {https://doi.org/10.3758/s13428-017-0986-3} {A {Bayesian}
188	  approach to estimating variance components within a multivariate
189	  generalizability theory framework}.
190	\newblock \emph{Behavior Research Methods}, 50.
191	
192	\bibitem[{Kearns(2026)}]{kearns2026construct}
193	Ryan~Othniel Kearns. 2026.
194	\newblock \href {https://arxiv.org/abs/2602.15532} {Quantifying construct
195	  validity in large language model evaluations}.
196	\newblock \emph{arXiv preprint arXiv:2602.15532}.
197	
198	\bibitem[{Kiela et~al.(2021)Kiela, Bartolo, Nie, Kaushik, Geiger, Wu, Vidgen,
199	  Prasad, Singh, Ringshia, Ma, Thrush, Riedel, Waseem, Stenetorp, Jia, Bansal,
200	  Potts, and Williams}]{kiela2021dynabench}
201	Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger,
202	  Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia,
203	  Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Waseem, Pontus Stenetorp,
204	  Robin Jia, Mohit Bansal, Christopher Potts, and Adina Williams. 2021.
205	\newblock Dynabench: Rethinking benchmarking in {NLP}.
206	\newblock In \emph{Proceedings of the 2021 Conference of the North American
207	  Chapter of the Association for Computational Linguistics (NAACL)}.
208	
209	\bibitem[{Kipnis et~al.(2025)Kipnis, Voudouris, Schulze~Buschoff, and
210	  Schulz}]{kipnis2025metabench}
211	Alex Kipnis, Konstantinos Voudouris, Luca Schulze~Buschoff, and Eric Schulz.
212	  2025.
213	\newblock \href {https://arxiv.org/abs/2407.12844} {metabench -- a sparse
214	  benchmark of reasoning and knowledge in large language models}.
215	\newblock In \emph{Proceedings of the International Conference on Learning
216	  Representations}.
217	
218	\bibitem[{Kunievsky and Evans(2025)}]{kunievsky2025intent}
219	Nitzan Kunievsky and James~A. Evans. 2025.
220	\newblock \href {https://arxiv.org/abs/2506.16584} {Measuring intent
221	  comprehension in {LLM}s: A variance decomposition framework}.
222	\newblock \emph{arXiv preprint arXiv:2506.16584}.
223	
224	\bibitem[{Lalor et~al.(2019)Lalor, Wu, and Yu}]{lalor2019irt}
225	John~P. Lalor, Hao Wu, and Hong Yu. 2019.
226	\newblock \href {https://aclanthology.org/D19-1434/} {Learning latent
227	  parameters without human response patterns: Item response theory with
228	  artificial crowds}.
229	\newblock In \emph{Proceedings of the Conference on Empirical Methods in
230	  Natural Language Processing and International Joint Conference on Natural
231	  Language Processing (EMNLP-IJCNLP)}.
232	
233	\bibitem[{Li(2023)}]{li2023bootstrap}
234	Guangming Li. 2023.
235	\newblock \href {https://doi.org/10.1371/journal.pone.0288069} {Which method is
236	  optimal for estimating variance components and their variability in
237	  generalizability theory? {Evidence} from a set of unified rules for bootstrap
238	  method}.
239	\newblock \emph{PLoS ONE}.
240	
241	\bibitem[{Li et~al.(2025)Li, Tang, Chen, Cheng, Metoyer, Hua, and
242	  Chawla}]{li2025atlas}
243	Peiyu Li, Xiuxiu Tang, Si~Chen, Ying Cheng, Ronald Metoyer, Ting Hua, and
244	  Nitesh~V. Chawla. 2025.
245	\newblock \href {https://arxiv.org/abs/2511.04689} {Adaptive testing for {LLM}
246	  evaluation: A psychometric alternative to static benchmarks}.
247	\newblock \emph{arXiv preprint arXiv:2511.04689}.
248	
249	\bibitem[{Liang et~al.(2023)Liang, Bommasani, Lee, Tsipras, Soylu, Yasunaga,
250	  Zhang, Narayanan, Wu, Kumar et~al.}]{liang2023helm}
251	Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu,
252	  Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar,
253	  and 1 others. 2023.
254	\newblock Holistic evaluation of language models.
255	\newblock \emph{arXiv preprint arXiv:2211.09110}.
256	
257	\bibitem[{Madaan et~al.(2024)Madaan, Bhatia, Tulio~Ribeiro, and
258	  Roth}]{madaan2024quantifying}
259	Lovish Madaan, Samarth Bhatia, Marco Tulio~Ribeiro, and Dan Roth. 2024.
260	\newblock \href {https://arxiv.org/abs/2406.10229} {Quantifying variance in
261	  evaluation benchmarks}.
262	\newblock \emph{arXiv preprint arXiv:2406.10229}.
263	
264	\bibitem[{Magnusson et~al.(2023)Magnusson, Smith, and
265	  Dodge}]{magnusson2023reproducibility}
266	Ian Magnusson, Noah~A. Smith, and Jesse Dodge. 2023.
267	\newblock \href {https://aclanthology.org/2023.findings-acl.809/}
268	  {Reproducibility in {NLP}: What have we learned from the checklist?}
269	\newblock In \emph{Findings of the Association for Computational Linguistics
270	  (ACL)}.
271	
272	\bibitem[{Maia~Polo et~al.(2024)Maia~Polo, Weber, Choshen, Sun, Xu, and
273	  Yurochkin}]{polo2024tinybenchmarks}
274	Felipe Maia~Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and
275	  Mikhail Yurochkin. 2024.
276	\newblock \href {https://arxiv.org/abs/2402.14992} {{tinyBenchmarks}:
277	  Evaluating {LLM}s with fewer examples}.
278	\newblock In \emph{Proceedings of the International Conference on Machine
279	  Learning (ICML)}.
280	
281	\bibitem[{Meredith(1993)}]{meredith1993measurement}
282	William Meredith. 1993.
283	\newblock \href {https://doi.org/10.1007/BF02294825} {Measurement invariance,
284	  factor analysis and factorial invariance}.
285	\newblock \emph{Psychometrika}, 58(4):525--543.
286	
287	\bibitem[{Messina and Scotta(2026)}]{messina2026background}
288	Alberto Messina and Sara Scotta. 2026.
289	\newblock \href {https://arxiv.org/abs/2604.22411} {Introducing background
290	  temperature to characterise hidden randomness in large language models}.
291	\newblock \emph{arXiv preprint arXiv:2604.22411}.
292	
293	\bibitem[{Messing(2026)}]{messing2026hidden}
294	Solomon Messing. 2026.
295	\newblock \href {https://arxiv.org/abs/2604.11581} {Hidden measurement error in
296	  {LLM} pipelines distorts annotation, evaluation, and benchmarking}.
297	\newblock \emph{arXiv preprint arXiv:2604.11581}.
298	
299	\bibitem[{Mizrahi et~al.(2024)Mizrahi, Kaplan, Malkin, Dror, Shahaf, and
300	  Stanovsky}]{mizrahi2024state}
301	Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel
302	  Stanovsky. 2024.
303	\newblock \href {https://doi.org/10.1162/tacl_a_00681} {State of what art? {A}
304	  call for multi-prompt {LLM} evaluation}.
305	\newblock \emph{Transactions of the Association for Computational Linguistics},
306	  12:933--949.
307	
308	\bibitem[{Mushquash and O'Connor(2006)}]{mushquash2006gtheory}
309	Cilia Mushquash and Brian~P. O'Connor. 2006.
310	\newblock \href {https://doi.org/10.3758/BF03192810} {{SPSS} and {SAS} programs
311	  for generalizability theory analyses}.
312	\newblock \emph{Behavior Research Methods}.
313	
314	\bibitem[{Oren et~al.(2024)Oren, Meister, Chatterji, Ladhak, and
315	  Hashimoto}]{oren2024proving}
316	Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and
317	  Tatsunori~B. Hashimoto. 2024.
318	\newblock \href {https://arxiv.org/abs/2310.17623} {Proving test set
319	  contamination in black box language models}.
320	\newblock In \emph{Proceedings of the International Conference on Learning
321	  Representations (ICLR)}.
322	\newblock Outstanding Paper Honorable Mention.
323	
324	\bibitem[{Perlitz et~al.(2023)Perlitz, Bandel, Gera, Arviv, Ein-Dor, Shnarch,
325	  Slonim, Shmueli-Scheuer, and Choshen}]{perlitz2023efficient}
326	Yotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal
327	  Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen. 2023.
328	\newblock \href {https://arxiv.org/abs/2308.11696} {Efficient benchmarking of
329	  language models}.
330	\newblock \emph{arXiv preprint arXiv:2308.11696}.
331	
332	\bibitem[{Pezeshkpour and Hruschka(2024)}]{pezeshkpour2024ordering}
333	Pouya Pezeshkpour and Estevam Hruschka. 2024.
334	\newblock \href {https://aclanthology.org/2024.findings-naacl.130/} {Large
335	  language models sensitivity to the order of options in multiple-choice
336	  questions}.
337	\newblock In \emph{Findings of the North American Chapter of the Association
338	  for Computational Linguistics (NAACL)}.
339	
340	\bibitem[{Putnick and Bornstein(2016)}]{putnick2016measurement}
341	Diane~L. Putnick and Marc~H. Bornstein. 2016.
342	\newblock \href {https://doi.org/10.1016/j.dr.2016.06.004} {Measurement
343	  invariance conventions and reporting: {The} state of the art and future
344	  directions for psychological research}.
345	\newblock \emph{Developmental Review}, 41:71--90.
346	
347	\bibitem[{Qian et~al.(2026)Qian, Huang, Xu et~al.}]{qian2026benchmark}
348	Qi~Qian, Chengsong Huang, Jingwen Xu, and 1 others. 2026.
349	\newblock Benchmark$^2$: Systematic evaluation of llm benchmarks.
350	\newblock \emph{arXiv preprint arXiv:2601.03986}.
351	
352	\bibitem[{Rodriguez et~al.(2021)Rodriguez, Barrow, Hoyle, Lalor, Jia, and
353	  Boyd-Graber}]{rodriguez2021leaderboards}
354	Pedro Rodriguez, Joe Barrow, Alexander Hoyle, John~P. Lalor, Robin Jia, and
355	  Jordan Boyd-Graber. 2021.
356	\newblock \href {https://aclanthology.org/2021.acl-long.346/} {Evaluation
357	  examples are not equally informative: How should that change {NLP}
358	  leaderboards?}
359	\newblock In \emph{Proceedings of the Association for Computational Linguistics
360	  (ACL)}.
361	
362	\bibitem[{Romanou et~al.(2026)Romanou, Ibrahim, Ross, Shaib, Oktar, Bell,
363	  Ovalle, Dodge, Bosselut, Sinha, and Williams}]{brittlebench2026}
364	Angelika Romanou, Marah Ibrahim, Candace Ross, Chantal Shaib, Kerem Oktar,
365	  Samuel~J. Bell, Anaelia Ovalle, Jesse Dodge, Antoine Bosselut, Koustuv Sinha,
366	  and Adina Williams. 2026.
367	\newblock \href {https://arxiv.org/abs/2603.13285} {Brittlebench: Quantifying
368	  {LLM} robustness via prompt sensitivity}.
369	\newblock \emph{arXiv preprint arXiv:2603.13285}.
370	
371	\bibitem[{Saxon et~al.(2024)Saxon, Holtzman, West, Wang, and
372	  Saphra}]{saxon2024metrology}
373	Michael Saxon, Ari Holtzman, Peter West, William~Yang Wang, and Naomi Saphra.
374	  2024.
375	\newblock \href {https://arxiv.org/abs/2407.16711} {Benchmarks as microscopes:
376	  A call for model metrology}.
377	\newblock In \emph{Proceedings of the Conference on Language Modeling (COLM)}.
378	
379	\bibitem[{Sclar et~al.(2024)Sclar, Choi, Tsvetkov, and
380	  Suhr}]{sclar2024formatting}
381	Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. 2024.
382	\newblock \href {https://arxiv.org/abs/2310.11324} {Quantifying language
383	  models' sensitivity to spurious features in prompt design or: How {I} learned
384	  to start worrying about prompt formatting}.
385	\newblock In \emph{Proceedings of the International Conference on Learning
386	  Representations (ICLR)}.
387	
388	\bibitem[{Shanmugavelu et~al.(2024)Shanmugavelu, Taillefumier, Culver,
389	  Hernandez, Coletti, and Sedova}]{shanmugavelu2024floating}
390	Sanjif Shanmugavelu, Mathieu Taillefumier, Christopher Culver, Oscar Hernandez,
391	  Mark Coletti, and Ada Sedova. 2024.
392	\newblock \href {https://doi.org/10.1109/SCW63240.2024.00028} {Impacts of
393	  floating-point non-associativity on reproducibility for {HPC} and deep
394	  learning applications}.
395	\newblock In \emph{SC'24 Workshops (IEEE)}.
396	
397	\bibitem[{Shavelson and Webb(1991)}]{shavelson1991generalizability}
398	Richard~J. Shavelson and Noreen~M. Webb. 1991.
399	\newblock \emph{Generalizability Theory: A Primer}.
400	\newblock SAGE Publications.
401	
402	\bibitem[{Shavelson et~al.(1989)Shavelson, Webb, and
403	  Rowley}]{shavelson1989gtheory}
404	Richard~J. Shavelson, Noreen~M. Webb, and Glenn~L. Rowley. 1989.
405	\newblock \href {https://psycnet.apa.org/record/1989-34789-001}
406	  {Generalizability theory}.
407	\newblock \emph{American Psychologist}.
408	
409	\bibitem[{Song et~al.(2025)Song, Lee, and Jiao}]{song2025gtheory}
410	Dan Song, Won-Chan Lee, and Hong Jiao. 2025.
411	\newblock \href {https://arxiv.org/abs/2507.19980} {Exploring {LLM} autoscoring
412	  reliability in large-scale writing assessments using generalizability
413	  theory}.
414	\newblock \emph{arXiv preprint arXiv:2507.19980}.
415	
416	\bibitem[{Tuerlinckx et~al.(2006)Tuerlinckx, Rijmen, Verbeke, and
417	  De~Boeck}]{tuerlinckx2006glmm}
418	Francis Tuerlinckx, Frank Rijmen, Geert Verbeke, and Paul De~Boeck. 2006.
419	\newblock \href {https://doi.org/10.1348/000711005X79857} {Statistical
420	  inference in generalized linear mixed models: A review}.
421	\newblock \emph{British Journal of Mathematical and Statistical Psychology}.
422	
423	\bibitem[{Wang et~al.(2024)Wang, Ma, Zhang, Ni, Chandra, Guo, Ren, Arulraj, He,
424	  Jiang, Li, Ku, Wang, Zhuang, Fan, Yue, and Chen}]{wang2024mmlupro}
425	Yubo Wang, Xueguang Ma, Ge~Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo,
426	  Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai
427	  Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen. 2024.
428	\newblock \href {https://arxiv.org/abs/2406.01574} {{MMLU-Pro}: A more robust
429	  and challenging multi-task language understanding benchmark}.
430	\newblock In \emph{Advances in Neural Information Processing Systems (NeurIPS),
431	  Datasets and Benchmarks Track}.
432	
433	\bibitem[{Webb et~al.(2006)Webb, Shavelson, and Haertel}]{webb2006reliability}
434	Noreen~M. Webb, Richard~J. Shavelson, and Edward~H. Haertel. 2006.
435	\newblock \href {https://doi.org/10.1016/S0169-7161(06)26004-8} {Reliability
436	  coefficients and generalizability theory}.
437	\newblock In C.~R. Rao and Sandip Sinharay, editors, \emph{Handbook of
438	  Statistics}, volume~26 of \emph{Handbook of Statistics}, pages 81--124.
439	  Elsevier.
440	
441	\bibitem[{Ye et~al.(2025)Ye, Jin, Xie, Zhang, and Song}]{ye2025psychometrics}
442	Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, and Guojie Song. 2025.
443	\newblock \href {https://arxiv.org/abs/2505.08245} {Large language model
444	  psychometrics: A systematic review of evaluation, validation, and
445	  enhancement}.
446	\newblock \emph{arXiv preprint arXiv:2505.08245}.
447	
448	\bibitem[{Yuan et~al.(2025)Yuan, Li, Ding, Xie, Li, Zhao, Wan, Shi, Hu, and
449	  Liu}]{yuan2025layercast}
450	Juntao Yuan, Haoyang Li, Xingcheng Ding, Weijie Xie, Yue-Jiao Li, Wentao Zhao,
451	  Kaiyan Wan, Jiayi Shi, Xiaolu Hu, and Zhouhan Liu. 2025.
452	\newblock \href {https://arxiv.org/abs/2506.09501} {Understanding and
453	  mitigating numerical sources of nondeterminism in {LLM} inference}.
454	\newblock In \emph{Advances in Neural Information Processing Systems
455	  (NeurIPS)}.
456	\newblock Oral presentation.
457	
458	\bibitem[{Zhou et~al.(2026)Zhou, Huang, Zhao, Han, Wang, Chen, Yang, Bao, Dong,
459	  Xu, Zhu, Cao, and Zhao}]{zhou2026irt}
460	Hao Zhou, Huifeng Huang, Zhe Zhao, Long Han, Haobo Wang, Ke~Chen, Min Yang,
461	  Wanli Bao, Jiaxin Dong, Bo~Xu, Conghui Zhu, Hao Cao, and Tiejun Zhao. 2026.
462	\newblock \href {https://arxiv.org/abs/2505.15055} {Lost in benchmarks?
463	  rethinking large language model benchmarking with item response theory}.
464	\newblock In \emph{Proceedings of the AAAI Conference on Artificial
465	  Intelligence}.
466	\newblock Oral presentation.
467	
468	\bibitem[{Zhu et~al.(2026)Zhu, Hua, Miao, and Zhao}]{zhu2026benchmark}
469	Longyuan Zhu, Hairan Hua, Linlin Miao, and Bing Zhao. 2026.
470	\newblock \href {https://arxiv.org/abs/2602.11674} {Benchmark health index: A
471	  systematic framework for benchmarking the benchmarks of {LLM}s}.
472	\newblock \emph{arXiv preprint arXiv:2602.11674}.
473	
474	\end{thebibliography}
475	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "2616aef5-e69c-4a6d-bc0c-3c61966d3e5d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.bbl",
      "content": "\\begin{thebibliography}{59}\n\\providecommand{\\natexlab}[1]{#1}\n\n\\bibitem[{Alzahrani et~al.(2024)Alzahrani, Alyahya, Alnumay, Alrashed,\n  Alsubaie, Almushaykeh, Mirza, Alotaibi, Altwairesh, Alowisheq, Bari, and\n  Khan}]{alzahrani2024benchmarks}\nNorah Alzahrani, Hisham~Abdullah Alyahya, Yazeed Alnumay, Sultan Alrashed,\n  Shaykhah Alsubaie, Yusef Almushaykeh, Faisal Mirza, Nouf Alotaibi, Nora\n  Altwairesh, Areeb Alowisheq, M~Saiful Bari, and Haidar Khan. 2024.\n\\newblock \\href {https://arxiv.org/abs/2402.01781} {When benchmarks are\n  targets: Revealing the sensitivity of large language model leaderboards}.\n\\newblock In \\emph{Proceedings of the Association for Computational Linguistics\n  (ACL)}, pages 13787--13805.\n\n\\bibitem[{Bean et~al.(2025)Bean, Kearns, Romanou, Hafner, Mayne, Batzner,\n  Foroutan, Schmitz, Korgul, Batra, Deb, Beharry, Emde, Foster, Gausen,\n  Grandury, Han, Hofmann, Ibrahim, Kim, Kirk, Lin, Liu, Luettgau, Magomere,\n  Rystr{\\o}m, Sotnikova, Yang, Zhao, Bibi, Bosselut, Clark, Cohan, Foerster,\n  Gal, Hale, Raji, Summerfield, Torr, Ududec, Rocher, and\n  Mahdi}]{bean2025measuring}\nAndrew~M. Bean, Ryan~Othniel Kearns, Angelika Romanou, Franziska~Sofia Hafner,\n  Harry Mayne, Jan Batzner, Negar Foroutan, Chris Schmitz, Karolina Korgul,\n  Hunar Batra, Oishi Deb, Emma Beharry, Cornelius Emde, Thomas Foster, Anna\n  Gausen, Mar{\\'\\i}a Grandury, Simeng Han, Valentin Hofmann, Lujain Ibrahim,\n  and 23 others. 2025.\n\\newblock \\href {https://arxiv.org/abs/2511.04703} {Measuring what matters:\n  Construct validity in large language model benchmarks}.\n\\newblock In \\emph{Advances in Neural Information Processing Systems 38\n  ({NeurIPS} 2025), Datasets and Benchmarks Track}.\n\n\\bibitem[{Biderman et~al.(2024)Biderman, Schoelkopf, Sutawika, Gao, Tow,\n  Abbasi, Aji, Ammanamanchi, Black, Clive, DiPofi, Etxaniz, Fattori, Forde,\n  Foster, Hsu, Jaiswal, Lee, Li, Lovering, Muennighoff, Pavlick, Phang,\n  Skowron, Tan, Tang, Wang, Winata, Yvon, and Zou}]{biderman2024lessons}\nStella Biderman, Hailey Schoelkopf, Lintang Sutawika, Leo Gao, Jonathan Tow,\n  Baber Abbasi, Alham~Fikri Aji, Pawan~Sasanka Ammanamanchi, Sidney Black,\n  Jordan Clive, Anthony DiPofi, Julen Etxaniz, Benjamin Fattori, Jessica~Zosa\n  Forde, Charles Foster, Jeffrey Hsu, Mimansa Jaiswal, Won~Ik Lee, Haonan Li,\n  and 11 others. 2024.\n\\newblock \\href {https://arxiv.org/abs/2405.14782} {Lessons from the trenches\n  on reproducible evaluation of language models}.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}.\n\n\\bibitem[{Blackwell et~al.(2024)Blackwell, Barry, and\n  Cohn}]{blackwell2024towards}\nRobert~E. Blackwell, Jon Barry, and Anthony~G. Cohn. 2024.\n\\newblock \\href {https://arxiv.org/abs/2410.03492} {Towards reproducible llm\n  evaluation: Quantifying uncertainty in llm benchmark scores}.\n\\newblock \\emph{arXiv preprint arXiv:2410.03492}.\n\n\\bibitem[{Bouthillier et~al.(2021)Bouthillier, Delaunay, Bronzi, Trofimov,\n  Nichyporuk, Szeto, Sepahvand, Raff, Madan, Voleti, Kahou, Michalski, Arbel,\n  Pal, Varoquaux, and Vincent}]{bouthillier2021accounting}\nXavier Bouthillier, Pierre Delaunay, Mirko Bronzi, Assya Trofimov, Brennan\n  Nichyporuk, Justin Szeto, Nazanin~Mohammadi Sepahvand, Edward Raff, Kshitij\n  Madan, Vikram Voleti, Samira~Ebrahimi Kahou, Vincent Michalski, Tal Arbel,\n  Chris Pal, Ga{\\\"e}l Varoquaux, and Pascal Vincent. 2021.\n\\newblock \\href {https://arxiv.org/abs/2103.03098} {Accounting for variance in\n  machine learning benchmarks}.\n\\newblock In \\emph{Proceedings of Machine Learning and Systems (MLSys)}.\n\n\\bibitem[{Brennan(2001)}]{brennan2001generalizability}\nRobert~L. Brennan. 2001.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer.\n\n\\bibitem[{Bui et~al.(2025)Bui, Savova, and Wang}]{bui2025seeds}\nNgoc~Thang Bui, Guergana Savova, and Lijun Wang. 2025.\n\\newblock \\href {https://aclanthology.org/2025.ijcnlp-short.3/} {Assessing the\n  macro and micro effects of random seeds on fine-tuning large language\n  models}.\n\\newblock In \\emph{Proceedings of IJCNLP-AACL}.\n\n\\bibitem[{Burnell et~al.(2023)Burnell, Schellaert, Burden\n  et~al.}]{burnell2023rethink}\nRyan Burnell, Wout Schellaert, John Burden, and 1 others. 2023.\n\\newblock \\href {https://doi.org/10.1126/science.adf6369} {Rethink reporting of\n  evaluation results in {AI}}.\n\\newblock \\emph{Science}, 380(6641):136--138.\n\n\\bibitem[{Camuffo et~al.(2026)Camuffo, Gambardella, Kazemi, Malachowski, and\n  Pandey}]{varannot2026gtheory}\nArnaldo Camuffo, Alfonso Gambardella, Saeid Kazemi, Jakub Malachowski, and\n  Abhinav Pandey. 2026.\n\\newblock \\href {https://arxiv.org/abs/2601.02370} {Variance-aware {LLM}\n  annotation for strategy research: Sources, diagnostics, and a protocol for\n  reliable measurement}.\n\\newblock \\emph{arXiv preprint arXiv:2601.02370}.\n\n\\bibitem[{Cardinet et~al.(2010)Cardinet, Johnson, and\n  Pini}]{cardinet2010applying}\nJean Cardinet, Sandra Johnson, and Gianreto Pini. 2010.\n\\newblock \\emph{Applying Generalizability Theory Using {EduG}}.\n\\newblock Routledge.\n\n\\bibitem[{Clauser and Mazor(1998)}]{clauser1998dif}\nBrian~E. Clauser and Kathleen~M. Mazor. 1998.\n\\newblock \\href {https://doi.org/10.1111/j.1745-3992.1998.tb00619.x} {Using\n  statistical procedures to identify differentially functioning test items}.\n\\newblock \\emph{Educational Measurement: Issues and Practice}, 17(1):31--44.\n\n\\bibitem[{Dehghani et~al.(2021)Dehghani, Tay, Gritsenko, Zhao, Houlsby, Diaz,\n  Metzler, and Vinyals}]{dehghani2021benchmark}\nMostafa Dehghani, Yi~Tay, Alexey~A. Gritsenko, Zhe Zhao, Neil Houlsby, Fernando\n  Diaz, Donald Metzler, and Oriol Vinyals. 2021.\n\\newblock \\href {https://arxiv.org/abs/2107.07002} {The benchmark lottery}.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}.\n\n\\bibitem[{Dodge et~al.(2020)Dodge, Ilharco, Schwartz, Farhadi, Hajishirzi, and\n  Smith}]{dodge2020finetuning}\nJesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali Farhadi, Hannaneh Hajishirzi,\n  and Noah~A. Smith. 2020.\n\\newblock \\href {https://arxiv.org/abs/2002.06305} {Fine-tuning pretrained\n  language models: Weight initializations, data orders, and early stopping}.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}.\n\n\\bibitem[{Efron and Tibshirani(1993)}]{efron1993bootstrap}\nBradley Efron and Robert~J. Tibshirani. 1993.\n\\newblock \\emph{An Introduction to the Bootstrap}.\n\\newblock Chapman \\& Hall, New York.\n\n\\bibitem[{Freiesleben(2026)}]{freiesleben2026construct}\nTimo Freiesleben. 2026.\n\\newblock \\href {https://arxiv.org/abs/2603.15121} {Establishing construct\n  validity in {LLM} capability benchmarks requires nomological networks}.\n\\newblock \\emph{arXiv preprint arXiv:2603.15121}.\n\n\\bibitem[{Gao et~al.(2024)Gao, Tow, Abbasi, Biderman, Black, DiPofi, Foster,\n  Golber, Hsu, Le~Noac'h, Li, McDonell, Muennighoff, Ocqueteau, Phang,\n  Reynolds, Schoelkopf, Skowron, Sutawika, Tang, Thite, Wang, Wang, and\n  Zou}]{gao2024lmeval}\nLeo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony\n  DiPofi, Charles Foster, Laurence Golber, Jeffrey Hsu, Alain Le~Noac'h, Haonan\n  Li, Kyle McDonell, Niklas Muennighoff, Chris Ocqueteau, Jason Phang, Laria\n  Reynolds, Hailey Schoelkopf, Aviya Skowron, Lintang Sutawika, and 5 others.\n  2024.\n\\newblock \\href {https://doi.org/10.5281/zenodo.10256836} {A framework for\n  few-shot language model evaluation}.\n\n\\bibitem[{Gema et~al.(2025)Gema, Leang, Hong, Devoto, Mancino, Saxena, He,\n  Zhao, Du, Ghasemi~Madani, Barale, McHardy, Harris, Kaddour, Van~Krieken, and\n  Minervini}]{gema2025mmlu}\nAryo~Pradipta Gema, Joshua Ong~Jun Leang, Giwon Hong, Alessio Devoto, Alberto\n  Carlo~Maria Mancino, Rohit Saxena, Xuanli He, Yu~Zhao, Xiaotang Du,\n  Mohammad~Reza Ghasemi~Madani, Claire Barale, Robert McHardy, Joshua Harris,\n  Jean Kaddour, Emile Van~Krieken, and Pasquale Minervini. 2025.\n\\newblock \\href {https://doi.org/10.18653/v1/2025.naacl-long.262} {Are we done\n  with {MMLU}?}\n\\newblock In \\emph{Proceedings of the Conference of the North American Chapter\n  of the Association for Computational Linguistics (NAACL)}.\n\n\\bibitem[{Golchin and Surdeanu(2023)}]{golchin2023contamination}\nShahriar Golchin and Mihai Surdeanu. 2023.\n\\newblock \\href {https://arxiv.org/abs/2308.08493} {Time travel in {LLM}s:\n  Tracing data contamination in large language models}.\n\\newblock \\emph{arXiv preprint arXiv:2308.08493}.\n\n\\bibitem[{He and {Thinking Machines Lab}(2025)}]{thinkingmachines2025batch}\nHaiyang He and {Thinking Machines Lab}. 2025.\n\\newblock \\href {https://doi.org/10.64434/tml.20250910} {Defeating\n  nondeterminism in {LLM} inference}.\n\\newblock Thinking Machines Lab: Connectionism.\n\n\\bibitem[{Henderson et~al.(2018)Henderson, Islam, Bachman, Pineau, Precup, and\n  Meger}]{henderson2018deep}\nPeter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup,\n  and David Meger. 2018.\n\\newblock \\href {https://arxiv.org/abs/1709.06560} {Deep reinforcement learning\n  that matters}.\n\\newblock In \\emph{Proceedings of the AAAI Conference on Artificial\n  Intelligence}.\n\n\\bibitem[{Holland and Wainer(1993)}]{holland1993dif}\nPaul~W. Holland and Howard Wainer, editors. 1993.\n\\newblock \\emph{Differential Item Functioning}.\n\\newblock Lawrence Erlbaum Associates, Hillsdale, NJ.\n\n\\bibitem[{Hua et~al.(2025)Hua, Tang, Gu, Gu, Wong, and Qin}]{hua2025flaw}\nAngie Hua, Kevin Tang, Chaoqun Gu, Jing Gu, Edmund Wong, and Yilin Qin. 2025.\n\\newblock \\href {https://aclanthology.org/2025.emnlp-main.1006/} {Flaw or\n  artifact? rethinking prompt sensitivity in evaluating {LLM}s}.\n\\newblock In \\emph{Proceedings of the Conference on Empirical Methods in\n  Natural Language Processing (EMNLP)}.\n\n\\bibitem[{Jiang and Skorupski(2018)}]{jiang2018bayesian}\nZhehan Jiang and William Skorupski. 2018.\n\\newblock \\href {https://doi.org/10.3758/s13428-017-0986-3} {A {Bayesian}\n  approach to estimating variance components within a multivariate\n  generalizability theory framework}.\n\\newblock \\emph{Behavior Research Methods}, 50.\n\n\\bibitem[{Kearns(2026)}]{kearns2026construct}\nRyan~Othniel Kearns. 2026.\n\\newblock \\href {https://arxiv.org/abs/2602.15532} {Quantifying construct\n  validity in large language model evaluations}.\n\\newblock \\emph{arXiv preprint arXiv:2602.15532}.\n\n\\bibitem[{Kiela et~al.(2021)Kiela, Bartolo, Nie, Kaushik, Geiger, Wu, Vidgen,\n  Prasad, Singh, Ringshia, Ma, Thrush, Riedel, Waseem, Stenetorp, Jia, Bansal,\n  Potts, and Williams}]{kiela2021dynabench}\nDouwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger,\n  Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia,\n  Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Waseem, Pontus Stenetorp,\n  Robin Jia, Mohit Bansal, Christopher Potts, and Adina Williams. 2021.\n\\newblock Dynabench: Rethinking benchmarking in {NLP}.\n\\newblock In \\emph{Proceedings of the 2021 Conference of the North American\n  Chapter of the Association for Computational Linguistics (NAACL)}.\n\n\\bibitem[{Kipnis et~al.(2025)Kipnis, Voudouris, Schulze~Buschoff, and\n  Schulz}]{kipnis2025metabench}\nAlex Kipnis, Konstantinos Voudouris, Luca Schulze~Buschoff, and Eric Schulz.\n  2025.\n\\newblock \\href {https://arxiv.org/abs/2407.12844} {metabench -- a sparse\n  benchmark of reasoning and knowledge in large language models}.\n\\newblock In \\emph{Proceedings of the International Conference on Learning\n  Representations}.\n\n\\bibitem[{Kunievsky and Evans(2025)}]{kunievsky2025intent}\nNitzan Kunievsky and James~A. Evans. 2025.\n\\newblock \\href {https://arxiv.org/abs/2506.16584} {Measuring intent\n  comprehension in {LLM}s: A variance decomposition framework}.\n\\newblock \\emph{arXiv preprint arXiv:2506.16584}.\n\n\\bibitem[{Lalor et~al.(2019)Lalor, Wu, and Yu}]{lalor2019irt}\nJohn~P. Lalor, Hao Wu, and Hong Yu. 2019.\n\\newblock \\href {https://aclanthology.org/D19-1434/} {Learning latent\n  parameters without human response patterns: Item response theory with\n  artificial crowds}.\n\\newblock In \\emph{Proceedings of the Conference on Empirical Methods in\n  Natural Language Processing and International Joint Conference on Natural\n  Language Processing (EMNLP-IJCNLP)}.\n\n\\bibitem[{Li(2023)}]{li2023bootstrap}\nGuangming Li. 2023.\n\\newblock \\href {https://doi.org/10.1371/journal.pone.0288069} {Which method is\n  optimal for estimating variance components and their variability in\n  generalizability theory? {Evidence} from a set of unified rules for bootstrap\n  method}.\n\\newblock \\emph{PLoS ONE}.\n\n\\bibitem[{Li et~al.(2025)Li, Tang, Chen, Cheng, Metoyer, Hua, and\n  Chawla}]{li2025atlas}\nPeiyu Li, Xiuxiu Tang, Si~Chen, Ying Cheng, Ronald Metoyer, Ting Hua, and\n  Nitesh~V. Chawla. 2025.\n\\newblock \\href {https://arxiv.org/abs/2511.04689} {Adaptive testing for {LLM}\n  evaluation: A psychometric alternative to static benchmarks}.\n\\newblock \\emph{arXiv preprint arXiv:2511.04689}.\n\n\\bibitem[{Liang et~al.(2023)Liang, Bommasani, Lee, Tsipras, Soylu, Yasunaga,\n  Zhang, Narayanan, Wu, Kumar et~al.}]{liang2023helm}\nPercy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu,\n  Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar,\n  and 1 others. 2023.\n\\newblock Holistic evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2211.09110}.\n\n\\bibitem[{Madaan et~al.(2024)Madaan, Bhatia, Tulio~Ribeiro, and\n  Roth}]{madaan2024quantifying}\nLovish Madaan, Samarth Bhatia, Marco Tulio~Ribeiro, and Dan Roth. 2024.\n\\newblock \\href {https://arxiv.org/abs/2406.10229} {Quantifying variance in\n  evaluation benchmarks}.\n\\newblock \\emph{arXiv preprint arXiv:2406.10229}.\n\n\\bibitem[{Magnusson et~al.(2023)Magnusson, Smith, and\n  Dodge}]{magnusson2023reproducibility}\nIan Magnusson, Noah~A. Smith, and Jesse Dodge. 2023.\n\\newblock \\href {https://aclanthology.org/2023.findings-acl.809/}\n  {Reproducibility in {NLP}: What have we learned from the checklist?}\n\\newblock In \\emph{Findings of the Association for Computational Linguistics\n  (ACL)}.\n\n\\bibitem[{Maia~Polo et~al.(2024)Maia~Polo, Weber, Choshen, Sun, Xu, and\n  Yurochkin}]{polo2024tinybenchmarks}\nFelipe Maia~Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and\n  Mikhail Yurochkin. 2024.\n\\newblock \\href {https://arxiv.org/abs/2402.14992} {{tinyBenchmarks}:\n  Evaluating {LLM}s with fewer examples}.\n\\newblock In \\emph{Proceedings of the International Conference on Machine\n  Learning (ICML)}.\n\n\\bibitem[{Meredith(1993)}]{meredith1993measurement}\nWilliam Meredith. 1993.\n\\newblock \\href {https://doi.org/10.1007/BF02294825} {Measurement invariance,\n  factor analysis and factorial invariance}.\n\\newblock \\emph{Psychometrika}, 58(4):525--543.\n\n\\bibitem[{Messina and Scotta(2026)}]{messina2026background}\nAlberto Messina and Sara Scotta. 2026.\n\\newblock \\href {https://arxiv.org/abs/2604.22411} {Introducing background\n  temperature to characterise hidden randomness in large language models}.\n\\newblock \\emph{arXiv preprint arXiv:2604.22411}.\n\n\\bibitem[{Messing(2026)}]{messing2026hidden}\nSolomon Messing. 2026.\n\\newblock \\href {https://arxiv.org/abs/2604.11581} {Hidden measurement error in\n  {LLM} pipelines distorts annotation, evaluation, and benchmarking}.\n\\newblock \\emph{arXiv preprint arXiv:2604.11581}.\n\n\\bibitem[{Mizrahi et~al.(2024)Mizrahi, Kaplan, Malkin, Dror, Shahaf, and\n  Stanovsky}]{mizrahi2024state}\nMoran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel\n  Stanovsky. 2024.\n\\newblock \\href {https://doi.org/10.1162/tacl_a_00681} {State of what art? {A}\n  call for multi-prompt {LLM} evaluation}.\n\\newblock \\emph{Transactions of the Association for Computational Linguistics},\n  12:933--949.\n\n\\bibitem[{Mushquash and O'Connor(2006)}]{mushquash2006gtheory}\nCilia Mushquash and Brian~P. O'Connor. 2006.\n\\newblock \\href {https://doi.org/10.3758/BF03192810} {{SPSS} and {SAS} programs\n  for generalizability theory analyses}.\n\\newblock \\emph{Behavior Research Methods}.\n\n\\bibitem[{Oren et~al.(2024)Oren, Meister, Chatterji, Ladhak, and\n  Hashimoto}]{oren2024proving}\nYonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and\n  Tatsunori~B. Hashimoto. 2024.\n\\newblock \\href {https://arxiv.org/abs/2310.17623} {Proving test set\n  contamination in black box language models}.\n\\newblock In \\emph{Proceedings of the International Conference on Learning\n  Representations (ICLR)}.\n\\newblock Outstanding Paper Honorable Mention.\n\n\\bibitem[{Perlitz et~al.(2023)Perlitz, Bandel, Gera, Arviv, Ein-Dor, Shnarch,\n  Slonim, Shmueli-Scheuer, and Choshen}]{perlitz2023efficient}\nYotam Perlitz, Elron Bandel, Ariel Gera, Ofir Arviv, Liat Ein-Dor, Eyal\n  Shnarch, Noam Slonim, Michal Shmueli-Scheuer, and Leshem Choshen. 2023.\n\\newblock \\href {https://arxiv.org/abs/2308.11696} {Efficient benchmarking of\n  language models}.\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}.\n\n\\bibitem[{Pezeshkpour and Hruschka(2024)}]{pezeshkpour2024ordering}\nPouya Pezeshkpour and Estevam Hruschka. 2024.\n\\newblock \\href {https://aclanthology.org/2024.findings-naacl.130/} {Large\n  language models sensitivity to the order of options in multiple-choice\n  questions}.\n\\newblock In \\emph{Findings of the North American Chapter of the Association\n  for Computational Linguistics (NAACL)}.\n\n\\bibitem[{Putnick and Bornstein(2016)}]{putnick2016measurement}\nDiane~L. Putnick and Marc~H. Bornstein. 2016.\n\\newblock \\href {https://doi.org/10.1016/j.dr.2016.06.004} {Measurement\n  invariance conventions and reporting: {The} state of the art and future\n  directions for psychological research}.\n\\newblock \\emph{Developmental Review}, 41:71--90.\n\n\\bibitem[{Qian et~al.(2026)Qian, Huang, Xu et~al.}]{qian2026benchmark}\nQi~Qian, Chengsong Huang, Jingwen Xu, and 1 others. 2026.\n\\newblock Benchmark$^2$: Systematic evaluation of llm benchmarks.\n\\newblock \\emph{arXiv preprint arXiv:2601.03986}.\n\n\\bibitem[{Rodriguez et~al.(2021)Rodriguez, Barrow, Hoyle, Lalor, Jia, and\n  Boyd-Graber}]{rodriguez2021leaderboards}\nPedro Rodriguez, Joe Barrow, Alexander Hoyle, John~P. Lalor, Robin Jia, and\n  Jordan Boyd-Graber. 2021.\n\\newblock \\href {https://aclanthology.org/2021.acl-long.346/} {Evaluation\n  examples are not equally informative: How should that change {NLP}\n  leaderboards?}\n\\newblock In \\emph{Proceedings of the Association for Computational Linguistics\n  (ACL)}.\n\n\\bibitem[{Romanou et~al.(2026)Romanou, Ibrahim, Ross, Shaib, Oktar, Bell,\n  Ovalle, Dodge, Bosselut, Sinha, and Williams}]{brittlebench2026}\nAngelika Romanou, Marah Ibrahim, Candace Ross, Chantal Shaib, Kerem Oktar,\n  Samuel~J. Bell, Anaelia Ovalle, Jesse Dodge, Antoine Bosselut, Koustuv Sinha,\n  and Adina Williams. 2026.\n\\newblock \\href {https://arxiv.org/abs/2603.13285} {Brittlebench: Quantifying\n  {LLM} robustness via prompt sensitivity}.\n\\newblock \\emph{arXiv preprint arXiv:2603.13285}.\n\n\\bibitem[{Saxon et~al.(2024)Saxon, Holtzman, West, Wang, and\n  Saphra}]{saxon2024metrology}\nMichael Saxon, Ari Holtzman, Peter West, William~Yang Wang, and Naomi Saphra.\n  2024.\n\\newblock \\href {https://arxiv.org/abs/2407.16711} {Benchmarks as microscopes:\n  A call for model metrology}.\n\\newblock In \\emph{Proceedings of the Conference on Language Modeling (COLM)}.\n\n\\bibitem[{Sclar et~al.(2024)Sclar, Choi, Tsvetkov, and\n  Suhr}]{sclar2024formatting}\nMelanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. 2024.\n\\newblock \\href {https://arxiv.org/abs/2310.11324} {Quantifying language\n  models' sensitivity to spurious features in prompt design or: How {I} learned\n  to start worrying about prompt formatting}.\n\\newblock In \\emph{Proceedings of the International Conference on Learning\n  Representations (ICLR)}.\n\n\\bibitem[{Shanmugavelu et~al.(2024)Shanmugavelu, Taillefumier, Culver,\n  Hernandez, Coletti, and Sedova}]{shanmugavelu2024floating}\nSanjif Shanmugavelu, Mathieu Taillefumier, Christopher Culver, Oscar Hernandez,\n  Mark Coletti, and Ada Sedova. 2024.\n\\newblock \\href {https://doi.org/10.1109/SCW63240.2024.00028} {Impacts of\n  floating-point non-associativity on reproducibility for {HPC} and deep\n  learning applications}.\n\\newblock In \\emph{SC'24 Workshops (IEEE)}.\n\n\\bibitem[{Shavelson and Webb(1991)}]{shavelson1991generalizability}\nRichard~J. Shavelson and Noreen~M. Webb. 1991.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock SAGE Publications.\n\n\\bibitem[{Shavelson et~al.(1989)Shavelson, Webb, and\n  Rowley}]{shavelson1989gtheory}\nRichard~J. Shavelson, Noreen~M. Webb, and Glenn~L. Rowley. 1989.\n\\newblock \\href {https://psycnet.apa.org/record/1989-34789-001}\n  {Generalizability theory}.\n\\newblock \\emph{American Psychologist}.\n\n\\bibitem[{Song et~al.(2025)Song, Lee, and Jiao}]{song2025gtheory}\nDan Song, Won-Chan Lee, and Hong Jiao. 2025.\n\\newblock \\href {https://arxiv.org/abs/2507.19980} {Exploring {LLM} autoscoring\n  reliability in large-scale writing assessments using generalizability\n  theory}.\n\\newblock \\emph{arXiv preprint arXiv:2507.19980}.\n\n\\bibitem[{Tuerlinckx et~al.(2006)Tuerlinckx, Rijmen, Verbeke, and\n  De~Boeck}]{tuerlinckx2006glmm}\nFrancis Tuerlinckx, Frank Rijmen, Geert Verbeke, and Paul De~Boeck. 2006.\n\\newblock \\href {https://doi.org/10.1348/000711005X79857} {Statistical\n  inference in generalized linear mixed models: A review}.\n\\newblock \\emph{British Journal of Mathematical and Statistical Psychology}.\n\n\\bibitem[{Wang et~al.(2024)Wang, Ma, Zhang, Ni, Chandra, Guo, Ren, Arulraj, He,\n  Jiang, Li, Ku, Wang, Zhuang, Fan, Yue, and Chen}]{wang2024mmlupro}\nYubo Wang, Xueguang Ma, Ge~Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo,\n  Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai\n  Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen. 2024.\n\\newblock \\href {https://arxiv.org/abs/2406.01574} {{MMLU-Pro}: A more robust\n  and challenging multi-task language understanding benchmark}.\n\\newblock In \\emph{Advances in Neural Information Processing Systems (NeurIPS),\n  Datasets and Benchmarks Track}.\n\n\\bibitem[{Webb et~al.(2006)Webb, Shavelson, and Haertel}]{webb2006reliability}\nNoreen~M. Webb, Richard~J. Shavelson, and Edward~H. Haertel. 2006.\n\\newblock \\href {https://doi.org/10.1016/S0169-7161(06)26004-8} {Reliability\n  coefficients and generalizability theory}.\n\\newblock In C.~R. Rao and Sandip Sinharay, editors, \\emph{Handbook of\n  Statistics}, volume~26 of \\emph{Handbook of Statistics}, pages 81--124.\n  Elsevier.\n\n\\bibitem[{Ye et~al.(2025)Ye, Jin, Xie, Zhang, and Song}]{ye2025psychometrics}\nHaoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, and Guojie Song. 2025.\n\\newblock \\href {https://arxiv.org/abs/2505.08245} {Large language model\n  psychometrics: A systematic review of evaluation, validation, and\n  enhancement}.\n\\newblock \\emph{arXiv preprint arXiv:2505.08245}.\n\n\\bibitem[{Yuan et~al.(2025)Yuan, Li, Ding, Xie, Li, Zhao, Wan, Shi, Hu, and\n  Liu}]{yuan2025layercast}\nJuntao Yuan, Haoyang Li, Xingcheng Ding, Weijie Xie, Yue-Jiao Li, Wentao Zhao,\n  Kaiyan Wan, Jiayi Shi, Xiaolu Hu, and Zhouhan Liu. 2025.\n\\newblock \\href {https://arxiv.org/abs/2506.09501} {Understanding and\n  mitigating numerical sources of nondeterminism in {LLM} inference}.\n\\newblock In \\emph{Advances in Neural Information Processing Systems\n  (NeurIPS)}.\n\\newblock Oral presentation.\n\n\\bibitem[{Zhou et~al.(2026)Zhou, Huang, Zhao, Han, Wang, Chen, Yang, Bao, Dong,\n  Xu, Zhu, Cao, and Zhao}]{zhou2026irt}\nHao Zhou, Huifeng Huang, Zhe Zhao, Long Han, Haobo Wang, Ke~Chen, Min Yang,\n  Wanli Bao, Jiaxin Dong, Bo~Xu, Conghui Zhu, Hao Cao, and Tiejun Zhao. 2026.\n\\newblock \\href {https://arxiv.org/abs/2505.15055} {Lost in benchmarks?\n  rethinking large language model benchmarking with item response theory}.\n\\newblock In \\emph{Proceedings of the AAAI Conference on Artificial\n  Intelligence}.\n\\newblock Oral presentation.\n\n\\bibitem[{Zhu et~al.(2026)Zhu, Hua, Miao, and Zhao}]{zhu2026benchmark}\nLongyuan Zhu, Hairan Hua, Linlin Miao, and Bing Zhao. 2026.\n\\newblock \\href {https://arxiv.org/abs/2602.11674} {Benchmark health index: A\n  systematic framework for benchmarking the benchmarks of {LLM}s}.\n\\newblock \\emph{arXiv preprint arXiv:2602.11674}.\n\n\\end{thebibliography}\n",
      "numLines": 475,
      "startLine": 1,
      "totalLines": 475
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the paper files. I need to also read the `acl.sty` and `acl_natbib.bst` files since those are needed for compilation. Let me now proceed with the server-side approach:

1. Prepare the code files (already done in Step 1)
2. Transfer paper files to the server
3. Anonymize
4. Push

Since the paper files are text, I'll transfer them via ssh_execute using heredoc. Let me start the process on the server. I'll need to:
- Create paper directory
- Write all tex files there
- Write bib and bbl files


- Check if the graphicspath in main.tex needs updating since it currently references `../../figures/paper/`

For the anonymous repo, I'm setting up a directory structure with the source code, scripts, tests, data, and paper subdirectories containing all the tex files.

Since paper/main.tex and figures/paper/ are both at the root level in the anon repo, I need to change the graphicspath from `../../figures/paper/` to `../figures/paper/` to reflect the correct relative path.

Now I'm thinking through how to transfer the paper files to the server—base64 encoding each file and decoding on the server side seems like the most reliable approach given LaTeX's special characters.

Actually, I realize I can use a single-quoted heredoc with ssh_execute, which will prevent shell expansion of special characters like $ and \. That's simpler than base64 encoding, so I'll go with that approach and batch the file operations together for efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "1ac9e6d5-d464-4398-81da-430594203be6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XTeDPRqjh1hvTDeWYgqzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20825,
      "cache_read_input_tokens": 60129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20825
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

_source line 59_

所有论文文件已读取。现在需要把论文文件传到服务器上。我将使用 heredoc 方式通过 ssh_execute 写入（单引号 'EOF' 防止变量展开）。先写主要 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "6daed3cd-2580-4f83-8c1c-4caf9eeac0e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XTeDPRqjh1hvTDeWYgqzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20825,
      "cache_read_input_tokens": 60129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20825
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

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01JAgA5g7KecuVNjfk7uuMKm`</summary>

```json
{
  "server": "westd-32570",
  "command": "mkdir -p /tmp/anon_repo/paper && cat << 'TEXEOF' > /tmp/anon_repo/paper/main.tex\n\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\graphicspath{{../figures/paper/}}\n\n\\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n% === INTRODUCTION ===\n\\input{introduction}\n\n% === RELATED WORK ===\n\\input{related_work}\n\n% === METHOD ===\n\\input{method}\n\n% === EXPERIMENTS ===\n\\input{experiments}\n\n% === CONCLUSION ===\n\\input{conclusion}\n\n% === LIMITATIONS ===\n\\input{limitations}\n\n\\bibliography{references}\n\n% === APPENDIX ===\n\\input{appendix}\n\n\\end{document}\nTEXEOF\necho \"main.tex DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "5052f4d2-fa88-4cf6-a9b9-a092f3de6009",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XTeDPRqjh1hvTDeWYgqzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20825,
      "cache_read_input_tokens": 60129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20825
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

_source line 61 · 2026-05-23T19:08:06.234Z_

<details><summary>↩ Tool result · `toolu_01JAgA5g7KecuVNjfk7uuMKm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"main.tex DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "2ffcf54c-8a3d-4a18-88e4-4831755b13d2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"main.tex DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"main.tex DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01MQV2imGBQ7HarjQVsNog41`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/abstract.tex\nLarge Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. We apply Generalizability theory (G-theory) in a fully crossed design with up to seven facets across eight open-weight instruction-tuned models (7--9B parameters) and five benchmarks, totaling approximately 2.3 million evaluation records. D-study projections show that, under binary correctness scoring, a recommended 3-prompt $\\times$ 3-seed design achieves $G \\geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\\times$ item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3$\\times$ more total evaluations for 3$\\times$ fewer items, a tradeoff that favors multi-facet designs when item construction is costly. Model$\\times$item interaction (up to 36\\%) indicates that models differ primarily in which items they find difficult, not in overall ability. Preliminary validation across a 3B--72B parameter range and a cross-family check (Llama-3.1-70B) confirms stable variance structure across architecture families. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.\nTEXEOF\necho \"abstract.tex DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "67d11daf-1e52-4622-bb22-8daaff6b7341",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011h6ib73DBSPsmsUamzF79y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1475,
      "cache_read_input_tokens": 80954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1475
      },
      "output_tokens": 69,
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

_source line 63 · 2026-05-23T19:08:21.240Z_

<details><summary>↩ Tool result · `toolu_01MQV2imGBQ7HarjQVsNog41`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"abstract.tex DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "057fd8fc-bbba-41b3-b430-1c30e4a3b81d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"abstract.tex DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"abstract.tex DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
Now I need to write the introduction.tex, experiments.tex, method.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex, references.bib, and main.bbl. These are large files. Let me do them in batches. I'll also need acl.sty and acl_natbib.bst.

Actually, for the acl.sty and acl_natbib.bst, let me just copy them from the local project directory. But actually - I can't directly transfer files from local to remote. Let me check what format those files are in - they might be standard packages.


Since the bbl file is what's actually needed for compilation and the sty/bst files are standard ACL packages, I'll include all of them. Now I'll start writing the remaining tex files in batches, beginning with the introduction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "5c339846-eee8-40a5-95c0-8f0775948b02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YPjuqCGsHc7fPvgiMkS4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 82429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 500
      },
      "output_tokens": 12,
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

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01As2FmhyJQLss2EzPwrTV5D`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/introduction.tex\n\\section{Introduction}\n\\label{sec:introduction}\n\nIn our analysis of five benchmarks, item selection drives 34--38\\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\\%). On the free-form reasoning task GSM8K, the structure shifts: model$\\times$prompt interaction alone accounts for approximately 9\\%, while item selection drops to 17\\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \\citep{rodriguez2021leaderboards, dehghani2021benchmark}. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks to decompose these sources, quantify their interactions, and compare the resulting variance structure.\n\nExisting studies examine individual variance sources in isolation. \\citet{sclar2024formatting} and BrittleBench \\citep{brittlebench2026} documented 50--76\\% accuracy swings from prompt formatting; \\citet{yuan2025layercast} showed up to 9\\% variation from numerical precision; \\citet{pezeshkpour2024ordering}, \\citet{dodge2020finetuning}, and \\citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \\citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (judge identity: 43.8\\%), but excluded infrastructure facets and cross-benchmark comparison. \\citet{madaan2024quantifying} proposed per-factor metrics without crossing factors. IRT approaches \\citep{polo2024tinybenchmarks, lalor2019irt, zhou2026irt} optimize item selection but ignore prompt, seed, and ordering facets. \\citet{bouthillier2021accounting} established ANOVA-based variance decomposition for ML reproducibility. Three gaps remain: no study has (a) crossed infrastructure and methodology facets in a unified factorial design, (b) compared variance structures across response formats, or (c) translated variance components into design-dependent reproducibility budgets.\n\nWe address these gaps with a multi-benchmark G-theory study \\citep{shavelson1991generalizability, brennan2001generalizability} crossing up to seven facets across eight open-weight 7--9B parameter models and five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), totaling approximately 2.3 million records. D-study projections show that a recommended 3-prompt $\\times$ 3-seed design achieves $G \\geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\\times$ reduction from 552 single-condition items; the full 1,296-condition design further reduces to 55 items as a theoretical ceiling (Figure~\\ref{fig:teaser}). Model$\\times$item interaction (up to 36\\%) indicates that models differ primarily in \\emph{which items} they find difficult \\citep{pezeshkpour2024ordering, polo2024tinybenchmarks}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig0_teaser_dstudy}\n\\caption{D-study projections for MMLU (single-model baseline). A recommended 3-prompt $\\times$ 3-seed design reduces the budget from 552 to 178 items for $G \\geq 0.80$; the full multi-facet design reduces further to 55 items.}\n\\label{fig:teaser}\n\\end{figure}\n\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Design-dependent reproducibility budgets.} A recommended 3-prompt $\\times$ 3-seed design achieves $G \\geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\\times$ reduction over single-condition designs (552 items); the full 1,296-condition design reduces to 55 items (71,280 evaluations). Under binary scoring, BF16 and FP16 require no separate control ($<$0.1\\% interaction). IRT item selection and G-theory protocol optimization compose: IRT-selected 116 items yield $G = 0.457$ single-condition but $G = 0.895$ multi-facet (Table~\\ref{tab:dstudy}).\n\n    \\item \\textbf{Format-associated variance patterns (exploratory).} MC benchmarks concentrate 68--72\\% of variance in item-related components; FF benchmarks disperse to 31--41\\%. This hypothesis-generating observation warrants confirmation with larger benchmark samples.\n\\end{enumerate}\nWe release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.\nTEXEOF\necho \"introduction.tex DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "f4394939-3e1f-4c94-b583-fd71c3d9d765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YPjuqCGsHc7fPvgiMkS4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 82429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 500
      },
      "output_tokens": 12,
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

_source line 66 · 2026-05-23T19:09:02.358Z_

<details><summary>↩ Tool result · `toolu_01As2FmhyJQLss2EzPwrTV5D`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"introduction.tex DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "ff78eb8a-0465-462a-a0f1-96adb587f7be",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"introduction.tex DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"introduction.tex DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 67_

Now I'll write the remaining tex files in parallel to speed things up.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "6e1c9e3a-a0c0-4f87-83df-8bed472ea8d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSSNZTU9iSa2du1mFMNyLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 82929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1677
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

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01SwfA9xSTJEhe4teLempW3f`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/conclusion.tex\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nA recommended 3-prompt $\\times$ 3-seed design reduces item requirements from 552 to 178 for $G \\geq 0.80$, confirmed across five benchmarks under binary scoring; multi-facet designs minimize items when item construction is costly, while single-condition designs suit compute-constrained settings. $G_\\text{item}$ and $G_\\text{model}$ have different bottlenecks---item count for the former, prompt standardization for the latter---providing orthogonal optimization paths: adding items improves item reliability, while controlling prompt and seed conditions improves model discriminability. All budgets assume binary scoring; extending to other model scales and continuous metrics is a priority. We recommend that benchmark designers adopt multi-facet validation (at minimum 3 prompts $\\times$ 3 seeds) as standard practice when sizing pilot studies, and that leaderboard operators average over prompt and seed conditions to improve ranking stability. Code, data, and a D-study calculator will be released upon publication.\nTEXEOF\necho \"conclusion DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "89b323fd-a41e-48e4-8a48-38a2518201fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSSNZTU9iSa2du1mFMNyLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 82929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1677
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

_source line 69 · 2026-05-23T19:09:14.532Z_

<details><summary>↩ Tool result · `toolu_01SwfA9xSTJEhe4teLempW3f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"conclusion DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "26e11399-f463-40c6-ab96-29cea9dcd39f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"conclusion DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"conclusion DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016fT47FnZjDhdDduXvgWXJm`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/limitations.tex\n\\section{Limitations}\n\\label{sec:limitations}\n\nOur eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based or base models. Preliminary scale validation (\\S\\ref{sec:scale_validation}) with Qwen2.5 (3B/7B/72B) and cross-family Llama-3.1-70B confirms consistent variance structure across two architecture families, but validation beyond these two families is needed before extrapolating budget recommendations to arbitrary architectures.\n\nThe benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. All D-study budgets reported in this paper are strictly valid only under binary correctness scoring. Our partial-credit analysis (GSM8K, 8 models) shows $G$ drops from 0.86 to 0.77 (crossed design) with all models showing $G_\\text{partial} < G_\\text{binary}$, suggesting limited transferability to finer-grained scoring rubrics; the analysis is limited to a single benchmark, and its generalizability to other tasks is unknown. Our temperature range (0.0--0.7) does not cover high-temperature regimes ($\\tau > 1.0$) sometimes used in generation tasks. Our design varies few-shot example ordering but not example identity, a known variance source. Results depend on vLLM~0.9.2; different inference engines or vLLM versions may alter CUDA-level nondeterminism patterns.\n\nAll eight models may have encountered benchmark items during pre-training; differential contamination across architectures could inflate model$\\times$item interaction \\citep{golchin2023contamination, oren2024proving}, though consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver. Contamination affects absolute budget estimates but has limited impact on the multi-facet vs.\\ single-condition budget \\emph{ratio}, since both designs are equally exposed to contaminated items.\nTEXEOF\necho \"limitations DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "2402fd63-cfb4-4f34-b7f5-d4219741defa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSSNZTU9iSa2du1mFMNyLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 82929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1677
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

_source line 71 · 2026-05-23T19:09:31.043Z_

<details><summary>↩ Tool result · `toolu_016fT47FnZjDhdDduXvgWXJm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"limitations DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "0cc3283c-4bad-4712-8de6-53548a09be33",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"limitations DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"limitations DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Qp9S2zvzHv5UvjXCCdb5cD`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/related_work.tex\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Variance Decomposition in ML/NLP Evaluation.}\nFactorial decomposition of evaluation variance has roots in the ML reproducibility literature. \\citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Subsequent studies applied similar decomposition to specific evaluation facets \\citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \\citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark (judge identity: 43.8\\%; see Positioning below for detailed comparison). \\citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Holistic evaluation frameworks \\citep{liang2023helm, kiela2021dynabench} standardize multi-scenario comparison but do not decompose variance sources. \\citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \\citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \\citet{burnell2023rethink} called for rethinking evaluation reporting standards; \\citet{saxon2024metrology} advocated model metrology as a framework for rigorous benchmark design. Recently, G-theory has been applied to LLM-based writing assessment \\citep{song2025gtheory} and annotation reliability \\citep{varannot2026gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \\citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across five benchmarks, enabling direct comparison of variance structures across evaluation formats.\n\n\\paragraph{Infrastructure and Prompt Variance.}\nA parallel line of work examines individual variance sources in isolation. \\citet{yuan2025layercast} documented up to 9\\% accuracy variation from numerical precision; \\citet{messina2026background} and \\citet{thinkingmachines2025batch} formalized and mitigated CUDA nondeterminism from floating-point non-associativity. On the methodology side, \\citet{mizrahi2024state} advocated multi-prompt evaluation based on large-scale sensitivity analysis; \\citet{sclar2024formatting} and BrittleBench \\citep{brittlebench2026} found 50--76\\% accuracy swings from prompt formatting; \\citet{hua2025flaw} showed that much of this sensitivity is an artifact of log-likelihood scoring (our generation-based protocol controls for this). \\citet{pezeshkpour2024ordering} and \\citet{alzahrani2024benchmarks} documented ordering and benchmark sensitivity; \\citet{bui2025seeds} and \\citet{biderman2024lessons} documented seed and training sensitivity respectively. Each isolates one factor, precluding interaction estimation. Standardized evaluation frameworks such as lm-evaluation-harness \\citep{gao2024lmeval} reduce implementation variance but do not control prompt, seed, or ordering facets.\n\n\\paragraph{IRT and Efficient Benchmarking.}\nItem Response Theory (IRT) offers a complementary perspective on evaluation design by modeling item difficulty and discrimination parameters. \\citet{lalor2019irt} introduced IRT-based item analysis for NLP benchmarks, and \\citet{rodriguez2021leaderboards} showed that IRT reveals hidden properties of evaluation items that raw accuracy scores obscure. Building on this foundation, \\citet{polo2024tinybenchmarks} developed tinyBenchmarks, using IRT-based subsampling to reduce evaluation cost while preserving ranking accuracy, and \\citet{zhou2026irt} recommended a 116-item subset via PSN-IRT for efficient MMLU evaluation. \\citet{perlitz2023efficient} and \\citet{kipnis2025metabench} explored related strategies for benchmark compression; \\citet{li2025atlas} extended IRT to adaptive testing. Complementary benchmark revision efforts address item quality directly: MMLU-Redux \\citep{gema2025mmlu} identified annotation errors in MMLU, while MMLU-Pro \\citep{wang2024mmlupro} extended it with harder items and expanded option sets. These approaches optimize item selection or quality but do not model variance from prompt, seed, or ordering facets. IRT-selected items evaluated under a single methodological condition can therefore systematically underestimate the number of items required for reliable measurement across diverse evaluation settings.\n\n\\paragraph{Psychometrics Foundations.}\nG-theory \\cite{shavelson1991generalizability, brennan2001generalizability, cardinet2010applying} provides the canonical framework for multi-facet reliability analysis; \\citet{webb2006reliability} detail the random versus fixed facet distinctions central to our model specification. Extensions to binary data include \\citet{mushquash2006gtheory} and logistic-link generalized G-theory \\cite{jiang2018bayesian, tuerlinckx2006glmm}. We operationalize differential item functioning---established as a formal framework by \\citet{holland1993dif} and operationalized via statistical detection procedures by \\citet{clauser1998dif}---as model$\\times$item interaction. Recent psychometric perspectives on LLM evaluation address construct validity \\cite{kearns2026construct, bean2025measuring, freiesleben2026construct} and measurement properties \\cite{ye2025psychometrics}; \\citet{zhu2026benchmark} propose a benchmark health index for systematic meta-evaluation.\n\n\\paragraph{Positioning.}\nClosest to our work, \\citet{messing2026hidden} applied G-theory to LLM evaluation through their TEE framework, decomposing five methodology facets on a single benchmark (judge identity: 43.8\\%). We extend this in three directions: (i) we fix the judge to the model itself, replacing judge identity with infrastructure facets and additional methodology facets (seed, ordering); (ii) we cross facets across five benchmarks, enabling cross-format comparison; and (iii) we translate variance components into reproducibility budgets via D-study projections. The two studies are complementary: TEE characterizes judge selection, while we characterize item-and-protocol selection. Relative to IRT approaches \\citep{polo2024tinybenchmarks, zhou2026irt}, G-theory optimizes an orthogonal dimension: conditions needed for target reliability rather than item discrimination.\nTEXEOF\necho \"related_work DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "b78658e1-1e06-4c5d-9916-50338d42d9b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sFF6XyWAfDqaTVe3PcvbX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 84606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1171
      },
      "output_tokens": 69,
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

_source line 73 · 2026-05-23T19:10:19.003Z_

<details><summary>↩ Tool result · `toolu_01Qp9S2zvzHv5UvjXCCdb5cD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"related_work DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "dcda580e-4757-4f81-bb01-746590974b47",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"related_work DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"related_work DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_017PrVA6vGgrK4VQ61veDtnN`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/experiments.tex\n\\section{Experiments}\n\nAll experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.\n\n\\subsection{Single-Model Baseline}\n\\label{sec:single_model}\n\nWe first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.\n\n\\paragraph{Design.} The G-study crosses six facets: 200 items $\\times$ 3 numerical precisions (BF16, FP16, FP32) $\\times$ 6 prompt templates $\\times$ 6 random seeds $\\times$ 3 temperature levels (0.0, 0.3, 0.7) $\\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).\n\n\\paragraph{Results.} Under binary scoring, item difficulty (\\texttt{item\\_id}) accounts for 58.4\\% of total variance, with the residual term contributing 23.1\\%. All main facet effects are negligible ($<$1\\% each): precision 0.9\\%, prompt template, temperature, seed, and ordering each $<$0.5\\%. The interesting structure appears in item-conditional interactions: prompt$\\times$item is the largest at 5.5\\%, followed by seed$\\times$item (4.7\\%), precision$\\times$item (3.3\\%), temperature$\\times$item (2.9\\%), and ordering$\\times$item (0.8\\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.\n\nThe resulting generalizability coefficient is $G_\\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \\geq 0.80$ is achievable with as few as 55 items in this multi-facet design.\n\nFor text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: temperature dominates at 79.7\\% of variance, and $G_\\text{item}$ collapses to 0.007. This metric-conditional divergence motivates our exclusive use of binary correctness for the remaining analyses.\n\n\\subsection{Cross-Model Variance}\n\nExtending to eight models (BF16 subset, 460,800 records), Table~\\ref{tab:cross_model} shows that item difficulty drops from 58.4\\% to 37.9\\%, while model$\\times$item interaction emerges at 30.2\\% (up to 36\\% across benchmarks, \\S\\ref{sec:format_conditional}). The model main effect is 3--5\\% (MC) and 9--11\\% (FF)\\footnote{Ranges rounded to nearest integer; exact values are 2.8--5.4\\% (MC) and 8.5--10.7\\% (FF) per Table~\\ref{tab:cross_benchmark}.}, confirming that models differ primarily in \\emph{which items} they find difficult rather than in overall ability level (contamination implications in \\S\\ref{sec:limitations}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Variance decomposition for the cross-model MMLU design (8 models, BF16, 460,800 records). Components estimated via Henderson Method~I. $G_\\text{item} = 0.896$.}\n\\label{tab:cross_model}\n\\small\n\\begin{tabular}{lr}\n\\toprule\nComponent & Var.\\% \\\\\n\\midrule\n\\textbf{item\\_id} & \\textbf{37.9} \\\\\n\\underline{model$\\times$item} & \\underline{30.2} \\\\\nresidual & 25.0 \\\\\nmodel & 2.8 \\\\\nmodel$\\times$prompt & 1.6 \\\\\nprompt$\\times$item & 0.9 \\\\\ntemp.$\\times$item & 0.6 \\\\\nseed$\\times$item & 0.5 \\\\\nordering$\\times$item & 0.3 \\\\\nall others (each) & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Exploratory: Format-Associated Variance Patterns}\n\\label{sec:format_conditional}\n\nWe extend to five benchmarks (three MC: MMLU, ARC-Challenge, HellaSwag; two FF: GSM8K, MATH) using exp-002 (8 models $\\times$ BF16 $\\times$ 2 temperatures $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 4 orderings $\\times$ 200 items). Table~\\ref{tab:cross_benchmark} reveals a format-associated pattern: MC benchmarks concentrate item-related variance (item + model$\\times$item DIF) at 68--72\\%, while FF benchmarks disperse it to 31--41\\% ($n = 5$; permutation $p = 0.10$; item-level $d = 1.73$, benchmark-level CI spans zero); we report this as a descriptive observation. This does not extend to item budgets: HellaSwag (MC, 118 items for $G \\geq 0.80$) exceeds ARC (98) and MATH (101), showing format alone does not predict evaluation cost (Figure~\\ref{fig:cross_benchmark}). The factorial design is not fully symmetric: ordering applies only to MMLU, and prompt templates serve format-specific functions, potentially confounding format comparisons. Per-benchmark details---including HellaSwag and ARC exceptions, FF residual analysis, and difficulty dispersion as a variance predictor---are in Appendix~\\ref{app:format_details}. All format-associated findings are conditional on binary scoring (\\S\\ref{sec:binary}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Format-associated variance structure across five benchmarks (exp-002, 8 models). Variance components (\\%) per benchmark; MC = multiple-choice, FF = free-form. Bold = dominant non-residual component. $^\\dagger$For MC, reports prompt$\\times$item interaction (prompt main effect $<$1\\%); for FF, reports prompt main effect (item-conditional interactions absorbed into residual).}\n\\label{tab:cross_benchmark}\n\\scriptsize\n\\begin{tabular}{l rrr rr}\n\\toprule\n & \\multicolumn{3}{c}{MC} & \\multicolumn{2}{c}{FF} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n & MMLU & ARC & Hella. & GSM & MATH \\\\\n\\midrule\n\\textbf{item} & \\textbf{37.9} & \\textbf{37.9} & 34.3 & 16.9 & 24.0 \\\\\nmod.$\\times$item & 30.2 & 33.7 & \\textbf{36.0} & 14.6 & 17.3 \\\\\nmodel & 2.8 & 3.1 & 5.4 & 10.7 & 8.5 \\\\\nprompt$^\\dagger$ & 0.9 & 1.4 & 2.1 & 5.4 & 0.8 \\\\\nmod.$\\times$prmpt & 1.6 & 8.0 & 0.2 & 8.5 & 1.7 \\\\\nresidual & 25.0 & 15.4 & 21.4 & 39.9 & 43.9 \\\\\nall others & 1.6 & 0.5 & 0.6 & 4.0 & 3.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_cross_benchmark}\n\\caption{Variance decomposition (Henderson Method~I) across five benchmarks and eight models. Multiple-choice benchmarks share an item-dominated structure; HellaSwag is the exception where model$\\times$item (36.0\\%) exceeds item difficulty (34.3\\%). Free-form benchmarks (GSM8K, MATH) distribute variance across item, model, and interaction components with no single dominant source.}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsection{Precision Separability}\n\nUnder binary scoring, BF16 and FP16 are functionally interchangeable ($<$0.1\\% interaction \\cite{yuan2025layercast}); under text-exact-match, a precision$\\times$temperature interaction emerges at 1.3\\%, consistent with \\S\\ref{sec:single_model}. Precision need not be controlled for binary evaluation at BF16/FP16 \\cite{shanmugavelu2024floating}.\n\n\\subsection{Design-Dependent Reproducibility Budgets}\n\\label{sec:dstudy_budgets}\n\nHow many items does a given evaluation design need to achieve a target reliability? We translate variance components into item budgets via D-study projections.\n\nTable~\\ref{tab:dstudy} compares evaluation designs at the $G \\geq 0.80$ threshold using single-model (Llama-3.1-8B-Instruct) MMLU variance components. The multi-facet design (1,296 conditions per item) achieves $G = 0.936$ at 200 items and requires only 55 items for $G \\geq 0.80$. A single-condition design reaches only $G = 0.592$ at 200 items and requires 552 items---a 10.0$\\times$ budget ratio stable across subset sizes (CV = 1.9\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study reproducibility budgets under different evaluation designs (single-model, MMLU). Total evals = items $\\times$ conditions.}\n\\label{tab:dstudy}\n\\scriptsize\n\\begin{tabular}{lcrrrc}\n\\toprule\nDesign & Cond. & $n_{G{\\geq}.80}$ & Total & $G_{200}$ & $G_{116}$ \\\\\n\\midrule\nMulti-facet & 1{,}296 & \\textbf{55} & 71{,}280 & \\textbf{.936} & --- \\\\\nSingle-cond. & 1 & 552 & 552 & .592 & .457 \\\\\nIRT+multi & 1{,}296 & --- & 150{,}336 & --- & .895$^\\ddagger$ \\\\\n\\midrule\nIRT baseline & --- & 116 & 116 & --- & .457$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$\\,PSN-IRT 116 items \\cite{zhou2026irt} under single-condition: $G = 0.457$. $^\\ddagger$\\,Same 116 items under multi-facet: $G = 0.895$.}\n\\end{table}\n\n\\citet{zhou2026irt}'s IRT-selected 116 items yield $G = 0.457$ under single-condition but $G = 0.895$ under multi-facet conditions, demonstrating that IRT item selection and G-theory protocol optimization are orthogonal and complementary. An internal consistency check using four-model subsets confirms projection stability ($|\\Delta G| \\leq 0.029$ for MC, $\\leq 0.065$ for FF; Table~\\ref{tab:forward_pred}).\n\nFor practitioners, the design choice depends on the evaluation bottleneck: the full 1,296-condition design minimizes items (55 items, 71,280 evaluations per model); the recommended 3-prompt $\\times$ 3-seed design balances cost and reliability (178 items, 1,602 evaluations)\\footnote{The additional conditions require approximately 8 GPU-minutes per model across five benchmarks on a single accelerator, making the multi-facet overhead negligible relative to its diagnostic value.}; single-condition designs require 552 items at minimal per-item cost. Multi-facet designs suit settings where item construction is expensive (e.g., expert-crafted benchmarks); more items under fewer conditions suit compute-constrained evaluation (adoption gradient in Appendix~\\ref{app:intermediate_dstudy}). Cross-model projections show budget ratios of 11--22$\\times$ across benchmarks (bootstrap CIs all exceed 10$\\times$; Appendix~\\ref{app:dstudy_cross}), with multi-facet budgets of 93--128 items (95\\% bootstrap CIs spanning 71--162; Table~\\ref{tab:dstudy_cross}).\n\n\\paragraph{Projection assumptions.} Cross-model budgets increase to 93 items because model$\\times$item interaction enters relative error variance. Bootstrap CIs (71--162 items) and LOMO analysis (Appendix~\\ref{app:robustness}) assess stability; $G_\\text{item}$ is stable across benchmarks (0.863--0.896, CV = 1.4\\%; Appendix~\\ref{app:cross_benchmark_transfer}). All projections assume the 2024--2025 model generation; the 72B extension (\\S\\ref{sec:scale_validation}) provides preliminary support.\n\n\\subsection{Preliminary Scale Validation}\n\\label{sec:scale_validation}\n\nWithin-family analysis (Qwen2.5 3B/7B/72B on MMLU) shows qualitatively invariant variance structure: item difficulty dominates at all three scales (73--83\\%, all $G > 0.95$) with consistent facet ranking. The proportional increase at 72B is consistent with the Bernoulli variance ceiling: total variance (0.113) matches $p(1{-}p)$ at grand mean 0.87, compressing all components while item difficulty---the hardest to eliminate---retains the largest share. A crossed 3B$\\times$7B$\\times$72B design yields model$\\times$item = 38.5\\% $>$ item = 35.7\\%, reflecting expected DIF amplification across a 68--87\\% accuracy range ($G_\\text{item} = 0.720$; three models insufficient). The out-of-sample 72B provides preliminary within-family evidence that variance structure is stable across a 24$\\times$ parameter range within Qwen2.5. A cross-family check with Llama-3.1-70B-Instruct (same protocol, BF16, TP=4) yields item difficulty = 74.5\\% ($G_\\text{item} = 0.957$), confirming the item-dominated structure across architecturally distinct families: all main effects are zero, and the facet ranking matches Qwen2.5-72B. The 8.8pp item share gap (74.5\\% vs.\\ 83.3\\%) reflects accuracy-dependent Bernoulli ceiling compression, not structural divergence.\n\n\\paragraph{Robustness checks.} Three MMLU resamples yield CV = 3.1\\%; treating models as fixed increases $G$ by 0.077--0.113, confirming conservative budgets (\\S\\ref{sec:model_facet}; seven additional analyses in Appendix~\\ref{app:robustness}).\nTEXEOF\necho \"experiments DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "3499e6ca-b049-409a-8cfd-28bb68f24e56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEP91bD2NqnXvaAgsyvn3h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 85777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1881
      },
      "output_tokens": 72,
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

_source line 75 · 2026-05-23T19:11:54.709Z_

<details><summary>↩ Tool result · `toolu_017PrVA6vGgrK4VQ61veDtnN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"experiments DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "a80340a2-073e-4b70-bc89-9c96aa20427f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"experiments DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"experiments DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01WgD9Qf5AjdxaJH6dXkFEUV`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/method.tex\n\\section{Method and Experimental Design}\n\\label{sec:method}\n\n\\subsection{Generalizability Theory}\n\\label{sec:gtheory}\n\nGeneralizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \\cite{shavelson1991generalizability, brennan2001generalizability}. The \\emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.\n\nA \\emph{G-study} decomposes total observed variance into components $\\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \\cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \\cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \\cite{li2023bootstrap}.\n\nA \\emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:\n\\begin{equation}\nG_\\text{item} = \\frac{\\sigma^2_p}{\\sigma^2_p + \\sigma^2_\\text{rel}}\n\\label{eq:gcoeff}\n\\end{equation}\nwhere $\\sigma^2_\\text{rel} = \\sum_i \\sigma^2_{p \\times f_i} / n_{f_i} + \\sigma^2_\\text{residual} / \\prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \\cite[Ch.~4]{brennan2001generalizability}. A D-study projects reliability for a test averaging over $n_p$ items via $G(n_p) = n_p \\sigma^2_p / (n_p \\sigma^2_p + \\sigma^2_\\text{rel})$, enabling independent verification of all budget projections in Table~\\ref{tab:dstudy}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of evaluation designs \\emph{before} data collection \\cite{shavelson1989gtheory}. We define \\emph{item-related variance} as the sum of the item main effect ($\\sigma^2_p$) and the model$\\times$item interaction ($\\sigma^2_{pM}$). The latter captures differential item functioning (DIF): items whose difficulty ranking changes across models \\cite[Ch.~4]{brennan2001generalizability}. Because DIF is operationally an item-level property---it reflects model-specific item difficulty profiles rather than a global model ability shift---aggregating $\\sigma^2_p + \\sigma^2_{pM}$ provides a unified measure of item-driven variance. We note a semantic difference from educational measurement: person$\\times$item DIF reflects unidirectional person responses to items, whereas model$\\times$item DIF in LLM evaluation simultaneously reflects architecture-specific capability profiles---a dual interpretation. Bundling $\\sigma^2_p + \\sigma^2_{pM}$ has psychometric justification \\cite[Ch.~4]{brennan2001generalizability}, and we report unbundled components throughout to ensure transparency.\n\nIn ML terms, a G-study is a multi-way ANOVA where each facet is a design variable and variance components quantify each variable's contribution; a D-study projects the number of conditions per facet needed for a target reliability $G$, analogous to a signal-to-noise ratio where signal is item difficulty variance and noise is everything that changes across evaluation conditions.\n\nThroughout this paper, we use the following notation: $p$ = item, $M$ = model, $\\pi$ = numerical precision, $\\delta$ = prompt template, $s$ = random seed, $\\tau$ = sampling temperature, $o$ = answer ordering, and $\\sigma^2_x$ = variance component for source $x$.\n\n\\subsection{Experimental Design: MMLU}\n\\label{sec:exp001}\n\nWe design a fully crossed factorial experiment (exp-001) that simultaneously varies seven facets of LLM evaluation on MMLU. Table~\\ref{tab:design_matrix} summarizes the complete design matrix, and Figure~\\ref{fig:design_diagram} illustrates the crossing structure.\n\n\\paragraph{Facets.} Items ($p$): 200 MMLU questions selected via purposive stratified sampling across 10 of MMLU's 57 subjects (20 per subject, deterministic selection with arbitrarily chosen seed 42). The 10 subjects span four disciplinary domains---STEM: abstract algebra, college physics, high school mathematics, computer security; humanities: world religions, philosophy; social sciences: US foreign policy, international law; professional: professional medicine, clinical knowledge---ensuring that variance estimates are not dominated by a single knowledge domain. Resampling stability (CV = 3.1\\%) was evaluated within these 10 subjects; cross-subject generalization remains untested. Models ($M$): eight open-weight 7--9B parameter instruction-tuned models spanning eight architecture families---DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B-Instruct, Mistral-7B-v0.3-Instruct, OLMo-2-7B, Qwen3-8B, and Yi-1.5-9B (full identifiers in Appendix~\\ref{app:models})---treated as a quasi-random facet (\\S\\ref{sec:model_facet}). Numerical precision ($\\pi$): BF16, FP16, and FP32, all evaluated with \\texttt{enforce\\_eager=True} for fair comparison across precision levels. Prompt template ($\\delta$): six surface perturbations of the evaluation instruction \\cite{sclar2024formatting}, varying option layout (lettered vs.\\ numbered), instruction wording (direct vs.\\ contextual), and answer prompt cue for MC benchmarks; for FF benchmarks, templates vary chain-of-thought elicitation strategy (full template text in Appendix~\\ref{app:models}). Random seed ($s$): six fixed values (42, 123, 456, 789, 1024, 2048). Sampling temperature ($\\tau$): three levels (0.0, 0.3, 0.7) spanning deterministic to moderately stochastic decoding. Answer ordering ($o$): four permutations of few-shot demonstration examples (for MMLU; structurally inert for other benchmarks, see \\S\\ref{sec:exp002}) \\cite{pezeshkpour2024ordering}.\n\n\\paragraph{Sample sizes.} The cross-model BF16 balanced subset yields 460,800 records (8 models $\\times$ 200 items $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 2 temperatures $\\times$ 4 orderings). A single-model analysis (Llama) spans all three precisions, yielding 259,200 binary observations across 1,296 fully balanced conditions. The BF16 subset serves as the primary cross-model sample because BF16 is the standard inference precision for these architectures.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fully crossed G-theory design. Exp-001 evaluates MMLU across all facet levels; exp-002 extends to five benchmarks with reduced crossing. $^\\dagger$BF16 balanced subset (2 temperatures: 0.0, 0.7) for cross-model analysis; the full single-model design uses all 3 levels.}\n\\label{tab:design_matrix}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\nFacet & Levels & exp-001 & exp-002 \\\\\n\\midrule\nItem ($p$) & Stratified sample & 200 & 200$\\times$5 \\\\\nModel ($M$) & 8 architecture families & 8 & 8 \\\\\nPrecision ($\\pi$) & BF16 / FP16 / FP32 & 3 & 1 \\\\\nPrompt ($\\delta$) & Paraphrases & 6 & 6 \\\\\nSeed ($s$) & Fixed set & 6 & 6 \\\\\nTemperature ($\\tau$) & 0.0 / 0.3 / 0.7 & 3 & 2 \\\\\nOrdering ($o$) & Demo permutations & 4 & 4 \\\\\n\\midrule\n\\multicolumn{2}{l}{Total records} & 460,800$^\\dagger$ & 2,304,000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_design_diagram}\n\\caption{Fully crossed G-theory design for LLM evaluation. Each observation is a binary correctness score determined by the crossing of seven facets: item ($p$), model ($M$), precision ($\\pi$), prompt ($\\delta$), seed ($s$), temperature ($\\tau$), and ordering ($o$).}\n\\label{fig:design_diagram}\n\\end{figure}\n\n\\subsection{Cross-Benchmark Extension}\n\\label{sec:exp002}\n\nTo test whether the variance structure observed on MMLU generalizes across evaluation formats, exp-002 extends the design to five benchmarks: MMLU, ARC-Challenge, and HellaSwag (multiple-choice), and GSM8K and MATH (free-form generation). The design crosses 8 models $\\times$ BF16 $\\times$ 2 temperatures (0.0, 0.7) $\\times$ 6 prompts $\\times$ 6 seeds $\\times$ 4 orderings $\\times$ 200 items per benchmark, totaling 2,304,000 records. This reduced crossing fixes precision at BF16 and uses two temperature levels to concentrate statistical power on format-associated differences. The ordering facet operates only on MMLU, where it selects among four permutations of the few-shot demonstration examples. For all other benchmarks, the prompt construction does not use the ordering parameter; ordering is structurally inert ($\\sigma^2_{\\text{ordering}} = 0$ by construction) and is retained solely for design balance. The two temperature levels bracket the most common evaluation configurations: deterministic ($\\tau = 0.0$) and a moderate stochastic setting ($\\tau = 0.7$) representative of practical deployment. A subset analysis confirms that this reduced crossing preserves the variance structure of the full design ($\\Delta G = 0.0008$; Appendix~\\ref{app:robustness}).\n\n\n\\subsection{Evaluation Protocol}\n\\label{sec:protocol}\n\nAll evaluations use generation-based scoring (free-text response with answer extraction) rather than log-likelihood ranking, following \\citet{hua2025flaw}. Binary correctness (1/0) is the primary metric; text-exact-match is secondary. Inference uses vLLM~0.9.2 without batch-invariant kernels, preserving CUDA-level nondeterminism as a measurable variance source \\cite{messina2026background, thinkingmachines2025batch}. Few-shot protocols: 5-shot MMLU/ARC, 4-shot MATH, 8-shot GSM8K, 10-shot HellaSwag.\n\n\\subsection{Binary Data Assumptions}\n\\label{sec:binary}\n\nStandard G-theory assumes continuous, approximately normal outcome data \\cite{shavelson1991generalizability}. Our binary correctness scores (0/1) violate this assumption. We establish robustness through simulation and estimator properties, with two additional analyses (GLMM complement, accuracy-range stability) in Appendix~\\ref{app:robustness}.\n\nHenderson Method~I produces unbiased estimates for balanced designs regardless of outcome distribution \\cite[Ch.~12]{brennan2001generalizability}, and REML estimates differ by $<$0.5pp on all components. A probit simulation, GLMM complement ($\\rho = 1.0$), and accuracy-range analysis all confirm robustness (Appendix~\\ref{app:robustness}).\n\nAll findings in this paper are conditioned on binary correctness scoring. This measurement resolution collapses continuous generation quality into a pass/fail outcome, which may amplify item-related variance by reducing within-item response variability and mask finer-grained variance sources (e.g., partial credit, reasoning quality) that would emerge under richer scoring rubrics. The text-exact-match comparison in \\S\\ref{sec:single_model} ($G = 0.007$ vs.\\ $0.936$) illustrates how the scoring metric can fundamentally reshape variance structure. A partial-credit analysis on GSM8K (8 models, step-level scoring) confirms this conditionality: $G_\\text{item}$ drops from 0.86 to 0.77, with all eight models showing $G_\\text{partial} < G_\\text{binary}$ (mean $\\Delta G = -0.135$; Appendix~\\ref{app:robustness}), providing evidence that D-study budgets have limited transferability to finer-grained scoring rubrics.\n\n\\subsection{Model Facet Specification}\n\nOur target universe comprises open-weight, instruction-tuned models in the 7--9B parameter range (eight architecture families); results may not generalize to API-based, base, or $>$9B models. Our eight purposively selected models are treated as a quasi-random facet \\cite{meredith1993measurement, putnick2016measurement}. We report $G$ under random-model assumptions, the more conservative specification: across five benchmarks, treating models as fixed yields $G_\\text{fixed}$ of 0.951--0.990 (mean 0.975) versus $G_\\text{random}$ of 0.863--0.896 (mean 0.882), a consistent increase of 0.077--0.113 (mean 0.093), because model$\\times$item interaction (30--36\\%) enters the relative error variance under random assumptions. Consequently, our D-study budgets are upper bounds---practitioners will not under-sample regardless of facet classification. The variance decomposition itself (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_benchmark}) is invariant to this choice. Leave-one-model-out analysis preserves component rankings across all five benchmarks, and Cohen's $\\kappa$ pairwise agreement (mean $\\kappa = 0.33$--$0.46$) confirms genuine differential item functioning (Appendix~\\ref{app:robustness}). Four-model subset consistency checks match the observed eight-model $G$ within mean $|\\Delta G| = 0.035$ across all five benchmarks (\\S\\ref{sec:dstudy_budgets}).\n\nFor reference, $G_\\text{model}$ (treating models as the object of measurement) under the recommended 3-prompt $\\times$ 3-seed design with 200 items averages 0.79 across five benchmarks (range: 0.52 on ARC to 0.93 on HellaSwag). Model ranking reliability depends primarily on model$\\times$prompt interaction---ARC (8.0\\%) and GSM8K (8.5\\%) show lower $G_\\text{model}$ because prompt sensitivity reduces model discriminability. $G_\\text{item}$ remains the primary metric because item reliability is the direct optimization target for evaluation design; model reliability is a downstream consequence that improves with item count.\n\\label{sec:model_facet}\nTEXEOF\necho \"method DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "e60d2a97-92fe-49b9-acb2-46414aa50b60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuPPuyRNxg65VirKoWEagi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4075,
      "cache_read_input_tokens": 87658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4075
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

_source line 77 · 2026-05-23T19:13:36.301Z_

<details><summary>↩ Tool result · `toolu_01WgD9Qf5AjdxaJH6dXkFEUV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"method DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "c624c80f-4d2d-4488-a213-d946f5a06f54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"method DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"method DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TjYq9WPup9ZGerfy9GDqRS`</summary>

```json
{
  "server": "westd-32570",
  "command": "cat << 'TEXEOF' > /tmp/anon_repo/paper/appendix.tex\n\\appendix\n\\section{Additional Robustness Analyses}\n\\label{app:robustness}\n\nWe report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.\n\n\\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\\rho = 1.0$) relative to Henderson Method~I \\cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.\n\n\\paragraph{Accuracy-range stability.} The \\texttt{item\\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.\n\n\\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \\cite[Ch.~12]{brennan2001generalizability}.\n\n\\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\\rho = 0.732$ between binary and continuous rankings, excluding residual; \\texttt{item\\_id} dominant in all 100 replications; top-5 ordering correct in 79\\% of replications). Bias analysis by difficulty stratum shows $|\\text{bias}| = 0.28$--$0.37$ for items with $p \\in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This analysis covers the observed accuracy range ($p \\in [0.3, 0.9]$); extreme-difficulty items ($p < 0.3$ or $p > 0.9$) are rare in our sample ($<$8\\% of items) and may exhibit larger deviations. Henderson Method~I absorbs this Bernoulli-inherent variance into the residual, explaining inflated bias near medium difficulty; systematic component ordering is robustly recovered across all replications. Binary scoring inflates residual variance by absorbing the Bernoulli $p(1{-}p)$ ceiling, which enters $\\sigma^2_\\text{rel}$ and increases D-study item requirements. Within a matched probit simulation, binarization increases D-study budgets by approximately 36\\% (99 $\\to$ 135 items for $G \\geq 0.80$), driven by residual inflation (16\\% $\\to$ 41\\%) and item variance compression (50\\% $\\to$ 32\\%). Facet$\\times$item interactions---the components entering $\\sigma^2_\\text{rel}$---are best preserved under binarization (MAPE = 12.8\\%, range 8.7--17.5\\%), while residual variance inflates as expected from Bernoulli $p(1{-}p)$ noise (MAPE = 156\\%). D-study budgets derived from binary data are therefore conservative: continuous-scored designs would require equal or fewer items for the same $G$ threshold. Null calibration (ratio $= 1.0008$) confirms that this conservatism does not distort relative component magnitudes.\n\n\\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. Bootstrap CIs capture item-sampling variability conditional on these 8 specific models; model-level stability is assessed separately via LOMO (below). The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\\sim$127 unique items per 200-item resample) does not materially distort interval estimates. Stratified resampling by subject (10 subjects $\\times$ 20 items) produces CIs within 4\\% of simple item-level bootstrap, confirming that the within-subject dependence structure does not materially affect interval estimates.\n\n\\paragraph{Facet specification sensitivity.} Treating temperature and ordering as fixed (rather than random) facets changes $G_\\text{item}$ by only 0.37 percentage points (all-random: 0.820 vs.\\ fixed temperature+ordering: 0.824). The small difference reflects the negligible temperature$\\times$item (0.65\\%) and ordering$\\times$item (0.54\\%) variance shares. The random-facet assumption is therefore robust to facet classification.\n\n\\paragraph{Leave-one-model-out (LOMO).} Across all 40 leave-one-model-out subsets (8 models $\\times$ 5 benchmarks), $G_\\text{item}$ ranges from 0.833 to 0.919, with CV $\\leq$ 1.25\\% per benchmark. No single model removal changes $G$ by more than 0.030 (GSM8K, removing Gemma-2-9B). Item-related variance rankings are preserved in all 40 subsets. Table~\\ref{tab:lomo_full} reports per-benchmark stability. This supports treating models as exchangeable within the target universe of 7--9B instruction-tuned models (\\S\\ref{sec:model_facet}).\n\n\\begin{table}[h]\n\\centering\n\\caption{LOMO stability across five benchmarks (8 models $\\times$ 5 benchmarks = 40 subsets).}\n\\label{tab:lomo_full}\n\\scriptsize\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & $G_\\text{full}$ & CV (\\%) & Max $|\\Delta G|$ & Most impactful \\\\\n\\midrule\nMMLU & 0.896 & 0.49 & 0.019 & InternLM2.5-7B \\\\\nARC & 0.892 & 0.94 & 0.026 & Llama-3.1-8B \\\\\nHellaSwag & 0.872 & 1.09 & 0.028 & Llama-3.1-8B \\\\\nGSM8K & 0.863 & 1.25 & 0.030 & Gemma-2-9B \\\\\nMATH & 0.888 & 1.20 & 0.029 & InternLM2.5-7B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Inter-model agreement.} We computed pairwise Cohen's $\\kappa$ and Fleiss' $\\kappa$ across all model pairs on each benchmark. Mean pairwise $\\kappa$ ranges from 0.326 (MATH) to 0.461 (MMLU); Fleiss' $\\kappa$ ranges from 0.309 (GSM8K) to 0.456 (MMLU). HellaSwag uses six models ($\\kappa = 0.332$) due to missing OLMo and Yi data. The fair-to-moderate agreement independently confirms that the model$\\times$item interaction (30--36\\% of variance) reflects genuine differential item functioning: models disagree substantially on which items are difficult, consistent with prior DIF findings in educational measurement \\cite{holland1993dif, clauser1998dif}.\n\n\\paragraph{Scoring metric sensitivity.}\n\\label{sec:partial_credit}\nTo probe metric conditionality, we compared binary correctness with step-level partial credit on GSM8K using the full 8-model crossed design (200 items, 2,304 conditions per item). Under partial credit, $G_\\text{item}$ drops from 0.863 to 0.768, with residual variance rising from 39.9\\% to 64.9\\% and item variance falling from 16.9\\% to 10.3\\%. All eight models individually show $G_\\text{partial} < G_\\text{binary}$ (mean $\\Delta G = -0.135$, range $-0.025$ to $-0.309$), with $\\Delta G$ magnitude moderated by model accuracy: higher-accuracy models have fewer incorrect responses whose scores shift under partial credit (e.g., OLMo at 70.1\\% accuracy shows $\\Delta G = -0.025$, while Llama at 49.0\\% shows $\\Delta G = -0.309$). The mechanism is clear: 48.1\\% of incorrect responses have numerically correct arithmetic steps but incorrect problem setup, receiving partial score $= 1.0$ despite binary score $= 0$---this compresses item discrimination and inflates residual variance. Binary scoring amplifies prompt sensitivity by collapsing reasoning quality into pass/fail, confirming that all findings in this paper are metric-conditional.\n\n\\paragraph{Facet specification sensitivity: random vs.\\ fixed model.} Table~\\ref{tab:fixed_vs_random} reports per-benchmark generalizability coefficients under random and fixed model specifications. The consistent $\\Delta G$ of 0.077--0.113 confirms that random-model budgets are strictly more conservative across all benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Generalizability coefficients under random vs.\\ fixed model facet specification across five benchmarks.}\n\\label{tab:fixed_vs_random}\n\\scriptsize\n\\begin{tabular}{lrrr}\n\\toprule\nBenchmark & $G_\\text{random}$ & $G_\\text{fixed}$ & $\\Delta G$ \\\\\n\\midrule\nMMLU & 0.896 & 0.984 & $+$0.088 \\\\\nARC & 0.892 & 0.990 & $+$0.098 \\\\\nHellaSwag & 0.872 & 0.984 & $+$0.113 \\\\\nGSM8K & 0.863 & 0.951 & $+$0.089 \\\\\nMATH & 0.888 & 0.965 & $+$0.077 \\\\\n\\midrule\nMean & 0.882 & 0.975 & $+$0.093 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Null calibration.} We generate 100 Bernoulli-distributed datasets with item difficulties matched to the empirical distribution but no systematic facet effects. The observed-to-null variance ratio is 1.0008, confirming that Henderson Method~I does not introduce systematic bias when applied to binary outcomes. The null simulation also verifies that the item variance share (58.4\\%) is not an artifact of the Bernoulli $p(1{-}p)$ ceiling: the null produces item variance of 0.08\\%, three orders of magnitude below the observed value. Across all 100 replications, the same three components (item, model$\\times$item, residual) emerge as the top three (set consistency 100\\%), with Kendall's $\\tau = 0.81$ between binary and continuous rankings.\n\n\\paragraph{Reduced crossing validation.} To verify that the reduced crossing in exp-002 (BF16 only $\\times$ 2 temperatures) does not introduce confounding, we extracted the corresponding subset from the fully crossed exp-001 design. The generalizability coefficient differs by only 0.0008 ($G = 0.9361$ vs.\\ $0.9369$), and all non-precision variance components differ by less than 2 percentage points. The 10pp increase in item variance share (58.4\\% $\\to$ 68.5\\%) is fully explained by the removal of precision-related components ($\\sim$4.5\\% total), which redistributes across remaining sources. This confirms that the exp-002 design preserves the variance structure of the full crossing.\n\n\\section{Cross-Model D-Study Projections}\n\\label{app:dstudy_cross}\n\nTable~\\ref{tab:dstudy_cross} extends the single-model D-study (Table~\\ref{tab:dstudy} in main text) to per-benchmark cross-model projections with bootstrap confidence intervals (1,000 item-level resamples, 8 models, 2,304 conditions per item). The efficiency ratio is format-associated: MC benchmarks show 11--13$\\times$ (mean 12.0$\\times$ [11.6, 12.5]), while FF benchmarks show 21--22$\\times$ (mean 21.5$\\times$ [20.4, 22.8]).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model D-study reproducibility budgets with 95\\% bootstrap CIs. $n_{G \\geq 0.80}$: items needed. Multi = multi-facet (2,304 cond.); Total = items $\\times$ 2,304. Single = single-condition (total evals = item count).}\n\\label{tab:dstudy_cross}\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l rr r rr r}\n\\toprule\n & \\multicolumn{3}{c}{Multi-facet (2,304 cond.)} & \\multicolumn{2}{c}{Single-cond.} & \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n & Items & 95\\% CI & Total & Items & 95\\% CI & Ratio [95\\% CI] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Multiple-choice}} \\\\\nMMLU & 93 & [76, 116] & 214K & 1{,}216 & [1004, 1491] & 13.1 [12.5, 13.7] \\\\\nARC & 98 & [71, 139] & 226K & 1{,}078 & [793, 1512] & 11.0 [10.7, 11.4] \\\\\nHella. & 118 & [93, 151] & 272K & 1{,}403 & [1120, 1790] & 11.9 [11.5, 12.3] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Free-form}} \\\\\nGSM8K & 128 & [103, 162] & 295K & 2{,}768 & [2230, 3531] & 21.6 [20.7, 23.0] \\\\\nMATH & 101 & [86, 122] & 233K & 2{,}160 & [1853, 2631] & 21.4 [20.2, 22.5] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nThe higher item requirements relative to the single-model analysis (55 items in Table~\\ref{tab:dstudy}) reflect the additional model$\\times$item interaction variance that enters $\\sigma^2_\\text{rel}$ when models are crossed as a facet. The format-associated ratio pattern---FF benchmarks showing $\\sim$2$\\times$ the MC ratio---is consistent with the distributed variance structure observed in \\S\\ref{sec:format_conditional}, where FF benchmarks allocate more variance to model and model$\\times$prompt components.\n\n\\paragraph{Internal consistency check.} Table~\\ref{tab:forward_pred} reports consistency checks from four exp-001 models (DeepSeek, Llama, Mistral, Qwen3) to the full eight-model design across all five benchmarks. MC benchmarks show $|\\Delta G| \\leq 0.029$ ($<$3.5\\% error), while FF benchmarks show larger deviations ($|\\Delta G| \\leq 0.065$, $\\sim$7\\%) due to limited model diversity in the four-model subset. FF predictions consistently underestimate actual $G$ (conservative); MC predictions show mixed directions with small deviations ($|\\Delta G| \\leq 0.029$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Internal consistency: four-model subset vs.\\ eight-model $G_\\text{item}$. FF subsets underestimate actual $G$ (conservative); MC shows mixed directions with small deviations.}\n\\label{tab:forward_pred}\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\nBenchmark & Predicted $G$ & Actual $G$ & $|\\Delta G|$ & Error\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Multiple-choice}} \\\\\nMMLU & 0.888 & 0.896 & 0.009 & 0.96 \\\\\nARC & 0.904 & 0.892 & 0.012 & 1.38 \\\\\nHellaSwag & 0.901 & 0.872 & 0.029 & 3.33 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Free-form}} \\\\\nGSM8K & 0.803 & 0.863 & 0.059 & 6.88 \\\\\nMATH & 0.823 & 0.888 & 0.065 & 7.30 \\\\\n\\midrule\nMean & --- & --- & 0.035 & 3.97 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Budget sensitivity to estimation error.}\n\\label{app:budget_sensitivity}\nFigure~\\ref{fig:budget_sensitivity} shows the effect of $|\\Delta G| = 0.035$ estimation error on item budgets across all five benchmarks. The percentage increase is remarkably stable (23.0--24.5\\%, mean 23.2\\%), because the relative budget adjustment $\\Delta n / n$ depends on the $G$-formula ratio rather than on absolute variance components. Absolute $\\Delta n$ ranges from 13 (ARC) to 67 (GSM8K), scaling with the baseline budget.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{budget_sensitivity_band}\n\\caption{Effect of $|\\Delta G| = 0.035$ estimation error on item budgets across five benchmarks. The $\\sim$23\\% budget increase is consistent across all benchmarks, indicating D-study budgets are robust to estimation uncertainty.}\n\\label{fig:budget_sensitivity}\n\\end{figure}\n\n\\paragraph{Cross-benchmark $G$ stability.}\n\\label{app:cross_benchmark_transfer}\n$G_\\text{item}$ values cluster in a narrow band across all five benchmarks (0.863--0.896, CV = 1.4\\%), despite qualitatively different variance structures: MC benchmarks concentrate 68--72\\% in item-related components while GSM8K disperses variance across item (17\\%), model (11\\%), and interaction (15\\%) sources (Table~\\ref{tab:cross_benchmark}). This stability implies that D-study budget recommendations calibrated on one benchmark provide reasonable order-of-magnitude guidance for others. However, the 0.033 range in $G_\\text{item}$ translates to a 71--128 item range for multi-facet $G \\geq 0.80$ (Table~\\ref{tab:dstudy_cross}), and the variance compositions differ substantially---benchmark-specific G-studies remain necessary to identify dominant variance sources and optimize condition selection.\n\n\\section{Intermediate D-Study Designs}\n\\label{app:intermediate_dstudy}\n\nTable~\\ref{tab:intermediate_dstudy} shows how reliability improves as evaluation designs increase from single-condition to full multi-facet crossing. The steepest gain occurs at the ``minimal upgrade'' level (2 prompts): $G_{200}$ jumps from 0.592 to 0.692 at 2$\\times$ cost. A minimal sufficient design for $G \\geq 0.80$ is 3 prompts $\\times$ 3 seeds (9 conditions, $G_{200} = 0.818$, $n_{G \\geq 0.80} = 178$). Beyond the ``standard'' level (32 conditions), adding orderings provides negligible benefit (ordering$\\times$item $<$1\\%), confirming that prompt and seed diversity are the primary reliability drivers.\n\n\\begin{table}[h]\n\\centering\n\\caption{Intermediate D-study designs (single-model, MMLU). Designs are ordered by increasing conditions per item; $G_{200}$ and $n_{G \\geq 0.80}$ are D-study projections from exp-001 variance components.}\n\\label{tab:intermediate_dstudy}\n\\scriptsize\n\\begin{tabular}{llrrr}\n\\toprule\nDesign & Conditions & $G_{200}$ & $n_{G{\\geq}.80}$ \\\\\n\\midrule\nSingle-condition & 1 & .592 & 552 \\\\\nMinimal upgrade (2p) & 2 & .692 & 357 \\\\\nEasy upgrade (2p$\\times$2s) & 4 & .766 & 245 \\\\\nModerate (3p$\\times$3s) & 9 & .818 & 178 \\\\\nStandard (4p$\\times$4s$\\times$2t) & 32 & .869 & 121 \\\\\nEnhanced (+4 orderings) & 72 & .871 & 119 \\\\\nFull multi-facet & 1{,}296 & .936 & 55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Format-Associated Variance: Per-Benchmark Details}\n\\label{app:format_details}\n\nThis section supplements the compressed format-associated analysis in \\S\\ref{sec:format_conditional} with per-benchmark details.\n\n\\paragraph{MC benchmark exceptions.} HellaSwag is the sole MC case where model$\\times$item slightly exceeds item (36.0\\% vs.\\ 34.3\\%), though their sum (70.3\\%) remains in the MC range (68--72\\%). Among MC benchmarks, ARC-Challenge shows an anomalously high model$\\times$prompt interaction (8.0\\% vs.\\ $<$2\\% for MMLU and HellaSwag), suggesting that science-domain items are differentially sensitive to option formatting across model families.\n\n\\paragraph{FF benchmark patterns.} Free-form benchmarks differ markedly from MC. On GSM8K, variance distributes across item (16.9\\%), model$\\times$item (14.6\\%), model (10.7\\%), and model$\\times$prompt (8.5\\%); prompt main effect is 5.4\\%. MATH shows an intermediate pattern: item leads at 24.0\\% with model$\\times$item at 17.3\\%, but residual variance is substantially larger (43.9\\%). Item-level regression reveals that FF residual variance is predominantly explained by the Bernoulli variance ceiling $p(1{-}p)$ ($R^2 = 0.47$--$0.86$; Appendix~\\ref{app:ff_residual}): medium-difficulty items maximize binary outcome variance regardless of facet structure, so the elevated FF residuals reflect measurement resolution rather than unmodeled substantive sources.\n\n\\paragraph{Difficulty dispersion as variance predictor.} Difficulty dispersion ($\\text{std}(p_i)$) strongly predicts item variance share ($\\rho = 0.82$, $n = 5$ benchmarks; Appendix~\\ref{app:difficulty_scatter}; reasoning-heavy subjects show $G_\\text{item}$ as low as 0.614, Appendix~\\ref{app:subject_gstudy}). Format constrains the noise floor, but difficulty heterogeneity determines variance magnitude within it.\n\n\\section{Cross-Benchmark Difficulty Heterogeneity}\n\\label{app:difficulty_scatter}\n\nFigure~\\ref{fig:difficulty_scatter} plots item difficulty heterogeneity ($\\text{std}(p_i)$ across models) against \\texttt{item\\_id} variance share for all five benchmarks. MC benchmarks cluster at higher dispersion ($0.27$--$0.31$) and higher item variance ($34$--$38\\%$), while FF benchmarks occupy the lower-left region ($0.22$--$0.23$, $17$--$24\\%$). The cross-benchmark Spearman $\\rho = 0.82$ ($p = 0.089$, $n = 5$) is consistent in direction with the within-MMLU correlation ($\\rho = 0.806$, $p = 0.005$, $n = 10$ subjects); these are independent analyses at different granularities (benchmarks vs.\\ subjects within MMLU), providing multi-scale support for the item difficulty heterogeneity mechanism discussed in \\S\\ref{sec:format_conditional}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{fig4_difficulty_scatter}\n\\caption{Item difficulty heterogeneity ($\\text{std}(p_i)$, computed over available models per benchmark, 6--8 models) versus \\texttt{item\\_id} variance share (as reported in Table~\\ref{tab:cross_benchmark}) across five benchmarks. MC benchmarks (filled) exhibit higher difficulty dispersion and item variance than FF benchmarks (open). Spearman $\\rho = 0.82$, $p = 0.089$.}\n\\label{fig:difficulty_scatter}\n\\end{figure}\n\n\\section{MMLU Subject-Level Variance Decomposition}\n\\label{app:subject_gstudy}\n\nTable~\\ref{tab:subject_gstudy} reports per-subject variance decomposition for 10 MMLU subjects (20 items each, 8 models, 2,304 conditions per item). $G_\\text{item}$ ranges from 0.614 (\\texttt{high\\_school\\_mathematics}) to 0.930 (\\texttt{international\\_law}), with mean 0.843. Knowledge-intensive subjects (\\texttt{international\\_law}, \\texttt{clinical\\_knowledge}, \\texttt{world\\_religions}) show \\texttt{item\\_id} $>$ 40\\%, while reasoning-heavy subjects (\\texttt{high\\_school\\_mathematics}, \\texttt{abstract\\_algebra}) show model$\\times$item $>$ \\texttt{item\\_id}, consistent with models differing more in reasoning strategies than in factual recall. The \\texttt{high\\_school\\_mathematics} \\texttt{item\\_id} of 10.4\\% referenced in \\S\\ref{sec:format_conditional} is the lowest across all subjects, below even GSM8K (16.9\\%).\n\n\\begin{table}[h]\n\\centering\n\\caption{Subject-level variance decomposition within MMLU (20 items per subject, 8 models, 2,304 conditions per item). Sorted by $G_\\text{item}$ descending.}\n\\label{tab:subject_gstudy}\n\\scriptsize\n\\begin{tabular}{lrrrr}\n\\toprule\nSubject & Acc. & item\\% & mod.$\\times$it.\\% & $G_\\text{item}$ \\\\\n\\midrule\ninternational\\_law & .717 & 44.4 & 24.1 & .930 \\\\\nclinical\\_knowledge & .581 & 47.5 & 30.0 & .923 \\\\\nworld\\_religions & .826 & 42.2 & 27.1 & .910 \\\\\ncomputer\\_security & .740 & 37.0 & 24.9 & .908 \\\\\ncollege\\_physics & .436 & 31.6 & 30.1 & .876 \\\\\nphilosophy & .782 & 33.0 & 36.1 & .868 \\\\\nabstract\\_algebra & .457 & 24.1 & 32.8 & .822 \\\\\nus\\_foreign\\_policy & .864 & 20.4 & 36.9 & .802 \\\\\nprofessional\\_medicine & .671 & 19.9 & 41.7 & .778 \\\\\nhigh\\_school\\_math & .385 & 10.4 & 41.9 & .614 \\\\\n\\midrule\nMean & --- & 31.1 & 32.6 & .843 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{FF Residual Variance Analysis}\n\\label{app:ff_residual}\n\nTo investigate whether the elevated residual variance in free-form benchmarks (GSM8K 39.9\\%, MATH 43.9\\%) reflects unmodeled substantive sources or measurement properties of binary scoring, we regress item-level residual variance on item characteristics across all five benchmarks (Table~\\ref{tab:ff_residual}).\n\nThe dominant predictor is the quadratic difficulty effect ($p < 10^{-5}$ on all benchmarks): items near $p = 0.5$ show maximal residual variance, while items near the floor or ceiling show minimal residual. This inverted-U pattern directly mirrors the Bernoulli variance ceiling $p(1{-}p)$. Item content features (number of reasoning steps, answer length) are not significant predictors for GSM8K ($p > 0.38$), confirming that the difficulty--residual relationship is statistical rather than content-driven.\n\nFF benchmarks show substantially higher $R^2$ (mean 0.66) than MC benchmarks (mean 0.25), consistent with FF items spanning a wider difficulty range. The MC--FF contrast in residual magnitude is therefore a mathematical consequence of the difficulty distribution under binary scoring, not evidence of additional unmodeled variance sources in free-form evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Item-level residual variance regression. Difficulty$^2$ = quadratic (inverted-U) term reflecting the Bernoulli $p(1{-}p)$ ceiling. GSM8K additionally tests n\\_steps and answer\\_length (both $p > 0.38$).}\n\\label{tab:ff_residual}\n\\scriptsize\n\\begin{tabular}{lrrr}\n\\toprule\nBenchmark & $R^2$ (full) & $R^2$ (diff.\\ only) & Diff.$^2$ $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Multiple-choice}} \\\\\nMMLU & 0.377 & 0.347 & $<$0.001 \\\\\nARC & 0.221 & 0.204 & $<$0.001 \\\\\nHellaSwag & 0.156 & 0.140 & $<$0.001 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Free-form}} \\\\\nGSM8K & 0.468 & 0.449 & $<$0.001 \\\\\nMATH & 0.856 & 0.845 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Model and Prompt Details}\n\\label{app:models}\n\n\\paragraph{Models.} Table~\\ref{tab:model_ids} lists the eight models with their HuggingFace identifiers.\n\n\\begin{table}[h]\n\\centering\n\\caption{Models used in all experiments.}\n\\label{tab:model_ids}\n\\scriptsize\n\\begin{tabular}{llr}\n\\toprule\nShort name & HuggingFace identifier & Params \\\\\n\\midrule\nLlama-3.1-8B & \\texttt{meta-llama/Llama-3.1-8B-Instruct} & 8B \\\\\nGemma-2-9B & \\texttt{google/gemma-2-9b-it} & 9B \\\\\nMistral-7B-v0.3 & \\texttt{mistralai/Mistral-7B-Instruct-v0.3} & 7B \\\\\nQwen3-8B & \\texttt{Qwen/Qwen3-8B} & 8B \\\\\nYi-1.5-9B & \\texttt{01-ai/Yi-1.5-9B-Chat} & 9B \\\\\nOLMo-2-7B & \\texttt{allenai/OLMo-2-1124-7B-Instruct} & 7B \\\\\nInternLM2.5-7B & \\texttt{internlm/internlm2\\_5-7b-chat} & 7B \\\\\nDeepSeek-7B & \\texttt{deepseek-ai/deepseek-llm-7b-chat} & 7B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt templates.} Our six prompt templates follow a surface perturbation design inspired by BrittleBench \\cite{brittlebench2026}. For multiple-choice benchmarks, templates vary along three dimensions: option layout (lettered vs.\\ numbered), instruction wording (direct vs.\\ contextual), and answer prompt cue. For free-form benchmarks, templates vary chain-of-thought elicitation strategy. All six templates are semantically equivalent---they request the same task with different surface forms---to isolate formatting effects from content effects. ARC-Challenge and HellaSwag use the same six surface patterns as MMLU with domain-appropriate system instructions; MATH mirrors the GSM8K pattern with \\texttt{\\textbackslash boxed\\{\\}} answer formatting.\n\n\\smallskip\\noindent\\textit{MMLU templates (representative MC format):}\n\\begin{enumerate}\\setlength{\\itemsep}{0pt}\\setlength{\\parsep}{0pt}\\setlength{\\topsep}{0pt}\n\\item \\texttt{The following are multiple choice questions (with answers) about \\{subject\\}.\\textbackslash n\\textbackslash n\\{question\\}\\textbackslash nA. ... D. ...\\textbackslash nAnswer:}\n\\item \\texttt{Answer the following \\{subject\\} questions by selecting the correct option.\\textbackslash nQuestion: \\{question\\}\\textbackslash n(A) ... (B) ... (C) ... (D) ...\\textbackslash nCorrect answer:}\n\\item \\texttt{Below are \\{subject\\} multiple-choice problems. Pick the right letter.\\textbackslash nQ: \\{question\\}\\textbackslash n~~A) ... B) ... C) ... D) ...\\textbackslash nA:}\n\\item \\texttt{Answer the following \\{subject\\} question by selecting A, B, C, or D.\\textbackslash n\\{question\\}\\textbackslash n- A. ... - B. ... - C. ... - D. ...\\textbackslash nAnswer:}\n\\item \\texttt{Below is a \\{subject\\} exam question with four possible answers. Choose the correct one.\\textbackslash n\\{question\\}\\textbackslash nOption A: ... Option B: ... Option C: ... Option D: ...\\textbackslash nCorrect:}\n\\item \\texttt{Question (\\{subject\\}):\\textbackslash n\\{question\\}\\textbackslash nChoices: (A) ... (B) ... (C) ... (D) ...\\textbackslash nYour answer:}\n\\end{enumerate}\n\n\\smallskip\\noindent\\textit{GSM8K templates (representative FF format):}\n\\begin{enumerate}\\setlength{\\itemsep}{0pt}\\setlength{\\parsep}{0pt}\\setlength{\\topsep}{0pt}\n\\item \\texttt{Solve the following math problem step by step.\\textbackslash nQ: \\{question\\}\\textbackslash nA: Let's think step by step.}\n\\item \\texttt{Answer the following math word problem. Show your work.\\textbackslash nQuestion: \\{question\\}\\textbackslash nSolution:}\n\\item \\texttt{Solve each problem below. Write your reasoning, then give the final answer after \\#\\#\\#\\#.\\textbackslash nProblem: \\{question\\}\\textbackslash nReasoning:}\n\\item \\texttt{You are a math tutor. Solve the problem and show your steps.\\textbackslash n\\{question\\}\\textbackslash nSteps:}\n\\item \\texttt{Work through this math question carefully.\\textbackslash nQ: \\{question\\}\\textbackslash nWork:}\n\\item \\texttt{Math problem:\\textbackslash n\\{question\\}\\textbackslash nLet's solve this step by step.}\n\\end{enumerate}\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform related-work section.\n\\end{itemize}\nTEXEOF\necho \"appendix DONE\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "e2dc68c8-6c24-4607-80c4-c4b28d55241d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XP9Lp39yV28j8iH5wXbNuW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4118,
      "cache_read_input_tokens": 91733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4118
      },
      "output_tokens": 75,
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

_source line 79 · 2026-05-23T19:16:56.718Z_

<details><summary>↩ Tool result · `toolu_01TjYq9WPup9ZGerfy9GDqRS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"appendix DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "50f360f2-6a5c-4202-842f-692790486550",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"appendix DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"appendix DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
Now I need to write the references.bib and main.bbl files. These are large. Let me also get the acl.sty and acl_natbib.bst from local. Actually, for the sty/bst files, they're standard ACL template files. Let me just read them and transfer them.

Let me read the local acl.sty.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "50636f1b-4d1e-4e16-bf70-c44999aa8ab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb8CCvSX7qxozaWTb8MrV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9516,
      "cache_read_input_tokens": 95851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9516
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

_source line 81_

现在写 references.bib。由于文件很大，我将直接用服务器上完整的 bib 内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0172b4d-78a1-49be-a164-f361da73e33b",
  "uuid": "db26b296-7f4b-4ff4-995a-73f75b54d474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nb8CCvSX7qxozaWTb8MrV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9516,
      "cache_read_input_tokens": 95851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9516
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
