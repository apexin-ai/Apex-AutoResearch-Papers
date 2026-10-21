# audit appendix tables verification — Part 1 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

[Transcript overview](../audit-appendix-tables-verification.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/84/84354abf8d7056ed3624.json)

## Before a recorded user message

## Before a recorded user message

109 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "7dda252b-da53-48e5-b5ca-f478c879ecf8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/memory/"
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
    "resetsAt": 1779535800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "38dae043-bf95-44e1-8b11-c8768923d3c1",
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96"
}
```

---


### Assistant

_source line 4_

I'll audit all appendix tables against the registry. Let me start by reading the appendix files and the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "cbece7ba-5839-4446-87d1-a1561d98cac3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpexMGSdNTUn7SADFdDBrn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12382,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12382
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DVeW6qe5ptej8fxRmRy1Gc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "58db71f2-c6d4-4cdc-b3fd-5c4c78930019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpexMGSdNTUn7SADFdDBrn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12382,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12382
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

_source line 6 · 2026-05-23T10:43:33.201Z_

<details><summary>↩ Tool result · `toolu_01DVeW6qe5ptej8fxRmRy1Gc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "4ae59f4c-46c1-4854-83c5-a6d75cdef054",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the appendix files and the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "bd915ad6-de5a-4aab-909e-1bd3d1ed763b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoMgGvBjmA4Cr2BWgWWioS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 33,
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

_source line 8_

Let me read all appendix files and the registry simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "91d5823c-386e-4cbc-b442-80455e48ac26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoMgGvBjmA4Cr2BWgWWioS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 33,
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

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_016MBazVu6DqWBx2aZaqupr4`</summary>

```json
{
  "pattern": "artifacts/_project/paper/appendix_*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "665e9f9e-4089-4908-9875-a31722543685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoMgGvBjmA4Cr2BWgWWioS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 33,
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

_source line 10 · 2026-05-23T10:43:38.206Z_

<details><summary>↩ Tool result · `toolu_016MBazVu6DqWBx2aZaqupr4`</summary>

```text
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/appendix_scalability.tex
artifacts/_project/paper/appendix_kappa_case_study.tex
artifacts/_project/paper/appendix_prompt_sensitivity.tex
artifacts/_project/paper/appendix_reproducibility.tex
artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_sampling_table.tex
artifacts/_project/paper/appendix_doc_length.tex
artifacts/_project/paper/appendix_case_studies.tex
artifacts/_project/paper/appendix_power_analysis_523cc9.tex
artifacts/_project/paper/appendix_power_analysis.tex
artifacts/_project/paper/appendix_high_kappa_analysis.tex
artifacts/_project/paper/appendix_downstream_analysis.tex
artifacts/_project/paper/appendix_order_invariance.tex
artifacts/_project/paper/appendix_pumping_lemma.tex
artifacts/_project/paper/appendix_full_ft.tex
artifacts/_project/paper/appendix_gollie_comparison.tex
artifacts/_project/paper/appendix_quantization.tex
artifacts/_project/paper/appendix_70b_ablation.tex
artifacts/_project/paper/appendix_zs_crossmodel.tex
artifacts/_project/paper/appendix_related_work.tex
artifacts/_project/paper/appendix_wikievents_pilot.tex
artifacts/_project/paper/appendix_tcr.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/appendix_beam_search.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "17cea2b5-38fd-4d1e-a309-db16d54aec30",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/appendix_prompts.tex",
      "artifacts/_project/paper/appendix_scalability.tex",
      "artifacts/_project/paper/appendix_kappa_case_study.tex",
      "artifacts/_project/paper/appendix_prompt_sensitivity.tex",
      "artifacts/_project/paper/appendix_reproducibility.tex",
      "artifacts/_project/paper/appendix_llama_per_relation.tex",
      "artifacts/_project/paper/appendix_sampling_table.tex",
      "artifacts/_project/paper/appendix_doc_length.tex",
      "artifacts/_project/paper/appendix_case_studies.tex",
      "artifacts/_project/paper/appendix_power_analysis_523cc9.tex",
      "artifacts/_project/paper/appendix_power_analysis.tex",
      "artifacts/_project/paper/appendix_high_kappa_analysis.tex",
      "artifacts/_project/paper/appendix_downstream_analysis.tex",
      "artifacts/_project/paper/appendix_order_invariance.tex",
      "artifacts/_project/paper/appendix_pumping_lemma.tex",
      "artifacts/_project/paper/appendix_full_ft.tex",
      "artifacts/_project/paper/appendix_gollie_comparison.tex",
      "artifacts/_project/paper/appendix_quantization.tex",
      "artifacts/_project/paper/appendix_70b_ablation.tex",
      "artifacts/_project/paper/appendix_zs_crossmodel.tex",
      "artifacts/_project/paper/appendix_related_work.tex",
      "artifacts/_project/paper/appendix_wikievents_pilot.tex",
      "artifacts/_project/paper/appendix_tcr.tex",
      "artifacts/_project/paper/appendix_discussion.tex",
      "artifacts/_project/paper/appendix_beam_search.tex"
    ],
    "durationMs": 13,
    "numFiles": 25,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Bc2X4k9tHHBEMu2CooXvk1`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": 0,
  "fields": [
    "*"
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
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "8f1e0d24-8c30-44a9-b995-623b3193d5a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoMgGvBjmA4Cr2BWgWWioS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 475
      },
      "output_tokens": 33,
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

_source line 12 · 2026-05-23T10:43:39.365Z_

<details><summary>↩ Tool result · `toolu_01Bc2X4k9tHHBEMu2CooXvk1`</summary>

```text
Error: result (303,132 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "94914bfa-4127-4642-bc08-597e9beb2387",
  "tool_use_result": {
    "content": "Error: result (303,132 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_70b_lora_docred_200_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:41:30.126Z\", \"updated_at\": \"2026-05-23T08:04:47.609Z\", \"hypothesis\": \"Full S2 (grammar+semantic+repair) on 70B LoRA DocRED should achieve near-zero DR while maintaining R_F1 close to beam4_s1 (48.14). The repair layer resolves residual DR violations from S1. This is the strongest constraint configuration for DocRED LoRA.\", \"parent\": \"eval_70b_lora_docred_200_beam4_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s2 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_full_s2.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 88990, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_full_s2.log\"}, \"metrics\": {\"R_F1\": 36.45, \"R_P\": 31.25, \"R_R\": 43.72, \"E_F1\": 84.96, \"E_P\": 84.6, \"E_R\": 85.34, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 13, \"CF_pct\": 0.34, \"parse_fail_pct\": 0, \"pred_entities\": 3819, \"pred_relations\": 3546, \"entity_tp\": 3218, \"entity_fp\": 586, \"entity_fn\": 553, \"relation_tp\": 1104, \"relation_fp\": 2429, \"relation_fn\": 1421}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T08:04:47.609Z\"}, \"sf2_qwen_int4_docred_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:52:58.757Z\", \"updated_at\": \"2026-05-23T07:57:03.714Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement or extraction quality on DocRED S1, maintaining DR=0% and R-F1 within 2pp of FP16 baseline\", \"parent\": \"d065_qwen_greedy_4096_r2\", \"spec\": {\"command\": \"bash scripts/run_qwen_docred_int4.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 21101, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Qwen3-8B-DocRED-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged/\", \"eval_data\": \"DocRED dev 200 docs\", \"log_path\": \"/tmp/sf2_qwen_int4_docred_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 200, \"parse_failures\": 37, \"parse_fail_pct\": 18.5, \"total_entities_pred\": 2985, \"total_relations_pred\": 2385, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.1, \"E_P\": 84.87, \"E_R\": 66.93, \"E_F1\": 74.84, \"R_P\": 41.59, \"R_R\": 38.65, \"R_F1\": 40.07, \"et_violations\": 0, \"rv_violations\": 0, \"dr_violations\": 0, \"cf_violations\": 3}, \"checkpoint_path\": \"outputs/sf2_qwen_int4_docred_s1/\", \"completed_at\": \"2026-05-23T07:57:03.714Z\"}, \"sf2_llama_int4_docred_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:53:03.669Z\", \"updated_at\": \"2026-05-23T07:13:24.996Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement or extraction quality on DocRED S1, maintaining DR=0% and R-F1 within 2pp of FP16 baseline\", \"parent\": \"d066_sweep_llama_docred_beam1_s1\", \"spec\": {\"command\": \"bash scripts/run_llama_docred_int4.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 21381, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-8B-DocRED-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged/\", \"eval_data\": \"DocRED dev 200 docs\", \"log_path\": \"/tmp/sf2_llama_int4_docred_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.22, \"R-F1\": 48.04, \"E-F1\": 84.18, \"R-P\": 44.79, \"R-R\": 51.8, \"E-P\": 85.5, \"E-R\": 82.9, \"samples\": 200, \"parse_fail\": 5, \"parse_fail_pct\": 2.5, \"entities_pred\": 3669, \"relations_pred\": 2997}, \"checkpoint_path\": \"outputs/sf2_llama_int4_docred_s1/output.jsonl\", \"log_path\": \"outputs/sf2_llama_int4_docred_s1/eval_results.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T07:13:24.996Z\"}, \"sf2_70b_prompt_sensitivity\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:45:02.263Z\", \"updated_at\": \"2026-05-23T05:45:25.528Z\", \"hypothesis\": \"70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.\", \"spec\": {\"command\": \"python run_prompt_sensitivity_70b.py\", \"server\": \"westd-21461\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42}}, \"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:58:33.950Z\", \"updated_at\": \"2026-05-23T05:35:25.774Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Llama-3.1-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"w5_llama_lora_scierc_constrained_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl --device cuda:0\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Llama-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test (551 docs)\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"log_path\": \"outputs/sf2_llama_int4_scierc_s1/violation_report.json\", \"checkpoint_path\": \"outputs/sf2_llama_int4_scierc_s1/raw_outputs.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:32:49.329Z\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:58:51.930Z\", \"updated_at\": \"2026-05-23T05:35:24.911Z\", \"hypothesis\": \"AWQ INT4 quantization of fine-tuned Qwen3-8B does not significantly affect constraint enforcement on SciERC S1\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/ --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/sf2_qwen_int4_scierc_s1/output.jsonl --device cuda:0 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-FT-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/Qwen3-8B-SciERC-FT-AWQ-INT4/\", \"eval_data\": \"SciERC test 551 sentences\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"log_path\": \"outputs/sf2_qwen_int4_scierc_s1/violation_report.json\", \"checkpoint_path\": \"outputs/sf2_qwen_int4_scierc_s1/output.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:32:46.404Z\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:14:38.851Z\", \"updated_at\": \"2026-05-23T05:15:20.167Z\", \"hypothesis\": \"GoLLIE-7B achieves low schema violation rates on SciERC zero-shot because it outputs very conservatively (few entities, almost no relations), resulting in trivially low violation rates but extremely poor recall and F1.\", \"spec\": {\"command\": \"python scripts/gollie_scierc_inference.py + python scripts/eval_gollie_scierc.py + python scripts/eval_gollie_comparison.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"GoLLIE-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/gollie_model/\", \"eval_data\": \"SciERC test (100 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/gollie_model/\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/gollie_scierc/\"}, \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:15:20.167Z\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:41:26.371Z\", \"updated_at\": \"2026-05-23T02:30:50.739Z\", \"hypothesis\": \"Full S1 (grammar+semantic) constraints on 70B ZS DocRED should achieve DR close to semantic_only (1.66%) since grammar adds zero DR contribution in ZS setting. R_F1 should remain ~13 (matching unconstrained 13.25). This completes the ZS DocRED ablation matrix.\", \"parent\": \"eval_70b_zs_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode full_s1 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_full_s1.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 88678, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\"}, \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/70b_zs_docred_200_full_s1.jsonl\", \"log_path\": \"/tmp/70b_zs_docred_200_full_s1.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:30:50.739Z\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:19.975Z\", \"updated_at\": \"2026-05-23T01:55:24.472Z\", \"hypothesis\": \"Grammar-only constraints on 70B LoRA DocRED will eliminate RV violations but not reduce DR, mirroring the SciERC ablation pattern where grammar layer provides zero DR contribution at fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_grammar_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 984253, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_grammar_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T01:55:24.472Z\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:17.601Z\", \"updated_at\": \"2026-05-23T01:20:56.659Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA DocRED will reduce DR violations from unconstrained baseline (DR=0.88%) with minimal F1 impact, isolating the semantic layer's contribution in document-level RE at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 983803, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 docred\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"log_path\": \"/tmp/70b_lora_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T01:20:56.659Z\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:55:27.332Z\", \"updated_at\": \"2026-05-23T00:38:42.757Z\", \"hypothesis\": \"70B ZS DocRED unconstrained 200-doc baseline to complete the ablation matrix. Expect DR~15% and R-F1~13 consistent with prior 99-doc measurement, providing matched-subset comparison for semantic_only (DR=1.66%) and grammar_only experiments.\", \"parent\": \"70b_docred_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode unconstrained --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_unconstrained.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 84588, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_unconstrained.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:38:42.757Z\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:24:11.190Z\", \"updated_at\": \"2026-05-23T00:37:43.935Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS DocRED will show minimal DR reduction (similar to SciERC 70B ZS pattern where grammar_only DR≈unconstrained), confirming that grammar layer's negligible contribution at 70B scale generalizes across datasets.\", \"parent\": \"r16_70b_docred_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode grammar_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_grammar_only.jsonl --max_new_tokens 4096 --max_samples 200\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"eval_data\": \"DocRED dev 200-doc subset\", \"checkpoint_source\": \"n/a (zero-shot)\", \"log_path\": \"/tmp/70b_zs_docred_200_grammar_only.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T00:37:43.935Z\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:35:21.150Z\", \"updated_at\": \"2026-05-22T22:55:11.458Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS DocRED will significantly reduce DR violations from zero-shot baseline, demonstrating the semantic layer's effectiveness on document-level RE without fine-tuning.\", \"parent\": \"70b_docred_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --dataset docred --mode semantic_only --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_zs_docred_200_semantic_only.jsonl --max_docs 200 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"DocRED dev 200 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_docred_200_semantic_only.log\"}, \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:55:11.459Z\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:15:28.977Z\", \"updated_at\": \"2026-05-22T21:21:11.254Z\", \"hypothesis\": \"70B LoRA DocRED with beam search (k=4) + full_s1 on 200-doc subset will achieve DR=0% and CF≈0% while maintaining R-F1 comparable to greedy S1 (43.95), consistent with 8B beam search pattern.\", \"parent\": \"eval_70b_lora_docred_200_s1_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146 --data_path data/docred/dev.json --dataset docred --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/70b_lora_docred_200_beam4_s1.jsonl --max_new_tokens 4096 --max_samples 200 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 70638, \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/70b_lora_docred_200_beam4_s1.jsonl\", \"log_path\": \"westd-21461:/tmp/70b_lora_docred_200_beam4_s1.log\", \"note\": \"PEFT awq.py patched to support AwqMarlinLinear for AWQ+LoRA. Estimated ~1.8h (32s/sample).\"}, \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:21:11.254Z\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:13:55.324Z\", \"updated_at\": \"2026-05-22T20:31:32.878Z\", \"hypothesis\": \"70B LoRA SciERC with grammar-only constrained decoding will reduce DR violations compared to unconstrained (DR=1.5%) but less than full_s1 (DR=0%), isolating grammar layer's independent contribution at 70B fine-tuned scale.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_grammar_only.log\", \"pid\": 70175}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}, \"completed_at\": \"2026-05-22T18:44:02.122Z\"}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:45:13.928Z\", \"updated_at\": \"2026-05-22T20:30:18.431Z\", \"hypothesis\": \"Independent 70B ZS SciERC unconstrained baseline to verify prior DR and R-F1 numbers from r16_70b_scierc_zs_s1 experiment. Expect DR~6-8% and R-F1~11 consistent with earlier measurements.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode unconstrained --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_unconstrained.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0 (NVIDIA RTX PRO 6000 Blackwell 96GB)\", \"pid\": 74572, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/tmp/70b_zs_scierc_unconstrained.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:18.431Z\"}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:04:58.305Z\", \"updated_at\": \"2026-05-22T20:30:16.494Z\", \"hypothesis\": \"Full S2 constrained decoding on 70B LoRA SciERC achieves DR=0% like S1, with potentially fewer CF violations due to S2's enhanced cross-field consistency checking. R-F1 should be comparable to S1 (44.53-44.81).\", \"parent\": \"eval_70b_lora_scierc_s1_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s2 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_full_s2.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 972139, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_full_s2.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:16.494Z\"}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:04:55.672Z\", \"updated_at\": \"2026-05-22T20:30:13.188Z\", \"hypothesis\": \"Semantic-only constraints on 70B LoRA SciERC will reduce DR from 1.5% (unconstrained) toward 0%, consistent with the 70B ZS pattern where semantic layer is the primary DR reduction mechanism. Without grammar layer, some RV violations may appear.\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 971668, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}, \"completed_at\": \"2026-05-22T20:30:13.188Z\"}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:48:40.066Z\", \"updated_at\": \"2026-05-22T18:16:23.650Z\", \"hypothesis\": \"Shuffling entity type order in the constraint schema (seed=42) does not significantly change constrained decoding results (R-F1 within ±0.5pp, violation rates identical), confirming that OntoCoDec is order-invariant. This addresses R19-W3 reviewer concern about entity registry ordering sensitivity.\", \"parent\": \"w5_lora_scierc_constrained_eval\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints_shuffled.json --output_path outputs/entity_order_shuffled_qwen_scierc.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 967058, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/entity_order_shuffled_qwen_scierc.log\", \"shuffle_seed\": 42, \"original_entity_order\": [\"Task\", \"Method\", \"Material\", \"Metric\", \"OtherScientificTerm\", \"Generic\"], \"shuffled_entity_order\": [\"Metric\", \"Method\", \"Material\", \"OtherScientificTerm\", \"Task\", \"Generic\"], \"original_relation_order\": [\"Used-for\", \"Feature-of\", \"Hyponym-of\", \"Part-of\", \"Compare\", \"Conjunction\", \"Evaluate-for\"], \"shuffled_relation_order\": [\"Conjunction\", \"Evaluate-for\", \"Compare\", \"Part-of\", \"Feature-of\", \"Hyponym-of\", \"Used-for\"]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}, \"completed_at\": \"2026-05-22T18:04:14.919Z\"}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:36.807Z\", \"updated_at\": \"2026-05-22T18:09:49.840Z\", \"hypothesis\": \"Semantic-only constraints on 70B ZS will reduce DR partially (similar to 8B pattern: ~24% reduction) without eliminating RV/ET, isolating semantic layer's independent contribution at 70B scale.\", \"parent\": \"r16_70b_scierc_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode semantic_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_semantic_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"r16_70b_scierc_zs_s1\", \"eval_data\": \"scierc test set (551 docs)\", \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_semantic_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}, \"completed_at\": \"2026-05-22T18:09:49.840Z\"}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:44.901Z\", \"updated_at\": \"2026-05-22T18:09:48.056Z\", \"hypothesis\": \"Grammar-only constraints on 70B ZS reduce domain-range violations compared to unconstrained baseline (DR=6.41%) but less effectively than full_s1 (DR=0%), isolating grammar layer's contribution to constraint enforcement.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --dataset scierc --mode grammar_only --constraints_path ontology_constraints.json --output_path outputs/70b_zs_scierc_grammar_only.jsonl --max_new_tokens 2048\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 (ZS)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/eval_70b_zs_scierc_grammar_only.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}, \"completed_at\": \"2026-05-22T18:09:48.056Z\"}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:39:43.218Z\", \"updated_at\": \"2026-05-22T18:04:29.880Z\", \"hypothesis\": \"70B LoRA fine-tuned model with beam search (k=4) and full_s1 constrained decoding on SciERC achieves DR=0% and CF=0%, matching 8B beam search behavior, while maintaining or improving extraction F1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --dataset scierc --mode full_s1 --decoding_strategy beam --num_beams 4 --constraints_path ontology_constraints.json --output_path outputs/70b_lora_scierc_beam4_s1.jsonl --max_new_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4 + LoRA r16 scierc\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test 551 docs\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"log_path\": \"/tmp/70b_lora_scierc_beam4_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}, \"completed_at\": \"2026-05-22T18:04:29.880Z\"}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:48:16.222Z\", \"updated_at\": \"2026-05-22T16:27:25.157Z\", \"spec\": {\"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/tmp/beam4_tcr_llama_scierc.log\"}, \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\", \"hypothesis\": \"TCR reranking on beam4 outputs will change beam selection for LLaMA-SciERC by penalizing constraint-violating candidates, improving DR violation rate and overall F1 compared to vanilla beam4.\", \"completed_at\": \"2026-05-22T16:27:25.157Z\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:37:32.074Z\", \"updated_at\": \"2026-05-22T15:49:03.706Z\", \"hypothesis\": \"TCR (Type Consistency Reranking) with beam search (k=4) on Qwen3-8B LoRA SciERC will reduce domain/range violations compared to standard beam search by reranking candidates based on type consistency scores, while maintaining or improving Entity/Relation F1.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python beam_tcr_rerank.py --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --dataset scierc --beam_width 4 --alpha 0.7 --output_path outputs/beam4_tcr_qwen_scierc.jsonl --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"/tmp/beam_tcr_run.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T15:37:47.865Z\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}, \"parent\": \"d066_beam_sweep\"}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:29:07.493Z\", \"updated_at\": \"2026-05-22T13:30:06.224Z\", \"hypothesis\": \"vLLM's guided_json (JSON schema-constrained decoding) produces equivalent violation rates and F1 scores to our XGrammar grammar-only ablation, confirming that guided_json ≈ GCD (grammar-constrained decoding) without semantic constraints.\", \"spec\": {\"command\": \"python vllm_guided_json_eval.py --model_path /root/autodl-tmp/models/Qwen3-8B-link --data_path data/processed_data/test.json --output_path outputs/vllm_guided_json_scierc_zs.jsonl --max_tokens 2048\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 0}, \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval-only experiment)\", \"log_path\": \"/tmp/vllm_guided_json_eval.log\", \"completed_at\": \"2026-05-22T13:30:06.224Z\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:47:05.464Z\", \"updated_at\": \"2026-05-22T10:34:22.854Z\", \"hypothesis\": \"70B LoRA DocRED with Full S1 constrained decoding on 200-doc subset will achieve DR→0% while maintaining R-F1 comparable to unconstrained, confirming scale-independent constraint composability on DocRED at 70B scale\", \"parent\": \"eval_70b_lora_docred_200_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 /tmp/run_docred_s1.py (monkey-patched AWQ+LoRA loader)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": \"11466\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"200 (first 200 docs)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\"}, \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_s1_constrained.jsonl\", \"log_path\": \"westd-21461:/tmp/constrained_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:34:01.646Z\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:44:23.637Z\", \"updated_at\": \"2026-05-22T10:34:14.027Z\", \"hypothesis\": \"Beam width k∈{1,2,4,8} on SciERC (LoRA, Qwen3-8B) will show monotonic DR/CF reduction with diminishing returns past k=4, establishing the cost-effectiveness trade-off for the beam search appendix Pareto analysis.\", \"spec\": {\"command\": \"d066 DocRED beam sweep (k=1,2,4,8 x unc/s1 x Qwen/Llama, 200 docs each)\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B + Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"note\": \"ANALYZING->RUNNING transition blocked. Actual status: DocRED sweep actively running on both servers. SciERC sweep complete.\"}, \"notes\": \"全部 8 配置完成 + eval 齐全。beam8 con: E-F1=66.36, R-F1=43.65, DR=0%, CF=0%, avg_time=5.058s。Pareto optimal: k=2 con (E-F1=67.71, R-F1=44.60, DR=0%)。k=8 相比 k=2 F1 下降 ~1.3pp 且推理慢 46%，收益递减明确。可入稿。\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\", \"checkpoint_path\": \"parent experiment - see child experiments for individual outputs\", \"log_path\": \"parent experiment - see child experiments for individual logs\", \"completed_at\": \"2026-05-22T10:34:14.027Z\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-22T07:36:58.067Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}, \"parent\": \"w5_llama_docred_lora_training\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-22T07:36:56.885Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:49:59.199Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:50:01.253379+00:00\"}]}, \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"outputs/w8_llama_docred_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T16:55:22.088Z\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-22T07:36:54.996Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:36.469Z\", \"updated_at\": \"2026-05-22T07:36:52.623Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen FT SciERC will show high DR (comparable to or worse than unconstrained), proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_ft.log\"}, \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:46.097Z\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:39.235Z\", \"updated_at\": \"2026-05-22T07:36:49.828Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama FT SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama FT)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_ft.log\"}, \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:50.516Z\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:06:11.811Z\", \"updated_at\": \"2026-05-22T07:09:22.684Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models on DocRED 200-doc subset unconstrained extraction, serving as the unconstrained baseline for S1 comparison at 70B scale\", \"parent\": \"r16_70b_lora_docred\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -c 'import peft.import_utils as _piu; _piu.is_gptqmodel_available = lambda: False; import runpy, sys; sys.argv=[...]; runpy.run_path(\\\"run_constrained_extraction.py\\\", run_name=\\\"__main__\\\")'\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": \"998 (truncated to 200)\", \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-1146)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/checkpoint-1146\", \"eval_data\": \"DocRED dev (200-doc subset)\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}, \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_200_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_docred/docred_unconstrained.log\", \"completed_at\": \"2026-05-22T07:09:22.684Z\"}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:46:31.480Z\", \"updated_at\": \"2026-05-22T06:47:38.556Z\", \"hypothesis\": \"70B LoRA SciERC with Full S1 constrained decoding will achieve DR→0% while maintaining R-F1 comparable to unconstrained (44.73), confirming scale-independent constraint effectiveness at 70B with fine-tuning\", \"parent\": \"eval_70b_lora_scierc_unconstrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16 (checkpoint-663)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"SciERC test (551 sentences)\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_s1.log\"}, \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:47:38.556Z\"}, \"eval_70b_lora_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:21:50.531Z\", \"updated_at\": \"2026-05-22T05:26:55.968Z\", \"hypothesis\": \"70B LoRA-finetuned model (r16, Llama-3.1-70B-AWQ-INT4) will achieve higher R-F1 than 8B models (Qwen FT R-F1=47.15, Llama FT R-F1=46.13) on SciERC unconstrained extraction due to larger model capacity\", \"parent\": \"r16_70b_lora_scierc\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --lora_path /root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl --max_new_tokens 4096 --seed 42\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-AWQ-INT4 + LoRA r16\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/checkpoint-663\", \"eval_data\": \"scierc test (551 sentences)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/r16_70b_lora_scierc/scierc_unconstrained.log\", \"completed_at\": \"2026-05-22T05:24:50.267Z\", \"metrics\": {\"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.5, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1806, \"relations\": 1133}}, \"r16_70b_docred_zs_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:03:19.394Z\", \"updated_at\": \"2026-05-22T05:19:05.018Z\", \"hypothesis\": \"Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on DocRED ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B SciERC results to DocRED and confirming scale-independent constraint effectiveness across datasets\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_docred_zs.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:07:51.929Z\", \"metrics\": {\"E_F1\": 69.11, \"R_F1\": 13.05, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.04, \"parse_fail_pct\": 0.1, \"samples\": 998, \"total_entities\": 16599, \"total_triples\": 13239, \"baseline_unc_DR_pct\": 14.98, \"baseline_unc_R_F1\": 13.01, \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_70b_docred_zs_s1.log\"}, \"d066_sweep_llama_beam8_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:06:56.291Z\", \"updated_at\": \"2026-05-22T04:07:12.776Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam8 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --output_file /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 755444. Relay from Llama beam2 s1 (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam8_unconstrained.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam8_unc.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}, \"completed_at\": \"2026-05-20T13:22:18.037Z\"}, \"d066_sweep_llama_beam2_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:07:25.146Z\", \"updated_at\": \"2026-05-22T04:07:10.538Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam2 constrained (full_s1) on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --max_samples 200 --seed 42\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 750801. Relay from Llama beam2 unc (success).\", \"checkpoint_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam2_full_s1.jsonl\", \"log_path\": \"westd-16980:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam2_s1.log\"}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}, \"completed_at\": \"2026-05-20T12:06:48.878Z\"}, \"d066_sweep_llama_docred_beam4_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:01:45.514Z\", \"updated_at\": \"2026-05-22T04:03:52.952Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_beam4_s1.log\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR%\": 0, \"CF%\": 0, \"PF%\": 0.5, \"ET%\": 0, \"RV%\": 0, \"samples\": 200, \"parse_fail\": 1}, \"command\": \"d066 beam sweep llama docred beam4 s1 (completed, retroactive fix)\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}, \"hypothesis\": \"Beam search k=4 with Full S1 constraints on Llama DocRED 200-doc will achieve DR=0% and CF near 0%, completing the beam sweep Pareto analysis across all beam widths for the DocRED dataset\", \"completed_at\": \"2026-05-22T04:03:52.952Z\"}, \"r16_70b_lora_scierc_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:32:17.414Z\", \"updated_at\": \"2026-05-22T02:32:17.415Z\", \"hypothesis\": \"70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale\"}, \"r16_70b_lora_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:04:39.980Z\", \"updated_at\": \"2026-05-22T02:11:31.447Z\", \"hypothesis\": \"70B AWQ INT4 + LoRA fine-tuning on DocRED will achieve higher R-F1 than 8B FT models, and S1 constraints will maintain DR→0% at 70B scale with fine-tuning, confirming scale-independent constraint effectiveness across datasets\", \"parent\": \"r16_70b_scierc_zs_s1\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 scripts/train_lora_70b_docred.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_docred/train.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/docred/sft_dev_llama.jsonl\", \"pid\": 839375, \"gpu_ids\": [1], \"note\": \"Restarted from scratch (previous run killed, empty checkpoint dir). LoRA r=16 alpha=32 on q/k/v/o_proj. bs=1 grad_accum=8 lr=2e-5 3epochs. ~10.4h ETA.\"}, \"notes\": \"Restarted with tensorboard. Step 10: loss=0.1472, grad_norm=0.1431. Step 20: loss=0.1499, grad_norm=0.1574. Warmup phase (LR ramping up), loss stable, gradients healthy. AWQ+LoRA working correctly.\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:08:00.797Z\", \"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:00:09.608Z\", \"updated_at\": \"2026-05-22T02:11:30.415Z\", \"hypothesis\": \"70B AWQ INT4 + LoRA fine-tuning on SciERC will achieve higher R-F1 than 8B FT models, and S1 constraints will maintain DR→0% at 70B scale with fine-tuning\", \"spec\": {\"command\": \"python3 train_70b_lora.py --dataset scierc --model_path /root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ-INT4 --output_dir /root/autodl-tmp/checkpoints/70b_lora_scierc --epochs 3 --lr 2e-4 --lora_r 16 --lora_alpha 32\", \"server\": \"westd-16980\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Llama-3.3-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/\", \"log_path\": \"/root/autodl-tmp/checkpoints/70b_lora_scierc/train.log\", \"pid\": 836206, \"gpu_ids\": [0, 1]}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:07:56.630Z\", \"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_scierc_zs_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:11:52.091Z\", \"updated_at\": \"2026-05-21T07:09:31.198Z\", \"hypothesis\": \"Llama-3.1-70B-Instruct-AWQ-INT4 with Full S1 constrained decoding on SciERC ZS will achieve DR→0% with R-F1 stable vs unconstrained, extending 70B DocRED results to SciERC and confirming scale-independent constraint effectiveness\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/run_70b_scierc_zs.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": 808988, \"data_path\": \"SciERC test set (551 sentences)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-70B-Instruct-AWQ-INT4\", \"model_path\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_path\": \"N/A (ZS eval)\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/r16_70b_scierc_zs_s1.log\"}, \"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T07:09:31.199Z\"}, \"r14_qwen_docred_beam4_998\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:43.999Z\", \"updated_at\": \"2026-05-21T05:43:45.941Z\", \"hypothesis\": \"Beam=4 S1 constrained on full DocRED 998-doc test set will show consistent DR elimination and R-F1 stability compared to 50-doc subset, addressing reviewer concern about subset representativeness\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.jsonl --device cuda:0 --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_source\": \"N/A (zero-shot)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_qwen_docred_beam4_998.log\", \"checkpoint_path\": \"N/A\"}, \"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:43:45.941Z\"}, \"r16_trie_llama_zs_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:40.697Z\", \"updated_at\": \"2026-05-21T04:59:53.422Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Llama ZS SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Llama ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_llama_zs.log\"}, \"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:53.422Z\"}, \"r16_trie_qwen_zs_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:37.808Z\", \"updated_at\": \"2026-05-21T04:59:47.872Z\", \"hypothesis\": \"Trie-only vocabulary constraint (GCD-equivalent, no JSON structure) on Qwen ZS SciERC will show high DR, proving grammar layer is prerequisite for vocabulary membership enforcement\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode trie_only --dataset scierc (Qwen ZS)\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": 241846, \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A (trie eval)\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r16_trie_qwen_zs.log\"}, \"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:59:47.872Z\"}, \"r14_llama_docred_beam4_998\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:47:34.166Z\", \"updated_at\": \"2026-05-21T04:50:39.829Z\", \"hypothesis\": \"Beam=4 S1 constrained on full DocRED 998-doc with Llama-3.1-8B will confirm DR elimination and R-F1 stability seen in 50-doc subset, providing second model evidence for SF3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --output_path /root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.jsonl --max_new_tokens 4096 --seed 42 --decoding_strategy beam --num_beams 4 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Llama-3.1-8B-Instruct (zero-shot)\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/schema_outputs/r14_llama_docred_beam4_998.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:50:35.683Z\", \"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:38:34.783Z\", \"updated_at\": \"2026-05-20T16:47:28.821Z\", \"hypothesis\": \"d066 SciERC beam sweep: Llama beam8 constrained (full_s1) on 551-sentence test set. Last Llama SciERC config.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam8_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T16:35:37.041Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:35:38.984Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T16:35:47.195455+00:00\"}]}, \"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:04:24.318Z\", \"updated_at\": \"2026-05-20T16:42:22.936Z\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam4_s1_551.log\", \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42}, \"hypothesis\": \"d066 SciERC beam sweep: Llama beam4 constrained (full_s1) on 551-sentence test set. Beam width k=4 with schema constraints should eliminate all four violation types (ET/RV/DR/CF=0) while maintaining R-F1 within ±1pp of unconstrained.\", \"completed_at\": \"2026-05-20T16:42:22.936Z\"}, \"d066_sweep_llama_docred_beam4_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:22:24.187Z\", \"updated_at\": \"2026-05-20T16:41:02.850Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam4 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 4 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam4_unconstrained.jsonl\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 761033. Relay from Llama beam8 unc (success).\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam4_unc.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam4_unc.log\", \"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:41:02.851Z\"}, \"d066_sweep_llama_docred_beam1_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T13:18:07.824Z\", \"updated_at\": \"2026-05-20T16:41:01.414Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam1 (greedy) constrained (full_s1) on 200-doc subset (westd-21461 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 209444. Relay from beam1 unc (success).\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam1_full_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam1_s1.log\", \"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:41:01.414Z\"}, \"d066_sweep_llama_beam8_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:17:06.965Z\", \"updated_at\": \"2026-05-20T16:40:59.767Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam8 constrained (full_s1) on 200-doc subset (westd-16980 GPU0). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-16980 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 756540. Relay after GPU0 freed.\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam8_full_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam8_s1.log\", \"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:40:59.767Z\"}, \"d065_qwen_greedy_4096_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:58:53.058Z\", \"updated_at\": \"2026-05-20T16:40:58.219Z\", \"hypothesis\": \"Qwen3-8B LoRA on full DocRED dev (998 docs) with greedy 4096 tokens will show comparable DR elimination under constrained decoding as seen in SciERC, confirming schema-semantic constraints generalize to high-cardinality relation extraction (96 types). Rerun after dual-process data corruption.\", \"parent\": \"d065_qwen_greedy_4096\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --output_file /root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_con_4096_rerun.jsonl --seed 42\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (998 docs, constrained decoding inference)\", \"note\": \"Rerun after dual-process corruption. PID 194615.\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d065_qwen_greedy_con_r2.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d065_qwen_greedy_con_r2.log\", \"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T16:40:58.219Z\"}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:04:53.443Z\", \"updated_at\": \"2026-05-20T16:37:54.940Z\", \"hypothesis\": \"d066 SciERC beam sweep: Llama beam2 constrained (full_s1) on 551-sentence test set.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 2 --max_new_tokens 4096 --seed 42 --data_path data/processed_data/test.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama_lora_scierc_merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"scierc test set (551 sentences)\"}, \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam2_full_s1.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam2_s1_551.log\", \"completed_at\": \"2026-05-20T15:37:46.989Z\"}, \"d066_sweep_llama_scierc_beam1_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:13:08.565Z\", \"updated_at\": \"2026-05-20T13:52:26.684Z\", \"hypothesis\": \"d066 SciERC beam sweep sub-task: Llama beam1 (greedy) unconstrained on 551-doc full set (westd-21461 GPU1). Part of d066_beam_sweep. Extends Qwen-only SciERC sweep to Llama model family.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --seed 42\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/scierc/test.json (551 docs)\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B LoRA SciERC (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/scierc/test.json\", \"note\": \"PID 205314. Relay from Qwen beam8 s1 SciERC (success).\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam1_unc.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}, \"completed_at\": \"2026-05-20T12:27:51.420Z\"}, \"d066_sweep_llama_docred_beam1_unc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:27:58.317Z\", \"updated_at\": \"2026-05-20T13:18:06.388Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam1 (greedy) unconstrained on 200-doc subset (westd-21461 GPU1). Part of d066_beam_sweep. DocRED data needed for Pareto dual-panel figure.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --decoding_strategy beam --num_beams 1 --max_new_tokens 4096 --max_samples 200 --seed 42 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"note\": \"PID 206397. Relay from Llama SciERC beam1 unc. DocRED priority per Director.\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_200_beam1_unconstrained.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_docred_beam1_unc.log\"}, \"conclusion\": \"success\", \"metrics\": {\"total\": 200, \"success\": 196, \"fail\": 4, \"output_file\": \"llama_docred_200_beam1_unconstrained.jsonl\"}, \"completed_at\": \"2026-05-20T13:18:06.388Z\"}, \"d066_sweep_21461_gpu1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:01:12.415Z\", \"updated_at\": \"2026-05-20T12:13:00.737Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Qwen beam8 constrained (full_s1) on 200-doc subset (westd-21461 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path qwen_lora_docred_merged --decoding_strategy beam --num_beams 8 --max_docs 200\", \"server\": \"westd-21461 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam8_full_s1.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d066_beam_sweep/d066_qwen_beam8_s1_21461.log\"}, \"conclusion\": \"success\", \"metrics\": {\"total\": 551, \"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"avg_time_s\": 5.058, \"output_file\": \"qwen_scierc_beam8_full_s1.jsonl\", \"note\": \"Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)\"}, \"completed_at\": \"2026-05-20T12:13:00.737Z\"}, \"w5_llama_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T19:58:10.837Z\", \"updated_at\": \"2026-05-20T11:59:24.791Z\", \"hypothesis\": \"Fine-tuned Llama-3.1-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Llama DocRED 上是否仍能消除残余 DR 且不损 R-F1\", \"parent\": \"w5_llama_docred_lora_training\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T00:22:01.892Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-16T04:51:37.138Z\", \"training_hours\": 4.49}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-16T00:26:15.420Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:26:16.832346+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:51:38.893721+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"pid\": 317464, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_constrained_eval.log\", \"model_name\": \"llama_lora_docred_merged\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"N/A\"}, \"notes\": \"重提交后 PID 317464 (wrapper) / 317469 (GPU subprocess) 在 cuda:0 正常运行。EXIT_CODE=143 来自 wrapper 层误报，非推理进程故障。Grammar 编译 96 relation types 耗时 ~9min（长初始化触发 wrapper 超时报警）。11/998 at ~14s/sample, ETA ~3.8h。脚本支持 --resume，如被 kill 可恢复。\", \"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 83.94, \"entity_precision\": 85, \"entity_recall\": 84.13, \"relation_f1_all_set\": 43.78, \"relation_precision_all_set\": 38.79, \"relation_recall_all_set\": 50.81, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.21, \"CF_pct\": 0.21, \"delta_vs_unconstrained\": {\"delta_e_f1\": 0.01, \"delta_r_f1\": 0.06, \"delta_dr\": -0.28, \"note\": \"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\"}, \"provenance\": \"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\"}, \"conclusion\": \"success\"}, \"d066_sweep_16980_gpu1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:01:11.031Z\", \"updated_at\": \"2026-05-20T11:23:11.984Z\", \"hypothesis\": \"d066 DocRED beam sweep sub-task: Llama beam2 unconstrained on 200-doc subset (westd-16980 GPU1). Part of d066_beam_sweep parent experiment.\", \"parent\": \"d066_beam_sweep\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 nohup python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path llama_lora_docred_merged --decoding_strategy beam --num_beams 2 --max_docs 200\", \"server\": \"westd-16980 GPU1\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Llama-3.1-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json (200-doc subset)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T11:21:34.505Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:21:35.106Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T11:21:41.240328+00:00\"}]}, \"notes\": \"Cron 误判：进程正常完成（200/200 samples, success=198, fail=2），但因无 W&B metrics 被 auto-resolved as failed。日志确认完整完成。输出: llama_docred_200_beam2_unconstrained.jsonl。待 eval 获取 metrics。\"}, \"d065_qwen_greedy_4096\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:15:26.700Z\", \"updated_at\": \"2026-05-20T08:24:26.139Z\", \"hypothesis\": \"Qwen3-8B LoRA on full DocRED dev (998 docs) with greedy 4096 tokens will show comparable DR elimination under constrained decoding as seen in SciERC, confirming schema-semantic constraints generalize to high-cardinality relation extraction (96 types).\", \"spec\": {\"command\": \"bash scripts/d065_qwen_greedy_4096_21461.sh (unc then con, sequential)\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json (998 docs)\", \"data_count\": 998, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_*_4096.jsonl\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d065_qwen_greedy_4096.log\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:24:19.389Z\", \"notes\": \"Llama 4096 eval 完成。unc: E-F1=84.77, R-F1=44.55, DR=0.49%, CF=0.08%; con: E-F1=84.71, R-F1=44.70, DR=0.00%, CF=0.26%。vs w5: E-F1 +1.3pp (PF% 从 ~5%→~2.5%), R-F1 持平。Qwen 仍在跑: unc 887/998 ETA ~09:00, con 707/998 ETA ~10:10。\"}, \"d066_docred_beam_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:42:56.730Z\", \"updated_at\": \"2026-05-20T03:02:27.736Z\", \"hypothesis\": \"DocRED beam width sweep (k=2,8) on Qwen LoRA 200-doc subset will show the same Pareto pattern as SciERC — k=2 as sweet spot with diminishing returns at k=8 — confirming the beam width recommendation generalizes across datasets with different schema complexity (DocRED: 96 relation types vs SciERC: 7).\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset docred --decoding_strategy beam --num_beams {2,8} --mode {unconstrained,full_s1} (4 runs serial)\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/docred/dev.json (200-doc subset)\", \"data_count\": 200, \"model_name\": \"Qwen3-8B LoRA DocRED (merged)\", \"seed\": 42, \"claim\": \"Claim 3 + deployment guidance\", \"paper_usage\": \"DocRED Pareto curve in appendix\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:27.736Z\"}, \"d067_seed_variance\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T23:44:45.500Z\", \"updated_at\": \"2026-05-20T02:42:31.802Z\", \"hypothesis\": \"Varying random seed (42,123,456) across models (Qwen,Llama) and datasets (SciERC,DocRED) under constrained vs unconstrained decoding will show low F1 variance (σ<1pp), confirming that reported improvements from constraint decoding are robust and not seed-dependent.\", \"spec\": {\"command\": \"bash scripts/d067_run_all.sh (3 configs × 2 seeds × unc/con, 12 runs serial)\", \"server\": \"westd-21461 GPU0\", \"data_path\": \"data/processed_data/test.json (SciERC) + data/docred/dev.json (DocRED)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B LoRA SciERC + Llama-3.1-8B LoRA SciERC + Qwen3-8B LoRA DocRED\", \"seed\": \"123, 456\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d067_*\", \"log_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/d067_run_all.log\"}, \"metrics\": {\"qwen_scierc_unc\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.25 ± 0.43\", \"DR\": \"2.06 ± 0.08\", \"CF\": \"0.00 ± 0.00\"}, \"qwen_scierc_con\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.22 ± 0.39\", \"DR\": \"0.00 ± 0.00\", \"CF\": \"0.48 ± 0.02\"}, \"llama_scierc_unc\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.38 ± 0.05\", \"DR\": \"1.04 ± 0.05\", \"CF\": \"0.00 ± 0.00\"}, \"llama_scierc_con\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.40 ± 0.05\", \"DR\": \"0.03 ± 0.04\", \"CF\": \"0.26 ± 0.02\"}, \"max_sigma_pp\": 0.43, \"greedy_deterministic\": true, \"snr_dr_improvement\": \">12x\", \"qwen_docred_status\": \"pending (not started)\", \"llama_scierc_seed456_con_status\": \"running (407/551)\"}, \"conclusion\": \"success\", \"notes\": \"Greedy decoding is deterministic; constraint effects (DR↓2pp) have SNR > 12× vs hardware variance (σ < 0.5pp). Seeds 123/456 produce byte-identical outputs on same hardware. Cross-server float noise is the only variance source. All σ < 0.5pp. DocRED Qwen not run (greedy determinism confirmed, not worth GPU). Error bars strategy: no error bars, appendix note greedy determinism.\", \"completed_at\": \"2026-05-20T02:42:31.802Z\"}, \"d068_constraint_guided_beam_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:38:01.430Z\", \"updated_at\": \"2026-05-19T16:49:55.045Z\", \"hypothesis\": \"Constraint-guided beam scoring (score = logP - β×violations) reduces CF without degrading DR/F1, by penalizing beams with more constraint violations during search\", \"spec\": {\"command\": \"python run_constrained_extraction.py --constraint_penalty {0.0,0.5,1.0,2.0} --decoding_strategy beam --num_beams 4 --constraint_mode full_s1\", \"server\": \"westd-16980 + westd-21461\", \"data_path\": \"data/processed_data/test.json (SciERC 551 samples)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B LoRA SciERC (qwen3_8b_lora_scierc_merged)\", \"seed\": 42, \"parameters\": {\"beta\": [0, 0.5, 1, 2], \"beam\": 4, \"mode\": \"full_s1\"}, \"claim\": \"Claim 3 + method enhancement\", \"code_location\": \"run_constrained_extraction.py:746-808 run_single_pass_beam()\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"log_path\": \"outputs/d068_guided_beam/ on both servers\", \"partial_result\": \"all violations 0% at ~20% completion - penalty has no effect on LoRA model\", \"negative_reason\": \"LoRA model beam candidates already 0% violations; penalty term always 0; F1 drops 0.3-5.3pp due to multi-sequence decoding noise. Director decided No-Go, killed at ~20% completion.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T16:49:55.045Z\"}, \"d064_docred_full_beam\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:03:41.626Z\", \"updated_at\": \"2026-05-19T14:40:11.790Z\", \"hypothesis\": \"Expanding DocRED beam search (k=4, LoRA+S1) from 50-doc subset to full 998-doc dev set will maintain zero violations (DR=0, RV=0, ET=0) while narrowing the confidence interval upper bound from 5.8% to ~0.3%, strengthening the zero-violation claim for the paper.\", \"spec\": {\"actual_status\": \"STILL RUNNING - startup recovery falsely marked DONE/failed\", \"status_override\": \"2026-05-19T14:40 UTC: Director confirmed processes still running on both servers. d064 will be re-registered as success when all 6 runs complete.\", \"servers\": {\"westd-21461\": \"Qwen beam-4 unc/con + Llama greedy unc/con (cascade)\", \"westd-16980\": \"Llama beam-4 unc + con (Option C: will add Llama greedy unc/con after beam)\"}, \"checkpoint_policy\": \"All Llama results use w5 checkpoint (16980). 21461 Llama greedy (d064 checkpoint) kept as internal reference only.\", \"command\": \"cascade inference scripts on both servers\", \"server\": \"westd-21461 + westd-16980\", \"data_path\": \"/root/autodl-tmp/OntoCoDec/data/docred/\", \"data_count\": 998, \"model_name\": \"Qwen-2.5-7B-Instruct + Llama-3.1-8B-Instruct (LoRA)\", \"seed\": 42}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T12:44:24.620Z\"}, \"d065_tcr_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:43:23.631Z\", \"updated_at\": \"2026-05-19T11:44:17.092Z\", \"hypothesis\": \"TCR's CF elimination generalizes across datasets (DocRED 96 rels, Mistral, 70B) and fine-tuning settings, but effectiveness is inversely correlated with mean schema constraint tightness (κ̄): higher κ̄ (more restrictive schemas like DocRED) produces more fundamental conflicts where no single entity type satisfies all relational contexts, causing DR to increase when CF is forcibly resolved.\", \"parent\": \"d065_tcr_pilot\", \"conclusion\": \"success\", \"metrics\": {\"configs_tested\": 10, \"all_cf_eliminated\": true, \"scierc_all_dr_delta_max\": 0.28, \"docred_lora_dr_delta_max\": 0.14, \"docred_zs_llama_dr_delta\": 9.38, \"docred_zs_70b_dr_delta\": 4.2, \"docred_zs_qwen_dr_delta\": 1.53, \"fund_conflict_scierc_max\": 2.04, \"fund_conflict_docred_zs_max\": 22.78, \"fund_conflict_docred_lora_max\": 12.16, \"lora_ef1_cost_max\": 0.0075, \"zs_docred_ef1_cost_max\": 0.0598}, \"checkpoint_path\": \"outputs/tcr/\", \"log_path\": \"d065_tcr_full_results.md\", \"completed_at\": \"2026-05-19T11:44:17.092Z\"}, \"d065_tcr_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:26:25.109Z\", \"updated_at\": \"2026-05-19T11:41:36.624Z\", \"hypothesis\": \"Post-hoc Type Consistency Resolution (TCR) can reduce CF violations by ≥30% in zero-shot and ≥50% in LoRA settings without increasing DR, by resolving cross-triple entity type conflicts using global relation constraint satisfaction scoring. During-decoding consensus failed (100% skip rate) due to lack of global information; post-hoc TCR has full document context and should succeed where per-token approaches cannot.\", \"conclusion\": \"success\", \"metrics\": {\"scierc_zs_qwen\": {\"cf_before\": 9.75, \"cf_after\": 0, \"dr_before\": 0.93, \"dr_after\": 1.21, \"ef1_delta\": -0.0129, \"fund_pct\": 2.04}, \"scierc_zs_llama\": {\"cf_before\": 6.4, \"cf_after\": 0, \"dr_before\": 0.08, \"dr_after\": 0.3, \"ef1_delta\": -0.0178, \"fund_pct\": 1.85}, \"scierc_lora_qwen\": {\"cf_before\": 1.19, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 0, \"ef1_delta\": -0.0075, \"fund_pct\": 0}, \"scierc_lora_llama\": {\"cf_before\": 0.46, \"cf_after\": 0, \"dr_before\": 0.09, \"dr_after\": 0.09, \"ef1_delta\": -0.0018, \"fund_pct\": 0}, \"scierc_zs_mistral\": {\"cf_before\": 0.67, \"cf_after\": 0, \"dr_before\": 13.36, \"dr_after\": 12.87, \"ef1_delta\": 0.0005, \"fund_pct\": 0}, \"docred_zs_qwen\": {\"cf_before\": 13.11, \"cf_after\": 0, \"dr_before\": 10.21, \"dr_after\": 11.74, \"ef1_delta\": -0.0344, \"fund_pct\": 13.52}, \"docred_zs_llama\": {\"cf_before\": 23.71, \"cf_after\": 0, \"dr_before\": 2.55, \"dr_after\": 11.93, \"ef1_delta\": -0.0521, \"fund_pct\": 22.78}, \"docred_zs_70b\": {\"cf_before\": 11.61, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 4.2, \"ef1_delta\": -0.0598, \"fund_pct\": 18.26}, \"docred_lora_qwen\": {\"cf_before\": 0.42, \"cf_after\": 0, \"dr_before\": 0.01, \"dr_after\": 0.14, \"ef1_delta\": -0.0016, \"fund_pct\": 12.16}, \"docred_lora_llama\": {\"cf_before\": 0.36, \"cf_after\": 0, \"dr_before\": 0.21, \"dr_after\": 0.2, \"ef1_delta\": -0.0017, \"fund_pct\": 11.59}, \"total_configs\": 10, \"all_cf_eliminated\": true}, \"checkpoint_path\": \"outputs/tcr/\", \"log_path\": \"scripts/tcr_resolver.py\", \"completed_at\": \"2026-05-19T11:32:42.343Z\"}, \"d063_gollie_violation_rate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T09:03:40.297Z\", \"updated_at\": \"2026-05-19T10:13:00.612Z\", \"hypothesis\": \"GoLLIE's code-generation IE approach (dataclass instantiation with type annotations) will still produce schema violations (DR/RV/ET) because its type annotations are soft hints in the prompt, not hard token-level constraints during decoding. This demonstrates OntoCoDec's complementary value even for schema-aware IE systems.\", \"conclusion\": \"success\", \"metrics\": {\"gollie_DR\": 0, \"gollie_RV\": 0, \"gollie_ET\": 0, \"gollie_CF\": 0.67, \"gollie_entities\": 300, \"gollie_relations\": 7, \"gollie_empty_docs_pct\": 45, \"docs_tested\": 100}, \"checkpoint_path\": \"outputs/gollie_scierc/violation_results.json\", \"log_path\": \"outputs/gollie_scierc/raw_outputs.jsonl\", \"completed_at\": \"2026-05-19T10:13:00.612Z\"}, \"d062_full_ft_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:32.642Z\", \"updated_at\": \"2026-05-19T05:11:24.604Z\", \"hypothesis\": \"Full fine-tuning Qwen3-8B on SciERC (all parameters, not just LoRA adapters) will yield higher extraction F1 than LoRA FT, and the unconstrained model will still produce schema violations (DR > 0%), confirming OntoCoDec constraints remain necessary even with stronger fine-tuning.\", \"spec\": {\"command\": \"bash scripts/run_d062_full_ft_scierc.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/sft/scierc_sft_train.jsonl\", \"data_count\": 1762, \"model_name\": \"Qwen3-8B (full fine-tuning)\", \"seed\": 42, \"training_method\": \"full_fine_tuning\", \"hyperparams\": {\"lr\": \"2e-4\", \"epochs\": 3, \"batch_size\": 16, \"gradient_checkpointing\": true, \"bf16\": true, \"warmup_ratio\": 0.1, \"optimizer\": \"AdamW\", \"schedule\": \"cosine\"}}, \"reproduce\": {\"finished_at\": \"2026-05-19T04:50:16.081Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T04:50:14.990Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:50:21.524569+00:00\"}]}, \"metrics\": {\"unconstrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 2.74, \"RV_pct\": 0.18, \"ET_pct\": 0, \"CF_pct\": 0}, \"constrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 1.31}, \"training\": {\"eval_loss_final\": 0.09459, \"epochs\": 3, \"total_steps\": 333, \"training_time\": \"21m49s\"}}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_full_ft_scierc/\", \"log_path\": \"/root/autodl-tmp/d062_full_ft_scierc.log\"}, \"d062_beam_latency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:35.458Z\", \"updated_at\": \"2026-05-19T04:30:54.166Z\", \"hypothesis\": \"Beam search (k=4) with constrained decoding will have higher latency overhead relative to greedy than unconstrained beam search, because the constraint processor must independently track and validate grammar/semantic state for each of the 4 beams at every decoding step.\", \"spec\": {\"command\": \"bash scripts/run_d062_beam_latency.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B LoRA FT (SciERC merged)\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/schema_outputs/d062_beam_latency.log\", \"completed_at\": \"2026-05-19T04:30:49.036Z\", \"metrics\": {\"beam4_unconstrained_s_per_doc\": 3.446, \"beam4_constrained_s_per_doc\": 4.013, \"beam4_unconstrained_total_s\": 1898.7, \"beam4_constrained_total_s\": 2211, \"beam_greedy_ratio_unconstrained\": 1.319, \"beam_greedy_ratio_constrained\": 1.397, \"constraint_overhead_beam\": 1.165, \"constraint_overhead_greedy\": 1.1, \"greedy_unconstrained_s_per_doc\": 2.612, \"greedy_constrained_s_per_doc\": 2.873}}, \"d062_ontology_scalability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T04:10:38.904Z\", \"updated_at\": \"2026-05-19T04:28:16.233Z\", \"hypothesis\": \"OntoCoDec's grammar compilation and per-token constraint overhead scale sub-linearly with ontology size (relations and entity types), because the prefix map grows linearly with entity type count but per-token masking only checks the active prefix path, not all types. Compile time may scale super-linearly due to CFG complexity, but inference overhead should remain bounded.\", \"spec\": {\"command\": \"python3 scripts/ontology_scalability_benchmark.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/\", \"data_count\": 40, \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"compile_small_total_s\": 0.334, \"compile_medium_total_s\": 0.322, \"compile_large_total_s\": 0.345, \"compile_xlarge_total_s\": 0.42, \"grammar_small_s\": 0.333, \"grammar_xlarge_s\": 0.365, \"semantic_small_s\": 0.0004, \"semantic_xlarge_s\": 0.017, \"overhead_small\": 1.02, \"overhead_medium\": 1.03, \"overhead_large\": 1.03, \"overhead_xlarge\": 1.03, \"failures\": 0}, \"log_path\": \"/root/autodl-tmp/d062_benchmark.log\", \"checkpoint_path\": \"n/a\", \"completed_at\": \"2026-05-19T04:28:16.233Z\"}, \"d062_cf_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:15:34.085Z\", \"updated_at\": \"2026-05-19T03:23:41.243Z\", \"hypothesis\": \"Majority voting over entity types within each document can reduce CF violations without significantly increasing DR violations, because the most frequent type assignment for each entity is likely the ontology-consistent one.\", \"spec\": {\"command\": \"python3 scripts/cf_majority_voting.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/outputs/\", \"data_count\": 8, \"model_name\": \"n/a (post-hoc)\", \"seed\": 0, \"checkpoint_source\": \"n/a\", \"checkpoint_path\": \"n/a\", \"log_path\": \"outputs/cf_correction_report_*.json\"}, \"metrics\": {\"qwen_scierc_zs\": {\"cf_before\": 245, \"cf_after\": 201, \"dr_rate_before\": 0.0093, \"dr_rate_after\": 0.0324}, \"llama_scierc_zs\": {\"cf_before\": 162, \"cf_after\": 123, \"dr_rate_before\": 0.0008, \"dr_rate_after\": 0.0236}, \"qwen_docred_zs\": {\"cf_before\": 518, \"cf_after\": 21, \"dr_rate_before\": 0.1021, \"dr_rate_after\": 0.1466}, \"llama_docred_zs\": {\"cf_before\": 1358, \"cf_after\": 107, \"dr_rate_before\": 0.0255, \"dr_rate_after\": 0.1665}, \"qwen_scierc_ft\": {\"cf_before\": 21, \"cf_after\": 12, \"dr_rate_before\": 0, \"dr_rate_after\": 0.0071}, \"llama_scierc_ft\": {\"cf_before\": 8, \"cf_after\": 4, \"dr_rate_before\": 0.0009, \"dr_rate_after\": 0.0037}, \"qwen_docred_ft\": {\"cf_before\": 48, \"cf_after\": 3, \"dr_rate_before\": 0.0001, \"dr_rate_after\": 0.0044}, \"llama_docred_ft\": {\"cf_before\": 41, \"cf_after\": 2, \"dr_rate_before\": 0.0021, \"dr_rate_after\": 0.005}}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T03:23:41.243Z\"}, \"p1_ee_ft_llama_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:28:30.109Z\", \"updated_at\": \"2026-05-19T00:06:31.547Z\", \"hypothesis\": \"After fixing schema mismatch (entities not required in EE JSON schema) and adding repetition_penalty=1.2, Llama-3.1-8B FT on WikiEvents EE will produce parseable constrained output with RoV/AC violations eliminated, validating dual-model composability on event extraction.\", \"parent\": \"p1_ee_ft_llama\", \"metrics\": {\"parse_rate_unconstrained\": 1, \"parse_rate_constrained\": 1, \"trigger_f1_unconstrained\": 0.2752, \"trigger_f1_constrained\": 0.2691, \"argument_f1_unconstrained\": 0.0998, \"argument_f1_constrained\": 0.0891, \"entity_f1\": 0, \"rov_rate_unconstrained\": 0.088, \"rov_rate_constrained\": 0, \"ac_rate_unconstrained\": 0.035, \"ac_rate_constrained\": 0.008, \"go_nogo_unconstrained\": 0.122, \"go_nogo_constrained\": 0.0078}, \"conclusion\": \"success\", \"spec\": {\"command\": \"run_constrained_extraction.py (unconstrained + full_s1)\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"data_path\": \"data/wikievents/test.jsonl\", \"data_count\": 20, \"model_name\": \"Llama-3.1-8B-Instruct LoRA FT merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged\", \"eval_data\": \"data/wikievents/test.jsonl (20 docs)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged\", \"log_path\": \"/root/schema_semantic_constrained_ie/logs/unconstrained_r2.log\", \"fixes\": [\"schema required entities->events only\", \"repetition_penalty=1.2\", \"peft AWQ monkey-patch\"]}, \"completed_at\": \"2026-05-18T23:45:05.884Z\"}, \"p1_ee_ft_composability_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:28:28.790Z\", \"updated_at\": \"2026-05-19T00:06:27.494Z\", \"hypothesis\": \"After fixing schema mismatch (entities not required in EE JSON schema) and adding repetition_penalty=1.2, Qwen3-8B FT on WikiEvents EE will produce parseable constrained output with RoV/AC violations eliminated, validating composability on event extraction.\", \"parent\": \"p1_ee_ft_composability_r4\", \"metrics\": {\"unconstrained\": {\"parse_rate\": 0.85, \"trigger_f1\": 0.3208, \"argument_f1\": 0.0785, \"rov_rate\": 0.3831, \"ac_rate\": 0.0268, \"go_nogo\": 0.41}, \"full_s1\": {\"parse_rate\": 0.95, \"trigger_f1\": 0.2672, \"argument_f1\": 0.0818, \"rov_rate\": 0, \"ac_rate\": 0, \"go_nogo\": 0}}, \"spec\": {\"command\": \"bash run_r5_all.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"data_path\": \"data/wikievents/test.jsonl\", \"data_count\": 20, \"model_name\": \"Qwen3-8B LoRA FT merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged\", \"eval_data\": \"data/wikievents/test.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged\", \"log_path\": \"/root/schema_semantic_constrained_ie/logs/r5_all.log\", \"fixes\": [\"schema required entities->events only\", \"repetition_penalty=1.2\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:56:34.434Z\"}, \"p1_ee_ft_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:57:43.193Z\", \"updated_at\": \"2026-05-18T23:23:46.294Z\", \"hypothesis\": \"LoRA fine-tuning Llama-3.1-8B-Instruct on WikiEvents EE (same config as Qwen) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), providing dual-model validation of OntoCoDec composability with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability_r4\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft_llama.sh\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 588752, \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_ee_ft_llama.log\", \"submitted_at\": \"2026-05-18T21:58:17.999Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train_llama.jsonl (generated by Step 0)\", \"data_count\": 194, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"self (LoRA training from base)\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/wikievents/test.jsonl\", \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"lora_dropout\": 0.05, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 4, \"grad_accum\": 4}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_8b_lora_wikievents_merged/\", \"wall_clock_seconds\": 5128.3, \"gpu_hours\": 1.42}, \"conclusion\": \"failed\", \"notes\": \"parse rate 15% constrained, same failure as Qwen\", \"completed_at\": \"2026-05-18T23:23:46.294Z\"}, \"p1_ee_ft_composability_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:50:56.983Z\", \"updated_at\": \"2026-05-18T23:23:35.581Z\", \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability_r3\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft.sh\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"pid\": 61838, \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_ee_ft_composability_r4.log\", \"submitted_at\": \"2026-05-18T21:51:25.516Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/sft/wikievents_sft_train.jsonl\", \"data_count\": 194, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"self (LoRA training from base)\", \"eval_data\": \"/root/schema_semantic_constrained_ie/data/wikievents/test.jsonl\", \"hyperparams\": {\"lora_r\": 16, \"lora_alpha\": 32, \"lora_dropout\": 0.05, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 1, \"grad_accum\": 8}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_wikievents_merged/\", \"wall_clock_seconds\": 5008.7, \"gpu_hours\": 1.39}, \"metrics\": {\"unconstrained\": {\"entity_f1\": 0, \"trigger_f1\": 0.4598, \"argument_f1\": 0.1581, \"rov\": 0.251, \"ac\": 0.06, \"cf\": 0, \"parse_rate\": 0.25}, \"full_s1\": {\"entity_f1\": 0.5823, \"trigger_f1\": 0.6, \"argument_f1\": 0.4667, \"rov\": 0, \"ac\": 0, \"cf\": 0.03, \"parse_rate\": 0.1}}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T23:14:54.256Z\", \"notes\": \"parse rate 10% constrained, FT breaks generation termination calibration\"}, \"p1_llama_ee_ft\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:21:21.236Z\", \"updated_at\": \"2026-05-18T22:25:10.485Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft_llama.sh\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"593696\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_llama_ee_ft.log\", \"submitted_at\": \"2026-05-18T22:25:10.185Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"w9_qwen_docred_zs_sampling_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:56:42.483Z\", \"updated_at\": \"2026-05-18T21:59:17.743Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path /root/autodl-tmp/schema_outputs/w9_docred_remaining.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling_r2.jsonl --batch_size 1 --max_new_tokens 4096 --temperature 0.7 --top_p 0.9 --skip_on_error --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:1\"], \"pid\": \"383602\", \"log_path\": \"/root/autodl-tmp/schema_outputs/w9_docred_r2.log\", \"submitted_at\": \"2026-05-16T19:56:51.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/schema_outputs/w9_docred_remaining.json\", \"data_count\": 892, \"model_name\": \"Qwen3-8B\", \"seed\": null, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling_r2.jsonl\", \"checkpoint_source\": \"Qwen3-8B pretrained (zero-shot)\", \"eval_data\": \"DocRED dev set (remaining 892 docs from index 106)\", \"tmux_session\": \"w9_docred_r2\", \"wall_clock_seconds\": 179718.7, \"gpu_hours\": 49.92}, \"conclusion\": \"success\", \"hypothesis\": \"Continuation of w9 DocRED sampling from doc 106, testing OntoCoDec full_s1 with temperature sampling (T=0.7) on remaining 892 DocRED documents\", \"parent\": \"w9_qwen_docred_zs_sampling\", \"completed_at\": \"2026-05-18T21:52:09.956Z\"}, \"70b_docred_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:43:03.053Z\", \"updated_at\": \"2026-05-18T21:47:50.088Z\", \"hypothesis\": \"OntoCoDec constrained decoding (full_s1 mode) on 70B AWQ-INT4 model eliminates all schema violations (ET, RV, DR) on DocRED without degrading extraction F1, demonstrating scalability to larger models and cross-sentence RE datasets.\", \"parent\": \"70b_scierc_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/70b_docred_constrained.jsonl --mode full_s1 --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"556631\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/70b_docred_constrained.log\", \"submitted_at\": \"2026-05-18T12:48:47.766Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"eval_data\": \"data/docred/dev.json\", \"wall_clock_seconds\": 32228.7, \"gpu_hours\": 8.95}, \"reproduce\": {\"finished_at\": \"2026-05-18T21:42:12.715Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:42:16.440666+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/70b_docred_constrained.jsonl\", \"metrics\": {\"ET_violation\": 0, \"RV_violation\": 0, \"DR_violation\": 0, \"CF_violation\": 7.01, \"entity_f1\": 69.05, \"entity_precision\": 75.03, \"entity_recall\": 63.95, \"relation_f1\": 13.07, \"relation_precision\": 12.54, \"relation_recall\": 13.64, \"parse_failures\": 1, \"docs_processed\": 997, \"total_docs\": 998, \"unique_entities\": 12207, \"total_triples\": 13249}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T21:45:56.501Z\"}, \"70b_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:43:01.940Z\", \"updated_at\": \"2026-05-18T21:45:38.925Z\", \"hypothesis\": \"70B AWQ-INT4 model without constrained decoding serves as baseline to measure unconstrained violation rates on DocRED, establishing the gap that OntoCoDec constrained decoding eliminates.\", \"parent\": \"70b_scierc_constrained\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/70b_docred_unconstrained.jsonl --mode unconstrained --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"556552\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/70b_docred_unconstrained.log\", \"submitted_at\": \"2026-05-18T12:48:47.766Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 32101.9, \"gpu_hours\": 8.92}, \"reproduce\": {\"finished_at\": \"2026-05-18T21:39:02.986Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:39:06.770468+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 69.03, \"entity_precision\": 75.03, \"entity_recall\": 63.92, \"relation_f1\": 13.03, \"relation_precision\": 12.43, \"relation_recall\": 13.69, \"ET_violation\": 0.02, \"RV_violation\": 7.8, \"DR_violation\": 15, \"CF_violation\": 0.07, \"parse_failures\": 0, \"docs_processed\": 998}, \"completed_at\": \"2026-05-18T21:43:49.621Z\"}, \"p1_ee_ft_composability_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:21:22.047Z\", \"updated_at\": \"2026-05-18T21:44:36.846Z\", \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability_r2\", \"spec\": {\"command\": \"bash /root/schema_semantic_constrained_ie/scripts/run_p1_ee_ft.sh\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"58432\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p1_ee_ft_composability_r3.log\", \"submitted_at\": \"2026-05-18T20:40:57.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"RuntimeError: WandbCallback requires wandb to be installed. transformers 5.8.1 ignores WANDB_DISABLED=true, needs report_to=none in TrainingArguments\", \"wall_clock_seconds\": 3818.9, \"gpu_hours\": 1.06}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T21:44:36.846Z\"}, \"p1_ee_ft_composability_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:47:21.742Z\", \"updated_at\": \"2026-05-18T19:55:16.374Z\", \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"parent\": \"p1_ee_ft_composability\", \"spec\": {\"command\": \"bash -c \\\"set -eo pipefail && source /root/miniconda3/bin/activate && cd /root/schema_semantic_constrained_ie && export WANDB_DISABLED=true && export CUDA_VISIBLE_DEVICES=0 && echo '=== Step 1: LoRA Training ===' && python scripts/train_lora_wikievents.py 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_train_r2.log && echo '=== Step 2: Unconstrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode unconstrained --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_unc_infer_r2.log && echo '=== Step 3: Constrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode full_s1 --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_con_infer_r2.log && echo '=== Step 4: Evaluation ===' && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_unc_r2.log && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_con_r2.log && echo '=== Step 5: Violation Check ===' && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_unc_r2.log && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_con_r2.log && echo '=== ALL DONE ===' | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE_r2\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"55824\", \"log_path\": \"/root/autodl-tmp/schema_outputs/p1_ee_ft_train_r2.log\", \"submitted_at\": \"2026-05-18T19:49:03.306Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"source activate + python may have hung on model download; Director confirmed third failure\", \"wall_clock_seconds\": 373.1, \"gpu_hours\": 0.1}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T19:55:16.374Z\"}, \"p1_ee_ft_composability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:21:54.303Z\", \"updated_at\": \"2026-05-18T19:47:11.788Z\", \"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-21461\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T19:23:43.507Z\", \"finished_at\": \"2026-05-18T19:45:36.540Z\", \"training_hours\": 0.36}, \"spec\": {\"command\": \"bash -c \\\"cd /root/schema_semantic_constrained_ie && export WANDB_DISABLED=true && export CUDA_VISIBLE_DEVICES=0 && echo '=== Step 1: LoRA Training ===' && python scripts/train_lora_wikievents.py 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_train.log && echo '=== Step 2: Unconstrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode unconstrained --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_unc_infer.log && echo '=== Step 3: Constrained Inference ===' && python run_constrained_extraction.py --dataset wikievents --mode full_s1 --model_path checkpoints/qwen3_8b_lora_wikievents_merged --data_path data/wikievents/test.jsonl --output_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --device cuda:0 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_con_infer.log && echo '=== Step 4: Evaluation ===' && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_unc.log && python eval_event_extraction.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_eval_con.log && echo '=== Step 5: Violation Check ===' && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_unconstrained.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_unc.log && python violation_checker_wikievents.py --input_path outputs/ee_qwen_ft_wikievents_full_s1.jsonl --constraints_path data/wikievents/ontology_constraints_wikievents.json 2>&1 | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_viol_con.log && echo '=== ALL DONE ===' | tee /root/autodl-tmp/schema_outputs/p1_ee_ft_COMPLETE\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"/root/autodl-tmp/schema_outputs/p1_ee_ft_train.log\", \"submitted_at\": \"2026-05-18T19:42:39.343Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"failure_reason\": \"python: command not found - tmux PATH lacks python binary, need absolute path /root/miniconda3/bin/python\", \"wall_clock_seconds\": 272.4, \"gpu_hours\": 0.08}, \"hypothesis\": \"LoRA fine-tuning Qwen3-8B on WikiEvents EE with correct train/dev/test splits (no data leakage) will produce a model whose unconstrained output has schema violations that are reduced by constrained decoding (full_s1), demonstrating composability of schema constraints with fine-tuned models.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:45:43.143726+00:00\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T19:47:11.788Z\"}, \"p8c_ft_scierc_latency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:43:08.206Z\", \"updated_at\": \"2026-05-18T19:04:35.630Z\", \"metrics\": {\"unconstrained_mean_s\": 2.612, \"constrained_mean_s\": 2.873, \"unconstrained_median_s\": 2.355, \"constrained_median_s\": 2.624, \"overhead_mean_pct\": 10, \"overhead_median_pct\": 11.42, \"per_doc_ratio_mean\": 1.205, \"per_doc_ratio_median\": 1.117, \"num_docs\": 551, \"unconstrained_total_s\": 1439, \"constrained_total_s\": 1582.9}, \"hypothesis\": \"OntoCoDec constrained decoding on fine-tuned Qwen3-8B SciERC has low latency overhead (~10%), confirming practical deployability for fine-tuned models\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py (FT Qwen3-8B SciERC)\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC-FT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\"}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/p8c_timing_ft_constrained.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_outputs/p8c_latency_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T18:45:18.087Z\"}, \"p8b_docred_latency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:14:28.888Z\", \"updated_at\": \"2026-05-18T17:48:57.349Z\", \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B DocRED (200-doc subset) measured on same GPU as P8 SciERC will confirm moderate overhead (<2x), providing consistent timing data for paper\", \"parent\": \"p8_latency_overhead\", \"spec\": {\"command\": \"run_constrained_extraction.py unconstrained+full_s1 then analyze_latency.py\", \"server\": \"westd-21461\", \"data_path\": \"/root/autodl-tmp/schema_outputs/docred_timing_subset_200.json\", \"data_count\": 200, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-8B (base, no fine-tuning)\", \"eval_data\": \"DocRED dev subset 200 docs\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T17:48:57.349Z\"}, \"w9_qwen_docred_zs_sampling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:28:21.393Z\", \"updated_at\": \"2026-05-18T15:49:26.958Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path /root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling.jsonl --batch_size 1 --max_new_tokens 4096 --temperature 0.7 --top_p 0.9 --skip_on_error --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": \"cuda:1\", \"pid\": \"40367\", \"log_path\": \"/root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling.log\", \"submitted_at\": \"2026-05-16T19:29:57.448Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": \"N/A (sampling)\", \"tmux_session\": \"w9_qwen_docred_zs_sampling\", \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/w9_qwen_docred_zs_sampling.jsonl\", \"wall_clock_seconds\": 157505.5, \"gpu_hours\": 43.75, \"kill_reason\": \"Director decision: DocRED sampling ROI too low. SciERC sampling sufficient.\"}, \"conclusion\": \"failed\", \"hypothesis\": \"Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B DocRED will maintain low violation rates while exploring output diversity on cross-sentence RE with 96 relation types\", \"reproduce\": {\"finished_at\": \"2026-05-18T15:15:00.468Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-18T15:15:02.928Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:15:06.410317+00:00\"}]}}, \"w9_qwen_scierc_zs_sampling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:28:19.627Z\", \"updated_at\": \"2026-05-18T15:11:59.448Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w9_qwen_scierc_zs_sampling.jsonl --batch_size 1 --max_new_tokens 4096 --temperature 0.7 --top_p 0.9\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"382074\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w9_qwen_scierc_zs_sampling.log\", \"submitted_at\": \"2026-05-16T19:29:55.453Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 157324.0, \"gpu_hours\": 43.7}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.75, \"CF_pct\": 9.9, \"E_F1\": 31.28, \"R_F1\": 7.42, \"parse_fail_rate\": 0, \"total_samples\": 551, \"note\": \"F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w9_qwen_scierc_zs_sampling.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w9_qwen_scierc_zs_sampling.log\", \"hypothesis\": \"Temperature sampling (T=0.7, top_p=0.9) with OntoCoDec full_s1 on Qwen3-8B SciERC will maintain low violation rates while potentially improving F1 through output diversity compared to greedy decoding\", \"completed_at\": \"2026-05-18T15:11:59.448Z\"}, \"p8_latency_overhead\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:40:32.126Z\", \"updated_at\": \"2026-05-18T15:09:46.707Z\", \"hypothesis\": \"OntoCoDec constrained decoding overhead on Qwen3-8B SciERC is moderate (<2x), demonstrating practical deployability\", \"spec\": {\"command\": \"bash -c \\\"cd /root/schema_semantic_constrained_ie && export HF_HUB_OFFLINE=1 && export CUDA_VISIBLE_DEVICES=1 && /root/miniconda3/bin/python3.12 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/p8_timing_unconstrained.jsonl --max_new_tokens 4096 --skip_on_error --device cuda:0 && echo '=== UNCONSTRAINED DONE ===' && /root/miniconda3/bin/python3.12 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl --max_new_tokens 4096 --skip_on_error --device cuda:0 && echo '=== CONSTRAINED DONE ===' && /root/miniconda3/bin/python3.12 analyze_latency.py /root/autodl-tmp/schema_outputs/p8_timing_unconstrained.jsonl /root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:1\"], \"pid\": \"30982\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p8_latency_overhead.log\", \"submitted_at\": \"2026-05-18T13:43:58.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5147.8, \"gpu_hours\": 1.43}, \"reproduce\": {\"finished_at\": \"2026-05-18T15:07:41.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:07:45.438951+00:00\"}]}, \"metrics\": {\"samples\": 551, \"unconstrained_mean_s\": 4.163, \"unconstrained_median_s\": 4.106, \"unconstrained_total_s\": 2293.7, \"constrained_mean_s\": 4.71, \"constrained_median_s\": 4.644, \"constrained_total_s\": 2595, \"overhead_ratio_mean\": 1.131, \"overhead_ratio_median\": 1.131, \"overhead_ratio_p95_perdoc\": 1.262, \"overhead_pct\": 13.1}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/p8_timing_constrained.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/p8_latency_overhead.log\", \"completed_at\": \"2026-05-18T15:09:46.707Z\"}, \"q1_llama_lora_scierc_beam4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:38:41.024Z\", \"updated_at\": \"2026-05-18T14:20:12.077Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/schema_semantic_constrained_ie && python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --decoding_strategy beam --num_beams 4 --output_path /root/autodl-tmp/schema_outputs/q1_llama_lora_scierc_beam4.jsonl --max_new_tokens 4096 --skip_on_error --device cuda:0\\\"\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"30426\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/q1_llama_lora_scierc_beam4.log\", \"submitted_at\": \"2026-05-18T13:39:49.737Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct-LoRA-SciERC\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\", \"wall_clock_seconds\": 2422.3, \"gpu_hours\": 0.67}, \"hypothesis\": \"Llama-3.1-8B LoRA fine-tuned + beam search k=4 with OntoCoDec full_s1 on SciERC will achieve zero violations (ET=0%, RV=0%, DR=0%, CF=0%), replicating w10_qwen_scierc_ft_beam_4 results on a second model and strengthening the 'zero violations' Abstract claim\", \"parent\": \"w10_qwen_scierc_ft_beam_4\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:12:22.985Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:12:31.003769+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/q1_llama_lora_scierc_beam4.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/q1_llama_lora_scierc_beam4.log\", \"conclusion\": \"success\", \"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 0, \"CF_violation_rate\": 0, \"entity_f1\": 67.94, \"relation_f1\": 46.11, \"samples\": 551, \"total_entities\": 1853, \"total_relations\": 727}, \"completed_at\": \"2026-05-18T14:20:12.077Z\"}, \"70b_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:25:09.814Z\", \"updated_at\": \"2026-05-18T13:34:48.000Z\", \"hypothesis\": \"70B AWQ-INT4 model on SciERC unconstrained baseline will establish violation rates and F1 for large model, testing whether model scale alone reduces ontology violations without constrained decoding\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python run_constrained_extraction.py --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/70b_scierc_unconstrained.jsonl --mode unconstrained --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": \"default\", \"gpu\": \"cuda:0\", \"pid\": 24552, \"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell 98GB\", \"log_path\": \"westd-21461:/tmp/70b_unconstrained.log\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/70b_scierc_unconstrained.jsonl\"}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.5, \"CF_count\": 0, \"CF_pct\": 0, \"E_F1\": 0.3517, \"E_P\": 0.3009, \"E_R\": 0.4232, \"R_F1\": 0.1122, \"R_P\": 0.0929, \"R_R\": 0.1417, \"total_entities\": 2353, \"total_relations\": 1485, \"parse_failures\": 0, \"samples\": 551}, \"conclusion\": \"success\", \"notes\": \"70B unconstrained baseline on SciERC: ET=0% (model scale eliminates entity type errors), RV=0.6%, DR=6.5%, CF=0. E_F1=0.3517, R_F1=0.1122. 551/551 completed, 0 parse failures.\", \"completed_at\": \"2026-05-18T13:34:48.000Z\"}, \"70b_scierc_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:25:10.903Z\", \"updated_at\": \"2026-05-18T13:34:41.438Z\", \"hypothesis\": \"70B AWQ-INT4 model with OntoCoDec constrained decoding (full_s1) on SciERC will achieve 0% ET/RV violations while maintaining or improving F1 vs unconstrained, demonstrating OntoCoDec scales to 70B models\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl --mode full_s1 --max_new_tokens 4096 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-70B-Instruct-AWQ-INT4\", \"seed\": \"default\", \"gpu\": \"cuda:1\", \"pid\": 24703, \"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell 98GB\", \"log_path\": \"westd-21461:/tmp/70b_constrained.log\", \"checkpoint_path\": \"westd-21461:/root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T13:32:04.555Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:32:06.135Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T13:32:11.810517+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/schema_outputs/70b_scierc_constrained.jsonl\", \"notes\": \"70B + OntoCoDec on SciERC: ET=0%, RV=0%, DR=0% (all structural violations eliminated). F1 virtually identical to unconstrained (E_F1=0.3514 vs 0.3517, R_F1=0.1124 vs 0.1122). 86 CF violations (3.66%). Confirms OntoCoDec scales to 70B with zero F1 cost. Cron 之前误标 failed，实际 551/551 完成。\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 86, \"CF_pct\": 3.66, \"E_F1\": 0.3514, \"E_P\": 0.3007, \"E_R\": 0.4226, \"R_F1\": 0.1124, \"R_P\": 0.0932, \"R_R\": 0.1417, \"total_entities\": 2351, \"total_relations\": 1481, \"parse_failures\": 0, \"samples\": 551}}, \"ee_mistral_wikievents_grammar_only_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:55:33.279Z\", \"updated_at\": \"2026-05-18T10:57:01.896Z\", \"hypothesis\": \"Grammar-only mode (no semantic constraints) on Mistral with fixed 938-line code will show high RoV/AC as ablation baseline, confirming semantic layer is essential for constraint compliance\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Mistral-7B-Instruct-v0.3 --mode grammar_only --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_grammar_only_v3.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/ee_mistral_wikievents_grammar_only_v3.jsonl\", \"log_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/violation_report_mistral_grammar_only_v3.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:56:03.323Z\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 64, \"AC\": 13.8, \"CF\": 1.1, \"go_no_go\": 77.73, \"entity_f1\": 0.1192, \"trigger_f1\": 0.0337, \"argument_f1\": 0.0027, \"code_version\": \"938-line (collision+exact-match fix)\", \"mode\": \"grammar_only\"}}, \"ee_mistral_wikievents_constrained_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:55:31.905Z\", \"updated_at\": \"2026-05-18T10:56:59.824Z\", \"hypothesis\": \"938-line fixed code with collision group continuation mask will reduce Mistral AC from 16.6% to near 0% by disambiguating SentencePiece entity type collisions at second+ token steps\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Mistral-7B-Instruct-v0.3 --mode full_s1 --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_constrained_v3_full.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/ee_mistral_wikievents_constrained_v3_full.jsonl\", \"log_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/violation_report_mistral_v3.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:56:02.188Z\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 1.3, \"CF\": 14.9, \"go_no_go\": 1.26, \"entity_f1\": 0.1171, \"trigger_f1\": 0.0387, \"argument_f1\": 0.0031, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 86, \"posthoc_ac_after\": 0}}, \"ee_llama_wikievents_constrained_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:52:02.423Z\", \"updated_at\": \"2026-05-18T10:52:28.084Z\", \"hypothesis\": \"938-line fixed code (collision group + exact-match fix) will maintain RoV=0% and reduce AC for Llama on WikiEvents full 246 docs, confirming cross-model generalization of the fix\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Meta-Llama-3.1-8B-Instruct --mode full_s1 --data_path data/wikievents/all.jsonl --output_path outputs/ee_llama_wikievents_constrained_v3_full.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"checkpoint_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/ee_llama_wikievents_constrained_v3_full.jsonl\", \"log_path\": \"westd-21461:/root/schema_semantic_constrained_ie/outputs/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:52:25.562Z\", \"metrics\": {\"parse_success\": \"207/246 (84.1%)\", \"parse_failures\": 39, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.8, \"CF\": 17.2, \"go_no_go\": 3.8, \"entity_f1\": 0.1763, \"trigger_f1\": 0.0748, \"argument_f1\": 0.0118, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 173, \"posthoc_arg_f1\": 0.0118}}, \"ee_qwen_wikievents_constrained_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:29:11.628Z\", \"updated_at\": \"2026-05-18T10:29:44.522Z\", \"hypothesis\": \"938-line fixed code (collision group + exact-match fix) will maintain RoV=0% and reduce AC from 2.1% to near 0% for Qwen on WikiEvents full 246 docs, confirming the fix generalizes across the full test set\", \"spec\": {\"command\": \"python run_constrained_extraction.py --dataset wikievents --model_path Qwen3-8B --mode full_s1 --data_path data/wikievents/all.jsonl --output_path outputs/ee_qwen_wikievents_constrained_v3_full.jsonl --max_new_tokens 16384 --skip_on_error\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Qwen3-8B\", \"seed\": \"default\", \"checkpoint_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/ee_qwen_wikievents_constrained_v3_full.jsonl\", \"log_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/violation_report_qwen_v3.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:29:37.217Z\", \"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"parse_failures\": 40, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 2.1, \"CF\": 21.1, \"go_no_go\": 2.05, \"entity_f1\": 0.1409, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 109, \"posthoc_arg_f1\": 0.017, \"cf_voting_fix_rate\": \"15.9%\", \"cf_voting_entity_f1\": 0.1352}}, \"ee_mistral_wikievents_constrained_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T21:42:15.493Z\", \"updated_at\": \"2026-05-18T01:42:46.453Z\", \"hypothesis\": \"WikiEvents constrained decoding with fixed tokenizer-agnostic continuation masking (full_s1 + vocab-scan prefix map) will eliminate EV (37.3%→0%) and RoV (63.9%→0%) for Mistral-7B, confirming the fix generalizes OntoCoDec across all three tokenizer families (byte-level BPE + SentencePiece)\", \"parent\": \"ee_mistral_wikievents_constrained\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --constraints_path data/wikievents/ontology_constraints_wikievents.json --data_path data/wikievents/all.jsonl --output_path outputs/ee_mistral_wikievents_constrained_v2_full.jsonl --skip_on_error --resume\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"gpu\": \"cuda:0\", \"pid\": 40830, \"checkpoint_source\": \"base_model:Mistral-7B-Instruct-v0.3\", \"eval_data\": \"data/wikievents/all.jsonl\", \"checkpoint_path\": \"outputs/ee_mistral_wikievents_constrained_v2_full.jsonl\", \"log_path\": \"logs/mistral_constrained_v2_full.log\"}, \"metrics\": {\"parse_success\": \"178/246 (72.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.1, \"AC\": 16.6, \"CF\": 13.9, \"trigger_f1\": 0.0508, \"argument_f1\": 0.0047, \"entity_f1\": 0.1245, \"parse_failures\": 68, \"go_no_go\": 16.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:42:46.453Z\"}, \"ee_qwen_wikievents_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:49:18.898Z\", \"updated_at\": \"2026-05-18T01:42:39.692Z\", \"hypothesis\": \"WikiEvents constrained decoding (full_s1 + continuation masking v2) will eliminate EV violations (24%→0%) and dramatically reduce RoV (74.9%→near 0%) with minimal F1 impact, demonstrating cross-task generalizability of OntoCoDec from RE to EE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name Qwen/Qwen3-8B --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode full_s1 --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_qwen_constrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/wikievents_qwen_constrained_full.jsonl\", \"log_path\": \"logs/qwen_constrained_full.log\"}, \"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.3, \"AC\": 2.1, \"CF\": 21.1, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"entity_f1\": 0.1409, \"parse_failures\": 40, \"go_no_go\": 2.4, \"note\": \"after retry with max_new_tokens=8192\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T22:24:23.672Z\"}, \"ee_mistral_wikievents_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:51:11.907Z\", \"updated_at\": \"2026-05-17T23:52:50.557Z\", \"hypothesis\": \"WikiEvents constrained decoding (full_s1 + continuation masking v2) will eliminate EV violations (37.3%→0%) and dramatically reduce RoV (63.9%→near 0%) with minimal F1 impact, demonstrating cross-task generalizability of OntoCoDec from RE to EE\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python run_constrained_extraction.py --mode full_s1 --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --constraints_path data/wikievents/ontology_constraints_wikievents.json --data_path data/wikievents/all.jsonl --output_path outputs/mistral_constrained_full.jsonl --resume\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/mistral_constrained_full.jsonl\", \"log_path\": \"logs/mistral_constrained_full.log\"}, \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"184/246 (74.8%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 54.8, \"AC\": 19.2, \"CF\": 0.7, \"note\": \"grammar_only baseline (old code without semantic mask fix)\"}, \"completed_at\": \"2026-05-17T23:52:50.557Z\"}, \"ee_llama_wikievents_constrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:49:20.228Z\", \"updated_at\": \"2026-05-17T23:52:42.652Z\", \"hypothesis\": \"WikiEvents constrained decoding (full_s1 + continuation masking v2) will eliminate EV violations (10.5%→0%) and dramatically reduce RoV (88.8%→near 0%) with minimal F1 impact, demonstrating cross-task generalizability of OntoCoDec from RE to EE\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name meta-llama/Llama-3.1-8B-Instruct --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode full_s1 --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_llama_constrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/wikievents_llama_constrained_full.jsonl\", \"log_path\": \"logs/llama_constrained_full.log\"}, \"metrics\": {\"parse_success\": \"215/246 (87.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.4, \"CF\": 15.5, \"trigger_f1\": 0.078, \"argument_f1\": 0.011, \"entity_f1\": 0.178, \"parse_failures\": 31, \"go_no_go\": 3.4, \"note\": \"after retry with max_new_tokens=8192\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T22:24:24.731Z\"}, \"ee_mistral_wikievents_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:51:09.310Z\", \"updated_at\": \"2026-05-17T20:52:08.375Z\", \"hypothesis\": \"WikiEvents zero-shot unconstrained baseline: Mistral-7B-Instruct-v0.3 will produce significant EV and RoV violations due to lack of schema constraints, establishing baseline violation rates for cross-task generalizability evaluation\", \"spec\": {\"command\": \"HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python run_constrained_extraction.py --mode unconstrained --dataset wikievents --model_path /root/autodl-tmp/.ms_cache/mistralai/Mistral-7B-Instruct-v0___3/ --data_path data/wikievents/all.jsonl --output_path outputs/mistral_unconstrained_full.jsonl\", \"server\": \"westd-21461\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": \"default\", \"checkpoint_path\": \"outputs/mistral_unconstrained_full.jsonl\", \"log_path\": \"logs/mistral_restart.log\"}, \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"194/246 (78.9%)\", \"ET\": 0, \"EV\": 37.3, \"RoV\": 63.9, \"AC\": 0, \"CF\": 0, \"trigger_f1\": 0.0241, \"argument_f1\": 0, \"entity_f1\": 0}, \"completed_at\": \"2026-05-17T20:52:08.375Z\"}, \"ee_llama_wikievents_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:35:35.416Z\", \"updated_at\": \"2026-05-17T19:36:23.547Z\", \"hypothesis\": \"WikiEvents zero-shot unconstrained baseline: Llama-3.1-8B will produce significant EV and RoV violations due to lack of schema constraints, establishing baseline violation rates for cross-task generalizability evaluation\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name meta-llama/Llama-3.1-8B-Instruct --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode unconstrained --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_llama_unconstrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"checkpoint_path\": \"N/A\", \"log_path\": \"outputs/wikievents_llama_unconstrained_full.jsonl\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:36:15.874Z\", \"metrics\": {\"parse_success\": \"226/246 (91.9%)\", \"ET\": 0, \"EV\": 10.5, \"RoV\": 88.8, \"AC\": 0.1, \"CF\": 0, \"trigger_f1\": 0.0572, \"argument_f1\": 0, \"entity_f1\": 0}}, \"ee_qwen_wikievents_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T19:35:34.282Z\", \"updated_at\": \"2026-05-17T19:36:21.800Z\", \"hypothesis\": \"WikiEvents zero-shot unconstrained baseline: Qwen3-8B will produce significant EV and RoV violations due to lack of schema constraints, establishing baseline violation rates for cross-task generalizability evaluation\", \"spec\": {\"command\": \"python run_constrained_extraction.py --model_name Qwen/Qwen3-8B --dataset wikievents --data_path data/wikievents/all.jsonl --constraint_mode unconstrained --ontology_path data/wikievents/ontology_constraints_wikievents.json --output_file outputs/wikievents_qwen_unconstrained_full.jsonl --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/wikievents/all.jsonl\", \"data_count\": 246, \"model_name\": \"Qwen/Qwen3-8B\", \"seed\": \"default\", \"checkpoint_path\": \"N/A\", \"log_path\": \"outputs/wikievents_qwen_unconstrained_full.jsonl\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T19:36:14.859Z\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"ET\": 0, \"EV\": 24, \"RoV\": 74.9, \"AC\": 0.3, \"CF\": 0, \"trigger_f1\": 0.1184, \"argument_f1\": 0.0009, \"entity_f1\": 0}}, \"r4_prompt_detailed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:33:16.258Z\", \"updated_at\": \"2026-05-17T17:02:29.748Z\", \"spec\": {\"command\": \"python run_prompt_sensitivity.py --prompt_variant detailed\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"443521\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/r4_prompt_detailed.log\", \"submitted_at\": \"2026-05-17T12:33:16.038Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"outputs/r4_detailed_full_s1.jsonl\", \"wall_clock_seconds\": 16153.7, \"gpu_hours\": 4.49}, \"hypothesis\": \"OntoCoDec constraint enforcement is robust to prompt variation: a detailed prompt (with type definitions and extraction guidelines) should achieve similar DR reduction as the default prompt\", \"metrics\": {\"unconstrained\": {\"ET_pct\": 0.22, \"RV_pct\": 0.45, \"DR_pct\": 11.07, \"E_F1\": 33.55, \"R_F1\": 10.48}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.64, \"E_F1\": 33.56, \"R_F1\": 10.48}, \"DR_reduction_pct\": 94.2, \"delta_R_F1_pp\": 0, \"delta_E_F1_pp\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T17:02:29.748Z\"}, \"r4_prompt_minimal\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:33:14.503Z\", \"updated_at\": \"2026-05-17T17:02:28.635Z\", \"spec\": {\"command\": \"python run_prompt_sensitivity.py --prompt_variant minimal\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"443445\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/r4_prompt_minimal.log\", \"submitted_at\": \"2026-05-17T12:33:14.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"outputs/r4_minimal_full_s1.jsonl\", \"wall_clock_seconds\": 16154.4, \"gpu_hours\": 4.49}, \"hypothesis\": \"OntoCoDec constraint enforcement is robust to prompt variation: a minimal prompt (listing only entity/relation types) should achieve similar DR reduction as the default prompt\", \"metrics\": {\"unconstrained\": {\"ET_pct\": 0.58, \"RV_pct\": 1.16, \"DR_pct\": 16.91, \"E_F1\": 31.98, \"R_F1\": 7.91}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.92, \"E_F1\": 31.99, \"R_F1\": 7.85}, \"DR_reduction_pct\": 94.6, \"delta_R_F1_pp\": -0.06, \"delta_E_F1_pp\": 0.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T17:02:28.635Z\"}, \"w10_qwen_scierc_ft_beam_4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:47:48.852Z\", \"updated_at\": \"2026-05-17T10:27:12.254Z\", \"hypothesis\": \"FT+beam composability: Qwen3-8B SciERC LoRA FT + beam k=4 + full_s1 constraints will reduce residual DR from FT greedy (0.20%) to 0%, demonstrating that beam search eliminates the last constraint-search failures even in fine-tuned models. Validates full-stack OntoCoDec+FT+beam composability.\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w10_qwen_scierc_ft_beam_k4.jsonl --decoding_strategy beam --num_beams 4 --device cuda:0 --batch_size 1 --max_new_tokens 2048 --max_samples 551\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-LoRA-SciERC (FT)\", \"seed\": 42}, \"metrics\": {\"DR\": 0, \"CF\": 0, \"total_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0, \"E_F1\": 66.88, \"E_P\": 64.69, \"E_R\": 69.22, \"R_F1\": 44.23, \"R_P\": 39.41, \"R_R\": 50.41, \"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1802, \"total_relations\": 1246, \"vs_ft_greedy\": {\"baseline\": \"w5_lora_scierc_constrained_eval\", \"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"1.18% → 0.0% (eliminated all violations)\", \"E_F1_delta\": \"67.05 → 66.88 (-0.17, negligible)\", \"R_F1_delta\": \"43.77 → 44.23 (+0.46, slight improvement)\"}, \"vs_zs_beam_k4\": {\"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"0.53% → 0.0% (eliminated)\", \"E_F1_delta\": \"32.00 → 66.88 (+34.88)\", \"R_F1_delta\": \"8.56 → 44.23 (+35.67)\"}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w10_qwen_scierc_ft_beam_k4.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/logs/w10_qwen_scierc_ft_beam_k4.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:27:12.254Z\"}, \"w10_beam_ablation_k8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:31:56.573Z\", \"updated_at\": \"2026-05-17T09:46:19.797Z\", \"hypothesis\": \"Beam search k=8 on Qwen3-8B SciERC (551 docs) will match or marginally improve on k=4 (DR=0%, CF=0.53%), testing whether larger beam width yields diminishing returns for constraint satisfaction once DR is already eliminated.\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/scierc_qwen_beam_k8_551.jsonl --decoding_strategy beam --num_beams 8 --device cuda:1 --max_samples 551\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (ZS)\", \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.08, \"CF_count\": 2, \"E_F1\": 32.18, \"R_F1\": 8.39, \"E_P\": 26.95, \"E_R\": 39.93, \"R_P\": 6.54, \"R_R\": 11.7, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1744, \"total_entities\": 2483, \"vs_greedy\": {\"DR_delta\": -0.93, \"CF_delta\": -9.82, \"E_F1_delta\": 1.2, \"R_F1_delta\": 0.03}, \"vs_beam_k4\": {\"DR_delta\": 0, \"CF_delta\": -0.45, \"E_F1_delta\": 0.18, \"R_F1_delta\": -0.17}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_qwen_beam_k8_551.jsonl\", \"log_path\": \"N/A - submit_training_job tmux\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:46:19.797Z\"}, \"w9_mistral_docred_beam_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:40:36.971Z\", \"updated_at\": \"2026-05-17T09:42:22.695Z\", \"hypothesis\": \"Beam search (k=4) on Mistral-7B DocRED (50 docs) will reduce DR from greedy baseline (33.21%) through broader token exploration, but entity type misclassification limits improvement. Boundary condition for beam search effectiveness.\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset docred --model_path mistralai/Mistral-7B-Instruct-v0.3 --decoding_strategy beam --num_beams 4 --max_samples 50\", \"server\": \"westd-21461\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 50, \"model_name\": \"Mistral-7B-Instruct-v0.3 (ZS)\", \"seed\": 42}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w9_mistral_docred_beam4_full_s1.jsonl\", \"log_path\": \"N/A - retroactive registration\", \"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 21.37, \"CF_violations\": 1, \"total_triples\": 524, \"total_entities\": 597, \"docs_checked\": 49, \"parse_failures\": 1, \"E_F1\": 51.78, \"E_P\": 65.2, \"E_R\": 42.94, \"R_F1\": 5.7, \"R_P\": 6.49, \"R_R\": 5.08, \"R_tp\": 34, \"R_gold\": 669, \"R_pred\": 524}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:42:22.695Z\"}, \"w10_beam_ablation_k2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:31:55.361Z\", \"updated_at\": \"2026-05-17T09:32:16.894Z\", \"hypothesis\": \"Beam search k=2 on Qwen3-8B SciERC (551 docs) will partially reduce DR and CF compared to greedy (DR=0.93%, CF=9.90%), but less effectively than k=4 (DR=0%, CF=0.53%). Establishes the lower bound of the beam size-constraint satisfaction curve.\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/scierc_qwen_beam_k2_551.jsonl --decoding_strategy beam --num_beams 2 --device cuda:0 --max_samples 551\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (ZS)\", \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.35, \"CF_count\": 71, \"CF_pct\": 4.12, \"E_F1\": 31.54, \"R_F1\": 8.75, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1724, \"vs_greedy\": {\"DR_delta\": -0.58, \"CF_delta\": -5.78, \"E_F1_delta\": 0.56, \"R_F1_delta\": 0.39, \"note\": \"Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36\"}, \"vs_beam_k4\": {\"DR_delta\": 0.35, \"CF_delta\": 3.59, \"E_F1_delta\": -0.46, \"R_F1_delta\": 0.19, \"note\": \"k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56\"}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_qwen_beam_k2_551.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_beam_ablation_k2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T09:32:16.894Z\"}, \"w10_mistral_scierc_beam_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:24:10.347Z\", \"updated_at\": \"2026-05-17T08:33:57.080Z\", \"hypothesis\": \"Beam search (k=4) on Mistral SciERC will reduce DR from greedy baseline (13.4%) through broader token-level exploration, but entity type misclassification may limit improvement compared to calibrated models (Qwen/Llama achieve DR=0% with beam). Completes the 3x2 beam search matrix.\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/scierc_mistral_beam_551.jsonl --decoding_strategy beam --num_beams 4 --device cuda:0\", \"server\": \"westd-21461\", \"gpu\": [\"cuda:0\"], \"pid\": \"5112\", \"model_name\": \"Mistral-7B-Instruct-v0.3 (ZS)\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"notes\": \"No fix_mistral_regex. Completes 3x2 beam matrix.\"}, \"metrics\": {\"total_samples\": 551, \"parse_failures\": 1, \"parse_rate\": 0.9982, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.79, \"CF_pct\": 0.57, \"E_P\": 23.04, \"E_R\": 31.64, \"E_F1\": 26.66, \"R_P\": 3.13, \"R_R\": 7.22, \"R_F1\": 4.37, \"total_entities\": 2294, \"total_triples\": 2241, \"vs_greedy\": {\"baseline\": \"w6_mistral_scierc_constrained\", \"greedy_DR\": 13.4, \"greedy_CF\": 1.27, \"greedy_E_F1\": 27.46, \"greedy_R_F1\": 3.67, \"delta_DR\": \"+0.39pp\", \"delta_CF\": \"-0.70pp\", \"delta_E_F1\": \"-0.80pp\", \"delta_R_F1\": \"+0.70pp\"}}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_mistral_beam_551.jsonl\", \"log_path\": \"/root/runs/schema_semantic_constrained_ie/w10_mistral_scierc_beam_551.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T08:33:53.672Z\", \"analysis\": \"Beam search (k=4) on Mistral SciERC shows mixed results vs greedy. R_F1 improved (+0.70pp, 4.37 vs 3.67) and CF violations halved (0.57% vs 1.27%), but DR slightly worse (13.79% vs 13.4%) and E_F1 slightly worse (26.66 vs 27.46). Hypothesis partially falsified: beam search did not reduce DR violations. Consistent with finding that Mistral entity type misclassification is the bottleneck, not token-level exploration breadth.\"}, \"w10_llama_docred_beam_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:11:24.746Z\", \"updated_at\": \"2026-05-17T07:56:15.809Z\", \"hypothesis\": \"Beam search (k=4) on Llama DocRED will reduce DR and CF violations, completing the beam search matrix (3rd model-dataset combination). Llama's weaker entity typing on DocRED may limit DR elimination compared to Qwen.\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_llama_beam_50.jsonl --decoding_strategy beam --num_beams 4 --device cuda:0 --max_samples 50\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"424211\", \"model_name\": \"Llama-3.1-8B-Instruct (ZS)\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 50, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.94, \"E_F1\": 55.62, \"R_F1\": 9.47, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"total_samples\": 50, \"vs_greedy_full_s1\": {\"DR_delta\": -2.57, \"CF_delta\": -11.19, \"E_F1_delta\": 0.61, \"R_F1_delta\": 3.2, \"note\": \"Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27\"}, \"checker_note\": \"Must use violation_checker_docred.py for DocRED (not violation_checker.py)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_llama_beam_50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_llama_docred_beam_50.log\", \"completed_at\": \"2026-05-17T07:37:38.035Z\"}, \"w10_type_consensus_docred_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:06:56.659Z\", \"updated_at\": \"2026-05-17T07:09:42.510Z\", \"hypothesis\": \"GTC Layer 3 on DocRED (96 relation types, complex schema) will reduce CF violations while maintaining DR through DR-aware skip mechanism; skip frequency expected higher than SciERC due to more type ambiguity in fine-grained ontology\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset docred --type_consensus --max_samples 50 --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"419622\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log\", \"submitted_at\": \"2026-05-17T06:07:17.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/processed_data/docred_test.json\", \"data_count\": 50, \"seed\": 42, \"notes\": \"GTC Layer 3 v2 on DocRED 96-type schema. Testing skip frequency under complex ontology.\", \"wall_clock_seconds\": 3745.3, \"gpu_hours\": 1.04}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 8.69, \"CF_pct\": 2.4, \"E_F1\": 59.08, \"R_F1\": 8.33, \"gtc_skip_total\": 601, \"gtc_skip_unique_entities\": 213, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_full_s1_consensus_50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_docred_50.log\", \"completed_at\": \"2026-05-17T07:09:42.510Z\"}, \"w10_type_consensus_prototype\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:07:18.638Z\", \"updated_at\": \"2026-05-17T07:09:41.619Z\", \"hypothesis\": \"Document-level type consensus constraint (forcing same entity text to receive identical type across all relation triples) will eliminate CF violations caused by inconsistent type assignment, reducing CF from ~9.90% toward 0% on SciERC without increasing DR\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode full_s1 --dataset scierc --type_consensus --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"417859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log\", \"submitted_at\": \"2026-05-17T05:34:19.247Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"notes\": \"GTC Layer 3 v2 (DR-aware skip). Kill switch: DR>2% → abort.\", \"wall_clock_seconds\": 5722.4, \"gpu_hours\": 1.59}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36, \"gtc_skip_total\": 672, \"gtc_skip_unique_entities\": 258, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/scierc_full_s1_consensus_v2.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w10_type_consensus_prototype.log\", \"completed_at\": \"2026-05-17T07:09:41.619Z\"}, \"w9_qwen_scierc_stability_3seeds\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:55:58.164Z\", \"updated_at\": \"2026-05-17T05:05:28.139Z\", \"hypothesis\": \"Greedy full_s1 constraint results on SciERC are stable across random seeds: DR should remain in 0.7-1.2% range (near the 0.93% baseline), demonstrating that the single-run result is not an outlier\", \"spec\": {\"command\": \"bash run_stability_test.sh (seeds 123,456,789 sequential)\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"406710\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"seed\": \"123,456,789\"}, \"metrics\": {\"seed_123\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_456\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_789\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"cross_seed_DR_std\": 0, \"cross_seed_DR_range\": 0, \"conclusion_note\": \"Greedy decoding is fully deterministic - seed has no effect on output. All metrics identical across 3 seeds.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/stability_seed123.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/stability_test.log\", \"completed_at\": \"2026-05-17T05:05:28.139Z\"}, \"w9_qwen_docred_beam_50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:48:50.746Z\", \"updated_at\": \"2026-05-17T04:50:39.890Z\", \"hypothesis\": \"Beam search (k=4) on Qwen3-8B DocRED 50 docs with full_s1: DR should decrease from greedy baseline 10.21% but likely not reach 0% due to DocRED's tighter schema (96 types, avg 5.68 valid pairs). Tests whether beam exploration can find legal paths in a complex constraint space.\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --decoding_strategy beam --num_beams 4 --max_samples 50 --output_path outputs/w9_qwen_docred_beam_50.jsonl\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"412229\", \"model_name\": \"Qwen3-8B\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 50, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.55, \"E_F1\": 58.64, \"R_F1\": 9.37, \"total_samples\": 50, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"vs_greedy_full_s1\": {\"DR_delta\": -10.21, \"CF_delta\": -2.02, \"E_F1_delta\": -0.73, \"R_F1_delta\": 1.14, \"note\": \"Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema.\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w9_qwen_docred_beam_50.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w9_qwen_docred_beam_50.log\", \"completed_at\": \"2026-05-17T04:50:39.891Z\"}, \"w9_llama_scierc_beam_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:18:21.758Z\", \"updated_at\": \"2026-05-17T03:45:51.748Z\", \"hypothesis\": \"Beam search (k=4) with full_s1 constraints on Llama-3.1-8B SciERC 551 docs will show DR reduction similar to Qwen (0.93%→0%), confirming beam search compatibility is model-agnostic\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --beam_size 4 --output_path outputs/llama_scierc_beam_full_s1_551.jsonl\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"406047\", \"model_name\": \"Llama-3.1-8B-Instruct\", \"data_path\": \"data/scierc/test.json\", \"data_count\": 551, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.93, \"CF_count\": 15, \"E_F1\": 25.04, \"E_P\": 21.27, \"E_R\": 30.42, \"R_F1\": 3.33, \"R_P\": 2.68, \"R_R\": 4.41, \"total_entities\": 2398, \"total_relations\": 1606, \"parse_fail_rate\": 0, \"total_samples\": 551, \"vs_greedy_full_s1\": {\"DR_delta\": -0.08, \"CF_delta\": -5.63, \"E_F1_delta\": 1.55, \"R_F1_delta\": 0.79, \"note\": \"Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/schema_constrained_ie/outputs/llama_scierc_beam_full_s1_551.jsonl\", \"log_path\": \"/root/autodl-tmp/schema_constrained_ie/outputs/llama_scierc_beam_full_s1_551.log\", \"completed_at\": \"2026-05-17T03:45:51.748Z\"}, \"posthoc_filtering_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:46:07.823Z\", \"updated_at\": \"2026-05-17T02:56:24.306Z\", \"spec\": {\"hypothesis\": \"Post-hoc filtering baseline: generate unconstrained triples then remove DR/RV/ET violations. Comparison with OntoCoDec decoding-time enforcement on precision, recall, coverage, and residual violations.\", \"command\": \"python posthoc_filter.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/outputs/\", \"data_count\": 2, \"model_name\": \"Qwen3-8B (unconstrained outputs)\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/posthoc_report_docred.json\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/posthoc_report_scierc.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:46:23.429Z\", \"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}, \"hypothesis\": \"Zero-shot unconstrained output 上跑 post-hoc filtering（规则删除违规三元组）作为 constrained decoding 的替代方案。预期 post-hoc 能消除 DR 但丢失有效三元组导致 recall 下降，证明解码时约束优于后处理。\", \"parent\": \"phase2_scierc_unconstrained\"}, \"phase2_scierc_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:36:35.941Z\", \"updated_at\": \"2026-05-17T02:56:23.629Z\", \"spec\": {\"command\": \"bash -c \\\"tmux kill-session -t phase2_scierc_full_s2 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s2.jsonl --device cuda:0 --batch_size 1 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s2.log\", \"submitted_at\": \"2026-05-14T01:07:00.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 368.6, \"gpu_hours\": 0.1}, \"hypothesis\": \"S2 两通道约束解码全量验证 — Grammar (Pass 1) + Semantic (Pass 2) 分离式约束。S2 pilot50 已验证 D/R violation=0%，全量运行检验 F1 稳定性和 per-relation 效果。与 S1 对比验证两种架构的 F1-violation trade-off。\", \"notes\": \"✅ 全量完成 551/551 via --resume. S2 两通道约束解码结果。DR=0.97% (vs S1 0.93%), RV=0%, ET=0%, R-F1=0.0803, E-F1=0.319.\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T01:06:58.685Z\", \"command\": \"bash -c \\\"tmux kill-session -t phase2_scierc_full_s2 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s2.jsonl --device cuda:0 --batch_size 1 --resume\\\"\", \"finished_at\": \"2026-05-14T01:13:08.809Z\", \"training_hours\": 0.1}, \"pid\": 144858, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s2.log\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T01:13:09.036Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:13:12.640712+00:00\"}]}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s2.jsonl\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"parent\": \"phase2_s2_pilot50\"}, \"llama_docred_unconstrained_mt6144\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:17:33.154Z\", \"updated_at\": \"2026-05-17T02:56:22.209Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"246947\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained_mt6144.log\", \"submitted_at\": \"2026-05-15T08:19:27.565Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20932.1, \"gpu_hours\": 5.81}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": \"246947\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained_mt6144.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"finished_at\": \"2026-05-15T13:59:24.508Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:59:25.767053+00:00\"}]}, \"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained_mt6144.jsonl\", \"notes\": \"mt6144 vs mt4096 对比: parse_failures 68→67 (-1, 几乎无变化); unique_entities 11525→11534 (+9); triples 16437→16584 (+147, +0.9%); E-F1 55.65%→55.67% (+0.02pp); R-F1 5.98%→5.95% (-0.03pp); DR 26.07%→26.18% (+0.11pp); RV 16.03%→15.89% (-0.14pp); ET/CF 不变. 67 个 FAIL 中绝大多数 inference time ~96s (仍触发 max_tokens cap), 说明这些失败主要源于模型陷入重复循环直到 token 上限, 而非文档过长. 增加 max_new_tokens 不能挽救此类失败. 训练 wall clock 约 5h39m, 比 mt4096 (~5h02m) 多约 37 分钟. 结论: max_new_tokens 4096→6144 对 unconstrained 生成无实质影响, 不建议采用作为后续 baseline.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:08:19.680Z\", \"hypothesis\": \"Llama DocRED unconstrained max_tokens=6144 重跑，消除输出截断。预期三元组产出量增加，violation profile 可能因完整输出而变化，为 constrained 对比提供公平 baseline。\", \"parent\": \"llama_docred_unconstrained\"}, \"llama_docred_full_s1_mt6144\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T08:17:36.675Z\", \"updated_at\": \"2026-05-17T02:56:21.312Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"finished_at\": \"2026-05-15T14:59:20.782Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T08:19:51.861Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:19:53.379823+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:59:25.181921+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"247487\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log\", \"submitted_at\": \"2026-05-15T08:22:03.222Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24176.2, \"gpu_hours\": 6.72}, \"pid\": \"247487\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log\", \"notes\": \"⚠️ 变量混淆：此实验同时包含 CF fallback 代码修改 + max_tokens 6144（两个变量）。CF 数据可作为 'Llama DocRED with fallback + mt6144' 参考点，但不能用于纯 CF ablation 对比。纯 CF ablation 必须控制 max_tokens=4096。unconstrained_mt6144 不受影响（不走 semantic layer）。\", \"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_full_s1_mt6144.jsonl\", \"hypothesis\": \"Llama DocRED full_s1 max_tokens=6144 重跑，消除原实验输出截断。若截断导致丢失有效三元组，预期 R-F1 提升；DR 应维持近 0%。\", \"parent\": \"llama_docred_full_s1\"}, \"beam_search_scierc_full_551\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:42:41.314Z\", \"updated_at\": \"2026-05-17T02:56:20.332Z\", \"hypothesis\": \"Beam search (size=4) with OntoCoDec constraints on SciERC full set will maintain DR≈0% (as seen in 50-doc dry-run) while improving F1 over greedy, demonstrating decoding-strategy-agnostic constraint enforcement\", \"spec\": {\"command\": \"python run_constrained_extraction.py --decoding_strategy beam --num_beams 4 --constraint_mode full_s1 (SciERC 551 docs)\", \"server\": \"westd-16980\", \"data_path\": \"SciERC test set\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"gpu\": \"cuda:0\", \"pid\": \"399097\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"westd-16980:/root/schema_semantic_constrained_ie/outputs/beam_search_scierc_full_551.jsonl\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T01:43:45.104Z\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.53, \"E_F1\": 32, \"R_F1\": 8.56, \"E_P\": 26.83, \"E_R\": 39.63, \"R_P\": 6.69, \"R_R\": 11.91, \"parse_fail_rate\": 0, \"total_entities\": 2476, \"total_relations\": 1737}, \"parent\": \"phase2_scierc_full_s1\"}, \"w7_llama_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:47:04.863Z\", \"updated_at\": \"2026-05-17T02:56:17.967Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Llama-3.1-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"pid\": 344026, \"log_path\": \"/tmp/w7_llama_scierc_ft_semantic_only.log\"}, \"hypothesis\": \"FT Llama + semantic-only ablation on SciERC: isolate semantic layer contribution in FT regime. Semantic层单独能否消除DR? 与grammar_only对比揭示两层各自贡献。\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}, \"checkpoint_path\": \"outputs/w7_llama_scierc_ft_semantic_only.jsonl\", \"notes\": \"551/551 完成。Semantic-only 在 FT Llama 上: DR=0.65% (vs unconstrained 1.11%, grammar_only 1.11%, full_s1 0.09%)。Semantic 约束单独将 DR 降低 42%，但不如 full_s1 的 grammar+semantic 联合约束。R_F1=45.47% 与 baseline 持平，无质量损失。CF=2 是新增的 cross-field 一致性问题。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:32:01.872Z\", \"parent\": \"w5_llama_lora_scierc_unconstrained_eval\"}, \"w7_llama_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:47:02.522Z\", \"updated_at\": \"2026-05-17T02:56:17.093Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Llama-3.1-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"pid\": 342707, \"log_path\": \"/tmp/w7_llama_scierc_ft_grammar_only.log\"}, \"hypothesis\": \"FT Llama + grammar-only ablation on SciERC: isolate grammar layer contribution in FT regime. FT已修复RV/ET(均0%), DR残留1.11%. Grammar-only能否消除DR?\", \"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}, \"checkpoint_path\": \"outputs/w7_llama_scierc_ft_grammar_only.jsonl\", \"log_path\": \"/tmp/w7_llama_scierc_ft_grammar_only.log\", \"notes\": \"551/551 complete. As expected, grammar_only does not reduce DR (1.11% same as unconstrained FT baseline). ET=0%, RV=0%, CF=0% all clean. F1 slightly better than Qwen FT grammar_only (E_F1=0.6776 vs 0.6705, R_F1=0.4545 vs 0.4386).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:49:15.016Z\", \"parent\": \"w5_llama_lora_scierc_unconstrained_eval\"}, \"w7_qwen_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:46:59.364Z\", \"updated_at\": \"2026-05-17T02:56:16.228Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"pid\": 340898, \"log_path\": \"/tmp/w7_qwen_scierc_ft_semantic_only.log\"}, \"hypothesis\": \"FT Qwen + semantic-only ablation on SciERC: isolate semantic layer contribution in FT regime. Semantic层单独能否消除DR? 与grammar_only对比揭示两层各自贡献。\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}, \"checkpoint_path\": \"outputs/w7_qwen_scierc_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T07:25:31.487Z\", \"notes\": \"551/551 完成。Semantic-only 在 FT Qwen 上: DR 1.95%→0.6% (−68%), ET/RV=0%。CF=15（grammar 层对 CF 有抑制作用）。F1 与 grammar_only 几乎一致 (R_F1=0.4369 vs 0.4386)。Ablation 结论: grammar 层消除 RV/ET，semantic 层消除 DR。两层互补，缺一不可——grammar_only DR=1.9%(未降)，semantic_only DR=0.6%(降68%)，full_s1 DR=0%(完全消除)。\", \"parent\": \"w5_lora_scierc_unconstrained_eval\"}, \"w7_qwen_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:46:56.566Z\", \"updated_at\": \"2026-05-17T02:56:15.201Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"pid\": 337069, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w7_qwen_scierc_ft_grammar_only.log\"}, \"hypothesis\": \"FT Qwen + grammar-only ablation on SciERC: isolate grammar layer contribution in FT regime. FT已修复RV/ET(均0%), DR残留1.95%. Grammar-only能否消除DR?\", \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:42.468Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:41:43.361Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:45.053980+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}, \"notes\": \"551/551 完成。Grammar-only 在 FT Qwen 上: ET/RV/CF 全部清零，DR 残留 1.9% (22/1128)——与 unconstrained (1.95%) 几乎一致，说明 grammar 层不约束 DR，DR 消除完全依赖 semantic 层。E_F1=0.6705, R_F1=0.4386 与 unconstrained 持平。Tokenizer regex 警告为 transformers 4.57.6 false positive (Reviewer PASS)。\", \"parent\": \"w5_lora_scierc_unconstrained_eval\"}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:40.179Z\", \"updated_at\": \"2026-05-17T02:56:13.750Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"287667\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_llama_lora_scierc_unconstrained.jsonl\", \"submitted_at\": \"2026-05-15T17:19:48.001Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"Meta-Llama-3.1-8B-Instruct-LoRA-SciERC\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\", \"parent\": \"w5_llama_lora_scierc_training\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"wall_clock_seconds\": 271.9, \"gpu_hours\": 0.08}, \"hypothesis\": \"Fine-tuned Llama-3.1-8B SciERC unconstrained eval — 验证 LoRA 后残余 DR 是否仍 >2%，决定 OntoCoDec 在 fine-tuned Llama 上的 composability 价值。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:24:19.934Z\", \"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}, \"parent\": \"w5_llama_lora_scierc_training\"}, \"w5_llama_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:42.462Z\", \"updated_at\": \"2026-05-17T02:56:12.734Z\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraint_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_constrained.jsonl --mode full_s1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"290317\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_lora_scierc_constrained_eval.log\", \"submitted_at\": \"2026-05-15T17:38:56.723Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama-3.1-8b-instruct-lora-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"SciERC test set (551 samples)\", \"wall_clock_seconds\": 2003.1, \"gpu_hours\": 0.56}, \"hypothesis\": \"Fine-tuned Llama-3.1-8B + OntoCoDec constrained eval on SciERC — composability 验证：约束解码在 fine-tuned Llama 上仍有效且不损 F1。完成 Llama SciERC 2×2 matrix。\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:59:25.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:59:27.794917+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}, \"checkpoint_path\": \"outputs/w5_llama_lora_scierc_constrained.jsonl\", \"completed_at\": \"2026-05-15T18:12:19.787Z\", \"parent\": \"w5_llama_lora_scierc_training\"}, \"w5_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:57:42.154Z\", \"updated_at\": \"2026-05-17T02:56:11.350Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_full_s1_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"282127\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_constrained_eval.log\", \"submitted_at\": \"2026-05-15T15:58:03.052Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1664.8, \"gpu_hours\": 0.46}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"282127\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_constrained_eval.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_full_s1_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-15T16:22:21.690Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:22:23.113142+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}, \"hypothesis\": \"Fine-tuning + constrained decoding composability: 约束解码在 fine-tuned 模型上仍有效，且不显著损害 F1\", \"checkpoint_path\": \"checkpoints/qwen3_8b_lora_scierc_merged\", \"completed_at\": \"2026-05-15T16:25:47.858Z\", \"parent\": \"w5_lora_scierc_training\"}, \"w1_cf_fallback_scierc_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:32:48.425Z\", \"updated_at\": \"2026-05-17T02:56:05.216Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"270088\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log\", \"submitted_at\": \"2026-05-15T14:07:14.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2999.4, \"gpu_hours\": 0.83}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"270088\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-15T14:47:53.690Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:47:54.986519+00:00\"}]}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_scierc_pilot.jsonl\", \"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}, \"notes\": \"CF fallback 实验在 SciERC + Qwen3-8B 上的 pilot 结果：CF 从 9.90% 下降到 0.04% (-9.86pp)，但 DR 从 0.93% 上升到 14.78% (+13.85pp)。DR+CF budget 净增 +3.99pp。F1 几乎不变 (E-F1=30.98% 与 baseline 完全一致；R-F1=8.23%, -0.13pp)。Grammar-first fallback 触发率 36.64% (6237/17024 mask calls)，CF-registry fallback 4.48%。判定：成功降低 CF 但代价是 DR 大幅恶化，违规没有真正减少，只是从 CF 转移到 DR。建议改进方向：(1) 仅在 CF-registry 命中时回退，保留 DR enforcement；(2) rebuttal 中诚实呈现这是 violation re-routing 而非 reduction。详细报告见 artifact w1_cf_fallback_scierc_pilot_analysis。\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T14:57:13.885Z\", \"hypothesis\": \"Constrained fallback (CF) 策略 SciERC pilot：约束解码产生空输出时回退至 unconstrained 生成，预期降低空输出率同时维持 violation 控制。若 fallback 频率过高则 CF 策略不可行。\"}, \"w5_lora_scierc_training\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T14:56:20.233Z\", \"updated_at\": \"2026-05-17T02:55:56.797Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 scripts/train_lora_scierc.py\\\"\", \"finished_at\": \"2026-05-15T15:16:50.985Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T14:58:56.873Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:58:58.618383+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:16:52.498789+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 scripts/train_lora_scierc.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"276523\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log\", \"submitted_at\": \"2026-05-15T15:02:11.699Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"wall_clock_seconds\": 1068.6, \"gpu_hours\": 0.3}, \"pid\": \"276523\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log\", \"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}, \"conclusion\": \"success\", \"hypothesis\": \"Qwen3-8B LoRA fine-tune on SciERC 建立 fine-tuned baseline，用于 composability 验证。预期 E-F1/R-F1 大幅提升但残余 DR>0%，证明 FT 后 OntoCoDec 约束解码仍有价值。\"}, \"w8_qwen_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:13:03.945Z\", \"updated_at\": \"2026-05-16T15:25:52.761Z\", \"hypothesis\": \"FT Qwen DocRED + grammar_only eval: FT 后 DR 残留 0.76%，grammar_only 能消除多少？与 w8_llama_docred_ft_grammar_only 配对，补全 DocRED FT ablation 两模型对比。预期 DR≈0.76%（与 SciERC 模式一致：grammar 层不约束 DR）。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_qwen_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-21461\", \"gpu\": 0, \"pid\": 18555, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log\", \"submitted_at\": \"2026-05-16T09:27:52.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path_final\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log\", \"wall_clock_seconds\": 21480.4, \"gpu_hours\": 5.97}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:20:38.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:20:40.840918+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}, \"completed_at\": \"2026-05-16T15:25:52.761Z\"}, \"w6_mistral_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:59:02.565Z\", \"updated_at\": \"2026-05-16T10:41:37.382Z\", \"hypothesis\": \"Mistral (3rd model) SciERC unconstrained baseline — 获取 zero-shot violation profile (DR/RV/ET) 和 F1，验证 OntoCoDec 三模型泛化性\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w6_mistral_scierc_unconstrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"pid\": 332156, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_scierc_unconstrained.log\", \"submitted_at\": \"2026-05-16T04:53:56.502Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"wall_clock_seconds\": 2104.7, \"gpu_hours\": 0.58, \"checkpoint_path\": \"N/A\"}, \"notes\": \"Mistral-7B unconstrained SciERC: E_F1=0.2728, R_F1=0.0366. 0% parse failures. 56.94% dangling relations, 1.5% ET violations, 0% RV violations. Poor IE performance typical of unconstrained 7B model on SciERC.\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:27:35.554Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:27:39.086911+00:00\"}]}, \"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w6_mistral_scierc_unconstrained.jsonl\", \"completed_at\": \"2026-05-16T05:29:01.251Z\"}, \"w6_mistral_scierc_constrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T02:59:03.181Z\", \"updated_at\": \"2026-05-16T10:40:00.429Z\", \"hypothesis\": \"Mistral-7B constrained SciERC (full_s1 mode) - test if schema constraints reduce violations and improve F1 vs unconstrained baseline (E_F1=0.2728, R_F1=0.0366, DR=56.94%)\", \"failure_reason\": \"TypeError: xgrammar.GrammarMatcher.accept_token expected int but got ffi.Tensor. xgrammar/tvm version mismatch on westd-21461. Crashed 10s after start.\", \"completed_at\": \"2026-05-16T05:28:06.343Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w6_mistral_scierc_constrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"pid\": 334606, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_scierc_constrained.log\"}, \"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}, \"notes\": \"Mistral-7B constrained SciERC: 551/551 complete, 0 failures. OntoCoDec eliminated ET (1.5%→0%) and RV (0%→0%), reduced DR massively (56.94%→13.4%, -43.54pp). F1 unchanged (E_F1=0.2746 vs 0.2728, R_F1=0.0367 vs 0.0366). Residual DR 13.4% much higher than FT models (~1-2%), consistent with zero-shot regime needing stronger semantic constraints.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\"}, \"w8_ft_posthoc_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.203Z\", \"updated_at\": \"2026-05-16T09:35:31.720Z\", \"hypothesis\": \"FT 后 DR<2%，post-hoc filtering 能否替代 OntoCoDec？对 4 组 FT unconstrained output 跑 posthoc_filter.py，量化 recall 损失和 coverage 代价。预期：post-hoc 过滤虽消除 DR 但丢失 TP（recall 下降），证明 constrained decoding 的 generation-time 优势。\", \"conclusion\": \"success\", \"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}, \"notes\": \"零样本 + FT 两组 post-hoc baseline 完成。关键发现：ZS 下 post-hoc R_F1 在全部 5 组中 ≥ constrained R_F1（Qwen DocRED 差距最大 +1.38pp）。原因：post-hoc 删除大量 FP 提升 precision，recall 损失有限（TP_lost 仅占 rejected 的 1-2%）。constrained decoding 在 ZS 下强制约束干扰模型分布，总体 F1 反而略低。论文论点需调整：constrained decoding 的 ZS 价值不在 \\\"F1 保留\\\" 而在 \\\"生成时硬保证 0% violations + composability\\\"。\", \"checkpoint_path\": \"N/A (CPU-only analysis, no checkpoint)\", \"log_path\": \"N/A (CPU-only analysis)\", \"completed_at\": \"2026-05-16T09:35:31.720Z\"}, \"w6_mistral_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T02:59:03.876Z\", \"updated_at\": \"2026-05-16T09:28:49.721Z\", \"hypothesis\": \"Mistral (3rd model) DocRED unconstrained baseline — 获取复杂 schema (96 relations) 下的 violation profile，与 Qwen/Llama 对比\", \"notes\": \"PID 5571 on cuda:0 via nohup. Model loaded from symlink /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 -> ms_cache. 2x RTX PRO 6000 Blackwell 98GB. Log at /tmp/w6_mistral_docred_unconstrained.log.\", \"failure_reason\": \"\", \"completed_at\": \"2026-05-16T05:28:07.908Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 5571 on cuda:0 via nohup. Model loaded from symlink /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 -> ms_cache. 2x RTX PRO 6000 Blackwell 98GB. Log at /tmp/w6_mistral_docred_unconstrained.log.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:47.316246+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_unconstrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": 0, \"pid\": 7740, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_docred_unconstrained.log\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:44.102Z\"}, \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T03:19:37.979Z\", \"updated_at\": \"2026-05-16T09:10:49.476Z\", \"hypothesis\": \"Mistral (3rd model) + OntoCoDec constrained eval on DocRED — 验证约束解码在第三模型+复杂 schema 上的泛化性\", \"notes\": \"Constrained decoding eliminates ET/RV violations completely (0%), reduces DR from 57.42%→33.20% (-24.22pp). E_F1 +2.08pp, R_F1 +2.02pp vs unconstrained. DR残余33%来自semantic constraint未覆盖的domain-range组合。\", \"failure_reason\": \"Process killed by fix worker (pkill) during orphan cleanup. Had 15/998 samples before kill.\", \"completed_at\": \"2026-05-16T05:31:30.251Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 6789 on cuda:1 via nohup. Patched xgrammar 0.2.0 hf.py (accept_token .item() fix for transformers 5.8.1 compat). Model loaded from symlink. Log at /tmp/w6_mistral_docred_constrained.log.\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_constrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": 1, \"pid\": 8347, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_docred_constrained.log\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}, \"checkpoint_path\": \"outputs/w6_mistral_docred_constrained.jsonl\", \"conclusion\": \"success\"}, \"w5_qwen_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:03:33.642Z\", \"updated_at\": \"2026-05-16T08:10:01.206Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Qwen DocRED 上是否仍能消除残余 DR 且不损 R-F1\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"321568\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_constrained_eval.log\", \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"notes\": \"由另一个 worker 提交，本次确认进程正常运行。PID 321568 (GPU subprocess), wrapper PID 321563, tmux session. CUDA_VISIBLE_DEVICES=1 由 wrapper 控制。模型已加载，2/998 开始推理。Grammar 编译 96 relation types 后开始生成。ETA ~5-6h (参考 unconstrained 5.82h, constrained 更慢)。\", \"reproduce\": {\"finished_at\": \"2026-05-16T08:05:39.680Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:05:41.651478+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w5_qwen_docred_lora_constrained_eval.jsonl\", \"completed_at\": \"2026-05-16T08:10:01.206Z\"}, \"w5_llama_docred_sft_data_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:07:32.770Z\", \"updated_at\": \"2026-05-16T03:21:57.320Z\", \"hypothesis\": \"Generate Llama-3.1-8B-Instruct format DocRED SFT train/dev JSONL — prerequisite for Llama DocRED LoRA fine-tune (composability matrix Llama×DocRED cell)\", \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}, \"spec\": {\"checkpoint_path\": \"N/A (data gen)\", \"log_path\": \"N/A (data gen)\", \"command\": \"python3 prepare_sft_data_docred_llama.py\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/\", \"data_count\": 4051, \"model_name\": \"N/A\", \"seed\": 42}, \"completed_at\": \"2026-05-16T03:20:06.742Z\"}, \"w1_cf_fallback_llama_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:33:00.998Z\", \"updated_at\": \"2026-05-16T03:21:56.516Z\", \"spec\": {\"hypothesis\": \"W1 CF fallback 在 Llama DocRED 上的效果。Llama DocRED full_s1 原 CF=12.02%（最高），预期 fallback 大幅降低。Phase 3 实验。\", \"parent\": \"llama_docred_full_s1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_llama_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"killed\", \"notes\": \"D020: 取消。CF fallback 改为 Analytical Finding 方案，仅用 SciERC pilot 数据。D027 确认 Qwen DocRED CF fallback 代码未生效（实际跑 full_s1）。Analytical finding 结论跨模型适用——CF↔DR 根本性张力不依赖模型选择。最终状态: killed。\", \"completed_at\": \"2026-05-16T03:19:55.843Z\"}, \"w1_cf_fallback_llama_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:32:57.470Z\", \"updated_at\": \"2026-05-16T03:21:55.322Z\", \"spec\": {\"hypothesis\": \"W1 CF fallback 在 Llama SciERC 上的跨模型验证。Llama SciERC full_s1 原 CF=6.56%，预期显著降低。Phase 2 实验。\", \"parent\": \"llama_scierc_full_s1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_llama_scierc.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"gpu\": \"cuda:1\"}, \"conclusion\": \"killed\", \"notes\": \"D020: 取消。CF fallback 改为 Analytical Finding 方案，仅用 SciERC pilot 数据。Qwen SciERC pilot 已充分证明 CF↔DR re-routing（CF -9.86pp 但 DR +13.85pp，budget +3.99pp）。跨模型重复无额外信息量。最终状态: killed。\", \"completed_at\": \"2026-05-16T03:19:54.869Z\"}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:03:32.625Z\", \"updated_at\": \"2026-05-16T01:55:03.824Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"304006\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log\", \"submitted_at\": \"2026-05-15T20:03:48.762Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"wall_clock_seconds\": 20941.5, \"gpu_hours\": 5.82}, \"reproduce\": {\"finished_at\": \"2026-05-16T01:49:51.884Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:49:53.877179+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:52:50.220Z\", \"notes\": \"998/998 完成, 927 success / 71 fail. 两组指标已计算. parse_fail_rate=7.11% 高于 Llama(2.3%), Qwen 在长文档上更易超时. R_F1=40.86 略低于 Llama(43.72), E_F1=82.15 略低于 Llama(83.93). DR_pct=0.76% 高于 Llama(0.49%), 说明 Qwen LoRA 残留更多 domain-range 违规.\"}, \"w5_llama_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T19:58:07.956Z\", \"updated_at\": \"2026-05-16T00:22:57.512Z\", \"hypothesis\": \"Fine-tuned Llama-3.1-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta\", \"parent\": \"w5_llama_docred_lora_training\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:11:58.831Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-15T23:14:38.851Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:14:41.289164+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:12:00.360157+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SIGTERM (exit 143) — 外部 kill，非 OOM/崩溃。日志尾部无 Traceback，正常生成中被终止。运行 3.27h (998 samples, batch=1, max_tokens=4096)。已有 ops worker (ops:llama_eval_timeout_fix) 在处理修复重提。| 已有成果: 可能有部分输出 (outputs/w5_llama_docred_lora_unconstrained_eval.jsonl) | 建议: 等 ops worker 完成后确认重提结果\"}}, \"notes\": \"Process received SIGTERM (exit 143) after completing all 998/998 samples. Output file verified complete. Log shows 776 pad_token_id warnings (batch_size=1, some samples produce multiple warnings). No OOM, no traceback. SIGTERM likely from job scheduler timeout, but all inference output was already written. Diagnosed and reclassified from failed→success on 2026-05-16.\", \"spec\": {\"command\": \"nohup python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_unconstrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"312930\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-8B-Instruct-LoRA-DocRED\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:52.649Z\", \"updated_at\": \"2026-05-15T20:02:42.106Z\", \"hypothesis\": \"Qwen3-8B LoRA fine-tune on DocRED — 填补 Qwen DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"298245\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_training.log\", \"submitted_at\": \"2026-05-15T18:22:06Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6015.9, \"gpu_hours\": 1.67}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:01:28.494Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:55:53.910959+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:01:30.155403+00:00\"}]}, \"notes\": \"Retry #4 (PID 298245, cuda:1): 级联故障修复后由 ops worker 重提交。前次失败原因: GPU 0 幽灵进程争抢显存 + 命令中 CUDA_VISIBLE_DEVICES 硬编码覆盖 wrapper。修复后 wrapper 统一控制 CUDA_VISIBLE_DEVICES。双卡 99% util 已确认。ETA ~2h on RTX PRO 6000。\", \"completed_at\": \"2026-05-15T20:02:21.920Z\", \"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:15:19.269Z\", \"updated_at\": \"2026-05-15T19:57:16.365Z\", \"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on DocRED — 填补 Llama DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred_llama.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"298323\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_training.log\", \"submitted_at\": \"2026-05-15T18:23:07Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"wall_clock_seconds\": 5649.4, \"gpu_hours\": 1.57}, \"notes\": \"Retry #1 (PID 298323, cuda:0): 级联故障修复后重提。首次提交(PID 297434)因幽灵进程占满 cuda:0 显存导致 OOM。修复: 移除命令中 CUDA_VISIBLE_DEVICES 硬编码，由 wrapper 统一控制。参数对齐 Llama SciERC LoRA: rank=16, alpha=32, lr=2e-4, 3 epochs, bs=2, grad_accum=8, max_length=4096。ETA ~80-90min on RTX PRO 6000。输出: checkpoints/llama_lora_docred/ (adapter) + /root/autodl-tmp/checkpoints/llama_lora_docred_merged/ (merged)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T19:54:59.123Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:55:00.912384+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged/\", \"completed_at\": \"2026-05-15T19:57:16.365Z\"}, \"w5_docred_sft_data_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:51:09.748Z\", \"updated_at\": \"2026-05-15T18:01:39.032Z\", \"hypothesis\": \"Generate DocRED SFT train/dev JSONL from train_annotated.json + dev.json — prerequisite for Qwen/Llama DocRED LoRA fine-tune\", \"spec\": {\"command\": \"python3 scripts/prepare_sft_data_docred.py\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"292314\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T17:51:19.316Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/\", \"data_count\": 4051, \"model_name\": \"Qwen3-8B\", \"seed\": null, \"wall_clock_seconds\": 379.5, \"gpu_hours\": 0.11, \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:51:44.980Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:51:46.380733+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train.jsonl,/root/schema_semantic_constrained_ie/data/docred/sft_dev.jsonl\", \"completed_at\": \"2026-05-15T17:57:38.825Z\", \"notes\": \"数据质量验证完成：4051行全部JSON解析通过，0损坏。Prompt用Qwen3 chat模板（含think tag），6实体类型+96关系类型。Completion为合法JSON（entities+relations）。数据可直接用于SFT训练。Train: 3053样本/19M, Dev: 998样本/6.0M。\"}, \"w5_llama_lora_scierc_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:38.168Z\", \"updated_at\": \"2026-05-15T17:24:38.949Z\", \"spec\": {\"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on SciERC, extending Claim 3 composability to cross-model. Mirrors Qwen3-8B LoRA config (r=16, alpha=32, lr=2e-4, 3 epochs).\", \"parent\": \"w5_lora_scierc_training\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"dataset\": \"SciERC\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"log_path\": \"logs/w5_llama_lora_scierc_training.log\", \"adapter_path\": \"checkpoints/llama_lora_scierc\", \"base_model\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct\"}, \"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on SciERC — 扩展 composability 验证到跨模型。预期：(1) LoRA 训练后 E-F1/R-F1 大幅提升（对标 Qwen LoRA +36pp/+36pp）；(2) 为 Llama SciERC 2×2 composability matrix 提供 fine-tuned baseline。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:17:30.599Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}, \"completed_at\": \"2026-05-15T17:18:45.275Z\"}, \"w1_cf_fallback_docred\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T10:32:53.234Z\", \"updated_at\": \"2026-05-15T16:55:58.012Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\"}, \"notes\": \"Reviewer #12 三次确认: 实际运行 --mode full_s1 (非 CF fallback), 与 phase2_docred_full_s1 重复。CF fallback 代码恢复失败或未生效。命令行明确显示 --mode full_s1。PID 283824 已 kill。W1 CF fallback 整体定论: SciERC pilot (analytical finding) 已充分, DocRED 不再重跑。\", \"completed_at\": \"2026-05-15T15:47:59.075Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"notes\": \"D020: Director 取消全部 CF fallback 实验。改用 Analytical Finding 方案——pilot negative 本身作为论文素材。仅跑约 30s 即被终止。\"}}, \"spec\": {\"command\": \"bash -c \\\"rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"283824\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_docred.log\", \"submitted_at\": \"2026-05-15T16:26:41.953Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed - ran wrong code)\", \"wall_clock_seconds\": 1756.1, \"gpu_hours\": 0.49}, \"pid\": \"283824\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_docred.log\", \"conclusion\": \"killed\"}, \"w5_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:23:25.030Z\", \"updated_at\": \"2026-05-15T16:01:58.250Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B still produces >2% decode rate violations on SciERC unconstrained, justifying OntoCoDec constraint application\", \"parent\": \"w5_lora_scierc_training\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_unconstrained_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 278380, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"data_count_note\": \"551 per-sentence samples derived from 100 SciERC test documents (matches phase2_scierc_unconstrained sample count)\", \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\", \"seed\": null, \"checkpoint_source\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test set (551 samples)\", \"constraints_path\": \"/root/schema_semantic_constrained_ie/ontology_constraints.json\", \"output_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.log\", \"mode\": \"unconstrained\", \"max_new_tokens\": 4096, \"batch_size\": 1, \"path_note\": \"Task spec called for data/scierc/test.json + data/scierc/ontology_constraints_scierc.json which do not exist on this server; substituted the actual paths used by all prior phase2_scierc_* experiments.\"}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 278385, \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\", \"completed_at\": \"2026-05-15T15:55:17.802Z\", \"notes\": \"LoRA fine-tuned Qwen3-8B unconstrained eval on SciERC: 聚合 DR=1.95% 略低于 2% gate 阈值，但按关系类型拆分后 Evaluate-for DR=13.13%（99 个三元组中 13 个违规）、Part-of 5.8%、Compare 5.0%。表明 tight-constraint 关系是 fine-tuning 无法覆盖的长尾——OntoCoDec 的互补价值在于消除这些 schema-ambiguous relation 的残余 DR。Quality: R-F1=43.9% (+35.7pp vs base), E-F1=67.1% (+36.1pp vs base). ET/RV/CF 全部清零。\"}, \"llama_docred_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:59.855Z\", \"updated_at\": \"2026-05-14T20:29:59.744Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"194295\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1.log\", \"submitted_at\": \"2026-05-14T14:41:22.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20912.7, \"gpu_hours\": 5.81}, \"hypothesis\": \"Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上的效果。与 Qwen3-8B DocRED full_s1 (DR 10.19%) 对比，验证约束解码在不同模型+复杂 schema 上的泛化性。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T14:39:33.737Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T20:24:03.061Z\", \"training_hours\": 5.74}, \"pid\": \"194295\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:24:04.262279+00:00\"}]}, \"checkpoint_path\": \"outputs/llama_docred_full_s1.jsonl\", \"completed_at\": \"2026-05-14T20:24:03Z\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}, \"conclusion\": \"success\", \"notes\": \"ET/RV→0%, DR 26.07%→2.55% (优于Qwen的10.19%)。但CF从0.17%暴涨至12.02%，说明Llama的entity type预测更容易被约束扰动。F1基本持平(E-F1 -0.64pp, R-F1 +0.29pp)。Parse failures从68增至91。Grammar-first fallback频繁触发。\"}, \"llama_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:58.719Z\", \"updated_at\": \"2026-05-14T19:45:08.201Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"193605\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained.log\", \"submitted_at\": \"2026-05-14T14:35:57.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18533.7, \"gpu_hours\": 5.15}, \"hypothesis\": \"Llama-3.1-8B-Instruct 在 DocRED unconstrained baseline。与 Qwen3-8B DocRED unconstrained 对比 violation 分布。验证不同模型在复杂 schema (96 relations) 上的 violation 模式差异。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T14:15:03.413Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T19:39:03.154Z\", \"training_hours\": 5.4}, \"pid\": \"193605\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:39:05.142651+00:00\"}]}, \"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}, \"conclusion\": \"success\", \"notes\": \"v2 checker (unique_et dedup) + all_set F1。930/998 docs parsed (68 parse failures, 6.8% vs Qwen 1.2%)。Violation profile 与 Qwen3-8B 显著不同：RV 大幅降低 (16.03% vs 29.66%，-13.6pp，Llama 更倾向使用标准关系名) 但 DR 更高 (26.07% vs 18.46%，+7.6pp，即使关系名正确 head/tail 类型约束违反更多)。ET 极低 (0.13% vs 2.48%，-2.35pp)，CF 接近 (0.17% vs 0.10%)。F1 弱于 Qwen: R-F1 5.98% vs 7.74% (-1.76pp)，E-F1 55.65% vs 58.15% (-2.50pp)。DR 26.07% 为约束解码提供更大改进空间。\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained.jsonl\", \"completed_at\": \"2026-05-14T19:44:51.441Z\"}, \"phase2_docred_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:55:50.031Z\", \"updated_at\": \"2026-05-14T18:52:55.527Z\", \"hypothesis\": \"Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_grammar_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"150766\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"/root/runs/schema_semantic_constrained_ie/docred_grammar_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_grammar_only.jsonl\", \"completed_at\": \"2026-05-14T07:40:10.382Z\"}, \"llama_scierc_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:56.936Z\", \"updated_at\": \"2026-05-14T18:31:43.217Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"190648\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_full_s1.log\", \"submitted_at\": \"2026-05-14T13:50:35.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 1249.5, \"gpu_hours\": 0.35}, \"hypothesis\": \"Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 SciERC 上的效果。与 Qwen3-8B full_s1 (DR 0.93%) 对比，验证 OntoCoDec 的 model-agnostic 特性。零代码修改。D009 cross-model 验证核心实验。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:50:33.979Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-14T14:11:24.215Z\", \"training_hours\": 0.35}, \"pid\": \"190648\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_full_s1.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:11:25.248Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:11:26.755217+00:00\"}]}, \"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_scierc_full_s1.jsonl\", \"notes\": \"550/551 samples (1 corrupt line from duplicate PID removed). DR 0.08% — 约束合规性极好，优于 Qwen3-8B full_s1 (0.93%)。但 E-F1=23.49% (vs Qwen 30.98%), R-F1=2.54% (vs Qwen 8.36%)，Llama 在 IE 质量上显著弱于 Qwen。对比 Llama unconstrained: DR 13.3%→0.08% (约束生效), E-F1 23.56%→23.49% (持平), R-F1 2.68%→2.54% (微降)。约束大幅降低违规率但未提升抽取质量。Cross-field consistency violations 较高 (6.56%)。\"}, \"llama_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:55.421Z\", \"updated_at\": \"2026-05-14T18:31:40.240Z\", \"spec\": {\"data_path\": \"scierc_test\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"command\": \"python3 run_extraction.py --config configs/llama_scierc_unconstrained.yaml\", \"server\": \"westd-16980\"}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:19:48.866Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-14T13:46:24.376Z\", \"training_hours\": 0.44}, \"pid\": \"188367\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_unconstrained.log\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 SciERC unconstrained baseline — 验证 OntoCoDec 跨模型泛化性。零代码修改，与 Qwen3-8B unconstrained 对比 violation 分布差异。预期 DR~15%, RV~1.4%, ET~0.4%（Llama instruction-following 可能更好）。D009 cross-model 验证的第一步。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:46:25.548989+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_scierc_unconstrained.jsonl\", \"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"completed_at\": \"2026-05-14T13:49:13.425Z\", \"notes\": \"Llama-3.1-8B-Instruct SciERC unconstrained baseline 完成。551 样本（550成功/1失败）。Violation: ET=0%, RV=0.5%, DR=13.3%。F1: E-F1=23.56%, R-F1=2.68%。与 Qwen3-8B unconstrained 对比：Llama violation 略低（DR 13.3% vs 15.4%），但 F1 明显更差（E-F1 低7.5pp, R-F1 低5.5pp）。Llama 更倾向保守提取——提取数量少、violation 低但 recall 也低。Qwen3 在 unconstrained 设定下提取质量优于 Llama。\"}, \"phase2_scierc_full_s1\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T21:48:44.785Z\", \"updated_at\": \"2026-05-14T18:31:34.603Z\", \"hypothesis\": \"Grammar + Semantic 双层约束 (S1 单通道) 能否同时消除 rv + dr violations？F1 变化是关键：<2pp 降=完美，2-5pp=可接受 trade-off，>5pp=需要 S2 策略\", \"notes\": \"✅ _v2 干净数据全量完成 551/551. DR violation = 0.93% (baseline 15.37%, -14.44pp). ET=0%, RV=0%. 数据来源: phase2_scierc_full_s1_v2.jsonl\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T23:49:56.383Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python3 && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s1.jsonl --device cuda:0 --batch_size 1\\\"\", \"finished_at\": \"2026-05-14T00:33:47.489Z\", \"training_hours\": 0.73}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-13T23:45:41.906Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:45:42.821098+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:33:48.999924+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断完成: EXIT_CODE=127, bash: line 1: python3: command not found。Root cause: submit_training_job 未在命令前加 conda 环境激活。修复方案: 命令前缀加 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。retry_count=0, 自动重试中。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 run_constrained_extraction.py --mode full_s1 ...\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"retry #2: bash -c wrapping fixes EXIT_CODE=127\"}, \"pid\": \"134593\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s1.log\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl\"}, \"phase2_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T21:48:44.427Z\", \"updated_at\": \"2026-05-14T18:31:31.811Z\", \"hypothesis\": \"Semantic-only constrained decoding (TypeConstraintProcessor) 能否消除 domain/range violations？预期 dr_violation→0%，但可能影响 F1（约束过强导致生成偏移）\", \"notes\": \"✅ _v2 干净数据全量完成 551/551. DR violation = 11.65% (baseline 15.37%, -3.72pp). ET=0.4%, RV=1.51%.\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:49:33.935Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python3 && python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_semantic_only.jsonl --device cuda:0 --batch_size 1\\\"\", \"finished_at\": \"2026-05-14T00:33:32.617Z\", \"training_hours\": 0.73}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-13T23:45:39.272Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:45:40.115539+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:33:34.349694+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断完成: EXIT_CODE=127, bash: line 1: python3: command not found。Root cause: 同 phase2_scierc_full_s1, submit 未激活 conda。修复方案同上。retry_count=0, 自动重试中。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 run_constrained_extraction.py --mode semantic_only ...\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"retry #2: bash -c wrapping fixes EXIT_CODE=127\"}, \"pid\": \"134202\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_semantic_only.log\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_semantic_only_v2.jsonl\"}, \"phase2_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T21:48:43.487Z\", \"updated_at\": \"2026-05-14T18:31:29.442Z\", \"hypothesis\": \"Grammar-only constrained decoding (XGrammar JSON schema + enum) 能否消除 relation vocabulary violations 同时不影响 F1？预期 rv_violation→0%, dr_violation 不变\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:39:02.641Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T22:38:46.650Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:38:47.328842+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:39:03.395560+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断中: 进程到 176/551 无 traceback 静默退出。cron 追踪 stale PID 导致 5× dead 判定。已派 Worker diagnose:phase2_scierc_grammar_only 深查。\"}}, \"notes\": \"进程从未崩溃。原 'crash' 判定是 cron 追踪 stale PID 123425（已杀的 batch script）导致 5× dead 误报。实际进程 PID 126473 一直在 GPU 1 正常运行。nvidia-smi 确认: GPU 1 上 grammar_only(126473) + unconstrained(126948) 共享，各占 ~16.5GB，利用率 92%。\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_grammar_only.jsonl --device cuda:0 --batch_size 1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"126473\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_grammar_only.log\", \"note\": \"CUDA_VISIBLE_DEVICES=1 by submit_training_job. 进程从未崩溃 — 'crash' 是 cron 追踪 stale PID 123425 的误报。PID 126473 一直在跑。两个 Phase 2 实验共享 GPU 1（各 ~16.5GB），利用率 92%。\"}, \"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_grammar_only.jsonl\", \"conclusion\": \"success\"}, \"phase2_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:07.120Z\", \"updated_at\": \"2026-05-14T18:31:26.645Z\", \"hypothesis\": \"Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的代码路径和 prompt，确保 F1 对比公平。预期结果接近 Phase 0 (entity_f1=0.31, relation_f1=0.08)\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"126948\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_unconstrained.log\", \"submitted_at\": \"2026-05-13T22:20:28.660Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"CUDA_VISIBLE_DEVICES=1 injected by submit_training_job. Progress 353/551 at 23:10 UTC\", \"wall_clock_seconds\": 5186.0, \"gpu_hours\": 1.44}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:44:02.820Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:44:06.470330+00:00\"}]}, \"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_unconstrained.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_unconstrained.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:46:54.651Z\"}, \"phase2_docred_full_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T02:07:20.166Z\", \"updated_at\": \"2026-05-14T18:31:19.721Z\", \"hypothesis\": \"Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\", \"notes\": \"DR 18.46%→10.19% (↓44.8%). RV 29.66%→0.03% (↓99.9%), ET 8.18%→0% (↓100%). R-F1 7.74%→8.23% (+0.49pp), E-F1 58.15%→59.37% (+1.22pp). F1 method: all_set (OOV predictions included in denominator). 之前 recognized_set 方法 (R-F1=9.33%→8.17%, -1.16pp) 是错误的——它过滤了 unconstrained 的 5189 个 OOV predictions，人为抬高 precision。Grammar-only DR 上升(18.46→26.17%)是审稿必问点：grammar 强制 valid relation name 后 entity type 与新 relation 的 domain/range 不匹配加剧，恰好证明 semantic 层必要性。\", \"completed_at\": \"2026-05-14T02:55:47.271Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"修复后重启 (PID 157042, tmux: phase2_docred_full_s1, cuda:1)。根因: TypeConstraintProcessor._apply_type_mask 在 allowed_types 与 grammar-valid tokens 无交集时，把所有 grammar-valid tokens 设为 -inf，导致 argmax 选中 grammar-invalid token (logit=-1e10 > -inf)。修复: _apply_type_mask 增加安全检查，若无 semantically-allowed type 有非 grammar-masked logit，跳过 semantic masking 交由 grammar 控制。Dry-run 验证 doc 88(原崩溃点)+7 docs 全部通过。--resume 从 87 继续，当前 89/998。\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:29:08.943533+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"157042\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log\", \"fix_applied\": \"type_mask_processor.py: semantic mask safety check — skip semantic masking when allowed_types have no non-grammar-masked logits\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:29:07.765Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_full_s1.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:40:51.107Z\", \"updated_at\": \"2026-05-14T18:31:13.783Z\", \"hypothesis\": \"Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"172859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_semantic_only.log\", \"submitted_at\": \"2026-05-14T08:30:43.644Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21989.5, \"gpu_hours\": 6.11}, \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": \"172859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_semantic_only.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T14:13:58.319Z\"}, \"notes\": \"DocRED semantic-only（checker 修复后定稿数字）。ET 10.44% (修复前 18.44%, -8pp: strip 修 507 假阳性 + PERSON alias 修 1108 假阳性)。DR 13.84% (修复前 15.05%, -1.21pp: normalize 也修正了 DR pair 匹配)。CF 1.05% (修复前 2.29%)。残余 ET 2107 violations 是真实退化：WORK(823)/EVENT(743)/ETHNIC_GROUP(137) 等非标类型。F1 无变化。998 lines, 0 duplicates。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:13:59.612547+00:00\"}]}, \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_semantic_only.jsonl\", \"completed_at\": \"2026-05-14T14:37:13.158Z\"}, \"phase2_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:40:50.853Z\", \"updated_at\": \"2026-05-14T18:31:10.378Z\", \"hypothesis\": \"DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"170502\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_unconstrained.log\", \"submitted_at\": \"2026-05-14T07:40:49.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20601.7, \"gpu_hours\": 5.72}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": \"170502\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_unconstrained.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T13:10:49.905Z\"}, \"notes\": \"✅ Phase 2 重新分析完成。998 lines, 0 duplicates — 文件干净无残留。正确值: DR=18.5%, RV=29.7%, ET=8.2%, E-F1=58.15%, R-F1=7.74%。F1 method: all_set (Reviewer 2026-05-14 确认正确)。论文可 claim: constrained decoding 不损失 R-F1。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:10:51.383206+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_unconstrained.jsonl\", \"completed_at\": \"2026-05-14T13:24:10.838Z\"}, \"mvp_phase0_docred_schema_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:36:06.125Z\", \"updated_at\": \"2026-05-14T02:56:53.324Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred_schema.jsonl --device cuda:0 --constraints_path data/docred/ontology_constraints_docred.json --prompt_mode schema_informed --batch_size 4 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"Resume from killed mvp_phase0_docred_schema. Original ran ~3.5h before being killed by cleanup Worker.\"}, \"hypothesis\": \"Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\", \"notes\": \"归档：mvp_phase0_docred_schema 已完成全量 998/998 并有完整 metrics，此 r2 续跑实验不再需要。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T02:56:53.324Z\"}, \"phase2_s2_pilot50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:25:10.566Z\", \"updated_at\": \"2026-05-14T02:04:44.195Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --num_samples 50 --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 50, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_s2_pilot50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_s2_pilot50.log\", \"note\": \"S2 50-sample pilot run. D/R violation=0% verified. relation_f1=0.0 root cause under investigation by Worker analysis:s2_relation_f1_rootcause.\"}, \"hypothesis\": \"S2 两通道约束解码 50 样本 pilot — 验证 PositionDetector 修复后 D/R violation=0%，评估 relation_f1 质量\", \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}, \"completed_at\": \"2026-05-13T23:26:16.718Z\", \"notes\": \"S2 pilot 实际 relation_f1=0.1008（非此前误报的 0.0）。根因：原 F1=0 来自 10 样本 dryrun 的 violation_report，不是 pilot50 评估结果。S2 架构无问题，F1 与 unconstrained 持平。FP 分析: entity span 质量差是主因(52.6% head+tail 都不匹配 gold)。改进方向: few-shot entity prompt / 编号引用格式 / 阻止自引用。\"}, \"mvp_phase0_docred_schema\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:58:18.184Z\", \"updated_at\": \"2026-05-14T01:49:57.097Z\", \"hypothesis\": \"Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心\", \"spec\": {\"command\": \"python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred_schema.jsonl --device cuda:0 --constraints_path data/docred/ontology_constraints_docred.json --prompt_mode schema_informed --batch_size 4\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"116365\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_docred_schema.log\", \"submitted_at\": \"2026-05-13T20:13:18.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wall_clock_seconds\": 13513.6, \"gpu_hours\": 3.75}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:58:31.565Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:58:32.325Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:58:33.241310+00:00\"}]}, \"notes\": \"Resume 完成 998/998 docs. Schema-informed prompt 结果: ET=0.61% (baseline 7.5%, Δ-6.89%), RV=18.4% (baseline 28.9%, Δ-10.5%), DR=12.8% (baseline 18.7%, Δ-5.9%). 全维度显著改善。\", \"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}, \"checkpoint_path\": \"outputs/raw_outputs_docred_schema.jsonl\"}, \"mvp_phase0_violation_rate_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:05.075Z\", \"updated_at\": \"2026-05-13T21:46:35.193Z\", \"hypothesis\": \"DocRED 有 96 relation types，约束空间远大于 SciERC (7 types)，预期 unconstrained LLM 的 per-triple violation rate 显著高于 SciERC，验证违规率与约束空间复杂度正相关\", \"spec\": {\"command\": \"python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred.jsonl --device cuda:0 --batch_size 4 --resume\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"pid\": 113148, \"resumed_from_doc\": 265, \"batch_size\": 4, \"current_progress\": 281, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_docred.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate_docred.log\"}, \"metrics\": {\"total_docs\": 998, \"parsed_docs\": 962, \"json_parse_rate\": 0.964, \"total_entities\": 19099, \"total_triples\": 16540, \"entity_type_violation_rate\": 0.075, \"relation_vocabulary_violation_rate\": 0.289, \"domain_range_violation_rate\": 0.187, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.187, \"fuzzy_matches\": 126, \"top_dr_violations_by_rate\": {\"P35_head_of_state\": 1, \"P710_participant\": 0.919, \"P172_ethnic_group\": 0.875}, \"top_dr_violations_by_count\": {\"P31_instance_of\": {\"violations\": 322, \"total\": 533, \"rate\": 0.604}, \"P1001_applies_to_jurisdiction\": {\"violations\": 264, \"total\": 594, \"rate\": 0.444}, \"P1344_participant_in\": {\"violations\": 194, \"total\": 312, \"rate\": 0.622}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:46:35.193Z\"}, \"mvp_phase0_scierc_schema\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:58:17.259Z\", \"updated_at\": \"2026-05-13T20:58:13.410Z\", \"hypothesis\": \"Schema-informed prompt（显式给出 domain/range 约束）能否降低违规率？与 minimal prompt 对比，若违规率仍 >5% 则证明 prompt 级干预不足以替代 decoding-time enforcement\", \"spec\": {\"command\": \"python3 run_extraction.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --output_path outputs/raw_outputs_schema.jsonl --backend transformers --prompt_mode schema_informed --constraints_path ontology_constraints.json\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"110676\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_scierc_schema.log\", \"submitted_at\": \"2026-05-13T19:11:32.249Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_schema.jsonl\", \"wall_clock_seconds\": 3650.3, \"gpu_hours\": 1.01}, \"metrics\": {\"domain_range_violation_rate\": 0.0578, \"relation_vocabulary_violation_rate\": 0.003, \"entity_type_violation_rate\": 0, \"total_violation_rate\": 0.0253, \"go_nogo_metric\": 0.0578, \"total_triples\": 1661, \"vs_minimal_dr_reduction\": -0.624, \"per_relation\": {\"Used-for\": {\"rate\": \"TBD\"}, \"Feature-of\": {\"delta_pp\": -22.3}, \"Part-of\": {\"delta_pp\": -22.5}, \"Compare\": {\"delta_pp\": -14.8}, \"Evaluate-for\": {\"delta_pp\": 5.8}}, \"mcnemar_all_significant\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T20:12:22.502Z\"}, \"mvp_phase0_violation_rate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:35:38.680Z\", \"updated_at\": \"2026-05-13T19:13:34.510Z\", \"hypothesis\": \"Unconstrained LLM (Qwen3-8B) 在 SciERC zero-shot IE 任务上的本体类型约束违反率 >5%，证明解码时约束强制的必要性\", \"spec\": {\"command\": \"python3 run_extraction.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --output_path outputs/raw_outputs.jsonl --backend transformers\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"106528\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate.log\", \"submitted_at\": \"2026-05-13T18:05:45.748Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs.jsonl\", \"wall_clock_seconds\": 4068.8, \"gpu_hours\": 1.13}, \"metrics\": {\"total_triples\": 1724, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.1537, \"entity_f1\": 0.3101, \"relation_f1\": 0.0823, \"per_relation\": {\"Used-for\": {\"total\": 787, \"dr_violations\": 6, \"rate\": 0.0076}, \"Conjunction\": {\"total\": 32, \"dr_violations\": 0, \"rate\": 0}, \"Hyponym-of\": {\"total\": 124, \"dr_violations\": 18, \"rate\": 0.1452}, \"Evaluate-for\": {\"total\": 133, \"dr_violations\": 32, \"rate\": 0.2406}, \"Part-of\": {\"total\": 72, \"dr_violations\": 18, \"rate\": 0.25}, \"Feature-of\": {\"total\": 486, \"dr_violations\": 163, \"rate\": 0.3354}, \"Compare\": {\"total\": 66, \"dr_violations\": 28, \"rate\": 0.4242}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T19:13:34.510Z\"}}, \"count\": 164, \"total\": 164, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5331}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The registry is very large. Let me read the appendix files first, then query the registry for specific experiments. Let me start by reading all the appendix files that contain tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "662f6bc2-957a-4ab3-804b-ff838b012e28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 14_

Registry is large — I'll read the appendix files first, then query the registry for specific experiments. Let me read all the key appendix files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "0db94f74-066b-4c7a-8739-c35f9791fdb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01Rb7bAsLgXdQnReEtXzeho5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "b4345f6e-d321-4434-97e2-08074ec53c3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 16 · 2026-05-23T10:43:43.343Z_

<details><summary>↩ Tool result · `toolu_01Rb7bAsLgXdQnReEtXzeho5`</summary>

```text
1	% Appendix: Quantization Robustness (SF2 response)
2	% exp_ids: sf2_qwen_int4_scierc_s1, sf2_llama_int4_scierc_s1,
3	%          sf2_qwen_int4_docred_s1, sf2_llama_int4_docred_s1,
4	%          d065_qwen_greedy_4096_r2, d066_sweep_llama_docred_beam1_s1
5	
6	\section{Quantization Robustness}
7	\label{app:quantization}
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3.2pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}l rrr rrr@{}}
15	\toprule
16	& \multicolumn{3}{c}{\textbf{Qwen3-8B}} & \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} \\
17	\cmidrule(lr){2-4} \cmidrule(l){5-7}
18	& FP16 & INT4 & $\Delta$ & FP16 & INT4 & $\Delta$ \\
19	\midrule
20	\multicolumn{7}{@{}l}{\textit{SciERC (551 docs)}} \\[2pt]
21	DR\,(\%)\,$\downarrow$  & 0     & 0     & 0      & 0.09  & 0     & $-$0.09 \\
22	R-F1\,$\uparrow$ & 43.77 & 41.71 & $-$2.06 & 45.47 & 43.98 & $-$1.49 \\
23	E-F1\,$\uparrow$ & 67.05 & 67.05 & 0.00   & 67.76 & 67.54 & $-$0.22 \\
24	\addlinespace[4pt]
25	\multicolumn{7}{@{}l}{\textit{DocRED (200 docs)}} \\[2pt]
26	DR\,(\%)\,$\downarrow$  & 0     & 0     & 0      & 0     & 0     & 0 \\
27	R-F1\,$\uparrow$ & 40.79\textsuperscript{\dag} & 40.07 & $-$0.72 & 47.35 & 48.04 & $+$0.69 \\
28	E-F1\,$\uparrow$ & 81.87\textsuperscript{\dag} & 74.84 & $-$7.03\textsuperscript{\ddag} & 85.43 & 84.18 & $-$1.25 \\
29	PF\,(\%) & 8.5\textsuperscript{\dag}  & 18.5  & $+$10.0\textsuperscript{\ddag} & 2.0   & 2.5   & $+$0.5 \\
30	\bottomrule
31	\end{tabular}}
32	\caption{FP16 vs.\ INT4 (AWQ) quantization under LoRA + S1 on SciERC and DocRED. F1 $\times$ 100; PF = parse-failure rate.
33	\textsuperscript{\dag}Qwen DocRED FP16 evaluated on 998 docs (all other configurations use matched subsets).
34	\textsuperscript{\ddag}E-F1 drop primarily attributable to increased parse failures under INT4 quantization on long documents rather than constraint interference (DR remains 0\%).}
35	\label{tab:quantization}
36	\end{table}
37	
38	INT4 (AWQ) quantization preserves constraint enforcement across both datasets: DR remains at 0\% for all four model--dataset configurations under INT4, with the sole FP16 violation (Llama SciERC, 0.09\%) disappearing after quantization.
39	R-F1 changes range from $-$2.06 to $+$0.69\,pp, consistent with expected quantization quality costs independent of the constraint layers.
40	On DocRED, Qwen INT4 exhibits elevated parse failures (18.5\% vs.\ 8.5\% FP16) due to timeout on long documents under quantized inference; the resulting E-F1 gap ($-$7.03\,pp) reflects generation-length degradation rather than constraint-layer interference, as DR remains 0\%.
41	These results provide indirect evidence that the 70B AWQ INT4 results (\S\ref{sec:70b-results}) are not confounded by quantization artifacts in the constraint enforcement mechanism.
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "6a7c19d7-2cc8-48ac-8bd0-a596a3821cfa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex",
      "content": "% Appendix: Quantization Robustness (SF2 response)\n% exp_ids: sf2_qwen_int4_scierc_s1, sf2_llama_int4_scierc_s1,\n%          sf2_qwen_int4_docred_s1, sf2_llama_int4_docred_s1,\n%          d065_qwen_greedy_4096_r2, d066_sweep_llama_docred_beam1_s1\n\n\\section{Quantization Robustness}\n\\label{app:quantization}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.2pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrr rrr@{}}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Qwen3-8B}} & \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(l){5-7}\n& FP16 & INT4 & $\\Delta$ & FP16 & INT4 & $\\Delta$ \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{SciERC (551 docs)}} \\\\[2pt]\nDR\\,(\\%)\\,$\\downarrow$  & 0     & 0     & 0      & 0.09  & 0     & $-$0.09 \\\\\nR-F1\\,$\\uparrow$ & 43.77 & 41.71 & $-$2.06 & 45.47 & 43.98 & $-$1.49 \\\\\nE-F1\\,$\\uparrow$ & 67.05 & 67.05 & 0.00   & 67.76 & 67.54 & $-$0.22 \\\\\n\\addlinespace[4pt]\n\\multicolumn{7}{@{}l}{\\textit{DocRED (200 docs)}} \\\\[2pt]\nDR\\,(\\%)\\,$\\downarrow$  & 0     & 0     & 0      & 0     & 0     & 0 \\\\\nR-F1\\,$\\uparrow$ & 40.79\\textsuperscript{\\dag} & 40.07 & $-$0.72 & 47.35 & 48.04 & $+$0.69 \\\\\nE-F1\\,$\\uparrow$ & 81.87\\textsuperscript{\\dag} & 74.84 & $-$7.03\\textsuperscript{\\ddag} & 85.43 & 84.18 & $-$1.25 \\\\\nPF\\,(\\%) & 8.5\\textsuperscript{\\dag}  & 18.5  & $+$10.0\\textsuperscript{\\ddag} & 2.0   & 2.5   & $+$0.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{FP16 vs.\\ INT4 (AWQ) quantization under LoRA + S1 on SciERC and DocRED. F1 $\\times$ 100; PF = parse-failure rate.\n\\textsuperscript{\\dag}Qwen DocRED FP16 evaluated on 998 docs (all other configurations use matched subsets).\n\\textsuperscript{\\ddag}E-F1 drop primarily attributable to increased parse failures under INT4 quantization on long documents rather than constraint interference (DR remains 0\\%).}\n\\label{tab:quantization}\n\\end{table}\n\nINT4 (AWQ) quantization preserves constraint enforcement across both datasets: DR remains at 0\\% for all four model--dataset configurations under INT4, with the sole FP16 violation (Llama SciERC, 0.09\\%) disappearing after quantization.\nR-F1 changes range from $-$2.06 to $+$0.69\\,pp, consistent with expected quantization quality costs independent of the constraint layers.\nOn DocRED, Qwen INT4 exhibits elevated parse failures (18.5\\% vs.\\ 8.5\\% FP16) due to timeout on long documents under quantized inference; the resulting E-F1 gap ($-$7.03\\,pp) reflects generation-length degradation rather than constraint-layer interference, as DR remains 0\\%.\nThese results provide indirect evidence that the 70B AWQ INT4 results (\\S\\ref{sec:70b-results}) are not confounded by quantization artifacts in the constraint enforcement mechanism.\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  }
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_015juG5vupDTvPVeWAPSU7D7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ae2db0a4-0c9b-4a5b-8361-ebe4c09bc079",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 18 · 2026-05-23T10:43:44.328Z_

<details><summary>↩ Tool result · `toolu_015juG5vupDTvPVeWAPSU7D7`</summary>

```text
1	% Appendix: 70B-Class LoRA Ablation on SciERC
2	% exp_ids: eval_70b_lora_scierc_unconstrained, eval_70b_lora_scierc_grammar_only,
3	%          eval_70b_lora_scierc_semantic_only, eval_70b_lora_scierc_s1_constrained,
4	%          eval_70b_lora_scierc_s2_constrained, eval_70b_lora_scierc_beam4_s1
5	
6	\paragraph{70B-class fine-tuned ablation.}
7	\label{app:70b-ablation}
8	
9	Table~\ref{tab:70b-ft-ablation} presents the constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on SciERC (551 documents).
10	
11	\begin{table}[h]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3.6pt}
15	\begin{tabular}{@{}l rrrr rr@{}}
16	\toprule
17	\textbf{Mode}
18	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
19	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
20	\midrule
21	Unconstrained & 1.50 & 0 & 0 & 0    & 44.73 & 64.86 \\
22	Grammar       & 1.50 & 0 & 0 & 0    & 44.63 & 64.82 \\
23	Semantic      & 0.60 & 0 & 0 & 9    & 44.73 & 64.86 \\
24	S1            & \textbf{0} & 0 & 0 & 15 & 44.53 & 64.76 \\
25	S2            & \textbf{0} & 0 & 0 & 18 & 36.28 & 62.35 \\
26	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{1} & \textbf{44.81} & \textbf{64.89} \\
27	\bottomrule
28	\end{tabular}
29	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on SciERC (551 docs).
30	CF: violation count. F1 $\times$100.}
31	\label{tab:70b-ft-ablation}
32	\end{table}
33	
34	The grammar layer provides no independent DR benefit at 70B (1.50\%\,$\to$\,1.50\% on SciERC; on DocRED zero-shot, DR actually increases $+$3.58\,pp due to RV$\to$DR conversion in the high-$\bar{\kappa}$ schema; Table~\ref{tab:70b-docred-zs-ablation}).
35	The semantic layer is the sole effective defense (1.50\%\,$\to$\,0.60\%, 60\% reduction) with no R-F1 cost ($\Delta{=}$0\,pp), and full S1 eliminates all DR.
36	S2 eliminates DR but causes severe R-F1 degradation ($-$8.45\,pp), indicating that optimal constraint granularity is scale-dependent: the additional S2 constraints become overly restrictive at 70B, where stronger baseline generation makes fine-grained intervention counterproductive.
37	Beam ($k{=}4$) S1 remains the optimal configuration (DR${=}$0\%, CF${=}$1, R-F1${=}$44.81).
38	Notably, S2 increases CF from 15 (S1) to 18 despite its cross-field consistency design, suggesting that over-constraining induces cascading generation degradation that creates new violations.
39	
40	% exp_ids: eval_70b_lora_docred_200_unconstrained, eval_70b_lora_docred_200_grammar_only,
41	%          eval_70b_lora_docred_200_semantic_only, eval_70b_lora_docred_200_s1_constrained,
42	%          eval_70b_lora_docred_200_beam4_s1
43	\paragraph{70B-class DocRED results.}
44	\label{app:70b-docred}
45	
46	Table~\ref{tab:70b-docred-ablation} presents the six-way constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on DocRED (998 documents).
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\setlength{\tabcolsep}{3.6pt}
52	\begin{tabular}{@{}l rrrr rr@{}}
53	\toprule
54	\textbf{Mode}
55	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
56	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
57	\midrule
58	Unconstrained & 0.22 & 0.57 & 0 & 2      & 43.80 & 80.34 \\
59	Grammar       & 0.38 & 0    & 0 & 0.06\%$^\dagger$ & 43.96 & 80.13 \\
60	Semantic      & \textbf{0} & 0.51 & 0 & 0.21\%$^\dagger$ & 43.61 & 80.06 \\
61	S1            & \textbf{0} & 0 & 0 & 0.18\%$^\dagger$ & 43.95 & 79.38 \\
62	S2            & \textbf{0} & 0 & 0 & 0.34\%$^\dagger$ & 36.45 & 84.96 \\
63	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{0} & \textbf{48.14} & \textbf{85.57} \\
64	\bottomrule
65	\end{tabular}
66	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on DocRED (998 docs).
67	CF: violation count except $^\dagger$reported as percentage (raw count unavailable).
68	F1 $\times$100.
69	PF: greedy S1 12.5\% (25/200 docs), S2 0\% (0/200), beam4 S1 0.5\% (1/200).}
70	\label{tab:70b-docred-ablation}
71	\end{table}
72	
73	The DocRED LoRA ablation mirrors the SciERC pattern: grammar eliminates RV (0.57\%\,$\to$\,0\%) but DR increases slightly ($+$0.16\,pp); semantic-only independently eliminates DR (0.22\%\,$\to$\,0\%) but retains RV (0.51\%).
74	The complementary layer interaction is stable across datasets under LoRA fine-tuning.
75	S2 eliminates DR and parse failures (PF${=}$0\%) but causes severe R-F1 degradation ($-$7.50\,pp vs.\ S1), mirroring the SciERC pattern ($-$8.45\,pp; Table~\ref{tab:70b-ft-ablation}): at 70B, the repair layer over-constrains relation predictions where baseline DR is already near-zero (0.22\%).
76	CF increases from 0.18\% (S1) to 0.34\% (S2), confirming that over-constraining induces cascading inconsistencies across datasets.
77	The $+$4.19\,pp R-F1 gain from beam search (43.95\,$\to$\,48.14) is largely attributable to parse failure recovery: greedy S1 fails to parse 12.5\% of documents (25/200), while beam reduces this to 0.5\% (1/200), recovering $\sim$24 documents that contribute no triples under greedy decoding.
78	The controlled comparison on SciERC---where both greedy and beam achieve 0\% parse failure---isolates the pure beam quality gain at $+$0.28\,pp, consistent with the 8B pattern (Appendix~\ref{app:beam-search}).
79	
80	% exp_ids: r16_70b_docred_zs_unconstrained, r16_70b_docred_zs_grammar_only,
81	%          r16_70b_docred_zs_semantic_only
82	\paragraph{70B-class DocRED zero-shot ablation.}
83	\label{app:70b-docred-zs}
84	
85	Table~\ref{tab:70b-docred-zs-ablation} presents the layer ablation on DocRED under zero-shot decoding at 70B.
86	
87	\begin{table}[h]
88	\centering
89	\small
90	\setlength{\tabcolsep}{3.6pt}
91	\begin{tabular}{@{}l rrrr rr@{}}
92	\toprule
93	\textbf{Mode}
94	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
95	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
96	\midrule
97	Unconstrained & 13.45 & 7.88 & 0 & 0    & 13.25 & 70.14 \\
98	Grammar       & 17.03 & 0    & 0 & 0    & 13.23 & 70.12 \\
99	Semantic      & 1.66  & 8.24 & 0.12 & 132  & 13.05 & 70.10 \\
100	S1            & \textbf{0} & 0 & 0 & 173  & 13.25 & 70.05 \\
101	\bottomrule
102	\end{tabular}
103	\caption{70B-class zero-shot layer ablation on DocRED.
104	CF: violation count. F1 $\times$100.}
105	\label{tab:70b-docred-zs-ablation}
106	\end{table}
107	
108	Grammar-only eliminates RV (7.88\%\,$\to$\,0\%) but DR increases by $+$3.58\,pp (13.45\%\,$\to$\,17.03\%): forced vocabulary mapping in DocRED's high-$\bar{\kappa}$ schema ($\bar{\kappa}{=}0.842$, ${\sim}$16\% type pairs valid) converts RV into DR violations.
109	Semantic-only independently achieves 87.7\% DR reduction (13.45\%\,$\to$\,1.66\%) with no R-F1 cost, confirming the pattern from SciERC (84\%; Table~\ref{tab:70b-ft-ablation}).
110	Full S1 eliminates all DR (13.45\%\,$\to$\,0\%) with zero R-F1 cost (13.25\,$=$\,13.25), confirming that the two layers compose correctly despite their opposing individual DR effects.
111	CF increases from 0 (unconstrained) to 173 (S1), consistent with the pattern that stricter constraint enforcement in ZS introduces more cross-field inconsistencies.
112	The two layers serve complementary roles: grammar provides the RV elimination foundation that semantic-layer DR enforcement requires, while the semantic layer addresses the DR that grammar alone cannot---and in high-$\bar{\kappa}$ schemas, exacerbates.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "5f881b6f-900b-4e24-a154-9838189b7350",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex",
      "content": "% Appendix: 70B-Class LoRA Ablation on SciERC\n% exp_ids: eval_70b_lora_scierc_unconstrained, eval_70b_lora_scierc_grammar_only,\n%          eval_70b_lora_scierc_semantic_only, eval_70b_lora_scierc_s1_constrained,\n%          eval_70b_lora_scierc_s2_constrained, eval_70b_lora_scierc_beam4_s1\n\n\\paragraph{70B-class fine-tuned ablation.}\n\\label{app:70b-ablation}\n\nTable~\\ref{tab:70b-ft-ablation} presents the constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on SciERC (551 documents).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\begin{tabular}{@{}l rrrr rr@{}}\n\\toprule\n\\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$} \\\\\n\\midrule\nUnconstrained & 1.50 & 0 & 0 & 0    & 44.73 & 64.86 \\\\\nGrammar       & 1.50 & 0 & 0 & 0    & 44.63 & 64.82 \\\\\nSemantic      & 0.60 & 0 & 0 & 9    & 44.73 & 64.86 \\\\\nS1            & \\textbf{0} & 0 & 0 & 15 & 44.53 & 64.76 \\\\\nS2            & \\textbf{0} & 0 & 0 & 18 & 36.28 & 62.35 \\\\\nBeam4 S1      & \\textbf{0} & 0 & 0 & \\textbf{1} & \\textbf{44.81} & \\textbf{64.89} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on SciERC (551 docs).\nCF: violation count. F1 $\\times$100.}\n\\label{tab:70b-ft-ablation}\n\\end{table}\n\nThe grammar layer provides no independent DR benefit at 70B (1.50\\%\\,$\\to$\\,1.50\\% on SciERC; on DocRED zero-shot, DR actually increases $+$3.58\\,pp due to RV$\\to$DR conversion in the high-$\\bar{\\kappa}$ schema; Table~\\ref{tab:70b-docred-zs-ablation}).\nThe semantic layer is the sole effective defense (1.50\\%\\,$\\to$\\,0.60\\%, 60\\% reduction) with no R-F1 cost ($\\Delta{=}$0\\,pp), and full S1 eliminates all DR.\nS2 eliminates DR but causes severe R-F1 degradation ($-$8.45\\,pp), indicating that optimal constraint granularity is scale-dependent: the additional S2 constraints become overly restrictive at 70B, where stronger baseline generation makes fine-grained intervention counterproductive.\nBeam ($k{=}4$) S1 remains the optimal configuration (DR${=}$0\\%, CF${=}$1, R-F1${=}$44.81).\nNotably, S2 increases CF from 15 (S1) to 18 despite its cross-field consistency design, suggesting that over-constraining induces cascading generation degradation that creates new violations.\n\n% exp_ids: eval_70b_lora_docred_200_unconstrained, eval_70b_lora_docred_200_grammar_only,\n%          eval_70b_lora_docred_200_semantic_only, eval_70b_lora_docred_200_s1_constrained,\n%          eval_70b_lora_docred_200_beam4_s1\n\\paragraph{70B-class DocRED results.}\n\\label{app:70b-docred}\n\nTable~\\ref{tab:70b-docred-ablation} presents the six-way constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on DocRED (998 documents).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\begin{tabular}{@{}l rrrr rr@{}}\n\\toprule\n\\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$} \\\\\n\\midrule\nUnconstrained & 0.22 & 0.57 & 0 & 2      & 43.80 & 80.34 \\\\\nGrammar       & 0.38 & 0    & 0 & 0.06\\%$^\\dagger$ & 43.96 & 80.13 \\\\\nSemantic      & \\textbf{0} & 0.51 & 0 & 0.21\\%$^\\dagger$ & 43.61 & 80.06 \\\\\nS1            & \\textbf{0} & 0 & 0 & 0.18\\%$^\\dagger$ & 43.95 & 79.38 \\\\\nS2            & \\textbf{0} & 0 & 0 & 0.34\\%$^\\dagger$ & 36.45 & 84.96 \\\\\nBeam4 S1      & \\textbf{0} & 0 & 0 & \\textbf{0} & \\textbf{48.14} & \\textbf{85.57} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on DocRED (998 docs).\nCF: violation count except $^\\dagger$reported as percentage (raw count unavailable).\nF1 $\\times$100.\nPF: greedy S1 12.5\\% (25/200 docs), S2 0\\% (0/200), beam4 S1 0.5\\% (1/200).}\n\\label{tab:70b-docred-ablation}\n\\end{table}\n\nThe DocRED LoRA ablation mirrors the SciERC pattern: grammar eliminates RV (0.57\\%\\,$\\to$\\,0\\%) but DR increases slightly ($+$0.16\\,pp); semantic-only independently eliminates DR (0.22\\%\\,$\\to$\\,0\\%) but retains RV (0.51\\%).\nThe complementary layer interaction is stable across datasets under LoRA fine-tuning.\nS2 eliminates DR and parse failures (PF${=}$0\\%) but causes severe R-F1 degradation ($-$7.50\\,pp vs.\\ S1), mirroring the SciERC pattern ($-$8.45\\,pp; Table~\\ref{tab:70b-ft-ablation}): at 70B, the repair layer over-constrains relation predictions where baseline DR is already near-zero (0.22\\%).\nCF increases from 0.18\\% (S1) to 0.34\\% (S2), confirming that over-constraining induces cascading inconsistencies across datasets.\nThe $+$4.19\\,pp R-F1 gain from beam search (43.95\\,$\\to$\\,48.14) is largely attributable to parse failure recovery: greedy S1 fails to parse 12.5\\% of documents (25/200), while beam reduces this to 0.5\\% (1/200), recovering $\\sim$24 documents that contribute no triples under greedy decoding.\nThe controlled comparison on SciERC---where both greedy and beam achieve 0\\% parse failure---isolates the pure beam quality gain at $+$0.28\\,pp, consistent with the 8B pattern (Appendix~\\ref{app:beam-search}).\n\n% exp_ids: r16_70b_docred_zs_unconstrained, r16_70b_docred_zs_grammar_only,\n%          r16_70b_docred_zs_semantic_only\n\\paragraph{70B-class DocRED zero-shot ablation.}\n\\label{app:70b-docred-zs}\n\nTable~\\ref{tab:70b-docred-zs-ablation} presents the layer ablation on DocRED under zero-shot decoding at 70B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\begin{tabular}{@{}l rrrr rr@{}}\n\\toprule\n\\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$} \\\\\n\\midrule\nUnconstrained & 13.45 & 7.88 & 0 & 0    & 13.25 & 70.14 \\\\\nGrammar       & 17.03 & 0    & 0 & 0    & 13.23 & 70.12 \\\\\nSemantic      & 1.66  & 8.24 & 0.12 & 132  & 13.05 & 70.10 \\\\\nS1            & \\textbf{0} & 0 & 0 & 173  & 13.25 & 70.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{70B-class zero-shot layer ablation on DocRED.\nCF: violation count. F1 $\\times$100.}\n\\label{tab:70b-docred-zs-ablation}\n\\end{table}\n\nGrammar-only eliminates RV (7.88\\%\\,$\\to$\\,0\\%) but DR increases by $+$3.58\\,pp (13.45\\%\\,$\\to$\\,17.03\\%): forced vocabulary mapping in DocRED's high-$\\bar{\\kappa}$ schema ($\\bar{\\kappa}{=}0.842$, ${\\sim}$16\\% type pairs valid) converts RV into DR violations.\nSemantic-only independently achieves 87.7\\% DR reduction (13.45\\%\\,$\\to$\\,1.66\\%) with no R-F1 cost, confirming the pattern from SciERC (84\\%; Table~\\ref{tab:70b-ft-ablation}).\nFull S1 eliminates all DR (13.45\\%\\,$\\to$\\,0\\%) with zero R-F1 cost (13.25\\,$=$\\,13.25), confirming that the two layers compose correctly despite their opposing individual DR effects.\nCF increases from 0 (unconstrained) to 173 (S1), consistent with the pattern that stricter constraint enforcement in ZS introduces more cross-field inconsistencies.\nThe two layers serve complementary roles: grammar provides the RV elimination foundation that semantic-layer DR enforcement requires, while the semantic layer addresses the DR that grammar alone cannot---and in high-$\\bar{\\kappa}$ schemas, exacerbates.\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  }
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01AKgMU9xbmUACG83bqT5uyT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "7104e4ef-1004-41e4-b814-d546068acc5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 20 · 2026-05-23T10:43:44.777Z_

<details><summary>↩ Tool result · `toolu_01AKgMU9xbmUACG83bqT5uyT`</summary>

```text
1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under S1 constraints (zero-shot).
23	SciERC: 551 documents; DocRED: matched 50-document subsets (same documents for greedy and beam); full 998-doc DocRED results in Table~\ref{tab:beam-docred-998-zs}.
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcccccc@{}}
28	\toprule
29	\textbf{Model / Dataset} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
30	\midrule
31	\multirow{2}{*}{Qwen3-8B / SciERC (551)}
32	  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
33	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.53} & 32.00 & 8.56 \\
34	\midrule
35	\multirow{2}{*}{Qwen3-8B / DocRED (50)}
36	  & Greedy      & 0 & 0 & 8.69 & 2.08 & 59.08 & 8.33 \\
37	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.55} & 58.64 & 9.37 \\
38	\midrule
39	\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}
40	  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\
41	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.93} & 25.04 & 3.33 \\
42	\midrule
43	\multirow{2}{*}{Llama-3.1-8B / DocRED (50)}
44	  & Greedy      & 0 & 0 & 1.58 & 6.85 & 55.35 & 6.12 \\
45	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.94} & 55.62 & 9.47 \\
46	\midrule
47	\multirow{2}{*}{Mistral-7B / SciERC (551)}
48	  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\
49	  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \textbf{0.57} & 26.66 & 4.37 \\
50	\midrule
51	\multirow{2}{*}{Mistral-7B / DocRED (50)}
52	  & Greedy      & 0 & 0 & 28.37 & 0.34 & 51.60 & 4.19 \\
53	  & Beam ($k{=}4$) & 0 & 0 & \textbf{21.37} & \textbf{0.19} & 51.78 & 5.70 \\
54	\bottomrule
55	\end{tabular}}
56	\end{table}
57	
58	\paragraph{Discussion.}
59	For calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\% across all four model-dataset combinations (both SciERC with 6 entity types, 551 documents, and DocRED with 96 relation types, 50 documents), regardless of schema complexity.
60	On SciERC, beam search eliminates DR for both Qwen (0.93\%\,$\to$\,0\%) and Llama (0.08\%\,$\to$\,0\%), and substantially reduces CF (Qwen: 9.90\%\,$\to$\,0.53\%; Llama: 6.56\%\,$\to$\,0.93\%).
61	On DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69\%\,$\to$\,0\%) and Llama (1.58\%\,$\to$\,0\%), with CF reductions of 74\% and 86\% respectively.
62	Llama DocRED shows the largest R-F1 gain ($+$3.4\,pp), consistent with beam search recovering valid type assignments that greedy decoding missed due to constraint fallback.
63	The CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.
64	
65	Mistral-7B-v0.3 constitutes a boundary condition on both datasets.
66	On SciERC (6 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.
67	On DocRED (96 relation types), beam search reduces DR by 25\% relative (28.4\%\,$\to$\,21.4\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.
68	This contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \cap S(t) = \emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.
69	
70	\paragraph{Beam width ablation.}
71	Table~\ref{tab:beam-ablation} varies beam width $k \in \{1,2,4,8\}$ on Qwen3-8B / SciERC (551 documents) under S1 constraints.
72	
73	\begin{table}[h]
74	\centering
75	\small
76	\caption{Effect of beam width on constraint satisfaction and extraction quality (Qwen3-8B, SciERC, 551 documents, S1 constraints). $k{=}1$ corresponds to greedy decoding.}
77	\label{tab:beam-ablation}
78	\begin{tabular}{@{}rcccc@{}}
79	\toprule
80	$k$ & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
81	\midrule
82	1 (greedy) & 0.93 & 9.90 & 30.98 & 8.36 \\
83	2          & 0.35 & 4.12 & 31.54 & \textbf{8.75} \\
84	4          & \textbf{0}    & 0.53 & 32.00 & 8.56 \\
85	8          & \textbf{0}    & \textbf{0.08} & \textbf{32.18} & 8.39 \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	DR elimination at $k{\geq}4$ confirms that constraint-search failure is resolved with moderate exploration width.
91	CF continues to decrease with larger beam (0.08\% at $k{=}8$, only 2 residual violations), while entity extraction quality improves monotonically.
92	$k{=}4$ represents the optimal cost-effectiveness trade-off: it eliminates all DR violations at roughly half the compute cost of $k{=}8$.
93	
94	\paragraph{Beam width--latency Pareto analysis (LoRA).}
95	% exp_id: d066_beam_sweep
96	Figure~\ref{fig:beam-pareto} and Table~\ref{tab:beam-sweep} extend the beam width analysis to LoRA fine-tuning, where the constrained--unconstrained interaction shifts qualitatively: LoRA + S1 already achieves DR=0\% at $k{=}1$ (greedy), so beam search targets CF reduction rather than DR elimination (contrast: zero-shot requires $k{\geq}4$ for DR=0\%).
97	Among constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\%, 1.39$\times$ latency); $k{\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\times$).
98	
99	\begin{figure*}[ht]
100	\centering
101	\includegraphics[width=\textwidth]{figures/beam_pareto.pdf}
102	\caption{Beam width vs.\ R-F1 under LoRA fine-tuning. Left: SciERC (Qwen3-8B solid, Llama-3.1-8B dashed; 551 docs). Right: DocRED (Llama-3.1-8B, 200 docs). Bubble area $\propto$ total violation rate (DR+CF+RV); green rings mark zero-violation configurations. Star: Pareto-optimal ($k{=}2$).}
103	\label{fig:beam-pareto}
104	\end{figure*}
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Beam width sweep on SciERC (Qwen3-8B LoRA, 551 documents). \textsc{unc}: unconstrained; \textsc{con}: schema-constrained. Latency relative to $k{=}1$ unconstrained. Highlighted row: Pareto-optimal configuration.}
110	\label{tab:beam-sweep}
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}cl cccc cc@{}}
113	\toprule
114	$k$ & Mode & E-F1 & R-F1 & DR (\%) & CF (\%) & Latency (s) & Rel.\ Lat. \\
115	\midrule
116	\multirow{2}{*}{1}
117	 & \textsc{unc} & 66.88 & 42.95 & 2.11 & 0    & 2.494 & 1.00$\times$ \\
118	 & \textsc{con} & 66.88 & 42.95 & \textbf{0} & 0.50 & 2.932 & 1.18$\times$ \\
119	\midrule
120	\multirow{2}{*}{2}
121	 & \textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\times$ \\
122	 & \cellcolor{blue!8}\textsc{con} & \cellcolor{blue!8}67.71 & \cellcolor{blue!8}\textbf{44.60} & \cellcolor{blue!8}\textbf{0} & \cellcolor{blue!8}0.11 & \cellcolor{blue!8}3.463 & \cellcolor{blue!8}1.39$\times$ \\
123	\midrule
124	\multirow{2}{*}{4}
125	 & \textsc{unc} & 67.49 & 43.72 & 1.89 & 0    & 3.485 & 1.40$\times$ \\
126	 & \textsc{con} & 67.22 & 43.60 & \textbf{0} & 0    & 4.069 & 1.63$\times$ \\
127	\midrule
128	\multirow{2}{*}{8}
129	 & \textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\times$ \\
130	 & \textsc{con} & 66.36 & 43.65 & \textbf{0} & 0    & 5.058 & 2.03$\times$ \\
131	\bottomrule
132	\end{tabular}}
133	\end{table}
134	
135	\paragraph{Composability with fine-tuning.}
136	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with S1 constraints already achieves DR=0\% but retains CF=1.18\% (22 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
137	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=43.60; changes within $\pm$0.5\,pp).
138	Llama-3.1-8B (LoRA, SciERC) with S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.18; the zero-violation result thus generalizes across calibrated model families.
139	% exp_id: q1_llama_ft_beam_scierc
140	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
141	
142	The initial 50-document DocRED subset (Table~\ref{tab:beam-search}) was subsequently validated on the full 998-document set (Table~\ref{tab:beam-docred-998-zs}): both models achieve DR${=}$0\%, confirming subset representativeness.
143	Llama shows the larger improvement (CF 8.54\%\,$\to$\,1.00\%, 88\% reduction; R-F1 $+$2.6\,pp), consistent with beam search resolving constraint-search failures that greedy decoding cannot.
144	
145	\begin{table}[h]
146	\centering
147	\small
148	\caption{Zero-shot beam search ($k{=}4$) under S1 constraints on the full DocRED dev set (998 documents).
149	ET/RV/DR/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.}
150	\label{tab:beam-docred-998-zs}
151	\begin{tabular}{@{}lcccccc@{}}
152	\toprule
153	\textbf{Model} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
154	\midrule
155	Qwen3-8B  & 0 & 0 & \textbf{0} & 4.94 & 58.19 & 8.72 \\
156	Llama-3.1-8B & 0 & 0 & \textbf{0} & 1.00 & 57.81 & 8.83 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\bar{\kappa}$ regime.
162	Parse failure rates under LoRA beam-4 range from 1.3\% to 2.9\%, lower than the zero-shot rate.
163	
164	\begin{table}[h]
165	\centering
166	\small
167	\caption{LoRA greedy vs.\ beam search ($k{=}4$) on DocRED (998 dev documents) under S1 constraints.
168	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\%); PF = parse failure rate (\%); F1 $\times$ 100.}
169	\label{tab:beam-docred-lora}
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{@{}llccccccc@{}}
172	\toprule
173	\textbf{Model} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ & PF \\
174	\midrule
175	\multirow{2}{*}{Qwen3-8B}
176	  & Greedy con & 0 & 0 & 0 & 0.22 & 81.87 & 40.79 & 7.8 \\ % d065_qwen_greedy_4096_r2
177	  & Beam-4 con & 0 & \textbf{0} & \textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\
178	\midrule
179	\multirow{2}{*}{Llama-3.1-8B}
180	  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\ % d065: 4096 context
181	  & Beam-4 con & 0 & 0 & 0 & \textbf{0} & \textbf{85.23} & \textbf{47.17} & \textbf{1.3} \\
182	\bottomrule
183	\end{tabular}}
184	\end{table}
185	
186	Llama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\bar{\kappa}$ regime.
187	Qwen3-8B achieves DR=0\% with near-zero CF (0.01\%); R-F1 is preserved ($\pm$0.06\,pp).
188	Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
189	
190	\paragraph{Latency overhead.}
191	Table~\ref{tab:beam-latency} reports wall-clock latency for greedy and beam search ($k{=}4$) under LoRA fine-tuning.
192	
193	\begin{table}[h]
194	\centering
195	\small
196	\begin{tabular}{@{}lrr@{}}
197	\toprule
198	\textbf{Condition} & \textbf{s/doc} & \textbf{Overhead} \\
199	\midrule
200	Greedy unconstrained   & 2.612 & 1.00$\times$ \\
201	Greedy constrained (S1)& 2.873 & 1.10$\times$ \\
202	Beam-4 unconstrained   & 3.446 & 1.32$\times$ \\
203	Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
204	\bottomrule
205	\end{tabular}
206	\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}
207	\label{tab:beam-latency}
208	\end{table}
209	
210	Beam search itself adds 32\% latency (4 beams); constraint overhead increases from 10\% (greedy) to 17\% (beam) because each beam independently maintains grammar and semantic state.
211	Per-beam entity registry memory is $O(|\text{entities}|)$ per beam; at $k{=}8$ with typical document sizes, overhead is ${<}$1\,MB per beam, negligible relative to model memory.
212	The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
213	
214	We also explored a type-consensus constraint that forces identical entity types across all relations within a document.
215	However, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\leftrightarrow$DR trade-off.
216	With DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\% skip rate on 551 SciERC documents and 50 DocRED documents).
217	This confirms that beam search resolves the CF$\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.
218	
219	\paragraph{TCR reranking under beam search.}
220	TCR reranking with beam search ($k{=}4$) showed no effect on either Qwen3-8B or Llama-3.1-8B under LoRA (0/551 SciERC candidates changed): fine-tuned beam candidates are already type-consistent (TCR score${=}$1.0 for all candidates), confirming that beam search implicitly subsumes post-hoc type consensus under fine-tuning.
221	This further strengthens the beam search deployment recommendation: beam not only eliminates all four violation types but also renders post-hoc CF resolution unnecessary.
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "0b6159ec-b058-4590-b648-17a830f5c4f9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex",
      "content": "\\section{Beam Search Compatibility}\n\\label{app:beam-search}\n\nOntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.\nThe main experiments (\\S\\ref{sec:experiments}) use greedy decoding; Appendix~\\ref{app:sampling} validates nucleus sampling.\nHere we verify compatibility with beam search, completing coverage of the three standard decoding strategies.\n\n\\paragraph{Implementation challenges.}\nTwo stateful components require adaptation for beam search.\n(1)~The grammar layer (XGrammar) maintains an internal \\texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.\nOur solution instantiates a fresh \\texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).\n(2)~The semantic layer's \\texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.\nOur solution isolates state per beam by calling \\texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).\nBoth adaptations add ${\\sim}125$ lines total without modifying the existing greedy/sampling logic.\n\n\\paragraph{Results.}\nTable~\\ref{tab:beam-search} compares beam search ($k{=}4$, \\texttt{early\\_stopping=True}) against greedy decoding under S1 constraints across six model-dataset combinations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Beam search ($k{=}4$) vs.\\ greedy decoding under S1 constraints (zero-shot).\nSciERC: 551 documents; DocRED: matched 50-document subsets (same documents for greedy and beam); full 998-doc DocRED results in Table~\\ref{tab:beam-docred-998-zs}.\nET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\\%); F1 $\\times$ 100.}\n\\label{tab:beam-search}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\n\\textbf{Model / Dataset} & \\textbf{Decoding} & ET & RV & DR$\\,\\downarrow$ & CF$\\,\\downarrow$ & E-F1$\\,\\uparrow$ & R-F1$\\,\\uparrow$ \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B / SciERC (551)}\n  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\\\\n  & Beam ($k{=}4$) & 0 & 0 & \\textbf{0} & \\textbf{0.53} & 32.00 & 8.56 \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B / DocRED (50)}\n  & Greedy      & 0 & 0 & 8.69 & 2.08 & 59.08 & 8.33 \\\\\n  & Beam ($k{=}4$) & 0 & 0 & \\textbf{0} & \\textbf{0.55} & 58.64 & 9.37 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}\n  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\\\\n  & Beam ($k{=}4$) & 0 & 0 & \\textbf{0} & \\textbf{0.93} & 25.04 & 3.33 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B / DocRED (50)}\n  & Greedy      & 0 & 0 & 1.58 & 6.85 & 55.35 & 6.12 \\\\\n  & Beam ($k{=}4$) & 0 & 0 & \\textbf{0} & \\textbf{0.94} & 55.62 & 9.47 \\\\\n\\midrule\n\\multirow{2}{*}{Mistral-7B / SciERC (551)}\n  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\\\\n  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \\textbf{0.57} & 26.66 & 4.37 \\\\\n\\midrule\n\\multirow{2}{*}{Mistral-7B / DocRED (50)}\n  & Greedy      & 0 & 0 & 28.37 & 0.34 & 51.60 & 4.19 \\\\\n  & Beam ($k{=}4$) & 0 & 0 & \\textbf{21.37} & \\textbf{0.19} & 51.78 & 5.70 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Discussion.}\nFor calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\\% across all four model-dataset combinations (both SciERC with 6 entity types, 551 documents, and DocRED with 96 relation types, 50 documents), regardless of schema complexity.\nOn SciERC, beam search eliminates DR for both Qwen (0.93\\%\\,$\\to$\\,0\\%) and Llama (0.08\\%\\,$\\to$\\,0\\%), and substantially reduces CF (Qwen: 9.90\\%\\,$\\to$\\,0.53\\%; Llama: 6.56\\%\\,$\\to$\\,0.93\\%).\nOn DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69\\%\\,$\\to$\\,0\\%) and Llama (1.58\\%\\,$\\to$\\,0\\%), with CF reductions of 74\\% and 86\\% respectively.\nLlama DocRED shows the largest R-F1 gain ($+$3.4\\,pp), consistent with beam search recovering valid type assignments that greedy decoding missed due to constraint fallback.\nThe CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.\n\nMistral-7B-v0.3 constitutes a boundary condition on both datasets.\nOn SciERC (6 entity types), beam search does not reduce DR (13.4\\%\\,$\\to$\\,13.8\\%), though CF drops by 55\\% relative (1.27\\%\\,$\\to$\\,0.57\\%) and R-F1 improves by $+$0.7\\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.\nOn DocRED (96 relation types), beam search reduces DR by 25\\% relative (28.4\\%\\,$\\to$\\,21.4\\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.\nThis contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \\cap S(t) = \\emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.\n\n\\paragraph{Beam width ablation.}\nTable~\\ref{tab:beam-ablation} varies beam width $k \\in \\{1,2,4,8\\}$ on Qwen3-8B / SciERC (551 documents) under S1 constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of beam width on constraint satisfaction and extraction quality (Qwen3-8B, SciERC, 551 documents, S1 constraints). $k{=}1$ corresponds to greedy decoding.}\n\\label{tab:beam-ablation}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\n$k$ & DR$\\,\\downarrow$ & CF$\\,\\downarrow$ & E-F1$\\,\\uparrow$ & R-F1$\\,\\uparrow$ \\\\\n\\midrule\n1 (greedy) & 0.93 & 9.90 & 30.98 & 8.36 \\\\\n2          & 0.35 & 4.12 & 31.54 & \\textbf{8.75} \\\\\n4          & \\textbf{0}    & 0.53 & 32.00 & 8.56 \\\\\n8          & \\textbf{0}    & \\textbf{0.08} & \\textbf{32.18} & 8.39 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDR elimination at $k{\\geq}4$ confirms that constraint-search failure is resolved with moderate exploration width.\nCF continues to decrease with larger beam (0.08\\% at $k{=}8$, only 2 residual violations), while entity extraction quality improves monotonically.\n$k{=}4$ represents the optimal cost-effectiveness trade-off: it eliminates all DR violations at roughly half the compute cost of $k{=}8$.\n\n\\paragraph{Beam width--latency Pareto analysis (LoRA).}\n% exp_id: d066_beam_sweep\nFigure~\\ref{fig:beam-pareto} and Table~\\ref{tab:beam-sweep} extend the beam width analysis to LoRA fine-tuning, where the constrained--unconstrained interaction shifts qualitatively: LoRA + S1 already achieves DR=0\\% at $k{=}1$ (greedy), so beam search targets CF reduction rather than DR elimination (contrast: zero-shot requires $k{\\geq}4$ for DR=0\\%).\nAmong constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\\%, 1.39$\\times$ latency); $k{\\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\\times$).\n\n\\begin{figure*}[ht]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/beam_pareto.pdf}\n\\caption{Beam width vs.\\ R-F1 under LoRA fine-tuning. Left: SciERC (Qwen3-8B solid, Llama-3.1-8B dashed; 551 docs). Right: DocRED (Llama-3.1-8B, 200 docs). Bubble area $\\propto$ total violation rate (DR+CF+RV); green rings mark zero-violation configurations. Star: Pareto-optimal ($k{=}2$).}\n\\label{fig:beam-pareto}\n\\end{figure*}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Beam width sweep on SciERC (Qwen3-8B LoRA, 551 documents). \\textsc{unc}: unconstrained; \\textsc{con}: schema-constrained. Latency relative to $k{=}1$ unconstrained. Highlighted row: Pareto-optimal configuration.}\n\\label{tab:beam-sweep}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}cl cccc cc@{}}\n\\toprule\n$k$ & Mode & E-F1 & R-F1 & DR (\\%) & CF (\\%) & Latency (s) & Rel.\\ Lat. \\\\\n\\midrule\n\\multirow{2}{*}{1}\n & \\textsc{unc} & 66.88 & 42.95 & 2.11 & 0    & 2.494 & 1.00$\\times$ \\\\\n & \\textsc{con} & 66.88 & 42.95 & \\textbf{0} & 0.50 & 2.932 & 1.18$\\times$ \\\\\n\\midrule\n\\multirow{2}{*}{2}\n & \\textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\\times$ \\\\\n & \\cellcolor{blue!8}\\textsc{con} & \\cellcolor{blue!8}67.71 & \\cellcolor{blue!8}\\textbf{44.60} & \\cellcolor{blue!8}\\textbf{0} & \\cellcolor{blue!8}0.11 & \\cellcolor{blue!8}3.463 & \\cellcolor{blue!8}1.39$\\times$ \\\\\n\\midrule\n\\multirow{2}{*}{4}\n & \\textsc{unc} & 67.49 & 43.72 & 1.89 & 0    & 3.485 & 1.40$\\times$ \\\\\n & \\textsc{con} & 67.22 & 43.60 & \\textbf{0} & 0    & 4.069 & 1.63$\\times$ \\\\\n\\midrule\n\\multirow{2}{*}{8}\n & \\textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\\times$ \\\\\n & \\textsc{con} & 66.36 & 43.65 & \\textbf{0} & 0    & 5.058 & 2.03$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Composability with fine-tuning.}\nUnder greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with S1 constraints already achieves DR=0\\% but retains CF=1.18\\% (22 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.\nAdding beam search ($k{=}4$) eliminates all residual CF violations (1.18\\%\\,$\\to$\\,0\\%), yielding zero violations across all four metrics (ET=0\\%, RV=0\\%, DR=0\\%, CF=0\\%) while preserving extraction quality (E-F1=66.88, R-F1=43.60; changes within $\\pm$0.5\\,pp).\nLlama-3.1-8B (LoRA, SciERC) with S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\\%, RV=0\\%, DR=0\\%, CF=0\\%) with R-F1=46.18; the zero-violation result thus generalizes across calibrated model families.\n% exp_id: q1_llama_ft_beam_scierc\nThe three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.\n\nThe initial 50-document DocRED subset (Table~\\ref{tab:beam-search}) was subsequently validated on the full 998-document set (Table~\\ref{tab:beam-docred-998-zs}): both models achieve DR${=}$0\\%, confirming subset representativeness.\nLlama shows the larger improvement (CF 8.54\\%\\,$\\to$\\,1.00\\%, 88\\% reduction; R-F1 $+$2.6\\,pp), consistent with beam search resolving constraint-search failures that greedy decoding cannot.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Zero-shot beam search ($k{=}4$) under S1 constraints on the full DocRED dev set (998 documents).\nET/RV/DR/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.}\n\\label{tab:beam-docred-998-zs}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Model} & ET & RV & DR$\\,\\downarrow$ & CF$\\,\\downarrow$ & E-F1$\\,\\uparrow$ & R-F1$\\,\\uparrow$ \\\\\n\\midrule\nQwen3-8B  & 0 & 0 & \\textbf{0} & 4.94 & 58.19 & 8.72 \\\\\nLlama-3.1-8B & 0 & 0 & \\textbf{0} & 1.00 & 57.81 & 8.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\\bar{\\kappa}$ regime.\nParse failure rates under LoRA beam-4 range from 1.3\\% to 2.9\\%, lower than the zero-shot rate.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LoRA greedy vs.\\ beam search ($k{=}4$) on DocRED (998 dev documents) under S1 constraints.\nET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\\%); PF = parse failure rate (\\%); F1 $\\times$ 100.}\n\\label{tab:beam-docred-lora}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Decoding} & ET & RV & DR$\\,\\downarrow$ & CF$\\,\\downarrow$ & E-F1$\\,\\uparrow$ & R-F1$\\,\\uparrow$ & PF \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}\n  & Greedy con & 0 & 0 & 0 & 0.22 & 81.87 & 40.79 & 7.8 \\\\ % d065_qwen_greedy_4096_r2\n  & Beam-4 con & 0 & \\textbf{0} & \\textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n  & Greedy con & 0 & 0 & 0 & 0.26 & 84.71 & 44.70 & 2.6 \\\\ % d065: 4096 context\n  & Beam-4 con & 0 & 0 & 0 & \\textbf{0} & \\textbf{85.23} & \\textbf{47.17} & \\textbf{1.3} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLlama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\\bar{\\kappa}$ regime.\nQwen3-8B achieves DR=0\\% with near-zero CF (0.01\\%); R-F1 is preserved ($\\pm$0.06\\,pp).\nCombined with the sampling robustness results (Appendix~\\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.\n\n\\paragraph{Latency overhead.}\nTable~\\ref{tab:beam-latency} reports wall-clock latency for greedy and beam search ($k{=}4$) under LoRA fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{s/doc} & \\textbf{Overhead} \\\\\n\\midrule\nGreedy unconstrained   & 2.612 & 1.00$\\times$ \\\\\nGreedy constrained (S1)& 2.873 & 1.10$\\times$ \\\\\nBeam-4 unconstrained   & 3.446 & 1.32$\\times$ \\\\\nBeam-4 constrained (S1)& 4.013 & 1.54$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}\n\\label{tab:beam-latency}\n\\end{table}\n\nBeam search itself adds 32\\% latency (4 beams); constraint overhead increases from 10\\% (greedy) to 17\\% (beam) because each beam independently maintains grammar and semantic state.\nPer-beam entity registry memory is $O(|\\text{entities}|)$ per beam; at $k{=}8$ with typical document sizes, overhead is ${<}$1\\,MB per beam, negligible relative to model memory.\nThe total 1.54$\\times$ overhead is acceptable for offline batch IE; \\texttt{early\\_stopping} limits additional compute to partial-sequence exploration.\n\nWe also explored a type-consensus constraint that forces identical entity types across all relations within a document.\nHowever, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\\leftrightarrow$DR trade-off.\nWith DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\\% skip rate on 551 SciERC documents and 50 DocRED documents).\nThis confirms that beam search resolves the CF$\\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.\n\n\\paragraph{TCR reranking under beam search.}\nTCR reranking with beam search ($k{=}4$) showed no effect on either Qwen3-8B or Llama-3.1-8B under LoRA (0/551 SciERC candidates changed): fine-tuned beam candidates are already type-consistent (TCR score${=}$1.0 for all candidates), confirming that beam search implicitly subsumes post-hoc type consensus under fine-tuning.\nThis further strengthens the beam search deployment recommendation: beam not only eliminates all four violation types but also renders post-hoc CF resolution unnecessary.\n",
      "numLines": 222,
      "startLine": 1,
      "totalLines": 222
    }
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01N2gLQe7hXThqRcRuu3WDJm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ac2c9775-c2eb-40af-a45b-14c2acc9f2fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 22 · 2026-05-23T10:43:45.497Z_

<details><summary>↩ Tool result · `toolu_01N2gLQe7hXThqRcRuu3WDJm`</summary>

```text
1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations.
28	The token-level fallback rate (36.6\% on SciERC Llama) is inflated by continuation tokens of multi-token type names (e.g., \textsc{OtherScientificTerm}, averaging 2.87 BPE tokens); at semantically meaningful first-token positions, the rate is 0.04--5.7\% (zero-shot) and drops to $\leq$\,0.11\% under fine-tuning.
29	These events account for the residual DR that persists after constraint enforcement.
30	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
31	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
32	
33	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
34	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
35	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
36	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
37	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
38	This metric directly quantifies the layer interaction (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
39	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
40	
41	%%% Fallback Causal Tracing %%%
42	% exp_ids: Task C causal tracing (Qwen/Llama × ZS/FT × S1)
43	
44	\paragraph{Fallback Causal Tracing.}
45	\label{app:causal-tracing}
46	
47	To establish that grammar-first fallback is the \emph{sole} mechanism producing residual DR violations, we instrument the constraint processor to log, for each violation, whether the semantic mask was active ($S(t) \cap G(t) \neq \emptyset$) or bypassed via fallback ($S(t) \cap G(t) = \emptyset$) at the type-bearing position.
48	Table~\ref{tab:causal-tracing} reports the results across four SciERC configurations.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\begin{tabular}{@{}ll rrr@{}}
54	\toprule
55	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
56	\midrule
57	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
58	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
59	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
60	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
61	\bottomrule
62	\end{tabular}
63	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
64	\label{tab:causal-tracing}
65	\end{table}
66	
67	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
68	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
69	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
70	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
71	
72	%%% Enabling Dependency: Confound Analysis %%%
73	
74	\paragraph{Enabling Dependency: Confound Analysis.}
75	\label{app:enabling-confound}
76	
77	The scale-dependent layer interaction (\S\ref{sec:method}) shows that the semantic layer achieves only 24\% DR reduction without the grammar layer (Table~\ref{tab:scierc-ablation}).
78	A potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.
79	Without grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.
80	We quantify this via the semantic-only ablation (Table~\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\% to 2.71\%, indicating that 2.63\,pp of additional violations trace to structural ambiguity.
81	However, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \in \mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.
82	The confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.
83	
84	%%% CF-DR Trade-off Analysis %%%
85	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
86	
87	\paragraph{CF-DR Trade-off Analysis.}
88	\label{app:cf-dr-tradeoff}
89	
90	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
91	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
92	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\begin{tabular}{@{}l rrrr@{}}
98	\toprule
99	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
100	\midrule
101	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
102	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
103	\midrule
104	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
105	\bottomrule
106	\end{tabular}
107	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
108	\label{tab:cf-dr-tradeoff}
109	\end{table}
110	
111	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
112	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
113	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
114	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
115	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
116	
117	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
118	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
119	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
120	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
121	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
122	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
123	
124	Two complementary paths can lower CF without re-routing it to DR.
125	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
126	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
127	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
128	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
129	
130	%%% Dual-Factor Quantitative Analysis %%%
131	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
132	%          llama_scierc_full_s1, llama_docred_full_s1
133	
134	\paragraph{Dual-Factor Quantitative Analysis.}
135	\label{app:dual-factor}
136	
137	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
138	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
139	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
140	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
141	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
142	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
143	
144	\begin{figure}[t]
145	\centering
146	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
147	\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations ($n{=}3$ schemas; descriptive only).
148	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$, $p{=}0.058$ ($n{=}4$, df${=}2$; not significant); Mistral deviates due to entity misclassification.}
149	\label{fig:dual-factor-scatter}
150	\end{figure}
151	
152	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
153	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
154	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
155	
156	\paragraph{Dataset-Dependent F1 Impact.}
157	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
158	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
159	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
160	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp); F1 gain magnitude is proportional to baseline OOV rate.
161	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
162	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
163	
164	%%% Bootstrap CIs and Effect Sizes %%%
165	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
166	
167	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
168	\label{app:bootstrap-effect-sizes}
169	
170	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
171	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
172	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
173	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\setlength{\tabcolsep}{3pt}
179	\begin{tabular}{@{}ll rrrr@{}}
180	\toprule
181	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
182	\midrule
183	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
184	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
185	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
186	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
187	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
188	\midrule
189	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
190	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
191	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
192	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
193	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
194	\bottomrule
195	\end{tabular}
196	\caption{Bootstrap CIs and Cohen's $d$ for Table~\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).
197	$d$: Cohen's $d$ from pooled bootstrap SD.
198	Top: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\alpha_{\text{adj}}{=}0.0125$); $|d| \leq 0.37$ (negligible--small).
199	Bottom: DR\% reduction; all $p_{\text{Bonf}} < 0.005$, $|d| \geq 3.0$ (large).}
200	\label{tab:bootstrap-effect-sizes}
201	\end{table}
202	
203	%%% Paragraph 1: Low F1 Practical Significance %%%
204	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
205	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
206	
207	\paragraph{Practical Significance of Zero-Shot F1.}
208	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
209	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
210	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
211	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
212	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
213	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
214	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
215	
216	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
217	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
218	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
219	
220	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
221	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
222	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
223	However, this precision gain comes at substantial cost.
224	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
225	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
226	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
227	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
228	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
229	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
230	
231	%%% CF Violation Distribution %%%
232	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
233	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
234	
235	\paragraph{Cross-Field Violation Distribution.}
236	\label{app:cf-distribution}
237	
238	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\geq$3 types).
239	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
240	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
241	
242	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
243	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{@{}lr r@{}}
249	\toprule
250	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
251	\midrule
252	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
253	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
254	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
255	Method $\leftrightarrow$ Task & 20 & 8.2 \\
256	Material $\leftrightarrow$ Method & 17 & 6.9 \\
257	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
258	\midrule
259	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
260	\midrule
261	\textbf{Total} & \textbf{245} & 100.0 \\
262	\bottomrule
263	\end{tabular}
264	\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).
265	All 245 unique entity-document pairs involve pairwise conflicts.
266	Conflicts involving \textsc{Generic} account for 63.3\%.}
267	\label{tab:cf-distribution}
268	\end{table}
269	
270	%%% Cascade Error Analysis %%%
271	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)
272	
273	\paragraph{Cascade Error Analysis.}
274	\label{app:cascade-analysis}
275	
276	Table~\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.
277	The dominant source is hallucinated entities (58.1\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.
278	True cascade errors---where first-seen type registration for a \emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\% (18/248).
279	Correct type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\times$ more frequent (18.1\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.
280	
281	Under fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.
282	This confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\begin{tabular}{@{}l rr@{}}
288	\toprule
289	\textbf{CF Source Category} & \textbf{Count} & \textbf{\%} \\
290	\midrule
291	Hallucinated entity & 144 & 58.1 \\
292	Correct type lock & 45 & 18.1 \\
293	True cascade error & 18 & 7.3 \\
294	Other / ambiguous & 41 & 16.5 \\
295	\midrule
296	\textbf{Total} & \textbf{248} & 100.0 \\
297	\bottomrule
298	\end{tabular}
299	\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\_id: phase2\_scierc\_full\_s1).
300	``Hallucinated entity'': generated entity absent from input.
301	``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.
302	``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.
303	Under fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\_id: w5\_lora\_scierc\_full\_s1\_eval).}
304	\label{tab:cascade-breakdown}
305	\end{table}
306	
307	%%% Per-Relation DR Elimination under Fine-Tuning %%%
308	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
309	
310	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
311	\label{app:lora-per-relation}
312	
313	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
314	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
315	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
316	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\begin{tabular}{@{}l r rr rr@{}}
322	\toprule
323	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
324	\cmidrule(lr){3-4} \cmidrule(l){5-6}
325	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
326	\midrule
327	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
328	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
329	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
330	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
331	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
332	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
333	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
334	\bottomrule
335	\end{tabular}
336	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
337	$\kappa$: constraint tightness; $n$: predicted triple count.
338	Used-for gains one triple from Evaluate-for redirection.}
339	\label{tab:lora-per-relation}
340	\end{table}
341	
342	%%% Fine-Tuned Four-Way Ablation %%%
343	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
344	
345	\paragraph{Fine-Tuned Four-Way Ablation.}
346	\label{app:ft-ablation}
347	
348	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
349	
350	\begin{table}[t]
351	\centering
352	\small
353	\setlength{\tabcolsep}{3pt}
354	\resizebox{\columnwidth}{!}{%
355	\begin{tabular}{@{}lll rrrrr rr@{}}
356	\toprule
357	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
358	\midrule
359	\multirow{8}{*}{SciERC}
360	  & \multirow{4}{*}{Qwen3-8B}
361	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
362	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
363	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
364	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
365	  \cmidrule(l){2-10}
366	  & \multirow{4}{*}{Llama-3.1-8B}
367	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
368	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
369	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
370	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
371	\midrule
372	\multirow{8}{*}{DocRED}
373	  & \multirow{4}{*}{Qwen3-8B}
374	    & Unconstrained & 0.56 & 0.27 & 0.00 & 0.08 & 7.11 & 82.35 & 40.89 \\
375	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
376	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
377	  & & S1       & \textbf{0.00} & 0.00 & 0.00 & 0.22 & 8.52 & 81.87 & 40.79 \\
378	  \cmidrule(l){2-10}
379	  & \multirow{4}{*}{Llama-3.1-8B}
380	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 84.77 & 44.55 \\
381	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
382	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
383	  & & S1       & \textbf{0.00} & 0.00 & 0.00 & 0.26 & 2.51 & 84.71 & 44.70 \\
384	\bottomrule
385	\end{tabular}}%
386	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
387	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
388	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
389	Semantic layer is the sole effective DR defense, providing 39--69\% reduction.
390	F1 cost is negligible: max $\Delta$R-F1 = $-$0.10\,pp (Qwen DocRED, full vs.\ unconstrained).}
391	\label{tab:ft-ablation}
392	\end{table}
393	
394	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
395	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--69\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$63\%, Llama $-$39\%).
396	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.09\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
397	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.10\,pp (Qwen DocRED).
398	
399	%%% DocRED Zero-Shot Ablation (moved from main text) %%%
400	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
401	%          phase2_docred_semantic_only, phase2_docred_full_s1
402	
403	\paragraph{DocRED Zero-Shot Ablation.}
404	\label{app:docred-zs-ablation}
405	
406	Table~\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\ref{tab:scierc-ablation}.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\setlength{\tabcolsep}{3.6pt}
412	\resizebox{\columnwidth}{!}{%
413	\begin{tabular}{@{}l rrrrrr rr@{}}
414	\toprule
415	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
416	& \multicolumn{2}{c}{\textbf{F1}} \\
417	\cmidrule(lr){2-7} \cmidrule(l){8-9}
418	\textbf{Mode}
419	  & DR\,$\downarrow$ & $\Delta$DR
420	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
421	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
422	\midrule
423	Unconstrained
424	  & 18.46 & ---
425	  & 29.66 & 2.48
426	  & 0.10  & 18.56
427	  & 7.74  & 58.15 \\
428	Grammar
429	  & 26.17 & $\uparrow$42\%
430	  & \textbf{0.03} & \textbf{0}
431	  & 0.07  & 26.24
432	  & \textbf{8.31}  & \textbf{59.38} \\
433	Semantic
434	  & 13.84 & $\downarrow$25\%
435	  & 29.87 & 4.22
436	  & 1.05  & 14.89
437	  & 7.70  & 57.81 \\
438	S1
439	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
440	  & \textbf{0.03} & \textbf{0}
441	  & 2.57  & \textbf{12.78}
442	  & 8.23  & 59.37 \\
443	\bottomrule
444	\end{tabular}}%
445	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
446	$\Delta$DR: relative change vs.\ unconstrained.
447	Tot.\ = DR + CF (total type-violation burden).
448	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
449	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
450	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \S\ref{sec:docred-results}).}
451	\label{tab:docred-ablation}
452	\end{table}
453	
454	%%% Residual DR Error Analysis (Fine-Tuned) %%%
455	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
456	
457	\paragraph{Residual DR Error Analysis.}
458	\label{app:residual-dr-analysis}
459	
460	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
461	Manual inspection reveals four root causes:
462	
463	\begin{enumerate}[nosep,leftmargin=*]
464	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
465	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
466	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
467	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
468	\end{enumerate}
469	
470	Two dataset-specific patterns emerge.
471	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
472	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
473	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.
474	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
475	
476	%%% Post-Hoc Filtering Comparison (Extended) %%%
477	% exp_ids: posthoc_*_zs, posthoc_*_ft
478	
479	\paragraph{Post-Hoc Filtering: Extended Comparison.}
480	\label{app:posthoc-extended}
481	
482	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
483	
484	\begin{table}[t]
485	\centering
486	\small
487	\setlength{\tabcolsep}{3pt}
488	\resizebox{\columnwidth}{!}{%
489	\begin{tabular}{@{}lll rrr l@{}}
490	\toprule
491	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
492	\midrule
493	\multirow{6}{*}{ZS}
494	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
495	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
496	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
497	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
498	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
499	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
500	\midrule
501	\multirow{4}{*}{FT}
502	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
503	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
504	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
505	  & Llama   & DocRED & 0.64 & 43.92 & 44.70 & cd \\
506	\bottomrule
507	\end{tabular}}%
508	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
509	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
510	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
511	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
512	F1 $\times$100.}
513	\label{tab:posthoc-extended}
514	\end{table}
515	
516	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
517	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
518	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
519	
520	%%% Zero-Shot Runtime Profiling %%%
521	
522	\paragraph{Zero-Shot Runtime Profiling.}
523	\label{app:runtime}
524	
525	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
526	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
527	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
528	
529	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
530	\paragraph{Fine-Tuned Latency Profiling.}
531	\label{app:ft-latency}
532	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
533	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
534	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
535	
536	%%% Fuzzy Relation Matching %%%
537	
538	\paragraph{Relation Matching Protocol.}
539	\label{app:fuzzy-matching}
540	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
541	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
542	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
543	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
544	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
545	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
546	
547	%%% Per-Relation Violation Landscape %%%
548	
549	\paragraph{Per-Relation Violation Landscape.}
550	\label{app:per-relation-landscape}
551	
552	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
553	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
554	
555	\begin{table}[t]
556	\centering
557	\small
558	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
559	\label{tab:prompt_comparison}
560	\resizebox{\columnwidth}{!}{%
561	\begin{tabular}{ll cccc}
562	\toprule
563	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
564	\midrule
565	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
566	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
567	\midrule
568	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
569	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
570	\bottomrule
571	\end{tabular}}
572	\end{table}
573	
574	\begin{figure}[t]
575	\centering
576	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
577	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
578	\label{fig:per_relation_dr}
579	\end{figure}
580	
581	%%% WikiEvents Extended %%%
582	
583	\paragraph{WikiEvents Dataset Details.}
584	\label{app:wikievents}
585	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
586	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
587	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
588	
589	\paragraph{Constraint Tightness in WikiEvents.}
590	\label{app:wikievents-kappa}
591	% Data source: artifacts/w1c_wikievents_kappa_results.md
592	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
593	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
594	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
595	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
596	
597	%%% Lucky Violation Analysis %%%
598	% exp_ids: task_e_lucky_violation_analysis
599	
600	\paragraph{Lucky Violation Analysis.}
601	\label{app:lucky-violations}
602	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
603	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
604	Across four fine-tuned configurations, lucky violations average 0.49\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
605	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
606	
607	\begin{table}[h]
608	\centering
609	\small
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{@{}llrrrr@{}}
612	\toprule
613	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
614	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
615	\midrule
616	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
617	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
618	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
619	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
620	\midrule
621	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.49\%} & $-$0.26 & 0.78 \\
622	\bottomrule
623	\end{tabular}}
624	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
625	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
626	$\Delta$Recall: recall change from unconstrained to constrained.
627	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
628	\label{tab:lucky-violations}
629	\end{table}
630	
631	%%% Trie-Only Baseline %%%
632	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
633	
634	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
635	\label{app:trie-baseline}
636	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
637	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
638	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
639	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
640	
641	\begin{table}[h]
642	\centering
643	\small
644	\resizebox{\columnwidth}{!}{%
645	\begin{tabular}{@{}ll rrrr rr@{}}
646	\toprule
647	\textbf{Model} & \textbf{Setting}
648	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
649	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
650	\midrule
651	\multirow{2}{*}{Qwen3-8B}
652	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
653	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
654	\multirow{2}{*}{Llama-8B}
655	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
656	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
657	\midrule
658	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
659	\midrule
660	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
661	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
662	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
663	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
664	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
665	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
666	\bottomrule
667	\end{tabular}}
668	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
669	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
670	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
671	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
672	$^\dagger$50.8\% parse failure rate.}
673	\label{tab:trie-baseline}
674	\end{table}
675	
676	%%% GCD/BoostCD Equivalence Comparison %%%
677	
678	\paragraph{Comparison with Grammar-Based Constrained Decoding.}
679	\label{app:gcd-comparison}
680	
681	Table~\ref{tab:gcd-comparison} summarizes the relationship between OntoCoDec's constraint layers and existing grammar-based constrained decoding methods.
682	
683	\begin{table}[h]
684	\centering
685	\small
686	\resizebox{\columnwidth}{!}{%
687	\begin{tabular}{@{}l l l l l l@{}}
688	\toprule
689	\textbf{Method} & \textbf{Constraint Type} & \textbf{Level} & \textbf{DR Red.} & \textbf{CF} & \textbf{State} \\
690	\midrule
691	GCD~\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\sim}$3\% & N/A & Stateless \\
692	BoostCD~\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\sim}$3\%$^\dagger$ & N/A & Stateless \\
693	Trie-Only (Tab.~\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\%$^\ddagger$ & N/A & Stateless \\
694	\midrule
695	vLLM \texttt{guided\_json}~\cite{kwon2023vllm} & JSON Schema & Grammar & ${\sim}$3\%$^\S$ & N/A & Stateless \\
696	\midrule
697	OntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\sim}$3\% & N/A & Stateless \\
698	OntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\% (FT) & ${\leq}$1.4\% (FT) & Entity reg. \\
699	\bottomrule
700	\end{tabular}}
701	\caption{Comparison with grammar-based constrained decoding methods.
702	$^\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.
703	$^\ddagger$Vocabulary-only constraints without JSON structure cause DR to \emph{increase} (15--96\%; Table~\ref{tab:trie-baseline}).
704	$^\S$Experimentally verified: DR${=}$15.26\% vs.\ grammar-only 14.84\% ($\Delta{<}$0.5\,pp; Table~\ref{tab:vllm-verification}).
705	Grammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \S\ref{sec:related_work}).}
706	\label{tab:gcd-comparison}
707	\end{table}
708	
709	Our grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\to$ pushdown automaton $\to$ per-step allowed token set).
710	Table~\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\to$0\% but only ${\sim}$3\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.
711	
712	% exp_id: vllm_guided_json_scierc_zs
713	\paragraph{External verification via vLLM.}
714	To confirm this equivalence experimentally, we evaluated vLLM's \texttt{guided\_json} mode~\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).
715	
716	\begin{table}[h]
717	\centering
718	\small
719	\begin{tabular}{@{}l rrrr r@{}}
720	\toprule
721	\textbf{Method} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{R-F1\,$\uparrow$} \\
722	\midrule
723	Grammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\
724	vLLM \texttt{guided\_json} & 15.26 & 0 & 0 & --- & 8.75 \\
725	\midrule
726	$\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\
727	\bottomrule
728	\end{tabular}
729	\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\ vLLM \texttt{guided\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\sim}$15\% DR violations unaddressed.}
730	\label{tab:vllm-verification}
731	\end{table}
732	
733	All metrics differ by $<$0.5\,pp (Table~\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\sim}$15\% DR gap.
734	The critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.
735	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "adbf0200-dfc1-41d6-a11c-129ea902df27",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
      "content": "% Appendix B — Extended Discussion\n% Contains discussion paragraphs moved from the main text during compression.\n\n\\section{Extended Discussion}\\label{app:discussion}\n\n%%% CF Dual Mechanism %%%\n% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{CF Dual Mechanism.}\nCF violations arise from two distinct mechanisms:\n(1)~\\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.\nThe entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.\n(2)~\\emph{Grammar-first fallback} (\\S\\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.\n\nThese mechanisms have sharply different model profiles.\nQwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\\% of its CF violations to registry override.\nLlama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.\nThis asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\\,=\\,2.57\\% on DocRED vs.\\ Llama's 12.02\\%, despite both using identical constraint configurations.\nThe difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.\n\n%%% Fallback Behavior and Effective Coverage %%%\n% exp_ids: cf_fallback_ablation_scierc (final data)\n\n\\paragraph{Fallback Behavior and Effective Coverage.}\n\\label{app:fallback-coverage}\nThe two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.\n\\emph{Grammar-first fallback} occurs when $S(t) \\cap G(t) = \\emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations.\nThe token-level fallback rate (36.6\\% on SciERC Llama) is inflated by continuation tokens of multi-token type names (e.g., \\textsc{OtherScientificTerm}, averaging 2.87 BPE tokens); at semantically meaningful first-token positions, the rate is 0.04--5.7\\% (zero-shot) and drops to $\\leq$\\,0.11\\% under fine-tuning.\nThese events account for the residual DR that persists after constraint enforcement.\n\\emph{Registry-consistent fallback} (4.5\\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.\nTogether, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.\n\nWe define \\emph{effective semantic constraint coverage} as $1 - f_{\\text{gf}}$, where $f_{\\text{gf}}$ is the grammar-first fallback rate.\nOn SciERC, Llama-3.1-8B shows $f_{\\text{gf}} = 36.6\\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\\% effective coverage.\nOn DocRED, by contrast, Qwen3-8B shows $f_{\\text{gf}} = 0.08\\%$ (46 of 54{,}859), yielding 99.9\\% coverage.\nThe large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \\textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.\nDocRED types (\\textsc{PER}, \\textsc{ORG}, \\textsc{LOC}, \\textsc{TIME}, \\textsc{NUM}, \\textsc{MISC}) are all single-token, eliminating this inflation.\nThis metric directly quantifies the layer interaction (\\S\\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.\nQwen3-8B, with zero grammar-first fallbacks, achieves 100\\% effective coverage on SciERC, consistent with its lower residual DR (0.93\\% vs.\\ Llama's 0.08\\%).\n\n%%% Fallback Causal Tracing %%%\n% exp_ids: Task C causal tracing (Qwen/Llama × ZS/FT × S1)\n\n\\paragraph{Fallback Causal Tracing.}\n\\label{app:causal-tracing}\n\nTo establish that grammar-first fallback is the \\emph{sole} mechanism producing residual DR violations, we instrument the constraint processor to log, for each violation, whether the semantic mask was active ($S(t) \\cap G(t) \\neq \\emptyset$) or bypassed via fallback ($S(t) \\cap G(t) = \\emptyset$) at the type-bearing position.\nTable~\\ref{tab:causal-tracing} reports the results across four SciERC configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}ll rrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Setting} & \\textbf{Fallback Rate} & \\textbf{DR} & \\textbf{From FB} \\\\\n\\midrule\nQwen3-8B  & FT S1 & 0/2256 (0\\%)    & 0  & N/A \\\\\nQwen3-8B  & ZS S1 & 16/3458 (0.46\\%) & 16 & 100\\% \\\\\nLlama-3.1-8B & FT S1 & 1/2162 (0.05\\%) & 1  & 100\\% \\\\\nLlama-3.1-8B & ZS S1 & 1/2630 (0.04\\%) & 1  & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \\cap G(t) = \\emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\\_type positions (range constraints are tighter than domain constraints).}\n\\label{tab:causal-tracing}\n\\end{table}\n\nWhen the semantic mask is active, $\\text{DR}_{\\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.\nAll 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.\nFine-tuning reduces fallback to near-zero ($\\leq$0.05\\%), effectively eliminating the sole source of residual violations.\nAll fallback events occur at tail\\_type positions, where $|\\operatorname{range}(r, \\tau^h)|$ is smaller than $|\\operatorname{dom}(r)|$, making the intersection $S(t) \\cap G(t)$ more likely to be empty.\n\n%%% Enabling Dependency: Confound Analysis %%%\n\n\\paragraph{Enabling Dependency: Confound Analysis.}\n\\label{app:enabling-confound}\n\nThe scale-dependent layer interaction (\\S\\ref{sec:method}) shows that the semantic layer achieves only 24\\% DR reduction without the grammar layer (Table~\\ref{tab:scierc-ablation}).\nA potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.\nWithout grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.\nWe quantify this via the semantic-only ablation (Table~\\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\\% to 2.71\\%, indicating that 2.63\\,pp of additional violations trace to structural ambiguity.\nHowever, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \\in \\mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.\nThe confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.\n\n%%% CF-DR Trade-off Analysis %%%\n% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)\n\n\\paragraph{CF-DR Trade-off Analysis.}\n\\label{app:cf-dr-tradeoff}\n\nCF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\\% on SciERC, up to 12.02\\% on Llama DocRED).\nWe treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.\nTable~\\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\\sigma(r)$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l rrrr@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{DR\\,(\\%)} & \\textbf{CF\\,(\\%)} & \\textbf{DR+CF} & \\textbf{$f_{\\text{gf}}$\\,(\\%)} \\\\\n\\midrule\nS1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\\\\nCF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\\\\n\\midrule\n$\\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \\texttt{w1\\_cf\\_fallback\\_scierc\\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\\,pp. $f_{\\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\\% for SciERC Qwen; \\S\\ref{sec:greedy-limitation}).}\n\\label{tab:cf-dr-tradeoff}\n\\end{table}\n\nThe CF fallback variant nearly eliminates CF (9.90\\%\\,$\\to$\\,0.04\\%, $-$9.86\\,pp) but at the cost of a 15.9$\\times$ increase in DR (0.93\\%\\,$\\to$\\,14.78\\%, $+$13.85\\,pp).\n% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664\nThis is not a net improvement: total violations (DR+CF) rise from 10.83\\% to 14.82\\% ($+$3.99\\,pp), so the change \\emph{re-routes} violations rather than reducing them.\nThe mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.\nThe token-level grammar-first fallback is triggered at 36.64\\% of type-bearing positions (0.46\\% at first-token positions; \\S\\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.\n\nWe interpret this as a fundamental tension in composable constraint systems with \\emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.\nWithin this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\\% DR at the cost of 9.90\\% CF.\nThe direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.\nThe pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\\%), making the trade-off most visible.\nWhile the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.\nThe CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\\% of CF violations on SciERC involve the catch-all \\textsc{Generic} type (Table~\\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.\n\nTwo complementary paths can lower CF without re-routing it to DR.\n(i)~\\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\\% relative to the zero-shot setting (9.90\\%\\,$\\to$\\,1.18\\%; Table~\\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.\n% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118\nThe remaining 1.18\\% still traces to \\textsc{Generic}$\\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.\n(ii)~\\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.\n\n%%% Dual-Factor Quantitative Analysis %%%\n% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,\n%          llama_scierc_full_s1, llama_docred_full_s1\n\n\\paragraph{Dual-Factor Quantitative Analysis.}\n\\label{app:dual-factor}\n\nFigure~\\ref{fig:dual-factor-scatter} plots residual DR against the product $\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$ for model$\\times$dataset configurations.\nFor \\emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \\approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.\nThe strong fit supports the dual-factor pattern from \\S\\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.\nMistral-7B (unconstrained ET${=}$7.58\\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.\nThis motivates a principled exclusion criterion: models with unconstrained ET${>}$5\\% on either dataset fall outside the regime where the tightness$\\times$RV product is the primary DR driver.\nThe two DocRED points (high $\\bar{\\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\\bar{\\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/dual_factor_scatter.pdf}\n\\caption{Residual DR vs.\\ Schema Restrictiveness $\\times$ Baseline Violation Rate ($\\bar{\\kappa} \\times \\text{RV}_{\\text{baseline}}$) across four model$\\times$dataset configurations ($n{=}3$ schemas; descriptive only).\nLinear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$, $p{=}0.058$ ($n{=}4$, df${=}2$; not significant); Mistral deviates due to entity misclassification.}\n\\label{fig:dual-factor-scatter}\n\\end{figure}\n\n%%% Dataset-Dependent F1 Impact (moved from §7) %%%\n% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),\n%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)\n\n\\paragraph{Dataset-Dependent F1 Impact.}\nThe divergence in F1 significance between DocRED ($+$0.50\\,pp, $p < 0.001$) and SciERC ($+$0.13\\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.\nDocRED's baseline RV of 29.66\\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.\nSciERC's baseline RV is only 1.39\\% (24 OOV predictions), too few to produce a detectable F1 effect.\nLlama-3.1-8B's lower baseline RV (16.03\\%) yields a smaller but directionally consistent improvement ($+$0.29\\,pp vs.\\ $+$0.50\\,pp); F1 gain magnitude is proportional to baseline OOV rate.\n% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained\n% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)\n\n%%% Bootstrap CIs and Effect Sizes %%%\n% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci\n\n\\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}\n\\label{app:bootstrap-effect-sizes}\n\nTable~\\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\\ref{tab:composability}).\nAfter Bonferroni correction for $k{=}4$ comparisons ($\\alpha_{\\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \\leq 0.37$; Cohen, 1988).\nPer-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.\nConstraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \\geq 3.0$, all $p_{\\text{Bonf}} < 0.005$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}ll rrrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & $\\Delta$\\textbf{(pp)} & \\textbf{95\\% CI} & $p$ & $d$ \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\\\\nQwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\\\\nQwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\\\\nLlama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\\\\nLlama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textbf{DR\\% reduction:}} \\\\\nQwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\\\\nQwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\\\\nLlama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\\\\nLlama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap CIs and Cohen's $d$ for Table~\\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).\n$d$: Cohen's $d$ from pooled bootstrap SD.\nTop: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\\alpha_{\\text{adj}}{=}0.0125$); $|d| \\leq 0.37$ (negligible--small).\nBottom: DR\\% reduction; all $p_{\\text{Bonf}} < 0.005$, $|d| \\geq 3.0$ (large).}\n\\label{tab:bootstrap-effect-sizes}\n\\end{table}\n\n%%% Paragraph 1: Low F1 Practical Significance %%%\n% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),\n%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)\n\n\\paragraph{Practical Significance of Zero-Shot F1.}\nOur reported relation F1 of approximately 8\\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.\nFor reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\\% relation F1 with full training data~\\citep{zhong2021frustratingly,ye2022packed}.\nConstraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.\nEven after LoRA fine-tuning, residual DR of 1--2\\% persists on tight-constraint relations (Table~\\ref{tab:composability}); constraints remain necessary at deployment-grade quality.\n% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval\nIn our evaluation, F1 serves as a \\emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.\nThe contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\\S\\ref{sec:composability}) validates practical deployment value.\n\n%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%\n% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),\n%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)\n\n\\paragraph{Decoding-Time vs.\\ Post-Hoc Enforcement.}\nPost-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\\ 8.36; DocRED 9.61 vs.\\ 8.23).\n% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23\nHowever, this precision gain comes at substantial cost.\nOn DocRED, post-hoc filtering discards 48.1\\% of all predicted triples, including 127 true positives (11.2\\% of correct predictions); recall drops from 9.46\\% to 8.40\\%.\n% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40\nEntity type violations remain unresolved (ET\\,=\\,2.47\\% vs.\\ OntoCoDec's 0\\%), as filtering targets only domain/range and vocabulary violations.\n% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%\nOntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.\nThe two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.\n\n%%% CF Violation Distribution %%%\n% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),\n%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)\n\n\\paragraph{Cross-Field Violation Distribution.}\n\\label{app:cf-distribution}\n\nTable~\\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\\geq$3 types).\nConflicts involving the \\textsc{Generic} type account for 63.3\\% (155/245) of all violations.\n\\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.\n\nThe pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \\textsc{Generic}$\\leftrightarrow$\\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\\%); on DocRED, the analogous catch-all type \\textsc{MISC} drives 76.6\\% of Qwen's CF violations.\nUnder unconstrained decoding, CF rates collapse to $\\leq$1\\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lr r@{}}\n\\toprule\n\\textbf{Conflicting Type Pair} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nGeneric $\\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\\\\nGeneric $\\leftrightarrow$ Material & 35 & 14.3 \\\\\nGeneric $\\leftrightarrow$ Metric & 30 & 12.2 \\\\\nMethod $\\leftrightarrow$ Task & 20 & 8.2 \\\\\nMaterial $\\leftrightarrow$ Method & 17 & 6.9 \\\\\nOtherScientificTerm $\\leftrightarrow$ Task & 12 & 4.9 \\\\\n\\midrule\n10 further pairs (each $\\leq$3.3\\%) & 46 & 18.8 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{245} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).\nAll 245 unique entity-document pairs involve pairwise conflicts.\nConflicts involving \\textsc{Generic} account for 63.3\\%.}\n\\label{tab:cf-distribution}\n\\end{table}\n\n%%% Cascade Error Analysis %%%\n% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)\n\n\\paragraph{Cascade Error Analysis.}\n\\label{app:cascade-analysis}\n\nTable~\\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.\nThe dominant source is hallucinated entities (58.1\\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.\nTrue cascade errors---where first-seen type registration for a \\emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\\% (18/248).\nCorrect type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\\times$ more frequent (18.1\\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.\n\nUnder fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.\nThis confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}l rr@{}}\n\\toprule\n\\textbf{CF Source Category} & \\textbf{Count} & \\textbf{\\%} \\\\\n\\midrule\nHallucinated entity & 144 & 58.1 \\\\\nCorrect type lock & 45 & 18.1 \\\\\nTrue cascade error & 18 & 7.3 \\\\\nOther / ambiguous & 41 & 16.5 \\\\\n\\midrule\n\\textbf{Total} & \\textbf{248} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\\_id: phase2\\_scierc\\_full\\_s1).\n``Hallucinated entity'': generated entity absent from input.\n``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.\n``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.\nUnder fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\\_id: w5\\_lora\\_scierc\\_full\\_s1\\_eval).}\n\\label{tab:cascade-breakdown}\n\\end{table}\n\n%%% Per-Relation DR Elimination under Fine-Tuning %%%\n% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1\n\n\\paragraph{Per-Relation DR Elimination under Fine-Tuning.}\n\\label{app:lora-per-relation}\n\nTable~\\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.\nFine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \\textsc{Evaluate-for} ($\\kappa{=}0.361$, 13.13\\%), \\textsc{Part-of} ($\\kappa{=}0.417$, 5.77\\%), and \\textsc{Compare} ($\\kappa{=}0.528$, 5.00\\%).\nAdding OntoCoDec constraints eliminates all remaining violations across all relations.\nOne \\textsc{Evaluate-for} triple (99\\,$\\to$\\,98) is redirected to \\textsc{Used-for} (634\\,$\\to$\\,635) by token-level masking: the head entity's registered type falls outside \\textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}l r rr rr@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{LoRA Unconstr.}} & \\multicolumn{2}{c}{\\textbf{LoRA + S1}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(l){5-6}\n\\textbf{Relation} & $\\kappa$ & DR\\,(\\%) & $n$ & DR\\,(\\%) & $n$ \\\\\n\\midrule\nEvaluate-for & 0.361 & 13.13 & 99 & \\textbf{0} & 98 \\\\\nPart-of      & 0.417 & 5.77  & 52 & \\textbf{0} & 52 \\\\\nCompare      & 0.528 & 5.00  & 40 & \\textbf{0} & 40 \\\\\nConjunction  & 0.306 & 1.31  & 153 & \\textbf{0} & 153 \\\\\nFeature-of   & 0.278 & 1.35  & 74 & \\textbf{0} & 74 \\\\\nUsed-for     & 0.028 & 0.16  & 634 & \\textbf{0} & 635 \\\\\nHyponym-of   & 0.417 & 0     & --- & \\textbf{0} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).\n$\\kappa$: constraint tightness; $n$: predicted triple count.\nUsed-for gains one triple from Evaluate-for redirection.}\n\\label{tab:lora-per-relation}\n\\end{table}\n\n%%% Fine-Tuned Four-Way Ablation %%%\n% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*\n\n\\paragraph{Fine-Tuned Four-Way Ablation.}\n\\label{app:ft-ablation}\n\nTable~\\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrrr rr@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{Mode} & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF} & \\textbf{PF} & \\textbf{E-F1\\,$\\uparrow$} & \\textbf{R-F1\\,$\\uparrow$} \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\\n  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\\\\n  & & S1       & \\textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\\\\n  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\\\\n  & & S1       & \\textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\\\\n\\midrule\n\\multirow{8}{*}{DocRED}\n  & \\multirow{4}{*}{Qwen3-8B}\n    & Unconstrained & 0.56 & 0.27 & 0.00 & 0.08 & 7.11 & 82.35 & 40.89 \\\\\n  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\\\\n  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\\\\n  & & S1       & \\textbf{0.00} & 0.00 & 0.00 & 0.22 & 8.52 & 81.87 & 40.79 \\\\\n  \\cmidrule(l){2-10}\n  & \\multirow{4}{*}{Llama-3.1-8B}\n    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 84.77 & 44.55 \\\\\n  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\\\\n  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\\\\n  & & S1       & \\textbf{0.00} & 0.00 & 0.00 & 0.26 & 2.51 & 84.71 & 44.70 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\\times$ 2 datasets).\nDR/RV/ET/CF: violation rates (\\%); PF: parse failure rate (\\%); F1 $\\times$100.\nGrammar layer is a no-op post-fine-tuning (DR change $<$0.2\\,pp in all 4 settings; RV and ET already 0\\% without constraints).\nSemantic layer is the sole effective DR defense, providing 39--69\\% reduction.\nF1 cost is negligible: max $\\Delta$R-F1 = $-$0.10\\,pp (Qwen DocRED, full vs.\\ unconstrained).}\n\\label{tab:ft-ablation}\n\\end{table}\n\nThe grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\\% without constraints, and grammar-only DR change is $<$0.2\\,pp (4/4 settings).\nThe semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--69\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$63\\%, Llama $-$39\\%).\nAdding both layers achieves near-complete elimination (DR\\,$\\leq$\\,0.09\\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.\nF1 cost is negligible: the maximum R-F1 decrease across S1 vs.\\ unconstrained is $-$0.10\\,pp (Qwen DocRED).\n\n%%% DocRED Zero-Shot Ablation (moved from main text) %%%\n% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,\n%          phase2_docred_semantic_only, phase2_docred_full_s1\n\n\\paragraph{DocRED Zero-Shot Ablation.}\n\\label{app:docred-zs-ablation}\n\nTable~\\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\\ref{tab:scierc-ablation}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 18.46 & ---\n  & 29.66 & 2.48\n  & 0.10  & 18.56\n  & 7.74  & 58.15 \\\\\nGrammar\n  & 26.17 & $\\uparrow$42\\%\n  & \\textbf{0.03} & \\textbf{0}\n  & 0.07  & 26.24\n  & \\textbf{8.31}  & \\textbf{59.38} \\\\\nSemantic\n  & 13.84 & $\\downarrow$25\\%\n  & 29.87 & 4.22\n  & 1.05  & 14.89\n  & 7.70  & 57.81 \\\\\nS1\n  & \\textbf{10.21} & $\\downarrow$\\textbf{45\\%}\n  & \\textbf{0.03} & \\textbf{0}\n  & 2.57  & \\textbf{12.78}\n  & 8.23  & 59.37 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained.\nTot.\\ = DR + CF (total type-violation burden).\nBest per column in \\textbf{bold} (CF excluded; Tot.\\ included).\nF1 $\\times$100. Bootstrap significance: R-F1 $+$0.50\\,pp ($p < 0.001$).\nGrammar-only $\\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \\S\\ref{sec:docred-results}).}\n\\label{tab:docred-ablation}\n\\end{table}\n\n%%% Residual DR Error Analysis (Fine-Tuned) %%%\n% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*\n\n\\paragraph{Residual DR Error Analysis.}\n\\label{app:residual-dr-analysis}\n\nAcross all fine-tuned settings (2 models $\\times$ 2 datasets $\\times$ S1), only 36 domain/range violations remain.\nManual inspection reveals four root causes:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\emph{Entity type errors} (39\\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \\textsc{LOC} when the gold standard requires \\textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.\n\\item \\emph{Schema coverage gaps} (33\\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.\n\\item \\emph{Incorrect relation selection} (17\\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.\n\\item \\emph{Direction reversal} (11\\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.\n\\end{enumerate}\n\nTwo dataset-specific patterns emerge.\nOutside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.\nOn DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\\%), with entity type errors as the dominant cause (14/33, 42\\%).\nThis asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.\nThe implication is twofold: (i)~the irreducible floor from schema gaps is small ($\\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.\n\n%%% Post-Hoc Filtering Comparison (Extended) %%%\n% exp_ids: posthoc_*_zs, posthoc_*_ft\n\n\\paragraph{Post-Hoc Filtering: Extended Comparison.}\n\\label{app:posthoc-extended}\n\nTable~\\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrr l@{}}\n\\toprule\n\\textbf{Setting} & \\textbf{Model} & \\textbf{Dataset} & \\textbf{Reject\\%} & \\textbf{R-F1$_{\\text{ph}}$} & \\textbf{R-F1$_{\\text{cd}}$} & \\textbf{Winner} \\\\\n\\midrule\n\\multirow{6}{*}{ZS}\n  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\\\\n  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\\\\n  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\\\\n  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\\\\n  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\\\\n  & Mistral & DocRED & \\textbf{73.7} & 3.85  & \\textbf{5.52} & cd \\\\\n\\midrule\n\\multirow{4}{*}{FT}\n  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\\n  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\\\\n  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\\\\n  & Llama   & DocRED & 0.64 & 43.92 & 44.70 & cd \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Post-hoc filtering (ph) vs.\\ constrained decoding (cd).\nIn zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.\nAt reject rate $>$70\\% (Mistral DocRED), post-hoc F1 collapses below constrained.\nUnder fine-tuning, rejection rates drop to 0.6--2.0\\% and the two strategies are equivalent ($\\Delta \\leq 0.55$\\,pp; each wins two groups).\nF1 $\\times$100.}\n\\label{tab:posthoc-extended}\n\\end{table}\n\nThe crossover point occurs when post-hoc rejection exceeds $\\sim$70\\%: Mistral DocRED rejects 73.7\\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\\,pp).\nOntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.\nUnder fine-tuning, both strategies converge because few violations remain to filter or constrain ($\\Delta \\leq 0.55$\\,pp across all four FT groups, with each strategy winning two).\n\n%%% Zero-Shot Runtime Profiling %%%\n\n\\paragraph{Zero-Shot Runtime Profiling.}\n\\label{app:runtime}\n\nOn SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\\,s/doc and S1 constrained decoding averages 4.710\\,s/doc ($+$13.1\\% overhead).\nOn DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.\nXGrammar automaton compilation takes 0.044\\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\\,s on SciERC (Table~\\ref{tab:scalability}), amortized to zero over the evaluation set.\n\n% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified\n\\paragraph{Fine-Tuned Latency Profiling.}\n\\label{app:ft-latency}\nUnder LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\\,s/doc and S1 constrained decoding averages 2.873\\,s/doc ($+$10.0\\% overhead, $n{=}551$).\nFine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\\,s vs.\\ 4.163\\,s/doc unconstrained); absolute generation time drops by 37\\%.\nThe relative overhead ($+$10.0\\%) is slightly lower than zero-shot ($+$13.1\\%), consistent with shorter sequences requiring fewer constraint checks per document.\n\n%%% Fuzzy Relation Matching %%%\n\n\\paragraph{Relation Matching Protocol.}\n\\label{app:fuzzy-matching}\nRelation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\\ spaces, abbreviations).\nA predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\\% \\emph{and} edit distance $\\leq 2$.\nThis protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\\_of\\_government'' for ``head of government'').\nOn Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\\,pp R-F1; strict R-F1\\,=\\,3.50\\% vs.\\ fuzzy 4.34\\%).\nFor Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).\nAll F1 figures in the main text use fuzzy normalization consistently across all models and conditions.\n\n%%% Per-Relation Violation Landscape %%%\n\n\\paragraph{Per-Relation Violation Landscape.}\n\\label{app:per-relation-landscape}\n\nTable~\\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.\nFigure~\\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Violation rates (\\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}\n\\label{tab:prompt_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll cccc}\n\\toprule\nDataset & Prompt & DR$\\downarrow$ & RV$\\downarrow$ & ET$\\downarrow$ & CF$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\\\\n & Schema-informed & 5.8 & 0.3 & \\textbf{0.0} & --- \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\\\\n & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_per_relation_dr.pdf}\n\\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\\ref{app:llama-per-relation}).}\n\\label{fig:per_relation_dr}\n\\end{figure}\n\n%%% WikiEvents Extended %%%\n\n\\paragraph{WikiEvents Dataset Details.}\n\\label{app:wikievents}\nWikiEvents~\\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.\nIt defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\\_type, role)$\\to$allowed\\_entity\\_types constraints.\nThe grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.\n\n\\paragraph{Constraint Tightness in WikiEvents.}\n\\label{app:wikievents-kappa}\n% Data source: artifacts/w1c_wikievents_kappa_results.md\nWikiEvents role-level tightness (with $|\\mathcal{E}|{=}27$) has mean $\\bar{\\kappa}{=}0.82$ and median 0.89; 84\\% of roles have $\\kappa \\geq 0.80$ (4 or fewer valid entity types out of 27).\nThe tightness-violation pattern extends to event extraction: roles with $\\kappa \\geq 0.90$ exhibit the highest AC rate (50\\%), compared to 21\\% for medium-tightness ($0.80 \\leq \\kappa < 0.90$) and 30\\% for loose ($\\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.\nHowever, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\\to$VEH) show 0\\% AC despite $\\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\\to$CRM, Sentence$\\to$SEN) show near-100\\% AC because LLMs default to common types (PER, ORG).\nThe loose group's elevated rate (30\\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\\% AC, $\\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.\n\n%%% Lucky Violation Analysis %%%\n% exp_ids: task_e_lucky_violation_analysis\n\n\\paragraph{Lucky Violation Analysis.}\n\\label{app:lucky-violations}\nTable~\\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.\nA ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.\nAcross four fine-tuned configurations, lucky violations average 0.49\\% of gold triples (range 0.01--0.51\\%), confirming that nearly all removed DR violations are false positives.\nOn Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{DR (\\%)} & \\textbf{Lucky} & \\textbf{$\\Delta$Recall} & \\textbf{Churn} \\\\\n& & \\textbf{unc$\\to$con} & \\textbf{(\\% gold)} & \\textbf{(pp)} & \\textbf{(\\%)} \\\\\n\\midrule\nQwen3-8B  & SciERC & 1.95$\\to$0    & 4 (0.41\\%) & $-$0.10 & 0.22 \\\\\nLlama-8B  & SciERC & 1.11$\\to$0.09 & 5 (0.51\\%) & $\\pm$0.00 & 0 \\\\\nQwen3-8B  & DocRED & 1.03$\\to$0.01 & 1 (0.01\\%) & $-$0.84 & 2.05 \\\\\nLlama-8B  & DocRED & 0.64$\\to$0.21 & 1 (0.01\\%) & $-$0.10 & 0.86 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Average}} & & \\textit{0.49\\%} & $-$0.26 & 0.78 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Lucky violation analysis across four LoRA fine-tuned configurations.\nLucky: count (and \\% of gold triples) of constraint-removed violations matching gold labels.\n$\\Delta$Recall: recall change from unconstrained to constrained.\nChurn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}\n\\label{tab:lucky-violations}\n\\end{table}\n\n%%% Trie-Only Baseline %%%\n% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc\n\n\\paragraph{Trie-Only Baseline (GCD-Equivalent).}\n\\label{app:trie-baseline}\nTable~\\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.\nThe trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\\%, RV${=}$0\\% across all configurations), functionally equivalent to GCD's~\\cite{geng2023gcd} constrained decoding.\nHowever, without grammar-level JSON enforcement, models systematically omit entity type fields (83\\% of triples) or produce malformed JSON (0--51\\% parse failure), causing DR to rise to 15--96\\%---far worse than unconstrained baselines.\nThe effect is most dramatic for Llama-8B LoRA: 50.8\\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rrrr rr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Setting}\n  & \\textbf{ET\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{PF\\,(\\%)} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}\n  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\\\\n  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\\\\n\\multirow{2}{*}{Llama-8B}\n  & LoRA  & 0 & 0 & 15.2$^\\dagger$  & 0    & 19.95 & 50.8 \\\\\n  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Comparison with OntoCoDec S1:}} \\\\\n\\midrule\n& & \\multicolumn{2}{c}{\\textbf{S1 DR\\,(\\%)}} & \\textbf{Trie DR\\,(\\%)} & \\multicolumn{2}{c}{\\textbf{DR Gap (pp)}} & \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-5} \\cmidrule(lr){6-7}\nQwen3-8B  & LoRA  & \\multicolumn{2}{c}{0}    & 95.5  & \\multicolumn{2}{c}{95.5}  & \\\\\nQwen3-8B  & ZS    & \\multicolumn{2}{c}{0.93} & 29.3  & \\multicolumn{2}{c}{28.4}  & \\\\\nLlama-8B  & LoRA  & \\multicolumn{2}{c}{0.09} & 15.2  & \\multicolumn{2}{c}{15.1}  & \\\\\nLlama-8B  & ZS    & \\multicolumn{2}{c}{0.08} & 84.4  & \\multicolumn{2}{c}{84.3}  & \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.\nTop: full trie-only metrics (ET/RV/DR/CF: violation rates \\%; R-F1 $\\times$100; PF: parse failure rate).\nTrie achieves ET${=}$0\\%, RV${=}$0\\% but DR rises to 15--96\\% because models omit type fields without structural enforcement.\nBottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.\n$^\\dagger$50.8\\% parse failure rate.}\n\\label{tab:trie-baseline}\n\\end{table}\n\n%%% GCD/BoostCD Equivalence Comparison %%%\n\n\\paragraph{Comparison with Grammar-Based Constrained Decoding.}\n\\label{app:gcd-comparison}\n\nTable~\\ref{tab:gcd-comparison} summarizes the relationship between OntoCoDec's constraint layers and existing grammar-based constrained decoding methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l l l l l l@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Constraint Type} & \\textbf{Level} & \\textbf{DR Red.} & \\textbf{CF} & \\textbf{State} \\\\\n\\midrule\nGCD~\\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\\sim}$3\\% & N/A & Stateless \\\\\nBoostCD~\\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\\sim}$3\\%$^\\dagger$ & N/A & Stateless \\\\\nTrie-Only (Tab.~\\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\\%$^\\ddagger$ & N/A & Stateless \\\\\n\\midrule\nvLLM \\texttt{guided\\_json}~\\cite{kwon2023vllm} & JSON Schema & Grammar & ${\\sim}$3\\%$^\\S$ & N/A & Stateless \\\\\n\\midrule\nOntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\\sim}$3\\% & N/A & Stateless \\\\\nOntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\\% (FT) & ${\\leq}$1.4\\% (FT) & Entity reg. \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Comparison with grammar-based constrained decoding methods.\n$^\\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.\n$^\\ddagger$Vocabulary-only constraints without JSON structure cause DR to \\emph{increase} (15--96\\%; Table~\\ref{tab:trie-baseline}).\n$^\\S$Experimentally verified: DR${=}$15.26\\% vs.\\ grammar-only 14.84\\% ($\\Delta{<}$0.5\\,pp; Table~\\ref{tab:vllm-verification}).\nGrammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \\S\\ref{sec:related_work}).}\n\\label{tab:gcd-comparison}\n\\end{table}\n\nOur grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\\to$ pushdown automaton $\\to$ per-step allowed token set).\nTable~\\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\\to$0\\% but only ${\\sim}$3\\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.\n\n% exp_id: vllm_guided_json_scierc_zs\n\\paragraph{External verification via vLLM.}\nTo confirm this equivalence experimentally, we evaluated vLLM's \\texttt{guided\\_json} mode~\\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}l rrrr r@{}}\n\\toprule\n\\textbf{Method} & \\textbf{DR\\,$\\downarrow$} & \\textbf{RV\\,$\\downarrow$} & \\textbf{ET\\,$\\downarrow$} & \\textbf{CF} & \\textbf{R-F1\\,$\\uparrow$} \\\\\n\\midrule\nGrammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\\\\nvLLM \\texttt{guided\\_json} & 15.26 & 0 & 0 & --- & 8.75 \\\\\n\\midrule\n$\\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\\ vLLM \\texttt{guided\\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\\sim}$15\\% DR violations unaddressed.}\n\\label{tab:vllm-verification}\n\\end{table}\n\nAll metrics differ by $<$0.5\\,pp (Table~\\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\\sim}$15\\% DR gap.\nThe critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.\n",
      "numLines": 735,
      "startLine": 1,
      "totalLines": 735
    }
  }
}
```

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01PiNj6wJAuBfQ48NRcS4Fnv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ce766863-901c-4ca9-a7cc-77c9221593ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 24 · 2026-05-23T10:43:46.193Z_

<details><summary>↩ Tool result · `toolu_01PiNj6wJAuBfQ48NRcS4Fnv`</summary>

```text
1	% Appendix: GoLLIE Comparison (D4 response)
2	% exp_ids: gollie_7b_scierc_zs_100, ontcodec_qwen_ft_s1_scierc_100, ontcodec_llama_ft_s1_scierc_100
3	
4	\section{GoLLIE Comparison}
5	\label{app:gollie-comparison}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\setlength{\tabcolsep}{3.2pt}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}l rrrr rr r@{}}
13	\toprule
14	\textbf{Method}
15	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
16	  & R-F1\,$\uparrow$ & E-F1\,$\uparrow$
17	  & \#Pred \\
18	\midrule
19	GoLLIE-7B (ZS)        & 0    & 0 & 0 & 0.83 & 0.0   & 9.17  & 5 \\
20	OntoCoDec Qwen (FT+S1)  & 0    & 0 & 0 & 0.61 & 43.69 & 66.43 & 1121 \\
21	OntoCoDec Llama (FT+S1) & 0    & 0 & 0 & 0.62 & 45.47 & 67.09 & 1070 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{GoLLIE-7B vs.\ OntoCoDec on SciERC (100 docs, zero-shot for GoLLIE, LoRA + S1 for OntoCoDec). F1 $\times$ 100.}
25	\label{tab:gollie-comparison}
26	\end{table}
27	
28	GoLLIE-7B achieves zero DR/RV/ET violations by generating only 5 predicted relations across 100 documents (54\% produce empty output), representing a trivial solution where formal correctness is achieved through near-complete abstention.
29	OntoCoDec achieves comparable violation rates (DR${=}$0\%, lower CF) while maintaining R-F1 43--45\% with ${\sim}$200$\times$ more predictions.
30	Code-style schema encoding thus trades coverage for formal correctness; OntoCoDec achieves both through decoding-time enforcement rather than training-time internalization.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "e8ff8292-eb1e-4dc3-9b67-67c5396b8e35",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex",
      "content": "% Appendix: GoLLIE Comparison (D4 response)\n% exp_ids: gollie_7b_scierc_zs_100, ontcodec_qwen_ft_s1_scierc_100, ontcodec_llama_ft_s1_scierc_100\n\n\\section{GoLLIE Comparison}\n\\label{app:gollie-comparison}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.2pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrr rr r@{}}\n\\toprule\n\\textbf{Method}\n  & DR\\,$\\downarrow$ & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF\n  & R-F1\\,$\\uparrow$ & E-F1\\,$\\uparrow$\n  & \\#Pred \\\\\n\\midrule\nGoLLIE-7B (ZS)        & 0    & 0 & 0 & 0.83 & 0.0   & 9.17  & 5 \\\\\nOntoCoDec Qwen (FT+S1)  & 0    & 0 & 0 & 0.61 & 43.69 & 66.43 & 1121 \\\\\nOntoCoDec Llama (FT+S1) & 0    & 0 & 0 & 0.62 & 45.47 & 67.09 & 1070 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{GoLLIE-7B vs.\\ OntoCoDec on SciERC (100 docs, zero-shot for GoLLIE, LoRA + S1 for OntoCoDec). F1 $\\times$ 100.}\n\\label{tab:gollie-comparison}\n\\end{table}\n\nGoLLIE-7B achieves zero DR/RV/ET violations by generating only 5 predicted relations across 100 documents (54\\% produce empty output), representing a trivial solution where formal correctness is achieved through near-complete abstention.\nOntoCoDec achieves comparable violation rates (DR${=}$0\\%, lower CF) while maintaining R-F1 43--45\\% with ${\\sim}$200$\\times$ more predictions.\nCode-style schema encoding thus trades coverage for formal correctness; OntoCoDec achieves both through decoding-time enforcement rather than training-time internalization.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01Pe82b1AWdSYV2cKePeDaLG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "1536bc8c-79ad-42fe-a6a3-9d09cd7b3be3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 26 · 2026-05-23T10:43:46.695Z_

<details><summary>↩ Tool result · `toolu_01Pe82b1AWdSYV2cKePeDaLG`</summary>

```text
1	% Appendix: WikiEvents Event Extraction Pilot (moved from §5 main text)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\section{WikiEvents Event Extraction Pilot}
8	\label{app:wikievents-pilot}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[h]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
43	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
44	  & S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{WikiEvents EE results (zero-shot, $n{=}246$ documents).
48	Violation rates over parsed documents.
49	\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
50	F1 (\%). $n{=}20$ test documents for fine-tuning; MDE${\approx}\pm$5.0\,pp; results are directional only.}
51	\label{tab:wikievents}
52	\end{table}
53	
54	\paragraph{Results.}
55	Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
56	S1 eliminates EV and RoV across all models, validating tokenizer-agnostic design across byte-level BPE and SentencePiece.
57	Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}).
58	Residual AC (1.3--3.8\%) traces to semantically similar types; CF rises to 15--21\% due to EE's multi-argument entity reuse.
59	Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.
60	
61	% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
62	\paragraph{Composability with fine-tuning (preliminary, $n{=}20$).}
63	On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
64	CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences (power analysis in Appendix~\ref{app:power-analysis-full}).
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "9601ca0a-724e-4ed8-a7c7-3186fb8e2ac6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex",
      "content": "% Appendix: WikiEvents Event Extraction Pilot (moved from §5 main text)\n% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,\n%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,\n%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2\n% v3 final data confirmed by Director 2026-05-18.\n\n\\section{WikiEvents Event Extraction Pilot}\n\\label{app:wikievents-pilot}\n\nWe apply OntoCoDec to event extraction (EE) on WikiEvents~\\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\\ref{app:wikievents}) without modification.\nViolations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).\n\n% ──────────────────────────────────────────\n%  Table: WikiEvents three-model comparison (v3 final)\n%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}\n% ──────────────────────────────────────────\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{2.8pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rrrr rr@{}}\n\\toprule\n& & \\multicolumn{4}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){3-6} \\cmidrule(l){7-8}\n\\textbf{Model} & \\textbf{Mode}\n  & EV\\,$\\downarrow$ & RoV\\,$\\downarrow$ & AC & CF\n  & Trig.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen3-8B}\n  & Unconstr.\\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\\\\n  & Grammar    & \\textbf{0} & 76.1 & 8.2 & --- & --- & --- \\\\\n  & S1    & \\textbf{0} & \\textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & Unconstr.\\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\\\\n  & Grammar    & \\textbf{0} & 77.0 & 8.8 & --- & --- & --- \\\\\n  & S1    & \\textbf{0} & \\textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral\\\\7B}}\n  & Unconstr.\\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\\\\n  & Grammar    & \\textbf{0} & 64.0 & 13.8 & --- & --- & --- \\\\\n  & S1    & \\textbf{0} & \\textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{WikiEvents EE results (zero-shot, $n{=}246$ documents).\nViolation rates over parsed documents.\n\\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).\nF1 (\\%). $n{=}20$ test documents for fine-tuning; MDE${\\approx}\\pm$5.0\\,pp; results are directional only.}\n\\label{tab:wikievents}\n\\end{table}\n\n\\paragraph{Results.}\nUnconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\\%; Table~\\ref{tab:wikievents}), with entity F1\\,=\\,0 because the parser cannot process off-schema output.\nS1 eliminates EV and RoV across all models, validating tokenizer-agnostic design across byte-level BPE and SentencePiece.\nGrammar-only eliminates EV but leaves RoV at 64--77\\% and surfaces latent AC (8--14\\%), consistent with DocRED's pattern (\\S\\ref{sec:docred-results}).\nResidual AC (1.3--3.8\\%) traces to semantically similar types; CF rises to 15--21\\% due to EE's multi-argument entity reuse.\nUnlike RE, EE shows measurable F1 gains: entity F1 0\\%\\,$\\to$\\,12--18\\%, trigger F1 $+$1.5--1.8\\,pp.\n\n% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5\n\\paragraph{Composability with fine-tuning (preliminary, $n{=}20$).}\nOn the full official test split (20 documents; 194/20/20~\\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\\%\\,$\\to$\\,0\\%, Llama 8.8\\%\\,$\\to$\\,0\\%) and reduces AC to $\\leq$0.8\\%, with argument F1 within $\\pm$1.1\\,pp; trigger F1 shifts ($-$5.4/$-$0.6\\,pp) have wide CIs consistent with n${=}$20.\nCF remains low (0.77--1.18\\%); per-document variance is high (Arg-F1 std/mean ${>}$\\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences (power analysis in Appendix~\\ref{app:power-analysis-full}).\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01NZT2U9TgCsp8zzymzadC7e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "37dc6226-fd66-4844-8601-0cca243cdb8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 28 · 2026-05-23T10:43:47.145Z_

<details><summary>↩ Tool result · `toolu_01NZT2U9TgCsp8zzymzadC7e`</summary>

```text
1	% Appendix: Zero-Shot Cross-Model and Cross-Dataset Details
2	% Moved from main text §5.2--§5.3 per reviewer guidance to focus main text on fine-tuned results.
3	
4	\section{Zero-Shot Cross-Model Validation}
5	\label{app:cross-model-zs}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\setlength{\tabcolsep}{3.4pt}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}ll rrrr r@{}}
13	\toprule
14	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
15	& \textbf{R-F1} \\
16	\cmidrule(lr){3-6} \cmidrule(l){7-7}
17	\textbf{Dataset} & \textbf{Model}
18	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
19	  & $\uparrow$ \\
20	\midrule
21	\multirow{6}{*}{SciERC}
22	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
23	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
24	  \cmidrule(l){2-7}
25	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
26	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
27	  \cmidrule(l){2-7}
28	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
29	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
30	\midrule
31	\multirow{6}{*}{DocRED}
32	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
33	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
34	  \cmidrule(l){2-7}
35	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
36	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
37	  \cmidrule(l){2-7}
38	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
39	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
40	\bottomrule
41	\end{tabular}}%
42	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
43	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
44	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
45	F1 $\times$100.}
46	\label{tab:cross-model}
47	\end{table}
48	
49	\paragraph{Cross-model results.}
50	RV and ET reach $\leq$0.03\% for all models on both datasets.
51	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
52	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%); fine-tuning resolves both (\S\ref{sec:composability}).
53	Post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates (Appendix~\ref{app:posthoc-extended}).
54	
55	\paragraph{Cross-dataset validation on DocRED.}
56	\label{sec:docred-results}
57	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
58	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.50\,pp ($p < 0.001$).
59	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
60	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the scale-dependent layer interaction.
61	Fine-tuning resolves residual DR entirely (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "25f81361-c0e5-436f-93b1-9318bfc00766",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex",
      "content": "% Appendix: Zero-Shot Cross-Model and Cross-Dataset Details\n% Moved from main text §5.2--§5.3 per reviewer guidance to focus main text on fine-tuned results.\n\n\\section{Zero-Shot Cross-Model Validation}\n\\label{app:cross-model-zs}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.4pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rrrr r@{}}\n\\toprule\n& & \\multicolumn{4}{c}{\\textbf{Violation Rates (\\%)}}\n& \\textbf{R-F1} \\\\\n\\cmidrule(lr){3-6} \\cmidrule(l){7-7}\n\\textbf{Dataset} & \\textbf{Model}\n  & DR\\,$\\downarrow$ & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF\n  & $\\uparrow$ \\\\\n\\midrule\n\\multirow{6}{*}{SciERC}\n  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\\\\n  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\\\\n  \\cmidrule(l){2-7}\n  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\\\\n  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\\\\n  \\cmidrule(l){2-7}\n  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\\dagger$ & 3.66 \\\\\n  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\\\\n\\midrule\n\\multirow{6}{*}{DocRED}\n  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\\\\n  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\\\\n  \\cmidrule(l){2-7}\n  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\\\\n  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\\\\n  \\cmidrule(l){2-7}\n  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\\\\n  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.\nParse failures: Llama DocRED 9.1\\%; others $\\leq$1.1\\%.\n$^\\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.\nF1 $\\times$100.}\n\\label{tab:cross-model}\n\\end{table}\n\n\\paragraph{Cross-model results.}\nRV and ET reach $\\leq$0.03\\% for all models on both datasets.\nDR drops 76--99\\% on SciERC and 42--90\\% on DocRED; R-F1 improves in 5/6 settings.\nCF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\\%) but reduces it for Mistral (56.87\\%\\,$\\to$\\,1.27\\%); fine-tuning resolves both (\\S\\ref{sec:composability}).\nPost-hoc filtering achieves DR${=}$0\\% but at 15--74\\% rejection rates (Appendix~\\ref{app:posthoc-extended}).\n\n\\paragraph{Cross-dataset validation on DocRED.}\n\\label{sec:docred-results}\nDocRED (96 relations, 14$\\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\\ref{tab:docred-ablation}).\nS1 reduces DR from 18.46\\% to 10.21\\% ($\\downarrow$45\\%), eliminates RV (29.66\\%\\,$\\to$\\,0.03\\%) and ET, with R-F1 $+$0.50\\,pp ($p < 0.001$).\nThe lower DR reduction (45\\% vs.\\ 94\\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\\S\\ref{sec:greedy-limitation}).\nGrammar-only \\emph{increases} DR (18.46\\%\\,$\\to$\\,26.17\\%) via \\textit{latent violation surfacing}: grammar forces OOV$\\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the scale-dependent layer interaction.\nFine-tuning resolves residual DR entirely (Table~\\ref{tab:composability}; residual decomposition in Appendix~\\ref{app:residual-dr-analysis}).\n",
      "numLines": 62,
      "startLine": 1,
      "totalLines": 62
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01RxhHNpDLrTForCp63spFwY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "a2487017-be72-4374-a283-0f27d1eace56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bVjp7U81pWfxaJe7264dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 24698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 30 · 2026-05-23T10:43:47.716Z_

<details><summary>↩ Tool result · `toolu_01RxhHNpDLrTForCp63spFwY`</summary>

```text
1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, demonstrating that constraint enforcement remains necessary even after full parameter updates. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "9549fe3b-75d0-4ca3-83a2-33fe94e3c9cf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex",
      "content": "\\section{Full Fine-Tuning Baseline}\n\\label{app:full-ft}\n\nTo verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\\times}10^{-4}$, seed 42).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\n& \\textbf{E-F1} & \\textbf{R-F1} & \\textbf{DR\\%} & \\textbf{CF\\%} \\\\\n\\midrule\nFull FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\\\\nFull FT + S1 & 64.78 & 37.89 & \\textbf{0} & 1.31 \\\\\n\\midrule\nLoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\\\\nLoRA + S1 & 67.05 & 43.77 & \\textbf{0} & 1.18 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Full fine-tuning vs.\\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}\n\\label{tab:full-ft}\n\\end{table}\n\nFull fine-tuning retains 2.74\\% DR violations (30 triples), concentrated in Part-of (14.6\\%), Hyponym-of (9.6\\%), and Evaluate-for (8.4\\%). S1 eliminates all 30 violations with no F1 cost, demonstrating that constraint enforcement remains necessary even after full parameter updates. The CF$\\leftrightarrow$DR trade-off persists (CF 0\\%$\\to$1.31\\%), consistent with the LoRA pattern (1.18\\%).\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---


### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
I've read all the major appendix files. Now I need to query the registry for specific experiments mentioned in these files. Let me also read the remaining appendix files that might contain tables. Let me first list all the experiments I need to verify and then query them systematically.

Let me organize what tables I need to verify:

1. **appendix_quantization.tex** — tab:quantization
   - exp_ids: sf2_qwen_int4_scierc_s1, sf2_llama_int4_scierc_s1, sf2_qwen_int4_docred_s1, sf2_llama_int4_docred_s1, d065_qwen_greedy_4096_r2, d066_sweep_llama_docred_beam1_s1


2. **appendix_70b_ablation.tex** — tab:70b-ft-ablation, tab:70b-docred-ablation, tab:70b-docred-zs-ablation
   - exp_ids: eval_70b_lora_scierc_*, eval_70b_lora_docred_200_*, r16_70b_docred_zs_*
3. **appendix_beam_search.tex** — tab:beam-search, tab:beam-ablation, tab:beam-sweep, tab:beam-docred-998-zs, tab:beam-docred-lora, tab:beam-latency
   - exp_ids: d066

, various beam experiments
4. **appendix_discussion.tex** — tab:causal-tracing, tab:cf-dr-tradeoff, tab:cf-distribution, tab:cascade-breakdown, tab:lora-per-relation, tab:ft-ablation, tab:docred-ablation, tab:lucky-violations, tab:trie-baseline, tab:gcd-comparison, tab:vllm-verification, tab:posthoc-extended, tab:bootstrap-effect-sizes, tab:prompt_comparison
5. **appendix_gollie_comparison.tex** — tab:gollie-comparison
   - exp_ids: gollie_7b_scierc_zs_100, ontcodec_qwen_ft_s1_scierc_100, ontcodec_llama_ft_s1_scierc_100
6. **appendix_wikievents_pilot.tex** — tab:wikievents
   - exp_ids: ee

Now I need to track down the remaining appendix files and their corresponding experiment IDs. I'm looking at cross-model comparisons across different model families, full fine-tuning results, and then checking a bunch of other appendix files for scalability, sampling, order invariance, and various analysis sections. The experiment registry is quite large, so I'll need to query it strategically for the specific experiments rather than trying to load everything at once.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ecf2e76b-cc87-4079-8480-b28f2b82d4c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 32_

Now let me read the remaining appendix files that might contain tables, and start querying the registry for specific experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3902848d-0a16-4a59-a54a-49a36ee19b9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

<details open><summary>🔧 Tool call — Read · `toolu_012a18tjBkCayGHk7gmX6Seq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "fdaa3062-2367-4221-a80f-fa0b403e52ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 34 · 2026-05-23T10:44:12.557Z_

<details><summary>↩ Tool result · `toolu_012a18tjBkCayGHk7gmX6Seq`</summary>

```text
1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Full constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\,s to 0.42\,s for 7$\to$1{,}000 relations; Table~\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\sim$0.044\,s and semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "aa53105f-86a5-473b-88b0-339ec16be0c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex",
      "content": "\\section{Ontology Scalability}\n\\label{app:scalability}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\n\\textbf{Scale} & \\textbf{Types} & \\textbf{Rels} & \\textbf{Compile (s)} & \\textbf{Overhead} \\\\\n\\midrule\nSmall (SciERC) & 6 & 7 & 0.33 & 1.02$\\times$ \\\\\nMedium (DocRED) & 6 & 96 & 0.32 & 1.03$\\times$ \\\\\nLarge (synth.) & 100 & 500 & 0.35 & 1.03$\\times$ \\\\\nXLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\\times$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}\n\\label{tab:scalability}\n\\end{table}\n\nFull constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\\,s to 0.42\\,s for 7$\\to$1{,}000 relations; Table~\\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\\sim$0.044\\,s and semantic constraint compilation grows linearly but remains negligible (0.4\\,ms to 17\\,ms).\nInference overhead is constant at 2--3\\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.\nThe practical limit is first-token uniqueness: when entity types exceed $\\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\\S\\ref{sec:dynamic-masking}).\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01D2LYkrPoQoS7CYUbFuh9Gp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "63701ddd-c9de-46b5-b40a-749ec8726a20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 36 · 2026-05-23T10:44:13.648Z_

<details><summary>↩ Tool result · `toolu_01D2LYkrPoQoS7CYUbFuh9Gp`</summary>

```text
1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, S1 constraints).}
6	\label{tab:sampling-robustness}
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{llcccccc}
9	\toprule
10	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
11	\midrule
12	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
13	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
14	\midrule
15	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
16	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
17	\bottomrule
18	\end{tabular}}
19	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "16519267-333f-4e3b-b658-7046c4c094e3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex",
      "content": "\\section{Sampling Robustness}\\label{app:sampling}\n\n\\begin{table}[h]\n\\centering\n\\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\\ greedy decoding (Qwen3-8B, S1 constraints).}\n\\label{tab:sampling-robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccccc}\n\\toprule\nDataset & Decoding & ET\\% & RV\\% & DR\\% & CF\\% & E-F1 & R-F1 \\\\\n\\midrule\n\\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\\\\n& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\\\\n\\midrule\n\\multirow{2}{*}{DocRED (114$^\\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\\\\n& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\\\\n\\bottomrule\n\\end{tabular}}\n\\par\\smallskip\\footnotesize $^\\dagger$Subset of 114 documents; full DocRED sampling requires ${\\sim}300$h due to extended generation under high-temperature sampling with complex schemas.\n\\end{table}\n",
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_013pkMwfNGezyWkGEm1vApFB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3cb018b0-91df-4b3c-8889-8cb8778d49e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 38 · 2026-05-23T10:44:13.976Z_

<details><summary>↩ Tool result · `toolu_013pkMwfNGezyWkGEm1vApFB`</summary>

```text
1	% Appendix: Order Invariance of Compiled Constraints
2	
3	\paragraph{Order invariance.}
4	\label{app:order-invariance}
5	To verify that OntoCoDec's outputs are independent of schema enumeration order, we randomly shuffle the entity and relation type lists in the compiled constraint file (\texttt{ontology\_constraints.json}) and re-run greedy S1 decoding on all 551 SciERC documents.
6	The raw model outputs and parsed triples are byte-identical to the canonical-order run across all documents.
7	This holds because the grammar layer accepts the same token set at each type-bearing position regardless of the order in which types are listed in the schema, and greedy decoding is deterministic given identical logit masks.
8	The result confirms that OntoCoDec introduces no spurious order dependence from schema compilation.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "cd63a77d-5551-4084-ae75-573508324367",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex",
      "content": "% Appendix: Order Invariance of Compiled Constraints\n\n\\paragraph{Order invariance.}\n\\label{app:order-invariance}\nTo verify that OntoCoDec's outputs are independent of schema enumeration order, we randomly shuffle the entity and relation type lists in the compiled constraint file (\\texttt{ontology\\_constraints.json}) and re-run greedy S1 decoding on all 551 SciERC documents.\nThe raw model outputs and parsed triples are byte-identical to the canonical-order run across all documents.\nThis holds because the grammar layer accepts the same token set at each type-bearing position regardless of the order in which types are listed in the schema, and greedy decoding is deterministic given identical logit masks.\nThe result confirms that OntoCoDec introduces no spurious order dependence from schema compilation.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01Ec5j8XVyt8Ta5SrT9JhXLA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "89f51d45-4a0c-4de8-96a8-5870b4f268b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 40 · 2026-05-23T10:44:14.444Z_

<details><summary>↩ Tool result · `toolu_01Ec5j8XVyt8Ta5SrT9JhXLA`</summary>

```text
1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, which indicates stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's residual DR on the same relations is markedly lower (P1198 reaches only 20.0\%) and no relation-level fallback concentration comparable to Qwen is observed.
37	% exp_ids: llama_docred_full_s1, qwen_docred_full_s1
38	The substantially lower residual DR for Llama (2.55\% vs.\ Qwen's 10.21\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "b756d27f-d870-4c91-b480-aac82e4dff23",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex",
      "content": "% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)\n% exp_ids: llama_docred_unconstrained, llama_docred_full_s1\n\n\\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\\label{app:llama-per-relation}\n\nTable~\\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under S1 constraints.\nThe Llama baseline exhibits an RV rate of 16.03\\%, substantially lower than Qwen's 29.66\\%, which indicates stronger baseline vocabulary compliance.\n% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)\nS1 completely eliminates RV violations and reduces the residual DR rate to 2.55\\% (418/16{,}368 triples), with only three relations exceeding 10\\%.\n% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)\n\n\\begin{table}[h]\n\\centering\n\\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under S1 constraints. Relations with $>$20 triples and 0\\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}\n\\label{tab:llama-per-relation-dr}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrr@{}}\n\\toprule\nRelation & PID & Triples & DR Violations & DR Rate (\\%) \\\\\n\\midrule\ndissolved/demolished & P576 & 73 & 24 & 32.9 \\\\\nfollowed by          & P156 & 117 & 24 & 20.5 \\\\\nunemployment rate    & P1198 & 15 & 3 & 20.0 \\\\\nend time             & P582 & 130 & 21 & 16.2 \\\\\ninstance of          & P31  & 290 & 37 & 12.8 \\\\\nproduct/material produced & P1056 & 98 & 11 & 11.2 \\\\\nlocation of formation & P740 & 81 & 8 & 9.9 \\\\\nhead of state        & P35  & 41  & 3  & 7.3 \\\\\napplies to jurisdiction & P1001 & 637 & 45 & 7.1 \\\\\nconflict             & P607 & 453 & 30 & 6.6 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n% exp_ids: llama_docred_full_s1\n\nCompared with Qwen, which retains a 10.21\\% residual DR under S1 concentrated in P1198 (83\\% fallback) and P171 (78\\% fallback), Llama's residual DR on the same relations is markedly lower (P1198 reaches only 20.0\\%) and no relation-level fallback concentration comparable to Qwen is observed.\n% exp_ids: llama_docred_full_s1, qwen_docred_full_s1\nThe substantially lower residual DR for Llama (2.55\\% vs.\\ Qwen's 10.21\\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01JXNZWEp9VYZB11fyUQfxGz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "4a158863-dcf5-421e-a1a5-c48ed57b12dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 42 · 2026-05-23T10:44:14.850Z_

<details><summary>↩ Tool result · `toolu_01JXNZWEp9VYZB11fyUQfxGz`</summary>

```text
1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{ll rrrrr rr}
13	\toprule
14	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
15	\midrule
16	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
17	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
18	\midrule
19	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
20	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
21	\midrule
22	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
23	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
24	\bottomrule
25	\end{tabular}}
26	\end{table}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
32	\label{tab:doc-length-docred}
33	\resizebox{\columnwidth}{!}{%
34	\begin{tabular}{ll rrrrr rr}
35	\toprule
36	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
37	\midrule
38	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
39	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
40	\midrule
41	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
42	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
43	\midrule
44	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 &  5.6 \\
45	             & Const. &   0 &    0 &  731 & 200 &  931 & 54.8 &  5.8 \\
46	\bottomrule
47	\end{tabular}}
48	\end{table}
49	
50	\begin{table}[h]
51	\centering
52	\small
53	\caption{Violation reduction percentage by document length bin (Qwen3-8B, S1 constraints).}
54	\label{tab:doc-length-reduction}
55	\resizebox{\columnwidth}{!}{%
56	\begin{tabular}{l rr rr}
57	\toprule
58	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{DocRED}} \\
59	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
60	\textbf{Bin} & \textbf{Viols (U$\to$C)} & \textbf{Red.\%} & \textbf{Viols (U$\to$C)} & \textbf{Red.\%} \\
61	\midrule
62	Short  & 63 $\to$ 10  & 84.1 & 2445 $\to$ 633  & 74.1 \\
63	Medium & 119 $\to$ 22 & 81.5 & 2941 $\to$ 729  & 75.2 \\
64	Long   & 118 $\to$ 24 & 79.7 & 3550 $\to$ 931  & 73.8 \\
65	\bottomrule
66	\end{tabular}}
67	\end{table}
68	
69	The violation reduction rate is consistent across all length bins: 80--84\% for SciERC and 74--75\% for DocRED.
70	Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction; the constraint framework scales reliably with document complexity.
71	ET and RV violations are fully eliminated across all bins.
72	F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "6908713f-ea9f-4dd0-882b-5b47d484a99f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex",
      "content": "\\section{Effect of Document Length on Constraint Effectiveness}\n\\label{app:doc-length}\n\nTo examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\\leq$ 19 words, Medium $\\leq$ 27, Long $>$ 27.}\n\\label{tab:doc-length-scierc}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrrrr rr}\n\\toprule\n\\textbf{Bin} & \\textbf{Mode} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{CF} & \\textbf{Total} & \\textbf{E-F1} & \\textbf{R-F1} \\\\\n\\midrule\nShort (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\\\\n             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\\\\n\\midrule\nMedium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\\\\n             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\\\\n\\midrule\nLong (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\\\\n             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\\leq$ 160 words, Medium $\\leq$ 208, Long $>$ 208.}\n\\label{tab:doc-length-docred}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrrrr rr}\n\\toprule\n\\textbf{Bin} & \\textbf{Mode} & \\textbf{ET} & \\textbf{RV} & \\textbf{DR} & \\textbf{CF} & \\textbf{Total} & \\textbf{E-F1} & \\textbf{R-F1} \\\\\n\\midrule\nShort (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\\\\n             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\\\\n\\midrule\nMedium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\\\\n             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\\\\n\\midrule\nLong (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 &  5.6 \\\\\n             & Const. &   0 &    0 &  731 & 200 &  931 & 54.8 &  5.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Violation reduction percentage by document length bin (Qwen3-8B, S1 constraints).}\n\\label{tab:doc-length-reduction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l rr rr}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{DocRED}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Bin} & \\textbf{Viols (U$\\to$C)} & \\textbf{Red.\\%} & \\textbf{Viols (U$\\to$C)} & \\textbf{Red.\\%} \\\\\n\\midrule\nShort  & 63 $\\to$ 10  & 84.1 & 2445 $\\to$ 633  & 74.1 \\\\\nMedium & 119 $\\to$ 22 & 81.5 & 2941 $\\to$ 729  & 75.2 \\\\\nLong   & 118 $\\to$ 24 & 79.7 & 3550 $\\to$ 931  & 73.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe violation reduction rate is consistent across all length bins: 80--84\\% for SciERC and 74--75\\% for DocRED.\nLonger documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction; the constraint framework scales reliably with document complexity.\nET and RV violations are fully eliminated across all bins.\nF1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.\n",
      "numLines": 73,
      "startLine": 1,
      "totalLines": 73
    }
  }
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_013EKbkYm7bnEvV7MmXP54Hq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ead29aa3-2dfc-488a-bd6b-6106d3ef0e1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 44 · 2026-05-23T10:44:16.029Z_

<details><summary>↩ Tool result · `toolu_013EKbkYm7bnEvV7MmXP54Hq`</summary>

```text
1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{llcccccc}
13	\toprule
14	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
15	\midrule
16	\multirow{2}{*}{Default}
17	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
18	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
19	\midrule
20	\multirow{2}{*}{Minimal}
21	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
22	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
23	\midrule
24	\multirow{2}{*}{Detailed}
25	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
26	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
31	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for all three prompt variants. Domain-range violations are reduced by 94.0\%--94.6\%, with a standard deviation of only 0.3 percentage points across prompts. Meanwhile, F1 scores remain effectively unchanged: the largest shift is 0.13 percentage points (R-F1, Default prompt), so constraint enforcement does not degrade extraction quality.
32	
33	Notably, prompt variation has a measurable effect on baseline (unconstrained) violation rates, with DR ranging from 11.1\% (Detailed) to 16.9\% (Minimal). Under constrained decoding, this range narrows to 0.64\%--0.93\%, a 20$\times$ reduction in cross-prompt variance. This convergence is expected: because OntoCoDec enforces constraints at the token level during decoding, it operates independently of prompt content. The consistent reduction rates across diverse prompt styles confirm that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.
34	Schema-informed prompting results serve as an upper bound on zero-shot prompt-level intervention; training-based approaches (e.g., GoLLIE) achieve compliance through code-generation format but with different coverage trade-offs (\S\ref{sec:related_work}).
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "d39339db-995b-4728-bc73-b25f14b9811b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex",
      "content": "\\section{Prompt Sensitivity Analysis}\n\\label{app:prompt-sensitivity}\n\nTo verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \\textbf{Default} (the prompt used in all main experiments), \\textbf{Minimal} (a shortened version listing only entity/relation types), and \\textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\\%), respectively. $\\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}\n\\label{tab:prompt-sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Prompt} & \\textbf{Mode} & \\textbf{ET\\%} & \\textbf{RV\\%} & \\textbf{DR\\%} & \\textbf{$\\Delta$DR} & \\textbf{E-F1} & \\textbf{R-F1} \\\\\n\\midrule\n\\multirow{2}{*}{Default}\n  & Unconstrained & 0.40 & 1.39 & 15.37 & \\multirow{2}{*}{94.0\\%} & 31.01 & 8.23 \\\\\n  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\\\\n\\midrule\n\\multirow{2}{*}{Minimal}\n  & Unconstrained & 0.58 & 1.16 & 16.91 & \\multirow{2}{*}{94.6\\%} & 31.98 & 7.91 \\\\\n  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\\\\n\\midrule\n\\multirow{2}{*}{Detailed}\n  & Unconstrained & 0.22 & 0.45 & 11.07 & \\multirow{2}{*}{94.2\\%} & 33.55 & 10.48 \\\\\n  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\\%) for all three prompt variants. Domain-range violations are reduced by 94.0\\%--94.6\\%, with a standard deviation of only 0.3 percentage points across prompts. Meanwhile, F1 scores remain effectively unchanged: the largest shift is 0.13 percentage points (R-F1, Default prompt), so constraint enforcement does not degrade extraction quality.\n\nNotably, prompt variation has a measurable effect on baseline (unconstrained) violation rates, with DR ranging from 11.1\\% (Detailed) to 16.9\\% (Minimal). Under constrained decoding, this range narrows to 0.64\\%--0.93\\%, a 20$\\times$ reduction in cross-prompt variance. This convergence is expected: because OntoCoDec enforces constraints at the token level during decoding, it operates independently of prompt content. The consistent reduction rates across diverse prompt styles confirm that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.\nSchema-informed prompting results serve as an upper bound on zero-shot prompt-level intervention; training-based approaches (e.g., GoLLIE) achieve compliance through code-generation format but with different coverage trade-offs (\\S\\ref{sec:related_work}).\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01CpX1fccmZ2ce5pfjcTX4oc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "fcb700ad-38d9-4023-87ad-3cca3dabc142",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 46 · 2026-05-23T10:44:16.461Z_

<details><summary>↩ Tool result · `toolu_01CpX1fccmZ2ce5pfjcTX4oc`</summary>

```text
1	% Appendix: Schema Ambiguity Analysis
2	% High-kappa relations and their impact on DR enforcement
3	
4	\paragraph{Schema ambiguity analysis.}
5	\label{app:kappa-analysis}
6	
7	We define the \emph{schema ambiguity} of a relation $r$ as the average fraction of relations that share each of $r$'s valid type pairs:
8	\begin{equation}
9	\alpha_r = \frac{1}{|\mathcal{P}_r|} \sum_{(h,t) \in \mathcal{P}_r} \frac{|\{r' \in \mathcal{R} : (h,t) \in \mathcal{P}_{r'}\}|}{|\mathcal{R}|}
10	\label{eq:schema-ambiguity}
11	\end{equation}
12	where $\mathcal{P}_r$ is the set of valid entity type pairs for relation $r$ and $\mathcal{R}$ is the full relation set.
13	High $\alpha_r$ indicates that $r$'s valid type pairs are shared by many other relations, limiting the discriminative power of type constraints for that relation.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Schema ambiguity $\alpha$ for all SciERC relations and the 12 DocRED relations with $\alpha \geq 0.36$. \textbf{Gold \%}: fraction of all gold triples belonging to this relation. All SciERC relations exceed the threshold due to the small schema (7 relations, 6 entity types); in DocRED, only 12 of 96 relations qualify, covering 3.8\% of gold triples.}
19	\label{tab:high-kappa-rels}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{@{}llrrrr@{}}
22	\toprule
23	\textbf{Dataset} & \textbf{Relation} & $\alpha$ & \textbf{$|\mathcal{P}_r|$} & \textbf{Gold} & \textbf{Gold \%} \\
24	\midrule
25	\multicolumn{6}{@{}l}{\textit{SciERC (all 7 relations exceed $\alpha \geq 0.36$)}} \\
26	SciERC & Hyponym-of    & 0.83 & 21 &  298 &  9.3 \\
27	SciERC & Part-of       & 0.83 & 21 &  179 &  5.6 \\
28	SciERC & Compare       & 0.82 & 17 &  166 &  5.2 \\
29	SciERC & Conjunction   & 0.77 & 25 &  400 & 12.4 \\
30	SciERC & Feature-of    & 0.76 & 26 &  173 &  5.4 \\
31	SciERC & Evaluate-for  & 0.71 & 23 &  313 &  9.7 \\
32	SciERC & Used-for      & 0.67 & 35 & 1{,}690 & 52.5 \\
33	\midrule
34	\multicolumn{6}{@{}l}{\textit{DocRED (12 of 96 relations with $\alpha \geq 0.36$; 3.8\% of gold)}} \\
35	DocRED & sister city (P190)          & 0.42 &  1 &    4 & 0.01 \\
36	DocRED & basin country (P205)        & 0.42 &  1 &   85 & 0.22 \\
37	DocRED & mouth of watercourse (P403) & 0.42 &  1 &   95 & 0.25 \\
38	DocRED & separated from (P807)       & 0.41 &  2 &    2 & 0.01 \\
39	DocRED & replaces (P1365)            & 0.39 &  4 &   18 & 0.05 \\
40	DocRED & capital of (P1376)          & 0.37 &  3 &   76 & 0.20 \\
41	DocRED & place of birth (P19)        & 0.37 &  3 &  511 & 1.34 \\
42	DocRED & operator (P137)             & 0.36 &  7 &   95 & 0.25 \\
43	DocRED & military branch (P241)      & 0.36 &  5 &  108 & 0.28 \\
44	DocRED & production company (P272)   & 0.36 &  5 &   82 & 0.21 \\
45	DocRED & place of death (P20)        & 0.36 &  4 &  203 & 0.53 \\
46	DocRED & location (P276)             & 0.36 &  5 &  172 & 0.45 \\
47	\bottomrule
48	\end{tabular}}
49	\end{table}
50	
51	\begin{table}[h]
52	\centering
53	\small
54	\caption{DR violation rates partitioned by schema ambiguity. High-$\alpha$ relations ($\alpha \geq 0.36$) start with substantially higher unconstrained DR on DocRED, and retain elevated residual DR under S1 for Qwen but not for Llama.}
55	\label{tab:dr-by-ambiguity}
56	\begin{tabular}{@{}llrrrr@{}}
57	\toprule
58	& & \multicolumn{2}{c}{\textbf{Unconstrained}} & \multicolumn{2}{c}{\textbf{S1 (Constrained)}} \\
59	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
60	\textbf{Model} & \textbf{Partition} & DR\% & $n$ & DR\% & $n$ \\
61	\midrule
62	\multirow{2}{*}{Llama-3.1-8B}
63	 & High-$\alpha$ (12 rels) & 43.8 &   861 &  3.2 & 1{,}043 \\
64	 & Low-$\alpha$ (84 rels)  & 29.9 & 12{,}809 &  2.5 & 15{,}325 \\
65	\midrule
66	\multirow{2}{*}{Qwen3-8B}
67	 & High-$\alpha$ (12 rels) & 31.9 &   718 & 20.0 & 1{,}119 \\
68	 & Low-$\alpha$ (84 rels)  & 21.2 & 10{,}898 &  9.5 & 16{,}217 \\
69	\bottomrule
70	\end{tabular}
71	\end{table}
72	
73	Table~\ref{tab:high-kappa-rels} reveals a structural asymmetry between datasets.
74	In SciERC, all seven relations have $\alpha \geq 0.67$: with only 7 relations over $6^2 = 36$ entity type pair slots, extensive overlap is inevitable.
75	For example, the pair (Method, Method) is valid for all 7 relations ($\alpha = 1.0$).
76	In DocRED, 96 relations spread across the same 36 type pair slots yield much lower per-relation ambiguity; only 12 relations exceed $\alpha \geq 0.36$, and these collectively cover just 3.8\% of gold triples.
77	
78	Table~\ref{tab:dr-by-ambiguity} shows the DR impact stratified by ambiguity.
79	On DocRED, high-$\alpha$ relations exhibit substantially higher unconstrained DR (43.8\% for Llama vs.\ 29.9\% for low-$\alpha$), reflecting the inherent difficulty of relations whose valid type pairs are shared by dozens of other relations---the model frequently assigns a type combination that, while valid for \emph{some} relation, violates the constraints of the target relation.
80	Under S1 constraints, Llama reduces both groups to near-parity (3.2\% vs.\ 2.5\%), whereas Qwen retains a 2$\times$ gap (20.0\% vs.\ 9.5\%), indicating that constraint effectiveness on high-ambiguity relations depends on the model's baseline type accuracy.
81	Excluding the 12 high-$\alpha$ relations from the DocRED evaluation changes the overall S1 DR only marginally---from 2.55\% to 2.51\% for Llama and from 10.21\% to 9.53\% for Qwen---confirming that their small gold footprint (3.8\%) limits their aggregate impact despite elevated per-relation rates.
82	On SciERC, where all relations have high $\alpha$, the exclusion analysis is vacuous; yet OntoCoDec still reduces DR from 15.4\% to 0.9\% (Qwen) and from 13.3\% to 0.08\% (Llama), demonstrating that high schema ambiguity does not preclude effective constraint enforcement.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "fc2d1c49-c81e-4daf-a79c-ac588fd1947f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex",
      "content": "% Appendix: Schema Ambiguity Analysis\n% High-kappa relations and their impact on DR enforcement\n\n\\paragraph{Schema ambiguity analysis.}\n\\label{app:kappa-analysis}\n\nWe define the \\emph{schema ambiguity} of a relation $r$ as the average fraction of relations that share each of $r$'s valid type pairs:\n\\begin{equation}\n\\alpha_r = \\frac{1}{|\\mathcal{P}_r|} \\sum_{(h,t) \\in \\mathcal{P}_r} \\frac{|\\{r' \\in \\mathcal{R} : (h,t) \\in \\mathcal{P}_{r'}\\}|}{|\\mathcal{R}|}\n\\label{eq:schema-ambiguity}\n\\end{equation}\nwhere $\\mathcal{P}_r$ is the set of valid entity type pairs for relation $r$ and $\\mathcal{R}$ is the full relation set.\nHigh $\\alpha_r$ indicates that $r$'s valid type pairs are shared by many other relations, limiting the discriminative power of type constraints for that relation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Schema ambiguity $\\alpha$ for all SciERC relations and the 12 DocRED relations with $\\alpha \\geq 0.36$. \\textbf{Gold \\%}: fraction of all gold triples belonging to this relation. All SciERC relations exceed the threshold due to the small schema (7 relations, 6 entity types); in DocRED, only 12 of 96 relations qualify, covering 3.8\\% of gold triples.}\n\\label{tab:high-kappa-rels}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Relation} & $\\alpha$ & \\textbf{$|\\mathcal{P}_r|$} & \\textbf{Gold} & \\textbf{Gold \\%} \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{SciERC (all 7 relations exceed $\\alpha \\geq 0.36$)}} \\\\\nSciERC & Hyponym-of    & 0.83 & 21 &  298 &  9.3 \\\\\nSciERC & Part-of       & 0.83 & 21 &  179 &  5.6 \\\\\nSciERC & Compare       & 0.82 & 17 &  166 &  5.2 \\\\\nSciERC & Conjunction   & 0.77 & 25 &  400 & 12.4 \\\\\nSciERC & Feature-of    & 0.76 & 26 &  173 &  5.4 \\\\\nSciERC & Evaluate-for  & 0.71 & 23 &  313 &  9.7 \\\\\nSciERC & Used-for      & 0.67 & 35 & 1{,}690 & 52.5 \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{DocRED (12 of 96 relations with $\\alpha \\geq 0.36$; 3.8\\% of gold)}} \\\\\nDocRED & sister city (P190)          & 0.42 &  1 &    4 & 0.01 \\\\\nDocRED & basin country (P205)        & 0.42 &  1 &   85 & 0.22 \\\\\nDocRED & mouth of watercourse (P403) & 0.42 &  1 &   95 & 0.25 \\\\\nDocRED & separated from (P807)       & 0.41 &  2 &    2 & 0.01 \\\\\nDocRED & replaces (P1365)            & 0.39 &  4 &   18 & 0.05 \\\\\nDocRED & capital of (P1376)          & 0.37 &  3 &   76 & 0.20 \\\\\nDocRED & place of birth (P19)        & 0.37 &  3 &  511 & 1.34 \\\\\nDocRED & operator (P137)             & 0.36 &  7 &   95 & 0.25 \\\\\nDocRED & military branch (P241)      & 0.36 &  5 &  108 & 0.28 \\\\\nDocRED & production company (P272)   & 0.36 &  5 &   82 & 0.21 \\\\\nDocRED & place of death (P20)        & 0.36 &  4 &  203 & 0.53 \\\\\nDocRED & location (P276)             & 0.36 &  5 &  172 & 0.45 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DR violation rates partitioned by schema ambiguity. High-$\\alpha$ relations ($\\alpha \\geq 0.36$) start with substantially higher unconstrained DR on DocRED, and retain elevated residual DR under S1 for Qwen but not for Llama.}\n\\label{tab:dr-by-ambiguity}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{Unconstrained}} & \\multicolumn{2}{c}{\\textbf{S1 (Constrained)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n\\textbf{Model} & \\textbf{Partition} & DR\\% & $n$ & DR\\% & $n$ \\\\\n\\midrule\n\\multirow{2}{*}{Llama-3.1-8B}\n & High-$\\alpha$ (12 rels) & 43.8 &   861 &  3.2 & 1{,}043 \\\\\n & Low-$\\alpha$ (84 rels)  & 29.9 & 12{,}809 &  2.5 & 15{,}325 \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}\n & High-$\\alpha$ (12 rels) & 31.9 &   718 & 20.0 & 1{,}119 \\\\\n & Low-$\\alpha$ (84 rels)  & 21.2 & 10{,}898 &  9.5 & 16{,}217 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:high-kappa-rels} reveals a structural asymmetry between datasets.\nIn SciERC, all seven relations have $\\alpha \\geq 0.67$: with only 7 relations over $6^2 = 36$ entity type pair slots, extensive overlap is inevitable.\nFor example, the pair (Method, Method) is valid for all 7 relations ($\\alpha = 1.0$).\nIn DocRED, 96 relations spread across the same 36 type pair slots yield much lower per-relation ambiguity; only 12 relations exceed $\\alpha \\geq 0.36$, and these collectively cover just 3.8\\% of gold triples.\n\nTable~\\ref{tab:dr-by-ambiguity} shows the DR impact stratified by ambiguity.\nOn DocRED, high-$\\alpha$ relations exhibit substantially higher unconstrained DR (43.8\\% for Llama vs.\\ 29.9\\% for low-$\\alpha$), reflecting the inherent difficulty of relations whose valid type pairs are shared by dozens of other relations---the model frequently assigns a type combination that, while valid for \\emph{some} relation, violates the constraints of the target relation.\nUnder S1 constraints, Llama reduces both groups to near-parity (3.2\\% vs.\\ 2.5\\%), whereas Qwen retains a 2$\\times$ gap (20.0\\% vs.\\ 9.5\\%), indicating that constraint effectiveness on high-ambiguity relations depends on the model's baseline type accuracy.\nExcluding the 12 high-$\\alpha$ relations from the DocRED evaluation changes the overall S1 DR only marginally---from 2.55\\% to 2.51\\% for Llama and from 10.21\\% to 9.53\\% for Qwen---confirming that their small gold footprint (3.8\\%) limits their aggregate impact despite elevated per-relation rates.\nOn SciERC, where all relations have high $\\alpha$, the exclusion analysis is vacuous; yet OntoCoDec still reduces DR from 15.4\\% to 0.9\\% (Qwen) and from 13.3\\% to 0.08\\% (Llama), demonstrating that high schema ambiguity does not preclude effective constraint enforcement.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  }
}
```

</details>

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_015zJnewKE6e5WwhNhpr2Uot`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "03439147-ed69-4517-896b-469b94fbe6e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BQ3rszdNfArmegvKRyKrm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37059,
      "cache_read_input_tokens": 25761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37059
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

_source line 48 · 2026-05-23T10:44:16.682Z_

<details><summary>↩ Tool result · `toolu_015zJnewKE6e5WwhNhpr2Uot`</summary>

```text
1	\paragraph{Downstream impact of violation removal.}
2	\label{app:downstream-impact}
3	
4	A natural concern with schema-constrained decoding is whether enforcing ontological validity removes \emph{lucky violations}---predictions that happen to be correct (true positives) yet violate the schema.
5	To quantify this trade-off, we audit all true-positive relation triples produced by unconstrained fine-tuned models and check whether any of them carry a domain--range (DR) violation, i.e., an entity-type pair \mbox{$\langle h_\tau, t_\tau \rangle$} not sanctioned by the ontology for that relation.
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\begin{tabular}{llrrrl}
11	\toprule
12	\textbf{Dataset} & \textbf{Model} & \textbf{TP} & \textbf{Lucky} & \textbf{\%\,TP} & \textbf{R drop} \\
13	\midrule
14	SciERC & Qwen-LoRA  & 461  & 4 & 0.87\% & 0.41\,pp \\
15	SciERC & Llama-LoRA & 467  & 5 & 1.07\% & 0.51\,pp \\
16	DocRED & Qwen-LoRA  & 5746 & 1 & 0.02\% & 0.01\,pp \\
17	DocRED & Llama-LoRA & 6226 & 1 & 0.02\% & 0.01\,pp \\
18	\bottomrule
19	\end{tabular}
20	\caption{Lucky violations: true-positive triples that carry a domain--range violation. \textbf{Lucky} counts such triples; \textbf{R drop} is the recall decrease (in percentage points) if they were removed.}
21	\label{tab:lucky-violations-detail}
22	\end{table}
23	
24	Across all four configurations, lucky violations account for at most 1.07\% of true positives (5 out of 467 on SciERC with Llama-LoRA) and as few as 0.02\% on DocRED.
25	The corresponding recall drop is negligible---at most 0.51 percentage points---while the vast majority of violated triples that constraints remove are false positives.
26	For example, on DocRED with Qwen-LoRA, constraints eliminate 164 schema-violating predictions but only 1 of them is actually correct; the other 163 are errors that would pollute a downstream knowledge graph.
27	
28	Inspecting the lucky violations qualitatively, they arise from borderline entity-type assignments rather than genuine schema gaps.
29	On SciERC, the recurring pattern involves \textsc{Metric}-typed entities (e.g., BLEU, NIST) appearing as heads of \texttt{Hyponym-of} relations, a pair absent from the training ontology because these metrics are rarely annotated as hyponyms.
30	On DocRED, the single lucky violation stems from an entity typed as \textsc{Misc} instead of \textsc{Org} (``Assassin's Creed Unity''), making its \texttt{developer} relation invalid under the schema despite being factually correct.
31	
32	These findings confirm that schema-constrained decoding introduces a minimal recall cost while providing a substantial precision gain.
33	Retaining these few lucky violations would allow schema-invalid triples into the knowledge graph, undermining the structural guarantees that motivate constrained decoding in the first place.
34	The net effect is overwhelmingly positive: constraints act as a high-precision filter that removes far more erroneous triples than correct ones.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "4e0f24b0-0362-416a-98e5-df8ce7726301",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex",
      "content": "\\paragraph{Downstream impact of violation removal.}\n\\label{app:downstream-impact}\n\nA natural concern with schema-constrained decoding is whether enforcing ontological validity removes \\emph{lucky violations}---predictions that happen to be correct (true positives) yet violate the schema.\nTo quantify this trade-off, we audit all true-positive relation triples produced by unconstrained fine-tuned models and check whether any of them carry a domain--range (DR) violation, i.e., an entity-type pair \\mbox{$\\langle h_\\tau, t_\\tau \\rangle$} not sanctioned by the ontology for that relation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrl}\n\\toprule\n\\textbf{Dataset} & \\textbf{Model} & \\textbf{TP} & \\textbf{Lucky} & \\textbf{\\%\\,TP} & \\textbf{R drop} \\\\\n\\midrule\nSciERC & Qwen-LoRA  & 461  & 4 & 0.87\\% & 0.41\\,pp \\\\\nSciERC & Llama-LoRA & 467  & 5 & 1.07\\% & 0.51\\,pp \\\\\nDocRED & Qwen-LoRA  & 5746 & 1 & 0.02\\% & 0.01\\,pp \\\\\nDocRED & Llama-LoRA & 6226 & 1 & 0.02\\% & 0.01\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Lucky violations: true-positive triples that carry a domain--range violation. \\textbf{Lucky} counts such triples; \\textbf{R drop} is the recall decrease (in percentage points) if they were removed.}\n\\label{tab:lucky-violations-detail}\n\\end{table}\n\nAcross all four configurations, lucky violations account for at most 1.07\\% of true positives (5 out of 467 on SciERC with Llama-LoRA) and as few as 0.02\\% on DocRED.\nThe corresponding recall drop is negligible---at most 0.51 percentage points---while the vast majority of violated triples that constraints remove are false positives.\nFor example, on DocRED with Qwen-LoRA, constraints eliminate 164 schema-violating predictions but only 1 of them is actually correct; the other 163 are errors that would pollute a downstream knowledge graph.\n\nInspecting the lucky violations qualitatively, they arise from borderline entity-type assignments rather than genuine schema gaps.\nOn SciERC, the recurring pattern involves \\textsc{Metric}-typed entities (e.g., BLEU, NIST) appearing as heads of \\texttt{Hyponym-of} relations, a pair absent from the training ontology because these metrics are rarely annotated as hyponyms.\nOn DocRED, the single lucky violation stems from an entity typed as \\textsc{Misc} instead of \\textsc{Org} (``Assassin's Creed Unity''), making its \\texttt{developer} relation invalid under the schema despite being factually correct.\n\nThese findings confirm that schema-constrained decoding introduces a minimal recall cost while providing a substantial precision gain.\nRetaining these few lucky violations would allow schema-invalid triples into the knowledge graph, undermining the structural guarantees that motivate constrained decoding in the first place.\nThe net effect is overwhelmingly positive: constraints act as a high-precision filter that removes far more erroneous triples than correct ones.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---


### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the remaining appendix files that might have tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "79d79795-2fd8-480e-9eb3-66164919a0ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wt5oMfPGRoWmYcLmQ2sgML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10291,
      "cache_read_input_tokens": 62820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10291
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

_source line 50_

Let me read the remaining appendix files and start querying the registry for specific experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "faaca65d-47d3-40c6-a01a-dd3bf29f89ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wt5oMfPGRoWmYcLmQ2sgML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10291,
      "cache_read_input_tokens": 62820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10291
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01VKzVT6s8mXtHMEjjWKnq7y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "cecec99b-9736-4df7-9654-ff8b34ece5e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wt5oMfPGRoWmYcLmQ2sgML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10291,
      "cache_read_input_tokens": 62820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10291
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

_source line 52 · 2026-05-23T10:44:25.795Z_

<details><summary>↩ Tool result · `toolu_01VKzVT6s8mXtHMEjjWKnq7y`</summary>

```text
1	% Appendix: Post-hoc Type Consistency Resolution (TCR)
2	% exp_ids: d065_tcr_pilot (all 10 configs)
3	
4	\section{Post-hoc Type Consistency Resolution}
5	\label{app:tcr}
6	
7	S1 enforces domain/range constraints per-triple but does not enforce global entity type consensus, leaving residual CF violations where the same entity receives different types across triples.
8	We evaluate a post-hoc resolution step (TCR): for each entity with conflicting type assignments, TCR selects the type that maximizes satisfaction count across all relations referencing that entity, subject to domain/range constraints.
9	Unlike naive majority voting (which ignores relational constraints and increases DR), TCR is constraint-aware: candidate types are scored by how many of the entity's relational contexts they satisfy.
10	TCR runs after S1 decoding completes and has access to the full document context.
11	
12	% ──────────────────────────────────────────
13	%  Table: TCR results on SciERC
14	% ──────────────────────────────────────────
15	\begin{table}[h]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rr rr r r@{}}
20	\toprule
21	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
22	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
23	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
24	\midrule
25	\multirow{3}{*}{Zero-shot}
26	  & Qwen    & 9.75 & \textbf{0} & 0.93  & 1.21  & $-$1.29 & 2.04 \\
27	  & Llama   & 6.40 & \textbf{0} & 0.08  & 0.30  & $-$1.78 & 1.85 \\
28	  & Mistral & 0.67 & \textbf{0} & 13.36 & 12.87 & $+$0.05 & 0 \\
29	\midrule
30	\multirow{2}{*}{LoRA}
31	  & Qwen    & 1.19 & \textbf{0} & 0     & 0     & $-$0.75 & 0 \\
32	  & Llama   & 0.46 & \textbf{0} & 0.09  & 0.09  & $-$0.18 & 0 \\
33	\bottomrule
34	\end{tabular}}
35	\caption{TCR on SciERC ($\bar{\kappa}{=}0.333$, 551 docs).
36	Pre/Post: before/after TCR.
37	$\Delta$E-F1: entity F1 change (F1$\times$100).
38	Fund.: percentage of conflicting entities where no single type satisfies all relational constraints (fundamental conflicts).
39	TCR eliminates all CF with DR increases $\leq$0.28\,pp; fundamental conflicts are 0--2\%.}
40	\label{tab:tcr-scierc}
41	\end{table}
42	
43	% ──────────────────────────────────────────
44	%  Table: TCR results on DocRED
45	% ──────────────────────────────────────────
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{@{}ll rr rr r r@{}}
51	\toprule
52	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
53	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
54	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness varies inversely with schema constraint tightness $\bar{\kappa}$ (descriptive pattern across two schemas).
75	On SciERC ($\bar{\kappa}{=}0.333$), fundamental conflicts constitute 0--2\% of type disagreements: most conflicts are resolvable because the loose schema admits many valid type pairs, and TCR can find a type satisfying all relational contexts.
76	DR increases are bounded ($\leq$0.28\,pp), and E-F1 cost is modest ($\leq$1.78\,pp in zero-shot, $\leq$0.75\,pp under LoRA).
77	On DocRED ($\bar{\kappa}{=}0.842$), 13--23\% of conflicts are fundamental: the tight schema renders most type pairs invalid, so unifying an entity's type across all its relational contexts inevitably violates some domain/range constraints.
78	This produces severe DR regressions under zero-shot (Llama: 2.55\%$\to$11.93\%; 70B: 0\%$\to$4.20\%), where baseline CF is high enough that many entities require resolution.
79	Under LoRA, baseline CF is already low (0.36--0.42\%), limiting both the scope for TCR improvement and the DR cost.
80	
81	This $\bar{\kappa}$-dependent boundary is consistent with the constraint tightness analysis in \S\ref{sec:composition}: $\bar{\kappa}$ characterizes not only the decoding-time DR residual regime but also the feasibility of post-hoc type resolution.
82	Beam search (\S\ref{sec:beam-results}) resolves CF and DR simultaneously across all $\bar{\kappa}$ values (SciERC and DocRED (998 docs): DR$\to$0\% for calibrated models), making it the preferred approach for high-tightness schemas.
83	TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\times$) is undesirable.
84	Integrating TCR into the decoding loop would require global optimization over all generated triples, conflicting with the autoregressive generation paradigm.
85	TCR is complementary to OntoCoDec---it addresses CF (which OntoCoDec's per-triple enforcement cannot prevent) while OntoCoDec addresses DR (which post-hoc correction cannot guarantee).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3f01fcf8-a98b-4e4e-8995-3e95cabf7c17",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex",
      "content": "% Appendix: Post-hoc Type Consistency Resolution (TCR)\n% exp_ids: d065_tcr_pilot (all 10 configs)\n\n\\section{Post-hoc Type Consistency Resolution}\n\\label{app:tcr}\n\nS1 enforces domain/range constraints per-triple but does not enforce global entity type consensus, leaving residual CF violations where the same entity receives different types across triples.\nWe evaluate a post-hoc resolution step (TCR): for each entity with conflicting type assignments, TCR selects the type that maximizes satisfaction count across all relations referencing that entity, subject to domain/range constraints.\nUnlike naive majority voting (which ignores relational constraints and increases DR), TCR is constraint-aware: candidate types are scored by how many of the entity's relational contexts they satisfy.\nTCR runs after S1 decoding completes and has access to the full document context.\n\n% ──────────────────────────────────────────\n%  Table: TCR results on SciERC\n% ──────────────────────────────────────────\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rr rr r r@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{CF (\\%)}} & \\multicolumn{2}{c}{\\textbf{DR (\\%)}} & \\textbf{$\\Delta$E-F1} & \\textbf{Fund.} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-7} \\cmidrule(l){8-8}\n\\textbf{Config} & \\textbf{Model} & Pre & Post & Pre & Post & (pp) & (\\%) \\\\\n\\midrule\n\\multirow{3}{*}{Zero-shot}\n  & Qwen    & 9.75 & \\textbf{0} & 0.93  & 1.21  & $-$1.29 & 2.04 \\\\\n  & Llama   & 6.40 & \\textbf{0} & 0.08  & 0.30  & $-$1.78 & 1.85 \\\\\n  & Mistral & 0.67 & \\textbf{0} & 13.36 & 12.87 & $+$0.05 & 0 \\\\\n\\midrule\n\\multirow{2}{*}{LoRA}\n  & Qwen    & 1.19 & \\textbf{0} & 0     & 0     & $-$0.75 & 0 \\\\\n  & Llama   & 0.46 & \\textbf{0} & 0.09  & 0.09  & $-$0.18 & 0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{TCR on SciERC ($\\bar{\\kappa}{=}0.333$, 551 docs).\nPre/Post: before/after TCR.\n$\\Delta$E-F1: entity F1 change (F1$\\times$100).\nFund.: percentage of conflicting entities where no single type satisfies all relational constraints (fundamental conflicts).\nTCR eliminates all CF with DR increases $\\leq$0.28\\,pp; fundamental conflicts are 0--2\\%.}\n\\label{tab:tcr-scierc}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  Table: TCR results on DocRED\n% ──────────────────────────────────────────\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rr rr r r@{}}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{CF (\\%)}} & \\multicolumn{2}{c}{\\textbf{DR (\\%)}} & \\textbf{$\\Delta$E-F1} & \\textbf{Fund.} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-7} \\cmidrule(l){8-8}\n\\textbf{Config} & \\textbf{Model} & Pre & Post & Pre & Post & (pp) & (\\%) \\\\\n\\midrule\n\\multirow{3}{*}{Zero-shot}\n  & Qwen    & 13.11 & \\textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\\\\n  & Llama   & 23.71 & \\textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\\\\n  & 70B     & 11.61 & \\textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\\\\n\\midrule\n\\multirow{2}{*}{LoRA}\n  & Qwen    &  0.42 & \\textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\\\\n  & Llama   &  0.36 & \\textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{TCR on DocRED ($\\bar{\\kappa}{=}0.842$, 998 docs).\nUnder zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\\,pp for Llama) and E-F1 drops (up to $-$5.98\\,pp for 70B).\nFundamental conflict rates are 12--23\\%, an order of magnitude higher than SciERC.\nUnder LoRA, low baseline CF (0.36--0.42\\%) limits both TCR impact and DR cost.}\n\\label{tab:tcr-docred}\n\\end{table}\n\n\\paragraph{Analysis.}\nTCR effectiveness varies inversely with schema constraint tightness $\\bar{\\kappa}$ (descriptive pattern across two schemas).\nOn SciERC ($\\bar{\\kappa}{=}0.333$), fundamental conflicts constitute 0--2\\% of type disagreements: most conflicts are resolvable because the loose schema admits many valid type pairs, and TCR can find a type satisfying all relational contexts.\nDR increases are bounded ($\\leq$0.28\\,pp), and E-F1 cost is modest ($\\leq$1.78\\,pp in zero-shot, $\\leq$0.75\\,pp under LoRA).\nOn DocRED ($\\bar{\\kappa}{=}0.842$), 13--23\\% of conflicts are fundamental: the tight schema renders most type pairs invalid, so unifying an entity's type across all its relational contexts inevitably violates some domain/range constraints.\nThis produces severe DR regressions under zero-shot (Llama: 2.55\\%$\\to$11.93\\%; 70B: 0\\%$\\to$4.20\\%), where baseline CF is high enough that many entities require resolution.\nUnder LoRA, baseline CF is already low (0.36--0.42\\%), limiting both the scope for TCR improvement and the DR cost.\n\nThis $\\bar{\\kappa}$-dependent boundary is consistent with the constraint tightness analysis in \\S\\ref{sec:composition}: $\\bar{\\kappa}$ characterizes not only the decoding-time DR residual regime but also the feasibility of post-hoc type resolution.\nBeam search (\\S\\ref{sec:beam-results}) resolves CF and DR simultaneously across all $\\bar{\\kappa}$ values (SciERC and DocRED (998 docs): DR$\\to$0\\% for calibrated models), making it the preferred approach for high-tightness schemas.\nTCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\\times$) is undesirable.\nIntegrating TCR into the decoding loop would require global optimization over all generated triples, conflicting with the autoregressive generation paradigm.\nTCR is complementary to OntoCoDec---it addresses CF (which OntoCoDec's per-triple enforcement cannot prevent) while OntoCoDec addresses DR (which post-hoc correction cannot guarantee).\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_011nx13zrRcSjDQithAYgiXu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "045ee79f-a9be-439b-a73b-c89e935ada8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wt5oMfPGRoWmYcLmQ2sgML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10291,
      "cache_read_input_tokens": 62820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10291
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

_source line 54 · 2026-05-23T10:44:26.731Z_

<details><summary>↩ Tool result · `toolu_011nx13zrRcSjDQithAYgiXu`</summary>

```text
1	% Appendix: Statistical Power Analysis for WikiEvents n=20
2	% Addresses reviewer concern about WikiEvents FT statistical power.
3	% Include via \input{appendix_power_analysis} in the appendix.
4	
5	\paragraph{Statistical power across evaluation settings.}
6	\label{app:power-analysis-full}
7	Table~\ref{tab:power-analysis} reports bootstrap confidence interval width and minimum detectable effect (MDE) for F1 across evaluation settings (${\geq}$1{,}000 bootstrap resamples; MDE at 80\% power, $\alpha{=}0.05$, paired test, $\rho{=}0.9$).
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\begin{tabular}{lrrr}
13	\toprule
14	\textbf{Dataset} & \textbf{$n$} & \textbf{95\% CI (F1)} & \textbf{MDE (F1)} \\
15	\midrule
16	SciERC & 551 & $\pm$1.8\,pp & 1.2\,pp \\
17	DocRED & 998 & $\pm$0.8\,pp & 0.5\,pp \\
18	DocRED (70B) & 200 & $\pm$3.3\,pp & 2.1\,pp \\
19	WikiEvents & 20 & $\pm$3.0\,pp & 2.0\,pp \\
20	\bottomrule
21	\end{tabular}
22	\caption{Statistical precision by dataset size.
23	95\% CI: bootstrap confidence interval half-width for per-configuration F1.
24	MDE: minimum detectable F1 difference at 80\% power ($\alpha{=}0.05$, paired test, conservative $\rho{=}0.9$).
25	SciERC/DocRED: zero-shot Rel-F1; DocRED (70B): LoRA Rel-F1 (200-doc subset); WikiEvents: LoRA Arg-F1.}
26	\label{tab:power-analysis}
27	\end{table}
28	
29	WikiEvents' $n{=}20$ yields an Arg-F1 margin of error of $\pm$3.0\,pp---comparable to the 200-document DocRED subset ($\pm$3.3\,pp)---with MDE${\approx}$2.0\,pp.
30	However, the primary WikiEvents claims concern violation elimination, not F1 improvement: RoV drops from 8.8--38.3\% to exactly 0\% across both models (bootstrap 95\% CI $[0\%,\,0\%]$ vs.\ $[2.4\%,\,15.4\%]$ / $[25.4\%,\,46.7\%]$; power${\approx}$1.0).
31	The small test set limits detection of subtle F1 shifts, but complete elimination of schema violations is unambiguous at $n{=}20$; the primary evidence for F1 preservation rests on SciERC ($n{=}551$) and DocRED ($n{=}998$), where CIs are ${\leq}$1.8\,pp.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "9dfd54b1-5ce0-4102-9861-b6b26d85a440",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex",
      "content": "% Appendix: Statistical Power Analysis for WikiEvents n=20\n% Addresses reviewer concern about WikiEvents FT statistical power.\n% Include via \\input{appendix_power_analysis} in the appendix.\n\n\\paragraph{Statistical power across evaluation settings.}\n\\label{app:power-analysis-full}\nTable~\\ref{tab:power-analysis} reports bootstrap confidence interval width and minimum detectable effect (MDE) for F1 across evaluation settings (${\\geq}$1{,}000 bootstrap resamples; MDE at 80\\% power, $\\alpha{=}0.05$, paired test, $\\rho{=}0.9$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{95\\% CI (F1)} & \\textbf{MDE (F1)} \\\\\n\\midrule\nSciERC & 551 & $\\pm$1.8\\,pp & 1.2\\,pp \\\\\nDocRED & 998 & $\\pm$0.8\\,pp & 0.5\\,pp \\\\\nDocRED (70B) & 200 & $\\pm$3.3\\,pp & 2.1\\,pp \\\\\nWikiEvents & 20 & $\\pm$3.0\\,pp & 2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical precision by dataset size.\n95\\% CI: bootstrap confidence interval half-width for per-configuration F1.\nMDE: minimum detectable F1 difference at 80\\% power ($\\alpha{=}0.05$, paired test, conservative $\\rho{=}0.9$).\nSciERC/DocRED: zero-shot Rel-F1; DocRED (70B): LoRA Rel-F1 (200-doc subset); WikiEvents: LoRA Arg-F1.}\n\\label{tab:power-analysis}\n\\end{table}\n\nWikiEvents' $n{=}20$ yields an Arg-F1 margin of error of $\\pm$3.0\\,pp---comparable to the 200-document DocRED subset ($\\pm$3.3\\,pp)---with MDE${\\approx}$2.0\\,pp.\nHowever, the primary WikiEvents claims concern violation elimination, not F1 improvement: RoV drops from 8.8--38.3\\% to exactly 0\\% across both models (bootstrap 95\\% CI $[0\\%,\\,0\\%]$ vs.\\ $[2.4\\%,\\,15.4\\%]$ / $[25.4\\%,\\,46.7\\%]$; power${\\approx}$1.0).\nThe small test set limits detection of subtle F1 shifts, but complete elimination of schema violations is unambiguous at $n{=}20$; the primary evidence for F1 preservation rests on SciERC ($n{=}551$) and DocRED ($n{=}998$), where CIs are ${\\leq}$1.8\\,pp.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01AtCYsm32LUn3GdNbrfTMHq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3f2a038a-c7b4-4216-adc0-0da1d7051171",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wt5oMfPGRoWmYcLmQ2sgML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10291,
      "cache_read_input_tokens": 62820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10291
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

_source line 56 · 2026-05-23T10:44:28.195Z_

<details><summary>↩ Tool result · `toolu_01AtCYsm32LUn3GdNbrfTMHq`</summary>

```text
1	% Appendix: Constraint Tightness Case Study
2	% Data source: case_study_kappa_dr_dddc01.md (Qwen-2.5-7B zero-shot unconstrained)
3	
4	\section{Constraint Tightness Case Study}
5	\label{app:kappa-case-study}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\resizebox{\columnwidth}{!}{%
11	\begin{tabular}{@{}llccc l@{}}
12	\toprule
13	\textbf{Relation} & \textbf{Dataset} & $\kappa$ & \textbf{DR\%} & $n$ & \textbf{Explanation} \\
14	\midrule
15	\multicolumn{6}{@{}l}{\textit{Highest DR violation rate}} \\
16	basin country        & DocRED & .97 & 74.6 &  63 & Sole valid pair \textsc{loc}$\to$\textsc{loc}; head mistyped as \textsc{org}/\textsc{misc} \\
17	product produced     & DocRED & .94 & 67.2 &  61 & Requires \textsc{org} head; model assigns \textsc{loc}/\textsc{per} \\
18	participant of       & DocRED & .81 & 58.6 & 326 & Hallucinated \textsc{event} type; \textsc{per}$\leftrightarrow$event confusion \\
19	\textsc{Compare}     & SciERC & .53 & 42.4 &  66 & Cross-category pairs violate same-type constraint \\
20	\textsc{Feature-of}  & SciERC & .28 & 33.5 & 486 & Fuzzy Task/OtherScientificTerm boundary \\
21	\midrule
22	\multicolumn{6}{@{}l}{\textit{High $\kappa$ with zero violations (DR = 0\%)}} \\
23	lyrics by            & DocRED & .94 &  0.0 &   9 & Unambiguous \textsc{per}$\to$\textsc{misc}; creative roles rarely mistyped \\
24	place of birth       & DocRED & .92 &  0.0 & 157 & Unambiguous \textsc{per}$\to$\textsc{loc}; no type confusion \\
25	place of death       & DocRED & .89 &  0.0 &  60 & Strong \textsc{per}$\to$\textsc{loc} prior; mirrors place of birth \\
26	subsidiary           & DocRED & .86 &  0.0 &   5 & Clear \textsc{org}$\to$\textsc{org} corporate semantics \\
27	father               & DocRED & .81 &  0.0 &  69 & Clear \textsc{per}$\to$\textsc{per} kinship semantics \\
28	\bottomrule
29	\end{tabular}}
30	\caption{Per-relation $\kappa$ vs.\ DR violation rate (Qwen3-8B, zero-shot, unconstrained).
31	High $\kappa$ is necessary but not sufficient for high DR: relations with unambiguous entity types (place of birth, $\kappa{=}0.92$) have zero violations, while equally tight relations with confusable types (basin country, $\kappa{=}0.97$) show 74.6\% DR.}
32	\label{tab:kappa-case-study}
33	\end{table}
34	
35	\paragraph{Analysis.}
36	The case study confirms that violation susceptibility is driven by the interaction of constraint tightness and entity type confusability, not tightness alone.
37	Among DocRED relations with $\kappa \geq 0.81$, those involving semantically unambiguous type pairs (\textsc{per}$\to$\textsc{loc} for kinship/geographic relations) achieve DR${=}$0\%, while those requiring the model to distinguish frequently confused types (\textsc{loc} vs.\ \textsc{org}, \textsc{per} vs.\ \textsc{misc}) show DR${>}$50\%.
38	On SciERC, the highest-DR relation (\textsc{Compare}, 42.4\%) has only moderate $\kappa$ (0.53) but high type confusability across scientific categories.
39	This two-factor pattern motivates constrained decoding: the largest gains come from high-$\kappa$, confusable-type relations where the model's type uncertainty is channeled into valid pairs.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "e86bd0f7-8d68-4ba3-8eb0-63c93b4d314b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex",
      "content": "% Appendix: Constraint Tightness Case Study\n% Data source: case_study_kappa_dr_dddc01.md (Qwen-2.5-7B zero-shot unconstrained)\n\n\\section{Constraint Tightness Case Study}\n\\label{app:kappa-case-study}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccc l@{}}\n\\toprule\n\\textbf{Relation} & \\textbf{Dataset} & $\\kappa$ & \\textbf{DR\\%} & $n$ & \\textbf{Explanation} \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{Highest DR violation rate}} \\\\\nbasin country        & DocRED & .97 & 74.6 &  63 & Sole valid pair \\textsc{loc}$\\to$\\textsc{loc}; head mistyped as \\textsc{org}/\\textsc{misc} \\\\\nproduct produced     & DocRED & .94 & 67.2 &  61 & Requires \\textsc{org} head; model assigns \\textsc{loc}/\\textsc{per} \\\\\nparticipant of       & DocRED & .81 & 58.6 & 326 & Hallucinated \\textsc{event} type; \\textsc{per}$\\leftrightarrow$event confusion \\\\\n\\textsc{Compare}     & SciERC & .53 & 42.4 &  66 & Cross-category pairs violate same-type constraint \\\\\n\\textsc{Feature-of}  & SciERC & .28 & 33.5 & 486 & Fuzzy Task/OtherScientificTerm boundary \\\\\n\\midrule\n\\multicolumn{6}{@{}l}{\\textit{High $\\kappa$ with zero violations (DR = 0\\%)}} \\\\\nlyrics by            & DocRED & .94 &  0.0 &   9 & Unambiguous \\textsc{per}$\\to$\\textsc{misc}; creative roles rarely mistyped \\\\\nplace of birth       & DocRED & .92 &  0.0 & 157 & Unambiguous \\textsc{per}$\\to$\\textsc{loc}; no type confusion \\\\\nplace of death       & DocRED & .89 &  0.0 &  60 & Strong \\textsc{per}$\\to$\\textsc{loc} prior; mirrors place of birth \\\\\nsubsidiary           & DocRED & .86 &  0.0 &   5 & Clear \\textsc{org}$\\to$\\textsc{org} corporate semantics \\\\\nfather               & DocRED & .81 &  0.0 &  69 & Clear \\textsc{per}$\\to$\\textsc{per} kinship semantics \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-relation $\\kappa$ vs.\\ DR violation rate (Qwen3-8B, zero-shot, unconstrained).\nHigh $\\kappa$ is necessary but not sufficient for high DR: relations with unambiguous entity types (place of birth, $\\kappa{=}0.92$) have zero violations, while equally tight relations with confusable types (basin country, $\\kappa{=}0.97$) show 74.6\\% DR.}\n\\label{tab:kappa-case-study}\n\\end{table}\n\n\\paragraph{Analysis.}\nThe case study confirms that violation susceptibility is driven by the interaction of constraint tightness and entity type confusability, not tightness alone.\nAmong DocRED relations with $\\kappa \\geq 0.81$, those involving semantically unambiguous type pairs (\\textsc{per}$\\to$\\textsc{loc} for kinship/geographic relations) achieve DR${=}$0\\%, while those requiring the model to distinguish frequently confused types (\\textsc{loc} vs.\\ \\textsc{org}, \\textsc{per} vs.\\ \\textsc{misc}) show DR${>}$50\\%.\nOn SciERC, the highest-DR relation (\\textsc{Compare}, 42.4\\%) has only moderate $\\kappa$ (0.53) but high type confusability across scientific categories.\nThis two-factor pattern motivates constrained decoding: the largest gains come from high-$\\kappa$, confusable-type relations where the model's type uncertainty is channeled into valid pairs.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jmhv5uRBTrna3XRgbB4gde`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results && cat mcp-agent-ml-research-read_registry-1779533019341.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# List all experiment IDs\nfor exp in result:\n    print(exp.get('exp_id', 'NO_ID'))\n\" 2>/dev/null | head -100",
  "description": "List all experiment IDs from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "eb9b505c-c144-48e6-8d7a-9fcd0859e099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wt5oMfPGRoWmYcLmQ2sgML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10291,
      "cache_read_input_tokens": 62820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10291
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

_source line 58 · 2026-05-23T10:44:32.704Z_

<details><summary>↩ Tool result · `toolu_01Jmhv5uRBTrna3XRgbB4gde`</summary>

```text
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "92418ee7-be86-4b95-83ff-385a09319abc",
  "tool_use_result": {
    "stdout": "",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
The bash command didn't output anything. Let me try reading the registry file differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "0b674310-5191-400f-b1fc-a3b89dd26194",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQufvejCw7K2d9XVh3qjY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5148,
      "cache_read_input_tokens": 73111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5148
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

_source line 60_

Let me try a different approach to read the registry file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "174974bb-26de-4bbb-9d50-250e91c94b45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQufvejCw7K2d9XVh3qjY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5148,
      "cache_read_input_tokens": 73111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5148
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

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01HRJ21UQ3U5x1hAMtEEGQgj`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json, sys\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nfor exp in result:\n    eid = exp.get('exp_id', 'NO_ID')\n    print(eid)\n\" 2>&1 | head -150",
  "description": "List experiment IDs from registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "b3a197b3-f4cb-4adb-aa0b-0ba135043848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQufvejCw7K2d9XVh3qjY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5148,
      "cache_read_input_tokens": 73111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5148
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

_source line 62 · 2026-05-23T10:44:40.465Z_

<details><summary>↩ Tool result · `toolu_01HRJ21UQ3U5x1hAMtEEGQgj`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = exp.get('exp_id', 'NO_ID')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "4c2add4a-e707-4818-a04f-3b1d3b264b1c",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 7, in &lt;module>\n    eid = exp.get('exp_id', 'NO_ID')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01GZPdXdmsEPMbpTS1BgPZ9v`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint(type(result))\nif isinstance(result, list):\n    print('len:', len(result))\n    print('first item type:', type(result[0]))\n    print('first item:', result[0][:200] if isinstance(result[0], str) else json.dumps(result[0])[:200])\nelif isinstance(result, dict):\n    print('keys:', list(result.keys())[:20])\n\" 2>&1",
  "description": "Inspect registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "148b9541-5c02-4ca7-ba34-b9b8054b934b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tfn9jStHG6R6AzngZb9Crh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 380,
      "cache_read_input_tokens": 78259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 380
      },
      "output_tokens": 73,
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

_source line 64 · 2026-05-23T10:44:49.176Z_

<details><summary>↩ Tool result · `toolu_01GZPdXdmsEPMbpTS1BgPZ9v`</summary>

```text
&lt;class 'dict'>
keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "58b60481-7baf-4233-b515-942bae0b0c17",
  "tool_use_result": {
    "stdout": "&lt;class 'dict'>\nkeys: ['success', 'data', 'error', 'metadata']",
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_013piDiTjQTN2tWmbwn71MfG`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']\nprint('Total experiments:', len(exps))\nfor exp in exps:\n    print(exp.get('exp_id', 'NO_ID'))\n\" 2>&1 | head -200",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "bd7b73c5-a744-45b5-890a-9bbafee9bcfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcggRfexHgDobtwenxeRis",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 78639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 350
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

_source line 66 · 2026-05-23T10:44:53.217Z_

<details><summary>↩ Tool result · `toolu_013piDiTjQTN2tWmbwn71MfG`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    print(exp.get('exp_id', 'NO_ID'))
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3b7b9b04-974b-4778-a535-f8ead94f5f95",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    print(exp.get('exp_id', 'NO_ID'))\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 4",
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

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01MnvLJsmSzijSs6miTTgA1L`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nfor k in result:\n    v = result[k]\n    print(f'{k}: type={type(v).__name__}, len={len(v) if hasattr(v, \\\"__len__\\\") else \\\"N/A\\\"}')\n    if isinstance(v, str):\n        print(f'  preview: {v[:200]}')\n    elif isinstance(v, list):\n        print(f'  first item type: {type(v[0]).__name__ if v else \\\"empty\\\"}')\n        if v and isinstance(v[0], str):\n            print(f'  first: {v[0][:200]}')\n\" 2>&1",
  "description": "Inspect registry structure details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "a1f7ee81-daf3-4244-b2f3-c4578567c335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bp7WAC6bncFbceeyXneHrg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 78989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

_source line 68 · 2026-05-23T10:44:58.333Z_

<details><summary>↩ Tool result · `toolu_01MnvLJsmSzijSs6miTTgA1L`</summary>

```text
success: type=bool, len=N/A
data: type=dict, len=4
error: type=NoneType, len=N/A
metadata: type=dict, len=1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "42447321-fc5b-4489-bd3b-148ae06f949c",
  "tool_use_result": {
    "stdout": "success: type=bool, len=N/A\ndata: type=dict, len=4\nerror: type=NoneType, len=N/A\nmetadata: type=dict, len=1",
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

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01FcKw4Aymziqm9rpUZgk4yS`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nd = result['data']\nfor k in d:\n    v = d[k]\n    print(f'{k}: type={type(v).__name__}')\n    if isinstance(v, list):\n        print(f'  len={len(v)}')\n        if v:\n            print(f'  first item type: {type(v[0]).__name__}')\n            if isinstance(v[0], dict):\n                print(f'  first item keys: {list(v[0].keys())[:10]}')\n                print(f'  first exp_id: {v[0].get(\\\"exp_id\\\", \\\"NO_ID\\\")}')\n\" 2>&1",
  "description": "Explore registry data dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "18229f1c-9858-40a3-94b2-90b27ae967a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hyPzU1XW7stfgTBV18qPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 79337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
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

_source line 70 · 2026-05-23T10:45:05.843Z_

<details><summary>↩ Tool result · `toolu_01FcKw4Aymziqm9rpUZgk4yS`</summary>

```text
experiments: type=dict
count: type=int
total: type=int
baseline: type=NoneType
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "f2f95007-6e4f-4ce3-827e-7c6db42479d7",
  "tool_use_result": {
    "stdout": "experiments: type=dict\ncount: type=int\ntotal: type=int\nbaseline: type=NoneType",
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01HaPPkdUw4fZeYP2wvwZa2c`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Type: {type(exps).__name__}')\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print(f'Count: {len(keys)}')\n    for k in keys:\n        print(k)\n\" 2>&1",
  "description": "List experiment IDs from registry experiments dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "23b47c24-3aa9-404e-8c86-ff3e728311ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vi1uXgFAJgqH76RXhEXJfC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 79762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 413
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

_source line 72 · 2026-05-23T10:45:09.877Z_

<details><summary>↩ Tool result · `toolu_01HaPPkdUw4fZeYP2wvwZa2c`</summary>

```text
Type: dict
Count: 164
eval_70b_lora_docred_200_full_s2
sf2_qwen_int4_docred_s1
sf2_llama_int4_docred_s1
sf2_70b_prompt_sensitivity
sf2_llama_int4_scierc_s1
sf2_qwen_int4_scierc_s1
sf2_gollie_scierc_violation
eval_70b_zs_docred_200_full_s1
eval_70b_lora_docred_200_grammar_only
eval_70b_lora_docred_200_semantic_only
eval_70b_zs_docred_200_unconstrained
eval_70b_zs_docred_200_grammar_only
eval_70b_zs_docred_200_semantic_only
eval_70b_lora_docred_200_beam4_s1
eval_70b_lora_scierc_grammar_only
eval_70b_zs_scierc_unconstrained
eval_70b_lora_scierc_full_s2
eval_70b_lora_scierc_semantic_only
entity_order_ablation_qwen_scierc
eval_70b_zs_scierc_semantic_only
eval_70b_zs_scierc_grammar_only
eval_70b_lora_scierc_beam4_s1
tcr_beam4_llama_scierc
tcr_beam4_qwen_scierc
vllm_guided_json_scierc_zs
eval_70b_lora_docred_200_s1_constrained
d066_beam_sweep
w8_llama_docred_ft_grammar_only
w8_llama_docred_ft_semantic_only
w8_qwen_docred_ft_semantic_only
r16_trie_qwen_ft_scierc
r16_trie_llama_ft_scierc
eval_70b_lora_docred_200_unconstrained
eval_70b_lora_scierc_s1_constrained
eval_70b_lora_scierc_unconstrained
r16_70b_docred_zs_s1
d066_sweep_llama_beam8_unc
d066_sweep_llama_beam2_s1
d066_sweep_llama_docred_beam4_s1
r16_70b_lora_scierc_eval
r16_70b_lora_docred
r16_70b_lora_scierc
r16_70b_scierc_zs_s1
r14_qwen_docred_beam4_998
r16_trie_llama_zs_scierc
r16_trie_qwen_zs_scierc
r14_llama_docred_beam4_998
d066_sweep_llama_scierc_beam8_s1_551
d066_sweep_llama_scierc_beam4_s1_551
d066_sweep_llama_docred_beam4_unc
d066_sweep_llama_docred_beam1_s1
d066_sweep_llama_beam8_s1
d065_qwen_greedy_4096_r2
d066_sweep_llama_scierc_beam2_s1_551
d066_sweep_llama_scierc_beam1_unc
d066_sweep_llama_docred_beam1_unc
d066_sweep_21461_gpu1
w5_llama_docred_lora_constrained_eval
d066_sweep_16980_gpu1
d065_qwen_greedy_4096
d066_docred_beam_sweep
d067_seed_variance
d068_constraint_guided_beam_pilot
d064_docred_full_beam
d065_tcr_full
d065_tcr_pilot
d063_gollie_violation_rate
d062_full_ft_scierc
d062_beam_latency
d062_ontology_scalability
d062_cf_majority_voting
p1_ee_ft_llama_r2
p1_ee_ft_composability_r5
p1_ee_ft_llama
p1_ee_ft_composability_r4
p1_llama_ee_ft
w9_qwen_docred_zs_sampling_r2
70b_docred_constrained
70b_docred_unconstrained
p1_ee_ft_composability_r3
p1_ee_ft_composability_r2
p1_ee_ft_composability
p8c_ft_scierc_latency
p8b_docred_latency
w9_qwen_docred_zs_sampling
w9_qwen_scierc_zs_sampling
p8_latency_overhead
q1_llama_lora_scierc_beam4
70b_scierc_unconstrained
70b_scierc_constrained
ee_mistral_wikievents_grammar_only_v3
ee_mistral_wikievents_constrained_v3
ee_llama_wikievents_constrained_v3
ee_qwen_wikievents_constrained_v3
ee_mistral_wikievents_constrained_v2
ee_qwen_wikievents_constrained
ee_mistral_wikievents_constrained
ee_llama_wikievents_constrained
ee_mistral_wikievents_unconstrained
ee_llama_wikievents_unconstrained
ee_qwen_wikievents_unconstrained
r4_prompt_detailed
r4_prompt_minimal
w10_qwen_scierc_ft_beam_4
w10_beam_ablation_k8
w9_mistral_docred_beam_50
w10_beam_ablation_k2
w10_mistral_scierc_beam_551
w10_llama_docred_beam_50
w10_type_consensus_docred_50
w10_type_consensus_prototype
w9_qwen_scierc_stability_3seeds
w9_qwen_docred_beam_50
w9_llama_scierc_beam_551
posthoc_filtering_baseline
phase2_scierc_full_s2
llama_docred_unconstrained_mt6144
llama_docred_full_s1_mt6144
beam_search_scierc_full_551
w7_llama_scierc_ft_semantic_only
w7_llama_scierc_ft_grammar_only
w7_qwen_scierc_ft_semantic_only
w7_qwen_scierc_ft_grammar_only
w5_llama_lora_scierc_unconstrained_eval
w5_llama_lora_scierc_constrained_eval
w5_lora_scierc_constrained_eval
w1_cf_fallback_scierc_pilot
w5_lora_scierc_training
w8_qwen_docred_ft_grammar_only
w6_mistral_scierc_unconstrained
w6_mistral_scierc_constrained
w8_ft_posthoc_baseline
w6_mistral_docred_unconstrained
w6_mistral_docred_constrained
w5_qwen_docred_lora_constrained_eval
w5_llama_docred_sft_data_gen
w1_cf_fallback_llama_docred
w1_cf_fallback_llama_scierc
w5_qwen_docred_lora_unconstrained_eval
w5_llama_docred_lora_unconstrained_eval
w5_qwen_docred_lora_training
w5_llama_docred_lora_training
w5_docred_sft_data_gen
w5_llama_lora_scierc_training
w1_cf_fallback_docred
w5_lora_scierc_unconstrained_eval
llama_docred_full_s1
llama_docred_unconstrained
phase2_docred_grammar_only
llama_scierc_full_s1
llama_scierc_unconstrained
phase2_scierc_full_s1
phase2_scierc_semantic_only
phase2_scierc_grammar_only
phase2_scierc_unconstrained
phase2_docred_full_s1
phase2_docred_semantic_only
phase2_docred_unconstrained
mvp_phase0_docred_schema_r2
phase2_s2_pilot50
mvp_phase0_docred_schema
mvp_phase0_violation_rate_docred
mvp_phase0_scierc_schema
mvp_phase0_violation_rate
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "c0978eca-f15a-449f-9890-cf343745b6ae",
  "tool_use_result": {
    "stdout": "Type: dict\nCount: 164\neval_70b_lora_docred_200_full_s2\nsf2_qwen_int4_docred_s1\nsf2_llama_int4_docred_s1\nsf2_70b_prompt_sensitivity\nsf2_llama_int4_scierc_s1\nsf2_qwen_int4_scierc_s1\nsf2_gollie_scierc_violation\neval_70b_zs_docred_200_full_s1\neval_70b_lora_docred_200_grammar_only\neval_70b_lora_docred_200_semantic_only\neval_70b_zs_docred_200_unconstrained\neval_70b_zs_docred_200_grammar_only\neval_70b_zs_docred_200_semantic_only\neval_70b_lora_docred_200_beam4_s1\neval_70b_lora_scierc_grammar_only\neval_70b_zs_scierc_unconstrained\neval_70b_lora_scierc_full_s2\neval_70b_lora_scierc_semantic_only\nentity_order_ablation_qwen_scierc\neval_70b_zs_scierc_semantic_only\neval_70b_zs_scierc_grammar_only\neval_70b_lora_scierc_beam4_s1\ntcr_beam4_llama_scierc\ntcr_beam4_qwen_scierc\nvllm_guided_json_scierc_zs\neval_70b_lora_docred_200_s1_constrained\nd066_beam_sweep\nw8_llama_docred_ft_grammar_only\nw8_llama_docred_ft_semantic_only\nw8_qwen_docred_ft_semantic_only\nr16_trie_qwen_ft_scierc\nr16_trie_llama_ft_scierc\neval_70b_lora_docred_200_unconstrained\neval_70b_lora_scierc_s1_constrained\neval_70b_lora_scierc_unconstrained\nr16_70b_docred_zs_s1\nd066_sweep_llama_beam8_unc\nd066_sweep_llama_beam2_s1\nd066_sweep_llama_docred_beam4_s1\nr16_70b_lora_scierc_eval\nr16_70b_lora_docred\nr16_70b_lora_scierc\nr16_70b_scierc_zs_s1\nr14_qwen_docred_beam4_998\nr16_trie_llama_zs_scierc\nr16_trie_qwen_zs_scierc\nr14_llama_docred_beam4_998\nd066_sweep_llama_scierc_beam8_s1_551\nd066_sweep_llama_scierc_beam4_s1_551\nd066_sweep_llama_docred_beam4_unc\nd066_sweep_llama_docred_beam1_s1\nd066_sweep_llama_beam8_s1\nd065_qwen_greedy_4096_r2\nd066_sweep_llama_scierc_beam2_s1_551\nd066_sweep_llama_scierc_beam1_unc\nd066_sweep_llama_docred_beam1_unc\nd066_sweep_21461_gpu1\nw5_llama_docred_lora_constrained_eval\nd066_sweep_16980_gpu1\nd065_qwen_greedy_4096\nd066_docred_beam_sweep\nd067_seed_variance\nd068_constraint_guided_beam_pilot\nd064_docred_full_beam\nd065_tcr_full\nd065_tcr_pilot\nd063_gollie_violation_rate\nd062_full_ft_scierc\nd062_beam_latency\nd062_ontology_scalability\nd062_cf_majority_voting\np1_ee_ft_llama_r2\np1_ee_ft_composability_r5\np1_ee_ft_llama\np1_ee_ft_composability_r4\np1_llama_ee_ft\nw9_qwen_docred_zs_sampling_r2\n70b_docred_constrained\n70b_docred_unconstrained\np1_ee_ft_composability_r3\np1_ee_ft_composability_r2\np1_ee_ft_composability\np8c_ft_scierc_latency\np8b_docred_latency\nw9_qwen_docred_zs_sampling\nw9_qwen_scierc_zs_sampling\np8_latency_overhead\nq1_llama_lora_scierc_beam4\n70b_scierc_unconstrained\n70b_scierc_constrained\nee_mistral_wikievents_grammar_only_v3\nee_mistral_wikievents_constrained_v3\nee_llama_wikievents_constrained_v3\nee_qwen_wikievents_constrained_v3\nee_mistral_wikievents_constrained_v2\nee_qwen_wikievents_constrained\nee_mistral_wikievents_constrained\nee_llama_wikievents_constrained\nee_mistral_wikievents_unconstrained\nee_llama_wikievents_unconstrained\nee_qwen_wikievents_unconstrained\nr4_prompt_detailed\nr4_prompt_minimal\nw10_qwen_scierc_ft_beam_4\nw10_beam_ablation_k8\nw9_mistral_docred_beam_50\nw10_beam_ablation_k2\nw10_mistral_scierc_beam_551\nw10_llama_docred_beam_50\nw10_type_consensus_docred_50\nw10_type_consensus_prototype\nw9_qwen_scierc_stability_3seeds\nw9_qwen_docred_beam_50\nw9_llama_scierc_beam_551\nposthoc_filtering_baseline\nphase2_scierc_full_s2\nllama_docred_unconstrained_mt6144\nllama_docred_full_s1_mt6144\nbeam_search_scierc_full_551\nw7_llama_scierc_ft_semantic_only\nw7_llama_scierc_ft_grammar_only\nw7_qwen_scierc_ft_semantic_only\nw7_qwen_scierc_ft_grammar_only\nw5_llama_lora_scierc_unconstrained_eval\nw5_llama_lora_scierc_constrained_eval\nw5_lora_scierc_constrained_eval\nw1_cf_fallback_scierc_pilot\nw5_lora_scierc_training\nw8_qwen_docred_ft_grammar_only\nw6_mistral_scierc_unconstrained\nw6_mistral_scierc_constrained\nw8_ft_posthoc_baseline\nw6_mistral_docred_unconstrained\nw6_mistral_docred_constrained\nw5_qwen_docred_lora_constrained_eval\nw5_llama_docred_sft_data_gen\nw1_cf_fallback_llama_docred\nw1_cf_fallback_llama_scierc\nw5_qwen_docred_lora_unconstrained_eval\nw5_llama_docred_lora_unconstrained_eval\nw5_qwen_docred_lora_training\nw5_llama_docred_lora_training\nw5_docred_sft_data_gen\nw5_llama_lora_scierc_training\nw1_cf_fallback_docred\nw5_lora_scierc_unconstrained_eval\nllama_docred_full_s1\nllama_docred_unconstrained\nphase2_docred_grammar_only\nllama_scierc_full_s1\nllama_scierc_unconstrained\nphase2_scierc_full_s1\nphase2_scierc_semantic_only\nphase2_scierc_grammar_only\nphase2_scierc_unconstrained\nphase2_docred_full_s1\nphase2_docred_semantic_only\nphase2_docred_unconstrained\nmvp_phase0_docred_schema_r2\nphase2_s2_pilot50\nmvp_phase0_docred_schema\nmvp_phase0_violation_rate_docred\nmvp_phase0_scierc_schema\nmvp_phase0_violation_rate",
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

_source line 73_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 164 experiment IDs. I need to query specific experiments to verify the numbers in the appendix tables. Given the large number of tables and experiments, let me use a systematic approach.

Let me create a comprehensive script that extracts metrics from the registry for all relevant experiments, then compare them against the paper values.

Let me query the registry for the specific experiments mentioned in the appendix files. I'll do this in batches using the MCP tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "f96e0ee7-3078-4da3-bb8c-0814c49746e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTJCzaedc8KGwSR2F9SC12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 80175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2542
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

_source line 74_

Good, I have 164 experiments in the registry. Now let me systematically extract metrics for all experiments referenced in the appendix tables. I'll use targeted registry queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "154334a8-0952-42e6-b0b2-ddc6ccb0e94d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTJCzaedc8KGwSR2F9SC12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 80175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2542
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

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_011DDVqMiVSmzU7nxU9EU6pp`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 << 'PYEOF'\nimport json\n\nwith open(\"$REGFILE\") as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Key experiments for quantization table\nquant_ids = [\n    'sf2_qwen_int4_scierc_s1', 'sf2_llama_int4_scierc_s1',\n    'sf2_qwen_int4_docred_s1', 'sf2_llama_int4_docred_s1',\n    'd065_qwen_greedy_4096_r2', 'd066_sweep_llama_docred_beam1_s1',\n    'entity_order_ablation_qwen_scierc'\n]\n\nfor eid in quant_ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f\"\\n=== {eid} ===\")\n        metrics = exp.get('metrics', {})\n        if isinstance(metrics, str):\n            try:\n                metrics = json.loads(metrics)\n            except:\n                pass\n        print(json.dumps(metrics, indent=2)[:1500])\n    else:\n        print(f\"\\n=== {eid} === NOT FOUND\")\nPYEOF",
  "description": "Extract quantization experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "2128a8b5-43d5-4598-bb2f-f924b69ce32b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTJCzaedc8KGwSR2F9SC12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 80175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2542
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

_source line 76 · 2026-05-23T10:45:26.504Z_

<details><summary>↩ Tool result · reported error · `toolu_011DDVqMiVSmzU7nxU9EU6pp`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
FileNotFoundError: [Errno 2] No such file or directory: '$REGFILE'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "caf543d2-ea8c-48a1-a2b0-bc716ae0bd04",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\nFileNotFoundError: [Errno 2] No such file or directory: '$REGFILE'"
}
```

</details>

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01XMotKSbPftqauvjbXtS8Xb`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\nquant_ids = [\n    'sf2_qwen_int4_scierc_s1', 'sf2_llama_int4_scierc_s1',\n    'sf2_qwen_int4_docred_s1', 'sf2_llama_int4_docred_s1',\n    'd065_qwen_greedy_4096_r2', 'd066_sweep_llama_docred_beam1_s1',\n    'entity_order_ablation_qwen_scierc'\n]\n\nfor eid in quant_ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        print(json.dumps(metrics, indent=2)[:2000])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\"",
  "description": "Extract quantization experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "a8c8e381-e1c7-4b72-8760-9b54b3d994ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DEmonpesfj53TXd7gm7RY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 82717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 78 · 2026-05-23T10:45:31.538Z_

<details><summary>↩ Tool result · `toolu_01XMotKSbPftqauvjbXtS8Xb`</summary>

```text
=== sf2_qwen_int4_scierc_s1 ===
{
  "DR%": 0,
  "RV%": 0,
  "ET%": 0,
  "CF%": 1.1,
  "R-F1": 41.71,
  "E-F1": 67.05,
  "samples": 551,
  "R-P": 38.52,
  "R-R": 45.48,
  "E-P": 64.76,
  "E-R": 69.52
}

=== sf2_llama_int4_scierc_s1 ===
{
  "DR%": 0,
  "RV%": 0,
  "ET%": 0,
  "CF%": 0.94,
  "R-F1": 43.98,
  "E-F1": 67.54,
  "samples": 551,
  "R-P": 40.47,
  "R-R": 48.15,
  "E-P": 65.51,
  "E-R": 69.7
}

=== sf2_qwen_int4_docred_s1 ===
{
  "total_samples": 200,
  "parse_failures": 37,
  "parse_fail_pct": 18.5,
  "total_entities_pred": 2985,
  "total_relations_pred": 2385,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.1,
  "E_P": 84.87,
  "E_R": 66.93,
  "E_F1": 74.84,
  "R_P": 41.59,
  "R_R": 38.65,
  "R_F1": 40.07,
  "et_violations": 0,
  "rv_violations": 0,
  "dr_violations": 0,
  "cf_violations": 3
}

=== sf2_llama_int4_docred_s1 ===
{
  "DR%": 0,
  "RV%": 0,
  "ET%": 0,
  "CF%": 0.22,
  "R-F1": 48.04,
  "E-F1": 84.18,
  "R-P": 44.79,
  "R-R": 51.8,
  "E-P": 85.5,
  "E-R": 82.9,
  "samples": 200,
  "parse_fail": 5,
  "parse_fail_pct": 2.5,
  "entities_pred": 3669,
  "relations_pred": 2997
}

=== d065_qwen_greedy_4096_r2 ===
{
  "E-F1": 81.87,
  "R-F1": 40.79,
  "DR_pct": 0,
  "CF_pct": 0.22,
  "ET_pct": 0,
  "RV_pct": 0,
  "PF_pct": 8.52,
  "samples": 998
}

=== d066_sweep_llama_docred_beam1_s1 ===
{
  "E-F1": 85.43,
  "R-F1": 47.35,
  "DR_pct": 0,
  "CF_pct": 0.19,
  "PF_pct": 2,
  "samples": 200
}

=== entity_order_ablation_qwen_scierc ===
{
  "E_F1": 67.05,
  "E_P": 65.23,
  "E_R": 68.98,
  "R_F1": 43.77,
  "R_P": 40.78,
  "R_R": 47.23,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_count": 21,
  "parse_fail_pct": 0,
  "samples": 551,
  "entities": 1784,
  "relations": 1128,
  "corrected_original_R_F1": 43.77,
  "corrected_original_E_F1": 67.05,
  "corrected_original_DR_pct": 0,
  "corrected_original_CF_count": 21,
  "corrected_delta_R_F1": 0,
  "corrected_delta_E_F1": 0,
  "raw_output_identical": true,
  "parsed_output_identical": true,
  "note": "CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "237053f7-3be9-4865-8ea2-b69e5de1b740",
  "tool_use_result": {
    "stdout": "=== sf2_qwen_int4_scierc_s1 ===\n{\n  \"DR%\": 0,\n  \"RV%\": 0,\n  \"ET%\": 0,\n  \"CF%\": 1.1,\n  \"R-F1\": 41.71,\n  \"E-F1\": 67.05,\n  \"samples\": 551,\n  \"R-P\": 38.52,\n  \"R-R\": 45.48,\n  \"E-P\": 64.76,\n  \"E-R\": 69.52\n}\n\n=== sf2_llama_int4_scierc_s1 ===\n{\n  \"DR%\": 0,\n  \"RV%\": 0,\n  \"ET%\": 0,\n  \"CF%\": 0.94,\n  \"R-F1\": 43.98,\n  \"E-F1\": 67.54,\n  \"samples\": 551,\n  \"R-P\": 40.47,\n  \"R-R\": 48.15,\n  \"E-P\": 65.51,\n  \"E-R\": 69.7\n}\n\n=== sf2_qwen_int4_docred_s1 ===\n{\n  \"total_samples\": 200,\n  \"parse_failures\": 37,\n  \"parse_fail_pct\": 18.5,\n  \"total_entities_pred\": 2985,\n  \"total_relations_pred\": 2385,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.1,\n  \"E_P\": 84.87,\n  \"E_R\": 66.93,\n  \"E_F1\": 74.84,\n  \"R_P\": 41.59,\n  \"R_R\": 38.65,\n  \"R_F1\": 40.07,\n  \"et_violations\": 0,\n  \"rv_violations\": 0,\n  \"dr_violations\": 0,\n  \"cf_violations\": 3\n}\n\n=== sf2_llama_int4_docred_s1 ===\n{\n  \"DR%\": 0,\n  \"RV%\": 0,\n  \"ET%\": 0,\n  \"CF%\": 0.22,\n  \"R-F1\": 48.04,\n  \"E-F1\": 84.18,\n  \"R-P\": 44.79,\n  \"R-R\": 51.8,\n  \"E-P\": 85.5,\n  \"E-R\": 82.9,\n  \"samples\": 200,\n  \"parse_fail\": 5,\n  \"parse_fail_pct\": 2.5,\n  \"entities_pred\": 3669,\n  \"relations_pred\": 2997\n}\n\n=== d065_qwen_greedy_4096_r2 ===\n{\n  \"E-F1\": 81.87,\n  \"R-F1\": 40.79,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.22,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"PF_pct\": 8.52,\n  \"samples\": 998\n}\n\n=== d066_sweep_llama_docred_beam1_s1 ===\n{\n  \"E-F1\": 85.43,\n  \"R-F1\": 47.35,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.19,\n  \"PF_pct\": 2,\n  \"samples\": 200\n}\n\n=== entity_order_ablation_qwen_scierc ===\n{\n  \"E_F1\": 67.05,\n  \"E_P\": 65.23,\n  \"E_R\": 68.98,\n  \"R_F1\": 43.77,\n  \"R_P\": 40.78,\n  \"R_R\": 47.23,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_count\": 21,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551,\n  \"entities\": 1784,\n  \"relations\": 1128,\n  \"corrected_original_R_F1\": 43.77,\n  \"corrected_original_E_F1\": 67.05,\n  \"corrected_original_DR_pct\": 0,\n  \"corrected_original_CF_count\": 21,\n  \"corrected_delta_R_F1\": 0,\n  \"corrected_delta_E_F1\": 0,\n  \"raw_output_identical\": true,\n  \"parsed_output_identical\": true,\n  \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"\n}",
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

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Good, I'm getting the registry data. Let me now systematically verify all the appendix tables. Let me continue querying for the remaining experiment sets. I'll do this in parallel batches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ce9edddb-49b2-47bc-b1b1-c346df019097",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Voq6ejX5grBHX3YV689mSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1897,
      "cache_read_input_tokens": 83438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1897
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

_source line 80_

Good, the quantization data is coming through. Let me now query the remaining experiment sets in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "a427e725-cf52-4e19-8a80-b5e514bab275",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Voq6ejX5grBHX3YV689mSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1897,
      "cache_read_input_tokens": 83438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1897
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

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01W19spjs4ovKJ7FCBHPxigW`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# 70B ablation experiments\nids_70b = [\n    'eval_70b_lora_scierc_unconstrained', 'eval_70b_lora_scierc_grammar_only',\n    'eval_70b_lora_scierc_semantic_only', 'eval_70b_lora_scierc_s1_constrained',\n    'eval_70b_lora_scierc_full_s2', 'eval_70b_lora_scierc_beam4_s1',\n    'eval_70b_lora_docred_200_unconstrained', 'eval_70b_lora_docred_200_grammar_only',\n    'eval_70b_lora_docred_200_semantic_only', 'eval_70b_lora_docred_200_s1_constrained',\n    'eval_70b_lora_docred_200_full_s2', 'eval_70b_lora_docred_200_beam4_s1',\n    'r16_70b_docred_zs_unconstrained', 'r16_70b_docred_zs_grammar_only',\n    'r16_70b_docred_zs_semantic_only', 'r16_70b_docred_zs_s1',\n    'eval_70b_zs_scierc_unconstrained', 'eval_70b_zs_scierc_grammar_only',\n    'eval_70b_zs_scierc_semantic_only',\n    'eval_70b_zs_docred_200_unconstrained', 'eval_70b_zs_docred_200_grammar_only',\n    'eval_70b_zs_docred_200_semantic_only', 'eval_70b_zs_docred_200_full_s1',\n]\n\nfor eid in ids_70b:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        print(json.dumps(metrics, indent=2)[:1500])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\"",
  "description": "Extract 70B ablation experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "0f07867c-8f8c-4d2a-9623-ea7669861837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Voq6ejX5grBHX3YV689mSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1897,
      "cache_read_input_tokens": 83438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1897
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

_source line 82 · 2026-05-23T10:45:47.407Z_

<details><summary>↩ Tool result · `toolu_01W19spjs4ovKJ7FCBHPxigW`</summary>

```text
=== eval_70b_lora_scierc_unconstrained ===
{
  "E_F1": 64.86,
  "E_P": 62.74,
  "E_R": 67.12,
  "R_F1": 44.73,
  "R_P": 41.61,
  "R_R": 48.36,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 1.5,
  "CF_pct": 0,
  "parse_fail_pct": 0,
  "samples": 551,
  "entities": 1806,
  "relations": 1133
}

=== eval_70b_lora_scierc_grammar_only ===
{
  "samples": 551,
  "json_failures": 0,
  "json_failure_rate": 0,
  "entities": 1805,
  "relations": 1133,
  "entity_type_violations": 0,
  "entity_type_violation_rate": 0,
  "relation_vocab_violations": 0,
  "relation_vocab_violation_rate": 0,
  "domain_range_violations": 17,
  "domain_range_violation_rate": 0.015,
  "cross_field_consistency_violations": 0,
  "fuzzy_relation_matches": 0,
  "entity_P": 0.6272,
  "entity_R": 0.6707,
  "entity_F1": 0.6482,
  "relation_P": 0.4152,
  "relation_R": 0.4825,
  "relation_F1": 0.4463
}

=== eval_70b_lora_scierc_semantic_only ===
{
  "samples": 551,
  "json_failures": 0,
  "entities": 1806,
  "relations": 1133,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.6,
  "CF_count": 9,
  "E_F1": 64.86,
  "E_P": 62.74,
  "E_R": 67.12,
  "R_F1": 44.73,
  "R_P": 41.61,
  "R_R": 48.36,
  "parse_fail_pct": 0
}

=== eval_70b_lora_scierc_s1_constrained ===
{
  "entity_f1": 0.6476,
  "entity_precision": 0.6266,
  "entity_recall": 0.6701,
  "relation_f1": 0.4453,
  "relation_precision": 0.4149,
  "relation_recall": 0.4805,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_count": 15,
  "parse_fail_pct": 0,
  "fuzzy_matches": 0,
  "num_samples": 551,
  "num_entities": 1805,
  "num_relations": 1129
}

=== eval_70b_lora_scierc_full_s2 ===
{
  "samples": 551,
  "json_failures": 0,
  "entities": 1531,
  "relations": 1027,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_count": 18,
  "E_F1": 62.35,
  "E_P": 65.44,
  "E_R": 59.53,
  "R_F1": 36.28,
  "R_P": 35.35,
  "R_R": 37.27,
  "parse_fail_pct": 0
}

=== eval_70b_lora_scierc_beam4_s1 ===
{
  "E_F1": 64.89,
  "E_P": 62.29,
  "E_R": 67.72,
  "R_F1": 44.81,
  "R_P": 39.45,
  "R_R": 51.85,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_count": 1,
  "parse_fail_pct": 0,
  "samples": 551,
  "entities": 1839,
  "relations": 1283
}

=== eval_70b_lora_docred_200_unconstrained ===
{
  "E_F1": 80.34,
  "E_P": 85.13,
  "E_R": 76.05,
  "R_F1": 43.8,
  "R_P": 39.6,
  "R_R": 48.99,
  "ET_pct": 0,
  "RV_pct": 0.57,
  "DR_pct": 0.22,
  "CF_pct": 0.06,
  "parse_fail_pct": 10,
  "samples": 200,
  "relations": 3159,
  "RV_count": 18,
  "DR_count": 7,
  "CF_count": 2
}

=== eval_70b_lora_docred_200_grammar_only ===
{
  "samples": 200,
  "parse_fail_pct": 10.5,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.38,
  "CF_pct": 0.06,
  "E_F1": 80.13,
  "E_P": 85.16,
  "E_R": 75.66,
  "R_F1": 43.96,
  "R_P": 39.78,
  "R_R": 49.11,
  "entities_pred": 3362,
  "relations_pred": 3154
}

=== eval_70b_lora_docred_200_semantic_only ===
{
  "samples": 200,
  "parse_fail_pct": 11,
  "ET_pct": 0,
  "RV_pct": 0.51,
  "DR_pct": 0,
  "CF_pct": 0.21,
  "E_F1": 80.06,
  "E_P": 85.21,
  "E_R": 75.5,
  "R_F1": 43.61,
  "R_P": 39.44,
  "R_R": 48.75,
  "entities_pred": 3351,
  "relations_pred": 3148
}

=== eval_70b_lora_docred_200_s1_constrained ===
{
  "E_F1": 79.38,
  "E_P": 85.24,
  "E_R": 74.28,
  "R_F1": 43.95,
  "R_P": 40.48,
  "R_R": 48.08,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_pct": 0.18,
  "parse_fail_pct": 12.5,
  "samples": 200
}

=== eval_70b_lora_docred_200_full_s2 ===
{
  "R_F1": 36.45,
  "R_P": 31.25,
  "R_R": 43.72,
  "E_F1": 84.96,
  "E_P": 84.6,
  "E_R": 85.34,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_count": 13,
  "CF_pct": 0.34,
  "parse_fail_pct": 0,
  "pred_entities": 3819,
  "pred_relations": 3546,
  "entity_tp": 3218,
  "entity_fp": 586,
  "entity_fn": 553,
  "relation_tp": 1104,
  "relation_fp": 2429,
  "relation_fn": 1421
}

=== eval_70b_lora_docred_200_beam4_s1 ===
{
  "E-F1": 85.57,
  "E-P": 85.45,
  "E-R": 85.68,
  "R-F1": 48.14,
  "R-P": 44.24,
  "R-R": 52.79,
  "ET%": 0,
  "RV%": 0,
  "DR%": 0,
  "CF%": 0,
  "parse_fail": "1/200 (0.5%)",
  "entities_pred": 3790,
  "relations_pred": 3030
}

=== r16_70b_docred_zs_unconstrained === NOT FOUND

=== r16_70b_docred_zs_grammar_only === NOT FOUND

=== r16_70b_docred_zs_semantic_only === NOT FOUND

=== r16_70b_docred_zs_s1 ===
{
  "E_F1": 69.11,
  "R_F1": 13.05,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_pct": 0.04,
  "parse_fail_pct": 0.1,
  "samples": 998,
  "total_entities": 16599,
  "total_triples": 13239,
  "baseline_unc_DR_pct": 14.98,
  "baseline_unc_R_F1": 13.01,
  "note": "Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch."
}

=== eval_70b_zs_scierc_unconstrained ===
{
  "samples": 551,
  "json_failures": 0,
  "entities": 2353,
  "relations": 1483,
  "ET_pct": 0,
  "RV_pct": 0.6,
  "DR_pct": 6.4,
  "CF_count": 0,
  "E_F1": 35.22,
  "E_P": 30.13,
  "E_R": 42.38,
  "R_F1": 11.23,
  "R_P": 9.31,
  "R_R": 14.17,
  "parse_fail_pct": 0
}

=== eval_70b_zs_scierc_grammar_only ===
{
  "R_F1": 11.23,
  "DR_pct": 6.33,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_count": 0,
  "samples": 551
}

=== eval_70b_zs_scierc_semantic_only ===
{
  "R_F1": 11.37,
  "DR_pct": 1.01,
  "RV_pct": 0.6,
  "ET_pct": 0,
  "CF_count": 76,
  "samples": 551
}

=== eval_70b_zs_docred_200_unconstrained ===
{
  "samples": 200,
  "parse_failures": 0,
  "entities_pred": 3242,
  "relations_pred": 2637,
  "ET_pct": 0,
  "RV_pct": 7.88,
  "DR_pct": 13.45,
  "CF_count": 0,
  "fuzzy_matches": 8,
  "E_F1": 70.14,
  "E_P": 75.85,
  "E_R": 65.23,
  "R_F1": 13.25,
  "R_P": 12.97,
  "R_R": 13.54
}

=== eval_70b_zs_docred_200_grammar_only ===
{
  "samples": 200,
  "parse_failures": 1,
  "entities_pred": 3221,
  "relations_pred": 2609,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 17.03,
  "CF_count": 0,
  "fuzzy_matches": 0,
  "E_F1": 70.12,
  "E_P": 75.88,
  "E_R": 65.17,
  "R_F1": 13.23,
  "R_P": 12.99,
  "R_R": 13.47
}

=== eval_70b_zs_docred_200_semantic_only ===
{
  "samples": 200,
  "parse_failures": 0,
  "entities": 3240,
  "relations": 2596,
  "ET_pct": 0.12,
  "RV_pct": 8.24,
  "DR_pct": 1.66,
  "CF_count": 132,
  "CF_pct": 4.07,
  "E_F1": 70.1,
  "E_P": 75.87,
  "E_R": 65.15,
  "R_F1": 13.05,
  "R_P": 12.88,
  "R_R": 13.23,
  "fuzzy_matches": 8
}

=== eval_70b_zs_docred_200_full_s1 ===
{
  "DR%": 0,
  "RV%": 0,
  "ET%": 0,
  "CF%": 5.34,
  "E-F1": 70.05,
  "R-F1": 13.25,
  "PF%": 0,
  "entities_pred": 3234,
  "relations_pred": 2637,
  "triples_checked": 2642
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "c66f43f0-9553-4a86-9322-ddaa7f296fb4",
  "tool_use_result": {
    "stdout": "=== eval_70b_lora_scierc_unconstrained ===\n{\n  \"E_F1\": 64.86,\n  \"E_P\": 62.74,\n  \"E_R\": 67.12,\n  \"R_F1\": 44.73,\n  \"R_P\": 41.61,\n  \"R_R\": 48.36,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 1.5,\n  \"CF_pct\": 0,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551,\n  \"entities\": 1806,\n  \"relations\": 1133\n}\n\n=== eval_70b_lora_scierc_grammar_only ===\n{\n  \"samples\": 551,\n  \"json_failures\": 0,\n  \"json_failure_rate\": 0,\n  \"entities\": 1805,\n  \"relations\": 1133,\n  \"entity_type_violations\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocab_violations\": 0,\n  \"relation_vocab_violation_rate\": 0,\n  \"domain_range_violations\": 17,\n  \"domain_range_violation_rate\": 0.015,\n  \"cross_field_consistency_violations\": 0,\n  \"fuzzy_relation_matches\": 0,\n  \"entity_P\": 0.6272,\n  \"entity_R\": 0.6707,\n  \"entity_F1\": 0.6482,\n  \"relation_P\": 0.4152,\n  \"relation_R\": 0.4825,\n  \"relation_F1\": 0.4463\n}\n\n=== eval_70b_lora_scierc_semantic_only ===\n{\n  \"samples\": 551,\n  \"json_failures\": 0,\n  \"entities\": 1806,\n  \"relations\": 1133,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.6,\n  \"CF_count\": 9,\n  \"E_F1\": 64.86,\n  \"E_P\": 62.74,\n  \"E_R\": 67.12,\n  \"R_F1\": 44.73,\n  \"R_P\": 41.61,\n  \"R_R\": 48.36,\n  \"parse_fail_pct\": 0\n}\n\n=== eval_70b_lora_scierc_s1_constrained ===\n{\n  \"entity_f1\": 0.6476,\n  \"entity_precision\": 0.6266,\n  \"entity_recall\": 0.6701,\n  \"relation_f1\": 0.4453,\n  \"relation_precision\": 0.4149,\n  \"relation_recall\": 0.4805,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_count\": 15,\n  \"parse_fail_pct\": 0,\n  \"fuzzy_matches\": 0,\n  \"num_samples\": 551,\n  \"num_entities\": 1805,\n  \"num_relations\": 1129\n}\n\n=== eval_70b_lora_scierc_full_s2 ===\n{\n  \"samples\": 551,\n  \"json_failures\": 0,\n  \"entities\": 1531,\n  \"relations\": 1027,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_count\": 18,\n  \"E_F1\": 62.35,\n  \"E_P\": 65.44,\n  \"E_R\": 59.53,\n  \"R_F1\": 36.28,\n  \"R_P\": 35.35,\n  \"R_R\": 37.27,\n  \"parse_fail_pct\": 0\n}\n\n=== eval_70b_lora_scierc_beam4_s1 ===\n{\n  \"E_F1\": 64.89,\n  \"E_P\": 62.29,\n  \"E_R\": 67.72,\n  \"R_F1\": 44.81,\n  \"R_P\": 39.45,\n  \"R_R\": 51.85,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_count\": 1,\n  \"parse_fail_pct\": 0,\n  \"samples\": 551,\n  \"entities\": 1839,\n  \"relations\": 1283\n}\n\n=== eval_70b_lora_docred_200_unconstrained ===\n{\n  \"E_F1\": 80.34,\n  \"E_P\": 85.13,\n  \"E_R\": 76.05,\n  \"R_F1\": 43.8,\n  \"R_P\": 39.6,\n  \"R_R\": 48.99,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.57,\n  \"DR_pct\": 0.22,\n  \"CF_pct\": 0.06,\n  \"parse_fail_pct\": 10,\n  \"samples\": 200,\n  \"relations\": 3159,\n  \"RV_count\": 18,\n  \"DR_count\": 7,\n  \"CF_count\": 2\n}\n\n=== eval_70b_lora_docred_200_grammar_only ===\n{\n  \"samples\": 200,\n  \"parse_fail_pct\": 10.5,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.38,\n  \"CF_pct\": 0.06,\n  \"E_F1\": 80.13,\n  \"E_P\": 85.16,\n  \"E_R\": 75.66,\n  \"R_F1\": 43.96,\n  \"R_P\": 39.78,\n  \"R_R\": 49.11,\n  \"entities_pred\": 3362,\n  \"relations_pred\": 3154\n}\n\n=== eval_70b_lora_docred_200_semantic_only ===\n{\n  \"samples\": 200,\n  \"parse_fail_pct\": 11,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.51,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.21,\n  \"E_F1\": 80.06,\n  \"E_P\": 85.21,\n  \"E_R\": 75.5,\n  \"R_F1\": 43.61,\n  \"R_P\": 39.44,\n  \"R_R\": 48.75,\n  \"entities_pred\": 3351,\n  \"relations_pred\": 3148\n}\n\n=== eval_70b_lora_docred_200_s1_constrained ===\n{\n  \"E_F1\": 79.38,\n  \"E_P\": 85.24,\n  \"E_R\": 74.28,\n  \"R_F1\": 43.95,\n  \"R_P\": 40.48,\n  \"R_R\": 48.08,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_pct\": 0.18,\n  \"parse_fail_pct\": 12.5,\n  \"samples\": 200\n}\n\n=== eval_70b_lora_docred_200_full_s2 ===\n{\n  \"R_F1\": 36.45,\n  \"R_P\": 31.25,\n  \"R_R\": 43.72,\n  \"E_F1\": 84.96,\n  \"E_P\": 84.6,\n  \"E_R\": 85.34,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_count\": 13,\n  \"CF_pct\": 0.34,\n  \"parse_fail_pct\": 0,\n  \"pred_entities\": 3819,\n  \"pred_relations\": 3546,\n  \"entity_tp\": 3218,\n  \"entity_fp\": 586,\n  \"entity_fn\": 553,\n  \"relation_tp\": 1104,\n  \"relation_fp\": 2429,\n  \"relation_fn\": 1421\n}\n\n=== eval_70b_lora_docred_200_beam4_s1 ===\n{\n  \"E-F1\": 85.57,\n  \"E-P\": 85.45,\n  \"E-R\": 85.68,\n  \"R-F1\": 48.14,\n  \"R-P\": 44.24,\n  \"R-R\": 52.79,\n  \"ET%\": 0,\n  \"RV%\": 0,\n  \"DR%\": 0,\n  \"CF%\": 0,\n  \"parse_fail\": \"1/200 (0.5%)\",\n  \"entities_pred\": 3790,\n  \"relations_pred\": 3030\n}\n\n=== r16_70b_docred_zs_unconstrained === NOT FOUND\n\n=== r16_70b_docred_zs_grammar_only === NOT FOUND\n\n=== r16_70b_docred_zs_semantic_only === NOT FOUND\n\n=== r16_70b_docred_zs_s1 ===\n{\n  \"E_F1\": 69.11,\n  \"R_F1\": 13.05,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_pct\": 0.04,\n  \"parse_fail_pct\": 0.1,\n  \"samples\": 998,\n  \"total_entities\": 16599,\n  \"total_triples\": 13239,\n  \"baseline_unc_DR_pct\": 14.98,\n  \"baseline_unc_R_F1\": 13.01,\n  \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"\n}\n\n=== eval_70b_zs_scierc_unconstrained ===\n{\n  \"samples\": 551,\n  \"json_failures\": 0,\n  \"entities\": 2353,\n  \"relations\": 1483,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.6,\n  \"DR_pct\": 6.4,\n  \"CF_count\": 0,\n  \"E_F1\": 35.22,\n  \"E_P\": 30.13,\n  \"E_R\": 42.38,\n  \"R_F1\": 11.23,\n  \"R_P\": 9.31,\n  \"R_R\": 14.17,\n  \"parse_fail_pct\": 0\n}\n\n=== eval_70b_zs_scierc_grammar_only ===\n{\n  \"R_F1\": 11.23,\n  \"DR_pct\": 6.33,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_count\": 0,\n  \"samples\": 551\n}\n\n=== eval_70b_zs_scierc_semantic_only ===\n{\n  \"R_F1\": 11.37,\n  \"DR_pct\": 1.01,\n  \"RV_pct\": 0.6,\n  \"ET_pct\": 0,\n  \"CF_count\": 76,\n  \"samples\": 551\n}\n\n=== eval_70b_zs_docred_200_unconstrained ===\n{\n  \"samples\": 200,\n  \"parse_failures\": 0,\n  \"entities_pred\": 3242,\n  \"relations_pred\": 2637,\n  \"ET_pct\": 0,\n  \"RV_pct\": 7.88,\n  \"DR_pct\": 13.45,\n  \"CF_count\": 0,\n  \"fuzzy_matches\": 8,\n  \"E_F1\": 70.14,\n  \"E_P\": 75.85,\n  \"E_R\": 65.23,\n  \"R_F1\": 13.25,\n  \"R_P\": 12.97,\n  \"R_R\": 13.54\n}\n\n=== eval_70b_zs_docred_200_grammar_only ===\n{\n  \"samples\": 200,\n  \"parse_failures\": 1,\n  \"entities_pred\": 3221,\n  \"relations_pred\": 2609,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 17.03,\n  \"CF_count\": 0,\n  \"fuzzy_matches\": 0,\n  \"E_F1\": 70.12,\n  \"E_P\": 75.88,\n  \"E_R\": 65.17,\n  \"R_F1\": 13.23,\n  \"R_P\": 12.99,\n  \"R_R\": 13.47\n}\n\n=== eval_70b_zs_docred_200_semantic_only ===\n{\n  \"samples\": 200,\n  \"parse_failures\": 0,\n  \"entities\": 3240,\n  \"relations\": 2596,\n  \"ET_pct\": 0.12,\n  \"RV_pct\": 8.24,\n  \"DR_pct\": 1.66,\n  \"CF_count\": 132,\n  \"CF_pct\": 4.07,\n  \"E_F1\": 70.1,\n  \"E_P\": 75.87,\n  \"E_R\": 65.15,\n  \"R_F1\": 13.05,\n  \"R_P\": 12.88,\n  \"R_R\": 13.23,\n  \"fuzzy_matches\": 8\n}\n\n=== eval_70b_zs_docred_200_full_s1 ===\n{\n  \"DR%\": 0,\n  \"RV%\": 0,\n  \"ET%\": 0,\n  \"CF%\": 5.34,\n  \"E-F1\": 70.05,\n  \"R-F1\": 13.25,\n  \"PF%\": 0,\n  \"entities_pred\": 3234,\n  \"relations_pred\": 2637,\n  \"triples_checked\": 2642\n}",
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

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
Good progress. Let me now look at the 70B DocRED ZS ablation table more carefully. The paper says:

tab:70b-docred-zs-ablation:
- Unconstrained: DR=13.45, RV=7.88, ET=0, CF=0, R-F1=13.25, E-F1=70.14
- Grammar: DR=17.03, RV=0, ET=0, CF=0, R-F1=13.23, E-F1=70.12


- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10
- S1: DR=0, RV=0, ET=0, CF=173, R-F1=13.25, E-F1=70.05

Now I'm checking the registry entries to verify these match the reported results.

- eval_70b_zs_docred_200_unconstrained: DR=13.45, RV=7.88, ET=0, CF=0, R-F1=13.25, E-F1=70.14 ✅
- eval_70b_zs_docred_200_grammar_only: DR=17.03, RV=0, ET=0, CF=0, R-F1=13.23, E-F1=70.12 ✅
- eval_70b_zs_docred_200_semantic_only: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10 ✅
- eval_70b_zs_docred_200_full_s1: DR=0, RV=0, ET=0, CF=173, R-F1=13.25, E-F1=70.05

There's a discrepancy I'm noticing—the paper reports CF=173 for S1, but I'm seeing CF%=5.34% in the registry. If 173 is a count out of 2637 total relations, that would be about 6.56%, which doesn't align with the percentage shown.

Let me work through the math more carefully. With 2642 triples checked, 173 would be roughly 6.55%, still not matching the 5.34% figure. I'm wondering if the registry is computing this differently, or if there are separate experiment IDs for the 200-document versus 998-document versions that I need to distinguish between. So the registry entries with the 200-doc suffix match the paper's results perfectly across all three conditions—unconstrained, grammar-only, and semantic-only. Now I need to verify the S1 variant matches as well by checking if the remaining metrics in the registry align with what's shown in the table.

The CF count of 173 seems to be calculated differently than the 5.34% percentage—dividing 173 by the predicted entity count of 3234 gives roughly 5.34%, suggesting the percentage is normalized by entities rather than relations. The DocRED zero-shot ablation numbers check out. Now I'm verifying the quantization table results across different models and datasets—comparing the paper's reported values for SciERC with both Qwen and Llama in FP16 and INT4 formats against the corresponding experiment logs to ensure they match up. Confirming the Llama/INT4 DocRED results match the expected experiment, and now I need to locate the FP16 SciERC Llama LoRA S1 values to complete the validation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ab28ca8c-1661-496e-949d-14d6611de174",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV75xdJr6W3NfnMxhu86in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4691,
      "cache_read_input_tokens": 85335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4691
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

_source line 84_

Let me continue querying the remaining experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "c6d3f200-7ae3-4863-9f72-cfef2524c1fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV75xdJr6W3NfnMxhu86in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4691,
      "cache_read_input_tokens": 85335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4691
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

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_013hHH6jtAcp8cBggd4TBRzx`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# FT ablation, cross-model, DocRED ablation, GoLLIE, FP16 baselines\nids = [\n    # Llama SciERC FP16 (LoRA constrained)\n    'w5_llama_lora_scierc_constrained_eval',\n    'w5_llama_lora_scierc_unconstrained_eval',\n    'w5_lora_scierc_constrained_eval',\n    'w5_lora_scierc_unconstrained_eval',\n    # DocRED FT\n    'w5_qwen_docred_lora_constrained_eval',\n    'w5_qwen_docred_lora_unconstrained_eval',\n    'w5_llama_docred_lora_constrained_eval',\n    'w5_llama_docred_lora_unconstrained_eval',\n    # FT ablation grammar/semantic\n    'w7_qwen_scierc_ft_grammar_only',\n    'w7_qwen_scierc_ft_semantic_only',\n    'w7_llama_scierc_ft_grammar_only',\n    'w7_llama_scierc_ft_semantic_only',\n    'w8_qwen_docred_ft_grammar_only',\n    'w8_qwen_docred_ft_semantic_only',\n    'w8_llama_docred_ft_grammar_only',\n    'w8_llama_docred_ft_semantic_only',\n    # GoLLIE\n    'sf2_gollie_scierc_violation',\n    'd063_gollie_violation_rate',\n    # Full FT\n    'd062_full_ft_scierc',\n]\n\nfor eid in ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        print(json.dumps(metrics, indent=2)[:1500])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\"",
  "description": "Extract FT ablation and other experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "a5b7a050-40fc-4b43-8399-0b1eb1390763",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AV75xdJr6W3NfnMxhu86in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4691,
      "cache_read_input_tokens": 85335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4691
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

_source line 86 · 2026-05-23T10:46:39.364Z_

<details><summary>↩ Tool result · `toolu_013hHH6jtAcp8cBggd4TBRzx`</summary>

```text
=== w5_llama_lora_scierc_constrained_eval ===
{
  "domain_range_violation_rate": 0.0009,
  "relation_vocabulary_violation_rate": 0,
  "entity_type_violation_rate": 0,
  "cross_field_consistency_violation_rate": 0.0046,
  "relation_f1": 0.4547,
  "relation_precision": 0.432,
  "relation_recall": 0.4795,
  "entity_f1": 0.6776,
  "entity_precision": 0.6647,
  "entity_recall": 0.691,
  "total_relations": 1081,
  "total_entities": 1757,
  "total_samples": 551,
  "parse_failures": 0
}

=== w5_llama_lora_scierc_unconstrained_eval ===
{
  "total_samples": 551,
  "total_entities": 1757,
  "total_relations": 1082,
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.0111,
  "cross_field_consistency_violation_rate": 0,
  "total_violation_rate": 0.0042,
  "entity_precision": 0.6647,
  "entity_recall": 0.691,
  "entity_f1": 0.6776,
  "relation_precision": 0.432,
  "relation_recall": 0.4795,
  "relation_f1": 0.4545
}

=== w5_lora_scierc_constrained_eval ===
{
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0,
  "cross_field_consistency_violation_rate": 0.0118,
  "entity_f1": 0.6705,
  "entity_precision": 0.6523,
  "entity_recall": 0.6898,
  "relation_f1": 0.4377,
  "relation_precision": 0.4078,
  "relation_recall": 0.4723,
  "total_entities": 1784,
  "total_relations": 1128,
  "total_samples": 551,
  "cross_field_consistency_violations": 21
}

=== w5_lora_scierc_unconstrained_eval ===
{
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.0195,
  "cross_field_consistency_violation_rate": 0,
  "entity_f1": 0.6705,
  "entity_precision": 0.6523,
  "entity_recall": 0.6898,
  "relation_f1": 0.4386,
  "relation_precision": 0.4087,
  "relation_recall": 0.4733,
  "total_entities": 1784,
  "total_relations": 1128,
  "domain_range_violations": 22,
  "go_nogo_metric": 0.0195,
  "dr_gate": "FAILED"
}

=== w5_qwen_docred_lora_constrained_eval ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.01,
  "CF_pct": 0.41,
  "E_F1": 81.43,
  "E_P": 85.41,
  "E_R": 77.81,
  "R_F1": 40.56,
  "R_P": 36.35,
  "R_R": 45.86,
  "parse_fail_rate": 8.52,
  "total_samples": 998,
  "success_samples": 913,
  "fail_samples": 85,
  "total_entities_pred": 17799,
  "total_relations_pred": 15563,
  "E_F1_excl_fail": 85.69,
  "R_F1_excl_fail": 42.23,
  "delta_vs_unconstrained": {
    "delta_DR": -0.75,
    "delta_RV": -0.27,
    "delta_R_F1": -0.3,
    "delta_R_F1_excl_fail": 0.03,
    "DR_reduction_pct": 98.7,
    "note": "Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20"
  }
}

=== w5_qwen_docred_lora_unconstrained_eval ===
{
  "ET_pct": 0,
  "RV_pct": 0.27,
  "DR_pct": 0.76,
  "CF_pct": 0.12,
  "E_F1": 82.15,
  "E_P": 85.44,
  "E_R": 79.11,
  "R_F1": 40.86,
  "R_P": 36.41,
  "R_R": 46.56,
  "parse_fail_rate": 7.11,
  "total_samples": 998,
  "success_samples": 927,
  "fail_samples": 71,
  "total_entities_pred": 18091,
  "total_relations_pred": 15870,
  "ET_pct_excl_fail": 0,
  "RV_pct_excl_fail": 0.27,
  "DR_pct_excl_fail": 0.76,
  "CF_pct_excl_fail": 0.12,
  "E_F1_excl_fail": 85.72,
  "E_P_excl_fail": 85.44,
  "E_R_excl_fail": 86,
  "R_F1_excl_fail": 42.2,
  "R_P_excl_fail": 36.41,
  "R_R_excl_fail": 50.17
}

=== w5_llama_docred_lora_constrained_eval ===
{
  "total": 998,
  "parse_failures": 25,
  "parse_fail_rate": 2.51,
  "entities": 19077,
  "relations": 16074,
  "entity_f1": 83.94,
  "entity_precision": 85,
  "entity_recall": 84.13,
  "relation_f1_all_set": 43.78,
  "relation_precision_all_set": 38.79,
  "relation_recall_all_set": 50.81,
  "et_violations": 0,
  "et_violation_rate": 0,
  "rv_violations": 0,
  "rv_violation_rate": 0,
  "dr_violations": 33,
  "dr_violation_rate": 0.21,
  "CF_pct": 0.21,
  "delta_vs_unconstrained": {
    "delta_e_f1": 0.01,
    "delta_r_f1": 0.06,
    "delta_dr": -0.28,
    "note": "Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20."
  },
  "provenance": "eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director."
}

=== w5_llama_docred_lora_unconstrained_eval ===
{
  "ET_pct": 0,
  "RV_pct": 0.15,
  "DR_pct": 0.49,
  "E_F1": 83.93,
  "E_P": 84.93,
  "E_R": 82.96,
  "R_F1": 43.72,
  "R_P": 38.59,
  "R_R": 50.41,
  "parse_fail_rate": 2.3,
  "total_samples": 998,
  "total_entities_pred": 19106,
  "total_relations_pred": 16171
}

=== w7_qwen_scierc_ft_grammar_only ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 1.9,
  "CF_pct": 0,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "total_entities": 1784,
  "total_relations": 1128,
  "E_P": 0.6523,
  "E_R": 0.6898,
  "E_F1": 0.6705,
  "R_P": 0.4087,
  "R_R": 0.4733,
  "R_F1": 0.4386,
  "DR_violations": 22,
  "tokenizer_warning": "false_positive_transformers_4.57.6"
}

=== w7_qwen_scierc_ft_semantic_only ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.6,
  "CF_count": 15,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "total_entities": 1784,
  "total_relations": 1128,
  "E_P": 0.6523,
  "E_R": 0.6898,
  "E_F1": 0.6705,
  "R_P": 0.4073,
  "R_R": 0.4713,
  "R_F1": 0.4369,
  "DR_violations": 7,
  "delta_vs_grammar_only": {
    "DR_delta": -1.3,
    "note": "semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%"
  },
  "delta_vs_unconstrained": {
    "DR_delta": -1.35,
    "note": "unconstrained DR=1.95% \u2192 semantic_only 0.6%"
  }
}

=== w7_llama_scierc_ft_grammar_only ===
{
  "total_samples": 551,
  "json_parse_failures": 0,
  "total_entities": 1757,
  "total_relations": 1082,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.0111,
  "cross_field_consistency_violation_rate": 0,
  "entity_f1": {
    "precision": 0.6647,
    "recall": 0.691,
    "f1": 0.6776
  },
  "relation_f1": {
    "precision": 0.432,
    "recall": 0.4795,
    "f1": 0.4545
  }
}

=== w7_llama_scierc_ft_semantic_only ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.65,
  "CF_count": 2,
  "E_F1": 67.76,
  "E_P": 66.47,
  "E_R": 69.1,
  "R_F1": 45.47,
  "R_P": 43.24,
  "R_R": 47.95,
  "total_entities": 1757,
  "total_relations": 1081,
  "json_parse_failures": 0
}

=== w8_qwen_docred_ft_grammar_only ===
{
  "E_F1": 82.19,
  "E_P": 85.47,
  "E_R": 79.16,
  "R_F1": 40.85,
  "R_P": 36.27,
  "R_R": 46.77,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.61,
  "CF_pct": 0.11,
  "parse_fail_rate": 7.01,
  "total_samples": 998,
  "parse_failures": 70
}

=== w8_qwen_docred_ft_semantic_only ===
{
  "R_F1": 40.85,
  "R_P": 36.33,
  "R_R": 46.65,
  "parse_fail_pct": 7.52,
  "samples": 998,
  "note": "Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp)."
}

=== w8_llama_docred_ft_grammar_only ===
{
  "R_F1": 43.72,
  "R_P": 38.57,
  "R_R": 50.44,
  "parse_fail_pct": 2.3,
  "samples": 998,
  "note": "Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp)."
}

=== w8_llama_docred_ft_semantic_only ===
{
  "R_F1": 43.85,
  "R_P": 38.85,
  "R_R": 50.31,
  "parse_fail_pct": 2.4,
  "samples": 998,
  "note": "Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp)."
}

=== sf2_gollie_scierc_violation ===
{
  "GoLLIE_ZS": {
    "DR_pct": 0,
    "RV_pct": 0,
    "ET_pct": 0,
    "CF_pct": 0.83,
    "E_F1": 9.17,
    "R_F1": 0,
    "pred_ents": 241,
    "pred_rels": 5,
    "docs_with_output": 54
  },
  "OntoCoDec_Qwen_FT_S1": {
    "DR_pct": 0,
    "RV_pct": 0,
    "ET_pct": 0,
    "CF_pct": 0.61,
    "E_F1": 66.43,
    "R_F1": 43.69
  },
  "OntoCoDec_Llama_FT_S1": {
    "DR_pct": 0,
    "RV_pct": 0,
    "ET_pct": 0,
    "CF_pct": 0.62,
    "E_F1": 67.09,
    "R_F1": 45.47
  }
}

=== d063_gollie_violation_rate ===
{
  "gollie_DR": 0,
  "gollie_RV": 0,
  "gollie_ET": 0,
  "gollie_CF": 0.67,
  "gollie_entities": 300,
  "gollie_relations": 7,
  "gollie_empty_docs_pct": 45,
  "docs_tested": 100
}

=== d062_full_ft_scierc ===
{
  "unconstrained": {
    "entity_f1": 0.6478,
    "relation_f1": 0.3789,
    "DR_pct": 2.74,
    "RV_pct": 0.18,
    "ET_pct": 0,
    "CF_pct": 0
  },
  "constrained": {
    "entity_f1": 0.6478,
    "relation_f1": 0.3789,
    "DR_pct": 0,
    "RV_pct": 0,
    "ET_pct": 0,
    "CF_pct": 1.31
  },
  "training": {
    "eval_loss_final": 0.09459,
    "epochs": 3,
    "total_steps": 333,
    "training_time": "21m49s"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "53076671-6e12-4593-90e0-50f10c80ba97",
  "tool_use_result": {
    "stdout": "=== w5_llama_lora_scierc_constrained_eval ===\n{\n  \"domain_range_violation_rate\": 0.0009,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0.0046,\n  \"relation_f1\": 0.4547,\n  \"relation_precision\": 0.432,\n  \"relation_recall\": 0.4795,\n  \"entity_f1\": 0.6776,\n  \"entity_precision\": 0.6647,\n  \"entity_recall\": 0.691,\n  \"total_relations\": 1081,\n  \"total_entities\": 1757,\n  \"total_samples\": 551,\n  \"parse_failures\": 0\n}\n\n=== w5_llama_lora_scierc_unconstrained_eval ===\n{\n  \"total_samples\": 551,\n  \"total_entities\": 1757,\n  \"total_relations\": 1082,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0111,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"total_violation_rate\": 0.0042,\n  \"entity_precision\": 0.6647,\n  \"entity_recall\": 0.691,\n  \"entity_f1\": 0.6776,\n  \"relation_precision\": 0.432,\n  \"relation_recall\": 0.4795,\n  \"relation_f1\": 0.4545\n}\n\n=== w5_lora_scierc_constrained_eval ===\n{\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0.0118,\n  \"entity_f1\": 0.6705,\n  \"entity_precision\": 0.6523,\n  \"entity_recall\": 0.6898,\n  \"relation_f1\": 0.4377,\n  \"relation_precision\": 0.4078,\n  \"relation_recall\": 0.4723,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"total_samples\": 551,\n  \"cross_field_consistency_violations\": 21\n}\n\n=== w5_lora_scierc_unconstrained_eval ===\n{\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0195,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"entity_f1\": 0.6705,\n  \"entity_precision\": 0.6523,\n  \"entity_recall\": 0.6898,\n  \"relation_f1\": 0.4386,\n  \"relation_precision\": 0.4087,\n  \"relation_recall\": 0.4733,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"domain_range_violations\": 22,\n  \"go_nogo_metric\": 0.0195,\n  \"dr_gate\": \"FAILED\"\n}\n\n=== w5_qwen_docred_lora_constrained_eval ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.01,\n  \"CF_pct\": 0.41,\n  \"E_F1\": 81.43,\n  \"E_P\": 85.41,\n  \"E_R\": 77.81,\n  \"R_F1\": 40.56,\n  \"R_P\": 36.35,\n  \"R_R\": 45.86,\n  \"parse_fail_rate\": 8.52,\n  \"total_samples\": 998,\n  \"success_samples\": 913,\n  \"fail_samples\": 85,\n  \"total_entities_pred\": 17799,\n  \"total_relations_pred\": 15563,\n  \"E_F1_excl_fail\": 85.69,\n  \"R_F1_excl_fail\": 42.23,\n  \"delta_vs_unconstrained\": {\n    \"delta_DR\": -0.75,\n    \"delta_RV\": -0.27,\n    \"delta_R_F1\": -0.3,\n    \"delta_R_F1_excl_fail\": 0.03,\n    \"DR_reduction_pct\": 98.7,\n    \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"\n  }\n}\n\n=== w5_qwen_docred_lora_unconstrained_eval ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.27,\n  \"DR_pct\": 0.76,\n  \"CF_pct\": 0.12,\n  \"E_F1\": 82.15,\n  \"E_P\": 85.44,\n  \"E_R\": 79.11,\n  \"R_F1\": 40.86,\n  \"R_P\": 36.41,\n  \"R_R\": 46.56,\n  \"parse_fail_rate\": 7.11,\n  \"total_samples\": 998,\n  \"success_samples\": 927,\n  \"fail_samples\": 71,\n  \"total_entities_pred\": 18091,\n  \"total_relations_pred\": 15870,\n  \"ET_pct_excl_fail\": 0,\n  \"RV_pct_excl_fail\": 0.27,\n  \"DR_pct_excl_fail\": 0.76,\n  \"CF_pct_excl_fail\": 0.12,\n  \"E_F1_excl_fail\": 85.72,\n  \"E_P_excl_fail\": 85.44,\n  \"E_R_excl_fail\": 86,\n  \"R_F1_excl_fail\": 42.2,\n  \"R_P_excl_fail\": 36.41,\n  \"R_R_excl_fail\": 50.17\n}\n\n=== w5_llama_docred_lora_constrained_eval ===\n{\n  \"total\": 998,\n  \"parse_failures\": 25,\n  \"parse_fail_rate\": 2.51,\n  \"entities\": 19077,\n  \"relations\": 16074,\n  \"entity_f1\": 83.94,\n  \"entity_precision\": 85,\n  \"entity_recall\": 84.13,\n  \"relation_f1_all_set\": 43.78,\n  \"relation_precision_all_set\": 38.79,\n  \"relation_recall_all_set\": 50.81,\n  \"et_violations\": 0,\n  \"et_violation_rate\": 0,\n  \"rv_violations\": 0,\n  \"rv_violation_rate\": 0,\n  \"dr_violations\": 33,\n  \"dr_violation_rate\": 0.21,\n  \"CF_pct\": 0.21,\n  \"delta_vs_unconstrained\": {\n    \"delta_e_f1\": 0.01,\n    \"delta_r_f1\": 0.06,\n    \"delta_dr\": -0.28,\n    \"note\": \"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\"\n  },\n  \"provenance\": \"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\"\n}\n\n=== w5_llama_docred_lora_unconstrained_eval ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.15,\n  \"DR_pct\": 0.49,\n  \"E_F1\": 83.93,\n  \"E_P\": 84.93,\n  \"E_R\": 82.96,\n  \"R_F1\": 43.72,\n  \"R_P\": 38.59,\n  \"R_R\": 50.41,\n  \"parse_fail_rate\": 2.3,\n  \"total_samples\": 998,\n  \"total_entities_pred\": 19106,\n  \"total_relations_pred\": 16171\n}\n\n=== w7_qwen_scierc_ft_grammar_only ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 1.9,\n  \"CF_pct\": 0,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"E_P\": 0.6523,\n  \"E_R\": 0.6898,\n  \"E_F1\": 0.6705,\n  \"R_P\": 0.4087,\n  \"R_R\": 0.4733,\n  \"R_F1\": 0.4386,\n  \"DR_violations\": 22,\n  \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"\n}\n\n=== w7_qwen_scierc_ft_semantic_only ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.6,\n  \"CF_count\": 15,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"E_P\": 0.6523,\n  \"E_R\": 0.6898,\n  \"E_F1\": 0.6705,\n  \"R_P\": 0.4073,\n  \"R_R\": 0.4713,\n  \"R_F1\": 0.4369,\n  \"DR_violations\": 7,\n  \"delta_vs_grammar_only\": {\n    \"DR_delta\": -1.3,\n    \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"\n  },\n  \"delta_vs_unconstrained\": {\n    \"DR_delta\": -1.35,\n    \"note\": \"unconstrained DR=1.95% \\u2192 semantic_only 0.6%\"\n  }\n}\n\n=== w7_llama_scierc_ft_grammar_only ===\n{\n  \"total_samples\": 551,\n  \"json_parse_failures\": 0,\n  \"total_entities\": 1757,\n  \"total_relations\": 1082,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0111,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"entity_f1\": {\n    \"precision\": 0.6647,\n    \"recall\": 0.691,\n    \"f1\": 0.6776\n  },\n  \"relation_f1\": {\n    \"precision\": 0.432,\n    \"recall\": 0.4795,\n    \"f1\": 0.4545\n  }\n}\n\n=== w7_llama_scierc_ft_semantic_only ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.65,\n  \"CF_count\": 2,\n  \"E_F1\": 67.76,\n  \"E_P\": 66.47,\n  \"E_R\": 69.1,\n  \"R_F1\": 45.47,\n  \"R_P\": 43.24,\n  \"R_R\": 47.95,\n  \"total_entities\": 1757,\n  \"total_relations\": 1081,\n  \"json_parse_failures\": 0\n}\n\n=== w8_qwen_docred_ft_grammar_only ===\n{\n  \"E_F1\": 82.19,\n  \"E_P\": 85.47,\n  \"E_R\": 79.16,\n  \"R_F1\": 40.85,\n  \"R_P\": 36.27,\n  \"R_R\": 46.77,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.61,\n  \"CF_pct\": 0.11,\n  \"parse_fail_rate\": 7.01,\n  \"total_samples\": 998,\n  \"parse_failures\": 70\n}\n\n=== w8_qwen_docred_ft_semantic_only ===\n{\n  \"R_F1\": 40.85,\n  \"R_P\": 36.33,\n  \"R_R\": 46.65,\n  \"parse_fail_pct\": 7.52,\n  \"samples\": 998,\n  \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"\n}\n\n=== w8_llama_docred_ft_grammar_only ===\n{\n  \"R_F1\": 43.72,\n  \"R_P\": 38.57,\n  \"R_R\": 50.44,\n  \"parse_fail_pct\": 2.3,\n  \"samples\": 998,\n  \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"\n}\n\n=== w8_llama_docred_ft_semantic_only ===\n{\n  \"R_F1\": 43.85,\n  \"R_P\": 38.85,\n  \"R_R\": 50.31,\n  \"parse_fail_pct\": 2.4,\n  \"samples\": 998,\n  \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"\n}\n\n=== sf2_gollie_scierc_violation ===\n{\n  \"GoLLIE_ZS\": {\n    \"DR_pct\": 0,\n    \"RV_pct\": 0,\n    \"ET_pct\": 0,\n    \"CF_pct\": 0.83,\n    \"E_F1\": 9.17,\n    \"R_F1\": 0,\n    \"pred_ents\": 241,\n    \"pred_rels\": 5,\n    \"docs_with_output\": 54\n  },\n  \"OntoCoDec_Qwen_FT_S1\": {\n    \"DR_pct\": 0,\n    \"RV_pct\": 0,\n    \"ET_pct\": 0,\n    \"CF_pct\": 0.61,\n    \"E_F1\": 66.43,\n    \"R_F1\": 43.69\n  },\n  \"OntoCoDec_Llama_FT_S1\": {\n    \"DR_pct\": 0,\n    \"RV_pct\": 0,\n    \"ET_pct\": 0,\n    \"CF_pct\": 0.62,\n    \"E_F1\": 67.09,\n    \"R_F1\": 45.47\n  }\n}\n\n=== d063_gollie_violation_rate ===\n{\n  \"gollie_DR\": 0,\n  \"gollie_RV\": 0,\n  \"gollie_ET\": 0,\n  \"gollie_CF\": 0.67,\n  \"gollie_entities\": 300,\n  \"gollie_relations\": 7,\n  \"gollie_empty_docs_pct\": 45,\n  \"docs_tested\": 100\n}\n\n=== d062_full_ft_scierc ===\n{\n  \"unconstrained\": {\n    \"entity_f1\": 0.6478,\n    \"relation_f1\": 0.3789,\n    \"DR_pct\": 2.74,\n    \"RV_pct\": 0.18,\n    \"ET_pct\": 0,\n    \"CF_pct\": 0\n  },\n  \"constrained\": {\n    \"entity_f1\": 0.6478,\n    \"relation_f1\": 0.3789,\n    \"DR_pct\": 0,\n    \"RV_pct\": 0,\n    \"ET_pct\": 0,\n    \"CF_pct\": 1.31\n  },\n  \"training\": {\n    \"eval_loss_final\": 0.09459,\n    \"epochs\": 3,\n    \"total_steps\": 333,\n    \"training_time\": \"21m49s\"\n  }\n}",
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

_source line 87_

<details><summary>Logged reasoning block</summary>

```text
Now let me look at some discrepancies. Let me check the ft-ablation table values (tab:ft-ablation):

Paper says:

SciERC/Qwen:
- Unconstrained: DR=1.95, RV=0.00, ET=0.00, CF=0.00, PF=0.00, E-F1=67.05, R-F1=43.86
- Grammar: DR=1.90, RV=0.00, ET=0.00, CF=0.00, PF=0.00, E-F1=67.05, R-F1=43.86


- Semantic: DR=0.60, RV=0.00, ET=0.00, CF=0.18, PF=0.00, E-F1=67.05, R-F1=43.69
- S1: DR=0, RV=0.00, ET=0.00, CF=1.18, PF=0.00, E-F1=67.05, R-F1=43.77

Now comparing against the registry values where the unconstrained configuration shows DR=1.95%, RV=0, ET=0, CF=0.

I'm noticing a discrepancy with the semantic model's CF value. The paper reports CF=0.18, but when I look at CF_count=15 with total_relations=1128, the math doesn't quite line up. Let me figure out what denominator CF is actually using here. I'm getting 1.33% when dividing violations by relations, which still doesn't match the paper's 0.18%. Let me reconsider what the denominator might be—maybe CF is calculated per entity rather than per relation. Testing this theory with another data point: if I divide 21 violations by 1784 total entities, I get 1.18%, which matches the constrained eval result exactly. So the metric appears to be violations divided by total entities, not relations. I'm getting 0.843% for that calculation, which still doesn't match the 0.18% in the paper. Let me reconsider whether CF is being computed differently across experiments—maybe it's calculated per-relation or per-unique-entity rather than per-entity overall, or perhaps the CF_count values I'm seeing represent something different than what goes into the percentage calculation.

Looking at w5_lora_scierc_constrained_eval more carefully, I can verify that 21 violations divided by 1784 entities gives 0.0118, which matches the reported rate—so CF is definitely per-entity. But applying that same logic to semantic_only with 15 violations and 1784 entities gives 0.841%, not 0.18%, so something's still off.

Let me check if there's a consistent pattern across other experiments. For the Llama constrained eval, the rate of 0.0046 matches 0.46% from the paper, which suggests the calculations should align—but the semantic_only numbers aren't cooperating. I'm noticing a significant gap between the paper's reported CF percentage for Qwen semantic (0.18%) and what I'm calculating from the data (0.84%), which suggests the CF metric might be computed differently than I assumed—perhaps normalized by relation count or unique entity pairs rather than total entities. Let me examine the raw CF_count values more carefully to understand what denominator the paper actually used. I should move forward and flag this as a potential discrepancy rather than getting stuck on the denominator—the registry shows CF_count=15 for the Qwen SciERC semantic-only experiment but the paper reports CF=0.18%, and I need to verify what denominator was actually used. Looking at the S1 case where CF_count=21 corresponds to 1.18%, that suggests a denominator around 1780, which might be the total semantic decisions or entity mentions rather than unique entities. similar. And if semantic has CF=0.18%, that means CF_count should be about 1780*0.0018 ≈ 3.2 ≈ 3.

But the registry says CF_count=15 for semantic. So there may be a mismatch between what the registry stored and what the paper uses.

Hmm, let me think about this differently. Maybe the CF metric in the ft-ablation table uses a denominator of total unique entities mentioned across all relations (e.g., unique entity-document pairs). That could be very different from total_entities.

Actually, for S1: CF_count=21, CF%=1.18%, so denominator=21/0.0118=1780. total_entities=1784. So roughly 1780. OK, close enough.

For semantic: CF_count=15, if the denominator is the same 1784, then 15/1784=0.84%, but the paper says 0.18%. That's a 4.7x difference, which suggests something fundamental is different about how the semantic-only ablation computes CF violations—possibly because it lacks the grammar layer that enforces vocabulary constraints in the standard setup. I'm going to move on from this discrepancy since I've spent enough time investigating it.

Let me now verify the numbers I can check more directly. I notice the w8_qwen_docred_ft_semantic_only experiment was re-verified on 2026-05-22 with a note about a parse-failure bug in the old unified_f1_eval.py. The paper reports DocRED/Qwen/Semantic R-F1=40.89, and the corrected registry shows 40.85, but the old value was 40.89—suggesting the paper might still be using the pre-correction value.

Looking at the other affected experiments, I'm seeing a pattern: w8_llama_docred_ft_grammar_only has a corrected R-F1=43.72 versus the old 43.77 that the paper cites, and w8_llama_docred_ft_semantic_only shows corrected 43.85 versus old 43.90 that appears in the paper. All three cases point to the paper using the buggy values from before the parse-failure fix. Now I need to check the remaining DocRED fine-tuning results to see if this issue extends further. I'm noticing a discrepancy between the paper's reported values and what's in the registry. The paper shows R-F1=40.89 and E-F1=82.35 for the unconstrained model, but the registry has slightly different numbers (40.86 and 82.15). Looking at the notes, it seems there's a distinction between old values from unified_f1_eval.py and corrected values from eval_d064.py, though the unconstrained entry wasn't explicitly marked as re-verified like some others were. I'm also seeing that the DR metric differs significantly between the paper (0.56) and registry (0.76), which suggests they might be using different evaluation scripts or versions. I'm noticing the registry shows DR=0.76 for the unconstrained DocRED experiment, but the paper reports 0.56—along with other metric discrepancies like CF values. Given the parse-failure bug fix mentioned in the w8 experiments, these DocRED numbers might have been corrected. I'm cross-checking against the d065_qwen_greedy baseline used in the quantization table, which shows E-F1=81.87 and R-F1=40.79 matching the ft-ablation table's S1 constrained values, though the PF metric seems to diverge. The corrected evaluation pipeline produces slightly different values than what appears in the ft-ablation table. Now I'm checking the Llama DocRED results to see if they have the same issue with using the old buggy evaluation metrics.

Looking at the registry values for the unconstrained Llama setup, I'm seeing a significant discrepancy—the paper reports E-F1 of 84.77 and R-F1 of 44.55, but the registry shows 83.93 and 43.72 respectively, which is off by about 0.8 percentage points in each direction. This appears to be another instance of the parse-failure bug affecting the stored evaluation results. There's a 0.92 percentage point gap between what the registry shows (43.78) and what the paper reports (44.70) for the constrained R-F1 score. Looking at the delta between constrained and unconstrained results, the math doesn't add up either—if unconstrained is 43.72 and the delta is only 0.06, the constrained value should be 43.78, not 44.70. I need to figure out whether the paper values come from a different experiment or evaluation script entirely.

Checking the registry metadata more carefully, I notice the corrected eval used eval_d064.py with precision and recall adjustments made on 2026-05-20. The deltas show only tiny differences between constrained and unconstrained (delta_e_f1: 0.01, delta_r_f1: 0.06), which suggests the paper's reported values might actually come from the older unified_f1_eval.py script rather than the corrected version. So the actual corrected numbers from eval_d064.py for Llama DocRED would be unconstrained at E-F1=83.93 and R-F1=43.72, with the constrained S1 values being only marginally higher.

This creates an inconsistency across the tables—the fine-tuning ablation uses pre-correction values throughout for DocRED, while the quantization table draws from more recent experiments like d065 and d066 that naturally incorporate the bug fixes since they were run after the correction was implemented.

I need to track all these discrepancies systematically. The w5_llama_docred_lora_constrained_eval shows a corrected R-F1 of 43.78, but the paper reports 44.70 for the constrained condition—let me check if this gap could stem from different evaluation methodologies or dataset subsets, especially since the w5 experiment used 998 samples which should match what's in the fine-tuning ablation table.

Examining the constrained eval metrics more closely...

The corrected delta between constrained and unconstrained is only 0.06 percentage points, whereas the paper shows 0.15pp—both are small differences, but the absolute values diverge by roughly 0.9pp. This confirms the DocRED rows in the ft-ablation table are using pre-correction values, the same issue already identified in Table 2 of the main text.

Now I need to systematically audit the remaining tables—cross-model comparisons, beam search results, discussion tables—and query the corresponding experiments to build a complete picture of what's been corrected and what hasn't.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3533033a-d145-4a31-b9d3-0a97ca556cb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxT97G4wnLzHjvJfM9t9kT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 90026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
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

_source line 88_

Let me continue querying experiments for the remaining tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "219fa8be-0850-4a37-afc0-49a163ffb6e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxT97G4wnLzHjvJfM9t9kT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 90026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
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

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01RBG2zAhpAnB6q7yn8vfZY3`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Cross-model, ZS ablation experiments\nids = [\n    'phase2_scierc_unconstrained', 'phase2_scierc_grammar_only',\n    'phase2_scierc_semantic_only', 'phase2_scierc_full_s1',\n    'phase2_docred_unconstrained', 'phase2_docred_grammar_only',\n    'phase2_docred_semantic_only', 'phase2_docred_full_s1',\n    'llama_scierc_unconstrained', 'llama_scierc_full_s1',\n    'llama_docred_unconstrained', 'llama_docred_full_s1',\n    'w6_mistral_scierc_unconstrained', 'w6_mistral_scierc_constrained',\n    'w6_mistral_docred_unconstrained', 'w6_mistral_docred_constrained',\n]\n\nfor eid in ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        print(json.dumps(metrics, indent=2)[:1500])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\"",
  "description": "Extract cross-model and ZS ablation metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "7ea462a1-d49f-4317-8e93-86e171377494",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxT97G4wnLzHjvJfM9t9kT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7512,
      "cache_read_input_tokens": 90026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7512
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

_source line 90 · 2026-05-23T10:48:51.202Z_

<details><summary>↩ Tool result · `toolu_01RBG2zAhpAnB6q7yn8vfZY3`</summary>

```text
=== phase2_scierc_unconstrained ===
{
  "json_parse_rate": 1,
  "entity_f1": 0.3101,
  "entity_precision": 0.2605,
  "entity_recall": 0.3831,
  "relation_f1": 0.0823,
  "relation_precision": 0.0644,
  "relation_recall": 0.114,
  "entity_type_violation_rate": 0.004,
  "relation_vocabulary_violation_rate": 0.0139,
  "domain_range_violation_rate": 0.1537,
  "cross_field_consistency_violation_rate": 0.0008,
  "total_triples": 1724,
  "total_entities": 2474,
  "total_samples": 551,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== phase2_scierc_grammar_only ===
{
  "total_samples": 551,
  "total_triples": 1725,
  "total_entities": 2474,
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.1484,
  "cross_field_consistency_violation_rate": 0.0008,
  "entity_f1": 0.3098,
  "entity_precision": 0.2598,
  "entity_recall": 0.3837,
  "relation_f1": 0.0823,
  "relation_precision": 0.0643,
  "relation_recall": 0.114,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== phase2_scierc_semantic_only ===
{
  "total_samples": 551,
  "total_triples": 1726,
  "total_entities": 2474,
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0.004,
  "relation_vocabulary_violation_rate": 0.0151,
  "domain_range_violation_rate": 0.1165,
  "cross_field_consistency_violation_rate": 0.0271,
  "entity_f1": 0.3101,
  "entity_precision": 0.2605,
  "entity_recall": 0.3831,
  "relation_f1": 0.0815,
  "relation_precision": 0.0637,
  "relation_recall": 0.1129,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== phase2_scierc_full_s1 ===
{
  "total_samples": 551,
  "total_triples": 1729,
  "total_entities": 2474,
  "json_parse_rate": 1,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0,
  "domain_range_violation_rate": 0.0093,
  "cross_field_consistency_violation_rate": 0.099,
  "entity_f1": 0.3098,
  "entity_precision": 0.2598,
  "entity_recall": 0.3837,
  "relation_f1": 0.0836,
  "relation_precision": 0.0654,
  "relation_recall": 0.116,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== phase2_docred_unconstrained ===
{
  "documents_checked": 986,
  "parse_failures": 12,
  "total_entities": 20171,
  "total_triples": 17497,
  "entity_type_violation_rate": 0.0248,
  "relation_vocabulary_violation_rate": 0.2966,
  "domain_range_violation_rate": 0.1846,
  "cross_field_consistency_violation_rate": 0.001,
  "entity_f1": 58.15,
  "entity_precision": 57.26,
  "entity_recall": 58.32,
  "relation_f1": 7.74,
  "relation_precision": 6.55,
  "relation_recall": 9.46,
  "unrecognized_relations": 5189,
  "f1_method": "all_set (includes OOV predictions in denominator)",
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)",
  "et_v1": 0.0818,
  "et_fix_note": "v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)"
}

=== phase2_docred_grammar_only ===
{
  "documents_checked": 985,
  "parse_failures": 13,
  "total_entities": 20150,
  "total_triples": 17341,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0.0003,
  "domain_range_violation_rate": 0.2617,
  "cross_field_consistency_violation_rate": 0.0007,
  "relation_f1": 8.31,
  "relation_precision": 7.06,
  "relation_recall": 10.12,
  "entity_f1": 59.38,
  "entity_precision": 58.47,
  "entity_recall": 60.32,
  "unrecognized_relations": 5,
  "f1_method": "all_set",
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== phase2_docred_semantic_only ===
{
  "documents_checked": 987,
  "parse_failures": 11,
  "total_entities": 20185,
  "total_triples": 17571,
  "entity_type_violation_rate": 0.0422,
  "relation_vocabulary_violation_rate": 0.2987,
  "domain_range_violation_rate": 0.1384,
  "cross_field_consistency_violation_rate": 0.0105,
  "entity_f1": 57.81,
  "entity_precision": 57.27,
  "entity_recall": 58.37,
  "relation_f1": 7.7,
  "relation_precision": 6.54,
  "relation_recall": 9.37,
  "f1_method": "all_set",
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)",
  "et_v1": 0.1044,
  "et_fix_note": "v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)"
}

=== phase2_docred_full_s1 ===
{
  "documents_checked": 987,
  "parse_failures": 11,
  "total_entities": 20187,
  "total_triples": 17341,
  "entity_type_violation_rate": 0,
  "relation_vocabulary_violation_rate": 0.0003,
  "domain_range_violation_rate": 0.1021,
  "cross_field_consistency_violation_rate": 0.0257,
  "entity_f1": 59.37,
  "entity_precision": 58.45,
  "entity_recall": 59.63,
  "relation_f1": 8.23,
  "relation_precision": 6.99,
  "relation_recall": 10.01,
  "unrecognized_relations": 5,
  "f1_method": "all_set",
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== llama_scierc_unconstrained ===
{
  "entity_type_violation_rate": 0,
  "relation_vocab_violation_rate": 0.0055,
  "domain_range_violation_rate": 0.1334,
  "cross_field_consistency_violations": 6,
  "entity_f1": 0.2356,
  "entity_precision": 0.1983,
  "entity_recall": 0.2902,
  "relation_f1": 0.0268,
  "relation_precision": 0.0236,
  "relation_recall": 0.031,
  "total_entities": 2451,
  "total_relations": 1274,
  "json_parse_failures": 1,
  "samples": 551,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== llama_scierc_full_s1 ===
{
  "samples": 550,
  "entities_extracted": 2469,
  "relations_extracted": 1315,
  "domain_range_violation_rate": 0.0008,
  "relation_vocab_violation_rate": 0,
  "entity_type_violation_rate": 0,
  "cross_field_consistency_violation_rate": 0.0656,
  "total_violation_rate": 0.0431,
  "entity_f1": 0.2349,
  "entity_precision": 0.1972,
  "entity_recall": 0.2902,
  "relation_f1": 0.0254,
  "relation_precision": 0.0221,
  "relation_recall": 0.0298,
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}

=== llama_docred_unconstrained ===
{
  "checker_version": "fixed_20260514_v2",
  "f1_method": "all_set",
  "documents": 998,
  "documents_checked": 930,
  "parse_failures": 68,
  "unique_entities": 11525,
  "total_triples": 16437,
  "dr_eligible_triples": 13789,
  "ET_rate_pct": 0.13,
  "RV_rate_pct": 16.03,
  "DR_rate_pct": 26.07,
  "CF_rate_pct": 0.17,
  "entity_precision": 61.22,
  "entity_recall": 51.02,
  "entity_f1": 55.65,
  "relation_precision": 5.22,
  "relation_recall": 7,
  "relation_f1": 5.98,
  "fuzzy_relation_matches": 121
}

=== llama_docred_full_s1 ===
{
  "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)",
  "f1_method": "all_set",
  "violations": {
    "ET": 0,
    "RV": 0,
    "DR": 2.55,
    "CF": 12.02
  },
  "f1": {
    "entity_f1": 55.01,
    "entity_precision": 61.41,
    "entity_recall": 49.82,
    "relation_f1": 6.27,
    "relation_precision": 5.49,
    "relation_recall": 7.32
  },
  "counts": {
    "documents": 998,
    "documents_checked": 907,
    "parse_failures": 91,
    "unique_entities": 11296,
    "triples": 16368
  }
}

=== w6_mistral_scierc_unconstrained ===
{
  "E_P": 0.2402,
  "E_R": 0.3156,
  "E_F1": 0.2728,
  "R_P": 0.0295,
  "R_R": 0.0483,
  "R_F1": 0.0366,
  "ET_pct": 1.5,
  "RV_pct": 0,
  "DR_pct": 56.94,
  "CF_pct": 56.87,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "total_pred_entities": 2202,
  "total_pred_relations": 1593
}

=== w6_mistral_scierc_constrained ===
{
  "E_P": 0.2437,
  "E_R": 0.3144,
  "E_F1": 0.2746,
  "R_P": 0.0292,
  "R_R": 0.0493,
  "R_F1": 0.0367,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 13.4,
  "CF_pct": 1.27,
  "CF_count": 21,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "total_pred_entities": 2162,
  "total_pred_relations": 1647,
  "delta_vs_unconstrained": {
    "delta_E_F1": 0.0018,
    "delta_R_F1": 0.0001,
    "delta_ET": -1.5,
    "delta_RV": 0,
    "delta_DR": -43.54,
    "note": "Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%"
  }
}

=== w6_mistral_docred_unconstrained ===
{
  "total_samples": 998,
  "parse_failures": 7,
  "parse_fail_rate": 0.7,
  "total_pred_entities": 12580,
  "total_pred_relations": 11879,
  "ET_pct": 7.58,
  "RV_pct": 42.35,
  "DR_pct": 57.42,
  "CF_pct": 24.78,
  "E_P": 0.6221,
  "E_R": 0.3975,
  "E_F1": 0.4851,
  "R_P": 0.0447,
  "R_R": 0.0432,
  "R_F1": 0.0434,
  "f1_method": "fuzzy_normalized",
  "f1_note": "Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance \u22642 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants)."
}

=== w6_mistral_docred_constrained ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 33.2,
  "CF_pct": 0.19,
  "E_P": 65.02,
  "E_R": 41.4,
  "E_F1": 50.59,
  "R_P": 5.67,
  "R_R": 5.37,
  "R_F1": 5.52,
  "parse_fail_rate": 0.8,
  "total_samples": 998,
  "total_pred_entities": 12535,
  "total_pred_relations": 11554,
  "delta_vs_unconstrained": {
    "ET_pct": -7.58,
    "RV_pct": -42.35,
    "DR_pct": -24.22,
    "CF_pct": -24.59,
    "E_F1": 2.08,
    "R_F1": 2.02
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "6db89aeb-14e9-4449-a20e-2275a3a71d74",
  "tool_use_result": {
    "stdout": "=== phase2_scierc_unconstrained ===\n{\n  \"json_parse_rate\": 1,\n  \"entity_f1\": 0.3101,\n  \"entity_precision\": 0.2605,\n  \"entity_recall\": 0.3831,\n  \"relation_f1\": 0.0823,\n  \"relation_precision\": 0.0644,\n  \"relation_recall\": 0.114,\n  \"entity_type_violation_rate\": 0.004,\n  \"relation_vocabulary_violation_rate\": 0.0139,\n  \"domain_range_violation_rate\": 0.1537,\n  \"cross_field_consistency_violation_rate\": 0.0008,\n  \"total_triples\": 1724,\n  \"total_entities\": 2474,\n  \"total_samples\": 551,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_scierc_grammar_only ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1725,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.1484,\n  \"cross_field_consistency_violation_rate\": 0.0008,\n  \"entity_f1\": 0.3098,\n  \"entity_precision\": 0.2598,\n  \"entity_recall\": 0.3837,\n  \"relation_f1\": 0.0823,\n  \"relation_precision\": 0.0643,\n  \"relation_recall\": 0.114,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_scierc_semantic_only ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1726,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0.004,\n  \"relation_vocabulary_violation_rate\": 0.0151,\n  \"domain_range_violation_rate\": 0.1165,\n  \"cross_field_consistency_violation_rate\": 0.0271,\n  \"entity_f1\": 0.3101,\n  \"entity_precision\": 0.2605,\n  \"entity_recall\": 0.3831,\n  \"relation_f1\": 0.0815,\n  \"relation_precision\": 0.0637,\n  \"relation_recall\": 0.1129,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_scierc_full_s1 ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1729,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0093,\n  \"cross_field_consistency_violation_rate\": 0.099,\n  \"entity_f1\": 0.3098,\n  \"entity_precision\": 0.2598,\n  \"entity_recall\": 0.3837,\n  \"relation_f1\": 0.0836,\n  \"relation_precision\": 0.0654,\n  \"relation_recall\": 0.116,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_docred_unconstrained ===\n{\n  \"documents_checked\": 986,\n  \"parse_failures\": 12,\n  \"total_entities\": 20171,\n  \"total_triples\": 17497,\n  \"entity_type_violation_rate\": 0.0248,\n  \"relation_vocabulary_violation_rate\": 0.2966,\n  \"domain_range_violation_rate\": 0.1846,\n  \"cross_field_consistency_violation_rate\": 0.001,\n  \"entity_f1\": 58.15,\n  \"entity_precision\": 57.26,\n  \"entity_recall\": 58.32,\n  \"relation_f1\": 7.74,\n  \"relation_precision\": 6.55,\n  \"relation_recall\": 9.46,\n  \"unrecognized_relations\": 5189,\n  \"f1_method\": \"all_set (includes OOV predictions in denominator)\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\",\n  \"et_v1\": 0.0818,\n  \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"\n}\n\n=== phase2_docred_grammar_only ===\n{\n  \"documents_checked\": 985,\n  \"parse_failures\": 13,\n  \"total_entities\": 20150,\n  \"total_triples\": 17341,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0.0003,\n  \"domain_range_violation_rate\": 0.2617,\n  \"cross_field_consistency_violation_rate\": 0.0007,\n  \"relation_f1\": 8.31,\n  \"relation_precision\": 7.06,\n  \"relation_recall\": 10.12,\n  \"entity_f1\": 59.38,\n  \"entity_precision\": 58.47,\n  \"entity_recall\": 60.32,\n  \"unrecognized_relations\": 5,\n  \"f1_method\": \"all_set\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_docred_semantic_only ===\n{\n  \"documents_checked\": 987,\n  \"parse_failures\": 11,\n  \"total_entities\": 20185,\n  \"total_triples\": 17571,\n  \"entity_type_violation_rate\": 0.0422,\n  \"relation_vocabulary_violation_rate\": 0.2987,\n  \"domain_range_violation_rate\": 0.1384,\n  \"cross_field_consistency_violation_rate\": 0.0105,\n  \"entity_f1\": 57.81,\n  \"entity_precision\": 57.27,\n  \"entity_recall\": 58.37,\n  \"relation_f1\": 7.7,\n  \"relation_precision\": 6.54,\n  \"relation_recall\": 9.37,\n  \"f1_method\": \"all_set\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\",\n  \"et_v1\": 0.1044,\n  \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"\n}\n\n=== phase2_docred_full_s1 ===\n{\n  \"documents_checked\": 987,\n  \"parse_failures\": 11,\n  \"total_entities\": 20187,\n  \"total_triples\": 17341,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0.0003,\n  \"domain_range_violation_rate\": 0.1021,\n  \"cross_field_consistency_violation_rate\": 0.0257,\n  \"entity_f1\": 59.37,\n  \"entity_precision\": 58.45,\n  \"entity_recall\": 59.63,\n  \"relation_f1\": 8.23,\n  \"relation_precision\": 6.99,\n  \"relation_recall\": 10.01,\n  \"unrecognized_relations\": 5,\n  \"f1_method\": \"all_set\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== llama_scierc_unconstrained ===\n{\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocab_violation_rate\": 0.0055,\n  \"domain_range_violation_rate\": 0.1334,\n  \"cross_field_consistency_violations\": 6,\n  \"entity_f1\": 0.2356,\n  \"entity_precision\": 0.1983,\n  \"entity_recall\": 0.2902,\n  \"relation_f1\": 0.0268,\n  \"relation_precision\": 0.0236,\n  \"relation_recall\": 0.031,\n  \"total_entities\": 2451,\n  \"total_relations\": 1274,\n  \"json_parse_failures\": 1,\n  \"samples\": 551,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== llama_scierc_full_s1 ===\n{\n  \"samples\": 550,\n  \"entities_extracted\": 2469,\n  \"relations_extracted\": 1315,\n  \"domain_range_violation_rate\": 0.0008,\n  \"relation_vocab_violation_rate\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0.0656,\n  \"total_violation_rate\": 0.0431,\n  \"entity_f1\": 0.2349,\n  \"entity_precision\": 0.1972,\n  \"entity_recall\": 0.2902,\n  \"relation_f1\": 0.0254,\n  \"relation_precision\": 0.0221,\n  \"relation_recall\": 0.0298,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== llama_docred_unconstrained ===\n{\n  \"checker_version\": \"fixed_20260514_v2\",\n  \"f1_method\": \"all_set\",\n  \"documents\": 998,\n  \"documents_checked\": 930,\n  \"parse_failures\": 68,\n  \"unique_entities\": 11525,\n  \"total_triples\": 16437,\n  \"dr_eligible_triples\": 13789,\n  \"ET_rate_pct\": 0.13,\n  \"RV_rate_pct\": 16.03,\n  \"DR_rate_pct\": 26.07,\n  \"CF_rate_pct\": 0.17,\n  \"entity_precision\": 61.22,\n  \"entity_recall\": 51.02,\n  \"entity_f1\": 55.65,\n  \"relation_precision\": 5.22,\n  \"relation_recall\": 7,\n  \"relation_f1\": 5.98,\n  \"fuzzy_relation_matches\": 121\n}\n\n=== llama_docred_full_s1 ===\n{\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\",\n  \"f1_method\": \"all_set\",\n  \"violations\": {\n    \"ET\": 0,\n    \"RV\": 0,\n    \"DR\": 2.55,\n    \"CF\": 12.02\n  },\n  \"f1\": {\n    \"entity_f1\": 55.01,\n    \"entity_precision\": 61.41,\n    \"entity_recall\": 49.82,\n    \"relation_f1\": 6.27,\n    \"relation_precision\": 5.49,\n    \"relation_recall\": 7.32\n  },\n  \"counts\": {\n    \"documents\": 998,\n    \"documents_checked\": 907,\n    \"parse_failures\": 91,\n    \"unique_entities\": 11296,\n    \"triples\": 16368\n  }\n}\n\n=== w6_mistral_scierc_unconstrained ===\n{\n  \"E_P\": 0.2402,\n  \"E_R\": 0.3156,\n  \"E_F1\": 0.2728,\n  \"R_P\": 0.0295,\n  \"R_R\": 0.0483,\n  \"R_F1\": 0.0366,\n  \"ET_pct\": 1.5,\n  \"RV_pct\": 0,\n  \"DR_pct\": 56.94,\n  \"CF_pct\": 56.87,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_pred_entities\": 2202,\n  \"total_pred_relations\": 1593\n}\n\n=== w6_mistral_scierc_constrained ===\n{\n  \"E_P\": 0.2437,\n  \"E_R\": 0.3144,\n  \"E_F1\": 0.2746,\n  \"R_P\": 0.0292,\n  \"R_R\": 0.0493,\n  \"R_F1\": 0.0367,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 13.4,\n  \"CF_pct\": 1.27,\n  \"CF_count\": 21,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_pred_entities\": 2162,\n  \"total_pred_relations\": 1647,\n  \"delta_vs_unconstrained\": {\n    \"delta_E_F1\": 0.0018,\n    \"delta_R_F1\": 0.0001,\n    \"delta_ET\": -1.5,\n    \"delta_RV\": 0,\n    \"delta_DR\": -43.54,\n    \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"\n  }\n}\n\n=== w6_mistral_docred_unconstrained ===\n{\n  \"total_samples\": 998,\n  \"parse_failures\": 7,\n  \"parse_fail_rate\": 0.7,\n  \"total_pred_entities\": 12580,\n  \"total_pred_relations\": 11879,\n  \"ET_pct\": 7.58,\n  \"RV_pct\": 42.35,\n  \"DR_pct\": 57.42,\n  \"CF_pct\": 24.78,\n  \"E_P\": 0.6221,\n  \"E_R\": 0.3975,\n  \"E_F1\": 0.4851,\n  \"R_P\": 0.0447,\n  \"R_R\": 0.0432,\n  \"R_F1\": 0.0434,\n  \"f1_method\": \"fuzzy_normalized\",\n  \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance \\u22642 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"\n}\n\n=== w6_mistral_docred_constrained ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 33.2,\n  \"CF_pct\": 0.19,\n  \"E_P\": 65.02,\n  \"E_R\": 41.4,\n  \"E_F1\": 50.59,\n  \"R_P\": 5.67,\n  \"R_R\": 5.37,\n  \"R_F1\": 5.52,\n  \"parse_fail_rate\": 0.8,\n  \"total_samples\": 998,\n  \"total_pred_entities\": 12535,\n  \"total_pred_relations\": 11554,\n  \"delta_vs_unconstrained\": {\n    \"ET_pct\": -7.58,\n    \"RV_pct\": -42.35,\n    \"DR_pct\": -24.22,\n    \"CF_pct\": -24.59,\n    \"E_F1\": 2.08,\n    \"R_F1\": 2.02\n  }\n}",
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

_source line 91_

<details><summary>Logged reasoning block</summary>

```text
Now I have the cross-model ZS data. Let me verify the cross-model table values.

**tab:cross-model (appendix_zs_crossmodel.tex)**

Paper says:
- SciERC/Qwen (U): DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23
- SciERC/Qwen (S1): DR=0.93, RV=0, ET=0, CF=9.90, R-F1=8.36

Registry phase2_scierc_unconstrained:


- DR=0.1537=15.37% ✅, RV=0.0139=1.39% ✅, ET=0.004=0.40% ✅, CF=0.0008=0.08% ✅
- R-F1=0.0823=8.23% ✅

Registry phase2_scierc_full_s1:
- DR=0.0093=0.93% ✅, RV=0, ET=0, CF=0.099=9.9% ✅
- R-F1=0.0836=8.36% ✅

All values match perfectly across both configurations.

Now checking the Llama unconstrained results—the metrics align with what the paper reports, including the cross-field consistency violations calculation that confirms the 0.24% figure. Moving on to the S1 variant with its notably higher cross-field error rate of 6.56%.

The Mistral models show a stark contrast: the unconstrained version has severe issues with a 56.94% deletion rate and 56.87% cross-field violations, while the S1 variant performs much better with only 13.40% deletions and 1.27% cross-field errors.

Now I'm checking the DocRED results with Qwen—the unconstrained model shows concerning patterns with 29.66% relation violations and 18.46% deletions, though the S1 variant improves significantly on the deletion rate down to 10.21%. Compiling the performance metrics for the remaining model configurations... Now I'm checking the ablation study results from the DocRED table—comparing the unconstrained baseline against the grammar, semantic, and S1 constraint variants, verifying that the registry values match the paper's reported metrics across all conditions. Finishing up the S1 metrics, and all the DocRED zero-shot ablation values are checking out. Now I'm carefully verifying the fine-tuning ablation table, starting with the SciERC/Qwen unconstrained results from the paper against what's in the registry.

The unconstrained baseline matches perfectly across all metrics. Moving on to the grammar-only variant, which also aligns with the paper's reported numbers. Now I'm checking the semantic variant results.

For the semantic-only configuration, I'm seeing a discrepancy with the CF metric. The registry shows 15 constraint failures, but when I calculate 15 divided by 1784 total instances, I get 0.841%, whereas the paper reports 0.18%. I'm wondering if the denominator might be different—perhaps it's calculated per-document rather than per-instance, or there's a different computation method entirely. Let me examine the semantic-only data more carefully to understand how the CF rate is being computed differently without the grammar layer. I'm trying to figure out what denominator would give 0.18% from the CF count of 15 — maybe it's calculated differently than I'm thinking, perhaps from entity-document pairs or some other metric in the registry that I'm not seeing clearly. But the discrepancy might be due to rounding or a slightly different calculation method. For Llama S1, the CF rate matches perfectly at 0.46%, which gives me confidence in the per-entity interpretation. Now I'm testing whether Qwen's semantic-only CF count of 0.18% could be explained by a different entity count—if the paper's 0.18% is accurate, that would suggest a CF_count around 3.

21, but the registry shows 15, which is a substantial gap. Looking more closely at the semantic-only experiment notes, I see references to delta metrics for DR rather than CF, so the CF_count=15 might have been computed differently than what the paper reports. I'm flagging this as a potential discrepancy and moving forward to check the remaining tables.

Rather than examining every single metric across all the tables, I should focus on the most problematic areas: the DocRED FT values with the parse-failure bug, the 70B model results, WikiEvents, and GoLLIE. Let me continue systematically through those.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "c37e016b-66d0-4af8-a717-6b27069c5b23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtSAwUY6ihzfwpBXZGJVty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11108,
      "cache_read_input_tokens": 97538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11108
      },
      "output_tokens": 10,
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

_source line 92_

Let me now query the beam search, WikiEvents, and remaining experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "8fc74095-b230-4d29-b93a-5813bded175f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtSAwUY6ihzfwpBXZGJVty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11108,
      "cache_read_input_tokens": 97538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11108
      },
      "output_tokens": 10,
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

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01CfeUoHT7684wewoTa72tD6`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Beam search experiments\nids = [\n    'beam_search_scierc_full_551',\n    'w9_qwen_scierc_zs_sampling', 'w9_qwen_docred_zs_sampling_r2',\n    'w10_beam_ablation_k2', 'w10_beam_ablation_k8',\n    'w10_qwen_scierc_ft_beam_4',\n    'w10_mistral_scierc_beam_551',\n    'w10_llama_docred_beam_50',\n    'w9_qwen_docred_beam_50', 'w9_llama_scierc_beam_551',\n    'w9_mistral_docred_beam_50',\n    'w10_type_consensus_prototype', 'w10_type_consensus_docred_50',\n    'r14_qwen_docred_beam4_998', 'r14_llama_docred_beam4_998',\n    'q1_llama_lora_scierc_beam4',\n    'd066_beam_sweep',\n    'd066_sweep_llama_scierc_beam1_unc',\n    'd066_sweep_llama_scierc_beam2_s1_551',\n    'd066_sweep_llama_scierc_beam4_s1_551',\n    'd066_sweep_llama_scierc_beam8_s1_551',\n    'd066_sweep_llama_beam2_s1',\n    'd066_sweep_llama_beam8_s1',\n    'd066_sweep_llama_beam8_unc',\n    'd066_sweep_llama_docred_beam1_unc',\n    'd066_sweep_llama_docred_beam4_unc',\n    'd066_sweep_llama_docred_beam4_s1',\n    'd062_beam_latency',\n]\n\nfor eid in ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        m_str = json.dumps(metrics, indent=2)\n        print(m_str[:2000])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\" 2>&1 | head -600",
  "description": "Extract beam search experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "2cb8161c-ac25-4556-a626-806dc10ac0c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtSAwUY6ihzfwpBXZGJVty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11108,
      "cache_read_input_tokens": 97538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11108
      },
      "output_tokens": 10,
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

_source line 94 · 2026-05-23T10:50:10.459Z_

<details><summary>↩ Tool result · `toolu_01CfeUoHT7684wewoTa72tD6`</summary>

```text
=== beam_search_scierc_full_551 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.53,
  "E_F1": 32,
  "R_F1": 8.56,
  "E_P": 26.83,
  "E_R": 39.63,
  "R_P": 6.69,
  "R_R": 11.91,
  "parse_fail_rate": 0,
  "total_entities": 2476,
  "total_relations": 1737
}

=== w9_qwen_scierc_zs_sampling ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.75,
  "CF_pct": 9.9,
  "E_F1": 31.28,
  "R_F1": 7.42,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "note": "F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36"
}

=== w9_qwen_docred_zs_sampling_r2 ===
{}

=== w10_beam_ablation_k2 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.35,
  "CF_count": 71,
  "CF_pct": 4.12,
  "E_F1": 31.54,
  "R_F1": 8.75,
  "parse_failures": 0,
  "total_samples": 551,
  "total_triples": 1724,
  "vs_greedy": {
    "DR_delta": -0.58,
    "CF_delta": -5.78,
    "E_F1_delta": 0.56,
    "R_F1_delta": 0.39,
    "note": "Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36"
  },
  "vs_beam_k4": {
    "DR_delta": 0.35,
    "CF_delta": 3.59,
    "E_F1_delta": -0.46,
    "R_F1_delta": 0.19,
    "note": "k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56"
  }
}

=== w10_beam_ablation_k8 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.08,
  "CF_count": 2,
  "E_F1": 32.18,
  "R_F1": 8.39,
  "E_P": 26.95,
  "E_R": 39.93,
  "R_P": 6.54,
  "R_R": 11.7,
  "parse_failures": 0,
  "total_samples": 551,
  "total_triples": 1744,
  "total_entities": 2483,
  "vs_greedy": {
    "DR_delta": -0.93,
    "CF_delta": -9.82,
    "E_F1_delta": 1.2,
    "R_F1_delta": 0.03
  },
  "vs_beam_k4": {
    "DR_delta": 0,
    "CF_delta": -0.45,
    "E_F1_delta": 0.18,
    "R_F1_delta": -0.17
  }
}

=== w10_qwen_scierc_ft_beam_4 ===
{
  "DR": 0,
  "CF": 0,
  "total_violation_rate": 0,
  "entity_type_violation_rate": 0,
  "relation_vocab_violation_rate": 0,
  "domain_range_violation_rate": 0,
  "cross_field_consistency_violation_rate": 0,
  "E_F1": 66.88,
  "E_P": 64.69,
  "E_R": 69.22,
  "R_F1": 44.23,
  "R_P": 39.41,
  "R_R": 50.41,
  "total_samples": 551,
  "json_parse_failures": 0,
  "total_entities": 1802,
  "total_relations": 1246,
  "vs_ft_greedy": {
    "baseline": "w5_lora_scierc_constrained_eval",
    "DR_delta": "0% \u2192 0% (same)",
    "CF_delta": "1.18% \u2192 0.0% (eliminated all violations)",
    "E_F1_delta": "67.05 \u2192 66.88 (-0.17, negligible)",
    "R_F1_delta": "43.77 \u2192 44.23 (+0.46, slight improvement)"
  },
  "vs_zs_beam_k4": {
    "DR_delta": "0% \u2192 0% (same)",
    "CF_delta": "0.53% \u2192 0.0% (eliminated)",
    "E_F1_delta": "32.00 \u2192 66.88 (+34.88)",
    "R_F1_delta": "8.56 \u2192 44.23 (+35.67)"
  }
}

=== w10_mistral_scierc_beam_551 ===
{
  "total_samples": 551,
  "parse_failures": 1,
  "parse_rate": 0.9982,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 13.79,
  "CF_pct": 0.57,
  "E_P": 23.04,
  "E_R": 31.64,
  "E_F1": 26.66,
  "R_P": 3.13,
  "R_R": 7.22,
  "R_F1": 4.37,
  "total_entities": 2294,
  "total_triples": 2241,
  "vs_greedy": {
    "baseline": "w6_mistral_scierc_constrained",
    "greedy_DR": 13.4,
    "greedy_CF": 1.27,
    "greedy_E_F1": 27.46,
    "greedy_R_F1": 3.67,
    "delta_DR": "+0.39pp",
    "delta_CF": "-0.70pp",
    "delta_E_F1": "-0.80pp",
    "delta_R_F1": "+0.70pp"
  }
}

=== w10_llama_docred_beam_50 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.94,
  "E_F1": 55.62,
  "R_F1": 9.47,
  "parse_failures": 3,
  "parse_fail_rate": 6,
  "total_samples": 50,
  "vs_greedy_full_s1": {
    "DR_delta": -2.57,
    "CF_delta": -11.19,
    "E_F1_delta": 0.61,
    "R_F1_delta": 3.2,
    "note": "Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27"
  },
  "checker_note": "Must use violation_checker_docred.py for DocRED (not violation_checker.py)"
}

=== w9_qwen_docred_beam_50 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.55,
  "E_F1": 58.64,
  "R_F1": 9.37,
  "total_samples": 50,
  "parse_failures": 3,
  "parse_fail_rate": 6,
  "vs_greedy_full_s1": {
    "DR_delta": -10.21,
    "CF_delta": -2.02,
    "E_F1_delta": -0.73,
    "R_F1_delta": 1.14,
    "note": "Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema."
  }
}

=== w9_llama_scierc_beam_551 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.93,
  "CF_count": 15,
  "E_F1": 25.04,
  "E_P": 21.27,
  "E_R": 30.42,
  "R_F1": 3.33,
  "R_P": 2.68,
  "R_R": 4.41,
  "total_entities": 2398,
  "total_relations": 1606,
  "parse_fail_rate": 0,
  "total_samples": 551,
  "vs_greedy_full_s1": {
    "DR_delta": -0.08,
    "CF_delta": -5.63,
    "E_F1_delta": 1.55,
    "R_F1_delta": 0.79,
    "note": "Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%"
  }
}

=== w9_mistral_docred_beam_50 ===
{
  "ET_violation_rate": 0,
  "RV_violation_rate": 0,
  "DR_violation_rate": 21.37,
  "CF_violations": 1,
  "total_triples": 524,
  "total_entities": 597,
  "docs_checked": 49,
  "parse_failures": 1,
  "E_F1": 51.78,
  "E_P": 65.2,
  "E_R": 42.94,
  "R_F1": 5.7,
  "R_P": 6.49,
  "R_R": 5.08,
  "R_tp": 34,
  "R_gold": 669,
  "R_pred": 524
}

=== w10_type_consensus_prototype ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.93,
  "CF_pct": 9.9,
  "E_F1": 30.98,
  "R_F1": 8.36,
  "gtc_skip_total": 672,
  "gtc_skip_unique_entities": 258,
  "gtc_effective_corrections": 0,
  "delta_DR": 0,
  "delta_CF": 0
}

=== w10_type_consensus_docred_50 ===
{
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 8.69,
  "CF_pct": 2.4,
  "E_F1": 59.08,
  "R_F1": 8.33,
  "gtc_skip_total": 601,
  "gtc_skip_unique_entities": 213,
  "gtc_effective_corrections": 0,
  "delta_DR": 0,
  "delta_CF": 0
}

=== r14_qwen_docred_beam4_998 ===
{
  "E_F1": 58.19,
  "R_F1": 8.72,
  "DR_pct": 0,
  "RV_pct": 0,
  "ET_pct": 0,
  "CF_pct": 4.94,
  "parse_fail_pct": 3.51,
  "samples": 998,
  "success": 963,
  "fail": 35
}

=== r14_llama_docred_beam4_998 ===
{
  "R_F1": 8.83,
  "E_F1": 57.81,
  "DR_pct": 0,
  "CF_pct": 1,
  "ET_pct": 0,
  "RV_pct": 0,
  "parse_fail_pct": 3.91,
  "samples": 998,
  "success": 959,
  "fail": 39,
  "baseline_ZS_greedy_R_F1": 6.27,
  "baseline_ZS_greedy_E_F1": 54.93,
  "baseline_ZS_greedy_DR_pct": 2.55,
  "baseline_ZS_greedy_CF_pct": 8.54
}

=== q1_llama_lora_scierc_beam4 ===
{
  "ET_violation_rate": 0,
  "RV_violation_rate": 0,
  "DR_violation_rate": 0,
  "CF_violation_rate": 0,
  "entity_f1": 67.94,
  "relation_f1": 46.11,
  "samples": 551,
  "total_entities": 1853,
  "total_relations": 727
}

=== d066_beam_sweep ===
{
  "scierc_qwen3_8b": {
    "k1_unc": {
      "E_F1": 66.88,
      "R_F1": 42.95,
      "DR_pct": 2.11,
      "CF_pct": 0,
      "avg_time": 2.494
    },
    "k1_con": {
      "E_F1": 66.88,
      "R_F1": 42.95,
      "DR_pct": 0,
      "CF_pct": 0.5,
      "avg_time": 2.932
    },
    "k2_unc": {
      "E_F1": 67.79,
      "R_F1": 44.75,
      "DR_pct": 1.54,
      "CF_pct": 0,
      "avg_time": 2.954
    },
    "k2_con": {
      "E_F1": 67.71,
      "R_F1": 44.6,
      "DR_pct": 0,
      "CF_pct": 0.11,
      "avg_time": 3.463
    },
    "k4_unc": {
      "E_F1": 67.49,
      "R_F1": 43.72,
      "DR_pct": 1.89,
      "CF_pct": 0,
      "avg_time": 3.485
    },
    "k4_con": {
      "E_F1": 67.22,
      "R_F1": 43.6,
      "DR_pct": 0,
      "CF_pct": 0,
      "avg_time": 4.069
    },
    "k8_unc": {
      "E_F1": 66.4,
      "R_F1": 43.17,
      "DR_pct": 1.77,
      "CF_pct": 0,
      "avg_time": 4.194
    },
    "k8_con": {
      "E_F1": 66.36,
      "R_F1": 43.65,
      "DR_pct": 0,
      "CF_pct": 0,
      "avg_time": 5.058
    }
  },
  "pareto_optimal": "k=2 con",
  "best_E_F1": {
    "config": "k=2 unc",
    "value": 67.79
  },
  "best_R_F1": {
    "config": "k=2 unc",
    "value": 44.75
  }
}

=== d066_sweep_llama_scierc_beam1_unc ===
{
  "total": 275,
  "success": 275,
  "fail": 0,
  "output_file": "llama_scierc_beam1_unconstrained.jsonl",
  "note": "INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized \u2014 must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun."
}

=== d066_sweep_llama_scierc_beam2_s1_551 ===
{
  "entity_f1": 68.34,
  "entity_p": 66.59,
  "entity_r": 70.17,
  "relation_f1": 46.12,
  "relation_p": 42.73,
  "relation_r": 50.1,
  "parse_fail_pct": 0,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0.17,
  "note": "ET/RV corrected from 100\u21920: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc"
}

=== d066_sweep_llama_scierc_beam4_s1_551 ===
{
  "E-F1": 68.06,
  "E-P": 65.96,
  "E-R": 70.29,
  "R-F1": 46.18,
  "R-P": 42.1,
  "R-R": 51.13,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0,
  "parse_fail": 0,
  "samples": 551,
  "note": "ET/RV corrected from 100\u21920: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc"
}

=== d066_sweep_llama_scierc_beam8_s1_551 ===
{
  "E-F1": 67.51,
  "E-P": 64.99,
  "E-R": 70.23,
  "R-F1": 44.95,
  "R-P": 40.1,
  "R-R": 51.13,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0,
  "CF_pct": 0,
  "PF_pct": 0,
  "samples": 551,
  "note": "Reconcile false positive corrected. Eval with --dataset scierc confirmed."
}

=== d066_sweep_llama_beam2_s1 ===
{
  "E_F1": 85.6,
  "E_P": 85.29,
  "E_R": 85.92,
  "R_F1": 51.17,
  "R_P": 48.51,
  "R_R": 54.14,
  "DR_pct": 0,
  "CF_pct": 0,
  "ET_pct": 0,
  "RV_pct": 0,
  "parse_fail_pct": 0.5,
  "total_samples": 200,
  "total_entities_pred": 3814,
  "total_relations_pred": 2839
}

=== d066_sweep_llama_beam8_s1 ===
{
  "E-F1": 85.76,
  "R-F1": 51.74,
  "DR_pct": 0,
  "CF_pct": 0,
  "PF_pct": 0.5,
  "samples": 200
}

=== d066_sweep_llama_beam8_unc ===
{
  "E_F1": 85.77,
  "E_P": 85.7,
  "E_R": 85.84,
  "R_F1": 51.97,
  "R_P": 49.76,
  "R_R": 54.38,
  "DR_pct": 0,
  "CF_pct": 0.05,
  "ET_pct": 0,
  "RV_pct": 0.07,
  "parse_fail_pct": 0.5,
  "total_samples": 200,
  "total_entities_pred": 3788,
  "total_relations_pred": 2779
}

=== d066_sweep_llama_docred_beam1_unc ===
{
  "total": 200,
  "success": 196,
  "fail": 4,
  "output_file": "llama_docred_200_beam1_unconstrained.jsonl"
}

=== d066_sweep_llama_docred_beam4_unc ===
{
  "E-F1": 85.67,
  "R-F1": 52.65,
  "DR_pct": 0.04,
  "CF_pct": 0.08,
  "PF_pct": 0.5,
  "samples": 200
}

=== d066_sweep_llama_docred_beam4_s1 ===
{
  "E-F1": 85.61,
  "E-P": 85.48,
  "E-R": 85.73,
  "R-F1": 51.89,
  "R-P": 51.59,
  "R-R": 52.2,
  "DR_pct": 0,
  "CF_pct": 0,
  "PF_pct": 0.5,
  "ET_pct": 0,
  "RV_pct": 0,
  "samples": 200,
  "parse_fail": 1
}

=== d062_beam_latency ===
{
  "beam4_unconstrained_s_per_doc": 3.446,
  "beam4_constrained_s_per_doc": 4.013,
  "beam4_unconstrained_total_s": 1898.7,
  "beam4_constrained_total_s": 2211,
  "beam_greedy_ratio_unconstrained": 1.319,
  "beam_greedy_ratio_constrained": 1.397,
  "constraint_overhead_beam": 1.165,
  "constraint_overhead_greedy": 1.1,
  "greedy_unconstrained_s_per_doc": 2.612,
  "greedy_constrained_s_per_doc": 2.873
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "ed1d9508-b7c5-4c72-9d89-e540c374804e",
  "tool_use_result": {
    "stdout": "=== beam_search_scierc_full_551 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.53,\n  \"E_F1\": 32,\n  \"R_F1\": 8.56,\n  \"E_P\": 26.83,\n  \"E_R\": 39.63,\n  \"R_P\": 6.69,\n  \"R_R\": 11.91,\n  \"parse_fail_rate\": 0,\n  \"total_entities\": 2476,\n  \"total_relations\": 1737\n}\n\n=== w9_qwen_scierc_zs_sampling ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.75,\n  \"CF_pct\": 9.9,\n  \"E_F1\": 31.28,\n  \"R_F1\": 7.42,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"note\": \"F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36\"\n}\n\n=== w9_qwen_docred_zs_sampling_r2 ===\n{}\n\n=== w10_beam_ablation_k2 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.35,\n  \"CF_count\": 71,\n  \"CF_pct\": 4.12,\n  \"E_F1\": 31.54,\n  \"R_F1\": 8.75,\n  \"parse_failures\": 0,\n  \"total_samples\": 551,\n  \"total_triples\": 1724,\n  \"vs_greedy\": {\n    \"DR_delta\": -0.58,\n    \"CF_delta\": -5.78,\n    \"E_F1_delta\": 0.56,\n    \"R_F1_delta\": 0.39,\n    \"note\": \"Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36\"\n  },\n  \"vs_beam_k4\": {\n    \"DR_delta\": 0.35,\n    \"CF_delta\": 3.59,\n    \"E_F1_delta\": -0.46,\n    \"R_F1_delta\": 0.19,\n    \"note\": \"k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56\"\n  }\n}\n\n=== w10_beam_ablation_k8 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.08,\n  \"CF_count\": 2,\n  \"E_F1\": 32.18,\n  \"R_F1\": 8.39,\n  \"E_P\": 26.95,\n  \"E_R\": 39.93,\n  \"R_P\": 6.54,\n  \"R_R\": 11.7,\n  \"parse_failures\": 0,\n  \"total_samples\": 551,\n  \"total_triples\": 1744,\n  \"total_entities\": 2483,\n  \"vs_greedy\": {\n    \"DR_delta\": -0.93,\n    \"CF_delta\": -9.82,\n    \"E_F1_delta\": 1.2,\n    \"R_F1_delta\": 0.03\n  },\n  \"vs_beam_k4\": {\n    \"DR_delta\": 0,\n    \"CF_delta\": -0.45,\n    \"E_F1_delta\": 0.18,\n    \"R_F1_delta\": -0.17\n  }\n}\n\n=== w10_qwen_scierc_ft_beam_4 ===\n{\n  \"DR\": 0,\n  \"CF\": 0,\n  \"total_violation_rate\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocab_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"E_F1\": 66.88,\n  \"E_P\": 64.69,\n  \"E_R\": 69.22,\n  \"R_F1\": 44.23,\n  \"R_P\": 39.41,\n  \"R_R\": 50.41,\n  \"total_samples\": 551,\n  \"json_parse_failures\": 0,\n  \"total_entities\": 1802,\n  \"total_relations\": 1246,\n  \"vs_ft_greedy\": {\n    \"baseline\": \"w5_lora_scierc_constrained_eval\",\n    \"DR_delta\": \"0% \\u2192 0% (same)\",\n    \"CF_delta\": \"1.18% \\u2192 0.0% (eliminated all violations)\",\n    \"E_F1_delta\": \"67.05 \\u2192 66.88 (-0.17, negligible)\",\n    \"R_F1_delta\": \"43.77 \\u2192 44.23 (+0.46, slight improvement)\"\n  },\n  \"vs_zs_beam_k4\": {\n    \"DR_delta\": \"0% \\u2192 0% (same)\",\n    \"CF_delta\": \"0.53% \\u2192 0.0% (eliminated)\",\n    \"E_F1_delta\": \"32.00 \\u2192 66.88 (+34.88)\",\n    \"R_F1_delta\": \"8.56 \\u2192 44.23 (+35.67)\"\n  }\n}\n\n=== w10_mistral_scierc_beam_551 ===\n{\n  \"total_samples\": 551,\n  \"parse_failures\": 1,\n  \"parse_rate\": 0.9982,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 13.79,\n  \"CF_pct\": 0.57,\n  \"E_P\": 23.04,\n  \"E_R\": 31.64,\n  \"E_F1\": 26.66,\n  \"R_P\": 3.13,\n  \"R_R\": 7.22,\n  \"R_F1\": 4.37,\n  \"total_entities\": 2294,\n  \"total_triples\": 2241,\n  \"vs_greedy\": {\n    \"baseline\": \"w6_mistral_scierc_constrained\",\n    \"greedy_DR\": 13.4,\n    \"greedy_CF\": 1.27,\n    \"greedy_E_F1\": 27.46,\n    \"greedy_R_F1\": 3.67,\n    \"delta_DR\": \"+0.39pp\",\n    \"delta_CF\": \"-0.70pp\",\n    \"delta_E_F1\": \"-0.80pp\",\n    \"delta_R_F1\": \"+0.70pp\"\n  }\n}\n\n=== w10_llama_docred_beam_50 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.94,\n  \"E_F1\": 55.62,\n  \"R_F1\": 9.47,\n  \"parse_failures\": 3,\n  \"parse_fail_rate\": 6,\n  \"total_samples\": 50,\n  \"vs_greedy_full_s1\": {\n    \"DR_delta\": -2.57,\n    \"CF_delta\": -11.19,\n    \"E_F1_delta\": 0.61,\n    \"R_F1_delta\": 3.2,\n    \"note\": \"Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27\"\n  },\n  \"checker_note\": \"Must use violation_checker_docred.py for DocRED (not violation_checker.py)\"\n}\n\n=== w9_qwen_docred_beam_50 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.55,\n  \"E_F1\": 58.64,\n  \"R_F1\": 9.37,\n  \"total_samples\": 50,\n  \"parse_failures\": 3,\n  \"parse_fail_rate\": 6,\n  \"vs_greedy_full_s1\": {\n    \"DR_delta\": -10.21,\n    \"CF_delta\": -2.02,\n    \"E_F1_delta\": -0.73,\n    \"R_F1_delta\": 1.14,\n    \"note\": \"Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema.\"\n  }\n}\n\n=== w9_llama_scierc_beam_551 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.93,\n  \"CF_count\": 15,\n  \"E_F1\": 25.04,\n  \"E_P\": 21.27,\n  \"E_R\": 30.42,\n  \"R_F1\": 3.33,\n  \"R_P\": 2.68,\n  \"R_R\": 4.41,\n  \"total_entities\": 2398,\n  \"total_relations\": 1606,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"vs_greedy_full_s1\": {\n    \"DR_delta\": -0.08,\n    \"CF_delta\": -5.63,\n    \"E_F1_delta\": 1.55,\n    \"R_F1_delta\": 0.79,\n    \"note\": \"Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%\"\n  }\n}\n\n=== w9_mistral_docred_beam_50 ===\n{\n  \"ET_violation_rate\": 0,\n  \"RV_violation_rate\": 0,\n  \"DR_violation_rate\": 21.37,\n  \"CF_violations\": 1,\n  \"total_triples\": 524,\n  \"total_entities\": 597,\n  \"docs_checked\": 49,\n  \"parse_failures\": 1,\n  \"E_F1\": 51.78,\n  \"E_P\": 65.2,\n  \"E_R\": 42.94,\n  \"R_F1\": 5.7,\n  \"R_P\": 6.49,\n  \"R_R\": 5.08,\n  \"R_tp\": 34,\n  \"R_gold\": 669,\n  \"R_pred\": 524\n}\n\n=== w10_type_consensus_prototype ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.93,\n  \"CF_pct\": 9.9,\n  \"E_F1\": 30.98,\n  \"R_F1\": 8.36,\n  \"gtc_skip_total\": 672,\n  \"gtc_skip_unique_entities\": 258,\n  \"gtc_effective_corrections\": 0,\n  \"delta_DR\": 0,\n  \"delta_CF\": 0\n}\n\n=== w10_type_consensus_docred_50 ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 8.69,\n  \"CF_pct\": 2.4,\n  \"E_F1\": 59.08,\n  \"R_F1\": 8.33,\n  \"gtc_skip_total\": 601,\n  \"gtc_skip_unique_entities\": 213,\n  \"gtc_effective_corrections\": 0,\n  \"delta_DR\": 0,\n  \"delta_CF\": 0\n}\n\n=== r14_qwen_docred_beam4_998 ===\n{\n  \"E_F1\": 58.19,\n  \"R_F1\": 8.72,\n  \"DR_pct\": 0,\n  \"RV_pct\": 0,\n  \"ET_pct\": 0,\n  \"CF_pct\": 4.94,\n  \"parse_fail_pct\": 3.51,\n  \"samples\": 998,\n  \"success\": 963,\n  \"fail\": 35\n}\n\n=== r14_llama_docred_beam4_998 ===\n{\n  \"R_F1\": 8.83,\n  \"E_F1\": 57.81,\n  \"DR_pct\": 0,\n  \"CF_pct\": 1,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"parse_fail_pct\": 3.91,\n  \"samples\": 998,\n  \"success\": 959,\n  \"fail\": 39,\n  \"baseline_ZS_greedy_R_F1\": 6.27,\n  \"baseline_ZS_greedy_E_F1\": 54.93,\n  \"baseline_ZS_greedy_DR_pct\": 2.55,\n  \"baseline_ZS_greedy_CF_pct\": 8.54\n}\n\n=== q1_llama_lora_scierc_beam4 ===\n{\n  \"ET_violation_rate\": 0,\n  \"RV_violation_rate\": 0,\n  \"DR_violation_rate\": 0,\n  \"CF_violation_rate\": 0,\n  \"entity_f1\": 67.94,\n  \"relation_f1\": 46.11,\n  \"samples\": 551,\n  \"total_entities\": 1853,\n  \"total_relations\": 727\n}\n\n=== d066_beam_sweep ===\n{\n  \"scierc_qwen3_8b\": {\n    \"k1_unc\": {\n      \"E_F1\": 66.88,\n      \"R_F1\": 42.95,\n      \"DR_pct\": 2.11,\n      \"CF_pct\": 0,\n      \"avg_time\": 2.494\n    },\n    \"k1_con\": {\n      \"E_F1\": 66.88,\n      \"R_F1\": 42.95,\n      \"DR_pct\": 0,\n      \"CF_pct\": 0.5,\n      \"avg_time\": 2.932\n    },\n    \"k2_unc\": {\n      \"E_F1\": 67.79,\n      \"R_F1\": 44.75,\n      \"DR_pct\": 1.54,\n      \"CF_pct\": 0,\n      \"avg_time\": 2.954\n    },\n    \"k2_con\": {\n      \"E_F1\": 67.71,\n      \"R_F1\": 44.6,\n      \"DR_pct\": 0,\n      \"CF_pct\": 0.11,\n      \"avg_time\": 3.463\n    },\n    \"k4_unc\": {\n      \"E_F1\": 67.49,\n      \"R_F1\": 43.72,\n      \"DR_pct\": 1.89,\n      \"CF_pct\": 0,\n      \"avg_time\": 3.485\n    },\n    \"k4_con\": {\n      \"E_F1\": 67.22,\n      \"R_F1\": 43.6,\n      \"DR_pct\": 0,\n      \"CF_pct\": 0,\n      \"avg_time\": 4.069\n    },\n    \"k8_unc\": {\n      \"E_F1\": 66.4,\n      \"R_F1\": 43.17,\n      \"DR_pct\": 1.77,\n      \"CF_pct\": 0,\n      \"avg_time\": 4.194\n    },\n    \"k8_con\": {\n      \"E_F1\": 66.36,\n      \"R_F1\": 43.65,\n      \"DR_pct\": 0,\n      \"CF_pct\": 0,\n      \"avg_time\": 5.058\n    }\n  },\n  \"pareto_optimal\": \"k=2 con\",\n  \"best_E_F1\": {\n    \"config\": \"k=2 unc\",\n    \"value\": 67.79\n  },\n  \"best_R_F1\": {\n    \"config\": \"k=2 unc\",\n    \"value\": 44.75\n  }\n}\n\n=== d066_sweep_llama_scierc_beam1_unc ===\n{\n  \"total\": 275,\n  \"success\": 275,\n  \"fail\": 0,\n  \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\",\n  \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized \\u2014 must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"\n}\n\n=== d066_sweep_llama_scierc_beam2_s1_551 ===\n{\n  \"entity_f1\": 68.34,\n  \"entity_p\": 66.59,\n  \"entity_r\": 70.17,\n  \"relation_f1\": 46.12,\n  \"relation_p\": 42.73,\n  \"relation_r\": 50.1,\n  \"parse_fail_pct\": 0,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.17,\n  \"note\": \"ET/RV corrected from 100\\u21920: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"\n}\n\n=== d066_sweep_llama_scierc_beam4_s1_551 ===\n{\n  \"E-F1\": 68.06,\n  \"E-P\": 65.96,\n  \"E-R\": 70.29,\n  \"R-F1\": 46.18,\n  \"R-P\": 42.1,\n  \"R-R\": 51.13,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"parse_fail\": 0,\n  \"samples\": 551,\n  \"note\": \"ET/RV corrected from 100\\u21920: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"\n}\n\n=== d066_sweep_llama_scierc_beam8_s1_551 ===\n{\n  \"E-F1\": 67.51,\n  \"E-P\": 64.99,\n  \"E-R\": 70.23,\n  \"R-F1\": 44.95,\n  \"R-P\": 40.1,\n  \"R-R\": 51.13,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"PF_pct\": 0,\n  \"samples\": 551,\n  \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"\n}\n\n=== d066_sweep_llama_beam2_s1 ===\n{\n  \"E_F1\": 85.6,\n  \"E_P\": 85.29,\n  \"E_R\": 85.92,\n  \"R_F1\": 51.17,\n  \"R_P\": 48.51,\n  \"R_R\": 54.14,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"parse_fail_pct\": 0.5,\n  \"total_samples\": 200,\n  \"total_entities_pred\": 3814,\n  \"total_relations_pred\": 2839\n}\n\n=== d066_sweep_llama_beam8_s1 ===\n{\n  \"E-F1\": 85.76,\n  \"R-F1\": 51.74,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"PF_pct\": 0.5,\n  \"samples\": 200\n}\n\n=== d066_sweep_llama_beam8_unc ===\n{\n  \"E_F1\": 85.77,\n  \"E_P\": 85.7,\n  \"E_R\": 85.84,\n  \"R_F1\": 51.97,\n  \"R_P\": 49.76,\n  \"R_R\": 54.38,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0.05,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.07,\n  \"parse_fail_pct\": 0.5,\n  \"total_samples\": 200,\n  \"total_entities_pred\": 3788,\n  \"total_relations_pred\": 2779\n}\n\n=== d066_sweep_llama_docred_beam1_unc ===\n{\n  \"total\": 200,\n  \"success\": 196,\n  \"fail\": 4,\n  \"output_file\": \"llama_docred_200_beam1_unconstrained.jsonl\"\n}\n\n=== d066_sweep_llama_docred_beam4_unc ===\n{\n  \"E-F1\": 85.67,\n  \"R-F1\": 52.65,\n  \"DR_pct\": 0.04,\n  \"CF_pct\": 0.08,\n  \"PF_pct\": 0.5,\n  \"samples\": 200\n}\n\n=== d066_sweep_llama_docred_beam4_s1 ===\n{\n  \"E-F1\": 85.61,\n  \"E-P\": 85.48,\n  \"E-R\": 85.73,\n  \"R-F1\": 51.89,\n  \"R-P\": 51.59,\n  \"R-R\": 52.2,\n  \"DR_pct\": 0,\n  \"CF_pct\": 0,\n  \"PF_pct\": 0.5,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"samples\": 200,\n  \"parse_fail\": 1\n}\n\n=== d062_beam_latency ===\n{\n  \"beam4_unconstrained_s_per_doc\": 3.446,\n  \"beam4_constrained_s_per_doc\": 4.013,\n  \"beam4_unconstrained_total_s\": 1898.7,\n  \"beam4_constrained_total_s\": 2211,\n  \"beam_greedy_ratio_unconstrained\": 1.319,\n  \"beam_greedy_ratio_constrained\": 1.397,\n  \"constraint_overhead_beam\": 1.165,\n  \"constraint_overhead_greedy\": 1.1,\n  \"greedy_unconstrained_s_per_doc\": 2.612,\n  \"greedy_constrained_s_per_doc\": 2.873\n}",
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

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
Let me now verify the beam search tables:

**tab:beam-search (beam_search, 50-doc subsets)**

Paper says:
- Qwen/SciERC/Greedy: ET=0, RV=0, DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36
- Qwen/SciERC/Beam4: ET=0, RV=0, DR=0, CF=0.53, E-F1=32.00, R-F1=8.56

Registry phase2_scierc_full_s1: DR=0.0093=0.93% ✅, CF=0.099=9.90% ✅, E-F1=0.3098*100=30.98 ✅, R-F1=0.0836

*100=8.36 ✅
Registry beam_search_scierc_full_551: DR=0 ✅, CF=0.53% ✅, E-F1=32 ✅, R-F1=8.56 ✅

Now checking the DocRED results with the 50-doc subset. The greedy approach shows ET=0, RV=0, DR=8.69, CF=2.08, E-F1=59.08, R-F1=8.33, but when I look up the registry entry for w10_type_consensus_docred_50, the DR and E-F1 match perfectly, though there's a discrepancy with CF—the paper reports 2.08 but the registry shows 2.4, so I need to investigate that mismatch.

Looking at the beam search comparison notes, the full 998-doc greedy baseline has different metrics than the 50-doc subset, which explains why I'm seeing variations. The 50-doc greedy experiment appears to be the one I should be validating against, not the larger dataset.

Now I'm checking whether the beam results actually match the paper's reported numbers. The Qwen DocRED 50-doc beam search results are aligning perfectly with the registry values across all metrics.

For Llama on SciERC, both the greedy baseline and beam search results are matching up as well—the registry entries show the same error rates, conflict scores, and F1 scores when converted from decimal to percentage format.

Now I'm checking the DocRED results with the 50-document subset. The paper reports DR=1.58, CF=6.85, E-F1=55.35, R-F1=6.12 for the greedy baseline, but my notes from the experiment show different values: DR=2.57%, CF=12.13%, E-F1=55.01, R-F1=6.27. These don't align with what the paper claims, and I'm trying to figure out where the discrepancy is coming from.

Looking at the paper's table caption, it specifies that the results are from "matched 50-document subsets (same documents for greedy and beam)," meaning the greedy baseline values should be computed on the exact same 50 documents used in the beam-search experiment. The 50-doc greedy values were likely generated as part of that beam experiment run rather than stored separately in the registry, so I can't directly verify them against my records.

I'll move forward with checking the other beam tables instead.

Now examining the Qwen SciERC beam ablation results across different beam widths. The k=1 greedy baseline matches perfectly across all metrics—DR, CF, E-F1, and R-F1 all align with the registry entry for phase2_scierc_full_s1.

Checking the remaining beam widths: k=2 through k=8 all validate successfully against their corresponding registry entries, with each metric matching exactly. The complete beam ablation ablation is confirmed across all configurations.

Now I'm verifying the Qwen SciERC LoRA beam sweep results from the paper, comparing both unconstrained and constrained variants across different beam widths to ensure the reported metrics align with what we have on file. Looking at the performance metrics across different k values and configurations, all the results are passing their validation checks with solid F1 scores and acceptable latency and reliability measurements. Now I'm verifying the latency scaling factors by dividing each timing against the baseline, and they're all matching the expected relative values.

Moving on to the DocRED beam search results—I'm checking the Qwen and Llama configurations against the paper's reported metrics for error types, conflict cases, and F1 scores. The Qwen registry entry matches perfectly across all fields, and I'm confirming the Llama values as well.

Now I'm looking at the LoRA fine-tuned results, comparing the greedy and beam-4 configurations for Qwen. I found the greedy variant in the registry but I'm noticing a discrepancy in the conflict case percentage—the paper reports 0.22 but the registry shows 8.52, which doesn't align. I'm noticing the ft-ablation table shows PF=8.52% for Qwen DocRED S1, which aligns with the registry, but the beam-docred-lora table lists PF=7.8% for the same model with greedy decoding—these might be from different experimental setups or the 7.8% could be calculated on a subset rather than the full dataset. I'm having trouble locating the specific experiment ID for the Qwen Beam-4 constrained row from the paper, even though I can see the metrics listed. For the Llama DocRED LoRA greedy results, I notice the paper reports CF=0.26, which I need to verify against the registry data.

Looking at the corrected registry values for w5_llama_docred_lora_constrained_eval, there are notable discrepancies: the paper shows E-F1=84.71 versus the registry's 83.94 (a 0.77 percentage point difference), R-F1=44.70 versus 43.78 (0.92pp difference), and CF=0.26 versus 0.21. These gaps suggest the paper values come from before the parse-failure bug correction was applied.

Now checking the Beam-4 results for Llama, the paper reports E-F1=85.23 and R-F1=47.17, but the registry entry d066_sweep_llama_docred_beam4_s1 shows E-F1=85.61 and R-F1=51.89—a substantial 4.72 percentage point gap in recall that needs investigation.

The issue is that d066_sweep is for 200 documents while the beam-docred-lora table uses 998 dev documents, so this registry entry doesn't match the paper's experimental setup. I'm searching through the registry for a corresponding 998-doc beam4 LoRA experiment for Llama but haven't found one yet.

Now checking the Mistral beam results against the registry—the greedy SciERC values match perfectly, but I need to verify the beam4 variant as well. Now I'm checking the baseline results for the 50-doc greedy experiment against the paper, but I don't have a matching registry entry to verify those numbers. Moving on to the latency metrics, I'm comparing the beam search and greedy decoding times from the paper with the registry values I have, and the greedy variants are matching perfectly so far.

All the beam-4 latency measurements check out too, and the computed ratios all align with what the paper reports. Now I'm moving into the GoLLIE comparison table to verify those results as well. Now I'm verifying the full fine-tuning results against the paper, comparing the unconstrained and constrained variants across different methods like standard fine-tuning and LoRA, checking that the entity F1 scores and other metrics align properly. I'm noticing discrepancies between the evaluation results across different tables—the LoRA unconstrained metrics vary depending on which table I'm looking at, and the dropout rates don't match between the full fine-tuning and fine-tuning ablation tables. The S1 results align between tables, but the unconstrained LoRA metrics diverge significantly—the ft-ablation reports DR=1.95 while the full-ft table shows DR=0.31, suggesting these might be from different experimental runs or evaluation settings. The LoRA metrics in the full-ft table don't match what I'm seeing in the registry entries—the R-F1 values are close but the DR percentages are wildly different (0.31% vs 1.95%), suggesting these might be from different LoRA checkpoints or experiments entirely. I need to flag this inconsistency since the full-ft table's LoRA row appears to be pulling from an older or different run than what's documented in the registry.

Now let me check the WikiEvents results and consolidate all the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "07d9ff08-8da7-40fb-84ac-4b20d6379c6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqQaNTH6SCBJBXScXaukdn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 108646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10965
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

_source line 96_

Let me now check WikiEvents, TCR, and other remaining experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "3f7b560d-8bd2-4409-ba35-0f5ba67fb7fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqQaNTH6SCBJBXScXaukdn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 108646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10965
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_018BteM1QV1QpizKU1DZoV2B`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/49c451d1-d5da-4e97-ad4f-6fd660d56a96/tool-results/mcp-agent-ml-research-read_registry-1779533019341.txt\"\npython3 -c \"\nimport json\n\nwith open('${REGFILE}') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# WikiEvents, TCR, posthoc, trie, vllm, prompt sensitivity\nids = [\n    'ee_qwen_wikievents_unconstrained', 'ee_llama_wikievents_unconstrained',\n    'ee_mistral_wikievents_unconstrained',\n    'ee_qwen_wikievents_constrained_v3', 'ee_llama_wikievents_constrained_v3',\n    'ee_mistral_wikievents_constrained_v3',\n    'ee_mistral_wikievents_grammar_only_v3',\n    'ee_qwen_wikievents_constrained', 'ee_llama_wikievents_constrained',\n    'ee_mistral_wikievents_constrained_v2',\n    'd065_tcr_pilot', 'd065_tcr_full',\n    'posthoc_filtering_baseline', 'w8_ft_posthoc_baseline',\n    'r16_trie_qwen_ft_scierc', 'r16_trie_llama_ft_scierc',\n    'r16_trie_qwen_zs_scierc', 'r16_trie_llama_zs_scierc',\n    'vllm_guided_json_scierc_zs',\n    'r4_prompt_minimal', 'r4_prompt_detailed',\n    'p1_ee_ft_composability_r5',\n    'w1_cf_fallback_scierc_pilot',\n    'd062_ontology_scalability',\n    'p8c_ft_scierc_latency',\n]\n\nfor eid in ids:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'\\\\n=== {eid} ===')\n        metrics = exp.get('metrics', {})\n        m_str = json.dumps(metrics, indent=2)\n        print(m_str[:2000])\n    else:\n        print(f'\\\\n=== {eid} === NOT FOUND')\n\" 2>&1 | head -800",
  "description": "Extract WikiEvents, TCR, and remaining experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49c451d1-d5da-4e97-ad4f-6fd660d56a96",
  "uuid": "c7d5dc30-701e-4bb8-acc0-c2de695fe9a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqQaNTH6SCBJBXScXaukdn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10965,
      "cache_read_input_tokens": 108646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10965
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
