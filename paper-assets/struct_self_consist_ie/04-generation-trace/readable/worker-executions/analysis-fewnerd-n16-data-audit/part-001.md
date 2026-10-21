# analysis fewnerd n16 data audit — Part 1 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[Transcript overview](../analysis-fewnerd-n16-data-audit.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/1f/1f50996e18172e45c8f8.json)

## Before a recorded user message

## Before a recorded user message

17 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
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
  "uuid": "7601f4e3-d32e-43b3-9140-acfaa5318fd8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779193800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2846b0a3-3b3b-4b60-8d29-d4ec95e0db84",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Assistant

_source line 4_

I'll tackle both tasks in parallel: registry lookup, SSH data search, and caption script investigation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "1e10cbf5-ee3f-447d-83b8-d790206218b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMZCDaoJFaSrKPsRpvroZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13380
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01S9Y7SzrGbuNHT7ntYF6CpM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
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
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "fbca8f30-c1dd-4464-af20-41c3f99f0727",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMZCDaoJFaSrKPsRpvroZS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13380,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13380
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

_source line 6 · 2026-05-19T07:57:27.745Z_

<details><summary>↩ Tool result · `toolu_01S9Y7SzrGbuNHT7ntYF6CpM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b6435bbb-5aab-4900-a61c-ace7890370a3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I'll run the registry lookup and SSH searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "92d3905e-3557-4588-a2dc-f27ef1bf89ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiRU77rwQHZicJFqJvXM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1038
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

Starting parallel searches: registry for FewNERD N=16 experiments, SSH for output files, and the plot script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "ba97fcb3-3c00-423c-832f-14631acb810e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiRU77rwQHZicJFqJvXM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1038
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LCDainKy3GNXHLCgeecKJH`</summary>

```json
{
  "project": "struct_self_consist_ie",
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
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "d731237a-975d-47f4-9ccc-a0aa6017e3ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiRU77rwQHZicJFqJvXM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1038
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

_source line 10 · 2026-05-19T07:57:34.189Z_

<details><summary>↩ Tool result · `toolu_01LCDainKy3GNXHLCgeecKJH`</summary>

```text
Error: result (259,757 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "9e54dc6a-d02b-4ab1-8d21-5d0feffb4ba0",
  "tool_use_result": {
    "content": "Error: result (259,757 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_qwen25_32b_fewnerd\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:25.428Z\", \"updated_at\": \"2026-05-19T07:52:18.591Z\", \"hypothesis\": \"The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:41.246Z\"}, \"notes\": \"2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h.\"}, \"exp_qwen25_7b_fewnerd\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:41:43.121Z\", \"updated_at\": \"2026-05-19T07:48:40.207Z\", \"hypothesis\": \"Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale.\"}, \"exp_wnut17_qwen25_7b\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:33.960Z\", \"updated_at\": \"2026-05-19T06:47:45.220Z\", \"hypothesis\": \"The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:45.220Z\"}}, \"exp_qwen25_14b_fewnerd\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:31.620Z\", \"updated_at\": \"2026-05-19T06:47:43.938Z\", \"hypothesis\": \"The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-19T06:47:43.938Z\"}}, \"exp_qwen25_72b_zeroshot\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:28.597Z\", \"updated_at\": \"2026-05-19T06:47:42.657Z\", \"hypothesis\": \"The correlation-selection gap persists in zero-shot settings at 72B scale. Qwen2.5-72B-Instruct without fine-tuning should exhibit similar structured self-consistency phenomena on SciERC/CoNLL/FewNERD: oracle headroom exists, QE signals correlate with quality, but instance-level selection fails. This tests generalization beyond fine-tuned models.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:42.658Z\"}}, \"exp_llama_fewnerd_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:18:49.938Z\", \"updated_at\": \"2026-05-19T03:15:04.486Z\", \"hypothesis\": \"LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.\", \"parent\": \"exp_llama_fewnerd_lora\", \"spec\": {\"command\": \"bash code/run_llama_fewnerd_inference.sh\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"LLaMA-3.1-8B-FewNERD-LoRA-merged\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"exp_llama_fewnerd_lora\", \"eval_data\": \"FewNERD test set\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-fewnerd-merged/\", \"log_path\": \"logs/llama_fewnerd_inference.log\"}, \"conclusion\": \"success\", \"metrics\": {\"3seed_mean\": {\"greedy_f1\": 0.7842, \"oracle_f1\": 0.8843, \"headroom_pp\": 10.01, \"degeneracy_pct\": 23.36, \"lp_delta_pp\": 0.36, \"dgs_delta_pp\": -0.35}, \"seed_42\": {\"greedy_f1\": 0.7841, \"oracle_f1\": 0.8854, \"degen\": 27.32}, \"seed_123\": {\"greedy_f1\": 0.784, \"oracle_f1\": 0.8839, \"degen\": 24.63}, \"seed_456\": {\"greedy_f1\": 0.7844, \"oracle_f1\": 0.8835, \"degen\": 18.13}, \"signal_ranking\": \"LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)\", \"lp_only_positive\": true, \"n_instances_gold_filtered\": 32565}, \"completed_at\": \"2026-05-19T03:15:04.486Z\"}, \"exp_entity_construction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:12.074Z\", \"updated_at\": \"2026-05-19T02:40:17.571Z\", \"hypothesis\": \"Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/entity_construction_fair.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/entity_construction_fair/\", \"log_path\": \"output/entity_construction_fair/\"}, \"completed_at\": \"2026-05-19T02:15:19.616Z\", \"metrics\": {\"n16_fair_cv\": {\"scierc_ner\": {\"cv_uniform_delta\": \"+1.35pp\", \"p_value\": 0.018, \"significant\": true}, \"conll_ner\": {\"cv_uniform_delta\": \"+0.10pp\", \"p_value\": 0.303, \"significant\": false}, \"fewnerd_ner\": {\"cv_uniform_delta\": \"+1.32pp\", \"p_value\": 0, \"significant\": true}, \"scierc_re\": {\"cv_uniform_delta\": \"+1.69pp\", \"p_value\": 0.049, \"significant\": true}}, \"n8_fair_cv\": {\"scierc_ner\": {\"uniform_confirm\": \"+1.54pp (p=0.023, sig)\", \"lp_weighted_confirm\": \"+1.67pp (p=0.004, sig)\", \"cv_uniform\": \"+1.12pp (p=0.057, borderline)\"}, \"conll_ner\": {\"cv_uniform\": \"-0.39pp (p=0.963, not sig)\"}, \"fewnerd_ner\": {\"lp_weighted_cv\": \"+0.88pp (p=0.000, sig)\", \"uniform_cv\": \"+0.32pp (p=0.003, sig)\"}}, \"adaptive_combination\": \"INVALIDATED - gold label leakage confirmed\", \"note\": \"5-fold CV, bootstrap B=10000, paired one-sided\"}}, \"exp_lp_alignment_gating\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:16.520Z\", \"updated_at\": \"2026-05-19T02:15:48.197Z\", \"hypothesis\": \"Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/lp_alignment_gated_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:23.716Z\", \"metrics\": {\"adjusted_score\": \"mean_rho * valid_ratio\", \"threshold\": 0.3, \"accuracy\": \"3/3 datasets correct\", \"robust_range\": \"0.2-0.4\"}}, \"exp_selective_prediction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:13.989Z\", \"updated_at\": \"2026-05-19T02:15:46.588Z\", \"hypothesis\": \"QE signals (especially voting_confidence) can drive practical selective prediction: filtering out low-confidence instances yields significant F1 improvement on retained instances, enabling human-AI collaboration for structured IE.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/selective_prediction.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:21.704Z\", \"metrics\": {\"vc_best_signal\": true, \"f1_at_80pct_coverage\": {\"scierc\": \"+5.0pp\", \"conll\": \"+8.4pp\", \"fewnerd\": \"+6.2pp\"}, \"precision_coverage_curves\": \"output/prescriptive_analysis/fig_selective_prediction.pdf\"}}, \"exp_llama_fewnerd_lora\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:20:55.859Z\", \"updated_at\": \"2026-05-19T01:08:20.832Z\", \"hypothesis\": \"LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER\", \"spec\": {\"command\": \"llamafactory-cli train train_config_llama_fewnerd.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 137865, \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": -1, \"model_name\": \"LLaMA-Few-NERD-LoRA\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"run_script\": \"run_llama_fewnerd_train_single_gpu.sh\", \"tmux_session\": \"llama_fewnerd\", \"note\": \"Retroactively registered - data_count unknown, seed assumed 42\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 3, \"train_loss\": 0.0516, \"eval_loss\": 0.0323, \"train_runtime_hours\": 15.35, \"total_steps\": 24708, \"final_checkpoint\": \"checkpoint-24708\", \"adapter_size_mb\": 320}, \"completed_at\": \"2026-05-19T01:08:20.832Z\"}, \"hidden_state_probe_conll_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:57:45.711Z\", \"updated_at\": \"2026-05-19T00:30:18.272Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:18.272Z\"}, \"hidden_state_probe_conll_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:35:05.317Z\", \"updated_at\": \"2026-05-19T00:30:16.471Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:16.471Z\"}, \"exp_031_fewnerd_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:04:12.040Z\", \"updated_at\": \"2026-05-19T00:30:14.652Z\", \"hypothesis\": \"FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:14.652Z\"}, \"exp_030_conll_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:24:47.839Z\", \"updated_at\": \"2026-05-19T00:30:12.698Z\", \"hypothesis\": \"CoNLL T=1.2 temperature ablation: test if higher temperature reduces degeneracy on CoNLL as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：N不一致(N=8 vs T=1.0基准的N=16)。Director决定不重跑——SciERC T消融(T=0.5/0.8/1.0/1.2, 551inst, N=8)已够用，论文温度消融用SciERC单数据集。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:12.699Z\"}, \"mbr_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:06.462Z\", \"updated_at\": \"2026-05-19T00:29:39.285Z\", \"conclusion\": \"killed\", \"notes\": \"MBR tested negative as one of 6 methods, stale entry\", \"completed_at\": \"2026-05-19T00:29:39.285Z\"}, \"dgs_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:04.572Z\", \"updated_at\": \"2026-05-19T00:29:37.275Z\", \"hypothesis\": \"Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.\", \"conclusion\": \"killed\", \"notes\": \"D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)\", \"completed_at\": \"2026-05-19T00:29:37.275Z\"}, \"exp_fewnerd_s789_n8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:17:34.011Z\", \"updated_at\": \"2026-05-18T23:18:28.125Z\", \"hypothesis\": \"FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.\", \"parent\": \"exp_029a\", \"spec\": {\"command\": \"python code/analyze_fewnerd_s789.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B (ft_002_v2)\", \"seed\": 789, \"checkpoint_source\": \"exp_021 shards\", \"eval_data\": \"FewNERD test (37648 instances, 32565 gold-filtered)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:18:17.902Z\", \"metrics\": {\"greedy_f1\": 0.7478, \"oracle_f1\": 0.8714, \"headroom_pp\": 12.37, \"degen_rate\": 0.1177, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"lp_sel_f1\": 0.7614, \"lp_delta_pp\": 1.36, \"lp_rho_global\": 0.1788, \"lp_rho_cond\": 0.176, \"dgs_f1\": 0.7621, \"dgs_delta_pp\": 1.43, \"dgs_vs_lp_pp\": 0.07, \"best_signal\": \"LP\", \"four_seed_mean_greedy\": 0.7481, \"four_seed_mean_lp_delta_pp\": 1.38, \"four_seed_lp_delta_ci95\": [1.32, 1.44]}}, \"exp_026_t12_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:43.694Z\", \"updated_at\": \"2026-05-18T22:07:24.547Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:05.941Z\", \"metrics\": {\"ner_greedy_f1\": 0.6637, \"ner_oracle_f1\": 0.7821, \"rho_sj_ner\": 0.3995, \"sample_f1_pct_zero\": 14.08, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t12_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:42.754Z\", \"updated_at\": \"2026-05-18T22:07:23.135Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:04.119Z\", \"metrics\": {\"ner_greedy_f1\": 0.6595, \"ner_oracle_f1\": 0.7895, \"rho_sj_ner\": 0.359, \"sample_f1_pct_zero\": 13.99, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:41.840Z\", \"updated_at\": \"2026-05-18T22:07:21.767Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:02.272Z\", \"metrics\": {\"ner_greedy_f1\": 0.6621, \"ner_oracle_f1\": 0.7754, \"rho_sj_ner\": 0.3921, \"sample_f1_pct_zero\": 12.97, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:40.599Z\", \"updated_at\": \"2026-05-18T22:07:20.459Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:00.430Z\", \"metrics\": {\"ner_greedy_f1\": 0.6633, \"ner_oracle_f1\": 0.7777, \"rho_sj_ner\": 0.3809, \"sample_f1_pct_zero\": 12.59, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:39.473Z\", \"updated_at\": \"2026-05-18T22:07:19.035Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=42) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 42 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:58.573Z\", \"metrics\": {\"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.7798, \"rho_sj_ner\": 0.3598, \"sample_f1_pct_zero\": 12.9, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:38.605Z\", \"updated_at\": \"2026-05-18T22:07:17.604Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:56.681Z\", \"metrics\": {\"ner_greedy_f1\": 0.6641, \"ner_oracle_f1\": 0.7694, \"rho_sj_ner\": 0.3771, \"sample_f1_pct_zero\": 11.79, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:37.454Z\", \"updated_at\": \"2026-05-18T22:07:16.089Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:54.734Z\", \"metrics\": {\"ner_greedy_f1\": 0.6607, \"ner_oracle_f1\": 0.7714, \"rho_sj_ner\": 0.3893, \"sample_f1_pct_zero\": 11.22, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:36.536Z\", \"updated_at\": \"2026-05-18T22:07:14.675Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:52.749Z\", \"metrics\": {\"ner_greedy_f1\": 0.6639, \"ner_oracle_f1\": 0.7437, \"rho_sj_ner\": 0.3279, \"sample_f1_pct_zero\": 10.28, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:35.201Z\", \"updated_at\": \"2026-05-18T22:07:13.198Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:50.703Z\", \"metrics\": {\"ner_greedy_f1\": 0.6611, \"ner_oracle_f1\": 0.7444, \"rho_sj_ner\": 0.3133, \"sample_f1_pct_zero\": 10.09, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_029b\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:32:18.543Z\", \"updated_at\": \"2026-05-18T22:05:45.856Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.\", \"parent\": \"ft_002_v2\", \"failure_reason\": \"OOM on cuda:1 due to residual vLLM process (PID 416808) occupying 30.2GB VRAM\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:05:15.948Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:29.806594+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:58:43.646574+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:05:20.480884+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"completed_at\": \"2026-05-18T00:56:47.625Z\", \"spec\": {\"pid\": \"441471\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_scierc_10ep.yaml\", \"data_path\": \"scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"scierc_uie_test\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_029b.log\"}, \"metrics\": {\"degen_rate\": 0.478, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_029a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:32:17.191Z\", \"updated_at\": \"2026-05-18T22:05:44.959Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.\", \"parent\": \"ft_002_v2\", \"spec\": {\"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=0 bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 436761, \"data_path\": \"data/scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_029a_inference.log\", \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"data/scierc_uie_dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:55:16.392Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:20.617085+00:00\"}]}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:00:18.242Z\", \"metrics\": {\"degen_rate\": 0.064, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_021_fewnerd_n8_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:17.992Z\", \"updated_at\": \"2026-05-18T22:04:50.774Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:35.573Z\", \"metrics\": {\"degen_rate\": 0.1212, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7888, \"ner_oracle_f1\": 0.881, \"rho_fk_ner\": 0.1632, \"rho_sj_ner\": 0.313, \"sample_f1_pct_zero\": 19.32}}, \"exp_021_fewnerd_n8_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:16.735Z\", \"updated_at\": \"2026-05-18T22:04:49.470Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:33.731Z\", \"metrics\": {\"degen_rate\": 0.1312, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7885, \"ner_oracle_f1\": 0.8892, \"rho_fk_ner\": 0.1602, \"rho_sj_ner\": 0.3083, \"sample_f1_pct_zero\": 20.39}}, \"exp_002_conll_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:15.720Z\", \"updated_at\": \"2026-05-18T22:04:46.954Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:31.934Z\", \"metrics\": {\"degen_rate\": 0.5544, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9074, \"ner_oracle_f1\": 0.9549, \"rho_fk_ner\": 0.4718, \"rho_sj_ner\": 0.4819, \"sample_f1_pct_zero\": 7.02}}, \"exp_002_conll_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:14.343Z\", \"updated_at\": \"2026-05-18T22:04:45.039Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 123 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:29.992Z\", \"metrics\": {\"degen_rate\": 0.471, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9068, \"ner_oracle_f1\": 0.9633, \"rho_fk_ner\": 0.4524, \"rho_sj_ner\": 0.4621, \"sample_f1_pct_zero\": 7.54}}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-18T20:50:15.047Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.\", \"parent\": \"exp_017_llama_conll_n16_s456\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024\", \"gpu\": \"cuda:2\", \"pid\": \"175870\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_s456_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8672, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.469, \"rho_sj_ner\": 0.4734, \"rho_vc_ner\": 0.4722, \"rho_em_ner\": 0.4752, \"rho_lp_ner\": 0.3099, \"auroc_fk_ner\": 0.7408, \"auroc_sj_ner\": 0.7428, \"auroc_vc_ner\": 0.7495, \"auroc_em_ner\": 0.7444, \"auroc_lp_ner\": 0.7628, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_s456_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:25.899Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-18T20:50:11.906Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.\", \"parent\": \"exp_017_llama_conll_n16\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024\", \"gpu\": \"cuda:1\", \"pid\": \"175734\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8647, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.4752, \"rho_sj_ner\": 0.4836, \"rho_vc_ner\": 0.4746, \"rho_em_ner\": 0.4818, \"rho_lp_ner\": 0.3136, \"auroc_fk_ner\": 0.7467, \"auroc_sj_ner\": 0.7496, \"auroc_vc_ner\": 0.7529, \"auroc_em_ner\": 0.7508, \"auroc_lp_ner\": 0.7661, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:23.213Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).\"}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:12:43.492Z\", \"updated_at\": \"2026-05-18T20:50:04.988Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=456 with explicit max_tokens=1024. Replaces exp_007 re-analysis for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"157584\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"finished_at\": \"2026-05-15T06:18:22.307Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:18:24.880896+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456_r1024\", \"metrics\": {\"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:45.350Z\", \"hypothesis\": \"LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:09:57.155Z\", \"updated_at\": \"2026-05-18T20:50:00.335Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=42 with explicit max_tokens=1024. Replaces exp_007_llama_inference for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 42, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed42_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"156809\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"finished_at\": \"2026-05-15T06:15:47.963Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:15:50.613872+00:00\"}]}, \"metrics\": {\"degen_rate\": 0.2495, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:47.660Z\", \"hypothesis\": \"LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.\"}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:12:16.041Z\", \"updated_at\": \"2026-05-18T20:49:50.398Z\", \"spec\": {\"hypothesis\": \"Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16\", \"plan_id\": \"exp-002\", \"parent\": \"exp_002_ner_conll2003\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.4844, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}, \"checkpoint_path\": \"output/exp_002_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_002_conll_n16.log\", \"completed_at\": \"2026-05-14T18:58:40.473Z\", \"hypothesis\": \"CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).\"}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-18T20:49:42.395Z\", \"spec\": {\"hypothesis\": \"Verify if max_tokens=512 truncation inflated Table 1 N=8 SciERC signal values. Rerun with max_tokens=1024 for clean comparison.\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"parent\": \"exp_012_logprob_baseline\", \"data_count\": 551, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024\", \"checkpoint_path\": \"output/exp_012_rerun_1024/\", \"log_path\": \"output/exp_012_rerun_1024/run.log\", \"data_path\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1777, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}, \"completed_at\": \"2026-05-14T23:10:33.075Z\", \"hypothesis\": \"Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.\"}, \"exp_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:27.504Z\", \"updated_at\": \"2026-05-18T20:49:10.758Z\", \"hypothesis\": \"LLaMA-3.1-8B on SciERC with seed=456 will show consistent 5-signal ranking patterns (SJ/FK > logprob) and DGS selection gains comparable to seed=42 and seed=123, confirming cross-seed stability.\", \"spec\": {\"command\": \"python3 code/analyze_llama_scierc_seed456_5signal.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_018_llama_scierc_seed456/samples.jsonl\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"same as seed123\", \"eval_data\": \"SciERC test (551 instances)\", \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456/5signal_dgs_report.json\", \"log_path\": \"output/exp_018_llama_scierc_seed456/run.log\"}, \"metrics\": {\"greedy_f1\": 0.6457, \"oracle_f1\": 0.7574, \"headroom\": 0.1117, \"dgs_f1\": 0.6454, \"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"rho_SJ_full\": 0.3663, \"rho_FK_full\": 0.3115, \"rho_logprob_full\": 0.1911, \"rho_EM_full\": 0.3088, \"rho_vc_full\": 0.4135, \"auroc_SJ_full\": 0.7061, \"auroc_EM_full\": 0.7538, \"n_valid\": 529, \"n_conditional\": 478}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:16:00.973Z\"}, \"exp_007_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:10:26.278Z\", \"updated_at\": \"2026-05-18T20:49:08.934Z\", \"name\": \"LLaMA-3.1-8B SciERC NER inference seed=123\", \"hypothesis\": \"Structural consistency signals (SJ, FK) correlate with entity F1 for LLaMA-8B on SciERC at seed=123, and DGS selection improves over greedy baseline\", \"spec\": {\"command\": \"python3 code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct (SciERC LoRA fine-tuned)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-scierc-lora\", \"log_path\": \"output/exp_018_llama_scierc_seed123/report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T19:11:30.781Z\", \"metrics\": {\"greedy_f1\": 0.6454, \"oracle_f1\": 0.7657, \"headroom\": 0.1204, \"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"dgs_delta_pp\": -0.38, \"rho_SJ_full\": 0.3552, \"rho_voting_conf_full\": 0.4193, \"auroc_SJ_full\": 0.7092, \"auroc_EM_full\": 0.7468}}, \"exp_qwen3_4b_conll_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:08:28.512Z\", \"updated_at\": \"2026-05-18T20:49:06.922Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"222184\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_qwen3_4b_conll_scs_inference/report.json\", \"submitted_at\": \"2026-05-15T19:10:19.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-merged\", \"wall_clock_seconds\": 523.8, \"gpu_hours\": 0.15}, \"metrics\": {\"greedy_f1\": 0.9251, \"oracle_f1\": 0.9408, \"oracle_headroom_pp\": 1.57, \"SJ_rho_full\": 0.4045, \"SJ_rho_cond\": 0.4306, \"FK_rho_full\": 0.3961, \"FK_rho_cond\": 0.42, \"LP_rho_full\": 0.3186, \"LP_rho_cond\": 0.3378, \"LP_auroc_full\": 0.7689, \"LP_auroc_cond\": 0.8153, \"fleiss_kappa_mean\": 0.9349, \"soft_jaccard_mean\": 0.9754, \"structural_beats_surface\": true, \"rho_advantage_pp\": 0.84, \"n_instances\": 3453, \"n_gold_empty_filtered\": 697, \"n_greedy_f1_zero_filtered\": 112, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:19:03.585Z\", \"notes\": \"4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement.\", \"hypothesis\": \"CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.\"}, \"exp_qwen3_4b_conll_scs_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:41:33.501Z\", \"updated_at\": \"2026-05-18T20:49:03.705Z\", \"hypothesis\": \"CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA checkpoint-4200 merged)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-conll2003-lora/checkpoint-4200\", \"gpu\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/qwen3-4b-conll2003-merged-ckpt4200\", \"log_path\": \"/tmp/infer_4b_conll_v2.log\", \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_4b_conll_scs_v2\"}, \"metrics\": {\"greedy_f1\": 0.9234, \"oracle_f1\": 0.9404, \"oracle_headroom_pp\": 1.7, \"SJ_rho_full\": 0.4217, \"SJ_rho_cond\": 0.459, \"FK_rho_full\": 0.4181, \"FK_rho_cond\": 0.4538, \"LP_rho_full\": 0.3313, \"LP_rho_cond\": 0.3487, \"LP_auroc_full\": 0.7761, \"LP_auroc_cond\": 0.8209, \"n_instances\": 3453, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:54:14.575Z\", \"notes\": \"Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values.\"}, \"exp_qwen3_4b_scierc_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:45:33.384Z\", \"updated_at\": \"2026-05-18T20:49:01.260Z\", \"hypothesis\": \"SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_scierc_scs_inference\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-4b-scierc-merged (checkpoint-400)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-scierc-merged\", \"eval_data\": \"scierc test set\"}, \"metrics\": {\"ner_greedy_f1\": 0.6612, \"ner_oracle_f1\": 0.7839, \"ner_headroom_pp\": 12.28, \"ner_SJ_rho\": 0.4221, \"ner_FK_rho\": 0.3258, \"ner_LP_rho\": 0.28, \"re_greedy_f1\": 0.4136, \"re_oracle_f1\": 0.5846, \"re_headroom_pp\": 17.1, \"re_SJ_rho\": 0.2673, \"re_FK_rho\": 0.3593, \"re_LP_rho\": 0.3512, \"re_sample_f1_pct_zero\": 0.476, \"re_LP_rho_cond\": 0.1135, \"re_LP_rho_cond_p\": 0.074, \"degen_rate\": 0.104, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"/tmp/exp_qwen3_4b_scierc_scs_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T20:00:03.730Z\"}, \"exp_027_fewnerd_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:28:57.036Z\", \"updated_at\": \"2026-05-18T20:48:58.455Z\", \"spec\": {\"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"parent\": \"exp_021_fewnerd_full\", \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"data_path\": \"data/fewnerd_n16_subset/test.json\", \"data_count\": 5000, \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --start_index {0,1250,2500,3750} --end_index {1250,2500,3750,5000} --output_dir output/exp_027_fewnerd_n16/shard_{0-3}\", \"checkpoint_path\": \"output/exp_027_fewnerd_n16/sampled_results.jsonl\", \"log_path\": \"output/exp_027_fewnerd_n16/\"}, \"conclusion\": \"success\", \"metrics\": {\"LP_delta_pp\": 1.88, \"LP_delta_95CI\": [1.41, 2.37], \"degen_rate\": 0.0706, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"greedy_f1\": 0.7478, \"lp_sel_f1\": 0.7666, \"oracle_f1\": 0.902, \"headroom_pp\": 15.42, \"all_8_types_positive\": true, \"n_instances\": 5000, \"N_samples\": 16, \"bootstrap_p\": \"<0.001\"}, \"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"completed_at\": \"2026-05-17T05:46:48.460Z\"}, \"exp_026_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:18:18.780Z\", \"updated_at\": \"2026-05-18T20:48:24.965Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --n_samples 8 --temperature 1.2 --seed 42 --max_tokens 1024 --collect_logprobs --output_dir output/exp_026_t12\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"log_path\": \"output/exp_026_t12.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 1.2, \"task\": \"T-ablation\", \"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:37.648Z\", \"hypothesis\": \"Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:46.027Z\", \"updated_at\": \"2026-05-18T20:48:24.112Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t08/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.8, \"task\": \"T-ablation\", \"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:36.243Z\", \"hypothesis\": \"Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:19:35.753Z\", \"updated_at\": \"2026-05-18T20:48:23.339Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t05/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.5, \"task\": \"T-ablation\", \"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:34.808Z\", \"hypothesis\": \"Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_T12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:31.060Z\", \"updated_at\": \"2026-05-18T20:48:22.668Z\", \"hypothesis\": \"T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T09:39:51.733Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"finished_at\": \"2026-05-17T09:48:04.019Z\", \"training_hours\": 0.14}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"381369\", \"log_path\": \"output/exp_026_T12_run.log\", \"submitted_at\": \"2026-05-17T09:41:39.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T12/\", \"wall_clock_seconds\": 1114.4, \"gpu_hours\": 0.31}, \"pid\": \"381369\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T12.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:08.312470+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.075, \"lp_range_std\": 0.059, \"within_instance_rho_mean\": 0.2245, \"within_instance_rho_median\": 0.3152, \"within_instance_rho_valid_pct\": 0.875, \"greedy_f1\": 0.62, \"oracle_f1\": 0.758, \"lp_sel_f1\": 0.621, \"sj_sel_f1\": 0.597, \"em_sel_f1\": 0.596, \"vc_sel_f1\": 0.582, \"sj_rho\": 0.384, \"fk_rho\": 0.386, \"lp_rho\": 0.182, \"vc_rho\": 0.342, \"sj_auroc\": 0.683, \"lp_auroc\": 0.566}, \"completed_at\": \"2026-05-17T10:00:13.771Z\"}, \"exp_026_T08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:29.602Z\", \"updated_at\": \"2026-05-18T20:48:21.975Z\", \"hypothesis\": \"T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T09:39:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:56.543Z\", \"training_hours\": 0.13}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"380680\", \"log_path\": \"output/exp_026_T08_run.log\", \"submitted_at\": \"2026-05-17T09:41:20.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T08/\", \"wall_clock_seconds\": 1131.4, \"gpu_hours\": 0.31}, \"pid\": \"380680\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T08.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:02.635244+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.043, \"lp_range_std\": 0.042, \"within_instance_rho_mean\": 0.1701, \"within_instance_rho_median\": 0.2635, \"within_instance_rho_valid_pct\": 0.728, \"greedy_f1\": 0.616, \"oracle_f1\": 0.737, \"lp_sel_f1\": 0.627, \"sj_sel_f1\": 0.619, \"em_sel_f1\": 0.611, \"vc_sel_f1\": 0.603, \"sj_rho\": 0.378, \"fk_rho\": 0.34, \"lp_rho\": 0.212, \"vc_rho\": 0.352, \"sj_auroc\": 0.662, \"lp_auroc\": 0.571}, \"completed_at\": \"2026-05-17T10:00:12.248Z\"}, \"exp_026_T05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:28.066Z\", \"updated_at\": \"2026-05-18T20:48:16.286Z\", \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"380188\", \"log_path\": \"output/exp_026_T05_run.log\", \"submitted_at\": \"2026-05-17T09:40:51.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T05/\", \"wall_clock_seconds\": 1158.3, \"gpu_hours\": 0.32}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"380188\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T05.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:31.332Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:47:35.127151+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.022, \"lp_range_std\": 0.021, \"within_instance_rho_mean\": 0.1306, \"within_instance_rho_median\": 0.2182, \"within_instance_rho_valid_pct\": 0.597, \"greedy_f1\": 0.617, \"oracle_f1\": 0.71, \"lp_sel_f1\": 0.622, \"sj_sel_f1\": 0.622, \"em_sel_f1\": 0.619, \"vc_sel_f1\": 0.61, \"sj_rho\": 0.333, \"fk_rho\": 0.341, \"lp_rho\": 0.208, \"vc_rho\": 0.353, \"sj_auroc\": 0.644, \"lp_auroc\": 0.577}, \"completed_at\": \"2026-05-17T10:00:10.083Z\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:02.953Z\", \"updated_at\": \"2026-05-18T20:47:52.122Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.\", \"parent\": \"exp_017_llama_conll_n16_s123\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:20:51.219Z\", \"notes\": \"Output exists on autodl-5090. Registry status corrected from killed to success.\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\", \"metrics\": {\"degen_rate\": 0.8636, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:14.370Z\", \"updated_at\": \"2026-05-18T20:47:51.435Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed123/\", \"log_path\": \"output/exp_018_llama_scierc_seed123.log\", \"samples_md5\": \"072eeca68236d46b4c5c84b945209abc\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:04.855Z\", \"hypothesis\": \"LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\", \"metrics\": {\"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:13.570Z\", \"updated_at\": \"2026-05-18T20:47:50.032Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=456, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed456/\", \"log_path\": \"output/exp_018_qwen_scierc_seed456/run.log\", \"samples_md5\": \"46d0de47ad7693c07e7df3a77c90c3be\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:03.898Z\", \"hypothesis\": \"Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.2042, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:12.747Z\", \"updated_at\": \"2026-05-18T20:47:49.306Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed123/\", \"log_path\": \"output/exp_018_qwen_scierc_seed123.log\", \"samples_md5\": \"866a59581dea56f4633149f0b18a31ae\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:02.954Z\", \"hypothesis\": \"Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.172, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_epoch_dgs_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:57.921Z\", \"updated_at\": \"2026-05-18T20:01:46.134Z\", \"hypothesis\": \"DGS benefit is strictly monotonic with degeneracy rate: higher degeneracy → greater DGS improvement, validating that degeneracy rate is the key gating signal\", \"spec\": {\"command\": \"python3 code/epoch_dgs_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"completed_at\": \"2026-05-18T20:01:46.134Z\"}, \"exp_diagnostic_calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:56.064Z\", \"updated_at\": \"2026-05-18T20:01:44.364Z\", \"hypothesis\": \"A 3-indicator regression model (degeneracy rate, LP-F1 correlation, LP range) can quantitatively predict the optimal LP selection delta for unseen instances\", \"spec\": {\"command\": \"python3 code/diagnostic_calibration.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"completed_at\": \"2026-05-18T20:01:44.364Z\"}, \"exp_adaptive_temperature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:52.771Z\", \"updated_at\": \"2026-05-18T20:01:42.646Z\", \"hypothesis\": \"Adjusting sampling temperature based on instance-level confidence indicators can improve output diversity-quality tradeoff\", \"spec\": {\"command\": \"python3 code/adaptive_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"completed_at\": \"2026-05-18T20:01:42.646Z\"}, \"exp_entity_consensus\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:50.628Z\", \"updated_at\": \"2026-05-18T20:01:40.869Z\", \"hypothesis\": \"Constructing new output from N samples using entity frequency thresholds and LP-weighted decisions can capture complementary information that single-sample selection misses\", \"spec\": {\"command\": \"python3 code/entity_consensus.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"completed_at\": \"2026-05-18T20:01:40.869Z\"}, \"exp_ccs_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:48.671Z\", \"updated_at\": \"2026-05-18T20:01:39.128Z\", \"hypothesis\": \"Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy selection by adapting to local confidence patterns\", \"spec\": {\"command\": \"python3 code/ccs_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"completed_at\": \"2026-05-18T20:01:39.128Z\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T14:39:32.014Z\", \"updated_at\": \"2026-05-18T19:11:03.240Z\", \"completed_at\": \"2026-05-14T17:12:15.687Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"hypothesis\": \"On CoNLL (high degeneracy regime), LLaMA should show the same pattern as Qwen3: LP selection fails due to narrow headroom, but structural signals retain diagnostic value (QE rho). Cross-model validation of the degeneracy-driven signal effectiveness framework.\", \"parent\": \"exp_007_llama_inference\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T11:30:53.467Z\"}, \"metrics\": {\"degeneracy_cf1_gold_filtered\": 0.894, \"n_constant_f1\": 2465, \"n_gold_filtered\": 2756, \"n_total\": 3453, \"greedy_f1\": 0.9239, \"oracle_f1\": 0.9451, \"random_f1\": 0.9207, \"headroom_pp\": 2.11, \"dgs_f1\": 0.9254, \"dgs_delta_pp\": 0.14, \"dgs_nondegen_lp_delta_pp\": 1.37, \"selection_f1\": {\"SJ\": {\"f1\": 0.9237, \"delta_pp\": -0.04}, \"FK\": {\"f1\": 0.924, \"delta_pp\": -0.02}, \"VC\": {\"f1\": 0.925, \"delta_pp\": 0.08}, \"EM\": {\"f1\": 0.9244, \"delta_pp\": 0.02}, \"LP\": {\"f1\": 0.9244, \"delta_pp\": 0.02}}, \"qe_rho_full_3seed\": {\"SJ\": {\"mean\": 0.4631, \"sd\": 0.0074}, \"FK\": {\"mean\": 0.4546, \"sd\": 0.0061}, \"EM\": {\"mean\": 0.4603, \"sd\": 0.0078}, \"VC\": {\"mean\": 0.4579, \"sd\": 0.003}, \"LP\": {\"mean\": 0.3099, \"sd\": 0.0055}}, \"qe_auroc_full_3seed\": {\"SJ\": {\"mean\": 0.736, \"sd\": 0.0064}, \"FK\": {\"mean\": 0.732, \"sd\": 0.0063}, \"EM\": {\"mean\": 0.7355, \"sd\": 0.0069}, \"VC\": {\"mean\": 0.7394, \"sd\": 0.0041}, \"LP\": {\"mean\": 0.7629, \"sd\": 0.0044}}, \"lp_range\": {\"mean\": 0.0198, \"std\": 0.0315, \"median\": 0.0002}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/exp017_full_signal_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/full_signal_analysis.json\"}}, \"exp_017_llama_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:47:36.156Z\", \"updated_at\": \"2026-05-18T18:43:42.649Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_llama_conll2003_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"674921\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_finetune.log\", \"submitted_at\": \"2026-05-18T16:47:35.786Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/llmfactory_train.json\", \"data_count\": 14037, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora-3ep\", \"checkpoint_source\": \"Meta-Llama-3.1-8B-Instruct (base model, LoRA from scratch)\", \"eval_data\": \"conll2003_uie_dev\", \"wall_clock_seconds\": 6176.5, \"gpu_hours\": 1.72}, \"hypothesis\": \"Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.\", \"parent\": \"exp_llama_fewnerd_lora\", \"conclusion\": \"success\", \"metrics\": {\"degeneracy_rate\": 0.853, \"greedy_f1\": 0.928, \"oracle_f1\": 0.951, \"headroom\": 0.023, \"selection_f1\": 0.934, \"full_rho_SJ\": 0.45, \"full_rho_FK\": 0.443, \"full_rho_VC\": 0.437, \"full_rho_EM\": 0.448, \"full_rho_LP\": 0.273, \"full_AUROC_SJ\": 0.752, \"full_AUROC_EM\": 0.753, \"full_AUROC_LP\": 0.739, \"cond_rho_SJ\": 0.454, \"cond_rho_EM\": 0.458, \"cond_rho_LP\": 0.311, \"cond_AUROC_EM\": 0.783, \"cond_AUROC_LP\": 0.804}, \"completed_at\": \"2026-05-18T18:30:32.331Z\"}, \"exp_028_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:22:18.594Z\", \"updated_at\": \"2026-05-18T18:23:06.601Z\", \"hypothesis\": \"Full-sequence mean LP underperforms as a quality signal because format/schema tokens dilute the entity-relevant logprob signal; isolating entity-only tokens should yield higher QE correlation and selection F1.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python code/exp028_entity_token_lp_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_entity_token_lp/scierc/samples.jsonl\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_028_entity_token_lp/analysis_results.json\"}, \"completed_at\": \"2026-05-18T18:22:59.312Z\", \"metrics\": {\"greedy_f1\": 0.643, \"oracle_f1\": 0.7845, \"full_lp_global_rho\": 0.2971, \"entity_text_type_lp_global_rho\": 0.4401, \"full_lp_selection_f1\": 0.6465, \"entity_text_type_lp_selection_f1\": 0.6357, \"dilution_ratio\": 0.32, \"full_lp_within_range_median\": 0.0402, \"entity_text_type_within_range_median\": 0.1346, \"schema_only_within_range_median\": 0.0089}}, \"exp_026_t12_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:30:33.407Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t12/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 96.4, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:33.407Z\"}, \"exp_026_t08_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:30:31.219Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t08/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.8, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:31.219Z\"}, \"exp_026_t05_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:30:28.965Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t05/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.2, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:28.965Z\"}, \"exp_027_mlp_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:39:22.524Z\", \"updated_at\": \"2026-05-18T06:41:51.069Z\", \"metrics\": {\"lr_auroc\": 0.6522, \"mlp_auroc\": 0.6381, \"rf_auroc\": 0.5868, \"mlp_15feat_auroc\": 0.6341, \"lr_sel_f1\": 0.6406, \"mlp_sel_f1\": 0.6278, \"greedy_f1\": 0.6441, \"oracle_f1\": 0.8231, \"best_single_signal_auroc\": 0.6476, \"feature_bottleneck_confirmed\": true}, \"hypothesis\": \"MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap\", \"spec\": {\"command\": \"python train_mlp_verifier.py --n_samples 16 --cv_folds 5 --seeds 42,123,456\", \"server\": \"a100\", \"data_path\": \"output/exp_001_n16_seed*/samples.jsonl\", \"data_count\": 529, \"model_name\": \"sklearn LR/MLP/RF\", \"seed\": \"42,123,456\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_027_mlp_verifier/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T06:41:51.069Z\"}, \"exp_028_fewnerd_5epoch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:53:12.913Z\", \"updated_at\": \"2026-05-17T20:29:42.274Z\", \"spec\": {\"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"parent\": \"exp_021_fewnerd_full\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"log_path\": \"logs/exp_028_4gpu_train.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.3133, \"greedy_f1\": 0.7773, \"lp_sel_delta_pp\": 0.624, \"lp_sel_f1\": 0.7835, \"oracle_f1\": 0.8723, \"within_instance_rho_mean\": 0.4066, \"within_instance_rho_median\": 0.6151}, \"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"completed_at\": \"2026-05-17T20:29:42.274Z\"}, \"exp_028\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T07:35:39.447Z\", \"updated_at\": \"2026-05-17T20:26:59.399Z\", \"hypothesis\": \"Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-17T12:09:43.334Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:06:01.040147+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\", \"log_path\": \"logs/exp_028_4gpu_train.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:05:57.260Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.313, \"greedy_f1\": 0.7773, \"lp_sel_f1\": 0.7835, \"lp_sel_delta_pp\": 0.62, \"oracle_f1\": 0.8723, \"within_instance_rho\": 0.4066, \"train_loss\": 0.0189, \"eval_loss\": 0.0311}}, \"exp_024_claim_audit\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:36.291Z\", \"updated_at\": \"2026-05-17T10:55:08.244Z\", \"hypothesis\": \"Systematic cross-chapter numerical consistency audit: verify all quantitative claims in paper against source experiment data, catch stale values and cross-reference errors before submission.\", \"conclusion\": \"success\", \"metrics\": {\"consistent\": 97, \"errors\": 1, \"warnings\": 5, \"old_residuals_found\": 0}, \"spec\": {\"checkpoint_path\": \"artifacts/exp_024_claim_audit/audit_report.md\", \"log_path\": \"N/A\", \"command\": \"CPU-only paper audit\", \"server\": \"local\", \"data_path\": \"docs/paper/\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0}, \"completed_at\": \"2026-05-17T10:55:08.244Z\"}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:21.577Z\", \"updated_at\": \"2026-05-17T03:33:39.786Z\", \"hypothesis\": \"3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.\", \"spec\": {\"command\": \"python code/bootstrap_significance.py\", \"server\": \"local\", \"data_path\": \"output/exp_016_rerun_1024/\", \"data_count\": 529, \"model_name\": \"N/A (statistical analysis)\", \"seed\": \"3-seed bootstrap (1000 iterations)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_016_rerun_1024_bootstrap/\"}, \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}, \"completed_at\": \"2026-05-14T23:44:48.818Z\", \"parent\": \"exp_016_rerun_1024\"}, \"exp_verbalized_confidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:20.552Z\", \"updated_at\": \"2026-05-17T03:33:39.197Z\", \"hypothesis\": \"Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_verbalized_confidence.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp002_conll2003/samples.jsonl\", \"data_count\": 3285, \"model_name\": \"qwen3-8b-scierc-merged-v2 + qwen3-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"output/review_round9_experiments/verbalized_confidence/\", \"log_path\": \"output/review_round9_experiments/verbalized_confidence_run.log\"}, \"completed_at\": \"2026-05-16T03:09:39.916Z\", \"metrics\": {\"scierc\": {\"VerbConf_rho\": 0.2965, \"VerbConf_auroc\": 0.6811, \"VerbConf_sel_f1\": 0.6195, \"VerbConf_delta\": -0.0245, \"best_existing_rho\": 0.3792, \"VerbConf_mean\": 8.58, \"VerbConf_std\": 1.15, \"parse_fail_rate\": 0.0026}, \"conll\": {\"VerbConf_rho\": 0.3366, \"VerbConf_auroc\": 0.7469, \"VerbConf_sel_f1\": 0.8886, \"VerbConf_delta\": -0.0193, \"best_existing_rho\": 0.4507, \"VerbConf_mean\": 9.24, \"VerbConf_std\": 1.32, \"parse_fail_rate\": 0}}, \"parent\": \"exp_012_rerun_1024\"}, \"exp_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:39:44.631Z\", \"updated_at\": \"2026-05-17T03:33:38.371Z\", \"hypothesis\": \"Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-16T05:41:33.768Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"scierc_ner\": {\"greedy_f1\": 0.643, \"full_lp_sel_f1\": 0.6465, \"entity_lp_sel_f1\": 0.6262, \"oracle_f1\": 0.7845, \"entity_lp_delta_vs_full_lp\": -0.0203}, \"conll_ner\": {\"greedy_f1\": 0.9065, \"full_lp_sel_f1\": 0.8989, \"entity_lp_sel_f1\": 0.8659, \"oracle_f1\": 0.948, \"entity_lp_delta_vs_full_lp\": -0.033}, \"finding\": \"entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)\"}, \"spec\": {\"command\": \"python analyze_entity_token_lp.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/ + output/exp_002_conll_rerun_1024/\", \"data_count\": \"529 (SciERC NER) + 2756 (CoNLL NER)\", \"model_name\": \"Qwen3-8B (finetuned)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/exp_entity_token_lp/results.json\", \"log_path\": \"artifacts/exp_entity_token_lp/report.md\"}, \"completed_at\": \"2026-05-16T06:28:46.845Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:22.868Z\", \"updated_at\": \"2026-05-17T03:33:37.623Z\", \"spec\": {\"command\": \"python run_freeform_inference.py --seed 42 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"169042\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_ablation.log\", \"submitted_at\": \"2026-05-15T09:42:30.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Free-form decoding recovers logprob variance and selection ability lost under constrained decoding\", \"plan_id\": \"exp-018\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"tmux_session\": \"exp_freeform_ablation\", \"wall_clock_seconds\": 1059.0, \"gpu_hours\": 0.29}, \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"completed_at\": \"2026-05-15T10:00:09.238Z\", \"hypothesis\": \"Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:03:06.876Z\", \"updated_at\": \"2026-05-17T02:58:19.490Z\", \"spec\": {\"hypothesis\": \"RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.\", \"plan_id\": \"exp-008\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"gpu\": \"cuda:2\", \"server\": \"gpu-5090-4x-2\", \"gpu_budget_hours\": 12, \"description\": \"RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.\", \"priority\": \"P1\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 42, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp008_re_n16/\", \"completed_at\": \"2026-05-14T12:28:39.268Z\", \"hypothesis\": \"RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:46:06.430Z\", \"updated_at\": \"2026-05-17T02:58:18.225Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"63407\", \"log_path\": \"output/exp001_n16_seed123_run.log\", \"submitted_at\": \"2026-05-14T12:46:06.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 551, \"data_path\": \"data/scierc/processed_data\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"checkpoint_path\": \"output/exp001_n16_seed123/\", \"wall_clock_seconds\": 2748.0, \"gpu_hours\": 0.76}, \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}, \"completed_at\": \"2026-05-14T13:31:54.232Z\", \"hypothesis\": \"SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples.\"}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:20.748Z\", \"updated_at\": \"2026-05-17T02:58:16.747Z\", \"spec\": {\"command\": \"bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_llama.yaml'\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"60970\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"submitted_at\": \"2026-05-14T12:43:09.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data\", \"data_count\": 1861, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"log_file\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"wall_clock_seconds\": 165.8, \"gpu_hours\": 0.05}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:43:50.977Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:45:54.952Z\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}, \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"hypothesis\": \"Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.\"}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:17.544Z\", \"updated_at\": \"2026-05-17T02:58:14.928Z\", \"spec\": {\"merged_model_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"pilot_command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot --num_test 9999 --collect_logprobs\", \"pilot_pid\": 71498, \"pilot_server\": \"autodl-5090\", \"pilot_started_at\": \"2026-05-14T21:36:00Z\", \"test_samples\": 1287}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T11:43:50.537Z\", \"finished_at\": \"2026-05-14T12:53:13.262Z\", \"training_hours\": 1.16}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:53:14.768981+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\", \"log_path\": \"output/exp003_wnut17_pilot/\", \"completed_at\": \"2026-05-14T13:40:20.979Z\", \"hypothesis\": \"WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.\"}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:41.067Z\", \"updated_at\": \"2026-05-17T02:58:12.996Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:05.416Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:05.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:10.317185+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=456 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.503Z\", \"updated_at\": \"2026-05-17T02:58:11.623Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:13.823Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:13.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:16.532801+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=123 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.867Z\", \"updated_at\": \"2026-05-17T02:58:10.171Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:18.988Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:19.577Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:21.528032+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}, \"hypothesis\": \"RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.\"}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:54:48.055Z\", \"updated_at\": \"2026-05-17T02:58:03.014Z\", \"spec\": {\"command\": \"python run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp007_llama_inference/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"75172\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_llama_inference.log\", \"submitted_at\": \"2026-05-14T13:54:47.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"description\": \"LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0, logprobs collected.\", \"wall_clock_seconds\": 1038.5, \"gpu_hours\": 0.29}, \"log_path\": \"output/exp007_llama_inference/\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:12:06.442Z\", \"hypothesis\": \"LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.\"}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:47:34.654Z\", \"updated_at\": \"2026-05-17T02:58:01.627Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_eval --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/wnut17\", \"data_count\": 1287, \"model_name\": \"qwen3-8b-wnut17-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:08:17.429Z\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}, \"hypothesis\": \"WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.\"}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:01:53.585Z\", \"updated_at\": \"2026-05-17T02:58:00.378Z\", \"spec\": {\"command\": \"python3 code/exp010_selection_curves.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2, output/exp_008_re_n16_v2, output/exp002_conll2003\", \"data_count\": \"551+397+3453 instances\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"description\": \"Best-of-N selection curves: F1 vs N for 7 signals across 3 datasets\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp010.log\", \"completed_at\": \"2026-05-14T15:02:22.638Z\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}, \"hypothesis\": \"Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.\"}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.628Z\", \"updated_at\": \"2026-05-17T02:57:59.595Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=456, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed456\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 456, \"gpu\": [\"cuda:2\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s456\", \"account\": \"root\", \"log_path\": \"output/exp_007_llama_seed456/run.log\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/\", \"completed_at\": \"2026-05-14T15:19:20.693Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}, \"hypothesis\": \"LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.157Z\", \"updated_at\": \"2026-05-17T02:57:58.879Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=123, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 123, \"gpu\": [\"cuda:1\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s123\", \"account\": \"root\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:19:43.424Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}, \"hypothesis\": \"LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:51.386Z\", \"updated_at\": \"2026-05-17T02:57:58.166Z\", \"spec\": {\"description\": \"RE N=16 on SciERC, seed=123, seed robustness test for relation extraction\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1, robust across seeds\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": [\"cuda:3\"], \"backend\": \"tmux\", \"tmux_session\": \"exp008_rs123\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_seed123/run.log\"}, \"log_path\": \"output/exp_008_re_seed123/run.log\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-14T15:21:39.591Z\", \"hypothesis\": \"RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.\"}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:02.350Z\", \"updated_at\": \"2026-05-17T02:57:57.324Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=42, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed42_v2\", \"gpu\": [\"cuda:1\"], \"pid\": \"78728\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed42_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:34.091Z\", \"log_path\": \"output/exp_001_seed42_v2/\", \"hypothesis\": \"SciERC NER seed=42 v2: primary seed baseline under corrected pipeline. Establishes canonical signal rankings (SJ>FK>LP) for NER with gold-filtering.\"}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:04.210Z\", \"updated_at\": \"2026-05-17T02:57:42.106Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=123, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC (seed robustness check)\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 123, \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed123_v2\", \"gpu\": [\"cuda:2\"], \"pid\": \"78733\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed123_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.076Z\", \"log_path\": \"output/exp_001_seed123_v2/\", \"hypothesis\": \"SciERC NER seed=123 v2: second seed for multi-seed validation. Establishes reproducibility of structural>surface signal ranking across random seeds.\"}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:06.296Z\", \"updated_at\": \"2026-05-17T02:57:41.178Z\", \"spec\": {\"description\": \"RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1 on SciERC full dataset\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2\", \"gpu\": [\"cuda:3\"], \"pid\": \"78737\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_n16_v2/run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.598Z\", \"log_path\": \"output/exp_008_re_n16_v2/\", \"hypothesis\": \"RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.\"}, \"exp_005_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:28:14.924Z\", \"updated_at\": \"2026-05-17T02:57:38.756Z\", \"spec\": {\"description\": \"Temperature sensitivity analysis: T=0.7 vs T=1.0 across 5 signals (SJ, FK, logprob, EM, voting_conf)\", \"command\": \"python code/analyze_exp005_v2_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/mvp_pilot_004 + output/mvp_pilot_005 + output/exp_012_logprob\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_005_v2_temperature/temperature_sensitivity_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:28:35.949Z\", \"hypothesis\": \"Selection F1 analysis v2: compute actual selection F1 (pick best sample by each signal) vs greedy and oracle. First evidence of correlation-selection gap under corrected pipeline.\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:30:02.348Z\", \"updated_at\": \"2026-05-17T02:57:36.914Z\", \"spec\": {\"command\": \"python3 code/exp_006_v2_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_{001_seed42,001_seed123,002_conll,008_re}_v2/\", \"data_count\": 4952, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_006_v2/exp_006_v2_results.json\", \"log_path\": \"output/exp_006_v2_run.log\", \"completed_at\": \"2026-05-14T15:30:32.474Z\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}, \"hypothesis\": \"Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.\"}, \"exp_004_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:31:40.554Z\", \"updated_at\": \"2026-05-17T02:57:35.012Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/analyze_exp004_v2_re_diagnostic.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/\"}, \"completed_at\": \"2026-05-14T15:32:04.966Z\", \"hypothesis\": \"N-ablation v2 (N=4,8,16,32): tests how sample count affects signal ρ and selection F1. Validates N-scaling curve for structural vs surface signals under corrected pipeline.\"}, \"exp_009_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:36:47.946Z\", \"updated_at\": \"2026-05-17T02:57:32.655Z\", \"spec\": {\"command\": \"python3 code/exp_009_v2_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis\", \"seed\": 42}, \"checkpoint_path\": \"output/exp_009_v2/results.json\", \"log_path\": \"output/exp_009_v2_run.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:37:18.311Z\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}, \"hypothesis\": \"Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.\"}, \"exp_016_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:39:07.501Z\", \"updated_at\": \"2026-05-17T02:57:30.726Z\", \"spec\": {\"command\": \"python code/exp_016_v2_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis_only\", \"seed\": 42, \"checkpoint_path\": \"output/exp_016_v2/\", \"log_path\": \"/tmp/exp016v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:39:34.478Z\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}, \"hypothesis\": \"Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.\"}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:38:55.569Z\", \"updated_at\": \"2026-05-17T02:57:23.336Z\", \"spec\": {\"hypothesis\": \"NER/RE N=16 seed=456 robustness test, third seed for 3-seed stability\", \"plan_id\": \"exp-001\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"metrics\": {\"full_rho_kappa_f1\": 0.3383, \"full_rho_sj_f1\": 0.2988, \"cond_rho_kappa_f1\": 0.233, \"cond_rho_sj_f1\": 0.3245, \"logprob_full_rho\": 0.3405, \"logprob_full_auroc\": 0.6694, \"logprob_cond_rho\": 0.0501, \"structural_gt_surface\": false}, \"note\": \"CRITICAL: Ran with --subtask joint instead of --subtask ner. seed42/seed123 v2 used --subtask ner. Results valid for joint-mode analysis but NOT comparable for NER 3-seed protocol. Need NER-only rerun.\", \"log_path\": \"output/exp_001_seed456_v2/run.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:12:14.682Z\", \"hypothesis\": \"SciERC joint NER+RE seed=456 v2: early pipeline version. Tests multi-seed stability of signal rankings on joint extraction task.\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:33:23.653Z\", \"updated_at\": \"2026-05-17T02:57:21.948Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation of structural consistency signals\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll\", \"command\": \"python code/run_llama_conll_infer.py\", \"server\": \"autodl-5090\", \"data_path\": \"conll2003 test\", \"data_count\": 3453, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"n_samples\": 8, \"temperature\": 1, \"description\": \"LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset validation)\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:55:33.476Z\", \"notes\": \"LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).\", \"hypothesis\": \"LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.\"}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:56.415Z\", \"updated_at\": \"2026-05-17T02:57:20.068Z\", \"spec\": {\"description\": \"WNUT-17 retrain: downsample gold-empty instances to ≤25%, fine-tune Qwen3-8B, inference N=16 T=1.0 with log-probs\", \"hypothesis\": \"After removing excess empty instances, structural consistency signals (SJ) will show stronger correlation on social media NER\", \"plan_id\": \"exp-003\", \"claim\": 1, \"model_name\": \"Qwen3-8B\", \"dataset\": \"WNUT-17 (downsampled)\", \"priority\": \"P0\", \"parent\": \"exp_003_ner_wnut17\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_wnut17.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json\", \"data_count\": 1637, \"seed\": 42, \"pid\": 92215, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\", \"downsampling\": \"empty instances 63.8% -> 25.0%, total 3394 -> 1637\", \"metrics\": {\"train_loss\": 0.105, \"eval_loss\": 0.0836, \"epochs\": 5, \"train_time_min\": 16.37, \"train_samples_per_sec\": 8.33}, \"note\": \"D045: Training succeeded (train_loss=0.105) but inference FAIL: 54% F1=0, SJ rho=0.062 (p=0.106). WNUT-17 abandoned — model capability insufficient on social media NER. Paper reports as Claim 3 (capability boundary) evidence.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:11:36.559Z\", \"hypothesis\": \"WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:13:00.414Z\", \"updated_at\": \"2026-05-17T02:57:18.227Z\", \"spec\": {\"hypothesis\": \"NER N=16 seed=456 robustness test (NER-only rerun, fixing subtask mismatch from exp_001_seed456_v2)\", \"plan_id\": \"exp-001\", \"parent\": \"exp_001_seed456_v2\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data\", \"metrics\": {\"sj_rho\": 0.384, \"structural_gt_surface\": true, \"structural_surface_delta\": 0.16}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2_ner/\"}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"pid\": 96161, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:52:01.372Z\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"SciERC NER seed=456 v2: corrected pipeline rerun with gold-filtering. Part of multi-seed validation protocol for NER signal ranking stability.\"}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:56:31.535Z\", \"updated_at\": \"2026-05-17T02:57:16.383Z\", \"spec\": {\"command\": \"python code/exp_009_v2_re_rerun.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_008_re_n16_v2/samples.jsonl\", \"data_count\": 397, \"model_name\": \"cpu_analysis\", \"seed\": 42, \"checkpoint_source\": \"exp_008_re_n16_v2\", \"checkpoint_path\": \"output/exp_009_v2_re_rerun/results.json\", \"log_path\": \"/tmp/re_rerun.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:56:58.168Z\", \"hypothesis\": \"Capability stratification v2 (RE rerun): corrected stratification analysis for RE with proper gold-filtering. Fixes early pipeline bug affecting RE quartile ρ values.\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:31:44.366Z\", \"updated_at\": \"2026-05-17T02:57:12.521Z\", \"spec\": {\"hypothesis\": \"LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.\", \"plan_id\": \"exp-007\", \"parent\": \"exp_007_llama_inference\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"eval_data\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_007_llama_n16/samples.jsonl\", \"log_path\": \"output/exp_007_llama_n16.log\", \"completed_at\": \"2026-05-14T19:03:39.163Z\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}, \"hypothesis\": \"LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.\"}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:19:35.318Z\", \"updated_at\": \"2026-05-17T02:56:57.283Z\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll_infer\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"data_count\": 3453, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16\", \"data_path\": \"data/conll2003\", \"pid\": 106997, \"n_samples\": 16, \"temperature\": 1, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16/all_signals_report.json\"}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:45:16.265Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-17T02:56:55.830Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}, \"hypothesis\": \"Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.\"}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T12:10:30.350Z\", \"updated_at\": \"2026-05-17T02:56:53.526Z\", \"completed_at\": \"2026-05-14T12:28:38.721Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6577, \"oracle_f1\": 0.8129, \"headroom\": 0.1553, \"rho_sj_full\": 0.3297, \"rho_fk_full\": 0.2578, \"rho_logprob_full\": 0.2866, \"rho_sj_cond\": 0.3394, \"rho_fk_cond\": 0.2721, \"rho_logprob_cond\": 0.2567, \"sj_beats_fk\": true, \"rho_advantage\": 0.0719}, \"re\": {\"greedy_f1\": 0.4312, \"oracle_f1\": 0.6737, \"headroom\": 0.2425, \"rho_sj_full\": 0.285, \"rho_fk_full\": 0.2372, \"rho_logprob_full\": 0.2626, \"rho_sj_cond\": 0.3525, \"rho_fk_cond\": 0.2614, \"rho_logprob_cond\": 0.1927, \"sj_beats_fk\": true, \"rho_advantage\": 0.0478}, \"verdict\": \"FAIL\"}}}, \"spec\": {\"hypothesis\": \"N=16 seed456 multi-seed robustness verification for SciERC NER+RE\", \"plan_id\": \"exp-001\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 456, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"174595\", \"log_path\": \"output/exp001_n16_seed456_run.log\", \"tmux_session\": \"exp_001_n16_seed456\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"metrics\": {\"instance_count\": 551, \"n_valid\": 529, \"n_gold_empty\": 22, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4098, \"rho_fk_ner\": 0.2723, \"rho_vc_ner\": 0.4449, \"rho_em_ner\": 0.3363, \"rho_lp_ner\": 0.2415, \"rho_sj_re\": 0.2835, \"rho_fk_re\": 0.2929, \"auroc_sj_ner\": 0.6823, \"auroc_fk_ner\": 0.6179, \"auroc_vc_ner\": 0.6981, \"auroc_em_ner\": 0.649, \"auroc_lp_ner\": 0.5885, \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}, \"log_path\": \"output/exp001_n16_seed456_run.log\", \"hypothesis\": \"SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering.\"}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:07.210Z\", \"updated_at\": \"2026-05-17T02:56:29.417Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (SciERC model on CoNLL data)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/conll2003\", \"seed\": 42, \"pid\": 179761, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset conll2003 --data_dir data/conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_scierc_to_conll\", \"data_count\": 3500}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_011_ood_scierc_to_conll/samples.jsonl\", \"log_path\": \"output/exp_011_ood_scierc_to_conll/report.json\", \"completed_at\": \"2026-05-15T11:47:47.953Z\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}, \"hypothesis\": \"Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.\"}, \"exp_qwen3_4b_scierc_finetune_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:25.512Z\", \"updated_at\": \"2026-05-17T02:56:24.418Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"227123\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"submitted_at\": \"2026-05-15T19:26:31.444Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 1668.8, \"gpu_hours\": 0.46}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 585, \"completed_steps\": 585, \"best_checkpoint\": \"checkpoint-400\", \"best_eval_loss\": 0.0898, \"epochs\": 5}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"completed_at\": \"2026-05-15T19:54:20.255Z\", \"hypothesis\": \"Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.\"}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:08.325Z\", \"updated_at\": \"2026-05-17T02:56:14.242Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (CoNLL model on SciERC data, joint NER+RE)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"data_path\": \"data/scierc/processed_data\", \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 181723, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset scierc --data_dir data/scierc/processed_data --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_conll_to_scierc\", \"data_count\": 551}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_011_ood_conll_to_scierc/samples.jsonl\", \"log_path\": \"output/exp_011_ood_conll_to_scierc/report.json\", \"completed_at\": \"2026-05-15T11:50:21.969Z\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}, \"hypothesis\": \"Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).\"}, \"exp_freeform_seed789_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:26.805Z\", \"updated_at\": \"2026-05-17T02:56:11.818Z\", \"spec\": {\"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v3.log\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed789/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:30:51.048Z\", \"metrics\": {\"n_instances\": 551, \"n_samples\": 8, \"parse_rate_pct\": 100, \"elapsed_seconds\": 229.7, \"freeform_ner_selection_gap\": 0.0028, \"freeform_re_selection_gap\": 0.0219, \"freeform_lp_std\": 0.0183, \"freeform_lp_range\": 0.054908, \"freeform_tied_pct\": 59, \"re_lp_flip_positive\": true, \"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88}, \"hypothesis\": \"Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.\"}, \"exp_freeform_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:29.851Z\", \"updated_at\": \"2026-05-17T02:56:09.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"216722\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789.log\", \"submitted_at\": \"2026-05-15T18:58:46.406Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92.2, \"gpu_hours\": 0.03}, \"notes\": \"Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:00:18.576Z\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4408, \"parse_rate_pct\": 100, \"elapsed_seconds\": 227.5}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6205, \"selected\": 0.6232, \"gap\": 0.0027}, \"selection_re\": {\"greedy\": 0.2909, \"selected\": 0.31, \"gap\": 0.0191}, \"logprob_variance\": {\"mean_std\": 0.0183, \"mean_range\": 0.054908, \"tied_pct\": 59}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.393995, \"auroc\": 0.734474}, \"FK\": {\"rho\": 0.312292, \"auroc\": 0.794384}, \"LP\": {\"rho\": 0.247096, \"auroc\": 0.677824}, \"EM\": {\"rho\": 0.320383, \"auroc\": 0.527033}, \"VC\": {\"rho\": 0.420625, \"auroc\": 0.768111}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.201746, \"auroc\": 0.574388}, \"FK\": {\"rho\": 0.2202, \"auroc\": 0.633014}, \"LP\": {\"rho\": 0.295765, \"auroc\": 0.687067}, \"EM\": {\"rho\": 0.103633, \"auroc\": 0.474737}, \"VC\": {\"rho\": 0.306868, \"auroc\": 0.642197}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88, \"tied_reduction_pp\": 0.7}}, \"hypothesis\": \"Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:48.842Z\", \"updated_at\": \"2026-05-17T02:56:09.256Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=456): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 456 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed456\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"gpu\": \"cuda:2\", \"tmux_session\": \"exp_freeform_seed456\", \"log_path\": \"results/exp_freeform_ablation_seed456/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed456\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4407, \"parse_rate_pct\": 99.98, \"elapsed_seconds\": 232.4}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6198, \"selected\": 0.6205, \"gap\": 0.0007}, \"selection_re\": {\"greedy\": 0.2908, \"selected\": 0.3108, \"gap\": 0.02}, \"logprob_variance\": {\"mean_std\": 0.018631, \"mean_range\": 0.056792, \"tied_pct\": 58.4}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.378498, \"auroc\": 0.707769}, \"FK\": {\"rho\": 0.286163, \"auroc\": 0.754779}, \"LP\": {\"rho\": 0.227089, \"auroc\": 0.672081}, \"EM\": {\"rho\": 0.319997, \"auroc\": 0.47789}, \"VC\": {\"rho\": 0.416853, \"auroc\": 0.756543}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.211331, \"auroc\": 0.572335}, \"FK\": {\"rho\": 0.259074, \"auroc\": 0.652998}, \"LP\": {\"rho\": 0.306382, \"auroc\": 0.70134}, \"EM\": {\"rho\": 0.1043, \"auroc\": 0.461641}, \"VC\": {\"rho\": 0.301507, \"auroc\": 0.628873}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.9, \"variance_ratio_range\": 0.91, \"tied_reduction_pp\": 1.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:12:29.413Z\", \"hypothesis\": \"Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-17T02:56:06.903Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\", \"log_path\": \"results/exp_freeform_ablation_seed123/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed123\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance_ratio_range\": 0.96, \"tied_reduction_pp\": 2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:29:48.939Z\", \"hypothesis\": \"Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:59:24.201Z\", \"updated_at\": \"2026-05-17T02:56:02.685Z\", \"spec\": {\"command\": \"python code/exp009_stratification_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp001_n16_seed42 + output/exp008_re_n16 + output/exp002_conll2003\", \"data_count\": 4555, \"model_name\": \"analysis_only\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp009_stratification_results.json\", \"log_path\": \"/tmp/exp009.log\", \"completed_at\": \"2026-05-14T14:59:46.463Z\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}, \"notes\": \"Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED.\", \"hypothesis\": \"Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.\"}, \"exp_023_lora_rank8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:59.501Z\", \"updated_at\": \"2026-05-17T02:55:50.540Z\", \"spec\": {\"hypothesis\": \"LoRA rank=8 ablation: does reducing rank from 32 to 8 significantly affect correlation-selection patterns?\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:2\", \"pid\": 288382, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp023_rank8_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8\", \"command\": \"CUDA_VISIBLE_DEVICES=2 llamafactory-cli train train_config_rank8.yaml\", \"trainable_params\": \"21.8M\", \"total_steps\": 585, \"estimated_runtime\": \"26min\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1018, \"eval_loss\": 0.0776, \"train_runtime\": \"28m45s\", \"ner_full\": {\"n\": 529, \"greedy_f1\": 0.6397, \"oracle_f1\": 0.7998, \"oracle_headroom\": 0.1601, \"degeneracy_rate\": 0.072, \"SJ_rho\": 0.3649, \"FK_rho\": 0.2838, \"VC_rho\": 0.394, \"EM_rho\": 0.2562, \"LP_rho\": 0.2105, \"SJ_auroc\": 0.689, \"FK_auroc\": 0.6002, \"VC_auroc\": 0.6886, \"EM_auroc\": 0.7265, \"LP_auroc\": 0.6054, \"sel_SJ\": 0.6306, \"sel_FK\": 0.6265, \"sel_VC\": 0.5919, \"sel_EM\": 0.6073, \"sel_LP\": 0.635}, \"ner_cond\": {\"n\": 477, \"SJ_rho\": 0.3056, \"FK_rho\": 0.1452, \"VC_rho\": 0.3191, \"EM_rho\": 0.3558, \"LP_rho\": 0.169}, \"re_full\": {\"n\": 397, \"greedy_f1\": 0.3712, \"oracle_f1\": 0.609, \"oracle_headroom\": 0.2378, \"degeneracy_rate\": 0.217, \"SJ_rho\": 0.2244, \"FK_rho\": 0.3448, \"VC_rho\": 0.3617, \"EM_rho\": 0.068, \"LP_rho\": 0.2737, \"SJ_auroc\": 0.7092, \"FK_auroc\": 0.6469, \"VC_auroc\": 0.7533, \"EM_auroc\": 0.7306, \"LP_auroc\": 0.6325, \"sel_SJ\": 0.3584, \"sel_FK\": 0.3498, \"sel_VC\": 0.3715, \"sel_EM\": 0.3291, \"sel_LP\": 0.3606}, \"re_cond\": {\"n\": 242, \"SJ_rho\": 0.3601, \"FK_rho\": 0.2343, \"VC_rho\": 0.3703, \"EM_rho\": 0.4613, \"LP_rho\": 0.1809}}, \"completed_at\": \"2026-05-16T11:22:34.576Z\", \"hypothesis\": \"LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_022_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:27.375Z\", \"updated_at\": \"2026-05-17T02:55:49.870Z\", \"hypothesis\": \"3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 789 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_022_seed789/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (qwen3-8b-scierc-merged-v2)\", \"seed\": 789, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_022_seed789/run.log\", \"gpu\": \"cuda:0\", \"pid\": 286743, \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_022_seed789\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:17.461Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_025_n32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:38:26.420Z\", \"updated_at\": \"2026-05-17T02:55:46.212Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_025_n32/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:39.849Z\", \"metrics\": {\"n_samples\": 32, \"degeneracy_pct\": 4, \"lp_range\": 0.0781, \"oracle_f1\": 0.8412, \"greedy_f1\": 0.6615, \"oracle_gap\": 0.1797, \"selection_f1_lp_delta\": 0.54, \"selection_f1_sj_delta\": 0.16, \"selection_f1_fk_delta\": 0.6, \"selection_f1_em_delta\": 0.68, \"selection_f1_vc_delta\": -5.21, \"best_signal\": \"EM\", \"best_delta\": 0.68, \"metric_space\": \"micro_f1_filtered_529inst\", \"note\": \"corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\"}, \"hypothesis\": \"N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_021_fewnerd_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:33:44.079Z\", \"updated_at\": \"2026-05-17T02:55:45.560Z\", \"hypothesis\": \"Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.\", \"spec\": {\"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"gpu_count\": 4, \"training_mode\": \"DDP\", \"checkpoint_path\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"log_path\": \"output/exp_021_inference/\"}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6177, \"train_loss\": 0.048, \"eval_loss\": 0.0275, \"train_runtime\": \"3h57m\", \"epochs\": 3, \"final_checkpoint\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"adapter_path\": \"output/exp_021_fewnerd_full/adapter_model.safetensors\", \"inference_instances\": 37648, \"inference_filtered\": 32565, \"inference_n_samples\": 8, \"greedy_macro_f1\": 0.7478, \"oracle_macro_f1\": 0.8719, \"headroom\": 0.124, \"zero_f1_rate\": 0.119, \"degeneracy_rate\": 0.101, \"lp_within_range_mean\": 0.0879, \"lp_within_range_median\": 0.0662, \"lp_global_rho\": 0.4215, \"lp_cond_rho\": 0.4225, \"sj_global_rho\": 0.3002, \"sj_cond_rho\": 0.2937, \"fk_global_rho\": 0.3132, \"fk_cond_rho\": 0.3093, \"em_global_rho\": 0.2871, \"em_cond_rho\": 0.271, \"vc_global_rho\": 0.3858, \"vc_cond_rho\": 0.3234, \"lp_selection_delta_pp\": 1.36, \"vc_selection_delta_pp\": -1.79, \"sj_selection_delta_pp\": -2.14, \"fk_selection_delta_pp\": -2.26, \"em_selection_delta_pp\": -3.85, \"lp_bootstrap_ci_95_pp\": [1.18, 1.53], \"lp_sample_auroc\": 0.5782, \"vc_sample_auroc\": 0.5354, \"fk_sample_auroc\": 0.521, \"sj_sample_auroc\": 0.5197, \"em_sample_auroc\": 0.5137, \"scenario\": \"A_partial\", \"note\": \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}, \"completed_at\": \"2026-05-16T22:04:16.683Z\", \"parent\": \"exp_020_fewnerd_smoke\"}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:36.569Z\", \"updated_at\": \"2026-05-17T02:55:35.391Z\", \"spec\": {\"hypothesis\": \"Comprehensive evaluation of all 5 confidence signals with extended metrics\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"exp_012_logprob_baseline\", \"method\": \"CPU-only analysis: 6 metrics x 5 signals x 2 subtasks (NER+RE)\", \"command\": \"python code/analyze_exp015_metrics_expansion.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:22:32.661Z\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}, \"notes\": \"RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.\", \"hypothesis\": \"Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.\"}, \"exp_020_fewnerd_smoke\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:25.272Z\", \"updated_at\": \"2026-05-16T16:33:59.109Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/ft_fewnerd_smoke\", \"log_path\": \"checkpoints/fewnerd_train.log\"}, \"hypothesis\": \"1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.031, \"total_steps\": 8236, \"training_time\": \"5h54m\", \"pilot_greedy_f1\": 0.8037, \"pilot_instances\": 200, \"merged_model_path\": \"checkpoints/qwen3-8b-fewnerd-merged\"}, \"completed_at\": \"2026-05-16T16:33:59.109Z\"}, \"exp_vc_lp_cascade_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:44:02.658Z\", \"updated_at\": \"2026-05-16T06:31:26.755Z\", \"hypothesis\": \"VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:26.755Z\"}, \"exp_tacred_re_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:43:59.002Z\", \"updated_at\": \"2026-05-16T06:31:25.273Z\", \"hypothesis\": \"TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:25.273Z\"}, \"exp_vc_quartile_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:48:35.263Z\", \"updated_at\": \"2026-05-16T05:00:36.736Z\", \"hypothesis\": \"VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.\", \"spec\": {\"command\": \"python vc_quartile_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp_002_conll_n8_seed42/samples.jsonl\", \"data_count\": 3682, \"model_name\": \"analysis_only (Qwen3-8B data)\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"artifacts/vc_quartile_analysis/results.json\", \"log_path\": \"artifacts/vc_quartile_analysis/report.md\", \"completed_at\": \"2026-05-16T05:00:30.439Z\", \"metrics\": {\"scierc_ner\": {\"Q1_lp_delta\": 0.016, \"Q2_lp_delta\": -0.006, \"Q3_lp_delta\": 0.02, \"Q4_lp_delta\": -0.004, \"Q4_mean_vc\": 0.921, \"Q1_headroom\": 0.169, \"Q4_headroom\": 0.048, \"overall_lp_delta\": 0.006, \"n\": 529}, \"scierc_re\": {\"Q1_lp_delta\": -0.036, \"Q2_lp_delta\": -0.021, \"Q3_lp_delta\": -0.022, \"Q4_lp_delta\": 0.04, \"Q4_mean_vc\": 0.894, \"Q1_headroom\": 0.211, \"Q4_headroom\": 0.145, \"overall_lp_delta\": -0.009, \"n\": 397}, \"conll_ner\": {\"Q1_lp_delta\": -0.037, \"Q2_lp_delta\": -0.005, \"Q3_lp_delta\": 0, \"Q4_lp_delta\": 0, \"overall_lp_delta\": -0.01, \"n\": 2756, \"note\": \"Q3/Q4 degenerate (VC=1.0, all samples identical)\"}, \"conclusion\": \"VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).\"}}, \"exp_llama3b_scierc_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:23.638Z\", \"updated_at\": \"2026-05-16T03:59:26.005Z\", \"hypothesis\": \"Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.2-3b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/review_round9_experiments/llama3b_scierc/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.2-3B-Instruct (LoRA r=32 SciERC fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/llama3.2-3b-scierc-merged\", \"log_path\": \"output/review_round9_experiments/llama3b_scierc/inference.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:59:16.198Z\", \"metrics\": {\"ner_full\": {\"SJ_rho\": 0.3754, \"FK_rho\": 0.2676, \"LP_rho\": 0.2662, \"EM_rho\": 0.3341, \"VC_rho\": 0.4602, \"SJ_auroc\": 0.7383, \"FK_auroc\": 0.6714, \"LP_auroc\": 0.633, \"EM_auroc\": 0.7763, \"VC_auroc\": 0.7429, \"n\": 529}, \"ner_cond\": {\"SJ_rho\": 0.3445, \"FK_rho\": 0.2125, \"LP_rho\": 0.2099, \"EM_rho\": 0.3952, \"VC_rho\": 0.3815, \"SJ_auroc\": 0.7292, \"FK_auroc\": 0.66, \"LP_auroc\": 0.6156, \"EM_auroc\": 0.7822, \"VC_auroc\": 0.7222, \"n\": 476}, \"greedy_f1\": 0.6267, \"oracle_f1\": 0.763, \"oracle_headroom\": 0.1363, \"selection_f1_SJ\": 0.6328, \"selection_f1_VC\": 0.6113, \"selection_f1_FK\": 0.6295, \"selection_f1_EM\": 0.6174, \"selection_f1_LP\": 0.6279, \"n_gold_empty\": 22, \"structural_beats_surface\": true, \"rho_advantage_SJ_over_FK\": 0.1078}}, \"exp_freeform_conll_4seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:17.133Z\", \"updated_at\": \"2026-05-16T03:04:49.550Z\", \"hypothesis\": \"Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.\", \"spec\": {\"command\": \"python run_freeform_conll.py --seed {42,123,456,789} --gpu {0,1,2,3} --n_samples 8 --temperature 1.0\", \"server\": \"autodl-4x5090\", \"data_path\": \"data/conll2003/test.jsonl\", \"data_count\": 3453, \"model_name\": \"checkpoints/qwen3-8b-conll2003-merged\", \"seed\": \"42,123,456,789\"}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"log_path\": \"output/review_round9_experiments/freeform_conll/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:04:40.278Z\", \"metrics\": {\"greedy_f1\": \"0.9035±0.0004\", \"oracle_f1\": \"0.9460±0.0023\", \"lp_range_median\": \"0.0581±0.0072\", \"rho_sj\": \"0.4606±0.0188\", \"rho_fk\": \"0.4372±0.0209\", \"rho_em\": \"0.4714±0.0168\", \"rho_vc\": \"0.4606±0.0138\", \"rho_lp\": \"0.3262±0.0120\", \"sel_f1_sj\": \"0.8994±0.0014\", \"sel_f1_vc\": \"0.9006±0.0026\", \"sel_f1_lp\": \"0.8958±0.0009\", \"seeds\": [42, 123, 456, 789], \"n_samples\": 8, \"temperature\": 1, \"instances\": 2756, \"gold_empty_filtered\": 697}}, \"exp_qwen3_4b_conll_merge_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:42.107Z\", \"updated_at\": \"2026-05-15T20:07:12.593Z\", \"hypothesis\": \"CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_merge_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA merged, ckpt-4200)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen3_4b_conll_finetune_resume (checkpoint-4200)\"}, \"checkpoint_path\": \"N/A - duplicate\", \"log_path\": \"N/A - duplicate\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate.\", \"completed_at\": \"2026-05-15T20:03:47.431Z\"}, \"exp_qwen3_4b_scierc_merge_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:43.332Z\", \"updated_at\": \"2026-05-15T20:04:15.433Z\", \"hypothesis\": \"SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"checkpoint_path\": \"N/A - superseded\", \"log_path\": \"N/A - superseded\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup.\", \"completed_at\": \"2026-05-15T20:04:15.433Z\"}, \"exp_qwen3_4b_scierc_finetune_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:45.518Z\", \"updated_at\": \"2026-05-15T19:39:04.438Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"226610\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v3.log\", \"submitted_at\": \"2026-05-15T19:24:55.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 849.0, \"gpu_hours\": 0.24}, \"conclusion\": \"failed\", \"notes\": \"OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。\", \"completed_at\": \"2026-05-15T19:39:04.438Z\"}, \"exp_qwen3_4b_conll_finetune_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:38:19.388Z\", \"updated_at\": \"2026-05-15T19:38:43.468Z\", \"hypothesis\": \"CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"hypothesis\": \"CoNLL2003 NER LoRA fine-tune with Qwen3-4B, resume from checkpoint-3800 to complete 5 epochs\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_conll2003_4b_resume.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"data/conll2003/llmfactory_train.json\", \"data_count\": 14042, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"resume_from\": \"checkpoint-3800\", \"lora_rank\": 32, \"lora_alpha\": 64, \"num_train_epochs\": 5, \"learning_rate\": 0.0002, \"batch_size\": \"2 x 8 grad_accum\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"best_checkpoint\": \"checkpoint-4200\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora/trainer_state.json\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.001136, \"eval_loss\": 0.0225, \"best_global_step\": 4200, \"best_metric_eval_loss\": 0.0225, \"total_steps\": 4390, \"epochs\": 5, \"train_runtime_sec\": 1185.8, \"train_samples_per_second\": 59.2, \"resumed_from_step\": 3800}, \"completed_at\": \"2026-05-15T19:38:43.468Z\"}, \"exp_qwen3_4b_scierc_finetune_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:03:49.204Z\", \"updated_at\": \"2026-05-15T19:24:32.466Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": \"219830\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v2.log\", \"submitted_at\": \"2026-05-15T19:05:31.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 1861, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/\", \"wall_clock_seconds\": 1122.6, \"gpu_hours\": 0.31}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:24:14.124Z\", \"notes\": \"PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。\"}, \"exp_qwen3_4b_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T17:18:35.501Z\", \"updated_at\": \"2026-05-15T19:10:24.822Z\", \"hypothesis\": \"Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:45:42.215Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-15T18:45:43.672Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:45:49.686191+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_conll2003_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/conll2003\", \"data_count\": 14041, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"log_path\": \"checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"lora_config\": {\"trainable_params\": \"66M / 4.09B (1.62%)\", \"target_modules\": \"q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj\", \"epochs\": 5, \"batch_size\": 16, \"total_steps\": 4390, \"enable_thinking\": false}}, \"conclusion\": \"success\", \"notes\": \"Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.\", \"metrics\": {\"final_loss\": 0.0086, \"total_steps_completed\": 3920, \"total_steps_target\": 4390, \"epochs_completed\": 4.46, \"epochs_target\": 5, \"best_checkpoint\": \"checkpoint-3800\", \"note\": \"Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.\"}}, \"exp_freeform_seed789_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:02:03.813Z\", \"updated_at\": \"2026-05-15T19:06:44.537Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"218882\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v2.log\", \"submitted_at\": \"2026-05-15T19:02:03.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Multi-seed free-form ablation (seed=789): third seed for 3-seed mean±σ statistical significance. Verify RE LP flip and NER gap stability.\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 789, \"wall_clock_seconds\": 274.9, \"gpu_hours\": 0.08}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:06:37.887Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:06:38.388Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:06:53.109123+00:00\"}]}}, \"exp_qwen3_4b_scierc_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:58.948Z\", \"updated_at\": \"2026-05-15T19:03:05.505Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"218258\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune.log\", \"submitted_at\": \"2026-05-15T19:00:10.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 175.3, \"gpu_hours\": 0.05}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:03:05.505Z\"}, \"exp_lp_t07_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:12.094Z\", \"updated_at\": \"2026-05-15T16:30:35.531Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_lp_t07_scierc\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (LoRA fine-tuned on SciERC, ft_002_v2 merged)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hyperparams\": {\"n_samples\": 8, \"temperature\": 0.7, \"max_tokens\": 1024}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:28:29.563Z\"}, \"exp_lp_scierc_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:06.918Z\", \"updated_at\": \"2026-05-15T16:03:13.881Z\", \"hypothesis\": \"LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 \\\"LP compression is model/task intrinsic\\\" claim。对比 T=1.0 的 LP range 分布。\", \"spec\": {\"command\": \"python run_sc_ie.py --dataset scierc --subtask ner --model qwen --n_samples 8 --temperature 0.7 --use_logprob --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"196993\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/\", \"submitted_at\": \"2026-05-15T15:35:31.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/report.json\", \"wall_clock_seconds\": 1206.2, \"gpu_hours\": 0.34}, \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.662, \"ner_oracle_f1\": 0.764, \"ner_headroom_pp\": 10.2, \"ner_rho_sj_full\": 0.365, \"ner_rho_sj_cond\": 0.363, \"ner_rho_fk_full\": 0.289, \"ner_rho_fk_cond\": 0.255, \"lp_rho_full\": 0.249, \"lp_rho_cond\": 0.185, \"ner_rho_advantage\": 0.076, \"zero_f1_pct\": 11, \"full_n\": 529, \"cond_n\": 477, \"verdict\": \"success_supports_LP_compression_claim\"}, \"completed_at\": \"2026-05-15T15:55:37.889Z\"}, \"exp_re_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:40.607Z\", \"updated_at\": \"2026-05-15T15:55:41.890Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed456\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"199161\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/\", \"submitted_at\": \"2026-05-15T15:40:59.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/report.json\", \"wall_clock_seconds\": 882.3, \"gpu_hours\": 0.25}, \"hypothesis\": \"SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.664, \"ner_oracle_f1\": 0.775, \"ner_headroom_pp\": 11.1, \"ner_rho_sj_cond\": 0.283, \"ner_rho_fk_cond\": 0.145, \"re_greedy_f1\": 0.417, \"re_oracle_f1\": 0.581, \"re_headroom_pp\": 16.3, \"re_rho_sj_cond\": 0.315, \"re_rho_fk_cond\": 0.123, \"re_zero_f1_pct\": 45.3, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:41.890Z\"}, \"exp_re_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:38.271Z\", \"updated_at\": \"2026-05-15T15:55:40.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed123\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199021\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/\", \"submitted_at\": \"2026-05-15T15:40:58.073Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/report.json\", \"wall_clock_seconds\": 881.9, \"gpu_hours\": 0.24}, \"hypothesis\": \"SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.663, \"ner_oracle_f1\": 0.786, \"ner_headroom_pp\": 12.3, \"ner_rho_sj_cond\": 0.404, \"ner_rho_fk_cond\": 0.182, \"re_greedy_f1\": 0.42, \"re_oracle_f1\": 0.593, \"re_headroom_pp\": 17.3, \"re_rho_sj_cond\": 0.277, \"re_rho_fk_cond\": 0.063, \"re_zero_f1_pct\": 43.6, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:40.000Z\"}, \"exp_017_llama_conll_n8_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:29:34.595Z\", \"updated_at\": \"2026-05-15T15:46:22.722Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"195927\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"submitted_at\": \"2026-05-15T15:31:17.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 881.3, \"gpu_hours\": 0.24}, \"hypothesis\": \"LLaMA CoNLL N=8 T=0.7 防御性实验：填补\\\"LLaMA 仅在 SciERC 上测过\\\"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。\", \"parent\": \"exp_017_llama_conll\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T15:31:15.772Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"finished_at\": \"2026-05-15T15:40:02.605Z\", \"training_hours\": 0.15}, \"pid\": \"195927\", \"log_path\": \"/root/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:40:08.277684+00:00\"}]}, \"metrics\": {\"n_valid\": 2756, \"greedy_f1\": 0.9242, \"oracle_f1\": 0.9391, \"lp_range_median\": 1.1e-05, \"lp_tied_fraction_005\": 0.9579, \"signals\": {\"SJ\": {\"rho\": 0.3934, \"auroc\": 0.6506}, \"FK\": {\"rho\": 0.3879, \"auroc\": 0.6488}, \"VC\": {\"rho\": 0.375, \"auroc\": 0.6551}, \"EM\": {\"rho\": 0.3888, \"auroc\": 0.6494}, \"LP\": {\"rho\": 0.2951, \"auroc\": 0.7509}}, \"selection_f1\": {\"SJ\": 0.9247, \"FK\": 0.9254, \"VC\": 0.9264, \"EM\": 0.9255, \"LP\": 0.9248}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"completed_at\": \"2026-05-15T15:45:59.311Z\"}, \"exp008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"53600\", \"log_path\": \"~/runs/struct_self_consist_ie/exp008_re_n16.log\", \"submitted_at\": \"2026-05-14T12:15:14.917Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)\", \"wall_clock_seconds\": 87984.9, \"gpu_hours\": 24.44}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:41:39.774Z\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:48.078Z\", \"updated_at\": \"2026-05-15T12:41:32.192Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed456 && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs 2>&1 | tee output/exp001_n16_seed456/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"50302\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed456.log\", \"submitted_at\": \"2026-05-14T12:12:41.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 88131.0, \"gpu_hours\": 24.48}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:32.192Z\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:45.739Z\", \"updated_at\": \"2026-05-15T12:41:31.168Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed123 && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"48530\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed123.log\", \"submitted_at\": \"2026-05-14T12:09:45.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only, 551 instances on autodl-5090)\", \"wall_clock_seconds\": 88305.5, \"gpu_hours\": 24.53}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:31.168Z\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:44:31.348Z\", \"updated_at\": \"2026-05-15T12:41:30.065Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"62170\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log\", \"submitted_at\": \"2026-05-14T12:44:31.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86219.0, \"gpu_hours\": 23.95}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:30.065Z\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:47.915Z\", \"updated_at\": \"2026-05-15T12:41:29.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"61812\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log\", \"submitted_at\": \"2026-05-14T12:44:06.059Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86243.0, \"gpu_hours\": 23.96}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:29.068Z\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:21.510Z\", \"updated_at\": \"2026-05-15T12:41:27.410Z\", \"spec\": {\"description\": \"Fine-tune LLaMA-3.1-8B on SciERC + NER pilot (N=8, T=0.7). Model-agnostic validation.\", \"hypothesis\": \"SJ advantage is model-agnostic, not Qwen3-specific\", \"plan_id\": \"exp-007\", \"claim\": 1, \"model_name\": \"llama-3.1-8b-instruct (new fine-tune)\", \"dataset\": \"SciERC\", \"priority\": \"P0\", \"failure_reason\": \"Superseded by exp_007_ner_multi_model + exp_007_llama_inference (completed on autodl-5090)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_007_llama_inference (DONE)\", \"notes\": \"Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:27.410Z\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:25:56.211Z\", \"updated_at\": \"2026-05-15T12:41:26.419Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"57524\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log\", \"submitted_at\": \"2026-05-14T12:25:56.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_002_ner_conll2003 (completed on autodl-5090)\", \"wall_clock_seconds\": 87330.3, \"gpu_hours\": 24.26}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_002_ner_conll2003 (DONE)\", \"notes\": \"Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:26.419Z\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:08:54.395Z\", \"updated_at\": \"2026-05-15T12:40:53.995Z\", \"spec\": {\"hypothesis\": \"Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision\", \"plan_id\": \"exp-019\", \"model_name\": \"microsoft/deberta-v3-large\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl\", \"data_count\": 551, \"seed\": 42}, \"conclusion\": \"killed\", \"notes\": \"Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\", \"completed_at\": \"2026-05-15T12:40:53.995Z\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:15.150Z\", \"updated_at\": \"2026-05-15T06:22:40.868Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=456, max_tokens=1024. Fresh inference (D066 decision: replace exp_007 re-analysis with independent replication).\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T06:08:05.756Z\", \"notes\": \"SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:57.682Z\", \"updated_at\": \"2026-05-15T01:20:53.108Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.\", \"parent\": \"exp_002_conll_n16\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:53.108Z\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:59.685Z\", \"updated_at\": \"2026-05-15T01:20:52.194Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.\", \"parent\": \"exp_007_llama_n16\", \"model_name\": \"llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:52.194Z\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-15T01:20:49.812Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed123.\", \"parent\": \"exp_001_seed123_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed123_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:49.812Z\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:55.975Z\", \"updated_at\": \"2026-05-15T01:20:48.914Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed456.\", \"parent\": \"exp_001_seed456_v2_ner\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:48.914Z\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:52.571Z\", \"updated_at\": \"2026-05-14T22:28:53.686Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed42.\", \"parent\": \"exp_001_seed42_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed42_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"output/exp_001_seed42_v2_r1024\", \"log_path\": \"output/exp_001_seed42_v2_r1024/run.log\", \"completed_at\": \"2026-05-14T22:27:43.836Z\"}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.987Z\", \"updated_at\": \"2026-05-14T20:24:45.875Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 456}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s456/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s456/all_signals_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:24:45.875Z\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.084Z\", \"updated_at\": \"2026-05-14T19:43:06.607Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:43:06.607Z\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:10.852Z\", \"updated_at\": \"2026-05-14T17:51:43.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"62585\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_008_re_n16_full.log\", \"submitted_at\": \"2026-05-14T12:45:10.764Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18393.2, \"gpu_hours\": 5.11}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)\", \"completed_at\": \"2026-05-14T17:51:43.957Z\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:29.393Z\", \"updated_at\": \"2026-05-14T12:42:58.393Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs\", \"server\": \"gpu-5090-4x-2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp001_n16_seed123/\", \"completed_at\": \"2026-05-14T12:28:38.104Z\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:15:23.771Z\", \"updated_at\": \"2026-05-14T12:42:55.931Z\", \"spec\": {\"command\": \"python code/analyze_exp016_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"N/A (CPU-only analysis)\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"pilot_004\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp016_signal_ensemble/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:15:53.341Z\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:10.898Z\", \"updated_at\": \"2026-05-14T12:42:49.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"54357\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log\", \"submitted_at\": \"2026-05-14T12:15:46.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:43:48.643Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:55:45.664Z\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:39:53.226Z\", \"updated_at\": \"2026-05-14T12:40:17.202Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-lora-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged\", \"log_path\": \"/tmp/pilot_conll2003.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:40:08.402Z\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:15.223Z\", \"updated_at\": \"2026-05-14T12:27:35.413Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test 99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"58208\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"submitted_at\": \"2026-05-14T12:27:35.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T11:43:49.959Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"completed_at\": \"2026-05-14T12:18:04.097Z\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:49:44.497Z\", \"updated_at\": \"2026-05-14T11:50:24.620Z\", \"spec\": {\"hypothesis\": \"RE diagnostic: per-relation-type breakdown reveals which types drive low RE rho; error propagation and threshold sensitivity clarify the gap between NER and RE consistency signals\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-relation-type SJ/FK/voting rho, error propagation classification, threshold sensitivity, bootstrap CI, Fisher z-test NER vs RE\", \"command\": \"python3 code/analyze_exp004_re_diagnostic.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic/\", \"checkpoint_source\": \"mvp_pilot_004\", \"eval_data\": \"scierc_test_551\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:50:04.662Z\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:45:16.360Z\", \"updated_at\": \"2026-05-14T11:45:38.570Z\", \"spec\": {\"hypothesis\": \"Temperature sensitivity: systematic comparison of T=0.7 vs T=1.0 on all 5 confidence signals\", \"method\": \"CPU-only analysis from checkpoint metrics (pilot_004 T=1.0, pilot_005 T=0.7, exp_012/013/014)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"server\": \"local\", \"seed\": 42, \"parent\": \"mvp_pilot_004,mvp_pilot_005\", \"command\": \"python3 analyze_exp005_temperature.py\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"log_path\": \"N/A\", \"checkpoint_source\": \"pilot_004+pilot_005 checkpoint metrics\", \"eval_data\": \"SciERC test set (n=551)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:45:38.570Z\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:21.203Z\", \"updated_at\": \"2026-05-14T11:33:30.085Z\", \"spec\": {\"hypothesis\": \"Entity-level majority voting confidence beats SJ as correlation signal\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-entity voting across N=8 samples, consensus construction, confidence = mean voting rate\", \"command\": \"python code/analyze_entity_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:09.468Z\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:18.753Z\", \"updated_at\": \"2026-05-14T11:33:22.644Z\", \"spec\": {\"hypothesis\": \"Exact-match voting rate correlates with F1\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Count exact-match duplicates across N=8 samples\", \"command\": \"python code/analyze_exact_match_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T11:18:09.026Z\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:16.166Z\", \"updated_at\": \"2026-05-14T11:13:30.240Z\", \"spec\": {\"hypothesis\": \"Log-probability baseline: mean sequence log-prob correlates with F1 as well as or better than SJ\", \"model_name\": \"ft_002_v2 (qwen3-8b-scierc-merged-v2)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"vLLM forward pass for log-probs + Spearman rho + AUROC + Kendall tau\", \"command\": \"python3 code/extract_logprobs.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/logprob_analysis.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:06:42.542Z\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:47:06.597Z\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"spec\": {\"hypothesis\": \"RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 397, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1\", \"command\": \"python3 code/analyze_component_wise_re.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_analysis.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}, \"completed_at\": \"2026-05-14T09:22:26.155Z\"}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:51:38.203Z\", \"updated_at\": \"2026-05-14T09:10:40.918Z\", \"spec\": {\"hypothesis\": \"With improved RE quality (F1=41.8%), structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa, reaching rho_sj >= 0.40 on RE\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 31041, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\"}, \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:10:40.918Z\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:28:40.861Z\", \"updated_at\": \"2026-05-14T08:51:32.405Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) with OOM fix improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:1\", \"pid\": 24947, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002v2_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_v2.yaml\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}, \"completed_at\": \"2026-05-14T08:51:32.405Z\"}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:16.991Z\", \"updated_at\": \"2026-05-14T08:48:14.040Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"Qwen3-8B-SciERC-LoRA (ft_001)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + gold-empty filter + conditional rho\", \"gpu\": \"cuda:0\", \"note\": \"Rerun of mvp_pilot_001 which crashed silently\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-lora --data_dir data/scierc --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 512 --output_dir output/mvp_pilot_001 --num_test 551 --seed 42 --tensor_parallel 1\", \"failure_reason\": \"Worker used LoRA adapter path instead of merged model path; vLLM cannot load LoRA adapter directly\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:48:14.040Z\"}, \"ft_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:18.640Z\", \"updated_at\": \"2026-05-14T08:28:00.590Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, relation direction hint\", \"command\": \"llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml\", \"gpu\": \"cuda:1\", \"pid\": 19666, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"total_steps\": 585, \"trainable_params\": \"87.3M\", \"estimated_runtime\": \"29min\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:02:30.390Z\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:04:28.030Z\", \"updated_at\": \"2026-05-14T08:27:58.182Z\", \"spec\": {\"hypothesis\": \"Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"method\": \"LoRA r=16 alpha=32\", \"framework\": \"LLaMA Factory 0.9.4\", \"command\": \"sft training qwen3-8b on scierc with lora\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log\", \"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"epoch\": 3, \"train_runtime\": \"0:17:49\", \"note\": \"gate0: NER PASS 60.4% / RE FAIL 33.8%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:30:32.889Z\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:21:09.847Z\", \"updated_at\": \"2026-05-14T08:21:44.983Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003 --num_test 551 --seed 42 --tensor_parallel 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged\", \"seed\": 42}, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/mvp_pilot_003.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T08:21:30.319Z\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:16.313Z\", \"updated_at\": \"2026-05-14T08:05:34.348Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"qwen3-8b-scierc-merged\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T07:52:47.006Z\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 171, \"total\": 171, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4781}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QXvEm9aWFSQStaFscvbF3Q`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -maxdepth 3 -type d -iname \"*fewnerd*n16*\" -o -type d -iname \"*fewnerd*n_16*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "42b9de6c-e8bb-43e3-9165-06515f60bc14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiRU77rwQHZicJFqJvXM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1038
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

_source line 12 · 2026-05-19T07:57:35.507Z_

<details><summary>↩ Tool result · `toolu_01QXvEm9aWFSQStaFscvbF3Q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "4c0d1c6b-e341-4972-98bf-552e45761f9e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LPwE2HQoeL3QjNstTjLDPP`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/code/ -name \"*selection_gap*\" -o -name \"*plot*gap*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "4ae2f47b-2f6c-4f3b-aca2-6d025b26d08d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiRU77rwQHZicJFqJvXM94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 25221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1038
      },
      "output_tokens": 30,
      "service_tier": "standard",
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

_source line 14 · 2026-05-19T07:57:36.048Z_

<details><summary>↩ Tool result · `toolu_01LPwE2HQoeL3QjNstTjLDPP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_1024.py\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_3seed.py\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_n8.py\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_single.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8118677a-2c61-4757-8070-0b8d0a7b90a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_1024.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_3seed.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_n8.py\\\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_single.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_1024.py\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_3seed.py\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_n8.py\\n/root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_single.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 15_

Found `exp_027_fewnerd_n16` output dir and several plot scripts. Now I'll dig into all three in parallel: registry data for fewnerd experiments, the exp_027 output contents, and the plot scripts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "21ce88e5-9c22-49c7-b996-60a097c7c837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RihQ478HfRpZgiypaMzZEq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 26259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1316
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

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_015m3rum4qZMnSTQyRS5scaY`</summary>

```json
{
  "description": "Registry FewNERD N16 lookup",
  "prompt": "Parse the registry JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt\n\nThis file is JSON with schema: {result: string}. The \"result\" field is itself a JSON string containing an array of experiment objects.\n\nI need ALL experiments whose exp_id or name contains \"fewnerd\" (case-insensitive). For each matching experiment, return the FULL object including all fields — especially: exp_id, status, conclusion, metrics, config, notes, and any other fields present. Quote all numeric values verbatim.\n\nAlso search for any experiment with \"n16\" or \"n_16\" in its name/id.\n\nUse jq or python to parse. Return the complete data for all matching experiments.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "29d258d0-4dbf-4b59-8daf-f8d2b23b7506",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RihQ478HfRpZgiypaMzZEq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 26259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1316
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Registry FewNERD N16 lookup",
  "task_type": "local_agent",
  "prompt": "Parse the registry JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt\n\nThis file is JSON with schema: {result: string}. The \"result\" field is itself a JSON string containing an array of experiment objects.\n\nI need ALL experiments whose exp_id or name contains \"fewnerd\" (case-insensitive). For each matching experiment, return the FULL object including all fields — especially: exp_id, status, conclusion, metrics, config, notes, and any other fields present. Quote all numeric values verbatim.\n\nAlso search for any experiment with \"n16\" or \"n_16\" in its name/id.\n\nUse jq or python to parse. Return the complete data for all matching experiments.",
  "uuid": "56ded0c3-6b0b-4e66-9680-e85473f68924",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


## Round 1

## Round 1

139 recorded events


### User

_source line 18 · 2026-05-19T07:57:44.552Z_

Parse the registry JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt

This file is JSON with schema: {result: string}. The "result" field is itself a JSON string containing an array of experiment objects.

I need ALL experiments whose exp_id or name contains "fewnerd" (case-insensitive). For each matching experiment, return the FULL object including all fields — especially: exp_id, status, conclusion, metrics, config, notes, and any other fields present. Quote all numeric values verbatim.

Also search for any experiment with "n16" or "n_16" in its name/id.

Use jq or python to parse. Return the complete data for all matching experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "22f2e590-6567-404f-8e3d-1c517910f134"
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jbq7PBdFKYfFefPixp1efz`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8a47175c-028b-411f-b196-6a369f946b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RihQ478HfRpZgiypaMzZEq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 26259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1316
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FMhuQz2YY8SgMp1Uu9EbxY`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_3seed.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8ccafbbc-3e91-42e6-9861-cd55280feaeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RihQ478HfRpZgiypaMzZEq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 26259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1316
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

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Running Parse registry JSON and filter experiments matching fewnerd/n16/n_16",
  "usage": {
    "total_tokens": 16016,
    "tool_uses": 1,
    "duration_ms": 6645
  },
  "last_tool_name": "Bash",
  "uuid": "1474b3d9-853b-4930-b909-17eea0e63580",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01M8UkEAsoG5oE7L3V7tWvw8`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt | python3 -c \"\nimport json, sys, re\n\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\n\nmatches = []\nfor exp in result:\n    exp_str = json.dumps(exp).lower()\n    exp_id = str(exp.get('exp_id', '')).lower()\n    name = str(exp.get('name', '')).lower()\n    \n    # Check for fewnerd, n16, n_16 in exp_id or name\n    if any(kw in exp_id or kw in name for kw in ['fewnerd', 'n16', 'n_16']):\n        matches.append(exp)\n\nprint(json.dumps(matches, indent=2, ensure_ascii=False))\nprint(f'\\n--- Total matching experiments: {len(matches)} ---')\n\"\n",
  "description": "Parse registry JSON and filter experiments matching fewnerd/n16/n_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c2a7e435-ceb9-4314-b99a-388dc3b8616e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142taEVV4JtfX9i5ysqYeKN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15939,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 74,
      "service_tier": "standard",
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

_source line 23 · 2026-05-19T07:57:51.512Z_

<details><summary>↩ Tool result · reported error · `toolu_01M8UkEAsoG5oE7L3V7tWvw8`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    exp_id = str(exp.get('exp_id', '')).lower()
                 ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8061c6ae-b595-44db-892b-026c7b79579e",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 10, in &lt;module>\n    exp_id = str(exp.get('exp_id', '')).lower()\n                 ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---


### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Running Inspect the structure of the parsed registry JSON",
  "usage": {
    "total_tokens": 17328,
    "tool_uses": 2,
    "duration_ms": 13951
  },
  "last_tool_name": "Bash",
  "uuid": "2f18d885-374d-4717-91ce-0d8cfd941e64",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y6thA1cS5tnNve6kUysMZm`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nprint(f'Type of result: {type(result)}')\nif isinstance(result, list):\n    print(f'Length: {len(result)}')\n    for i, item in enumerate(result[:3]):\n        print(f'Item {i} type: {type(item)}')\n        if isinstance(item, str):\n            print(f'  Value: {item[:200]}')\n        elif isinstance(item, dict):\n            print(f'  Keys: {list(item.keys())}')\nelif isinstance(result, dict):\n    print(f'Keys: {list(result.keys())}')\n    for k in list(result.keys())[:5]:\n        v = result[k]\n        print(f'  {k}: type={type(v)}')\n        if isinstance(v, list) and len(v) > 0:\n            print(f'    First item type: {type(v[0])}')\n            if isinstance(v[0], dict):\n                print(f'    First item keys: {list(v[0].keys())}')\n\"\n",
  "description": "Inspect the structure of the parsed registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "3044355b-cbfb-4bf4-832e-adacc79ef8b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2gPheypPYC4nBmveepk7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 15939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1312,
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

_source line 26 · 2026-05-19T07:57:58.602Z_

<details><summary>↩ Tool result · `toolu_01Y6thA1cS5tnNve6kUysMZm`</summary>

```text
Type of result: &lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']
  success: type=&lt;class 'bool'>
  data: type=&lt;class 'dict'>
  error: type=&lt;class 'NoneType'>
  metadata: type=&lt;class 'dict'>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "f200303a-3daa-4acd-874a-03bd4d15a339"
}
```

</details>

---


### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Running Inspect data structure inside the registry",
  "usage": {
    "total_tokens": 17967,
    "tool_uses": 3,
    "duration_ms": 19445
  },
  "last_tool_name": "Bash",
  "uuid": "e9abd871-e730-4607-bbfd-6f6639b7e5cf",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_0125Lbi1J176z85yGcbvjNvP`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\ndata = result['data']\nprint(f'Data keys: {list(data.keys())}')\nfor k in data.keys():\n    v = data[k]\n    print(f'  {k}: type={type(v).__name__}, ', end='')\n    if isinstance(v, list):\n        print(f'len={len(v)}')\n        if len(v) > 0:\n            print(f'    First item type: {type(v[0]).__name__}')\n            if isinstance(v[0], dict):\n                print(f'    First item keys: {list(v[0].keys())}')\n    elif isinstance(v, dict):\n        print(f'keys={list(v.keys())[:10]}')\n    else:\n        print(f'value={v}')\n\"\n",
  "description": "Inspect data structure inside the registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "d19b8a45-ba02-415b-bef7-fb2803b7b0f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MT4pBZ4dJDua1P9vk6x1gU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 568,
      "cache_read_input_tokens": 17251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 568,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-19T07:58:04.161Z_

<details><summary>↩ Tool result · `toolu_0125Lbi1J176z85yGcbvjNvP`</summary>

```text
Data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, keys=['exp_qwen25_32b_fewnerd', 'exp_qwen25_7b_fewnerd', 'exp_wnut17_qwen25_7b', 'exp_qwen25_14b_fewnerd', 'exp_qwen25_72b_zeroshot', 'exp_llama_fewnerd_inference', 'exp_entity_construction', 'exp_lp_alignment_gating', 'exp_selective_prediction', 'exp_llama_fewnerd_lora']
  count: type=int, value=171
  total: type=int, value=171
  baseline: type=NoneType, value=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c7a4c424-b98d-4937-8550-6aa073fb34e6"
}
```

</details>

---


### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Running Filter experiments matching fewnerd/n16/n_16 from the dict-keyed experiments",
  "usage": {
    "total_tokens": 18642,
    "tool_uses": 4,
    "duration_ms": 26101
  },
  "last_tool_name": "Bash",
  "uuid": "800403fa-398f-4b86-9ff5-1c69c82c4489",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01MHTpt9hdtBCeoUSviEafvf`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\n# experiments is a dict keyed by exp_id\nmatches = {}\nfor exp_id, exp_data in experiments.items():\n    exp_id_lower = exp_id.lower()\n    # Also check name if present\n    name = ''\n    if isinstance(exp_data, dict):\n        name = str(exp_data.get('name', '')).lower()\n    elif isinstance(exp_data, list):\n        # might be a list of sub-experiments\n        pass\n    \n    combined = exp_id_lower + ' ' + name\n    if any(kw in combined for kw in ['fewnerd', 'n16', 'n_16']):\n        matches[exp_id] = exp_data\n\nprint(json.dumps(matches, indent=2, ensure_ascii=False))\nprint(f'\\n--- Total matching experiment keys: {len(matches)} ---')\n\" 2>&1 | head -50\n",
  "description": "Filter experiments matching fewnerd/n16/n_16 from the dict-keyed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "75142da9-6bc2-4a47-a013-649cc6fd06a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R7bZJrBJPYt7AN2pNYA5FF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 17819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 602,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-19T07:58:10.745Z_

<details><summary>↩ Tool result · `toolu_01MHTpt9hdtBCeoUSviEafvf`</summary>

```text
{
  "exp_qwen25_32b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:25.428Z",
    "updated_at": "2026-05-19T07:52:18.591Z",
    "hypothesis": "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.",
    "server": "autodl-5090",
    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
    "account": "root",
    "reproduce": {
      "server": "autodl-5090",
      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
      "started_at": "2026-05-19T06:47:41.246Z"
    },
    "notes": "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."
  },
  "exp_qwen25_7b_fewnerd": {
    "status": "QUEUED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:41:43.121Z",
    "updated_at": "2026-05-19T07:48:40.207Z",
    "hypothesis": "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."
  },
  "exp_qwen25_14b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:31.620Z",
    "updated_at": "2026-05-19T06:47:43.938Z",
    "hypothesis": "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.",
    "server": "autodl-5090-c",
    "gpu": "cuda:0,cuda:1",
    "account": "root",
    "reproduce": {
      "server": "autodl-5090-c",
      "gpu": "cuda:0,cuda:1",
      "started_at": "2026-05-19T06:47:43.938Z"
    }
  },
  "exp_llama_fewnerd_inference": {
    "status": "DONE",
    "retry_count": 0,
    "created_at": "2026-05-19T02:18:49.938Z",
    "updated_at": "2026-05-19T03:15:04.486Z",
    "hypothesis": "LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.",
    "parent": "exp_llama_fewnerd_lora",
    "spec": {
      "command": "bash code/run_llama_fewnerd_inference.sh",
      "server": "autodl-5090",
      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b082b6dc-56fb-4c49-8291-c1f225098f99"
}
```

</details>

---


### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Running Print ALL matching experiments fully (no head truncation)",
  "usage": {
    "total_tokens": 20234,
    "tool_uses": 5,
    "duration_ms": 31663
  },
  "last_tool_name": "Bash",
  "uuid": "5eb252bd-23f2-4c4e-840a-281d9e3cb797",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_014i2nkeSZEzHJCofmtKRPcD`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\nmatches = {}\nfor exp_id, exp_data in experiments.items():\n    exp_id_lower = exp_id.lower()\n    name = ''\n    if isinstance(exp_data, dict):\n        name = str(exp_data.get('name', '')).lower()\n    combined = exp_id_lower + ' ' + name\n    if any(kw in combined for kw in ['fewnerd', 'n16', 'n_16']):\n        matches[exp_id] = exp_data\n\nprint(json.dumps(matches, indent=2, ensure_ascii=False))\nprint(f'\\n--- Total matching experiment keys: {len(matches)} ---')\n\" 2>&1\n",
  "description": "Print ALL matching experiments fully (no head truncation)",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8dddf29a-0a8e-46d6-8a1a-9b6e95ddbdc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNYvCmyv1F8PCe3jAxSDWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 18421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1520,
        "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-19T07:58:16.524Z_

<details><summary>↩ Tool result · `toolu_014i2nkeSZEzHJCofmtKRPcD`</summary>

```text
&lt;persisted-output>
Output too large (59.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt

Preview (first 2KB):
{
  "exp_qwen25_32b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:25.428Z",
    "updated_at": "2026-05-19T07:52:18.591Z",
    "hypothesis": "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.",
    "server": "autodl-5090",
    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
    "account": "root",
    "reproduce": {
      "server": "autodl-5090",
      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
      "started_at": "2026-05-19T06:47:41.246Z"
    },
    "notes": "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."
  },
  "exp_qwen25_7b_fewnerd": {
    "status": "QUEUED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:41:43.121Z",
    "updated_at": "2026-05-19T07:48:40.207Z",
    "hypothesis": "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."
  },
  "exp_qwen25_14b_fewnerd": {
    "status": "ALLOCATED",
    "retry_count": 0,
    "created_at": "2026-05-19T06:19:31.620Z",
    "updated_at": "2026-05-19T06:47:43.938Z",
    "hypothesis": "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.",
    "server": "autodl-5090-c",
    "gpu": "cuda:0,cuda:1",
    "account": "root",
    "reproduce": {
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "4ed46b7c-303a-40ff-9faa-b562ac56b151"
}
```

</details>

---


### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "usage": {
    "total_tokens": 21588,
    "tool_uses": 6,
    "duration_ms": 35920
  },
  "last_tool_name": "Read",
  "uuid": "cdf0b550-b718-47f1-9ee0-8c2e7d16d8f4",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01XeWHr2hMCeddFWmMT6aCFA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "23b48a00-e600-4c32-b963-1614885f2b4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8B7eHbsRJYq495n1wD4xB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 19941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1282,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-19T07:58:20.747Z_

<details><summary>↩ Tool result · reported error · `toolu_01XeWHr2hMCeddFWmMT6aCFA`</summary>

```text
File content (26113 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "d4b8e0a5-e86d-4ed6-b8f1-b3a43bf40569",
  "tool_use_result": "Error: File content (26113 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "usage": {
    "total_tokens": 21845,
    "tool_uses": 7,
    "duration_ms": 38957
  },
  "last_tool_name": "Read",
  "uuid": "959adbfb-1fb0-4bab-8ee9-7a176eb33b05",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01MyPGbersD8pHnSzBtUQXqB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c28e9353-ae6d-42dd-81ad-31897b9de7b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Uw8kKYbgEc5qAFUQCN9QB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 21223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 192,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-19T07:58:24.021Z_

<details><summary>↩ Tool result · `toolu_01MyPGbersD8pHnSzBtUQXqB`</summary>

```text
1	{
2	  "exp_qwen25_32b_fewnerd": {
3	    "status": "ALLOCATED",
4	    "retry_count": 0,
5	    "created_at": "2026-05-19T06:19:25.428Z",
6	    "updated_at": "2026-05-19T07:52:18.591Z",
7	    "hypothesis": "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.",
8	    "server": "autodl-5090",
9	    "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
10	    "account": "root",
11	    "reproduce": {
12	      "server": "autodl-5090",
13	      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
14	      "started_at": "2026-05-19T06:47:41.246Z"
15	    },
16	    "notes": "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."
17	  },
18	  "exp_qwen25_7b_fewnerd": {
19	    "status": "QUEUED",
20	    "retry_count": 0,
21	    "created_at": "2026-05-19T06:41:43.121Z",
22	    "updated_at": "2026-05-19T07:48:40.207Z",
23	    "hypothesis": "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."
24	  },
25	  "exp_qwen25_14b_fewnerd": {
26	    "status": "ALLOCATED",
27	    "retry_count": 0,
28	    "created_at": "2026-05-19T06:19:31.620Z",
29	    "updated_at": "2026-05-19T06:47:43.938Z",
30	    "hypothesis": "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.",
31	    "server": "autodl-5090-c",
32	    "gpu": "cuda:0,cuda:1",
33	    "account": "root",
34	    "reproduce": {
35	      "server": "autodl-5090-c",
36	      "gpu": "cuda:0,cuda:1",
37	      "started_at": "2026-05-19T06:47:43.938Z"
38	    }
39	  },
40	  "exp_llama_fewnerd_inference": {
41	    "status": "DONE",
42	    "retry_count": 0,
43	    "created_at": "2026-05-19T02:18:49.938Z",
44	    "updated_at": "2026-05-19T03:15:04.486Z",
45	    "hypothesis": "LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.",
46	    "parent": "exp_llama_fewnerd_lora",
47	    "spec": {
48	      "command": "bash code/run_llama_fewnerd_inference.sh",
49	      "server": "autodl-5090",
50	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/",
51	      "data_count": 37648,
52	      "model_name": "LLaMA-3.1-8B-FewNERD-LoRA-merged",
53	      "seed": "42,123,456",
54	      "checkpoint_source": "exp_llama_fewnerd_lora",
55	      "eval_data": "FewNERD test set",
56	      "checkpoint_path": "checkpoints/llama3.1-8b-fewnerd-merged/",
57	      "log_path": "logs/llama_fewnerd_inference.log"
58	    },
59	    "conclusion": "success",
60	    "metrics": {
61	      "3seed_mean": {
62	        "greedy_f1": 0.7842,
63	        "oracle_f1": 0.8843,
64	        "headroom_pp": 10.01,
65	        "degeneracy_pct": 23.36,
66	        "lp_delta_pp": 0.36,
67	        "dgs_delta_pp": -0.35
68	      },
69	      "seed_42": {
70	        "greedy_f1": 0.7841,
71	        "oracle_f1": 0.8854,
72	        "degen": 27.32
73	      },
74	      "seed_123": {
75	        "greedy_f1": 0.784,
76	        "oracle_f1": 0.8839,
77	        "degen": 24.63
78	      },
79	      "seed_456": {
80	        "greedy_f1": 0.7844,
81	        "oracle_f1": 0.8835,
82	        "degen": 18.13
83	      },
84	      "signal_ranking": "LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)",
85	      "lp_only_positive": true,
86	      "n_instances_gold_filtered": 32565
87	    },
88	    "completed_at": "2026-05-19T03:15:04.486Z"
89	  },
90	  "exp_llama_fewnerd_lora": {
91	    "status": "DONE",
92	    "retry_count": 0,
93	    "created_at": "2026-05-18T13:20:55.859Z",
94	    "updated_at": "2026-05-19T01:08:20.832Z",
95	    "hypothesis": "LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER",
96	    "spec": {
97	      "command": "llamafactory-cli train train_config_llama_fewnerd.yaml",
98	      "server": "autodl-5090",
99	      "gpu": "cuda:1",
100	      "pid": 137865,
101	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd",
102	      "data_count": -1,
103	      "model_name": "LLaMA-Few-NERD-LoRA",
104	      "seed": 42,
105	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log",
106	      "run_script": "run_llama_fewnerd_train_single_gpu.sh",
107	      "tmux_session": "llama_fewnerd",
108	      "note": "Retroactively registered - data_count unknown, seed assumed 42"
109	    },
110	    "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora",
111	    "log_path": "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log",
112	    "conclusion": "success",
113	    "metrics": {
114	      "epoch": 3,
115	      "train_loss": 0.0516,
116	      "eval_loss": 0.0323,
117	      "train_runtime_hours": 15.35,
118	      "total_steps": 24708,
119	      "final_checkpoint": "checkpoint-24708",
120	      "adapter_size_mb": 320
121	    },
122	    "completed_at": "2026-05-19T01:08:20.832Z"
123	  },
124	  "exp_031_fewnerd_t12": {
125	    "status": "DONE",
126	    "retry_count": 0,
127	    "created_at": "2026-05-18T20:04:12.040Z",
128	    "updated_at": "2026-05-19T00:30:14.652Z",
129	    "hypothesis": "FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC",
130	    "conclusion": "killed",
131	    "failure_reason": "数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。",
132	    "notes": "T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient",
133	    "completed_at": "2026-05-19T00:30:14.652Z"
134	  },
135	  "exp_fewnerd_s789_n8": {
136	    "status": "DONE",
137	    "retry_count": 0,
138	    "created_at": "2026-05-18T23:17:34.011Z",
139	    "updated_at": "2026-05-18T23:18:28.125Z",
140	    "hypothesis": "FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.",
141	    "parent": "exp_029a",
142	    "spec": {
143	      "command": "python code/analyze_fewnerd_s789.py",
144	      "server": "autodl-5090",
145	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl",
146	      "data_count": 37648,
147	      "model_name": "Qwen3-8B (ft_002_v2)",
148	      "seed": 789,
149	      "checkpoint_source": "exp_021 shards",
150	      "eval_data": "FewNERD test (37648 instances, 32565 gold-filtered)",
151	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/",
152	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log"
153	    },
154	    "conclusion": "success",
155	    "completed_at": "2026-05-18T23:18:17.902Z",
156	    "metrics": {
157	      "greedy_f1": 0.7478,
158	      "oracle_f1": 0.8714,
159	      "headroom_pp": 12.37,
160	      "degen_rate": 0.1177,
161	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
162	      "instance_count": 37648,
163	      "n_valid": 32565,
164	      "lp_sel_f1": 0.7614,
165	      "lp_delta_pp": 1.36,
166	      "lp_rho_global": 0.1788,
167	      "lp_rho_cond": 0.176,
168	      "dgs_f1": 0.7621,
169	      "dgs_delta_pp": 1.43,
170	      "dgs_vs_lp_pp": 0.07,
171	      "best_signal": "LP",
172	      "four_seed_mean_greedy": 0.7481,
173	      "four_seed_mean_lp_delta_pp": 1.38,
174	      "four_seed_lp_delta_ci95": [
175	        1.32,
176	        1.44
177	      ]
178	    }
179	  },
180	  "exp_021_fewnerd_n8_seed456": {
181	    "status": "DONE",
182	    "retry_count": 0,
183	    "created_at": "2026-05-18T22:03:17.992Z",
184	    "updated_at": "2026-05-18T22:04:50.774Z",
185	    "hypothesis": "Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.",
186	    "spec": {
187	      "command": "python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0",
188	      "server": "autodl-5090",
189	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd",
190	      "data_count": 37648,
191	      "model_name": "Qwen3-8B",
192	      "seed": 456,
193	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456",
194	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log"
195	    },
196	    "conclusion": "success",
197	    "completed_at": "2026-05-18T22:04:35.573Z",
198	    "metrics": {
199	      "degen_rate": 0.1212,
200	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
201	      "instance_count": 37648,
202	      "n_valid": 32565,
203	      "n_gold_empty": 5083,
204	      "ner_greedy_f1": 0.7888,
205	      "ner_oracle_f1": 0.881,
206	      "rho_fk_ner": 0.1632,
207	      "rho_sj_ner": 0.313,
208	      "sample_f1_pct_zero": 19.32
209	    }
210	  },
211	  "exp_021_fewnerd_n8_seed123": {
212	    "status": "DONE",
213	    "retry_count": 0,
214	    "created_at": "2026-05-18T22:03:16.735Z",
215	    "updated_at": "2026-05-18T22:04:49.470Z",
216	    "hypothesis": "Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.",
217	    "spec": {
218	      "command": "python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0",
219	      "server": "autodl-5090",
220	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd",
221	      "data_count": 37648,
222	      "model_name": "Qwen3-8B",
223	      "seed": 123,
224	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123",
225	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log"
226	    },
227	    "conclusion": "success",
228	    "completed_at": "2026-05-18T22:04:33.731Z",
229	    "metrics": {
230	      "degen_rate": 0.1312,
231	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
232	      "instance_count": 37648,
233	      "n_valid": 32565,
234	      "n_gold_empty": 5083,
235	      "ner_greedy_f1": 0.7885,
236	      "ner_oracle_f1": 0.8892,
237	      "rho_fk_ner": 0.1602,
238	      "rho_sj_ner": 0.3083,
239	      "sample_f1_pct_zero": 20.39
240	    }
241	  },
242	  "exp_002_conll_n16_seed456": {
243	    "status": "DONE",
244	    "retry_count": 0,
245	    "created_at": "2026-05-18T22:03:15.720Z",
246	    "updated_at": "2026-05-18T22:04:46.954Z",
247	    "hypothesis": "Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.",
248	    "spec": {
249	      "command": "python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0",
250	      "server": "autodl-5090",
251	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/conll2003",
252	      "data_count": 3453,
253	      "model_name": "Qwen3-8B",
254	      "seed": 456,
255	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456",
256	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log"
257	    },
258	    "conclusion": "success",
259	    "completed_at": "2026-05-18T22:04:31.934Z",
260	    "metrics": {
261	      "degen_rate": 0.5544,
262	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
263	      "instance_count": 3453,
264	      "n_valid": 2756,
265	      "n_gold_empty": 697,
266	      "ner_greedy_f1": 0.9074,
267	      "ner_oracle_f1": 0.9549,
268	      "rho_fk_ner": 0.4718,
269	      "rho_sj_ner": 0.4819,
270	      "sample_f1_pct_zero": 7.02
271	    }
272	  },
273	  "exp_002_conll_n16_seed123": {
274	    "status": "DONE",
275	    "retry_count": 0,
276	    "created_at": "2026-05-18T22:03:14.343Z",
277	    "updated_at": "2026-05-18T22:04:45.039Z",
278	    "hypothesis": "Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.",
279	    "spec": {
280	      "command": "python scs_inference.py --dataset conll2003 --seed 123 --n_samples 16 --temperature 1.0",
281	      "server": "autodl-5090",
282	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/conll2003",
283	      "data_count": 3453,
284	      "model_name": "Qwen3-8B",
285	      "seed": 123,
286	      "checkpoint_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123",
287	      "log_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log"
288	    },
289	    "conclusion": "success",
290	    "completed_at": "2026-05-18T22:04:29.992Z",
291	    "metrics": {
292	      "degen_rate": 0.471,
293	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
294	      "instance_count": 3453,
295	      "n_valid": 2756,
296	      "n_gold_empty": 697,
297	      "ner_greedy_f1": 0.9068,
298	      "ner_oracle_f1": 0.9633,
299	      "rho_fk_ner": 0.4524,
300	      "rho_sj_ner": 0.4621,
301	      "sample_f1_pct_zero": 7.54
302	    }
303	  },
304	  "exp_017_llama_conll_n16_s456_r1024": {
305	    "status": "DONE",
306	    "retry_count": 0,
307	    "created_at": "2026-05-14T22:17:04.572Z",
308	    "updated_at": "2026-05-18T20:50:15.047Z",
309	    "spec": {
310	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.",
311	      "parent": "exp_017_llama_conll_n16_s456",
312	      "model_name": "llama3.1-8b-conll2003-merged",
313	      "dataset": "CoNLL-2003",
314	      "seed": 456,
315	      "server": "autodl-5090",
316	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024",
317	      "gpu": "cuda:2",
318	      "pid": "175870",
319	      "data_path": "data/conll2003",
320	      "data_count": 3453,
321	      "tmux_session": "exp_017_llama_conll_n16_s456_r1024"
322	    },
323	    "conclusion": "success",
324	    "metrics": {
325	      "degen_rate": 0.8672,
326	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
327	      "instance_count": 3453,
328	      "n_valid": 2756,
329	      "n_gold_empty": 697,
330	      "parse_rate": 1,
331	      "ner_greedy_f1": 0.9265,
332	      "ner_oracle_f1": 0.9499,
333	      "rho_fk_ner": 0.469,
334	      "rho_sj_ner": 0.4734,
335	      "rho_vc_ner": 0.4722,
336	      "rho_em_ner": 0.4752,
337	      "rho_lp_ner": 0.3099,
338	      "auroc_fk_ner": 0.7408,
339	      "auroc_sj_ner": 0.7428,
340	      "auroc_vc_ner": 0.7495,
341	      "auroc_em_ner": 0.7444,
342	      "auroc_lp_ner": 0.7628,
343	      "auroc_note": "median F1=1.0, AUROC uses >=median threshold",
344	      "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."
345	    },
346	    "checkpoint_path": "N/A (inference-only)",
347	    "log_path": "output/exp_017_llama_conll_n16_s456_r1024_run.log",
348	    "completed_at": "2026-05-15T11:45:25.899Z",
349	    "hypothesis": "LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction."
350	  },
351	  "exp_017_llama_conll_n16_r1024": {
352	    "status": "DONE",
353	    "retry_count": 0,
354	    "created_at": "2026-05-14T22:17:01.036Z",
355	    "updated_at": "2026-05-18T20:50:11.906Z",
356	    "spec": {
357	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.",
358	      "parent": "exp_017_llama_conll_n16",
359	      "model_name": "llama3.1-8b-conll2003-merged",
360	      "dataset": "CoNLL-2003",
361	      "seed": 42,
362	      "server": "autodl-5090",
363	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024",
364	      "gpu": "cuda:1",
365	      "pid": "175734",
366	      "data_path": "data/conll2003",
367	      "data_count": 3453,
368	      "tmux_session": "exp_017_llama_conll_n16_r1024"
369	    },
370	    "conclusion": "success",
371	    "metrics": {
372	      "degen_rate": 0.8647,
373	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
374	      "instance_count": 3453,
375	      "n_valid": 2756,
376	      "n_gold_empty": 697,
377	      "parse_rate": 1,
378	      "ner_greedy_f1": 0.9265,
379	      "ner_oracle_f1": 0.9499,
380	      "rho_fk_ner": 0.4752,
381	      "rho_sj_ner": 0.4836,
382	      "rho_vc_ner": 0.4746,
383	      "rho_em_ner": 0.4818,
384	      "rho_lp_ner": 0.3136,
385	      "auroc_fk_ner": 0.7467,
386	      "auroc_sj_ner": 0.7496,
387	      "auroc_vc_ner": 0.7529,
388	      "auroc_em_ner": 0.7508,
389	      "auroc_lp_ner": 0.7661,
390	      "auroc_note": "median F1=1.0, AUROC uses >=median threshold",
391	      "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."
392	    },
393	    "checkpoint_path": "N/A (inference-only)",
394	    "log_path": "output/exp_017_llama_conll_n16_r1024_run.log",
395	    "completed_at": "2026-05-15T11:45:23.213Z",
396	    "hypothesis": "LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances)."
397	  },
398	  "exp_002_conll_n16": {
399	    "status": "DONE",
400	    "retry_count": 0,
401	    "created_at": "2026-05-14T18:12:16.041Z",
402	    "updated_at": "2026-05-18T20:49:50.398Z",
403	    "spec": {
404	      "hypothesis": "Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16",
405	      "plan_id": "exp-002",
406	      "parent": "exp_002_ner_conll2003",
407	      "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16",
408	      "server": "autodl-5090",
409	      "data_path": "data/conll2003",
410	      "data_count": 3453,
411	      "model_name": "qwen3-8b-conll2003-merged",
412	      "seed": 42
413	    },
414	    "conclusion": "success",
415	    "metrics": {
416	      "degen_rate": 0.4844,
417	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
418	      "N": 16,
419	      "dataset": "conll2003",
420	      "subtask": "ner",
421	      "n_instances": 3453,
422	      "n_valid": 2756,
423	      "n_conditional": 2614,
424	      "greedy_f1": 0.907,
425	      "full": {
426	        "SJ_rho": 0.4496,
427	        "FK_rho": 0.3928,
428	        "logprob_rho": 0.3146,
429	        "EM_rho": 0.4627,
430	        "voting_conf_rho": 0.4286,
431	        "SJ_AUROC": 0.8264,
432	        "FK_AUROC": 0.7821,
433	        "logprob_AUROC": 0.7531,
434	        "EM_AUROC": 0.8409,
435	        "voting_conf_AUROC": 0.8071,
436	        "SJ_ECE": 0.0747,
437	        "FK_ECE": 0.1786,
438	        "logprob_ECE": 0.2031,
439	        "EM_ECE": 0.0786,
440	        "voting_conf_ECE": 0.529
441	      },
442	      "conditional": {
443	        "SJ_rho": 0.4208,
444	        "FK_rho": 0.3494,
445	        "logprob_rho": 0.3756,
446	        "EM_rho": 0.4658,
447	        "voting_conf_rho": 0.3654,
448	        "SJ_AUROC": 0.8405,
449	        "FK_AUROC": 0.7819,
450	        "logprob_AUROC": 0.8259,
451	        "EM_AUROC": 0.8781,
452	        "voting_conf_AUROC": 0.7951,
453	        "SJ_ECE": 0.0982,
454	        "FK_ECE": 0.1899,
455	        "logprob_ECE": 0.2504,
456	        "EM_ECE": 0.0997,
457	        "voting_conf_ECE": 0.6096
458	      },
459	      "n8_vs_n16_delta_rho_full": {
460	        "SJ": 0.0139,
461	        "FK": -0.007,
462	        "logprob": -0.0011,
463	        "EM": 0.012,
464	        "voting_conf": 0.0049
465	      }
466	    },
467	    "checkpoint_path": "output/exp_002_conll_n16/samples.jsonl",
468	    "log_path": "output/exp_002_conll_n16.log",
469	    "completed_at": "2026-05-14T18:58:40.473Z",
470	    "hypothesis": "CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9)."
471	  },
472	  "exp_027_fewnerd_n16": {
473	    "status": "DONE",
474	    "retry_count": 0,
475	    "created_at": "2026-05-17T05:28:57.036Z",
476	    "updated_at": "2026-05-18T20:48:58.455Z",
477	    "spec": {
478	      "hypothesis": "LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.",
479	      "parent": "exp_021_fewnerd_full",
480	      "model_name": "qwen3-8b-fewnerd-exp021-merged",
481	      "data_path": "data/fewnerd_n16_subset/test.json",
482	      "data_count": 5000,
483	      "seed": 42,
484	      "server": "autodl-5090",
485	      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
486	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --start_index {0,1250,2500,3750} --end_index {1250,2500,3750,5000} --output_dir output/exp_027_fewnerd_n16/shard_{0-3}",
487	      "checkpoint_path": "output/exp_027_fewnerd_n16/sampled_results.jsonl",
488	      "log_path": "output/exp_027_fewnerd_n16/"
489	    },
490	    "conclusion": "success",
491	    "metrics": {
492	      "LP_delta_pp": 1.88,
493	      "LP_delta_95CI": [
494	        1.41,
495	        2.37
496	      ],
497	      "degen_rate": 0.0706,
498	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered",
499	      "greedy_f1": 0.7478,
500	      "lp_sel_f1": 0.7666,
501	      "oracle_f1": 0.902,
502	      "headroom_pp": 15.42,
503	      "all_8_types_positive": true,
504	      "n_instances": 5000,
505	      "N_samples": 16,
506	      "bootstrap_p": "<0.001"
507	    },
508	    "hypothesis": "LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.",
509	    "completed_at": "2026-05-17T05:46:48.460Z"
510	  },
511	  "exp_017_llama_conll_n16_s123_r1024": {
512	    "status": "DONE",
513	    "retry_count": 0,
514	    "created_at": "2026-05-14T22:17:02.953Z",
515	    "updated_at": "2026-05-18T20:47:52.122Z",
516	    "spec": {
517	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.",
518	      "parent": "exp_017_llama_conll_n16_s123",
519	      "model_name": "llama3.1-8b-conll2003-merged",
520	      "dataset": "CoNLL-2003",
521	      "seed": 123,
522	      "server": "autodl-5090",
523	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024",
524	      "data_path": "data/conll2003",
525	      "data_count": 3453
526	    },
527	    "conclusion": "success",
528	    "completed_at": "2026-05-15T01:20:51.219Z",
529	    "notes": "Output exists on autodl-5090. Registry status corrected from killed to success.",
530	    "hypothesis": "LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.",
531	    "metrics": {
532	      "degen_rate": 0.8636,
533	      "degen_rate_source": "unified_metrics_constant_f1_gold_filtered"
534	    }
535	  },
536	  "exp_028_fewnerd_5epoch": {
537	    "status": "DONE",
538	    "retry_count": 0,
539	    "created_at": "2026-05-17T07:53:12.913Z",
540	    "updated_at": "2026-05-17T20:29:42.274Z",
541	    "spec": {
542	      "hypothesis": "Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.",
543	      "parent": "exp_021_fewnerd_full",
544	      "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\"",
545	      "server": "autodl-5090",
546	      "gpu": "cuda:0,1,2,3",
547	      "data_path": "data/fewnerd_uie_train",
548	      "data_count": 131767,
549	      "model_name": "Qwen3-8B LoRA rank=32",
550	      "seed": 42,
551	      "log_path": "logs/exp_028_4gpu_train.log",
552	      "checkpoint_path": "checkpoints/qwen3-8b-fewnerd-5epoch-lora"
553	    },
554	    "conclusion": "negative",
555	    "metrics": {
556	      "degeneracy_cf1_gold": 0.3133,
557	      "greedy_f1": 0.7773,
558	      "lp_sel_delta_pp": 0.624,
559	      "lp_sel_f1": 0.7835,
560	      "oracle_f1": 0.8723,
561	      "within_instance_rho_mean": 0.4066,
562	      "within_instance_rho_median": 0.6151
563	    },
564	    "hypothesis": "Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.",
565	    "completed_at": "2026-05-17T20:29:42.274Z"
566	  },
567	  "exp_008_re_n16": {
568	    "status": "DONE",
569	    "retry_count": 0,
570	    "created_at": "2026-05-14T12:03:06.876Z",
571	    "updated_at": "2026-05-17T02:58:19.490Z",
572	    "spec": {
573	      "hypothesis": "RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.",
574	      "plan_id": "exp-008",
575	      "model_name": "qwen3-8b-scierc-merged-v2",
576	      "dataset": "SciERC",
577	      "gpu": "cuda:2",
578	      "server": "gpu-5090-4x-2",
579	      "gpu_budget_hours": 12,
580	      "description": "RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.",
581	      "priority": "P1",
582	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs",
583	      "data_path": "data/scierc/processed_data",
584	      "data_count": 551,
585	      "seed": 42,
586	      "num_instances": 200,
587	      "partial": true,
588	      "note": "Only 200/551 instances due to --num_test default bug. Needs full rerun."
589	    },
590	    "metrics": {
591	      "ner": {
592	        "greedy_f1": 0.6635,
593	        "oracle_f1": 0.8208,
594	        "headroom": 0.1572,
595	        "rho_sj_full": 0.377,
596	        "rho_fk_full": 0.2508,
597	        "rho_logprob_full": 0.3153,
598	        "rho_sj_cond": 0.3598,
599	        "rho_fk_cond": 0.2251,
600	        "rho_logprob_cond": 0.2927,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "fc5ef91e-193c-4171-87c8-6a27546674b3"
}
```

</details>

---


### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "usage": {
    "total_tokens": 34192,
    "tool_uses": 8,
    "duration_ms": 44664
  },
  "last_tool_name": "Read",
  "uuid": "db7ee835-ddc8-4909-990c-90c396a03235",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01LLvMesQ9pq63rDA2XnxAR1`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "offset": 600,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "68ebc718-1100-4810-89c3-f9a6121a4be8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uNSuM5JJH1NamEYwDqkd2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12309,
      "cache_read_input_tokens": 21415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12309,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 44 · 2026-05-19T07:58:29.224Z_

<details><summary>↩ Tool result · `toolu_01LLvMesQ9pq63rDA2XnxAR1`</summary>

```text
600	        "rho_logprob_cond": 0.2927,
601	        "sj_beats_fk": true,
602	        "rho_advantage": 0.1262
603	      },
604	      "re": {
605	        "greedy_f1": 0.4339,
606	        "oracle_f1": 0.6658,
607	        "headroom": 0.2319,
608	        "rho_sj_full": 0.2966,
609	        "rho_fk_full": 0.2871,
610	        "rho_logprob_full": 0.2986,
611	        "rho_sj_cond": 0.3975,
612	        "rho_fk_cond": 0.3774,
613	        "rho_logprob_cond": 0.2745,
614	        "sj_beats_fk": true,
615	        "rho_advantage": 0.0095
616	      },
617	      "verdict": "FAIL"
618	    },
619	    "conclusion": "success",
620	    "checkpoint_path": "N/A",
621	    "log_path": "output/exp008_re_n16/",
622	    "completed_at": "2026-05-14T12:28:39.268Z",
623	    "hypothesis": "RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections."
624	  },
625	  "exp_001_ner_n16_seed123": {
626	    "status": "DONE",
627	    "retry_count": 0,
628	    "created_at": "2026-05-14T12:46:06.430Z",
629	    "updated_at": "2026-05-17T02:58:18.225Z",
630	    "spec": {
631	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\"",
632	      "server": "autodl-5090",
633	      "gpu": [
634	        "cuda:3"
635	      ],
636	      "pid": "63407",
637	      "log_path": "output/exp001_n16_seed123_run.log",
638	      "submitted_at": "2026-05-14T12:46:06.234Z",
639	      "submitted_via": "submit_training_job",
640	      "backend": "tmux",
641	      "account": "root",
642	      "data_count": 551,
643	      "data_path": "data/scierc/processed_data",
644	      "model_name": "qwen3-8b-scierc-merged-v2",
645	      "seed": 123,
646	      "checkpoint_path": "output/exp001_n16_seed123/",
647	      "wall_clock_seconds": 2748.0,
648	      "gpu_hours": 0.76
649	    },
650	    "conclusion": "success",
651	    "metrics": {
652	      "ner": {
653	        "greedy_f1": 0.663,
654	        "oracle_f1": 0.809,
655	        "headroom": 0.146,
656	        "rho_sj": 0.423,
657	        "rho_fk": 0.29,
658	        "rho_logprob": 0.239,
659	        "rho_sj_cond": 0.423,
660	        "rho_fk_cond": 0.26
661	      },
662	      "re": {
663	        "greedy_f1": 0.419,
664	        "oracle_f1": 0.625,
665	        "headroom": 0.206,
666	        "rho_sj": 0.267,
667	        "rho_fk": 0.315,
668	        "rho_sj_cond": 0.364,
669	        "rho_fk_cond": 0.331
670	      },
671	      "verdict": "FAIL",
672	      "verdict_note": "RE rho_sj=0.267 < 0.40; RE >30% samples F1=0",
673	      "n_instances": 551,
674	      "seed": 123,
675	      "N": 16,
676	      "T": 1
677	    },
678	    "completed_at": "2026-05-14T13:31:54.232Z",
679	    "hypothesis": "SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples."
680	  },
681	  "exp_008_re_n16_t10_full": {
682	    "status": "DONE",
683	    "retry_count": 0,
684	    "created_at": "2026-05-14T13:27:42.867Z",
685	    "updated_at": "2026-05-17T02:58:10.171Z",
686	    "spec": {
687	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs",
688	      "server": "autodl-5090",
689	      "data_path": "data/scierc/processed_data",
690	      "data_count": 551,
691	      "model_name": "qwen3-8b-scierc-merged-v2",
692	      "seed": 42
693	    },
694	    "reproduce": {
695	      "finished_at": "2026-05-14T13:44:18.988Z"
696	    },
697	    "failure_reason": "",
698	    "conclusion": "negative",
699	    "completed_at": "2026-05-14T13:44:19.577Z",
700	    "extra": {
701	      "hook_events": [
702	        {
703	          "event": "on_failed",
704	          "action": "agent",
705	          "ts": "2026-05-14T13:44:21.528032+00:00"
706	        }
707	      ]
708	    },
709	    "metrics": {
710	      "ner": {
711	        "rho_sj": 0.444
712	      },
713	      "re": {
714	        "rho_sj": 0.248
715	      },
716	      "n_instances": 551,
717	      "N": 16,
718	      "T": 1,
719	      "seed": 42,
720	      "mode": "RE-only",
721	      "source": "director_corrected"
722	    },
723	    "hypothesis": "RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections."
724	  },
725	  "exp_008_re_n16_v2": {
726	    "status": "DONE",
727	    "retry_count": 0,
728	    "created_at": "2026-05-14T14:34:06.296Z",
729	    "updated_at": "2026-05-17T02:57:41.178Z",
730	    "spec": {
731	      "description": "RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs",
732	      "hypothesis": "Structural consistency correlates with per-instance RE F1 on SciERC full dataset",
733	      "server": "autodl-5090",
734	      "data_path": "data/scierc/processed_data",
735	      "data_count": 551,
736	      "model_name": "ft_002_v2",
737	      "seed": 42,
738	      "command": "CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2",
739	      "gpu": [
740	        "cuda:3"
741	      ],
742	      "pid": "78737",
743	      "backend": "tmux",
744	      "account": "root",
745	      "log_path": "output/exp_008_re_n16_v2/run.log"
746	    },
747	    "conclusion": "negative",
748	    "metrics": {
749	      "sj_rho_full": 0.281,
750	      "sj_rho_cond": 0.308,
751	      "f1_zero_pct": 44.3,
752	      "conclusion_note": "RE N=16 v2 negative: SJ weak, 44.3% F1=0"
753	    },
754	    "checkpoint_path": "N/A (inference)",
755	    "completed_at": "2026-05-14T15:23:35.598Z",
756	    "log_path": "output/exp_008_re_n16_v2/",
757	    "hypothesis": "RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high."
758	  },
759	  "exp_007_llama_n16": {
760	    "status": "DONE",
761	    "retry_count": 0,
762	    "created_at": "2026-05-14T18:31:44.366Z",
763	    "updated_at": "2026-05-17T02:57:12.521Z",
764	    "spec": {
765	      "hypothesis": "LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.",
766	      "plan_id": "exp-007",
767	      "parent": "exp_007_llama_inference",
768	      "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16",
769	      "server": "autodl-5090",
770	      "data_path": "data/scierc/processed_data",
771	      "data_count": 551,
772	      "model_name": "llama3.1-8b-scierc-merged",
773	      "seed": 42,
774	      "checkpoint_source": "checkpoints/llama3.1-8b-scierc-merged",
775	      "eval_data": "data/scierc/processed_data"
776	    },
777	    "conclusion": "success",
778	    "checkpoint_path": "output/exp_007_llama_n16/samples.jsonl",
779	    "log_path": "output/exp_007_llama_n16.log",
780	    "completed_at": "2026-05-14T19:03:39.163Z",
781	    "metrics": {
782	      "N": 16,
783	      "dataset": "scierc",
784	      "subtask": "ner",
785	      "n_instances": 551,
786	      "n_valid": 529,
787	      "n_conditional": 478,
788	      "greedy_f1": 0.645,
789	      "full": {
790	        "SJ_rho": 0.3791,
791	        "FK_rho": 0.3081,
792	        "logprob_rho": 0.2041,
793	        "EM_rho": 0.3159,
794	        "voting_conf_rho": 0.4515,
795	        "SJ_AUROC": 0.717,
796	        "FK_AUROC": 0.6581,
797	        "logprob_AUROC": 0.5656,
798	        "EM_AUROC": 0.7686,
799	        "voting_conf_AUROC": 0.7266,
800	        "SJ_ECE": 0.1019,
801	        "FK_ECE": 0.1556,
802	        "logprob_ECE": 0.084,
803	        "EM_ECE": 0.1761,
804	        "voting_conf_ECE": 0.1365
805	      },
806	      "conditional": {
807	        "SJ_rho": 0.3222,
808	        "FK_rho": 0.2182,
809	        "logprob_rho": 0.1286,
810	        "EM_rho": 0.3563,
811	        "voting_conf_rho": 0.3356,
812	        "SJ_AUROC": 0.7014,
813	        "FK_AUROC": 0.6392,
814	        "logprob_AUROC": 0.545,
815	        "EM_AUROC": 0.7708,
816	        "voting_conf_AUROC": 0.6988,
817	        "SJ_ECE": 0.1466,
818	        "FK_ECE": 0.1853,
819	        "logprob_ECE": 0.1141,
820	        "EM_ECE": 0.1887,
821	        "voting_conf_ECE": 0.2634
822	      },
823	      "n8_vs_n16_delta_rho_full": {
824	        "SJ": 0.0161,
825	        "FK": -0.0185,
826	        "logprob": 0.0214,
827	        "EM": 0.0007,
828	        "voting_conf": 0.0184
829	      }
830	    },
831	    "hypothesis": "LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen."
832	  },
833	  "exp_017_llama_conll_n16": {
834	    "status": "DONE",
835	    "retry_count": 0,
836	    "created_at": "2026-05-14T19:19:35.318Z",
837	    "updated_at": "2026-05-17T02:56:57.283Z",
838	    "spec": {
839	      "hypothesis": "LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.",
840	      "plan_id": "exp-017",
841	      "parent": "exp_017_llama_conll_infer",
842	      "model_name": "llama3.1-8b-conll2003-merged",
843	      "dataset": "CoNLL-2003",
844	      "data_count": 3453,
845	      "seed": 42,
846	      "server": "autodl-5090",
847	      "command": "CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16",
848	      "data_path": "data/conll2003",
849	      "pid": 106997,
850	      "n_samples": 16,
851	      "temperature": 1,
852	      "checkpoint_source": "checkpoints/llama3.1-8b-conll2003-merged",
853	      "eval_data": "conll2003 test set",
854	      "checkpoint_path": "output/exp_017_llama_conll_n16/samples.jsonl",
855	      "log_path": "output/exp_017_llama_conll_n16/all_signals_report.json"
856	    },
857	    "metrics": {
858	      "greedy_f1": 0.9243,
859	      "oracle_f1": 0.9487,
860	      "oracle_headroom": 0.0244,
861	      "n_instances": 3453,
862	      "n_valid": 2756,
863	      "n_conditional": 2642,
864	      "structural_beats_surface": true,
865	      "full": {
866	        "SJ_rho": 0.4642,
867	        "SJ_AUROC": 0.7391,
868	        "SJ_ECE": 0.1131,
869	        "FK_rho": 0.4566,
870	        "FK_AUROC": 0.736,
871	        "FK_ECE": 0.1071,
872	        "logprob_rho": 0.3058,
873	        "logprob_AUROC": 0.7594,
874	        "logprob_ECE": 0.1288,
875	        "EM_rho": 0.4613,
876	        "EM_AUROC": 0.7391,
877	        "EM_ECE": 0.1084,
878	        "voting_conf_rho": 0.4554,
879	        "voting_conf_AUROC": 0.7406,
880	        "voting_conf_ECE": 0.0844
881	      },
882	      "conditional": {
883	        "SJ_rho": 0.4597,
884	        "SJ_AUROC": 0.7565,
885	        "SJ_ECE": 0.0846,
886	        "FK_rho": 0.4515,
887	        "FK_AUROC": 0.753,
888	        "FK_ECE": 0.0813,
889	        "logprob_rho": 0.3193,
890	        "logprob_AUROC": 0.8023,
891	        "logprob_ECE": 0.0921,
892	        "EM_rho": 0.4618,
893	        "EM_AUROC": 0.7589,
894	        "EM_ECE": 0.0757,
895	        "voting_conf_rho": 0.3978,
896	        "voting_conf_AUROC": 0.7287,
897	        "voting_conf_ECE": 0.0742
898	      },
899	      "best_of_n": {
900	        "greedy": 0.9243,
901	        "random_avg": 0.9213,
902	        "sj_best": 0.9259,
903	        "logprob_best": 0.925,
904	        "voting_conf_best": 0.9268,
905	        "oracle": 0.9487
906	      },
907	      "n8_vs_n16_delta": {
908	        "full_SJ_rho_delta": 0.0328,
909	        "full_FK_rho_delta": 0.0289,
910	        "full_logprob_rho_delta": -0.0014,
911	        "full_EM_rho_delta": 0.0307,
912	        "full_voting_conf_rho_delta": 0.0298,
913	        "cond_SJ_rho_delta": 0.0241,
914	        "cond_FK_rho_delta": 0.0205,
915	        "cond_logprob_rho_delta": -0.0089,
916	        "cond_EM_rho_delta": 0.0215,
917	        "cond_voting_conf_rho_delta": 0.0235
918	      }
919	    },
920	    "conclusion": "success",
921	    "completed_at": "2026-05-14T19:45:16.265Z",
922	    "hypothesis": "LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family."
923	  },
924	  "exp_001_n16_seed456": {
925	    "status": "DONE",
926	    "retry_count": 1,
927	    "created_at": "2026-05-14T12:10:30.350Z",
928	    "updated_at": "2026-05-17T02:56:53.526Z",
929	    "completed_at": "2026-05-14T12:28:38.721Z",
930	    "extra": {
931	      "previous_failure": {
932	        "conclusion": "success",
933	        "metrics": {
934	          "ner": {
935	            "greedy_f1": 0.6577,
936	            "oracle_f1": 0.8129,
937	            "headroom": 0.1553,
938	            "rho_sj_full": 0.3297,
939	            "rho_fk_full": 0.2578,
940	            "rho_logprob_full": 0.2866,
941	            "rho_sj_cond": 0.3394,
942	            "rho_fk_cond": 0.2721,
943	            "rho_logprob_cond": 0.2567,
944	            "sj_beats_fk": true,
945	            "rho_advantage": 0.0719
946	          },
947	          "re": {
948	            "greedy_f1": 0.4312,
949	            "oracle_f1": 0.6737,
950	            "headroom": 0.2425,
951	            "rho_sj_full": 0.285,
952	            "rho_fk_full": 0.2372,
953	            "rho_logprob_full": 0.2626,
954	            "rho_sj_cond": 0.3525,
955	            "rho_fk_cond": 0.2614,
956	            "rho_logprob_cond": 0.1927,
957	            "sj_beats_fk": true,
958	            "rho_advantage": 0.0478
959	          },
960	          "verdict": "FAIL"
961	        }
962	      }
963	    },
964	    "spec": {
965	      "hypothesis": "N=16 seed456 multi-seed robustness verification for SciERC NER+RE",
966	      "plan_id": "exp-001",
967	      "model_name": "qwen3-8b-scierc-merged-v2",
968	      "data_path": "data/scierc/processed_data",
969	      "data_count": 551,
970	      "seed": 456,
971	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs",
972	      "server": "autodl-5090",
973	      "gpu": "cuda:0",
974	      "pid": "174595",
975	      "log_path": "output/exp001_n16_seed456_run.log",
976	      "tmux_session": "exp_001_n16_seed456"
977	    },
978	    "conclusion": "success",
979	    "checkpoint_path": "N/A (inference-only)",
980	    "metrics": {
981	      "instance_count": 551,
982	      "n_valid": 529,
983	      "n_gold_empty": 22,
984	      "parse_rate": 1,
985	      "ner_greedy_f1": 0.6617,
986	      "ner_oracle_f1": 0.8075,
987	      "re_greedy_f1": 0.4215,
988	      "re_oracle_f1": 0.4748,
989	      "rho_sj_ner": 0.4098,
990	      "rho_fk_ner": 0.2723,
991	      "rho_vc_ner": 0.4449,
992	      "rho_em_ner": 0.3363,
993	      "rho_lp_ner": 0.2415,
994	      "rho_sj_re": 0.2835,
995	      "rho_fk_re": 0.2929,
996	      "auroc_sj_ner": 0.6823,
997	      "auroc_fk_ner": 0.6179,
998	      "auroc_vc_ner": 0.6981,
999	      "auroc_em_ner": 0.649,
1000	      "auroc_lp_ner": 0.5885,
1001	      "rho_note": "CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529)."
1002	    },
1003	    "log_path": "output/exp001_n16_seed456_run.log",
1004	    "hypothesis": "SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering."
1005	  },
1006	  "exp_021_fewnerd_full": {
1007	    "status": "DONE",
1008	    "retry_count": 0,
1009	    "created_at": "2026-05-16T16:33:44.079Z",
1010	    "updated_at": "2026-05-17T02:55:45.560Z",
1011	    "hypothesis": "Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.",
1012	    "spec": {
1013	      "gpu": "cuda:0,cuda:1,cuda:2,cuda:3",
1014	      "gpu_count": 4,
1015	      "training_mode": "DDP",
1016	      "checkpoint_path": "output/exp_021_fewnerd_full/checkpoint-6177",
1017	      "log_path": "output/exp_021_inference/"
1018	    },
1019	    "conclusion": "success",
1020	    "metrics": {
1021	      "total_steps": 6177,
1022	      "train_loss": 0.048,
1023	      "eval_loss": 0.0275,
1024	      "train_runtime": "3h57m",
1025	      "epochs": 3,
1026	      "final_checkpoint": "output/exp_021_fewnerd_full/checkpoint-6177",
1027	      "adapter_path": "output/exp_021_fewnerd_full/adapter_model.safetensors",
1028	      "inference_instances": 37648,
1029	      "inference_filtered": 32565,
1030	      "inference_n_samples": 8,
1031	      "greedy_macro_f1": 0.7478,
1032	      "oracle_macro_f1": 0.8719,
1033	      "headroom": 0.124,
1034	      "zero_f1_rate": 0.119,
1035	      "degeneracy_rate": 0.101,
1036	      "lp_within_range_mean": 0.0879,
1037	      "lp_within_range_median": 0.0662,
1038	      "lp_global_rho": 0.4215,
1039	      "lp_cond_rho": 0.4225,
1040	      "sj_global_rho": 0.3002,
1041	      "sj_cond_rho": 0.2937,
1042	      "fk_global_rho": 0.3132,
1043	      "fk_cond_rho": 0.3093,
1044	      "em_global_rho": 0.2871,
1045	      "em_cond_rho": 0.271,
1046	      "vc_global_rho": 0.3858,
1047	      "vc_cond_rho": 0.3234,
1048	      "lp_selection_delta_pp": 1.36,
1049	      "vc_selection_delta_pp": -1.79,
1050	      "sj_selection_delta_pp": -2.14,
1051	      "fk_selection_delta_pp": -2.26,
1052	      "em_selection_delta_pp": -3.85,
1053	      "lp_bootstrap_ci_95_pp": [
1054	        1.18,
1055	        1.53
1056	      ],
1057	      "lp_sample_auroc": 0.5782,
1058	      "vc_sample_auroc": 0.5354,
1059	      "fk_sample_auroc": 0.521,
1060	      "sj_sample_auroc": 0.5197,
1061	      "em_sample_auroc": 0.5137,
1062	      "scenario": "A_partial",
1063	      "note": "Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics."
1064	    },
1065	    "completed_at": "2026-05-16T22:04:16.683Z",
1066	    "parent": "exp_020_fewnerd_smoke"
1067	  },
1068	  "exp_020_fewnerd_smoke": {
1069	    "status": "DONE",
1070	    "retry_count": 0,
1071	    "created_at": "2026-05-16T10:29:25.272Z",
1072	    "updated_at": "2026-05-16T16:33:59.109Z",
1073	    "spec": {
1074	      "checkpoint_path": "checkpoints/ft_fewnerd_smoke",
1075	      "log_path": "checkpoints/fewnerd_train.log"
1076	    },
1077	    "hypothesis": "1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.",
1078	    "conclusion": "success",
1079	    "metrics": {
1080	      "final_loss": 0.031,
1081	      "total_steps": 8236,
1082	      "training_time": "5h54m",
1083	      "pilot_greedy_f1": 0.8037,
1084	      "pilot_instances": 200,
1085	      "merged_model_path": "checkpoints/qwen3-8b-fewnerd-merged"
1086	    },
1087	    "completed_at": "2026-05-16T16:33:59.109Z"
1088	  },
1089	  "exp008_re_n16": {
1090	    "status": "DONE",
1091	    "retry_count": 0,
1092	    "created_at": "2026-05-14T12:09:50.987Z",
1093	    "updated_at": "2026-05-15T12:41:39.774Z",
1094	    "spec": {
1095	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\"",
1096	      "server": "gpu-5090-4x-2",
1097	      "gpu": [
1098	        "cuda:2"
1099	      ],
1100	      "pid": "53600",
1101	      "log_path": "~/runs/struct_self_consist_ie/exp008_re_n16.log",
1102	      "submitted_at": "2026-05-14T12:15:14.917Z",
1103	      "submitted_via": "submit_training_job",
1104	      "backend": "tmux",
1105	      "account": "root",
1106	      "failure_reason": "Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)",
1107	      "wall_clock_seconds": 87984.9,
1108	      "gpu_hours": 24.44
1109	    },
1110	    "conclusion": "killed",
1111	    "completed_at": "2026-05-15T12:41:39.774Z"
1112	  },
1113	  "exp_001_n16_seed456_full": {
1114	    "status": "DONE",
1115	    "retry_count": 0,
1116	    "created_at": "2026-05-14T12:44:31.348Z",
1117	    "updated_at": "2026-05-15T12:41:30.065Z",
1118	    "spec": {
1119	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\"",
1120	      "server": "gpu-5090-4x-2",
1121	      "gpu": [
1122	        "cuda:1"
1123	      ],
1124	      "pid": "62170",
1125	      "log_path": "~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log",
1126	      "submitted_at": "2026-05-14T12:44:31.087Z",
1127	      "submitted_via": "submit_training_job",
1128	      "backend": "tmux",
1129	      "account": "root",
1130	      "failure_reason": "Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)",
1131	      "wall_clock_seconds": 86219.0,
1132	      "gpu_hours": 23.95
1133	    },
1134	    "conclusion": "killed",
1135	    "failure_reason": "superseded by v2",
1136	    "completed_at": "2026-05-15T12:41:30.065Z"
1137	  },
1138	  "exp_001_n16_seed123_full": {
1139	    "status": "DONE",
1140	    "retry_count": 0,
1141	    "created_at": "2026-05-14T12:43:47.915Z",
1142	    "updated_at": "2026-05-15T12:41:29.068Z",
1143	    "spec": {
1144	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\"",
1145	      "server": "gpu-5090-4x-2",
1146	      "gpu": [
1147	        "cuda:0"
1148	      ],
1149	      "pid": "61812",
1150	      "log_path": "~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log",
1151	      "submitted_at": "2026-05-14T12:44:06.059Z",
1152	      "submitted_via": "submit_training_job",
1153	      "backend": "tmux",
1154	      "account": "root",
1155	      "failure_reason": "Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)",
1156	      "wall_clock_seconds": 86243.0,
1157	      "gpu_hours": 23.96
1158	    },
1159	    "conclusion": "killed",
1160	    "failure_reason": "superseded by v2",
1161	    "completed_at": "2026-05-15T12:41:29.068Z"
1162	  },
1163	  "exp_002_conll_n16_r1024": {
1164	    "status": "DONE",
1165	    "retry_count": 0,
1166	    "created_at": "2026-05-14T22:16:57.682Z",
1167	    "updated_at": "2026-05-15T01:20:53.108Z",
1168	    "spec": {
1169	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.",
1170	      "parent": "exp_002_conll_n16",
1171	      "model_name": "qwen3-8b-conll2003-merged",
1172	      "dataset": "CoNLL-2003",
1173	      "seed": 42,
1174	      "server": "autodl-5090",
1175	      "command": "CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024",
1176	      "data_path": "data/conll2003",
1177	      "data_count": 3453
1178	    },
1179	    "conclusion": "killed",
1180	    "completed_at": "2026-05-15T01:20:53.108Z"
1181	  },
1182	  "exp_007_llama_n16_r1024": {
1183	    "status": "DONE",
1184	    "retry_count": 0,
1185	    "created_at": "2026-05-14T22:16:59.685Z",
1186	    "updated_at": "2026-05-15T01:20:52.194Z",
1187	    "spec": {
1188	      "hypothesis": "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.",
1189	      "parent": "exp_007_llama_n16",
1190	      "model_name": "llama3.1-8b-scierc-merged",
1191	      "dataset": "SciERC",
1192	      "seed": 42,
1193	      "server": "autodl-5090",
1194	      "command": "CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024",
1195	      "data_path": "data/scierc/processed_data",
1196	      "data_count": 9999
1197	    },
1198	    "conclusion": "killed",
1199	    "completed_at": "2026-05-15T01:20:52.194Z"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "e9953ea7-25ea-4ee5-8065-2ae73d19f088"
}
```

</details>

---


### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "usage": {
    "total_tokens": 45891,
    "tool_uses": 9,
    "duration_ms": 50281
  },
  "last_tool_name": "Read",
  "uuid": "71d0040d-a826-43e1-a138-980ebdfb62a2",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01VcK3iDccdwRpYBAAZFdhZu`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/bhxefydqt.txt",
  "offset": 1198,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "fa4fb415-22d1-4f96-a34f-7e7c545b2f46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYeAFB2h9fV1LjUoVVd8DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11661,
      "cache_read_input_tokens": 33724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11661,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 47 · 2026-05-19T07:58:34.840Z_

<details><summary>↩ Tool result · `toolu_01VcK3iDccdwRpYBAAZFdhZu`</summary>

```text
1198	    "conclusion": "killed",
1199	    "completed_at": "2026-05-15T01:20:52.194Z"
1200	  },
1201	  "exp_017_llama_conll_n16_s456": {
1202	    "status": "DONE",
1203	    "retry_count": 0,
1204	    "created_at": "2026-05-14T19:23:21.987Z",
1205	    "updated_at": "2026-05-14T20:24:45.875Z",
1206	    "hypothesis": "LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol",
1207	    "spec": {
1208	      "command": "CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456",
1209	      "server": "autodl-5090",
1210	      "data_path": "data/conll2003",
1211	      "data_count": 3453,
1212	      "model_name": "llama3.1-8b-conll2003-merged",
1213	      "seed": 456
1214	    },
1215	    "metrics": {
1216	      "greedy_f1": 0.9243,
1217	      "oracle_f1": 0.9488,
1218	      "oracle_headroom": 0.0245,
1219	      "n_instances": 3453,
1220	      "n_valid": 2756,
1221	      "n_conditional": 2642,
1222	      "structural_beats_surface": true,
1223	      "full": {
1224	        "SJ_rho": 0.4552,
1225	        "SJ_AUROC": 0.7288,
1226	        "SJ_ECE": 0.1134,
1227	        "FK_rho": 0.4478,
1228	        "FK_AUROC": 0.7248,
1229	        "FK_ECE": 0.109,
1230	        "logprob_rho": 0.3078,
1231	        "logprob_AUROC": 0.7612,
1232	        "logprob_ECE": 0.1289,
1233	        "EM_rho": 0.452,
1234	        "EM_AUROC": 0.7275,
1235	        "EM_ECE": 0.1082,
1236	        "voting_conf_rho": 0.4571,
1237	        "voting_conf_AUROC": 0.7348,
1238	        "voting_conf_ECE": 0.0863
1239	      },
1240	      "conditional": {
1241	        "SJ_rho": 0.4505,
1242	        "SJ_AUROC": 0.7449,
1243	        "SJ_ECE": 0.0826,
1244	        "FK_rho": 0.4422,
1245	        "FK_AUROC": 0.7401,
1246	        "FK_ECE": 0.0835,
1247	        "logprob_rho": 0.3242,
1248	        "logprob_AUROC": 0.8067,
1249	        "logprob_ECE": 0.0921,
1250	        "EM_rho": 0.451,
1251	        "EM_AUROC": 0.745,
1252	        "EM_ECE": 0.0756,
1253	        "voting_conf_rho": 0.3962,
1254	        "voting_conf_AUROC": 0.7202,
1255	        "voting_conf_ECE": 0.0746
1256	      },
1257	      "best_of_n": {
1258	        "greedy": 0.9243,
1259	        "random_avg": 0.9215,
1260	        "sj_best": 0.9243,
1261	        "logprob_best": 0.9243,
1262	        "voting_conf_best": 0.9243,
1263	        "oracle": 0.9488
1264	      },
1265	      "n8_vs_n16_delta": {
1266	        "full_SJ_rho_delta": 0.0238,
1267	        "full_FK_rho_delta": 0.0201,
1268	        "full_logprob_rho_delta": 0.0006,
1269	        "full_EM_rho_delta": 0.0214,
1270	        "full_voting_conf_rho_delta": 0.0315,
1271	        "cond_SJ_rho_delta": 0.0149,
1272	        "cond_FK_rho_delta": 0.0112,
1273	        "cond_logprob_rho_delta": -0.004,
1274	        "cond_EM_rho_delta": 0.0107,
1275	        "cond_voting_conf_rho_delta": 0.0219
1276	      }
1277	    },
1278	    "checkpoint_path": "output/exp_017_llama_conll_n16_s456/samples.jsonl",
1279	    "log_path": "output/exp_017_llama_conll_n16_s456/all_signals_report.json",
1280	    "conclusion": "success",
1281	    "completed_at": "2026-05-14T20:24:45.875Z"
1282	  },
1283	  "exp_017_llama_conll_n16_s123": {
1284	    "status": "DONE",
1285	    "retry_count": 0,
1286	    "created_at": "2026-05-14T19:23:21.084Z",
1287	    "updated_at": "2026-05-14T19:43:06.607Z",
1288	    "hypothesis": "LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol",
1289	    "spec": {
1290	      "hypothesis": "LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)",
1291	      "command": "CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123",
1292	      "server": "autodl-5090",
1293	      "data_path": "/root/autodl-tmp/struct_self_consist_ie/data/conll2003",
1294	      "data_count": 3453,
1295	      "model_name": "llama3.1-8b-conll2003-merged",
1296	      "seed": 123,
1297	      "checkpoint_source": "checkpoints/llama3.1-8b-conll2003-merged",
1298	      "eval_data": "data/conll2003",
1299	      "checkpoint_path": "output/exp_017_llama_conll_n16_s123/samples.jsonl",
1300	      "log_path": "output/exp_017_llama_conll_n16_s123.log"
1301	    },
1302	    "metrics": {
1303	      "greedy_f1": 0.9266,
1304	      "oracle_f1": 0.9497,
1305	      "oracle_headroom": 0.0231,
1306	      "n_instances": 3453,
1307	      "n_valid": 2756,
1308	      "n_conditional": 2642,
1309	      "structural_beats_surface": true,
1310	      "full": {
1311	        "SJ_rho": 0.4698,
1312	        "SJ_AUROC": 0.7402,
1313	        "SJ_ECE": 0.1135,
1314	        "FK_rho": 0.4594,
1315	        "FK_AUROC": 0.7351,
1316	        "FK_ECE": 0.1114,
1317	        "logprob_rho": 0.3161,
1318	        "logprob_AUROC": 0.768,
1319	        "logprob_ECE": 0.129,
1320	        "EM_rho": 0.4676,
1321	        "EM_AUROC": 0.7399,
1322	        "EM_ECE": 0.1082,
1323	        "voting_conf_rho": 0.4612,
1324	        "voting_conf_AUROC": 0.7429,
1325	        "voting_conf_ECE": 0.0832
1326	      },
1327	      "conditional": {
1328	        "SJ_rho": 0.4712,
1329	        "SJ_AUROC": 0.7609,
1330	        "SJ_ECE": 0.0828,
1331	        "FK_rho": 0.4595,
1332	        "FK_AUROC": 0.7547,
1333	        "FK_ECE": 0.0858,
1334	        "logprob_rho": 0.3314,
1335	        "logprob_AUROC": 0.8134,
1336	        "logprob_ECE": 0.0922,
1337	        "EM_rho": 0.4732,
1338	        "EM_AUROC": 0.7626,
1339	        "EM_ECE": 0.075,
1340	        "voting_conf_rho": 0.4086,
1341	        "voting_conf_AUROC": 0.7338,
1342	        "voting_conf_ECE": 0.0706
1343	      },
1344	      "best_of_n": {
1345	        "greedy": 0.9242,
1346	        "random_avg": 0.9216,
1347	        "sj_best": 0.9247,
1348	        "logprob_best": 0.9253,
1349	        "voting_conf_best": 0.9255,
1350	        "oracle": 0.9486
1351	      },
1352	      "n8_vs_n16_delta": {
1353	        "full_SJ_rho_delta": 0.0384,
1354	        "full_FK_rho_delta": 0.0317,
1355	        "full_logprob_rho_delta": 0.0089,
1356	        "full_SJ_AUROC_delta": 0.0363,
1357	        "full_FK_AUROC_delta": 0.0325,
1358	        "full_logprob_AUROC_delta": 0.007,
1359	        "cond_SJ_rho_delta": 0.0356,
1360	        "cond_FK_rho_delta": 0.0285,
1361	        "cond_logprob_rho_delta": 0.0032
1362	      }
1363	    },
1364	    "log_path": "output/exp_017_llama_conll_n16_s123.log",
1365	    "checkpoint_path": "output/exp_017_llama_conll_n16_s123/samples.jsonl",
1366	    "conclusion": "success",
1367	    "completed_at": "2026-05-14T19:43:06.607Z"
1368	  },
1369	  "exp_008_re_n16_full": {
1370	    "status": "DONE",
1371	    "retry_count": 0,
1372	    "created_at": "2026-05-14T12:45:10.852Z",
1373	    "updated_at": "2026-05-14T17:51:43.957Z",
1374	    "spec": {
1375	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\"",
1376	      "server": "gpu-5090-4x-2",
1377	      "gpu": [
1378	        "cuda:2"
1379	      ],
1380	      "pid": "62585",
1381	      "log_path": "~/runs/struct_self_consist_ie/exp_008_re_n16_full.log",
1382	      "submitted_at": "2026-05-14T12:45:10.764Z",
1383	      "submitted_via": "submit_training_job",
1384	      "backend": "tmux",
1385	      "account": "root",
1386	      "wall_clock_seconds": 18393.2,
1387	      "gpu_hours": 5.11
1388	    },
1389	    "conclusion": "killed",
1390	    "failure_reason": "superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)",
1391	    "completed_at": "2026-05-14T17:51:43.957Z"
1392	  },
1393	  "exp_001_n16_seed123": {
1394	    "status": "DONE",
1395	    "retry_count": 0,
1396	    "created_at": "2026-05-14T12:10:29.393Z",
1397	    "updated_at": "2026-05-14T12:42:58.393Z",
1398	    "spec": {
1399	      "command": "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs",
1400	      "server": "gpu-5090-4x-2",
1401	      "data_path": "data/scierc/processed_data",
1402	      "data_count": 551,
1403	      "model_name": "qwen3-8b-scierc-merged-v2",
1404	      "seed": 123,
1405	      "num_instances": 200,
1406	      "partial": true,
1407	      "note": "Only 200/551 instances due to --num_test default bug. Needs full rerun."
1408	    },
1409	    "metrics": {
1410	      "ner": {
1411	        "greedy_f1": 0.655,
1412	        "oracle_f1": 0.8028,
1413	        "headroom": 0.1478,
1414	        "rho_sj_full": 0.4076,
1415	        "rho_fk_full": 0.2799,
1416	        "rho_logprob_full": 0.3189,
1417	        "rho_sj_cond": 0.4271,
1418	        "rho_fk_cond": 0.2743,
1419	        "rho_logprob_cond": 0.2835,
1420	        "sj_beats_fk": true,
1421	        "rho_advantage": 0.1277
1422	      },
1423	      "re": {
1424	        "greedy_f1": 0.4243,
1425	        "oracle_f1": 0.6771,
1426	        "headroom": 0.2528,
1427	        "rho_sj_full": 0.2943,
1428	        "rho_fk_full": 0.2657,
1429	        "rho_logprob_full": 0.3005,
1430	        "rho_sj_cond": 0.4003,
1431	        "rho_fk_cond": 0.313,
1432	        "rho_logprob_cond": 0.2317,
1433	        "sj_beats_fk": true,
1434	        "rho_advantage": 0.0286
1435	      },
1436	      "verdict": "FAIL"
1437	    },
1438	    "conclusion": "success",
1439	    "checkpoint_path": "N/A",
1440	    "log_path": "output/exp001_n16_seed123/",
1441	    "completed_at": "2026-05-14T12:28:38.104Z"
1442	  },
1443	  "exp_001_ner_n16_scierc": {
1444	    "status": "DONE",
1445	    "retry_count": 0,
1446	    "created_at": "2026-05-14T11:42:10.898Z",
1447	    "updated_at": "2026-05-14T12:42:49.592Z",
1448	    "spec": {
1449	      "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\"",
1450	      "server": "autodl-5090",
1451	      "gpu": [
1452	        "cuda:0"
1453	      ],
1454	      "pid": "54357",
1455	      "log_path": "~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log",
1456	      "submitted_at": "2026-05-14T12:15:46.646Z",
1457	      "submitted_via": "submit_training_job",
1458	      "backend": "tmux",
1459	      "account": "root"
1460	    },
1461	    "server": "autodl-5090",
1462	    "gpu": "cuda:0",
1463	    "account": "root",
1464	    "reproduce": {
1465	      "server": "autodl-5090",
1466	      "gpu": "cuda:0",
1467	      "started_at": "2026-05-14T11:43:48.643Z"
1468	    },
1469	    "conclusion": "success",
1470	    "completed_at": "2026-05-14T11:55:45.664Z",
1471	    "metrics": {
1472	      "n_instances": 551,
1473	      "ner_n": 529,
1474	      "re_n": 397,
1475	      "N": 16,
1476	      "T": 1,
1477	      "seed": 42,
1478	      "full_test_set": true,
1479	      "ner_voting_conf_rho": 0.399,
1480	      "ner_sj_rho": 0.398,
1481	      "ner_em_rho": 0.339,
1482	      "ner_fk_rho": 0.288,
1483	      "ner_logprob_rho": 0.237,
1484	      "ner_voting_conf_auroc": 0.704,
1485	      "ner_sj_auroc": 0.697,
1486	      "ner_cond_em_rho": 0.414,
1487	      "ner_cond_sj_rho": 0.349,
1488	      "ner_cond_vc_rho": 0.34,
1489	      "re_voting_conf_rho": 0.38,
1490	      "re_logprob_rho": 0.293,
1491	      "re_fk_rho": 0.281,
1492	      "re_sj_rho": 0.277,
1493	      "re_em_rho": 0.148,
1494	      "re_voting_conf_auroc": 0.699,
1495	      "re_cond_em_rho": 0.475,
1496	      "re_cond_sj_rho": 0.318,
1497	      "re_cond_vc_rho": 0.35,
1498	      "re_cond_em_auroc": 0.742,
1499	      "diagnosis": "551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7."
1500	    }
1501	  }
1502	}
1503	
1504	--- Total matching experiment keys: 36 ---
1505	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "fd67f058-6be9-4a7a-a520-6c2fa0cd3fd8"
}
```

</details>

---


### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "description": "Running Identify n16/n_16 experiments not already in the fewnerd set",
  "usage": {
    "total_tokens": 52223,
    "tool_uses": 10,
    "duration_ms": 63929
  },
  "last_tool_name": "Bash",
  "uuid": "b8ac6b8b-b7d3-4716-b90f-db01bbba01f0",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01FYLFTVKUa3Sk69jAo1yUes`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt') as f:\n    raw = json.load(f)\n\nresult = json.loads(raw['result'])\nexperiments = result['data']['experiments']\n\n# Find all with n16 or n_16 that don't also have fewnerd\nn16_only = {}\nfewnerd_ids = set()\nn16_ids = set()\n\nfor exp_id, exp_data in experiments.items():\n    exp_id_lower = exp_id.lower()\n    name = ''\n    if isinstance(exp_data, dict):\n        name = str(exp_data.get('name', '')).lower()\n    combined = exp_id_lower + ' ' + name\n    \n    if 'fewnerd' in combined:\n        fewnerd_ids.add(exp_id)\n    if 'n16' in combined or 'n_16' in combined:\n        n16_ids.add(exp_id)\n\n# Show which n16 experiments are NOT fewnerd (already shown above)\nn16_not_fewnerd = n16_ids - fewnerd_ids\nprint('=== n16/n_16 experiments already included (also contain fewnerd): ===')\nfor eid in sorted(n16_ids & fewnerd_ids):\n    print(f'  {eid}')\n\nprint()\nprint('=== n16/n_16 experiments NOT containing fewnerd (additional matches): ===')\nfor eid in sorted(n16_not_fewnerd):\n    print(f'  {eid}')\n\nprint()\nprint(f'Total fewnerd matches: {len(fewnerd_ids)}')\nprint(f'Total n16/n_16 matches: {len(n16_ids)}')\nprint(f'n16/n_16 already in fewnerd set: {len(n16_ids & fewnerd_ids)}')\nprint(f'n16/n_16 additional (not fewnerd): {len(n16_not_fewnerd)}')\nprint(f'Grand total unique matches: {len(fewnerd_ids | n16_ids)}')\n\"\n",
  "description": "Identify n16/n_16 experiments not already in the fewnerd set"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c89bf873-7bf0-4830-8504-b900b739ec46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012oZ2udNvbDw7Djyj2aiUWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6328,
      "cache_read_input_tokens": 45385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6328,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-19T07:58:48.589Z_

<details><summary>↩ Tool result · `toolu_01FYLFTVKUa3Sk69jAo1yUes`</summary>

```text
=== n16/n_16 experiments already included (also contain fewnerd): ===
  exp_027_fewnerd_n16

=== n16/n_16 experiments NOT containing fewnerd (additional matches): ===
  exp008_re_n16
  exp_001_n16_seed123
  exp_001_n16_seed123_full
  exp_001_n16_seed456
  exp_001_n16_seed456_full
  exp_001_ner_n16_scierc
  exp_001_ner_n16_seed123
  exp_002_conll_n16
  exp_002_conll_n16_r1024
  exp_002_conll_n16_seed123
  exp_002_conll_n16_seed456
  exp_007_llama_n16
  exp_007_llama_n16_r1024
  exp_008_re_n16
  exp_008_re_n16_full
  exp_008_re_n16_t10_full
  exp_008_re_n16_v2
  exp_017_llama_conll_n16
  exp_017_llama_conll_n16_r1024
  exp_017_llama_conll_n16_s123
  exp_017_llama_conll_n16_s123_r1024
  exp_017_llama_conll_n16_s456
  exp_017_llama_conll_n16_s456_r1024

Total fewnerd matches: 13
Total n16/n_16 matches: 24
n16/n_16 already in fewnerd set: 1
n16/n_16 additional (not fewnerd): 23
Grand total unique matches: 36
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "68b97513-c5d2-48a4-a1a6-845b101c9ae6"
}
```

</details>

---


### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a37fba2a40b1ce129",
  "tool_use_id": "toolu_015m3rum4qZMnSTQyRS5scaY",
  "status": "completed",
  "output_file": "",
  "summary": "Registry FewNERD N16 lookup",
  "usage": {
    "total_tokens": 53404,
    "tool_uses": 10,
    "duration_ms": 257759
  },
  "uuid": "8be0f119-cb71-47e2-bfa6-9aa936faa3a3",
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd"
}
```

---


### Tool result

_source line 52 · 2026-05-19T08:02:02.317Z_

<details><summary>↩ Tool result · `toolu_015m3rum4qZMnSTQyRS5scaY`</summary>

```text
All 36 matching experiments have been fully extracted. Here is the complete data:

---

## Summary: 36 matching experiments (13 fewnerd + 23 n16-only + 1 overlap)

### FEWNERD experiments (13 total)

**1. exp_qwen25_32b_fewnerd**
- status: "ALLOCATED"
- retry_count: 0
- created_at: "2026-05-19T06:19:25.428Z"
- updated_at: "2026-05-19T07:52:18.591Z"
- hypothesis: "The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap."
- server: "autodl-5090"
- gpu: "cuda:0,cuda:1,cuda:2,cuda:3"
- account: "root"
- reproduce: {server: "autodl-5090", gpu: "cuda:0,cuda:1,cuda:2,cuda:3", started_at: "2026-05-19T06:47:41.246Z"}
- notes: "2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h."

**2. exp_qwen25_7b_fewnerd**
- status: "QUEUED"
- retry_count: 0
- created_at: "2026-05-19T06:41:43.121Z"
- updated_at: "2026-05-19T07:48:40.207Z"
- hypothesis: "Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale."

**3. exp_qwen25_14b_fewnerd**
- status: "ALLOCATED"
- retry_count: 0
- created_at: "2026-05-19T06:19:31.620Z"
- updated_at: "2026-05-19T06:47:43.938Z"
- hypothesis: "The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings."
- server: "autodl-5090-c"
- gpu: "cuda:0,cuda:1"
- account: "root"
- reproduce: {server: "autodl-5090-c", gpu: "cuda:0,cuda:1", started_at: "2026-05-19T06:47:43.938Z"}

**4. exp_llama_fewnerd_inference**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-19T02:18:49.938Z"
- updated_at: "2026-05-19T03:15:04.486Z"
- completed_at: "2026-05-19T03:15:04.486Z"
- hypothesis: "LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness."
- parent: "exp_llama_fewnerd_lora"
- spec: {command: "bash code/run_llama_fewnerd_inference.sh", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/", data_count: 37648, model_name: "LLaMA-3.1-8B-FewNERD-LoRA-merged", seed: "42,123,456", checkpoint_source: "exp_llama_fewnerd_lora", eval_data: "FewNERD test set", checkpoint_path: "checkpoints/llama3.1-8b-fewnerd-merged/", log_path: "logs/llama_fewnerd_inference.log"}
- metrics:
  - 3seed_mean: {greedy_f1: 0.7842, oracle_f1: 0.8843, headroom_pp: 10.01, degeneracy_pct: 23.36, lp_delta_pp: 0.36, dgs_delta_pp: -0.35}
  - seed_42: {greedy_f1: 0.7841, oracle_f1: 0.8854, degen: 27.32}
  - seed_123: {greedy_f1: 0.784, oracle_f1: 0.8839, degen: 24.63}
  - seed_456: {greedy_f1: 0.7844, oracle_f1: 0.8835, degen: 18.13}
  - signal_ranking: "LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)"
  - lp_only_positive: true
  - n_instances_gold_filtered: 32565

**5. exp_llama_fewnerd_lora**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T13:20:55.859Z"
- updated_at: "2026-05-19T01:08:20.832Z"
- completed_at: "2026-05-19T01:08:20.832Z"
- hypothesis: "LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER"
- spec: {command: "llamafactory-cli train train_config_llama_fewnerd.yaml", server: "autodl-5090", gpu: "cuda:1", pid: 137865, data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd", model_name: "LLaMA-Few-NERD-LoRA", seed: 42, log_path: "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log", run_script: "run_llama_fewnerd_train_single_gpu.sh", tmux_session: "llama_fewnerd", note: "Retroactively registered - data_count unknown, seed assumed 42"}
- checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora"
- log_path: "/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log"
- metrics: {epoch: 3, train_loss: 0.0516, eval_loss: 0.0323, train_runtime_hours: 15.35, total_steps: 24708, final_checkpoint: "checkpoint-24708", adapter_size_mb: 320}

**6. exp_031_fewnerd_t12**
- status: "DONE"
- conclusion: "killed"
- created_at: "2026-05-18T20:04:12.040Z"
- completed_at: "2026-05-19T00:30:14.652Z"
- hypothesis: "FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC"
- failure_reason: "数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。"
- notes: "T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient"

**7. exp_fewnerd_s789_n8**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T23:17:34.011Z"
- completed_at: "2026-05-18T23:18:17.902Z"
- hypothesis: "FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime."
- parent: "exp_029a"
- spec: {command: "python code/analyze_fewnerd_s789.py", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl", data_count: 37648, model_name: "Qwen3-8B (ft_002_v2)", seed: 789, checkpoint_source: "exp_021 shards", eval_data: "FewNERD test (37648 instances, 32565 gold-filtered)", checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/", log_path: "/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log"}
- metrics: {greedy_f1: 0.7478, oracle_f1: 0.8714, headroom_pp: 12.37, degen_rate: 0.1177, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", instance_count: 37648, n_valid: 32565, lp_sel_f1: 0.7614, lp_delta_pp: 1.36, lp_rho_global: 0.1788, lp_rho_cond: 0.176, dgs_f1: 0.7621, dgs_delta_pp: 1.43, dgs_vs_lp_pp: 0.07, best_signal: "LP", four_seed_mean_greedy: 0.7481, four_seed_mean_lp_delta_pp: 1.38, four_seed_lp_delta_ci95: [1.32, 1.44]}

**8. exp_021_fewnerd_n8_seed456**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T22:03:17.992Z"
- completed_at: "2026-05-18T22:04:35.573Z"
- hypothesis: "Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset."
- spec: {command: "python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd", data_count: 37648, model_name: "Qwen3-8B", seed: 456, checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456", log_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log"}
- metrics: {degen_rate: 0.1212, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", instance_count: 37648, n_valid: 32565, n_gold_empty: 5083, ner_greedy_f1: 0.7888, ner_oracle_f1: 0.881, rho_fk_ner: 0.1632, rho_sj_ner: 0.313, sample_f1_pct_zero: 19.32}

**9. exp_021_fewnerd_n8_seed123**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-18T22:03:16.735Z"
- completed_at: "2026-05-18T22:04:33.731Z"
- hypothesis: "Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset."
- spec: {command: "python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0", server: "autodl-5090", data_path: "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd", data_count: 37648, model_name: "Qwen3-8B", seed: 123, checkpoint_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123", log_path: "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log"}
- metrics: {degen_rate: 0.1312, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", instance_count: 37648, n_valid: 32565, n_gold_empty: 5083, ner_greedy_f1: 0.7885, ner_oracle_f1: 0.8892, rho_fk_ner: 0.1602, rho_sj_ner: 0.3083, sample_f1_pct_zero: 20.39}

**10. exp_027_fewnerd_n16** (also matches n16)
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-17T05:28:57.036Z"
- completed_at: "2026-05-17T05:46:48.460Z"
- hypothesis: "LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective."
- parent: "exp_021_fewnerd_full"
- spec: {model_name: "qwen3-8b-fewnerd-exp021-merged", data_path: "data/fewnerd_n16_subset/test.json", data_count: 5000, seed: 42, server: "autodl-5090", gpu: "cuda:0,cuda:1,cuda:2,cuda:3", command: "python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged ...", checkpoint_path: "output/exp_027_fewnerd_n16/sampled_results.jsonl", log_path: "output/exp_027_fewnerd_n16/"}
- metrics: {LP_delta_pp: 1.88, LP_delta_95CI: [1.41, 2.37], degen_rate: 0.0706, degen_rate_source: "unified_metrics_constant_f1_gold_filtered", greedy_f1: 0.7478, lp_sel_f1: 0.7666, oracle_f1: 0.902, headroom_pp: 15.42, all_8_types_positive: true, n_instances: 5000, N_samples: 16, bootstrap_p: "<0.001"}

**11. exp_028_fewnerd_5epoch**
- status: "DONE"
- conclusion: "negative"
- created_at: "2026-05-17T07:53:12.913Z"
- completed_at: "2026-05-17T20:29:42.274Z"
- hypothesis: "Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain."
- spec: {server: "autodl-5090", gpu: "cuda:0,1,2,3", data_path: "data/fewnerd_uie_train", data_count: 131767, model_name: "Qwen3-8B LoRA rank=32", seed: 42, log_path: "logs/exp_028_4gpu_train.log", checkpoint_path: "checkpoints/qwen3-8b-fewnerd-5epoch-lora"}
- metrics: {degeneracy_cf1_gold: 0.3133, greedy_f1: 0.7773, lp_sel_delta_pp: 0.624, lp_sel_f1: 0.7835, oracle_f1: 0.8723, within_instance_rho_mean: 0.4066, within_instance_rho_median: 0.6151}

**12. exp_021_fewnerd_full**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-16T16:33:44.079Z"
- completed_at: "2026-05-16T22:04:16.683Z"
- hypothesis: "Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics."
- parent: "exp_020_fewnerd_smoke"
- spec: {gpu: "cuda:0,cuda:1,cuda:2,cuda:3", gpu_count: 4, training_mode: "DDP", checkpoint_path: "output/exp_021_fewnerd_full/checkpoint-6177", log_path: "output/exp_021_inference/"}
- metrics: {total_steps: 6177, train_loss: 0.048, eval_loss: 0.0275, train_runtime: "3h57m", epochs: 3, final_checkpoint: "output/exp_021_fewnerd_full/checkpoint-6177", adapter_path: "output/exp_021_fewnerd_full/adapter_model.safetensors", inference_instances: 37648, inference_filtered: 32565, inference_n_samples: 8, greedy_macro_f1: 0.7478, oracle_macro_f1: 0.8719, headroom: 0.124, zero_f1_rate: 0.119, degeneracy_rate: 0.101, lp_within_range_mean: 0.0879, lp_within_range_median: 0.0662, lp_global_rho: 0.4215, lp_cond_rho: 0.4225, sj_global_rho: 0.3002, sj_cond_rho: 0.2937, fk_global_rho: 0.3132, fk_cond_rho: 0.3093, em_global_rho: 0.2871, em_cond_rho: 0.271, vc_global_rho: 0.3858, vc_cond_rho: 0.3234, lp_selection_delta_pp: 1.36, vc_selection_delta_pp: -1.79, sj_selection_delta_pp: -2.14, fk_selection_delta_pp: -2.26, em_selection_delta_pp: -3.85, lp_bootstrap_ci_95_pp: [1.18, 1.53], lp_sample_auroc: 0.5782, vc_sample_auroc: 0.5354, fk_sample_auroc: 0.521, sj_sample_auroc: 0.5197, em_sample_auroc: 0.5137, scenario: "A_partial", note: "Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics."}

**13. exp_020_fewnerd_smoke**
- status: "DONE"
- conclusion: "success"
- created_at: "2026-05-16T10:29:25.272Z"
- completed_at: "2026-05-16T16:33:59.109Z"
- hypothesis: "1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances."
- metrics: {final_loss: 0.031, total_steps: 8236, training_time: "5h54m", pilot_greedy_f1: 0.8037, pilot_instances: 200, merged_model_path: "checkpoints/qwen3-8b-fewnerd-merged"}

---

### N16 experiments (23 additional, not containing "fewnerd")

**14. exp_002_conll_n16_seed456**
- status: "DONE", conclusion: "success"
- created_at: "2026-05-18T22:03:15.720Z", completed_at: "2026-05-18T22:04:31.934Z"
- hypothesis: "Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds."
- spec: {command: "python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0", server: "autodl-5090", data_count: 3453, model_name: "Qwen3-8B", seed: 456}
- metrics: {degen_rate: 0.5544, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, ner_greedy_f1: 0.9074, ner_oracle_f1: 0.9549, rho_fk_ner: 0.4718, rho_sj_ner: 0.4819, sample_f1_pct_zero: 7.02}

**15. exp_002_conll_n16_seed123**
- status: "DONE", conclusion: "success"
- created_at: "2026-05-18T22:03:14.343Z", completed_at: "2026-05-18T22:04:29.992Z"
- hypothesis: "Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds."
- metrics: {degen_rate: 0.471, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, ner_greedy_f1: 0.9068, ner_oracle_f1: 0.9633, rho_fk_ner: 0.4524, rho_sj_ner: 0.4621, sample_f1_pct_zero: 7.54}

**16. exp_017_llama_conll_n16_s456_r1024**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-15T11:45:25.899Z"
- hypothesis: "LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction."
- spec: {model_name: "llama3.1-8b-conll2003-merged", dataset: "CoNLL-2003", seed: 456, server: "autodl-5090", gpu: "cuda:2", data_count: 3453}
- metrics: {degen_rate: 0.8672, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, parse_rate: 1, ner_greedy_f1: 0.9265, ner_oracle_f1: 0.9499, rho_fk_ner: 0.469, rho_sj_ner: 0.4734, rho_vc_ner: 0.4722, rho_em_ner: 0.4752, rho_lp_ner: 0.3099, auroc_fk_ner: 0.7408, auroc_sj_ner: 0.7428, auroc_vc_ner: 0.7495, auroc_em_ner: 0.7444, auroc_lp_ner: 0.7628, rho_note: "CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."}

**17. exp_017_llama_conll_n16_r1024**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-15T11:45:23.213Z"
- hypothesis: "LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction."
- metrics: {degen_rate: 0.8647, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, parse_rate: 1, ner_greedy_f1: 0.9265, ner_oracle_f1: 0.9499, rho_fk_ner: 0.4752, rho_sj_ner: 0.4836, rho_vc_ner: 0.4746, rho_em_ner: 0.4818, rho_lp_ner: 0.3136, auroc_fk_ner: 0.7467, auroc_sj_ner: 0.7496, auroc_vc_ner: 0.7529, auroc_em_ner: 0.7508, auroc_lp_ner: 0.7661, rho_note: "CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756)."}

**18. exp_002_conll_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T18:58:40.473Z"
- hypothesis: "CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9)."
- spec: {model_name: "qwen3-8b-conll2003-merged", seed: 42, server: "autodl-5090", data_count: 3453}
- metrics: {degen_rate: 0.4844, N: 16, dataset: "conll2003", n_instances: 3453, n_valid: 2756, n_conditional: 2614, greedy_f1: 0.907, full: {SJ_rho: 0.4496, FK_rho: 0.3928, logprob_rho: 0.3146, EM_rho: 0.4627, voting_conf_rho: 0.4286, SJ_AUROC: 0.8264, FK_AUROC: 0.7821, logprob_AUROC: 0.7531, EM_AUROC: 0.8409, voting_conf_AUROC: 0.8071, SJ_ECE: 0.0747, FK_ECE: 0.1786, logprob_ECE: 0.2031, EM_ECE: 0.0786, voting_conf_ECE: 0.529}, conditional: {SJ_rho: 0.4208, FK_rho: 0.3494, logprob_rho: 0.3756, EM_rho: 0.4658, voting_conf_rho: 0.3654, SJ_AUROC: 0.8405, FK_AUROC: 0.7819, logprob_AUROC: 0.8259, EM_AUROC: 0.8781, voting_conf_AUROC: 0.7951, SJ_ECE: 0.0982, FK_ECE: 0.1899, logprob_ECE: 0.2504, EM_ECE: 0.0997, voting_conf_ECE: 0.6096}, n8_vs_n16_delta_rho_full: {SJ: 0.0139, FK: -0.007, logprob: -0.0011, EM: 0.012, voting_conf: 0.0049}}

**19. exp_017_llama_conll_n16_s123_r1024**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-15T01:20:51.219Z"
- hypothesis: "LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation."
- notes: "Output exists on autodl-5090. Registry status corrected from killed to success."
- metrics: {degen_rate: 0.8636, degen_rate_source: "unified_metrics_constant_f1_gold_filtered"}

**20. exp_008_re_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T12:28:39.268Z"
- hypothesis: "RE N=16 initial evaluation: first relation extraction test with structural signals."
- spec: {model_name: "qwen3-8b-scierc-merged-v2", dataset: "SciERC", seed: 42, data_count: 551, num_instances: 200, partial: true, note: "Only 200/551 instances due to --num_test default bug."}
- metrics: {ner: {greedy_f1: 0.6635, oracle_f1: 0.8208, headroom: 0.1572, rho_sj_full: 0.377, rho_fk_full: 0.2508, rho_logprob_full: 0.3153, rho_sj_cond: 0.3598, rho_fk_cond: 0.2251, rho_logprob_cond: 0.2927, sj_beats_fk: true, rho_advantage: 0.1262}, re: {greedy_f1: 0.4339, oracle_f1: 0.6658, headroom: 0.2319, rho_sj_full: 0.2966, rho_fk_full: 0.2871, rho_logprob_full: 0.2986, rho_sj_cond: 0.3975, rho_fk_cond: 0.3774, rho_logprob_cond: 0.2745, sj_beats_fk: true, rho_advantage: 0.0095}, verdict: "FAIL"}

**21. exp_001_ner_n16_seed123**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T13:31:54.232Z"
- hypothesis: "SciERC NER N=16 seed=123: multi-seed validation at N=16."
- spec: {model_name: "qwen3-8b-scierc-merged-v2", seed: 123, data_count: 551}
- metrics: {ner: {greedy_f1: 0.663, oracle_f1: 0.809, headroom: 0.146, rho_sj: 0.423, rho_fk: 0.29, rho_logprob: 0.239, rho_sj_cond: 0.423, rho_fk_cond: 0.26}, re: {greedy_f1: 0.419, oracle_f1: 0.625, headroom: 0.206, rho_sj: 0.267, rho_fk: 0.315, rho_sj_cond: 0.364, rho_fk_cond: 0.331}, verdict: "FAIL", verdict_note: "RE rho_sj=0.267 < 0.40; RE >30% samples F1=0", n_instances: 551, seed: 123, N: 16, T: 1}

**22. exp_008_re_n16_t10_full**
- status: "DONE", conclusion: "negative"
- completed_at: "2026-05-14T13:44:19.577Z"
- hypothesis: "RE N=16 evaluation v2: early RE evaluation attempt."
- metrics: {ner: {rho_sj: 0.444}, re: {rho_sj: 0.248}, n_instances: 551, N: 16, T: 1, seed: 42, mode: "RE-only", source: "director_corrected"}

**23. exp_008_re_n16_v2**
- status: "DONE", conclusion: "negative"
- completed_at: "2026-05-14T15:23:35.598Z"
- hypothesis: "RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count."
- metrics: {sj_rho_full: 0.281, sj_rho_cond: 0.308, f1_zero_pct: 44.3, conclusion_note: "RE N=16 v2 negative: SJ weak, 44.3% F1=0"}

**24. exp_007_llama_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T19:03:39.163Z"
- hypothesis: "LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count."
- spec: {model_name: "llama3.1-8b-scierc-merged", seed: 42, data_count: 551}
- metrics: {N: 16, dataset: "scierc", n_instances: 551, n_valid: 529, n_conditional: 478, greedy_f1: 0.645, full: {SJ_rho: 0.3791, FK_rho: 0.3081, logprob_rho: 0.2041, EM_rho: 0.3159, voting_conf_rho: 0.4515, SJ_AUROC: 0.717, FK_AUROC: 0.6581, logprob_AUROC: 0.5656, EM_AUROC: 0.7686, voting_conf_AUROC: 0.7266}, conditional: {SJ_rho: 0.3222, FK_rho: 0.2182, logprob_rho: 0.1286, EM_rho: 0.3563, voting_conf_rho: 0.3356}, n8_vs_n16_delta_rho_full: {SJ: 0.0161, FK: -0.0185, logprob: 0.0214, EM: 0.0007, voting_conf: 0.0184}}

**25. exp_017_llama_conll_n16**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T19:45:16.265Z"
- hypothesis: "LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL."
- metrics: {greedy_f1: 0.9243, oracle_f1: 0.9487, oracle_headroom: 0.0244, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4642, FK_rho: 0.4566, logprob_rho: 0.3058, EM_rho: 0.4613, voting_conf_rho: 0.4554, SJ_AUROC: 0.7391, FK_AUROC: 0.736, logprob_AUROC: 0.7594, EM_AUROC: 0.7391, voting_conf_AUROC: 0.7406}, conditional: {SJ_rho: 0.4597, FK_rho: 0.4515, logprob_rho: 0.3193, EM_rho: 0.4618, voting_conf_rho: 0.3978}, best_of_n: {greedy: 0.9243, random_avg: 0.9213, sj_best: 0.9259, logprob_best: 0.925, voting_conf_best: 0.9268, oracle: 0.9487}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0328, full_FK_rho_delta: 0.0289, full_logprob_rho_delta: -0.0014, full_EM_rho_delta: 0.0307, full_voting_conf_rho_delta: 0.0298}}

**26. exp_001_n16_seed456**
- status: "DONE", conclusion: "success", retry_count: 1
- completed_at: "2026-05-14T12:28:38.721Z"
- hypothesis: "SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count."
- metrics: {instance_count: 551, n_valid: 529, n_gold_empty: 22, parse_rate: 1, ner_greedy_f1: 0.6617, ner_oracle_f1: 0.8075, re_greedy_f1: 0.4215, re_oracle_f1: 0.4748, rho_sj_ner: 0.4098, rho_fk_ner: 0.2723, rho_vc_ner: 0.4449, rho_em_ner: 0.3363, rho_lp_ner: 0.2415, rho_sj_re: 0.2835, rho_fk_re: 0.2929, auroc_sj_ner: 0.6823, auroc_fk_ner: 0.6179, auroc_vc_ner: 0.6981, auroc_em_ner: 0.649, auroc_lp_ner: 0.5885, rho_note: "CORRECTED 2026-05-15: old values included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529)."}
- extra.previous_failure.metrics: {ner: {greedy_f1: 0.6577, oracle_f1: 0.8129, headroom: 0.1553, rho_sj_full: 0.3297, rho_fk_full: 0.2578, rho_logprob_full: 0.2866}, re: {greedy_f1: 0.4312, oracle_f1: 0.6737, headroom: 0.2425, rho_sj_full: 0.285, rho_fk_full: 0.2372, rho_logprob_full: 0.2626}, verdict: "FAIL"}

**27. exp_017_llama_conll_n16_s456**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T20:24:45.875Z"
- hypothesis: "LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds"
- metrics: {greedy_f1: 0.9243, oracle_f1: 0.9488, oracle_headroom: 0.0245, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4552, FK_rho: 0.4478, logprob_rho: 0.3078, EM_rho: 0.452, voting_conf_rho: 0.4571}, conditional: {SJ_rho: 0.4505, FK_rho: 0.4422, logprob_rho: 0.3242, EM_rho: 0.451, voting_conf_rho: 0.3962}, best_of_n: {greedy: 0.9243, random_avg: 0.9215, sj_best: 0.9243, logprob_best: 0.9243, voting_conf_best: 0.9243, oracle: 0.9488}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0238, full_FK_rho_delta: 0.0201, full_logprob_rho_delta: 0.0006, full_EM_rho_delta: 0.0214, full_voting_conf_rho_delta: 0.0315}}

**28. exp_017_llama_conll_n16_s123**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T19:43:06.607Z"
- hypothesis: "LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds"
- metrics: {greedy_f1: 0.9266, oracle_f1: 0.9497, oracle_headroom: 0.0231, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4698, FK_rho: 0.4594, logprob_rho: 0.3161, EM_rho: 0.4676, voting_conf_rho: 0.4612}, conditional: {SJ_rho: 0.4712, FK_rho: 0.4595, logprob_rho: 0.3314, EM_rho: 0.4732, voting_conf_rho: 0.4086}, best_of_n: {greedy: 0.9242, random_avg: 0.9216, sj_best: 0.9247, logprob_best: 0.9253, voting_conf_best: 0.9255, oracle: 0.9486}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0384, full_FK_rho_delta: 0.0317, full_logprob_rho_delta: 0.0089}}

**29. exp_008_re_n16_full**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-14T17:51:43.957Z"
- failure_reason: "superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)"

**30. exp_001_n16_seed123**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T12:28:38.104Z"
- spec: {data_count: 551, model_name: "qwen3-8b-scierc-merged-v2", seed: 123, num_instances: 200, partial: true, note: "Only 200/551 instances due to --num_test default bug."}
- metrics: {ner: {greedy_f1: 0.655, oracle_f1: 0.8028, headroom: 0.1478, rho_sj_full: 0.4076, rho_fk_full: 0.2799, rho_logprob_full: 0.3189, sj_beats_fk: true, rho_advantage: 0.1277}, re: {greedy_f1: 0.4243, oracle_f1: 0.6771, headroom: 0.2528, rho_sj_full: 0.2943, rho_fk_full: 0.2657, rho_logprob_full: 0.3005, sj_beats_fk: true, rho_advantage: 0.0286}, verdict: "FAIL"}

**31. exp_001_ner_n16_scierc**
- status: "DONE", conclusion: "success"
- completed_at: "2026-05-14T11:55:45.664Z"
- metrics: {n_instances: 551, ner_n: 529, re_n: 397, N: 16, T: 1, seed: 42, full_test_set: true, ner_voting_conf_rho: 0.399, ner_sj_rho: 0.398, ner_em_rho: 0.339, ner_fk_rho: 0.288, ner_logprob_rho: 0.237, ner_voting_conf_auroc: 0.704, ner_sj_auroc: 0.697, ner_cond_em_rho: 0.414, ner_cond_sj_rho: 0.349, ner_cond_vc_rho: 0.34, re_voting_conf_rho: 0.38, re_logprob_rho: 0.293, re_fk_rho: 0.281, re_sj_rho: 0.277, re_em_rho: 0.148, re_voting_conf_auroc: 0.699, re_cond_em_rho: 0.475, re_cond_sj_rho: 0.318, re_cond_vc_rho: 0.35, re_cond_em_auroc: 0.742, diagnosis: "551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40)."}

**32. exp_002_conll_n16_r1024**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T01:20:53.108Z"
- spec: {hypothesis: "D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.", model_name: "qwen3-8b-conll2003-merged", dataset: "CoNLL-2003", seed: 42}

**33. exp_007_llama_n16_r1024**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T01:20:52.194Z"
- spec: {hypothesis: "D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.", model_name: "llama3.1-8b-scierc-merged", dataset: "SciERC", seed: 42}

**34. exp008_re_n16** (note: no underscore after "exp008")
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T12:41:39.774Z"
- failure_reason: "Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)"
- spec: {server: "gpu-5090-4x-2", wall_clock_seconds: 87984.9, gpu_hours: 24.44}

**35. exp_001_n16_seed456_full**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T12:41:30.065Z"
- failure_reason: "superseded by v2"
- spec: {server: "gpu-5090-4x-2", wall_clock_seconds: 86219.0, gpu_hours: 23.95}

**36. exp_001_n16_seed123_full**
- status: "DONE", conclusion: "killed"
- completed_at: "2026-05-15T12:41:29.068Z"
- failure_reason: "superseded by v2"
- spec: {server: "gpu-5090-4x-2", wall_clock_seconds: 86243.0, gpu_hours: 23.96}

---

### Totals

| Category | Count |
|---|---|
| fewnerd experiments | 13 |
| n16 experiments (additional) | 23 |
| Overlap (fewnerd + n16) | 1 (exp_027_fewnerd_n16) |
| **Grand total unique** | **36** |

By status: 3 ALLOCATED/QUEUED (exp_qwen25_32b_fewnerd, exp_qwen25_7b_fewnerd, exp_qwen25_14b_fewnerd), 33 DONE. By conclusion among DONE: 22 success, 3 negative, 8 killed. No experiments matched "n_16" (with underscore before 16).

agentId: a37fba2a40b1ce129 (use SendMessage with to: 'a37fba2a40b1ce129' to continue this agent)
&lt;usage>total_tokens: 65744
tool_uses: 10
duration_ms: 257762&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "bcd8d191-a5ec-461a-b7ad-4c9b0d122d4e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Parse the registry JSON file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/8a7c5621-29b1-4475-9625-e962f960c1bd/tool-results/mcp-agent-ml-research-read_registry-1779177454168.txt\n\nThis file is JSON with schema: {result: string}. The \"result\" field is itself a JSON string containing an array of experiment objects.\n\nI need ALL experiments whose exp_id or name contains \"fewnerd\" (case-insensitive). For each matching experiment, return the FULL object including all fields — especially: exp_id, status, conclusion, metrics, config, notes, and any other fields present. Quote all numeric values verbatim.\n\nAlso search for any experiment with \"n16\" or \"n_16\" in its name/id.\n\nUse jq or python to parse. Return the complete data for all matching experiments.",
    "agentId": "a37fba2a40b1ce129",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All 36 matching experiments have been fully extracted. Here is the complete data:\n\n---\n\n## Summary: 36 matching experiments (13 fewnerd + 23 n16-only + 1 overlap)\n\n### FEWNERD experiments (13 total)\n\n**1. exp_qwen25_32b_fewnerd**\n- status: \"ALLOCATED\"\n- retry_count: 0\n- created_at: \"2026-05-19T06:19:25.428Z\"\n- updated_at: \"2026-05-19T07:52:18.591Z\"\n- hypothesis: \"The correlation-selection gap (high QE correlation but no selection gain) generalizes to 32B-scale models. Qwen2.5-32B QLoRA fine-tuned on FewNERD should show the same pattern: structural signals have high ρ but fail at instance-level selection, while entity construction (θ=2/N) provides significant F1 gain. This fills the 8B→72B scale gap.\"\n- server: \"autodl-5090\"\n- gpu: \"cuda:0,cuda:1,cuda:2,cuda:3\"\n- account: \"root\"\n- reproduce: {server: \"autodl-5090\", gpu: \"cuda:0,cuda:1,cuda:2,cuda:3\", started_at: \"2026-05-19T06:47:41.246Z\"}\n- notes: \"2026-05-19 15:52 UTC: 32B model download in progress, 26GB/~65GB (~40%), 8 incomplete blobs remaining. PIDs 764902/764903 still active. Disk OK (84GB free). ETA ~1-2h.\"\n\n**2. exp_qwen25_7b_fewnerd**\n- status: \"QUEUED\"\n- retry_count: 0\n- created_at: \"2026-05-19T06:41:43.121Z\"\n- updated_at: \"2026-05-19T07:48:40.207Z\"\n- hypothesis: \"Qwen2.5-7B fine-tuned on FewNERD provides the baseline point for a pure Qwen2.5 family scale curve (7B/14B/32B/72B). This eliminates the confound of mixing Qwen2.5 and Qwen3 families when studying how the correlation-selection gap changes with model scale.\"\n\n**3. exp_qwen25_14b_fewnerd**\n- status: \"ALLOCATED\"\n- retry_count: 0\n- created_at: \"2026-05-19T06:19:31.620Z\"\n- updated_at: \"2026-05-19T06:47:43.938Z\"\n- hypothesis: \"The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.\"\n- server: \"autodl-5090-c\"\n- gpu: \"cuda:0,cuda:1\"\n- account: \"root\"\n- reproduce: {server: \"autodl-5090-c\", gpu: \"cuda:0,cuda:1\", started_at: \"2026-05-19T06:47:43.938Z\"}\n\n**4. exp_llama_fewnerd_inference**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-19T02:18:49.938Z\"\n- updated_at: \"2026-05-19T03:15:04.486Z\"\n- completed_at: \"2026-05-19T03:15:04.486Z\"\n- hypothesis: \"LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.\"\n- parent: \"exp_llama_fewnerd_lora\"\n- spec: {command: \"bash code/run_llama_fewnerd_inference.sh\", server: \"autodl-5090\", data_path: \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/\", data_count: 37648, model_name: \"LLaMA-3.1-8B-FewNERD-LoRA-merged\", seed: \"42,123,456\", checkpoint_source: \"exp_llama_fewnerd_lora\", eval_data: \"FewNERD test set\", checkpoint_path: \"checkpoints/llama3.1-8b-fewnerd-merged/\", log_path: \"logs/llama_fewnerd_inference.log\"}\n- metrics:\n  - 3seed_mean: {greedy_f1: 0.7842, oracle_f1: 0.8843, headroom_pp: 10.01, degeneracy_pct: 23.36, lp_delta_pp: 0.36, dgs_delta_pp: -0.35}\n  - seed_42: {greedy_f1: 0.7841, oracle_f1: 0.8854, degen: 27.32}\n  - seed_123: {greedy_f1: 0.784, oracle_f1: 0.8839, degen: 24.63}\n  - seed_456: {greedy_f1: 0.7844, oracle_f1: 0.8835, degen: 18.13}\n  - signal_ranking: \"LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)\"\n  - lp_only_positive: true\n  - n_instances_gold_filtered: 32565\n\n**5. exp_llama_fewnerd_lora**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-18T13:20:55.859Z\"\n- updated_at: \"2026-05-19T01:08:20.832Z\"\n- completed_at: \"2026-05-19T01:08:20.832Z\"\n- hypothesis: \"LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER\"\n- spec: {command: \"llamafactory-cli train train_config_llama_fewnerd.yaml\", server: \"autodl-5090\", gpu: \"cuda:1\", pid: 137865, data_path: \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", model_name: \"LLaMA-Few-NERD-LoRA\", seed: 42, log_path: \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", run_script: \"run_llama_fewnerd_train_single_gpu.sh\", tmux_session: \"llama_fewnerd\", note: \"Retroactively registered - data_count unknown, seed assumed 42\"}\n- checkpoint_path: \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\"\n- log_path: \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\"\n- metrics: {epoch: 3, train_loss: 0.0516, eval_loss: 0.0323, train_runtime_hours: 15.35, total_steps: 24708, final_checkpoint: \"checkpoint-24708\", adapter_size_mb: 320}\n\n**6. exp_031_fewnerd_t12**\n- status: \"DONE\"\n- conclusion: \"killed\"\n- created_at: \"2026-05-18T20:04:12.040Z\"\n- completed_at: \"2026-05-19T00:30:14.652Z\"\n- hypothesis: \"FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC\"\n- failure_reason: \"数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。\"\n- notes: \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\"\n\n**7. exp_fewnerd_s789_n8**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-18T23:17:34.011Z\"\n- completed_at: \"2026-05-18T23:18:17.902Z\"\n- hypothesis: \"FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.\"\n- parent: \"exp_029a\"\n- spec: {command: \"python code/analyze_fewnerd_s789.py\", server: \"autodl-5090\", data_path: \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl\", data_count: 37648, model_name: \"Qwen3-8B (ft_002_v2)\", seed: 789, checkpoint_source: \"exp_021 shards\", eval_data: \"FewNERD test (37648 instances, 32565 gold-filtered)\", checkpoint_path: \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/\", log_path: \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log\"}\n- metrics: {greedy_f1: 0.7478, oracle_f1: 0.8714, headroom_pp: 12.37, degen_rate: 0.1177, degen_rate_source: \"unified_metrics_constant_f1_gold_filtered\", instance_count: 37648, n_valid: 32565, lp_sel_f1: 0.7614, lp_delta_pp: 1.36, lp_rho_global: 0.1788, lp_rho_cond: 0.176, dgs_f1: 0.7621, dgs_delta_pp: 1.43, dgs_vs_lp_pp: 0.07, best_signal: \"LP\", four_seed_mean_greedy: 0.7481, four_seed_mean_lp_delta_pp: 1.38, four_seed_lp_delta_ci95: [1.32, 1.44]}\n\n**8. exp_021_fewnerd_n8_seed456**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-18T22:03:17.992Z\"\n- completed_at: \"2026-05-18T22:04:35.573Z\"\n- hypothesis: \"Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\"\n- spec: {command: \"python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0\", server: \"autodl-5090\", data_path: \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", data_count: 37648, model_name: \"Qwen3-8B\", seed: 456, checkpoint_path: \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456\", log_path: \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log\"}\n- metrics: {degen_rate: 0.1212, degen_rate_source: \"unified_metrics_constant_f1_gold_filtered\", instance_count: 37648, n_valid: 32565, n_gold_empty: 5083, ner_greedy_f1: 0.7888, ner_oracle_f1: 0.881, rho_fk_ner: 0.1632, rho_sj_ner: 0.313, sample_f1_pct_zero: 19.32}\n\n**9. exp_021_fewnerd_n8_seed123**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-18T22:03:16.735Z\"\n- completed_at: \"2026-05-18T22:04:33.731Z\"\n- hypothesis: \"Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\"\n- spec: {command: \"python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0\", server: \"autodl-5090\", data_path: \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", data_count: 37648, model_name: \"Qwen3-8B\", seed: 123, checkpoint_path: \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123\", log_path: \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log\"}\n- metrics: {degen_rate: 0.1312, degen_rate_source: \"unified_metrics_constant_f1_gold_filtered\", instance_count: 37648, n_valid: 32565, n_gold_empty: 5083, ner_greedy_f1: 0.7885, ner_oracle_f1: 0.8892, rho_fk_ner: 0.1602, rho_sj_ner: 0.3083, sample_f1_pct_zero: 20.39}\n\n**10. exp_027_fewnerd_n16** (also matches n16)\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-17T05:28:57.036Z\"\n- completed_at: \"2026-05-17T05:46:48.460Z\"\n- hypothesis: \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\"\n- parent: \"exp_021_fewnerd_full\"\n- spec: {model_name: \"qwen3-8b-fewnerd-exp021-merged\", data_path: \"data/fewnerd_n16_subset/test.json\", data_count: 5000, seed: 42, server: \"autodl-5090\", gpu: \"cuda:0,cuda:1,cuda:2,cuda:3\", command: \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged ...\", checkpoint_path: \"output/exp_027_fewnerd_n16/sampled_results.jsonl\", log_path: \"output/exp_027_fewnerd_n16/\"}\n- metrics: {LP_delta_pp: 1.88, LP_delta_95CI: [1.41, 2.37], degen_rate: 0.0706, degen_rate_source: \"unified_metrics_constant_f1_gold_filtered\", greedy_f1: 0.7478, lp_sel_f1: 0.7666, oracle_f1: 0.902, headroom_pp: 15.42, all_8_types_positive: true, n_instances: 5000, N_samples: 16, bootstrap_p: \"<0.001\"}\n\n**11. exp_028_fewnerd_5epoch**\n- status: \"DONE\"\n- conclusion: \"negative\"\n- created_at: \"2026-05-17T07:53:12.913Z\"\n- completed_at: \"2026-05-17T20:29:42.274Z\"\n- hypothesis: \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\"\n- spec: {server: \"autodl-5090\", gpu: \"cuda:0,1,2,3\", data_path: \"data/fewnerd_uie_train\", data_count: 131767, model_name: \"Qwen3-8B LoRA rank=32\", seed: 42, log_path: \"logs/exp_028_4gpu_train.log\", checkpoint_path: \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\"}\n- metrics: {degeneracy_cf1_gold: 0.3133, greedy_f1: 0.7773, lp_sel_delta_pp: 0.624, lp_sel_f1: 0.7835, oracle_f1: 0.8723, within_instance_rho_mean: 0.4066, within_instance_rho_median: 0.6151}\n\n**12. exp_021_fewnerd_full**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-16T16:33:44.079Z\"\n- completed_at: \"2026-05-16T22:04:16.683Z\"\n- hypothesis: \"Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.\"\n- parent: \"exp_020_fewnerd_smoke\"\n- spec: {gpu: \"cuda:0,cuda:1,cuda:2,cuda:3\", gpu_count: 4, training_mode: \"DDP\", checkpoint_path: \"output/exp_021_fewnerd_full/checkpoint-6177\", log_path: \"output/exp_021_inference/\"}\n- metrics: {total_steps: 6177, train_loss: 0.048, eval_loss: 0.0275, train_runtime: \"3h57m\", epochs: 3, final_checkpoint: \"output/exp_021_fewnerd_full/checkpoint-6177\", adapter_path: \"output/exp_021_fewnerd_full/adapter_model.safetensors\", inference_instances: 37648, inference_filtered: 32565, inference_n_samples: 8, greedy_macro_f1: 0.7478, oracle_macro_f1: 0.8719, headroom: 0.124, zero_f1_rate: 0.119, degeneracy_rate: 0.101, lp_within_range_mean: 0.0879, lp_within_range_median: 0.0662, lp_global_rho: 0.4215, lp_cond_rho: 0.4225, sj_global_rho: 0.3002, sj_cond_rho: 0.2937, fk_global_rho: 0.3132, fk_cond_rho: 0.3093, em_global_rho: 0.2871, em_cond_rho: 0.271, vc_global_rho: 0.3858, vc_cond_rho: 0.3234, lp_selection_delta_pp: 1.36, vc_selection_delta_pp: -1.79, sj_selection_delta_pp: -2.14, fk_selection_delta_pp: -2.26, em_selection_delta_pp: -3.85, lp_bootstrap_ci_95_pp: [1.18, 1.53], lp_sample_auroc: 0.5782, vc_sample_auroc: 0.5354, fk_sample_auroc: 0.521, sj_sample_auroc: 0.5197, em_sample_auroc: 0.5137, scenario: \"A_partial\", note: \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}\n\n**13. exp_020_fewnerd_smoke**\n- status: \"DONE\"\n- conclusion: \"success\"\n- created_at: \"2026-05-16T10:29:25.272Z\"\n- completed_at: \"2026-05-16T16:33:59.109Z\"\n- hypothesis: \"1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances.\"\n- metrics: {final_loss: 0.031, total_steps: 8236, training_time: \"5h54m\", pilot_greedy_f1: 0.8037, pilot_instances: 200, merged_model_path: \"checkpoints/qwen3-8b-fewnerd-merged\"}\n\n---\n\n### N16 experiments (23 additional, not containing \"fewnerd\")\n\n**14. exp_002_conll_n16_seed456**\n- status: \"DONE\", conclusion: \"success\"\n- created_at: \"2026-05-18T22:03:15.720Z\", completed_at: \"2026-05-18T22:04:31.934Z\"\n- hypothesis: \"Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\"\n- spec: {command: \"python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0\", server: \"autodl-5090\", data_count: 3453, model_name: \"Qwen3-8B\", seed: 456}\n- metrics: {degen_rate: 0.5544, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, ner_greedy_f1: 0.9074, ner_oracle_f1: 0.9549, rho_fk_ner: 0.4718, rho_sj_ner: 0.4819, sample_f1_pct_zero: 7.02}\n\n**15. exp_002_conll_n16_seed123**\n- status: \"DONE\", conclusion: \"success\"\n- created_at: \"2026-05-18T22:03:14.343Z\", completed_at: \"2026-05-18T22:04:29.992Z\"\n- hypothesis: \"Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\"\n- metrics: {degen_rate: 0.471, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, ner_greedy_f1: 0.9068, ner_oracle_f1: 0.9633, rho_fk_ner: 0.4524, rho_sj_ner: 0.4621, sample_f1_pct_zero: 7.54}\n\n**16. exp_017_llama_conll_n16_s456_r1024**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-15T11:45:25.899Z\"\n- hypothesis: \"LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"\n- spec: {model_name: \"llama3.1-8b-conll2003-merged\", dataset: \"CoNLL-2003\", seed: 456, server: \"autodl-5090\", gpu: \"cuda:2\", data_count: 3453}\n- metrics: {degen_rate: 0.8672, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, parse_rate: 1, ner_greedy_f1: 0.9265, ner_oracle_f1: 0.9499, rho_fk_ner: 0.469, rho_sj_ner: 0.4734, rho_vc_ner: 0.4722, rho_em_ner: 0.4752, rho_lp_ner: 0.3099, auroc_fk_ner: 0.7408, auroc_sj_ner: 0.7428, auroc_vc_ner: 0.7495, auroc_em_ner: 0.7444, auroc_lp_ner: 0.7628, rho_note: \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}\n\n**17. exp_017_llama_conll_n16_r1024**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-15T11:45:23.213Z\"\n- hypothesis: \"LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction.\"\n- metrics: {degen_rate: 0.8647, instance_count: 3453, n_valid: 2756, n_gold_empty: 697, parse_rate: 1, ner_greedy_f1: 0.9265, ner_oracle_f1: 0.9499, rho_fk_ner: 0.4752, rho_sj_ner: 0.4836, rho_vc_ner: 0.4746, rho_em_ner: 0.4818, rho_lp_ner: 0.3136, auroc_fk_ner: 0.7467, auroc_sj_ner: 0.7496, auroc_vc_ner: 0.7529, auroc_em_ner: 0.7508, auroc_lp_ner: 0.7661, rho_note: \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}\n\n**18. exp_002_conll_n16**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T18:58:40.473Z\"\n- hypothesis: \"CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).\"\n- spec: {model_name: \"qwen3-8b-conll2003-merged\", seed: 42, server: \"autodl-5090\", data_count: 3453}\n- metrics: {degen_rate: 0.4844, N: 16, dataset: \"conll2003\", n_instances: 3453, n_valid: 2756, n_conditional: 2614, greedy_f1: 0.907, full: {SJ_rho: 0.4496, FK_rho: 0.3928, logprob_rho: 0.3146, EM_rho: 0.4627, voting_conf_rho: 0.4286, SJ_AUROC: 0.8264, FK_AUROC: 0.7821, logprob_AUROC: 0.7531, EM_AUROC: 0.8409, voting_conf_AUROC: 0.8071, SJ_ECE: 0.0747, FK_ECE: 0.1786, logprob_ECE: 0.2031, EM_ECE: 0.0786, voting_conf_ECE: 0.529}, conditional: {SJ_rho: 0.4208, FK_rho: 0.3494, logprob_rho: 0.3756, EM_rho: 0.4658, voting_conf_rho: 0.3654, SJ_AUROC: 0.8405, FK_AUROC: 0.7819, logprob_AUROC: 0.8259, EM_AUROC: 0.8781, voting_conf_AUROC: 0.7951, SJ_ECE: 0.0982, FK_ECE: 0.1899, logprob_ECE: 0.2504, EM_ECE: 0.0997, voting_conf_ECE: 0.6096}, n8_vs_n16_delta_rho_full: {SJ: 0.0139, FK: -0.007, logprob: -0.0011, EM: 0.012, voting_conf: 0.0049}}\n\n**19. exp_017_llama_conll_n16_s123_r1024**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-15T01:20:51.219Z\"\n- hypothesis: \"LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation.\"\n- notes: \"Output exists on autodl-5090. Registry status corrected from killed to success.\"\n- metrics: {degen_rate: 0.8636, degen_rate_source: \"unified_metrics_constant_f1_gold_filtered\"}\n\n**20. exp_008_re_n16**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T12:28:39.268Z\"\n- hypothesis: \"RE N=16 initial evaluation: first relation extraction test with structural signals.\"\n- spec: {model_name: \"qwen3-8b-scierc-merged-v2\", dataset: \"SciERC\", seed: 42, data_count: 551, num_instances: 200, partial: true, note: \"Only 200/551 instances due to --num_test default bug.\"}\n- metrics: {ner: {greedy_f1: 0.6635, oracle_f1: 0.8208, headroom: 0.1572, rho_sj_full: 0.377, rho_fk_full: 0.2508, rho_logprob_full: 0.3153, rho_sj_cond: 0.3598, rho_fk_cond: 0.2251, rho_logprob_cond: 0.2927, sj_beats_fk: true, rho_advantage: 0.1262}, re: {greedy_f1: 0.4339, oracle_f1: 0.6658, headroom: 0.2319, rho_sj_full: 0.2966, rho_fk_full: 0.2871, rho_logprob_full: 0.2986, rho_sj_cond: 0.3975, rho_fk_cond: 0.3774, rho_logprob_cond: 0.2745, sj_beats_fk: true, rho_advantage: 0.0095}, verdict: \"FAIL\"}\n\n**21. exp_001_ner_n16_seed123**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T13:31:54.232Z\"\n- hypothesis: \"SciERC NER N=16 seed=123: multi-seed validation at N=16.\"\n- spec: {model_name: \"qwen3-8b-scierc-merged-v2\", seed: 123, data_count: 551}\n- metrics: {ner: {greedy_f1: 0.663, oracle_f1: 0.809, headroom: 0.146, rho_sj: 0.423, rho_fk: 0.29, rho_logprob: 0.239, rho_sj_cond: 0.423, rho_fk_cond: 0.26}, re: {greedy_f1: 0.419, oracle_f1: 0.625, headroom: 0.206, rho_sj: 0.267, rho_fk: 0.315, rho_sj_cond: 0.364, rho_fk_cond: 0.331}, verdict: \"FAIL\", verdict_note: \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", n_instances: 551, seed: 123, N: 16, T: 1}\n\n**22. exp_008_re_n16_t10_full**\n- status: \"DONE\", conclusion: \"negative\"\n- completed_at: \"2026-05-14T13:44:19.577Z\"\n- hypothesis: \"RE N=16 evaluation v2: early RE evaluation attempt.\"\n- metrics: {ner: {rho_sj: 0.444}, re: {rho_sj: 0.248}, n_instances: 551, N: 16, T: 1, seed: 42, mode: \"RE-only\", source: \"director_corrected\"}\n\n**23. exp_008_re_n16_v2**\n- status: \"DONE\", conclusion: \"negative\"\n- completed_at: \"2026-05-14T15:23:35.598Z\"\n- hypothesis: \"RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count.\"\n- metrics: {sj_rho_full: 0.281, sj_rho_cond: 0.308, f1_zero_pct: 44.3, conclusion_note: \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}\n\n**24. exp_007_llama_n16**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T19:03:39.163Z\"\n- hypothesis: \"LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count.\"\n- spec: {model_name: \"llama3.1-8b-scierc-merged\", seed: 42, data_count: 551}\n- metrics: {N: 16, dataset: \"scierc\", n_instances: 551, n_valid: 529, n_conditional: 478, greedy_f1: 0.645, full: {SJ_rho: 0.3791, FK_rho: 0.3081, logprob_rho: 0.2041, EM_rho: 0.3159, voting_conf_rho: 0.4515, SJ_AUROC: 0.717, FK_AUROC: 0.6581, logprob_AUROC: 0.5656, EM_AUROC: 0.7686, voting_conf_AUROC: 0.7266}, conditional: {SJ_rho: 0.3222, FK_rho: 0.2182, logprob_rho: 0.1286, EM_rho: 0.3563, voting_conf_rho: 0.3356}, n8_vs_n16_delta_rho_full: {SJ: 0.0161, FK: -0.0185, logprob: 0.0214, EM: 0.0007, voting_conf: 0.0184}}\n\n**25. exp_017_llama_conll_n16**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T19:45:16.265Z\"\n- hypothesis: \"LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL.\"\n- metrics: {greedy_f1: 0.9243, oracle_f1: 0.9487, oracle_headroom: 0.0244, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4642, FK_rho: 0.4566, logprob_rho: 0.3058, EM_rho: 0.4613, voting_conf_rho: 0.4554, SJ_AUROC: 0.7391, FK_AUROC: 0.736, logprob_AUROC: 0.7594, EM_AUROC: 0.7391, voting_conf_AUROC: 0.7406}, conditional: {SJ_rho: 0.4597, FK_rho: 0.4515, logprob_rho: 0.3193, EM_rho: 0.4618, voting_conf_rho: 0.3978}, best_of_n: {greedy: 0.9243, random_avg: 0.9213, sj_best: 0.9259, logprob_best: 0.925, voting_conf_best: 0.9268, oracle: 0.9487}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0328, full_FK_rho_delta: 0.0289, full_logprob_rho_delta: -0.0014, full_EM_rho_delta: 0.0307, full_voting_conf_rho_delta: 0.0298}}\n\n**26. exp_001_n16_seed456**\n- status: \"DONE\", conclusion: \"success\", retry_count: 1\n- completed_at: \"2026-05-14T12:28:38.721Z\"\n- hypothesis: \"SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count.\"\n- metrics: {instance_count: 551, n_valid: 529, n_gold_empty: 22, parse_rate: 1, ner_greedy_f1: 0.6617, ner_oracle_f1: 0.8075, re_greedy_f1: 0.4215, re_oracle_f1: 0.4748, rho_sj_ner: 0.4098, rho_fk_ner: 0.2723, rho_vc_ner: 0.4449, rho_em_ner: 0.3363, rho_lp_ner: 0.2415, rho_sj_re: 0.2835, rho_fk_re: 0.2929, auroc_sj_ner: 0.6823, auroc_fk_ner: 0.6179, auroc_vc_ner: 0.6981, auroc_em_ner: 0.649, auroc_lp_ner: 0.5885, rho_note: \"CORRECTED 2026-05-15: old values included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}\n- extra.previous_failure.metrics: {ner: {greedy_f1: 0.6577, oracle_f1: 0.8129, headroom: 0.1553, rho_sj_full: 0.3297, rho_fk_full: 0.2578, rho_logprob_full: 0.2866}, re: {greedy_f1: 0.4312, oracle_f1: 0.6737, headroom: 0.2425, rho_sj_full: 0.285, rho_fk_full: 0.2372, rho_logprob_full: 0.2626}, verdict: \"FAIL\"}\n\n**27. exp_017_llama_conll_n16_s456**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T20:24:45.875Z\"\n- hypothesis: \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds\"\n- metrics: {greedy_f1: 0.9243, oracle_f1: 0.9488, oracle_headroom: 0.0245, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4552, FK_rho: 0.4478, logprob_rho: 0.3078, EM_rho: 0.452, voting_conf_rho: 0.4571}, conditional: {SJ_rho: 0.4505, FK_rho: 0.4422, logprob_rho: 0.3242, EM_rho: 0.451, voting_conf_rho: 0.3962}, best_of_n: {greedy: 0.9243, random_avg: 0.9215, sj_best: 0.9243, logprob_best: 0.9243, voting_conf_best: 0.9243, oracle: 0.9488}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0238, full_FK_rho_delta: 0.0201, full_logprob_rho_delta: 0.0006, full_EM_rho_delta: 0.0214, full_voting_conf_rho_delta: 0.0315}}\n\n**28. exp_017_llama_conll_n16_s123**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T19:43:06.607Z\"\n- hypothesis: \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds\"\n- metrics: {greedy_f1: 0.9266, oracle_f1: 0.9497, oracle_headroom: 0.0231, n_instances: 3453, n_valid: 2756, structural_beats_surface: true, full: {SJ_rho: 0.4698, FK_rho: 0.4594, logprob_rho: 0.3161, EM_rho: 0.4676, voting_conf_rho: 0.4612}, conditional: {SJ_rho: 0.4712, FK_rho: 0.4595, logprob_rho: 0.3314, EM_rho: 0.4732, voting_conf_rho: 0.4086}, best_of_n: {greedy: 0.9242, random_avg: 0.9216, sj_best: 0.9247, logprob_best: 0.9253, voting_conf_best: 0.9255, oracle: 0.9486}, n8_vs_n16_delta: {full_SJ_rho_delta: 0.0384, full_FK_rho_delta: 0.0317, full_logprob_rho_delta: 0.0089}}\n\n**29. exp_008_re_n16_full**\n- status: \"DONE\", conclusion: \"killed\"\n- completed_at: \"2026-05-14T17:51:43.957Z\"\n- failure_reason: \"superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)\"\n\n**30. exp_001_n16_seed123**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T12:28:38.104Z\"\n- spec: {data_count: 551, model_name: \"qwen3-8b-scierc-merged-v2\", seed: 123, num_instances: 200, partial: true, note: \"Only 200/551 instances due to --num_test default bug.\"}\n- metrics: {ner: {greedy_f1: 0.655, oracle_f1: 0.8028, headroom: 0.1478, rho_sj_full: 0.4076, rho_fk_full: 0.2799, rho_logprob_full: 0.3189, sj_beats_fk: true, rho_advantage: 0.1277}, re: {greedy_f1: 0.4243, oracle_f1: 0.6771, headroom: 0.2528, rho_sj_full: 0.2943, rho_fk_full: 0.2657, rho_logprob_full: 0.3005, sj_beats_fk: true, rho_advantage: 0.0286}, verdict: \"FAIL\"}\n\n**31. exp_001_ner_n16_scierc**\n- status: \"DONE\", conclusion: \"success\"\n- completed_at: \"2026-05-14T11:55:45.664Z\"\n- metrics: {n_instances: 551, ner_n: 529, re_n: 397, N: 16, T: 1, seed: 42, full_test_set: true, ner_voting_conf_rho: 0.399, ner_sj_rho: 0.398, ner_em_rho: 0.339, ner_fk_rho: 0.288, ner_logprob_rho: 0.237, ner_voting_conf_auroc: 0.704, ner_sj_auroc: 0.697, ner_cond_em_rho: 0.414, ner_cond_sj_rho: 0.349, ner_cond_vc_rho: 0.34, re_voting_conf_rho: 0.38, re_logprob_rho: 0.293, re_fk_rho: 0.281, re_sj_rho: 0.277, re_em_rho: 0.148, re_voting_conf_auroc: 0.699, re_cond_em_rho: 0.475, re_cond_sj_rho: 0.318, re_cond_vc_rho: 0.35, re_cond_em_auroc: 0.742, diagnosis: \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40).\"}\n\n**32. exp_002_conll_n16_r1024**\n- status: \"DONE\", conclusion: \"killed\"\n- completed_at: \"2026-05-15T01:20:53.108Z\"\n- spec: {hypothesis: \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.\", model_name: \"qwen3-8b-conll2003-merged\", dataset: \"CoNLL-2003\", seed: 42}\n\n**33. exp_007_llama_n16_r1024**\n- status: \"DONE\", conclusion: \"killed\"\n- completed_at: \"2026-05-15T01:20:52.194Z\"\n- spec: {hypothesis: \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.\", model_name: \"llama3.1-8b-scierc-merged\", dataset: \"SciERC\", seed: 42}\n\n**34. exp008_re_n16** (note: no underscore after \"exp008\")\n- status: \"DONE\", conclusion: \"killed\"\n- completed_at: \"2026-05-15T12:41:39.774Z\"\n- failure_reason: \"Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)\"\n- spec: {server: \"gpu-5090-4x-2\", wall_clock_seconds: 87984.9, gpu_hours: 24.44}\n\n**35. exp_001_n16_seed456_full**\n- status: \"DONE\", conclusion: \"killed\"\n- completed_at: \"2026-05-15T12:41:30.065Z\"\n- failure_reason: \"superseded by v2\"\n- spec: {server: \"gpu-5090-4x-2\", wall_clock_seconds: 86219.0, gpu_hours: 23.95}\n\n**36. exp_001_n16_seed123_full**\n- status: \"DONE\", conclusion: \"killed\"\n- completed_at: \"2026-05-15T12:41:29.068Z\"\n- failure_reason: \"superseded by v2\"\n- spec: {server: \"gpu-5090-4x-2\", wall_clock_seconds: 86243.0, gpu_hours: 23.96}\n\n---\n\n### Totals\n\n| Category | Count |\n|---|---|\n| fewnerd experiments | 13 |\n| n16 experiments (additional) | 23 |\n| Overlap (fewnerd + n16) | 1 (exp_027_fewnerd_n16) |\n| **Grand total unique** | **36** |\n\nBy status: 3 ALLOCATED/QUEUED (exp_qwen25_32b_fewnerd, exp_qwen25_7b_fewnerd, exp_qwen25_14b_fewnerd), 33 DONE. By conclusion among DONE: 22 success, 3 negative, 8 killed. No experiments matched \"n_16\" (with underscore before 16)."
      }
    ],
    "totalDurationMs": 257762,
    "totalTokens": 65744,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 51713,
      "output_tokens": 12850,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12850,
          "cache_read_input_tokens": 51713,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1180,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 6,
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


### Tool result

_source line 53 · 2026-05-19T08:02:02.689Z_

<details><summary>↩ Tool result · `toolu_01Jbq7PBdFKYfFefPixp1efz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 165192\\ndrwxr-xr-x   6 root root       170 May 17 13:48 .\\ndrwxr-xr-x 183 root root     12288 May 19 15:26 ..\\n-rw-r--r--   1 root root      2207 May 17 13:48 paired_n8_baseline.json\\n-rw-r--r--   1 root root      4412 May 17 13:41 results.json\\n-rw-r--r--   1 root root 169127242 May 17 13:40 samples.jsonl\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_0\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_1\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_2\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "75ab1665-f368-4437-8b46-6b93ffb6b5ff",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 165192\\\\ndrwxr-xr-x   6 root root       170 May 17 13:48 .\\\\ndrwxr-xr-x 183 root root     12288 May 19 15:26 ..\\\\n-rw-r--r--   1 root root      2207 May 17 13:48 paired_n8_baseline.json\\\\n-rw-r--r--   1 root root      4412 May 17 13:41 results.json\\\\n-rw-r--r--   1 root root 169127242 May 17 13:40 samples.jsonl\\\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_0\\\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_1\\\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_2\\\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_3\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 165192\\ndrwxr-xr-x   6 root root       170 May 17 13:48 .\\ndrwxr-xr-x 183 root root     12288 May 19 15:26 ..\\n-rw-r--r--   1 root root      2207 May 17 13:48 paired_n8_baseline.json\\n-rw-r--r--   1 root root      4412 May 17 13:41 results.json\\n-rw-r--r--   1 root root 169127242 May 17 13:40 samples.jsonl\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_0\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_1\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_2\\ndrwxr-xr-x   2 root root        77 May 17 13:40 shard_3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-19T08:02:03.105Z_

<details><summary>↩ Tool result · `toolu_01FMhuQz2YY8SgMp1Uu9EbxY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fig: Selection gap bar chart — 3-seed n=551 data.\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\n\\nplt.rcParams.update({\\n    'font.family': 'serif',\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\n    'font.size': 9,\\n    'axes.labelsize': 9,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n    'legend.fontsize': 7.5,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'text.usetex': False,\\n})\\n\\nOUT = Path('/root/autodl-tmp/struct_self_consist_ie/output')\\nFIG_DIR = OUT / 'figures'\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\n\\nwith open(OUT / 'analysis_scierc_n16_3seed_selection_f1_merged.json') as f:\\n    merged = json.load(f)\\n\\nner_agg = merged['qwen_scierc_ner_n16']['aggregated']\\nre_agg = merged['qwen_scierc_re_n16']['aggregated']\\n\\nsignals = ['VC', 'SJ', 'FK', 'EM', 'LP']\\nsignal_labels = ['VC', 'SJ', 'FK', 'EM', 'LP']\\n\\n# Extract delta and std\\nner_delta = []\\nner_std = []\\nre_delta = []\\nre_std = []\\n\\nfor sig in signals:\\n    nd = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']\\n    ns = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']\\n    ner_delta.append(nd * 100)  # to pp\\n    ner_std.append(ns * 100)\\n\\n    rd = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']\\n    rs = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']\\n    re_delta.append(rd * 100)\\n    re_std.append(rs * 100)\\n\\nner_delta = np.array(ner_delta)\\nner_std = np.array(ner_std)\\nre_delta = np.array(re_delta)\\nre_std = np.array(re_std)\\n\\n# Colors: consistency signals (VC/SJ/FK/EM) blue family, LP orange/red\\ncolors_ner = ['#4c72b0'] * 4 + ['#dd8452']\\ncolors_re = ['#6c92d0'] * 4 + ['#e8a878']\\n\\nfig, ax = plt.subplots(figsize=(5.5, 3.0))\\n\\nx = np.arange(len(signals))\\nwidth = 0.35\\n\\nbars_ner = ax.bar(x - width/2, ner_delta, width,\\n                  yerr=ner_std, capsize=2.5, error_kw={'linewidth': 0.8},\\n                  color=[c for c in colors_ner], alpha=0.85,\\n                  edgecolor='white', linewidth=0.5, label='NER', zorder=2)\\nbars_re = ax.bar(x + width/2, re_delta, width,\\n                 yerr=re_std, capsize=2.5, error_kw={'linewidth': 0.8},\\n                 color=[c for c in colors_re], alpha=0.85,\\n                 edgecolor='white', linewidth=0.5, label='RE', zorder=2)\\n\\nax.axhline(y=0, color='black', linewidth=0.6, zorder=1)\\n\\n# Value annotations\\nfor i, (nd, rd) in enumerate(zip(ner_delta, re_delta)):\\n    y_ner = nd + (ner_std[i] + 0.15) * (1 if nd >= 0 else -1)\\n    y_re = rd + (re_std[i] + 0.15) * (1 if rd >= 0 else -1)\\n    va_ner = 'bottom' if nd >= 0 else 'top'\\n    va_re = 'bottom' if rd >= 0 else 'top'\\n    ax.text(i - width/2, y_ner, f'{nd:+.2f}', ha='center', va=va_ner,\\n            fontsize=6, fontweight='bold', color='#333333')\\n    ax.text(i + width/2, y_re, f'{rd:+.2f}', ha='center', va=va_re,\\n            fontsize=6, fontweight='bold', color='#333333')\\n\\n# Oracle/random annotations\\nner_oracle_delta = (ner_agg['oracle_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100\\nre_oracle_delta = (re_agg['oracle_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100\\nner_random_delta = (ner_agg['random_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100\\nre_random_delta = (re_agg['random_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100\\n\\nax.annotate(f'oracle: NER +{ner_oracle_delta:.1f} / RE +{re_oracle_delta:.1f} pp',\\n            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6, color='#2ca02c',\\n            ha='right', va='top',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))\\nax.annotate(f'random: NER {ner_random_delta:.1f} / RE {re_random_delta:.1f} pp',\\n            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6, color='gray',\\n            ha='right', va='bottom',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))\\n\\nax.set_xticks(x)\\nax.set_xticklabels(signal_labels)\\nax.set_ylabel('ΔF1 vs Greedy (pp)')\\nax.set_title('Selection Gap: Signal vs Greedy (SciERC, n=551, 3 seeds)', fontsize=9, fontweight='bold')\\nax.legend(loc='upper left', fontsize=7, framealpha=0.85)\\n\\ny_max = max(abs(ner_delta).max() + ner_std.max(), abs(re_delta).max() + re_std.max()) + 1.5\\nax.set_ylim(-y_max, y_max)\\nax.tick_params(labelsize=7)\\nax.grid(axis='y', alpha=0.2, linewidth=0.3)\\n\\nfig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')\\nfig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)\\nplt.close(fig)\\n\\n# Print values for verification\\nprint(\\\"=== NER Selection Gap (pp) ===\\\")\\nprint(f\\\"  greedy F1: {ner_agg['greedy_f1']['mean']:.5f}\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: Δ={ner_delta[i]:+.2f} ± {ner_std[i]:.2f}\\\")\\nprint(f\\\"  oracle delta: +{ner_oracle_delta:.2f} pp\\\")\\nprint(f\\\"  random delta: {ner_random_delta:.2f} pp\\\")\\n\\nprint(\\\"\\\\n=== RE Selection Gap (pp) ===\\\")\\nprint(f\\\"  greedy F1: {re_agg['greedy_f1']['mean']:.5f}\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: Δ={re_delta[i]:+.2f} ± {re_std[i]:.2f}\\\")\\nprint(f\\\"  oracle delta: +{re_oracle_delta:.2f} pp\\\")\\nprint(f\\\"  random delta: {re_random_delta:.2f} pp\\\")\\n\\nprint(f\\\"\\\\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}\\\")\\nprint(f\\\"Saved: {FIG_DIR / 'fig_selection_gap.png'}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8825b140-5425-4766-93d3-3d2df21dddf1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Fig: Selection gap bar chart — 3-seed n=551 data.\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport json\\\\nimport numpy as np\\\\nimport matplotlib\\\\nmatplotlib.use('Agg')\\\\nimport matplotlib.pyplot as plt\\\\nfrom pathlib import Path\\\\n\\\\nplt.rcParams.update({\\\\n    'font.family': 'serif',\\\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\\\n    'font.size': 9,\\\\n    'axes.labelsize': 9,\\\\n    'axes.titlesize': 10,\\\\n    'xtick.labelsize': 8,\\\\n    'ytick.labelsize': 8,\\\\n    'legend.fontsize': 7.5,\\\\n    'figure.dpi': 300,\\\\n    'savefig.dpi': 300,\\\\n    'savefig.bbox': 'tight',\\\\n    'savefig.pad_inches': 0.05,\\\\n    'text.usetex': False,\\\\n})\\\\n\\\\nOUT = Path('/root/autodl-tmp/struct_self_consist_ie/output')\\\\nFIG_DIR = OUT / 'figures'\\\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\\\n\\\\nwith open(OUT / 'analysis_scierc_n16_3seed_selection_f1_merged.json') as f:\\\\n    merged = json.load(f)\\\\n\\\\nner_agg = merged['qwen_scierc_ner_n16']['aggregated']\\\\nre_agg = merged['qwen_scierc_re_n16']['aggregated']\\\\n\\\\nsignals = ['VC', 'SJ', 'FK', 'EM', 'LP']\\\\nsignal_labels = ['VC', 'SJ', 'FK', 'EM', 'LP']\\\\n\\\\n# Extract delta and std\\\\nner_delta = []\\\\nner_std = []\\\\nre_delta = []\\\\nre_std = []\\\\n\\\\nfor sig in signals:\\\\n    nd = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']\\\\n    ns = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']\\\\n    ner_delta.append(nd * 100)  # to pp\\\\n    ner_std.append(ns * 100)\\\\n\\\\n    rd = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']\\\\n    rs = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']\\\\n    re_delta.append(rd * 100)\\\\n    re_std.append(rs * 100)\\\\n\\\\nner_delta = np.array(ner_delta)\\\\nner_std = np.array(ner_std)\\\\nre_delta = np.array(re_delta)\\\\nre_std = np.array(re_std)\\\\n\\\\n# Colors: consistency signals (VC/SJ/FK/EM) blue family, LP orange/red\\\\ncolors_ner = ['#4c72b0'] * 4 + ['#dd8452']\\\\ncolors_re = ['#6c92d0'] * 4 + ['#e8a878']\\\\n\\\\nfig, ax = plt.subplots(figsize=(5.5, 3.0))\\\\n\\\\nx = np.arange(len(signals))\\\\nwidth = 0.35\\\\n\\\\nbars_ner = ax.bar(x - width/2, ner_delta, width,\\\\n                  yerr=ner_std, capsize=2.5, error_kw={'linewidth': 0.8},\\\\n                  color=[c for c in colors_ner], alpha=0.85,\\\\n                  edgecolor='white', linewidth=0.5, label='NER', zorder=2)\\\\nbars_re = ax.bar(x + width/2, re_delta, width,\\\\n                 yerr=re_std, capsize=2.5, error_kw={'linewidth': 0.8},\\\\n                 color=[c for c in colors_re], alpha=0.85,\\\\n                 edgecolor='white', linewidth=0.5, label='RE', zorder=2)\\\\n\\\\nax.axhline(y=0, color='black', linewidth=0.6, zorder=1)\\\\n\\\\n# Value annotations\\\\nfor i, (nd, rd) in enumerate(zip(ner_delta, re_delta)):\\\\n    y_ner = nd + (ner_std[i] + 0.15) * (1 if nd >= 0 else -1)\\\\n    y_re = rd + (re_std[i] + 0.15) * (1 if rd >= 0 else -1)\\\\n    va_ner = 'bottom' if nd >= 0 else 'top'\\\\n    va_re = 'bottom' if rd >= 0 else 'top'\\\\n    ax.text(i - width/2, y_ner, f'{nd:+.2f}', ha='center', va=va_ner,\\\\n            fontsize=6, fontweight='bold', color='#333333')\\\\n    ax.text(i + width/2, y_re, f'{rd:+.2f}', ha='center', va=va_re,\\\\n            fontsize=6, fontweight='bold', color='#333333')\\\\n\\\\n# Oracle/random annotations\\\\nner_oracle_delta = (ner_agg['oracle_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100\\\\nre_oracle_delta = (re_agg['oracle_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100\\\\nner_random_delta = (ner_agg['random_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100\\\\nre_random_delta = (re_agg['random_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100\\\\n\\\\nax.annotate(f'oracle: NER +{ner_oracle_delta:.1f} / RE +{re_oracle_delta:.1f} pp',\\\\n            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6, color='#2ca02c',\\\\n            ha='right', va='top',\\\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))\\\\nax.annotate(f'random: NER {ner_random_delta:.1f} / RE {re_random_delta:.1f} pp',\\\\n            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6, color='gray',\\\\n            ha='right', va='bottom',\\\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))\\\\n\\\\nax.set_xticks(x)\\\\nax.set_xticklabels(signal_labels)\\\\nax.set_ylabel('ΔF1 vs Greedy (pp)')\\\\nax.set_title('Selection Gap: Signal vs Greedy (SciERC, n=551, 3 seeds)', fontsize=9, fontweight='bold')\\\\nax.legend(loc='upper left', fontsize=7, framealpha=0.85)\\\\n\\\\ny_max = max(abs(ner_delta).max() + ner_std.max(), abs(re_delta).max() + re_std.max()) + 1.5\\\\nax.set_ylim(-y_max, y_max)\\\\nax.tick_params(labelsize=7)\\\\nax.grid(axis='y', alpha=0.2, linewidth=0.3)\\\\n\\\\nfig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')\\\\nfig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)\\\\nplt.close(fig)\\\\n\\\\n# Print values for verification\\\\nprint(\\\\\\\"=== NER Selection Gap (pp) ===\\\\\\\")\\\\nprint(f\\\\\\\"  greedy F1: {ner_agg['greedy_f1']['mean']:.5f}\\\\\\\")\\\\nfor i, sig in enumerate(signals):\\\\n    print(f\\\\\\\"  {sig}: Δ={ner_delta[i]:+.2f} ± {ner_std[i]:.2f}\\\\\\\")\\\\nprint(f\\\\\\\"  oracle delta: +{ner_oracle_delta:.2f} pp\\\\\\\")\\\\nprint(f\\\\\\\"  random delta: {ner_random_delta:.2f} pp\\\\\\\")\\\\n\\\\nprint(\\\\\\\"\\\\\\\\n=== RE Selection Gap (pp) ===\\\\\\\")\\\\nprint(f\\\\\\\"  greedy F1: {re_agg['greedy_f1']['mean']:.5f}\\\\\\\")\\\\nfor i, sig in enumerate(signals):\\\\n    print(f\\\\\\\"  {sig}: Δ={re_delta[i]:+.2f} ± {re_std[i]:.2f}\\\\\\\")\\\\nprint(f\\\\\\\"  oracle delta: +{re_oracle_delta:.2f} pp\\\\\\\")\\\\nprint(f\\\\\\\"  random delta: {re_random_delta:.2f} pp\\\\\\\")\\\\n\\\\nprint(f\\\\\\\"\\\\\\\\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}\\\\\\\")\\\\nprint(f\\\\\\\"Saved: {FIG_DIR / 'fig_selection_gap.png'}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fig: Selection gap bar chart — 3-seed n=551 data.\\\"\\\"\\\"\\nimport json\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\n\\nplt.rcParams.update({\\n    'font.family': 'serif',\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\n    'font.size': 9,\\n    'axes.labelsize': 9,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n    'legend.fontsize': 7.5,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'text.usetex': False,\\n})\\n\\nOUT = Path('/root/autodl-tmp/struct_self_consist_ie/output')\\nFIG_DIR = OUT / 'figures'\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\n\\nwith open(OUT / 'analysis_scierc_n16_3seed_selection_f1_merged.json') as f:\\n    merged = json.load(f)\\n\\nner_agg = merged['qwen_scierc_ner_n16']['aggregated']\\nre_agg = merged['qwen_scierc_re_n16']['aggregated']\\n\\nsignals = ['VC', 'SJ', 'FK', 'EM', 'LP']\\nsignal_labels = ['VC', 'SJ', 'FK', 'EM', 'LP']\\n\\n# Extract delta and std\\nner_delta = []\\nner_std = []\\nre_delta = []\\nre_std = []\\n\\nfor sig in signals:\\n    nd = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']\\n    ns = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']\\n    ner_delta.append(nd * 100)  # to pp\\n    ner_std.append(ns * 100)\\n\\n    rd = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']\\n    rs = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']\\n    re_delta.append(rd * 100)\\n    re_std.append(rs * 100)\\n\\nner_delta = np.array(ner_delta)\\nner_std = np.array(ner_std)\\nre_delta = np.array(re_delta)\\nre_std = np.array(re_std)\\n\\n# Colors: consistency signals (VC/SJ/FK/EM) blue family, LP orange/red\\ncolors_ner = ['#4c72b0'] * 4 + ['#dd8452']\\ncolors_re = ['#6c92d0'] * 4 + ['#e8a878']\\n\\nfig, ax = plt.subplots(figsize=(5.5, 3.0))\\n\\nx = np.arange(len(signals))\\nwidth = 0.35\\n\\nbars_ner = ax.bar(x - width/2, ner_delta, width,\\n                  yerr=ner_std, capsize=2.5, error_kw={'linewidth': 0.8},\\n                  color=[c for c in colors_ner], alpha=0.85,\\n                  edgecolor='white', linewidth=0.5, label='NER', zorder=2)\\nbars_re = ax.bar(x + width/2, re_delta, width,\\n                 yerr=re_std, capsize=2.5, error_kw={'linewidth': 0.8},\\n                 color=[c for c in colors_re], alpha=0.85,\\n                 edgecolor='white', linewidth=0.5, label='RE', zorder=2)\\n\\nax.axhline(y=0, color='black', linewidth=0.6, zorder=1)\\n\\n# Value annotations\\nfor i, (nd, rd) in enumerate(zip(ner_delta, re_delta)):\\n    y_ner = nd + (ner_std[i] + 0.15) * (1 if nd >= 0 else -1)\\n    y_re = rd + (re_std[i] + 0.15) * (1 if rd >= 0 else -1)\\n    va_ner = 'bottom' if nd >= 0 else 'top'\\n    va_re = 'bottom' if rd >= 0 else 'top'\\n    ax.text(i - width/2, y_ner, f'{nd:+.2f}', ha='center', va=va_ner,\\n            fontsize=6, fontweight='bold', color='#333333')\\n    ax.text(i + width/2, y_re, f'{rd:+.2f}', ha='center', va=va_re,\\n            fontsize=6, fontweight='bold', color='#333333')\\n\\n# Oracle/random annotations\\nner_oracle_delta = (ner_agg['oracle_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100\\nre_oracle_delta = (re_agg['oracle_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100\\nner_random_delta = (ner_agg['random_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100\\nre_random_delta = (re_agg['random_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100\\n\\nax.annotate(f'oracle: NER +{ner_oracle_delta:.1f} / RE +{re_oracle_delta:.1f} pp',\\n            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6, color='#2ca02c',\\n            ha='right', va='top',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))\\nax.annotate(f'random: NER {ner_random_delta:.1f} / RE {re_random_delta:.1f} pp',\\n            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6, color='gray',\\n            ha='right', va='bottom',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))\\n\\nax.set_xticks(x)\\nax.set_xticklabels(signal_labels)\\nax.set_ylabel('ΔF1 vs Greedy (pp)')\\nax.set_title('Selection Gap: Signal vs Greedy (SciERC, n=551, 3 seeds)', fontsize=9, fontweight='bold')\\nax.legend(loc='upper left', fontsize=7, framealpha=0.85)\\n\\ny_max = max(abs(ner_delta).max() + ner_std.max(), abs(re_delta).max() + re_std.max()) + 1.5\\nax.set_ylim(-y_max, y_max)\\nax.tick_params(labelsize=7)\\nax.grid(axis='y', alpha=0.2, linewidth=0.3)\\n\\nfig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')\\nfig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)\\nplt.close(fig)\\n\\n# Print values for verification\\nprint(\\\"=== NER Selection Gap (pp) ===\\\")\\nprint(f\\\"  greedy F1: {ner_agg['greedy_f1']['mean']:.5f}\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: Δ={ner_delta[i]:+.2f} ± {ner_std[i]:.2f}\\\")\\nprint(f\\\"  oracle delta: +{ner_oracle_delta:.2f} pp\\\")\\nprint(f\\\"  random delta: {ner_random_delta:.2f} pp\\\")\\n\\nprint(\\\"\\\\n=== RE Selection Gap (pp) ===\\\")\\nprint(f\\\"  greedy F1: {re_agg['greedy_f1']['mean']:.5f}\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: Δ={re_delta[i]:+.2f} ± {re_std[i]:.2f}\\\")\\nprint(f\\\"  oracle delta: +{re_oracle_delta:.2f} pp\\\")\\nprint(f\\\"  random delta: {re_random_delta:.2f} pp\\\")\\n\\nprint(f\\\"\\\\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}\\\")\\nprint(f\\\"Saved: {FIG_DIR / 'fig_selection_gap.png'}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze what I've found so far:

## Task 1: FewNERD N=16 data tracing

The key experiment is **exp_027_fewnerd_n16**:
- status: DONE, conclusion: success
- data_count: **5000** (subset, not full test set)
- N_samples: 16
- metrics:
  - greedy_f1: 0.7478
  - lp_sel_f1: 0.7666
  - LP_delta_pp: 1.88
  - oracle_f1: 0.902
  - headroom_pp: 15.42
  - degen_rate: 0.0706

There's a discrepancy between what the paper claims and what the registry shows. The paper references "+0.52pp" for LP selection at N=16, but the experiment logs LP_delta_pp as 1.88—that's a significant difference I need to reconcile.

Looking at the data more carefully, I notice the N=8 experiments show an LP delta of 1.36, while N=16 shows 1.88. The difference between those is exactly 0.52, which matches the paper's claim. So the "+0.52pp" might be referring to the marginal improvement from scaling N=8 to N=16, not the absolute delta itself.

For the construction metric, I'm seeing 1.32 appears as the lower confidence bound in the N=8 results, but I need to check the exp_027 results to understand what "construction" specifically refers to in the paper's context.

Looking at the plot script for the selection gap figure, it includes five signals (VC, SJ, FK, EM, LP) and plots their selection gaps rather than ρ values directly. The caption mentions ρ, so it might be referencing correlation values from a separate analysis rather than what's shown in this particular figure. I should verify what the actual data contains for ρ.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "22d7ee71-5b76-415e-9e82-fefba6d73ac4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9Tz1Co1uT2QbJXVDaFjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16668,
      "cache_read_input_tokens": 27575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16668
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

Good data from the registry. Now I need: (1) exp_027's results.json and paired_n8_baseline.json for the exact numbers, (2) the actual figure caption in the tex file, and (3) the merged analysis data that the plot script reads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "888fc87f-27be-4d9d-b422-567c36546e2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9Tz1Co1uT2QbJXVDaFjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16668,
      "cache_read_input_tokens": 27575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16668
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018zyh1E7B6jecKnhHp3TD8R`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "3f6d492b-b1e5-4786-a838-5c815afeaab0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9Tz1Co1uT2QbJXVDaFjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16668,
      "cache_read_input_tokens": 27575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16668
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

_source line 58 · 2026-05-19T08:02:31.018Z_

<details><summary>↩ Tool result · `toolu_018zyh1E7B6jecKnhHp3TD8R`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"input\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl\\\",\\n    \\\"n_total\\\": 5000,\\n    \\\"n_filtered\\\": 4351,\\n    \\\"n_samples\\\": 16\\n  },\\n  \\\"basic\\\": {\\n    \\\"greedy_macro_f1\\\": 0.7477663070201398,\\n    \\\"oracle_macro_f1\\\": 0.9020490317710066,\\n    \\\"headroom_pp\\\": 15.428272475086679,\\n    \\\"zero_f1_rate_pct\\\": 12.066191680073546,\\n    \\\"degeneracy_rate_pct\\\": 4.52769478280855,\\n    \\\"lp_range_median\\\": 0.10055117345445004\\n  },\\n  \\\"qe\\\": {\\n    \\\"LP\\\": {\\n      \\\"auroc\\\": 0.5598,\\n      \\\"spearman_global\\\": 0.4156,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.4358,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"SJ\\\": {\\n      \\\"auroc\\\": 0.5153,\\n      \\\"spearman_global\\\": 0.3191,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.3369,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"FK\\\": {\\n      \\\"auroc\\\": 0.5164,\\n      \\\"spearman_global\\\": 0.3275,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.3462,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"EM\\\": {\\n      \\\"auroc\\\": 0.5089,\\n      \\\"spearman_global\\\": 0.3006,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.315,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"VC\\\": {\\n      \\\"auroc\\\": 0.5339,\\n      \\\"spearman_global\\\": 0.3916,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.36,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    }\\n  },\\n  \\\"selection\\\": {\\n    \\\"LP\\\": {\\n      \\\"f1\\\": 0.7666,\\n      \\\"delta_pp\\\": 1.8837\\n    },\\n    \\\"SJ\\\": {\\n      \\\"f1\\\": 0.7342,\\n      \\\"delta_pp\\\": -1.3592\\n    },\\n    \\\"FK\\\": {\\n      \\\"f1\\\": 0.7331,\\n      \\\"delta_pp\\\": -1.4674\\n    },\\n    \\\"EM\\\": {\\n      \\\"f1\\\": 0.7205,\\n      \\\"delta_pp\\\": -2.7221\\n    },\\n    \\\"VC\\\": {\\n      \\\"f1\\\": 0.7195,\\n      \\\"delta_pp\\\": -2.8233\\n    }\\n  },\\n  \\\"bootstrap\\\": {\\n    \\\"LP\\\": {\\n      \\\"mean_delta_pp\\\": 1.8835,\\n      \\\"ci_95_lo_pp\\\": 1.406,\\n      \\\"ci_95_hi_pp\\\": 2.3679,\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"SJ\\\": {\\n      \\\"mean_delta_pp\\\": -1.3651,\\n      \\\"ci_95_lo_pp\\\": -1.8902,\\n      \\\"ci_95_hi_pp\\\": -0.8533,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"FK\\\": {\\n      \\\"mean_delta_pp\\\": -1.4683,\\n      \\\"ci_95_lo_pp\\\": -2.0042,\\n      \\\"ci_95_hi_pp\\\": -0.9347,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"EM\\\": {\\n      \\\"mean_delta_pp\\\": -2.7245,\\n      \\\"ci_95_lo_pp\\\": -3.3215,\\n      \\\"ci_95_hi_pp\\\": -2.1332,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"VC\\\": {\\n      \\\"mean_delta_pp\\\": -2.819,\\n      \\\"ci_95_lo_pp\\\": -3.6386,\\n      \\\"ci_95_hi_pp\\\": -1.9959,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    }\\n  },\\n  \\\"cross_dataset\\\": {\\n    \\\"scierc\\\": {\\n      \\\"greedy\\\": 0.614,\\n      \\\"oracle\\\": 0.752,\\n      \\\"headroom\\\": 13.8,\\n      \\\"lp_rho\\\": 0.205,\\n      \\\"lp_delta\\\": 0.42\\n    },\\n    \\\"fewnerd\\\": {\\n      \\\"greedy\\\": 0.7477663070201398,\\n      \\\"oracle\\\": 0.9020490317710066,\\n      \\\"headroom\\\": 15.428272475086679,\\n      \\\"lp_rho\\\": 0.4156,\\n      \\\"lp_delta\\\": 1.8837\\n    }\\n  },\\n  \\\"entity_types\\\": {\\n    \\\"art\\\": {\\n      \\\"count\\\": 365,\\n      \\\"greedy_f1\\\": 0.7978,\\n      \\\"oracle_f1\\\": 0.8969,\\n      \\\"lp_selection_f1\\\": 0.8034,\\n      \\\"lp_delta_pp\\\": 0.5681,\\n      \\\"zero_f1_rate\\\": 7.1\\n    },\\n    \\\"building\\\": {\\n      \\\"count\\\": 479,\\n      \\\"greedy_f1\\\": 0.7409,\\n      \\\"oracle_f1\\\": 0.8952,\\n      \\\"lp_selection_f1\\\": 0.7428,\\n      \\\"lp_delta_pp\\\": 0.1931,\\n      \\\"zero_f1_rate\\\": 9.4\\n    },\\n    \\\"event\\\": {\\n      \\\"count\\\": 386,\\n      \\\"greedy_f1\\\": 0.7088,\\n      \\\"oracle_f1\\\": 0.8788,\\n      \\\"lp_selection_f1\\\": 0.7277,\\n      \\\"lp_delta_pp\\\": 1.8959,\\n      \\\"zero_f1_rate\\\": 8.8\\n    },\\n    \\\"location\\\": {\\n      \\\"count\\\": 1800,\\n      \\\"greedy_f1\\\": 0.7934,\\n      \\\"oracle_f1\\\": 0.9163,\\n      \\\"lp_selection_f1\\\": 0.8006,\\n      \\\"lp_delta_pp\\\": 0.7207,\\n      \\\"zero_f1_rate\\\": 5.6\\n    },\\n    \\\"organization\\\": {\\n      \\\"count\\\": 1560,\\n      \\\"greedy_f1\\\": 0.7589,\\n      \\\"oracle_f1\\\": 0.9069,\\n      \\\"lp_selection_f1\\\": 0.7717,\\n      \\\"lp_delta_pp\\\": 1.2776,\\n      \\\"zero_f1_rate\\\": 8.1\\n    },\\n    \\\"other\\\": {\\n      \\\"count\\\": 687,\\n      \\\"greedy_f1\\\": 0.6602,\\n      \\\"oracle_f1\\\": 0.879,\\n      \\\"lp_selection_f1\\\": 0.7066,\\n      \\\"lp_delta_pp\\\": 4.6326,\\n      \\\"zero_f1_rate\\\": 17.8\\n    },\\n    \\\"person\\\": {\\n      \\\"count\\\": 1631,\\n      \\\"greedy_f1\\\": 0.8125,\\n      \\\"oracle_f1\\\": 0.9221,\\n      \\\"lp_selection_f1\\\": 0.8225,\\n      \\\"lp_delta_pp\\\": 0.9947,\\n      \\\"zero_f1_rate\\\": 4.9\\n    },\\n    \\\"product\\\": {\\n      \\\"count\\\": 436,\\n      \\\"greedy_f1\\\": 0.707,\\n      \\\"oracle_f1\\\": 0.8736,\\n      \\\"lp_selection_f1\\\": 0.7118,\\n      \\\"lp_delta_pp\\\": 0.4777,\\n      \\\"zero_f1_rate\\\": 14.2\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "ef0aa77b-2aed-46fa-b826-51721e49c765",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"input\\\\\\\": \\\\\\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl\\\\\\\",\\\\n    \\\\\\\"n_total\\\\\\\": 5000,\\\\n    \\\\\\\"n_filtered\\\\\\\": 4351,\\\\n    \\\\\\\"n_samples\\\\\\\": 16\\\\n  },\\\\n  \\\\\\\"basic\\\\\\\": {\\\\n    \\\\\\\"greedy_macro_f1\\\\\\\": 0.7477663070201398,\\\\n    \\\\\\\"oracle_macro_f1\\\\\\\": 0.9020490317710066,\\\\n    \\\\\\\"headroom_pp\\\\\\\": 15.428272475086679,\\\\n    \\\\\\\"zero_f1_rate_pct\\\\\\\": 12.066191680073546,\\\\n    \\\\\\\"degeneracy_rate_pct\\\\\\\": 4.52769478280855,\\\\n    \\\\\\\"lp_range_median\\\\\\\": 0.10055117345445004\\\\n  },\\\\n  \\\\\\\"qe\\\\\\\": {\\\\n    \\\\\\\"LP\\\\\\\": {\\\\n      \\\\\\\"auroc\\\\\\\": 0.5598,\\\\n      \\\\\\\"spearman_global\\\\\\\": 0.4156,\\\\n      \\\\\\\"spearman_global_p\\\\\\\": 0.0,\\\\n      \\\\\\\"spearman_conditional\\\\\\\": 0.4358,\\\\n      \\\\\\\"spearman_conditional_p\\\\\\\": 0.0\\\\n    },\\\\n    \\\\\\\"SJ\\\\\\\": {\\\\n      \\\\\\\"auroc\\\\\\\": 0.5153,\\\\n      \\\\\\\"spearman_global\\\\\\\": 0.3191,\\\\n      \\\\\\\"spearman_global_p\\\\\\\": 0.0,\\\\n      \\\\\\\"spearman_conditional\\\\\\\": 0.3369,\\\\n      \\\\\\\"spearman_conditional_p\\\\\\\": 0.0\\\\n    },\\\\n    \\\\\\\"FK\\\\\\\": {\\\\n      \\\\\\\"auroc\\\\\\\": 0.5164,\\\\n      \\\\\\\"spearman_global\\\\\\\": 0.3275,\\\\n      \\\\\\\"spearman_global_p\\\\\\\": 0.0,\\\\n      \\\\\\\"spearman_conditional\\\\\\\": 0.3462,\\\\n      \\\\\\\"spearman_conditional_p\\\\\\\": 0.0\\\\n    },\\\\n    \\\\\\\"EM\\\\\\\": {\\\\n      \\\\\\\"auroc\\\\\\\": 0.5089,\\\\n      \\\\\\\"spearman_global\\\\\\\": 0.3006,\\\\n      \\\\\\\"spearman_global_p\\\\\\\": 0.0,\\\\n      \\\\\\\"spearman_conditional\\\\\\\": 0.315,\\\\n      \\\\\\\"spearman_conditional_p\\\\\\\": 0.0\\\\n    },\\\\n    \\\\\\\"VC\\\\\\\": {\\\\n      \\\\\\\"auroc\\\\\\\": 0.5339,\\\\n      \\\\\\\"spearman_global\\\\\\\": 0.3916,\\\\n      \\\\\\\"spearman_global_p\\\\\\\": 0.0,\\\\n      \\\\\\\"spearman_conditional\\\\\\\": 0.36,\\\\n      \\\\\\\"spearman_conditional_p\\\\\\\": 0.0\\\\n    }\\\\n  },\\\\n  \\\\\\\"selection\\\\\\\": {\\\\n    \\\\\\\"LP\\\\\\\": {\\\\n      \\\\\\\"f1\\\\\\\": 0.7666,\\\\n      \\\\\\\"delta_pp\\\\\\\": 1.8837\\\\n    },\\\\n    \\\\\\\"SJ\\\\\\\": {\\\\n      \\\\\\\"f1\\\\\\\": 0.7342,\\\\n      \\\\\\\"delta_pp\\\\\\\": -1.3592\\\\n    },\\\\n    \\\\\\\"FK\\\\\\\": {\\\\n      \\\\\\\"f1\\\\\\\": 0.7331,\\\\n      \\\\\\\"delta_pp\\\\\\\": -1.4674\\\\n    },\\\\n    \\\\\\\"EM\\\\\\\": {\\\\n      \\\\\\\"f1\\\\\\\": 0.7205,\\\\n      \\\\\\\"delta_pp\\\\\\\": -2.7221\\\\n    },\\\\n    \\\\\\\"VC\\\\\\\": {\\\\n      \\\\\\\"f1\\\\\\\": 0.7195,\\\\n      \\\\\\\"delta_pp\\\\\\\": -2.8233\\\\n    }\\\\n  },\\\\n  \\\\\\\"bootstrap\\\\\\\": {\\\\n    \\\\\\\"LP\\\\\\\": {\\\\n      \\\\\\\"mean_delta_pp\\\\\\\": 1.8835,\\\\n      \\\\\\\"ci_95_lo_pp\\\\\\\": 1.406,\\\\n      \\\\\\\"ci_95_hi_pp\\\\\\\": 2.3679,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant_005\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"SJ\\\\\\\": {\\\\n      \\\\\\\"mean_delta_pp\\\\\\\": -1.3651,\\\\n      \\\\\\\"ci_95_lo_pp\\\\\\\": -1.8902,\\\\n      \\\\\\\"ci_95_hi_pp\\\\\\\": -0.8533,\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant_005\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"FK\\\\\\\": {\\\\n      \\\\\\\"mean_delta_pp\\\\\\\": -1.4683,\\\\n      \\\\\\\"ci_95_lo_pp\\\\\\\": -2.0042,\\\\n      \\\\\\\"ci_95_hi_pp\\\\\\\": -0.9347,\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant_005\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"EM\\\\\\\": {\\\\n      \\\\\\\"mean_delta_pp\\\\\\\": -2.7245,\\\\n      \\\\\\\"ci_95_lo_pp\\\\\\\": -3.3215,\\\\n      \\\\\\\"ci_95_hi_pp\\\\\\\": -2.1332,\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant_005\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"VC\\\\\\\": {\\\\n      \\\\\\\"mean_delta_pp\\\\\\\": -2.819,\\\\n      \\\\\\\"ci_95_lo_pp\\\\\\\": -3.6386,\\\\n      \\\\\\\"ci_95_hi_pp\\\\\\\": -1.9959,\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant_005\\\\\\\": false\\\\n    }\\\\n  },\\\\n  \\\\\\\"cross_dataset\\\\\\\": {\\\\n    \\\\\\\"scierc\\\\\\\": {\\\\n      \\\\\\\"greedy\\\\\\\": 0.614,\\\\n      \\\\\\\"oracle\\\\\\\": 0.752,\\\\n      \\\\\\\"headroom\\\\\\\": 13.8,\\\\n      \\\\\\\"lp_rho\\\\\\\": 0.205,\\\\n      \\\\\\\"lp_delta\\\\\\\": 0.42\\\\n    },\\\\n    \\\\\\\"fewnerd\\\\\\\": {\\\\n      \\\\\\\"greedy\\\\\\\": 0.7477663070201398,\\\\n      \\\\\\\"oracle\\\\\\\": 0.9020490317710066,\\\\n      \\\\\\\"headroom\\\\\\\": 15.428272475086679,\\\\n      \\\\\\\"lp_rho\\\\\\\": 0.4156,\\\\n      \\\\\\\"lp_delta\\\\\\\": 1.8837\\\\n    }\\\\n  },\\\\n  \\\\\\\"entity_types\\\\\\\": {\\\\n    \\\\\\\"art\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 365,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.7978,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.8969,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.8034,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 0.5681,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 7.1\\\\n    },\\\\n    \\\\\\\"building\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 479,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.7409,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.8952,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.7428,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 0.1931,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 9.4\\\\n    },\\\\n    \\\\\\\"event\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 386,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.7088,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.8788,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.7277,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 1.8959,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 8.8\\\\n    },\\\\n    \\\\\\\"location\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 1800,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.7934,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.9163,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.8006,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 0.7207,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 5.6\\\\n    },\\\\n    \\\\\\\"organization\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 1560,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.7589,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.9069,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.7717,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 1.2776,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 8.1\\\\n    },\\\\n    \\\\\\\"other\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 687,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.6602,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.879,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.7066,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 4.6326,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 17.8\\\\n    },\\\\n    \\\\\\\"person\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 1631,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.8125,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.9221,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.8225,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 0.9947,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 4.9\\\\n    },\\\\n    \\\\\\\"product\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 436,\\\\n      \\\\\\\"greedy_f1\\\\\\\": 0.707,\\\\n      \\\\\\\"oracle_f1\\\\\\\": 0.8736,\\\\n      \\\\\\\"lp_selection_f1\\\\\\\": 0.7118,\\\\n      \\\\\\\"lp_delta_pp\\\\\\\": 0.4777,\\\\n      \\\\\\\"zero_f1_rate\\\\\\\": 14.2\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"input\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl\\\",\\n    \\\"n_total\\\": 5000,\\n    \\\"n_filtered\\\": 4351,\\n    \\\"n_samples\\\": 16\\n  },\\n  \\\"basic\\\": {\\n    \\\"greedy_macro_f1\\\": 0.7477663070201398,\\n    \\\"oracle_macro_f1\\\": 0.9020490317710066,\\n    \\\"headroom_pp\\\": 15.428272475086679,\\n    \\\"zero_f1_rate_pct\\\": 12.066191680073546,\\n    \\\"degeneracy_rate_pct\\\": 4.52769478280855,\\n    \\\"lp_range_median\\\": 0.10055117345445004\\n  },\\n  \\\"qe\\\": {\\n    \\\"LP\\\": {\\n      \\\"auroc\\\": 0.5598,\\n      \\\"spearman_global\\\": 0.4156,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.4358,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"SJ\\\": {\\n      \\\"auroc\\\": 0.5153,\\n      \\\"spearman_global\\\": 0.3191,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.3369,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"FK\\\": {\\n      \\\"auroc\\\": 0.5164,\\n      \\\"spearman_global\\\": 0.3275,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.3462,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"EM\\\": {\\n      \\\"auroc\\\": 0.5089,\\n      \\\"spearman_global\\\": 0.3006,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.315,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    },\\n    \\\"VC\\\": {\\n      \\\"auroc\\\": 0.5339,\\n      \\\"spearman_global\\\": 0.3916,\\n      \\\"spearman_global_p\\\": 0.0,\\n      \\\"spearman_conditional\\\": 0.36,\\n      \\\"spearman_conditional_p\\\": 0.0\\n    }\\n  },\\n  \\\"selection\\\": {\\n    \\\"LP\\\": {\\n      \\\"f1\\\": 0.7666,\\n      \\\"delta_pp\\\": 1.8837\\n    },\\n    \\\"SJ\\\": {\\n      \\\"f1\\\": 0.7342,\\n      \\\"delta_pp\\\": -1.3592\\n    },\\n    \\\"FK\\\": {\\n      \\\"f1\\\": 0.7331,\\n      \\\"delta_pp\\\": -1.4674\\n    },\\n    \\\"EM\\\": {\\n      \\\"f1\\\": 0.7205,\\n      \\\"delta_pp\\\": -2.7221\\n    },\\n    \\\"VC\\\": {\\n      \\\"f1\\\": 0.7195,\\n      \\\"delta_pp\\\": -2.8233\\n    }\\n  },\\n  \\\"bootstrap\\\": {\\n    \\\"LP\\\": {\\n      \\\"mean_delta_pp\\\": 1.8835,\\n      \\\"ci_95_lo_pp\\\": 1.406,\\n      \\\"ci_95_hi_pp\\\": 2.3679,\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant_005\\\": true\\n    },\\n    \\\"SJ\\\": {\\n      \\\"mean_delta_pp\\\": -1.3651,\\n      \\\"ci_95_lo_pp\\\": -1.8902,\\n      \\\"ci_95_hi_pp\\\": -0.8533,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"FK\\\": {\\n      \\\"mean_delta_pp\\\": -1.4683,\\n      \\\"ci_95_lo_pp\\\": -2.0042,\\n      \\\"ci_95_hi_pp\\\": -0.9347,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"EM\\\": {\\n      \\\"mean_delta_pp\\\": -2.7245,\\n      \\\"ci_95_lo_pp\\\": -3.3215,\\n      \\\"ci_95_hi_pp\\\": -2.1332,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    },\\n    \\\"VC\\\": {\\n      \\\"mean_delta_pp\\\": -2.819,\\n      \\\"ci_95_lo_pp\\\": -3.6386,\\n      \\\"ci_95_hi_pp\\\": -1.9959,\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant_005\\\": false\\n    }\\n  },\\n  \\\"cross_dataset\\\": {\\n    \\\"scierc\\\": {\\n      \\\"greedy\\\": 0.614,\\n      \\\"oracle\\\": 0.752,\\n      \\\"headroom\\\": 13.8,\\n      \\\"lp_rho\\\": 0.205,\\n      \\\"lp_delta\\\": 0.42\\n    },\\n    \\\"fewnerd\\\": {\\n      \\\"greedy\\\": 0.7477663070201398,\\n      \\\"oracle\\\": 0.9020490317710066,\\n      \\\"headroom\\\": 15.428272475086679,\\n      \\\"lp_rho\\\": 0.4156,\\n      \\\"lp_delta\\\": 1.8837\\n    }\\n  },\\n  \\\"entity_types\\\": {\\n    \\\"art\\\": {\\n      \\\"count\\\": 365,\\n      \\\"greedy_f1\\\": 0.7978,\\n      \\\"oracle_f1\\\": 0.8969,\\n      \\\"lp_selection_f1\\\": 0.8034,\\n      \\\"lp_delta_pp\\\": 0.5681,\\n      \\\"zero_f1_rate\\\": 7.1\\n    },\\n    \\\"building\\\": {\\n      \\\"count\\\": 479,\\n      \\\"greedy_f1\\\": 0.7409,\\n      \\\"oracle_f1\\\": 0.8952,\\n      \\\"lp_selection_f1\\\": 0.7428,\\n      \\\"lp_delta_pp\\\": 0.1931,\\n      \\\"zero_f1_rate\\\": 9.4\\n    },\\n    \\\"event\\\": {\\n      \\\"count\\\": 386,\\n      \\\"greedy_f1\\\": 0.7088,\\n      \\\"oracle_f1\\\": 0.8788,\\n      \\\"lp_selection_f1\\\": 0.7277,\\n      \\\"lp_delta_pp\\\": 1.8959,\\n      \\\"zero_f1_rate\\\": 8.8\\n    },\\n    \\\"location\\\": {\\n      \\\"count\\\": 1800,\\n      \\\"greedy_f1\\\": 0.7934,\\n      \\\"oracle_f1\\\": 0.9163,\\n      \\\"lp_selection_f1\\\": 0.8006,\\n      \\\"lp_delta_pp\\\": 0.7207,\\n      \\\"zero_f1_rate\\\": 5.6\\n    },\\n    \\\"organization\\\": {\\n      \\\"count\\\": 1560,\\n      \\\"greedy_f1\\\": 0.7589,\\n      \\\"oracle_f1\\\": 0.9069,\\n      \\\"lp_selection_f1\\\": 0.7717,\\n      \\\"lp_delta_pp\\\": 1.2776,\\n      \\\"zero_f1_rate\\\": 8.1\\n    },\\n    \\\"other\\\": {\\n      \\\"count\\\": 687,\\n      \\\"greedy_f1\\\": 0.6602,\\n      \\\"oracle_f1\\\": 0.879,\\n      \\\"lp_selection_f1\\\": 0.7066,\\n      \\\"lp_delta_pp\\\": 4.6326,\\n      \\\"zero_f1_rate\\\": 17.8\\n    },\\n    \\\"person\\\": {\\n      \\\"count\\\": 1631,\\n      \\\"greedy_f1\\\": 0.8125,\\n      \\\"oracle_f1\\\": 0.9221,\\n      \\\"lp_selection_f1\\\": 0.8225,\\n      \\\"lp_delta_pp\\\": 0.9947,\\n      \\\"zero_f1_rate\\\": 4.9\\n    },\\n    \\\"product\\\": {\\n      \\\"count\\\": 436,\\n      \\\"greedy_f1\\\": 0.707,\\n      \\\"oracle_f1\\\": 0.8736,\\n      \\\"lp_selection_f1\\\": 0.7118,\\n      \\\"lp_delta_pp\\\": 0.4777,\\n      \\\"zero_f1_rate\\\": 14.2\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011aKHqVg2b463DywJp58i87`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/paired_n8_baseline.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "ed7547f4-da4e-4576-8ed1-8fe297136250",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9Tz1Co1uT2QbJXVDaFjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16668,
      "cache_read_input_tokens": 27575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16668
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

_source line 60 · 2026-05-19T08:02:31.839Z_

<details><summary>↩ Tool result · `toolu_011aKHqVg2b463DywJp58i87`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"description\\\": \\\"Paired N=8 baseline (exp-021 filtered to exp-027 5000 instances)\\\",\\n    \\\"n_instances\\\": 4351,\\n    \\\"n_matched\\\": 5000,\\n    \\\"n_missing\\\": 0,\\n    \\\"greedy_mismatch_count\\\": 52\\n  },\\n  \\\"n8\\\": {\\n    \\\"greedy_f1\\\": 0.7478,\\n    \\\"lp_sel_f1\\\": 0.7614,\\n    \\\"lp_delta_pp\\\": 1.37,\\n    \\\"oracle_f1\\\": 0.8692,\\n    \\\"degeneracy_rate_pct\\\": 11.08,\\n    \\\"spearman_rho\\\": 0.6226,\\n    \\\"bootstrap\\\": {\\n      \\\"ci_95_lo_pp\\\": 0.884,\\n      \\\"ci_95_hi_pp\\\": 1.8639,\\n      \\\"p_value\\\": 0.0\\n    }\\n  },\\n  \\\"n16\\\": {\\n    \\\"greedy_f1\\\": 0.7476,\\n    \\\"lp_sel_f1\\\": 0.7664,\\n    \\\"lp_delta_pp\\\": 1.88,\\n    \\\"oracle_f1\\\": 0.9019,\\n    \\\"degeneracy_rate_pct\\\": 4.53,\\n    \\\"spearman_rho\\\": 0.6248\\n  },\\n  \\\"paired_bootstrap\\\": {\\n    \\\"point_estimate_pp\\\": 0.5169,\\n    \\\"ci_95_lo_pp\\\": 0.1721,\\n    \\\"ci_95_hi_pp\\\": 0.8712,\\n    \\\"p_value\\\": 0.0034,\\n    \\\"significant_005\\\": true,\\n    \\\"conclusion\\\": \\\"LP selection SCALES with N (significant)\\\"\\n  },\\n  \\\"per_type\\\": {\\n    \\\"art\\\": {\\n      \\\"count\\\": 167,\\n      \\\"degen_pct_n8\\\": 24.0,\\n      \\\"lp_delta_pp_n8\\\": -0.27,\\n      \\\"lp_delta_pp_n16\\\": 0.96,\\n      \\\"improvement_pp\\\": 1.24\\n    },\\n    \\\"building\\\": {\\n      \\\"count\\\": 240,\\n      \\\"degen_pct_n8\\\": 4.6,\\n      \\\"lp_delta_pp_n8\\\": -1.07,\\n      \\\"lp_delta_pp_n16\\\": -0.45,\\n      \\\"improvement_pp\\\": 0.63\\n    },\\n    \\\"event\\\": {\\n      \\\"count\\\": 151,\\n      \\\"degen_pct_n8\\\": 6.0,\\n      \\\"lp_delta_pp_n8\\\": 2.91,\\n      \\\"lp_delta_pp_n16\\\": 4.24,\\n      \\\"improvement_pp\\\": 1.33\\n    },\\n    \\\"location\\\": {\\n      \\\"count\\\": 1015,\\n      \\\"degen_pct_n8\\\": 12.4,\\n      \\\"lp_delta_pp_n8\\\": 0.97,\\n      \\\"lp_delta_pp_n16\\\": 0.76,\\n      \\\"improvement_pp\\\": -0.21\\n    },\\n    \\\"organization\\\": {\\n      \\\"count\\\": 902,\\n      \\\"degen_pct_n8\\\": 6.7,\\n      \\\"lp_delta_pp_n8\\\": 0.82,\\n      \\\"lp_delta_pp_n16\\\": 1.98,\\n      \\\"improvement_pp\\\": 1.17\\n    },\\n    \\\"other\\\": {\\n      \\\"count\\\": 502,\\n      \\\"degen_pct_n8\\\": 7.4,\\n      \\\"lp_delta_pp_n8\\\": 4.93,\\n      \\\"lp_delta_pp_n16\\\": 6.19,\\n      \\\"improvement_pp\\\": 1.26\\n    },\\n    \\\"person\\\": {\\n      \\\"count\\\": 1071,\\n      \\\"degen_pct_n8\\\": 16.2,\\n      \\\"lp_delta_pp_n8\\\": 1.52,\\n      \\\"lp_delta_pp_n16\\\": 1.42,\\n      \\\"improvement_pp\\\": -0.1\\n    },\\n    \\\"product\\\": {\\n      \\\"count\\\": 303,\\n      \\\"degen_pct_n8\\\": 8.6,\\n      \\\"lp_delta_pp_n8\\\": -0.04,\\n      \\\"lp_delta_pp_n16\\\": 1.02,\\n      \\\"improvement_pp\\\": 1.06\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "820964b8-7b49-45f5-9e18-ba5fba538b7b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"meta\\\\\\\": {\\\\n    \\\\\\\"description\\\\\\\": \\\\\\\"Paired N=8 baseline (exp-021 filtered to exp-027 5000 instances)\\\\\\\",\\\\n    \\\\\\\"n_instances\\\\\\\": 4351,\\\\n    \\\\\\\"n_matched\\\\\\\": 5000,\\\\n    \\\\\\\"n_missing\\\\\\\": 0,\\\\n    \\\\\\\"greedy_mismatch_count\\\\\\\": 52\\\\n  },\\\\n  \\\\\\\"n8\\\\\\\": {\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.7478,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 0.7614,\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": 1.37,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.8692,\\\\n    \\\\\\\"degeneracy_rate_pct\\\\\\\": 11.08,\\\\n    \\\\\\\"spearman_rho\\\\\\\": 0.6226,\\\\n    \\\\\\\"bootstrap\\\\\\\": {\\\\n      \\\\\\\"ci_95_lo_pp\\\\\\\": 0.884,\\\\n      \\\\\\\"ci_95_hi_pp\\\\\\\": 1.8639,\\\\n      \\\\\\\"p_value\\\\\\\": 0.0\\\\n    }\\\\n  },\\\\n  \\\\\\\"n16\\\\\\\": {\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.7476,\\\\n    \\\\\\\"lp_sel_f1\\\\\\\": 0.7664,\\\\n    \\\\\\\"lp_delta_pp\\\\\\\": 1.88,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.9019,\\\\n    \\\\\\\"degeneracy_rate_pct\\\\\\\": 4.53,\\\\n    \\\\\\\"spearman_rho\\\\\\\": 0.6248\\\\n  },\\\\n  \\\\\\\"paired_bootstrap\\\\\\\": {\\\\n    \\\\\\\"point_estimate_pp\\\\\\\": 0.5169,\\\\n    \\\\\\\"ci_95_lo_pp\\\\\\\": 0.1721,\\\\n    \\\\\\\"ci_95_hi_pp\\\\\\\": 0.8712,\\\\n    \\\\\\\"p_value\\\\\\\": 0.0034,\\\\n    \\\\\\\"significant_005\\\\\\\": true,\\\\n    \\\\\\\"conclusion\\\\\\\": \\\\\\\"LP selection SCALES with N (significant)\\\\\\\"\\\\n  },\\\\n  \\\\\\\"per_type\\\\\\\": {\\\\n    \\\\\\\"art\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 167,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 24.0,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": -0.27,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 0.96,\\\\n      \\\\\\\"improvement_pp\\\\\\\": 1.24\\\\n    },\\\\n    \\\\\\\"building\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 240,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 4.6,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": -1.07,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": -0.45,\\\\n      \\\\\\\"improvement_pp\\\\\\\": 0.63\\\\n    },\\\\n    \\\\\\\"event\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 151,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 6.0,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": 2.91,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 4.24,\\\\n      \\\\\\\"improvement_pp\\\\\\\": 1.33\\\\n    },\\\\n    \\\\\\\"location\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 1015,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 12.4,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": 0.97,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 0.76,\\\\n      \\\\\\\"improvement_pp\\\\\\\": -0.21\\\\n    },\\\\n    \\\\\\\"organization\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 902,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 6.7,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": 0.82,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 1.98,\\\\n      \\\\\\\"improvement_pp\\\\\\\": 1.17\\\\n    },\\\\n    \\\\\\\"other\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 502,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 7.4,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": 4.93,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 6.19,\\\\n      \\\\\\\"improvement_pp\\\\\\\": 1.26\\\\n    },\\\\n    \\\\\\\"person\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 1071,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 16.2,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": 1.52,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 1.42,\\\\n      \\\\\\\"improvement_pp\\\\\\\": -0.1\\\\n    },\\\\n    \\\\\\\"product\\\\\\\": {\\\\n      \\\\\\\"count\\\\\\\": 303,\\\\n      \\\\\\\"degen_pct_n8\\\\\\\": 8.6,\\\\n      \\\\\\\"lp_delta_pp_n8\\\\\\\": -0.04,\\\\n      \\\\\\\"lp_delta_pp_n16\\\\\\\": 1.02,\\\\n      \\\\\\\"improvement_pp\\\\\\\": 1.06\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"description\\\": \\\"Paired N=8 baseline (exp-021 filtered to exp-027 5000 instances)\\\",\\n    \\\"n_instances\\\": 4351,\\n    \\\"n_matched\\\": 5000,\\n    \\\"n_missing\\\": 0,\\n    \\\"greedy_mismatch_count\\\": 52\\n  },\\n  \\\"n8\\\": {\\n    \\\"greedy_f1\\\": 0.7478,\\n    \\\"lp_sel_f1\\\": 0.7614,\\n    \\\"lp_delta_pp\\\": 1.37,\\n    \\\"oracle_f1\\\": 0.8692,\\n    \\\"degeneracy_rate_pct\\\": 11.08,\\n    \\\"spearman_rho\\\": 0.6226,\\n    \\\"bootstrap\\\": {\\n      \\\"ci_95_lo_pp\\\": 0.884,\\n      \\\"ci_95_hi_pp\\\": 1.8639,\\n      \\\"p_value\\\": 0.0\\n    }\\n  },\\n  \\\"n16\\\": {\\n    \\\"greedy_f1\\\": 0.7476,\\n    \\\"lp_sel_f1\\\": 0.7664,\\n    \\\"lp_delta_pp\\\": 1.88,\\n    \\\"oracle_f1\\\": 0.9019,\\n    \\\"degeneracy_rate_pct\\\": 4.53,\\n    \\\"spearman_rho\\\": 0.6248\\n  },\\n  \\\"paired_bootstrap\\\": {\\n    \\\"point_estimate_pp\\\": 0.5169,\\n    \\\"ci_95_lo_pp\\\": 0.1721,\\n    \\\"ci_95_hi_pp\\\": 0.8712,\\n    \\\"p_value\\\": 0.0034,\\n    \\\"significant_005\\\": true,\\n    \\\"conclusion\\\": \\\"LP selection SCALES with N (significant)\\\"\\n  },\\n  \\\"per_type\\\": {\\n    \\\"art\\\": {\\n      \\\"count\\\": 167,\\n      \\\"degen_pct_n8\\\": 24.0,\\n      \\\"lp_delta_pp_n8\\\": -0.27,\\n      \\\"lp_delta_pp_n16\\\": 0.96,\\n      \\\"improvement_pp\\\": 1.24\\n    },\\n    \\\"building\\\": {\\n      \\\"count\\\": 240,\\n      \\\"degen_pct_n8\\\": 4.6,\\n      \\\"lp_delta_pp_n8\\\": -1.07,\\n      \\\"lp_delta_pp_n16\\\": -0.45,\\n      \\\"improvement_pp\\\": 0.63\\n    },\\n    \\\"event\\\": {\\n      \\\"count\\\": 151,\\n      \\\"degen_pct_n8\\\": 6.0,\\n      \\\"lp_delta_pp_n8\\\": 2.91,\\n      \\\"lp_delta_pp_n16\\\": 4.24,\\n      \\\"improvement_pp\\\": 1.33\\n    },\\n    \\\"location\\\": {\\n      \\\"count\\\": 1015,\\n      \\\"degen_pct_n8\\\": 12.4,\\n      \\\"lp_delta_pp_n8\\\": 0.97,\\n      \\\"lp_delta_pp_n16\\\": 0.76,\\n      \\\"improvement_pp\\\": -0.21\\n    },\\n    \\\"organization\\\": {\\n      \\\"count\\\": 902,\\n      \\\"degen_pct_n8\\\": 6.7,\\n      \\\"lp_delta_pp_n8\\\": 0.82,\\n      \\\"lp_delta_pp_n16\\\": 1.98,\\n      \\\"improvement_pp\\\": 1.17\\n    },\\n    \\\"other\\\": {\\n      \\\"count\\\": 502,\\n      \\\"degen_pct_n8\\\": 7.4,\\n      \\\"lp_delta_pp_n8\\\": 4.93,\\n      \\\"lp_delta_pp_n16\\\": 6.19,\\n      \\\"improvement_pp\\\": 1.26\\n    },\\n    \\\"person\\\": {\\n      \\\"count\\\": 1071,\\n      \\\"degen_pct_n8\\\": 16.2,\\n      \\\"lp_delta_pp_n8\\\": 1.52,\\n      \\\"lp_delta_pp_n16\\\": 1.42,\\n      \\\"improvement_pp\\\": -0.1\\n    },\\n    \\\"product\\\": {\\n      \\\"count\\\": 303,\\n      \\\"degen_pct_n8\\\": 8.6,\\n      \\\"lp_delta_pp_n8\\\": -0.04,\\n      \\\"lp_delta_pp_n16\\\": 1.02,\\n      \\\"improvement_pp\\\": 1.06\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Grep · `toolu_01PGUcM6bbRSouBkvc751QAH`</summary>

```json
{
  "pattern": "fig_selection_gap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "1ecc4ec8-f5fb-43a2-9fa8-c56a1bf39a79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9Tz1Co1uT2QbJXVDaFjh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16668,
      "cache_read_input_tokens": 27575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16668
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

_source line 62 · 2026-05-19T08:02:33.512Z_

<details><summary>↩ Tool result · `toolu_01PGUcM6bbRSouBkvc751QAH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-140-The oracle gap of 18.7~pp (0.561 vs.\ 0.374) indicates substantially more per-instance variance than NER.
artifacts/_project/paper/experiments.tex-141-Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-142-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-143-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-144-\centering
artifacts/_project/paper/experiments.tex:145:\includegraphics[width=\columnwidth]{figures/fig_selection_gap}
artifacts/_project/paper/experiments.tex-146-\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}
artifacts/_project/paper/experiments.tex-147-\label{fig:selection_gap}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-148-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-149-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-150-\paragraph{Quality estimation $\neq$ output selection.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-83-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-84-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-85-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-86-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-87-\centering
docs/paper/sections/experiments.tex:88:\includegraphics[width=\columnwidth]{fig_selection_gap}
docs/paper/sections/experiments.tex-89-\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show quality estimation $\rho$; the line with error bars shows $\Delta$F1 vs.\ greedy. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}
docs/paper/sections/experiments.tex-90-\label{fig:selection_gap}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-91-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-92-
docs/paper/sections/experiments.tex-93-Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-309-On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
docs/paper/sections/appendix.tex-310-On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-311-
docs/paper/sections/appendix.tex-312-\section{Diversity and Selection Analysis}\label{app:diversity}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-313-
docs/paper/sections/appendix.tex:314:% fig_selection_gap promoted to main text (\S\ref{sec:selection_gap})
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-315-
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-316-\paragraph{Output diversity quantification.}
docs/paper/sections/appendix.tex-317-Table~\ref{tab:diversity} summarizes output diversity across configurations.
docs/paper/sections/appendix.tex-318-On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-319-LLaMA shows similar diversity (39\% unique, F1 std 0.11).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "00895c1d-1b8a-4e1d-9f02-9964fe213ee1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-140-The oracle gap of 18.7~pp (0.561 vs.\\ 0.374) indicates substantially more per-instance variance than NER.\nartifacts/_project/paper/experiments.tex-141-Log-probability's success here may stem from its per-token nature: unlike instance-level consistency signals, logprob evaluates each sample independently, enabling it to distinguish a particularly successful extraction from its peers even when all extractions share similar structural consistency.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-142-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-143-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-144-\\centering\nartifacts/_project/paper/experiments.tex:145:\\includegraphics[width=\\columnwidth]{figures/fig_selection_gap}\nartifacts/_project/paper/experiments.tex-146-\\caption{The correlation-selection gap on SciERC ($N{=}8$). Left: strong QE correlation (Spearman $\\rho$ up to 0.50). Right: negligible selection gains (best-of-$N$ F1 at or below greedy). Dashed line indicates greedy baseline.}\nartifacts/_project/paper/experiments.tex-147-\\label{fig:selection_gap}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-148-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-149-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex-150-\\paragraph{Quality estimation $\\neq$ output selection.}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-83-\\end{tabular}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-84-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-85-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-86-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-87-\\centering\ndocs/paper/sections/experiments.tex:88:\\includegraphics[width=\\columnwidth]{fig_selection_gap}\ndocs/paper/sections/experiments.tex-89-\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show quality estimation $\\rho$; the line with error bars shows $\\Delta$F1 vs.\\ greedy. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\ndocs/paper/sections/experiments.tex-90-\\label{fig:selection_gap}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-91-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex-92-\ndocs/paper/sections/experiments.tex-93-Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-309-On SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\ndocs/paper/sections/appendix.tex-310-On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-311-\ndocs/paper/sections/appendix.tex-312-\\section{Diversity and Selection Analysis}\\label{app:diversity}\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-313-\ndocs/paper/sections/appendix.tex:314:% fig_selection_gap promoted to main text (\\S\\ref{sec:selection_gap})\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-315-\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-316-\\paragraph{Output diversity quantification.}\ndocs/paper/sections/appendix.tex-317-Table~\\ref{tab:diversity} summarizes output diversity across configurations.\ndocs/paper/sections/appendix.tex-318-On SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\n/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex-319-LLaMA shows similar diversity (39\\% unique, F1 std 0.11).",
    "numLines": 35
  }
}
```

</details>

---


### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key data. Let me analyze:

## Task 1: FewNERD N=16 data tracing

From exp_027_fewnerd_n16 results.json:
- **5000 instances** (subset), 4351 after gold filtering
- LP_delta_pp: **1.88** (not 0.52)
- greedy_f1: 0.7478, oracle_f1: 0.902

From paired_n8_baseline.json:
- N=8 LP delta: 1.37pp
- N=16 LP delta: 1.88pp  


- **Paired bootstrap point estimate: 0.5169pp** (CI: [0.172, 0.871])

So the "+0.52pp" in experiments.tex is actually the paired difference between N=16 and N=8 LP selection, representing the incremental gain from doubling N rather than the absolute LP delta. For the "construction +1.32pp" mentioned in experiments.tex, I need to check if this appears elsewhere since it's not in the exp_027 results, though the registry shows exp_fewnerd_s789_n8 has related entries.

Looking at the confidence interval bounds, 1.32 appears to be the lower CI bound for seed_lp_delta. But "construction" likely refers to entity construction (θ=2/N or DGS) rather than LP selection itself. Let me trace back to the actual caption in the active docs version to understand what this "+1.32pp" is measuring.

The caption describes a dual-axis plot where bars represent quality estimation ρ (up to 0.38) and a line with error bars shows ΔF1 versus greedy, but the plotting script I'm looking at only generates ΔF1 bars. There's a mismatch between what the caption describes and what the script actually produces—I need to find the correct plotting script that creates this dual visualization. version of the script that generates the actual figure used in the paper.

Let me check what the current figure file looks like and if there's another plot script.

Actually wait - there are 4 plot scripts:
- plot_selection_gap_1024.py
- plot_selection_gap_3seed.py  
- plot_selection_gap_n8.py
- plot_selection_gap_single.py

The one I read (3seed) only plots ΔF1 bars. The caption in the paper mentions "Bars show quality estimation ρ; the line with error bars shows ΔF1." So either:
1. A different script generates the actual figure, or
2. The caption doesn't match the figure

I need to check all the scripts and find the one that actually generates the current fig_selection_gap.

Now I'm looking at the experiments.tex file around lines 143 and 212 to understand the FewNERD claims better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "fba7a254-98a5-4525-a4b4-f46019a1adcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZY9iTCZ9Lxgti282e2wBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8103,
      "cache_read_input_tokens": 44243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8103
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

_source line 64_

Found the key data. Now I need to check: (1) the experiments.tex lines with the FewNERD N=16 claims, (2) the other plot scripts, and (3) the actual figure data source for ρ values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "3e1b84d0-5033-486f-b183-80667401db7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZY9iTCZ9Lxgti282e2wBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8103,
      "cache_read_input_tokens": 44243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8103
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

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01QusQBh6Q9HPpMnoDtYxnHo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 130,
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
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "a1e57f3d-db95-45fc-b6eb-a498d10235c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZY9iTCZ9Lxgti282e2wBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8103,
      "cache_read_input_tokens": 44243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8103
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

_source line 66 · 2026-05-19T08:02:57.631Z_

<details><summary>↩ Tool result · `toolu_01QusQBh6Q9HPpMnoDtYxnHo`</summary>

```text
130	
131	\paragraph{Degeneracy alone does not predict LP selection direction.}
132	Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP (Few-NERD per-entity-type $\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
133	Cross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\rho{\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\rho{\approx}0.26$, even at matched duration $\rho{=}0.319$; Table~\ref{tab:epoch_scierc}) does not.
134	Conditional analysis on the favorable subset yields $+2.47$~pp on SciERC but remains negative on CoNLL (Appendix~\ref{app:conditional_decomp}).
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139	\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
140	\label{fig:degeneracy_scatter}
141	\end{figure}
142	
143	LP selection gains scale with $N$ (Few-NERD $N{=}16$: $+0.52$~pp, $p{=}0.003$; Appendix~\ref{app:n_scaling}); structural signals remain negative regardless of sample budget.
144	
145	%% ============================================================
146	\subsection{Robustness}
147	\label{sec:robustness_main}
148	
149	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
150	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\approx}0.028$; Table~\ref{tab:ranking-stability}).
151	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
157	\label{tab:scale_ablation}
158	\begin{tabular}{@{}ll cc r@{}}
159	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "394cf608-a45e-489c-89ef-fcdea0ecd62f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP (Few-NERD per-entity-type $\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\\rho{\\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\\rho{\\approx}0.26$, even at matched duration $\\rho{=}0.319$; Table~\\ref{tab:epoch_scierc}) does not.\nConditional analysis on the favorable subset yields $+2.47$~pp on SciERC but remains negative on CoNLL (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nLP selection gains scale with $N$ (Few-NERD $N{=}16$: $+0.52$~pp, $p{=}0.003$; Appendix~\\ref{app:n_scaling}); structural signals remain negative regardless of sample budget.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule",
      "numLines": 30,
      "startLine": 130,
      "totalLines": 228
    }
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_013BXKeiRmpLzeza7ZJmYmpo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 200,
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
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "bccf385a-18dc-4f6b-a131-e63b214c9ca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZY9iTCZ9Lxgti282e2wBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8103,
      "cache_read_input_tokens": 44243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8103
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

_source line 68 · 2026-05-19T08:02:58.519Z_

<details><summary>↩ Tool result · `toolu_013BXKeiRmpLzeza7ZJmYmpo`</summary>

```text
200	\midrule
201	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
202	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
203	\addlinespace
204	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
205	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
206	\addlinespace
207	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
208	\bottomrule
209	\end{tabular}}
210	\end{table}
211	
212	LP-weighted construction significantly improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), with LP-weighted gains positive across all 7 seed-dataset combinations, recovering approximately 8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no significant gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures.
213	Construction gains scale with $N$: at $N{=}16$ on Few-NERD, $\Delta$ rises to $+1.32$\,pp (seed-42; Appendix~\ref{app:n_scaling}), as more samples provide broader entity coverage.
214	
215	\paragraph{Construction and LP selection are complementary.}
216	Construction dominates on SciERC ($+1.02$\,pp vs.\ LP selection $+0.04{\pm}0.48$\,pp, not significant), where LP-quality alignment is weak (within-instance $\rho{\approx}0.2$).
217	On Few-NERD, both methods yield comparable gains (construction $+1.40$\,pp, LP selection $+1.39$\,pp; Tables~\ref{tab:entity_construction}, \ref{tab:fewnerd}), where alignment is strong ($\rho{\approx}0.5$--$0.7$).
218	The gating criterion is LP-quality alignment: when alignment is weak, construction is the only effective strategy; when alignment is strong, both methods succeed.
219	
220	\paragraph{LP-alignment gating.}
221	We probe 50 held-out validation instances to estimate within-instance $\rho(\text{LP}, \text{F1})$. Above threshold $0.3$, LP selection is applied; below it, entity construction is used instead; when construction yields negative gain (as on CoNLL), the protocol defaults to greedy decoding. Adjusted $\rho$ scores on the dev split (SciERC $0.167$, CoNLL $0.065$, Few-NERD $0.516$) correctly route all three datasets, with dev-set routing matching test-set routing 3/3. This preliminary protocol requires further validation with larger validation sets. Two caveats apply: (a) the protocol is validated on three datasets with large inter-dataset margins; (b) on high-degeneracy datasets (CoNLL, valid ratio 22\%), the adjusted score magnitude is noisy but the routing decision remains robust due to wide margin from the $0.3$ threshold.
222	
223	\paragraph{Selective prediction.}
224	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, retaining high-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; VC strongest on Qwen, model-dependent on LLaMA; Table~\ref{tab:cross_selection}).
225	When selection fails, QE scores route low-confidence instances to human review.
226	
227	\phantomsection\label{sec:selection_results}
228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "d7f1cfc1-2f72-46f9-bbdc-d74646e8bfa5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction significantly improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), with LP-weighted gains positive across all 7 seed-dataset combinations, recovering approximately 8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no significant gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures.\nConstruction gains scale with $N$: at $N{=}16$ on Few-NERD, $\\Delta$ rises to $+1.32$\\,pp (seed-42; Appendix~\\ref{app:n_scaling}), as more samples provide broader entity coverage.\n\n\\paragraph{Construction and LP selection are complementary.}\nConstruction dominates on SciERC ($+1.02$\\,pp vs.\\ LP selection $+0.04{\\pm}0.48$\\,pp, not significant), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, both methods yield comparable gains (construction $+1.40$\\,pp, LP selection $+1.39$\\,pp; Tables~\\ref{tab:entity_construction}, \\ref{tab:fewnerd}), where alignment is strong ($\\rho{\\approx}0.5$--$0.7$).\nThe gating criterion is LP-quality alignment: when alignment is weak, construction is the only effective strategy; when alignment is strong, both methods succeed.\n\n\\paragraph{LP-alignment gating.}\nWe probe 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above threshold $0.3$, LP selection is applied; below it, entity construction is used instead; when construction yields negative gain (as on CoNLL), the protocol defaults to greedy decoding. Adjusted $\\rho$ scores on the dev split (SciERC $0.167$, CoNLL $0.065$, Few-NERD $0.516$) correctly route all three datasets, with dev-set routing matching test-set routing 3/3. This preliminary protocol requires further validation with larger validation sets. Two caveats apply: (a) the protocol is validated on three datasets with large inter-dataset margins; (b) on high-degeneracy datasets (CoNLL, valid ratio 22\\%), the adjusted score magnitude is noisy but the routing decision remains robust due to wide margin from the $0.3$ threshold.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, retaining high-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; VC strongest on Qwen, model-dependent on LLaMA; Table~\\ref{tab:cross_selection}).\nWhen selection fails, QE scores route low-confidence instances to human review.\n\n\\phantomsection\\label{sec:selection_results}\n",
      "numLines": 29,
      "startLine": 200,
      "totalLines": 228
    }
  }
}
```

</details>

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LchfwZa78zwqPRrphe9oCr`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_n8.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "405d7826-578d-443f-a9a7-e32de595aed2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZY9iTCZ9Lxgti282e2wBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8103,
      "cache_read_input_tokens": 44243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8103
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

_source line 70 · 2026-05-19T08:03:00.350Z_

<details><summary>↩ Tool result · `toolu_01LchfwZa78zwqPRrphe9oCr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fig: Selection gap bar chart — N=8 NER, 3-seed, Director-confirmed deltas.\\\"\\\"\\\"\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\n\\nplt.rcParams.update({\\n    'font.family': 'serif',\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\n    'font.size': 9,\\n    'axes.labelsize': 9,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n    'legend.fontsize': 7.5,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'text.usetex': False,\\n})\\n\\nFIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\n\\n# --- Director-confirmed NER N=8 delta (pp, vs greedy, 3-seed) ---\\nsignals = ['VC', 'SJ', 'FK', 'EM', 'LP']\\nner_delta = np.array([-2.540, -0.433, -0.438, -1.145, +0.038])\\n\\n# Std from analysis_multiseed_selection_f1.json (qwen_scierc_ner_n8, delta_vs_greedy_std * 100)\\nner_std = np.array([0.842, 0.985, 0.927, 0.705, 0.480])\\n\\n# Oracle/random from same JSON\\ngreedy_mean = 0.64583\\noracle_mean = 0.77637\\nrandom_mean = 0.60688\\noracle_delta = (oracle_mean - greedy_mean) * 100  # +13.05 pp\\nrandom_delta = (random_mean - greedy_mean) * 100  # -3.90 pp\\n\\n# Colors: structural signals blue, LP orange\\ncolors = ['#4c72b0'] * 4 + ['#dd8452']\\n\\nfig, ax = plt.subplots(figsize=(4.5, 2.8))\\n\\nx = np.arange(len(signals))\\nwidth = 0.55\\n\\nbars = ax.bar(x, ner_delta, width,\\n              yerr=ner_std, capsize=3, error_kw={'linewidth': 0.8},\\n              color=colors, alpha=0.85,\\n              edgecolor='white', linewidth=0.5, zorder=2)\\n\\nax.axhline(y=0, color='black', linewidth=0.6, zorder=1)\\n\\n# Value labels\\nfor i, (d, s) in enumerate(zip(ner_delta, ner_std)):\\n    y = d + (s + 0.15) * (1 if d >= 0 else -1)\\n    va = 'bottom' if d >= 0 else 'top'\\n    ax.text(i, y, f'{d:+.2f}', ha='center', va=va,\\n            fontsize=7, fontweight='bold', color='#333333')\\n\\n# Oracle/random annotations\\nax.annotate(f'oracle: +{oracle_delta:.1f} pp',\\n            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6.5, color='#2ca02c',\\n            ha='right', va='top',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))\\nax.annotate(f'random: {random_delta:.1f} pp',\\n            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6.5, color='gray',\\n            ha='right', va='bottom',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))\\n\\nax.set_xticks(x)\\nax.set_xticklabels(signals)\\nax.set_ylabel(r'$\\\\Delta$F1 vs Greedy (pp)')\\nax.set_title('Selection Gap: Signal vs Greedy (SciERC NER, N=8, 3 seeds)',\\n             fontsize=8.5, fontweight='bold')\\n\\ny_max = max(abs(ner_delta).max() + ner_std.max(), 2.0) + 1.5\\nax.set_ylim(-y_max, y_max)\\nax.tick_params(labelsize=7)\\nax.grid(axis='y', alpha=0.2, linewidth=0.3)\\n\\nfig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')\\nfig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)\\nplt.close(fig)\\n\\n# Verification\\nprint(\\\"=== NER N=8 Selection Gap (pp) — Director-confirmed ===\\\")\\nprint(f\\\"  greedy F1: {greedy_mean:.5f}\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: Δ={ner_delta[i]:+.3f} ± {ner_std[i]:.3f}\\\")\\nprint(f\\\"  oracle delta: +{oracle_delta:.2f} pp\\\")\\nprint(f\\\"  random delta: {random_delta:.2f} pp\\\")\\nprint(f\\\"\\\\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}\\\")\\nprint(f\\\"Saved: {FIG_DIR / 'fig_selection_gap.png'}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "61c322a5-7669-41ea-ac15-6ca6331b48de",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Fig: Selection gap bar chart — N=8 NER, 3-seed, Director-confirmed deltas.\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport numpy as np\\\\nimport matplotlib\\\\nmatplotlib.use('Agg')\\\\nimport matplotlib.pyplot as plt\\\\nfrom pathlib import Path\\\\n\\\\nplt.rcParams.update({\\\\n    'font.family': 'serif',\\\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\\\n    'font.size': 9,\\\\n    'axes.labelsize': 9,\\\\n    'axes.titlesize': 10,\\\\n    'xtick.labelsize': 8,\\\\n    'ytick.labelsize': 8,\\\\n    'legend.fontsize': 7.5,\\\\n    'figure.dpi': 300,\\\\n    'savefig.dpi': 300,\\\\n    'savefig.bbox': 'tight',\\\\n    'savefig.pad_inches': 0.05,\\\\n    'text.usetex': False,\\\\n})\\\\n\\\\nFIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')\\\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\\\n\\\\n# --- Director-confirmed NER N=8 delta (pp, vs greedy, 3-seed) ---\\\\nsignals = ['VC', 'SJ', 'FK', 'EM', 'LP']\\\\nner_delta = np.array([-2.540, -0.433, -0.438, -1.145, +0.038])\\\\n\\\\n# Std from analysis_multiseed_selection_f1.json (qwen_scierc_ner_n8, delta_vs_greedy_std * 100)\\\\nner_std = np.array([0.842, 0.985, 0.927, 0.705, 0.480])\\\\n\\\\n# Oracle/random from same JSON\\\\ngreedy_mean = 0.64583\\\\noracle_mean = 0.77637\\\\nrandom_mean = 0.60688\\\\noracle_delta = (oracle_mean - greedy_mean) * 100  # +13.05 pp\\\\nrandom_delta = (random_mean - greedy_mean) * 100  # -3.90 pp\\\\n\\\\n# Colors: structural signals blue, LP orange\\\\ncolors = ['#4c72b0'] * 4 + ['#dd8452']\\\\n\\\\nfig, ax = plt.subplots(figsize=(4.5, 2.8))\\\\n\\\\nx = np.arange(len(signals))\\\\nwidth = 0.55\\\\n\\\\nbars = ax.bar(x, ner_delta, width,\\\\n              yerr=ner_std, capsize=3, error_kw={'linewidth': 0.8},\\\\n              color=colors, alpha=0.85,\\\\n              edgecolor='white', linewidth=0.5, zorder=2)\\\\n\\\\nax.axhline(y=0, color='black', linewidth=0.6, zorder=1)\\\\n\\\\n# Value labels\\\\nfor i, (d, s) in enumerate(zip(ner_delta, ner_std)):\\\\n    y = d + (s + 0.15) * (1 if d >= 0 else -1)\\\\n    va = 'bottom' if d >= 0 else 'top'\\\\n    ax.text(i, y, f'{d:+.2f}', ha='center', va=va,\\\\n            fontsize=7, fontweight='bold', color='#333333')\\\\n\\\\n# Oracle/random annotations\\\\nax.annotate(f'oracle: +{oracle_delta:.1f} pp',\\\\n            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6.5, color='#2ca02c',\\\\n            ha='right', va='top',\\\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))\\\\nax.annotate(f'random: {random_delta:.1f} pp',\\\\n            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6.5, color='gray',\\\\n            ha='right', va='bottom',\\\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))\\\\n\\\\nax.set_xticks(x)\\\\nax.set_xticklabels(signals)\\\\nax.set_ylabel(r'$\\\\\\\\Delta$F1 vs Greedy (pp)')\\\\nax.set_title('Selection Gap: Signal vs Greedy (SciERC NER, N=8, 3 seeds)',\\\\n             fontsize=8.5, fontweight='bold')\\\\n\\\\ny_max = max(abs(ner_delta).max() + ner_std.max(), 2.0) + 1.5\\\\nax.set_ylim(-y_max, y_max)\\\\nax.tick_params(labelsize=7)\\\\nax.grid(axis='y', alpha=0.2, linewidth=0.3)\\\\n\\\\nfig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')\\\\nfig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)\\\\nplt.close(fig)\\\\n\\\\n# Verification\\\\nprint(\\\\\\\"=== NER N=8 Selection Gap (pp) — Director-confirmed ===\\\\\\\")\\\\nprint(f\\\\\\\"  greedy F1: {greedy_mean:.5f}\\\\\\\")\\\\nfor i, sig in enumerate(signals):\\\\n    print(f\\\\\\\"  {sig}: Δ={ner_delta[i]:+.3f} ± {ner_std[i]:.3f}\\\\\\\")\\\\nprint(f\\\\\\\"  oracle delta: +{oracle_delta:.2f} pp\\\\\\\")\\\\nprint(f\\\\\\\"  random delta: {random_delta:.2f} pp\\\\\\\")\\\\nprint(f\\\\\\\"\\\\\\\\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}\\\\\\\")\\\\nprint(f\\\\\\\"Saved: {FIG_DIR / 'fig_selection_gap.png'}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fig: Selection gap bar chart — N=8 NER, 3-seed, Director-confirmed deltas.\\\"\\\"\\\"\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\n\\nplt.rcParams.update({\\n    'font.family': 'serif',\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\n    'font.size': 9,\\n    'axes.labelsize': 9,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n    'legend.fontsize': 7.5,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'text.usetex': False,\\n})\\n\\nFIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\n\\n# --- Director-confirmed NER N=8 delta (pp, vs greedy, 3-seed) ---\\nsignals = ['VC', 'SJ', 'FK', 'EM', 'LP']\\nner_delta = np.array([-2.540, -0.433, -0.438, -1.145, +0.038])\\n\\n# Std from analysis_multiseed_selection_f1.json (qwen_scierc_ner_n8, delta_vs_greedy_std * 100)\\nner_std = np.array([0.842, 0.985, 0.927, 0.705, 0.480])\\n\\n# Oracle/random from same JSON\\ngreedy_mean = 0.64583\\noracle_mean = 0.77637\\nrandom_mean = 0.60688\\noracle_delta = (oracle_mean - greedy_mean) * 100  # +13.05 pp\\nrandom_delta = (random_mean - greedy_mean) * 100  # -3.90 pp\\n\\n# Colors: structural signals blue, LP orange\\ncolors = ['#4c72b0'] * 4 + ['#dd8452']\\n\\nfig, ax = plt.subplots(figsize=(4.5, 2.8))\\n\\nx = np.arange(len(signals))\\nwidth = 0.55\\n\\nbars = ax.bar(x, ner_delta, width,\\n              yerr=ner_std, capsize=3, error_kw={'linewidth': 0.8},\\n              color=colors, alpha=0.85,\\n              edgecolor='white', linewidth=0.5, zorder=2)\\n\\nax.axhline(y=0, color='black', linewidth=0.6, zorder=1)\\n\\n# Value labels\\nfor i, (d, s) in enumerate(zip(ner_delta, ner_std)):\\n    y = d + (s + 0.15) * (1 if d >= 0 else -1)\\n    va = 'bottom' if d >= 0 else 'top'\\n    ax.text(i, y, f'{d:+.2f}', ha='center', va=va,\\n            fontsize=7, fontweight='bold', color='#333333')\\n\\n# Oracle/random annotations\\nax.annotate(f'oracle: +{oracle_delta:.1f} pp',\\n            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6.5, color='#2ca02c',\\n            ha='right', va='top',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))\\nax.annotate(f'random: {random_delta:.1f} pp',\\n            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6.5, color='gray',\\n            ha='right', va='bottom',\\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))\\n\\nax.set_xticks(x)\\nax.set_xticklabels(signals)\\nax.set_ylabel(r'$\\\\Delta$F1 vs Greedy (pp)')\\nax.set_title('Selection Gap: Signal vs Greedy (SciERC NER, N=8, 3 seeds)',\\n             fontsize=8.5, fontweight='bold')\\n\\ny_max = max(abs(ner_delta).max() + ner_std.max(), 2.0) + 1.5\\nax.set_ylim(-y_max, y_max)\\nax.tick_params(labelsize=7)\\nax.grid(axis='y', alpha=0.2, linewidth=0.3)\\n\\nfig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')\\nfig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)\\nplt.close(fig)\\n\\n# Verification\\nprint(\\\"=== NER N=8 Selection Gap (pp) — Director-confirmed ===\\\")\\nprint(f\\\"  greedy F1: {greedy_mean:.5f}\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: Δ={ner_delta[i]:+.3f} ± {ner_std[i]:.3f}\\\")\\nprint(f\\\"  oracle delta: +{oracle_delta:.2f} pp\\\")\\nprint(f\\\"  random delta: {random_delta:.2f} pp\\\")\\nprint(f\\\"\\\\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}\\\")\\nprint(f\\\"Saved: {FIG_DIR / 'fig_selection_gap.png'}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 71_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HxoMdmbAZfagUT8EVGkA32`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/plot_selection_gap_single.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b9601c38-46cd-4f5a-b9fa-9b6da45afe8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZY9iTCZ9Lxgti282e2wBt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8103,
      "cache_read_input_tokens": 44243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8103
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

_source line 72 · 2026-05-19T08:03:00.876Z_

<details><summary>↩ Tool result · `toolu_01HxoMdmbAZfagUT8EVGkA32`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fig: Selection gap single panel — NER-only, dual Y-axis (rho + delta F1).\\\"\\\"\\\"\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nfrom matplotlib.patches import Patch\\nfrom matplotlib.lines import Line2D\\nfrom pathlib import Path\\n\\nplt.rcParams.update({\\n    'font.family': 'serif',\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\n    'font.size': 9,\\n    'axes.labelsize': 9,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n    'legend.fontsize': 7,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'text.usetex': False,\\n})\\n\\nFIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')\\nPAPER_FIG = Path('/root/autodl-tmp/struct_self_consist_ie/docs/paper/figures')\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\nPAPER_FIG.mkdir(parents=True, exist_ok=True)\\n\\n# --- Data: SciERC NER, N=8, T=1.0 ---\\nsignals = ['SJ', 'FK', 'EM', 'VC', 'LP']\\n\\n# Spearman rho: exp_016_rerun_1024/correlation_matrix.json (seed42, n=529)\\nrho = np.array([0.3599, 0.2665, 0.2990, 0.2524, 0.2052])\\n\\n# Delta F1 vs greedy (pp): analysis_multiseed_selection_f1.json (3 seeds)\\ndelta_f1 = np.array([-0.451, -0.457, -1.193, -2.646, +0.040])\\ndelta_std = np.array([1.026, 0.966, 0.734, 0.877, 0.500])\\n\\n# Baselines\\ngreedy_mean = 0.64583\\noracle_mean = 0.77637\\nrandom_mean = 0.60688\\noracle_delta = (oracle_mean - greedy_mean) * 100\\nrandom_delta = (random_mean - greedy_mean) * 100\\n\\n# --- Plot ---\\nfig, ax1 = plt.subplots(figsize=(4.5, 2.8))\\nx = np.arange(len(signals))\\nwidth = 0.5\\n\\n# Left axis: Spearman rho (blue bars)\\nbar_color = '#4c72b0'\\nbars = ax1.bar(x, rho, width, color=bar_color, alpha=0.75,\\n               edgecolor='white', linewidth=0.5, zorder=2)\\nax1.set_ylabel(r'Spearman $\\\\rho$', color=bar_color, fontsize=9)\\nax1.tick_params(axis='y', labelcolor=bar_color, labelsize=7)\\nax1.set_ylim(0, 0.48)\\nax1.set_xticks(x)\\nax1.set_xticklabels(signals, fontsize=8)\\n\\n# Bar value labels\\nfor i, r in enumerate(rho):\\n    ax1.text(i, r + 0.010, f'.{int(r*1000):03d}', ha='center', va='bottom',\\n             fontsize=6.5, color=bar_color, fontweight='bold')\\n\\n# Right axis: Delta F1 (red line + error bars)\\nax2 = ax1.twinx()\\nline_color = '#c44e52'\\nax2.errorbar(x, delta_f1, yerr=delta_std, fmt='o-', color=line_color,\\n             markersize=4.5, capsize=3, linewidth=1.2, elinewidth=0.8,\\n             markeredgecolor='white', markeredgewidth=0.5, zorder=3)\\nax2.set_ylabel(r'$\\\\Delta$F1 vs Greedy (pp)', color=line_color, fontsize=9)\\nax2.tick_params(axis='y', labelcolor=line_color, labelsize=7)\\nax2.set_ylim(-6.5, 16)\\n\\n# Zero line\\nax2.axhline(y=0, color='black', linestyle='-', linewidth=0.4, alpha=0.4, zorder=1)\\n\\n# Oracle dashed line + label\\nax2.axhline(y=oracle_delta, color='#2ca02c', linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)\\nax2.text(len(signals)-1, oracle_delta + 0.5, f'Oracle +{oracle_delta:.1f}',\\n         fontsize=6, color='#2ca02c', ha='right', va='bottom',\\n         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#2ca02c',\\n                   alpha=0.85, linewidth=0.5))\\n\\n# Random dotted line + label\\nax2.axhline(y=random_delta, color='gray', linestyle=':', linewidth=0.8, alpha=0.6, zorder=1)\\nax2.text(0.02, random_delta - 0.3, f'Random {random_delta:.1f}',\\n         fontsize=6, color='gray', ha='left', va='top',\\n         transform=ax2.get_yaxis_transform(),\\n         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='gray',\\n                   alpha=0.85, linewidth=0.5))\\n\\n# Delta value labels\\nfor i, (d, s) in enumerate(zip(delta_f1, delta_std)):\\n    if i == 3:  # VC: place above to avoid random overlap\\n        y_off = d + s + 0.3\\n        va = 'bottom'\\n    else:\\n        y_off = d - s - 0.4\\n        va = 'top'\\n    ax2.text(i, y_off, f'{d:+.2f}', ha='center', va=va,\\n             fontsize=6, color=line_color, fontweight='bold')\\n\\n# Grid\\nax1.grid(axis='y', alpha=0.15, linewidth=0.3)\\nax1.set_axisbelow(True)\\n\\n# Legend\\nlegend_elements = [\\n    Patch(facecolor=bar_color, alpha=0.75, edgecolor='white', label=r'Spearman $\\\\rho$'),\\n    Line2D([0], [0], color=line_color, marker='o', markersize=4, linewidth=1.2,\\n           markeredgecolor='white', markeredgewidth=0.5, label=r'$\\\\Delta$F1 vs Greedy (pp)')\\n]\\nax1.legend(handles=legend_elements, loc='upper center', fontsize=6.5,\\n           framealpha=0.9, edgecolor='#cccccc', ncol=2,\\n           bbox_to_anchor=(0.5, 1.0))\\n\\nax1.set_title('SciERC NER, N=8, T=1.0', fontsize=8.5, fontweight='bold', pad=12)\\n\\nfig.tight_layout()\\nfor path in [FIG_DIR, PAPER_FIG]:\\n    fig.savefig(path / 'fig_selection_gap.pdf', format='pdf')\\n    fig.savefig(path / 'fig_selection_gap.png', format='png', dpi=300)\\nplt.close(fig)\\n\\nprint(\\\"=== Data ===\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: rho={rho[i]:.4f}, delta={delta_f1[i]:+.3f} +/- {delta_std[i]:.3f} pp\\\")\\nprint(f\\\"  Oracle: +{oracle_delta:.2f} pp | Random: {random_delta:.2f} pp\\\")\\nprint(f\\\"Saved to {FIG_DIR} and {PAPER_FIG}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "9aacadca-4bc3-4fa0-80f1-d6834aec2b13",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Fig: Selection gap single panel — NER-only, dual Y-axis (rho + delta F1).\\\\\\\"\\\\\\\"\\\\\\\"\\\\nimport numpy as np\\\\nimport matplotlib\\\\nmatplotlib.use('Agg')\\\\nimport matplotlib.pyplot as plt\\\\nfrom matplotlib.patches import Patch\\\\nfrom matplotlib.lines import Line2D\\\\nfrom pathlib import Path\\\\n\\\\nplt.rcParams.update({\\\\n    'font.family': 'serif',\\\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\\\n    'font.size': 9,\\\\n    'axes.labelsize': 9,\\\\n    'axes.titlesize': 10,\\\\n    'xtick.labelsize': 8,\\\\n    'ytick.labelsize': 8,\\\\n    'legend.fontsize': 7,\\\\n    'figure.dpi': 300,\\\\n    'savefig.dpi': 300,\\\\n    'savefig.bbox': 'tight',\\\\n    'savefig.pad_inches': 0.05,\\\\n    'text.usetex': False,\\\\n})\\\\n\\\\nFIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')\\\\nPAPER_FIG = Path('/root/autodl-tmp/struct_self_consist_ie/docs/paper/figures')\\\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\\\nPAPER_FIG.mkdir(parents=True, exist_ok=True)\\\\n\\\\n# --- Data: SciERC NER, N=8, T=1.0 ---\\\\nsignals = ['SJ', 'FK', 'EM', 'VC', 'LP']\\\\n\\\\n# Spearman rho: exp_016_rerun_1024/correlation_matrix.json (seed42, n=529)\\\\nrho = np.array([0.3599, 0.2665, 0.2990, 0.2524, 0.2052])\\\\n\\\\n# Delta F1 vs greedy (pp): analysis_multiseed_selection_f1.json (3 seeds)\\\\ndelta_f1 = np.array([-0.451, -0.457, -1.193, -2.646, +0.040])\\\\ndelta_std = np.array([1.026, 0.966, 0.734, 0.877, 0.500])\\\\n\\\\n# Baselines\\\\ngreedy_mean = 0.64583\\\\noracle_mean = 0.77637\\\\nrandom_mean = 0.60688\\\\noracle_delta = (oracle_mean - greedy_mean) * 100\\\\nrandom_delta = (random_mean - greedy_mean) * 100\\\\n\\\\n# --- Plot ---\\\\nfig, ax1 = plt.subplots(figsize=(4.5, 2.8))\\\\nx = np.arange(len(signals))\\\\nwidth = 0.5\\\\n\\\\n# Left axis: Spearman rho (blue bars)\\\\nbar_color = '#4c72b0'\\\\nbars = ax1.bar(x, rho, width, color=bar_color, alpha=0.75,\\\\n               edgecolor='white', linewidth=0.5, zorder=2)\\\\nax1.set_ylabel(r'Spearman $\\\\\\\\rho$', color=bar_color, fontsize=9)\\\\nax1.tick_params(axis='y', labelcolor=bar_color, labelsize=7)\\\\nax1.set_ylim(0, 0.48)\\\\nax1.set_xticks(x)\\\\nax1.set_xticklabels(signals, fontsize=8)\\\\n\\\\n# Bar value labels\\\\nfor i, r in enumerate(rho):\\\\n    ax1.text(i, r + 0.010, f'.{int(r*1000):03d}', ha='center', va='bottom',\\\\n             fontsize=6.5, color=bar_color, fontweight='bold')\\\\n\\\\n# Right axis: Delta F1 (red line + error bars)\\\\nax2 = ax1.twinx()\\\\nline_color = '#c44e52'\\\\nax2.errorbar(x, delta_f1, yerr=delta_std, fmt='o-', color=line_color,\\\\n             markersize=4.5, capsize=3, linewidth=1.2, elinewidth=0.8,\\\\n             markeredgecolor='white', markeredgewidth=0.5, zorder=3)\\\\nax2.set_ylabel(r'$\\\\\\\\Delta$F1 vs Greedy (pp)', color=line_color, fontsize=9)\\\\nax2.tick_params(axis='y', labelcolor=line_color, labelsize=7)\\\\nax2.set_ylim(-6.5, 16)\\\\n\\\\n# Zero line\\\\nax2.axhline(y=0, color='black', linestyle='-', linewidth=0.4, alpha=0.4, zorder=1)\\\\n\\\\n# Oracle dashed line + label\\\\nax2.axhline(y=oracle_delta, color='#2ca02c', linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)\\\\nax2.text(len(signals)-1, oracle_delta + 0.5, f'Oracle +{oracle_delta:.1f}',\\\\n         fontsize=6, color='#2ca02c', ha='right', va='bottom',\\\\n         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#2ca02c',\\\\n                   alpha=0.85, linewidth=0.5))\\\\n\\\\n# Random dotted line + label\\\\nax2.axhline(y=random_delta, color='gray', linestyle=':', linewidth=0.8, alpha=0.6, zorder=1)\\\\nax2.text(0.02, random_delta - 0.3, f'Random {random_delta:.1f}',\\\\n         fontsize=6, color='gray', ha='left', va='top',\\\\n         transform=ax2.get_yaxis_transform(),\\\\n         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='gray',\\\\n                   alpha=0.85, linewidth=0.5))\\\\n\\\\n# Delta value labels\\\\nfor i, (d, s) in enumerate(zip(delta_f1, delta_std)):\\\\n    if i == 3:  # VC: place above to avoid random overlap\\\\n        y_off = d + s + 0.3\\\\n        va = 'bottom'\\\\n    else:\\\\n        y_off = d - s - 0.4\\\\n        va = 'top'\\\\n    ax2.text(i, y_off, f'{d:+.2f}', ha='center', va=va,\\\\n             fontsize=6, color=line_color, fontweight='bold')\\\\n\\\\n# Grid\\\\nax1.grid(axis='y', alpha=0.15, linewidth=0.3)\\\\nax1.set_axisbelow(True)\\\\n\\\\n# Legend\\\\nlegend_elements = [\\\\n    Patch(facecolor=bar_color, alpha=0.75, edgecolor='white', label=r'Spearman $\\\\\\\\rho$'),\\\\n    Line2D([0], [0], color=line_color, marker='o', markersize=4, linewidth=1.2,\\\\n           markeredgecolor='white', markeredgewidth=0.5, label=r'$\\\\\\\\Delta$F1 vs Greedy (pp)')\\\\n]\\\\nax1.legend(handles=legend_elements, loc='upper center', fontsize=6.5,\\\\n           framealpha=0.9, edgecolor='#cccccc', ncol=2,\\\\n           bbox_to_anchor=(0.5, 1.0))\\\\n\\\\nax1.set_title('SciERC NER, N=8, T=1.0', fontsize=8.5, fontweight='bold', pad=12)\\\\n\\\\nfig.tight_layout()\\\\nfor path in [FIG_DIR, PAPER_FIG]:\\\\n    fig.savefig(path / 'fig_selection_gap.pdf', format='pdf')\\\\n    fig.savefig(path / 'fig_selection_gap.png', format='png', dpi=300)\\\\nplt.close(fig)\\\\n\\\\nprint(\\\\\\\"=== Data ===\\\\\\\")\\\\nfor i, sig in enumerate(signals):\\\\n    print(f\\\\\\\"  {sig}: rho={rho[i]:.4f}, delta={delta_f1[i]:+.3f} +/- {delta_std[i]:.3f} pp\\\\\\\")\\\\nprint(f\\\\\\\"  Oracle: +{oracle_delta:.2f} pp | Random: {random_delta:.2f} pp\\\\\\\")\\\\nprint(f\\\\\\\"Saved to {FIG_DIR} and {PAPER_FIG}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Fig: Selection gap single panel — NER-only, dual Y-axis (rho + delta F1).\\\"\\\"\\\"\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nfrom matplotlib.patches import Patch\\nfrom matplotlib.lines import Line2D\\nfrom pathlib import Path\\n\\nplt.rcParams.update({\\n    'font.family': 'serif',\\n    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],\\n    'font.size': 9,\\n    'axes.labelsize': 9,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n    'legend.fontsize': 7,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'text.usetex': False,\\n})\\n\\nFIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')\\nPAPER_FIG = Path('/root/autodl-tmp/struct_self_consist_ie/docs/paper/figures')\\nFIG_DIR.mkdir(parents=True, exist_ok=True)\\nPAPER_FIG.mkdir(parents=True, exist_ok=True)\\n\\n# --- Data: SciERC NER, N=8, T=1.0 ---\\nsignals = ['SJ', 'FK', 'EM', 'VC', 'LP']\\n\\n# Spearman rho: exp_016_rerun_1024/correlation_matrix.json (seed42, n=529)\\nrho = np.array([0.3599, 0.2665, 0.2990, 0.2524, 0.2052])\\n\\n# Delta F1 vs greedy (pp): analysis_multiseed_selection_f1.json (3 seeds)\\ndelta_f1 = np.array([-0.451, -0.457, -1.193, -2.646, +0.040])\\ndelta_std = np.array([1.026, 0.966, 0.734, 0.877, 0.500])\\n\\n# Baselines\\ngreedy_mean = 0.64583\\noracle_mean = 0.77637\\nrandom_mean = 0.60688\\noracle_delta = (oracle_mean - greedy_mean) * 100\\nrandom_delta = (random_mean - greedy_mean) * 100\\n\\n# --- Plot ---\\nfig, ax1 = plt.subplots(figsize=(4.5, 2.8))\\nx = np.arange(len(signals))\\nwidth = 0.5\\n\\n# Left axis: Spearman rho (blue bars)\\nbar_color = '#4c72b0'\\nbars = ax1.bar(x, rho, width, color=bar_color, alpha=0.75,\\n               edgecolor='white', linewidth=0.5, zorder=2)\\nax1.set_ylabel(r'Spearman $\\\\rho$', color=bar_color, fontsize=9)\\nax1.tick_params(axis='y', labelcolor=bar_color, labelsize=7)\\nax1.set_ylim(0, 0.48)\\nax1.set_xticks(x)\\nax1.set_xticklabels(signals, fontsize=8)\\n\\n# Bar value labels\\nfor i, r in enumerate(rho):\\n    ax1.text(i, r + 0.010, f'.{int(r*1000):03d}', ha='center', va='bottom',\\n             fontsize=6.5, color=bar_color, fontweight='bold')\\n\\n# Right axis: Delta F1 (red line + error bars)\\nax2 = ax1.twinx()\\nline_color = '#c44e52'\\nax2.errorbar(x, delta_f1, yerr=delta_std, fmt='o-', color=line_color,\\n             markersize=4.5, capsize=3, linewidth=1.2, elinewidth=0.8,\\n             markeredgecolor='white', markeredgewidth=0.5, zorder=3)\\nax2.set_ylabel(r'$\\\\Delta$F1 vs Greedy (pp)', color=line_color, fontsize=9)\\nax2.tick_params(axis='y', labelcolor=line_color, labelsize=7)\\nax2.set_ylim(-6.5, 16)\\n\\n# Zero line\\nax2.axhline(y=0, color='black', linestyle='-', linewidth=0.4, alpha=0.4, zorder=1)\\n\\n# Oracle dashed line + label\\nax2.axhline(y=oracle_delta, color='#2ca02c', linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)\\nax2.text(len(signals)-1, oracle_delta + 0.5, f'Oracle +{oracle_delta:.1f}',\\n         fontsize=6, color='#2ca02c', ha='right', va='bottom',\\n         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#2ca02c',\\n                   alpha=0.85, linewidth=0.5))\\n\\n# Random dotted line + label\\nax2.axhline(y=random_delta, color='gray', linestyle=':', linewidth=0.8, alpha=0.6, zorder=1)\\nax2.text(0.02, random_delta - 0.3, f'Random {random_delta:.1f}',\\n         fontsize=6, color='gray', ha='left', va='top',\\n         transform=ax2.get_yaxis_transform(),\\n         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='gray',\\n                   alpha=0.85, linewidth=0.5))\\n\\n# Delta value labels\\nfor i, (d, s) in enumerate(zip(delta_f1, delta_std)):\\n    if i == 3:  # VC: place above to avoid random overlap\\n        y_off = d + s + 0.3\\n        va = 'bottom'\\n    else:\\n        y_off = d - s - 0.4\\n        va = 'top'\\n    ax2.text(i, y_off, f'{d:+.2f}', ha='center', va=va,\\n             fontsize=6, color=line_color, fontweight='bold')\\n\\n# Grid\\nax1.grid(axis='y', alpha=0.15, linewidth=0.3)\\nax1.set_axisbelow(True)\\n\\n# Legend\\nlegend_elements = [\\n    Patch(facecolor=bar_color, alpha=0.75, edgecolor='white', label=r'Spearman $\\\\rho$'),\\n    Line2D([0], [0], color=line_color, marker='o', markersize=4, linewidth=1.2,\\n           markeredgecolor='white', markeredgewidth=0.5, label=r'$\\\\Delta$F1 vs Greedy (pp)')\\n]\\nax1.legend(handles=legend_elements, loc='upper center', fontsize=6.5,\\n           framealpha=0.9, edgecolor='#cccccc', ncol=2,\\n           bbox_to_anchor=(0.5, 1.0))\\n\\nax1.set_title('SciERC NER, N=8, T=1.0', fontsize=8.5, fontweight='bold', pad=12)\\n\\nfig.tight_layout()\\nfor path in [FIG_DIR, PAPER_FIG]:\\n    fig.savefig(path / 'fig_selection_gap.pdf', format='pdf')\\n    fig.savefig(path / 'fig_selection_gap.png', format='png', dpi=300)\\nplt.close(fig)\\n\\nprint(\\\"=== Data ===\\\")\\nfor i, sig in enumerate(signals):\\n    print(f\\\"  {sig}: rho={rho[i]:.4f}, delta={delta_f1[i]:+.3f} +/- {delta_std[i]:.3f} pp\\\")\\nprint(f\\\"  Oracle: +{oracle_delta:.2f} pp | Random: {random_delta:.2f} pp\\\")\\nprint(f\\\"Saved to {FIG_DIR} and {PAPER_FIG}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 73_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete picture. Let me analyze:

## Task 1: FewNERD N=16 data tracing

### L143: LP selection "+0.52pp" (N=16)
The paper says: "LP selection gains scale with N (Few-NERD N=16: +0.52 pp, p=0.003; Appendix app:n_scaling)"

From paired_n8_baseline.json:
- `paired_bootstrap.point_estimate_pp`: 0.5169 ≈ 0.52
- `paired_bootstrap.p_value`: 0.0034 ≈ 0.003


- This represents the additional gain from N=8→N=16 (1.88 - 1.37 = 0.51), sourced from `exp_027_fewnerd_n16/paired_n8_baseline.json` on the 5K subset. **Confirmed.**

### L213: Construction "+1.32pp" (N=16)
The paper says: "Construction gains scale with N: at N=16 on Few-NERD,

I'm noticing a discrepancy here. The paper claims the delta "rises to +1.32 pp" at N=16, but the entity construction table at L204 shows +1.40±0.51 pp for N=8. That's actually a decrease, not a rise—+1.32 is lower than +1.40. Let me check if I'm reading the table correctly or if there's something about how these metrics are being reported that I'm missing. I'm realizing the discrepancy: the table shows a 4-seed average of +1.40pp for N=8 construction, but the text claims it "rises to +1.32pp" at N=16 using only seed-42 data. That's comparing different experimental protocols, which makes the "rises" claim misleading since the single-seed result is actually lower. I need to track down where the N=16 entity construction numbers are coming from, since I'm not finding them in the results file. I'm looking at the plot_selection_gap_single.py script which generates a dual-axis figure with quality estimation ρ values as bars and ΔF1 versus greedy as a line with error bars. The script shows ρ values for SciERC N=8 across different signals, with SJ having the highest ρ at 0.3599 and VC at 0.2524, but these don't align with the exp_021_fewnerd_full data I was examining earlier.

Looking at the data source from exp_016_rerun_1024, I notice the caption claims "ρ up to 0.38" but the actual maximum ρ value in the SciERC N=8 data is 0.36 from SJ, which is a discrepancy I need to resolve.

There's also a mismatch between what the caption says about "2-seed mean" and what the script indicates—the ρ values come from seed42 only (n=529), while the ΔF1 metrics are averaged across 3 seeds, so the figure is mixing data from different seed configurations.

Let me check the quality estimation table to see if the 2-seed or 3-seed mean ρ values match the 0.38 mentioned in the caption. Looking at the FewNERD experiment, I see vc_global_rho is 0.3858, which is close. For SciERC with N=16, the ner_voting_conf_rho is 0.399 and ner_sj_rho is 0.398, but I need to find the N=8 SciERC data to match what the figure shows.

The seed42-only values for SciERC N=8 show SJ at 0.36 as the maximum, but the caption claims "ρ up to 0.38"—these don't align. The discrepancy suggests the caption is referring to multi-seed mean ρ values rather than single-seed results, so I need to locate those aggregated metrics in the quality estimation table. I need to find the multi-seed ρ values for SciERC with N=8 in the analysis data to see if any configuration actually reaches 0.38. Let me also check the appendix section on n_scaling to understand what data is documented there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "3de8a57d-a637-49ac-9300-9b364337d2b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNhq8SU2hLmY8P9hzZTiYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7728,
      "cache_read_input_tokens": 52346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7728
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

I now have a clear picture of the figure. The active script is `plot_selection_gap_single.py` — it's a dual-axis chart with SJ/FK/EM/VC/LP, where bars = ρ (seed42 only), line = ΔF1 (3-seed). The max ρ in the plotted data is SJ=0.3599≈0.36, but the caption says "ρ up to 0.38". Let me now check the appendix n_scaling section and search for N=16 entity construction data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "28da040c-4a46-497d-86c0-38c1def6a2cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNhq8SU2hLmY8P9hzZTiYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7728,
      "cache_read_input_tokens": 52346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7728
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

<details open><summary>🔧 Tool call — Grep · `toolu_01Vz1K1fpMcZYsLb92qJG34r`</summary>

```json
{
  "pattern": "n_scaling|n.scaling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "4c1acf51-1c2b-4aef-9952-8f21de47b6c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNhq8SU2hLmY8P9hzZTiYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7728,
      "cache_read_input_tokens": 52346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7728
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

_source line 76 · 2026-05-19T08:03:59.587Z_

<details><summary>↩ Tool result · `toolu_01Vz1K1fpMcZYsLb92qJG34r`</summary>

```text
965-Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
966-These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
967-
968:\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
969-
970:Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
971-
972-\begin{table}[t]
973-\centering
974-\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
975:\label{tab:n-scaling}
976-\small
977-\begin{tabular}{l ccc ccc}
978-\toprule
--
1035-Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
1036-
1037-\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
1038:Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
1039-Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).
1040-LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\% and oracle headroom reaches ${\sim}20$~pp, the best signal captures less than 5\% of the available improvement.
1041-Degeneracy drops monotonically (43\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
--
1045-\centering
1046-\small
1047-\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
1048:\label{tab:n_scaling_selection}
1049-\begin{tabular}{ccccccccc}
1050-\toprule
1051-$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "0dd40cd6-ee6b-4129-b4ee-05ddd13c2a03",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "965-Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\n966-These instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n967-\n968:\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n969-\n970:Tables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n971-\n972-\\begin{table}[t]\n973-\\centering\n974-\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n975:\\label{tab:n-scaling}\n976-\\small\n977-\\begin{tabular}{l ccc ccc}\n978-\\toprule\n--\n1035-Doubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER); additional samples stabilize structural signals more than LP.\n1036-\n1037-\\paragraph{$N$-scaling: selection headroom vs.\\ selection gain.}\n1038:Table~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\n1039-Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).\n1040-LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}20$~pp, the best signal captures less than 5\\% of the available improvement.\n1041-Degeneracy drops monotonically (43\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\n--\n1045-\\centering\n1046-\\small\n1047-\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\n1048:\\label{tab:n_scaling_selection}\n1049-\\begin{tabular}{ccccccccc}\n1050-\\toprule\n1051-$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\",
    "numLines": 30
  }
}
```

</details>

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MRiffQWq42L5T5SwDRxd1U`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*construct*n16*\" -o -name \"*n16*construct*\" -o -name \"*entity_construct*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "7f3c24db-d33e-452e-acb5-0fa96129cf12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNhq8SU2hLmY8P9hzZTiYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7728,
      "cache_read_input_tokens": 52346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7728
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

_source line 78 · 2026-05-19T08:04:01.937Z_

<details><summary>↩ Tool result · `toolu_01MRiffQWq42L5T5SwDRxd1U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/entity_construction\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_log.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8_log.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "45030401-c466-4154-9722-9c057e0ca8c1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/entity_construction\\\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair\\\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_log.txt\\\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8\\\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8_log.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/entity_construction\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_log.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8_log.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019X3scJ1bH1hw27N77YgmN4`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -maxdepth 1 -name \"*n_scaling*\" -o -name \"*scaling*\" -o -name \"*n16*construct*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c8087247-7c5b-4c05-b9ef-405aac88fc45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNhq8SU2hLmY8P9hzZTiYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7728,
      "cache_read_input_tokens": 52346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7728
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

_source line 80 · 2026-05-19T08:04:02.874Z_

<details><summary>↩ Tool result · `toolu_019X3scJ1bH1hw27N77YgmN4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling\\n/root/autodl-tmp/struct_self_consist_ie/output/n_scaling_gf_maxlp.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b4fd8583-1282-4641-acac-41076f49bf76",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling\\\\n/root/autodl-tmp/struct_self_consist_ie/output/n_scaling_gf_maxlp.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/bootstrap_ci_nscaling\\n/root/autodl-tmp/struct_self_consist_ie/output/n_scaling_gf_maxlp.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
Let me look at the entity construction output directories and the n_scaling data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "fc16de44-31ad-4023-ad7f-b88118d4bce2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127XuuRystFDgTrKvS9oeGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4437,
      "cache_read_input_tokens": 60074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4437
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

_source line 82_

Found entity_construction directories and n_scaling files. Let me check the entity construction results for N=16 and the appendix content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b3806513-cf8e-4db4-896f-7e1abd8ec4bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127XuuRystFDgTrKvS9oeGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4437,
      "cache_read_input_tokens": 60074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4437
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

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KTSwACSMxsSzZd293Sk5Ch`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/entity_construction/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "55e3c37e-9c97-4a88-be3c-3a6dbd0b384c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127XuuRystFDgTrKvS9oeGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4437,
      "cache_read_input_tokens": 60074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4437
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

_source line 84 · 2026-05-19T08:04:08.831Z_

<details><summary>↩ Tool result · `toolu_01KTSwACSMxsSzZd293Sk5Ch`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 44\\ndrwxr-xr-x   2 root root    86 May 19 09:43 .\\ndrwxr-xr-x 183 root root 12288 May 19 15:26 ..\\n-rw-r--r--   1 root root  1361 May 19 09:43 best_threshold_summary.json\\n-rw-r--r--   1 root root 21621 May 19 09:43 construction_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "637b7389-6f6e-4ffd-976a-261effb1d407",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 44\\\\ndrwxr-xr-x   2 root root    86 May 19 09:43 .\\\\ndrwxr-xr-x 183 root root 12288 May 19 15:26 ..\\\\n-rw-r--r--   1 root root  1361 May 19 09:43 best_threshold_summary.json\\\\n-rw-r--r--   1 root root 21621 May 19 09:43 construction_results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 44\\ndrwxr-xr-x   2 root root    86 May 19 09:43 .\\ndrwxr-xr-x 183 root root 12288 May 19 15:26 ..\\n-rw-r--r--   1 root root  1361 May 19 09:43 best_threshold_summary.json\\n-rw-r--r--   1 root root 21621 May 19 09:43 construction_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013KSrhXKLgAcbS2XM8pVwJa`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "76fbf374-93cf-445e-be38-0ef6a8cd87dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127XuuRystFDgTrKvS9oeGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4437,
      "cache_read_input_tokens": 60074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4437
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

_source line 86 · 2026-05-19T08:04:09.549Z_

<details><summary>↩ Tool result · `toolu_013KSrhXKLgAcbS2XM8pVwJa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 52\\ndrwxr-xr-x   2 root root   108 May 19 10:08 .\\ndrwxr-xr-x 183 root root 12288 May 19 15:26 ..\\n-rw-r--r--   1 root root  3669 May 19 10:08 adaptive_combination.json\\n-rw-r--r--   1 root root  7192 May 19 10:08 bootstrap_tests.json\\n-rw-r--r--   1 root root 23686 May 19 10:08 fair_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "3847a5f6-9544-4680-b319-d50c5c04c096",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 52\\\\ndrwxr-xr-x   2 root root   108 May 19 10:08 .\\\\ndrwxr-xr-x 183 root root 12288 May 19 15:26 ..\\\\n-rw-r--r--   1 root root  3669 May 19 10:08 adaptive_combination.json\\\\n-rw-r--r--   1 root root  7192 May 19 10:08 bootstrap_tests.json\\\\n-rw-r--r--   1 root root 23686 May 19 10:08 fair_results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 52\\ndrwxr-xr-x   2 root root   108 May 19 10:08 .\\ndrwxr-xr-x 183 root root 12288 May 19 15:26 ..\\n-rw-r--r--   1 root root  3669 May 19 10:08 adaptive_combination.json\\n-rw-r--r--   1 root root  7192 May 19 10:08 bootstrap_tests.json\\n-rw-r--r--   1 root root 23686 May 19 10:08 fair_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012frSxpGjLYbPnZKRcuf9Sp`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n_scaling_gf_maxlp.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8f967541-616a-476c-8778-583e58263d92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127XuuRystFDgTrKvS9oeGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4437,
      "cache_read_input_tokens": 60074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4437
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

_source line 88 · 2026-05-19T08:04:10.685Z_

<details><summary>↩ Tool result · `toolu_012frSxpGjLYbPnZKRcuf9Sp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"N=2\\\": {\\n    \\\"N\\\": 2,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.6831851485554365,\\n    \\\"oracle_headroom_pp\\\": 4.350160508283507,\\n    \\\"degen_pct\\\": 42.722117202268436,\\n    \\\"elapsed_s\\\": 0.0437619686126709,\\n    \\\"LP_sel_f1\\\": 0.6307527958284102,\\n    \\\"LP_delta_pp\\\": -0.8930747644191328,\\n    \\\"SJ_sel_f1\\\": 0.6124373078643066,\\n    \\\"SJ_delta_pp\\\": -2.7246235608294866,\\n    \\\"FK_sel_f1\\\": 0.6124373078643066,\\n    \\\"FK_delta_pp\\\": -2.7246235608294866,\\n    \\\"EM_sel_f1\\\": 0.6124373078643066,\\n    \\\"EM_delta_pp\\\": -2.7246235608294866,\\n    \\\"VC_sel_f1\\\": 0.6130812581663244,\\n    \\\"VC_delta_pp\\\": -2.6602285306277063,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": -0.8930747644191328\\n  },\\n  \\\"N=4\\\": {\\n    \\\"N\\\": 4,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.742071252999197,\\n    \\\"oracle_headroom_pp\\\": 10.238770952659548,\\n    \\\"degen_pct\\\": 20.982986767485823,\\n    \\\"elapsed_s\\\": 0.09875702857971191,\\n    \\\"LP_sel_f1\\\": 0.6399765693243954,\\n    \\\"LP_delta_pp\\\": 0.02930258517939155,\\n    \\\"SJ_sel_f1\\\": 0.6365973056065349,\\n    \\\"SJ_delta_pp\\\": -0.30862378660665435,\\n    \\\"FK_sel_f1\\\": 0.63568005440573,\\n    \\\"FK_delta_pp\\\": -0.4003489066871424,\\n    \\\"EM_sel_f1\\\": 0.632259535626043,\\n    \\\"EM_delta_pp\\\": -0.74240078465585,\\n    \\\"VC_sel_f1\\\": 0.6180644207220433,\\n    \\\"VC_delta_pp\\\": -2.1619122750558217,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.02930258517939155\\n  },\\n  \\\"N=8\\\": {\\n    \\\"N\\\": 8,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.784797595808938,\\n    \\\"oracle_headroom_pp\\\": 14.511405233633656,\\n    \\\"degen_pct\\\": 10.964083175803403,\\n    \\\"elapsed_s\\\": 0.2820611000061035,\\n    \\\"LP_sel_f1\\\": 0.6435647809077143,\\n    \\\"LP_delta_pp\\\": 0.38812374351128165,\\n    \\\"SJ_sel_f1\\\": 0.6416811520392083,\\n    \\\"SJ_delta_pp\\\": 0.1997608566606801,\\n    \\\"FK_sel_f1\\\": 0.6411876212054127,\\n    \\\"FK_delta_pp\\\": 0.15040777328112487,\\n    \\\"EM_sel_f1\\\": 0.6320061519216418,\\n    \\\"EM_delta_pp\\\": -0.76773915509597,\\n    \\\"VC_sel_f1\\\": 0.6110108962660947,\\n    \\\"VC_delta_pp\\\": -2.867264720650675,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.38812374351128165\\n  },\\n  \\\"N=16\\\": {\\n    \\\"N\\\": 16,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.8168792612554427,\\n    \\\"oracle_headroom_pp\\\": 17.719571778284127,\\n    \\\"degen_pct\\\": 7.372400756143667,\\n    \\\"elapsed_s\\\": 0.9487478733062744,\\n    \\\"LP_sel_f1\\\": 0.6475128387310084,\\n    \\\"LP_delta_pp\\\": 0.7829295258406921,\\n    \\\"SJ_sel_f1\\\": 0.6421272088179683,\\n    \\\"SJ_delta_pp\\\": 0.24436653453667745,\\n    \\\"FK_sel_f1\\\": 0.6394835911459953,\\n    \\\"FK_delta_pp\\\": -0.019995232660618978,\\n    \\\"EM_sel_f1\\\": 0.6391168134162686,\\n    \\\"EM_delta_pp\\\": -0.05667300563328981,\\n    \\\"VC_sel_f1\\\": 0.6002271095843874,\\n    \\\"VC_delta_pp\\\": -3.945643388821407,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.7829295258406921\\n  },\\n  \\\"N=32\\\": {\\n    \\\"N\\\": 32,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.839572761831741,\\n    \\\"oracle_headroom_pp\\\": 19.988921835913953,\\n    \\\"degen_pct\\\": 3.9697542533081283,\\n    \\\"elapsed_s\\\": 3.5440638065338135,\\n    \\\"LP_sel_f1\\\": 0.6491559890620271,\\n    \\\"LP_delta_pp\\\": 0.9472445589425615,\\n    \\\"SJ_sel_f1\\\": 0.64316936661816,\\n    \\\"SJ_delta_pp\\\": 0.3485823145558564,\\n    \\\"FK_sel_f1\\\": 0.6461876673680299,\\n    \\\"FK_delta_pp\\\": 0.6504123895428426,\\n    \\\"EM_sel_f1\\\": 0.6419040884736426,\\n    \\\"EM_delta_pp\\\": 0.22205450010410743,\\n    \\\"VC_sel_f1\\\": 0.5961394255817696,\\n    \\\"VC_delta_pp\\\": -4.354411789083191,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.9472445589425615\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "8e613ecc-c183-4f5a-80a9-f6dcb5a1e701",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"N=2\\\\\\\": {\\\\n    \\\\\\\"N\\\\\\\": 2,\\\\n    \\\\\\\"n_gf\\\\\\\": 529,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.6396835434726015,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.6831851485554365,\\\\n    \\\\\\\"oracle_headroom_pp\\\\\\\": 4.350160508283507,\\\\n    \\\\\\\"degen_pct\\\\\\\": 42.722117202268436,\\\\n    \\\\\\\"elapsed_s\\\\\\\": 0.0437619686126709,\\\\n    \\\\\\\"LP_sel_f1\\\\\\\": 0.6307527958284102,\\\\n    \\\\\\\"LP_delta_pp\\\\\\\": -0.8930747644191328,\\\\n    \\\\\\\"SJ_sel_f1\\\\\\\": 0.6124373078643066,\\\\n    \\\\\\\"SJ_delta_pp\\\\\\\": -2.7246235608294866,\\\\n    \\\\\\\"FK_sel_f1\\\\\\\": 0.6124373078643066,\\\\n    \\\\\\\"FK_delta_pp\\\\\\\": -2.7246235608294866,\\\\n    \\\\\\\"EM_sel_f1\\\\\\\": 0.6124373078643066,\\\\n    \\\\\\\"EM_delta_pp\\\\\\\": -2.7246235608294866,\\\\n    \\\\\\\"VC_sel_f1\\\\\\\": 0.6130812581663244,\\\\n    \\\\\\\"VC_delta_pp\\\\\\\": -2.6602285306277063,\\\\n    \\\\\\\"best_signal\\\\\\\": \\\\\\\"LP\\\\\\\",\\\\n    \\\\\\\"best_delta_pp\\\\\\\": -0.8930747644191328\\\\n  },\\\\n  \\\\\\\"N=4\\\\\\\": {\\\\n    \\\\\\\"N\\\\\\\": 4,\\\\n    \\\\\\\"n_gf\\\\\\\": 529,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.6396835434726015,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.742071252999197,\\\\n    \\\\\\\"oracle_headroom_pp\\\\\\\": 10.238770952659548,\\\\n    \\\\\\\"degen_pct\\\\\\\": 20.982986767485823,\\\\n    \\\\\\\"elapsed_s\\\\\\\": 0.09875702857971191,\\\\n    \\\\\\\"LP_sel_f1\\\\\\\": 0.6399765693243954,\\\\n    \\\\\\\"LP_delta_pp\\\\\\\": 0.02930258517939155,\\\\n    \\\\\\\"SJ_sel_f1\\\\\\\": 0.6365973056065349,\\\\n    \\\\\\\"SJ_delta_pp\\\\\\\": -0.30862378660665435,\\\\n    \\\\\\\"FK_sel_f1\\\\\\\": 0.63568005440573,\\\\n    \\\\\\\"FK_delta_pp\\\\\\\": -0.4003489066871424,\\\\n    \\\\\\\"EM_sel_f1\\\\\\\": 0.632259535626043,\\\\n    \\\\\\\"EM_delta_pp\\\\\\\": -0.74240078465585,\\\\n    \\\\\\\"VC_sel_f1\\\\\\\": 0.6180644207220433,\\\\n    \\\\\\\"VC_delta_pp\\\\\\\": -2.1619122750558217,\\\\n    \\\\\\\"best_signal\\\\\\\": \\\\\\\"LP\\\\\\\",\\\\n    \\\\\\\"best_delta_pp\\\\\\\": 0.02930258517939155\\\\n  },\\\\n  \\\\\\\"N=8\\\\\\\": {\\\\n    \\\\\\\"N\\\\\\\": 8,\\\\n    \\\\\\\"n_gf\\\\\\\": 529,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.6396835434726015,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.784797595808938,\\\\n    \\\\\\\"oracle_headroom_pp\\\\\\\": 14.511405233633656,\\\\n    \\\\\\\"degen_pct\\\\\\\": 10.964083175803403,\\\\n    \\\\\\\"elapsed_s\\\\\\\": 0.2820611000061035,\\\\n    \\\\\\\"LP_sel_f1\\\\\\\": 0.6435647809077143,\\\\n    \\\\\\\"LP_delta_pp\\\\\\\": 0.38812374351128165,\\\\n    \\\\\\\"SJ_sel_f1\\\\\\\": 0.6416811520392083,\\\\n    \\\\\\\"SJ_delta_pp\\\\\\\": 0.1997608566606801,\\\\n    \\\\\\\"FK_sel_f1\\\\\\\": 0.6411876212054127,\\\\n    \\\\\\\"FK_delta_pp\\\\\\\": 0.15040777328112487,\\\\n    \\\\\\\"EM_sel_f1\\\\\\\": 0.6320061519216418,\\\\n    \\\\\\\"EM_delta_pp\\\\\\\": -0.76773915509597,\\\\n    \\\\\\\"VC_sel_f1\\\\\\\": 0.6110108962660947,\\\\n    \\\\\\\"VC_delta_pp\\\\\\\": -2.867264720650675,\\\\n    \\\\\\\"best_signal\\\\\\\": \\\\\\\"LP\\\\\\\",\\\\n    \\\\\\\"best_delta_pp\\\\\\\": 0.38812374351128165\\\\n  },\\\\n  \\\\\\\"N=16\\\\\\\": {\\\\n    \\\\\\\"N\\\\\\\": 16,\\\\n    \\\\\\\"n_gf\\\\\\\": 529,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.6396835434726015,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.8168792612554427,\\\\n    \\\\\\\"oracle_headroom_pp\\\\\\\": 17.719571778284127,\\\\n    \\\\\\\"degen_pct\\\\\\\": 7.372400756143667,\\\\n    \\\\\\\"elapsed_s\\\\\\\": 0.9487478733062744,\\\\n    \\\\\\\"LP_sel_f1\\\\\\\": 0.6475128387310084,\\\\n    \\\\\\\"LP_delta_pp\\\\\\\": 0.7829295258406921,\\\\n    \\\\\\\"SJ_sel_f1\\\\\\\": 0.6421272088179683,\\\\n    \\\\\\\"SJ_delta_pp\\\\\\\": 0.24436653453667745,\\\\n    \\\\\\\"FK_sel_f1\\\\\\\": 0.6394835911459953,\\\\n    \\\\\\\"FK_delta_pp\\\\\\\": -0.019995232660618978,\\\\n    \\\\\\\"EM_sel_f1\\\\\\\": 0.6391168134162686,\\\\n    \\\\\\\"EM_delta_pp\\\\\\\": -0.05667300563328981,\\\\n    \\\\\\\"VC_sel_f1\\\\\\\": 0.6002271095843874,\\\\n    \\\\\\\"VC_delta_pp\\\\\\\": -3.945643388821407,\\\\n    \\\\\\\"best_signal\\\\\\\": \\\\\\\"LP\\\\\\\",\\\\n    \\\\\\\"best_delta_pp\\\\\\\": 0.7829295258406921\\\\n  },\\\\n  \\\\\\\"N=32\\\\\\\": {\\\\n    \\\\\\\"N\\\\\\\": 32,\\\\n    \\\\\\\"n_gf\\\\\\\": 529,\\\\n    \\\\\\\"greedy_f1\\\\\\\": 0.6396835434726015,\\\\n    \\\\\\\"oracle_f1\\\\\\\": 0.839572761831741,\\\\n    \\\\\\\"oracle_headroom_pp\\\\\\\": 19.988921835913953,\\\\n    \\\\\\\"degen_pct\\\\\\\": 3.9697542533081283,\\\\n    \\\\\\\"elapsed_s\\\\\\\": 3.5440638065338135,\\\\n    \\\\\\\"LP_sel_f1\\\\\\\": 0.6491559890620271,\\\\n    \\\\\\\"LP_delta_pp\\\\\\\": 0.9472445589425615,\\\\n    \\\\\\\"SJ_sel_f1\\\\\\\": 0.64316936661816,\\\\n    \\\\\\\"SJ_delta_pp\\\\\\\": 0.3485823145558564,\\\\n    \\\\\\\"FK_sel_f1\\\\\\\": 0.6461876673680299,\\\\n    \\\\\\\"FK_delta_pp\\\\\\\": 0.6504123895428426,\\\\n    \\\\\\\"EM_sel_f1\\\\\\\": 0.6419040884736426,\\\\n    \\\\\\\"EM_delta_pp\\\\\\\": 0.22205450010410743,\\\\n    \\\\\\\"VC_sel_f1\\\\\\\": 0.5961394255817696,\\\\n    \\\\\\\"VC_delta_pp\\\\\\\": -4.354411789083191,\\\\n    \\\\\\\"best_signal\\\\\\\": \\\\\\\"LP\\\\\\\",\\\\n    \\\\\\\"best_delta_pp\\\\\\\": 0.9472445589425615\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"N=2\\\": {\\n    \\\"N\\\": 2,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.6831851485554365,\\n    \\\"oracle_headroom_pp\\\": 4.350160508283507,\\n    \\\"degen_pct\\\": 42.722117202268436,\\n    \\\"elapsed_s\\\": 0.0437619686126709,\\n    \\\"LP_sel_f1\\\": 0.6307527958284102,\\n    \\\"LP_delta_pp\\\": -0.8930747644191328,\\n    \\\"SJ_sel_f1\\\": 0.6124373078643066,\\n    \\\"SJ_delta_pp\\\": -2.7246235608294866,\\n    \\\"FK_sel_f1\\\": 0.6124373078643066,\\n    \\\"FK_delta_pp\\\": -2.7246235608294866,\\n    \\\"EM_sel_f1\\\": 0.6124373078643066,\\n    \\\"EM_delta_pp\\\": -2.7246235608294866,\\n    \\\"VC_sel_f1\\\": 0.6130812581663244,\\n    \\\"VC_delta_pp\\\": -2.6602285306277063,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": -0.8930747644191328\\n  },\\n  \\\"N=4\\\": {\\n    \\\"N\\\": 4,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.742071252999197,\\n    \\\"oracle_headroom_pp\\\": 10.238770952659548,\\n    \\\"degen_pct\\\": 20.982986767485823,\\n    \\\"elapsed_s\\\": 0.09875702857971191,\\n    \\\"LP_sel_f1\\\": 0.6399765693243954,\\n    \\\"LP_delta_pp\\\": 0.02930258517939155,\\n    \\\"SJ_sel_f1\\\": 0.6365973056065349,\\n    \\\"SJ_delta_pp\\\": -0.30862378660665435,\\n    \\\"FK_sel_f1\\\": 0.63568005440573,\\n    \\\"FK_delta_pp\\\": -0.4003489066871424,\\n    \\\"EM_sel_f1\\\": 0.632259535626043,\\n    \\\"EM_delta_pp\\\": -0.74240078465585,\\n    \\\"VC_sel_f1\\\": 0.6180644207220433,\\n    \\\"VC_delta_pp\\\": -2.1619122750558217,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.02930258517939155\\n  },\\n  \\\"N=8\\\": {\\n    \\\"N\\\": 8,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.784797595808938,\\n    \\\"oracle_headroom_pp\\\": 14.511405233633656,\\n    \\\"degen_pct\\\": 10.964083175803403,\\n    \\\"elapsed_s\\\": 0.2820611000061035,\\n    \\\"LP_sel_f1\\\": 0.6435647809077143,\\n    \\\"LP_delta_pp\\\": 0.38812374351128165,\\n    \\\"SJ_sel_f1\\\": 0.6416811520392083,\\n    \\\"SJ_delta_pp\\\": 0.1997608566606801,\\n    \\\"FK_sel_f1\\\": 0.6411876212054127,\\n    \\\"FK_delta_pp\\\": 0.15040777328112487,\\n    \\\"EM_sel_f1\\\": 0.6320061519216418,\\n    \\\"EM_delta_pp\\\": -0.76773915509597,\\n    \\\"VC_sel_f1\\\": 0.6110108962660947,\\n    \\\"VC_delta_pp\\\": -2.867264720650675,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.38812374351128165\\n  },\\n  \\\"N=16\\\": {\\n    \\\"N\\\": 16,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.8168792612554427,\\n    \\\"oracle_headroom_pp\\\": 17.719571778284127,\\n    \\\"degen_pct\\\": 7.372400756143667,\\n    \\\"elapsed_s\\\": 0.9487478733062744,\\n    \\\"LP_sel_f1\\\": 0.6475128387310084,\\n    \\\"LP_delta_pp\\\": 0.7829295258406921,\\n    \\\"SJ_sel_f1\\\": 0.6421272088179683,\\n    \\\"SJ_delta_pp\\\": 0.24436653453667745,\\n    \\\"FK_sel_f1\\\": 0.6394835911459953,\\n    \\\"FK_delta_pp\\\": -0.019995232660618978,\\n    \\\"EM_sel_f1\\\": 0.6391168134162686,\\n    \\\"EM_delta_pp\\\": -0.05667300563328981,\\n    \\\"VC_sel_f1\\\": 0.6002271095843874,\\n    \\\"VC_delta_pp\\\": -3.945643388821407,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.7829295258406921\\n  },\\n  \\\"N=32\\\": {\\n    \\\"N\\\": 32,\\n    \\\"n_gf\\\": 529,\\n    \\\"greedy_f1\\\": 0.6396835434726015,\\n    \\\"oracle_f1\\\": 0.839572761831741,\\n    \\\"oracle_headroom_pp\\\": 19.988921835913953,\\n    \\\"degen_pct\\\": 3.9697542533081283,\\n    \\\"elapsed_s\\\": 3.5440638065338135,\\n    \\\"LP_sel_f1\\\": 0.6491559890620271,\\n    \\\"LP_delta_pp\\\": 0.9472445589425615,\\n    \\\"SJ_sel_f1\\\": 0.64316936661816,\\n    \\\"SJ_delta_pp\\\": 0.3485823145558564,\\n    \\\"FK_sel_f1\\\": 0.6461876673680299,\\n    \\\"FK_delta_pp\\\": 0.6504123895428426,\\n    \\\"EM_sel_f1\\\": 0.6419040884736426,\\n    \\\"EM_delta_pp\\\": 0.22205450010410743,\\n    \\\"VC_sel_f1\\\": 0.5961394255817696,\\n    \\\"VC_delta_pp\\\": -4.354411789083191,\\n    \\\"best_signal\\\": \\\"LP\\\",\\n    \\\"best_delta_pp\\\": 0.9472445589425615\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_01GNxPqCDTQ5h7mBq1mJELtg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 968,
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
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c8dc3cb5-5f34-4490-9df0-cbb4ef5ef5ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127XuuRystFDgTrKvS9oeGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4437,
      "cache_read_input_tokens": 60074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4437
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

_source line 90 · 2026-05-19T08:04:10.838Z_

<details><summary>↩ Tool result · `toolu_01GNxPqCDTQ5h7mBq1mJELtg`</summary>

```text
968	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
969	
970	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
971	
972	\begin{table}[t]
973	\centering
974	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
975	\label{tab:n-scaling}
976	\small
977	\begin{tabular}{l ccc ccc}
978	\toprule
979	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
980	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
981	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
982	\midrule
983	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
984	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
985	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
986	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
987	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
988	\midrule
989	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
990	\bottomrule
991	\end{tabular}
992	\end{table}
993	
994	\begin{table}[t]
995	\centering
996	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
997	\label{tab:ranking-stability}
998	\small
999	\begin{tabular}{ll cc l}
1000	\toprule
1001	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
1002	\midrule
1003	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1004	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
1005	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1006	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
1007	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
1008	\bottomrule
1009	\end{tabular}
1010	\end{table}
1011	
1012	\begin{table}[t]
1013	\centering
1014	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
1015	\label{tab:sigma-comparison}
1016	\small
1017	\begin{tabular}{l cc cc}
1018	\toprule
1019	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
1020	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1021	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
1022	\midrule
1023	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
1024	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
1025	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
1026	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
1027	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
1028	\midrule
1029	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
1030	\bottomrule
1031	\end{tabular}
1032	\end{table}
1033	
1034	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
1035	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
1036	
1037	\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
1038	Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
1039	Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).
1040	LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\% and oracle headroom reaches ${\sim}20$~pp, the best signal captures less than 5\% of the available improvement.
1041	Degeneracy drops monotonically (43\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
1042	VC selection degrades with increasing $N$ ($-2.66$~pp at $N{=}2$ to $-4.35$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
1043	
1044	\begin{table}[t]
1045	\centering
1046	\small
1047	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
1048	\label{tab:n_scaling_selection}
1049	\begin{tabular}{ccccccccc}
1050	\toprule
1051	$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
1052	\midrule
1053	2 & 42.7\% & $+$4.4 & $-$0.89 & $-$2.72 & $-$2.72 & $-$2.72 & $-$2.66 & $-$0.89 \\
1054	4 & 21.0\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\
1055	8 & 11.0\% & $+$14.5 & $+$0.39 & $+$0.20 & $+$0.15 & $-$0.77 & $-$2.87 & $+$0.39 \\
1056	16 & 7.4\% & $+$17.7 & $+$0.78 & $+$0.24 & $-$0.02 & $-$0.06 & $-$3.95 & $+$0.78 \\
1057	32 & 4.0\% & $+$20.0 & $+$0.95 & $+$0.35 & $+$0.65 & $+$0.22 & $-$4.35 & $+$0.95 \\
1058	\bottomrule
1059	\end{tabular}
1060	\end{table}
1061	\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$). Values differ slightly from Table~\ref{tab:selection} (0.645) and Table~\ref{tab:fewnerd} (0.644) due to seed and aggregation differences; relative trends are consistent.}
1062	
1063	\paragraph{Bootstrap significance at $N{=}32$.}
1064	Table~\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).
1065	No signal achieves significant improvement over greedy at $\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \textit{worse} ($-4.36$~pp, $p{=}1.0$).
1066	However, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test); the signals carry meaningful quality information yet fail to translate it into reliable selection gains.
1067	The oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "16011f89-64c7-459d-ba3b-a609f44766e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER); additional samples stabilize structural signals more than LP.\n\n\\paragraph{$N$-scaling: selection headroom vs.\\ selection gain.}\nTable~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\nOracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}20$~pp, the best signal captures less than 5\\% of the available improvement.\nDegeneracy drops monotonically (43\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\nVC selection degrades with increasing $N$ ($-2.66$~pp at $N{=}2$ to $-4.35$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\n\\label{tab:n_scaling_selection}\n\\begin{tabular}{ccccccccc}\n\\toprule\n$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\\n\\midrule\n2 & 42.7\\% & $+$4.4 & $-$0.89 & $-$2.72 & $-$2.72 & $-$2.72 & $-$2.66 & $-$0.89 \\\\\n4 & 21.0\\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\\\\n8 & 11.0\\% & $+$14.5 & $+$0.39 & $+$0.20 & $+$0.15 & $-$0.77 & $-$2.87 & $+$0.39 \\\\\n16 & 7.4\\% & $+$17.7 & $+$0.78 & $+$0.24 & $-$0.02 & $-$0.06 & $-$3.95 & $+$0.78 \\\\\n32 & 4.0\\% & $+$20.0 & $+$0.95 & $+$0.35 & $+$0.65 & $+$0.22 & $-$4.35 & $+$0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$). Values differ slightly from Table~\\ref{tab:selection} (0.645) and Table~\\ref{tab:fewnerd} (0.644) due to seed and aggregation differences; relative trends are consistent.}\n\n\\paragraph{Bootstrap significance at $N{=}32$.}\nTable~\\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).\nNo signal achieves significant improvement over greedy at $\\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \\textit{worse} ($-4.36$~pp, $p{=}1.0$).\nHowever, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test); the signals carry meaningful quality information yet fail to translate it into reliable selection gains.\nThe oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.",
      "numLines": 100,
      "startLine": 968,
      "totalLines": 1572
    }
  }
}
```

</details>

---


### Assistant

_source line 91_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. The Appendix `app:n_scaling` only contains **SciERC** data. It has no FewNERD N=16 data at all. This confirms the audit finding.

Let me now look at the entity construction results to trace the "+1.32pp" number.

Let me check the entity construction results for N=16.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "86b4bc09-c477-4f70-9b35-4369c3d92d34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xj7PdP9XfXxjBs2atdpF9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6467,
      "cache_read_input_tokens": 64511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6467
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

_source line 92_

The appendix `app:n_scaling` only contains SciERC data — no FewNERD. Now let me check the entity construction results for the N=16 "+1.32pp" claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c6246917-3fdc-4acc-8703-6e6451a62247",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xj7PdP9XfXxjBs2atdpF9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6467,
      "cache_read_input_tokens": 64511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6467
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

_source line 93_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SMf3ZLN1PnXHAxG4Q7E49z`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "243b2b62-b9ac-4ed1-b142-a08ebd65a84b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xj7PdP9XfXxjBs2atdpF9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6467,
      "cache_read_input_tokens": 64511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6467
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

_source line 94 · 2026-05-19T08:04:19.524Z_

<details><summary>↩ Tool result · `toolu_01SMf3ZLN1PnXHAxG4Q7E49z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"greedy\\\": {\\n      \\\"F1\\\": 0.6441821796820129,\\n      \\\"P\\\": 0.6603624688690851,\\n      \\\"R\\\": 0.6592213866788535,\\n      \\\"F1_ci\\\": [\\n        0.6441821796820129,\\n        0.6176077230897646,\\n        0.6696392929629891\\n      ]\\n    },\\n    \\\"lp_selection\\\": {\\n      \\\"F1\\\": 0.6465303389349577,\\n      \\\"P\\\": 0.6573904041767935,\\n      \\\"R\\\": 0.6673611832402002,\\n      \\\"F1_ci\\\": [\\n        0.6465303389349577,\\n        0.6205930208003457,\\n        0.6704501894665882\\n      ]\\n    },\\n    \\\"sj_selection\\\": {\\n      \\\"F1\\\": 0.5852966275038706,\\n      \\\"P\\\": 0.6395602664506257,\\n      \\\"R\\\": 0.5711171468732904,\\n      \\\"F1_ci\\\": [\\n        0.5852966275038706,\\n        0.556005787952858,\\n        0.6152187447083478\\n      ]\\n    },\\n    \\\"oracle\\\": {\\n      \\\"F1\\\": 0.8193707573669766,\\n      \\\"P\\\": 0.8411265640471689,\\n      \\\"R\\\": 0.8225174321582639,\\n      \\\"F1_ci\\\": [\\n        0.8193707573669766,\\n        0.7989642787374356,\\n        0.8384514456348106\\n      ]\\n    },\\n    \\\"random\\\": {\\n      \\\"F1\\\": 0.6101006899591651,\\n      \\\"F1_ci\\\": [\\n        0.6101006899591651,\\n        0.5876596860410922,\\n        0.6321353597483295\\n      ]\\n    },\\n    \\\"re_greedy\\\": {\\n      \\\"F1\\\": 0.4756774419595503,\\n      \\\"P\\\": 0.4801939186627277,\\n      \\\"R\\\": 0.4877418527702082\\n    },\\n    \\\"re_lp_selection\\\": {\\n      \\\"F1\\\": 0.42991434662178574,\\n      \\\"P\\\": 0.42879415270719623,\\n      \\\"R\\\": 0.44988966085374404\\n    },\\n    \\\"re_oracle\\\": {\\n      \\\"F1\\\": 0.7109748530131049\\n    },\\n    \\\"construction_uniform_t0.1\\\": {\\n      \\\"F1\\\": 0.6469695336362352,\\n      \\\"P\\\": 0.5795871346674749,\\n      \\\"R\\\": 0.7928432940720276,\\n      \\\"F1_ci\\\": [\\n        0.6469695336362352,\\n        0.6232693678219065,\\n        0.6686463012077631\\n      ],\\n      \\\"threshold\\\": 0.1,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.43690358432159904,\\n      \\\"RE_P\\\": 0.3902232064883426,\\n      \\\"RE_R\\\": 0.5647035436732979\\n    },\\n    \\\"construction_uniform_t0.2\\\": {\\n      \\\"F1\\\": 0.6637070316293044,\\n      \\\"P\\\": 0.6352976838326555,\\n      \\\"R\\\": 0.7410311805396871,\\n      \\\"F1_ci\\\": [\\n        0.6637070316293044,\\n        0.6387957431574689,\\n        0.6860671791729281\\n      ],\\n      \\\"threshold\\\": 0.2,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.48481421805396013,\\n      \\\"RE_P\\\": 0.4683931537901292,\\n      \\\"RE_R\\\": 0.541558577947992\\n    },\\n    \\\"construction_uniform_t0.3\\\": {\\n      \\\"F1\\\": 0.6615770786042108,\\n      \\\"P\\\": 0.6462090524472376,\\n      \\\"R\\\": 0.7204082621851997,\\n      \\\"F1_ci\\\": [\\n        0.6615770786042108,\\n        0.6361103202368631,\\n        0.6844515600909462\\n      ],\\n      \\\"threshold\\\": 0.3,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.4899703009594036,\\n      \\\"RE_P\\\": 0.4872767644034185,\\n      \\\"RE_R\\\": 0.5226864922517096\\n    },\\n    \\\"construction_uniform_t0.4\\\": {\\n      \\\"F1\\\": 0.6576532725092716,\\n      \\\"P\\\": 0.6759999399885979,\\n      \\\"R\\\": 0.6757057687114398,\\n      \\\"F1_ci\\\": [\\n        0.6576532725092716,\\n        0.6314842705757862,\\n        0.6823670047288417\\n      ],\\n      \\\"threshold\\\": 0.4,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.49630200748014597,\\n      \\\"RE_P\\\": 0.5132024402818354,\\n      \\\"RE_R\\\": 0.5031662834120301\\n    },\\n    \\\"construction_uniform_t0.5\\\": {\\n      \\\"F1\\\": 0.6528146920529592,\\n      \\\"P\\\": 0.6846828397395505,\\n      \\\"R\\\": 0.65596726839638,\\n      \\\"F1_ci\\\": [\\n        0.6528146920529592,\\n        0.6258234468108229,\\n        0.6779823428905756\\n      ],\\n      \\\"threshold\\\": 0.5,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.4926901603900381,\\n      \\\"RE_P\\\": 0.5230795669358995,\\n      \\\"RE_R\\\": 0.4877283502047207\\n    },\\n    \\\"construction_uniform_t0.6\\\": {\\n      \\\"F1\\\": 0.6153159116902848,\\n      \\\"P\\\": 0.6862243826327001,\\n      \\\"R\\\": 0.5922599139990444,\\n      \\\"F1_ci\\\": [\\n        0.6153159116902848,\\n        0.5876963670013234,\\n        0.6422491495536612\\n      ],\\n      \\\"threshold\\\": 0.6,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.4767985850466669,\\n      \\\"RE_P\\\": 0.5291512205500863,\\n      \\\"RE_R\\\": 0.4581442292217339\\n    },\\n    \\\"construction_uniform_t0.7\\\": {\\n      \\\"F1\\\": 0.5822513688347933,\\n      \\\"P\\\": 0.687550634620578,\\n      \\\"R\\\": 0.541872840455071,\\n      \\\"F1_ci\\\": [\\n        0.5822513688347933,\\n        0.5530255078608477,\\n        0.61\\n\\n... [截断: 输出过长，省略 13621 字符] ...\\n\\n2697953\\n      ],\\n      \\\"threshold\\\": 0.5,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"P\\\": 0.7342621290919181,\\n      \\\"R\\\": 0.6448465220021863,\\n      \\\"F1_ci\\\": [\\n        0.6712108628975318,\\n        0.6595751434559981,\\n        0.682044076470082\\n      ],\\n      \\\"threshold\\\": 0.6,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.7\\\": {\\n      \\\"F1\\\": 0.591199095415274,\\n      \\\"P\\\": 0.6864205586798093,\\n      \\\"R\\\": 0.5497497788081852,\\n      \\\"F1_ci\\\": [\\n        0.591199095415274,\\n        0.579234940607012,\\n        0.6029485038882076\\n      ],\\n      \\\"threshold\\\": 0.7,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"P\\\": 0.6437124725679081,\\n      \\\"R\\\": 0.4869106164546503,\\n      \\\"F1_ci\\\": [\\n        0.5339617561124026,\\n        0.5215417782974746,\\n        0.5460491685629593\\n      ],\\n      \\\"threshold\\\": 0.8,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.9\\\": {\\n      \\\"F1\\\": 0.34048116114025495,\\n      \\\"P\\\": 0.46301051026401524,\\n      \\\"R\\\": 0.2913081487540279,\\n      \\\"F1_ci\\\": [\\n        0.34048116114025495,\\n        0.32917991358764737,\\n        0.3516075064993751\\n      ],\\n      \\\"threshold\\\": 0.9,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.1\\\": {\\n      \\\"F1\\\": 0.7328569407749095,\\n      \\\"P\\\": 0.6589371324647737,\\n      \\\"R\\\": 0.8821899039113171,\\n      \\\"F1_ci\\\": [\\n        0.7328569407749095,\\n        0.7249552558205652,\\n        0.7403962650245636\\n      ],\\n      \\\"threshold\\\": 0.1,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.2\\\": {\\n      \\\"F1\\\": 0.7621279480308844,\\n      \\\"P\\\": 0.7339500482793615,\\n      \\\"R\\\": 0.8206917043039286,\\n      \\\"F1_ci\\\": [\\n        0.7621279480308844,\\n        0.7529999283446229,\\n        0.771106466187632\\n      ],\\n      \\\"threshold\\\": 0.2,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.3\\\": {\\n      \\\"F1\\\": 0.7613280913427132,\\n      \\\"P\\\": 0.7489693319776569,\\n      \\\"R\\\": 0.7972872742541721,\\n      \\\"F1_ci\\\": [\\n        0.7613280913427132,\\n        0.7517992142017296,\\n        0.7704520966862431\\n      ],\\n      \\\"threshold\\\": 0.3,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.4\\\": {\\n      \\\"F1\\\": 0.7403014922869728,\\n      \\\"P\\\": 0.7563222548400211,\\n      \\\"R\\\": 0.7450454192859323,\\n      \\\"F1_ci\\\": [\\n        0.7403014922869728,\\n        0.7300516285129836,\\n        0.750152931985901\\n      ],\\n      \\\"threshold\\\": 0.4,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.5\\\": {\\n      \\\"F1\\\": 0.7183834375032269,\\n      \\\"P\\\": 0.7510840095227834,\\n      \\\"R\\\": 0.7097263353928221,\\n      \\\"F1_ci\\\": [\\n        0.7183834375032269,\\n        0.7073732442492698,\\n        0.7289286995601849\\n      ],\\n      \\\"threshold\\\": 0.5,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"P\\\": 0.7342621290919181,\\n      \\\"R\\\": 0.6448465220021863,\\n      \\\"F1_ci\\\": [\\n        0.6712108628975318,\\n        0.6595751434559981,\\n        0.682044076470082\\n      ],\\n      \\\"threshold\\\": 0.6,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.7\\\": {\\n      \\\"F1\\\": 0.6181885284709259,\\n      \\\"P\\\": 0.7094420862979814,\\n      \\\"R\\\": 0.5781943296096657,\\n      \\\"F1_ci\\\": [\\n        0.6181885284709259,\\n        0.6065476945549937,\\n        0.6296751796722696\\n      ],\\n      \\\"threshold\\\": 0.7,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"P\\\": 0.6437124725679081,\\n      \\\"R\\\": 0.4869106164546503,\\n      \\\"F1_ci\\\": [\\n        0.5339617561124026,\\n        0.5215417782974746,\\n        0.5460491685629593\\n      ],\\n      \\\"threshold\\\": 0.8,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.9\\\": {\\n      \\\"F1\\\": 0.34303959507078724,\\n      \\\"P\\\": 0.46645799360117907,\\n      \\\"R\\\": 0.2935107075527715,\\n      \\\"F1_ci\\\": [\\n        0.34303959507078724,\\n        0.33173607672333816,\\n        0.3542600354286932\\n      ],\\n      \\\"threshold\\\": 0.9,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "107a6e1f-b8d9-4a8b-beec-0a1fa4f22e5d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"greedy\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6441821796820129,\\\\n      \\\\\\\"P\\\\\\\": 0.6603624688690851,\\\\n      \\\\\\\"R\\\\\\\": 0.6592213866788535,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6441821796820129,\\\\n        0.6176077230897646,\\\\n        0.6696392929629891\\\\n      ]\\\\n    },\\\\n    \\\\\\\"lp_selection\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6465303389349577,\\\\n      \\\\\\\"P\\\\\\\": 0.6573904041767935,\\\\n      \\\\\\\"R\\\\\\\": 0.6673611832402002,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6465303389349577,\\\\n        0.6205930208003457,\\\\n        0.6704501894665882\\\\n      ]\\\\n    },\\\\n    \\\\\\\"sj_selection\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5852966275038706,\\\\n      \\\\\\\"P\\\\\\\": 0.6395602664506257,\\\\n      \\\\\\\"R\\\\\\\": 0.5711171468732904,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.5852966275038706,\\\\n        0.556005787952858,\\\\n        0.6152187447083478\\\\n      ]\\\\n    },\\\\n    \\\\\\\"oracle\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.8193707573669766,\\\\n      \\\\\\\"P\\\\\\\": 0.8411265640471689,\\\\n      \\\\\\\"R\\\\\\\": 0.8225174321582639,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.8193707573669766,\\\\n        0.7989642787374356,\\\\n        0.8384514456348106\\\\n      ]\\\\n    },\\\\n    \\\\\\\"random\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6101006899591651,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6101006899591651,\\\\n        0.5876596860410922,\\\\n        0.6321353597483295\\\\n      ]\\\\n    },\\\\n    \\\\\\\"re_greedy\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.4756774419595503,\\\\n      \\\\\\\"P\\\\\\\": 0.4801939186627277,\\\\n      \\\\\\\"R\\\\\\\": 0.4877418527702082\\\\n    },\\\\n    \\\\\\\"re_lp_selection\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.42991434662178574,\\\\n      \\\\\\\"P\\\\\\\": 0.42879415270719623,\\\\n      \\\\\\\"R\\\\\\\": 0.44988966085374404\\\\n    },\\\\n    \\\\\\\"re_oracle\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7109748530131049\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.1\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6469695336362352,\\\\n      \\\\\\\"P\\\\\\\": 0.5795871346674749,\\\\n      \\\\\\\"R\\\\\\\": 0.7928432940720276,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6469695336362352,\\\\n        0.6232693678219065,\\\\n        0.6686463012077631\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.1,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n      \\\\\\\"RE_F1\\\\\\\": 0.43690358432159904,\\\\n      \\\\\\\"RE_P\\\\\\\": 0.3902232064883426,\\\\n      \\\\\\\"RE_R\\\\\\\": 0.5647035436732979\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.2\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6637070316293044,\\\\n      \\\\\\\"P\\\\\\\": 0.6352976838326555,\\\\n      \\\\\\\"R\\\\\\\": 0.7410311805396871,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6637070316293044,\\\\n        0.6387957431574689,\\\\n        0.6860671791729281\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.2,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n      \\\\\\\"RE_F1\\\\\\\": 0.48481421805396013,\\\\n      \\\\\\\"RE_P\\\\\\\": 0.4683931537901292,\\\\n      \\\\\\\"RE_R\\\\\\\": 0.541558577947992\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.3\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6615770786042108,\\\\n      \\\\\\\"P\\\\\\\": 0.6462090524472376,\\\\n      \\\\\\\"R\\\\\\\": 0.7204082621851997,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6615770786042108,\\\\n        0.6361103202368631,\\\\n        0.6844515600909462\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.3,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n      \\\\\\\"RE_F1\\\\\\\": 0.4899703009594036,\\\\n      \\\\\\\"RE_P\\\\\\\": 0.4872767644034185,\\\\n      \\\\\\\"RE_R\\\\\\\": 0.5226864922517096\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.4\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6576532725092716,\\\\n      \\\\\\\"P\\\\\\\": 0.6759999399885979,\\\\n      \\\\\\\"R\\\\\\\": 0.6757057687114398,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6576532725092716,\\\\n        0.6314842705757862,\\\\n        0.6823670047288417\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.4,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n      \\\\\\\"RE_F1\\\\\\\": 0.49630200748014597,\\\\n      \\\\\\\"RE_P\\\\\\\": 0.5132024402818354,\\\\n      \\\\\\\"RE_R\\\\\\\": 0.5031662834120301\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.5\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6528146920529592,\\\\n      \\\\\\\"P\\\\\\\": 0.6846828397395505,\\\\n      \\\\\\\"R\\\\\\\": 0.65596726839638,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6528146920529592,\\\\n        0.6258234468108229,\\\\n        0.6779823428905756\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.5,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n      \\\\\\\"RE_F1\\\\\\\": 0.4926901603900381,\\\\n      \\\\\\\"RE_P\\\\\\\": 0.5230795669358995,\\\\n      \\\\\\\"RE_R\\\\\\\": 0.4877283502047207\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.6\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6153159116902848,\\\\n      \\\\\\\"P\\\\\\\": 0.6862243826327001,\\\\n      \\\\\\\"R\\\\\\\": 0.5922599139990444,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6153159116902848,\\\\n        0.5876963670013234,\\\\n        0.6422491495536612\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.6,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n      \\\\\\\"RE_F1\\\\\\\": 0.4767985850466669,\\\\n      \\\\\\\"RE_P\\\\\\\": 0.5291512205500863,\\\\n      \\\\\\\"RE_R\\\\\\\": 0.4581442292217339\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.7\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5822513688347933,\\\\n      \\\\\\\"P\\\\\\\": 0.687550634620578,\\\\n      \\\\\\\"R\\\\\\\": 0.541872840455071,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.5822513688347933,\\\\n        0.5530255078608477,\\\\n        0.61\\\\n\\\\n... [截断: 输出过长，省略 13621 字符] ...\\\\n\\\\n2697953\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.5,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.6\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6712108628975318,\\\\n      \\\\\\\"P\\\\\\\": 0.7342621290919181,\\\\n      \\\\\\\"R\\\\\\\": 0.6448465220021863,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6712108628975318,\\\\n        0.6595751434559981,\\\\n        0.682044076470082\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.6,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.7\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.591199095415274,\\\\n      \\\\\\\"P\\\\\\\": 0.6864205586798093,\\\\n      \\\\\\\"R\\\\\\\": 0.5497497788081852,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.591199095415274,\\\\n        0.579234940607012,\\\\n        0.6029485038882076\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.7,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.8\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5339617561124026,\\\\n      \\\\\\\"P\\\\\\\": 0.6437124725679081,\\\\n      \\\\\\\"R\\\\\\\": 0.4869106164546503,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.5339617561124026,\\\\n        0.5215417782974746,\\\\n        0.5460491685629593\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.8,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_uniform_t0.9\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.34048116114025495,\\\\n      \\\\\\\"P\\\\\\\": 0.46301051026401524,\\\\n      \\\\\\\"R\\\\\\\": 0.2913081487540279,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.34048116114025495,\\\\n        0.32917991358764737,\\\\n        0.3516075064993751\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.9,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"uniform\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.1\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7328569407749095,\\\\n      \\\\\\\"P\\\\\\\": 0.6589371324647737,\\\\n      \\\\\\\"R\\\\\\\": 0.8821899039113171,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.7328569407749095,\\\\n        0.7249552558205652,\\\\n        0.7403962650245636\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.1,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.2\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7621279480308844,\\\\n      \\\\\\\"P\\\\\\\": 0.7339500482793615,\\\\n      \\\\\\\"R\\\\\\\": 0.8206917043039286,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.7621279480308844,\\\\n        0.7529999283446229,\\\\n        0.771106466187632\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.2,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.3\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7613280913427132,\\\\n      \\\\\\\"P\\\\\\\": 0.7489693319776569,\\\\n      \\\\\\\"R\\\\\\\": 0.7972872742541721,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.7613280913427132,\\\\n        0.7517992142017296,\\\\n        0.7704520966862431\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.3,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.4\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7403014922869728,\\\\n      \\\\\\\"P\\\\\\\": 0.7563222548400211,\\\\n      \\\\\\\"R\\\\\\\": 0.7450454192859323,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.7403014922869728,\\\\n        0.7300516285129836,\\\\n        0.750152931985901\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.4,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.5\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7183834375032269,\\\\n      \\\\\\\"P\\\\\\\": 0.7510840095227834,\\\\n      \\\\\\\"R\\\\\\\": 0.7097263353928221,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.7183834375032269,\\\\n        0.7073732442492698,\\\\n        0.7289286995601849\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.5,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.6\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6712108628975318,\\\\n      \\\\\\\"P\\\\\\\": 0.7342621290919181,\\\\n      \\\\\\\"R\\\\\\\": 0.6448465220021863,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6712108628975318,\\\\n        0.6595751434559981,\\\\n        0.682044076470082\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.6,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.7\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6181885284709259,\\\\n      \\\\\\\"P\\\\\\\": 0.7094420862979814,\\\\n      \\\\\\\"R\\\\\\\": 0.5781943296096657,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.6181885284709259,\\\\n        0.6065476945549937,\\\\n        0.6296751796722696\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.7,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.8\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5339617561124026,\\\\n      \\\\\\\"P\\\\\\\": 0.6437124725679081,\\\\n      \\\\\\\"R\\\\\\\": 0.4869106164546503,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.5339617561124026,\\\\n        0.5215417782974746,\\\\n        0.5460491685629593\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.8,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_t0.9\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.34303959507078724,\\\\n      \\\\\\\"P\\\\\\\": 0.46645799360117907,\\\\n      \\\\\\\"R\\\\\\\": 0.2935107075527715,\\\\n      \\\\\\\"F1_ci\\\\\\\": [\\\\n        0.34303959507078724,\\\\n        0.33173607672333816,\\\\n        0.3542600354286932\\\\n      ],\\\\n      \\\\\\\"threshold\\\\\\\": 0.9,\\\\n      \\\\\\\"variant\\\\\\\": \\\\\\\"lp_weighted\\\\\\\"\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"greedy\\\": {\\n      \\\"F1\\\": 0.6441821796820129,\\n      \\\"P\\\": 0.6603624688690851,\\n      \\\"R\\\": 0.6592213866788535,\\n      \\\"F1_ci\\\": [\\n        0.6441821796820129,\\n        0.6176077230897646,\\n        0.6696392929629891\\n      ]\\n    },\\n    \\\"lp_selection\\\": {\\n      \\\"F1\\\": 0.6465303389349577,\\n      \\\"P\\\": 0.6573904041767935,\\n      \\\"R\\\": 0.6673611832402002,\\n      \\\"F1_ci\\\": [\\n        0.6465303389349577,\\n        0.6205930208003457,\\n        0.6704501894665882\\n      ]\\n    },\\n    \\\"sj_selection\\\": {\\n      \\\"F1\\\": 0.5852966275038706,\\n      \\\"P\\\": 0.6395602664506257,\\n      \\\"R\\\": 0.5711171468732904,\\n      \\\"F1_ci\\\": [\\n        0.5852966275038706,\\n        0.556005787952858,\\n        0.6152187447083478\\n      ]\\n    },\\n    \\\"oracle\\\": {\\n      \\\"F1\\\": 0.8193707573669766,\\n      \\\"P\\\": 0.8411265640471689,\\n      \\\"R\\\": 0.8225174321582639,\\n      \\\"F1_ci\\\": [\\n        0.8193707573669766,\\n        0.7989642787374356,\\n        0.8384514456348106\\n      ]\\n    },\\n    \\\"random\\\": {\\n      \\\"F1\\\": 0.6101006899591651,\\n      \\\"F1_ci\\\": [\\n        0.6101006899591651,\\n        0.5876596860410922,\\n        0.6321353597483295\\n      ]\\n    },\\n    \\\"re_greedy\\\": {\\n      \\\"F1\\\": 0.4756774419595503,\\n      \\\"P\\\": 0.4801939186627277,\\n      \\\"R\\\": 0.4877418527702082\\n    },\\n    \\\"re_lp_selection\\\": {\\n      \\\"F1\\\": 0.42991434662178574,\\n      \\\"P\\\": 0.42879415270719623,\\n      \\\"R\\\": 0.44988966085374404\\n    },\\n    \\\"re_oracle\\\": {\\n      \\\"F1\\\": 0.7109748530131049\\n    },\\n    \\\"construction_uniform_t0.1\\\": {\\n      \\\"F1\\\": 0.6469695336362352,\\n      \\\"P\\\": 0.5795871346674749,\\n      \\\"R\\\": 0.7928432940720276,\\n      \\\"F1_ci\\\": [\\n        0.6469695336362352,\\n        0.6232693678219065,\\n        0.6686463012077631\\n      ],\\n      \\\"threshold\\\": 0.1,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.43690358432159904,\\n      \\\"RE_P\\\": 0.3902232064883426,\\n      \\\"RE_R\\\": 0.5647035436732979\\n    },\\n    \\\"construction_uniform_t0.2\\\": {\\n      \\\"F1\\\": 0.6637070316293044,\\n      \\\"P\\\": 0.6352976838326555,\\n      \\\"R\\\": 0.7410311805396871,\\n      \\\"F1_ci\\\": [\\n        0.6637070316293044,\\n        0.6387957431574689,\\n        0.6860671791729281\\n      ],\\n      \\\"threshold\\\": 0.2,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.48481421805396013,\\n      \\\"RE_P\\\": 0.4683931537901292,\\n      \\\"RE_R\\\": 0.541558577947992\\n    },\\n    \\\"construction_uniform_t0.3\\\": {\\n      \\\"F1\\\": 0.6615770786042108,\\n      \\\"P\\\": 0.6462090524472376,\\n      \\\"R\\\": 0.7204082621851997,\\n      \\\"F1_ci\\\": [\\n        0.6615770786042108,\\n        0.6361103202368631,\\n        0.6844515600909462\\n      ],\\n      \\\"threshold\\\": 0.3,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.4899703009594036,\\n      \\\"RE_P\\\": 0.4872767644034185,\\n      \\\"RE_R\\\": 0.5226864922517096\\n    },\\n    \\\"construction_uniform_t0.4\\\": {\\n      \\\"F1\\\": 0.6576532725092716,\\n      \\\"P\\\": 0.6759999399885979,\\n      \\\"R\\\": 0.6757057687114398,\\n      \\\"F1_ci\\\": [\\n        0.6576532725092716,\\n        0.6314842705757862,\\n        0.6823670047288417\\n      ],\\n      \\\"threshold\\\": 0.4,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.49630200748014597,\\n      \\\"RE_P\\\": 0.5132024402818354,\\n      \\\"RE_R\\\": 0.5031662834120301\\n    },\\n    \\\"construction_uniform_t0.5\\\": {\\n      \\\"F1\\\": 0.6528146920529592,\\n      \\\"P\\\": 0.6846828397395505,\\n      \\\"R\\\": 0.65596726839638,\\n      \\\"F1_ci\\\": [\\n        0.6528146920529592,\\n        0.6258234468108229,\\n        0.6779823428905756\\n      ],\\n      \\\"threshold\\\": 0.5,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.4926901603900381,\\n      \\\"RE_P\\\": 0.5230795669358995,\\n      \\\"RE_R\\\": 0.4877283502047207\\n    },\\n    \\\"construction_uniform_t0.6\\\": {\\n      \\\"F1\\\": 0.6153159116902848,\\n      \\\"P\\\": 0.6862243826327001,\\n      \\\"R\\\": 0.5922599139990444,\\n      \\\"F1_ci\\\": [\\n        0.6153159116902848,\\n        0.5876963670013234,\\n        0.6422491495536612\\n      ],\\n      \\\"threshold\\\": 0.6,\\n      \\\"variant\\\": \\\"uniform\\\",\\n      \\\"RE_F1\\\": 0.4767985850466669,\\n      \\\"RE_P\\\": 0.5291512205500863,\\n      \\\"RE_R\\\": 0.4581442292217339\\n    },\\n    \\\"construction_uniform_t0.7\\\": {\\n      \\\"F1\\\": 0.5822513688347933,\\n      \\\"P\\\": 0.687550634620578,\\n      \\\"R\\\": 0.541872840455071,\\n      \\\"F1_ci\\\": [\\n        0.5822513688347933,\\n        0.5530255078608477,\\n        0.61\\n\\n... [截断: 输出过长，省略 13621 字符] ...\\n\\n2697953\\n      ],\\n      \\\"threshold\\\": 0.5,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"P\\\": 0.7342621290919181,\\n      \\\"R\\\": 0.6448465220021863,\\n      \\\"F1_ci\\\": [\\n        0.6712108628975318,\\n        0.6595751434559981,\\n        0.682044076470082\\n      ],\\n      \\\"threshold\\\": 0.6,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.7\\\": {\\n      \\\"F1\\\": 0.591199095415274,\\n      \\\"P\\\": 0.6864205586798093,\\n      \\\"R\\\": 0.5497497788081852,\\n      \\\"F1_ci\\\": [\\n        0.591199095415274,\\n        0.579234940607012,\\n        0.6029485038882076\\n      ],\\n      \\\"threshold\\\": 0.7,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"P\\\": 0.6437124725679081,\\n      \\\"R\\\": 0.4869106164546503,\\n      \\\"F1_ci\\\": [\\n        0.5339617561124026,\\n        0.5215417782974746,\\n        0.5460491685629593\\n      ],\\n      \\\"threshold\\\": 0.8,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_uniform_t0.9\\\": {\\n      \\\"F1\\\": 0.34048116114025495,\\n      \\\"P\\\": 0.46301051026401524,\\n      \\\"R\\\": 0.2913081487540279,\\n      \\\"F1_ci\\\": [\\n        0.34048116114025495,\\n        0.32917991358764737,\\n        0.3516075064993751\\n      ],\\n      \\\"threshold\\\": 0.9,\\n      \\\"variant\\\": \\\"uniform\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.1\\\": {\\n      \\\"F1\\\": 0.7328569407749095,\\n      \\\"P\\\": 0.6589371324647737,\\n      \\\"R\\\": 0.8821899039113171,\\n      \\\"F1_ci\\\": [\\n        0.7328569407749095,\\n        0.7249552558205652,\\n        0.7403962650245636\\n      ],\\n      \\\"threshold\\\": 0.1,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.2\\\": {\\n      \\\"F1\\\": 0.7621279480308844,\\n      \\\"P\\\": 0.7339500482793615,\\n      \\\"R\\\": 0.8206917043039286,\\n      \\\"F1_ci\\\": [\\n        0.7621279480308844,\\n        0.7529999283446229,\\n        0.771106466187632\\n      ],\\n      \\\"threshold\\\": 0.2,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.3\\\": {\\n      \\\"F1\\\": 0.7613280913427132,\\n      \\\"P\\\": 0.7489693319776569,\\n      \\\"R\\\": 0.7972872742541721,\\n      \\\"F1_ci\\\": [\\n        0.7613280913427132,\\n        0.7517992142017296,\\n        0.7704520966862431\\n      ],\\n      \\\"threshold\\\": 0.3,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.4\\\": {\\n      \\\"F1\\\": 0.7403014922869728,\\n      \\\"P\\\": 0.7563222548400211,\\n      \\\"R\\\": 0.7450454192859323,\\n      \\\"F1_ci\\\": [\\n        0.7403014922869728,\\n        0.7300516285129836,\\n        0.750152931985901\\n      ],\\n      \\\"threshold\\\": 0.4,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.5\\\": {\\n      \\\"F1\\\": 0.7183834375032269,\\n      \\\"P\\\": 0.7510840095227834,\\n      \\\"R\\\": 0.7097263353928221,\\n      \\\"F1_ci\\\": [\\n        0.7183834375032269,\\n        0.7073732442492698,\\n        0.7289286995601849\\n      ],\\n      \\\"threshold\\\": 0.5,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"P\\\": 0.7342621290919181,\\n      \\\"R\\\": 0.6448465220021863,\\n      \\\"F1_ci\\\": [\\n        0.6712108628975318,\\n        0.6595751434559981,\\n        0.682044076470082\\n      ],\\n      \\\"threshold\\\": 0.6,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.7\\\": {\\n      \\\"F1\\\": 0.6181885284709259,\\n      \\\"P\\\": 0.7094420862979814,\\n      \\\"R\\\": 0.5781943296096657,\\n      \\\"F1_ci\\\": [\\n        0.6181885284709259,\\n        0.6065476945549937,\\n        0.6296751796722696\\n      ],\\n      \\\"threshold\\\": 0.7,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"P\\\": 0.6437124725679081,\\n      \\\"R\\\": 0.4869106164546503,\\n      \\\"F1_ci\\\": [\\n        0.5339617561124026,\\n        0.5215417782974746,\\n        0.5460491685629593\\n      ],\\n      \\\"threshold\\\": 0.8,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    },\\n    \\\"construction_lp_weighted_t0.9\\\": {\\n      \\\"F1\\\": 0.34303959507078724,\\n      \\\"P\\\": 0.46645799360117907,\\n      \\\"R\\\": 0.2935107075527715,\\n      \\\"F1_ci\\\": [\\n        0.34303959507078724,\\n        0.33173607672333816,\\n        0.3542600354286932\\n      ],\\n      \\\"threshold\\\": 0.9,\\n      \\\"variant\\\": \\\"lp_weighted\\\"\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UGBYqVdNvvx8pR3B8VdG5f`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair/fair_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "e70f189f-49bc-40bb-9543-63f3f311da37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xj7PdP9XfXxjBs2atdpF9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6467,
      "cache_read_input_tokens": 64511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6467
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

_source line 96 · 2026-05-19T08:04:20.143Z_

<details><summary>↩ Tool result · `toolu_01UGBYqVdNvvx8pR3B8VdG5f`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"greedy\\\": {\\n      \\\"F1\\\": 0.6441821796820129,\\n      \\\"std\\\": 0.3050883196377791\\n    },\\n    \\\"lp_selection\\\": {\\n      \\\"F1\\\": 0.6465303389349577,\\n      \\\"std\\\": 0.30071210692461203\\n    },\\n    \\\"sj_selection\\\": {\\n      \\\"F1\\\": 0.5852966275038706,\\n      \\\"std\\\": 0.3406276188220908\\n    },\\n    \\\"oracle\\\": {\\n      \\\"F1\\\": 0.8193707573669766,\\n      \\\"std\\\": 0.23333648613492924\\n    },\\n    \\\"random\\\": {\\n      \\\"F1\\\": 0.6098954691549506,\\n      \\\"std\\\": 0.26151799667465325\\n    },\\n    \\\"construction_uniform_majority\\\": {\\n      \\\"F1\\\": 0.6528146920529592,\\n      \\\"std\\\": 0.30194273280927686,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"construction_uniform_confirm\\\": {\\n      \\\"F1\\\": 0.6469695336362352,\\n      \\\"std\\\": 0.2600518644002841,\\n      \\\"theta\\\": 0.125\\n    },\\n    \\\"construction_uniform_cv\\\": {\\n      \\\"F1\\\": 0.6576789618722392,\\n      \\\"std\\\": 0.014821897598001978,\\n      \\\"fold_f1s\\\": [\\n        0.6598717151020148,\\n        0.6538839397746167,\\n        0.6616350568903289,\\n        0.6334715044481971,\\n        0.6795325931460386\\n      ],\\n      \\\"fold_thetas\\\": [\\n        0.35,\\n        0.2,\\n        0.2,\\n        0.2,\\n        0.35\\n      ]\\n    },\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008632512370946359,\\n      \\\"ci_95\\\": [\\n        -0.003791963965516347,\\n        0.020730607954267292\\n      ],\\n      \\\"p_value\\\": 0.0844,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.002787353954222393,\\n      \\\"ci_95\\\": [\\n        -0.014480068531011032,\\n        0.020922071081157054\\n      ],\\n      \\\"p_value\\\": 0.3801,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01345547097798849,\\n      \\\"ci_95\\\": [\\n        0.0009839962198741237,\\n        0.02630432351819819\\n      ],\\n      \\\"p_value\\\": 0.0178,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0023481592529448476,\\n      \\\"ci_95\\\": [\\n        -0.010436567965856096,\\n        0.015129877508434367\\n      ],\\n      \\\"p_value\\\": 0.3519,\\n      \\\"significant\\\": false\\n    },\\n    \\\"construction_lp_weighted_majority\\\": {\\n      \\\"F1\\\": 0.6439082026171693,\\n      \\\"std\\\": 0.3069043108236961,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"construction_lp_weighted_confirm\\\": {\\n      \\\"F1\\\": 0.6525456892277284,\\n      \\\"std\\\": 0.26492647762736143,\\n      \\\"theta\\\": 0.125\\n    },\\n    \\\"construction_lp_weighted_cv\\\": {\\n      \\\"F1\\\": 0.6574455724351872,\\n      \\\"std\\\": 0.015061023033978613,\\n      \\\"fold_f1s\\\": [\\n        0.661362749348321,\\n        0.6512259583430504,\\n        0.6616350568903289,\\n        0.6334715044481971,\\n        0.6795325931460386\\n      ],\\n      \\\"fold_thetas\\\": [\\n        0.25,\\n        0.25,\\n        0.2,\\n        0.2,\\n        0.35\\n      ]\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.0002739770648436429,\\n      \\\"ci_95\\\": [\\n        -0.012955645550847519,\\n        0.011613805127758964\\n      ],\\n      \\\"p_value\\\": 0.5123,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008363509545715585,\\n      \\\"ci_95\\\": [\\n        -0.007401747073516637,\\n        0.02510800810259234\\n      ],\\n      \\\"p_value\\\": 0.1555,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.013221640351074353,\\n      \\\"ci_95\\\": [\\n        0.0009737906171938178,\\n        0.0258295341900646\\n      ],\\n      \\\"p_value\\\": 0.0176,\\n      \\\"significant\\\": true\\n    },\\n    \\\"adaptive_uniform\\\": {\\n      \\\"F1\\\": 0.6847878341277908,\\n      \\\"std\\\": 0.02189925605023344,\\n      \\\"fold_f1s\\\": [\\n        0.6958404117840801,\\n        0.6755965855577399,\\n        0.679735018650113,\\n        0.6535154710676061,\\n        0.7192516835794147\\n      ],\\n      \\\"fold_params\\\": [\\n        {\\n          \\\"gate_threshold\\\": 0.2,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.2,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.2,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n\\n\\n... [截断: 输出过长，省略 15686 字符] ...\\n\\n      ],\\n      \\\"p_value\\\": 0.0662,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.014245721350301178,\\n      \\\"ci_95\\\": [\\n        0.008743637236230993,\\n        0.01991429890808697\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"adaptive_uniform\\\": {\\n      \\\"F1\\\": 0.803309687348112,\\n      \\\"std\\\": 0.008590420839837815,\\n      \\\"fold_f1s\\\": [\\n        0.7929812312724132,\\n        0.8104361364207069,\\n        0.8052695115263174,\\n        0.7937597181019834,\\n        0.8141018394191398\\n      ],\\n      \\\"fold_params\\\": [\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        }\\n      ]\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0555410065159577,\\n      \\\"ci_95\\\": [\\n        0.04925720708508786,\\n        0.06177817005800181\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"lp_alignment_gating\\\": {\\n      \\\"dataset\\\": \\\"fewnerd\\\",\\n      \\\"mean_alignment\\\": 0.46774044270699244,\\n      \\\"median_alignment\\\": 0.592999453328881,\\n      \\\"frac_positive\\\": 0.8055619397839577,\\n      \\\"recommendation\\\": \\\"LP selection\\\"\\n    },\\n    \\\"sweep_uniform_t0.1\\\": {\\n      \\\"F1\\\": 0.7328569407749095,\\n      \\\"theta\\\": 0.1\\n    },\\n    \\\"sweep_uniform_t0.15\\\": {\\n      \\\"F1\\\": 0.7577056787114553,\\n      \\\"theta\\\": 0.15\\n    },\\n    \\\"sweep_uniform_t0.2\\\": {\\n      \\\"F1\\\": 0.7621443646182042,\\n      \\\"theta\\\": 0.2\\n    },\\n    \\\"sweep_uniform_t0.25\\\": {\\n      \\\"F1\\\": 0.7621443646182042,\\n      \\\"theta\\\": 0.25\\n    },\\n    \\\"sweep_uniform_t0.3\\\": {\\n      \\\"F1\\\": 0.7613025544291045,\\n      \\\"theta\\\": 0.3\\n    },\\n    \\\"sweep_uniform_t0.35\\\": {\\n      \\\"F1\\\": 0.7517259297711838,\\n      \\\"theta\\\": 0.35\\n    },\\n    \\\"sweep_uniform_t0.4\\\": {\\n      \\\"F1\\\": 0.7403014922869728,\\n      \\\"theta\\\": 0.4\\n    },\\n    \\\"sweep_uniform_t0.45\\\": {\\n      \\\"F1\\\": 0.7188912739876688,\\n      \\\"theta\\\": 0.45\\n    },\\n    \\\"sweep_uniform_t0.5\\\": {\\n      \\\"F1\\\": 0.7188912739876688,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"sweep_uniform_t0.55\\\": {\\n      \\\"F1\\\": 0.6990773679868102,\\n      \\\"theta\\\": 0.55\\n    },\\n    \\\"sweep_uniform_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"theta\\\": 0.6\\n    },\\n    \\\"sweep_uniform_t0.7\\\": {\\n      \\\"F1\\\": 0.591199095415274,\\n      \\\"theta\\\": 0.7\\n    },\\n    \\\"sweep_uniform_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"theta\\\": 0.8\\n    },\\n    \\\"sweep_uniform_t0.9\\\": {\\n      \\\"F1\\\": 0.34048116114025495,\\n      \\\"theta\\\": 0.9\\n    },\\n    \\\"sweep_lp_weighted_t0.1\\\": {\\n      \\\"F1\\\": 0.7328569407749095,\\n      \\\"theta\\\": 0.1\\n    },\\n    \\\"sweep_lp_weighted_t0.15\\\": {\\n      \\\"F1\\\": 0.7577056787114553,\\n      \\\"theta\\\": 0.15\\n    },\\n    \\\"sweep_lp_weighted_t0.2\\\": {\\n      \\\"F1\\\": 0.7621279480308844,\\n      \\\"theta\\\": 0.2\\n    },\\n    \\\"sweep_lp_weighted_t0.25\\\": {\\n      \\\"F1\\\": 0.7630133126515145,\\n      \\\"theta\\\": 0.25\\n    },\\n    \\\"sweep_lp_weighted_t0.3\\\": {\\n      \\\"F1\\\": 0.7613280913427132,\\n      \\\"theta\\\": 0.3\\n    },\\n    \\\"sweep_lp_weighted_t0.35\\\": {\\n      \\\"F1\\\": 0.7517259297711838,\\n      \\\"theta\\\": 0.35\\n    },\\n    \\\"sweep_lp_weighted_t0.4\\\": {\\n      \\\"F1\\\": 0.7403014922869728,\\n      \\\"theta\\\": 0.4\\n    },\\n    \\\"sweep_lp_weighted_t0.45\\\": {\\n      \\\"F1\\\": 0.7256764770204788,\\n      \\\"theta\\\": 0.45\\n    },\\n    \\\"sweep_lp_weighted_t0.5\\\": {\\n      \\\"F1\\\": 0.7183834375032269,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"sweep_lp_weighted_t0.55\\\": {\\n      \\\"F1\\\": 0.6990773679868102,\\n      \\\"theta\\\": 0.55\\n    },\\n    \\\"sweep_lp_weighted_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"theta\\\": 0.6\\n    },\\n    \\\"sweep_lp_weighted_t0.7\\\": {\\n      \\\"F1\\\": 0.6181885284709259,\\n      \\\"theta\\\": 0.7\\n    },\\n    \\\"sweep_lp_weighted_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"theta\\\": 0.8\\n    },\\n    \\\"sweep_lp_weighted_t0.9\\\": {\\n      \\\"F1\\\": 0.34303959507078724,\\n      \\\"theta\\\": 0.9\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c277eae6-cfed-4e15-915f-c1af97546fac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"greedy\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6441821796820129,\\\\n      \\\\\\\"std\\\\\\\": 0.3050883196377791\\\\n    },\\\\n    \\\\\\\"lp_selection\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6465303389349577,\\\\n      \\\\\\\"std\\\\\\\": 0.30071210692461203\\\\n    },\\\\n    \\\\\\\"sj_selection\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5852966275038706,\\\\n      \\\\\\\"std\\\\\\\": 0.3406276188220908\\\\n    },\\\\n    \\\\\\\"oracle\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.8193707573669766,\\\\n      \\\\\\\"std\\\\\\\": 0.23333648613492924\\\\n    },\\\\n    \\\\\\\"random\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6098954691549506,\\\\n      \\\\\\\"std\\\\\\\": 0.26151799667465325\\\\n    },\\\\n    \\\\\\\"construction_uniform_majority\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6528146920529592,\\\\n      \\\\\\\"std\\\\\\\": 0.30194273280927686,\\\\n      \\\\\\\"theta\\\\\\\": 0.5\\\\n    },\\\\n    \\\\\\\"construction_uniform_confirm\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6469695336362352,\\\\n      \\\\\\\"std\\\\\\\": 0.2600518644002841,\\\\n      \\\\\\\"theta\\\\\\\": 0.125\\\\n    },\\\\n    \\\\\\\"construction_uniform_cv\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6576789618722392,\\\\n      \\\\\\\"std\\\\\\\": 0.014821897598001978,\\\\n      \\\\\\\"fold_f1s\\\\\\\": [\\\\n        0.6598717151020148,\\\\n        0.6538839397746167,\\\\n        0.6616350568903289,\\\\n        0.6334715044481971,\\\\n        0.6795325931460386\\\\n      ],\\\\n      \\\\\\\"fold_thetas\\\\\\\": [\\\\n        0.35,\\\\n        0.2,\\\\n        0.2,\\\\n        0.2,\\\\n        0.35\\\\n      ]\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.008632512370946359,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.003791963965516347,\\\\n        0.020730607954267292\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0844,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.002787353954222393,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.014480068531011032,\\\\n        0.020922071081157054\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.3801,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.01345547097798849,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.0009839962198741237,\\\\n        0.02630432351819819\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0178,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"bootstrap_lp_selection_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.0023481592529448476,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.010436567965856096,\\\\n        0.015129877508434367\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.3519,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_majority\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6439082026171693,\\\\n      \\\\\\\"std\\\\\\\": 0.3069043108236961,\\\\n      \\\\\\\"theta\\\\\\\": 0.5\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_confirm\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6525456892277284,\\\\n      \\\\\\\"std\\\\\\\": 0.26492647762736143,\\\\n      \\\\\\\"theta\\\\\\\": 0.125\\\\n    },\\\\n    \\\\\\\"construction_lp_weighted_cv\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6574455724351872,\\\\n      \\\\\\\"std\\\\\\\": 0.015061023033978613,\\\\n      \\\\\\\"fold_f1s\\\\\\\": [\\\\n        0.661362749348321,\\\\n        0.6512259583430504,\\\\n        0.6616350568903289,\\\\n        0.6334715044481971,\\\\n        0.6795325931460386\\\\n      ],\\\\n      \\\\\\\"fold_thetas\\\\\\\": [\\\\n        0.25,\\\\n        0.25,\\\\n        0.2,\\\\n        0.2,\\\\n        0.35\\\\n      ]\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0002739770648436429,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.012955645550847519,\\\\n        0.011613805127758964\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.5123,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.008363509545715585,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.007401747073516637,\\\\n        0.02510800810259234\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.1555,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.013221640351074353,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.0009737906171938178,\\\\n        0.0258295341900646\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0176,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"adaptive_uniform\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6847878341277908,\\\\n      \\\\\\\"std\\\\\\\": 0.02189925605023344,\\\\n      \\\\\\\"fold_f1s\\\\\\\": [\\\\n        0.6958404117840801,\\\\n        0.6755965855577399,\\\\n        0.679735018650113,\\\\n        0.6535154710676061,\\\\n        0.7192516835794147\\\\n      ],\\\\n      \\\\\\\"fold_params\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.2,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.2,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.2,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n\\\\n\\\\n... [截断: 输出过长，省略 15686 字符] ...\\\\n\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0662,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.014245721350301178,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.008743637236230993,\\\\n        0.01991429890808697\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"adaptive_uniform\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.803309687348112,\\\\n      \\\\\\\"std\\\\\\\": 0.008590420839837815,\\\\n      \\\\\\\"fold_f1s\\\\\\\": [\\\\n        0.7929812312724132,\\\\n        0.8104361364207069,\\\\n        0.8052695115263174,\\\\n        0.7937597181019834,\\\\n        0.8141018394191398\\\\n      ],\\\\n      \\\\\\\"fold_params\\\\\\\": [\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.3,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.3,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.3,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.3,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        },\\\\n        {\\\\n          \\\\\\\"gate_threshold\\\\\\\": 0.3,\\\\n          \\\\\\\"construction_theta\\\\\\\": 0.1\\\\n        }\\\\n      ]\\\\n    },\\\\n    \\\\\\\"bootstrap_adaptive_uniform_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.0555410065159577,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.04925720708508786,\\\\n        0.06177817005800181\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"lp_alignment_gating\\\\\\\": {\\\\n      \\\\\\\"dataset\\\\\\\": \\\\\\\"fewnerd\\\\\\\",\\\\n      \\\\\\\"mean_alignment\\\\\\\": 0.46774044270699244,\\\\n      \\\\\\\"median_alignment\\\\\\\": 0.592999453328881,\\\\n      \\\\\\\"frac_positive\\\\\\\": 0.8055619397839577,\\\\n      \\\\\\\"recommendation\\\\\\\": \\\\\\\"LP selection\\\\\\\"\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.1\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7328569407749095,\\\\n      \\\\\\\"theta\\\\\\\": 0.1\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.15\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7577056787114553,\\\\n      \\\\\\\"theta\\\\\\\": 0.15\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.2\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7621443646182042,\\\\n      \\\\\\\"theta\\\\\\\": 0.2\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.25\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7621443646182042,\\\\n      \\\\\\\"theta\\\\\\\": 0.25\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.3\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7613025544291045,\\\\n      \\\\\\\"theta\\\\\\\": 0.3\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.35\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7517259297711838,\\\\n      \\\\\\\"theta\\\\\\\": 0.35\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.4\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7403014922869728,\\\\n      \\\\\\\"theta\\\\\\\": 0.4\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.45\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7188912739876688,\\\\n      \\\\\\\"theta\\\\\\\": 0.45\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.5\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7188912739876688,\\\\n      \\\\\\\"theta\\\\\\\": 0.5\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.55\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6990773679868102,\\\\n      \\\\\\\"theta\\\\\\\": 0.55\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.6\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6712108628975318,\\\\n      \\\\\\\"theta\\\\\\\": 0.6\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.7\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.591199095415274,\\\\n      \\\\\\\"theta\\\\\\\": 0.7\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.8\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5339617561124026,\\\\n      \\\\\\\"theta\\\\\\\": 0.8\\\\n    },\\\\n    \\\\\\\"sweep_uniform_t0.9\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.34048116114025495,\\\\n      \\\\\\\"theta\\\\\\\": 0.9\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.1\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7328569407749095,\\\\n      \\\\\\\"theta\\\\\\\": 0.1\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.15\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7577056787114553,\\\\n      \\\\\\\"theta\\\\\\\": 0.15\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.2\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7621279480308844,\\\\n      \\\\\\\"theta\\\\\\\": 0.2\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.25\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7630133126515145,\\\\n      \\\\\\\"theta\\\\\\\": 0.25\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.3\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7613280913427132,\\\\n      \\\\\\\"theta\\\\\\\": 0.3\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.35\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7517259297711838,\\\\n      \\\\\\\"theta\\\\\\\": 0.35\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.4\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7403014922869728,\\\\n      \\\\\\\"theta\\\\\\\": 0.4\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.45\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7256764770204788,\\\\n      \\\\\\\"theta\\\\\\\": 0.45\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.5\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.7183834375032269,\\\\n      \\\\\\\"theta\\\\\\\": 0.5\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.55\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6990773679868102,\\\\n      \\\\\\\"theta\\\\\\\": 0.55\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.6\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6712108628975318,\\\\n      \\\\\\\"theta\\\\\\\": 0.6\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.7\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6181885284709259,\\\\n      \\\\\\\"theta\\\\\\\": 0.7\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.8\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.5339617561124026,\\\\n      \\\\\\\"theta\\\\\\\": 0.8\\\\n    },\\\\n    \\\\\\\"sweep_lp_weighted_t0.9\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.34303959507078724,\\\\n      \\\\\\\"theta\\\\\\\": 0.9\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"greedy\\\": {\\n      \\\"F1\\\": 0.6441821796820129,\\n      \\\"std\\\": 0.3050883196377791\\n    },\\n    \\\"lp_selection\\\": {\\n      \\\"F1\\\": 0.6465303389349577,\\n      \\\"std\\\": 0.30071210692461203\\n    },\\n    \\\"sj_selection\\\": {\\n      \\\"F1\\\": 0.5852966275038706,\\n      \\\"std\\\": 0.3406276188220908\\n    },\\n    \\\"oracle\\\": {\\n      \\\"F1\\\": 0.8193707573669766,\\n      \\\"std\\\": 0.23333648613492924\\n    },\\n    \\\"random\\\": {\\n      \\\"F1\\\": 0.6098954691549506,\\n      \\\"std\\\": 0.26151799667465325\\n    },\\n    \\\"construction_uniform_majority\\\": {\\n      \\\"F1\\\": 0.6528146920529592,\\n      \\\"std\\\": 0.30194273280927686,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"construction_uniform_confirm\\\": {\\n      \\\"F1\\\": 0.6469695336362352,\\n      \\\"std\\\": 0.2600518644002841,\\n      \\\"theta\\\": 0.125\\n    },\\n    \\\"construction_uniform_cv\\\": {\\n      \\\"F1\\\": 0.6576789618722392,\\n      \\\"std\\\": 0.014821897598001978,\\n      \\\"fold_f1s\\\": [\\n        0.6598717151020148,\\n        0.6538839397746167,\\n        0.6616350568903289,\\n        0.6334715044481971,\\n        0.6795325931460386\\n      ],\\n      \\\"fold_thetas\\\": [\\n        0.35,\\n        0.2,\\n        0.2,\\n        0.2,\\n        0.35\\n      ]\\n    },\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008632512370946359,\\n      \\\"ci_95\\\": [\\n        -0.003791963965516347,\\n        0.020730607954267292\\n      ],\\n      \\\"p_value\\\": 0.0844,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.002787353954222393,\\n      \\\"ci_95\\\": [\\n        -0.014480068531011032,\\n        0.020922071081157054\\n      ],\\n      \\\"p_value\\\": 0.3801,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01345547097798849,\\n      \\\"ci_95\\\": [\\n        0.0009839962198741237,\\n        0.02630432351819819\\n      ],\\n      \\\"p_value\\\": 0.0178,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0023481592529448476,\\n      \\\"ci_95\\\": [\\n        -0.010436567965856096,\\n        0.015129877508434367\\n      ],\\n      \\\"p_value\\\": 0.3519,\\n      \\\"significant\\\": false\\n    },\\n    \\\"construction_lp_weighted_majority\\\": {\\n      \\\"F1\\\": 0.6439082026171693,\\n      \\\"std\\\": 0.3069043108236961,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"construction_lp_weighted_confirm\\\": {\\n      \\\"F1\\\": 0.6525456892277284,\\n      \\\"std\\\": 0.26492647762736143,\\n      \\\"theta\\\": 0.125\\n    },\\n    \\\"construction_lp_weighted_cv\\\": {\\n      \\\"F1\\\": 0.6574455724351872,\\n      \\\"std\\\": 0.015061023033978613,\\n      \\\"fold_f1s\\\": [\\n        0.661362749348321,\\n        0.6512259583430504,\\n        0.6616350568903289,\\n        0.6334715044481971,\\n        0.6795325931460386\\n      ],\\n      \\\"fold_thetas\\\": [\\n        0.25,\\n        0.25,\\n        0.2,\\n        0.2,\\n        0.35\\n      ]\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.0002739770648436429,\\n      \\\"ci_95\\\": [\\n        -0.012955645550847519,\\n        0.011613805127758964\\n      ],\\n      \\\"p_value\\\": 0.5123,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008363509545715585,\\n      \\\"ci_95\\\": [\\n        -0.007401747073516637,\\n        0.02510800810259234\\n      ],\\n      \\\"p_value\\\": 0.1555,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.013221640351074353,\\n      \\\"ci_95\\\": [\\n        0.0009737906171938178,\\n        0.0258295341900646\\n      ],\\n      \\\"p_value\\\": 0.0176,\\n      \\\"significant\\\": true\\n    },\\n    \\\"adaptive_uniform\\\": {\\n      \\\"F1\\\": 0.6847878341277908,\\n      \\\"std\\\": 0.02189925605023344,\\n      \\\"fold_f1s\\\": [\\n        0.6958404117840801,\\n        0.6755965855577399,\\n        0.679735018650113,\\n        0.6535154710676061,\\n        0.7192516835794147\\n      ],\\n      \\\"fold_params\\\": [\\n        {\\n          \\\"gate_threshold\\\": 0.2,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.2,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.2,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n\\n\\n... [截断: 输出过长，省略 15686 字符] ...\\n\\n      ],\\n      \\\"p_value\\\": 0.0662,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.014245721350301178,\\n      \\\"ci_95\\\": [\\n        0.008743637236230993,\\n        0.01991429890808697\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"adaptive_uniform\\\": {\\n      \\\"F1\\\": 0.803309687348112,\\n      \\\"std\\\": 0.008590420839837815,\\n      \\\"fold_f1s\\\": [\\n        0.7929812312724132,\\n        0.8104361364207069,\\n        0.8052695115263174,\\n        0.7937597181019834,\\n        0.8141018394191398\\n      ],\\n      \\\"fold_params\\\": [\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        },\\n        {\\n          \\\"gate_threshold\\\": 0.3,\\n          \\\"construction_theta\\\": 0.1\\n        }\\n      ]\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0555410065159577,\\n      \\\"ci_95\\\": [\\n        0.04925720708508786,\\n        0.06177817005800181\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"lp_alignment_gating\\\": {\\n      \\\"dataset\\\": \\\"fewnerd\\\",\\n      \\\"mean_alignment\\\": 0.46774044270699244,\\n      \\\"median_alignment\\\": 0.592999453328881,\\n      \\\"frac_positive\\\": 0.8055619397839577,\\n      \\\"recommendation\\\": \\\"LP selection\\\"\\n    },\\n    \\\"sweep_uniform_t0.1\\\": {\\n      \\\"F1\\\": 0.7328569407749095,\\n      \\\"theta\\\": 0.1\\n    },\\n    \\\"sweep_uniform_t0.15\\\": {\\n      \\\"F1\\\": 0.7577056787114553,\\n      \\\"theta\\\": 0.15\\n    },\\n    \\\"sweep_uniform_t0.2\\\": {\\n      \\\"F1\\\": 0.7621443646182042,\\n      \\\"theta\\\": 0.2\\n    },\\n    \\\"sweep_uniform_t0.25\\\": {\\n      \\\"F1\\\": 0.7621443646182042,\\n      \\\"theta\\\": 0.25\\n    },\\n    \\\"sweep_uniform_t0.3\\\": {\\n      \\\"F1\\\": 0.7613025544291045,\\n      \\\"theta\\\": 0.3\\n    },\\n    \\\"sweep_uniform_t0.35\\\": {\\n      \\\"F1\\\": 0.7517259297711838,\\n      \\\"theta\\\": 0.35\\n    },\\n    \\\"sweep_uniform_t0.4\\\": {\\n      \\\"F1\\\": 0.7403014922869728,\\n      \\\"theta\\\": 0.4\\n    },\\n    \\\"sweep_uniform_t0.45\\\": {\\n      \\\"F1\\\": 0.7188912739876688,\\n      \\\"theta\\\": 0.45\\n    },\\n    \\\"sweep_uniform_t0.5\\\": {\\n      \\\"F1\\\": 0.7188912739876688,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"sweep_uniform_t0.55\\\": {\\n      \\\"F1\\\": 0.6990773679868102,\\n      \\\"theta\\\": 0.55\\n    },\\n    \\\"sweep_uniform_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"theta\\\": 0.6\\n    },\\n    \\\"sweep_uniform_t0.7\\\": {\\n      \\\"F1\\\": 0.591199095415274,\\n      \\\"theta\\\": 0.7\\n    },\\n    \\\"sweep_uniform_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"theta\\\": 0.8\\n    },\\n    \\\"sweep_uniform_t0.9\\\": {\\n      \\\"F1\\\": 0.34048116114025495,\\n      \\\"theta\\\": 0.9\\n    },\\n    \\\"sweep_lp_weighted_t0.1\\\": {\\n      \\\"F1\\\": 0.7328569407749095,\\n      \\\"theta\\\": 0.1\\n    },\\n    \\\"sweep_lp_weighted_t0.15\\\": {\\n      \\\"F1\\\": 0.7577056787114553,\\n      \\\"theta\\\": 0.15\\n    },\\n    \\\"sweep_lp_weighted_t0.2\\\": {\\n      \\\"F1\\\": 0.7621279480308844,\\n      \\\"theta\\\": 0.2\\n    },\\n    \\\"sweep_lp_weighted_t0.25\\\": {\\n      \\\"F1\\\": 0.7630133126515145,\\n      \\\"theta\\\": 0.25\\n    },\\n    \\\"sweep_lp_weighted_t0.3\\\": {\\n      \\\"F1\\\": 0.7613280913427132,\\n      \\\"theta\\\": 0.3\\n    },\\n    \\\"sweep_lp_weighted_t0.35\\\": {\\n      \\\"F1\\\": 0.7517259297711838,\\n      \\\"theta\\\": 0.35\\n    },\\n    \\\"sweep_lp_weighted_t0.4\\\": {\\n      \\\"F1\\\": 0.7403014922869728,\\n      \\\"theta\\\": 0.4\\n    },\\n    \\\"sweep_lp_weighted_t0.45\\\": {\\n      \\\"F1\\\": 0.7256764770204788,\\n      \\\"theta\\\": 0.45\\n    },\\n    \\\"sweep_lp_weighted_t0.5\\\": {\\n      \\\"F1\\\": 0.7183834375032269,\\n      \\\"theta\\\": 0.5\\n    },\\n    \\\"sweep_lp_weighted_t0.55\\\": {\\n      \\\"F1\\\": 0.6990773679868102,\\n      \\\"theta\\\": 0.55\\n    },\\n    \\\"sweep_lp_weighted_t0.6\\\": {\\n      \\\"F1\\\": 0.6712108628975318,\\n      \\\"theta\\\": 0.6\\n    },\\n    \\\"sweep_lp_weighted_t0.7\\\": {\\n      \\\"F1\\\": 0.6181885284709259,\\n      \\\"theta\\\": 0.7\\n    },\\n    \\\"sweep_lp_weighted_t0.8\\\": {\\n      \\\"F1\\\": 0.5339617561124026,\\n      \\\"theta\\\": 0.8\\n    },\\n    \\\"sweep_lp_weighted_t0.9\\\": {\\n      \\\"F1\\\": 0.34303959507078724,\\n      \\\"theta\\\": 0.9\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 97_

<details><summary>Logged reasoning block</summary>

```text
The entity_construction results I've seen are for N=8 (8 samples). The FewNERD entity construction shows:
- greedy F1: 0.7477
- construction_lp_weighted at different thresholds

But I need N=16 entity construction for FewNERD. The files I found (`entity_construction` and `entity_construction_fair`) are N=8 data (the FewNERD data appears to be from exp_021 which is N=8).

Actually wait, looking more carefully at the truncated output, I can see there are fewnerd results in these files. 

Looking at the `fair_results.json` file, I can see it contains FewNERD data with a greedy F1 of 0.7478 for N=8, matching exp_021. The construction_lp_weighted_cv shows a bootstrap mean difference of about 1.42 percentage points with p-value of 0.0, but this is still N=8 construction data. I'm trying to figure out where the "+1.32pp" improvement is coming from.

I need to track down whether an N=16 entity construction experiment was actually run on FewNERD. The exp_027_fewnerd_n16 results only show selection metrics, not construction results. Let me check if there's an N=16 version in the entity_construction_fair directory or if this improvement was reported from a different experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "f91c6fb0-a05c-44ea-8ec2-2f851a27e897",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uawzNKfnxXWiufbTQSr3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9744,
      "cache_read_input_tokens": 70978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9744
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

_source line 98_

The entity construction results I've found so far are N=8. Let me search specifically for N=16 entity construction on FewNERD.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "7369f7e5-5fc7-4825-a1be-2d488c3179d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uawzNKfnxXWiufbTQSr3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9744,
      "cache_read_input_tokens": 70978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9744
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

_source line 99_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015vCwXZgWPec1fZK6pJocEc`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*construct*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "21856913-c306-4a01-b277-16daec66ef32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uawzNKfnxXWiufbTQSr3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9744,
      "cache_read_input_tokens": 70978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9744
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

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VwVigpka13TmV6P9c69ZmL`</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*n16*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "bc58beb8-4f78-4373-8d55-ecfb15b47753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uawzNKfnxXWiufbTQSr3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9744,
      "cache_read_input_tokens": 70978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9744
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

_source line 101 · 2026-05-19T08:04:35.357Z_

<details><summary>↩ Tool result · `toolu_015vCwXZgWPec1fZK6pJocEc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_log.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8_log.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c3916a88-be6b-4285-96ad-83278f9d65e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_log.txt\\\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8_log.txt\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_log.txt\\n/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair_n8_log.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-19T08:04:35.775Z_

<details><summary>↩ Tool result · `toolu_01VwVigpka13TmV6P9c69ZmL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16.log\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_5signal_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456.log\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_conll_n16_3seed_5signal_summary.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n16.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_r1024_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_5signal_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/figures/lp_range_cdf_n16_3seed.pdf\\n/root/autodl-tmp/struct_self_consist_ie/output/figures/lp_range_cdf_n16_3seed.png\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf_n16_3seed.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_re_n16_3seed_selection_f1.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1_merged.json\\n/root/autodl-tmp/struct_self_consist_ie/output/task3_llama_n16_check.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "d0863027-d20b-42f8-b4ea-761c3915fa9c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_run.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_run.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_5signal_results.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_conll_n16_3seed_5signal_summary.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n16.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_run.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_r1024_run.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024_run.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_analysis.py\\\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_5signal_results.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/figures/lp_range_cdf_n16_3seed.pdf\\\\n/root/autodl-tmp/struct_self_consist_ie/output/figures/lp_range_cdf_n16_3seed.png\\\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf_n16_3seed.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_re_n16_3seed_selection_f1.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1_merged.json\\\\n/root/autodl-tmp/struct_self_consist_ie/output/task3_llama_n16_check.py\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\\\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp008_re_n16_t10_full.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16.log\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_5signal_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456.log\\n/root/autodl-tmp/struct_self_consist_ie/output/llama_conll_n16_3seed_5signal_summary.json\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/selection_f1_llama_scierc_n16.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed456_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_r1024_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s456_r1024_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_5signal_results.json\\n/root/autodl-tmp/struct_self_consist_ie/output/figures/lp_range_cdf_n16_3seed.pdf\\n/root/autodl-tmp/struct_self_consist_ie/output/figures/lp_range_cdf_n16_3seed.png\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_lp_range_cdf_n16_3seed.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_re_n16_3seed_selection_f1.json\\n/root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1_merged.json\\n/root/autodl-tmp/struct_self_consist_ie/output/task3_llama_n16_check.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
No N=16 entity construction data for FewNERD. The entity_construction results only have N=8 (seed42) results. The exp_027_fewnerd_n16 only has selection metrics.

Now let me check the entity construction data for fewnerd in `entity_construction/construction_results.json` more carefully. The data was truncated. Let me check the fewnerd section specifically.

Also, the +1.32 claim at L213 says "seed-42" and references Appendix app:n_scaling. But the appendix only has SciERC n-scaling data (QE correlation scaling and selection scaling), no entity construction N=16 data for either dataset.


Looking at the fair_results.json, I can see the FewNERD entity construction numbers show a bootstrap mean_diff around 1.42pp for N=8, but there's no corresponding N=16 entity construction experiment—only the selection delta of 1.88pp exists for that configuration.

Now I'm noticing something odd in the paper's claim: it says construction gains "rise to +1.32pp" at N=16, but the table shows +1.40±0.51pp at N=8, which is actually higher. The 1.32 number appears to be the lower confidence bound from the N=8 experiment, not a separate N=16 result, so the scaling claim seems backwards or based on misread data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "42322adf-4c93-454c-8a7d-072e30cadbfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4hpvNEUPi1HEZebh3gUVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 80722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1946
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

_source line 104_

No N=16 entity construction files exist for FewNERD. Let me check the table context around L204 and also look at what ρ values the caption's "0.38" could be referring to.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "cf500003-31e6-4fe7-bc23-97f89ff36e6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4hpvNEUPi1HEZebh3gUVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 80722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1946
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

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_01RdCYuLCXfgMTZ1qchjGYpT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 180,
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
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "befc5fd3-265d-48a4-a62e-002ac77ba50b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4hpvNEUPi1HEZebh3gUVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 80722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1946
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

_source line 106 · 2026-05-19T08:04:56.657Z_

<details><summary>↩ Tool result · `toolu_01RdCYuLCXfgMTZ1qchjGYpT`</summary>

```text
180	Hidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%) but do not improve selection (gap closure $-5.1$\% vs.\ $+4.8$\%; Appendix~\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.
181	
182	%% ============================================================
183	\subsection{Prescriptive Results}
184	\label{sec:prescriptive}
185	
186	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
187	
188	\paragraph{Entity-level construction.}
189	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\theta{=}2/N$ (an entity is included if it appears in ${\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\theta \in [0.15, 0.35]$ (Appendix~\ref{app:theta_sweep}; $\theta{=}0.5$ majority baseline in Appendix~\ref{app:entity_merge}).
190	
191	\begin{table}[t]
192	\centering
193	\small
194	\caption{Entity-level construction vs.\ greedy decoding ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\ greedy; LP-weighted positive across all seeds. Best per dataset in \textbf{bold}.}
195	\label{tab:entity_construction}
196	\resizebox{\columnwidth}{!}{%
197	\begin{tabular}{@{}llcccc@{}}
198	\toprule
199	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
200	\midrule
201	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
202	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
203	\addlinespace
204	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
205	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
206	\addlinespace
207	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
208	\bottomrule
209	\end{tabular}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "3401399b-3bd3-49f2-86ac-718fd6b36ac0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "Hidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%) but do not improve selection (gap closure $-5.1$\\% vs.\\ $+4.8$\\%; Appendix~\\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\\theta{=}2/N$ (an entity is included if it appears in ${\\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\\theta \\in [0.15, 0.35]$ (Appendix~\\ref{app:theta_sweep}; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\\ greedy; LP-weighted positive across all seeds. Best per dataset in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}",
      "numLines": 30,
      "startLine": 180,
      "totalLines": 228
    }
  }
}
```

</details>

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SRhbzWGJBo1rtTCEERVNGu`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"rho\" /root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1_merged.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "6a70aea4-c9b1-4fb9-8ce9-d8ed16e041d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4hpvNEUPi1HEZebh3gUVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 80722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1946
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

_source line 108 · 2026-05-19T08:04:58.051Z_

<details><summary>↩ Tool result · `toolu_01SRhbzWGJBo1rtTCEERVNGu`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "802c9856-e8f4-4642-9ab1-c6375903a0fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HbwjgsqM9pV11N8Xb64Zwz`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair/bootstrap_tests.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "22a8f525-d9b9-40de-82d2-27e62cbec4e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4hpvNEUPi1HEZebh3gUVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 80722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1946
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

_source line 110 · 2026-05-19T08:04:58.931Z_

<details><summary>↩ Tool result · `toolu_01HbwjgsqM9pV11N8Xb64Zwz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008632512370946359,\\n      \\\"ci_95\\\": [\\n        -0.003791963965516347,\\n        0.020730607954267292\\n      ],\\n      \\\"p_value\\\": 0.0844,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.002787353954222393,\\n      \\\"ci_95\\\": [\\n        -0.014480068531011032,\\n        0.020922071081157054\\n      ],\\n      \\\"p_value\\\": 0.3801,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01345547097798849,\\n      \\\"ci_95\\\": [\\n        0.0009839962198741237,\\n        0.02630432351819819\\n      ],\\n      \\\"p_value\\\": 0.0178,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0023481592529448476,\\n      \\\"ci_95\\\": [\\n        -0.010436567965856096,\\n        0.015129877508434367\\n      ],\\n      \\\"p_value\\\": 0.3519,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.0002739770648436429,\\n      \\\"ci_95\\\": [\\n        -0.012955645550847519,\\n        0.011613805127758964\\n      ],\\n      \\\"p_value\\\": 0.5123,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008363509545715585,\\n      \\\"ci_95\\\": [\\n        -0.007401747073516637,\\n        0.02510800810259234\\n      ],\\n      \\\"p_value\\\": 0.1555,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.013221640351074353,\\n      \\\"ci_95\\\": [\\n        0.0009737906171938178,\\n        0.0258295341900646\\n      ],\\n      \\\"p_value\\\": 0.0176,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.04054050539199403,\\n      \\\"ci_95\\\": [\\n        0.02520716355809246,\\n        0.05671076104490387\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"re_bootstrap_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.017012718430487805,\\n      \\\"ci_95\\\": [\\n        -0.004241096280321234,\\n        0.03843625367491151\\n      ],\\n      \\\"p_value\\\": 0.0577,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.03877385763795127,\\n      \\\"ci_95\\\": [\\n        -0.06513666219930019,\\n        -0.013443998202601294\\n      ],\\n      \\\"p_value\\\": 0.9984,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.016944093503639814,\\n      \\\"ci_95\\\": [\\n        -0.003071267631759127,\\n        0.03738629150727449\\n      ],\\n      \\\"p_value\\\": 0.0491,\\n      \\\"significant\\\": true\\n    },\\n    \\\"re_bootstrap_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01633499875465849,\\n      \\\"ci_95\\\": [\\n        -0.004337920008997516,\\n        0.037507703386720395\\n      ],\\n      \\\"p_value\\\": 0.063,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.032849927184058415,\\n      \\\"ci_95\\\": [\\n        -0.058434469977958474,\\n        -0.008123714862396852\\n      ],\\n      \\\"p_value\\\": 0.9951,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.016256690169733645,\\n      \\\"ci_95\\\": [\\n        -0.003759394092569898,\\n        0.03660975996278453\\n      ],\\n      \\\"p_value\\\": 0.0563,\\n      \\\"significant\\\": false\\n    }\\n  },\\n  \\\"conll\\\": {\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.006577494322841373,\\n      \\\"ci_95\\\": [\\n        -0.010970439839989165,\\n        -0.0023855440430373197\\n      ],\\n      \\\"p_value\\\": 0.9993,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.02724585599918863,\\n      \\\"ci_95\\\": [\\n        -0.033208926393966665,\\n        -0.021236457988772557\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0010409620256079646,\\n      \\\"ci_95\\\": [\\n        -0.002756243546775295,\\n        0.005028159895137432\\n      ],\\n      \\\"p_value\\\": 0.3031,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.011001713361957103,\\n      \\\"ci_95\\\": [\\n        -0.01494763939737124,\\n        -0.007087396577233873\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.007592229063991209,\\n      \\\"ci_95\\\": [\\n        -0.012042551325255375,\\n        -0.003414701712148993\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.014256333057760523,\\n      \\\"ci_95\\\": [\\n        -0.01942309639882521,\\n        -0.008949497734361976\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.0008813003193684586,\\n      \\\"ci_95\\\": [\\n        -0.004453925865039304,\\n        0.00274692884485563\\n      ],\\n      \\\"p_value\\\": 0.681,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.006951271010592901,\\n      \\\"ci_95\\\": [\\n        0.0023769061757714046,\\n        0.01177028627073427\\n      ],\\n      \\\"p_value\\\": 0.0012,\\n      \\\"significant\\\": true\\n    }\\n  },\\n  \\\"fewnerd\\\": {\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.028875033032470885,\\n      \\\"ci_95\\\": [\\n        -0.03472299470435823,\\n        -0.023169186372892836\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.014909366245230347,\\n      \\\"ci_95\\\": [\\n        -0.022441220802478457,\\n        -0.00726311142791446\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.013224082837758746,\\n      \\\"ci_95\\\": [\\n        0.007524222009906602,\\n        0.01907102308654646\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01883722530975516,\\n      \\\"ci_95\\\": [\\n        0.01405986593075787,\\n        0.0236791290744509\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.029382869516912866,\\n      \\\"ci_95\\\": [\\n        -0.03522879014046676,\\n        -0.023646884431677694\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.005191754957446426,\\n      \\\"ci_95\\\": [\\n        -0.0015834687341434387,\\n        0.012048554839400006\\n      ],\\n      \\\"p_value\\\": 0.0662,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.014245721350301178,\\n      \\\"ci_95\\\": [\\n        0.008743637236230993,\\n        0.01991429890808697\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0555410065159577,\\n      \\\"ci_95\\\": [\\n        0.04925720708508786,\\n        0.06177817005800181\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "65be98bd-16c0-4f05-b6d9-f669b1aeaa69",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"bootstrap_construction_uniform_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.008632512370946359,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.003791963965516347,\\\\n        0.020730607954267292\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0844,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.002787353954222393,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.014480068531011032,\\\\n        0.020922071081157054\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.3801,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.01345547097798849,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.0009839962198741237,\\\\n        0.02630432351819819\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0178,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"bootstrap_lp_selection_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.0023481592529448476,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.010436567965856096,\\\\n        0.015129877508434367\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.3519,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0002739770648436429,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.012955645550847519,\\\\n        0.011613805127758964\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.5123,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.008363509545715585,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.007401747073516637,\\\\n        0.02510800810259234\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.1555,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.013221640351074353,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.0009737906171938178,\\\\n        0.0258295341900646\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0176,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"bootstrap_adaptive_uniform_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.04054050539199403,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.02520716355809246,\\\\n        0.05671076104490387\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"re_bootstrap_uniform_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.017012718430487805,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.004241096280321234,\\\\n        0.03843625367491151\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0577,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"re_bootstrap_uniform_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.03877385763795127,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.06513666219930019,\\\\n        -0.013443998202601294\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.9984,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"re_bootstrap_uniform_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.016944093503639814,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.003071267631759127,\\\\n        0.03738629150727449\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0491,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"re_bootstrap_lp_weighted_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.01633499875465849,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.004337920008997516,\\\\n        0.037507703386720395\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.063,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"re_bootstrap_lp_weighted_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.032849927184058415,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.058434469977958474,\\\\n        -0.008123714862396852\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.9951,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"re_bootstrap_lp_weighted_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.016256690169733645,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.003759394092569898,\\\\n        0.03660975996278453\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0563,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    }\\\\n  },\\\\n  \\\\\\\"conll\\\\\\\": {\\\\n    \\\\\\\"bootstrap_construction_uniform_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.006577494322841373,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.010970439839989165,\\\\n        -0.0023855440430373197\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.9993,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.02724585599918863,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.033208926393966665,\\\\n        -0.021236457988772557\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.0010409620256079646,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.002756243546775295,\\\\n        0.005028159895137432\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.3031,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_lp_selection_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.011001713361957103,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.01494763939737124,\\\\n        -0.007087396577233873\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.007592229063991209,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.012042551325255375,\\\\n        -0.003414701712148993\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.014256333057760523,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.01942309639882521,\\\\n        -0.008949497734361976\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.0008813003193684586,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.004453925865039304,\\\\n        0.00274692884485563\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.681,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_adaptive_uniform_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.006951271010592901,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.0023769061757714046,\\\\n        0.01177028627073427\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0012,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    }\\\\n  },\\\\n  \\\\\\\"fewnerd\\\\\\\": {\\\\n    \\\\\\\"bootstrap_construction_uniform_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.028875033032470885,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.03472299470435823,\\\\n        -0.023169186372892836\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.014909366245230347,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.022441220802478457,\\\\n        -0.00726311142791446\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_uniform_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.013224082837758746,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.007524222009906602,\\\\n        0.01907102308654646\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"bootstrap_lp_selection_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.01883722530975516,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.01405986593075787,\\\\n        0.0236791290744509\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": -0.029382869516912866,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.03522879014046676,\\\\n        -0.023646884431677694\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 1.0,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.005191754957446426,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        -0.0015834687341434387,\\\\n        0.012048554839400006\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0662,\\\\n      \\\\\\\"significant\\\\\\\": false\\\\n    },\\\\n    \\\\\\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.014245721350301178,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.008743637236230993,\\\\n        0.01991429890808697\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"bootstrap_adaptive_uniform_vs_greedy\\\\\\\": {\\\\n      \\\\\\\"mean_diff\\\\\\\": 0.0555410065159577,\\\\n      \\\\\\\"ci_95\\\\\\\": [\\\\n        0.04925720708508786,\\\\n        0.06177817005800181\\\\n      ],\\\\n      \\\\\\\"p_value\\\\\\\": 0.0,\\\\n      \\\\\\\"significant\\\\\\\": true\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008632512370946359,\\n      \\\"ci_95\\\": [\\n        -0.003791963965516347,\\n        0.020730607954267292\\n      ],\\n      \\\"p_value\\\": 0.0844,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.002787353954222393,\\n      \\\"ci_95\\\": [\\n        -0.014480068531011032,\\n        0.020922071081157054\\n      ],\\n      \\\"p_value\\\": 0.3801,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01345547097798849,\\n      \\\"ci_95\\\": [\\n        0.0009839962198741237,\\n        0.02630432351819819\\n      ],\\n      \\\"p_value\\\": 0.0178,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0023481592529448476,\\n      \\\"ci_95\\\": [\\n        -0.010436567965856096,\\n        0.015129877508434367\\n      ],\\n      \\\"p_value\\\": 0.3519,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.0002739770648436429,\\n      \\\"ci_95\\\": [\\n        -0.012955645550847519,\\n        0.011613805127758964\\n      ],\\n      \\\"p_value\\\": 0.5123,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.008363509545715585,\\n      \\\"ci_95\\\": [\\n        -0.007401747073516637,\\n        0.02510800810259234\\n      ],\\n      \\\"p_value\\\": 0.1555,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.013221640351074353,\\n      \\\"ci_95\\\": [\\n        0.0009737906171938178,\\n        0.0258295341900646\\n      ],\\n      \\\"p_value\\\": 0.0176,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.04054050539199403,\\n      \\\"ci_95\\\": [\\n        0.02520716355809246,\\n        0.05671076104490387\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"re_bootstrap_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.017012718430487805,\\n      \\\"ci_95\\\": [\\n        -0.004241096280321234,\\n        0.03843625367491151\\n      ],\\n      \\\"p_value\\\": 0.0577,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.03877385763795127,\\n      \\\"ci_95\\\": [\\n        -0.06513666219930019,\\n        -0.013443998202601294\\n      ],\\n      \\\"p_value\\\": 0.9984,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.016944093503639814,\\n      \\\"ci_95\\\": [\\n        -0.003071267631759127,\\n        0.03738629150727449\\n      ],\\n      \\\"p_value\\\": 0.0491,\\n      \\\"significant\\\": true\\n    },\\n    \\\"re_bootstrap_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01633499875465849,\\n      \\\"ci_95\\\": [\\n        -0.004337920008997516,\\n        0.037507703386720395\\n      ],\\n      \\\"p_value\\\": 0.063,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.032849927184058415,\\n      \\\"ci_95\\\": [\\n        -0.058434469977958474,\\n        -0.008123714862396852\\n      ],\\n      \\\"p_value\\\": 0.9951,\\n      \\\"significant\\\": false\\n    },\\n    \\\"re_bootstrap_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.016256690169733645,\\n      \\\"ci_95\\\": [\\n        -0.003759394092569898,\\n        0.03660975996278453\\n      ],\\n      \\\"p_value\\\": 0.0563,\\n      \\\"significant\\\": false\\n    }\\n  },\\n  \\\"conll\\\": {\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.006577494322841373,\\n      \\\"ci_95\\\": [\\n        -0.010970439839989165,\\n        -0.0023855440430373197\\n      ],\\n      \\\"p_value\\\": 0.9993,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.02724585599918863,\\n      \\\"ci_95\\\": [\\n        -0.033208926393966665,\\n        -0.021236457988772557\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0010409620256079646,\\n      \\\"ci_95\\\": [\\n        -0.002756243546775295,\\n        0.005028159895137432\\n      ],\\n      \\\"p_value\\\": 0.3031,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.011001713361957103,\\n      \\\"ci_95\\\": [\\n        -0.01494763939737124,\\n        -0.007087396577233873\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.007592229063991209,\\n      \\\"ci_95\\\": [\\n        -0.012042551325255375,\\n        -0.003414701712148993\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.014256333057760523,\\n      \\\"ci_95\\\": [\\n        -0.01942309639882521,\\n        -0.008949497734361976\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.0008813003193684586,\\n      \\\"ci_95\\\": [\\n        -0.004453925865039304,\\n        0.00274692884485563\\n      ],\\n      \\\"p_value\\\": 0.681,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.006951271010592901,\\n      \\\"ci_95\\\": [\\n        0.0023769061757714046,\\n        0.01177028627073427\\n      ],\\n      \\\"p_value\\\": 0.0012,\\n      \\\"significant\\\": true\\n    }\\n  },\\n  \\\"fewnerd\\\": {\\n    \\\"bootstrap_construction_uniform_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.028875033032470885,\\n      \\\"ci_95\\\": [\\n        -0.03472299470435823,\\n        -0.023169186372892836\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.014909366245230347,\\n      \\\"ci_95\\\": [\\n        -0.022441220802478457,\\n        -0.00726311142791446\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_uniform_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.013224082837758746,\\n      \\\"ci_95\\\": [\\n        0.007524222009906602,\\n        0.01907102308654646\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_lp_selection_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.01883722530975516,\\n      \\\"ci_95\\\": [\\n        0.01405986593075787,\\n        0.0236791290744509\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_construction_lp_weighted_majority_vs_greedy\\\": {\\n      \\\"mean_diff\\\": -0.029382869516912866,\\n      \\\"ci_95\\\": [\\n        -0.03522879014046676,\\n        -0.023646884431677694\\n      ],\\n      \\\"p_value\\\": 1.0,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_confirm_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.005191754957446426,\\n      \\\"ci_95\\\": [\\n        -0.0015834687341434387,\\n        0.012048554839400006\\n      ],\\n      \\\"p_value\\\": 0.0662,\\n      \\\"significant\\\": false\\n    },\\n    \\\"bootstrap_construction_lp_weighted_cv_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.014245721350301178,\\n      \\\"ci_95\\\": [\\n        0.008743637236230993,\\n        0.01991429890808697\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    },\\n    \\\"bootstrap_adaptive_uniform_vs_greedy\\\": {\\n      \\\"mean_diff\\\": 0.0555410065159577,\\n      \\\"ci_95\\\": [\\n        0.04925720708508786,\\n        0.06177817005800181\\n      ],\\n      \\\"p_value\\\": 0.0,\\n      \\\"significant\\\": true\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
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
Now I have the full picture.

## FewNERD entity construction (N=8) from bootstrap_tests.json:
- `bootstrap_construction_lp_weighted_cv_vs_greedy`: mean_diff = 0.01424 (1.42pp), CI [0.87, 1.99], p=0.0
- `bootstrap_lp_selection_vs_greedy`: mean_diff = 0.01884 (1.88pp) — wait, that's the LP selection from exp_027_fewnerd_n16. 

I need to verify which dataset the entity_construction_fair analysis is actually using. The timestamps suggest the fair analysis from May 19 could be pulling from the N=16 experiment completed on May 17, but I'm seeing N=8 construction data mixed in here.

Looking at the bootstrap results more carefully: the LP-weighted construction CV shows 1.42pp mean difference for FewNERD, which matches the paper's reported 1.40±0.51pp for N=8. So that's consistent. But I need to figure out what the N=16 construction gains actually are to complete the scaling claim. I realize the construction_results.json file was too large and got cut off in the output—I only saw the SciERC section before it truncated. The FewNERD results might actually be there with both N=8 and N=16 data, so let me search specifically for FewNERD in the non-fair construction results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "006a9c10-0ba7-4f7d-b105-f9b0121eacc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J73AFhqjVDDB2EXZKtqNJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 82668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 112_

Let me check the FewNERD section of the construction_results.json specifically (it was truncated earlier).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "1f0f899b-36ae-4d0d-841d-1c801598691f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J73AFhqjVDDB2EXZKtqNJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 82668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 113_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HtWBLmuQzVsk7FJ1kxHnvz`</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json')); print(list(d.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "94d84855-5a1f-4048-82f2-cc8f4b86725e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J73AFhqjVDDB2EXZKtqNJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 82668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 114 · 2026-05-19T08:05:22.456Z_

<details><summary>↩ Tool result · `toolu_01HtWBLmuQzVsk7FJ1kxHnvz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "200e1f2d-c1f2-43f0-92bb-d6c41a55a98b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0192Y3MaypZmq43GnVx6jdAi`</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json')); fewnerd=d.get('fewnerd',d.get('fewnerd_n16',{})); print(list(fewnerd.keys())[:20])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "16166767-0b41-40c8-ac21-09728ceac965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J73AFhqjVDDB2EXZKtqNJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 82668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 116 · 2026-05-19T08:05:24.347Z_

<details><summary>↩ Tool result · `toolu_0192Y3MaypZmq43GnVx6jdAi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "4fe5f21d-62cf-40da-8ab4-89a742b447b5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 117_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Ke5Qp9uqK8FQQvpWhLycTb`</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json')); print(json.dumps({k: list(v.keys())[:3] for k,v in d.items()}))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "502d602a-07c9-4395-91ee-13c326be394b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J73AFhqjVDDB2EXZKtqNJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5851,
      "cache_read_input_tokens": 82668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5851
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

_source line 118 · 2026-05-19T08:05:25.390Z_

<details><summary>↩ Tool result · `toolu_01Ke5Qp9uqK8FQQvpWhLycTb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c15a7de6-870d-4c69-b2ea-35116e356c18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 119_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01BMkHqkEW4riC13ELe2DpZR`</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json')); print(list(d.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b9790035-8f22-4c78-a4d7-421d9493c669",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATNBhwif5nXneLcUAhiC2e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1681,
      "cache_read_input_tokens": 88519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1681
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

_source line 120 · 2026-05-19T08:05:28.803Z_

<details><summary>↩ Tool result · `toolu_01BMkHqkEW4riC13ELe2DpZR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"import json; d=json.load(open(\\\\'/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\')); print(list(d.keys()))\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "18698d9c-6758-4d84-a964-206069a44e5e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'python3 -c \\\\\\\"import json; d=json.load(open(\\\\\\\\'/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\\\\\')); print(list(d.keys()))\\\\\\\"'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"import json; d=json.load(open(\\\\'/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\')); print(list(d.keys()))\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01MvfPJzhuqsHdFyJwgP1NL1`</summary>

```json
{
  "server": "autodl-5090",
  "command": "/root/miniconda3/envs/scs/bin/python -c \"import json; d=json.load(open('/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json')); print(list(d.keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "c4c7ec72-ce2a-4a12-8a81-27f29372a393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H78Ly7KbqH8optCE5yJN2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 331,
      "cache_read_input_tokens": 90200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 331
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

_source line 122 · 2026-05-19T08:05:33.461Z_

<details><summary>↩ Tool result · `toolu_01MvfPJzhuqsHdFyJwgP1NL1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: '/root/miniconda3/envs/scs/bin/python -c \\\"import json; d=json.load(open(\\\\'/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\')); print(list(d.keys()))\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: /root/miniconda3/envs/scs/bin/python: No such file or directory\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.92}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "06db5448-90b5-4ece-a3c9-ba6a2dad4b95",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: '/root/miniconda3/envs/scs/bin/python -c \\\\\\\"import json; d=json.load(open(\\\\\\\\'/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\\\\\')); print(list(d.keys()))\\\\\\\"'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: /root/miniconda3/envs/scs/bin/python: No such file or directory\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.92}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: '/root/miniconda3/envs/scs/bin/python -c \\\"import json; d=json.load(open(\\\\'/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json\\\\')); print(list(d.keys()))\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: /root/miniconda3/envs/scs/bin/python: No such file or directory\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.92}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01K79NadhZhKTuwQoMjcJipR`</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "4dc84af4-2be6-49ae-bab8-da37e2bddc82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg7MaoNHhMyqsQdjZWNT2n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 90531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 477
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

_source line 124 · 2026-05-19T08:05:37.846Z_

<details><summary>↩ Tool result · `toolu_01K79NadhZhKTuwQoMjcJipR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"greedy\\\": {\\n      \\\"F1\\\": 0.6441821796820129,\\n      \\\"P\\\": 0.6603624688690851,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "095adedb-b9ea-4f6a-b11c-81ece356ffc6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"greedy\\\\\\\": {\\\\n      \\\\\\\"F1\\\\\\\": 0.6441821796820129,\\\\n      \\\\\\\"P\\\\\\\": 0.6603624688690851,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"greedy\\\": {\\n      \\\"F1\\\": 0.6441821796820129,\\n      \\\"P\\\": 0.6603624688690851,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 125_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017MdrPvtG1ycvDqA6JRprfc`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"fewnerd\\|n16\\|n_16\" /root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "15cbd173-5fde-425b-b8a2-5ce8eb51fc86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tg7MaoNHhMyqsQdjZWNT2n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 90531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 477
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

_source line 126 · 2026-05-19T08:05:38.013Z_

<details><summary>↩ Tool result · `toolu_017MdrPvtG1ycvDqA6JRprfc`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "aff948e2-7d60-4a79-ae40-99b8feda40c0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 127_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01QbxfWVYrDHqw79p8V7m1cm`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"fewnerd\" /root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "b993e5a7-363c-4ffd-8c6e-f1f240922c67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sWxAf6RMwhfJZ16f8Aaxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 91008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
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

_source line 128 · 2026-05-19T08:05:41.829Z_

<details><summary>↩ Tool result · `toolu_01QbxfWVYrDHqw79p8V7m1cm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"601:  \\\"fewnerd\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "80ea263d-481e-43dc-81c6-44084385547c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"601:  \\\\\\\"fewnerd\\\\\\\": {\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"601:  \\\"fewnerd\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KG5b5PjtdKb3yUzCsr3bcP`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"fewnerd\" /root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair/fair_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "738070cf-efcc-4119-bdd0-f338f0d391c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sWxAf6RMwhfJZ16f8Aaxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 91008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 556
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

_source line 130 · 2026-05-19T08:05:42.361Z_

<details><summary>↩ Tool result · `toolu_01KG5b5PjtdKb3yUzCsr3bcP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"707:  \\\"fewnerd\\\": {\\n890:      \\\"dataset\\\": \\\"fewnerd\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "353ff421-83a4-4a26-90ec-8fd49ff3437a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"707:  \\\\\\\"fewnerd\\\\\\\": {\\\\n890:      \\\\\\\"dataset\\\\\\\": \\\\\\\"fewnerd\\\\\\\",\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"707:  \\\"fewnerd\\\": {\\n890:      \\\"dataset\\\": \\\"fewnerd\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 131_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Hb3mr7skKxuFEJrhsouQVt`</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -n +601 /root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8a7c5621-29b1-4475-9625-e962f960c1bd",
  "uuid": "afcb5b40-cc00-4460-a36e-daae1769c5f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuQXc9CCsjYcAaDYGbPG8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 91564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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
