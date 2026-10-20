# audit final appendix tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_audit_final-appendix-tables_20260523T191706.log`
- **Structured JSON:** [`e1db034ee24abd87fb80.json`](../../sessions/e1/e1db034ee24abd87fb80.json)

## Before a recorded user message

67 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
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
  "uuid": "b2779e85-fb5b-45c9-a39a-8b0a476c565d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/memory/"
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
    "resetsAt": 1779581400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a9407883-9336-4e85-a0c5-aba90f237563",
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8"
}
```

---

### Assistant

_source line 4_

I'll start by reading the appendix, experiments tex, and registry data in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "961d66a1-49e9-4688-b89a-ef94e10caa18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgL2Dswvh9wKvK8wRCsZes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12303,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12303
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

<details open><summary>🔧 Tool call — Read · `toolu_01Y3RdyuRfuJCfJaV7pz9bhH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "40f39c3e-e161-49a9-9b24-11e0ff1f348a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgL2Dswvh9wKvK8wRCsZes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12303,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12303
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

_source line 6 · 2026-05-23T19:17:16.174Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y3RdyuRfuJCfJaV7pz9bhH`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "616e7da6-786e-4990-9740-5ecf12541280",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01WkbQ2Df46J4Gja8A2GK7RQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "d8768369-4d1a-4273-a1a6-ba74eea29736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgL2Dswvh9wKvK8wRCsZes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12303,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12303
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

_source line 8 · 2026-05-23T19:17:16.699Z_

<details><summary>↩ Tool result · reported error · `toolu_01WkbQ2Df46J4Gja8A2GK7RQ`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "0667305b-ee52-4b00-a1f8-b146ae3428f2",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study."
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EGYAKWFa6Pyatv3qfLhqRC`</summary>

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
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "65fd98ec-1109-4077-a3be-e30c50702604",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgL2Dswvh9wKvK8wRCsZes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12303,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12303
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

_source line 10 · 2026-05-23T19:17:17.602Z_

<details><summary>↩ Tool result · `toolu_01EGYAKWFa6Pyatv3qfLhqRC`</summary>

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
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "ac2ba0d8-a9ee-4da7-8a07-616fa69f6613",
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

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The local paper files don't exist. According to the project context, the paper files are on the server at `/root/trace-verdict-study/docs/paper/`. Let me read them from the server via SSH, and also fetch the registry data.

But wait - I should check if there are local copies first. Let me look for the paper files locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "7b743cac-62c2-42ec-ab7e-5d840d157aec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tsqvz3Hk2rc35sBxY3u9Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 24144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

_source line 12_

Paper files aren't at the local path. Per constraint C001, they're on the server. Let me find them locally and fetch the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "b2e169df-b325-4036-929c-5e89cb4bb1ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tsqvz3Hk2rc35sBxY3u9Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 24144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01HueDv8G2fHvTff144j2Bwn`</summary>

```json
{
  "pattern": "**/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "67e0638c-ea48-40be-9236-6486f9877ce4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tsqvz3Hk2rc35sBxY3u9Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 24144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

_source line 14 · 2026-05-23T19:17:27.631Z_

<details><summary>↩ Tool result · `toolu_01HueDv8G2fHvTff144j2Bwn`</summary>

```text
artifacts/_project/paper/appendix.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "c1d27463-97a8-4b19-acdb-b0e19c81eb3c",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/appendix.tex",
      "docs/paper/appendix.tex"
    ],
    "durationMs": 20,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01DosEjDVwogW9s55SuZUB9t`</summary>

```json
{
  "pattern": "**/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "2d3a6383-5e68-463b-bad9-68a8235f31ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tsqvz3Hk2rc35sBxY3u9Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 24144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

_source line 16 · 2026-05-23T19:17:28.174Z_

<details><summary>↩ Tool result · `toolu_01DosEjDVwogW9s55SuZUB9t`</summary>

```text
artifacts/_project/paper/experiments.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "c5414c52-56d7-4d88-9bd0-c381136f3fd4",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiments.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 12,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FStdsd9UaBEW5rCTJdC6VZ`</summary>

```json
{
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
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "a6413012-44b4-418b-a488-8e00c68367fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tsqvz3Hk2rc35sBxY3u9Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 24144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 746
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

_source line 18 · 2026-05-23T19:17:28.387Z_

<details><summary>↩ Tool result · `toolu_01FStdsd9UaBEW5rCTJdC6VZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"no_trace_seed123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:16:15.921Z\", \"updated_at\": \"2026-05-22T23:42:31.000Z\", \"hypothesis\": \"Replication of no_trace baseline with seed=123 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\", \"spec\": {\"command\": \"bash -c \\\"... python train/train_sft.py --condition no_trace --gpu 0 --gradient_checkpointing --seed 123\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/humaneval_trainset.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\"}}, \"no_trace_seed456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:16:16.072Z\", \"updated_at\": \"2026-05-22T23:16:26.102Z\", \"hypothesis\": \"Replication of no_trace baseline with seed=456 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\"}, \"attention_gradient_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:26:08.040Z\", \"updated_at\": \"2026-05-22T19:26:34.240Z\", \"hypothesis\": \"In full_trace models, execution trace tokens dominate input but receive disproportionately low attention and gradient signal at verdict position, demonstrating gradient dilution where non-diagnostic tokens dilute learning signal away from diagnostic content.\", \"spec\": {\"command\": \"attention gradient analysis script\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"exception_only_seed42\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/attention_gradient_analysis/\", \"log_path\": \"N/A (analysis script)\"}, \"conclusion\": \"success\", \"metrics\": {\"analysis_files_produced\": 10, \"analysis_type\": \"attention_gradient\"}, \"completed_at\": \"2026-05-22T19:26:34.240Z\"}, \"gradient_masking_qwen7b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:26:03.894Z\", \"updated_at\": \"2026-05-22T19:26:07.917Z\", \"conclusion\": \"killed\"}, \"exc_type_only\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:25:59.333Z\", \"updated_at\": \"2026-05-22T19:26:03.358Z\", \"conclusion\": \"killed\"}, \"cross_dataset_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:25:00.707Z\", \"updated_at\": \"2026-05-22T19:25:54.359Z\", \"spec\": {\"command\": \"cross-dataset batch runner\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"cross_dataset_eval\", \"checkpoint_path\": \"N/A (batch runner)\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\"}, \"hypothesis\": \"Batch runner for cross-dataset generalization experiments: trains models on one dataset and evaluates on another to test whether trace-based SFT learns transferable reasoning patterns rather than dataset-specific shortcuts.\", \"conclusion\": \"success\", \"metrics\": {\"sub_experiments_completed\": 4, \"all_success\": true}, \"completed_at\": \"2026-05-22T19:25:54.360Z\"}, \"cross_mbpp2he_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:52:56.834Z\", \"updated_at\": \"2026-05-22T19:25:38.928Z\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"pass_f1\": 1, \"fail_f1\": 1, \"n_test\": 1190}, \"spec\": {\"command\": \"cross-dataset batch\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_exception_only/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\"}, \"hypothesis\": \"Cross-dataset generalization MBPP→HE with exception_only: exception trace SFT learns transferable code reasoning patterns that generalize across datasets, predicting smaller accuracy drop compared to no_trace baseline when trained on MBPP and tested on HumanEval.\", \"completed_at\": \"2026-05-22T19:25:38.928Z\"}, \"cross_mbpp2he_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:52:58.755Z\", \"updated_at\": \"2026-05-22T19:25:37.503Z\", \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.6799, \"pass_f1\": 0.7363, \"fail_f1\": 0.5927, \"n_test\": 1190}, \"spec\": {\"command\": \"cross-dataset batch\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_no_trace/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\"}, \"hypothesis\": \"Cross-dataset generalization MBPP→HE with no_trace baseline: without execution traces, SFT relies on dataset-specific code patterns that do not transfer well across datasets, predicting larger accuracy drop when trained on MBPP and tested on HumanEval.\", \"completed_at\": \"2026-05-22T19:25:37.503Z\"}, \"nomarker_cross_he2mbpp_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:35:34.065Z\", \"updated_at\": \"2026-05-22T17:33:57.115Z\", \"hypothesis\": \"Exception_only_nomarker model (trained on HumanEval without pass/fail markers) transfers to MBPP with minimal accuracy loss, demonstrating that marker-free SFT still learns transferable code reasoning patterns. This strengthens the anti-tautology defense by showing cross-dataset generalization does not depend on explicit verdict markers.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition cross_he2mbpp_exception_only_nomarker --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --gpu 0 --gradient_checkpointing --seed 42\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1640, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"cross_he2mbpp_nomarker_test_4270\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.955, \"accuracy_ci_lower\": 0.948, \"accuracy_ci_upper\": 0.961, \"pass_precision\": 0.99, \"pass_recall\": 0.94, \"pass_f1\": 0.97, \"fail_precision\": 0.88, \"fail_recall\": 0.99, \"fail_f1\": 0.93, \"majority_baseline\": 0.69, \"lift\": 0.264, \"n_test\": 4270}, \"completed_at\": \"2026-05-22T17:33:57.116Z\"}, \"gradient_masking_qwen7b_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:35:12.813Z\", \"updated_at\": \"2026-05-22T16:58:23.973Z\", \"hypothesis\": \"Replication of gradient masking ablation with seed=456 to establish statistical robustness. Random masking of 99.8% token gradients on exception_only data should reproduce seed42 (98.99%) and seed123 results, confirming that gradient dilution accounts for only ~1pp degradation while content quality explains ~95% of full_trace's poor performance.\", \"parent\": \"gradient_masking_qwen7b_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 456 --wandb_project trace-verdict-study --wandb_run_name gradient_masking_qwen7b_seed456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/humaneval_trainset.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9933, \"pass_f1\": 0.9953, \"fail_f1\": 0.9883, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"n_test\": 1190, \"gradient_mask_ratio\": 0.998}, \"completed_at\": \"2026-05-22T16:58:23.973Z\"}, \"exc_message_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:32:37.876Z\", \"updated_at\": \"2026-05-22T13:33:24.076Z\", \"hypothesis\": \"Exception message text alone (without type or stacktrace) carries natural language description of the error. Tests whether the semantic content of the error message is sufficient for verdict classification, or whether structural context (stacktrace) is also needed.\", \"parent\": \"vota_exception_only_seed42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exc_message_only --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42 --gpu 0 --seed 42 --gradient_checkpointing --wandb_project trace-verdict-study --wandb_run_name exc_message_only_seed42\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.995, \"pass_f1\": 0.9965, \"fail_f1\": 0.9912, \"pass_precision\": 1, \"pass_recall\": 0.9929, \"fail_precision\": 0.9826, \"fail_recall\": 1, \"n_test\": 1190, \"eval_loss\": 0.58, \"train_loss\": 0.1828}, \"completed_at\": \"2026-05-22T13:33:24.076Z\"}, \"gradient_masking_qwen7b_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:33:00.898Z\", \"updated_at\": \"2026-05-22T12:33:07.778Z\", \"hypothesis\": \"Seed robustness check for gradient masking ablation. If seed123 also shows ~99% accuracy with 99.8% gradient masking, confirms that content quality (not gradient distribution) is the dominant factor across random initializations.\", \"parent\": \"gradient_masking_qwen7b_seed42\"}, \"exc_type_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:52:35.048Z\", \"updated_at\": \"2026-05-22T10:52:53.082Z\", \"hypothesis\": \"Exception type alone (e.g. 'ValueError') without message or stacktrace retains most of exception_only's diagnostic power, since the error type is the primary signal for verdict classification.\", \"parent\": \"vota_exception_only_seed42_v2\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"pass_f1\": 1, \"fail_f1\": 1, \"pass_precision\": 1, \"pass_recall\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2849, \"n_test\": 1190}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42.log\", \"command\": \"python train/train_sft.py --condition exc_type_only --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ --gpu 0 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"completed_at\": \"2026-05-22T10:52:53.082Z\"}, \"exc_stacktrace_only_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:32:37.400Z\", \"updated_at\": \"2026-05-22T10:32:43.923Z\", \"hypothesis\": \"Exception stacktrace (line numbers + local variable context without error type/message) provides structural execution path information. If accuracy is high, structural context alone is sufficient for verdict classification; if low, the error type/message carries the primary signal.\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"gradient_masking_qwen7b_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:44:29.302Z\", \"updated_at\": \"2026-05-22T09:50:37.759Z\", \"hypothesis\": \"If gradient dilution is the primary cause of full_trace degradation, masking exception_only gradients to full_trace's sparsity level (~0.2% label tokens) should degrade performance significantly. If performance stays at exception_only level (~99%), content quality (not gradient distribution) is the dominant factor.\", \"parent\": \"full_trace_label_only_seed42\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9899, \"accuracy_ci_lower\": 0.984, \"accuracy_ci_upper\": 0.995, \"majority_baseline\": 0.7151, \"lift\": 0.275, \"pass_f1\": 0.993, \"fail_f1\": 0.982, \"pass_precision\": 1, \"pass_recall\": 0.99, \"fail_precision\": 0.98, \"fail_recall\": 0.99, \"n_test\": 1190, \"gradient_mask_ratio\": 0.998, \"eval_loss\": 0.0533}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42.log\", \"command\": \"python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"completed_at\": \"2026-05-22T09:50:37.760Z\"}, \"deepseek_ae_only_seed123\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:46:24.864Z\", \"updated_at\": \"2026-05-20T13:30:43.575Z\", \"hypothesis\": \"DeepSeek ae_only seed123 应在 98-100%（与 seed42=98.74% 接近），确认 Tier 1 ae_only 最低值是 DeepSeek 的自然水平而非 seed anomaly\", \"parent\": \"deepseek_ae_only_seed42\"}, \"codellama13b_vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:35:09.665Z\", \"updated_at\": \"2026-05-20T13:30:36.364Z\", \"hypothesis\": \"CodeLlama-13B VOTA seed123 应在 97-100%（与 seed42=98.57% 接近），验证 VOTA Tier 1 跨 seed 稳定性，补强 C4 universality claim\", \"parent\": \"codellama13b_vota_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed123/final\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9891}, \"completed_at\": \"2026-05-20T13:30:36.364Z\"}, \"qwen15b_exception_only_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:56:13.468Z\", \"updated_at\": \"2026-05-20T12:56:25.490Z\", \"hypothesis\": \"Qwen-1.5B exception_only seed123 应在 99-100%（与 seed42=99.83% 接近），强化 C1 exception dominance 全模型全 seed ≥99.33% claim\", \"parent\": \"qwen15b_exception_only_seed42\"}, \"qwen15b_loop_only_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:35:15.163Z\", \"updated_at\": \"2026-05-20T11:54:28.603Z\", \"hypothesis\": \"Qwen-1.5B loop_only seed123 应在 75-82%（与 seed42=78.32% 接近），验证 1.5B Tier 2 跨 seed 稳定性 + 强化 D106 architecture-level 证据\", \"parent\": \"qwen15b_loop_only_seed42\"}, \"qwen1.5b_full_trace_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:16.238Z\", \"updated_at\": \"2026-05-20T11:04:16.238Z\", \"conclusion\": \"killed\"}, \"codellama_vota_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:12.939Z\", \"updated_at\": \"2026-05-20T11:04:12.939Z\", \"conclusion\": \"killed\"}, \"codellama_no_trace_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:12.025Z\", \"updated_at\": \"2026-05-20T11:04:12.025Z\", \"conclusion\": \"killed\"}, \"codellama_exception_only_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:11.572Z\", \"updated_at\": \"2026-05-20T11:04:11.572Z\", \"conclusion\": \"killed\"}, \"qwen1.5b_vota_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:08.643Z\", \"updated_at\": \"2026-05-20T10:44:08.643Z\", \"conclusion\": \"killed\"}, \"qwen1.5b_no_trace_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:07.835Z\", \"updated_at\": \"2026-05-20T10:44:07.835Z\", \"conclusion\": \"killed\"}, \"qwen1.5b_exception_only_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:07.214Z\", \"updated_at\": \"2026-05-20T10:44:07.214Z\", \"conclusion\": \"killed\"}, \"qwen15b_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:51:01.070Z\", \"updated_at\": \"2026-05-20T09:19:55.564Z\", \"hypothesis\": \"Qwen-1.5B loop_only 预期在 70-85% 范围，可能低于 7B (86.05%) 因 1.5B capacity 不足以从低密度 loop 信号中提取判别信息。填补 4-model Tier 2 矩阵\", \"parent\": \"qwen15b_full_trace_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.7832, \"pass_f1\": 0.853, \"fail_f1\": 0.59}, \"completed_at\": \"2026-05-20T09:19:55.564Z\"}, \"codellama13b_loop_only_seed456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:02:46.071Z\", \"updated_at\": \"2026-05-20T09:02:50.992Z\", \"hypothesis\": \"CodeLlama-13B loop_only seed456 应在 74-80%（与 seed42=77.06%, seed123=76.05% 接近），确认 Tier 2 在 CodeLlama 上 near-zero lift 是 seed-robust 的\", \"parent\": \"codellama13b_loop_only_seed42\"}, \"qwen15b_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:49:47.717Z\", \"updated_at\": \"2026-05-20T07:50:19.670Z\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"pass_precision\": 1, \"pass_recall\": 0.9871, \"pass_f1\": 0.9935, \"fail_precision\": 0.9686, \"fail_recall\": 1, \"fail_f1\": 0.984, \"majority_baseline\": 0.7151, \"lift\": 0.2756, \"eval_loss\": 0.1973, \"train_loss\": 0.0702, \"n\": 1190}, \"spec\": {\"command\": \"train + eval ae_only condition\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_ae_only_seed42.log\"}, \"hypothesis\": \"Assertion-error-only traces provide sufficient signal for a 1.5B parameter model to learn pass/fail classification at ≥95% accuracy, consistent with larger models (7B/13B), because the assertion error pattern is a strong binary discriminator regardless of model capacity.\", \"parent\": \"qwen15b_exception_only_seed42\", \"completed_at\": \"2026-05-20T07:50:19.670Z\"}, \"codellama13b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:25:08.019Z\", \"updated_at\": \"2026-05-20T06:57:17.305Z\", \"spec\": {\"checkpoint_path\": \"/root/trace-verdict-study/outputs/codellama13b_exception_only_seed42/\", \"log_path\": \"/root/trace-verdict-study/outputs/codellama13b_exception_only_seed42/eval_results.json\"}, \"hypothesis\": \"CodeLlama-13B exception_only should achieve ≥99% accuracy, confirming minimal sufficient signal universality across 13B-scale models\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 99.83}, \"completed_at\": \"2026-05-20T06:57:17.305Z\"}, \"codellama13b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:25:08.369Z\", \"updated_at\": \"2026-05-20T06:57:16.777Z\", \"spec\": {\"checkpoint_path\": \"/root/trace-verdict-study/outputs/codellama13b_vota_seed42/\", \"log_path\": \"/root/trace-verdict-study/outputs/codellama13b_vota_seed42/eval_results.json\"}, \"hypothesis\": \"CodeLlama-13B VOTA should achieve ≥95% accuracy, confirming VOTA tier 1 universality across model architectures\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 98.57}, \"completed_at\": \"2026-05-20T06:57:16.777Z\"}, \"qwen7b_full_trace_dynamics_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:40:56.724Z\", \"updated_at\": \"2026-05-19T06:41:32.669Z\", \"metrics\": {\"final_accuracy\": 0.8824, \"best_accuracy\": 0.8882, \"best_accuracy_step\": 350, \"step50_accuracy\": 0.8739, \"step100_accuracy\": 0.821, \"step200_accuracy\": 0.884, \"step444_accuracy\": 0.8824, \"final_train_loss\": 0.0085, \"best_pass_f1\": 0.9252, \"best_fail_f1\": 0.781, \"accuracy_gap_vs_exception_only\": -11.01}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_dynamics_seed42.log\", \"hypothesis\": \"Full trace with label_only_loss converges slower than exception_only because verbose execution traces dilute effective signal density, forcing the model to attend to irrelevant context and degrading gradient quality for verdict prediction.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"bash run_dynamics.sh qwen7b_full_trace_dynamics_seed42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"completed_at\": \"2026-05-19T06:41:32.669Z\"}, \"qwen15b_exception_only_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:48:18.227Z\", \"updated_at\": \"2026-05-18T23:49:05.454Z\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"n_test\": 1190}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123_v2/final\", \"log_path\": \"/root/runs/trace-verdict-study/qwen15b_exception_only_seed123_v2.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"train+eval qwen1.5b exception_only seed123 v2\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123}, \"hypothesis\": \"Qwen2.5-Coder-1.5B fine-tuned on exception-only traces can distinguish pass/fail test verdicts with high accuracy, because exception messages carry sufficient signal for verdict prediction even without full execution traces.\", \"completed_at\": \"2026-05-18T23:49:05.454Z\"}, \"deepseek_full_trace_seed42_v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:24:57.697Z\", \"updated_at\": \"2026-05-16T02:24:57.698Z\", \"notes\": \"DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with max_length=2048 (matches training). eval_results.json has stale 28.49% from max_length=16384 run; correct value in eval_results_maxlen2048.json. predictions.jsonl overwritten 2026-05-16 with maxlen2048 results (reliable). Systematic audit 2026-05-16 confirmed: adapter base_model=DeepSeek, no model mixup possible (dimension mismatch would crash).\"}, \"vota_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:52:29.262Z\", \"updated_at\": \"2026-05-15T20:53:03.185Z\", \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"pass_precision\": 1, \"pass_recall\": 0.9871, \"pass_f1\": 0.9935, \"fail_precision\": 0.9686, \"fail_recall\": 1, \"fail_f1\": 0.984, \"eval_loss\": 0.081, \"train_loss\": 0.0498, \"n_test\": 1190}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/vota_seed456.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"train+eval vota seed456 with gradient_checkpointing\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456}, \"completed_at\": \"2026-05-15T20:53:03.185Z\"}, \"medium_random50_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:51:02.394Z\", \"updated_at\": \"2026-05-14T01:51:35.564Z\", \"metrics\": {\"gen0\": {\"ppl\": 26.12, \"rankme\": 361.63, \"knn\": 0.988, \"rare\": 0.0346, \"corr\": 0.0101}, \"gen1\": {\"ppl\": 32.57, \"rankme\": 387.8, \"knn\": 0.988, \"rare\": 0.0277, \"corr\": 0.0331}, \"gen2\": {\"ppl\": 41.58, \"rankme\": 410.08, \"knn\": 0.988, \"rare\": 0.0214, \"corr\": 0.0088}, \"gen3\": {\"ppl\": 49.87, \"rankme\": 421.67, \"knn\": 0.988, \"rare\": 0.0182, \"corr\": -0.0018}, \"gen4\": {\"ppl\": 59.83, \"rankme\": 427.23, \"knn\": 0.988, \"rare\": 0.0161, \"corr\": -0.0014}, \"gen5\": {\"ppl\": 60.62, \"rankme\": 426.16, \"knn\": 0.988, \"rare\": 0.0144, \"corr\": -0.0004}, \"gen6\": {\"ppl\": 68.34, \"rankme\": 427.19, \"knn\": 0.988, \"rare\": 0.0134, \"corr\": -0.0071}, \"gen7\": {\"ppl\": 70.25, \"rankme\": 426.5, \"knn\": 0.988, \"rare\": 0.0128, \"corr\": -0.0034}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/div_cal_verify/results_medium_random50/random_50/gen_7\", \"log_path\": \"/root/autodl-tmp/div_cal_verify/medium_random50.log\", \"spec\": {\"command\": \"bash run_medium_random50.sh\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/div_cal_verify/\", \"data_count\": 977, \"model_name\": \"gpt2-medium\", \"seed\": 42}, \"completed_at\": \"2026-05-14T01:51:35.564Z\"}}, \"count\": 36, \"total\": 36, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0456}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "932810fe-5a3b-47ee-92d5-788f3ecce921",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"no_trace_seed123\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T23:16:15.921Z\\\", \\\"updated_at\\\": \\\"2026-05-22T23:42:31.000Z\\\", \\\"hypothesis\\\": \\\"Replication of no_trace baseline with seed=123 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"... python train/train_sft.py --condition no_trace --gpu 0 --gradient_checkpointing --seed 123\\\\\\\"\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data/humaneval_trainset.jsonl\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 123, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"humaneval_testset_1190\\\"}}, \\\"no_trace_seed456\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T23:16:16.072Z\\\", \\\"updated_at\\\": \\\"2026-05-22T23:16:26.102Z\\\", \\\"hypothesis\\\": \\\"Replication of no_trace baseline with seed=456 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\\\"}, \\\"attention_gradient_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T19:26:08.040Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:26:34.240Z\\\", \\\"hypothesis\\\": \\\"In full_trace models, execution trace tokens dominate input but receive disproportionately low attention and gradient signal at verdict position, demonstrating gradient dilution where non-diagnostic tokens dilute learning signal away from diagnostic content.\\\", \\\"spec\\\": {\\\"command\\\": \\\"attention gradient analysis script\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"exception_only_seed42\\\", \\\"eval_data\\\": \\\"humaneval_testset_1190\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/attention_gradient_analysis/\\\", \\\"log_path\\\": \\\"N/A (analysis script)\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"analysis_files_produced\\\": 10, \\\"analysis_type\\\": \\\"attention_gradient\\\"}, \\\"completed_at\\\": \\\"2026-05-22T19:26:34.240Z\\\"}, \\\"gradient_masking_qwen7b\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T19:26:03.894Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:26:07.917Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exc_type_only\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T19:25:59.333Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:26:03.358Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"cross_dataset_batch\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T19:25:00.707Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:25:54.359Z\\\", \\\"spec\\\": {\\\"command\\\": \\\"cross-dataset batch runner\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"cross_dataset_eval\\\", \\\"checkpoint_path\\\": \\\"N/A (batch runner)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\\\"}, \\\"hypothesis\\\": \\\"Batch runner for cross-dataset generalization experiments: trains models on one dataset and evaluates on another to test whether trace-based SFT learns transferable reasoning patterns rather than dataset-specific shortcuts.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"sub_experiments_completed\\\": 4, \\\"all_success\\\": true}, \\\"completed_at\\\": \\\"2026-05-22T19:25:54.360Z\\\"}, \\\"cross_mbpp2he_exception_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:52:56.834Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:25:38.928Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 1, \\\"pass_f1\\\": 1, \\\"fail_f1\\\": 1, \\\"n_test\\\": 1190}, \\\"spec\\\": {\\\"command\\\": \\\"cross-dataset batch\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"humaneval_testset_1190\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_exception_only/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\\\"}, \\\"hypothesis\\\": \\\"Cross-dataset generalization MBPP→HE with exception_only: exception trace SFT learns transferable code reasoning patterns that generalize across datasets, predicting smaller accuracy drop compared to no_trace baseline when trained on MBPP and tested on HumanEval.\\\", \\\"completed_at\\\": \\\"2026-05-22T19:25:38.928Z\\\"}, \\\"cross_mbpp2he_no_trace_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:52:58.755Z\\\", \\\"updated_at\\\": \\\"2026-05-22T19:25:37.503Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.6799, \\\"pass_f1\\\": 0.7363, \\\"fail_f1\\\": 0.5927, \\\"n_test\\\": 1190}, \\\"spec\\\": {\\\"command\\\": \\\"cross-dataset batch\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"humaneval_testset_1190\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_no_trace/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\\\"}, \\\"hypothesis\\\": \\\"Cross-dataset generalization MBPP→HE with no_trace baseline: without execution traces, SFT relies on dataset-specific code patterns that do not transfer well across datasets, predicting larger accuracy drop when trained on MBPP and tested on HumanEval.\\\", \\\"completed_at\\\": \\\"2026-05-22T19:25:37.503Z\\\"}, \\\"nomarker_cross_he2mbpp_exception_only\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T13:35:34.065Z\\\", \\\"updated_at\\\": \\\"2026-05-22T17:33:57.115Z\\\", \\\"hypothesis\\\": \\\"Exception_only_nomarker model (trained on HumanEval without pass/fail markers) transfers to MBPP with minimal accuracy loss, demonstrating that marker-free SFT still learns transferable code reasoning patterns. This strengthens the anti-tautology defense by showing cross-dataset generalization does not depend on explicit verdict markers.\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition cross_he2mbpp_exception_only_nomarker --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --gpu 0 --gradient_checkpointing --seed 42\\\\\\\"\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\\\", \\\"data_count\\\": 1640, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"cross_he2mbpp_nomarker_test_4270\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.955, \\\"accuracy_ci_lower\\\": 0.948, \\\"accuracy_ci_upper\\\": 0.961, \\\"pass_precision\\\": 0.99, \\\"pass_recall\\\": 0.94, \\\"pass_f1\\\": 0.97, \\\"fail_precision\\\": 0.88, \\\"fail_recall\\\": 0.99, \\\"fail_f1\\\": 0.93, \\\"majority_baseline\\\": 0.69, \\\"lift\\\": 0.264, \\\"n_test\\\": 4270}, \\\"completed_at\\\": \\\"2026-05-22T17:33:57.116Z\\\"}, \\\"gradient_masking_qwen7b_seed456\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T13:35:12.813Z\\\", \\\"updated_at\\\": \\\"2026-05-22T16:58:23.973Z\\\", \\\"hypothesis\\\": \\\"Replication of gradient masking ablation with seed=456 to establish statistical robustness. Random masking of 99.8% token gradients on exception_only data should reproduce seed42 (98.99%) and seed123 results, confirming that gradient dilution accounts for only ~1pp degradation while content quality explains ~95% of full_trace's poor performance.\\\", \\\"parent\\\": \\\"gradient_masking_qwen7b_seed42\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 456 --wandb_project trace-verdict-study --wandb_run_name gradient_masking_qwen7b_seed456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456\\\\\\\"\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data/humaneval_trainset.jsonl\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 456, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"humaneval_testset_1190\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.9933, \\\"pass_f1\\\": 0.9953, \\\"fail_f1\\\": 0.9883, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 0.9906, \\\"fail_precision\\\": 0.9769, \\\"fail_recall\\\": 1, \\\"n_test\\\": 1190, \\\"gradient_mask_ratio\\\": 0.998}, \\\"completed_at\\\": \\\"2026-05-22T16:58:23.973Z\\\"}, \\\"exc_message_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:32:37.876Z\\\", \\\"updated_at\\\": \\\"2026-05-22T13:33:24.076Z\\\", \\\"hypothesis\\\": \\\"Exception message text alone (without type or stacktrace) carries natural language description of the error. Tests whether the semantic content of the error message is sufficient for verdict classification, or whether structural context (stacktrace) is also needed.\\\", \\\"parent\\\": \\\"vota_exception_only_seed42_v2\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exc_message_only --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42 --gpu 0 --seed 42 --gradient_checkpointing --wandb_project trace-verdict-study --wandb_run_name exc_message_only_seed42\\\\\\\"\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen/Qwen2.5-7B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"trained_from_scratch\\\", \\\"eval_data\\\": \\\"humaneval_testset_1190\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.995, \\\"pass_f1\\\": 0.9965, \\\"fail_f1\\\": 0.9912, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 0.9929, \\\"fail_precision\\\": 0.9826, \\\"fail_recall\\\": 1, \\\"n_test\\\": 1190, \\\"eval_loss\\\": 0.58, \\\"train_loss\\\": 0.1828}, \\\"completed_at\\\": \\\"2026-05-22T13:33:24.076Z\\\"}, \\\"gradient_masking_qwen7b_seed123\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T12:33:00.898Z\\\", \\\"updated_at\\\": \\\"2026-05-22T12:33:07.778Z\\\", \\\"hypothesis\\\": \\\"Seed robustness check for gradient masking ablation. If seed123 also shows ~99% accuracy with 99.8% gradient masking, confirms that content quality (not gradient distribution) is the dominant factor across random initializations.\\\", \\\"parent\\\": \\\"gradient_masking_qwen7b_seed42\\\"}, \\\"exc_type_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:52:35.048Z\\\", \\\"updated_at\\\": \\\"2026-05-22T10:52:53.082Z\\\", \\\"hypothesis\\\": \\\"Exception type alone (e.g. 'ValueError') without message or stacktrace retains most of exception_only's diagnostic power, since the error type is the primary signal for verdict classification.\\\", \\\"parent\\\": \\\"vota_exception_only_seed42_v2\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 1, \\\"pass_f1\\\": 1, \\\"fail_f1\\\": 1, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 1, \\\"fail_precision\\\": 1, \\\"fail_recall\\\": 1, \\\"majority_baseline\\\": 0.7151, \\\"lift\\\": 0.2849, \\\"n_test\\\": 1190}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42/\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42.log\\\", \\\"command\\\": \\\"python train/train_sft.py --condition exc_type_only --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ --gpu 0 --seed 42\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/\\\", \\\"data_count\\\": 4720, \\\"model_name\\\": \\\"Qwen2.5-Coder-7B-Instruct\\\", \\\"seed\\\": 42}, \\\"completed_at\\\": \\\"2026-05-22T10:52:53.082Z\\\"}, \\\"exc_stacktrace_only_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T10:32:37.400Z\\\", \\\"updated_at\\\": \\\"2026-05-22T10:32:43.923Z\\\", \\\"hypothesis\\\": \\\"Exception stacktrace (line numbers + local variable context without error type/message) provides structural execution path information. If accuracy is high, structural context alone is sufficient for verdict classification; if low, the error type/message carries the primary signal.\\\", \\\"parent\\\": \\\"vota_exception_only_seed42_v2\\\"}, \\\"gradient_masking_qwen7b_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-22T07:44:29.302Z\\\", \\\"updated_at\\\": \\\"2026-05-22T09:50:37.759Z\\\", \\\"hypothesis\\\": \\\"If gradient dilution is the primary cause of full_trace degradation, masking exception_only gradients to full_trace's sparsity level (~0.2% label tokens) should degrade performance significantly. If performance stays at exception_only level (~99%), content quality (not gradient distribution) is the dominant factor.\\\", \\\"parent\\\": \\\"full_trace_label_only_seed42\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.9899, \\\"accuracy_ci_lower\\\": 0.984, \\\"accuracy_ci_upper\\\": 0.995, \\\"majority_baseline\\\": 0.7151, \\\"lift\\\": 0.275, \\\"pass_f1\\\": 0.993, \\\"fail_f1\\\": 0.982, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 0.99, \\\"fail_precision\\\": 0.98, \\\"fail_recall\\\": 0.99, \\\"n_test\\\": 1190, \\\"gradient_mask_ratio\\\": 0.998, \\\"eval_loss\\\": 0.0533}, \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42/final\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42.log\\\", \\\"command\\\": \\\"python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data/\\\", \\\"data_count\\\": 4720, \\\"model_name\\\": \\\"Qwen2.5-Coder-7B-Instruct\\\", \\\"seed\\\": 42}, \\\"completed_at\\\": \\\"2026-05-22T09:50:37.760Z\\\"}, \\\"deepseek_ae_only_seed123\\\": {\\\"status\\\": \\\"ALLOCATED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:46:24.864Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:30:43.575Z\\\", \\\"hypothesis\\\": \\\"DeepSeek ae_only seed123 应在 98-100%（与 seed42=98.74% 接近），确认 Tier 1 ae_only 最低值是 DeepSeek 的自然水平而非 seed anomaly\\\", \\\"parent\\\": \\\"deepseek_ae_only_seed42\\\"}, \\\"codellama13b_vota_seed123\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T07:35:09.665Z\\\", \\\"updated_at\\\": \\\"2026-05-20T13:30:36.364Z\\\", \\\"hypothesis\\\": \\\"CodeLlama-13B VOTA seed123 应在 97-100%（与 seed42=98.57% 接近），验证 VOTA Tier 1 跨 seed 稳定性，补强 C4 universality claim\\\", \\\"parent\\\": \\\"codellama13b_vota_seed42\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed123/final\\\", \\\"log_path\\\": \\\"~/runs/trace-verdict-study/codellama13b_vota_seed123.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.9891}, \\\"completed_at\\\": \\\"2026-05-20T13:30:36.364Z\\\"}, \\\"qwen15b_exception_only_seed123\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T12:56:13.468Z\\\", \\\"updated_at\\\": \\\"2026-05-20T12:56:25.490Z\\\", \\\"hypothesis\\\": \\\"Qwen-1.5B exception_only seed123 应在 99-100%（与 seed42=99.83% 接近），强化 C1 exception dominance 全模型全 seed ≥99.33% claim\\\", \\\"parent\\\": \\\"qwen15b_exception_only_seed42\\\"}, \\\"qwen15b_loop_only_seed123\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:35:15.163Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:54:28.603Z\\\", \\\"hypothesis\\\": \\\"Qwen-1.5B loop_only seed123 应在 75-82%（与 seed42=78.32% 接近），验证 1.5B Tier 2 跨 seed 稳定性 + 强化 D106 architecture-level 证据\\\", \\\"parent\\\": \\\"qwen15b_loop_only_seed42\\\"}, \\\"qwen1.5b_full_trace_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:04:16.238Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:04:16.238Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"codellama_vota_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:04:12.939Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:04:12.939Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"codellama_no_trace_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:04:12.025Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:04:12.025Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"codellama_exception_only_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T11:04:11.572Z\\\", \\\"updated_at\\\": \\\"2026-05-20T11:04:11.572Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen1.5b_vota_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:44:08.643Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:44:08.643Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen1.5b_no_trace_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:44:07.835Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:44:07.835Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen1.5b_exception_only_seed42\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T10:44:07.214Z\\\", \\\"updated_at\\\": \\\"2026-05-20T10:44:07.214Z\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"qwen15b_loop_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T07:51:01.070Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:19:55.564Z\\\", \\\"hypothesis\\\": \\\"Qwen-1.5B loop_only 预期在 70-85% 范围，可能低于 7B (86.05%) 因 1.5B capacity 不足以从低密度 loop 信号中提取判别信息。填补 4-model Tier 2 矩阵\\\", \\\"parent\\\": \\\"qwen15b_full_trace_seed42\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42/final\\\", \\\"log_path\\\": \\\"~/runs/trace-verdict-study/qwen15b_loop_only_seed42.log\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.7832, \\\"pass_f1\\\": 0.853, \\\"fail_f1\\\": 0.59}, \\\"completed_at\\\": \\\"2026-05-20T09:19:55.564Z\\\"}, \\\"codellama13b_loop_only_seed456\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T09:02:46.071Z\\\", \\\"updated_at\\\": \\\"2026-05-20T09:02:50.992Z\\\", \\\"hypothesis\\\": \\\"CodeLlama-13B loop_only seed456 应在 74-80%（与 seed42=77.06%, seed123=76.05% 接近），确认 Tier 2 在 CodeLlama 上 near-zero lift 是 seed-robust 的\\\", \\\"parent\\\": \\\"codellama13b_loop_only_seed42\\\"}, \\\"qwen15b_ae_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-20T07:49:47.717Z\\\", \\\"updated_at\\\": \\\"2026-05-20T07:50:19.670Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.9908, \\\"accuracy_ci_lower\\\": 0.9849, \\\"accuracy_ci_upper\\\": 0.9958, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 0.9871, \\\"pass_f1\\\": 0.9935, \\\"fail_precision\\\": 0.9686, \\\"fail_recall\\\": 1, \\\"fail_f1\\\": 0.984, \\\"majority_baseline\\\": 0.7151, \\\"lift\\\": 0.2756, \\\"eval_loss\\\": 0.1973, \\\"train_loss\\\": 0.0702, \\\"n\\\": 1190}, \\\"spec\\\": {\\\"command\\\": \\\"train + eval ae_only condition\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen2.5-Coder-1.5B-Instruct\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final\\\", \\\"log_path\\\": \\\"~/runs/trace-verdict-study/qwen15b_ae_only_seed42.log\\\"}, \\\"hypothesis\\\": \\\"Assertion-error-only traces provide sufficient signal for a 1.5B parameter model to learn pass/fail classification at ≥95% accuracy, consistent with larger models (7B/13B), because the assertion error pattern is a strong binary discriminator regardless of model capacity.\\\", \\\"parent\\\": \\\"qwen15b_exception_only_seed42\\\", \\\"completed_at\\\": \\\"2026-05-20T07:50:19.670Z\\\"}, \\\"codellama13b_exception_only_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T14:25:08.019Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:57:17.305Z\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/trace-verdict-study/outputs/codellama13b_exception_only_seed42/\\\", \\\"log_path\\\": \\\"/root/trace-verdict-study/outputs/codellama13b_exception_only_seed42/eval_results.json\\\"}, \\\"hypothesis\\\": \\\"CodeLlama-13B exception_only should achieve ≥99% accuracy, confirming minimal sufficient signal universality across 13B-scale models\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 99.83}, \\\"completed_at\\\": \\\"2026-05-20T06:57:17.305Z\\\"}, \\\"codellama13b_vota_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T14:25:08.369Z\\\", \\\"updated_at\\\": \\\"2026-05-20T06:57:16.777Z\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/trace-verdict-study/outputs/codellama13b_vota_seed42/\\\", \\\"log_path\\\": \\\"/root/trace-verdict-study/outputs/codellama13b_vota_seed42/eval_results.json\\\"}, \\\"hypothesis\\\": \\\"CodeLlama-13B VOTA should achieve ≥95% accuracy, confirming VOTA tier 1 universality across model architectures\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"accuracy\\\": 98.57}, \\\"completed_at\\\": \\\"2026-05-20T06:57:16.777Z\\\"}, \\\"qwen7b_full_trace_dynamics_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T06:40:56.724Z\\\", \\\"updated_at\\\": \\\"2026-05-19T06:41:32.669Z\\\", \\\"metrics\\\": {\\\"final_accuracy\\\": 0.8824, \\\"best_accuracy\\\": 0.8882, \\\"best_accuracy_step\\\": 350, \\\"step50_accuracy\\\": 0.8739, \\\"step100_accuracy\\\": 0.821, \\\"step200_accuracy\\\": 0.884, \\\"step444_accuracy\\\": 0.8824, \\\"final_train_loss\\\": 0.0085, \\\"best_pass_f1\\\": 0.9252, \\\"best_fail_f1\\\": 0.781, \\\"accuracy_gap_vs_exception_only\\\": -11.01}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/\\\", \\\"log_path\\\": \\\"~/runs/trace-verdict-study/qwen7b_full_trace_dynamics_seed42.log\\\", \\\"hypothesis\\\": \\\"Full trace with label_only_loss converges slower than exception_only because verbose execution traces dilute effective signal density, forcing the model to attend to irrelevant context and degrading gradient quality for verdict prediction.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_dynamics.sh qwen7b_full_trace_dynamics_seed42\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data/\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen2.5-Coder-7B-Instruct\\\", \\\"seed\\\": 42}, \\\"completed_at\\\": \\\"2026-05-19T06:41:32.669Z\\\"}, \\\"qwen15b_exception_only_seed123_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T23:48:18.227Z\\\", \\\"updated_at\\\": \\\"2026-05-18T23:49:05.454Z\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.9983, \\\"accuracy_ci_lower\\\": 0.9958, \\\"accuracy_ci_upper\\\": 1, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 0.9976, \\\"pass_f1\\\": 0.9988, \\\"fail_precision\\\": 0.9941, \\\"fail_recall\\\": 1, \\\"fail_f1\\\": 0.9971, \\\"n_test\\\": 1190}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123_v2/final\\\", \\\"log_path\\\": \\\"/root/runs/trace-verdict-study/qwen15b_exception_only_seed123_v2.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"train+eval qwen1.5b exception_only seed123 v2\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen2.5-Coder-1.5B-Instruct\\\", \\\"seed\\\": 123}, \\\"hypothesis\\\": \\\"Qwen2.5-Coder-1.5B fine-tuned on exception-only traces can distinguish pass/fail test verdicts with high accuracy, because exception messages carry sufficient signal for verdict prediction even without full execution traces.\\\", \\\"completed_at\\\": \\\"2026-05-18T23:49:05.454Z\\\"}, \\\"deepseek_full_trace_seed42_v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-16T02:24:57.697Z\\\", \\\"updated_at\\\": \\\"2026-05-16T02:24:57.698Z\\\", \\\"notes\\\": \\\"DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with max_length=2048 (matches training). eval_results.json has stale 28.49% from max_length=16384 run; correct value in eval_results_maxlen2048.json. predictions.jsonl overwritten 2026-05-16 with maxlen2048 results (reliable). Systematic audit 2026-05-16 confirmed: adapter base_model=DeepSeek, no model mixup possible (dimension mismatch would crash).\\\"}, \\\"vota_seed456_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-15T20:52:29.262Z\\\", \\\"updated_at\\\": \\\"2026-05-15T20:53:03.185Z\\\", \\\"metrics\\\": {\\\"accuracy\\\": 0.9908, \\\"accuracy_ci_lower\\\": 0.9849, \\\"accuracy_ci_upper\\\": 0.9958, \\\"pass_precision\\\": 1, \\\"pass_recall\\\": 0.9871, \\\"pass_f1\\\": 0.9935, \\\"fail_precision\\\": 0.9686, \\\"fail_recall\\\": 1, \\\"fail_f1\\\": 0.984, \\\"eval_loss\\\": 0.081, \\\"train_loss\\\": 0.0498, \\\"n_test\\\": 1190}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final\\\", \\\"log_path\\\": \\\"/root/runs/trace-verdict-study/vota_seed456.log\\\", \\\"conclusion\\\": \\\"success\\\", \\\"spec\\\": {\\\"command\\\": \\\"train+eval vota seed456 with gradient_checkpointing\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/trace-verdict-study/data\\\", \\\"data_count\\\": 1190, \\\"model_name\\\": \\\"Qwen2.5-Coder-7B-Instruct\\\", \\\"seed\\\": 456}, \\\"completed_at\\\": \\\"2026-05-15T20:53:03.185Z\\\"}, \\\"medium_random50_seed42\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-14T01:51:02.394Z\\\", \\\"updated_at\\\": \\\"2026-05-14T01:51:35.564Z\\\", \\\"metrics\\\": {\\\"gen0\\\": {\\\"ppl\\\": 26.12, \\\"rankme\\\": 361.63, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0346, \\\"corr\\\": 0.0101}, \\\"gen1\\\": {\\\"ppl\\\": 32.57, \\\"rankme\\\": 387.8, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0277, \\\"corr\\\": 0.0331}, \\\"gen2\\\": {\\\"ppl\\\": 41.58, \\\"rankme\\\": 410.08, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0214, \\\"corr\\\": 0.0088}, \\\"gen3\\\": {\\\"ppl\\\": 49.87, \\\"rankme\\\": 421.67, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0182, \\\"corr\\\": -0.0018}, \\\"gen4\\\": {\\\"ppl\\\": 59.83, \\\"rankme\\\": 427.23, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0161, \\\"corr\\\": -0.0014}, \\\"gen5\\\": {\\\"ppl\\\": 60.62, \\\"rankme\\\": 426.16, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0144, \\\"corr\\\": -0.0004}, \\\"gen6\\\": {\\\"ppl\\\": 68.34, \\\"rankme\\\": 427.19, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0134, \\\"corr\\\": -0.0071}, \\\"gen7\\\": {\\\"ppl\\\": 70.25, \\\"rankme\\\": 426.5, \\\"knn\\\": 0.988, \\\"rare\\\": 0.0128, \\\"corr\\\": -0.0034}}, \\\"conclusion\\\": \\\"success\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/div_cal_verify/results_medium_random50/random_50/gen_7\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/div_cal_verify/medium_random50.log\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash run_medium_random50.sh\\\", \\\"server\\\": \\\"westd-11235\\\", \\\"data_path\\\": \\\"/root/autodl-tmp/div_cal_verify/\\\", \\\"data_count\\\": 977, \\\"model_name\\\": \\\"gpt2-medium\\\", \\\"seed\\\": 42}, \\\"completed_at\\\": \\\"2026-05-14T01:51:35.564Z\\\"}}, \\\"count\\\": 36, \\\"total\\\": 36, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.0456}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"no_trace_seed123\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:16:15.921Z\", \"updated_at\": \"2026-05-22T23:42:31.000Z\", \"hypothesis\": \"Replication of no_trace baseline with seed=123 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\", \"spec\": {\"command\": \"bash -c \\\"... python train/train_sft.py --condition no_trace --gpu 0 --gradient_checkpointing --seed 123\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/humaneval_trainset.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\"}}, \"no_trace_seed456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:16:16.072Z\", \"updated_at\": \"2026-05-22T23:16:26.102Z\", \"hypothesis\": \"Replication of no_trace baseline with seed=456 to establish multi-seed statistics. Without execution traces, SFT should produce accuracy around 75% (matching seed42's result), confirming the no_trace baseline is stable across seeds.\"}, \"attention_gradient_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:26:08.040Z\", \"updated_at\": \"2026-05-22T19:26:34.240Z\", \"hypothesis\": \"In full_trace models, execution trace tokens dominate input but receive disproportionately low attention and gradient signal at verdict position, demonstrating gradient dilution where non-diagnostic tokens dilute learning signal away from diagnostic content.\", \"spec\": {\"command\": \"attention gradient analysis script\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"exception_only_seed42\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/attention_gradient_analysis/\", \"log_path\": \"N/A (analysis script)\"}, \"conclusion\": \"success\", \"metrics\": {\"analysis_files_produced\": 10, \"analysis_type\": \"attention_gradient\"}, \"completed_at\": \"2026-05-22T19:26:34.240Z\"}, \"gradient_masking_qwen7b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:26:03.894Z\", \"updated_at\": \"2026-05-22T19:26:07.917Z\", \"conclusion\": \"killed\"}, \"exc_type_only\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:25:59.333Z\", \"updated_at\": \"2026-05-22T19:26:03.358Z\", \"conclusion\": \"killed\"}, \"cross_dataset_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:25:00.707Z\", \"updated_at\": \"2026-05-22T19:25:54.359Z\", \"spec\": {\"command\": \"cross-dataset batch runner\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"cross_dataset_eval\", \"checkpoint_path\": \"N/A (batch runner)\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\"}, \"hypothesis\": \"Batch runner for cross-dataset generalization experiments: trains models on one dataset and evaluates on another to test whether trace-based SFT learns transferable reasoning patterns rather than dataset-specific shortcuts.\", \"conclusion\": \"success\", \"metrics\": {\"sub_experiments_completed\": 4, \"all_success\": true}, \"completed_at\": \"2026-05-22T19:25:54.360Z\"}, \"cross_mbpp2he_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:52:56.834Z\", \"updated_at\": \"2026-05-22T19:25:38.928Z\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"pass_f1\": 1, \"fail_f1\": 1, \"n_test\": 1190}, \"spec\": {\"command\": \"cross-dataset batch\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_exception_only/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\"}, \"hypothesis\": \"Cross-dataset generalization MBPP→HE with exception_only: exception trace SFT learns transferable code reasoning patterns that generalize across datasets, predicting smaller accuracy drop compared to no_trace baseline when trained on MBPP and tested on HumanEval.\", \"completed_at\": \"2026-05-22T19:25:38.928Z\"}, \"cross_mbpp2he_no_trace_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:52:58.755Z\", \"updated_at\": \"2026-05-22T19:25:37.503Z\", \"conclusion\": \"negative\", \"metrics\": {\"accuracy\": 0.6799, \"pass_f1\": 0.7363, \"fail_f1\": 0.5927, \"n_test\": 1190}, \"spec\": {\"command\": \"cross-dataset batch\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_no_trace/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log\"}, \"hypothesis\": \"Cross-dataset generalization MBPP→HE with no_trace baseline: without execution traces, SFT relies on dataset-specific code patterns that do not transfer well across datasets, predicting larger accuracy drop when trained on MBPP and tested on HumanEval.\", \"completed_at\": \"2026-05-22T19:25:37.503Z\"}, \"nomarker_cross_he2mbpp_exception_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:35:34.065Z\", \"updated_at\": \"2026-05-22T17:33:57.115Z\", \"hypothesis\": \"Exception_only_nomarker model (trained on HumanEval without pass/fail markers) transfers to MBPP with minimal accuracy loss, demonstrating that marker-free SFT still learns transferable code reasoning patterns. This strengthens the anti-tautology defense by showing cross-dataset generalization does not depend on explicit verdict markers.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition cross_he2mbpp_exception_only_nomarker --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --gpu 0 --gradient_checkpointing --seed 42\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/cross_dataset/\", \"data_count\": 1640, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"cross_he2mbpp_nomarker_test_4270\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.955, \"accuracy_ci_lower\": 0.948, \"accuracy_ci_upper\": 0.961, \"pass_precision\": 0.99, \"pass_recall\": 0.94, \"pass_f1\": 0.97, \"fail_precision\": 0.88, \"fail_recall\": 0.99, \"fail_f1\": 0.93, \"majority_baseline\": 0.69, \"lift\": 0.264, \"n_test\": 4270}, \"completed_at\": \"2026-05-22T17:33:57.116Z\"}, \"gradient_masking_qwen7b_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T13:35:12.813Z\", \"updated_at\": \"2026-05-22T16:58:23.973Z\", \"hypothesis\": \"Replication of gradient masking ablation with seed=456 to establish statistical robustness. Random masking of 99.8% token gradients on exception_only data should reproduce seed42 (98.99%) and seed123 results, confirming that gradient dilution accounts for only ~1pp degradation while content quality explains ~95% of full_trace's poor performance.\", \"parent\": \"gradient_masking_qwen7b_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 456 --wandb_project trace-verdict-study --wandb_run_name gradient_masking_qwen7b_seed456 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/humaneval_trainset.jsonl\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed456.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9933, \"pass_f1\": 0.9953, \"fail_f1\": 0.9883, \"pass_precision\": 1, \"pass_recall\": 0.9906, \"fail_precision\": 0.9769, \"fail_recall\": 1, \"n_test\": 1190, \"gradient_mask_ratio\": 0.998}, \"completed_at\": \"2026-05-22T16:58:23.973Z\"}, \"exc_message_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:32:37.876Z\", \"updated_at\": \"2026-05-22T13:33:24.076Z\", \"hypothesis\": \"Exception message text alone (without type or stacktrace) carries natural language description of the error. Tests whether the semantic content of the error message is sufficient for verdict classification, or whether structural context (stacktrace) is also needed.\", \"parent\": \"vota_exception_only_seed42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition exc_message_only --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42 --gpu 0 --seed 42 --gradient_checkpointing --wandb_project trace-verdict-study --wandb_run_name exc_message_only_seed42\\\"\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/\", \"data_count\": 1190, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"trained_from_scratch\", \"eval_data\": \"humaneval_testset_1190\", \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_message_only_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.995, \"pass_f1\": 0.9965, \"fail_f1\": 0.9912, \"pass_precision\": 1, \"pass_recall\": 0.9929, \"fail_precision\": 0.9826, \"fail_recall\": 1, \"n_test\": 1190, \"eval_loss\": 0.58, \"train_loss\": 0.1828}, \"completed_at\": \"2026-05-22T13:33:24.076Z\"}, \"gradient_masking_qwen7b_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:33:00.898Z\", \"updated_at\": \"2026-05-22T12:33:07.778Z\", \"hypothesis\": \"Seed robustness check for gradient masking ablation. If seed123 also shows ~99% accuracy with 99.8% gradient masking, confirms that content quality (not gradient distribution) is the dominant factor across random initializations.\", \"parent\": \"gradient_masking_qwen7b_seed42\"}, \"exc_type_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:52:35.048Z\", \"updated_at\": \"2026-05-22T10:52:53.082Z\", \"hypothesis\": \"Exception type alone (e.g. 'ValueError') without message or stacktrace retains most of exception_only's diagnostic power, since the error type is the primary signal for verdict classification.\", \"parent\": \"vota_exception_only_seed42_v2\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1, \"pass_f1\": 1, \"fail_f1\": 1, \"pass_precision\": 1, \"pass_recall\": 1, \"fail_precision\": 1, \"fail_recall\": 1, \"majority_baseline\": 0.7151, \"lift\": 0.2849, \"n_test\": 1190}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42/\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42.log\", \"command\": \"python train/train_sft.py --condition exc_type_only --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ --gpu 0 --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"completed_at\": \"2026-05-22T10:52:53.082Z\"}, \"exc_stacktrace_only_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:32:37.400Z\", \"updated_at\": \"2026-05-22T10:32:43.923Z\", \"hypothesis\": \"Exception stacktrace (line numbers + local variable context without error type/message) provides structural execution path information. If accuracy is high, structural context alone is sufficient for verdict classification; if low, the error type/message carries the primary signal.\", \"parent\": \"vota_exception_only_seed42_v2\"}, \"gradient_masking_qwen7b_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:44:29.302Z\", \"updated_at\": \"2026-05-22T09:50:37.759Z\", \"hypothesis\": \"If gradient dilution is the primary cause of full_trace degradation, masking exception_only gradients to full_trace's sparsity level (~0.2% label tokens) should degrade performance significantly. If performance stays at exception_only level (~99%), content quality (not gradient distribution) is the dominant factor.\", \"parent\": \"full_trace_label_only_seed42\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9899, \"accuracy_ci_lower\": 0.984, \"accuracy_ci_upper\": 0.995, \"majority_baseline\": 0.7151, \"lift\": 0.275, \"pass_f1\": 0.993, \"fail_f1\": 0.982, \"pass_precision\": 1, \"pass_recall\": 0.99, \"fail_precision\": 0.98, \"fail_recall\": 0.99, \"n_test\": 1190, \"gradient_mask_ratio\": 0.998, \"eval_loss\": 0.0533}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42/final\", \"log_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42.log\", \"command\": \"python train/train_sft.py --condition exception_only --gpu 0 --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 4720, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"completed_at\": \"2026-05-22T09:50:37.760Z\"}, \"deepseek_ae_only_seed123\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:46:24.864Z\", \"updated_at\": \"2026-05-20T13:30:43.575Z\", \"hypothesis\": \"DeepSeek ae_only seed123 应在 98-100%（与 seed42=98.74% 接近），确认 Tier 1 ae_only 最低值是 DeepSeek 的自然水平而非 seed anomaly\", \"parent\": \"deepseek_ae_only_seed42\"}, \"codellama13b_vota_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:35:09.665Z\", \"updated_at\": \"2026-05-20T13:30:36.364Z\", \"hypothesis\": \"CodeLlama-13B VOTA seed123 应在 97-100%（与 seed42=98.57% 接近），验证 VOTA Tier 1 跨 seed 稳定性，补强 C4 universality claim\", \"parent\": \"codellama13b_vota_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_vota_seed123/final\", \"log_path\": \"~/runs/trace-verdict-study/codellama13b_vota_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9891}, \"completed_at\": \"2026-05-20T13:30:36.364Z\"}, \"qwen15b_exception_only_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:56:13.468Z\", \"updated_at\": \"2026-05-20T12:56:25.490Z\", \"hypothesis\": \"Qwen-1.5B exception_only seed123 应在 99-100%（与 seed42=99.83% 接近），强化 C1 exception dominance 全模型全 seed ≥99.33% claim\", \"parent\": \"qwen15b_exception_only_seed42\"}, \"qwen15b_loop_only_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:35:15.163Z\", \"updated_at\": \"2026-05-20T11:54:28.603Z\", \"hypothesis\": \"Qwen-1.5B loop_only seed123 应在 75-82%（与 seed42=78.32% 接近），验证 1.5B Tier 2 跨 seed 稳定性 + 强化 D106 architecture-level 证据\", \"parent\": \"qwen15b_loop_only_seed42\"}, \"qwen1.5b_full_trace_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:16.238Z\", \"updated_at\": \"2026-05-20T11:04:16.238Z\", \"conclusion\": \"killed\"}, \"codellama_vota_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:12.939Z\", \"updated_at\": \"2026-05-20T11:04:12.939Z\", \"conclusion\": \"killed\"}, \"codellama_no_trace_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:12.025Z\", \"updated_at\": \"2026-05-20T11:04:12.025Z\", \"conclusion\": \"killed\"}, \"codellama_exception_only_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:04:11.572Z\", \"updated_at\": \"2026-05-20T11:04:11.572Z\", \"conclusion\": \"killed\"}, \"qwen1.5b_vota_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:08.643Z\", \"updated_at\": \"2026-05-20T10:44:08.643Z\", \"conclusion\": \"killed\"}, \"qwen1.5b_no_trace_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:07.835Z\", \"updated_at\": \"2026-05-20T10:44:07.835Z\", \"conclusion\": \"killed\"}, \"qwen1.5b_exception_only_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:44:07.214Z\", \"updated_at\": \"2026-05-20T10:44:07.214Z\", \"conclusion\": \"killed\"}, \"qwen15b_loop_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:51:01.070Z\", \"updated_at\": \"2026-05-20T09:19:55.564Z\", \"hypothesis\": \"Qwen-1.5B loop_only 预期在 70-85% 范围，可能低于 7B (86.05%) 因 1.5B capacity 不足以从低密度 loop 信号中提取判别信息。填补 4-model Tier 2 矩阵\", \"parent\": \"qwen15b_full_trace_seed42\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_loop_only_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_loop_only_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.7832, \"pass_f1\": 0.853, \"fail_f1\": 0.59}, \"completed_at\": \"2026-05-20T09:19:55.564Z\"}, \"codellama13b_loop_only_seed456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:02:46.071Z\", \"updated_at\": \"2026-05-20T09:02:50.992Z\", \"hypothesis\": \"CodeLlama-13B loop_only seed456 应在 74-80%（与 seed42=77.06%, seed123=76.05% 接近），确认 Tier 2 在 CodeLlama 上 near-zero lift 是 seed-robust 的\", \"parent\": \"codellama13b_loop_only_seed42\"}, \"qwen15b_ae_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:49:47.717Z\", \"updated_at\": \"2026-05-20T07:50:19.670Z\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"pass_precision\": 1, \"pass_recall\": 0.9871, \"pass_f1\": 0.9935, \"fail_precision\": 0.9686, \"fail_recall\": 1, \"fail_f1\": 0.984, \"majority_baseline\": 0.7151, \"lift\": 0.2756, \"eval_loss\": 0.1973, \"train_loss\": 0.0702, \"n\": 1190}, \"spec\": {\"command\": \"train + eval ae_only condition\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_ae_only_seed42/final\", \"log_path\": \"~/runs/trace-verdict-study/qwen15b_ae_only_seed42.log\"}, \"hypothesis\": \"Assertion-error-only traces provide sufficient signal for a 1.5B parameter model to learn pass/fail classification at ≥95% accuracy, consistent with larger models (7B/13B), because the assertion error pattern is a strong binary discriminator regardless of model capacity.\", \"parent\": \"qwen15b_exception_only_seed42\", \"completed_at\": \"2026-05-20T07:50:19.670Z\"}, \"codellama13b_exception_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:25:08.019Z\", \"updated_at\": \"2026-05-20T06:57:17.305Z\", \"spec\": {\"checkpoint_path\": \"/root/trace-verdict-study/outputs/codellama13b_exception_only_seed42/\", \"log_path\": \"/root/trace-verdict-study/outputs/codellama13b_exception_only_seed42/eval_results.json\"}, \"hypothesis\": \"CodeLlama-13B exception_only should achieve ≥99% accuracy, confirming minimal sufficient signal universality across 13B-scale models\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 99.83}, \"completed_at\": \"2026-05-20T06:57:17.305Z\"}, \"codellama13b_vota_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:25:08.369Z\", \"updated_at\": \"2026-05-20T06:57:16.777Z\", \"spec\": {\"checkpoint_path\": \"/root/trace-verdict-study/outputs/codellama13b_vota_seed42/\", \"log_path\": \"/root/trace-verdict-study/outputs/codellama13b_vota_seed42/eval_results.json\"}, \"hypothesis\": \"CodeLlama-13B VOTA should achieve ≥95% accuracy, confirming VOTA tier 1 universality across model architectures\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 98.57}, \"completed_at\": \"2026-05-20T06:57:16.777Z\"}, \"qwen7b_full_trace_dynamics_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:40:56.724Z\", \"updated_at\": \"2026-05-19T06:41:32.669Z\", \"metrics\": {\"final_accuracy\": 0.8824, \"best_accuracy\": 0.8882, \"best_accuracy_step\": 350, \"step50_accuracy\": 0.8739, \"step100_accuracy\": 0.821, \"step200_accuracy\": 0.884, \"step444_accuracy\": 0.8824, \"final_train_loss\": 0.0085, \"best_pass_f1\": 0.9252, \"best_fail_f1\": 0.781, \"accuracy_gap_vs_exception_only\": -11.01}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/\", \"log_path\": \"~/runs/trace-verdict-study/qwen7b_full_trace_dynamics_seed42.log\", \"hypothesis\": \"Full trace with label_only_loss converges slower than exception_only because verbose execution traces dilute effective signal density, forcing the model to attend to irrelevant context and degrading gradient quality for verdict prediction.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"bash run_dynamics.sh qwen7b_full_trace_dynamics_seed42\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data/\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 42}, \"completed_at\": \"2026-05-19T06:41:32.669Z\"}, \"qwen15b_exception_only_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:48:18.227Z\", \"updated_at\": \"2026-05-18T23:49:05.454Z\", \"metrics\": {\"accuracy\": 0.9983, \"accuracy_ci_lower\": 0.9958, \"accuracy_ci_upper\": 1, \"pass_precision\": 1, \"pass_recall\": 0.9976, \"pass_f1\": 0.9988, \"fail_precision\": 0.9941, \"fail_recall\": 1, \"fail_f1\": 0.9971, \"n_test\": 1190}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed123_v2/final\", \"log_path\": \"/root/runs/trace-verdict-study/qwen15b_exception_only_seed123_v2.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"train+eval qwen1.5b exception_only seed123 v2\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-1.5B-Instruct\", \"seed\": 123}, \"hypothesis\": \"Qwen2.5-Coder-1.5B fine-tuned on exception-only traces can distinguish pass/fail test verdicts with high accuracy, because exception messages carry sufficient signal for verdict prediction even without full execution traces.\", \"completed_at\": \"2026-05-18T23:49:05.454Z\"}, \"deepseek_full_trace_seed42_v3\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:24:57.697Z\", \"updated_at\": \"2026-05-16T02:24:57.698Z\", \"notes\": \"DeepSeek full_trace v3: label-preserving truncation fix. 79.16% confirmed with max_length=2048 (matches training). eval_results.json has stale 28.49% from max_length=16384 run; correct value in eval_results_maxlen2048.json. predictions.jsonl overwritten 2026-05-16 with maxlen2048 results (reliable). Systematic audit 2026-05-16 confirmed: adapter base_model=DeepSeek, no model mixup possible (dimension mismatch would crash).\"}, \"vota_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:52:29.262Z\", \"updated_at\": \"2026-05-15T20:53:03.185Z\", \"metrics\": {\"accuracy\": 0.9908, \"accuracy_ci_lower\": 0.9849, \"accuracy_ci_upper\": 0.9958, \"pass_precision\": 1, \"pass_recall\": 0.9871, \"pass_f1\": 0.9935, \"fail_precision\": 0.9686, \"fail_recall\": 1, \"fail_f1\": 0.984, \"eval_loss\": 0.081, \"train_loss\": 0.0498, \"n_test\": 1190}, \"checkpoint_path\": \"/root/autodl-tmp/trace-verdict-study-checkpoints/vota_seed456/final\", \"log_path\": \"/root/runs/trace-verdict-study/vota_seed456.log\", \"conclusion\": \"success\", \"spec\": {\"command\": \"train+eval vota seed456 with gradient_checkpointing\", \"server\": \"westd-11235\", \"data_path\": \"/root/trace-verdict-study/data\", \"data_count\": 1190, \"model_name\": \"Qwen2.5-Coder-7B-Instruct\", \"seed\": 456}, \"completed_at\": \"2026-05-15T20:53:03.185Z\"}, \"medium_random50_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:51:02.394Z\", \"updated_at\": \"2026-05-14T01:51:35.564Z\", \"metrics\": {\"gen0\": {\"ppl\": 26.12, \"rankme\": 361.63, \"knn\": 0.988, \"rare\": 0.0346, \"corr\": 0.0101}, \"gen1\": {\"ppl\": 32.57, \"rankme\": 387.8, \"knn\": 0.988, \"rare\": 0.0277, \"corr\": 0.0331}, \"gen2\": {\"ppl\": 41.58, \"rankme\": 410.08, \"knn\": 0.988, \"rare\": 0.0214, \"corr\": 0.0088}, \"gen3\": {\"ppl\": 49.87, \"rankme\": 421.67, \"knn\": 0.988, \"rare\": 0.0182, \"corr\": -0.0018}, \"gen4\": {\"ppl\": 59.83, \"rankme\": 427.23, \"knn\": 0.988, \"rare\": 0.0161, \"corr\": -0.0014}, \"gen5\": {\"ppl\": 60.62, \"rankme\": 426.16, \"knn\": 0.988, \"rare\": 0.0144, \"corr\": -0.0004}, \"gen6\": {\"ppl\": 68.34, \"rankme\": 427.19, \"knn\": 0.988, \"rare\": 0.0134, \"corr\": -0.0071}, \"gen7\": {\"ppl\": 70.25, \"rankme\": 426.5, \"knn\": 0.988, \"rare\": 0.0128, \"corr\": -0.0034}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/div_cal_verify/results_medium_random50/random_50/gen_7\", \"log_path\": \"/root/autodl-tmp/div_cal_verify/medium_random50.log\", \"spec\": {\"command\": \"bash run_medium_random50.sh\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/div_cal_verify/\", \"data_count\": 977, \"model_name\": \"gpt2-medium\", \"seed\": 42}, \"completed_at\": \"2026-05-14T01:51:35.564Z\"}}, \"count\": 36, \"total\": 36, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0456}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the paper files locally. Let me read them now. The files are at:
- `docs/paper/appendix.tex`
- `docs/paper/experiments.tex`

Let me also check for more registry entries - I got 36 but might be missing some. Let me also check if there are more relevant experiments. Let me read the paper files first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "5e908526-d3d6-4a03-9790-bc724d80f142",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123TjXKUf63Us1ZeM2EEtBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11331
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

_source line 20_

Found the paper files locally. Let me read them now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "b887d661-b8cd-45aa-aca5-623792f54812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123TjXKUf63Us1ZeM2EEtBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11331
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_0118o6rv3anowKQqpJymceHw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "408d8f95-fb96-4bc9-93b7-edc433734d41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123TjXKUf63Us1ZeM2EEtBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11331
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01MnsLiCTdbFdxNDvsi9dXSG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "0201a510-41f1-4505-bc89-de198d4acde9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123TjXKUf63Us1ZeM2EEtBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11331,
      "cache_read_input_tokens": 24890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11331
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

_source line 23 · 2026-05-23T19:17:35.067Z_

<details><summary>↩ Tool result · `toolu_01MnsLiCTdbFdxNDvsi9dXSG`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Why do complete traces degrade SFT verdict accuracy despite containing all diagnostic information?
5	(2)~Which trace components carry the verdict signal, and how does their density affect learning?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.\footnote{Problem-level partition (472 train / 119 test, zero crossover; \S\ref{sec:dataset}). \texttt{exception\_only} duplicates (48.99\% test; Appendix~\ref{sec:dedup_stats}) arise from within-problem variants; deduplication yields negligible ($<$0.1pp) delta.}
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.
8	Under problem-level clustered bootstrap ($n_\text{eff}{=}119$), all cross-tier gaps remain significant ($p{<}.001$); 3 of 80 within-tier pairwise comparisons lose significance after Holm--Bonferroni correction.
9	
10	\subsection{Cross-Model Comparison}
11	\label{sec:cross_model}
12	
13	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families under key conditions; single-seed entries are marked with $^\dag$.
14	Regex B5 (99.33\%) exploits the \texttt{[No exception data in trace]} format marker, providing a non-learned baseline; its collapse to 28.49\% under marker removal (\S\ref{sec:nomarker}) shows the SFT advantage is not format-driven.
15	
16	\begin{table}[t]
17	\centering
18	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\pm$std over 2--3 seeds; $^\dag$ = single seed (seed 42). Bold: best per model. Full per-seed breakdowns in Appendix~\ref{sec:full_results}; per-class metrics in Appendix~\ref{sec:per_class}.}
19	\label{tab:cross_model}
20	\small
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{lcccc}
23	\toprule
24	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
25	\midrule
26	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.39}{\scriptsize$\pm$0.10} \\
27	ae\_only & 99.64{\scriptsize$\pm$0.49} & 98.83{\scriptsize$\pm$0.36} & 99.08{\scriptsize$\pm$0.00} & 98.53{\scriptsize$\pm$0.30} \\
28	VOTA & 99.05{\scriptsize$\pm$0.38} & 99.54{\scriptsize$\pm$0.06} & 98.74{\scriptsize$\pm$0.24} & 99.25$^\ddag$ \\
29	loop\_only & 86.05{\scriptsize$\pm$0.52} & 79.54{\scriptsize$\pm$1.42} & 77.40{\scriptsize$\pm$1.54} & 80.31{\scriptsize$\pm$1.65} \\
30	full\_trace & 81.44{\scriptsize$\pm$1.11} & 77.06$^\dag$ & 79.9$^\S$ & 79.16$^\dag$ \\
31	no\_trace & 75.13$^\dag$ & 72.35{\scriptsize$\pm$4.48} & 76.47$^\dag$ & 73.36$^\dag$ \\
32	\midrule
33	Regex B5 (marker) & \multicolumn{4}{c}{99.33} \\
34	Majority baseline & \multicolumn{4}{c}{71.51} \\
35	\bottomrule
36	\end{tabular}%
37	}
38	\vspace{2pt}
39	\par\raggedright\footnotesize
40	$^\ddag$DeepSeek VOTA seed 42 (84.45\%) is a tokenizer-driven truncation failure (Appendix~\ref{sec:tokenizer_analysis}), reported as 2-seed mean.
41	$^\S$CodeLlama \texttt{full\_trace} not available; head-2048 proxy reported.
42	Per-seed breakdowns for all conditions in Appendix~\ref{sec:full_results}.
43	\end{table}
44	
45	\paragraph{Exception dominance across families.}
46	Under \texttt{exception\_only}, all four models achieve ${\geq}$99.33\% across all available seeds (Table~\ref{tab:cross_model}), spanning only 0.50pp across architectures (the tightest of any condition).
47	CodeLlama-13B seed 123 achieves 100\%, indicating the 2 persistent errors (\texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are convergence artifacts; 99.83\% is a floor, not a ceiling.
48	
49	\paragraph{Scale effects concentrate in Tier~2.}
50	Tier~1 signals are scale-invariant across 1.5B--13B (8.7$\times$): both \texttt{exception\_only} and \texttt{ae\_only} span ${\leq}$1.2pp.
51	\texttt{loop\_only} spans 8.57pp, with CodeLlama-13B below Qwen-1.5B, suggesting architecture matters more than parameter count for lower-density signals.
52	In contrast, \texttt{no\_trace} scales with capacity (Figure~\ref{fig:cross_scale}) and shows the highest seed variance ($\sigma{=}$4.48pp).
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
57	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale, while \texttt{no\_trace} shows monotonic sensitivity (+4.12pp). \texttt{nomarker} (markers removed) shows no scale degradation.}
58	\label{fig:cross_scale}
59	\end{figure}
60	
61	\paragraph{VOTA cross-family variation.}
62	Excluding outlier seeds, VOTA achieves ${\geq}$98.57\% across all four models (0.80pp range).
63	DeepSeek seed 42 (84.45\%) is a tokenizer-driven truncation failure (91.7\% of samples exceed 2{,}048 tokens after tokenization; Appendix~\ref{sec:tokenizer_analysis}), demonstrating that VOTA's longer sequences are sensitive to tokenizer efficiency: 1/4 models suffers catastrophic truncation under standard training length. \texttt{exception\_only}'s compact inputs (median 150 tokens) sidestep this vulnerability entirely.
64	
65	\subsection{Component Ablation}
66	\label{sec:ablation}
67	
68	Multi-seed \texttt{ae\_only} ablations use Qwen-7B; \texttt{loop\_only} is evaluated across three models to test Tier~2 generalization (Table~\ref{tab:cross_model}).
69	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy validated across all four models and three architecture families (Table~\ref{tab:cross_model}): Tier~1 (${\geq}$98.53\%) and Tier~2 (77--86\%) are separated by 12+pp with non-overlapping CIs.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. Entries marked $^\dag$/$^\S$/$^\ddag$ are 3-seed mean$\pm$std; unmarked entries are single seed (seed 42). Per-seed breakdowns in Appendix~\ref{sec:full_results}. Seed $\sigma$ negatively correlates with density (0.00 for exception to 0.52 for loop).}
74	\label{tab:ablation}
75	\small
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{llccc}
78	\toprule
79	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
80	\midrule
81	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
82	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
83	VOTA & exc+ae+loop & 99.05$^\S$ & [98.49, 99.50] & --- \\
84	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
85	loop\_only & loop compression & 86.05$^\ddag$ & [83.97, 87.96] & 2 \\
86	full\_trace & complete trace & 81.44{\scriptsize$\pm$1.11} & --- & --- \\
87	no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
88	\midrule
89	Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
90	3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
91	Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
92	\bottomrule
93	\end{tabular}%
94	}
95	\end{table}
96	
97	Tier~1 signals are individually sufficient: \texttt{exception\_only} (99.83\%$\pm$0.00) exceeds VOTA (99.05\%$\pm$0.38) by +0.78pp (2/3 seeds $p{<}.05$, all directionally consistent), implying that combining signals introduces noise.
98	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%, single seed), indicating exception dominance.
99	Individual exception subcomponents (type, stacktrace, message) each independently achieve ${\geq}$99.50\%, indicating that the binary presence of an exception event, rather than any specific subcomponent, drives Tier~1 performance (Appendix~\ref{sec:exc_subcomponent}).
100	The Tier~1/2 boundary is unambiguous: the lowest Tier~1 condition (\texttt{ae\_only} on DeepSeek, 98.53\%$\pm$0.30, 2 seeds) exceeds the highest Tier~2 (\texttt{loop\_only} on Qwen-7B, 86.05\%, CI [83.97, 87.96]) by 12.48\,pp with non-overlapping CIs (gap statistic supports $k{=}2$ clusters, silhouette ${\geq}$0.74).
101	Tier~2 \texttt{loop\_only} lifts over \texttt{no\_trace} are model-dependent: Qwen +10.92pp (7B) and +7.19pp (1.5B); DeepSeek +6.95pp; CodeLlama +0.93pp (n.s.).
102	\paragraph{Rule-based baseline comparison.}
103	The strongest non-trivial regex heuristic (B4: exception class name matching; Table~\ref{tab:regex}) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}.001$).
104	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
105	Across all formats, SFT outperforms the best applicable regex by +3.62--23.86pp (Appendix~\ref{sec:regex_baselines}).
106	
107	\paragraph{Zero-shot and few-shot LLM baselines.}
108	Zero-shot prompting spans 51.0--93.5\% across four models (42.44pp range); three-shot ICL on Qwen-7B (90.84\%) improves only 1.76pp.
109	SFT compresses this range to 0.50pp (99.39--99.89\%), closing a 6--49pp gap with 4,720 samples (Appendix~\ref{sec:zeroshot_cross_model}).
110	\paragraph{Frontier model crossover.}
111	Two frontier models illustrate that SFT's advantage depends on input density: under \texttt{no\_trace}, GPT-4o (84.45\%) and GPT-4.1 (77.31\%) outperform SFT Qwen-7B (75.13\%), but under \texttt{exception\_only} the ranking reverses (SFT 99.83\% vs.\ GPT-4o 87.98\%).
112	Compact diagnostic input unlocks SFT's full advantage over general reasoning capacity.
113	
114	\subsection{Format Marker Ablation}
115	\label{sec:nomarker}
116	
117	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
118	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
119	
120	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
121	Qwen-1.5B: 97.82\%, drop of 2.01pp.
122	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
123	Regex baselines illustrate this decomposition: B5 (\texttt{[No exception data]}$\to$pass, 99.33\% with markers) collapses to 28.49\% without markers, showing it is entirely format-dependent.
124	The strongest semantic regex B4 (exception class matching, 93.61\%) is marker-invariant; SFT \texttt{nomarker} (97.65\%) exceeds it by 4.04pp, isolating the learned semantic contribution beyond pattern matching.
125	
126	\paragraph{Cross-dataset transfer.}
127	Bidirectional evaluation demonstrates generalization: HumanEval${\to}$MBPP \texttt{exception\_only} achieves 99.41\% ($N{=}4{,}270$) and MBPP${\to}$HumanEval achieves 100.0\% ($N{=}1{,}640$), while \texttt{no\_trace} drops to near-majority baseline in both directions (70.56\% vs.\ 69.02\% majority; 67.99\% vs.\ 61.65\%).
128	The near-zero transfer loss for exception signals, across independently authored problem sets with no problem overlap, shows SFT learns language-level diagnostic patterns, not dataset-specific artifacts.
129	Under marker removal, cross-dataset accuracy drops to 95.5\% ($-$3.9pp), indicating that the majority of cross-dataset transfer relies on learned diagnostic patterns rather than format markers.
130	
131	\subsection{Decomposing the Full-Trace Degradation}
132	\label{sec:density}
133	
134	The 18.07pp gap between \texttt{exception\_only} (99.83\%) and \texttt{full\_trace} (81.76\%) could reflect gradient dilution (diagnostic tokens are ${\sim}$1/500 of full traces, diluting gradient signal during training) or content quality (verbose input buries diagnostic signals at inference).
135	
136	\paragraph{Controlled gradient masking.}
137	To isolate gradient dilution, we mask 99.8\% of gradient updates during \texttt{exception\_only} training, matching the diagnostic token ratio of full traces while preserving compact input.
138	This yields 99.22\% (mean $-$0.61pp from \texttt{exception\_only}, 3 seeds), limiting gradient dilution to ${\leq}$4\% of the 18.07pp gap (Table~\ref{tab:density}).
139	The gradient masking bound attributes the remaining ${\geq}$96\% to content quality (diagnostic signal density at inference), though forward-pass attention during masked training is an unquantified residual.
140	Note that masking affects only the backward pass; the model still attends to all input tokens during the forward pass, so this bounds gradient dilution's contribution but does not rule out attention-based information flow as a residual confound.
141	
142	\begin{table}[t]
143	\centering
144	\caption{Decomposition of the full-trace degradation (Qwen-7B). Gradient masking attributes ${\leq}$4\% to gradient dilution; the bound assigns the remainder to content quality, though forward-pass attention is a residual confound (\S\ref{sec:density}). Label-only loss provides a confounded but directionally consistent complementary estimate.}
145	\label{tab:density}
146	\small
147	\begin{tabular}{lcc}
148	\toprule
149	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$} \\
150	\midrule
151	exception\_only & 99.83{\scriptsize$\pm$0.00} & --- \\
152	\quad + grad mask (99.8\%) & 99.22{\scriptsize$\pm$0.20}$^\S$ & $-$0.61pp \\
153	full\_trace & 81.76$^\ddag$ & $-$18.07pp \\
154	\midrule
155	\multicolumn{3}{l}{\textit{Complementary (confounded):}} \\
156	full\_trace + label-only loss & 85.94{\scriptsize$\pm$1.12} & +4.50pp$^\dag$ \\
157	\bottomrule
158	\end{tabular}
159	\vspace{2pt}
160	\par\raggedright\footnotesize
161	$^\S$Mean $\pm$ std over 3 seeds (42, 123, 456).
162	$^\ddag$Matched-seed baseline; 3-seed mean 81.44\%$\pm$1.11 (Table~\ref{tab:cross_model}).
163	$^\dag$vs.\ \texttt{full\_trace} (81.44\%$\pm$1.11); not significant under clustered bootstrap (95\% CI [$-$0.6, +9.8]pp, $n_\text{eff}{=}119$).
164	\end{table}
165	
166	\paragraph{Complementary evidence.}
167	Label-only loss on full traces (+4.50pp, 3 seeds) yields a confounded upper bound of ${\leq}$26\% gradient contribution, consistent with the masking estimate (${\leq}$4\%) but not significant under clustered bootstrap (95\% CI [$-$0.6, +9.8]pp).
168	Qwen-1.5B shows a similar label-only pattern (17\%/83\%, 3 seeds); CodeLlama and DeepSeek exhibit label-only collapse to majority baseline (28.5\%), limiting this complementary analysis to the Qwen family.
169	The architecture dependence suggests label-only training is sensitive to model capacity or optimization landscape; the gradient masking ablation provides a more robust, architecture-independent decomposition.
170	Cross-architecture validation on two additional families is directionally consistent (single seed each): DeepSeek-Coder-6.7B achieves 99.33\% and CodeLlama-13B achieves 100\% under 99.8\% masking, both well above the full-trace range (77--82\%, Table~\ref{tab:cross_model}), supporting content quality as the dominant factor across architectures.
171	Error analysis supports the content quality interpretation: all 217 \texttt{full\_trace} errors occur where tokenizer truncation removes diagnostic markers, manifesting through mechanical truncation rather than semantic confusion.
172	
173	\subsection{Complementary Analyses}
174	\label{sec:additional}
175	
176	\paragraph{Trace length ablation.}
177	\label{sec:trace_length}
178	Varying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern: 1024-token prefixes (77.23\%) underperform 512-token prefixes (80.42\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\ref{sec:trace_length_full}).
179	Critically, removing the token budget entirely (no truncation) yields 81.76\%, identical to head-2048, ruling out truncation as the explanation for the full-trace degradation.
180	This non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\to$tail-2048 ($-$1.5pp).
181	
182	\paragraph{Truncation direction and budget curve.}
183	Tail-truncation dramatically outperforms head-truncation: tail-2048 exceeds head-2048 by 15.5--22.6pp across three models (Appendix~\ref{sec:trace_length_full}).
184	Figure~\ref{fig:budget_curve} reveals a sharp phase transition at 384$\to$512 tail tokens: all four models simultaneously jump +13.2--22.0pp, crossing from near-baseline to 93--98\%.
185	This threshold coincides with the globals module dump boundary (${\sim}$384 tokens), beyond which structured execution markers become visible (Table~\ref{tab:tail_cross_model}).
186	Beyond 512 tokens, all 12 model$\times$seed combinations converge into [93.61\%, 98.24\%] (Table~\ref{tab:tail512_seeds}).
187	\texttt{tail\_2048} captures 95--98\% of \texttt{exception\_only}'s accuracy; the residual 2--5pp gap shows semantic extraction still outperforms positional extraction.
188	
189	\begin{figure}[t]
190	\centering
191	\includegraphics[width=\columnwidth]{budget_curve}
192	\caption{Tail-truncation budget curve across four models and three architecture families ($N{=}1{,}190$). A sharp phase transition at 384$\to$512 tokens (+13.2--22.0pp) coincides with the globals module dump boundary. Dashed lines: \texttt{exception\_only} ceiling and \texttt{no\_trace} floor.}
193	\label{fig:budget_curve}
194	\end{figure}
195	
196	\paragraph{Calibration.}
197	\label{sec:calibration}
198	Calibration mirrors the tier hierarchy: \texttt{exception\_only} achieves ECE = 0.0027 vs.\ 0.171 for \texttt{no\_trace}, a 63$\times$ gap (Figure~\ref{fig:calibration}).
199	This calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \texttt{exception\_only} (Table~\ref{tab:calibration_model_level} in Appendix), indicating well-calibrated predictions rather than overfit confidence.
200	
201	\paragraph{Error analysis.}
202	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000; Appendix~\ref{sec:error_overlap}); per-type breakdown shows all standard exception types achieve 100\% accuracy, with only \texttt{GeneratorExit} (a benign \texttt{BaseException} subclass) causing failures (Appendix~\ref{sec:exception_type}).
203	
204	\paragraph{Length control.}
205	Padding \texttt{exception\_only} to 2{,}048 tokens, even in a semantically loaded position (after the verdict region), yields identical accuracy (99.83\%), indicating the 18--23pp gap arises from spurious patterns in verbose trace content, not sequence length.
206	
207	\paragraph{Supplementary OOD analysis.}
208	\label{sec:debugbench}
209	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the condition ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%.
210	However, narrow margins (3.29pp headroom from \texttt{no\_trace}) limit discriminative power; this supplementary analysis preserves the ranking but cannot establish effect sizes comparable to the primary dataset (Appendix~\ref{sec:debugbench_full}).
211	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "b34e9964-486a-4d84-9e28-0e90d5bf2ccf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nWe evaluate across two research questions:\n(1)~Why do complete traces degrade SFT verdict accuracy despite containing all diagnostic information?\n(2)~Which trace components carry the verdict signal, and how does their density affect learning?\nAll experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\\% CIs.\\footnote{Problem-level partition (472 train / 119 test, zero crossover; \\S\\ref{sec:dataset}). \\texttt{exception\\_only} duplicates (48.99\\% test; Appendix~\\ref{sec:dedup_stats}) arise from within-problem variants; deduplication yields negligible ($<$0.1pp) delta.}\nPairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}.0001$ unless noted.\nUnder problem-level clustered bootstrap ($n_\\text{eff}{=}119$), all cross-tier gaps remain significant ($p{<}.001$); 3 of 80 within-tier pairwise comparisons lose significance after Holm--Bonferroni correction.\n\n\\subsection{Cross-Model Comparison}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} compares four models spanning an 8.7$\\times$ parameter range (1.5B--13B) and three architecture families under key conditions; single-seed entries are marked with $^\\dag$.\nRegex B5 (99.33\\%) exploits the \\texttt{[No exception data in trace]} format marker, providing a non-learned baseline; its collapse to 28.49\\% under marker removal (\\S\\ref{sec:nomarker}) shows the SFT advantage is not format-driven.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model verdict accuracy (\\%, $N{=}1{,}190$) across four models (1.5B--13B) and three architecture families. Multi-seed entries report mean$\\pm$std over 2--3 seeds; $^\\dag$ = single seed (seed 42). Bold: best per model. Full per-seed breakdowns in Appendix~\\ref{sec:full_results}; per-class metrics in Appendix~\\ref{sec:per_class}.}\n\\label{tab:cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Qwen-7B} & \\textbf{Qwen-1.5B} & \\textbf{CL-13B} & \\textbf{DS-6.7B} \\\\\n\\midrule\nexception\\_only & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.83}{\\scriptsize$\\pm$0.00} & \\textbf{99.89}{\\scriptsize$\\pm$0.10} & \\textbf{99.39}{\\scriptsize$\\pm$0.10} \\\\\nae\\_only & 99.64{\\scriptsize$\\pm$0.49} & 98.83{\\scriptsize$\\pm$0.36} & 99.08{\\scriptsize$\\pm$0.00} & 98.53{\\scriptsize$\\pm$0.30} \\\\\nVOTA & 99.05{\\scriptsize$\\pm$0.38} & 99.54{\\scriptsize$\\pm$0.06} & 98.74{\\scriptsize$\\pm$0.24} & 99.25$^\\ddag$ \\\\\nloop\\_only & 86.05{\\scriptsize$\\pm$0.52} & 79.54{\\scriptsize$\\pm$1.42} & 77.40{\\scriptsize$\\pm$1.54} & 80.31{\\scriptsize$\\pm$1.65} \\\\\nfull\\_trace & 81.44{\\scriptsize$\\pm$1.11} & 77.06$^\\dag$ & 79.9$^\\S$ & 79.16$^\\dag$ \\\\\nno\\_trace & 75.13$^\\dag$ & 72.35{\\scriptsize$\\pm$4.48} & 76.47$^\\dag$ & 73.36$^\\dag$ \\\\\n\\midrule\nRegex B5 (marker) & \\multicolumn{4}{c}{99.33} \\\\\nMajority baseline & \\multicolumn{4}{c}{71.51} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\vspace{2pt}\n\\par\\raggedright\\footnotesize\n$^\\ddag$DeepSeek VOTA seed 42 (84.45\\%) is a tokenizer-driven truncation failure (Appendix~\\ref{sec:tokenizer_analysis}), reported as 2-seed mean.\n$^\\S$CodeLlama \\texttt{full\\_trace} not available; head-2048 proxy reported.\nPer-seed breakdowns for all conditions in Appendix~\\ref{sec:full_results}.\n\\end{table}\n\n\\paragraph{Exception dominance across families.}\nUnder \\texttt{exception\\_only}, all four models achieve ${\\geq}$99.33\\% across all available seeds (Table~\\ref{tab:cross_model}), spanning only 0.50pp across architectures (the tightest of any condition).\nCodeLlama-13B seed 123 achieves 100\\%, indicating the 2 persistent errors (\\texttt{GeneratorExit}; Appendix~\\ref{sec:irreducible}) are convergence artifacts; 99.83\\% is a floor, not a ceiling.\n\n\\paragraph{Scale effects concentrate in Tier~2.}\nTier~1 signals are scale-invariant across 1.5B--13B (8.7$\\times$): both \\texttt{exception\\_only} and \\texttt{ae\\_only} span ${\\leq}$1.2pp.\n\\texttt{loop\\_only} spans 8.57pp, with CodeLlama-13B below Qwen-1.5B, suggesting architecture matters more than parameter count for lower-density signals.\nIn contrast, \\texttt{no\\_trace} scales with capacity (Figure~\\ref{fig:cross_scale}) and shows the highest seed variance ($\\sigma{=}$4.48pp).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_cross_model_gap}\n\\caption{Verdict accuracy vs.\\ model scale. \\texttt{exception\\_only} maintains ${\\geq}$99.33\\% regardless of scale, while \\texttt{no\\_trace} shows monotonic sensitivity (+4.12pp). \\texttt{nomarker} (markers removed) shows no scale degradation.}\n\\label{fig:cross_scale}\n\\end{figure}\n\n\\paragraph{VOTA cross-family variation.}\nExcluding outlier seeds, VOTA achieves ${\\geq}$98.57\\% across all four models (0.80pp range).\nDeepSeek seed 42 (84.45\\%) is a tokenizer-driven truncation failure (91.7\\% of samples exceed 2{,}048 tokens after tokenization; Appendix~\\ref{sec:tokenizer_analysis}), demonstrating that VOTA's longer sequences are sensitive to tokenizer efficiency: 1/4 models suffers catastrophic truncation under standard training length. \\texttt{exception\\_only}'s compact inputs (median 150 tokens) sidestep this vulnerability entirely.\n\n\\subsection{Component Ablation}\n\\label{sec:ablation}\n\nMulti-seed \\texttt{ae\\_only} ablations use Qwen-7B; \\texttt{loop\\_only} is evaluated across three models to test Tier~2 generalization (Table~\\ref{tab:cross_model}).\nTable~\\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B and reveals a two-tier hierarchy validated across all four models and three architecture families (Table~\\ref{tab:cross_model}): Tier~1 (${\\geq}$98.53\\%) and Tier~2 (77--86\\%) are separated by 12+pp with non-overlapping CIs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. Entries marked $^\\dag$/$^\\S$/$^\\ddag$ are 3-seed mean$\\pm$std; unmarked entries are single seed (seed 42). Per-seed breakdowns in Appendix~\\ref{sec:full_results}. Seed $\\sigma$ negatively correlates with density (0.00 for exception to 0.52 for loop).}\n\\label{tab:ablation}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Components} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} & \\textbf{Tier} \\\\\n\\midrule\nae\\_only & assertion-point & 99.64$^\\dag$ & [99.26, 99.87] & 1 \\\\\nexception\\_only & exception events & \\textbf{99.83} & [99.58, 100.00] & 1 \\\\\nVOTA & exc+ae+loop & 99.05$^\\S$ & [98.49, 99.50] & --- \\\\\nVOTA\\_no\\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\\\\nloop\\_only & loop compression & 86.05$^\\ddag$ & [83.97, 87.96] & 2 \\\\\nfull\\_trace & complete trace & 81.44{\\scriptsize$\\pm$1.11} & --- & --- \\\\\nno\\_trace & none & 75.13 & [72.77, 77.48] & --- \\\\\n\\midrule\nRegex (best) & exc.\\ type regex & 93.61 & --- & --- \\\\\n3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\\\\nZero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTier~1 signals are individually sufficient: \\texttt{exception\\_only} (99.83\\%$\\pm$0.00) exceeds VOTA (99.05\\%$\\pm$0.38) by +0.78pp (2/3 seeds $p{<}.05$, all directionally consistent), implying that combining signals introduces noise.\nRemoving assertion points has no effect (\\texttt{VOTA\\_no\\_ae} = 99.41\\%, single seed), indicating exception dominance.\nIndividual exception subcomponents (type, stacktrace, message) each independently achieve ${\\geq}$99.50\\%, indicating that the binary presence of an exception event, rather than any specific subcomponent, drives Tier~1 performance (Appendix~\\ref{sec:exc_subcomponent}).\nThe Tier~1/2 boundary is unambiguous: the lowest Tier~1 condition (\\texttt{ae\\_only} on DeepSeek, 98.53\\%$\\pm$0.30, 2 seeds) exceeds the highest Tier~2 (\\texttt{loop\\_only} on Qwen-7B, 86.05\\%, CI [83.97, 87.96]) by 12.48\\,pp with non-overlapping CIs (gap statistic supports $k{=}2$ clusters, silhouette ${\\geq}$0.74).\nTier~2 \\texttt{loop\\_only} lifts over \\texttt{no\\_trace} are model-dependent: Qwen +10.92pp (7B) and +7.19pp (1.5B); DeepSeek +6.95pp; CodeLlama +0.93pp (n.s.).\n\\paragraph{Rule-based baseline comparison.}\nThe strongest non-trivial regex heuristic (B4: exception class name matching; Table~\\ref{tab:regex}) achieves 93.61\\% accuracy (F1=0.876), trailing SFT \\texttt{exception\\_only} (99.83\\%, F1=0.997) by 6.22pp (McNemar $p{<}.001$).\nThe gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \\texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\\ref{sec:regex_baselines}).\nAcross all formats, SFT outperforms the best applicable regex by +3.62--23.86pp (Appendix~\\ref{sec:regex_baselines}).\n\n\\paragraph{Zero-shot and few-shot LLM baselines.}\nZero-shot prompting spans 51.0--93.5\\% across four models (42.44pp range); three-shot ICL on Qwen-7B (90.84\\%) improves only 1.76pp.\nSFT compresses this range to 0.50pp (99.39--99.89\\%), closing a 6--49pp gap with 4,720 samples (Appendix~\\ref{sec:zeroshot_cross_model}).\n\\paragraph{Frontier model crossover.}\nTwo frontier models illustrate that SFT's advantage depends on input density: under \\texttt{no\\_trace}, GPT-4o (84.45\\%) and GPT-4.1 (77.31\\%) outperform SFT Qwen-7B (75.13\\%), but under \\texttt{exception\\_only} the ranking reverses (SFT 99.83\\% vs.\\ GPT-4o 87.98\\%).\nCompact diagnostic input unlocks SFT's full advantage over general reasoning capacity.\n\n\\subsection{Format Marker Ablation}\n\\label{sec:nomarker}\n\nThe \\texttt{exception\\_only} format includes a \\texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\\% accuracy; Appendix~\\ref{sec:regex_baselines}).\nTo quantify the marker's contribution, we retrain with all format markers removed (\\texttt{nomarker} condition).\n\nQwen-7B 3-seed mean: 97.65\\% $\\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\\%), a drop of 2.18pp from \\texttt{exception\\_only} (99.83\\%).\nQwen-1.5B: 97.82\\%, drop of 2.01pp.\nThe marker contribution (${\\sim}$2pp) accounts for only ${\\sim}$9\\% of the total exception lift over \\texttt{no\\_trace} (24.70pp on 7B).\nRegex baselines illustrate this decomposition: B5 (\\texttt{[No exception data]}$\\to$pass, 99.33\\% with markers) collapses to 28.49\\% without markers, showing it is entirely format-dependent.\nThe strongest semantic regex B4 (exception class matching, 93.61\\%) is marker-invariant; SFT \\texttt{nomarker} (97.65\\%) exceeds it by 4.04pp, isolating the learned semantic contribution beyond pattern matching.\n\n\\paragraph{Cross-dataset transfer.}\nBidirectional evaluation demonstrates generalization: HumanEval${\\to}$MBPP \\texttt{exception\\_only} achieves 99.41\\% ($N{=}4{,}270$) and MBPP${\\to}$HumanEval achieves 100.0\\% ($N{=}1{,}640$), while \\texttt{no\\_trace} drops to near-majority baseline in both directions (70.56\\% vs.\\ 69.02\\% majority; 67.99\\% vs.\\ 61.65\\%).\nThe near-zero transfer loss for exception signals, across independently authored problem sets with no problem overlap, shows SFT learns language-level diagnostic patterns, not dataset-specific artifacts.\nUnder marker removal, cross-dataset accuracy drops to 95.5\\% ($-$3.9pp), indicating that the majority of cross-dataset transfer relies on learned diagnostic patterns rather than format markers.\n\n\\subsection{Decomposing the Full-Trace Degradation}\n\\label{sec:density}\n\nThe 18.07pp gap between \\texttt{exception\\_only} (99.83\\%) and \\texttt{full\\_trace} (81.76\\%) could reflect gradient dilution (diagnostic tokens are ${\\sim}$1/500 of full traces, diluting gradient signal during training) or content quality (verbose input buries diagnostic signals at inference).\n\n\\paragraph{Controlled gradient masking.}\nTo isolate gradient dilution, we mask 99.8\\% of gradient updates during \\texttt{exception\\_only} training, matching the diagnostic token ratio of full traces while preserving compact input.\nThis yields 99.22\\% (mean $-$0.61pp from \\texttt{exception\\_only}, 3 seeds), limiting gradient dilution to ${\\leq}$4\\% of the 18.07pp gap (Table~\\ref{tab:density}).\nThe gradient masking bound attributes the remaining ${\\geq}$96\\% to content quality (diagnostic signal density at inference), though forward-pass attention during masked training is an unquantified residual.\nNote that masking affects only the backward pass; the model still attends to all input tokens during the forward pass, so this bounds gradient dilution's contribution but does not rule out attention-based information flow as a residual confound.\n\n\\begin{table}[t]\n\\centering\n\\caption{Decomposition of the full-trace degradation (Qwen-7B). Gradient masking attributes ${\\leq}$4\\% to gradient dilution; the bound assigns the remainder to content quality, though forward-pass attention is a residual confound (\\S\\ref{sec:density}). Label-only loss provides a confounded but directionally consistent complementary estimate.}\n\\label{tab:density}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$} \\\\\n\\midrule\nexception\\_only & 99.83{\\scriptsize$\\pm$0.00} & --- \\\\\n\\quad + grad mask (99.8\\%) & 99.22{\\scriptsize$\\pm$0.20}$^\\S$ & $-$0.61pp \\\\\nfull\\_trace & 81.76$^\\ddag$ & $-$18.07pp \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Complementary (confounded):}} \\\\\nfull\\_trace + label-only loss & 85.94{\\scriptsize$\\pm$1.12} & +4.50pp$^\\dag$ \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\par\\raggedright\\footnotesize\n$^\\S$Mean $\\pm$ std over 3 seeds (42, 123, 456).\n$^\\ddag$Matched-seed baseline; 3-seed mean 81.44\\%$\\pm$1.11 (Table~\\ref{tab:cross_model}).\n$^\\dag$vs.\\ \\texttt{full\\_trace} (81.44\\%$\\pm$1.11); not significant under clustered bootstrap (95\\% CI [$-$0.6, +9.8]pp, $n_\\text{eff}{=}119$).\n\\end{table}\n\n\\paragraph{Complementary evidence.}\nLabel-only loss on full traces (+4.50pp, 3 seeds) yields a confounded upper bound of ${\\leq}$26\\% gradient contribution, consistent with the masking estimate (${\\leq}$4\\%) but not significant under clustered bootstrap (95\\% CI [$-$0.6, +9.8]pp).\nQwen-1.5B shows a similar label-only pattern (17\\%/83\\%, 3 seeds); CodeLlama and DeepSeek exhibit label-only collapse to majority baseline (28.5\\%), limiting this complementary analysis to the Qwen family.\nThe architecture dependence suggests label-only training is sensitive to model capacity or optimization landscape; the gradient masking ablation provides a more robust, architecture-independent decomposition.\nCross-architecture validation on two additional families is directionally consistent (single seed each): DeepSeek-Coder-6.7B achieves 99.33\\% and CodeLlama-13B achieves 100\\% under 99.8\\% masking, both well above the full-trace range (77--82\\%, Table~\\ref{tab:cross_model}), supporting content quality as the dominant factor across architectures.\nError analysis supports the content quality interpretation: all 217 \\texttt{full\\_trace} errors occur where tokenizer truncation removes diagnostic markers, manifesting through mechanical truncation rather than semantic confusion.\n\n\\subsection{Complementary Analyses}\n\\label{sec:additional}\n\n\\paragraph{Trace length ablation.}\n\\label{sec:trace_length}\nVarying the head-truncated trace token budget (256--no limit) on Qwen-7B yields accuracy in a narrow 77.2\\%--81.8\\% band with a non-monotonic pattern: 1024-token prefixes (77.23\\%) underperform 512-token prefixes (80.42\\%, $p{=}.002$), because mid-length prefixes retain enough irrelevant content to mislead the model while discarding diagnostic events near the trace terminus (Appendix~\\ref{sec:trace_length_full}).\nCritically, removing the token budget entirely (no truncation) yields 81.76\\%, identical to head-2048, ruling out truncation as the explanation for the full-trace degradation.\nThis non-monotonicity is specific to head-truncation; under tail-truncation, accuracy increases monotonically for two of three models (Table~\\ref{tab:tail_cross_model} in Appendix), with only DeepSeek showing a mild architecture-specific reversal at tail-1024$\\to$tail-2048 ($-$1.5pp).\n\n\\paragraph{Truncation direction and budget curve.}\nTail-truncation dramatically outperforms head-truncation: tail-2048 exceeds head-2048 by 15.5--22.6pp across three models (Appendix~\\ref{sec:trace_length_full}).\nFigure~\\ref{fig:budget_curve} reveals a sharp phase transition at 384$\\to$512 tail tokens: all four models simultaneously jump +13.2--22.0pp, crossing from near-baseline to 93--98\\%.\nThis threshold coincides with the globals module dump boundary (${\\sim}$384 tokens), beyond which structured execution markers become visible (Table~\\ref{tab:tail_cross_model}).\nBeyond 512 tokens, all 12 model$\\times$seed combinations converge into [93.61\\%, 98.24\\%] (Table~\\ref{tab:tail512_seeds}).\n\\texttt{tail\\_2048} captures 95--98\\% of \\texttt{exception\\_only}'s accuracy; the residual 2--5pp gap shows semantic extraction still outperforms positional extraction.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{budget_curve}\n\\caption{Tail-truncation budget curve across four models and three architecture families ($N{=}1{,}190$). A sharp phase transition at 384$\\to$512 tokens (+13.2--22.0pp) coincides with the globals module dump boundary. Dashed lines: \\texttt{exception\\_only} ceiling and \\texttt{no\\_trace} floor.}\n\\label{fig:budget_curve}\n\\end{figure}\n\n\\paragraph{Calibration.}\n\\label{sec:calibration}\nCalibration mirrors the tier hierarchy: \\texttt{exception\\_only} achieves ECE = 0.0027 vs.\\ 0.171 for \\texttt{no\\_trace}, a 63$\\times$ gap (Figure~\\ref{fig:calibration}).\nThis calibration advantage generalizes across architectures and scales: all four models (1.5B--13B) achieve ECE ${<}$ 0.007 under \\texttt{exception\\_only} (Table~\\ref{tab:calibration_model_level} in Appendix), indicating well-calibrated predictions rather than overfit confidence.\n\n\\paragraph{Error analysis.}\n\\texttt{exception\\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000; Appendix~\\ref{sec:error_overlap}); per-type breakdown shows all standard exception types achieve 100\\% accuracy, with only \\texttt{GeneratorExit} (a benign \\texttt{BaseException} subclass) causing failures (Appendix~\\ref{sec:exception_type}).\n\n\\paragraph{Length control.}\nPadding \\texttt{exception\\_only} to 2{,}048 tokens, even in a semantically loaded position (after the verdict region), yields identical accuracy (99.83\\%), indicating the 18--23pp gap arises from spurious patterns in verbose trace content, not sequence length.\n\n\\paragraph{Supplementary OOD analysis.}\n\\label{sec:debugbench}\nOn DebugBench \\citep{tian2024debugbench} ($N{=}426$), the condition ranking is preserved: \\texttt{exception\\_only} 100\\%, VOTA 99.77\\%, \\texttt{no\\_trace} 96.71\\%.\nHowever, narrow margins (3.29pp headroom from \\texttt{no\\_trace}) limit discriminative power; this supplementary analysis preserves the ranking but cannot establish effect sizes comparable to the primary dataset (Appendix~\\ref{sec:debugbench_full}).\n",
      "numLines": 211,
      "startLine": 1,
      "totalLines": 211
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:17:35.181Z_

<details><summary>↩ Tool result · `toolu_0118o6rv3anowKQqpJymceHw`</summary>

```text
1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA seed 42 is a training failure (84.45\%, fail recall = 45.4\%) due to tokenizer-driven truncation; seeds 123/456 achieve 99.16\%/99.33\%.}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 85.94 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.05 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 86.05 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	AE Only           & DeepSeek-6.7B & 98.74 & 98.40 & 99.90 & 99.10 & 99.70 & 95.90 & 97.70 \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
33	%% ============================================================
34	\section{Training Details}
35	\label{sec:training_details}
36	
37	Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
38	All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.
39	
40	\begin{table}[t]
41	\centering
42	\caption{Training hyperparameters (shared across all conditions).}
43	\label{tab:hyperparams}
44	\small
45	\resizebox{\columnwidth}{!}{%
46	\begin{tabular}{ll}
47	\toprule
48	\textbf{Hyperparameter} & \textbf{Value} \\
49	\midrule
50	LoRA rank ($r$)            & 16 \\
51	LoRA alpha ($\alpha$)      & 32 \\
52	LoRA dropout               & 0.05 \\
53	LoRA target modules        & all linear layers \\
54	\midrule
55	Epochs                     & 3 \\
56	Per-device batch size       & 4 \\
57	Gradient accumulation steps & 8 \\
58	Effective batch size        & 32 \\
59	\midrule
60	Learning rate               & $2 \times 10^{-4}$ \\
61	LR scheduler                & linear decay \\
62	Warmup ratio                & 0.1 \\
63	Weight decay                & 0.01 \\
64	\midrule
65	Max sequence length         & 2048 tokens \\
66	Primary seed                & 42 \\
67	Robustness seeds            & 123, 456 \\
68	\midrule
69	Hardware                    & 1$\times$ enterprise-grade GPU (${\geq}$80\,GB VRAM) \\
70	Framework                   & HuggingFace TRL SFTTrainer \\
71	\bottomrule
72	\end{tabular}%
73	}
74	\end{table}
75	
76	Table~\ref{tab:train_time} reports per-condition training wall-clock times.
77	Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.
78	
79	\begin{table}[t]
80	\centering
81	\caption{Training wall-clock time per condition on a single enterprise-grade GPU (${\geq}$80\,GB VRAM). Where multiple seeds were run, individual times are listed.}
82	\label{tab:train_time}
83	\small
84	\begin{tabular}{llr}
85	\toprule
86	\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
87	\midrule
88	no\_trace       & 42         & ${\sim}$0.5 \\
89	full\_trace     & 42         & ${\sim}$2.2 \\
90	label\_only     & 42         & ${\sim}$2.2 \\
91	VOTA                     & 42         & ${\sim}$2.3 \\
92	exception\_only & 42         & ${\sim}$2.1 \\
93	exception\_only & 123        & ${\sim}$2.1 \\
94	exception\_only & 456        & ${\sim}$1.3 \\
95	ae\_only        & 42         & ${\sim}$1.8 \\
96	loop\_only      & 42         & ${\sim}$2.1 \\
97	VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	%% ============================================================
103	\section{VOTA Extraction Algorithm}
104	\label{sec:vota_algorithm}
105	
106	Algorithm~\ref{alg:vota} describes the three-component VOTA extraction pipeline applied to a raw \texttt{sys.settrace} execution log.
107	
108	\begin{algorithm}[t]
109	\caption{VOTA Trace Extraction}
110	\label{alg:vota}
111	\small
112	\begin{algorithmic}[1]
113	\REQUIRE Raw trace $T$ from \texttt{sys.settrace} (list of events)
114	\ENSURE Compressed VOTA representation $V$
115	\STATE $V \leftarrow$ empty string
116	\STATE \textbf{// Component 1: Exception summary}
117	\FOR{each event $e$ in $T$ with type \texttt{exception}}
118	  \STATE Parse traceback $\rightarrow$ extract error type, message, file, line
119	  \STATE Append \texttt{[ERROR] type: message (file:line)} to $V$
120	\ENDFOR
121	\IF{no exception events found}
122	  \STATE Append \texttt{[No exception data in trace]} to $V$
123	\ENDIF
124	\STATE \textbf{// Component 2: Assertion-point comparison}
125	\FOR{each \texttt{assert} or \texttt{return} event $e$ in $T$}
126	  \STATE Extract actual value from execution state
127	  \STATE Extract expected value from test assertion
128	  \STATE Append \texttt{[ASSERT] actual=... expected=... match=T/F} to $V$
129	\ENDFOR
130	\STATE \textbf{// Component 3: Loop compression}
131	\FOR{each consecutive repeated line sequence $S$ in $T$}
132	  \IF{$|S| \geq 2$ iterations of same loop body}
133	    \STATE Replace $S$ with single iteration + \texttt{[repeated $\times$N]}
134	  \ENDIF
135	\ENDFOR
136	\STATE Append compressed non-exception lines to $V$
137	\RETURN $V$
138	\end{algorithmic}
139	\end{algorithm}
140	
141	%% ============================================================
142	\section{VOTA Trace Examples}
143	\label{sec:vota_examples}
144	
145	We provide two representative VOTA trace examples illustrating the fail and pass cases.
146	In the fail case, the exception event provides an unambiguous fault signal.
147	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
148	
149	\paragraph{Fail example.}
150	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
151	
152	\begin{scriptsize}
153	\begin{verbatim}
154	## Function
155	def divide(a, b):
156	    return a / b
157	
158	## Test Input
159	divide(1, 0)
160	
161	## Expected Output
162	inf
163	
164	## VOTA Trace
165	[ERROR] ZeroDivisionError: division by zero
166	
167	## Verdict
168	fail
169	\end{verbatim}
170	\end{scriptsize}
171	
172	\paragraph{Pass example.}
173	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
174	
175	\begin{scriptsize}
176	\begin{verbatim}
177	## Function
178	def add(a, b):
179	    return a + b
180	
181	## Test Input
182	add(2, 3)
183	
184	## Expected Output
185	5
186	
187	## VOTA Trace
188	[LOOP] No loops detected.
189	[ASSERT] actual=5, expected=5
190	
191	## Verdict
192	pass
193	\end{verbatim}
194	\end{scriptsize}
195	
196	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
197	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
198	
199	%% ============================================================
200	\section{Full Experimental Results}
201	\label{sec:full_results}
202	
203	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
204	
205	\begin{table}[t]
206	\centering
207	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
208	\label{tab:full_qwen}
209	\small
210	\resizebox{\columnwidth}{!}{%
211	\begin{tabular}{lcccc}
212	\toprule
213	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
214	\midrule
215	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
216	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
217	VOTA                     & 99.41 & 98.66 & 99.08 & 99.05 $\pm$ 0.38 \\
218	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
219	label\_only     & 86.22 & 86.89 & 84.70 & 85.94 $\pm$ 1.12 \\
220	loop\_only      & 85.63 & 85.88 & 86.64 & 86.05 $\pm$ 0.52 \\
221	full\_trace     & 81.76 & 80.20 & 82.35 & 81.44 $\pm$ 1.11 \\
222	no\_trace       & 75.13 & ---   & ---   & --- \\
223	\bottomrule
224	\end{tabular}%
225	}
226	\end{table}
227	
228	\begin{table}[t]
229	\centering
230	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} is consistent across seeds: 99.33/99.50/99.33 ($\sigma{=}$0.10pp).}
231	\label{tab:full_deepseek}
232	\small
233	\resizebox{\columnwidth}{!}{%
234	\begin{tabular}{llcc}
235	\toprule
236	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
237	\midrule
238	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
239	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
240	exception\_only & 123 & 99.50 & \\
241	\midrule
242	VOTA                     & 42  & 84.45 & training failure; fail recall = 45.4\% \\
243	VOTA                     & 123 & 99.16 & \\
244	VOTA                     & 456 & 99.33 & \\
245	no\_trace       & 42  & 73.36 & \\
246	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
247	\bottomrule
248	\end{tabular}%
249	}
250	\end{table}
251	
252	%% ============================================================
253	\section{Tokenizer and Truncation Analysis}
254	\label{sec:tokenizer_analysis}
255	
256	DeepSeek VOTA seed 42 (84.45\%) is a training failure driven by tokenizer-induced truncation.
257	Re-evaluation of the seed 42 checkpoint with the standard max\_length=2048 yields 16\% accuracy, consistent with complete model collapse rather than marginal degradation.
258	The previously reported 84.45\% was obtained with max\_length=16384, which partially bypasses tokenizer truncation.
259	Seeds 123 and 456, evaluated under identical conditions, achieve 99.16\% and 99.33\% respectively.
260	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
261	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
262	Seeds 123 and 456 (99.16\% and 99.33\%) demonstrate that DeepSeek can learn VOTA when LoRA initialization avoids the truncation-sensitive basin; the 2-seed mean (99.25\%$\pm$0.12) matches the cross-model VOTA range (98.74--99.54\%).
263	
264	A post-hoc group analysis on seed 42 provides directional evidence: partitioning test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
265	Per-class analysis (Table~\ref{tab:per_class}) shows that seed 42 achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}.
266	
267	Seed robustness is consistent across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), and DeepSeek achieves 99.39\%$\pm$0.10 (seeds 42/456: 99.33\%, seed 123: 99.50\%).
268	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
269	
270	%% ============================================================
271	\section{Persistent Error Analysis}
272	\label{sec:irreducible}
273	
274	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
275	Both samples (IDs 901 and 905) share the following characteristics:
276	
277	\begin{itemize}
278	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95), a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
279	\item \textbf{Ground-truth label:} \texttt{pass}.
280	\item \textbf{Predicted label:} \texttt{fail} (false negative).
281	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
282	\end{itemize}
283	
284	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
285	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines, even though the function executes correctly and the test passes.
286	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
287	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
288	
289	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
290	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
291	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
292	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
293	
294	%% ============================================================
295	\section{Exception Type Accuracy Breakdown}
296	\label{sec:exception_type}
297	
298	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
299	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
300	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
301	
302	\begin{table}[t]
303	\centering
304	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
305	\label{tab:exception_type}
306	\small
307	\begin{tabular}{lcc}
308	\toprule
309	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
310	\midrule
311	TypeError & 96 & 100\% \\
312	ValueError & 62 & 100\% \\
313	IndexError & 41 & 100\% \\
314	KeyError & 28 & 100\% \\
315	AttributeError & 19 & 100\% \\
316	AssertionError & 15 & 100\% \\
317	RecursionError & 12 & 100\% \\
318	Other Exception & 66 & 100\% \\
319	\midrule
320	GeneratorExit (BaseException) & 2 & 0\% \\
321	No exception (pass class) & 849 & 100\% \\
322	\bottomrule
323	\end{tabular}
324	\end{table}
325	
326	This is consistent with the model having learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
327	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
328	
329	%% ============================================================
330	\section{Exception Subcomponent Ablation}
331	\label{sec:exc_subcomponent}
332	
333	To test whether verdict prediction depends on a specific exception subcomponent or merely the binary presence of an exception event, we train Qwen-2.5-7B on three subcomponent-only conditions (seed 42, $N{=}1{,}190$).
334	
335	\begin{table}[t]
336	\centering
337	\caption{Exception subcomponent ablation (Qwen-2.5-7B, seed 42, $N{=}1{,}190$). All three subcomponents independently achieve ${\geq}$99.50\%. $^\dag$Retains \texttt{[ERROR]} format marker; $^\ddag$no format markers, bare exception class name only.}
338	\label{tab:exc_subcomponent}
339	\small
340	\begin{tabular}{lccc}
341	\toprule
342	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{Fail R} & \textbf{Pass R} \\
343	\midrule
344	exc\_type\_only$^\dag$ & \textbf{100.00} & 100.00 & 100.00 \\
345	exc\_stacktrace\_only$^\dag$ & 99.83 & 100.00 & 99.76 \\
346	exc\_message\_only$^\ddag$ & 99.50 & 100.00 & 99.29 \\
347	\midrule
348	exception\_only (ref.) & 99.83 & 100.00 & 99.76 \\
349	\bottomrule
350	\end{tabular}
351	\end{table}
352	
353	All three subcomponents independently achieve ${\geq}$99.50\% with 100\% fail recall (Table~\ref{tab:exc_subcomponent}), showing that no single subcomponent is necessary for Tier~1 performance.
354	
355	\paragraph{Format marker confound.}
356	\texttt{exc\_type\_only} and \texttt{exc\_stacktrace\_only} retain the \texttt{[ERROR]} prefix marker present in the full \texttt{exception\_only} format; \texttt{exc\_message\_only} contains only the bare exception class name and message text without any format markers.
357	Because the marker alone is sufficient for near-perfect regex accuracy (B5: 99.33\%; \S\ref{sec:nomarker}), \texttt{exc\_type\_only} (100.00\%) and \texttt{exc\_stacktrace\_only} (99.83\%) are confounded with marker-based classification; we therefore do not make hierarchy claims among subcomponents.
358	\texttt{exc\_message\_only} (99.50\%) provides a clean test: without any format markers, it achieves accuracy comparable to the full \texttt{exception\_only} condition (99.83\%), complementing the dedicated marker-removal ablation (\texttt{nomarker}: 97.65\%; \S\ref{sec:nomarker}) as additional evidence that the model learns semantic exception patterns rather than format shortcuts.
359	
360	%% ============================================================
361	\section{Trace Length Ablation}
362	\label{sec:trace_length_full}
363	
364	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
365	
366	\begin{table}[t]
367	\centering
368	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
369	\label{tab:trace_length}
370	\small
371	\begin{tabular}{llcc}
372	\toprule
373	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
374	\midrule
375	Head & 256  & 78.82 & [76.4, 81.0] \\
376	Head & 512  & 80.42 & [78.2, 82.6] \\
377	Head & 1024 & 77.23 & [74.9, 79.6] \\
378	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
379	\midrule
380	Tail & 256  & 77.48 & --- \\
381	Tail & 512  & 93.61 & --- \\
382	Tail & 1024 & 96.47 & --- \\
383	Tail & 2048 & 97.31 & --- \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	% Budget curve figure moved to main text (Figure~\ref{fig:budget_curve}).
389	
390	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:budget_curve}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
391	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
392	
393	\begin{table}[t]
394	\centering
395	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}.01$; ***$p{<}.001$.}
396	\label{tab:trace_length_pairwise}
397	\small
398	\resizebox{\columnwidth}{!}{%
399	\begin{tabular}{llccc}
400	\toprule
401	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
402	\midrule
403	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
404	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
405	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
406	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
407	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
408	\midrule
409	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
410	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
411	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
412	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
413	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
414	\midrule
415	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
416	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
417	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
418	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
419	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
420	\bottomrule
421	\end{tabular}%
422	}
423	\end{table}
424	
425	\paragraph{Non-monotonic pattern (head-truncation).}
426	Under head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%, a statistically significant 3.19pp drop ($p{=}.002$, 95\% CI [$-$5.29, $-$1.09]).
427	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}.001$), but 1024 tokens is not significantly better than \texttt{no\_trace} (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}.078$, 95\% CI [$-$0.17, $+$4.37]).
428	This non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.
429	Under tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.
430	
431	\paragraph{Comparison to baselines.}
432	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}.078$), indicating that raw trace content provides some signal but unreliably so.
433	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
434	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
435	
436	\paragraph{Interpretation.}
437	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
438	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
439	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
440	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
441	
442	\paragraph{Truncation direction.}
443	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
444	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
445	
446	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
447	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
448	This is consistent with the trace format: the globals module dump consumes the first ${\sim}$384 tail tokens (pure noise), so structured execution markers (\texttt{[Line~X]} variable values) only become visible when the budget exceeds this threshold.
449	
450	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
451	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) indicates that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
452	
453	\paragraph{Cross-model budget curve.}
454	Table~\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\times$ parameter range.
455	
456	\begin{table}[t]
457	\centering
458	\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). All four models exhibit a transition between tail-384 and tail-512 (+11--22pp). $\downarrow$: non-monotonic decrease. $^\dag$CodeLlama tail-384/512/1024 trained with label-only loss to address tokenizer-driven gradient dilution (\S\ref{sec:tokenizer_analysis}); tail-1024 reports best-epoch accuracy (epoch 1). CodeLlama tail entries are not directly comparable to other models (which use full-sequence loss). $^\ddag$CodeLlama tail-2048 outlier (41.8\%): LoRA long-sequence instability under label-only loss; excluded from cross-model analysis.}
459	\label{tab:tail_cross_model}
460	\small
461	\resizebox{\columnwidth}{!}{%
462	\begin{tabular}{lcccccc}
463	\toprule
464	\textbf{Model} & \textbf{tail-256} & \textbf{tail-384} & \textbf{tail-512} & \textbf{tail-1024} & \textbf{tail-2048} & \textbf{exc\_only} \\
465	\midrule
466	Qwen-7B (7B) & 78.9 & 79.9 & 93.6 & 96.5 & 97.3 & 99.83 \\
467	DeepSeek (6.7B) & 76.4 & 80.7 & 93.9 & 96.5 & 95.0$\downarrow$ & 99.33 \\
468	CodeLlama (13B) & 77.9 & 82.7$^\dag$ & 98.2$^\dag$ & 98.2$^\dag$ & 41.8$^\ddag$ & 99.89 \\
469	Qwen-1.5B (1.5B) & 72.6 & 73.6 & 95.6 & 96.6 & 97.9 & 99.83 \\
470	\bottomrule
471	\end{tabular}%
472	}
473	\end{table}
474	
475	\begin{table}[t]
476	\centering
477	\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--78.9\%, 6.3pp). $^\dag$CodeLlama tail-2048 pending retraining (\S\ref{sec:tokenizer_analysis}).}
478	\label{tab:head_vs_tail}
479	\small
480	\resizebox{\columnwidth}{!}{%
481	\begin{tabular}{lccc}
482	\toprule
483	\textbf{Model} & \textbf{head-2048 (\%)} & \textbf{tail-2048 (\%)} & \textbf{Gap (pp)} \\
484	\midrule
485	Qwen-1.5B & 75.3 & 97.9 & +22.6 \\
486	DeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\
487	CodeLlama-13B & 79.9 & ---$^\dag$ & ---$^\dag$ \\
488	Qwen-7B & 81.8 & 97.3 & +15.5 \\
489	\bottomrule
490	\end{tabular}%
491	}
492	\end{table}
493	
494	Four patterns emerge from the budget curve.
495	\emph{Phase transition between 384 and 512 tokens}: the tail-384 column reveals that the transition is not instantaneous at 256$\to$512 but localized between 384 and 512 tokens.
496	At tail-384, all four models remain near baseline (73.6--80.7\%), gaining only +1.0--4.8pp over tail-256.
497	The steep jump occurs at 384$\to$512: +13.7pp (Qwen-7B), +13.2pp (DeepSeek), +15.5pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.
498	This localizes the critical threshold to ${\sim}$400--500 tokens: below ${\sim}$384 tokens, the entire token budget is consumed by globals module dumps (pure noise); above ${\sim}$512, at least one \texttt{[Line~X]} execution event marker becomes visible, regardless of model capacity or architecture.
499	
500	\emph{Convergence at tail-512+}: once the sharp performance jump is crossed, accuracy converges across all models into a 93.6--98.2\% band at tail-512 (seed 42).
501	Multi-seed validation shows robustness: across all 12 model$\times$seed combinations at tail-512 (Table~\ref{tab:tail512_seeds}), all accuracies fall within [93.61\%, 98.24\%], a 4.63pp band that compresses the signal-poor tail-256 spread (6.3pp) by 27\%.
502	CodeLlama-13B shows perfect per-model convergence at tail-512: all three seeds achieve 98.24\% ($\sigma{=}$0), consistent with the 13B scale and label-only loss providing a stronger optimization signal in the signal-rich regime (Table~\ref{tab:tail512_seeds}).
503	However, CodeLlama's higher tail-512 accuracy may partly reflect label-only loss rather than model capacity; direct comparison with other models (which use full-sequence loss) is confounded by this training difference.
504	
505	\begin{table}[t]
506	\centering
507	\caption{Cross-seed convergence at the tail-512 truncation point ($N{=}1{,}190$ per seed). All 12 model$\times$seed combinations fall within a 4.63pp band [93.61\%, 98.24\%]. CodeLlama-13B achieves identical accuracy across all three seeds ($\sigma{=}$0).}
508	\label{tab:tail512_seeds}
509	\small
510	\resizebox{\columnwidth}{!}{%
511	\begin{tabular}{lccccr}
512	\toprule
513	\textbf{Model} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean} & \textbf{$\sigma$} \\
514	\midrule
515	Qwen-7B (7B)      & 93.61 & 96.00 & 97.65 & 95.75 & 2.05 \\
516	DeepSeek (6.7B)    & 93.95 & 95.04 & 96.10 & 95.03 & 1.08 \\
517	Qwen-1.5B (1.5B)  & 95.63 & 97.65 & 96.72 & 96.67 & 1.01 \\
518	CodeLlama (13B)    & 98.24 & 98.24 & 98.24 & \textbf{98.24} & \textbf{0.00} \\
519	\midrule
520	\multicolumn{4}{l}{Cross-model band} & \multicolumn{2}{r}{[93.61, 98.24] = 4.63pp} \\
521	\bottomrule
522	\end{tabular}%
523	}
524	\end{table}
525	
526	At tail-1024, four models reach 96.5--98.2\% (CodeLlama 98.2\% under label-only loss, three others 96.5--96.6\%).
527	Scale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\%, 6.3pp) compress dramatically in the signal-rich regime.
528	
529	\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\% band (6.5pp; Table~\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--78.9\%, 6.3pp).
530	When the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.
531	
532	\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\% vs.\ Qwen-7B 78.9\%, $-$6.3pp), mirroring the \texttt{no\_trace} scale pattern.
533	In the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\% vs.\ 93.6\% at tail-512; 97.9\% vs.\ 97.3\% at tail-2048), consistent with sufficient trace signal eliminating the capacity advantage.
534	
535	\emph{Non-monotonicity at long sequences}: two models show accuracy decreases beyond tail-1024.
536	DeepSeek-6.7B drops $-$1.5pp from tail-1024 (96.5\%) to tail-2048 (95.0\%), consistent with its known long-context sensitivity (\S\ref{sec:training_dynamics}).
537	CodeLlama-13B exhibits a more severe collapse: tail-2048 under label-only loss drops to 41.8\% (vs.\ tail-1024 = 98.2\%), which we attribute to LoRA long-sequence instability under the label-only loss regime; this outlier is excluded from cross-model tail-2048 analysis.
538	Qwen-7B and Qwen-1.5B increase monotonically across all budgets.
539	
540	Table~\ref{tab:head_vs_tail} shows the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.
541	The gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.
542	
543	%% ============================================================
544	\section{Calibration Analysis}
545	\label{sec:calibration_full}
546	
547	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
548	
549	\begin{table}[t]
550	\centering
551	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
552	\label{tab:calibration}
553	\small
554	\begin{tabular}{lcc}
555	\toprule
556	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
557	\midrule
558	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
559	exception\_only & 0.0027 & 0.0013 \\
560	VOTA & 0.0054 & 0.005 \\
561	full\_trace & 0.096 & 0.144 \\
562	no\_trace & 0.171 & 0.197 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
568	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
569	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
570	
571	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
572	
573	\paragraph{Cross-model calibration.}
574	Table~\ref{tab:calibration_cross} extends the calibration analysis to four models (1.5B--13B) under \texttt{exception\_only}.
575	All four models achieve ECE ${<}$ 0.007 and Brier ${<}$ 0.007, indicating that calibration quality generalizes across architectures and scales.
576	CodeLlama-13B achieves the lowest ECE (0.0020) and MCE (0.0411), while DeepSeek-6.7B shows the highest ECE (0.0064) and Brier (0.0061), consistent with its higher error rate (8 errors vs.\ 2 for Qwen/CodeLlama).
577	
578	\begin{table}[t]
579	\centering
580	\caption{Cross-model calibration for \texttt{exception\_only} ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score; MCE = maximum calibration error. All four models (1.5B--13B) achieve ECE ${<}$ 0.007.}
581	\label{tab:calibration_cross}
582	\small
583	\begin{tabular}{lccc}
584	\toprule
585	\textbf{Model} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} & \textbf{MCE $\downarrow$} \\
586	\midrule
587	Qwen-1.5B & \textbf{0.0020} & \textbf{0.0013} & --- \\
588	CodeLlama-13B & \textbf{0.0020} & \textbf{0.0013} & \textbf{0.0411} \\
589	Qwen-7B & 0.0027 & \textbf{0.0013} & 0.8355 \\
590	DeepSeek-6.7B & 0.0064 & 0.0061 & 0.7756 \\
591	\bottomrule
592	\end{tabular}
593	\end{table}
594	
595	\begin{figure}[t]
596	\centering
597	\includegraphics[width=\columnwidth]{fig2_calibration}
598	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
599	\label{fig:calibration}
600	\end{figure}
601	
602	%% ============================================================
603	\section{Error Overlap Analysis}
604	\label{sec:error_overlap}
605	
606	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
607	
608	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
609	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
610	
611	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
612	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
613	
614	This analysis indicates that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
615	
616	\begin{figure}[t]
617	\centering
618	\includegraphics[width=\columnwidth]{error_overlap}
619	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, indicating it operates on an independent signal dimension.}
620	\label{fig:error_overlap}
621	\end{figure}
622	
623	%% ============================================================
624	\section{Cross-Dataset Generalization: DebugBench}
625	\label{sec:debugbench_full}
626	
627	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}, a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
628	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
629	
630	\begin{table}[t]
631	\centering
632	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
633	\label{tab:debugbench}
634	\small
635	\begin{tabular}{lcc}
636	\toprule
637	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
638	\midrule
639	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
640	VOTA & 99.77 & [99.30, 100.00] \\
641	no\_trace & 96.71 & [94.80, 98.40] \\
642	\midrule
643	Majority baseline & 51.41 & --- \\
644	\bottomrule
645	\end{tabular}
646	\end{table}
647	
648	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
649	The \texttt{exception\_only} condition achieves perfect accuracy, showing that the exception-based representation generalizes to a different fault distribution without degradation.
650	
651	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\% (compared to 75.13\% on HumanEval+MBPP), leaving only 3.29pp of headroom for trace-based improvement.
652	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
653	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
654	
655	These results support exception-based verdict prediction as a generalizable approach: the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets. However, the narrow DebugBench margins are insufficient to independently validate trace importance.
656	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
657	
658	%% ============================================================
659	\section{Cross-Model Robustness Analysis}
660	\label{sec:robustness_analysis}
661	
662	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
663	Exception events are consistently the most effective component on both models, and their structural simplicity (a fixed-format error message) ensures that the relative advantage over richer representations holds across all seeds.
664	All three DeepSeek \texttt{exception\_only} seeds achieve ${\geq}$99.33\% (99.33/99.50/99.33, $\sigma{=}$0.10pp), matching Qwen and CodeLlama at ${\geq}$99.83\%.
665	VOTA achieves ${\geq}$98.57\% across all models when excluding outlier seeds (cross-model range: 0.80pp), but DeepSeek VOTA exhibits seed-dependent instability: seed 42 (84.45\%) is a training failure due to tokenizer-induced truncation (91.7\% of training samples affected), while seeds 123/456 (99.16\%/99.33\%) match cross-model performance.
666	This VOTA instability is confounded by tokenizer efficiency and base model differences \citep{yang2024generalization}.
667	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
668	The resulting 0.50pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
669	The practical implication is that trace-based systems should default to the simplest sufficient signal.
670	
671	%% ============================================================
672	\section{Training Dynamics and Loss Decoupling}
673	\label{sec:training_dynamics}
674	
675	\begin{figure}[t]
676	\centering
677	\includegraphics[width=\columnwidth]{training_dynamics}
678	\caption{Training dynamics: \texttt{exception\_only} converges to 99.83\% by step 150; \texttt{full\_trace} with label-only loss oscillates (82--89\%) without convergence.}
679	\label{fig:training_dynamics}
680	\end{figure}
681	
682	The DeepSeek \texttt{exception\_only} results are consistent across all three seeds (99.33/99.50/99.33, $\sigma{=}$0.10pp), matching Qwen's cross-seed stability.
683	Epoch-level analysis shows mild degradation in seed 42: accuracy peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), while seed 456 shows no degradation (99.33\% at both epochs).
684	Early stopping may yield marginal gains, but the epoch effect is small (${\leq}$0.5pp).
685	The practical recommendation: for deployment, use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training loss, and train multiple seeds to select the best.
686	
687	The contrast with VOTA is instructive: DeepSeek VOTA seed 42 accuracy monotonically increases from 78.15\% to 84.45\% across epochs, consistent with a performance limit from high trace truncation (91.7\% of samples; \S\ref{sec:tokenizer_analysis}).
688	Seeds 123/456, which avoid the truncation-sensitive initialization basin, achieve 99.16\%/99.33\%, indicating that the deficit is seed-specific rather than a fundamental model limitation.
689	
690	%% ============================================================
691	\section{Deduplication Statistics}
692	\label{sec:dedup_stats}
693	
694	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
695	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format (correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic), the dataset contains duplicate rows.
696	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
697	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
698	
699	\paragraph{Problem-level partitioning and sensitivity analysis.}
700	Data is partitioned at the problem level: 472 training problems and 119 test problems, with zero crossover.
701	Duplicates arise from multiple candidate solutions per problem (up to 10 solutions each), not from cross-problem overlap.
702	To verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\times$ 4 models, minus conditions not run): deduplication produces a negligible ($<$0.1pp) accuracy delta in every case.
703	This shows that duplicate samples neither inflate nor deflate accuracy, because duplicates share the same ground-truth label and the model's prediction is deterministic at inference time.
704	Duplicates arise because the \texttt{exception\_only} format collapses passing solutions (which share identical ``no exception'' output) into identical rows; the redundancy is a property of the format's compactness for pass-class samples.
705	The \texttt{exception\_only} test set contains 48.99\% such duplicates; all confidence intervals treat samples as independent Bernoulli trials.
706	
707	\begin{table}[t]
708	\centering
709	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
710	\label{tab:dedup}
711	\small
712	\begin{tabular}{lccc}
713	\toprule
714	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
715	\midrule
716	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
717	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
718	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
719	\bottomrule
720	\end{tabular}
721	\end{table}
722	
723	%% ============================================================
724	\section{Regex Baseline Analysis}
725	\label{sec:regex_baselines}
726	
727	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
728	
729	\begin{table}[t]
730	\centering
731	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
732	\label{tab:regex}
733	\small
734	\resizebox{\columnwidth}{!}{%
735	\begin{tabular}{llc}
736	\toprule
737	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
738	\midrule
739	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
740	B2: Traceback presence & string match & 71.51 \\
741	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
742	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
743	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
744	B6: Error count $\geq$2 & count threshold & 92.02 \\
745	\midrule
746	VOTA format regex & best regex on VOTA traces & 75.55 \\
747	full\_trace format regex & best regex on full traces & 77.39 \\
748	\bottomrule
749	\end{tabular}%
750	}
751	\end{table}
752	
753	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
754	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught; the program passes despite an exception occurring in the trace.
755	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
756	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}.041$, indicating a statistically significant difference.
757	
758	\paragraph{Cross-format comparison.}
759	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
760	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
761	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
762	
763	\begin{table}[t]
764	\centering
765	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
766	\label{tab:regex_cross_format}
767	\small
768	\begin{tabular}{lccc}
769	\toprule
770	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
771	\midrule
772	exception\_only & 99.83 & 93.61 & +6.22 \\
773	VOTA & 99.05 & 75.55 & +23.50 \\
774	full\_trace & 81.76 & 77.39 & +4.37 \\
775	no\_trace & 75.13 & 71.51 & +3.62 \\
776	\bottomrule
777	\end{tabular}
778	\end{table}
779	
780	%% ============================================================
781	\section{Cross-Model Zero-Shot Comparison}
782	\label{sec:zeroshot_cross_model}
783	
784	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
785	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
786	SFT compresses the 42.44pp zero-shot range to 0.50pp, eliminating architecture-dependent variance.
787	
788	\begin{table}[t]
789	\centering
790	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.50pp.}
791	\label{tab:zeroshot_cross_model}
792	\small
793	\resizebox{\columnwidth}{!}{%
794	\begin{tabular}{llccc}
795	\toprule
796	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
797	\midrule
798	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
799	DeepSeek-6.7B & 6.7B & 90.59 & 99.39 & +8.80 \\
800	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
801	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
802	\midrule
803	Range & --- & 42.44pp & 0.50pp & --- \\
804	\bottomrule
805	\end{tabular}%
806	}
807	\end{table}
808	
809	\subsection{Calibration Analysis}
810	\label{sec:calibration_analysis}
811	
812	\begin{table}[h]
813	\centering
814	\caption{Model calibration on \texttt{exception\_only} (seed 42). All four models achieve ECE $<$ 0.005, indicating that near-perfect accuracy reflects genuine confidence rather than overfit predictions.}
815	\label{tab:calibration_model_level}
816	\small
817	\resizebox{\columnwidth}{!}{%
818	\begin{tabular}{lcccc}
819	\toprule
820	\textbf{Model} & \textbf{Accuracy} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} & \textbf{Mean Conf.} \\
821	\midrule
822	Qwen-2.5-1.5B & 99.83\% & 0.0014 & 0.0013 & 99.82\% \\
823	Qwen-2.5-7B & 99.83\% & 0.0017 & 0.0013 & 99.80\% \\
824	CodeLlama-13B & 99.83\% & 0.0020 & 0.0013 & 99.63\% \\
825	DeepSeek-6.7B & 99.33\% & 0.0048 & 0.0059 & 99.71\% \\
826	\bottomrule
827	\end{tabular}%
828	}
829	\end{table}
830	
831	%% ============================================================
832	\section{Use of AI Assistants}
833	\label{app:ai-assistants}
834	
835	We used Claude (Anthropic) as an AI coding and writing assistant
836	throughout this work. Specifically:
837	\begin{itemize}
838	    \item \textbf{Code:} drafting experiment scripts, data-processing
839	    pipelines, and analysis utilities; debugging and refactoring.
840	    \item \textbf{Writing:} drafting and revising paper sections,
841	    polishing prose, and reformatting LaTeX.
842	    \item \textbf{Literature:} summarizing related papers to inform
843	    the related-work section.
844	\end{itemize}
845	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "75ae9072-f93a-4c75-bc07-a5c065b308c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex",
      "content": "\\section{Per-Class Performance Breakdown}\n\\label{sec:per_class}\n\nTable~\\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA seed 42 is a training failure (84.45\\%, fail recall = 45.4\\%) due to tokenizer-driven truncation; seeds 123/456 achieve 99.16\\%/99.33\\%.}\n\\label{tab:per_class}\n\\small\n\\begin{tabular}{llccccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Model} & \\textbf{Acc} & \\textbf{Pass P} & \\textbf{Pass R} & \\textbf{Pass F1} & \\textbf{Fail P} & \\textbf{Fail R} & \\textbf{Fail F1} \\\\\n\\midrule\nNo Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\\\\nFull Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\\\\nFull Trace (LO)   & Qwen-2.5-7B & 85.94 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\\\\nVOTA              & Qwen-2.5-7B & 99.05 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\\\\nException Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\\\\nAE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\\\\nLoop Only         & Qwen-2.5-7B & 86.05 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\\\\nVOTA\\_no\\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\\\\n\\midrule\nNo Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\\\\nFull Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\\\\nVOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\\\\nException Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\\\\nAE Only           & DeepSeek-6.7B & 98.74 & 98.40 & 99.90 & 99.10 & 99.70 & 95.90 & 97.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n%% ============================================================\n\\section{Training Details}\n\\label{sec:training_details}\n\nTable~\\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.\nAll experiments use the HuggingFace TRL \\texttt{SFTTrainer} with LoRA \\citep{hu2022lora} applied to all linear layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training hyperparameters (shared across all conditions).}\n\\label{tab:hyperparams}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll}\n\\toprule\n\\textbf{Hyperparameter} & \\textbf{Value} \\\\\n\\midrule\nLoRA rank ($r$)            & 16 \\\\\nLoRA alpha ($\\alpha$)      & 32 \\\\\nLoRA dropout               & 0.05 \\\\\nLoRA target modules        & all linear layers \\\\\n\\midrule\nEpochs                     & 3 \\\\\nPer-device batch size       & 4 \\\\\nGradient accumulation steps & 8 \\\\\nEffective batch size        & 32 \\\\\n\\midrule\nLearning rate               & $2 \\times 10^{-4}$ \\\\\nLR scheduler                & linear decay \\\\\nWarmup ratio                & 0.1 \\\\\nWeight decay                & 0.01 \\\\\n\\midrule\nMax sequence length         & 2048 tokens \\\\\nPrimary seed                & 42 \\\\\nRobustness seeds            & 123, 456 \\\\\n\\midrule\nHardware                    & 1$\\times$ enterprise-grade GPU (${\\geq}$80\\,GB VRAM) \\\\\nFramework                   & HuggingFace TRL SFTTrainer \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nTable~\\ref{tab:train_time} reports per-condition training wall-clock times.\nConditions with longer trace inputs (e.g., \\texttt{full\\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training wall-clock time per condition on a single enterprise-grade GPU (${\\geq}$80\\,GB VRAM). Where multiple seeds were run, individual times are listed.}\n\\label{tab:train_time}\n\\small\n\\begin{tabular}{llr}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed(s)} & \\textbf{Time (h)} \\\\\n\\midrule\nno\\_trace       & 42         & ${\\sim}$0.5 \\\\\nfull\\_trace     & 42         & ${\\sim}$2.2 \\\\\nlabel\\_only     & 42         & ${\\sim}$2.2 \\\\\nVOTA                     & 42         & ${\\sim}$2.3 \\\\\nexception\\_only & 42         & ${\\sim}$2.1 \\\\\nexception\\_only & 123        & ${\\sim}$2.1 \\\\\nexception\\_only & 456        & ${\\sim}$1.3 \\\\\nae\\_only        & 42         & ${\\sim}$1.8 \\\\\nloop\\_only      & 42         & ${\\sim}$2.1 \\\\\nVOTA\\_no\\_ae    & 42         & ${\\sim}$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{VOTA Extraction Algorithm}\n\\label{sec:vota_algorithm}\n\nAlgorithm~\\ref{alg:vota} describes the three-component VOTA extraction pipeline applied to a raw \\texttt{sys.settrace} execution log.\n\n\\begin{algorithm}[t]\n\\caption{VOTA Trace Extraction}\n\\label{alg:vota}\n\\small\n\\begin{algorithmic}[1]\n\\REQUIRE Raw trace $T$ from \\texttt{sys.settrace} (list of events)\n\\ENSURE Compressed VOTA representation $V$\n\\STATE $V \\leftarrow$ empty string\n\\STATE \\textbf{// Component 1: Exception summary}\n\\FOR{each event $e$ in $T$ with type \\texttt{exception}}\n  \\STATE Parse traceback $\\rightarrow$ extract error type, message, file, line\n  \\STATE Append \\texttt{[ERROR] type: message (file:line)} to $V$\n\\ENDFOR\n\\IF{no exception events found}\n  \\STATE Append \\texttt{[No exception data in trace]} to $V$\n\\ENDIF\n\\STATE \\textbf{// Component 2: Assertion-point comparison}\n\\FOR{each \\texttt{assert} or \\texttt{return} event $e$ in $T$}\n  \\STATE Extract actual value from execution state\n  \\STATE Extract expected value from test assertion\n  \\STATE Append \\texttt{[ASSERT] actual=... expected=... match=T/F} to $V$\n\\ENDFOR\n\\STATE \\textbf{// Component 3: Loop compression}\n\\FOR{each consecutive repeated line sequence $S$ in $T$}\n  \\IF{$|S| \\geq 2$ iterations of same loop body}\n    \\STATE Replace $S$ with single iteration + \\texttt{[repeated $\\times$N]}\n  \\ENDIF\n\\ENDFOR\n\\STATE Append compressed non-exception lines to $V$\n\\RETURN $V$\n\\end{algorithmic}\n\\end{algorithm}\n\n%% ============================================================\n\\section{VOTA Trace Examples}\n\\label{sec:vota_examples}\n\nWe provide two representative VOTA trace examples illustrating the fail and pass cases.\nIn the fail case, the exception event provides an unambiguous fault signal.\nIn the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.\n\n\\paragraph{Fail example.}\nA \\texttt{ZeroDivisionError} triggers an \\texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \\texttt{fail}.\n\n\\begin{scriptsize}\n\\begin{verbatim}\n## Function\ndef divide(a, b):\n    return a / b\n\n## Test Input\ndivide(1, 0)\n\n## Expected Output\ninf\n\n## VOTA Trace\n[ERROR] ZeroDivisionError: division by zero\n\n## Verdict\nfail\n\\end{verbatim}\n\\end{scriptsize}\n\n\\paragraph{Pass example.}\nNo exception is raised, and the assertion point confirms that the actual output matches the expected value.\n\n\\begin{scriptsize}\n\\begin{verbatim}\n## Function\ndef add(a, b):\n    return a + b\n\n## Test Input\nadd(2, 3)\n\n## Expected Output\n5\n\n## VOTA Trace\n[LOOP] No loops detected.\n[ASSERT] actual=5, expected=5\n\n## Verdict\npass\n\\end{verbatim}\n\\end{scriptsize}\n\nThese examples illustrate the core asymmetry exploited by the \\texttt{exception\\_only} condition: fail cases produce an explicit \\texttt{[ERROR]} event, while pass cases are characterized by its absence.\nThis binary signal (presence vs.\\ absence of an exception) is sufficient for near-perfect verdict prediction.\n\n%% ============================================================\n\\section{Full Experimental Results}\n\\label{sec:full_results}\n\nTables~\\ref{tab:full_qwen} and \\ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \\texttt{exception\\_only} achieves 99.83\\% across all three seeds ($\\sigma{=}$0). \\texttt{ae\\_only} achieves 99.64\\% mean ($\\pm$0.49; seed 123 at 99.08\\% is the outlier).}\n\\label{tab:full_qwen}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\nexception\\_only & 99.83 & 99.83 & 99.83 & 99.83 $\\pm$ 0.00 \\\\\nae\\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\\pm$ 0.49 \\\\\nVOTA                     & 99.41 & 98.66 & 99.08 & 99.05 $\\pm$ 0.38 \\\\\nVOTA\\_no\\_ae    & 99.41 & ---   & ---   & --- \\\\\nlabel\\_only     & 86.22 & 86.89 & 84.70 & 85.94 $\\pm$ 1.12 \\\\\nloop\\_only      & 85.63 & 85.88 & 86.64 & 86.05 $\\pm$ 0.52 \\\\\nfull\\_trace     & 81.76 & 80.20 & 82.35 & 81.44 $\\pm$ 1.11 \\\\\nno\\_trace       & 75.13 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \\texttt{exception\\_only} is consistent across seeds: 99.33/99.50/99.33 ($\\sigma{=}$0.10pp).}\n\\label{tab:full_deepseek}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Accuracy} & \\textbf{Notes} \\\\\n\\midrule\nexception\\_only & 42  & 99.33 & epoch 1: 99.83 \\\\\nexception\\_only & 456 & 99.33 & CI [98.82, 99.75] \\\\\nexception\\_only & 123 & 99.50 & \\\\\n\\midrule\nVOTA                     & 42  & 84.45 & training failure; fail recall = 45.4\\% \\\\\nVOTA                     & 123 & 99.16 & \\\\\nVOTA                     & 456 & 99.33 & \\\\\nno\\_trace       & 42  & 73.36 & \\\\\nfull\\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n%% ============================================================\n\\section{Tokenizer and Truncation Analysis}\n\\label{sec:tokenizer_analysis}\n\nDeepSeek VOTA seed 42 (84.45\\%) is a training failure driven by tokenizer-induced truncation.\nRe-evaluation of the seed 42 checkpoint with the standard max\\_length=2048 yields 16\\% accuracy, consistent with complete model collapse rather than marginal degradation.\nThe previously reported 84.45\\% was obtained with max\\_length=16384, which partially bypasses tokenizer truncation.\nSeeds 123 and 456, evaluated under identical conditions, achieve 99.16\\% and 99.33\\% respectively.\nThe DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.\nThe training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.\nSeeds 123 and 456 (99.16\\% and 99.33\\%) demonstrate that DeepSeek can learn VOTA when LoRA initialization avoids the truncation-sensitive basin; the 2-seed mean (99.25\\%$\\pm$0.12) matches the cross-model VOTA range (98.74--99.54\\%).\n\nA post-hoc group analysis on seed 42 provides directional evidence: partitioning test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\\% (95\\% CI [80.75\\%, 85.24\\%]; Fisher exact $p{<}.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\\%).\nPer-class analysis (Table~\\ref{tab:per_class}) shows that seed 42 achieves 100\\% fail precision but only 45.43\\% fail recall, systematically defaulting to \\texttt{pass}.\n\nSeed robustness is consistent across models: Qwen \\texttt{exception\\_only} produces identical 99.83\\% across all three seeds ($\\sigma{=}0$), and DeepSeek achieves 99.39\\%$\\pm$0.10 (seeds 42/456: 99.33\\%, seed 123: 99.50\\%).\nBecause \\texttt{exception\\_only} test inputs contain 48.99\\% duplicates (607 unique of 1,190; \\S\\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\\% (Wilson CI [98.81, 99.91]).\n\n%% ============================================================\n\\section{Persistent Error Analysis}\n\\label{sec:irreducible}\n\nThe \\texttt{exception\\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\\% overlap across seeds.\nBoth samples (IDs 901 and 905) share the following characteristics:\n\n\\begin{itemize}\n\\item \\textbf{Function:} \\texttt{check\\_dict\\_case} (HumanEval/95), a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.\n\\item \\textbf{Ground-truth label:} \\texttt{pass}.\n\\item \\textbf{Predicted label:} \\texttt{fail} (false negative).\n\\item \\textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.\n\\end{itemize}\n\nManual inspection reveals the root cause: \\texttt{check\\_dict\\_case} uses \\texttt{all()} over a generator expression, and Python's \\texttt{all()} short-circuits on the first \\texttt{True} value, raising \\texttt{GeneratorExit} to terminate the generator.\nBecause \\texttt{GeneratorExit} is a \\texttt{BaseException} subclass, the tracer records it as seven \\texttt{[ERROR] GeneratorExit} lines, even though the function executes correctly and the test passes.\nThe model observes these spurious error markers and reasonably but incorrectly predicts \\texttt{fail}.\nThis is not a model failure but a representation ambiguity: the \\texttt{exception\\_only} format cannot distinguish genuine exceptions from benign \\texttt{BaseException} subclasses triggered by Python's iterator protocol.\n\nMost configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\\{901, 905\\}$.\nHowever, CodeLlama-13B seed 123 achieves 100\\% accuracy (0/1190 errors), correctly classifying both samples.\nThis demonstrates that 99.83\\% is a near-perfect \\emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.\nThe practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.\n\n%% ============================================================\n\\section{Exception Type Accuracy Breakdown}\n\\label{sec:exception_type}\n\nTable~\\ref{tab:exception_type} reports \\texttt{exception\\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).\nAll standard exception types (\\texttt{TypeError}, \\texttt{ValueError}, \\texttt{IndexError}, etc.) achieve 100\\% accuracy.\nThe only misclassifications arise from \\texttt{GeneratorExit}, a \\texttt{BaseException} subclass that is not an \\texttt{Exception}. It is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception type accuracy breakdown for \\texttt{exception\\_only} (Qwen-7B, seed=42). All true error types achieve 100\\%. The only failures come from \\texttt{GeneratorExit} (a \\texttt{BaseException} subclass, not an \\texttt{Exception}), which appears in 2 passing samples.}\n\\label{tab:exception_type}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Exception Type} & \\textbf{Samples} & \\textbf{Accuracy} \\\\\n\\midrule\nTypeError & 96 & 100\\% \\\\\nValueError & 62 & 100\\% \\\\\nIndexError & 41 & 100\\% \\\\\nKeyError & 28 & 100\\% \\\\\nAttributeError & 19 & 100\\% \\\\\nAssertionError & 15 & 100\\% \\\\\nRecursionError & 12 & 100\\% \\\\\nOther Exception & 66 & 100\\% \\\\\n\\midrule\nGeneratorExit (BaseException) & 2 & 0\\% \\\\\nNo exception (pass class) & 849 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis is consistent with the model having learned a clean decision boundary: any true \\texttt{Exception} subclass in the trace implies failure.\nThe \\texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \\S\\ref{sec:irreducible}.\n\n%% ============================================================\n\\section{Exception Subcomponent Ablation}\n\\label{sec:exc_subcomponent}\n\nTo test whether verdict prediction depends on a specific exception subcomponent or merely the binary presence of an exception event, we train Qwen-2.5-7B on three subcomponent-only conditions (seed 42, $N{=}1{,}190$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Exception subcomponent ablation (Qwen-2.5-7B, seed 42, $N{=}1{,}190$). All three subcomponents independently achieve ${\\geq}$99.50\\%. $^\\dag$Retains \\texttt{[ERROR]} format marker; $^\\ddag$no format markers, bare exception class name only.}\n\\label{tab:exc_subcomponent}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{Fail R} & \\textbf{Pass R} \\\\\n\\midrule\nexc\\_type\\_only$^\\dag$ & \\textbf{100.00} & 100.00 & 100.00 \\\\\nexc\\_stacktrace\\_only$^\\dag$ & 99.83 & 100.00 & 99.76 \\\\\nexc\\_message\\_only$^\\ddag$ & 99.50 & 100.00 & 99.29 \\\\\n\\midrule\nexception\\_only (ref.) & 99.83 & 100.00 & 99.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three subcomponents independently achieve ${\\geq}$99.50\\% with 100\\% fail recall (Table~\\ref{tab:exc_subcomponent}), showing that no single subcomponent is necessary for Tier~1 performance.\n\n\\paragraph{Format marker confound.}\n\\texttt{exc\\_type\\_only} and \\texttt{exc\\_stacktrace\\_only} retain the \\texttt{[ERROR]} prefix marker present in the full \\texttt{exception\\_only} format; \\texttt{exc\\_message\\_only} contains only the bare exception class name and message text without any format markers.\nBecause the marker alone is sufficient for near-perfect regex accuracy (B5: 99.33\\%; \\S\\ref{sec:nomarker}), \\texttt{exc\\_type\\_only} (100.00\\%) and \\texttt{exc\\_stacktrace\\_only} (99.83\\%) are confounded with marker-based classification; we therefore do not make hierarchy claims among subcomponents.\n\\texttt{exc\\_message\\_only} (99.50\\%) provides a clean test: without any format markers, it achieves accuracy comparable to the full \\texttt{exception\\_only} condition (99.83\\%), complementing the dedicated marker-removal ablation (\\texttt{nomarker}: 97.65\\%; \\S\\ref{sec:nomarker}) as additional evidence that the model learns semantic exception patterns rather than format shortcuts.\n\n%% ============================================================\n\\section{Trace Length Ablation}\n\\label{sec:trace_length_full}\n\nTo test whether the \\texttt{full\\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.\n\n\\begin{table}[t]\n\\centering\n\\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:trace_length}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Direction} & \\textbf{Max Tokens} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nHead & 256  & 78.82 & [76.4, 81.0] \\\\\nHead & 512  & 80.42 & [78.2, 82.6] \\\\\nHead & 1024 & 77.23 & [74.9, 79.6] \\\\\nHead & no\\_limit ($\\infty$) & 81.76 & [79.7, 83.9] \\\\\n\\midrule\nTail & 256  & 77.48 & --- \\\\\nTail & 512  & 93.61 & --- \\\\\nTail & 1024 & 96.47 & --- \\\\\nTail & 2048 & 97.31 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Budget curve figure moved to main text (Figure~\\ref{fig:budget_curve}).\n\nAs shown in Table~\\ref{tab:trace_length} and Figure~\\ref{fig:budget_curve}, all four trace length conditions fall within a 5pp range (77.2\\%--81.8\\%).\nTo quantify the reliability of the observed differences, Table~\\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}.01$; ***$p{<}.001$.}\n\\label{tab:trace_length_pairwise}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n& \\textbf{Comparison} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} & \\textbf{$p$-value} \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize Budget}}\n& 512 vs.\\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\\\\n& 1024 vs.\\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\\\\n& no\\_limit vs.\\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\\\\n& no\\_limit vs.\\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ no\\_trace}}\n& 256 $-$ no\\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\\\\n& 512 $-$ no\\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\\\\n& 1024 $-$ no\\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\\\\n& no\\_limit $-$ no\\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\\\\n\\midrule\n\\multirow{4}{*}{\\rotatebox{90}{\\scriptsize vs.\\ exc.}}\n& 256 $-$ exc\\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\\\\n& 512 $-$ exc\\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\\\\n& 1024 $-$ exc\\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\\\\n& no\\_limit $-$ exc\\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Non-monotonic pattern (head-truncation).}\nUnder head-truncation (retaining trace prefixes), the trend is non-monotonic: 512 tokens (80.42\\%) slightly outperforms 256 tokens (78.82\\%), but doubling to 1024 tokens \\emph{decreases} accuracy to 77.23\\%, a statistically significant 3.19pp drop ($p{=}.002$, 95\\% CI [$-$5.29, $-$1.09]).\nThe no-limit condition (81.76\\%) recovers and significantly exceeds 1024 tokens ($p{<}.001$), but 1024 tokens is not significantly better than \\texttt{no\\_trace} (75.13\\%; $\\Delta{=}{+}2.10$pp, $p{=}.078$, 95\\% CI [$-$0.17, $+$4.37]).\nThis non-monotonicity is specific to head-truncation: the 1024-token prefix retains enough irrelevant content to mislead the model while discarding diagnostic events that appear near the trace terminus.\nUnder tail-truncation, accuracy increases monotonically for Qwen-7B and Qwen-1.5B (Table~\\ref{tab:tail_cross_model}); only DeepSeek-6.7B shows a mild $-$1.5pp decrease at tail-1024$\\to$tail-2048, attributable to architecture-specific long-context sensitivity rather than a systematic mid-length pathology.\n\n\\paragraph{Comparison to baselines.}\nAll four trace budget conditions significantly exceed \\texttt{no\\_trace} except 1024 tokens ($p{=}.078$), indicating that raw trace content provides some signal but unreliably so.\nThe gap to \\texttt{exception\\_only} (99.83\\%) is massive for every budget condition (18--23pp, all $p{<}.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.\nThe best full-trace condition (no\\_limit, 81.76\\%) still lags \\texttt{exception\\_only} by 18.07pp (95\\% CI [$-$20.34, $-$15.88]).\n\n\\paragraph{Interpretation.}\nThese results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.\nThe non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.\nThe result reinforces the information density interpretation (\\S\\ref{sec:density}): the gap between full traces and VOTA is driven by the \\emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \\emph{length}.\nIn contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\\S\\ref{sec:cross_model}).\n\n\\paragraph{Truncation direction.}\nTail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \\texttt{tail\\_2048} achieves 97.31\\% vs.\\ \\texttt{head\\_2048} (no\\_limit) at 81.76\\%, a 15.55pp improvement.\nEven \\texttt{tail\\_512} (93.61\\%) exceeds every head-truncation condition by over 11pp.\n\nHowever, \\texttt{tail\\_256} (77.48\\%) performs at the \\texttt{no\\_trace} baseline level (75.13\\%), indicating that the diagnostic signal does not reside in the very last trace lines.\nThe critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.\nThis is consistent with the trace format: the globals module dump consumes the first ${\\sim}$384 tail tokens (pure noise), so structured execution markers (\\texttt{[Line~X]} variable values) only become visible when the budget exceeds this threshold.\n\nThe 18.07pp gap from \\texttt{full\\_trace} to \\texttt{exception\\_only} decomposes as: 86\\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\\% residual content noise (the 2.52pp gap from \\texttt{tail\\_2048} to \\texttt{exception\\_only} that persists regardless of truncation direction).\nThe fact that \\texttt{exception\\_only} (99.83\\%) still outperforms \\texttt{tail\\_2048} (97.31\\%) indicates that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.\n\n\\paragraph{Cross-model budget curve.}\nTable~\\ref{tab:tail_cross_model} extends the tail-truncation analysis to a full budget sweep across four models spanning three architecture families and an 8.7$\\times$ parameter range.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model tail-truncation budget curve ($N{=}1{,}190$). All four models exhibit a transition between tail-384 and tail-512 (+11--22pp). $\\downarrow$: non-monotonic decrease. $^\\dag$CodeLlama tail-384/512/1024 trained with label-only loss to address tokenizer-driven gradient dilution (\\S\\ref{sec:tokenizer_analysis}); tail-1024 reports best-epoch accuracy (epoch 1). CodeLlama tail entries are not directly comparable to other models (which use full-sequence loss). $^\\ddag$CodeLlama tail-2048 outlier (41.8\\%): LoRA long-sequence instability under label-only loss; excluded from cross-model analysis.}\n\\label{tab:tail_cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{tail-256} & \\textbf{tail-384} & \\textbf{tail-512} & \\textbf{tail-1024} & \\textbf{tail-2048} & \\textbf{exc\\_only} \\\\\n\\midrule\nQwen-7B (7B) & 78.9 & 79.9 & 93.6 & 96.5 & 97.3 & 99.83 \\\\\nDeepSeek (6.7B) & 76.4 & 80.7 & 93.9 & 96.5 & 95.0$\\downarrow$ & 99.33 \\\\\nCodeLlama (13B) & 77.9 & 82.7$^\\dag$ & 98.2$^\\dag$ & 98.2$^\\dag$ & 41.8$^\\ddag$ & 99.89 \\\\\nQwen-1.5B (1.5B) & 72.6 & 73.6 & 95.6 & 96.6 & 97.9 & 99.83 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model truncation direction comparison ($N{=}1{,}190$). Head-truncation retains the first 2,048 tokens; tail-truncation retains the last 2,048. All four models' head-2048 accuracies converge into a narrow 75.3--81.8\\% band (6.5pp), comparable to the tail-256 signal-poor band (72.6--78.9\\%, 6.3pp). $^\\dag$CodeLlama tail-2048 pending retraining (\\S\\ref{sec:tokenizer_analysis}).}\n\\label{tab:head_vs_tail}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{head-2048 (\\%)} & \\textbf{tail-2048 (\\%)} & \\textbf{Gap (pp)} \\\\\n\\midrule\nQwen-1.5B & 75.3 & 97.9 & +22.6 \\\\\nDeepSeek-6.7B & 78.7 & 95.0 & +16.3 \\\\\nCodeLlama-13B & 79.9 & ---$^\\dag$ & ---$^\\dag$ \\\\\nQwen-7B & 81.8 & 97.3 & +15.5 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nFour patterns emerge from the budget curve.\n\\emph{Phase transition between 384 and 512 tokens}: the tail-384 column reveals that the transition is not instantaneous at 256$\\to$512 but localized between 384 and 512 tokens.\nAt tail-384, all four models remain near baseline (73.6--80.7\\%), gaining only +1.0--4.8pp over tail-256.\nThe steep jump occurs at 384$\\to$512: +13.7pp (Qwen-7B), +13.2pp (DeepSeek), +15.5pp (CodeLlama), +22.0pp (Qwen-1.5B), crossing from near-baseline to near-ceiling.\nThis localizes the critical threshold to ${\\sim}$400--500 tokens: below ${\\sim}$384 tokens, the entire token budget is consumed by globals module dumps (pure noise); above ${\\sim}$512, at least one \\texttt{[Line~X]} execution event marker becomes visible, regardless of model capacity or architecture.\n\n\\emph{Convergence at tail-512+}: once the sharp performance jump is crossed, accuracy converges across all models into a 93.6--98.2\\% band at tail-512 (seed 42).\nMulti-seed validation shows robustness: across all 12 model$\\times$seed combinations at tail-512 (Table~\\ref{tab:tail512_seeds}), all accuracies fall within [93.61\\%, 98.24\\%], a 4.63pp band that compresses the signal-poor tail-256 spread (6.3pp) by 27\\%.\nCodeLlama-13B shows perfect per-model convergence at tail-512: all three seeds achieve 98.24\\% ($\\sigma{=}$0), consistent with the 13B scale and label-only loss providing a stronger optimization signal in the signal-rich regime (Table~\\ref{tab:tail512_seeds}).\nHowever, CodeLlama's higher tail-512 accuracy may partly reflect label-only loss rather than model capacity; direct comparison with other models (which use full-sequence loss) is confounded by this training difference.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed convergence at the tail-512 truncation point ($N{=}1{,}190$ per seed). All 12 model$\\times$seed combinations fall within a 4.63pp band [93.61\\%, 98.24\\%]. CodeLlama-13B achieves identical accuracy across all three seeds ($\\sigma{=}$0).}\n\\label{tab:tail512_seeds}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccr}\n\\toprule\n\\textbf{Model} & \\textbf{S42} & \\textbf{S123} & \\textbf{S456} & \\textbf{Mean} & \\textbf{$\\sigma$} \\\\\n\\midrule\nQwen-7B (7B)      & 93.61 & 96.00 & 97.65 & 95.75 & 2.05 \\\\\nDeepSeek (6.7B)    & 93.95 & 95.04 & 96.10 & 95.03 & 1.08 \\\\\nQwen-1.5B (1.5B)  & 95.63 & 97.65 & 96.72 & 96.67 & 1.01 \\\\\nCodeLlama (13B)    & 98.24 & 98.24 & 98.24 & \\textbf{98.24} & \\textbf{0.00} \\\\\n\\midrule\n\\multicolumn{4}{l}{Cross-model band} & \\multicolumn{2}{r}{[93.61, 98.24] = 4.63pp} \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAt tail-1024, four models reach 96.5--98.2\\% (CodeLlama 98.2\\% under label-only loss, three others 96.5--96.6\\%).\nScale and architecture differences that dominate the signal-poor regime (tail-256 range: 72.6--78.9\\%, 6.3pp) compress dramatically in the signal-rich regime.\n\n\\emph{Signal-poor convergence band}: head-2048 accuracies across all four models also converge into a narrow 75.3--81.8\\% band (6.5pp; Table~\\ref{tab:head_vs_tail}), comparable in width to the tail-256 band (72.6--78.9\\%, 6.3pp).\nWhen the diagnostic signal is absent (head-truncation discards trace terminus) or unreachable (tail-256 is too short), models of different scale and architecture collapse to similar performance, suggesting a shared floor determined by code comprehension rather than trace processing.\n\n\\emph{Scale behavior inversion}: in the signal-poor regime (tail-256), smaller models perform worse (Qwen-1.5B 72.6\\% vs.\\ Qwen-7B 78.9\\%, $-$6.3pp), mirroring the \\texttt{no\\_trace} scale pattern.\nIn the signal-rich regime (tail-512+), this reverses: Qwen-1.5B matches or exceeds Qwen-7B (95.6\\% vs.\\ 93.6\\% at tail-512; 97.9\\% vs.\\ 97.3\\% at tail-2048), consistent with sufficient trace signal eliminating the capacity advantage.\n\n\\emph{Non-monotonicity at long sequences}: two models show accuracy decreases beyond tail-1024.\nDeepSeek-6.7B drops $-$1.5pp from tail-1024 (96.5\\%) to tail-2048 (95.0\\%), consistent with its known long-context sensitivity (\\S\\ref{sec:training_dynamics}).\nCodeLlama-13B exhibits a more severe collapse: tail-2048 under label-only loss drops to 41.8\\% (vs.\\ tail-1024 = 98.2\\%), which we attribute to LoRA long-sequence instability under the label-only loss regime; this outlier is excluded from cross-model tail-2048 analysis.\nQwen-7B and Qwen-1.5B increase monotonically across all budgets.\n\nTable~\\ref{tab:head_vs_tail} shows the truncation direction effect: among the three models with complete data, tail-2048 outperforms head-2048 by 15.5--22.6pp.\nThe gap is largest for Qwen-1.5B (+22.6pp), indicating that smaller models benefit most from positional proximity to the diagnostic signal, as they lack the capacity to locate it within longer, noisier prefixes.\n\n%% ============================================================\n\\section{Calibration Analysis}\n\\label{sec:calibration_full}\n\nBeyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \\citep{spiess2025calibration}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} \\\\\n\\midrule\nae\\_only & \\textbf{0.0004} & \\textbf{0.0008} \\\\\nexception\\_only & 0.0027 & 0.0013 \\\\\nVOTA & 0.0054 & 0.005 \\\\\nfull\\_trace & 0.096 & 0.144 \\\\\nno\\_trace & 0.171 & 0.197 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.\nTier~1 conditions (\\texttt{ae\\_only}: ECE=0.0004; \\texttt{exception\\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \\texttt{full\\_trace} (ECE=0.096) and \\texttt{no\\_trace} (ECE=0.171) exhibit substantial miscalibration.\nVOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.\n\nThe Brier scores tell a consistent story: \\texttt{ae\\_only} (0.0008) and \\texttt{exception\\_only} (0.0013) achieve near-zero scores, while \\texttt{no\\_trace} (0.197) indicates substantial miscalibration.\n\n\\paragraph{Cross-model calibration.}\nTable~\\ref{tab:calibration_cross} extends the calibration analysis to four models (1.5B--13B) under \\texttt{exception\\_only}.\nAll four models achieve ECE ${<}$ 0.007 and Brier ${<}$ 0.007, indicating that calibration quality generalizes across architectures and scales.\nCodeLlama-13B achieves the lowest ECE (0.0020) and MCE (0.0411), while DeepSeek-6.7B shows the highest ECE (0.0064) and Brier (0.0061), consistent with its higher error rate (8 errors vs.\\ 2 for Qwen/CodeLlama).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model calibration for \\texttt{exception\\_only} ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score; MCE = maximum calibration error. All four models (1.5B--13B) achieve ECE ${<}$ 0.007.}\n\\label{tab:calibration_cross}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} & \\textbf{MCE $\\downarrow$} \\\\\n\\midrule\nQwen-1.5B & \\textbf{0.0020} & \\textbf{0.0013} & --- \\\\\nCodeLlama-13B & \\textbf{0.0020} & \\textbf{0.0013} & \\textbf{0.0411} \\\\\nQwen-7B & 0.0027 & \\textbf{0.0013} & 0.8355 \\\\\nDeepSeek-6.7B & 0.0064 & 0.0061 & 0.7756 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_calibration}\n\\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \\texttt{exception\\_only} (ECE=0.0027) clusters near the diagonal, while \\texttt{no\\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\\times$ gap.}\n\\label{fig:calibration}\n\\end{figure}\n\n%% ============================================================\n\\section{Error Overlap Analysis}\n\\label{sec:error_overlap}\n\nWe analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\\ref{fig:error_overlap}).\n\n\\texttt{exception\\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).\nThis orthogonality arises because \\texttt{exception\\_only} errors are caused by \\texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \\texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.\n\nAmong non-exception conditions, error sets exhibit hierarchical containment: \\texttt{ae\\_only} $\\subset$ VOTA $\\subset$ \\texttt{loop\\_only} $\\subset$ \\texttt{no\\_trace}, with pairwise Jaccard indices increasing with signal overlap.\n\\texttt{loop\\_only} and \\texttt{full\\_trace} share the highest overlap (Jaccard ${\\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.\n\nThis analysis indicates that \\texttt{exception\\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{error_overlap}\n\\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \\texttt{exception\\_only} (exc\\_only) has zero overlap with all other conditions, indicating it operates on an independent signal dimension.}\n\\label{fig:error_overlap}\n\\end{figure}\n\n%% ============================================================\n\\section{Cross-Dataset Generalization: DebugBench}\n\\label{sec:debugbench_full}\n\nTo test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \\citep{tian2024debugbench}, a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).\nAfter filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\\% CIs. The component ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is preserved, and exception\\_only achieves perfect accuracy.}\n\\label{tab:debugbench}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc (\\%)} & \\textbf{95\\% CI} \\\\\n\\midrule\nexception\\_only & \\textbf{100.00} & [99.14, 100.00] \\\\\nVOTA & 99.77 & [99.30, 100.00] \\\\\nno\\_trace & 96.71 & [94.80, 98.40] \\\\\n\\midrule\nMajority baseline & 51.41 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \\texttt{exception\\_only} (100.00\\%) $\\geq$ VOTA (99.77\\%) $>$ \\texttt{no\\_trace} (96.71\\%).\nThe \\texttt{exception\\_only} condition achieves perfect accuracy, showing that the exception-based representation generalizes to a different fault distribution without degradation.\n\nThe absolute margins are much narrower than on the main dataset: the \\texttt{no\\_trace} baseline already achieves 96.71\\% (compared to 75.13\\% on HumanEval+MBPP), leaving only 3.29pp of headroom for trace-based improvement.\nThis ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.\nIn contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.\n\nThese results support exception-based verdict prediction as a generalizable approach: the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\\_only $\\geq$ VOTA $>$ no\\_trace) is consistent across both datasets. However, the narrow DebugBench margins are insufficient to independently validate trace importance.\nThe 24.70pp trace lift on the main dataset (no\\_trace 75.13\\% $\\to$ exception\\_only 99.83\\%) remains the primary evidence for the value of exception-based trace signals.\n\n%% ============================================================\n\\section{Cross-Model Robustness Analysis}\n\\label{sec:robustness_analysis}\n\nThe cross-model gap pattern (Table~\\ref{tab:cross_model}) suggests a design principle: \\emph{trace representations should match the model capability floor, not the ceiling.}\nException events are consistently the most effective component on both models, and their structural simplicity (a fixed-format error message) ensures that the relative advantage over richer representations holds across all seeds.\nAll three DeepSeek \\texttt{exception\\_only} seeds achieve ${\\geq}$99.33\\% (99.33/99.50/99.33, $\\sigma{=}$0.10pp), matching Qwen and CodeLlama at ${\\geq}$99.83\\%.\nVOTA achieves ${\\geq}$98.57\\% across all models when excluding outlier seeds (cross-model range: 0.80pp), but DeepSeek VOTA exhibits seed-dependent instability: seed 42 (84.45\\%) is a training failure due to tokenizer-induced truncation (91.7\\% of training samples affected), while seeds 123/456 (99.16\\%/99.33\\%) match cross-model performance.\nThis VOTA instability is confounded by tokenizer efficiency and base model differences \\citep{yang2024generalization}.\nOur \\texttt{exception\\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.\nThe resulting 0.50pp cross-model gap (Table~\\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.\nThe practical implication is that trace-based systems should default to the simplest sufficient signal.\n\n%% ============================================================\n\\section{Training Dynamics and Loss Decoupling}\n\\label{sec:training_dynamics}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{training_dynamics}\n\\caption{Training dynamics: \\texttt{exception\\_only} converges to 99.83\\% by step 150; \\texttt{full\\_trace} with label-only loss oscillates (82--89\\%) without convergence.}\n\\label{fig:training_dynamics}\n\\end{figure}\n\nThe DeepSeek \\texttt{exception\\_only} results are consistent across all three seeds (99.33/99.50/99.33, $\\sigma{=}$0.10pp), matching Qwen's cross-seed stability.\nEpoch-level analysis shows mild degradation in seed 42: accuracy peaks at 99.83\\% after epoch~1 but settles at 99.33\\% by epoch~3 ($-$0.50pp), while seed 456 shows no degradation (99.33\\% at both epochs).\nEarly stopping may yield marginal gains, but the epoch effect is small (${\\leq}$0.5pp).\nThe practical recommendation: for deployment, use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training loss, and train multiple seeds to select the best.\n\nThe contrast with VOTA is instructive: DeepSeek VOTA seed 42 accuracy monotonically increases from 78.15\\% to 84.45\\% across epochs, consistent with a performance limit from high trace truncation (91.7\\% of samples; \\S\\ref{sec:tokenizer_analysis}).\nSeeds 123/456, which avoid the truncation-sensitive initialization basin, achieve 99.16\\%/99.33\\%, indicating that the deficit is seed-specific rather than a fundamental model limitation.\n\n%% ============================================================\n\\section{Deduplication Statistics}\n\\label{sec:dedup_stats}\n\nTable~\\ref{tab:dedup} reports the duplication rates across trace formats.\nBecause multiple passing solutions to the same problem produce identical (input, output) pairs in the \\texttt{exception\\_only} format (correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic), the dataset contains duplicate rows.\nTrain--test input overlap is zero (split by problem ID), so no information leakage occurs.\nThe high duplication in \\texttt{exception\\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.\n\n\\paragraph{Problem-level partitioning and sensitivity analysis.}\nData is partitioned at the problem level: 472 training problems and 119 test problems, with zero crossover.\nDuplicates arise from multiple candidate solutions per problem (up to 10 solutions each), not from cross-problem overlap.\nTo verify that deduplication does not alter any finding, we ran a sensitivity analysis across all 19 experimental conditions (7 trace formats $\\times$ 4 models, minus conditions not run): deduplication produces a negligible ($<$0.1pp) accuracy delta in every case.\nThis shows that duplicate samples neither inflate nor deflate accuracy, because duplicates share the same ground-truth label and the model's prediction is deterministic at inference time.\nDuplicates arise because the \\texttt{exception\\_only} format collapses passing solutions (which share identical ``no exception'' output) into identical rows; the redundancy is a property of the format's compactness for pass-class samples.\nThe \\texttt{exception\\_only} test set contains 48.99\\% such duplicates; all confidence intervals treat samples as independent Bernoulli trials.\n\n\\begin{table}[t]\n\\centering\n\\caption{Deduplication statistics. The \\texttt{exception\\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}\n\\label{tab:dedup}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split} & \\textbf{Total} & \\textbf{Unique} & \\textbf{Dup.\\ rate} \\\\\n\\midrule\nexception\\_only train & 4{,}720 & 2{,}858 & 39.45\\% \\\\\nexception\\_only test  & 1{,}190 &   607 & 48.99\\% \\\\\nraw\\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Regex Baseline Analysis}\n\\label{sec:regex_baselines}\n\nTo establish a non-learning upper bound, we evaluate six regex-based baselines on the \\texttt{exception\\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \\texttt{full\\_trace} inputs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \\texttt{exception\\_only}, McNemar $p{<}.001$). B6 uses an error count threshold. $^\\ddag$B5 exploits a data formatting artifact: the \\texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}\n\\label{tab:regex}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llc}\n\\toprule\n\\textbf{Baseline} & \\textbf{Method} & \\textbf{Acc (\\%)} \\\\\n\\midrule\nB1: \\texttt{[ERROR]} presence & string match & 93.45 \\\\\nB2: Traceback presence & string match & 71.51 \\\\\nB3: Any keyword & union of B1+B2+Exception & 93.45 \\\\\nB4: Exception type regex & regex on exception class names & \\textbf{93.61} \\\\\nB5: Format marker & \\texttt{[No exception data]} $\\to$ pass & 99.33$^\\ddag$ \\\\\nB6: Error count $\\geq$2 & count threshold & 92.02 \\\\\n\\midrule\nVOTA format regex & best regex on VOTA traces & 75.55 \\\\\nfull\\_trace format regex & best regex on full traces & 77.39 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nThe strongest legitimate baseline (B4, 93.61\\%) applies regex pattern-matching on Python exception class names (e.g., \\texttt{ValueError}, \\texttt{TypeError}).\nIts errors concentrate on 8 boundary samples where a \\texttt{ValueError} is raised inside a \\texttt{try/except} block and caught; the program passes despite an exception occurring in the trace.\nSFT \\texttt{exception\\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.\nB5 (99.33\\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\\ SFT yields $p{=}.041$, indicating a statistically significant difference.\n\n\\paragraph{Cross-format comparison.}\nTable~\\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.\nThe SFT advantage increases with format complexity: \\texttt{no\\_trace} (+3.62pp over majority baseline) $<$ \\texttt{full\\_trace} (+4.37pp) $<$ \\texttt{exception\\_only} (+6.22pp) $\\ll$ VOTA (+23.86pp).\nThe VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \\texttt{exception\\_only}'s simpler format allows regex to capture most of the signal.\n\n\\begin{table}[t]\n\\centering\n\\caption{SFT vs.\\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \\texttt{no\\_trace}, keyword matching for \\texttt{full\\_trace}, pattern matching for VOTA, exception type regex (B4) for \\texttt{exception\\_only}.}\n\\label{tab:regex_cross_format}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Format} & \\textbf{SFT (\\%)} & \\textbf{Regex (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nexception\\_only & 99.83 & 93.61 & +6.22 \\\\\nVOTA & 99.05 & 75.55 & +23.50 \\\\\nfull\\_trace & 81.76 & 77.39 & +4.37 \\\\\nno\\_trace & 75.13 & 71.51 & +3.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ============================================================\n\\section{Cross-Model Zero-Shot Comparison}\n\\label{sec:zeroshot_cross_model}\n\nTable~\\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \\texttt{exception\\_only} accuracy across four models.\nZero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.\nSFT compresses the 42.44pp zero-shot range to 0.50pp, eliminating architecture-dependent variance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Zero-shot vs.\\ SFT \\texttt{exception\\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.50pp.}\n\\label{tab:zeroshot_cross_model}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Size} & \\textbf{Zero-shot (\\%)} & \\textbf{SFT (\\%)} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nQwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\\\\nDeepSeek-6.7B & 6.7B & 90.59 & 99.39 & +8.80 \\\\\nQwen-7B & 7B & 89.08 & 99.83 & +10.75 \\\\\nCodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\\\\n\\midrule\nRange & --- & 42.44pp & 0.50pp & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Calibration Analysis}\n\\label{sec:calibration_analysis}\n\n\\begin{table}[h]\n\\centering\n\\caption{Model calibration on \\texttt{exception\\_only} (seed 42). All four models achieve ECE $<$ 0.005, indicating that near-perfect accuracy reflects genuine confidence rather than overfit predictions.}\n\\label{tab:calibration_model_level}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Accuracy} & \\textbf{ECE $\\downarrow$} & \\textbf{Brier $\\downarrow$} & \\textbf{Mean Conf.} \\\\\n\\midrule\nQwen-2.5-1.5B & 99.83\\% & 0.0014 & 0.0013 & 99.82\\% \\\\\nQwen-2.5-7B & 99.83\\% & 0.0017 & 0.0013 & 99.80\\% \\\\\nCodeLlama-13B & 99.83\\% & 0.0020 & 0.0013 & 99.63\\% \\\\\nDeepSeek-6.7B & 99.33\\% & 0.0048 & 0.0059 & 99.71\\% \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n%% ============================================================\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
      "numLines": 845,
      "startLine": 1,
      "totalLines": 845
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have the appendix and experiments tex files. I also have the registry data. Let me now systematically check the remaining registry entries I need. The registry returned 36 entries but I notice some key experiments are missing. Let me fetch the rest of the registry to make sure I have all relevant experiments.

Let me now systematically audit each table in the appendix against the registry and experiments.tex.

First, let me identify all tables in the appendix:
1. Table 5 (tab:per_class) - Per-class precision, recall, F1 for all conditions
2. Table 6 (tab:hyperparams) - Training hyperparameters


3. Table 7 (tab:train_time) - Training wall-clock time
4. Table 8 (tab:exception_type) - Exception type accuracy breakdown
5. Table 9 (tab:exc_subcomponent) - Exception subcomponent ablation
6. Table 10 (tab:trace_length) - Trace length and truncation direction ablation
7. Table 11 (tab:trace_length_pairwise) - Pairwise paired bootstrap comparisons
8. Table 12 (tab:tail_cross_model) - Cross-model tail-truncation budget curve
9. Table 13 (tab:head_vs_tail) - Cross-model truncation direction comparison
10. Table 14 (tab:tail512_seeds) - Cross-seed results showing convergence at tail-512
11. Table 15 (tab:calibration) - Calibration metrics on Qwen-2.5-7B
12. Table 16 (tab:calibration_cross) - Cross-model calibration for exception_only
13. Table 17 (tab:dedup) - Deduplication statistics
14. Table 18 (tab:regex) - Regex baseline accuracy
15. Table 19 (tab:regex_cross_format) - SFT vs. best regex baseline by trace format
16. Table 20 (tab:zeroshot_cross_model) - Zero-shot vs. SFT exception_only across four models
17. Table 21 (tab:calibration_model_level) - Model calibration on exception_only
18. Table 22 (tab:full_qwen) - Full results for Qwen-2.5-

Coder-7B
19. Table 23 (tab:full_deepseek) - Full results for DeepSeek-Coder-6.7B
20. Table (tab:debugbench) - DebugBench results
21. Table (tab:density) in experiments.tex - Decomposition of full-trace degradation

Wait, I need to reconsider the numbering. The main text has three tables, so the appendix tables should start from Table 4, not Table 5. Let me recount what the user actually asked for.

Rather than getting caught up in exact table numbers, let me just systematically go through each appendix table and check its content. I also need to track down specific experimental runs like the Qwen-7B variants with different trace configurations, the exception-only and ae-only seeds, VOTA experiments, and loop-only variants.

The registry gave me 36 entries to work with. Let me compile the key metrics I'm seeing—gradient masking with Qwen-7B across different seeds is hitting 98-99% accuracy, exception type-only reaches 100%, and exception message-only gets to 99.5%. Looking at the remaining results, I'm seeing some scattered entries with varying accuracy levels, but I realize the registry is incomplete—it only captures a subset of the 36 total experiments, with many in PREPARING or killed status. I should search for local result files to find the missing key experiments that aren't showing up in the registry. Now I'm compiling the accuracy percentages for additional model configurations across different attack types and seeds to cross-reference with what's in the registry. I should search for more evaluation result files locally to verify these numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "40e2c2b4-833c-453b-8285-4fed3539a2fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVqGGjXmmTLwTZ28gxhju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6943,
      "cache_creation_input_tokens": 20406,
      "cache_read_input_tokens": 36221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20406
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

_source line 26_

Now let me search for additional data sources to cross-reference — eval results and other experiment data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "b8f85367-6a28-4b8f-a46d-e963b56b9481",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVqGGjXmmTLwTZ28gxhju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6943,
      "cache_creation_input_tokens": 20406,
      "cache_read_input_tokens": 36221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20406
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

_source line 27_

<details open><summary>🔧 Tool call — Glob · `toolu_01NEzx1AoTPARJ5RfX6eFekx`</summary>

```json
{
  "pattern": "**/eval_results*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "0eba4e4c-32a8-4078-bbe2-d6b1b06e4307",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVqGGjXmmTLwTZ28gxhju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6943,
      "cache_creation_input_tokens": 20406,
      "cache_read_input_tokens": 36221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20406
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

_source line 28 · 2026-05-23T19:18:19.905Z_

<details><summary>↩ Tool result · `toolu_01NEzx1AoTPARJ5RfX6eFekx`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "de9ae1fe-53d2-4000-95f3-9f1eaec251c1",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 14,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ba1teAViJkLgYLxDY54khB`</summary>

```json
{
  "pattern": "**/results*.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "923370cf-589c-4c7d-a22b-485024222115",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVqGGjXmmTLwTZ28gxhju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6943,
      "cache_creation_input_tokens": 20406,
      "cache_read_input_tokens": 36221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20406
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

_source line 30_

<details open><summary>🔧 Tool call — Glob · `toolu_018WDHHQ5Pjrm36TGpSoUmr9`</summary>

```json
{
  "pattern": "**/artifacts/**/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "a4ee8541-b9c0-4634-a0af-d74a92000ebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XVqGGjXmmTLwTZ28gxhju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6943,
      "cache_creation_input_tokens": 20406,
      "cache_read_input_tokens": 36221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20406
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

_source line 31 · 2026-05-23T19:18:20.392Z_

<details><summary>↩ Tool result · `toolu_01Ba1teAViJkLgYLxDY54khB`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "23184cd1-2f3e-4f92-9e8c-985b8feb7e0e",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 18,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T19:18:20.403Z_

<details><summary>↩ Tool result · `toolu_018WDHHQ5Pjrm36TGpSoUmr9`</summary>

```text
artifacts/dream_reports/dream_20260515T013018/best/experiment_data.json
artifacts/dream_reports/dream_20260515T013018/median/experiment_data.json
artifacts/dream_reports/dream_20260515T013018/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T084908/best/experiment_data.json
artifacts/dream_reports/dream_20260515T084908/median/experiment_data.json
artifacts/dream_reports/dream_20260515T084908/worst/experiment_data.json
artifacts/_project/data/trace_ablation_bootstrap.json
artifacts/trace_ablation_bootstrap.json
artifacts/_project/data/regex_baseline_results.json
artifacts/regex_baseline_analysis/data/regex_baseline_results.json
artifacts/_project/data/debugbench_results_04bcfc.json
artifacts/_project/data/debugbench_results.json
artifacts/_project/data/c1_edge_samples.json
artifacts/_project/report/cluster_robust_ci.json
artifacts/analysis/cluster_robust_ci.json
artifacts/cluster_robust_ci.json
artifacts/dream_reports/dream_20260516T105259/best/experiment_data.json
artifacts/dream_reports/dream_20260516T105259/median/experiment_data.json
artifacts/dream_reports/dream_20260516T105259/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T155731/best/experiment_data.json
artifacts/dream_reports/dream_20260516T155731/median/experiment_data.json
artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json
artifacts/_project/data/table1_final.json
artifacts/table1_final.json
artifacts/dream_reports/dream_20260518T113804/best/experiment_data.json
artifacts/dream_reports/dream_20260518T113804/median/experiment_data.json
artifacts/dream_reports/dream_20260518T113804/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T125926/best/experiment_data.json
artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json
artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json
artifacts/deepseek_label_only_seed42/data/deepseek_label_only_seed42_results.json
artifacts/deepseek_label_only_seed42_results.json
artifacts/_project/data/cross_model_calibration_results.json
artifacts/_project/paper/figures/attention_pilot/attention_pilot_results_v2.json
artifacts/fewshot_predictions/fewshot_gpt41_exception_only_0shot.json
artifacts/fewshot_predictions/fewshot_gpt41_exception_only_3shot.json
artifacts/fewshot_predictions/fewshot_gpt41_no_trace_0shot.json
artifacts/fewshot_predictions/fewshot_gpt4o_exception_only_0shot.json
artifacts/fewshot_predictions/fewshot_gpt4o_exception_only_3shot.json
artifacts/fewshot_predictions/fewshot_gpt4o_no_trace_0shot.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "51ca0581-d610-453f-939a-c5ec3e285497",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T013018/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T013018/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T013018/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T084908/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T084908/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260515T084908/worst/experiment_data.json",
      "artifacts/_project/data/trace_ablation_bootstrap.json",
      "artifacts/trace_ablation_bootstrap.json",
      "artifacts/_project/data/regex_baseline_results.json",
      "artifacts/regex_baseline_analysis/data/regex_baseline_results.json",
      "artifacts/_project/data/debugbench_results_04bcfc.json",
      "artifacts/_project/data/debugbench_results.json",
      "artifacts/_project/data/c1_edge_samples.json",
      "artifacts/_project/report/cluster_robust_ci.json",
      "artifacts/analysis/cluster_robust_ci.json",
      "artifacts/cluster_robust_ci.json",
      "artifacts/dream_reports/dream_20260516T105259/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T105259/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T105259/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T155731/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T155731/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T155731/worst/experiment_data.json",
      "artifacts/_project/data/table1_final.json",
      "artifacts/table1_final.json",
      "artifacts/dream_reports/dream_20260518T113804/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T113804/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T113804/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T125926/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T125926/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T125926/worst/experiment_data.json",
      "artifacts/deepseek_label_only_seed42/data/deepseek_label_only_seed42_results.json",
      "artifacts/deepseek_label_only_seed42_results.json",
      "artifacts/_project/data/cross_model_calibration_results.json",
      "artifacts/_project/paper/figures/attention_pilot/attention_pilot_results_v2.json",
      "artifacts/fewshot_predictions/fewshot_gpt41_exception_only_0shot.json",
      "artifacts/fewshot_predictions/fewshot_gpt41_exception_only_3shot.json",
      "artifacts/fewshot_predictions/fewshot_gpt41_no_trace_0shot.json",
      "artifacts/fewshot_predictions/fewshot_gpt4o_exception_only_0shot.json",
      "artifacts/fewshot_predictions/fewshot_gpt4o_exception_only_3shot.json",
      "artifacts/fewshot_predictions/fewshot_gpt4o_no_trace_0shot.json"
    ],
    "durationMs": 23,
    "numFiles": 40,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Let me read the key data files to cross-reference with the paper tables. The most important ones are:
1. table1_final.json - likely the main comparison table data
2. regex_baseline_results.json - for regex baselines
3. debugbench_results.json - for DebugBench
4. cross_model_calibration_results.json - for calibration tables
5. trace_ablation_bootstrap.json - for trace length ablation

Let me read these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "11677071-7702-4fe0-953d-f81bdee18f61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 34_

Let me read the key data files to cross-reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "5f619364-ae02-4d70-932f-97b25f6d53ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_011UmYcryV9aKyxA1D3pRNhT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/table1_final.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "f0e7ba81-4425-4629-801d-6dfd910be80d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 36 · 2026-05-23T19:18:30.640Z_

<details><summary>↩ Tool result · `toolu_011UmYcryV9aKyxA1D3pRNhT`</summary>

```text
1	[
2	  {
3	    "model": "Qwen-2.5-Coder-7B",
4	    "condition": "no_trace",
5	    "accuracy": 0.7513,
6	    "ci_lower": 0.7277,
7	    "ci_upper": 0.7748,
8	    "n": 1190,
9	    "lift": 0.0362,
10	    "exp_id": "no_trace_seed42_v5",
11	    "seeds": 1
12	  },
13	  {
14	    "model": "Qwen-2.5-Coder-7B",
15	    "condition": "full_trace",
16	    "accuracy": 0.8176,
17	    "ci_lower": 0.7970,
18	    "ci_upper": 0.8390,
19	    "n": 1190,
20	    "lift": 0.1025,
21	    "exp_id": "full_trace_seed42_v5",
22	    "seeds": 1
23	  },
24	  {
25	    "model": "Qwen-2.5-Coder-7B",
26	    "condition": "label_only",
27	    "accuracy": 0.8648,
28	    "ci_lower": 0.8454,
29	    "ci_upper": 0.8842,
30	    "n": 1190,
31	    "lift": 0.1497,
32	    "exp_id": "label_only_seed123",
33	    "seeds": 2,
34	    "seed_values": [0.8706, 0.8590],
35	    "std": 0.0082
36	  },
37	  {
38	    "model": "Qwen-2.5-Coder-7B",
39	    "condition": "loop_only",
40	    "accuracy": 0.8605,
41	    "ci_lower": 0.8350,
42	    "ci_upper": 0.8840,
43	    "n": 1190,
44	    "lift": 0.1454,
45	    "exp_id": "loop_only_seed123",
46	    "seeds": 3,
47	    "seed_values": [0.8588, 0.8664, 0.8563],
48	    "std": 0.0043
49	  },
50	  {
51	    "model": "Qwen-2.5-Coder-7B",
52	    "condition": "VOTA",
53	    "accuracy": 0.9941,
54	    "ci_lower": 0.9882,
55	    "ci_upper": 0.9983,
56	    "n": 1190,
57	    "lift": 0.2790,
58	    "exp_id": "vota_seed42_v5",
59	    "seeds": 1
60	  },
61	  {
62	    "model": "Qwen-2.5-Coder-7B",
63	    "condition": "exception_only",
64	    "accuracy": 0.9983,
65	    "ci_lower": 0.9958,
66	    "ci_upper": 1.0000,
67	    "n": 1190,
68	    "lift": 0.2832,
69	    "exp_id": "exception_only_seed123",
70	    "seeds": 3,
71	    "seed_values": [0.9983, 0.9983, 0.9983],
72	    "std": 0.0000
73	  },
74	  {
75	    "model": "Qwen-2.5-Coder-7B",
76	    "condition": "ae_only",
77	    "accuracy": 0.9964,
78	    "ci_lower": 0.9930,
79	    "ci_upper": 0.9998,
80	    "n": 1190,
81	    "lift": 0.2813,
82	    "exp_id": "vota_ae_only_seed42",
83	    "seeds": 3,
84	    "seed_values": [0.9992, 0.9908, 0.9992],
85	    "std": 0.0049
86	  },
87	  {
88	    "model": "Qwen-2.5-Coder-1.5B",
89	    "condition": "no_trace",
90	    "accuracy": 0.6731,
91	    "ci_lower": 0.6465,
92	    "ci_upper": 0.6997,
93	    "n": 1190,
94	    "lift": -0.0420,
95	    "exp_id": "qwen15b_no_trace_seed42",
96	    "seeds": 1
97	  },
98	  {
99	    "model": "Qwen-2.5-Coder-1.5B",
100	    "condition": "full_trace",
101	    "accuracy": 0.7706,
102	    "ci_lower": 0.7467,
103	    "ci_upper": 0.7945,
104	    "n": 1190,
105	    "lift": 0.0555,
106	    "exp_id": "qwen15b_full_trace_seed42",
107	    "seeds": 1
108	  },
109	  {
110	    "model": "Qwen-2.5-Coder-1.5B",
111	    "condition": "VOTA",
112	    "accuracy": 0.9958,
113	    "ci_lower": 0.9921,
114	    "ci_upper": 0.9995,
115	    "n": 1190,
116	    "lift": 0.2807,
117	    "exp_id": "qwen15b_vota_seed42",
118	    "seeds": 1
119	  },
120	  {
121	    "model": "Qwen-2.5-Coder-1.5B",
122	    "condition": "exception_only",
123	    "accuracy": 0.9983,
124	    "ci_lower": 0.9958,
125	    "ci_upper": 1.0000,
126	    "n": 1190,
127	    "lift": 0.2832,
128	    "exp_id": "qwen15b_exception_only_seed42",
129	    "seeds": 1
130	  },
131	  {
132	    "model": "DeepSeek-Coder-6.7B-Instruct",
133	    "condition": "no_trace",
134	    "accuracy": 0.7336,
135	    "ci_lower": 0.7080,
136	    "ci_upper": 0.7570,
137	    "n": 1190,
138	    "lift": 0.0185,
139	    "exp_id": "deepseek_no_trace_seed42",
140	    "seeds": 1
141	  },
142	  {
143	    "model": "DeepSeek-Coder-6.7B-Instruct",
144	    "condition": "full_trace",
145	    "accuracy": 0.7916,
146	    "ci_lower": 0.7680,
147	    "ci_upper": 0.8130,
148	    "n": 1190,
149	    "lift": 0.0765,
150	    "exp_id": "deepseek_full_trace_seed42_v3",
151	    "seeds": 1
152	  },
153	  {
154	    "model": "DeepSeek-Coder-6.7B-Instruct",
155	    "condition": "VOTA",
156	    "accuracy": 0.8445,
157	    "ci_lower": 0.8260,
158	    "ci_upper": 0.8640,
159	    "n": 1190,
160	    "lift": 0.1294,
161	    "exp_id": "deepseek_vota_seed42",
162	    "seeds": 1,
163	    "note": "Context truncation reduces accuracy; intact samples achieve 100%"
164	  },
165	  {
166	    "model": "DeepSeek-Coder-6.7B-Instruct",
167	    "condition": "exception_only",
168	    "accuracy": 0.9933,
169	    "ci_lower": 0.9882,
170	    "ci_upper": 0.9975,
171	    "n": 1190,
172	    "lift": 0.2782,
173	    "exp_id": "deepseek_exception_only_seed42",
174	    "seeds": 1,
175	    "note": "seed123 outlier at 91.09% (2/3 seeds ≥99.33%)"
176	  },
177	  {
178	    "model": "CodeLlama-13B-Instruct",
179	    "condition": "no_trace",
180	    "accuracy": 0.7647,
181	    "ci_lower": 0.7380,
182	    "ci_upper": 0.7870,
183	    "n": 1190,
184	    "lift": 0.0496,
185	    "exp_id": "codellama13b_no_trace_seed42",
186	    "seeds": 1
187	  },
188	  {
189	    "model": "CodeLlama-13B-Instruct",
190	    "condition": "VOTA",
191	    "accuracy": 0.9857,
192	    "ci_lower": 0.9790,
193	    "ci_upper": 0.9920,
194	    "n": 1190,
195	    "lift": 0.2706,
196	    "exp_id": "codellama13b_vota_seed42",
197	    "seeds": 1
198	  },
199	  {
200	    "model": "CodeLlama-13B-Instruct",
201	    "condition": "exception_only",
202	    "accuracy": 0.9983,
203	    "ci_lower": 0.9958,
204	    "ci_upper": 1.0000,
205	    "n": 1190,
206	    "lift": 0.2832,
207	    "exp_id": "codellama13b_exception_only_seed42",
208	    "seeds": 1
209	  },
210	  {
211	    "model": "Qwen-2.5-Coder-7B (DebugBench)",
212	    "condition": "no_trace",
213	    "accuracy": 0.9671,
214	    "ci_lower": 0.9480,
215	    "ci_upper": 0.9840,
216	    "n": 426,
217	    "lift": 0.2520,
218	    "exp_id": "debugbench_no_trace_seed42",
219	    "seeds": 1
220	  },
221	  {
222	    "model": "Qwen-2.5-Coder-7B (DebugBench)",
223	    "condition": "VOTA",
224	    "accuracy": 0.9977,
225	    "ci_lower": 0.9930,
226	    "ci_upper": 1.0000,
227	    "n": 426,
228	    "lift": 0.2826,
229	    "exp_id": "debugbench_vota_seed42",
230	    "seeds": 1
231	  },
232	  {
233	    "model": "Qwen-2.5-Coder-7B (DebugBench)",
234	    "condition": "exception_only",
235	    "accuracy": 1.0000,
236	    "ci_lower": 0.9914,
237	    "ci_upper": 1.0000,
238	    "n": 426,
239	    "lift": 0.2849,
240	    "exp_id": "debugbench_exception_only_seed42",
241	    "seeds": 1
242	  }
243	]
244	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "f2f16a1f-5149-4c6e-a19f-bb083517db08",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/table1_final.json",
      "content": "[\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"no_trace\",\n    \"accuracy\": 0.7513,\n    \"ci_lower\": 0.7277,\n    \"ci_upper\": 0.7748,\n    \"n\": 1190,\n    \"lift\": 0.0362,\n    \"exp_id\": \"no_trace_seed42_v5\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"full_trace\",\n    \"accuracy\": 0.8176,\n    \"ci_lower\": 0.7970,\n    \"ci_upper\": 0.8390,\n    \"n\": 1190,\n    \"lift\": 0.1025,\n    \"exp_id\": \"full_trace_seed42_v5\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"label_only\",\n    \"accuracy\": 0.8648,\n    \"ci_lower\": 0.8454,\n    \"ci_upper\": 0.8842,\n    \"n\": 1190,\n    \"lift\": 0.1497,\n    \"exp_id\": \"label_only_seed123\",\n    \"seeds\": 2,\n    \"seed_values\": [0.8706, 0.8590],\n    \"std\": 0.0082\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"loop_only\",\n    \"accuracy\": 0.8605,\n    \"ci_lower\": 0.8350,\n    \"ci_upper\": 0.8840,\n    \"n\": 1190,\n    \"lift\": 0.1454,\n    \"exp_id\": \"loop_only_seed123\",\n    \"seeds\": 3,\n    \"seed_values\": [0.8588, 0.8664, 0.8563],\n    \"std\": 0.0043\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"VOTA\",\n    \"accuracy\": 0.9941,\n    \"ci_lower\": 0.9882,\n    \"ci_upper\": 0.9983,\n    \"n\": 1190,\n    \"lift\": 0.2790,\n    \"exp_id\": \"vota_seed42_v5\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"exception_only\",\n    \"accuracy\": 0.9983,\n    \"ci_lower\": 0.9958,\n    \"ci_upper\": 1.0000,\n    \"n\": 1190,\n    \"lift\": 0.2832,\n    \"exp_id\": \"exception_only_seed123\",\n    \"seeds\": 3,\n    \"seed_values\": [0.9983, 0.9983, 0.9983],\n    \"std\": 0.0000\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B\",\n    \"condition\": \"ae_only\",\n    \"accuracy\": 0.9964,\n    \"ci_lower\": 0.9930,\n    \"ci_upper\": 0.9998,\n    \"n\": 1190,\n    \"lift\": 0.2813,\n    \"exp_id\": \"vota_ae_only_seed42\",\n    \"seeds\": 3,\n    \"seed_values\": [0.9992, 0.9908, 0.9992],\n    \"std\": 0.0049\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-1.5B\",\n    \"condition\": \"no_trace\",\n    \"accuracy\": 0.6731,\n    \"ci_lower\": 0.6465,\n    \"ci_upper\": 0.6997,\n    \"n\": 1190,\n    \"lift\": -0.0420,\n    \"exp_id\": \"qwen15b_no_trace_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-1.5B\",\n    \"condition\": \"full_trace\",\n    \"accuracy\": 0.7706,\n    \"ci_lower\": 0.7467,\n    \"ci_upper\": 0.7945,\n    \"n\": 1190,\n    \"lift\": 0.0555,\n    \"exp_id\": \"qwen15b_full_trace_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-1.5B\",\n    \"condition\": \"VOTA\",\n    \"accuracy\": 0.9958,\n    \"ci_lower\": 0.9921,\n    \"ci_upper\": 0.9995,\n    \"n\": 1190,\n    \"lift\": 0.2807,\n    \"exp_id\": \"qwen15b_vota_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-1.5B\",\n    \"condition\": \"exception_only\",\n    \"accuracy\": 0.9983,\n    \"ci_lower\": 0.9958,\n    \"ci_upper\": 1.0000,\n    \"n\": 1190,\n    \"lift\": 0.2832,\n    \"exp_id\": \"qwen15b_exception_only_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"DeepSeek-Coder-6.7B-Instruct\",\n    \"condition\": \"no_trace\",\n    \"accuracy\": 0.7336,\n    \"ci_lower\": 0.7080,\n    \"ci_upper\": 0.7570,\n    \"n\": 1190,\n    \"lift\": 0.0185,\n    \"exp_id\": \"deepseek_no_trace_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"DeepSeek-Coder-6.7B-Instruct\",\n    \"condition\": \"full_trace\",\n    \"accuracy\": 0.7916,\n    \"ci_lower\": 0.7680,\n    \"ci_upper\": 0.8130,\n    \"n\": 1190,\n    \"lift\": 0.0765,\n    \"exp_id\": \"deepseek_full_trace_seed42_v3\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"DeepSeek-Coder-6.7B-Instruct\",\n    \"condition\": \"VOTA\",\n    \"accuracy\": 0.8445,\n    \"ci_lower\": 0.8260,\n    \"ci_upper\": 0.8640,\n    \"n\": 1190,\n    \"lift\": 0.1294,\n    \"exp_id\": \"deepseek_vota_seed42\",\n    \"seeds\": 1,\n    \"note\": \"Context truncation reduces accuracy; intact samples achieve 100%\"\n  },\n  {\n    \"model\": \"DeepSeek-Coder-6.7B-Instruct\",\n    \"condition\": \"exception_only\",\n    \"accuracy\": 0.9933,\n    \"ci_lower\": 0.9882,\n    \"ci_upper\": 0.9975,\n    \"n\": 1190,\n    \"lift\": 0.2782,\n    \"exp_id\": \"deepseek_exception_only_seed42\",\n    \"seeds\": 1,\n    \"note\": \"seed123 outlier at 91.09% (2/3 seeds ≥99.33%)\"\n  },\n  {\n    \"model\": \"CodeLlama-13B-Instruct\",\n    \"condition\": \"no_trace\",\n    \"accuracy\": 0.7647,\n    \"ci_lower\": 0.7380,\n    \"ci_upper\": 0.7870,\n    \"n\": 1190,\n    \"lift\": 0.0496,\n    \"exp_id\": \"codellama13b_no_trace_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"CodeLlama-13B-Instruct\",\n    \"condition\": \"VOTA\",\n    \"accuracy\": 0.9857,\n    \"ci_lower\": 0.9790,\n    \"ci_upper\": 0.9920,\n    \"n\": 1190,\n    \"lift\": 0.2706,\n    \"exp_id\": \"codellama13b_vota_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"CodeLlama-13B-Instruct\",\n    \"condition\": \"exception_only\",\n    \"accuracy\": 0.9983,\n    \"ci_lower\": 0.9958,\n    \"ci_upper\": 1.0000,\n    \"n\": 1190,\n    \"lift\": 0.2832,\n    \"exp_id\": \"codellama13b_exception_only_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B (DebugBench)\",\n    \"condition\": \"no_trace\",\n    \"accuracy\": 0.9671,\n    \"ci_lower\": 0.9480,\n    \"ci_upper\": 0.9840,\n    \"n\": 426,\n    \"lift\": 0.2520,\n    \"exp_id\": \"debugbench_no_trace_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B (DebugBench)\",\n    \"condition\": \"VOTA\",\n    \"accuracy\": 0.9977,\n    \"ci_lower\": 0.9930,\n    \"ci_upper\": 1.0000,\n    \"n\": 426,\n    \"lift\": 0.2826,\n    \"exp_id\": \"debugbench_vota_seed42\",\n    \"seeds\": 1\n  },\n  {\n    \"model\": \"Qwen-2.5-Coder-7B (DebugBench)\",\n    \"condition\": \"exception_only\",\n    \"accuracy\": 1.0000,\n    \"ci_lower\": 0.9914,\n    \"ci_upper\": 1.0000,\n    \"n\": 426,\n    \"lift\": 0.2849,\n    \"exp_id\": \"debugbench_exception_only_seed42\",\n    \"seeds\": 1\n  }\n]\n",
      "numLines": 244,
      "startLine": 1,
      "totalLines": 244
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01VtAMfGsoS53SyELq6ns5oU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/regex_baseline_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "267e149e-33d9-480c-9445-0441304269b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 38 · 2026-05-23T19:18:31.124Z_

<details><summary>↩ Tool result · `toolu_01VtAMfGsoS53SyELq6ns5oU`</summary>

```text
1	{
2	  "experiment_id": "regex_baseline_analysis",
3	  "dataset": "HumanEval+MBPP_exception_only_test",
4	  "n": 1190,
5	  "majority_baseline": 0.7151,
6	  "sft_exception_only": 0.9983,
7	  "baselines": {
8	    "B1_ERROR_presence": {
9	      "accuracy": 0.9345,
10	      "description": "Checks if 'ERROR' keyword appears in exception text"
11	    },
12	    "B2_Traceback": {
13	      "accuracy": 0.7151,
14	      "description": "Checks if 'Traceback' appears in exception text"
15	    },
16	    "B3_any_keyword": {
17	      "accuracy": 0.9345,
18	      "description": "Any error keyword match (union of patterns)"
19	    },
20	    "B4_exception_type": {
21	      "accuracy": 0.9361,
22	      "description": "Named exception type detection (e.g. ValueError, TypeError)"
23	    },
24	    "B5_format_marker": {
25	      "accuracy": 0.9933,
26	      "description": "Format-based verdict marker detection (structural pattern)"
27	    },
28	    "B6_error_count_ge2": {
29	      "accuracy": 0.9202,
30	      "description": "Two or more error occurrences in trace"
31	    }
32	  },
33	  "best_semantic_regex": {
34	    "name": "B4_exception_type",
35	    "accuracy": 0.9361,
36	    "gap_vs_sft_pp": -6.22
37	  },
38	  "best_overall_regex": {
39	    "name": "B5_format_marker",
40	    "accuracy": 0.9933,
41	    "gap_vs_sft_pp": -0.50,
42	    "mcnemar_p_vs_sft": 0.041
43	  },
44	  "conclusion": "Best regex 93.61% (semantic) / 99.33% (format). SFT 99.83% significantly better than strongest regex (McNemar p=0.041). SFT learns patterns beyond simple regex matching.",
45	  "source": "registry:regex_baseline_analysis"
46	}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "cfbe23bd-81f9-4115-ba75-d5c0e22c2cf9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/regex_baseline_results.json",
      "content": "{\n  \"experiment_id\": \"regex_baseline_analysis\",\n  \"dataset\": \"HumanEval+MBPP_exception_only_test\",\n  \"n\": 1190,\n  \"majority_baseline\": 0.7151,\n  \"sft_exception_only\": 0.9983,\n  \"baselines\": {\n    \"B1_ERROR_presence\": {\n      \"accuracy\": 0.9345,\n      \"description\": \"Checks if 'ERROR' keyword appears in exception text\"\n    },\n    \"B2_Traceback\": {\n      \"accuracy\": 0.7151,\n      \"description\": \"Checks if 'Traceback' appears in exception text\"\n    },\n    \"B3_any_keyword\": {\n      \"accuracy\": 0.9345,\n      \"description\": \"Any error keyword match (union of patterns)\"\n    },\n    \"B4_exception_type\": {\n      \"accuracy\": 0.9361,\n      \"description\": \"Named exception type detection (e.g. ValueError, TypeError)\"\n    },\n    \"B5_format_marker\": {\n      \"accuracy\": 0.9933,\n      \"description\": \"Format-based verdict marker detection (structural pattern)\"\n    },\n    \"B6_error_count_ge2\": {\n      \"accuracy\": 0.9202,\n      \"description\": \"Two or more error occurrences in trace\"\n    }\n  },\n  \"best_semantic_regex\": {\n    \"name\": \"B4_exception_type\",\n    \"accuracy\": 0.9361,\n    \"gap_vs_sft_pp\": -6.22\n  },\n  \"best_overall_regex\": {\n    \"name\": \"B5_format_marker\",\n    \"accuracy\": 0.9933,\n    \"gap_vs_sft_pp\": -0.50,\n    \"mcnemar_p_vs_sft\": 0.041\n  },\n  \"conclusion\": \"Best regex 93.61% (semantic) / 99.33% (format). SFT 99.83% significantly better than strongest regex (McNemar p=0.041). SFT learns patterns beyond simple regex matching.\",\n  \"source\": \"registry:regex_baseline_analysis\"\n}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01T6KupD5eWpsdxiXsDTPjBZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/debugbench_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "8df19667-dd6a-4878-ae74-e81f9f061d7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 40 · 2026-05-23T19:18:31.600Z_

<details><summary>↩ Tool result · `toolu_01T6KupD5eWpsdxiXsDTPjBZ`</summary>

```text
1	{
2	  "dataset": "DebugBench",
3	  "task_type": "bug_detection",
4	  "model": "Qwen-2.5-Coder-7B",
5	  "n_test": 426,
6	  "majority_baseline": 0.5141,
7	  "conditions": {
8	    "exception_only": {
9	      "accuracy": 1.0000,
10	      "accuracy_ci_wilson": [0.9914, 1.0000],
11	      "pass_precision": 1.0, "pass_recall": 1.0, "pass_f1": 1.0,
12	      "fail_precision": 1.0, "fail_recall": 1.0, "fail_f1": 1.0,
13	      "lift_vs_majority": 0.4859,
14	      "train_loss": 0.2435,
15	      "eval_loss": 0.4157,
16	      "exp_id": "debugbench_exception_only_seed42"
17	    },
18	    "vota": {
19	      "accuracy": 0.9977,
20	      "accuracy_ci": [0.993, 1.0],
21	      "pass_precision": 1.0, "pass_recall": 1.0, "pass_f1": 1.0,
22	      "fail_precision": 1.0, "fail_recall": 1.0, "fail_f1": 1.0,
23	      "lift_vs_majority": 0.4836,
24	      "errors": 1,
25	      "train_loss": 0.098,
26	      "eval_loss": 0.1179,
27	      "exp_id": "debugbench_vota_seed42"
28	    },
29	    "no_trace": {
30	      "accuracy": 0.9671,
31	      "accuracy_ci": [0.948, 0.984],
32	      "pass_precision": 1.0, "pass_recall": 0.936, "pass_f1": 0.967,
33	      "fail_precision": 0.937, "fail_recall": 1.0, "fail_f1": 0.967,
34	      "lift_vs_majority": 0.4531,
35	      "train_loss": 0.249,
36	      "eval_loss": 0.532,
37	      "exp_id": "debugbench_no_trace_seed42"
38	    }
39	  },
40	  "key_finding": "Exception_only achieves perfect accuracy (100%) on DebugBench, confirming cross-task generalization. Even no_trace baseline is 96.71% (DebugBench bugs almost always throw exceptions).",
41	  "source": "registry:debugbench_*_seed42"
42	}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "48757080-f271-46b0-a43e-3ae371d04b26",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/debugbench_results.json",
      "content": "{\n  \"dataset\": \"DebugBench\",\n  \"task_type\": \"bug_detection\",\n  \"model\": \"Qwen-2.5-Coder-7B\",\n  \"n_test\": 426,\n  \"majority_baseline\": 0.5141,\n  \"conditions\": {\n    \"exception_only\": {\n      \"accuracy\": 1.0000,\n      \"accuracy_ci_wilson\": [0.9914, 1.0000],\n      \"pass_precision\": 1.0, \"pass_recall\": 1.0, \"pass_f1\": 1.0,\n      \"fail_precision\": 1.0, \"fail_recall\": 1.0, \"fail_f1\": 1.0,\n      \"lift_vs_majority\": 0.4859,\n      \"train_loss\": 0.2435,\n      \"eval_loss\": 0.4157,\n      \"exp_id\": \"debugbench_exception_only_seed42\"\n    },\n    \"vota\": {\n      \"accuracy\": 0.9977,\n      \"accuracy_ci\": [0.993, 1.0],\n      \"pass_precision\": 1.0, \"pass_recall\": 1.0, \"pass_f1\": 1.0,\n      \"fail_precision\": 1.0, \"fail_recall\": 1.0, \"fail_f1\": 1.0,\n      \"lift_vs_majority\": 0.4836,\n      \"errors\": 1,\n      \"train_loss\": 0.098,\n      \"eval_loss\": 0.1179,\n      \"exp_id\": \"debugbench_vota_seed42\"\n    },\n    \"no_trace\": {\n      \"accuracy\": 0.9671,\n      \"accuracy_ci\": [0.948, 0.984],\n      \"pass_precision\": 1.0, \"pass_recall\": 0.936, \"pass_f1\": 0.967,\n      \"fail_precision\": 0.937, \"fail_recall\": 1.0, \"fail_f1\": 0.967,\n      \"lift_vs_majority\": 0.4531,\n      \"train_loss\": 0.249,\n      \"eval_loss\": 0.532,\n      \"exp_id\": \"debugbench_no_trace_seed42\"\n    }\n  },\n  \"key_finding\": \"Exception_only achieves perfect accuracy (100%) on DebugBench, confirming cross-task generalization. Even no_trace baseline is 96.71% (DebugBench bugs almost always throw exceptions).\",\n  \"source\": \"registry:debugbench_*_seed42\"\n}\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01J34hs4rjZhWbNdV1ArzMfX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "988e956c-4131-4381-a715-0c8f5472c194",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 42 · 2026-05-23T19:18:32.171Z_

<details><summary>↩ Tool result · `toolu_01J34hs4rjZhWbNdV1ArzMfX`</summary>

```text
1	qwen_7b: ECE=0.0027 MCE=0.8355 Brier=0.0013 Acc=0.9983\nqwen_1.5b: ECE=0.0020 MCE=0.7549 Brier=0.0013 Acc=0.9983\ncodellama_13b: ECE=0.0020 MCE=0.0411 Brier=0.0013 Acc=0.9983\ndeepseek_6.7b: ECE=0.0064 MCE=0.7756 Brier=0.0061 Acc=0.9933
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "ae162cc4-30a1-4660-8ebc-d9c61e31a50e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_results.json",
      "content": "qwen_7b: ECE=0.0027 MCE=0.8355 Brier=0.0013 Acc=0.9983\\nqwen_1.5b: ECE=0.0020 MCE=0.7549 Brier=0.0013 Acc=0.9983\\ncodellama_13b: ECE=0.0020 MCE=0.0411 Brier=0.0013 Acc=0.9983\\ndeepseek_6.7b: ECE=0.0064 MCE=0.7756 Brier=0.0061 Acc=0.9933",
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01UtihuUqdrhwBq6JgJnQWkH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/trace_ablation_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "516f01c5-dda7-444f-9010-dd049c8e05d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8HeDxygfejc6beaWYFkKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10025,
      "cache_read_input_tokens": 56627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10025
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

_source line 44 · 2026-05-23T19:18:32.850Z_

<details><summary>↩ Tool result · `toolu_01UtihuUqdrhwBq6JgJnQWkH`</summary>

```text
1	{
2	  "paired_tests": [
3	    {
4	      "pair": "256tok vs 512tok",
5	      "n_samples": 1190,
6	      "acc_a": 0.788235294117647,
7	      "acc_b": 0.8042016806722689,
8	      "diff": -0.015966386554621903,
9	      "ci_lower": -0.03529411764705892,
10	      "ci_upper": 0.003361344537815114,
11	      "p_value": 0.11698830116988301,
12	      "sig": "ns"
13	    },
14	    {
15	      "pair": "512tok vs 1024tok",
16	      "n_samples": 1190,
17	      "acc_a": 0.8042016806722689,
18	      "acc_b": 0.7722689075630252,
19	      "diff": 0.031932773109243695,
20	      "ci_lower": 0.01092436974789912,
21	      "ci_upper": 0.05294117647058827,
22	      "p_value": 0.0021997800219978004,
23	      "sig": "**"
24	    },
25	    {
26	      "pair": "1024tok vs no_limit",
27	      "n_samples": 1190,
28	      "acc_a": 0.7722689075630252,
29	      "acc_b": 0.8176470588235294,
30	      "diff": -0.04537815126050415,
31	      "ci_lower": -0.06554621848739495,
32	      "ci_upper": -0.025210084033613467,
33	      "p_value": 0.00019998000199980003,
34	      "sig": "***"
35	    },
36	    {
37	      "pair": "256tok vs no_limit",
38	      "n_samples": 1190,
39	      "acc_a": 0.788235294117647,
40	      "acc_b": 0.8176470588235294,
41	      "diff": -0.02941176470588236,
42	      "ci_lower": -0.05044117647058825,
43	      "ci_upper": -0.008403361344537896,
44	      "p_value": 0.0057994200579942,
45	      "sig": "**"
46	    },
47	    {
48	      "pair": "256tok vs no_trace",
49	      "n_samples": 1190,
50	      "acc_a": 0.788235294117647,
51	      "acc_b": 0.7512605042016807,
52	      "diff": 0.036974789915966366,
53	      "ci_lower": 0.014285714285714235,
54	      "ci_upper": 0.060504201680672276,
55	      "p_value": 0.0023997600239976003,
56	      "sig": "**"
57	    },
58	    {
59	      "pair": "512tok vs no_trace",
60	      "n_samples": 1190,
61	      "acc_a": 0.8042016806722689,
62	      "acc_b": 0.7512605042016807,
63	      "diff": 0.05294117647058827,
64	      "ci_lower": 0.030252100840336138,
65	      "ci_upper": 0.07563025210084029,
66	      "p_value": 0.00019998000199980003,
67	      "sig": "***"
68	    },
69	    {
70	      "pair": "1024tok vs no_trace",
71	      "n_samples": 1190,
72	      "acc_a": 0.7722689075630252,
73	      "acc_b": 0.7512605042016807,
74	      "diff": 0.021008403361344574,
75	      "ci_lower": -0.001680672268907557,
76	      "ci_upper": 0.043697478991596705,
77	      "p_value": 0.0775922407759224,
78	      "sig": "ns"
79	    },
80	    {
81	      "pair": "no_limit vs no_trace",
82	      "n_samples": 1190,
83	      "acc_a": 0.8176470588235294,
84	      "acc_b": 0.7512605042016807,
85	      "diff": 0.06638655462184873,
86	      "ci_lower": 0.043697478991596594,
87	      "ci_upper": 0.08991596638655464,
88	      "p_value": 0.00019998000199980003,
89	      "sig": "***"
90	    },
91	    {
92	      "pair": "256tok vs exception_only",
93	      "n_samples": 1190,
94	      "acc_a": 0.788235294117647,
95	      "acc_b": 0.9983193277310924,
96	      "diff": -0.2100840336134454,
97	      "ci_lower": -0.2344537815126051,
98	      "ci_upper": -0.18739495798319328,
99	      "p_value": 0.00019998000199980003,
100	      "sig": "***"
101	    },
102	    {
103	      "pair": "512tok vs exception_only",
104	      "n_samples": 1190,
105	      "acc_a": 0.8042016806722689,
106	      "acc_b": 0.9983193277310924,
107	      "diff": -0.1941176470588235,
108	      "ci_lower": -0.21764705882352942,
109	      "ci_upper": -0.17142857142857149,
110	      "p_value": 0.00019998000199980003,
111	      "sig": "***"
112	    },
113	    {
114	      "pair": "1024tok vs exception_only",
115	      "n_samples": 1190,
116	      "acc_a": 0.7722689075630252,
117	      "acc_b": 0.9983193277310924,
118	      "diff": -0.2260504201680672,
119	      "ci_lower": -0.2504201680672269,
120	      "ci_upper": -0.2025210084033614,
121	      "p_value": 0.00019998000199980003,
122	      "sig": "***"
123	    },
124	    {
125	      "pair": "no_limit vs exception_only",
126	      "n_samples": 1190,
127	      "acc_a": 0.8176470588235294,
128	      "acc_b": 0.9983193277310924,
129	      "diff": -0.18067226890756305,
130	      "ci_lower": -0.20336134453781518,
131	      "ci_upper": -0.1588235294117647,
132	      "p_value": 0.00019998000199980003,
133	      "sig": "***"
134	    }
135	  ],
136	  "per_condition_ci": {
137	    "256tok": {
138	      "acc": 0.788235294117647,
139	      "ci_lower": 0.7638655462184873,
140	      "ci_upper": 0.8109243697478992
141	    },
142	    "512tok": {
143	      "acc": 0.8042016806722689,
144	      "ci_lower": 0.7823529411764706,
145	      "ci_upper": 0.8260504201680672
146	    },
147	    "1024tok": {
148	      "acc": 0.7722689075630252,
149	      "ci_lower": 0.748718487394958,
150	      "ci_upper": 0.7966386554621848
151	    },
152	    "no_limit": {
153	      "acc": 0.8176470588235294,
154	      "ci_lower": 0.795798319327731,
155	      "ci_upper": 0.838655462184874
156	    },
157	    "no_trace": {
158	      "acc": 0.7512605042016807,
159	      "ci_lower": 0.7260504201680672,
160	      "ci_upper": 0.7756302521008404
161	    },
162	    "exception_only": {
163	      "acc": 0.9983193277310924,
164	      "ci_lower": 0.9957983193277311,
165	      "ci_upper": 1.0
166	    }
167	  },
168	  "config": {
169	    "n_bootstrap": 10000,
170	    "seed": 42
171	  }
172	}
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "be8461a0-46b0-4f45-97ef-61259b5c52c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/trace_ablation_bootstrap.json",
      "content": "{\n  \"paired_tests\": [\n    {\n      \"pair\": \"256tok vs 512tok\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.788235294117647,\n      \"acc_b\": 0.8042016806722689,\n      \"diff\": -0.015966386554621903,\n      \"ci_lower\": -0.03529411764705892,\n      \"ci_upper\": 0.003361344537815114,\n      \"p_value\": 0.11698830116988301,\n      \"sig\": \"ns\"\n    },\n    {\n      \"pair\": \"512tok vs 1024tok\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.8042016806722689,\n      \"acc_b\": 0.7722689075630252,\n      \"diff\": 0.031932773109243695,\n      \"ci_lower\": 0.01092436974789912,\n      \"ci_upper\": 0.05294117647058827,\n      \"p_value\": 0.0021997800219978004,\n      \"sig\": \"**\"\n    },\n    {\n      \"pair\": \"1024tok vs no_limit\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.7722689075630252,\n      \"acc_b\": 0.8176470588235294,\n      \"diff\": -0.04537815126050415,\n      \"ci_lower\": -0.06554621848739495,\n      \"ci_upper\": -0.025210084033613467,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    },\n    {\n      \"pair\": \"256tok vs no_limit\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.788235294117647,\n      \"acc_b\": 0.8176470588235294,\n      \"diff\": -0.02941176470588236,\n      \"ci_lower\": -0.05044117647058825,\n      \"ci_upper\": -0.008403361344537896,\n      \"p_value\": 0.0057994200579942,\n      \"sig\": \"**\"\n    },\n    {\n      \"pair\": \"256tok vs no_trace\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.788235294117647,\n      \"acc_b\": 0.7512605042016807,\n      \"diff\": 0.036974789915966366,\n      \"ci_lower\": 0.014285714285714235,\n      \"ci_upper\": 0.060504201680672276,\n      \"p_value\": 0.0023997600239976003,\n      \"sig\": \"**\"\n    },\n    {\n      \"pair\": \"512tok vs no_trace\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.8042016806722689,\n      \"acc_b\": 0.7512605042016807,\n      \"diff\": 0.05294117647058827,\n      \"ci_lower\": 0.030252100840336138,\n      \"ci_upper\": 0.07563025210084029,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    },\n    {\n      \"pair\": \"1024tok vs no_trace\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.7722689075630252,\n      \"acc_b\": 0.7512605042016807,\n      \"diff\": 0.021008403361344574,\n      \"ci_lower\": -0.001680672268907557,\n      \"ci_upper\": 0.043697478991596705,\n      \"p_value\": 0.0775922407759224,\n      \"sig\": \"ns\"\n    },\n    {\n      \"pair\": \"no_limit vs no_trace\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.8176470588235294,\n      \"acc_b\": 0.7512605042016807,\n      \"diff\": 0.06638655462184873,\n      \"ci_lower\": 0.043697478991596594,\n      \"ci_upper\": 0.08991596638655464,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    },\n    {\n      \"pair\": \"256tok vs exception_only\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.788235294117647,\n      \"acc_b\": 0.9983193277310924,\n      \"diff\": -0.2100840336134454,\n      \"ci_lower\": -0.2344537815126051,\n      \"ci_upper\": -0.18739495798319328,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    },\n    {\n      \"pair\": \"512tok vs exception_only\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.8042016806722689,\n      \"acc_b\": 0.9983193277310924,\n      \"diff\": -0.1941176470588235,\n      \"ci_lower\": -0.21764705882352942,\n      \"ci_upper\": -0.17142857142857149,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    },\n    {\n      \"pair\": \"1024tok vs exception_only\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.7722689075630252,\n      \"acc_b\": 0.9983193277310924,\n      \"diff\": -0.2260504201680672,\n      \"ci_lower\": -0.2504201680672269,\n      \"ci_upper\": -0.2025210084033614,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    },\n    {\n      \"pair\": \"no_limit vs exception_only\",\n      \"n_samples\": 1190,\n      \"acc_a\": 0.8176470588235294,\n      \"acc_b\": 0.9983193277310924,\n      \"diff\": -0.18067226890756305,\n      \"ci_lower\": -0.20336134453781518,\n      \"ci_upper\": -0.1588235294117647,\n      \"p_value\": 0.00019998000199980003,\n      \"sig\": \"***\"\n    }\n  ],\n  \"per_condition_ci\": {\n    \"256tok\": {\n      \"acc\": 0.788235294117647,\n      \"ci_lower\": 0.7638655462184873,\n      \"ci_upper\": 0.8109243697478992\n    },\n    \"512tok\": {\n      \"acc\": 0.8042016806722689,\n      \"ci_lower\": 0.7823529411764706,\n      \"ci_upper\": 0.8260504201680672\n    },\n    \"1024tok\": {\n      \"acc\": 0.7722689075630252,\n      \"ci_lower\": 0.748718487394958,\n      \"ci_upper\": 0.7966386554621848\n    },\n    \"no_limit\": {\n      \"acc\": 0.8176470588235294,\n      \"ci_lower\": 0.795798319327731,\n      \"ci_upper\": 0.838655462184874\n    },\n    \"no_trace\": {\n      \"acc\": 0.7512605042016807,\n      \"ci_lower\": 0.7260504201680672,\n      \"ci_upper\": 0.7756302521008404\n    },\n    \"exception_only\": {\n      \"acc\": 0.9983193277310924,\n      \"ci_lower\": 0.9957983193277311,\n      \"ci_upper\": 1.0\n    }\n  },\n  \"config\": {\n    \"n_bootstrap\": 10000,\n    \"seed\": 42\n  }\n}\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key data sources. Let me also look for more experiment data for the experiments not in the registry - particularly Qwen-7B per-class metrics, cross-dataset results, and nomarker experiments. Let me also look for the full set of per-seed data.

Let me also look for more artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "c982a010-e5ce-4989-ab71-6cc24d6e9c1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CBCHSNer9n1nBo1BDaDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7948,
      "cache_read_input_tokens": 66652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7948
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

_source line 46_

Let me fetch more data files for remaining tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "aa7f9e5b-453f-46ac-8b6e-46c0118e7469",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CBCHSNer9n1nBo1BDaDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7948,
      "cache_read_input_tokens": 66652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7948
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

_source line 47_

<details open><summary>🔧 Tool call — Glob · `toolu_01Fu78pbQDpaQfhsKFfJy25M`</summary>

```json
{
  "pattern": "**/artifacts/**/*calibration*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "1a9cd4e8-8395-4e58-959a-7f59de89e174",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CBCHSNer9n1nBo1BDaDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7948,
      "cache_read_input_tokens": 66652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7948
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

<details open><summary>🔧 Tool call — Glob · `toolu_01DjZBdkrT4pu9ZLGjpWnC9C`</summary>

```json
{
  "pattern": "**/artifacts/**/*nomarker*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "2adce490-19cc-4be9-bf03-daea5714bc47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CBCHSNer9n1nBo1BDaDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7948,
      "cache_read_input_tokens": 66652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7948
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

_source line 49 · 2026-05-23T19:18:40.086Z_

<details><summary>↩ Tool result · `toolu_01Fu78pbQDpaQfhsKFfJy25M`</summary>

```text
artifacts/plot_calibration.py
artifacts/calibration_analysis_seed42/chart/calibration_reliability_diagram_info.txt
artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt
artifacts/calibration_analysis_seed42/data/calibration_v2.py
artifacts/_project/chart/fig2_calibration.pdf
artifacts/_project/chart/fig2_calibration_info.md
artifacts/_project/chart/calibration_reliability_ref.md
artifacts/_project/report/cross_model_calibration.md
artifacts/cross_model_calibration.md
artifacts/_project/data/cross_model_calibration_results.json
artifacts/_project/report/calibration_report.md
artifacts/calibration_report.md
artifacts/_project/report/calibration_analysis.md
artifacts/calibration_analysis.md
artifacts/_project/paper/figures/calibration_reliability.pdf
artifacts/_project/paper/figures/calibration_reliability.png
artifacts/_project/report/calibration_cross_model_analysis.md
artifacts/calibration_cross_model_analysis.md
artifacts/cross_model_calibration/data/cross_model_calibration_results.txt
artifacts/_project/report/cross_model_calibration_plan019.md
artifacts/_project/chart/cross_model_calibration_plan019_diagram_ref.txt
artifacts/_project/data/cross_model_calibration_plan019_data.txt
artifacts/_project/report/cross_model_calibration_plan019_a3fb00.md
artifacts/cross_model_calibration_plan019.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "e66080b5-5754-4452-8b74-fe0703fa6a38",
  "tool_use_result": {
    "filenames": [
      "artifacts/plot_calibration.py",
      "artifacts/calibration_analysis_seed42/chart/calibration_reliability_diagram_info.txt",
      "artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt",
      "artifacts/calibration_analysis_seed42/data/calibration_v2.py",
      "artifacts/_project/chart/fig2_calibration.pdf",
      "artifacts/_project/chart/fig2_calibration_info.md",
      "artifacts/_project/chart/calibration_reliability_ref.md",
      "artifacts/_project/report/cross_model_calibration.md",
      "artifacts/cross_model_calibration.md",
      "artifacts/_project/data/cross_model_calibration_results.json",
      "artifacts/_project/report/calibration_report.md",
      "artifacts/calibration_report.md",
      "artifacts/_project/report/calibration_analysis.md",
      "artifacts/calibration_analysis.md",
      "artifacts/_project/paper/figures/calibration_reliability.pdf",
      "artifacts/_project/paper/figures/calibration_reliability.png",
      "artifacts/_project/report/calibration_cross_model_analysis.md",
      "artifacts/calibration_cross_model_analysis.md",
      "artifacts/cross_model_calibration/data/cross_model_calibration_results.txt",
      "artifacts/_project/report/cross_model_calibration_plan019.md",
      "artifacts/_project/chart/cross_model_calibration_plan019_diagram_ref.txt",
      "artifacts/_project/data/cross_model_calibration_plan019_data.txt",
      "artifacts/_project/report/cross_model_calibration_plan019_a3fb00.md",
      "artifacts/cross_model_calibration_plan019.md"
    ],
    "durationMs": 24,
    "numFiles": 24,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T19:18:40.090Z_

<details><summary>↩ Tool result · `toolu_01DjZBdkrT4pu9ZLGjpWnC9C`</summary>

```text
artifacts/nomarker_command.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "70de81ee-49aa-4c11-a611-42bbba619520",
  "tool_use_result": {
    "filenames": [
      "artifacts/nomarker_command.txt"
    ],
    "durationMs": 21,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Glob · `toolu_015qPSYRe33bw8TMQt691TUz`</summary>

```json
{
  "pattern": "**/artifacts/**/*cross*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "0db6981c-f3b3-4603-968f-6a63777b0a19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CBCHSNer9n1nBo1BDaDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7948,
      "cache_read_input_tokens": 66652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7948
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

_source line 52 · 2026-05-23T19:18:40.569Z_

<details><summary>↩ Tool result · `toolu_015qPSYRe33bw8TMQt691TUz`</summary>

```text
artifacts/cross_model_analysis/cross_model_comparison.md
artifacts/_project/report/cross_model_comparison.md
artifacts/_project/chart/fig3_cross_model_gap.pdf
artifacts/exception_only_seed_cross_analysis.md
artifacts/_project/chart/fig3_cross_model_gap_info.md
artifacts/_project/report/debugbench_cross_task_analysis.md
artifacts/debugbench_cross_task_analysis.md
artifacts/_project/report/cross_model_exception_only_overlap.md
artifacts/cross_model_exception_only_overlap.md
artifacts/_project/paper/cross_family_analysis_draft.md
artifacts/cross_family_analysis_draft.md
artifacts/_project/report/cross_model_comparison_table.md
artifacts/cross_model_comparison_table.md
artifacts/_project/report/cross_model_calibration.md
artifacts/cross_model_calibration.md
artifacts/_project/data/cross_model_calibration_results.json
artifacts/_project/report/calibration_cross_model_analysis.md
artifacts/calibration_cross_model_analysis.md
artifacts/cross_model_calibration/data/cross_model_calibration_results.txt
artifacts/_project/report/cross_model_calibration_plan019.md
artifacts/_project/chart/cross_model_calibration_plan019_diagram_ref.txt
artifacts/_project/data/cross_model_calibration_plan019_data.txt
artifacts/_project/report/cross_model_calibration_plan019_a3fb00.md
artifacts/cross_model_calibration_plan019.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "0fc7090f-2adb-43f2-8a4c-ffb9bf137580",
  "tool_use_result": {
    "filenames": [
      "artifacts/cross_model_analysis/cross_model_comparison.md",
      "artifacts/_project/report/cross_model_comparison.md",
      "artifacts/_project/chart/fig3_cross_model_gap.pdf",
      "artifacts/exception_only_seed_cross_analysis.md",
      "artifacts/_project/chart/fig3_cross_model_gap_info.md",
      "artifacts/_project/report/debugbench_cross_task_analysis.md",
      "artifacts/debugbench_cross_task_analysis.md",
      "artifacts/_project/report/cross_model_exception_only_overlap.md",
      "artifacts/cross_model_exception_only_overlap.md",
      "artifacts/_project/paper/cross_family_analysis_draft.md",
      "artifacts/cross_family_analysis_draft.md",
      "artifacts/_project/report/cross_model_comparison_table.md",
      "artifacts/cross_model_comparison_table.md",
      "artifacts/_project/report/cross_model_calibration.md",
      "artifacts/cross_model_calibration.md",
      "artifacts/_project/data/cross_model_calibration_results.json",
      "artifacts/_project/report/calibration_cross_model_analysis.md",
      "artifacts/calibration_cross_model_analysis.md",
      "artifacts/cross_model_calibration/data/cross_model_calibration_results.txt",
      "artifacts/_project/report/cross_model_calibration_plan019.md",
      "artifacts/_project/chart/cross_model_calibration_plan019_diagram_ref.txt",
      "artifacts/_project/data/cross_model_calibration_plan019_data.txt",
      "artifacts/_project/report/cross_model_calibration_plan019_a3fb00.md",
      "artifacts/cross_model_calibration_plan019.md"
    ],
    "durationMs": 13,
    "numFiles": 24,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Glob · `toolu_01ADKFK7kMA2qzUFhgkaVe7j`</summary>

```json
{
  "pattern": "**/artifacts/**/*per_class*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "aa904444-5a99-49c5-b48c-e3a915764f87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4CBCHSNer9n1nBo1BDaDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7948,
      "cache_read_input_tokens": 66652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7948
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

_source line 54 · 2026-05-23T19:18:40.673Z_

<details><summary>↩ Tool result · `toolu_01ADKFK7kMA2qzUFhgkaVe7j`</summary>

```text
artifacts/per_class_breakdown.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "9711b9ea-c69f-4d84-9e81-c2e0be08e2d9",
  "tool_use_result": {
    "filenames": [
      "artifacts/per_class_breakdown.tex"
    ],
    "durationMs": 16,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01M54mu6Xe6v92wdLPENfVAm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "ffafadfb-85fa-428a-a8e7-171d793d36fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01519kAWWy5Nd7t2TtnhnGRn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 74600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 56 · 2026-05-23T19:18:44.683Z_

<details><summary>↩ Tool result · `toolu_01M54mu6Xe6v92wdLPENfVAm`</summary>

```text
1	Server path: /root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json
2	
3	Summary:
4	No Trace:       Acc=0.7513  ECE=0.1715  MCE=0.4754  Brier=0.1972
5	Full Trace:     Acc=0.8176  ECE=0.0946  MCE=0.2490  Brier=0.1438
6	Exception Only: Acc=0.9983  ECE=0.0024  MCE=0.8359  Brier=0.0013
7	VOTA:           Acc=0.9941  ECE=0.0054  MCE=0.6211  Brier=0.0052
8	
9	Note: High MCE for Exception Only and VOTA is due to sparse low-confidence bins (1-2 samples).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "101c76b0-9865-460a-b986-92738b4c073c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/calibration_analysis_seed42/data/calibration_metrics_summary.txt",
      "content": "Server path: /root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json\n\nSummary:\nNo Trace:       Acc=0.7513  ECE=0.1715  MCE=0.4754  Brier=0.1972\nFull Trace:     Acc=0.8176  ECE=0.0946  MCE=0.2490  Brier=0.1438\nException Only: Acc=0.9983  ECE=0.0024  MCE=0.8359  Brier=0.0013\nVOTA:           Acc=0.9941  ECE=0.0054  MCE=0.6211  Brier=0.0052\n\nNote: High MCE for Exception Only and VOTA is due to sparse low-confidence bins (1-2 samples).",
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

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01Vbus5EFCAXr4ZvzqgaSa3v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/cross_model_calibration.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "366bbf32-af44-4914-b14f-d429ea2fc3c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01519kAWWy5Nd7t2TtnhnGRn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 74600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 58 · 2026-05-23T19:18:45.176Z_

<details><summary>↩ Tool result · `toolu_01Vbus5EFCAXr4ZvzqgaSa3v`</summary>

```text
1	# Cross-Model Calibration Analysis: Exception-Only Condition
2	
3	**Date**: 2026-05-18
4	**Test set**: 1190 samples (851 pass, 339 fail)
5	**Method**: Greedy generation + logit-based confidence (softmax over pass/fail token logits)
6	**Bins**: 10 equal-width bins from 0.5 to 1.0
7	
8	## Summary Table
9	
10	| Model | Accuracy | ECE | MCE | Brier Score |
11	|---|---|---|---|---|
12	| Qwen-7B | 0.9983 | 0.002717 | 0.8355 | 0.001311 |
13	| Qwen-1.5B | 0.9983 | 0.001976 | 0.7549 | 0.001255 |
14	| DeepSeek-6.7B | 0.9933 | 0.006411 | 0.7756 | 0.006126 |
15	| CodeLlama-13B | 0.9983 | 0.002039 | 0.0411 | 0.001310 |
16	
17	## Per-Class Calibration
18	
19	| Model | Class | ECE | MCE | Brier | n |
20	|---|---|---|---|---|---|
21	| Qwen-7B | pass | 0.0037 | 0.8355 | 0.0018 | 851 |
22	| Qwen-7B | fail | 0.0003 | 0.0003 | 0.0000 | 339 |
23	| Qwen-1.5B | pass | 0.0027 | 0.7549 | 0.0018 | 851 |
24	| Qwen-1.5B | fail | 0.0003 | 0.0003 | 0.0000 | 339 |
25	| DeepSeek-6.7B | pass | 0.0069 | 0.9149 | 0.0081 | 851 |
26	| DeepSeek-6.7B | fail | 0.0079 | 0.4073 | 0.0012 | 339 |
27	| CodeLlama-13B | pass | 0.0016 | 0.0411 | 0.0018 | 851 |
28	| CodeLlama-13B | fail | 0.0033 | 0.0033 | 0.0000 | 339 |
29	
30	## Reliability Diagram Data (non-empty bins only)
31	
32	### Qwen-7B
33	| Bin | Confidence | Accuracy | Count |
34	|---|---|---|---|
35	| [0.80, 0.85) | 0.835 | 0.000 | 1 |
36	| [0.90, 0.95) | 0.942 | 0.857 | 7 |
37	| [0.95, 1.00] | 0.998 | 1.000 | 1182 |
38	
39	### Qwen-1.5B
40	| Bin | Confidence | Accuracy | Count |
41	|---|---|---|---|
42	| [0.75, 0.80) | 0.755 | 0.000 | 1 |
43	| [0.90, 0.95) | 0.907 | 0.857 | 7 |
44	| [0.95, 1.00] | 0.999 | 1.000 | 1182 |
45	
46	### DeepSeek-6.7B
47	| Bin | Confidence | Accuracy | Count |
48	|---|---|---|---|
49	| [0.55, 0.60) | 0.593 | 1.000 | 1 |
50	| [0.75, 0.80) | 0.798 | 1.000 | 2 |
51	| [0.80, 0.85) | 0.835 | 1.000 | 1 |
52	| [0.85, 0.90) | 0.883 | 1.000 | 8 |
53	| [0.90, 0.95) | 0.918 | 0.143 | 7 |
54	| [0.95, 1.00] | 0.998 | 0.998 | 1171 |
55	
56	### CodeLlama-13B
57	| Bin | Confidence | Accuracy | Count |
58	|---|---|---|---|
59	| [0.70, 0.75) | 0.709 | 0.750 | 8 |
60	| [0.95, 1.00] | 0.998 | 1.000 | 1182 |
61	
62	## Key Findings
63	
64	1. **ECE is uniformly low across all 4 models** (0.002 to 0.006), confirming that exception-only fine-tuning produces well-calibrated classifiers regardless of base model architecture or size.
65	
66	2. **Accuracy is consistent**: 3 of 4 models achieve identical 99.83% accuracy. DeepSeek-6.7B is slightly lower at 99.33% (8 errors vs 2 for others).
67	
68	3. **MCE is misleading for 3 models**: Qwen-7B (0.84), Qwen-1.5B (0.75), and DeepSeek-6.7B (0.78) have high MCE values driven by 1-sample bins where a single wrong prediction creates |conf - acc| close to the confidence value. These are not systematic calibration failures.
69	
70	4. **CodeLlama-13B has the best calibration profile**: ECE=0.002, MCE=0.041. Its 8 uncertain samples land in [0.70, 0.75) with 75% accuracy, closely matching confidence. This is the only model where uncertain predictions are also well-calibrated.
71	
72	5. **DeepSeek-6.7B has a distinct failure mode**: Its [0.90, 0.95) bin shows 7 samples with mean confidence 0.918 but only 14.3% accuracy (6/7 wrong). These are overconfident misclassifications, unlike the other models where errors concentrate in lower-confidence bins.
73	
74	6. **Confidence distribution is extreme**: For all models, 98.4-99.3% of samples fall in the [0.95, 1.00] bin. The models are overwhelmingly confident and overwhelmingly correct.
75	
76	## Checkpoint Paths
77	- Qwen-7B: `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/`
78	- Qwen-1.5B: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/`
79	- DeepSeek-6.7B: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/`
80	- CodeLlama-13B: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/`
81	
82	## Raw JSON Results
83	Server path: `/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/`
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "f84b6134-b044-4288-8458-46eaaf6c4b7c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/report/cross_model_calibration.md",
      "content": "# Cross-Model Calibration Analysis: Exception-Only Condition\n\n**Date**: 2026-05-18\n**Test set**: 1190 samples (851 pass, 339 fail)\n**Method**: Greedy generation + logit-based confidence (softmax over pass/fail token logits)\n**Bins**: 10 equal-width bins from 0.5 to 1.0\n\n## Summary Table\n\n| Model | Accuracy | ECE | MCE | Brier Score |\n|---|---|---|---|---|\n| Qwen-7B | 0.9983 | 0.002717 | 0.8355 | 0.001311 |\n| Qwen-1.5B | 0.9983 | 0.001976 | 0.7549 | 0.001255 |\n| DeepSeek-6.7B | 0.9933 | 0.006411 | 0.7756 | 0.006126 |\n| CodeLlama-13B | 0.9983 | 0.002039 | 0.0411 | 0.001310 |\n\n## Per-Class Calibration\n\n| Model | Class | ECE | MCE | Brier | n |\n|---|---|---|---|---|---|\n| Qwen-7B | pass | 0.0037 | 0.8355 | 0.0018 | 851 |\n| Qwen-7B | fail | 0.0003 | 0.0003 | 0.0000 | 339 |\n| Qwen-1.5B | pass | 0.0027 | 0.7549 | 0.0018 | 851 |\n| Qwen-1.5B | fail | 0.0003 | 0.0003 | 0.0000 | 339 |\n| DeepSeek-6.7B | pass | 0.0069 | 0.9149 | 0.0081 | 851 |\n| DeepSeek-6.7B | fail | 0.0079 | 0.4073 | 0.0012 | 339 |\n| CodeLlama-13B | pass | 0.0016 | 0.0411 | 0.0018 | 851 |\n| CodeLlama-13B | fail | 0.0033 | 0.0033 | 0.0000 | 339 |\n\n## Reliability Diagram Data (non-empty bins only)\n\n### Qwen-7B\n| Bin | Confidence | Accuracy | Count |\n|---|---|---|---|\n| [0.80, 0.85) | 0.835 | 0.000 | 1 |\n| [0.90, 0.95) | 0.942 | 0.857 | 7 |\n| [0.95, 1.00] | 0.998 | 1.000 | 1182 |\n\n### Qwen-1.5B\n| Bin | Confidence | Accuracy | Count |\n|---|---|---|---|\n| [0.75, 0.80) | 0.755 | 0.000 | 1 |\n| [0.90, 0.95) | 0.907 | 0.857 | 7 |\n| [0.95, 1.00] | 0.999 | 1.000 | 1182 |\n\n### DeepSeek-6.7B\n| Bin | Confidence | Accuracy | Count |\n|---|---|---|---|\n| [0.55, 0.60) | 0.593 | 1.000 | 1 |\n| [0.75, 0.80) | 0.798 | 1.000 | 2 |\n| [0.80, 0.85) | 0.835 | 1.000 | 1 |\n| [0.85, 0.90) | 0.883 | 1.000 | 8 |\n| [0.90, 0.95) | 0.918 | 0.143 | 7 |\n| [0.95, 1.00] | 0.998 | 0.998 | 1171 |\n\n### CodeLlama-13B\n| Bin | Confidence | Accuracy | Count |\n|---|---|---|---|\n| [0.70, 0.75) | 0.709 | 0.750 | 8 |\n| [0.95, 1.00] | 0.998 | 1.000 | 1182 |\n\n## Key Findings\n\n1. **ECE is uniformly low across all 4 models** (0.002 to 0.006), confirming that exception-only fine-tuning produces well-calibrated classifiers regardless of base model architecture or size.\n\n2. **Accuracy is consistent**: 3 of 4 models achieve identical 99.83% accuracy. DeepSeek-6.7B is slightly lower at 99.33% (8 errors vs 2 for others).\n\n3. **MCE is misleading for 3 models**: Qwen-7B (0.84), Qwen-1.5B (0.75), and DeepSeek-6.7B (0.78) have high MCE values driven by 1-sample bins where a single wrong prediction creates |conf - acc| close to the confidence value. These are not systematic calibration failures.\n\n4. **CodeLlama-13B has the best calibration profile**: ECE=0.002, MCE=0.041. Its 8 uncertain samples land in [0.70, 0.75) with 75% accuracy, closely matching confidence. This is the only model where uncertain predictions are also well-calibrated.\n\n5. **DeepSeek-6.7B has a distinct failure mode**: Its [0.90, 0.95) bin shows 7 samples with mean confidence 0.918 but only 14.3% accuracy (6/7 wrong). These are overconfident misclassifications, unlike the other models where errors concentrate in lower-confidence bins.\n\n6. **Confidence distribution is extreme**: For all models, 98.4-99.3% of samples fall in the [0.95, 1.00] bin. The models are overwhelmingly confident and overwhelmingly correct.\n\n## Checkpoint Paths\n- Qwen-7B: `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/`\n- Qwen-1.5B: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_exception_only_seed42/final/`\n- DeepSeek-6.7B: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only/final/`\n- CodeLlama-13B: `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed42/final/`\n\n## Raw JSON Results\nServer path: `/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/`\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_019L9sEiTztahZbFMAoZ5ZeU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_plan019_data.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "d62ad623-d3b7-49cd-bd74-b078dde7f5ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01519kAWWy5Nd7t2TtnhnGRn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1183,
      "cache_read_input_tokens": 74600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1183
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 60 · 2026-05-23T19:18:45.700Z_

<details><summary>↩ Tool result · `toolu_019L9sEiTztahZbFMAoZ5ZeU`</summary>

```text
1	Qwen2.5-7B: acc=0.9983 ece=0.002717 mce=0.835484 brier=0.001311 conf=0.998006
2	DeepSeek-6.7B: acc=0.9933 ece=0.004890 mce=0.469227 brier=0.005887 conf=0.997062
3	CodeLlama-13B: acc=0.9983 ece=0.001971 mce=0.041056 brier=0.001310 conf=0.996348
4	Qwen2.5-1.5B: acc=0.9983 ece=0.001976 mce=0.754915 brier=0.001255 conf=0.998203
5	
6	Full JSON with reliability bins at remote: /root/trace-verdict-study/artifacts/cross_model_calibration_plan019.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "801b4d3e-0541-44a5-aaa4-ccb5337930e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/data/cross_model_calibration_plan019_data.txt",
      "content": "Qwen2.5-7B: acc=0.9983 ece=0.002717 mce=0.835484 brier=0.001311 conf=0.998006\nDeepSeek-6.7B: acc=0.9933 ece=0.004890 mce=0.469227 brier=0.005887 conf=0.997062\nCodeLlama-13B: acc=0.9983 ece=0.001971 mce=0.041056 brier=0.001310 conf=0.996348\nQwen2.5-1.5B: acc=0.9983 ece=0.001976 mce=0.754915 brier=0.001255 conf=0.998203\n\nFull JSON with reliability bins at remote: /root/trace-verdict-study/artifacts/cross_model_calibration_plan019.json",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Now I'm seeing a discrepancy. There are two sets of calibration results for DeepSeek-6.7B:

1. cross_model_calibration.md: ECE=0.006411, Brier=0.006126
2. cross_model_calibration_plan019_data.txt: ECE=0.004890, Brier=0.005887
3. cross_model_calibration_results.json: ECE=0.0064, Brier=0.0061

The paper's tab:calibration_cross says:


- DeepSeek-6.7B: ECE=0.0064, Brier=0.0061

And tab:calibration_model_level says:
- DeepSeek-6.7B: ECE=0.0048, Brier=0.0059

So there are two different calibration tables in the paper with different DeepSeek ECE values (0.0064 vs 0.0048). Let me check the actual table definitions to understand which one is which. I'm noticing a discrepancy across the appendix tables—the calibration metrics for the same models are showing different values depending on which table I'm looking at. For instance, Qwen-1.5B has an ECE of 0.0020 in one table but 0.0014 in another, and similar inconsistencies appear for Qwen-7B and CodeLlama-13B.

Looking at the raw data sources, I can see the cross-model calibration files are reporting slightly different ECE values as well—Qwen-7B shows 0.002717 consistently, but DeepSeek ranges from 0.006411 to 0.004890 depending on the source, which suggests there may be different experimental runs or data processing methods being used. I'm noticing inconsistencies in the ECE values across different sources—the calibration_metrics_summary.txt shows 0.0024 for exception_only, but cross_model_calibration.md reports 0.002717, and the paper itself uses 0.0027. These discrepancies stem from different binning strategies and data sources, which creates conflicting values within the same document that need to be reconciled. I need to track down where the ae_only calibration numbers are coming from, but let me focus on verifying what I can against the actual data first. Looking at the cross-model results in the table, I'm checking each model's performance metrics against the seed-based calculations to see if the reported means and standard deviations match up.

For the VOTA results, I'm noticing a discrepancy—the paper reports 99.05±0.38 for Qwen-7B, but the final table only shows a single seed result of 0.9941. However, when I look at the full results across all three seeds (42, 123, and 456), the mean works out to exactly 99.05 with the correct standard deviation, so the paper is using the multi-seed average rather than just the single seed value.

Now I'm going through all the tables systematically to verify each reported number.

Looking at the per-class appendix table, I see it's labeled as using seed 42 values, but the VOTA row shows 99.05 for Qwen-2.5-7B—which is the 3-seed mean, not the seed 42 result of 99.41. This is inconsistent with what the table caption claims. So the per_class table is showing the 3-seed mean values, not the seed 42 values as the caption suggests. For loop_only, the mean is 86.05%, but the actual seed 42 result should be 85.63%. I need to figure out which seed corresponds to which position in the seed_values array to confirm this discrepancy. I'm noticing a fundamental inconsistency in the per_class table for VOTA Qwen-7B: the accuracy value of 99.05% matches the 3-seed mean, but the precision/recall/F1 metrics appear to be from a single seed run (seed 42), which shouldn't be averaged across seeds anyway. This suggests either the row mixes statistics from different sources, or there's an error in how the table was constructed. Let me verify by checking if the individual error counts align with seed 42's accuracy of 99.41%. The numbers still don't align—if there are 11 errors total, the Pass recall should be around 98.71%, but the table shows 99.18%, which would only account for about 7 errors. When I work backward from the Pass recall of 99.18%, I get an accuracy of 99.41%, which matches seed 42's results, not the 99.05% listed in the Acc column. So there's definitely an inconsistency here between the reported accuracy and the per-class metrics in this row.

Now let me verify the same pattern holds for the loop_only results with Qwen-7B to see if this is a systematic issue. So the P/R/F1 values in the per-class results are actually from seed 42, not the 3-seed mean—that's why there's a mismatch with the reported accuracy. For label_only with the full trace condition, the same issue appears: the accuracy shown is 85.94 (the mean), but the precision and recall metrics correspond to seed 42's run where accuracy was 86.22. Let me verify this by working through the pass and fail recall rates to reconstruct the error counts.

Now I'm checking the other conditions to see if this inconsistency is widespread. No Trace and Exception Only appear consistent, but Full Trace shows a discrepancy between what's reported in the per-class table versus the aggregated results.

Looking more carefully at the pattern, I'm finding that VOTA, loop_only, and label_only all have the same issue: the accuracy values in the table don't match what seed 42 actually produced, suggesting the metrics are being pulled from different seeds or averaging methods inconsistently.

For Full Trace, the data shows three seeds with accuracies of 81.76, 80.20, and 82.35, averaging to 81.44, but the table reports 81.76 which matches seed 42 specifically.

Now checking AE Only, the per-class metrics show 99.92 accuracy which corresponds to seed 42 from the source data. But I'm noticing a pattern across multiple rows: VOTA, loop_only, and Full Trace are all reporting 3-seed means for accuracy while their precision, recall, and F1 scores come from seed 42 alone. The caption indicates everything should be from seed 42, so these accuracy values are inconsistent with what they claim.

Let me examine the full results table for Qwen-7B to see if this pattern continues elsewhere.

Looking at exception_only, all three seeds converge to 99.83 with zero variance, which checks out. For ae_only, the three seeds are 99.92, 99.08, and 99.92, giving a mean of 99.64 with standard deviation of 0.49—that's correct. Now checking VOTA's values across seeds... I'm checking the label_only results across the three seeds—86.22, 86.89, and 84.70—which average to 85.94 with a standard deviation of 1.12, matching what's shown in the table. But I notice table1_final only lists two seed values for label_only, so I need to reconcile which seeds correspond to which accuracy scores. I'm realizing the table1_final.json might be from an earlier snapshot with incomplete data, so I should trust the paper's reported values instead. Looking at the discrepancy more carefully—the paper reports a 3-seed mean of 85.94±1.12 for the label-only condition, but table1_final shows 0.8648 (86.48%), which matches a 2-seed average instead, suggesting these are different experimental runs or the JSON file wasn't updated with the final results.

Now I'm verifying the math on the reported numbers themselves. For loop_only, the three seed runs give 85.63, 85.88, and 86.64, which average to 86.05 with a standard deviation of 0.52—both match what's reported. Moving to full_trace with seeds 42, 123, and 456 yielding 81.76, 80.20, and 82.35...

Checking the calculations for full_trace and no_trace, then moving into the appendix table for deepseek results where I'm verifying the exception_only configuration across different seeds matches the registry values and reported means. Continuing to verify the full trace results with confidence intervals, then checking the exception subcomponent metrics where the exception type only variant shows perfect accuracy across all measures, while the stacktrace variant is still being prepared but follows the expected error pattern. Continuing to verify the trace length ablation results against the bootstrap confidence intervals from the source data. I'm verifying the confidence intervals for the 512 vs 256 token comparison—the data shows a difference of +1.60 percentage points, and when I flip the direction to match the paper's convention, the CI converts from [-0.0353, +0.0034] to [-0.34, +3.53], which aligns with what's reported.

Now checking the remaining comparisons: the 1024 vs 512 pair shows a -3.19pp difference with a p-value of 0.002 and CI of [-5.29, -1.09], all matching the paper. For the no_limit vs 1024 comparison, the data gives -4.54pp which flips to +4.54pp in the paper's direction, and the confidence interval is converting to [+2.52, +6.55]. Continuing through the remaining comparisons—512 versus no_trace shows a 5.29 percentage point difference with strong significance, while 1024 versus no_trace is marginal at 2.10pp with p=0.078. The no_limit condition pulls ahead substantially at 6.64pp difference. Now moving into the exception_only comparisons. Now I'm checking the calibration metrics for Qwen-7B across different configurations—looking at ECE and Brier scores to see how well the model's confidence aligns with actual accuracy. The values mostly match what's reported in the paper, though there's a slight discrepancy in the full trace ECE that I need to investigate.

I'm noticing the calibration_metrics_summary.txt uses a different binning strategy (0-1 range) compared to the cross_model_calibration data (0.5-1.0 range), which explains why the ECE values differ. When I cross-reference the exception_only condition, the values align perfectly, confirming the data is consistent across sources. The rounding discrepancy for ECE is minor—0.0946 should round to 0.095 at three decimal places, but the paper shows 0.096, likely from a different run or slight variation. Now I'm looking at the cross-model calibration results from the appendix table, checking ECE and Brier scores across different model sizes. Now I'm verifying the remaining model metrics from the calibration table against the paper's reported values, checking that DeepSeek and CodeLlama entries all align correctly. Now I'm comparing the ECE values across different sources and noticing some inconsistencies—the plan019 data shows Qwen2.5-1.5B at 0.001976, but the paper's calibration table lists it as 0.0014, which is a significant discrepancy that doesn't align with rounding. For DeepSeek the rounding checks out, but Qwen-7B is puzzling—the data shows 0.002717 while the paper reports 0.0017, which is too large a gap to be rounding error. Both my data and the cross-model calibration file agree on 0.002717, so I'm wondering if these tables used different binning strategies. Let me look at the Mean Confidence values to see if they align with the ECE calculations. Looking at the ECE values across both tables, I'm noticing a pattern where CodeLlama stays consistent at 0.0020, but the other models show different values depending on which table they're in. DeepSeek drops from 0.0064 to 0.0048, and Qwen models also shift between tables. This confirms what the user flagged earlier—the two calibration tables are using different bin configurations for their ECE calculations, which explains why the same experiments produce different results.

Now I'm checking the regex baseline results against the JSON data to verify the percentages are converting correctly from decimal form.

Looking at the cross-format comparison table, I can see how the SFT approach outperforms regex across different trace formats, with the biggest gap in the VOTA format where SFT gains over 23 percentage points. Let me verify these delta calculations are accurate.

Now I'm checking the main text against the table values—the paper claims SFT outperforms regex by +3.62 to +23.86 percentage points, but the table shows the maximum delta is +23.50 for VOTA, not +23.86. This discrepancy is what needs to be resolved.

Looking at the VOTA numbers more carefully, the difference comes down to which baseline is used: the 3-seed mean gives 23.50pp, while the seed42 value alone gives 23.86pp, so the main text appears to be citing the single-seed result rather than the averaged one. I'm noticing the appendix text itself has conflicting numbers—it states +23.86pp in the prose but the table shows +23.50pp, likely because one uses seed 42 results while the other averages across three seeds. The main text also references the same inconsistent 23.86 value. Now I'm checking the cross-dataset transfer results to see if there are similar discrepancies there. Looking at the nomarker cross-dataset results, the registry shows 95.5% accuracy which matches the paper's statement about the 3.9 percentage point drop from the baseline of 99.41%. Now I'm checking the appendix table with zero-shot versus SFT performance across different model sizes—Qwen-1.5B shows a 6.38 point improvement, DeepSeek-6.7B gains 8.80 points, and Qwen-7B improves by 10.75 points with fine-tuning.

I'm verifying the CodeLlama-13B results against the registry entries, where I'm seeing some variation in the reported SFT accuracy depending on the seed and configuration used. So if I use three seeds—42, 123, and 456—with values 99.83, 100.00, and 99.83 respectively, the mean works out to 99.89 with a standard deviation of 0.10, which matches the paper exactly. That confirms the CodeLlama exception-only results. Now I'm checking the delta between different model sizes to verify consistency across the benchmarks. Verifying the DebugBench results from the JSON file—exception_only hits 100%, VOTA reaches 99.77%, no_trace comes in at 96.71%, and the majority baseline sits at 51.41%, all matching the table values.

Now checking the cross-model tail-truncation results for Qwen-7B and DeepSeek across different tail lengths, with exception_only performance as the reference point.

Looking at the appendix data for CodeLlama, Qwen-1.5B, and other models with their tail-truncation performance metrics.

I'm noticing a discrepancy—the trace_length table shows Qwen-7B's tail-256 performance at 77.48, but the cross-model table lists it as 78.9. These should be measuring the same experiment, so something doesn't align here. Now I'm checking the other tail values and they mostly align with rounding, but the tail-256 discrepancy of 1.4 percentage points is too large to explain that way. I'm wondering if the cross-model table accidentally used the head-256 value instead of tail-256, since 78.82 rounds to 78.8 which is close to the 78.9 shown.

Actually, looking more carefully at the table metadata, the tail_cross_model table doesn't specify which seed was used, while trace_length explicitly states seed=42. The cross-model table might be averaging across multiple seeds rather than a single run, which would explain the discrepancy.

Now I'm checking the head-vs-tail comparison and tracing back to the original data. For Qwen-7B, the head-2048 value of 81.8 matches the full trace with no limit at 81.76 when rounded. But for Qwen-1.5B, the head-2048 value of 75.3 doesn't align with the full_trace value of 77.06, so I need to reconsider what "head-2048" actually means—it's likely training on full traces but truncated to keep only the first 2048 tokens, which would be different from the standard full_trace setup.

I'm noticing a more serious inconsistency with Qwen-7B tail-256: the trace_length table shows 77.48 (or 77.5 rounded) while the tail_cross_model table shows 78.9, which is a meaningful gap that suggests these might be from different experimental runs or there's a data entry error I need to flag.

Let me verify the exception_only results I can cross-check: Qwen-7B matches at 99.83, DeepSeek matches at 99.33, and I'm checking CodeLlama next.

CodeLlama shows 99.89 in the cross-model table, but the registry has 99.83 for seed 42 — that 99.89 is actually the 3-seed average. The table is mixing single-seed and multi-seed values without clear distinction, which is problematic.

For Qwen-1.5B, the exception_only value of 99.83 matches both the seed 42 result and the 3-seed mean (which happens to be 99.83±0.00).

Now looking at the tail-512 results broken down by seed for Qwen-7B and DeepSeek across three different random seeds, showing individual scores and their means with standard deviations.

Verifying the Qwen-7B calculations: the mean of 93.61, 96.00, and 97.65 gives 95.75, which checks out. For the standard deviation, I'm computing the deviations from the mean and their squared values, then averaging to get variance, which yields a standard deviation around 2.03 — the table shows 2.05, so there's a minor rounding difference. The calculations for the other models are checking out more cleanly—DeepSeek's mean and standard deviation match the paper's reported values, and I'm verifying Qwen-1.5B's numbers as well, though the last calculation got cut off mid-way through the variance computation.

Now I'm looking at a comparison table showing how these models perform differently on head versus tail positions in the context window, with notable gaps between their performance on the first 2048 tokens versus the last 2048 tokens. Now I'm verifying the deduplication statistics across the different datasets—checking that the unique counts and duplicate rates calculate correctly for the exception-only training and test sets, as well as the full raw traces. Now I'm cross-referencing the registry data for Qwen-1.5B's ae_only results—the paper reports 98.83±0.36, but the seed42 run shows 99.08, which suggests another seed must have produced a lower value to bring the mean down to 98.83. seeds are slightly lower. For loop_only, the seed42 result of 78.32% is notably lower than the reported 79.54% mean, suggesting the other seeds performed better. The full_trace result matches perfectly at 77.06%, but no_trace shows a concerning discrepancy—the paper reports 72.35% while seed42 only achieved 67.31%, a gap I need to investigate further.

Checking the raw data... I'm working through the math to verify whether the standard deviation of 4.48 is consistent with seed 42 scoring 67.31 when the mean across three seeds is 72.35. If the other two seeds average around 74.87 each, the variance calculation suggests their individual deviations from the mean would need to be quite small to match the reported standard deviation.

Now I'm spot-checking the CL-13B results against the registry values. The exception_only metric checks out at 99.89, and for VOTA I'm seeing that the mean of 98.74 could come from just two seeds (98.57 and 98.91) rather than three, which might explain why the standard deviation is so tight.

Moving to DS-6.7B, the exception_only also validates correctly at 99.39, but I'm noticing a discrepancy with ae_only—the per-class table shows 98.74 while the cross-model comparison shows 98.53±0.30, which are clearly different values that need reconciling. Looking at the standard deviation calculation, if I have two seed values of 98.74 and another around 98.32 with a mean of 98.53, the sample standard deviation works out to approximately 0.30, which matches what's reported.

Now I'm checking the ablation results from the experiments table. The ae_only configuration shows 99.64 as a 3-seed mean, exception_only reaches 99.83 with a confidence interval, and VOTA achieves 99.05 with its own interval bounds. I also see loop_only at 80.31±1.65, full_trace at 79.16, and no_trace at 73.36 in the results.

Verifying these against the source data: ae_only's three seeds average to 99.64, exception_only confirms at 99.83, VOTA matches at 99.05, and VOTA_no_ae comes in at 99.41. The loop_only, full_trace, and no_trace configurations all align with their reported values.

Now looking at the Tab:density results from experiments.tex, I see exception_only stays at 99.83 with no variance, but adding gradient masking drops it to 99.22 with some variance across seeds. The full_trace baseline is 81.76, and when combined with label-only loss it jumps to 85.94, gaining 4.50 percentage points.

Checking the registry entries for gradient masking across seeds, I have two completed results—seed42 at 98.99% and seed456 at 99.33%—while seed123 is still preparing. If the third seed also came in around 99.33%, that would average to 99.22 with the reported standard deviation, which matches the paper's claim.

Since seed123 shows no completed metrics in the registry despite being listed as a parent experiment, either the run finished but wasn't registered, or the paper's mean is based on different data. I can't fully reconcile this discrepancy with what's available.

Now I'm verifying the reported deltas against the registry values. The gradient masking delta of 0.61 percentage points matches what the paper claims. For the label-only condition, I'm checking the full trace: the baseline is 81.76, label-only reaches 85.94±1.12, giving a delta of 4.50 percentage points, which aligns with the paper's reported value.

Moving to the main text references, I'm cross-checking the experiments.tex file where it mentions the Qwen-7B 3-seed mean for the nomarker condition as 97.65% ± 0.96 with individual seeds at 96.55/98.32/98.07.  The average calculates to 97.647 and the standard deviation to 0.958, both matching the reported figures. The Qwen-1.5B drop of 2.01 percentage points also checks out. Now I'm examining the marker contribution claim that it accounts for roughly 2 percentage points and represents about 9% of the total exception lift over the no_trace baseline of 24.70 percentage points. I'm verifying the cross-dataset results by checking the registry values against what's reported in the paper—the sample sizes N=4,270 and N=1,640 correspond to the exception_only experiments, while the 67.99% and 70.56% no_trace accuracies are for the opposite direction transfers between HumanEval and MBPP. Looking at the marker removal results, the cross-dataset accuracy of 95.5% matches the registry entry, and the 3.9 percentage point drop aligns with the paper's claim. Now I'm checking the VOTA improvements in the regex_cross_format section, where the appendix lists increasing advantages across different trace formats, culminating in a 23.86 percentage point gain for VOTA over the majority baseline. I'm noticing a discrepancy in the VOTA results—the text claims +23.86pp but the table shows +23.50pp, and this same +23.86 figure appears in the experiments.tex file. Now I'm cross-checking the other key claims against their source data: the ECE comparison checks out at 63× the gap, and the calibration results for all four models are indeed under 0.007 as stated. The text at line 576 specifies that CodeLlama-13B has the lowest ECE at 0.0020 while DeepSeek-6.7B shows the highest at 0.0064, which aligns with the calibration cross-validation table. Now checking the exception_only results across all four models and their seeds—Qwen-7B, Qwen-1.5B, DeepSeek-6.7B, and CodeLlama-13B all meet or exceed the 99.33% threshold mentioned in the experiments file. I'm verifying the CL-13B VOTA calculation from the registry entries—taking the mean of the two seed values gives 98.74 with a standard deviation of 0.24, which matches the reported figure. I also confirmed that the CodeLlama-13B accuracy of 99.83% in the calibration table corresponds to seed 42, which aligns with the exception_only results I found earlier. Now I need to check the per-class breakdown for DeepSeek.

Looking at the DeepSeek metrics across different trace configurations: the No Trace variant shows 73.36% accuracy with balanced precision and recall around 81% for passes and 54% for failures, which matches the registry value. The Full Trace version reaches 79.16% accuracy, also confirmed in the registry. The VOTA approach improves to 84.45%, and all three of these check out against the stored values. However, I'm noticing a discrepancy with the Exception Only configuration—the table shows 99.33% accuracy, but the registry entry for that seed shows 0, which doesn't align. For DeepSeek conditions in per_class, the Acc column consistently uses seed 42 values. The real inconsistency shows up in Qwen-7B where the Acc column reports multi-seed means while P/R/F1 pull from seed 42 alone. I'm also noting a discrepancy between the two calibration tables that needs flagging. Let me cross-check the main text against the appendix—the tokenizer analysis section confirms the same 91.7% truncation rate mentioned in experiments.tex, and I'm seeing line 137 reports 99.22% as a mean across three seeds with a −0.61pp deviation from exception_only.

The math checks out: 99.83 minus 99.22 equals 0.61, and when I calculate the gradient dilution ratio against the 18.07pp gap (99.83 − 81.76), I get roughly 3.4%, which aligns with the paper's ≤4% claim within rounding tolerance. Now I'm reviewing the exception type breakdown to complete the full audit.

Generating exception table... The table shows Δ values ranging from +3.62 to +23.50pp, but the main text claims +3.62 to +23.86pp—that discrepancy comes from using the single seed 42 result (99.41%) instead of the 3-seed mean (99.05%) for VOTA. The appendix correctly uses the mean, but this inconsistency exists in both documents. I'm also noticing the per_class table caption says "seed 42" yet reports VOTA's accuracy as 99.05, which is the mean value, not the individual seed result.

Now I'm working through the per-class metrics for VOTA to verify which seed this actually represents. The recall and precision values suggest 7 errors distributed as pass→fail misclassifications, which aligns with the seed 42 accuracy of 99.41%, but the reported accuracy of 99.05% doesn't match that error count.

For loop_only, I'm checking whether the accuracy of 85.63 or 86.05 is correct by working backward from the pass and fail recall rates to determine the actual number of misses in each class. I've confirmed the inconsistency—all three rows pull P/R/F1 values from seed 42 while using the 3-seed mean for accuracy, which needs to be fixed. Now I'm compiling the audit report to document these discrepancies before resubmission.

The main issues are the per_class table accuracy values that don't match their seed 42 captions, the VOTA delta calculations that vary across different sections of the paper, and conflicting ECE values appearing in multiple calibration tables for the same experiments.

There's also a discrepancy in the tail-256 metric for Qwen-7B between two different tables—one shows 77.48 while the other shows 78.9 for what should be identical experimental conditions. I'm also noting some minor rounding inconsistencies in the calibration values that should be verified.

Beyond that, there's an issue with CodeLlama's exc_only entry appearing to use a 3-seed mean while other entries reference seed 42, suggesting inconsistent methodology across the table. And the gradient masking result reports a 3-seed mean with uncertainty, but seed123 isn't actually registered in the system yet—the paper may be reporting a value that wasn't formally logged.

Now I'm systematically going through each table to verify the data integrity. The per_class table has roughly thirty cells of actual data across the model rows, and I'm spot-checking key values against the source.

I've now verified most of the tables: the full model results for both Qwen and DeepSeek check out, the exception type and subcomponent breakdowns are consistent with the registry, trace length metrics match the bootstrap data, the pairwise comparisons are solid, and the seed-based results for tail512 and calibration all align with expectations. The tail_cross_model table is only partially verified so far.

Moving into the calibration and cross-model sections, I found a minor rounding discrepancy in the full trace ECE, and the calibration_model_level values diverge from the calibration_cross table in ways that need investigation. The dedup, regex, and zeroshot cross-model results all check out, though there's a text contradiction in the VOTA Δ section of the regex_cross_format table. Across roughly 250 cells examined, about 240 are consistent with the source data, leaving around 10 cells with issues spanning four different problem areas. Now I'm ready to compile the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "e11e452e-bd85-429c-acba-c7ed1baef081",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrH7MwNgB5JvSAt5nREkiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 75783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
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

Now I have all the data needed for a systematic audit. Let me also verify the key discrepancy items by reading one more calibration data file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "0b4350f8-ea5a-4c16-8226-1143826eafd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrH7MwNgB5JvSAt5nREkiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 75783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
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

<details open><summary>🔧 Tool call — Read · `toolu_016Lh4n7TDQ31a5pyxrbpPah`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_model_calibration/data/cross_model_calibration_results.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "79b49fcc-7169-4795-9d49-01c31b34f80c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrH7MwNgB5JvSAt5nREkiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2755,
      "cache_read_input_tokens": 75783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2755
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

_source line 64 · 2026-05-23T19:26:45.956Z_

<details><summary>↩ Tool result · `toolu_016Lh4n7TDQ31a5pyxrbpPah`</summary>

```text
1	Cross-model Calibration Results (exception_only, n=1190)
2	
3	Model            Accuracy   ECE      MCE      Brier
4	Qwen2.5-7B      0.9983     0.0027   0.8355   0.0013
5	Qwen2.5-1.5B    0.9983     0.0020   0.7549   0.0013
6	CodeLlama-13B   0.9983     0.0020   0.0411   0.0013
7	DeepSeek-6.7B   0.9933     0.0064   0.7756   0.0061
8	
9	Findings:
10	- ECE < 0.007 for all 4 models: calibration quality is universally strong
11	- 3/4 models achieve identical accuracy (99.83%), DeepSeek slightly lower (99.33%)
12	- Brier scores tightly clustered: 0.0013 for 3 models, 0.0061 for DeepSeek
13	- CodeLlama-13B has notably low MCE (0.041), indicating no high-confidence errors
14	- DeepSeek-6.7B weakest but still excellent calibration
15	
16	Source: /root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "31f92d1d-0fb4-410f-9d65-7b83adf7ce96",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/cross_model_calibration/data/cross_model_calibration_results.txt",
      "content": "Cross-model Calibration Results (exception_only, n=1190)\n\nModel            Accuracy   ECE      MCE      Brier\nQwen2.5-7B      0.9983     0.0027   0.8355   0.0013\nQwen2.5-1.5B    0.9983     0.0020   0.7549   0.0013\nCodeLlama-13B   0.9983     0.0020   0.0411   0.0013\nDeepSeek-6.7B   0.9933     0.0064   0.7756   0.0061\n\nFindings:\n- ECE < 0.007 for all 4 models: calibration quality is universally strong\n- 3/4 models achieve identical accuracy (99.83%), DeepSeek slightly lower (99.33%)\n- Brier scores tightly clustered: 0.0013 for 3 models, 0.0061 for DeepSeek\n- CodeLlama-13B has notably low MCE (0.041), indicating no high-confidence errors\n- DeepSeek-6.7B weakest but still excellent calibration\n\nSource: /root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Good. This confirms tab:calibration_cross uses these values (bins 0.5-1.0, 10 bins). The tab:calibration_model_level uses different values (from plan019 run, likely different bin config).

Now let me compile the full audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "cf5c5fa4-91df-429f-b64c-b5c94189a539",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EW3Nc2MueVqcZVnsc6mWA8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26863,
      "cache_read_input_tokens": 78538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26863
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

Audit complete. Here is the full report.

---

## Appendix Tables 5–23 数据审计报告

**核对范围**: 19 个数据表, ~250+ 个数值单元格
**数据源**: registry (36 experiments), table1_final.json, regex_baseline_results.json, debugbench_results.json, cross_model_calibration_results.json/txt, trace_ablation_bootstrap.json, calibration_metrics_summary.txt

---

### ❌ 必须修复 (4 issues)

**Issue 1: tab:per_class — 3 行 Acc 列用了 3-seed mean, P/R/F1 用 seed42**

Caption 标注 "seed 42"，但 VOTA/loop_only/Full Trace (LO) 的 Acc 列是 3-seed mean：

| Row | Acc(论文) | 来源 | Acc(seed42) | P/R/F1验算→Acc |
|-----|----------|------|-------------|---------------|
| VOTA, Qwen-7B | 99.05 | 3-seed mean | 99.41 | Pass R=99.18 → 7 errors → **99.41** |
| loop_only, Qwen-7B | 86.05 | 3-seed mean | 85.63 | Pass R=87.07 + Fail R=82.01 → 171 errors → **85.63** |
| Full Trace (LO), Qwen-7B | 85.94 | 3-seed mean | 86.22 | Pass R=93.18 + Fail R=68.73 → 164 errors → **86.22** |

修复方案：将这 3 行的 Acc 改为 seed42 值 (99.41/85.63/86.22)。

---

**Issue 2: VOTA regex Δ 三处不一致**

| 位置 | 值 | 来源 |
|------|---|------|
| tab:regex_cross_format (appendix table) | Δ=+23.50 | 99.05(3-seed) − 75.55 |
| appendix text (§B.10 inline) | +23.86 | 99.41(seed42) − 75.55 |
| experiments.tex line 105 | "+3.62–23.86pp" | same seed42 calc |

表和正文自相矛盾。修复方案：统一为 +23.50 (与表一致，用 3-seed mean) 或全改为 +6.22 (exception_only) 作为 max Δ 并重述。

---

**Issue 3: 两个 calibration 表 ECE 值不同**

tab:calibration_cross (§B.8) 和 tab:calibration_model_level (§C.1) 报告了同一组实验的不同 ECE：

| Model | tab:calibration_cross ECE | tab:calibration_model_level ECE | 差异 |
|-------|--------------------------|-------------------------------|------|
| Qwen-1.5B | 0.0020 | 0.0014 | −0.0006 |
| Qwen-7B | 0.0027 | 0.0017 | −0.0010 |
| DeepSeek-6.7B | 0.0064 | 0.0048 | −0.0016 |
| CodeLlama-13B | 0.0020 | 0.0020 | 0.0000 |

数据溯源：tab:calibration_cross 来自 cross_model_calibration_results.txt (bins 0.5–1.0)；tab:calibration_model_level 来自 plan019 run (不同 bin 配置)。

修复方案：统一 bin 配置，保留一个表删除另一个，或在 caption 明确标注 bin 差异。

---

**Issue 4: Qwen-7B tail-256 两表数值不一致**

| 表 | 值 |
|----|---|
| tab:trace_length (§B.7) | 77.48 |
| tab:tail_cross_model (§B.7) | 78.9 |

同一实验 (Qwen-7B, seed=42, N=1190) 不应有两个不同数值。78.9 可能误用了 head-256 (78.82→78.8)。

修复方案：核实原始 eval 结果，统一为正确值。

---

### ⚠️ 需确认 (4 items)

| # | 位置 | 问题 | 详情 |
|---|------|------|------|
| 5 | tab:calibration, full_trace ECE | 0.096 vs raw 0.0946 | 0.0946 at 3dp = 0.095, not 0.096 |
| 6 | tab:tail512_seeds, Qwen-7B σ | 2.05 vs computed 2.03 | 微小差异，可能由于显示精度 |
| 7 | tab:tail_cross_model, CL exc_only | 99.89 (3-seed mean) | 其他列均为 seed42，此处混用 |
| 8 | tab:density, grad mask 3-seed | mean=99.22±0.20 | seed123 registry 状态 PREPARING，未见结果 |

---

### ✅ 已验证一致 (全部表)

| Table | 内容 | 核对数 | 结果 |
|-------|------|--------|------|
| tab:full_qwen | Qwen-7B 全条件全 seed | 24 cells | ✅ mean/std 全部正确 |
| tab:full_deepseek | DS-6.7B 全条件全 seed | 16 cells | ✅ |
| tab:exc_subcomponent | 3 子成分 ablation | 12 cells | ✅ registry 完全匹配 |
| tab:trace_length | Head-truncation 4 条件 | 8 cells + CIs | ✅ bootstrap JSON 完全匹配 |
| tab:trace_length_pairwise | 12 对 pairwise bootstrap | 48 cells | ✅ JSON 精确匹配 |
| tab:tail512_seeds | 4 模型 ×3 seed at tail-512 | 20 cells | ✅ (σ 微偏 ⚠️) |
| tab:head_vs_tail | 4 模型 head vs tail | 9 cells | ✅ gaps 精确 |
| tab:calibration | Qwen-7B 5 条件 calibration | 10 cells | ✅ (full_trace ECE ⚠️) |
| tab:calibration_cross | 4 模型 cross-model cal | 12 cells | ✅ 与 raw data 匹配 |
| tab:exception_type | 10 类异常分类准确率 | 20 cells | ✅ 样本总和=1190 |
| tab:dedup | 去重统计 | 9 cells | ✅ 比例精确 |
| tab:regex | 6 regex baselines | 8 cells | ✅ JSON 完全匹配 |
| tab:regex_cross_format | 4 格式 SFT vs regex | 12 cells | ✅ Δ 算术正确 |
| tab:zeroshot_cross_model | 4 模型 zero-shot vs SFT | 16 cells | ✅ 范围/Δ 正确 |
| tab:debugbench | DebugBench 3 条件 | 8 cells | ✅ JSON 完全匹配 |
| tab:hyperparams | 超参数 | config | ✅ (非数据) |
| tab:train_time | 训练时间 | config | ✅ (非数据) |

---

### 主文↔Appendix 引用一致性

| 主文引用 | 值 | Appendix 值 | 状态 |
|----------|---|-------------|------|
| ECE 63× gap (experiments.tex:198) | 0.171/0.0027=63.3 | tab:calibration | ✅ |
| All ECE<0.007 (experiments.tex:199) | ref tab:calibration_model_level | 0.0014–0.0048 | ✅ |
| "+3.62–23.86pp" (experiments.tex:105) | — | tab:regex_cross_format max Δ=23.50 | ❌ |
| nomarker 97.65±0.96 (experiments.tex:120) | — | 无 appendix 表 | ✅ (自洽) |
| Cross-dataset 99.41% N=4270 (experiments.tex:127) | — | 无 appendix 表 | ✅ |
| Tier boundary 12.48pp (experiments.tex:100) | 98.53−86.05 | tab:cross_model | ✅ |

---

### 汇总

| 类别 | 数量 |
|------|------|
| 核对总数 | ~250 cells |
| ✅ 一致 | ~240 |
| ❌ 必须修复 | **4** (per_class 3行 Acc, VOTA Δ 矛盾, 2个 calibration 表, tail-256 矛盾) |
| ⚠️ 需确认 | **4** (rounding/labeling/registry gap) |

4 个 ❌ 都是同类问题：**seed42 vs 3-seed mean 混用**或**不同运行结果未统一**。建议在 DDL 前统一数据源并 one-pass 替换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "uuid": "54f9d26e-fce4-4cfe-be79-888da6de8ba3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EW3Nc2MueVqcZVnsc6mWA8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26863,
      "cache_read_input_tokens": 78538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26863
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

### Task result

_source line 67_

Audit complete. Here is the full report.

---

## Appendix Tables 5–23 数据审计报告

**核对范围**: 19 个数据表, ~250+ 个数值单元格
**数据源**: registry (36 experiments), table1_final.json, regex_baseline_results.json, debugbench_results.json, cross_model_calibration_results.json/txt, trace_ablation_bootstrap.json, calibration_metrics_summary.txt

---

### ❌ 必须修复 (4 issues)

**Issue 1: tab:per_class — 3 行 Acc 列用了 3-seed mean, P/R/F1 用 seed42**

Caption 标注 "seed 42"，但 VOTA/loop_only/Full Trace (LO) 的 Acc 列是 3-seed mean：

| Row | Acc(论文) | 来源 | Acc(seed42) | P/R/F1验算→Acc |
|-----|----------|------|-------------|---------------|
| VOTA, Qwen-7B | 99.05 | 3-seed mean | 99.41 | Pass R=99.18 → 7 errors → **99.41** |
| loop_only, Qwen-7B | 86.05 | 3-seed mean | 85.63 | Pass R=87.07 + Fail R=82.01 → 171 errors → **85.63** |
| Full Trace (LO), Qwen-7B | 85.94 | 3-seed mean | 86.22 | Pass R=93.18 + Fail R=68.73 → 164 errors → **86.22** |

修复方案：将这 3 行的 Acc 改为 seed42 值 (99.41/85.63/86.22)。

---

**Issue 2: VOTA regex Δ 三处不一致**

| 位置 | 值 | 来源 |
|------|---|------|
| tab:regex_cross_format (appendix table) | Δ=+23.50 | 99.05(3-seed) − 75.55 |
| appendix text (§B.10 inline) | +23.86 | 99.41(seed42) − 75.55 |
| experiments.tex line 105 | "+3.62–23.86pp" | same seed42 calc |

表和正文自相矛盾。修复方案：统一为 +23.50 (与表一致，用 3-seed mean) 或全改为 +6.22 (exception_only) 作为 max Δ 并重述。

---

**Issue 3: 两个 calibration 表 ECE 值不同**

tab:calibration_cross (§B.8) 和 tab:calibration_model_level (§C.1) 报告了同一组实验的不同 ECE：

| Model | tab:calibration_cross ECE | tab:calibration_model_level ECE | 差异 |
|-------|--------------------------|-------------------------------|------|
| Qwen-1.5B | 0.0020 | 0.0014 | −0.0006 |
| Qwen-7B | 0.0027 | 0.0017 | −0.0010 |
| DeepSeek-6.7B | 0.0064 | 0.0048 | −0.0016 |
| CodeLlama-13B | 0.0020 | 0.0020 | 0.0000 |

数据溯源：tab:calibration_cross 来自 cross_model_calibration_results.txt (bins 0.5–1.0)；tab:calibration_model_level 来自 plan019 run (不同 bin 配置)。

修复方案：统一 bin 配置，保留一个表删除另一个，或在 caption 明确标注 bin 差异。

---

**Issue 4: Qwen-7B tail-256 两表数值不一致**

| 表 | 值 |
|----|---|
| tab:trace_length (§B.7) | 77.48 |
| tab:tail_cross_model (§B.7) | 78.9 |

同一实验 (Qwen-7B, seed=42, N=1190) 不应有两个不同数值。78.9 可能误用了 head-256 (78.82→78.8)。

修复方案：核实原始 eval 结果，统一为正确值。

---

### ⚠️ 需确认 (4 items)

| # | 位置 | 问题 | 详情 |
|---|------|------|------|
| 5 | tab:calibration, full_trace ECE | 0.096 vs raw 0.0946 | 0.0946 at 3dp = 0.095, not 0.096 |
| 6 | tab:tail512_seeds, Qwen-7B σ | 2.05 vs computed 2.03 | 微小差异，可能由于显示精度 |
| 7 | tab:tail_cross_model, CL exc_only | 99.89 (3-seed mean) | 其他列均为 seed42，此处混用 |
| 8 | tab:density, grad mask 3-seed | mean=99.22±0.20 | seed123 registry 状态 PREPARING，未见结果 |

---

### ✅ 已验证一致 (全部表)

| Table | 内容 | 核对数 | 结果 |
|-------|------|--------|------|
| tab:full_qwen | Qwen-7B 全条件全 seed | 24 cells | ✅ mean/std 全部正确 |
| tab:full_deepseek | DS-6.7B 全条件全 seed | 16 cells | ✅ |
| tab:exc_subcomponent | 3 子成分 ablation | 12 cells | ✅ registry 完全匹配 |
| tab:trace_length | Head-truncation 4 条件 | 8 cells + CIs | ✅ bootstrap JSON 完全匹配 |
| tab:trace_length_pairwise | 12 对 pairwise bootstrap | 48 cells | ✅ JSON 精确匹配 |
| tab:tail512_seeds | 4 模型 ×3 seed at tail-512 | 20 cells | ✅ (σ 微偏 ⚠️) |
| tab:head_vs_tail | 4 模型 head vs tail | 9 cells | ✅ gaps 精确 |
| tab:calibration | Qwen-7B 5 条件 calibration | 10 cells | ✅ (full_trace ECE ⚠️) |
| tab:calibration_cross | 4 模型 cross-model cal | 12 cells | ✅ 与 raw data 匹配 |
| tab:exception_type | 10 类异常分类准确率 | 20 cells | ✅ 样本总和=1190 |
| tab:dedup | 去重统计 | 9 cells | ✅ 比例精确 |
| tab:regex | 6 regex baselines | 8 cells | ✅ JSON 完全匹配 |
| tab:regex_cross_format | 4 格式 SFT vs regex | 12 cells | ✅ Δ 算术正确 |
| tab:zeroshot_cross_model | 4 模型 zero-shot vs SFT | 16 cells | ✅ 范围/Δ 正确 |
| tab:debugbench | DebugBench 3 条件 | 8 cells | ✅ JSON 完全匹配 |
| tab:hyperparams | 超参数 | config | ✅ (非数据) |
| tab:train_time | 训练时间 | config | ✅ (非数据) |

---

### 主文↔Appendix 引用一致性

| 主文引用 | 值 | Appendix 值 | 状态 |
|----------|---|-------------|------|
| ECE 63× gap (experiments.tex:198) | 0.171/0.0027=63.3 | tab:calibration | ✅ |
| All ECE<0.007 (experiments.tex:199) | ref tab:calibration_model_level | 0.0014–0.0048 | ✅ |
| "+3.62–23.86pp" (experiments.tex:105) | — | tab:regex_cross_format max Δ=23.50 | ❌ |
| nomarker 97.65±0.96 (experiments.tex:120) | — | 无 appendix 表 | ✅ (自洽) |
| Cross-dataset 99.41% N=4270 (experiments.tex:127) | — | 无 appendix 表 | ✅ |
| Tier boundary 12.48pp (experiments.tex:100) | 98.53−86.05 | tab:cross_model | ✅ |

---

### 汇总

| 类别 | 数量 |
|------|------|
| 核对总数 | ~250 cells |
| ✅ 一致 | ~240 |
| ❌ 必须修复 | **4** (per_class 3行 Acc, VOTA Δ 矛盾, 2个 calibration 表, tail-256 矛盾) |
| ⚠️ 需确认 | **4** (rounding/labeling/registry gap) |

4 个 ❌ 都是同类问题：**seed42 vs 3-seed mean 混用**或**不同运行结果未统一**。建议在 DDL 前统一数据源并 one-pass 替换。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 631296,
  "duration_api_ms": 632170,
  "num_turns": 25,
  "stop_reason": "end_turn",
  "session_id": "29d985fc-f7fe-4799-9753-e6edaca757d8",
  "total_cost_usd": 1.677194,
  "usage": {
    "input_tokens": 6955,
    "cache_creation_input_tokens": 93560,
    "cache_read_input_tokens": 449296,
    "output_tokens": 33255,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 93560,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2730,
        "cache_read_input_tokens": 78538,
        "cache_creation_input_tokens": 26863,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 26863
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1546,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0016460000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6955,
      "outputTokens": 33255,
      "cacheReadInputTokens": 449296,
      "cacheCreationInputTokens": 93560,
      "webSearchRequests": 0,
      "costUSD": 1.675548,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "839cadd4-fc5d-42fa-9f15-39edd61382a2"
}
```

</details>

---
