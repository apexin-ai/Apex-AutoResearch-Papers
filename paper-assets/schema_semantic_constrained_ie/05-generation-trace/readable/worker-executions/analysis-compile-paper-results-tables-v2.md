# analysis compile paper results tables v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/workers/worker_analysis_compile_paper_results_tables_v2_20260516T164337.log`
- **Structured JSON:** [`ab96b8bfce81210ccb5b.json`](../../sessions/ab/ab96b8bfce81210ccb5b.json)

## Before a recorded user message

79 recorded events

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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "1c578aab-d33d-4b1b-99f2-b6b1832126c2",
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
    "resetsAt": 1778962800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "86e7514e-445b-4edf-a9a5-639cad346bfa",
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry to understand what experiments and metrics are available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "e01e6156-a3a1-472e-bd7a-bf2f1ff8c8aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1MXGzVi1Aufm1VhseQiqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11869
      },
      "output_tokens": 29,
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

I'll read the registry to get all experiment metrics, then compile the tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "375a8831-4513-487e-8a2a-db3f97f48e37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1MXGzVi1Aufm1VhseQiqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11869
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015GKH8QESSxYuaL3qdNsJew`</summary>

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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "cb53444d-1af5-4b39-8dec-e53ba19aa1f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1MXGzVi1Aufm1VhseQiqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11869
      },
      "output_tokens": 29,
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

_source line 7 · 2026-05-16T16:43:48.243Z_

<details><summary>↩ Tool result · `toolu_015GKH8QESSxYuaL3qdNsJew`</summary>

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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "3f1e792c-8acd-406d-b648-4c7d6945f4b4",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me read the registry to get all experiments for this project.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "acb55f2a-a373-4d71-88f8-22c42870488b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dhwa5JsbFB17APSnrJxoMa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 23710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017PncxiuQSg2z7urVmTVsAJ`</summary>

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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "f19c68f7-9ada-4e1e-9fce-8ec5931053a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dhwa5JsbFB17APSnrJxoMa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 23710,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 10 · 2026-05-16T16:43:52.709Z_

<details><summary>↩ Tool result · `toolu_017PncxiuQSg2z7urVmTVsAJ`</summary>

```text
Error: result (122,418 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt in sequential chunks until 100% of the content has been read.
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "84325358-cec8-470b-abb2-02f8cae8495a",
  "tool_use_result": {
    "content": "Error: result (122,418 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-16T16:22:28.075Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablation 有 Qwen 双模式数据。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"python run_constrained_extraction.py --mode semantic_only --dataset docred --model /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"server\": \"westd-21461\", \"data_path\": \"data/docred\", \"data_count\": 998, \"model_name\": \"qwen_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"qwen_lora_docred_merged\", \"eval_data\": \"docred_test_998\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_semantic_only.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T16:18:27.113Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T16:18:29.130284+00:00\"}]}, \"metrics\": {\"E_F1\": 82.15, \"E_P\": 85.58, \"E_R\": 78.99, \"R_F1\": 40.89, \"R_P\": 36.35, \"R_R\": 46.73, \"ET_pct\": 0, \"RV_pct\": 0.23, \"DR_pct\": 0.21, \"CF_pct\": 0.27, \"parse_fail_rate\": 7.52, \"total_samples\": 998, \"parse_failures\": 75, \"documents_checked\": 923, \"total_entities\": 18025, \"total_triples\": 15909, \"DR_violations\": 34, \"RV_violations\": 37, \"ET_violations\": 0, \"CF_violations\": 49}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:22:28.075Z\"}, \"w8_qwen_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:13:03.945Z\", \"updated_at\": \"2026-05-16T15:25:52.761Z\", \"hypothesis\": \"FT Qwen DocRED + grammar_only eval: FT 后 DR 残留 0.76%，grammar_only 能消除多少？与 w8_llama_docred_ft_grammar_only 配对，补全 DocRED FT ablation 两模型对比。预期 DR≈0.76%（与 SciERC 模式一致：grammar 层不约束 DR）。\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_qwen_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-21461\", \"gpu\": 0, \"pid\": 18555, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log\", \"submitted_at\": \"2026-05-16T09:27:52.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path_final\": \"~/runs/schema_semantic_constrained_ie/w8_qwen_docred_ft_grammar_only.log\", \"wall_clock_seconds\": 21480.4, \"gpu_hours\": 5.97}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:20:38.652Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:20:40.840918+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}, \"completed_at\": \"2026-05-16T15:25:52.761Z\"}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:54:02.910Z\", \"updated_at\": \"2026-05-16T13:15:05.364Z\", \"hypothesis\": \"FT Llama DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.49% 降至 ~0.2-0.3%（参照 SciERC 模式：semantic_only 降 DR 42%）。完成后 DocRED FT ablation 有 Llama 双模式数据，2 模型 ×2 模式全部完备。\", \"parent\": \"w5_llama_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": 1, \"pid\": 361202, \"model_name\": \"Llama-3.1-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.909Z\", \"updated_at\": \"2026-05-16T12:31:40.780Z\", \"hypothesis\": \"FT Llama DocRED + grammar_only eval: FT 后 DR 残留 0.49%，grammar_only 能消除多少？如果 grammar_only 已足够则 semantic 层在 FT regime 边际价值小；如果不够则两层在 FT 后仍互补。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w8_llama_docred_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"llama_lora_docred_merged\", \"seed\": 42, \"checkpoint_source\": \"w5_llama_docred_lora\", \"eval_data\": \"docred_dev_998\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"log_path\": \"/tmp/w8_llama_docred_ft_grammar_only.log\", \"completed_at\": \"2026-05-16T12:31:33.933Z\", \"metrics\": {\"E_F1\": 84.04, \"R_F1\": 43.77, \"entity_precision\": 84.99, \"entity_recall\": 83.11, \"relation_precision\": 38.6, \"relation_recall\": 50.53, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.51, \"CF_pct\": 0.12, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_relations\": 16199, \"unique_entities\": 13225, \"parse_failures\": 23}}, \"w6_mistral_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:59:02.565Z\", \"updated_at\": \"2026-05-16T10:41:37.382Z\", \"hypothesis\": \"Mistral (3rd model) SciERC unconstrained baseline — 获取 zero-shot violation profile (DR/RV/ET) 和 F1，验证 OntoCoDec 三模型泛化性\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w6_mistral_scierc_unconstrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"pid\": 332156, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_scierc_unconstrained.log\", \"submitted_at\": \"2026-05-16T04:53:56.502Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"wall_clock_seconds\": 2104.7, \"gpu_hours\": 0.58, \"checkpoint_path\": \"N/A\"}, \"notes\": \"Mistral-7B unconstrained SciERC: E_F1=0.2728, R_F1=0.0366. 0% parse failures. 56.94% dangling relations, 1.5% ET violations, 0% RV violations. Poor IE performance typical of unconstrained 7B model on SciERC.\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:27:35.554Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:27:39.086911+00:00\"}]}, \"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w6_mistral_scierc_unconstrained.jsonl\", \"completed_at\": \"2026-05-16T05:29:01.251Z\"}, \"w6_mistral_scierc_constrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T02:59:03.181Z\", \"updated_at\": \"2026-05-16T10:40:00.429Z\", \"hypothesis\": \"Mistral-7B constrained SciERC (full_s1 mode) - test if schema constraints reduce violations and improve F1 vs unconstrained baseline (E_F1=0.2728, R_F1=0.0366, DR=56.94%)\", \"failure_reason\": \"TypeError: xgrammar.GrammarMatcher.accept_token expected int but got ffi.Tensor. xgrammar/tvm version mismatch on westd-21461. Crashed 10s after start.\", \"completed_at\": \"2026-05-16T05:28:06.343Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w6_mistral_scierc_constrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"pid\": 334606, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_scierc_constrained.log\"}, \"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}, \"notes\": \"Mistral-7B constrained SciERC: 551/551 complete, 0 failures. OntoCoDec eliminated ET (1.5%→0%) and RV (0%→0%), reduced DR massively (56.94%→13.4%, -43.54pp). F1 unchanged (E_F1=0.2746 vs 0.2728, R_F1=0.0367 vs 0.0366). Residual DR 13.4% much higher than FT models (~1-2%), consistent with zero-shot regime needing stronger semantic constraints.\", \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\"}, \"w8_ft_posthoc_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:34:25.203Z\", \"updated_at\": \"2026-05-16T09:35:31.720Z\", \"hypothesis\": \"FT 后 DR<2%，post-hoc filtering 能否替代 OntoCoDec？对 4 组 FT unconstrained output 跑 posthoc_filter.py，量化 recall 损失和 coverage 代价。预期：post-hoc 过滤虽消除 DR 但丢失 TP（recall 下降），证明 constrained decoding 的 generation-time 优势。\", \"conclusion\": \"success\", \"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}, \"notes\": \"零样本 + FT 两组 post-hoc baseline 完成。关键发现：ZS 下 post-hoc R_F1 在全部 5 组中 ≥ constrained R_F1（Qwen DocRED 差距最大 +1.38pp）。原因：post-hoc 删除大量 FP 提升 precision，recall 损失有限（TP_lost 仅占 rejected 的 1-2%）。constrained decoding 在 ZS 下强制约束干扰模型分布，总体 F1 反而略低。论文论点需调整：constrained decoding 的 ZS 价值不在 \\\"F1 保留\\\" 而在 \\\"生成时硬保证 0% violations + composability\\\"。\", \"checkpoint_path\": \"N/A (CPU-only analysis, no checkpoint)\", \"log_path\": \"N/A (CPU-only analysis)\", \"completed_at\": \"2026-05-16T09:35:31.720Z\"}, \"w6_mistral_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T02:59:03.876Z\", \"updated_at\": \"2026-05-16T09:28:49.721Z\", \"hypothesis\": \"Mistral (3rd model) DocRED unconstrained baseline — 获取复杂 schema (96 relations) 下的 violation profile，与 Qwen/Llama 对比\", \"notes\": \"PID 5571 on cuda:0 via nohup. Model loaded from symlink /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 -> ms_cache. 2x RTX PRO 6000 Blackwell 98GB. Log at /tmp/w6_mistral_docred_unconstrained.log.\", \"failure_reason\": \"\", \"completed_at\": \"2026-05-16T05:28:07.908Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 5571 on cuda:0 via nohup. Model loaded from symlink /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 -> ms_cache. 2x RTX PRO 6000 Blackwell 98GB. Log at /tmp/w6_mistral_docred_unconstrained.log.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:36:47.316246+00:00\"}]}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_unconstrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": 0, \"pid\": 7740, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_docred_unconstrained.log\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:36:44.102Z\"}, \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T03:19:37.979Z\", \"updated_at\": \"2026-05-16T09:10:49.476Z\", \"hypothesis\": \"Mistral (3rd model) + OntoCoDec constrained eval on DocRED — 验证约束解码在第三模型+复杂 schema 上的泛化性\", \"notes\": \"Constrained decoding eliminates ET/RV violations completely (0%), reduces DR from 57.42%→33.20% (-24.22pp). E_F1 +2.08pp, R_F1 +2.02pp vs unconstrained. DR残余33%来自semantic constraint未覆盖的domain-range组合。\", \"failure_reason\": \"Process killed by fix worker (pkill) during orphan cleanup. Had 15/998 samples before kill.\", \"completed_at\": \"2026-05-16T05:31:30.251Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"PID 6789 on cuda:1 via nohup. Patched xgrammar 0.2.0 hf.py (accept_token .item() fix for transformers 5.8.1 compat). Model loaded from symlink. Log at /tmp/w6_mistral_docred_constrained.log.\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w6_mistral_docred_constrained.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-21461\", \"gpu\": 1, \"pid\": 8347, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w6_mistral_docred_constrained.log\", \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}, \"checkpoint_path\": \"outputs/w6_mistral_docred_constrained.jsonl\", \"conclusion\": \"success\"}, \"w7_llama_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:47:04.863Z\", \"updated_at\": \"2026-05-16T08:32:01.872Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Llama-3.1-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"pid\": 344026, \"log_path\": \"/tmp/w7_llama_scierc_ft_semantic_only.log\"}, \"hypothesis\": \"FT Llama + semantic-only ablation on SciERC: isolate semantic layer contribution in FT regime. Semantic层单独能否消除DR? 与grammar_only对比揭示两层各自贡献。\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}, \"checkpoint_path\": \"outputs/w7_llama_scierc_ft_semantic_only.jsonl\", \"notes\": \"551/551 完成。Semantic-only 在 FT Llama 上: DR=0.65% (vs unconstrained 1.11%, grammar_only 1.11%, full_s1 0.09%)。Semantic 约束单独将 DR 降低 42%，但不如 full_s1 的 grammar+semantic 联合约束。R_F1=45.47% 与 baseline 持平，无质量损失。CF=2 是新增的 cross-field 一致性问题。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:32:01.872Z\"}, \"w5_qwen_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:03:33.642Z\", \"updated_at\": \"2026-05-16T08:10:01.206Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Qwen DocRED 上是否仍能消除残余 DR 且不损 R-F1\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"321568\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_constrained_eval.log\", \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"notes\": \"由另一个 worker 提交，本次确认进程正常运行。PID 321568 (GPU subprocess), wrapper PID 321563, tmux session. CUDA_VISIBLE_DEVICES=1 由 wrapper 控制。模型已加载，2/998 开始推理。Grammar 编译 96 relation types 后开始生成。ETA ~5-6h (参考 unconstrained 5.82h, constrained 更慢)。\", \"reproduce\": {\"finished_at\": \"2026-05-16T08:05:39.680Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:05:41.651478+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}, \"conclusion\": \"success\", \"checkpoint_path\": \"outputs/w5_qwen_docred_lora_constrained_eval.jsonl\", \"completed_at\": \"2026-05-16T08:10:01.206Z\"}, \"w7_llama_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:47:02.522Z\", \"updated_at\": \"2026-05-16T07:49:15.016Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_llama_scierc_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Llama-3.1-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"pid\": 342707, \"log_path\": \"/tmp/w7_llama_scierc_ft_grammar_only.log\"}, \"hypothesis\": \"FT Llama + grammar-only ablation on SciERC: isolate grammar layer contribution in FT regime. FT已修复RV/ET(均0%), DR残留1.11%. Grammar-only能否消除DR?\", \"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}, \"checkpoint_path\": \"outputs/w7_llama_scierc_ft_grammar_only.jsonl\", \"log_path\": \"/tmp/w7_llama_scierc_ft_grammar_only.log\", \"notes\": \"551/551 complete. As expected, grammar_only does not reduce DR (1.11% same as unconstrained FT baseline). ET=0%, RV=0%, CF=0% all clean. F1 slightly better than Qwen FT grammar_only (E_F1=0.6776 vs 0.6705, R_F1=0.4545 vs 0.4386).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:49:15.016Z\"}, \"w7_qwen_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:46:59.364Z\", \"updated_at\": \"2026-05-16T07:25:47.279Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_semantic_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"pid\": 340898, \"log_path\": \"/tmp/w7_qwen_scierc_ft_semantic_only.log\"}, \"hypothesis\": \"FT Qwen + semantic-only ablation on SciERC: isolate semantic layer contribution in FT regime. Semantic层单独能否消除DR? 与grammar_only对比揭示两层各自贡献。\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}, \"checkpoint_path\": \"outputs/w7_qwen_scierc_ft_semantic_only.jsonl\", \"completed_at\": \"2026-05-16T07:25:31.487Z\", \"notes\": \"551/551 完成。Semantic-only 在 FT Qwen 上: DR 1.95%→0.6% (−68%), ET/RV=0%。CF=15（grammar 层对 CF 有抑制作用）。F1 与 grammar_only 几乎一致 (R_F1=0.4369 vs 0.4386)。Ablation 结论: grammar 层消除 RV/ET，semantic 层消除 DR。两层互补，缺一不可——grammar_only DR=1.9%(未降)，semantic_only DR=0.6%(降68%)，full_s1 DR=0%(完全消除)。\"}, \"w7_qwen_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:46:56.566Z\", \"updated_at\": \"2026-05-16T06:55:38.333Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w7_qwen_scierc_ft_grammar_only.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged\", \"pid\": 337069, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w7_qwen_scierc_ft_grammar_only.log\"}, \"hypothesis\": \"FT Qwen + grammar-only ablation on SciERC: isolate grammar layer contribution in FT regime. FT已修复RV/ET(均0%), DR残留1.95%. Grammar-only能否消除DR?\", \"reproduce\": {\"finished_at\": \"2026-05-16T06:41:42.468Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:41:43.361Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:41:45.053980+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}, \"notes\": \"551/551 完成。Grammar-only 在 FT Qwen 上: ET/RV/CF 全部清零，DR 残留 1.9% (22/1128)——与 unconstrained (1.95%) 几乎一致，说明 grammar 层不约束 DR，DR 消除完全依赖 semantic 层。E_F1=0.6705, R_F1=0.4386 与 unconstrained 持平。Tokenizer regex 警告为 transformers 4.57.6 false positive (Reviewer PASS)。\"}, \"w5_llama_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T19:58:10.837Z\", \"updated_at\": \"2026-05-16T05:12:06.855Z\", \"hypothesis\": \"Fine-tuned Llama-3.1-8B DocRED LoRA + OntoCoDec constrained eval — 验证 composability：约束解码在 fine-tuned Llama DocRED 上是否仍能消除残余 DR 且不损 R-F1\", \"parent\": \"w5_llama_docred_lora_training\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T00:22:01.892Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-16T04:51:37.138Z\", \"training_hours\": 4.49}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-16T00:26:15.420Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:26:16.832346+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:51:38.893721+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_constrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": 0, \"pid\": 317464, \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_constrained_eval.log\", \"model_name\": \"llama_lora_docred_merged\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"checkpoint_path\": \"N/A\"}, \"notes\": \"重提交后 PID 317464 (wrapper) / 317469 (GPU subprocess) 在 cuda:0 正常运行。EXIT_CODE=143 来自 wrapper 层误报，非推理进程故障。Grammar 编译 96 relation types 耗时 ~9min（长初始化触发 wrapper 超时报警）。11/998 at ~14s/sample, ETA ~3.8h。脚本支持 --resume，如被 kill 可恢复。\", \"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 85.23, \"entity_precision\": 85.04, \"entity_recall\": 85.41, \"relation_f1_all_set\": 44.23, \"relation_precision_all_set\": 38.82, \"relation_recall_all_set\": 51.4, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.2, \"cross_field_consistency_violations\": 41, \"delta_vs_unconstrained\": {\"delta_e_f1\": 1.3, \"delta_r_f1\": 0.51, \"delta_dr\": -0.29, \"delta_rv\": -0.15, \"note\": \"Computed as constrained - unconstrained on full-set metrics (not intersection subset). Corrected 2026-05-16 per Reviewer audit.\"}}, \"conclusion\": \"success\"}, \"w5_llama_docred_sft_data_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:07:32.770Z\", \"updated_at\": \"2026-05-16T03:21:57.320Z\", \"hypothesis\": \"Generate Llama-3.1-8B-Instruct format DocRED SFT train/dev JSONL — prerequisite for Llama DocRED LoRA fine-tune (composability matrix Llama×DocRED cell)\", \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}, \"spec\": {\"checkpoint_path\": \"N/A (data gen)\", \"log_path\": \"N/A (data gen)\", \"command\": \"python3 prepare_sft_data_docred_llama.py\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/\", \"data_count\": 4051, \"model_name\": \"N/A\", \"seed\": 42}, \"completed_at\": \"2026-05-16T03:20:06.742Z\"}, \"w1_cf_fallback_llama_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:33:00.998Z\", \"updated_at\": \"2026-05-16T03:21:56.516Z\", \"spec\": {\"hypothesis\": \"W1 CF fallback 在 Llama DocRED 上的效果。Llama DocRED full_s1 原 CF=12.02%（最高），预期 fallback 大幅降低。Phase 3 实验。\", \"parent\": \"llama_docred_full_s1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_llama_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"gpu\": \"cuda:0\"}, \"conclusion\": \"killed\", \"notes\": \"D020: 取消。CF fallback 改为 Analytical Finding 方案，仅用 SciERC pilot 数据。D027 确认 Qwen DocRED CF fallback 代码未生效（实际跑 full_s1）。Analytical finding 结论跨模型适用——CF↔DR 根本性张力不依赖模型选择。最终状态: killed。\", \"completed_at\": \"2026-05-16T03:19:55.843Z\"}, \"w1_cf_fallback_llama_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:32:57.470Z\", \"updated_at\": \"2026-05-16T03:21:55.322Z\", \"spec\": {\"hypothesis\": \"W1 CF fallback 在 Llama SciERC 上的跨模型验证。Llama SciERC full_s1 原 CF=6.56%，预期显著降低。Phase 2 实验。\", \"parent\": \"llama_scierc_full_s1\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_llama_scierc.jsonl --device cuda:1 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"gpu\": \"cuda:1\"}, \"conclusion\": \"killed\", \"notes\": \"D020: 取消。CF fallback 改为 Analytical Finding 方案，仅用 SciERC pilot 数据。Qwen SciERC pilot 已充分证明 CF↔DR re-routing（CF -9.86pp 但 DR +13.85pp，budget +3.99pp）。跨模型重复无额外信息量。最终状态: killed。\", \"completed_at\": \"2026-05-16T03:19:54.869Z\"}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:03:32.625Z\", \"updated_at\": \"2026-05-16T01:55:03.824Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta\", \"parent\": \"w5_qwen_docred_lora_training\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"304006\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log\", \"submitted_at\": \"2026-05-15T20:03:48.762Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B-LoRA-DocRED\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\", \"wall_clock_seconds\": 20941.5, \"gpu_hours\": 5.82}, \"reproduce\": {\"finished_at\": \"2026-05-16T01:49:51.884Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:49:53.877179+00:00\"}]}, \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:52:50.220Z\", \"notes\": \"998/998 完成, 927 success / 71 fail. 两组指标已计算. parse_fail_rate=7.11% 高于 Llama(2.3%), Qwen 在长文档上更易超时. R_F1=40.86 略低于 Llama(43.72), E_F1=82.15 略低于 Llama(83.93). DR_pct=0.76% 高于 Llama(0.49%), 说明 Qwen LoRA 残留更多 domain-range 违规.\"}, \"w5_llama_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-15T19:58:07.956Z\", \"updated_at\": \"2026-05-16T00:22:57.512Z\", \"hypothesis\": \"Fine-tuned Llama-3.1-8B DocRED LoRA unconstrained eval — 获取 fine-tuned baseline DR/R-F1，与 constrained eval 对比计算 composability delta\", \"parent\": \"w5_llama_docred_lora_training\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:11:58.831Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"completed_at\": \"2026-05-15T23:14:38.851Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:14:41.289164+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:12:00.360157+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SIGTERM (exit 143) — 外部 kill，非 OOM/崩溃。日志尾部无 Traceback，正常生成中被终止。运行 3.27h (998 samples, batch=1, max_tokens=4096)。已有 ops worker (ops:llama_eval_timeout_fix) 在处理修复重提。| 已有成果: 可能有部分输出 (outputs/w5_llama_docred_lora_unconstrained_eval.jsonl) | 建议: 等 ops worker 完成后确认重提结果\"}}, \"notes\": \"Process received SIGTERM (exit 143) after completing all 998/998 samples. Output file verified complete. Log shows 776 pad_token_id warnings (batch_size=1, some samples produce multiple warnings). No OOM, no traceback. SIGTERM likely from job scheduler timeout, but all inference output was already written. Diagnosed and reclassified from failed→success on 2026-05-16.\", \"spec\": {\"command\": \"nohup python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w5_llama_docred_lora_unconstrained_eval.jsonl --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"312930\", \"data_path\": \"data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Meta-Llama-3.1-8B-Instruct-LoRA-DocRED\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged\", \"eval_data\": \"data/docred/dev.json\"}, \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:48:52.649Z\", \"updated_at\": \"2026-05-15T20:02:42.106Z\", \"hypothesis\": \"Qwen3-8B LoRA fine-tune on DocRED — 填补 Qwen DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"298245\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_training.log\", \"submitted_at\": \"2026-05-15T18:22:06Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6015.9, \"gpu_hours\": 1.67}, \"reproduce\": {\"finished_at\": \"2026-05-15T20:01:28.494Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:55:53.910959+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:01:30.155403+00:00\"}]}, \"notes\": \"Retry #4 (PID 298245, cuda:1): 级联故障修复后由 ops worker 重提交。前次失败原因: GPU 0 幽灵进程争抢显存 + 命令中 CUDA_VISIBLE_DEVICES 硬编码覆盖 wrapper。修复后 wrapper 统一控制 CUDA_VISIBLE_DEVICES。双卡 99% util 已确认。ETA ~2h on RTX PRO 6000。\", \"completed_at\": \"2026-05-15T20:02:21.920Z\", \"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:15:19.269Z\", \"updated_at\": \"2026-05-15T19:57:16.365Z\", \"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on DocRED — 填补 Llama DocRED composability 2×2 matrix 的 FT 行。预期：(1) LoRA 后 E-F1/R-F1 大幅提升；(2) 残余 DR > 0% 证明 OntoCoDec 在 DocRED FT 上仍有 composability 价值。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred_llama.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"298323\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_docred_lora_training.log\", \"submitted_at\": \"2026-05-15T18:23:07Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/docred/sft_train_llama.jsonl\", \"data_count\": 3053, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": \"default\", \"wall_clock_seconds\": 5649.4, \"gpu_hours\": 1.57}, \"notes\": \"Retry #1 (PID 298323, cuda:0): 级联故障修复后重提。首次提交(PID 297434)因幽灵进程占满 cuda:0 显存导致 OOM。修复: 移除命令中 CUDA_VISIBLE_DEVICES 硬编码，由 wrapper 统一控制。参数对齐 Llama SciERC LoRA: rank=16, alpha=32, lr=2e-4, 3 epochs, bs=2, grad_accum=8, max_length=4096。ETA ~80-90min on RTX PRO 6000。输出: checkpoints/llama_lora_docred/ (adapter) + /root/autodl-tmp/checkpoints/llama_lora_docred_merged/ (merged)。\", \"reproduce\": {\"finished_at\": \"2026-05-15T19:54:59.123Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:55:00.912384+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_docred_merged/\", \"completed_at\": \"2026-05-15T19:57:16.365Z\"}, \"w5_llama_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:42.462Z\", \"updated_at\": \"2026-05-15T18:12:19.787Z\", \"spec\": {\"command\": \"cd /root/schema_semantic_constrained_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py --model_path /root/autodl-tmp/checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraint_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_constrained.jsonl --mode full_s1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"290317\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_llama_lora_scierc_constrained_eval.log\", \"submitted_at\": \"2026-05-15T17:38:56.723Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"llama-3.1-8b-instruct-lora-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"SciERC test set (551 samples)\", \"wall_clock_seconds\": 2003.1, \"gpu_hours\": 0.56}, \"hypothesis\": \"Fine-tuned Llama-3.1-8B + OntoCoDec constrained eval on SciERC — composability 验证：约束解码在 fine-tuned Llama 上仍有效且不损 F1。完成 Llama SciERC 2×2 matrix。\", \"reproduce\": {\"finished_at\": \"2026-05-15T17:59:25.871Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:59:27.794917+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}, \"checkpoint_path\": \"outputs/w5_llama_lora_scierc_constrained.jsonl\", \"completed_at\": \"2026-05-15T18:12:19.787Z\"}, \"w5_docred_sft_data_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:51:09.748Z\", \"updated_at\": \"2026-05-15T18:01:39.032Z\", \"hypothesis\": \"Generate DocRED SFT train/dev JSONL from train_annotated.json + dev.json — prerequisite for Qwen/Llama DocRED LoRA fine-tune\", \"spec\": {\"command\": \"python3 scripts/prepare_sft_data_docred.py\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"292314\", \"log_path\": \"N/A\", \"submitted_at\": \"2026-05-15T17:51:19.316Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/\", \"data_count\": 4051, \"model_name\": \"Qwen3-8B\", \"seed\": null, \"wall_clock_seconds\": 379.5, \"gpu_hours\": 0.11, \"checkpoint_path\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:51:44.980Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:51:46.380733+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/data/docred/sft_train.jsonl,/root/schema_semantic_constrained_ie/data/docred/sft_dev.jsonl\", \"completed_at\": \"2026-05-15T17:57:38.825Z\", \"notes\": \"数据质量验证完成：4051行全部JSON解析通过，0损坏。Prompt用Qwen3 chat模板（含think tag），6实体类型+96关系类型。Completion为合法JSON（entities+relations）。数据可直接用于SFT训练。Train: 3053样本/19M, Dev: 998样本/6.0M。\"}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:40.179Z\", \"updated_at\": \"2026-05-15T17:47:07.574Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path checkpoints/llama_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_llama_lora_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"287667\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_llama_lora_scierc_unconstrained.jsonl\", \"submitted_at\": \"2026-05-15T17:19:48.001Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/processed_data/test.json\", \"data_count\": 100, \"model_name\": \"Meta-Llama-3.1-8B-Instruct-LoRA-SciERC\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"eval_data\": \"data/processed_data/test.json\", \"parent\": \"w5_llama_lora_scierc_training\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"wall_clock_seconds\": 271.9, \"gpu_hours\": 0.08}, \"hypothesis\": \"Fine-tuned Llama-3.1-8B SciERC unconstrained eval — 验证 LoRA 后残余 DR 是否仍 >2%，决定 OntoCoDec 在 fine-tuned Llama 上的 composability 价值。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T17:24:19.934Z\", \"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}}, \"w5_llama_lora_scierc_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:33:38.168Z\", \"updated_at\": \"2026-05-15T17:24:38.949Z\", \"spec\": {\"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on SciERC, extending Claim 3 composability to cross-model. Mirrors Qwen3-8B LoRA config (r=16, alpha=32, lr=2e-4, 3 epochs).\", \"parent\": \"w5_lora_scierc_training\", \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"dataset\": \"SciERC\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/llama_lora_scierc_merged\", \"log_path\": \"logs/w5_llama_lora_scierc_training.log\", \"adapter_path\": \"checkpoints/llama_lora_scierc\", \"base_model\": \"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct\"}, \"hypothesis\": \"Llama-3.1-8B-Instruct LoRA fine-tune on SciERC — 扩展 composability 验证到跨模型。预期：(1) LoRA 训练后 E-F1/R-F1 大幅提升（对标 Qwen LoRA +36pp/+36pp）；(2) 为 Llama SciERC 2×2 composability matrix 提供 fine-tuned baseline。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T17:17:30.599Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}, \"completed_at\": \"2026-05-15T17:18:45.275Z\"}, \"w1_cf_fallback_docred\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T10:32:53.234Z\", \"updated_at\": \"2026-05-15T16:55:58.012Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\"}, \"notes\": \"Reviewer #12 三次确认: 实际运行 --mode full_s1 (非 CF fallback), 与 phase2_docred_full_s1 重复。CF fallback 代码恢复失败或未生效。命令行明确显示 --mode full_s1。PID 283824 已 kill。W1 CF fallback 整体定论: SciERC pilot (analytical finding) 已充分, DocRED 不再重跑。\", \"completed_at\": \"2026-05-15T15:47:59.075Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\", \"notes\": \"D020: Director 取消全部 CF fallback 实验。改用 Analytical Finding 方案——pilot negative 本身作为论文素材。仅跑约 30s 即被终止。\"}}, \"spec\": {\"command\": \"bash -c \\\"rm -f /root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_docred.jsonl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/w1_cf_fallback_docred.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"283824\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_docred.log\", \"submitted_at\": \"2026-05-15T16:26:41.953Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A (killed - ran wrong code)\", \"wall_clock_seconds\": 1756.1, \"gpu_hours\": 0.49}, \"pid\": \"283824\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_docred.log\", \"conclusion\": \"killed\"}, \"w5_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:57:42.154Z\", \"updated_at\": \"2026-05-15T16:25:47.858Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_full_s1_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"282127\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_constrained_eval.log\", \"submitted_at\": \"2026-05-15T15:58:03.052Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1664.8, \"gpu_hours\": 0.46}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"282127\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_constrained_eval.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_full_s1_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-15T16:22:21.690Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:22:23.113142+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}, \"hypothesis\": \"Fine-tuning + constrained decoding composability: 约束解码在 fine-tuned 模型上仍有效，且不显著损害 F1\", \"checkpoint_path\": \"checkpoints/qwen3_8b_lora_scierc_merged\", \"completed_at\": \"2026-05-15T16:25:47.858Z\"}, \"w5_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:23:25.030Z\", \"updated_at\": \"2026-05-15T16:01:58.250Z\", \"hypothesis\": \"Fine-tuned Qwen3-8B still produces >2% decode rate violations on SciERC unconstrained, justifying OntoCoDec constraint application\", \"parent\": \"w5_lora_scierc_training\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w5_lora_scierc_unconstrained_eval.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 278380, \"data_path\": \"data/processed_data/test.json\", \"data_count\": 551, \"data_count_note\": \"551 per-sentence samples derived from 100 SciERC test documents (matches phase2_scierc_unconstrained sample count)\", \"model_name\": \"Qwen3-8B-LoRA-SciERC\", \"model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\", \"seed\": null, \"checkpoint_source\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\", \"eval_data\": \"SciERC test set (551 samples)\", \"constraints_path\": \"/root/schema_semantic_constrained_ie/ontology_constraints.json\", \"output_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.log\", \"mode\": \"unconstrained\", \"max_new_tokens\": 4096, \"batch_size\": 1, \"path_note\": \"Task spec called for data/scierc/test.json + data/scierc/ontology_constraints_scierc.json which do not exist on this server; substituted the actual paths used by all prior phase2_scierc_* experiments.\"}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": 278385, \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w5_lora_scierc_unconstrained_eval.jsonl\", \"completed_at\": \"2026-05-15T15:55:17.802Z\", \"notes\": \"LoRA fine-tuned Qwen3-8B unconstrained eval on SciERC: 聚合 DR=1.95% 略低于 2% gate 阈值，但按关系类型拆分后 Evaluate-for DR=13.13%（99 个三元组中 13 个违规）、Part-of 5.8%、Compare 5.0%。表明 tight-constraint 关系是 fine-tuning 无法覆盖的长尾——OntoCoDec 的互补价值在于消除这些 schema-ambiguous relation 的残余 DR。Quality: R-F1=43.9% (+35.7pp vs base), E-F1=67.1% (+36.1pp vs base). ET/RV/CF 全部清零。\"}, \"w5_lora_scierc_training\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T14:56:20.233Z\", \"updated_at\": \"2026-05-15T15:20:00.313Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 scripts/train_lora_scierc.py\\\"\", \"finished_at\": \"2026-05-15T15:16:50.985Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T14:58:56.873Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:58:58.618383+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:16:52.498789+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 scripts/train_lora_scierc.py\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"276523\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log\", \"submitted_at\": \"2026-05-15T15:02:11.699Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"wall_clock_seconds\": 1068.6, \"gpu_hours\": 0.3}, \"pid\": \"276523\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w5_lora_scierc_training.log\", \"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}, \"conclusion\": \"success\"}, \"llama_docred_full_s1_mt6144\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T08:17:36.675Z\", \"updated_at\": \"2026-05-15T15:04:59.453Z\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"finished_at\": \"2026-05-15T14:59:20.782Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-15T08:19:51.861Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:19:53.379823+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:59:25.181921+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"247487\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log\", \"submitted_at\": \"2026-05-15T08:22:03.222Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24176.2, \"gpu_hours\": 6.72}, \"pid\": \"247487\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1_mt6144.log\", \"notes\": \"⚠️ 变量混淆：此实验同时包含 CF fallback 代码修改 + max_tokens 6144（两个变量）。CF 数据可作为 'Llama DocRED with fallback + mt6144' 参考点，但不能用于纯 CF ablation 对比。纯 CF ablation 必须控制 max_tokens=4096。unconstrained_mt6144 不受影响（不走 semantic layer）。\", \"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_full_s1_mt6144.jsonl\"}, \"w1_cf_fallback_scierc_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:32:48.425Z\", \"updated_at\": \"2026-05-15T14:57:13.885Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"270088\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log\", \"submitted_at\": \"2026-05-15T14:07:14.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2999.4, \"gpu_hours\": 0.83}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"270088\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-15T14:47:53.690Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:47:54.986519+00:00\"}]}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_scierc_pilot.jsonl\", \"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}, \"notes\": \"CF fallback 实验在 SciERC + Qwen3-8B 上的 pilot 结果：CF 从 9.90% 下降到 0.04% (-9.86pp)，但 DR 从 0.93% 上升到 14.78% (+13.85pp)。DR+CF budget 净增 +3.99pp。F1 几乎不变 (E-F1=30.98% 与 baseline 完全一致；R-F1=8.23%, -0.13pp)。Grammar-first fallback 触发率 36.64% (6237/17024 mask calls)，CF-registry fallback 4.48%。判定：成功降低 CF 但代价是 DR 大幅恶化，违规没有真正减少，只是从 CF 转移到 DR。建议改进方向：(1) 仅在 CF-registry 命中时回退，保留 DR enforcement；(2) rebuttal 中诚实呈现这是 violation re-routing 而非 reduction。详细报告见 artifact w1_cf_fallback_scierc_pilot_analysis。\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T14:57:13.885Z\"}, \"llama_docred_unconstrained_mt6144\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:17:33.154Z\", \"updated_at\": \"2026-05-15T14:09:53.452Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"246947\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained_mt6144.log\", \"submitted_at\": \"2026-05-15T08:19:27.565Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20932.1, \"gpu_hours\": 5.81}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": \"246947\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained_mt6144.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained_mt6144.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 6144\\\"\", \"finished_at\": \"2026-05-15T13:59:24.508Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:59:25.767053+00:00\"}]}, \"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained_mt6144.jsonl\", \"notes\": \"mt6144 vs mt4096 对比: parse_failures 68→67 (-1, 几乎无变化); unique_entities 11525→11534 (+9); triples 16437→16584 (+147, +0.9%); E-F1 55.65%→55.67% (+0.02pp); R-F1 5.98%→5.95% (-0.03pp); DR 26.07%→26.18% (+0.11pp); RV 16.03%→15.89% (-0.14pp); ET/CF 不变. 67 个 FAIL 中绝大多数 inference time ~96s (仍触发 max_tokens cap), 说明这些失败主要源于模型陷入重复循环直到 token 上限, 而非文档过长. 增加 max_new_tokens 不能挽救此类失败. 训练 wall clock 约 5h39m, 比 mt4096 (~5h02m) 多约 37 分钟. 结论: max_new_tokens 4096→6144 对 unconstrained 生成无实质影响, 不建议采用作为后续 baseline.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:08:19.680Z\"}, \"llama_docred_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:59.855Z\", \"updated_at\": \"2026-05-14T20:29:59.744Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"194295\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1.log\", \"submitted_at\": \"2026-05-14T14:41:22.992Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20912.7, \"gpu_hours\": 5.81}, \"hypothesis\": \"Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上的效果。与 Qwen3-8B DocRED full_s1 (DR 10.19%) 对比，验证约束解码在不同模型+复杂 schema 上的泛化性。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T14:39:33.737Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T20:24:03.061Z\", \"training_hours\": 5.74}, \"pid\": \"194295\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_full_s1.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:24:04.262279+00:00\"}]}, \"checkpoint_path\": \"outputs/llama_docred_full_s1.jsonl\", \"completed_at\": \"2026-05-14T20:24:03Z\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}, \"conclusion\": \"success\", \"notes\": \"ET/RV→0%, DR 26.07%→2.55% (优于Qwen的10.19%)。但CF从0.17%暴涨至12.02%，说明Llama的entity type预测更容易被约束扰动。F1基本持平(E-F1 -0.64pp, R-F1 +0.29pp)。Parse failures从68增至91。Grammar-first fallback频繁触发。\"}, \"llama_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:58.719Z\", \"updated_at\": \"2026-05-14T19:45:08.201Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"193605\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained.log\", \"submitted_at\": \"2026-05-14T14:35:57.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18533.7, \"gpu_hours\": 5.15}, \"hypothesis\": \"Llama-3.1-8B-Instruct 在 DocRED unconstrained baseline。与 Qwen3-8B DocRED unconstrained 对比 violation 分布。验证不同模型在复杂 schema (96 relations) 上的 violation 模式差异。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T14:15:03.413Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/llama_docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T19:39:03.154Z\", \"training_hours\": 5.4}, \"pid\": \"193605\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_docred_unconstrained.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T19:39:05.142651+00:00\"}]}, \"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}, \"conclusion\": \"success\", \"notes\": \"v2 checker (unique_et dedup) + all_set F1。930/998 docs parsed (68 parse failures, 6.8% vs Qwen 1.2%)。Violation profile 与 Qwen3-8B 显著不同：RV 大幅降低 (16.03% vs 29.66%，-13.6pp，Llama 更倾向使用标准关系名) 但 DR 更高 (26.07% vs 18.46%，+7.6pp，即使关系名正确 head/tail 类型约束违反更多)。ET 极低 (0.13% vs 2.48%，-2.35pp)，CF 接近 (0.17% vs 0.10%)。F1 弱于 Qwen: R-F1 5.98% vs 7.74% (-1.76pp)，E-F1 55.65% vs 58.15% (-2.50pp)。DR 26.07% 为约束解码提供更大改进空间。\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_docred_unconstrained.jsonl\", \"completed_at\": \"2026-05-14T19:44:51.441Z\"}, \"phase2_docred_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:55:50.031Z\", \"updated_at\": \"2026-05-14T18:52:55.527Z\", \"hypothesis\": \"Grammar-only constrained decoding 在 DocRED (96 relation types) 上能否消除 RV violations (28.9%) 和 ET violations (7.5%)？与 SciERC grammar_only (RV 1.4%→0%, ET 0.4%→0%) 对比，验证 grammar 层在复杂 schema 上的泛化性。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 nohup python3 run_constrained_extraction.py --mode grammar_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_grammar_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"150766\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"/root/runs/schema_semantic_constrained_ie/docred_grammar_only.log\"}, \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_grammar_only.jsonl\", \"completed_at\": \"2026-05-14T07:40:10.382Z\"}, \"posthoc_filtering_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:46:07.823Z\", \"updated_at\": \"2026-05-14T18:46:28.485Z\", \"spec\": {\"hypothesis\": \"Post-hoc filtering baseline: generate unconstrained triples then remove DR/RV/ET violations. Comparison with OntoCoDec decoding-time enforcement on precision, recall, coverage, and residual violations.\", \"command\": \"python posthoc_filter.py\", \"server\": \"westd-16980\", \"data_path\": \"/root/schema_semantic_constrained_ie/outputs/\", \"data_count\": 2, \"model_name\": \"Qwen3-8B (unconstrained outputs)\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/posthoc_report_docred.json\", \"log_path\": \"/root/schema_semantic_constrained_ie/outputs/posthoc_report_scierc.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:46:23.429Z\", \"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}}, \"llama_scierc_full_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:56.936Z\", \"updated_at\": \"2026-05-14T18:31:43.217Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"190648\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_full_s1.log\", \"submitted_at\": \"2026-05-14T13:50:35.755Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 1249.5, \"gpu_hours\": 0.35}, \"hypothesis\": \"Llama-3.1-8B-Instruct + Grammar+Semantic 双层约束 (S1) 在 SciERC 上的效果。与 Qwen3-8B full_s1 (DR 0.93%) 对比，验证 OntoCoDec 的 model-agnostic 特性。零代码修改。D009 cross-model 验证核心实验。\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:50:33.979Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-14T14:11:24.215Z\", \"training_hours\": 0.35}, \"pid\": \"190648\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_full_s1.log\", \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:11:25.248Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:11:26.755217+00:00\"}]}, \"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_scierc_full_s1.jsonl\", \"notes\": \"550/551 samples (1 corrupt line from duplicate PID removed). DR 0.08% — 约束合规性极好，优于 Qwen3-8B full_s1 (0.93%)。但 E-F1=23.49% (vs Qwen 30.98%), R-F1=2.54% (vs Qwen 8.36%)，Llama 在 IE 质量上显著弱于 Qwen。对比 Llama unconstrained: DR 13.3%→0.08% (约束生效), E-F1 23.56%→23.49% (持平), R-F1 2.68%→2.54% (微降)。约束大幅降低违规率但未提升抽取质量。Cross-field consistency violations 较高 (6.56%)。\"}, \"llama_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:42:55.421Z\", \"updated_at\": \"2026-05-14T18:31:40.240Z\", \"spec\": {\"data_path\": \"scierc_test\", \"data_count\": 551, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"command\": \"python3 run_extraction.py --config configs/llama_scierc_unconstrained.yaml\", \"server\": \"westd-16980\"}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:19:48.866Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/llama_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 2048\\\"\", \"finished_at\": \"2026-05-14T13:46:24.376Z\", \"training_hours\": 0.44}, \"pid\": \"188367\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/llama_scierc_unconstrained.log\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 SciERC unconstrained baseline — 验证 OntoCoDec 跨模型泛化性。零代码修改，与 Qwen3-8B unconstrained 对比 violation 分布差异。预期 DR~15%, RV~1.4%, ET~0.4%（Llama instruction-following 可能更好）。D009 cross-model 验证的第一步。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:46:25.548989+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/llama_scierc_unconstrained.jsonl\", \"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"completed_at\": \"2026-05-14T13:49:13.425Z\", \"notes\": \"Llama-3.1-8B-Instruct SciERC unconstrained baseline 完成。551 样本（550成功/1失败）。Violation: ET=0%, RV=0.5%, DR=13.3%。F1: E-F1=23.56%, R-F1=2.68%。与 Qwen3-8B unconstrained 对比：Llama violation 略低（DR 13.3% vs 15.4%），但 F1 明显更差（E-F1 低7.5pp, R-F1 低5.5pp）。Llama 更倾向保守提取——提取数量少、violation 低但 recall 也低。Qwen3 在 unconstrained 设定下提取质量优于 Llama。\"}, \"phase2_scierc_full_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:36:35.941Z\", \"updated_at\": \"2026-05-14T18:31:38.701Z\", \"spec\": {\"command\": \"bash -c \\\"tmux kill-session -t phase2_scierc_full_s2 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s2.jsonl --device cuda:0 --batch_size 1 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s2.log\", \"submitted_at\": \"2026-05-14T01:07:00.401Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 368.6, \"gpu_hours\": 0.1}, \"hypothesis\": \"S2 两通道约束解码全量验证 — Grammar (Pass 1) + Semantic (Pass 2) 分离式约束。S2 pilot50 已验证 D/R violation=0%，全量运行检验 F1 稳定性和 per-relation 效果。与 S1 对比验证两种架构的 F1-violation trade-off。\", \"notes\": \"✅ 全量完成 551/551 via --resume. S2 两通道约束解码结果。DR=0.97% (vs S1 0.93%), RV=0%, ET=0%, R-F1=0.0803, E-F1=0.319.\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T01:06:58.685Z\", \"command\": \"bash -c \\\"tmux kill-session -t phase2_scierc_full_s2 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s2.jsonl --device cuda:0 --batch_size 1 --resume\\\"\", \"finished_at\": \"2026-05-14T01:13:08.809Z\", \"training_hours\": 0.1}, \"pid\": 144858, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s2.log\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T01:13:09.036Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T01:13:12.640712+00:00\"}]}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s2.jsonl\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s1\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T21:48:44.785Z\", \"updated_at\": \"2026-05-14T18:31:34.603Z\", \"hypothesis\": \"Grammar + Semantic 双层约束 (S1 单通道) 能否同时消除 rv + dr violations？F1 变化是关键：<2pp 降=完美，2-5pp=可接受 trade-off，>5pp=需要 S2 策略\", \"notes\": \"✅ _v2 干净数据全量完成 551/551. DR violation = 0.93% (baseline 15.37%, -14.44pp). ET=0%, RV=0%. 数据来源: phase2_scierc_full_s1_v2.jsonl\", \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T23:49:56.383Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python3 && python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_full_s1.jsonl --device cuda:0 --batch_size 1\\\"\", \"finished_at\": \"2026-05-14T00:33:47.489Z\", \"training_hours\": 0.73}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-13T23:45:41.906Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:45:42.821098+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:33:48.999924+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断完成: EXIT_CODE=127, bash: line 1: python3: command not found。Root cause: submit_training_job 未在命令前加 conda 环境激活。修复方案: 命令前缀加 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。retry_count=0, 自动重试中。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 run_constrained_extraction.py --mode full_s1 ...\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"retry #2: bash -c wrapping fixes EXIT_CODE=127\"}, \"pid\": \"134593\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_full_s1.log\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl\"}, \"phase2_scierc_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-13T21:48:44.427Z\", \"updated_at\": \"2026-05-14T18:31:31.811Z\", \"hypothesis\": \"Semantic-only constrained decoding (TypeConstraintProcessor) 能否消除 domain/range violations？预期 dr_violation→0%，但可能影响 F1（约束过强导致生成偏移）\", \"notes\": \"✅ _v2 干净数据全量完成 551/551. DR violation = 11.65% (baseline 15.37%, -3.72pp). ET=0.4%, RV=1.51%.\", \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T23:49:33.935Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && which python3 && python3 run_constrained_extraction.py --mode semantic_only --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_semantic_only.jsonl --device cuda:0 --batch_size 1\\\"\", \"finished_at\": \"2026-05-14T00:33:32.617Z\", \"training_hours\": 0.73}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-13T23:45:39.272Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:45:40.115539+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T00:33:34.349694+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断完成: EXIT_CODE=127, bash: line 1: python3: command not found。Root cause: 同 phase2_scierc_full_s1, submit 未激活 conda。修复方案同上。retry_count=0, 自动重试中。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 run_constrained_extraction.py --mode semantic_only ...\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"retry #2: bash -c wrapping fixes EXIT_CODE=127\"}, \"pid\": \"134202\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_semantic_only.log\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_semantic_only_v2.jsonl\"}, \"phase2_scierc_grammar_only\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T21:48:43.487Z\", \"updated_at\": \"2026-05-14T18:31:29.442Z\", \"hypothesis\": \"Grammar-only constrained decoding (XGrammar JSON schema + enum) 能否消除 relation vocabulary violations 同时不影响 F1？预期 rv_violation→0%, dr_violation 不变\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:39:02.641Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-13T22:38:46.650Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T22:38:47.328842+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:39:03.395560+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"诊断中: 进程到 176/551 无 traceback 静默退出。cron 追踪 stale PID 导致 5× dead 判定。已派 Worker diagnose:phase2_scierc_grammar_only 深查。\"}}, \"notes\": \"进程从未崩溃。原 'crash' 判定是 cron 追踪 stale PID 123425（已杀的 batch script）导致 5× dead 误报。实际进程 PID 126473 一直在 GPU 1 正常运行。nvidia-smi 确认: GPU 1 上 grammar_only(126473) + unconstrained(126948) 共享，各占 ~16.5GB，利用率 92%。\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode grammar_only --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_grammar_only.jsonl --device cuda:0 --batch_size 1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"126473\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_grammar_only.log\", \"note\": \"CUDA_VISIBLE_DEVICES=1 by submit_training_job. 进程从未崩溃 — 'crash' 是 cron 追踪 stale PID 123425 的误报。PID 126473 一直在跑。两个 Phase 2 实验共享 GPU 1（各 ~16.5GB），利用率 92%。\"}, \"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_grammar_only.jsonl\", \"conclusion\": \"success\"}, \"phase2_scierc_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:07.120Z\", \"updated_at\": \"2026-05-14T18:31:26.645Z\", \"hypothesis\": \"Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的代码路径和 prompt，确保 F1 对比公平。预期结果接近 Phase 0 (entity_f1=0.31, relation_f1=0.08)\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode unconstrained --dataset scierc --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/phase2_scierc_unconstrained.jsonl --device cuda:0 --batch_size 1\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"126948\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_unconstrained.log\", \"submitted_at\": \"2026-05-13T22:20:28.660Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"CUDA_VISIBLE_DEVICES=1 injected by submit_training_job. Progress 353/551 at 23:10 UTC\", \"wall_clock_seconds\": 5186.0, \"gpu_hours\": 1.44}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:44:02.820Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:44:06.470330+00:00\"}]}, \"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_scierc_unconstrained.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_scierc_unconstrained.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:46:54.651Z\"}, \"phase2_docred_full_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T02:07:20.166Z\", \"updated_at\": \"2026-05-14T18:31:19.721Z\", \"hypothesis\": \"Grammar+Semantic 双层约束 (S1) 在 DocRED (96 relations) 上能否复现 SciERC 的 DR 消除效果 (15.37%→0.93%)？DocRED 约束更紧 (avg 5.68 valid pairs)，DR baseline 更高 (18.7%)，验证 OntoCoDec 在复杂 schema 上的泛化性。\", \"notes\": \"DR 18.46%→10.19% (↓44.8%). RV 29.66%→0.03% (↓99.9%), ET 8.18%→0% (↓100%). R-F1 7.74%→8.23% (+0.49pp), E-F1 58.15%→59.37% (+1.22pp). F1 method: all_set (OOV predictions included in denominator). 之前 recognized_set 方法 (R-F1=9.33%→8.17%, -1.16pp) 是错误的——它过滤了 unconstrained 的 5189 个 OOV predictions，人为抬高 precision。Grammar-only DR 上升(18.46→26.17%)是审稿必问点：grammar 强制 valid relation name 后 entity type 与新 relation 的 domain/range 不匹配加剧，恰好证明 semantic 层必要性。\", \"completed_at\": \"2026-05-14T02:55:47.271Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"修复后重启 (PID 157042, tmux: phase2_docred_full_s1, cuda:1)。根因: TypeConstraintProcessor._apply_type_mask 在 allowed_types 与 grammar-valid tokens 无交集时，把所有 grammar-valid tokens 设为 -inf，导致 argmax 选中 grammar-invalid token (logit=-1e10 > -inf)。修复: _apply_type_mask 增加安全检查，若无 semantically-allowed type 有非 grammar-masked logit，跳过 semantic masking 交由 grammar 控制。Dry-run 验证 doc 88(原崩溃点)+7 docs 全部通过。--resume 从 87 继续，当前 89/998。\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:29:08.943533+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode full_s1 --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_full_s1.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"157042\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log\", \"fix_applied\": \"type_mask_processor.py: semantic mask safety check — skip semantic masking when allowed_types have no non-grammar-masked logits\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:29:07.765Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_full_s1.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:40:51.107Z\", \"updated_at\": \"2026-05-14T18:31:13.783Z\", \"hypothesis\": \"Semantic-only constrained decoding 在 DocRED (96 relations, avg 5.68 valid pairs) 上的 DR 降低幅度。SciERC semantic_only DR↓24% (15.37→11.65%)，DocRED 约束更紧预期效果更明显。关键验证 Claim 3 enabling dependency：semantic_only 无法消除 RV/ET（需 grammar），证明两层互补非替代。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"pid\": \"172859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_semantic_only.log\", \"submitted_at\": \"2026-05-14T08:30:43.644Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 21989.5, \"gpu_hours\": 6.11}, \"server\": \"westd-16980\", \"gpu\": \"cuda:1\", \"pid\": \"172859\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_semantic_only.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode semantic_only --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_semantic_only.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T14:13:58.319Z\"}, \"notes\": \"DocRED semantic-only（checker 修复后定稿数字）。ET 10.44% (修复前 18.44%, -8pp: strip 修 507 假阳性 + PERSON alias 修 1108 假阳性)。DR 13.84% (修复前 15.05%, -1.21pp: normalize 也修正了 DR pair 匹配)。CF 1.05% (修复前 2.29%)。残余 ET 2107 violations 是真实退化：WORK(823)/EVENT(743)/ETHNIC_GROUP(137) 等非标类型。F1 无变化。998 lines, 0 duplicates。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:13:59.612547+00:00\"}]}, \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_semantic_only.jsonl\", \"completed_at\": \"2026-05-14T14:37:13.158Z\"}, \"phase2_docred_unconstrained\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:40:50.853Z\", \"updated_at\": \"2026-05-14T18:31:10.378Z\", \"hypothesis\": \"DocRED Phase 2 unconstrained baseline — 使用与 constrained 实验完全相同的 Phase 2 pipeline 和 prompt，确保消融表 F1/violation 对比公平。预期 DR~18.7%, RV~28.9%, ET~7.5%（接近 Phase 0）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"170502\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_unconstrained.log\", \"submitted_at\": \"2026-05-14T07:40:49.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20601.7, \"gpu_hours\": 5.72}, \"server\": \"westd-16980\", \"gpu\": \"cuda:0\", \"pid\": \"170502\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_docred_unconstrained.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_constrained_extraction.py --mode unconstrained --dataset docred --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --constraints_path data/docred/ontology_constraints_docred.json --output_path outputs/docred_unconstrained.jsonl --device cuda:0 --batch_size 1 --max_new_tokens 4096\\\"\", \"finished_at\": \"2026-05-14T13:10:49.905Z\"}, \"notes\": \"✅ Phase 2 重新分析完成。998 lines, 0 duplicates — 文件干净无残留。正确值: DR=18.5%, RV=29.7%, ET=8.2%, E-F1=58.15%, R-F1=7.74%。F1 method: all_set (Reviewer 2026-05-14 确认正确)。论文可 claim: constrained decoding 不损失 R-F1。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:10:51.383206+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/docred_unconstrained.jsonl\", \"completed_at\": \"2026-05-14T13:24:10.838Z\"}, \"mvp_phase0_docred_schema_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:36:06.125Z\", \"updated_at\": \"2026-05-14T02:56:53.324Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred_schema.jsonl --device cuda:0 --constraints_path data/docred/ontology_constraints_docred.json --prompt_mode schema_informed --batch_size 4 --resume\\\"\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"note\": \"Resume from killed mvp_phase0_docred_schema. Original ran ~3.5h before being killed by cleanup Worker.\"}, \"hypothesis\": \"Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心。（从被误杀的 mvp_phase0_docred_schema 恢复，--resume）\", \"notes\": \"归档：mvp_phase0_docred_schema 已完成全量 998/998 并有完整 metrics，此 r2 续跑实验不再需要。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T02:56:53.324Z\"}, \"phase2_s2_pilot50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:25:10.566Z\", \"updated_at\": \"2026-05-14T02:04:44.195Z\", \"spec\": {\"command\": \"python3 run_constrained_extraction.py --mode full_s2 --dataset scierc --num_samples 50 --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --device cuda:0\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 50, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/phase2_s2_pilot50.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/phase2_s2_pilot50.log\", \"note\": \"S2 50-sample pilot run. D/R violation=0% verified. relation_f1=0.0 root cause under investigation by Worker analysis:s2_relation_f1_rootcause.\"}, \"hypothesis\": \"S2 两通道约束解码 50 样本 pilot — 验证 PositionDetector 修复后 D/R violation=0%，评估 relation_f1 质量\", \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}, \"completed_at\": \"2026-05-13T23:26:16.718Z\", \"notes\": \"S2 pilot 实际 relation_f1=0.1008（非此前误报的 0.0）。根因：原 F1=0 来自 10 样本 dryrun 的 violation_report，不是 pilot50 评估结果。S2 架构无问题，F1 与 unconstrained 持平。FP 分析: entity span 质量差是主因(52.6% head+tail 都不匹配 gold)。改进方向: few-shot entity prompt / 编号引用格式 / 阻止自引用。\"}, \"mvp_phase0_docred_schema\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:58:18.184Z\", \"updated_at\": \"2026-05-14T01:49:57.097Z\", \"hypothesis\": \"Schema-informed prompt 在 DocRED (96 relation types) 上的违规率降低幅度是否小于 SciERC (7 types)？验证约束空间越大 prompt 级干预越力不从心\", \"spec\": {\"command\": \"python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred_schema.jsonl --device cuda:0 --constraints_path data/docred/ontology_constraints_docred.json --prompt_mode schema_informed --batch_size 4\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"116365\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_docred_schema.log\", \"submitted_at\": \"2026-05-13T20:13:18.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"wall_clock_seconds\": 13513.6, \"gpu_hours\": 3.75}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:58:31.565Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T23:58:32.325Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:58:33.241310+00:00\"}]}, \"notes\": \"Resume 完成 998/998 docs. Schema-informed prompt 结果: ET=0.61% (baseline 7.5%, Δ-6.89%), RV=18.4% (baseline 28.9%, Δ-10.5%), DR=12.8% (baseline 18.7%, Δ-5.9%). 全维度显著改善。\", \"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}, \"checkpoint_path\": \"outputs/raw_outputs_docred_schema.jsonl\"}, \"mvp_phase0_violation_rate_docred\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:38:05.075Z\", \"updated_at\": \"2026-05-13T21:46:35.193Z\", \"hypothesis\": \"DocRED 有 96 relation types，约束空间远大于 SciERC (7 types)，预期 unconstrained LLM 的 per-triple violation rate 显著高于 SciERC，验证违规率与约束空间复杂度正相关\", \"spec\": {\"command\": \"python3 run_extraction_docred.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/docred/dev.json --output_path outputs/raw_outputs_docred.jsonl --device cuda:0 --batch_size 4 --resume\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/schema_semantic_constrained_ie/data/docred/dev.json\", \"data_count\": 998, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"pid\": 113148, \"resumed_from_doc\": 265, \"batch_size\": 4, \"current_progress\": 281, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_docred.jsonl\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate_docred.log\"}, \"metrics\": {\"total_docs\": 998, \"parsed_docs\": 962, \"json_parse_rate\": 0.964, \"total_entities\": 19099, \"total_triples\": 16540, \"entity_type_violation_rate\": 0.075, \"relation_vocabulary_violation_rate\": 0.289, \"domain_range_violation_rate\": 0.187, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.187, \"fuzzy_matches\": 126, \"top_dr_violations_by_rate\": {\"P35_head_of_state\": 1, \"P710_participant\": 0.919, \"P172_ethnic_group\": 0.875}, \"top_dr_violations_by_count\": {\"P31_instance_of\": {\"violations\": 322, \"total\": 533, \"rate\": 0.604}, \"P1001_applies_to_jurisdiction\": {\"violations\": 264, \"total\": 594, \"rate\": 0.444}, \"P1344_participant_in\": {\"violations\": 194, \"total\": 312, \"rate\": 0.622}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:46:35.193Z\"}, \"mvp_phase0_scierc_schema\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:58:17.259Z\", \"updated_at\": \"2026-05-13T20:58:13.410Z\", \"hypothesis\": \"Schema-informed prompt（显式给出 domain/range 约束）能否降低违规率？与 minimal prompt 对比，若违规率仍 >5% 则证明 prompt 级干预不足以替代 decoding-time enforcement\", \"spec\": {\"command\": \"python3 run_extraction.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --output_path outputs/raw_outputs_schema.jsonl --backend transformers --prompt_mode schema_informed --constraints_path ontology_constraints.json\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"110676\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_scierc_schema.log\", \"submitted_at\": \"2026-05-13T19:11:32.249Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs_schema.jsonl\", \"wall_clock_seconds\": 3650.3, \"gpu_hours\": 1.01}, \"metrics\": {\"domain_range_violation_rate\": 0.0578, \"relation_vocabulary_violation_rate\": 0.003, \"entity_type_violation_rate\": 0, \"total_violation_rate\": 0.0253, \"go_nogo_metric\": 0.0578, \"total_triples\": 1661, \"vs_minimal_dr_reduction\": -0.624, \"per_relation\": {\"Used-for\": {\"rate\": \"TBD\"}, \"Feature-of\": {\"delta_pp\": -22.3}, \"Part-of\": {\"delta_pp\": -22.5}, \"Compare\": {\"delta_pp\": -14.8}, \"Evaluate-for\": {\"delta_pp\": 5.8}}, \"mcnemar_all_significant\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T20:12:22.502Z\"}, \"mvp_phase0_violation_rate\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:35:38.680Z\", \"updated_at\": \"2026-05-13T19:13:34.510Z\", \"hypothesis\": \"Unconstrained LLM (Qwen3-8B) 在 SciERC zero-shot IE 任务上的本体类型约束违反率 >5%，证明解码时约束强制的必要性\", \"spec\": {\"command\": \"python3 run_extraction.py --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B --data_path data/processed_data/test.json --output_path outputs/raw_outputs.jsonl --backend transformers\", \"server\": \"westd-16980\", \"gpu\": [\"cuda:0\"], \"pid\": \"106528\", \"log_path\": \"~/runs/schema_semantic_constrained_ie/mvp_phase0_violation_rate.log\", \"submitted_at\": \"2026-05-13T18:05:45.748Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema_semantic_constrained_ie/data/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/outputs/raw_outputs.jsonl\", \"wall_clock_seconds\": 4068.8, \"gpu_hours\": 1.13}, \"metrics\": {\"total_triples\": 1724, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.1537, \"entity_f1\": 0.3101, \"relation_f1\": 0.0823, \"per_relation\": {\"Used-for\": {\"total\": 787, \"dr_violations\": 6, \"rate\": 0.0076}, \"Conjunction\": {\"total\": 32, \"dr_violations\": 0, \"rate\": 0}, \"Hyponym-of\": {\"total\": 124, \"dr_violations\": 18, \"rate\": 0.1452}, \"Evaluate-for\": {\"total\": 133, \"dr_violations\": 32, \"rate\": 0.2406}, \"Part-of\": {\"total\": 72, \"dr_violations\": 18, \"rate\": 0.25}, \"Feature-of\": {\"total\": 486, \"dr_violations\": 163, \"rate\": 0.3354}, \"Compare\": {\"total\": 66, \"dr_violations\": 28, \"rate\": 0.4242}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T19:13:34.510Z\"}}, \"count\": 53, \"total\": 53, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.244}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

The registry is large. Let me extract the specific experiments I need using targeted queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "05971a8a-1744-4406-9499-4a5509225c1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoXQCQn4HC9MoU5bbVoNui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 24206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01Li8LmpJMwrYkZJB2Esgx8G`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(json.loads(sys.stdin.read())['result'])\n\n# List of experiment IDs we need\nneeded = [\n    # Table 2 ZS constrained\n    'phase2_scierc_full_s1', 'phase2_docred_full_s1',\n    'phase2_llama_scierc_full_s1', 'phase2_llama_docred_full_s1',\n    'w6_mistral_scierc_constrained', 'w6_mistral_docred_constrained',\n    # Table 2 ZS unconstrained\n    'phase1_scierc_zs_qwen', 'phase1_docred_zs_qwen',\n    'phase2_llama_scierc_unconstrained', 'phase2_llama_docred_unconstrained',\n    'w6_mistral_scierc_unconstrained', 'w6_mistral_docred_unconstrained',\n    # Table 2 FT constrained\n    'w5_lora_scierc_constrained_eval', 'w5_qwen_docred_lora_constrained_eval',\n    'w5_llama_lora_scierc_constrained_eval', 'w5_llama_docred_lora_constrained_eval',\n    # Table 2 FT unconstrained\n    'w5_lora_scierc_unconstrained_eval', 'w5_qwen_docred_lora_unconstrained_eval',\n    'w5_llama_lora_scierc_unconstrained_eval', 'w5_llama_docred_lora_unconstrained_eval',\n    # Table 4 ablation\n    'w7_qwen_scierc_ft_grammar_only', 'w7_qwen_scierc_ft_semantic_only',\n    'w7_llama_scierc_ft_grammar_only', 'w7_llama_scierc_ft_semantic_only',\n    'w8_qwen_docred_ft_grammar_only', 'w8_qwen_docred_ft_semantic_only',\n    'w8_llama_docred_ft_grammar_only', 'w8_llama_docred_ft_semantic_only',\n    # Table 5 posthoc\n    'w8_zs_posthoc_baseline', 'w8_ft_posthoc_baseline',\n    # Table 6 latency\n    'latency_profiling_scierc', 'latency_profiling_docred',\n]\n\nfound = {}\nfor exp in data:\n    eid = exp.get('experiment_id', '')\n    if eid in needed:\n        found[eid] = {\n            'status': exp.get('status'),\n            'metrics': exp.get('metrics'),\n            'conclusion': exp.get('conclusion'),\n        }\n\n# Print what we found\nfor eid in needed:\n    if eid in found:\n        print(f'=== {eid} (status: {found[eid][\\\"status\\\"]}) ===')\n        m = found[eid]['metrics']\n        if m:\n            print(json.dumps(m, indent=2)[:2000])\n        else:\n            print('  NO METRICS')\n        print()\n    else:\n        print(f'=== {eid} === NOT FOUND')\n        print()\n\" 2>&1 | head -600\n",
  "description": "Extract needed experiment metrics from registry JSON",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d57d575e-5406-4018-97ec-240557e910a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoXQCQn4HC9MoU5bbVoNui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 24206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

_source line 13 · 2026-05-16T16:44:06.602Z_

<details><summary>↩ Tool result · `toolu_01Li8LmpJMwrYkZJB2Esgx8G`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 35, in &lt;module>
    eid = exp.get('experiment_id', '')
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "20de822e-5fb4-4a79-ae82-78055b9b11f2",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 35, in &lt;module>\n    eid = exp.get('experiment_id', '')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01AAEKPZ9EPr7SxGPQSEmCCx`</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt",
  "description": "Check file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "62b4f6b1-211d-4d77-bc30-26847f084dbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8C7Y5vLvuxa31CAzD7zCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 24721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1154
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

_source line 15 · 2026-05-16T16:44:10.133Z_

<details><summary>↩ Tool result · `toolu_01AAEKPZ9EPr7SxGPQSEmCCx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:59.297Z\", \"updated_at\": \"2026-05-16T16:22:28.075Z\", \"hypothesis\": \"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablat
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "ec367acb-ebdc-424a-a33b-1492802078ff",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"w8_qwen_docred_ft_semantic_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T10:08:59.297Z\\\", \\\"updated_at\\\": \\\"2026-05-16T16:22:28.075Z\\\", \\\"hypothesis\\\": \\\"FT Qwen DocRED + semantic_only eval: 与 grammar_only 配对，验证 semantic 层在 FT+DocRED regime 下能否独立降低 DR。预期 DR 从 0.76% 降至 ~0.3-0.5%（参照 SciERC 模式：semantic_only 降 DR 68%��。完成后 DocRED FT ablat",
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_019HRjzi83Hjk2nQk3rbYwBs`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\nneeded = [\n    'phase2_scierc_full_s1', 'phase2_docred_full_s1',\n    'phase2_llama_scierc_full_s1', 'phase2_llama_docred_full_s1',\n    'w6_mistral_scierc_constrained', 'w6_mistral_docred_constrained',\n    'phase1_scierc_zs_qwen', 'phase1_docred_zs_qwen',\n    'phase2_llama_scierc_unconstrained', 'phase2_llama_docred_unconstrained',\n    'w6_mistral_scierc_unconstrained', 'w6_mistral_docred_unconstrained',\n    'w5_lora_scierc_constrained_eval', 'w5_qwen_docred_lora_constrained_eval',\n    'w5_llama_lora_scierc_constrained_eval', 'w5_llama_docred_lora_constrained_eval',\n    'w5_lora_scierc_unconstrained_eval', 'w5_qwen_docred_lora_unconstrained_eval',\n    'w5_llama_lora_scierc_unconstrained_eval', 'w5_llama_docred_lora_unconstrained_eval',\n    'w7_qwen_scierc_ft_grammar_only', 'w7_qwen_scierc_ft_semantic_only',\n    'w7_llama_scierc_ft_grammar_only', 'w7_llama_scierc_ft_semantic_only',\n    'w8_qwen_docred_ft_grammar_only', 'w8_qwen_docred_ft_semantic_only',\n    'w8_llama_docred_ft_grammar_only', 'w8_llama_docred_ft_semantic_only',\n    'w8_zs_posthoc_baseline', 'w8_ft_posthoc_baseline',\n    'latency_profiling_scierc', 'latency_profiling_docred',\n]\n\nfor eid in needed:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f'=== {eid} (status: {exp.get(\\\"status\\\")}) ===')\n        m = exp.get('metrics')\n        if m:\n            print(json.dumps(m, indent=2)[:3000])\n        else:\n            print('  NO METRICS')\n    else:\n        print(f'=== {eid} === NOT FOUND')\n    print()\n\" 2>&1",
  "description": "Extract metrics from registry experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d9bb8f86-a684-4710-86bf-c70c5319b25f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xcagQjKYrjF7YJRg7ajEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 25875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 17 · 2026-05-16T16:44:19.443Z_

<details><summary>↩ Tool result · `toolu_019HRjzi83Hjk2nQk3rbYwBs`</summary>

```text
=== phase2_scierc_full_s1 (status: DONE) ===
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

=== phase2_docred_full_s1 (status: DONE) ===
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

=== phase2_llama_scierc_full_s1 === NOT FOUND

=== phase2_llama_docred_full_s1 === NOT FOUND

=== w6_mistral_scierc_constrained (status: DONE) ===
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

=== w6_mistral_docred_constrained (status: DONE) ===
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

=== phase1_scierc_zs_qwen === NOT FOUND

=== phase1_docred_zs_qwen === NOT FOUND

=== phase2_llama_scierc_unconstrained === NOT FOUND

=== phase2_llama_docred_unconstrained === NOT FOUND

=== w6_mistral_scierc_unconstrained (status: DONE) ===
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

=== w6_mistral_docred_unconstrained (status: DONE) ===
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

=== w5_lora_scierc_constrained_eval (status: DONE) ===
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

=== w5_qwen_docred_lora_constrained_eval (status: DONE) ===
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

=== w5_llama_lora_scierc_constrained_eval (status: DONE) ===
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

=== w5_llama_docred_lora_constrained_eval (status: DONE) ===
{
  "total": 998,
  "parse_failures": 25,
  "parse_fail_rate": 2.51,
  "entities": 19077,
  "relations": 16074,
  "entity_f1": 85.23,
  "entity_precision": 85.04,
  "entity_recall": 85.41,
  "relation_f1_all_set": 44.23,
  "relation_precision_all_set": 38.82,
  "relation_recall_all_set": 51.4,
  "et_violations": 0,
  "et_violation_rate": 0,
  "rv_violations": 0,
  "rv_violation_rate": 0,
  "dr_violations": 33,
  "dr_violation_rate": 0.2,
  "cross_field_consistency_violations": 41,
  "delta_vs_unconstrained": {
    "delta_e_f1": 1.3,
    "delta_r_f1": 0.51,
    "delta_dr": -0.29,
    "delta_rv": -0.15,
    "note": "Computed as constrained - unconstrained on full-set metrics (not intersection subset). Corrected 2026-05-16 per Reviewer audit."
  }
}

=== w5_lora_scierc_unconstrained_eval (status: DONE) ===
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

=== w5_qwen_docred_lora_unconstrained_eval (status: DONE) ===
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

=== w5_llama_lora_scierc_unconstrained_eval (status: DONE) ===
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

=== w5_llama_docred_lora_unconstrained_eval (status: DONE) ===
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

=== w7_qwen_scierc_ft_grammar_only (status: DONE) ===
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

=== w7_qwen_scierc_ft_semantic_only (status: DONE) ===
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

=== w7_llama_scierc_ft_grammar_only (status: DONE) ===
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

=== w7_llama_scierc_ft_semantic_only (status: DONE) ===
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

=== w8_qwen_docred_ft_grammar_only (status: DONE) ===
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

=== w8_qwen_docred_ft_semantic_only (status: DONE) ===
{
  "E_F1": 82.15,
  "E_P": 85.58,
  "E_R": 78.99,
  "R_F1": 40.89,
  "R_P": 36.35,
  "R_R": 46.73,
  "ET_pct": 0,
  "RV_pct": 0.23,
  "DR_pct": 0.21,
  "CF_pct": 0.27,
  "parse_fail_rate": 7.52,
  "total_samples": 998,
  "parse_failures": 75,
  "documents_checked": 923,
  "total_entities": 18025,
  "total_triples": 15909,
  "DR_violations": 34,
  "RV_violations": 37,
  "ET_violations": 0,
  "CF_violations": 49
}

=== w8_llama_docred_ft_grammar_only (status: DONE) ===
{
  "E_F1": 84.04,
  "R_F1": 43.77,
  "entity_precision": 84.99,
  "entity_recall": 83.11,
  "relation_precision": 38.6,
  "relation_recall": 50.53,
  "ET_pct": 0,
  "RV_pct": 0,
  "DR_pct": 0.51,
  "CF_pct": 0.12,
  "parse_fail_rate": 2.3,
  "total_samples": 998,
  "total_relations": 16199,
  "unique_entities": 13225,
  "parse_failures": 23
}

=== w8_llama_docred_ft_semantic_only (status: RUNNING) ===
  NO METRICS

=== w8_zs_posthoc_baseline === NOT FOUND

=== w8_ft_posthoc_baseline (status: DONE) ===
{
  "ft_regime": {
    "qwen_scierc": {
      "R_F1_before": 43.86,
      "R_F1_posthoc": 43.94,
      "R_F1_constrained": 43.77,
      "reject_rate_pct": 1.95,
      "TP_lost": 4
    },
    "llama_scierc": {
      "R_F1_before": 45.45,
      "R_F1_posthoc": 45.23,
      "R_F1_constrained": 45.47,
      "reject_rate_pct": 1.11,
      "TP_lost": 5
    },
    "qwen_docred": {
      "R_F1_before": 40.91,
      "R_F1_posthoc": 41.11,
      "R_F1_constrained": "TBD",
      "reject_rate_pct": 1.03,
      "TP_lost": 1
    },
    "llama_docred": {
      "R_F1_before": 43.77,
      "R_F1_posthoc": 43.92,
      "R_F1_constrained": 44.23,
      "reject_rate_pct": 0.64,
      "TP_lost": 1
    }
  },
  "zs_regime": {
    "mistral_scierc": {
      "triples": 1584,
      "reject_pct": 20.27,
      "R_F1_before": 0.0376,
      "R_F1_posthoc": 0.0394,
      "R_F1_constrained": 0.0367,
      "TP_before": 48,
      "TP_after": 44,
      "TP_lost": 4
    },
    "qwen_scierc": {
      "triples": 1724,
      "reject_pct": 16.76,
      "R_F1_before": 0.0823,
      "R_F1_posthoc": 0.0863,
      "R_F1_constrained": 0.0836,
      "TP_before": 111,
      "TP_after": 104,
      "TP_lost": 7
    },
    "llama_scierc": {
      "triples": 1274,
      "reject_pct": 13.89,
      "R_F1_before": 0.0268,
      "R_F1_posthoc": 0.0271,
      "R_F1_constrained": 0.0254,
      "TP_before": 30,
      "TP_after": 28,
      "TP_lost": 2
    },
    "qwen_docred": {
      "triples": 17497,
      "reject_pct": 48.12,
      "R_F1_before": 0.0774,
      "R_F1_posthoc": 0.0961,
      "R_F1_constrained": 0.0823,
      "TP_before": 1137,
      "TP_after": 1010,
      "TP_lost": 127
    },
    "llama_docred": {
      "triples": 16437,
      "reject_pct": 42.18,
      "R_F1_before": 0.0598,
      "R_F1_posthoc": 0.0744,
      "R_F1_constrained": 0.0627,
      "TP_before": 850,
      "TP_after": 802,
      "TP_lost": 48
    },
    "mistral_docred": {
      "triples": 11836,
      "reject_pct": 73.73,
      "R_F1_before": 0.0434,
      "R_F1_posthoc": 0.0385,
      "R_F1_constrained": 0.0552,
      "TP_before": 518,
      "TP_after": 292,
      "TP_lost": 226,
      "removed_RV": 4172,
      "removed_ET": 3382,
      "removed_DR": 1173,
      "note": "Only ZS case where posthoc HURTS R_F1 \u2014 73.7% rejection rate loses 43.6% of TPs"
    }
  },
  "key_finding": "ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation."
}

=== latency_profiling_scierc === NOT FOUND

=== latency_profiling_docred === NOT FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "24b4c710-b8a2-41f4-8518-5887fcb7a160",
  "tool_use_result": {
    "stdout": "=== phase2_scierc_full_s1 (status: DONE) ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1729,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0093,\n  \"cross_field_consistency_violation_rate\": 0.099,\n  \"entity_f1\": 0.3098,\n  \"entity_precision\": 0.2598,\n  \"entity_recall\": 0.3837,\n  \"relation_f1\": 0.0836,\n  \"relation_precision\": 0.0654,\n  \"relation_recall\": 0.116,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_docred_full_s1 (status: DONE) ===\n{\n  \"documents_checked\": 987,\n  \"parse_failures\": 11,\n  \"total_entities\": 20187,\n  \"total_triples\": 17341,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0.0003,\n  \"domain_range_violation_rate\": 0.1021,\n  \"cross_field_consistency_violation_rate\": 0.0257,\n  \"entity_f1\": 59.37,\n  \"entity_precision\": 58.45,\n  \"entity_recall\": 59.63,\n  \"relation_f1\": 8.23,\n  \"relation_precision\": 6.99,\n  \"relation_recall\": 10.01,\n  \"unrecognized_relations\": 5,\n  \"f1_method\": \"all_set\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_llama_scierc_full_s1 === NOT FOUND\n\n=== phase2_llama_docred_full_s1 === NOT FOUND\n\n=== w6_mistral_scierc_constrained (status: DONE) ===\n{\n  \"E_P\": 0.2437,\n  \"E_R\": 0.3144,\n  \"E_F1\": 0.2746,\n  \"R_P\": 0.0292,\n  \"R_R\": 0.0493,\n  \"R_F1\": 0.0367,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 13.4,\n  \"CF_pct\": 1.27,\n  \"CF_count\": 21,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_pred_entities\": 2162,\n  \"total_pred_relations\": 1647,\n  \"delta_vs_unconstrained\": {\n    \"delta_E_F1\": 0.0018,\n    \"delta_R_F1\": 0.0001,\n    \"delta_ET\": -1.5,\n    \"delta_RV\": 0,\n    \"delta_DR\": -43.54,\n    \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"\n  }\n}\n\n=== w6_mistral_docred_constrained (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 33.2,\n  \"CF_pct\": 0.19,\n  \"E_P\": 65.02,\n  \"E_R\": 41.4,\n  \"E_F1\": 50.59,\n  \"R_P\": 5.67,\n  \"R_R\": 5.37,\n  \"R_F1\": 5.52,\n  \"parse_fail_rate\": 0.8,\n  \"total_samples\": 998,\n  \"total_pred_entities\": 12535,\n  \"total_pred_relations\": 11554,\n  \"delta_vs_unconstrained\": {\n    \"ET_pct\": -7.58,\n    \"RV_pct\": -42.35,\n    \"DR_pct\": -24.22,\n    \"CF_pct\": -24.59,\n    \"E_F1\": 2.08,\n    \"R_F1\": 2.02\n  }\n}\n\n=== phase1_scierc_zs_qwen === NOT FOUND\n\n=== phase1_docred_zs_qwen === NOT FOUND\n\n=== phase2_llama_scierc_unconstrained === NOT FOUND\n\n=== phase2_llama_docred_unconstrained === NOT FOUND\n\n=== w6_mistral_scierc_unconstrained (status: DONE) ===\n{\n  \"E_P\": 0.2402,\n  \"E_R\": 0.3156,\n  \"E_F1\": 0.2728,\n  \"R_P\": 0.0295,\n  \"R_R\": 0.0483,\n  \"R_F1\": 0.0366,\n  \"ET_pct\": 1.5,\n  \"RV_pct\": 0,\n  \"DR_pct\": 56.94,\n  \"CF_pct\": 56.87,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_pred_entities\": 2202,\n  \"total_pred_relations\": 1593\n}\n\n=== w6_mistral_docred_unconstrained (status: DONE) ===\n{\n  \"total_samples\": 998,\n  \"parse_failures\": 7,\n  \"parse_fail_rate\": 0.7,\n  \"total_pred_entities\": 12580,\n  \"total_pred_relations\": 11879,\n  \"ET_pct\": 7.58,\n  \"RV_pct\": 42.35,\n  \"DR_pct\": 57.42,\n  \"CF_pct\": 24.78,\n  \"E_P\": 0.6221,\n  \"E_R\": 0.3975,\n  \"E_F1\": 0.4851,\n  \"R_P\": 0.0447,\n  \"R_R\": 0.0432,\n  \"R_F1\": 0.0434,\n  \"f1_method\": \"fuzzy_normalized\",\n  \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance \\u22642 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"\n}\n\n=== w5_lora_scierc_constrained_eval (status: DONE) ===\n{\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0.0118,\n  \"entity_f1\": 0.6705,\n  \"entity_precision\": 0.6523,\n  \"entity_recall\": 0.6898,\n  \"relation_f1\": 0.4377,\n  \"relation_precision\": 0.4078,\n  \"relation_recall\": 0.4723,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"total_samples\": 551,\n  \"cross_field_consistency_violations\": 21\n}\n\n=== w5_qwen_docred_lora_constrained_eval (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.01,\n  \"CF_pct\": 0.41,\n  \"E_F1\": 81.43,\n  \"E_P\": 85.41,\n  \"E_R\": 77.81,\n  \"R_F1\": 40.56,\n  \"R_P\": 36.35,\n  \"R_R\": 45.86,\n  \"parse_fail_rate\": 8.52,\n  \"total_samples\": 998,\n  \"success_samples\": 913,\n  \"fail_samples\": 85,\n  \"total_entities_pred\": 17799,\n  \"total_relations_pred\": 15563,\n  \"E_F1_excl_fail\": 85.69,\n  \"R_F1_excl_fail\": 42.23,\n  \"delta_vs_unconstrained\": {\n    \"delta_DR\": -0.75,\n    \"delta_RV\": -0.27,\n    \"delta_R_F1\": -0.3,\n    \"delta_R_F1_excl_fail\": 0.03,\n    \"DR_reduction_pct\": 98.7,\n    \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"\n  }\n}\n\n=== w5_llama_lora_scierc_constrained_eval (status: DONE) ===\n{\n  \"domain_range_violation_rate\": 0.0009,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0.0046,\n  \"relation_f1\": 0.4547,\n  \"relation_precision\": 0.432,\n  \"relation_recall\": 0.4795,\n  \"entity_f1\": 0.6776,\n  \"entity_precision\": 0.6647,\n  \"entity_recall\": 0.691,\n  \"total_relations\": 1081,\n  \"total_entities\": 1757,\n  \"total_samples\": 551,\n  \"parse_failures\": 0\n}\n\n=== w5_llama_docred_lora_constrained_eval (status: DONE) ===\n{\n  \"total\": 998,\n  \"parse_failures\": 25,\n  \"parse_fail_rate\": 2.51,\n  \"entities\": 19077,\n  \"relations\": 16074,\n  \"entity_f1\": 85.23,\n  \"entity_precision\": 85.04,\n  \"entity_recall\": 85.41,\n  \"relation_f1_all_set\": 44.23,\n  \"relation_precision_all_set\": 38.82,\n  \"relation_recall_all_set\": 51.4,\n  \"et_violations\": 0,\n  \"et_violation_rate\": 0,\n  \"rv_violations\": 0,\n  \"rv_violation_rate\": 0,\n  \"dr_violations\": 33,\n  \"dr_violation_rate\": 0.2,\n  \"cross_field_consistency_violations\": 41,\n  \"delta_vs_unconstrained\": {\n    \"delta_e_f1\": 1.3,\n    \"delta_r_f1\": 0.51,\n    \"delta_dr\": -0.29,\n    \"delta_rv\": -0.15,\n    \"note\": \"Computed as constrained - unconstrained on full-set metrics (not intersection subset). Corrected 2026-05-16 per Reviewer audit.\"\n  }\n}\n\n=== w5_lora_scierc_unconstrained_eval (status: DONE) ===\n{\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0195,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"entity_f1\": 0.6705,\n  \"entity_precision\": 0.6523,\n  \"entity_recall\": 0.6898,\n  \"relation_f1\": 0.4386,\n  \"relation_precision\": 0.4087,\n  \"relation_recall\": 0.4733,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"domain_range_violations\": 22,\n  \"go_nogo_metric\": 0.0195,\n  \"dr_gate\": \"FAILED\"\n}\n\n=== w5_qwen_docred_lora_unconstrained_eval (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.27,\n  \"DR_pct\": 0.76,\n  \"CF_pct\": 0.12,\n  \"E_F1\": 82.15,\n  \"E_P\": 85.44,\n  \"E_R\": 79.11,\n  \"R_F1\": 40.86,\n  \"R_P\": 36.41,\n  \"R_R\": 46.56,\n  \"parse_fail_rate\": 7.11,\n  \"total_samples\": 998,\n  \"success_samples\": 927,\n  \"fail_samples\": 71,\n  \"total_entities_pred\": 18091,\n  \"total_relations_pred\": 15870,\n  \"ET_pct_excl_fail\": 0,\n  \"RV_pct_excl_fail\": 0.27,\n  \"DR_pct_excl_fail\": 0.76,\n  \"CF_pct_excl_fail\": 0.12,\n  \"E_F1_excl_fail\": 85.72,\n  \"E_P_excl_fail\": 85.44,\n  \"E_R_excl_fail\": 86,\n  \"R_F1_excl_fail\": 42.2,\n  \"R_P_excl_fail\": 36.41,\n  \"R_R_excl_fail\": 50.17\n}\n\n=== w5_llama_lora_scierc_unconstrained_eval (status: DONE) ===\n{\n  \"total_samples\": 551,\n  \"total_entities\": 1757,\n  \"total_relations\": 1082,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0111,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"total_violation_rate\": 0.0042,\n  \"entity_precision\": 0.6647,\n  \"entity_recall\": 0.691,\n  \"entity_f1\": 0.6776,\n  \"relation_precision\": 0.432,\n  \"relation_recall\": 0.4795,\n  \"relation_f1\": 0.4545\n}\n\n=== w5_llama_docred_lora_unconstrained_eval (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.15,\n  \"DR_pct\": 0.49,\n  \"E_F1\": 83.93,\n  \"E_P\": 84.93,\n  \"E_R\": 82.96,\n  \"R_F1\": 43.72,\n  \"R_P\": 38.59,\n  \"R_R\": 50.41,\n  \"parse_fail_rate\": 2.3,\n  \"total_samples\": 998,\n  \"total_entities_pred\": 19106,\n  \"total_relations_pred\": 16171\n}\n\n=== w7_qwen_scierc_ft_grammar_only (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 1.9,\n  \"CF_pct\": 0,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"E_P\": 0.6523,\n  \"E_R\": 0.6898,\n  \"E_F1\": 0.6705,\n  \"R_P\": 0.4087,\n  \"R_R\": 0.4733,\n  \"R_F1\": 0.4386,\n  \"DR_violations\": 22,\n  \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"\n}\n\n=== w7_qwen_scierc_ft_semantic_only (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.6,\n  \"CF_count\": 15,\n  \"parse_fail_rate\": 0,\n  \"total_samples\": 551,\n  \"total_entities\": 1784,\n  \"total_relations\": 1128,\n  \"E_P\": 0.6523,\n  \"E_R\": 0.6898,\n  \"E_F1\": 0.6705,\n  \"R_P\": 0.4073,\n  \"R_R\": 0.4713,\n  \"R_F1\": 0.4369,\n  \"DR_violations\": 7,\n  \"delta_vs_grammar_only\": {\n    \"DR_delta\": -1.3,\n    \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"\n  },\n  \"delta_vs_unconstrained\": {\n    \"DR_delta\": -1.35,\n    \"note\": \"unconstrained DR=1.95% \\u2192 semantic_only 0.6%\"\n  }\n}\n\n=== w7_llama_scierc_ft_grammar_only (status: DONE) ===\n{\n  \"total_samples\": 551,\n  \"json_parse_failures\": 0,\n  \"total_entities\": 1757,\n  \"total_relations\": 1082,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.0111,\n  \"cross_field_consistency_violation_rate\": 0,\n  \"entity_f1\": {\n    \"precision\": 0.6647,\n    \"recall\": 0.691,\n    \"f1\": 0.6776\n  },\n  \"relation_f1\": {\n    \"precision\": 0.432,\n    \"recall\": 0.4795,\n    \"f1\": 0.4545\n  }\n}\n\n=== w7_llama_scierc_ft_semantic_only (status: DONE) ===\n{\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.65,\n  \"CF_count\": 2,\n  \"E_F1\": 67.76,\n  \"E_P\": 66.47,\n  \"E_R\": 69.1,\n  \"R_F1\": 45.47,\n  \"R_P\": 43.24,\n  \"R_R\": 47.95,\n  \"total_entities\": 1757,\n  \"total_relations\": 1081,\n  \"json_parse_failures\": 0\n}\n\n=== w8_qwen_docred_ft_grammar_only (status: DONE) ===\n{\n  \"E_F1\": 82.19,\n  \"E_P\": 85.47,\n  \"E_R\": 79.16,\n  \"R_F1\": 40.85,\n  \"R_P\": 36.27,\n  \"R_R\": 46.77,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.61,\n  \"CF_pct\": 0.11,\n  \"parse_fail_rate\": 7.01,\n  \"total_samples\": 998,\n  \"parse_failures\": 70\n}\n\n=== w8_qwen_docred_ft_semantic_only (status: DONE) ===\n{\n  \"E_F1\": 82.15,\n  \"E_P\": 85.58,\n  \"E_R\": 78.99,\n  \"R_F1\": 40.89,\n  \"R_P\": 36.35,\n  \"R_R\": 46.73,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0.23,\n  \"DR_pct\": 0.21,\n  \"CF_pct\": 0.27,\n  \"parse_fail_rate\": 7.52,\n  \"total_samples\": 998,\n  \"parse_failures\": 75,\n  \"documents_checked\": 923,\n  \"total_entities\": 18025,\n  \"total_triples\": 15909,\n  \"DR_violations\": 34,\n  \"RV_violations\": 37,\n  \"ET_violations\": 0,\n  \"CF_violations\": 49\n}\n\n=== w8_llama_docred_ft_grammar_only (status: DONE) ===\n{\n  \"E_F1\": 84.04,\n  \"R_F1\": 43.77,\n  \"entity_precision\": 84.99,\n  \"entity_recall\": 83.11,\n  \"relation_precision\": 38.6,\n  \"relation_recall\": 50.53,\n  \"ET_pct\": 0,\n  \"RV_pct\": 0,\n  \"DR_pct\": 0.51,\n  \"CF_pct\": 0.12,\n  \"parse_fail_rate\": 2.3,\n  \"total_samples\": 998,\n  \"total_relations\": 16199,\n  \"unique_entities\": 13225,\n  \"parse_failures\": 23\n}\n\n=== w8_llama_docred_ft_semantic_only (status: RUNNING) ===\n  NO METRICS\n\n=== w8_zs_posthoc_baseline === NOT FOUND\n\n=== w8_ft_posthoc_baseline (status: DONE) ===\n{\n  \"ft_regime\": {\n    \"qwen_scierc\": {\n      \"R_F1_before\": 43.86,\n      \"R_F1_posthoc\": 43.94,\n      \"R_F1_constrained\": 43.77,\n      \"reject_rate_pct\": 1.95,\n      \"TP_lost\": 4\n    },\n    \"llama_scierc\": {\n      \"R_F1_before\": 45.45,\n      \"R_F1_posthoc\": 45.23,\n      \"R_F1_constrained\": 45.47,\n      \"reject_rate_pct\": 1.11,\n      \"TP_lost\": 5\n    },\n    \"qwen_docred\": {\n      \"R_F1_before\": 40.91,\n      \"R_F1_posthoc\": 41.11,\n      \"R_F1_constrained\": \"TBD\",\n      \"reject_rate_pct\": 1.03,\n      \"TP_lost\": 1\n    },\n    \"llama_docred\": {\n      \"R_F1_before\": 43.77,\n      \"R_F1_posthoc\": 43.92,\n      \"R_F1_constrained\": 44.23,\n      \"reject_rate_pct\": 0.64,\n      \"TP_lost\": 1\n    }\n  },\n  \"zs_regime\": {\n    \"mistral_scierc\": {\n      \"triples\": 1584,\n      \"reject_pct\": 20.27,\n      \"R_F1_before\": 0.0376,\n      \"R_F1_posthoc\": 0.0394,\n      \"R_F1_constrained\": 0.0367,\n      \"TP_before\": 48,\n      \"TP_after\": 44,\n      \"TP_lost\": 4\n    },\n    \"qwen_scierc\": {\n      \"triples\": 1724,\n      \"reject_pct\": 16.76,\n      \"R_F1_before\": 0.0823,\n      \"R_F1_posthoc\": 0.0863,\n      \"R_F1_constrained\": 0.0836,\n      \"TP_before\": 111,\n      \"TP_after\": 104,\n      \"TP_lost\": 7\n    },\n    \"llama_scierc\": {\n      \"triples\": 1274,\n      \"reject_pct\": 13.89,\n      \"R_F1_before\": 0.0268,\n      \"R_F1_posthoc\": 0.0271,\n      \"R_F1_constrained\": 0.0254,\n      \"TP_before\": 30,\n      \"TP_after\": 28,\n      \"TP_lost\": 2\n    },\n    \"qwen_docred\": {\n      \"triples\": 17497,\n      \"reject_pct\": 48.12,\n      \"R_F1_before\": 0.0774,\n      \"R_F1_posthoc\": 0.0961,\n      \"R_F1_constrained\": 0.0823,\n      \"TP_before\": 1137,\n      \"TP_after\": 1010,\n      \"TP_lost\": 127\n    },\n    \"llama_docred\": {\n      \"triples\": 16437,\n      \"reject_pct\": 42.18,\n      \"R_F1_before\": 0.0598,\n      \"R_F1_posthoc\": 0.0744,\n      \"R_F1_constrained\": 0.0627,\n      \"TP_before\": 850,\n      \"TP_after\": 802,\n      \"TP_lost\": 48\n    },\n    \"mistral_docred\": {\n      \"triples\": 11836,\n      \"reject_pct\": 73.73,\n      \"R_F1_before\": 0.0434,\n      \"R_F1_posthoc\": 0.0385,\n      \"R_F1_constrained\": 0.0552,\n      \"TP_before\": 518,\n      \"TP_after\": 292,\n      \"TP_lost\": 226,\n      \"removed_RV\": 4172,\n      \"removed_ET\": 3382,\n      \"removed_DR\": 1173,\n      \"note\": \"Only ZS case where posthoc HURTS R_F1 \\u2014 73.7% rejection rate loses 43.6% of TPs\"\n    }\n  },\n  \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"\n}\n\n=== latency_profiling_scierc === NOT FOUND\n\n=== latency_profiling_docred === NOT FOUND",
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

_source line 18_

Now let me search for the missing experiments with alternative names.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "caff9ab5-07bd-4cd6-ac01-a9f231c9ae11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145ZaRtcWGdVye1g6RpHo3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7941,
      "cache_read_input_tokens": 26277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7941
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1EHwDbmF3af7qu2c3MYDy`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea_gen_0509_6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Search for llama ZS experiments and latency/posthoc\nfor eid in sorted(experiments.keys()):\n    if any(k in eid for k in ['llama_scierc', 'llama_docred', 'latency', 'posthoc', 'phase1', 'phase2_llama', 'qwen_scierc_zs', 'qwen_docred_zs']):\n        exp = experiments[eid]\n        print(f'{eid} (status: {exp.get(\\\"status\\\")})')\n\" 2>&1",
  "description": "Search for missing experiment IDs",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "468a221d-f81b-437f-932e-4dfdd3758988",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145ZaRtcWGdVye1g6RpHo3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7941,
      "cache_read_input_tokens": 26277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7941
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

_source line 20 · 2026-05-16T16:44:31.683Z_

<details><summary>↩ Tool result · reported error · `toolu_01W1EHwDbmF3af7qu2c3MYDy`</summary>

```text
Exit code 1
cat: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea_gen_0509_6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt: No such file or directory
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    raw = json.loads(sys.stdin.read())['result']
          ~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "dee4b9cb-7001-45c1-905d-fe78ed69b4cc",
  "tool_use_result": "Error: Exit code 1\ncat: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea_gen_0509_6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt: No such file or directory\nTraceback (most recent call last):\n  File \"&lt;string>\", line 4, in &lt;module>\n    raw = json.loads(sys.stdin.read())['result']\n          ~~~~~~~~~~^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01X8hryJJtN7pyJcQHP5swLb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Search for llama ZS experiments and latency/posthoc\nfor eid in sorted(experiments.keys()):\n    if any(k in eid for k in ['llama_scierc', 'llama_docred', 'latency', 'posthoc', 'phase1', 'phase2_llama', 'qwen_scierc_zs', 'qwen_docred_zs']):\n        exp = experiments[eid]\n        print(f'{eid} (status: {exp.get(\\\"status\\\")})')\n\" 2>&1",
  "description": "Search for missing experiment IDs (corrected path)",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "f2c5ae82-81e7-4081-91c6-4ac734965f3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SJi4VUccFLii7XndcBKqr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 34218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 743
      },
      "output_tokens": 57,
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

_source line 22 · 2026-05-16T16:44:36.820Z_

<details><summary>↩ Tool result · `toolu_01X8hryJJtN7pyJcQHP5swLb`</summary>

```text
llama_docred_full_s1 (status: DONE)
llama_docred_full_s1_mt6144 (status: DONE)
llama_docred_unconstrained (status: DONE)
llama_docred_unconstrained_mt6144 (status: DONE)
llama_scierc_full_s1 (status: DONE)
llama_scierc_unconstrained (status: DONE)
posthoc_filtering_baseline (status: DONE)
w1_cf_fallback_llama_docred (status: DONE)
w1_cf_fallback_llama_scierc (status: DONE)
w5_llama_docred_lora_constrained_eval (status: DONE)
w5_llama_docred_lora_training (status: DONE)
w5_llama_docred_lora_unconstrained_eval (status: DONE)
w5_llama_docred_sft_data_gen (status: DONE)
w7_llama_scierc_ft_grammar_only (status: DONE)
w7_llama_scierc_ft_semantic_only (status: DONE)
w8_ft_posthoc_baseline (status: DONE)
w8_llama_docred_ft_grammar_only (status: DONE)
w8_llama_docred_ft_semantic_only (status: RUNNING)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "0b6d6803-a995-4db8-a283-7f168fc8138e",
  "tool_use_result": {
    "stdout": "llama_docred_full_s1 (status: DONE)\nllama_docred_full_s1_mt6144 (status: DONE)\nllama_docred_unconstrained (status: DONE)\nllama_docred_unconstrained_mt6144 (status: DONE)\nllama_scierc_full_s1 (status: DONE)\nllama_scierc_unconstrained (status: DONE)\nposthoc_filtering_baseline (status: DONE)\nw1_cf_fallback_llama_docred (status: DONE)\nw1_cf_fallback_llama_scierc (status: DONE)\nw5_llama_docred_lora_constrained_eval (status: DONE)\nw5_llama_docred_lora_training (status: DONE)\nw5_llama_docred_lora_unconstrained_eval (status: DONE)\nw5_llama_docred_sft_data_gen (status: DONE)\nw7_llama_scierc_ft_grammar_only (status: DONE)\nw7_llama_scierc_ft_semantic_only (status: DONE)\nw8_ft_posthoc_baseline (status: DONE)\nw8_llama_docred_ft_grammar_only (status: DONE)\nw8_llama_docred_ft_semantic_only (status: RUNNING)",
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_014C5AxAiBGgXVSrrcQGjVNJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Get metrics for the correct names\nneeded2 = ['llama_scierc_full_s1', 'llama_docred_full_s1', 'llama_scierc_unconstrained', 'llama_docred_unconstrained', 'posthoc_filtering_baseline']\nfor eid in needed2:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f'=== {eid} (status: {exp.get(\\\"status\\\")}) ===')\n        m = exp.get('metrics')\n        if m:\n            print(json.dumps(m, indent=2)[:2000])\n        else:\n            print('  NO METRICS')\n    else:\n        print(f'=== {eid} === NOT FOUND')\n    print()\n\" 2>&1",
  "description": "Get metrics for alternative experiment names",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "938b0bde-6928-48c1-8519-3e943e464f7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ezv1ai7cLoyeFQCjaXbz35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 34961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 853
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

_source line 24 · 2026-05-16T16:44:43.168Z_

<details><summary>↩ Tool result · `toolu_014C5AxAiBGgXVSrrcQGjVNJ`</summary>

```text
=== llama_scierc_full_s1 (status: DONE) ===
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

=== llama_docred_full_s1 (status: DONE) ===
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

=== llama_scierc_unconstrained (status: DONE) ===
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

=== llama_docred_unconstrained (status: DONE) ===
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

=== posthoc_filtering_baseline (status: DONE) ===
{
  "docred_f1_before": 7.74,
  "docred_f1_after": 9.61,
  "docred_precision_before": 6.55,
  "docred_precision_after": 11.22,
  "docred_recall_before": 9.46,
  "docred_recall_after": 8.4,
  "docred_rejection_rate": 0.481,
  "docred_tp_before": 1137,
  "docred_tp_after": 1010,
  "docred_tp_lost": 127,
  "docred_et_residual": 0.0247,
  "scierc_f1_before": 8.23,
  "scierc_f1_after": 8.63,
  "scierc_rejection_rate": 0.168,
  "scierc_recall_before": 11.4,
  "scierc_recall_after": 10.68,
  "scierc_tp_before": 111,
  "scierc_tp_after": 104
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "ab68a3a3-d45a-48a3-8717-792d0a3772ad",
  "tool_use_result": {
    "stdout": "=== llama_scierc_full_s1 (status: DONE) ===\n{\n  \"samples\": 550,\n  \"entities_extracted\": 2469,\n  \"relations_extracted\": 1315,\n  \"domain_range_violation_rate\": 0.0008,\n  \"relation_vocab_violation_rate\": 0,\n  \"entity_type_violation_rate\": 0,\n  \"cross_field_consistency_violation_rate\": 0.0656,\n  \"total_violation_rate\": 0.0431,\n  \"entity_f1\": 0.2349,\n  \"entity_precision\": 0.1972,\n  \"entity_recall\": 0.2902,\n  \"relation_f1\": 0.0254,\n  \"relation_precision\": 0.0221,\n  \"relation_recall\": 0.0298,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== llama_docred_full_s1 (status: DONE) ===\n{\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\",\n  \"f1_method\": \"all_set\",\n  \"violations\": {\n    \"ET\": 0,\n    \"RV\": 0,\n    \"DR\": 2.55,\n    \"CF\": 12.02\n  },\n  \"f1\": {\n    \"entity_f1\": 55.01,\n    \"entity_precision\": 61.41,\n    \"entity_recall\": 49.82,\n    \"relation_f1\": 6.27,\n    \"relation_precision\": 5.49,\n    \"relation_recall\": 7.32\n  },\n  \"counts\": {\n    \"documents\": 998,\n    \"documents_checked\": 907,\n    \"parse_failures\": 91,\n    \"unique_entities\": 11296,\n    \"triples\": 16368\n  }\n}\n\n=== llama_scierc_unconstrained (status: DONE) ===\n{\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocab_violation_rate\": 0.0055,\n  \"domain_range_violation_rate\": 0.1334,\n  \"cross_field_consistency_violations\": 6,\n  \"entity_f1\": 0.2356,\n  \"entity_precision\": 0.1983,\n  \"entity_recall\": 0.2902,\n  \"relation_f1\": 0.0268,\n  \"relation_precision\": 0.0236,\n  \"relation_recall\": 0.031,\n  \"total_entities\": 2451,\n  \"total_relations\": 1274,\n  \"json_parse_failures\": 1,\n  \"samples\": 551,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== llama_docred_unconstrained (status: DONE) ===\n{\n  \"checker_version\": \"fixed_20260514_v2\",\n  \"f1_method\": \"all_set\",\n  \"documents\": 998,\n  \"documents_checked\": 930,\n  \"parse_failures\": 68,\n  \"unique_entities\": 11525,\n  \"total_triples\": 16437,\n  \"dr_eligible_triples\": 13789,\n  \"ET_rate_pct\": 0.13,\n  \"RV_rate_pct\": 16.03,\n  \"DR_rate_pct\": 26.07,\n  \"CF_rate_pct\": 0.17,\n  \"entity_precision\": 61.22,\n  \"entity_recall\": 51.02,\n  \"entity_f1\": 55.65,\n  \"relation_precision\": 5.22,\n  \"relation_recall\": 7,\n  \"relation_f1\": 5.98,\n  \"fuzzy_relation_matches\": 121\n}\n\n=== posthoc_filtering_baseline (status: DONE) ===\n{\n  \"docred_f1_before\": 7.74,\n  \"docred_f1_after\": 9.61,\n  \"docred_precision_before\": 6.55,\n  \"docred_precision_after\": 11.22,\n  \"docred_recall_before\": 9.46,\n  \"docred_recall_after\": 8.4,\n  \"docred_rejection_rate\": 0.481,\n  \"docred_tp_before\": 1137,\n  \"docred_tp_after\": 1010,\n  \"docred_tp_lost\": 127,\n  \"docred_et_residual\": 0.0247,\n  \"scierc_f1_before\": 8.23,\n  \"scierc_f1_after\": 8.63,\n  \"scierc_rejection_rate\": 0.168,\n  \"scierc_recall_before\": 11.4,\n  \"scierc_recall_after\": 10.68,\n  \"scierc_tp_before\": 111,\n  \"scierc_tp_after\": 104\n}",
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

_source line 25_

Now let me look for Qwen ZS unconstrained baselines and latency data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "0d517d48-e278-4468-a613-c0dd281446fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wPGDrwMrMMQETMn7PFRbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 35814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1733
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hd24TkuPK33xDAJ6ZPn4cC`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Search for qwen unconstrained ZS\nfor eid in sorted(experiments.keys()):\n    if any(k in eid for k in ['qwen', 'latency', 'phase1', 'scierc_zs', 'docred_zs', 'unconstrained_s1', 'scierc_full', 'docred_full']):\n        if 'lora' not in eid and 'w5' not in eid and 'w7' not in eid and 'w8' not in eid:\n            exp = experiments[eid]\n            print(f'{eid} (status: {exp.get(\\\"status\\\")})')\n\" 2>&1",
  "description": "Search for Qwen ZS unconstrained and latency experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d114e2ad-1fa2-46fa-8954-cf6de2522faf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wPGDrwMrMMQETMn7PFRbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1733,
      "cache_read_input_tokens": 35814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1733
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

_source line 27 · 2026-05-16T16:44:49.627Z_

<details><summary>↩ Tool result · `toolu_01Hd24TkuPK33xDAJ6ZPn4cC`</summary>

```text
llama_docred_full_s1 (status: DONE)
llama_docred_full_s1_mt6144 (status: DONE)
llama_scierc_full_s1 (status: DONE)
phase2_docred_full_s1 (status: DONE)
phase2_scierc_full_s1 (status: DONE)
phase2_scierc_full_s2 (status: DONE)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "cf69977e-81d7-4d5d-9308-ae02f04d7f31",
  "tool_use_result": {
    "stdout": "llama_docred_full_s1 (status: DONE)\nllama_docred_full_s1_mt6144 (status: DONE)\nllama_scierc_full_s1 (status: DONE)\nphase2_docred_full_s1 (status: DONE)\nphase2_scierc_full_s1 (status: DONE)\nphase2_scierc_full_s2 (status: DONE)",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01817YerM18T2xPUU5kF8WAi`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Search for qwen unconstrained, phase1, latency\nfor eid in sorted(experiments.keys()):\n    if 'unconstrained' in eid or 'latency' in eid or 'phase1' in eid:\n        exp = experiments[eid]\n        print(f'{eid} (status: {exp.get(\\\"status\\\")})')\n\" 2>&1",
  "description": "Search for all unconstrained and latency experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "f7794d22-3a0a-4e35-b4cf-145e11acd1fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqecQKf7tHxUWfJZW8iELo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 559,
      "cache_read_input_tokens": 37547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 559
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

_source line 29 · 2026-05-16T16:44:54.420Z_

<details><summary>↩ Tool result · `toolu_01817YerM18T2xPUU5kF8WAi`</summary>

```text
llama_docred_unconstrained (status: DONE)
llama_docred_unconstrained_mt6144 (status: DONE)
llama_scierc_unconstrained (status: DONE)
phase2_docred_unconstrained (status: DONE)
phase2_scierc_unconstrained (status: DONE)
w5_llama_docred_lora_unconstrained_eval (status: DONE)
w5_llama_lora_scierc_unconstrained_eval (status: DONE)
w5_lora_scierc_unconstrained_eval (status: DONE)
w5_qwen_docred_lora_unconstrained_eval (status: DONE)
w6_mistral_docred_unconstrained (status: DONE)
w6_mistral_scierc_unconstrained (status: DONE)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "00e24e31-482f-4fbf-be6e-fc7229c3fff9",
  "tool_use_result": {
    "stdout": "llama_docred_unconstrained (status: DONE)\nllama_docred_unconstrained_mt6144 (status: DONE)\nllama_scierc_unconstrained (status: DONE)\nphase2_docred_unconstrained (status: DONE)\nphase2_scierc_unconstrained (status: DONE)\nw5_llama_docred_lora_unconstrained_eval (status: DONE)\nw5_llama_lora_scierc_unconstrained_eval (status: DONE)\nw5_lora_scierc_unconstrained_eval (status: DONE)\nw5_qwen_docred_lora_unconstrained_eval (status: DONE)\nw6_mistral_docred_unconstrained (status: DONE)\nw6_mistral_scierc_unconstrained (status: DONE)",
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_011wq6Ao81DAi6R8aXxtoU3t`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\nneeded = ['phase2_scierc_unconstrained', 'phase2_docred_unconstrained']\nfor eid in needed:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f'=== {eid} (status: {exp.get(\\\"status\\\")}) ===')\n        m = exp.get('metrics')\n        if m:\n            print(json.dumps(m, indent=2)[:2000])\n        else:\n            print('  NO METRICS')\n    print()\n\" 2>&1",
  "description": "Get Qwen unconstrained ZS metrics",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "9fba8311-2441-40e7-9bf7-863d7eb3bd32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZrUv95pR2g4eDzZi7C2sv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 38106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
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

_source line 31 · 2026-05-16T16:45:00.938Z_

<details><summary>↩ Tool result · `toolu_011wq6Ao81DAi6R8aXxtoU3t`</summary>

```text
=== phase2_scierc_unconstrained (status: DONE) ===
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

=== phase2_docred_unconstrained (status: DONE) ===
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "33be2dad-937d-4cce-914b-6c028361c8ce",
  "tool_use_result": {
    "stdout": "=== phase2_scierc_unconstrained (status: DONE) ===\n{\n  \"json_parse_rate\": 1,\n  \"entity_f1\": 0.3101,\n  \"entity_precision\": 0.2605,\n  \"entity_recall\": 0.3831,\n  \"relation_f1\": 0.0823,\n  \"relation_precision\": 0.0644,\n  \"relation_recall\": 0.114,\n  \"entity_type_violation_rate\": 0.004,\n  \"relation_vocabulary_violation_rate\": 0.0139,\n  \"domain_range_violation_rate\": 0.1537,\n  \"cross_field_consistency_violation_rate\": 0.0008,\n  \"total_triples\": 1724,\n  \"total_entities\": 2474,\n  \"total_samples\": 551,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_docred_unconstrained (status: DONE) ===\n{\n  \"documents_checked\": 986,\n  \"parse_failures\": 12,\n  \"total_entities\": 20171,\n  \"total_triples\": 17497,\n  \"entity_type_violation_rate\": 0.0248,\n  \"relation_vocabulary_violation_rate\": 0.2966,\n  \"domain_range_violation_rate\": 0.1846,\n  \"cross_field_consistency_violation_rate\": 0.001,\n  \"entity_f1\": 58.15,\n  \"entity_precision\": 57.26,\n  \"entity_recall\": 58.32,\n  \"relation_f1\": 7.74,\n  \"relation_precision\": 6.55,\n  \"relation_recall\": 9.46,\n  \"unrecognized_relations\": 5189,\n  \"f1_method\": \"all_set (includes OOV predictions in denominator)\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\",\n  \"et_v1\": 0.0818,\n  \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"\n}",
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

_source line 32_

Now let me check for latency profiling data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "b016589f-4fd6-4464-a8cb-f280c1a8eab5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjsUupeY4oVTyT4tztpUrU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 38670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_014foctCBFHzYjcSrqQa8P4H`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Search for latency\nfor eid in sorted(experiments.keys()):\n    if 'latency' in eid or 'throughput' in eid or 'speed' in eid or 'profil' in eid:\n        print(eid)\n\n# Also list all experiment keys for reference\nprint('\\\\n--- ALL EXPERIMENT IDS ---')\nfor eid in sorted(experiments.keys()):\n    print(eid)\n\" 2>&1",
  "description": "List all experiment IDs to find latency data",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "b1156642-40a2-4a06-adfe-67df1d2ec0c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjsUupeY4oVTyT4tztpUrU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 38670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 34 · 2026-05-16T16:45:06.760Z_

<details><summary>↩ Tool result · `toolu_014foctCBFHzYjcSrqQa8P4H`</summary>

```text
--- ALL EXPERIMENT IDS ---
llama_docred_full_s1
llama_docred_full_s1_mt6144
llama_docred_unconstrained
llama_docred_unconstrained_mt6144
llama_scierc_full_s1
llama_scierc_unconstrained
mvp_phase0_docred_schema
mvp_phase0_docred_schema_r2
mvp_phase0_scierc_schema
mvp_phase0_violation_rate
mvp_phase0_violation_rate_docred
phase2_docred_full_s1
phase2_docred_grammar_only
phase2_docred_semantic_only
phase2_docred_unconstrained
phase2_s2_pilot50
phase2_scierc_full_s1
phase2_scierc_full_s2
phase2_scierc_grammar_only
phase2_scierc_semantic_only
phase2_scierc_unconstrained
posthoc_filtering_baseline
w1_cf_fallback_docred
w1_cf_fallback_llama_docred
w1_cf_fallback_llama_scierc
w1_cf_fallback_scierc_pilot
w5_docred_sft_data_gen
w5_llama_docred_lora_constrained_eval
w5_llama_docred_lora_training
w5_llama_docred_lora_unconstrained_eval
w5_llama_docred_sft_data_gen
w5_llama_lora_scierc_constrained_eval
w5_llama_lora_scierc_training
w5_llama_lora_scierc_unconstrained_eval
w5_lora_scierc_constrained_eval
w5_lora_scierc_training
w5_lora_scierc_unconstrained_eval
w5_qwen_docred_lora_constrained_eval
w5_qwen_docred_lora_training
w5_qwen_docred_lora_unconstrained_eval
w6_mistral_docred_constrained
w6_mistral_docred_unconstrained
w6_mistral_scierc_constrained
w6_mistral_scierc_unconstrained
w7_llama_scierc_ft_grammar_only
w7_llama_scierc_ft_semantic_only
w7_qwen_scierc_ft_grammar_only
w7_qwen_scierc_ft_semantic_only
w8_ft_posthoc_baseline
w8_llama_docred_ft_grammar_only
w8_llama_docred_ft_semantic_only
w8_qwen_docred_ft_grammar_only
w8_qwen_docred_ft_semantic_only
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "904705ee-1a45-4bd0-a490-a206a0780e12",
  "tool_use_result": {
    "stdout": "--- ALL EXPERIMENT IDS ---\nllama_docred_full_s1\nllama_docred_full_s1_mt6144\nllama_docred_unconstrained\nllama_docred_unconstrained_mt6144\nllama_scierc_full_s1\nllama_scierc_unconstrained\nmvp_phase0_docred_schema\nmvp_phase0_docred_schema_r2\nmvp_phase0_scierc_schema\nmvp_phase0_violation_rate\nmvp_phase0_violation_rate_docred\nphase2_docred_full_s1\nphase2_docred_grammar_only\nphase2_docred_semantic_only\nphase2_docred_unconstrained\nphase2_s2_pilot50\nphase2_scierc_full_s1\nphase2_scierc_full_s2\nphase2_scierc_grammar_only\nphase2_scierc_semantic_only\nphase2_scierc_unconstrained\nposthoc_filtering_baseline\nw1_cf_fallback_docred\nw1_cf_fallback_llama_docred\nw1_cf_fallback_llama_scierc\nw1_cf_fallback_scierc_pilot\nw5_docred_sft_data_gen\nw5_llama_docred_lora_constrained_eval\nw5_llama_docred_lora_training\nw5_llama_docred_lora_unconstrained_eval\nw5_llama_docred_sft_data_gen\nw5_llama_lora_scierc_constrained_eval\nw5_llama_lora_scierc_training\nw5_llama_lora_scierc_unconstrained_eval\nw5_lora_scierc_constrained_eval\nw5_lora_scierc_training\nw5_lora_scierc_unconstrained_eval\nw5_qwen_docred_lora_constrained_eval\nw5_qwen_docred_lora_training\nw5_qwen_docred_lora_unconstrained_eval\nw6_mistral_docred_constrained\nw6_mistral_docred_unconstrained\nw6_mistral_scierc_constrained\nw6_mistral_scierc_unconstrained\nw7_llama_scierc_ft_grammar_only\nw7_llama_scierc_ft_semantic_only\nw7_qwen_scierc_ft_grammar_only\nw7_qwen_scierc_ft_semantic_only\nw8_ft_posthoc_baseline\nw8_llama_docred_ft_grammar_only\nw8_llama_docred_ft_semantic_only\nw8_qwen_docred_ft_grammar_only\nw8_qwen_docred_ft_semantic_only",
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01LAog8dyXT22euhQcVsUnY9`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d/tool-results/mcp-agent-ml-research-read_registry-1778949832693.txt | python3 -c \"\nimport json, sys\n\nraw = json.loads(sys.stdin.read())['result']\ndata = json.loads(raw)\nexperiments = data['data']['experiments']\n\n# Get ZS ablation data (grammar_only and semantic_only for Qwen in phase2)\nneeded = ['phase2_scierc_grammar_only', 'phase2_scierc_semantic_only', 'phase2_docred_grammar_only', 'phase2_docred_semantic_only']\nfor eid in needed:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f'=== {eid} (status: {exp.get(\\\"status\\\")}) ===')\n        m = exp.get('metrics')\n        if m:\n            print(json.dumps(m, indent=2)[:2000])\n        else:\n            print('  NO METRICS')\n    print()\n\" 2>&1",
  "description": "Get phase2 ablation experiment metrics",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "1cbf5048-0e5f-4da9-a2bc-3f2d3817a45c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RzRPPhzuaC3njfVmBFYMwn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 39624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1090
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

_source line 36 · 2026-05-16T16:45:12.416Z_

<details><summary>↩ Tool result · `toolu_01LAog8dyXT22euhQcVsUnY9`</summary>

```text
=== phase2_scierc_grammar_only (status: DONE) ===
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

=== phase2_scierc_semantic_only (status: DONE) ===
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

=== phase2_docred_grammar_only (status: DONE) ===
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

=== phase2_docred_semantic_only (status: DONE) ===
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "7e3bc979-6ed4-4747-ad7e-7633299dac88",
  "tool_use_result": {
    "stdout": "=== phase2_scierc_grammar_only (status: DONE) ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1725,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0,\n  \"domain_range_violation_rate\": 0.1484,\n  \"cross_field_consistency_violation_rate\": 0.0008,\n  \"entity_f1\": 0.3098,\n  \"entity_precision\": 0.2598,\n  \"entity_recall\": 0.3837,\n  \"relation_f1\": 0.0823,\n  \"relation_precision\": 0.0643,\n  \"relation_recall\": 0.114,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_scierc_semantic_only (status: DONE) ===\n{\n  \"total_samples\": 551,\n  \"total_triples\": 1726,\n  \"total_entities\": 2474,\n  \"json_parse_rate\": 1,\n  \"entity_type_violation_rate\": 0.004,\n  \"relation_vocabulary_violation_rate\": 0.0151,\n  \"domain_range_violation_rate\": 0.1165,\n  \"cross_field_consistency_violation_rate\": 0.0271,\n  \"entity_f1\": 0.3101,\n  \"entity_precision\": 0.2605,\n  \"entity_recall\": 0.3831,\n  \"relation_f1\": 0.0815,\n  \"relation_precision\": 0.0637,\n  \"relation_recall\": 0.1129,\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_docred_grammar_only (status: DONE) ===\n{\n  \"documents_checked\": 985,\n  \"parse_failures\": 13,\n  \"total_entities\": 20150,\n  \"total_triples\": 17341,\n  \"entity_type_violation_rate\": 0,\n  \"relation_vocabulary_violation_rate\": 0.0003,\n  \"domain_range_violation_rate\": 0.2617,\n  \"cross_field_consistency_violation_rate\": 0.0007,\n  \"relation_f1\": 8.31,\n  \"relation_precision\": 7.06,\n  \"relation_recall\": 10.12,\n  \"entity_f1\": 59.38,\n  \"entity_precision\": 58.47,\n  \"entity_recall\": 60.32,\n  \"unrecognized_relations\": 5,\n  \"f1_method\": \"all_set\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n\n=== phase2_docred_semantic_only (status: DONE) ===\n{\n  \"documents_checked\": 987,\n  \"parse_failures\": 11,\n  \"total_entities\": 20185,\n  \"total_triples\": 17571,\n  \"entity_type_violation_rate\": 0.0422,\n  \"relation_vocabulary_violation_rate\": 0.2987,\n  \"domain_range_violation_rate\": 0.1384,\n  \"cross_field_consistency_violation_rate\": 0.0105,\n  \"entity_f1\": 57.81,\n  \"entity_precision\": 57.27,\n  \"entity_recall\": 58.37,\n  \"relation_f1\": 7.7,\n  \"relation_precision\": 6.54,\n  \"relation_recall\": 9.37,\n  \"f1_method\": \"all_set\",\n  \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\",\n  \"et_v1\": 0.1044,\n  \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"\n}",
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

_source line 37_

I now have all the data needed. Let me also check if there's latency data in the project artifacts directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d3b99823-999d-4055-90cb-b4169352727f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQPgez8MkKAUwRCaAAGkd2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 40714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1479
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

_source line 38_

<details open><summary>🔧 Tool call — Glob · `toolu_013Z3hZ3vpWdkWQU1eMZiXz1`</summary>

```json
{
  "pattern": "**/*latency*",
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "74aadbd2-6c53-4770-8709-513da11f81e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQPgez8MkKAUwRCaAAGkd2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1479,
      "cache_read_input_tokens": 40714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1479
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

_source line 39 · 2026-05-16T16:45:16.436Z_

<details><summary>↩ Tool result · `toolu_013Z3hZ3vpWdkWQU1eMZiXz1`</summary>

```text
artifacts/_project/report/latency_profiling_design.md
logs/workers/worker_research_latency_profiling_design_20260516T025445.log
logs/workers/worker_research_latency_profiling_design_20260516T025445_result.json
artifacts/_project/data/latency_profiling_results.md
logs/workers/worker_analysis_latency_profiling_20260516T085245.log
logs/workers/worker_analysis_latency_profiling_20260516T085245_result.json
artifacts/_project/data/latency_profiling_results_a3397b.md
logs/workers/worker_analysis_latency_profiling_docred_20260516T091743.log
logs/workers/worker_analysis_latency_profiling_docred_20260516T091743_result.json
logs/workers/worker_analysis_latency_profiling_docred_collect_20260516T101608.log
logs/workers/worker_analysis_latency_profiling_docred_collect_20260516T101608_result.json
logs/workers/worker_ops_latency_docred_collect_20260516T115_20260516T111651.log
logs/workers/worker_ops_latency_docred_collect_20260516T115_20260516T111651_result.json
logs/workers/worker_code_latency_profiling_prep_20260516_20260516T123851.log
logs/workers/worker_code_latency_profiling_prep_20260516_20260516T123851_result.json
artifacts/_project/data/latency_profiling_docred_qwen_ft.json
artifacts/latency_profiling_docred_qwen_ft.json
logs/workers/worker_ops_latency_docred_artifact_20260516_20260516T131452.log
logs/workers/worker_ops_latency_docred_artifact_20260516_20260516T131452_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "3aa6e121-5b6a-498d-97f6-72cfa2b60d58",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/latency_profiling_design.md",
      "logs/workers/worker_research_latency_profiling_design_20260516T025445.log",
      "logs/workers/worker_research_latency_profiling_design_20260516T025445_result.json",
      "artifacts/_project/data/latency_profiling_results.md",
      "logs/workers/worker_analysis_latency_profiling_20260516T085245.log",
      "logs/workers/worker_analysis_latency_profiling_20260516T085245_result.json",
      "artifacts/_project/data/latency_profiling_results_a3397b.md",
      "logs/workers/worker_analysis_latency_profiling_docred_20260516T091743.log",
      "logs/workers/worker_analysis_latency_profiling_docred_20260516T091743_result.json",
      "logs/workers/worker_analysis_latency_profiling_docred_collect_20260516T101608.log",
      "logs/workers/worker_analysis_latency_profiling_docred_collect_20260516T101608_result.json",
      "logs/workers/worker_ops_latency_docred_collect_20260516T115_20260516T111651.log",
      "logs/workers/worker_ops_latency_docred_collect_20260516T115_20260516T111651_result.json",
      "logs/workers/worker_code_latency_profiling_prep_20260516_20260516T123851.log",
      "logs/workers/worker_code_latency_profiling_prep_20260516_20260516T123851_result.json",
      "artifacts/_project/data/latency_profiling_docred_qwen_ft.json",
      "artifacts/latency_profiling_docred_qwen_ft.json",
      "logs/workers/worker_ops_latency_docred_artifact_20260516_20260516T131452.log",
      "logs/workers/worker_ops_latency_docred_artifact_20260516_20260516T131452_result.json"
    ],
    "durationMs": 15,
    "numFiles": 19,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_011GCNXeapTxtPExSsUaSRdF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d6fc3690-ac34-47e8-b194-fcfc601ec0c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Kq9LxZMWc9TiJHwecc2C3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 42193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
      },
      "output_tokens": 59,
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

_source line 41 · 2026-05-16T16:45:21.906Z_

<details><summary>↩ Tool result · `toolu_011GCNXeapTxtPExSsUaSRdF`</summary>

```text
1	# Latency Profiling Results — OntoCoDec Constrained Decoding
2	
3	## Setup
4	- Model: Qwen3-8B-LoRA-SciERC merged checkpoint
5	- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB)
6	- Dataset: SciERC test set, 100 samples
7	- Controlled benchmark: model loaded once, 5-sample warmup, all modes run sequentially in same process
8	- Timing: `torch.cuda.synchronize()` + `time.perf_counter()` for accurate measurement
9	
10	## Results
11	
12	| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
13	|------|---|----------|---------|---------|---------|----------|-------|
14	| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |
15	| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |
16	| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |
17	| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | +2.3% | 56.4 |
18	
19	## Statistical Significance (paired t-test)
20	- unconstrained vs grammar_only: +0.044s (+1.7%), t=-10.34, p<0.0001
21	- unconstrained vs semantic_only: +0.032s (+1.2%), t=-11.04, p<0.0001
22	- unconstrained vs full_s1: +0.061s (+2.3%), t=-12.84, p<0.0001
23	
24	## Conclusion
25	Constrained decoding (full_s1 = grammar + semantic) adds **2.3% latency overhead** (61ms per sample on average). This is statistically significant but practically negligible. The grammar layer contributes most of the overhead (+1.7%), while the semantic layer adds only +1.2%. The combined overhead is sub-additive.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "7222a45b-dab1-477c-af9f-423d21be0d0b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_results.md",
      "content": "# Latency Profiling Results — OntoCoDec Constrained Decoding\n\n## Setup\n- Model: Qwen3-8B-LoRA-SciERC merged checkpoint\n- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB)\n- Dataset: SciERC test set, 100 samples\n- Controlled benchmark: model loaded once, 5-sample warmup, all modes run sequentially in same process\n- Timing: `torch.cuda.synchronize()` + `time.perf_counter()` for accurate measurement\n\n## Results\n\n| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |\n|------|---|----------|---------|---------|---------|----------|-------|\n| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |\n| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |\n| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |\n| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | +2.3% | 56.4 |\n\n## Statistical Significance (paired t-test)\n- unconstrained vs grammar_only: +0.044s (+1.7%), t=-10.34, p<0.0001\n- unconstrained vs semantic_only: +0.032s (+1.2%), t=-11.04, p<0.0001\n- unconstrained vs full_s1: +0.061s (+2.3%), t=-12.84, p<0.0001\n\n## Conclusion\nConstrained decoding (full_s1 = grammar + semantic) adds **2.3% latency overhead** (61ms per sample on average). This is statistically significant but practically negligible. The grammar layer contributes most of the overhead (+1.7%), while the semantic layer adds only +1.2%. The combined overhead is sub-additive.",
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01NK3gh2DC5gCkBVh3DtgwHs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/latency_profiling_docred_qwen_ft.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "91ff5219-2c75-41a5-b66b-50affde6317e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Kq9LxZMWc9TiJHwecc2C3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 42193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 730
      },
      "output_tokens": 59,
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

_source line 43 · 2026-05-16T16:45:22.422Z_

<details><summary>↩ Tool result · `toolu_01NK3gh2DC5gCkBVh3DtgwHs`</summary>

```text
1	{"grammar_compile_time": 0.043980566784739494, "unconstrained": {"times": [6.378096409142017, 12.904806893318892, 12.038921477273107, 20.268284460529685, 18.261225011199713, 32.78748765774071, 6.6753224208951, 23.577983113005757, 12.647348260506988, 14.435973633080721, 17.422500532120466, 18.18054690770805, 72.72121825441718, 8.055085074156523, 6.742973720654845, 31.48678945377469, 11.92347394861281, 72.7191240247339, 8.317223040387034, 18.78659504838288, 13.236967470496893, 33.63627894409001, 12.264321690425277, 12.51094469241798, 11.974207453429699, 21.431482255458832, 16.122038243338466, 10.940281864255667, 18.323722757399082, 8.355710972100496, 12.459809174761176, 16.61060857027769, 10.730936542153358, 14.043768879026175, 11.662266351282597, 10.728713903576136, 14.785508761182427, 18.943670831620693, 20.973368981853127, 3.371563460677862, 25.283405479043722, 20.6139914393425, 18.444203294813633, 44.85546909272671, 20.306889720261097, 18.144997648894787, 11.943682163953781, 7.155207136645913, 72.81720060296357, 19.50239374488592, 72.8808942772448, 13.850553181022406, 10.951422473415732, 14.08792595565319, 4.252429563552141, 17.4735092446208, 17.265274837613106, 33.99098568968475, 11.99583176523447, 26.998445607721806, 13.726001128554344, 15.647896165028214, 10.087503287941217, 16.891286307945848, 72.90231449715793, 19.079480711370707, 12.463391352444887, 73.3226670101285, 10.480010189116001, 18.468988155946136, 14.5319181997329, 15.528578028082848, 10.314775466918945, 73.59450464323163, 10.162157284095883, 12.7672466840595, 17.69708831049502, 17.937755431979895, 5.854288887232542, 73.40676330961287, 22.75332636386156, 8.927011910825968, 9.397222489118576, 33.85761443339288, 17.50231445580721, 18.90733857639134, 10.811178363859653, 21.79335847683251, 20.30550347082317, 21.03588560409844, 12.75754551589489, 25.19940305687487, 73.52147417515516, 10.887708401307464, 16.02421820536256, 12.47815710119903, 8.181803610175848, 14.464557247236371, 13.190638536587358, 13.182953821495175], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, "grammar_only": {"times": [6.9067496713250875, 13.261112984269857, 12.38665908575058, 20.87978365458548, 18.809831775724888, 33.768135687336326, 6.9042498003691435, 24.171144403517246, 13.015999279916286, 14.866080615669489, 18.01167885772884, 18.6995714250952, 74.66114605218172, 8.33304668404162, 6.9238660875707865, 32.386137798428535, 12.330656679347157, 74.3463108856231, 8.454486157745123, 19.835152650251985, 13.476182306185365, 34.263004176318645, 12.471885334700346, 12.723816562443972, 12.192164283245802, 21.815198013558984, 16.479781894013286, 11.148407194763422, 18.676691757515073, 8.47034278512001, 12.640493912622333, 16.98038451373577, 10.937077322974801, 14.317156048491597, 11.85463068075478, 10.91880226507783, 15.007725263014436, 19.33370135910809, 21.35784388333559, 3.421520000323653, 25.763957668095827, 21.10869081877172, 18.79173948056996, 45.630442848429084, 20.6815717369318, 18.450985699892044, 12.159474946558475, 7.256907857954502, 74.00583234243095, 19.849388629198074, 73.99573196843266, 14.049899296835065, 11.123929714784026, 14.329884564504027, 4.313716659322381, 17.745513210073113, 17.568181099370122, 34.5634214989841, 12.20412739366293, 27.513226369395852, 13.956474296748638, 15.9427545722574, 10.276996336877346, 17.205487055703998, 74.16082355752587, 19.433637829497457, 12.68960564211011, 74.08832980878651, 10.508835721760988, 18.59306325763464, 14.62512857094407, 15.643814334645867, 10.35752797499299, 74.17673393711448, 10.242604030296206, 12.899762954562902, 17.758652295917273, 18.059025786817074, 5.900256847962737, 74.03023993037641, 22.880664939060807, 8.982339071109891, 9.431443151086569, 34.187987891957164, 17.602290147915483, 18.9921967536211, 10.844821659848094, 21.883535688742995, 20.355838876217604, 21.140886306762695, 12.806551847606897, 25.32606054469943, 74.09502206370234, 10.967791611328721, 16.112454429268837, 12.501909343525767, 8.276074010878801, 14.578521655872464, 13.258567409589887, 13.267627440392971], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, "semantic_only": {"times": [6.4973948914557695, 13.15538077801466, 12.262474374845624, 20.759295407682657, 18.67730657570064, 33.648419791832566, 6.834786290302873, 24.045977694913745, 12.907351827248931, 14.722907124087214, 17.848377557471395, 18.577808275818825, 75.40496411174536, 8.204625265672803, 6.855202289298177, 32.274871626868844, 12.202825244516134, 75.42076211795211, 8.45564778149128, 19.214113363996148, 13.483631679788232, 34.533383982256055, 12.493441363796592, 12.743427649140358, 12.195249687880278, 21.912337254732847, 16.490081330761313, 11.137291455641389, 18.739502623677254, 8.45222758129239, 12.64387216605246, 16.990478726103902, 10.947511771693826, 14.330795800313354, 11.89573498815298, 10.906838927417994, 15.06378891505301, 19.375672807917, 21.432399759069085, 3.414650646969676, 25.884978419169784, 21.097305668517947, 18.82377853244543, 46.173155507072806, 20.749966828152537, 18.53318877518177, 12.162978349253535, 7.262097276747227, 75.51232428103685, 19.911529906094074, 75.48407456278801, 14.115792579948902, 11.139026479795575, 14.353618049994111, 4.304832950234413, 17.83449836820364, 17.62493285536766, 34.89687390625477, 12.235018802806735, 27.670012574642897, 13.987959800288081, 15.977609757333994, 10.29501809924841, 17.229443656280637, 75.67823846451938, 19.485825836658478, 12.709894612431526, 75.5993191357702, 10.498484654352069, 18.68632059544325, 14.641429588198662, 15.676915723830462, 10.373725907877088, 75.59297457709908, 10.22821401245892, 12.897676529362798, 17.86059606820345, 18.107891896739602, 5.890507934615016, 75.51570019125938, 23.00173819437623, 8.994013167917728, 9.497016409412026, 75.53713069297373, 17.63738601654768, 19.043374076485634, 10.847014414146543, 21.973770946264267, 20.431155558675528, 21.22267721220851, 12.83528783172369, 25.482754016295075, 75.64998476393521, 10.99561190418899, 16.177440160885453, 12.536373373121023, 8.267774553969502, 14.661314593628049, 13.315743800252676, 13.285708088427782], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, "full_s1": {"times": [6.557272005826235, 13.30385784804821, 12.393721845000982, 20.966787956655025, 18.84646543301642, 33.97123330272734, 6.879897966980934, 24.29985479451716, 12.998356265947223, 14.869501804932952, 17.984158493578434, 18.849919013679028, 76.2875934690237, 8.307313518598676, 6.929178504273295, 32.65210123360157, 12.316430946812034, 76.31797208078206, 8.589986260980368, 20.151168631389737, 13.631159098818898, 34.93915410526097, 12.632728463038802, 12.893065474927425, 12.354045446962118, 22.13497686944902, 16.693173775449395, 11.252564314752817, 18.948786783963442, 8.573606921359897, 12.790846752002835, 17.154880825430155, 11.101712444797158, 14.49220641888678, 12.012543451040983, 11.042622407898307, 15.202911971136928, 19.616007763892412, 21.66821843571961, 3.44002472050488, 26.173067569732666, 21.322467194870114, 19.05821535922587, 46.6952401753515, 20.961115062236786, 18.70112570747733, 12.290571074932814, 7.339368067681789, 76.24014202132821, 20.168137699365616, 76.25835328362882, 14.27820573747158, 11.254785351455212, 14.514818558469415, 4.3554796781390905, 18.05753686092794, 17.810633156448603, 35.22906826809049, 12.342857629060745, 27.953737488016486, 14.126854510977864, 16.15063438564539, 10.39058312959969, 17.40311536937952, 76.41485323384404, 19.67245303094387, 12.843625912442803, 76.37891258485615, 10.617164023220539, 18.871050599962473, 14.784893812611699, 15.83510966040194, 10.478933291509748, 76.39716600626707, 10.322485107928514, 13.050531685352325, 18.021803356707096, 18.26944730989635, 5.92651423625648, 76.69698422215879, 23.187818862497807, 9.064455602318048, 9.551359128206968, 76.14131500199437, 17.780814606696367, 19.20519828237593, 10.946219146251678, 22.183561097830534, 20.623430989682674, 21.442427676171064, 12.946139235049486, 25.714026479050517, 76.25824106112123, 11.080481877550483, 16.318021584302187, 12.635702196508646, 8.318728053942323, 14.814586939290166, 13.413050413131714, 13.398678639903665], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "02ca0b47-7b7a-4692-9b24-c29eef0efae6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/latency_profiling_docred_qwen_ft.json",
      "content": "{\"grammar_compile_time\": 0.043980566784739494, \"unconstrained\": {\"times\": [6.378096409142017, 12.904806893318892, 12.038921477273107, 20.268284460529685, 18.261225011199713, 32.78748765774071, 6.6753224208951, 23.577983113005757, 12.647348260506988, 14.435973633080721, 17.422500532120466, 18.18054690770805, 72.72121825441718, 8.055085074156523, 6.742973720654845, 31.48678945377469, 11.92347394861281, 72.7191240247339, 8.317223040387034, 18.78659504838288, 13.236967470496893, 33.63627894409001, 12.264321690425277, 12.51094469241798, 11.974207453429699, 21.431482255458832, 16.122038243338466, 10.940281864255667, 18.323722757399082, 8.355710972100496, 12.459809174761176, 16.61060857027769, 10.730936542153358, 14.043768879026175, 11.662266351282597, 10.728713903576136, 14.785508761182427, 18.943670831620693, 20.973368981853127, 3.371563460677862, 25.283405479043722, 20.6139914393425, 18.444203294813633, 44.85546909272671, 20.306889720261097, 18.144997648894787, 11.943682163953781, 7.155207136645913, 72.81720060296357, 19.50239374488592, 72.8808942772448, 13.850553181022406, 10.951422473415732, 14.08792595565319, 4.252429563552141, 17.4735092446208, 17.265274837613106, 33.99098568968475, 11.99583176523447, 26.998445607721806, 13.726001128554344, 15.647896165028214, 10.087503287941217, 16.891286307945848, 72.90231449715793, 19.079480711370707, 12.463391352444887, 73.3226670101285, 10.480010189116001, 18.468988155946136, 14.5319181997329, 15.528578028082848, 10.314775466918945, 73.59450464323163, 10.162157284095883, 12.7672466840595, 17.69708831049502, 17.937755431979895, 5.854288887232542, 73.40676330961287, 22.75332636386156, 8.927011910825968, 9.397222489118576, 33.85761443339288, 17.50231445580721, 18.90733857639134, 10.811178363859653, 21.79335847683251, 20.30550347082317, 21.03588560409844, 12.75754551589489, 25.19940305687487, 73.52147417515516, 10.887708401307464, 16.02421820536256, 12.47815710119903, 8.181803610175848, 14.464557247236371, 13.190638536587358, 13.182953821495175], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, \"grammar_only\": {\"times\": [6.9067496713250875, 13.261112984269857, 12.38665908575058, 20.87978365458548, 18.809831775724888, 33.768135687336326, 6.9042498003691435, 24.171144403517246, 13.015999279916286, 14.866080615669489, 18.01167885772884, 18.6995714250952, 74.66114605218172, 8.33304668404162, 6.9238660875707865, 32.386137798428535, 12.330656679347157, 74.3463108856231, 8.454486157745123, 19.835152650251985, 13.476182306185365, 34.263004176318645, 12.471885334700346, 12.723816562443972, 12.192164283245802, 21.815198013558984, 16.479781894013286, 11.148407194763422, 18.676691757515073, 8.47034278512001, 12.640493912622333, 16.98038451373577, 10.937077322974801, 14.317156048491597, 11.85463068075478, 10.91880226507783, 15.007725263014436, 19.33370135910809, 21.35784388333559, 3.421520000323653, 25.763957668095827, 21.10869081877172, 18.79173948056996, 45.630442848429084, 20.6815717369318, 18.450985699892044, 12.159474946558475, 7.256907857954502, 74.00583234243095, 19.849388629198074, 73.99573196843266, 14.049899296835065, 11.123929714784026, 14.329884564504027, 4.313716659322381, 17.745513210073113, 17.568181099370122, 34.5634214989841, 12.20412739366293, 27.513226369395852, 13.956474296748638, 15.9427545722574, 10.276996336877346, 17.205487055703998, 74.16082355752587, 19.433637829497457, 12.68960564211011, 74.08832980878651, 10.508835721760988, 18.59306325763464, 14.62512857094407, 15.643814334645867, 10.35752797499299, 74.17673393711448, 10.242604030296206, 12.899762954562902, 17.758652295917273, 18.059025786817074, 5.900256847962737, 74.03023993037641, 22.880664939060807, 8.982339071109891, 9.431443151086569, 34.187987891957164, 17.602290147915483, 18.9921967536211, 10.844821659848094, 21.883535688742995, 20.355838876217604, 21.140886306762695, 12.806551847606897, 25.32606054469943, 74.09502206370234, 10.967791611328721, 16.112454429268837, 12.501909343525767, 8.276074010878801, 14.578521655872464, 13.258567409589887, 13.267627440392971], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, \"semantic_only\": {\"times\": [6.4973948914557695, 13.15538077801466, 12.262474374845624, 20.759295407682657, 18.67730657570064, 33.648419791832566, 6.834786290302873, 24.045977694913745, 12.907351827248931, 14.722907124087214, 17.848377557471395, 18.577808275818825, 75.40496411174536, 8.204625265672803, 6.855202289298177, 32.274871626868844, 12.202825244516134, 75.42076211795211, 8.45564778149128, 19.214113363996148, 13.483631679788232, 34.533383982256055, 12.493441363796592, 12.743427649140358, 12.195249687880278, 21.912337254732847, 16.490081330761313, 11.137291455641389, 18.739502623677254, 8.45222758129239, 12.64387216605246, 16.990478726103902, 10.947511771693826, 14.330795800313354, 11.89573498815298, 10.906838927417994, 15.06378891505301, 19.375672807917, 21.432399759069085, 3.414650646969676, 25.884978419169784, 21.097305668517947, 18.82377853244543, 46.173155507072806, 20.749966828152537, 18.53318877518177, 12.162978349253535, 7.262097276747227, 75.51232428103685, 19.911529906094074, 75.48407456278801, 14.115792579948902, 11.139026479795575, 14.353618049994111, 4.304832950234413, 17.83449836820364, 17.62493285536766, 34.89687390625477, 12.235018802806735, 27.670012574642897, 13.987959800288081, 15.977609757333994, 10.29501809924841, 17.229443656280637, 75.67823846451938, 19.485825836658478, 12.709894612431526, 75.5993191357702, 10.498484654352069, 18.68632059544325, 14.641429588198662, 15.676915723830462, 10.373725907877088, 75.59297457709908, 10.22821401245892, 12.897676529362798, 17.86059606820345, 18.107891896739602, 5.890507934615016, 75.51570019125938, 23.00173819437623, 8.994013167917728, 9.497016409412026, 75.53713069297373, 17.63738601654768, 19.043374076485634, 10.847014414146543, 21.973770946264267, 20.431155558675528, 21.22267721220851, 12.83528783172369, 25.482754016295075, 75.64998476393521, 10.99561190418899, 16.177440160885453, 12.536373373121023, 8.267774553969502, 14.661314593628049, 13.315743800252676, 13.285708088427782], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, \"full_s1\": {\"times\": [6.557272005826235, 13.30385784804821, 12.393721845000982, 20.966787956655025, 18.84646543301642, 33.97123330272734, 6.879897966980934, 24.29985479451716, 12.998356265947223, 14.869501804932952, 17.984158493578434, 18.849919013679028, 76.2875934690237, 8.307313518598676, 6.929178504273295, 32.65210123360157, 12.316430946812034, 76.31797208078206, 8.589986260980368, 20.151168631389737, 13.631159098818898, 34.93915410526097, 12.632728463038802, 12.893065474927425, 12.354045446962118, 22.13497686944902, 16.693173775449395, 11.252564314752817, 18.948786783963442, 8.573606921359897, 12.790846752002835, 17.154880825430155, 11.101712444797158, 14.49220641888678, 12.012543451040983, 11.042622407898307, 15.202911971136928, 19.616007763892412, 21.66821843571961, 3.44002472050488, 26.173067569732666, 21.322467194870114, 19.05821535922587, 46.6952401753515, 20.961115062236786, 18.70112570747733, 12.290571074932814, 7.339368067681789, 76.24014202132821, 20.168137699365616, 76.25835328362882, 14.27820573747158, 11.254785351455212, 14.514818558469415, 4.3554796781390905, 18.05753686092794, 17.810633156448603, 35.22906826809049, 12.342857629060745, 27.953737488016486, 14.126854510977864, 16.15063438564539, 10.39058312959969, 17.40311536937952, 76.41485323384404, 19.67245303094387, 12.843625912442803, 76.37891258485615, 10.617164023220539, 18.871050599962473, 14.784893812611699, 15.83510966040194, 10.478933291509748, 76.39716600626707, 10.322485107928514, 13.050531685352325, 18.021803356707096, 18.26944730989635, 5.92651423625648, 76.69698422215879, 23.187818862497807, 9.064455602318048, 9.551359128206968, 76.14131500199437, 17.780814606696367, 19.20519828237593, 10.946219146251678, 22.183561097830534, 20.623430989682674, 21.442427676171064, 12.946139235049486, 25.714026479050517, 76.25824106112123, 11.080481877550483, 16.318021584302187, 12.635702196508646, 8.318728053942323, 14.814586939290166, 13.413050413131714, 13.398678639903665], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}}",
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_018SW5KKcAyhwpcyD2pPiY4o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_results_a3397b.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "7d97786d-2f53-41c7-916f-4c376540ff1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LViPWGUojkFjKb9Lkg8TkS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5904,
      "cache_read_input_tokens": 42923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5904
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

_source line 45 · 2026-05-16T16:45:27.565Z_

<details><summary>↩ Tool result · `toolu_018SW5KKcAyhwpcyD2pPiY4o`</summary>

```text
1	## Latency Profiling Results
2	
3	Controlled benchmark: 100 SciERC samples, Qwen3-8B FT checkpoint, single GPU (westd-16980 cuda:0, RTX PRO 6000), CUDA sync precise timing.
4	
5	| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
6	|------|---|----------|---------|---------|---------|----------|-------|
7	| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |
8	| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |
9	| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |
10	| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | +2.3% | 56.4 |
11	
12	All differences statistically significant (p < 0.0001, paired t-test).
13	
14	Key findings:
15	- Full constrained decoding (grammar + semantic) adds only 2.3% latency overhead (61ms/sample)
16	- Each constraint layer independently contributes ~1-2%
17	- Combined overhead is sub-additive (1.7% + 1.2% → 2.3%, not 2.9%)
18	- Practically negligible for production use
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "ab5cc740-8860-4fb0-a148-a61f6149a7e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_results_a3397b.md",
      "content": "## Latency Profiling Results\n\nControlled benchmark: 100 SciERC samples, Qwen3-8B FT checkpoint, single GPU (westd-16980 cuda:0, RTX PRO 6000), CUDA sync precise timing.\n\n| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |\n|------|---|----------|---------|---------|---------|----------|-------|\n| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |\n| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |\n| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |\n| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | +2.3% | 56.4 |\n\nAll differences statistically significant (p < 0.0001, paired t-test).\n\nKey findings:\n- Full constrained decoding (grammar + semantic) adds only 2.3% latency overhead (61ms/sample)\n- Each constraint layer independently contributes ~1-2%\n- Combined overhead is sub-additive (1.7% + 1.2% → 2.3%, not 2.9%)\n- Practically negligible for production use\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

Now let me check the DocRED latency data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "5d93b03f-c337-4bbf-888b-96610bd303d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PopVz41LiTFnzEDkSfqdZE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 562,
      "cache_read_input_tokens": 48827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 562
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01UHZ2kjdRAxvYYK16YDda5S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_docred_qwen_ft.json",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "90918421-da3b-4528-ab61-34936eb4e880",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PopVz41LiTFnzEDkSfqdZE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 562,
      "cache_read_input_tokens": 48827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 562
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

_source line 48 · 2026-05-16T16:45:32.417Z_

<details><summary>↩ Tool result · `toolu_01UHZ2kjdRAxvYYK16YDda5S`</summary>

```text
1	{"grammar_compile_time": 0.043980566784739494, "unconstrained": {"times": [6.378096409142017, 12.904806893318892, 12.038921477273107, 20.268284460529685, 18.261225011199713, 32.78748765774071, 6.6753224208951, 23.577983113005757, 12.647348260506988, 14.435973633080721, 17.422500532120466, 18.18054690770805, 72.72121825441718, 8.055085074156523, 6.742973720654845, 31.48678945377469, 11.92347394861281, 72.7191240247339, 8.317223040387034, 18.78659504838288, 13.236967470496893, 33.63627894409001, 12.264321690425277, 12.51094469241798, 11.974207453429699, 21.431482255458832, 16.122038243338466, 10.940281864255667, 18.323722757399082, 8.355710972100496, 12.459809174761176, 16.61060857027769, 10.730936542153358, 14.043768879026175, 11.662266351282597, 10.728713903576136, 14.785508761182427, 18.943670831620693, 20.973368981853127, 3.371563460677862, 25.283405479043722, 20.6139914393425, 18.444203294813633, 44.85546909272671, 20.306889720261097, 18.144997648894787, 11.943682163953781, 7.155207136645913, 72.81720060296357, 19.50239374488592, 72.8808942772448, 13.850553181022406, 10.951422473415732, 14.08792595565319, 4.252429563552141, 17.4735092446208, 17.265274837613106, 33.99098568968475, 11.99583176523447, 26.998445607721806, 13.726001128554344, 15.647896165028214, 10.087503287941217, 16.891286307945848, 72.90231449715793, 19.079480711370707, 12.463391352444887, 73.3226670101285, 10.480010189116001, 18.468988155946136, 14.5319181997329, 15.528578028082848, 10.314775466918945, 73.59450464323163, 10.162157284095883, 12.7672466840595, 17.69708831049502, 17.937755431979895, 5.854288887232542, 73.40676330961287, 22.75332636386156, 8.927011910825968, 9.397222489118576, 33.85761443339288, 17.50231445580721, 18.90733857639134, 10.811178363859653, 21.79335847683251, 20.30550347082317, 21.03588560409844, 12.75754551589489, 25.19940305687487, 73.52147417515516, 10.887708401307464, 16.02421820536256, 12.47815710119903, 8.181803610175848, 14.464557247236371, 13.190638536587358, 13.182953821495175], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, "grammar_only": {"times": [6.9067496713250875, 13.261112984269857, 12.38665908575058, 20.87978365458548, 18.809831775724888, 33.768135687336326, 6.9042498003691435, 24.171144403517246, 13.015999279916286, 14.866080615669489, 18.01167885772884, 18.6995714250952, 74.66114605218172, 8.33304668404162, 6.9238660875707865, 32.386137798428535, 12.330656679347157, 74.3463108856231, 8.454486157745123, 19.835152650251985, 13.476182306185365, 34.263004176318645, 12.471885334700346, 12.723816562443972, 12.192164283245802, 21.815198013558984, 16.479781894013286, 11.148407194763422, 18.676691757515073, 8.47034278512001, 12.640493912622333, 16.98038451373577, 10.937077322974801, 14.317156048491597, 11.85463068075478, 10.91880226507783, 15.007725263014436, 19.33370135910809, 21.35784388333559, 3.421520000323653, 25.763957668095827, 21.10869081877172, 18.79173948056996, 45.630442848429084, 20.6815717369318, 18.450985699892044, 12.159474946558475, 7.256907857954502, 74.00583234243095, 19.849388629198074, 73.99573196843266, 14.049899296835065, 11.123929714784026, 14.329884564504027, 4.313716659322381, 17.745513210073113, 17.568181099370122, 34.5634214989841, 12.20412739366293, 27.513226369395852, 13.956474296748638, 15.9427545722574, 10.276996336877346, 17.205487055703998, 74.16082355752587, 19.433637829497457, 12.68960564211011, 74.08832980878651, 10.508835721760988, 18.59306325763464, 14.62512857094407, 15.643814334645867, 10.35752797499299, 74.17673393711448, 10.242604030296206, 12.899762954562902, 17.758652295917273, 18.059025786817074, 5.900256847962737, 74.03023993037641, 22.880664939060807, 8.982339071109891, 9.431443151086569, 34.187987891957164, 17.602290147915483, 18.9921967536211, 10.844821659848094, 21.883535688742995, 20.355838876217604, 21.140886306762695, 12.806551847606897, 25.32606054469943, 74.09502206370234, 10.967791611328721, 16.112454429268837, 12.501909343525767, 8.276074010878801, 14.578521655872464, 13.258567409589887, 13.267627440392971], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, "semantic_only": {"times": [6.4973948914557695, 13.15538077801466, 12.262474374845624, 20.759295407682657, 18.67730657570064, 33.648419791832566, 6.834786290302873, 24.045977694913745, 12.907351827248931, 14.722907124087214, 17.848377557471395, 18.577808275818825, 75.40496411174536, 8.204625265672803, 6.855202289298177, 32.274871626868844, 12.202825244516134, 75.42076211795211, 8.45564778149128, 19.214113363996148, 13.483631679788232, 34.533383982256055, 12.493441363796592, 12.743427649140358, 12.195249687880278, 21.912337254732847, 16.490081330761313, 11.137291455641389, 18.739502623677254, 8.45222758129239, 12.64387216605246, 16.990478726103902, 10.947511771693826, 14.330795800313354, 11.89573498815298, 10.906838927417994, 15.06378891505301, 19.375672807917, 21.432399759069085, 3.414650646969676, 25.884978419169784, 21.097305668517947, 18.82377853244543, 46.173155507072806, 20.749966828152537, 18.53318877518177, 12.162978349253535, 7.262097276747227, 75.51232428103685, 19.911529906094074, 75.48407456278801, 14.115792579948902, 11.139026479795575, 14.353618049994111, 4.304832950234413, 17.83449836820364, 17.62493285536766, 34.89687390625477, 12.235018802806735, 27.670012574642897, 13.987959800288081, 15.977609757333994, 10.29501809924841, 17.229443656280637, 75.67823846451938, 19.485825836658478, 12.709894612431526, 75.5993191357702, 10.498484654352069, 18.68632059544325, 14.641429588198662, 15.676915723830462, 10.373725907877088, 75.59297457709908, 10.22821401245892, 12.897676529362798, 17.86059606820345, 18.107891896739602, 5.890507934615016, 75.51570019125938, 23.00173819437623, 8.994013167917728, 9.497016409412026, 75.53713069297373, 17.63738601654768, 19.043374076485634, 10.847014414146543, 21.973770946264267, 20.431155558675528, 21.22267721220851, 12.83528783172369, 25.482754016295075, 75.64998476393521, 10.99561190418899, 16.177440160885453, 12.536373373121023, 8.267774553969502, 14.661314593628049, 13.315743800252676, 13.285708088427782], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, "full_s1": {"times": [6.557272005826235, 13.30385784804821, 12.393721845000982, 20.966787956655025, 18.84646543301642, 33.97123330272734, 6.879897966980934, 24.29985479451716, 12.998356265947223, 14.869501804932952, 17.984158493578434, 18.849919013679028, 76.2875934690237, 8.307313518598676, 6.929178504273295, 32.65210123360157, 12.316430946812034, 76.31797208078206, 8.589986260980368, 20.151168631389737, 13.631159098818898, 34.93915410526097, 12.632728463038802, 12.893065474927425, 12.354045446962118, 22.13497686944902, 16.693173775449395, 11.252564314752817, 18.948786783963442, 8.573606921359897, 12.790846752002835, 17.154880825430155, 11.101712444797158, 14.49220641888678, 12.012543451040983, 11.042622407898307, 15.202911971136928, 19.616007763892412, 21.66821843571961, 3.44002472050488, 26.173067569732666, 21.322467194870114, 19.05821535922587, 46.6952401753515, 20.961115062236786, 18.70112570747733, 12.290571074932814, 7.339368067681789, 76.24014202132821, 20.168137699365616, 76.25835328362882, 14.27820573747158, 11.254785351455212, 14.514818558469415, 4.3554796781390905, 18.05753686092794, 17.810633156448603, 35.22906826809049, 12.342857629060745, 27.953737488016486, 14.126854510977864, 16.15063438564539, 10.39058312959969, 17.40311536937952, 76.41485323384404, 19.67245303094387, 12.843625912442803, 76.37891258485615, 10.617164023220539, 18.871050599962473, 14.784893812611699, 15.83510966040194, 10.478933291509748, 76.39716600626707, 10.322485107928514, 13.050531685352325, 18.021803356707096, 18.26944730989635, 5.92651423625648, 76.69698422215879, 23.187818862497807, 9.064455602318048, 9.551359128206968, 76.14131500199437, 17.780814606696367, 19.20519828237593, 10.946219146251678, 22.183561097830534, 20.623430989682674, 21.442427676171064, 12.946139235049486, 25.714026479050517, 76.25824106112123, 11.080481877550483, 16.318021584302187, 12.635702196508646, 8.318728053942323, 14.814586939290166, 13.413050413131714, 13.398678639903665], "tokens": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "3a598daf-9a90-4230-8213-66f2f5f48769",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_docred_qwen_ft.json",
      "content": "{\"grammar_compile_time\": 0.043980566784739494, \"unconstrained\": {\"times\": [6.378096409142017, 12.904806893318892, 12.038921477273107, 20.268284460529685, 18.261225011199713, 32.78748765774071, 6.6753224208951, 23.577983113005757, 12.647348260506988, 14.435973633080721, 17.422500532120466, 18.18054690770805, 72.72121825441718, 8.055085074156523, 6.742973720654845, 31.48678945377469, 11.92347394861281, 72.7191240247339, 8.317223040387034, 18.78659504838288, 13.236967470496893, 33.63627894409001, 12.264321690425277, 12.51094469241798, 11.974207453429699, 21.431482255458832, 16.122038243338466, 10.940281864255667, 18.323722757399082, 8.355710972100496, 12.459809174761176, 16.61060857027769, 10.730936542153358, 14.043768879026175, 11.662266351282597, 10.728713903576136, 14.785508761182427, 18.943670831620693, 20.973368981853127, 3.371563460677862, 25.283405479043722, 20.6139914393425, 18.444203294813633, 44.85546909272671, 20.306889720261097, 18.144997648894787, 11.943682163953781, 7.155207136645913, 72.81720060296357, 19.50239374488592, 72.8808942772448, 13.850553181022406, 10.951422473415732, 14.08792595565319, 4.252429563552141, 17.4735092446208, 17.265274837613106, 33.99098568968475, 11.99583176523447, 26.998445607721806, 13.726001128554344, 15.647896165028214, 10.087503287941217, 16.891286307945848, 72.90231449715793, 19.079480711370707, 12.463391352444887, 73.3226670101285, 10.480010189116001, 18.468988155946136, 14.5319181997329, 15.528578028082848, 10.314775466918945, 73.59450464323163, 10.162157284095883, 12.7672466840595, 17.69708831049502, 17.937755431979895, 5.854288887232542, 73.40676330961287, 22.75332636386156, 8.927011910825968, 9.397222489118576, 33.85761443339288, 17.50231445580721, 18.90733857639134, 10.811178363859653, 21.79335847683251, 20.30550347082317, 21.03588560409844, 12.75754551589489, 25.19940305687487, 73.52147417515516, 10.887708401307464, 16.02421820536256, 12.47815710119903, 8.181803610175848, 14.464557247236371, 13.190638536587358, 13.182953821495175], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, \"grammar_only\": {\"times\": [6.9067496713250875, 13.261112984269857, 12.38665908575058, 20.87978365458548, 18.809831775724888, 33.768135687336326, 6.9042498003691435, 24.171144403517246, 13.015999279916286, 14.866080615669489, 18.01167885772884, 18.6995714250952, 74.66114605218172, 8.33304668404162, 6.9238660875707865, 32.386137798428535, 12.330656679347157, 74.3463108856231, 8.454486157745123, 19.835152650251985, 13.476182306185365, 34.263004176318645, 12.471885334700346, 12.723816562443972, 12.192164283245802, 21.815198013558984, 16.479781894013286, 11.148407194763422, 18.676691757515073, 8.47034278512001, 12.640493912622333, 16.98038451373577, 10.937077322974801, 14.317156048491597, 11.85463068075478, 10.91880226507783, 15.007725263014436, 19.33370135910809, 21.35784388333559, 3.421520000323653, 25.763957668095827, 21.10869081877172, 18.79173948056996, 45.630442848429084, 20.6815717369318, 18.450985699892044, 12.159474946558475, 7.256907857954502, 74.00583234243095, 19.849388629198074, 73.99573196843266, 14.049899296835065, 11.123929714784026, 14.329884564504027, 4.313716659322381, 17.745513210073113, 17.568181099370122, 34.5634214989841, 12.20412739366293, 27.513226369395852, 13.956474296748638, 15.9427545722574, 10.276996336877346, 17.205487055703998, 74.16082355752587, 19.433637829497457, 12.68960564211011, 74.08832980878651, 10.508835721760988, 18.59306325763464, 14.62512857094407, 15.643814334645867, 10.35752797499299, 74.17673393711448, 10.242604030296206, 12.899762954562902, 17.758652295917273, 18.059025786817074, 5.900256847962737, 74.03023993037641, 22.880664939060807, 8.982339071109891, 9.431443151086569, 34.187987891957164, 17.602290147915483, 18.9921967536211, 10.844821659848094, 21.883535688742995, 20.355838876217604, 21.140886306762695, 12.806551847606897, 25.32606054469943, 74.09502206370234, 10.967791611328721, 16.112454429268837, 12.501909343525767, 8.276074010878801, 14.578521655872464, 13.258567409589887, 13.267627440392971], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 1917, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, \"semantic_only\": {\"times\": [6.4973948914557695, 13.15538077801466, 12.262474374845624, 20.759295407682657, 18.67730657570064, 33.648419791832566, 6.834786290302873, 24.045977694913745, 12.907351827248931, 14.722907124087214, 17.848377557471395, 18.577808275818825, 75.40496411174536, 8.204625265672803, 6.855202289298177, 32.274871626868844, 12.202825244516134, 75.42076211795211, 8.45564778149128, 19.214113363996148, 13.483631679788232, 34.533383982256055, 12.493441363796592, 12.743427649140358, 12.195249687880278, 21.912337254732847, 16.490081330761313, 11.137291455641389, 18.739502623677254, 8.45222758129239, 12.64387216605246, 16.990478726103902, 10.947511771693826, 14.330795800313354, 11.89573498815298, 10.906838927417994, 15.06378891505301, 19.375672807917, 21.432399759069085, 3.414650646969676, 25.884978419169784, 21.097305668517947, 18.82377853244543, 46.173155507072806, 20.749966828152537, 18.53318877518177, 12.162978349253535, 7.262097276747227, 75.51232428103685, 19.911529906094074, 75.48407456278801, 14.115792579948902, 11.139026479795575, 14.353618049994111, 4.304832950234413, 17.83449836820364, 17.62493285536766, 34.89687390625477, 12.235018802806735, 27.670012574642897, 13.987959800288081, 15.977609757333994, 10.29501809924841, 17.229443656280637, 75.67823846451938, 19.485825836658478, 12.709894612431526, 75.5993191357702, 10.498484654352069, 18.68632059544325, 14.641429588198662, 15.676915723830462, 10.373725907877088, 75.59297457709908, 10.22821401245892, 12.897676529362798, 17.86059606820345, 18.107891896739602, 5.890507934615016, 75.51570019125938, 23.00173819437623, 8.994013167917728, 9.497016409412026, 75.53713069297373, 17.63738601654768, 19.043374076485634, 10.847014414146543, 21.973770946264267, 20.431155558675528, 21.22267721220851, 12.83528783172369, 25.482754016295075, 75.64998476393521, 10.99561190418899, 16.177440160885453, 12.536373373121023, 8.267774553969502, 14.661314593628049, 13.315743800252676, 13.285708088427782], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1079, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 844, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 724, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}, \"full_s1\": {\"times\": [6.557272005826235, 13.30385784804821, 12.393721845000982, 20.966787956655025, 18.84646543301642, 33.97123330272734, 6.879897966980934, 24.29985479451716, 12.998356265947223, 14.869501804932952, 17.984158493578434, 18.849919013679028, 76.2875934690237, 8.307313518598676, 6.929178504273295, 32.65210123360157, 12.316430946812034, 76.31797208078206, 8.589986260980368, 20.151168631389737, 13.631159098818898, 34.93915410526097, 12.632728463038802, 12.893065474927425, 12.354045446962118, 22.13497686944902, 16.693173775449395, 11.252564314752817, 18.948786783963442, 8.573606921359897, 12.790846752002835, 17.154880825430155, 11.101712444797158, 14.49220641888678, 12.012543451040983, 11.042622407898307, 15.202911971136928, 19.616007763892412, 21.66821843571961, 3.44002472050488, 26.173067569732666, 21.322467194870114, 19.05821535922587, 46.6952401753515, 20.961115062236786, 18.70112570747733, 12.290571074932814, 7.339368067681789, 76.24014202132821, 20.168137699365616, 76.25835328362882, 14.27820573747158, 11.254785351455212, 14.514818558469415, 4.3554796781390905, 18.05753686092794, 17.810633156448603, 35.22906826809049, 12.342857629060745, 27.953737488016486, 14.126854510977864, 16.15063438564539, 10.39058312959969, 17.40311536937952, 76.41485323384404, 19.67245303094387, 12.843625912442803, 76.37891258485615, 10.617164023220539, 18.871050599962473, 14.784893812611699, 15.83510966040194, 10.478933291509748, 76.39716600626707, 10.322485107928514, 13.050531685352325, 18.021803356707096, 18.26944730989635, 5.92651423625648, 76.69698422215879, 23.187818862497807, 9.064455602318048, 9.551359128206968, 76.14131500199437, 17.780814606696367, 19.20519828237593, 10.946219146251678, 22.183561097830534, 20.623430989682674, 21.442427676171064, 12.946139235049486, 25.714026479050517, 76.25824106112123, 11.080481877550483, 16.318021584302187, 12.635702196508646, 8.318728053942323, 14.814586939290166, 13.413050413131714, 13.398678639903665], \"tokens\": [366, 741, 690, 1163, 1046, 1874, 384, 1346, 726, 827, 1000, 1043, 4096, 464, 387, 1798, 685, 4096, 478, 1119, 758, 1919, 704, 719, 688, 1228, 926, 627, 1053, 477, 712, 952, 617, 807, 670, 615, 842, 1088, 1203, 192, 1448, 1179, 1057, 2551, 1162, 1039, 685, 409, 4096, 1115, 4096, 794, 628, 805, 243, 1000, 990, 1942, 688, 1544, 787, 899, 581, 965, 4096, 1094, 716, 4096, 591, 1048, 823, 878, 585, 4096, 577, 726, 1001, 1017, 331, 4096, 1289, 507, 533, 4096, 991, 1068, 612, 1230, 1148, 1188, 723, 1426, 4096, 619, 909, 707, 466, 823, 749, 748]}}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

Now let me compute the DocRED latency stats and then compile all tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "6b482f4f-9e19-468c-bf2c-99be2ba2c326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PqsSjEhehNkx5WoVaojGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5189,
      "cache_read_input_tokens": 49389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5189
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

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01JY1vWGMQfj91u5CoopFMEc`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nimport numpy as np\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/data/latency_profiling_docred_qwen_ft.json') as f:\n    data = json.load(f)\n\nprint('DocRED Latency Profiling (Qwen FT, 100 samples):')\nprint(f'Grammar compile time: {data[\\\"grammar_compile_time\\\"]*1000:.1f}ms')\nprint()\n\nfor mode in ['unconstrained', 'grammar_only', 'semantic_only', 'full_s1']:\n    times = np.array(data[mode]['times'])\n    tokens = np.array(data[mode]['tokens'])\n    mean_t = np.mean(times)\n    p50 = np.median(times)\n    p95 = np.percentile(times, 95)\n    p99 = np.percentile(times, 99)\n    tok_per_s = np.sum(tokens) / np.sum(times)\n    \n    base_mean = np.mean(data['unconstrained']['times'])\n    overhead = (mean_t - base_mean) / base_mean * 100\n    \n    overhead_str = f'+{overhead:.1f}%' if mode != 'unconstrained' else '—'\n    print(f'{mode:20s} | N=100 | Mean={mean_t:.3f}s | P50={p50:.3f}s | P95={p95:.3f}s | P99={p99:.3f}s | {overhead_str} | {tok_per_s:.1f} tok/s')\n\"\n",
  "description": "Compute DocRED latency statistics",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "9e3177d1-7157-4b1c-9c4f-c640abdf1b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PqsSjEhehNkx5WoVaojGF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5189,
      "cache_read_input_tokens": 49389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5189
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

_source line 51 · 2026-05-16T16:45:44.280Z_

<details><summary>↩ Tool result · `toolu_01JY1vWGMQfj91u5CoopFMEc`</summary>

```text
DocRED Latency Profiling (Qwen FT, 100 samples):
Grammar compile time: 44.0ms

unconstrained        | N=100 | Mean=21.023s | P50=15.588s | P95=72.882s | P99=73.522s | — | 56.8 tok/s
grammar_only         | N=100 | Mean=21.366s | P50=15.793s | P95=74.089s | P99=74.349s | +1.6% | 55.9 tok/s
semantic_only        | N=100 | Mean=21.912s | P50=15.827s | P95=75.517s | P99=75.650s | +4.2% | 55.4 tok/s
full_s1              | N=100 | Mean=22.147s | P50=15.993s | P95=76.289s | P99=76.418s | +5.3% | 54.9 tok/s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "4119acea-11e6-4e72-9088-edcc14419538",
  "tool_use_result": {
    "stdout": "DocRED Latency Profiling (Qwen FT, 100 samples):\nGrammar compile time: 44.0ms\n\nunconstrained        | N=100 | Mean=21.023s | P50=15.588s | P95=72.882s | P99=73.522s | — | 56.8 tok/s\ngrammar_only         | N=100 | Mean=21.366s | P50=15.793s | P95=74.089s | P99=74.349s | +1.6% | 55.9 tok/s\nsemantic_only        | N=100 | Mean=21.912s | P50=15.827s | P95=75.517s | P99=75.650s | +4.2% | 55.4 tok/s\nfull_s1              | N=100 | Mean=22.147s | P50=15.993s | P95=76.289s | P99=76.418s | +5.3% | 54.9 tok/s",
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

_source line 52_

Now I have all the data. Let me compile the tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "a393d8b1-2b00-4563-8cd5-eb10a9e4a227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLpFmKE7VkBY2DMGWQDMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 54578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 802
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

_source line 53_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HeY7bxhcVwteojWJTqe3v9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "62a457ba-0bd4-4952-9217-4561c6fe4a72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLpFmKE7VkBY2DMGWQDMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 54578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 802
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

_source line 54 · 2026-05-16T16:45:48.235Z_

<details><summary>↩ Tool result · `toolu_01HeY7bxhcVwteojWJTqe3v9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "ea64f3c6-917e-4d5a-8d06-b6e90e5cca45",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the tables. Let me organize the data:

**Table 2: Main Results**

For consistency, I need to normalize the metric formats. Some experiments report percentages as decimals (0.3098 = 30.98%) and some as percentages directly (59.37%). Let me be careful about this.

Experiments with decimal format (multiply by 100):
- phase2_scierc_full_s1: E_F1=0.3098, R_F1=0.0836, ET=0%, RV=0%, DR=0.93%, CF=9.9%, parse_fail=0%


- phase2_scierc_unconstrained: E_F1=0.3101, R_F1=0.0823, ET=0.4%, RV=1.39%, DR=15.37%, CF=0.08%, parse_fail=0%
- llama_scierc_full_s1: E_F1=0.2349, R_F1=0.0254, ET=0%, RV=0%, DR=0.08%, CF=6.56%, parse_fail≈0.18%
- llama_scierc_unconstrained: E_F1=0.2356, R_F1=0.0268

Generating markdown table... Now I'm looking at the performance metrics for the DocRED experiments across different models and configurations, comparing entity and relation F1 scores along with various error types and parsing failures. I see the pattern now — the constrained version uses percentage format while the unconstrained version stores values as decimals, so I need to multiply by 100 to compare them directly. The constrained E_F1 of 50.59% matches the unconstrained 0.4851 converted to 48.51%, confirming they're measuring the same metrics in different formats.

Now I'm compiling the fine-tuning experiment results across the different model configurations, converting all scores to percentage format so I can build a consistent comparison table. Now I'm looking at the performance metrics for the Qwen and Llama models across different datasets and constraint settings. The Llama models on DocRED show stronger relation F1 scores compared to Qwen, with the constrained version reaching 85.23% entity F1 and 44.23% relation F1, though it has some constraint violations to investigate. I'm noticing the cross-field consistency rates vary quite a bit across models and datasets—some constrained versions actually show higher CF violation rates than their unconstrained counterparts, which is counterintuitive but I'll just report the numbers as they are. Let me continue filling in the CF% column for the remaining rows. I'm noticing the cross-field consistency metric behaves differently across experiments—it's higher in constrained mode for Qwen, which seems counterintuitive, but I'll report the numbers as they appear in the registry. The metric name varies across datasets (CF_pct vs cross_field_consistency_violation_rate), so I'll normalize everything to percentages. Now I need to compile the DocRED latency summary and pull together the data for Table 6 starting with SciERC.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "ee5a5a46-57e1-4d1b-8936-f04613787fc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2bf3gaJ1XHXantfYYG74f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 55380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 56_

Now I have all the data. Let me write the tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "807525dd-8caa-4fd4-8271-681b6c96c5e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2bf3gaJ1XHXantfYYG74f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 55380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 57_

<details open><summary>🔧 Tool call — Write · `toolu_01J85AvfytiaTdieZy8pz9p3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table2_main_results.md",
  "content": "# Table 2: Main Results — Zero-Shot and Fine-Tuned IE with OntoCoDec\n\n## Zero-Shot (ZS)\n\n| Model | Dataset | Method | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|---------|--------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | SciERC | Unconstrained | 31.01 | 8.23 | 0.40 | 1.39 | 15.37 | 0.08 | 0.00 |\n| Qwen3-8B | SciERC | **OntoCoDec** | 30.98 | 8.36 | 0.00 | 0.00 | 0.93 | 9.90 | 0.00 |\n| Llama3.1-8B | SciERC | Unconstrained | 23.56 | 2.68 | 0.00 | 0.55 | 13.34 | 0.47 | 0.18 |\n| Llama3.1-8B | SciERC | **OntoCoDec** | 23.49 | 2.54 | 0.00 | 0.00 | 0.08 | 6.56 | 0.00 |\n| Mistral-7B | SciERC | Unconstrained | 27.28 | 3.66 | 1.50 | 0.00 | 56.94 | 56.87 | 0.00 |\n| Mistral-7B | SciERC | **OntoCoDec** | 27.46 | 3.67 | 0.00 | 0.00 | 13.40 | 1.27 | 0.00 |\n| Qwen3-8B | DocRED | Unconstrained | 58.15 | 7.74 | 2.48 | 29.66 | 18.46 | 0.10 | 1.20 |\n| Qwen3-8B | DocRED | **OntoCoDec** | 59.37 | 8.23 | 0.00 | 0.03 | 10.21 | 2.57 | 1.11 |\n| Llama3.1-8B | DocRED | Unconstrained | 55.65 | 5.98 | 0.13 | 16.03 | 26.07 | 0.17 | 6.81 |\n| Llama3.1-8B | DocRED | **OntoCoDec** | 55.01 | 6.27 | 0.00 | 0.00 | 2.55 | 12.02 | 9.12 |\n| Mistral-7B | DocRED | Unconstrained | 48.51 | 4.34 | 7.58 | 42.35 | 57.42 | 24.78 | 0.70 |\n| Mistral-7B | DocRED | **OntoCoDec** | 50.59 | 5.52 | 0.00 | 0.00 | 33.20 | 0.19 | 0.80 |\n\n## Fine-Tuned (FT)\n\n| Model | Dataset | Method | E_F1 (%) | R_F1 (%) | R_F1_excl_fail (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|---------|--------|----------|----------|-------------------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | SciERC | Unconstrained | 67.05 | 43.86 | — | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | SciERC | **OntoCoDec** | 67.05 | 43.77 | — | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | SciERC | Unconstrained | 67.76 | 45.45 | — | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | SciERC | **OntoCoDec** | 67.76 | 45.47 | — | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n| Qwen3-8B | DocRED | Unconstrained | 82.15 | 40.86 | 42.20 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | DocRED | **OntoCoDec** | 81.43 | 40.56 | 42.23 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | DocRED | Unconstrained | 83.93 | 43.72 | — | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | DocRED | **OntoCoDec** | 85.23 | 44.23 | — | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Notes:**\n- ET = Entity Type violation rate, RV = Relation Vocabulary violation rate, DR = Domain-Range violation rate, CF = Cross-Field consistency violation rate\n- R_F1_excl_fail = R_F1 computed excluding parse-failure documents (shown only for DocRED where parse_fail_rate is high)\n- Qwen DocRED FT: overall R_F1 depressed by high parse_fail_rate; R_F1_excl_fail shows performance on successfully-parsed documents\n- All metrics from checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "b5b2ffba-f88a-4c04-800b-936c90e7d7d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2bf3gaJ1XHXantfYYG74f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 55380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
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

_source line 58 · 2026-05-16T16:46:56.939Z_

<details><summary>↩ Tool result · `toolu_01J85AvfytiaTdieZy8pz9p3`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table2_main_results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "b4ac2fd8-20f3-44e3-875d-42698a4a114c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table2_main_results.md",
    "content": "# Table 2: Main Results — Zero-Shot and Fine-Tuned IE with OntoCoDec\n\n## Zero-Shot (ZS)\n\n| Model | Dataset | Method | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|---------|--------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | SciERC | Unconstrained | 31.01 | 8.23 | 0.40 | 1.39 | 15.37 | 0.08 | 0.00 |\n| Qwen3-8B | SciERC | **OntoCoDec** | 30.98 | 8.36 | 0.00 | 0.00 | 0.93 | 9.90 | 0.00 |\n| Llama3.1-8B | SciERC | Unconstrained | 23.56 | 2.68 | 0.00 | 0.55 | 13.34 | 0.47 | 0.18 |\n| Llama3.1-8B | SciERC | **OntoCoDec** | 23.49 | 2.54 | 0.00 | 0.00 | 0.08 | 6.56 | 0.00 |\n| Mistral-7B | SciERC | Unconstrained | 27.28 | 3.66 | 1.50 | 0.00 | 56.94 | 56.87 | 0.00 |\n| Mistral-7B | SciERC | **OntoCoDec** | 27.46 | 3.67 | 0.00 | 0.00 | 13.40 | 1.27 | 0.00 |\n| Qwen3-8B | DocRED | Unconstrained | 58.15 | 7.74 | 2.48 | 29.66 | 18.46 | 0.10 | 1.20 |\n| Qwen3-8B | DocRED | **OntoCoDec** | 59.37 | 8.23 | 0.00 | 0.03 | 10.21 | 2.57 | 1.11 |\n| Llama3.1-8B | DocRED | Unconstrained | 55.65 | 5.98 | 0.13 | 16.03 | 26.07 | 0.17 | 6.81 |\n| Llama3.1-8B | DocRED | **OntoCoDec** | 55.01 | 6.27 | 0.00 | 0.00 | 2.55 | 12.02 | 9.12 |\n| Mistral-7B | DocRED | Unconstrained | 48.51 | 4.34 | 7.58 | 42.35 | 57.42 | 24.78 | 0.70 |\n| Mistral-7B | DocRED | **OntoCoDec** | 50.59 | 5.52 | 0.00 | 0.00 | 33.20 | 0.19 | 0.80 |\n\n## Fine-Tuned (FT)\n\n| Model | Dataset | Method | E_F1 (%) | R_F1 (%) | R_F1_excl_fail (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|---------|--------|----------|----------|-------------------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | SciERC | Unconstrained | 67.05 | 43.86 | — | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | SciERC | **OntoCoDec** | 67.05 | 43.77 | — | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | SciERC | Unconstrained | 67.76 | 45.45 | — | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | SciERC | **OntoCoDec** | 67.76 | 45.47 | — | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n| Qwen3-8B | DocRED | Unconstrained | 82.15 | 40.86 | 42.20 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | DocRED | **OntoCoDec** | 81.43 | 40.56 | 42.23 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | DocRED | Unconstrained | 83.93 | 43.72 | — | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | DocRED | **OntoCoDec** | 85.23 | 44.23 | — | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Notes:**\n- ET = Entity Type violation rate, RV = Relation Vocabulary violation rate, DR = Domain-Range violation rate, CF = Cross-Field consistency violation rate\n- R_F1_excl_fail = R_F1 computed excluding parse-failure documents (shown only for DocRED where parse_fail_rate is high)\n- Qwen DocRED FT: overall R_F1 depressed by high parse_fail_rate; R_F1_excl_fail shows performance on successfully-parsed documents\n- All metrics from checker_version: fixed_20260514_v2 (strip + alias + unique_et)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Write · `toolu_01B3614JdhPtguQWJDaWUe4e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table3_composability.md",
  "content": "# Table 3: Composability — FT + OntoCoDec (Post-Training Constraint Integration)\n\nOntoCoDec applied at inference time to fine-tuned models without retraining.\n\n| Model | Dataset | | E_F1 (%) | R_F1 (%) | DR% | RV% | CF% | Parse Fail% |\n|-------|---------|---|----------|----------|-----|-----|-----|-------------|\n| Qwen3-8B | SciERC | Unconstrained | 67.05 | 43.86 | 1.95 | 0.00 | 0.00 | 0.00 |\n| | | + OntoCoDec | 67.05 | 43.77 | 0.00 | 0.00 | 1.18 | 0.00 |\n| | | **Δ** | **0.00** | **−0.09** | **−1.95** | **0.00** | **+1.18** | **0.00** |\n| Qwen3-8B | DocRED | Unconstrained | 82.15 | 40.86 | 0.76 | 0.27 | 0.12 | 7.11 |\n| | | + OntoCoDec | 81.43 | 40.56 | 0.01 | 0.00 | 0.41 | 8.52 |\n| | | **Δ** | **−0.72** | **−0.30** | **−0.75** | **−0.27** | **+0.29** | **+1.41** |\n| Llama3.1-8B | SciERC | Unconstrained | 67.76 | 45.45 | 1.11 | 0.00 | 0.00 | 0.00 |\n| | | + OntoCoDec | 67.76 | 45.47 | 0.09 | 0.00 | 0.46 | 0.00 |\n| | | **Δ** | **0.00** | **+0.02** | **−1.02** | **0.00** | **+0.46** | **0.00** |\n| Llama3.1-8B | DocRED | Unconstrained | 83.93 | 43.72 | 0.49 | 0.15 | — | 2.30 |\n| | | + OntoCoDec | 85.23 | 44.23 | 0.20 | 0.00 | 0.26 | 2.51 |\n| | | **Δ** | **+1.30** | **+0.51** | **−0.29** | **−0.15** | — | **+0.21** |\n\n**Key Findings:**\n- OntoCoDec is composable: plug-in at inference without retraining, near-zero F1 cost (max Δ R_F1 = −0.30pp on Qwen DocRED)\n- DR reduction: 59–100% relative reduction across all settings\n- RV elimination: 0% residual in all constrained settings\n- Llama DocRED shows net positive Δ (+0.51 R_F1) — constrained decoding helps the model stay on-schema\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "26858973-5850-4dc8-b457-ea90d8f328a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013esyUYFGT1P7Mtad4bQMRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4648,
      "cache_read_input_tokens": 56370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4648
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

_source line 60 · 2026-05-16T16:47:10.933Z_

<details><summary>↩ Tool result · `toolu_01B3614JdhPtguQWJDaWUe4e`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table3_composability.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "80925145-9c37-4c0a-a8de-3af8f0d58ffc",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table3_composability.md",
    "content": "# Table 3: Composability — FT + OntoCoDec (Post-Training Constraint Integration)\n\nOntoCoDec applied at inference time to fine-tuned models without retraining.\n\n| Model | Dataset | | E_F1 (%) | R_F1 (%) | DR% | RV% | CF% | Parse Fail% |\n|-------|---------|---|----------|----------|-----|-----|-----|-------------|\n| Qwen3-8B | SciERC | Unconstrained | 67.05 | 43.86 | 1.95 | 0.00 | 0.00 | 0.00 |\n| | | + OntoCoDec | 67.05 | 43.77 | 0.00 | 0.00 | 1.18 | 0.00 |\n| | | **Δ** | **0.00** | **−0.09** | **−1.95** | **0.00** | **+1.18** | **0.00** |\n| Qwen3-8B | DocRED | Unconstrained | 82.15 | 40.86 | 0.76 | 0.27 | 0.12 | 7.11 |\n| | | + OntoCoDec | 81.43 | 40.56 | 0.01 | 0.00 | 0.41 | 8.52 |\n| | | **Δ** | **−0.72** | **−0.30** | **−0.75** | **−0.27** | **+0.29** | **+1.41** |\n| Llama3.1-8B | SciERC | Unconstrained | 67.76 | 45.45 | 1.11 | 0.00 | 0.00 | 0.00 |\n| | | + OntoCoDec | 67.76 | 45.47 | 0.09 | 0.00 | 0.46 | 0.00 |\n| | | **Δ** | **0.00** | **+0.02** | **−1.02** | **0.00** | **+0.46** | **0.00** |\n| Llama3.1-8B | DocRED | Unconstrained | 83.93 | 43.72 | 0.49 | 0.15 | — | 2.30 |\n| | | + OntoCoDec | 85.23 | 44.23 | 0.20 | 0.00 | 0.26 | 2.51 |\n| | | **Δ** | **+1.30** | **+0.51** | **−0.29** | **−0.15** | — | **+0.21** |\n\n**Key Findings:**\n- OntoCoDec is composable: plug-in at inference without retraining, near-zero F1 cost (max Δ R_F1 = −0.30pp on Qwen DocRED)\n- DR reduction: 59–100% relative reduction across all settings\n- RV elimination: 0% residual in all constrained settings\n- Llama DocRED shows net positive Δ (+0.51 R_F1) — constrained decoding helps the model stay on-schema\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Write · `toolu_01X1brwDHxu3MxwUdNQPaJSP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
  "content": "# Table 4: FT Ablation — Constraint Layer Decomposition\n\nModes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).\n\n## SciERC\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |\n| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |\n| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |\n| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n\n## DocRED\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |\n| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |\n| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |\n| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |\n| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Observations:**\n- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR\n- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)\n- Full combination: near-zero DR residual with sub-additive constraint interaction\n- F1 impact: ≤0.30pp R_F1 cost across all completed settings\n- Llama DocRED semantic_only: experiment still RUNNING\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "28d8caf6-2433-448f-b2f0-6fb4698fd366",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBTNDSYdQkWDQ4Fv5yqjyL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 61018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1001
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

_source line 62 · 2026-05-16T16:47:28.848Z_

<details><summary>↩ Tool result · `toolu_01X1brwDHxu3MxwUdNQPaJSP`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "61c71cab-6480-4aab-bfa7-bc29991f35c2",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
    "content": "# Table 4: FT Ablation — Constraint Layer Decomposition\n\nModes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).\n\n## SciERC\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |\n| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |\n| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |\n| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |\n| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |\n| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |\n| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |\n\n## DocRED\n\n| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |\n|-------|------|----------|----------|-----|-----|-----|-----|-------------|\n| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |\n| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |\n| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |\n| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |\n| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |\n| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |\n| Llama3.1-8B | semantic_only | — | — | — | — | — | — | RUNNING |\n| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |\n\n**Observations:**\n- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR\n- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)\n- Full combination: near-zero DR residual with sub-additive constraint interaction\n- F1 impact: ≤0.30pp R_F1 cost across all completed settings\n- Llama DocRED semantic_only: experiment still RUNNING\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Write · `toolu_01LafgZ7bXQwyeufbRQ9Gzpc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table5_posthoc.md",
  "content": "# Table 5: Post-hoc Filtering Baseline Comparison\n\nPost-hoc filtering: generate unconstrained, then reject triples violating ontology constraints.\nOntoCoDec: constrained decoding enforces constraints during generation.\n\n## Zero-Shot Regime\n\n| Model | Dataset | Triples | Reject% | R_F1 Before | R_F1 Post-hoc | R_F1 OntoCoDec | TP Lost (post-hoc) |\n|-------|---------|---------|---------|-------------|---------------|----------------|-------------------|\n| Qwen3-8B | SciERC | 1724 | 16.76 | 8.23 | 8.63 | 8.36 | 7 |\n| Llama3.1-8B | SciERC | 1274 | 13.89 | 2.68 | 2.71 | 2.54 | 2 |\n| Mistral-7B | SciERC | 1584 | 20.27 | 3.76 | 3.94 | 3.67 | 4 |\n| Qwen3-8B | DocRED | 17497 | 48.12 | 7.74 | 9.61 | 8.23 | 127 |\n| Llama3.1-8B | DocRED | 16437 | 42.18 | 5.98 | 7.44 | 6.27 | 48 |\n| Mistral-7B | DocRED | 11836 | **73.73** | 4.34 | 3.85 | 5.52 | 226 |\n\n## Fine-Tuned Regime\n\n| Model | Dataset | Reject% | R_F1 Before | R_F1 Post-hoc | R_F1 OntoCoDec | TP Lost (post-hoc) |\n|-------|---------|---------|-------------|---------------|----------------|-------------------|\n| Qwen3-8B | SciERC | 1.95 | 43.86 | 43.94 | 43.77 | 4 |\n| Llama3.1-8B | SciERC | 1.11 | 45.45 | 45.23 | 45.47 | 5 |\n| Qwen3-8B | DocRED | 1.03 | 40.91 | 41.11 | N/A | 1 |\n| Llama3.1-8B | DocRED | 0.64 | 43.77 | 43.92 | 44.23 | 1 |\n\n**Key Findings:**\n- ZS: Post-hoc achieves higher R_F1 than OntoCoDec in 5/6 settings (by removing low-precision violating triples that happen to be FPs)\n- Exception: Mistral DocRED — 73.7% rejection rate causes net F1 loss (loses 226 TPs, R_F1 drops 3.85 < 4.34 before)\n- FT: Rejection rates are very low (0.6–2.0%) since fine-tuned models already produce mostly valid outputs\n- OntoCoDec advantage over post-hoc: **structural guarantee** (0% ET/RV violations), composability, and no TP loss risk from over-rejection\n- Post-hoc cannot guarantee 0% violations (residual ET after filtering observed in Mistral DocRED: 2.47%)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "26ab7ef2-46c9-49cc-bdec-25ecf0e688d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WUdhAVCt5LCp4rnnaQrAL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1405,
      "cache_read_input_tokens": 62019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1405
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

_source line 64 · 2026-05-16T16:47:47.630Z_

<details><summary>↩ Tool result · `toolu_01LafgZ7bXQwyeufbRQ9Gzpc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table5_posthoc.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "b5b3af30-34ce-4a83-b8fb-477c2623fbea",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table5_posthoc.md",
    "content": "# Table 5: Post-hoc Filtering Baseline Comparison\n\nPost-hoc filtering: generate unconstrained, then reject triples violating ontology constraints.\nOntoCoDec: constrained decoding enforces constraints during generation.\n\n## Zero-Shot Regime\n\n| Model | Dataset | Triples | Reject% | R_F1 Before | R_F1 Post-hoc | R_F1 OntoCoDec | TP Lost (post-hoc) |\n|-------|---------|---------|---------|-------------|---------------|----------------|-------------------|\n| Qwen3-8B | SciERC | 1724 | 16.76 | 8.23 | 8.63 | 8.36 | 7 |\n| Llama3.1-8B | SciERC | 1274 | 13.89 | 2.68 | 2.71 | 2.54 | 2 |\n| Mistral-7B | SciERC | 1584 | 20.27 | 3.76 | 3.94 | 3.67 | 4 |\n| Qwen3-8B | DocRED | 17497 | 48.12 | 7.74 | 9.61 | 8.23 | 127 |\n| Llama3.1-8B | DocRED | 16437 | 42.18 | 5.98 | 7.44 | 6.27 | 48 |\n| Mistral-7B | DocRED | 11836 | **73.73** | 4.34 | 3.85 | 5.52 | 226 |\n\n## Fine-Tuned Regime\n\n| Model | Dataset | Reject% | R_F1 Before | R_F1 Post-hoc | R_F1 OntoCoDec | TP Lost (post-hoc) |\n|-------|---------|---------|-------------|---------------|----------------|-------------------|\n| Qwen3-8B | SciERC | 1.95 | 43.86 | 43.94 | 43.77 | 4 |\n| Llama3.1-8B | SciERC | 1.11 | 45.45 | 45.23 | 45.47 | 5 |\n| Qwen3-8B | DocRED | 1.03 | 40.91 | 41.11 | N/A | 1 |\n| Llama3.1-8B | DocRED | 0.64 | 43.77 | 43.92 | 44.23 | 1 |\n\n**Key Findings:**\n- ZS: Post-hoc achieves higher R_F1 than OntoCoDec in 5/6 settings (by removing low-precision violating triples that happen to be FPs)\n- Exception: Mistral DocRED — 73.7% rejection rate causes net F1 loss (loses 226 TPs, R_F1 drops 3.85 < 4.34 before)\n- FT: Rejection rates are very low (0.6–2.0%) since fine-tuned models already produce mostly valid outputs\n- OntoCoDec advantage over post-hoc: **structural guarantee** (0% ET/RV violations), composability, and no TP loss risk from over-rejection\n- Post-hoc cannot guarantee 0% violations (residual ET after filtering observed in Mistral DocRED: 2.47%)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Write · `toolu_01TJkcqtkiBhYHqx2Yhr8T5v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table6_latency.md",
  "content": "# Table 6: Latency Profiling — OntoCoDec Decoding Overhead\n\nHardware: NVIDIA RTX PRO 6000 (98GB), Qwen3-8B LoRA-merged checkpoint.\nProtocol: 100 samples, 5-sample warmup, `torch.cuda.synchronize()` + `time.perf_counter()`, same process sequential runs.\n\n## SciERC (avg output ~150 tokens/sample)\n\n| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |\n|------|---|----------|---------|---------|---------|----------|-------|\n| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |\n| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |\n| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |\n| **full (OntoCoDec)** | 100 | 2.655 | 2.416 | 6.162 | 8.449 | **+2.3%** | 56.4 |\n\n## DocRED (avg output ~1200 tokens/sample, includes max_tokens=4096 truncations)\n\n| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |\n|------|---|----------|---------|---------|---------|----------|-------|\n| unconstrained | 100 | 21.023 | 15.588 | 72.882 | 73.522 | — | 56.8 |\n| grammar_only | 100 | 21.366 | 15.793 | 74.089 | 74.349 | +1.6% | 55.9 |\n| semantic_only | 100 | 21.912 | 15.827 | 75.517 | 75.650 | +4.2% | 55.4 |\n| **full (OntoCoDec)** | 100 | 22.147 | 15.993 | 76.289 | 76.418 | **+5.3%** | 54.9 |\n\n## Summary\n\n| Dataset | Full OntoCoDec Overhead | Absolute Cost/Sample |\n|---------|------------------------|---------------------|\n| SciERC | +2.3% | +61 ms |\n| DocRED | +5.3% | +1.12 s |\n\n- Grammar compile time: 44ms (one-time, amortized over all samples)\n- All overhead differences statistically significant (p < 0.0001, paired t-test)\n- Grammar layer: +1.6–1.7% (token-level FSM constraint check)\n- Semantic layer: +1.2–4.2% (DR/CF validation per generated triple)\n- Combined overhead sub-additive on SciERC (1.7+1.2→2.3%), near-additive on DocRED (1.6+4.2→5.3%)\n- DocRED higher semantic overhead due to larger ontology (96 relation types, complex DR rules) vs SciERC (7 types)\n- Practically negligible for both datasets — constraint enforcement costs <6% throughput\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "3967e607-4c2e-4178-bf29-3f2150aa4e84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vssAD5ihj4my2ccgBKhLG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 63424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1038
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

_source line 66 · 2026-05-16T16:48:06.721Z_

<details><summary>↩ Tool result · `toolu_01TJkcqtkiBhYHqx2Yhr8T5v`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table6_latency.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "0c6b77b0-a0ee-4f16-8cad-ac114216e0ca",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table6_latency.md",
    "content": "# Table 6: Latency Profiling — OntoCoDec Decoding Overhead\n\nHardware: NVIDIA RTX PRO 6000 (98GB), Qwen3-8B LoRA-merged checkpoint.\nProtocol: 100 samples, 5-sample warmup, `torch.cuda.synchronize()` + `time.perf_counter()`, same process sequential runs.\n\n## SciERC (avg output ~150 tokens/sample)\n\n| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |\n|------|---|----------|---------|---------|---------|----------|-------|\n| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |\n| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | +1.7% | 56.7 |\n| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | +1.2% | 57.0 |\n| **full (OntoCoDec)** | 100 | 2.655 | 2.416 | 6.162 | 8.449 | **+2.3%** | 56.4 |\n\n## DocRED (avg output ~1200 tokens/sample, includes max_tokens=4096 truncations)\n\n| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |\n|------|---|----------|---------|---------|---------|----------|-------|\n| unconstrained | 100 | 21.023 | 15.588 | 72.882 | 73.522 | — | 56.8 |\n| grammar_only | 100 | 21.366 | 15.793 | 74.089 | 74.349 | +1.6% | 55.9 |\n| semantic_only | 100 | 21.912 | 15.827 | 75.517 | 75.650 | +4.2% | 55.4 |\n| **full (OntoCoDec)** | 100 | 22.147 | 15.993 | 76.289 | 76.418 | **+5.3%** | 54.9 |\n\n## Summary\n\n| Dataset | Full OntoCoDec Overhead | Absolute Cost/Sample |\n|---------|------------------------|---------------------|\n| SciERC | +2.3% | +61 ms |\n| DocRED | +5.3% | +1.12 s |\n\n- Grammar compile time: 44ms (one-time, amortized over all samples)\n- All overhead differences statistically significant (p < 0.0001, paired t-test)\n- Grammar layer: +1.6–1.7% (token-level FSM constraint check)\n- Semantic layer: +1.2–4.2% (DR/CF validation per generated triple)\n- Combined overhead sub-additive on SciERC (1.7+1.2→2.3%), near-additive on DocRED (1.6+4.2→5.3%)\n- DocRED higher semantic overhead due to larger ontology (96 relation types, complex DR rules) vs SciERC (7 types)\n- Practically negligible for both datasets — constraint enforcement costs <6% throughput\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 67_

Now let me register all artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "28416a30-934b-4306-a347-1eb07e7d7753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLdC7NRjS4Usod66WjKBJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 64462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Pa5WsLceZF84Zv1cBvuArd`</summary>

```json
{
  "name": "Table 2: Main Results (ZS + FT)",
  "type": "report",
  "description": "Main results table: 3 models × 2 datasets × 2 regimes (ZS/FT), showing E_F1, R_F1, violation rates, parse_fail_rate",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table2_main_results.md",
  "tags": [
    "paper",
    "table",
    "main-results"
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "7fbee625-1cd8-4981-86aa-bac5b4220bdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLdC7NRjS4Usod66WjKBJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 64462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
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

_source line 69 · 2026-05-16T16:48:13.452Z_

<details><summary>↩ Tool result · `toolu_01Pa5WsLceZF84Zv1cBvuArd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_fd9ddf\", \"name\": \"Table 2: Main Results (ZS + FT)\", \"type\": \"report\", \"description\": \"Main results table: 3 models × 2 datasets × 2 regimes (ZS/FT), showing E_F1, R_F1, violation rates, parse_fail_rate\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table2_main_results.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:13.317517+00:00\", \"tags\": [\"paper\", \"table\", \"main-results\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "162fcf95-8651-46e9-879d-bbd5531e1bfe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_fd9ddf\\\", \\\"name\\\": \\\"Table 2: Main Results (ZS + FT)\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Main results table: 3 models × 2 datasets × 2 regimes (ZS/FT), showing E_F1, R_F1, violation rates, parse_fail_rate\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/report/table2_main_results.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:48:13.317517+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"table\\\", \\\"main-results\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_fd9ddf\", \"name\": \"Table 2: Main Results (ZS + FT)\", \"type\": \"report\", \"description\": \"Main results table: 3 models × 2 datasets × 2 regimes (ZS/FT), showing E_F1, R_F1, violation rates, parse_fail_rate\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table2_main_results.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:13.317517+00:00\", \"tags\": [\"paper\", \"table\", \"main-results\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_014zG8yyNWtB4V19oLb4GGcW`</summary>

```json
{
  "name": "Table 3: Composability (FT+OntoCoDec)",
  "type": "report",
  "description": "Composability table: FT models + OntoCoDec at inference, showing delta metrics for Qwen/Llama × SciERC/DocRED",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table3_composability.md",
  "tags": [
    "paper",
    "table",
    "composability"
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "978c296f-8483-4eb5-a7d0-b6317b8cdff7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLdC7NRjS4Usod66WjKBJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 64462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
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

_source line 71 · 2026-05-16T16:48:15.922Z_

<details><summary>↩ Tool result · `toolu_014zG8yyNWtB4V19oLb4GGcW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_70fda8\", \"name\": \"Table 3: Composability (FT+OntoCoDec)\", \"type\": \"report\", \"description\": \"Composability table: FT models + OntoCoDec at inference, showing delta metrics for Qwen/Llama × SciERC/DocRED\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table3_composability.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:15.789978+00:00\", \"tags\": [\"paper\", \"table\", \"composability\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d6a7031f-f373-4f85-bcbb-4047f957bd36",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_70fda8\\\", \\\"name\\\": \\\"Table 3: Composability (FT+OntoCoDec)\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Composability table: FT models + OntoCoDec at inference, showing delta metrics for Qwen/Llama × SciERC/DocRED\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/report/table3_composability.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:48:15.789978+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"table\\\", \\\"composability\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_70fda8\", \"name\": \"Table 3: Composability (FT+OntoCoDec)\", \"type\": \"report\", \"description\": \"Composability table: FT models + OntoCoDec at inference, showing delta metrics for Qwen/Llama × SciERC/DocRED\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table3_composability.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:15.789978+00:00\", \"tags\": [\"paper\", \"table\", \"composability\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_0147gXiGH4QBvJhz1a3fC92q`</summary>

```json
{
  "name": "Table 4: FT Ablation",
  "type": "report",
  "description": "Ablation table: unconstrained/grammar_only/semantic_only/full for 2 models × 2 datasets in FT regime",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table4_ft_ablation.md",
  "tags": [
    "paper",
    "table",
    "ablation"
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "b96fdedb-3198-4d0a-8826-4130260e8589",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLdC7NRjS4Usod66WjKBJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 64462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
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

_source line 73 · 2026-05-16T16:48:17.898Z_

<details><summary>↩ Tool result · `toolu_0147gXiGH4QBvJhz1a3fC92q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_10113d\", \"name\": \"Table 4: FT Ablation\", \"type\": \"report\", \"description\": \"Ablation table: unconstrained/grammar_only/semantic_only/full for 2 models × 2 datasets in FT regime\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table4_ft_ablation.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:17.765754+00:00\", \"tags\": [\"paper\", \"table\", \"ablation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "a592bb66-03d3-4347-a6c4-683d817559de",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_10113d\\\", \\\"name\\\": \\\"Table 4: FT Ablation\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Ablation table: unconstrained/grammar_only/semantic_only/full for 2 models × 2 datasets in FT regime\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/report/table4_ft_ablation.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:48:17.765754+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"table\\\", \\\"ablation\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_10113d\", \"name\": \"Table 4: FT Ablation\", \"type\": \"report\", \"description\": \"Ablation table: unconstrained/grammar_only/semantic_only/full for 2 models × 2 datasets in FT regime\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table4_ft_ablation.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:17.765754+00:00\", \"tags\": [\"paper\", \"table\", \"ablation\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_017V5b5DfZHKgKRYfquxyeNg`</summary>

```json
{
  "name": "Table 5: Post-hoc Baseline",
  "type": "report",
  "description": "Post-hoc filtering baseline comparison: rejection rates, TP loss, R_F1 before/after for ZS and FT regimes",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table5_posthoc.md",
  "tags": [
    "paper",
    "table",
    "posthoc-baseline"
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "364a00e5-618c-4557-8d0e-6dfdc7c370b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLdC7NRjS4Usod66WjKBJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 64462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
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

_source line 75 · 2026-05-16T16:48:20.383Z_

<details><summary>↩ Tool result · `toolu_017V5b5DfZHKgKRYfquxyeNg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_921382\", \"name\": \"Table 5: Post-hoc Baseline\", \"type\": \"report\", \"description\": \"Post-hoc filtering baseline comparison: rejection rates, TP loss, R_F1 before/after for ZS and FT regimes\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table5_posthoc.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:20.248209+00:00\", \"tags\": [\"paper\", \"table\", \"posthoc-baseline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "925a66ed-0ac2-4fc8-8054-98d4378bbd2d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_921382\\\", \\\"name\\\": \\\"Table 5: Post-hoc Baseline\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Post-hoc filtering baseline comparison: rejection rates, TP loss, R_F1 before/after for ZS and FT regimes\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/report/table5_posthoc.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:48:20.248209+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"table\\\", \\\"posthoc-baseline\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_921382\", \"name\": \"Table 5: Post-hoc Baseline\", \"type\": \"report\", \"description\": \"Post-hoc filtering baseline comparison: rejection rates, TP loss, R_F1 before/after for ZS and FT regimes\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table5_posthoc.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:20.248209+00:00\", \"tags\": [\"paper\", \"table\", \"posthoc-baseline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_013LR4V6Wf1rCTkUZmDvaqjJ`</summary>

```json
{
  "name": "Table 6: Latency Profiling",
  "type": "report",
  "description": "Latency profiling: SciERC and DocRED decoding overhead for each constraint layer, tok/s, percentile timings",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/table6_latency.md",
  "tags": [
    "paper",
    "table",
    "latency"
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
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "ee290aec-bf4f-4217-8886-727ee4410f1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CLdC7NRjS4Usod66WjKBJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 64462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1047
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

_source line 77 · 2026-05-16T16:48:22.645Z_

<details><summary>↩ Tool result · `toolu_013LR4V6Wf1rCTkUZmDvaqjJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c46a66\", \"name\": \"Table 6: Latency Profiling\", \"type\": \"report\", \"description\": \"Latency profiling: SciERC and DocRED decoding overhead for each constraint layer, tok/s, percentile timings\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table6_latency.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:22.503254+00:00\", \"tags\": [\"paper\", \"table\", \"latency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "d8bc0b75-f8ec-4935-b44c-1bd3d1abb04f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_c46a66\\\", \\\"name\\\": \\\"Table 6: Latency Profiling\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Latency profiling: SciERC and DocRED decoding overhead for each constraint layer, tok/s, percentile timings\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/report/table6_latency.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T16:48:22.503254+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"table\\\", \\\"latency\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_c46a66\", \"name\": \"Table 6: Latency Profiling\", \"type\": \"report\", \"description\": \"Latency profiling: SciERC and DocRED decoding overhead for each constraint layer, tok/s, percentile timings\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/table6_latency.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:48:22.503254+00:00\", \"tags\": [\"paper\", \"table\", \"latency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

5 个表格全部编译完成并注册：

| 文件 | 内容 |
|------|------|
| `table2_main_results.md` | 3 模型 × 2 数据集 × ZS/FT，完整 violation rates |
| `table3_composability.md` | FT+OntoCoDec 即插即用，Δ metrics |
| `table4_ft_ablation.md` | 4 modes ablation（Llama DocRED semantic_only 标注 RUNNING） |
| `table5_posthoc.md` | Post-hoc filtering 对比，ZS+FT |
| `table6_latency.md` | SciERC +2.3% / DocRED +5.3% overhead |

缺失数据：
- `latency_profiling_scierc` / `latency_profiling_docred` registry 中无此 ID，数据从 artifacts 文件读取
- `phase1_scierc_zs_qwen` / `phase1_docred_zs_qwen` 实际 ID 为 `phase2_scierc_unconstrained` / `phase2_docred_unconstrained`
- `phase2_llama_*` 实际 ID 为 `llama_scierc_full_s1` / `llama_docred_full_s1` 等
- `w8_llama_docred_ft_semantic_only` 状态 RUNNING，Table 4 中标注
- `w8_zs_posthoc_baseline` 不存在，数据合并在 `w8_ft_posthoc_baseline` 的 `zs_regime` 字段中

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "uuid": "751470e6-0010-484e-973d-981ce82c0397",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuxhvVeEWjCQubc3osEekA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2854,
      "cache_read_input_tokens": 65509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2854
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

_source line 79_

5 个表格全部编译完成并注册：

| 文件 | 内容 |
|------|------|
| `table2_main_results.md` | 3 模型 × 2 数据集 × ZS/FT，完整 violation rates |
| `table3_composability.md` | FT+OntoCoDec 即插即用，Δ metrics |
| `table4_ft_ablation.md` | 4 modes ablation（Llama DocRED semantic_only 标注 RUNNING） |
| `table5_posthoc.md` | Post-hoc filtering 对比，ZS+FT |
| `table6_latency.md` | SciERC +2.3% / DocRED +5.3% overhead |

缺失数据：
- `latency_profiling_scierc` / `latency_profiling_docred` registry 中无此 ID，数据从 artifacts 文件读取
- `phase1_scierc_zs_qwen` / `phase1_docred_zs_qwen` 实际 ID 为 `phase2_scierc_unconstrained` / `phase2_docred_unconstrained`
- `phase2_llama_*` 实际 ID 为 `llama_scierc_full_s1` / `llama_docred_full_s1` 等
- `w8_llama_docred_ft_semantic_only` 状态 RUNNING，Table 4 中标注
- `w8_zs_posthoc_baseline` 不存在，数据合并在 `w8_ft_posthoc_baseline` 的 `zs_regime` 字段中

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 290519,
  "duration_api_ms": 289331,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "0e9a111f-2b9d-4af4-bdb7-53d0dddfe07d",
  "total_cost_usd": 1.3347975,
  "usage": {
    "input_tokens": 32,
    "cache_creation_input_tokens": 56522,
    "cache_read_input_tokens": 1102376,
    "output_tokens": 17137,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 56522,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 446,
        "cache_read_input_tokens": 65509,
        "cache_creation_input_tokens": 2854,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2854
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1687,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001762,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 32,
      "outputTokens": 17137,
      "cacheReadInputTokens": 1102376,
      "cacheCreationInputTokens": 56522,
      "webSearchRequests": 0,
      "costUSD": 1.3330355,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b6ea3f3f-4533-4bf2-a196-572dfc752c76"
}
```

</details>

---
